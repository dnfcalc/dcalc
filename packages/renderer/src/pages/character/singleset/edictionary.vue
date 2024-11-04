<script lang="tsx">
import type { PropType } from "vue"
import { computed, defineComponent, reactive, ref, renderList, watch } from "vue"
import { syncRef, useVModel } from "@vueuse/core"
import List from "../customize/list.vue"
import StoneList from "../stone/list.vue"
import MergeList from "../merge/list.vue"
import AsrahanList from "../asrahan/list.vue"
import FeaturesVue from "../specificity/index.vue"
import TriggerVue from "../equipment/trigger.vue"
import RecommendsVue from "./recommends.vue"
import FavoritesVue from "./favorites.vue"
import { useBasicInfoStore, useCharacterStore, useConfigStore, useGlobalStore } from "@/store"
import type { IEquipmentInfo } from "@/api/info/type"
import type { TreeNode } from "@/components/calc/tree/types"
import featureList from "@/utils/featureList"
import EquipList from "@/components/internal/equip/equip-list.vue"

import EquipIcon from "@/components/internal/equip/eq-icon.vue"

import EquipInfo from "@/components/internal/equip/eq-info.vue"
import { rarityClass } from "@/utils"
import api from "@/api"

  type FilterFunction = (e: IEquipmentInfo) => boolean

export default defineComponent({
  name: "EDictionary",
  props: {
    choosePart: {
      type: String,
      default: "-1"
    },
    selectEquip: {
      type: Object as PropType<Num | undefined>
    },
    simple: {
      type: Boolean,
      default: false
    },
    cusCalc: {
      type: Boolean,
      default: true
    }
  },
  async setup(props, ctx) {
    const configStore = useConfigStore()
    const basicStore = useBasicInfoStore()
    const characterStore = useCharacterStore()

    const choose_part = useVModel(props, "choosePart", ctx.emit, { passive: true })

    const selectEquip = useVModel(props, "selectEquip", ctx.emit, { passive: true })

    const armor_types = ["布甲", "皮甲", "轻甲", "重甲", "板甲"]
    const armor_parts = ["上衣", "头肩", "下装", "鞋", "腰带"]

    const jewel_parts = ["项链", "戒指", "手镯"]

    const special_parts = ["辅助装备", "魔法石", "耳环"]

    const else_parts = ["称号", "宠物"]

    const filter = ref<FilterFunction | null>(() => true)

    const filterMode = ref(characterStore.is_delear && props.simple)
    // const filterMode = ref(characterStore.is_delear)
    const rarity = ref("")

    const showMerge = ref(true)

    const items = computed<TreeNode[]>(() => {
      return [
        {
          label: "全部类别",
          value: "-1",
          onSelect() {
            filter.value = null
          }
        },
        {
          label: "武器",
          value: "武器",
          onSelect() {
            filter.value = e => e.part == "武器"
            choose_part.value = "武器"
          },
          children: characterStore.weapon_types.map(r => {
            return {
              label: r,
              value: r,
              onSelect() {
                filter.value = e => e.type == r && e.part == "武器"
                choose_part.value = "武器"
              }
            }
          })
        },
        {
          label: "防具",
          value: "防具",
          onSelect() {
            filter.value = e => armor_parts.includes(e.part)
          },
          children: armor_parts.map(part => {
            return {
              label: part,
              value: part,
              onSelect() {
                filter.value = e => e.part == part
                choose_part.value = part
              },
              children: armor_types.map(t => {
                return {
                  label: t,
                  value: `${part}_${t}`,
                  onSelect() {
                    filter.value = e => e.type == t && e.part == part
                    choose_part.value = part
                  }
                }
              })
            }
          })
        },
        {
          label: "首饰",
          value: "首饰",
          onSelect() {
            filter.value = e => jewel_parts.includes(e.part)
          },
          children: jewel_parts.map(part => {
            return {
              label: part,
              value: part,
              onSelect() {
                filter.value = e => e.part == part
                choose_part.value = part
              }
            }
          })
        },
        {
          label: "特殊装备",
          value: "特殊装备",
          onSelect() {
            filter.value = e => special_parts.includes(e.part)
          },
          children: special_parts.map(part => {
            return {
              label: part,
              value: part,
              onSelect() {
                filter.value = e => e.part == part
                choose_part.value = part
              }
            }
          })
        },
        {
          label: "其它",
          value: "其它",
          onSelect() {
            filter.value = e => special_parts.includes(e.part)
          },
          children: else_parts.map(part => {
            return {
              label: part,
              value: part,
              onSelect() {
                filter.value = e => e.part == part
                choose_part.value = part
              }
            }
          })
        }
      ]
    })

    const choose_feature = ref<ID[]>([])

    const pagination = reactive({
      page: 1,
      pageSize: 15
    })

    const keyword = reactive({
      value: "",
      cache: ""
    })

    const show_name = ref(false)
    const only_read = ref(false)
    const globalStore = useGlobalStore()

    const equips = computed(() => {
      let list = basicStore.equipment_list.filter(item => Number.parseInt(item.id?.toString() ?? "0") < 100000) ?? []
      list = [...(basicStore.equipment_info?.fusion ?? []), ...list]
      let props: any[] = []
      Object.keys(basicStore.entry_list ?? {}).forEach(index => {
        if ((basicStore.entry_list?.[index]?.props.join(";").indexOf(keyword.value.trim()) ?? -1) >= 0) {
          props.push(index)
        }
      })
      props = props.map(Number)
      list = list.filter(r => {
        const feats = choose_feature.value.filter(r => !!r)
        return ((r.name.includes(keyword.value.trim()) || r.suit.join(",").includes(keyword.value.trim())) && (feats.length == 0 || feats.every(f => r.features?.includes(f)))) || [...r.alternative, ...r.growth, ...r.stable].map(Number).filter(item => props.includes(item))?.length > 0
      })
      if (!!filter.value && filter.value instanceof Function) {
        list = list.filter(filter.value)
      }
      if (rarity.value) {
        list = list.filter(r => r.rarity == rarity.value)
      }
      if (props.simple) {
        list.sort((a, b) => {
          return b.alternative.length - a.alternative.length
        })
      }
      // list.sort((a, b) => {
      //   // if (configStore.single_set.includes(a.id)) return -1
      //   // if (configStore.single_set.includes(b.id)) return 1
      //   return b.alternative.length - a.alternative.length
      // })
      if (filterMode.value) {
        if (Object.keys(basicStore.use_count ?? {}).length == 0) {
          return list
        }
        list = list.filter(a => Object.keys(basicStore.use_count ?? {}).includes(a.id?.toString() ?? "") || a.part == "宠物" || a.part == "称号" || a.rarity == "传说")
        list.sort((a, b) => {
          return (basicStore.use_count?.[b?.id?.toString() ?? ""]?.count ?? 0) - (basicStore.use_count?.[a?.id?.toString() ?? ""]?.count ?? 0)
        })
        // list.filter(a=>a.id in )
      }
      return list
    })

    const show_list = computed(() => {
      const start = (pagination.page - 1) * pagination.pageSize
      const end = start + pagination.pageSize
      return equips.value.slice(start, end)
    })

    const choose_item = ref("-1")
    const cuscomVisible = ref(false)

    function reset() {
      choose_feature.value = []
      keyword.cache = ""
      keyword.value = ""
      choose_item.value = "-1"
      choose_part.value = "-1"
      pagination.page = 1
    }

    syncRef(choose_item, choose_part, { direction: "rtl" })

    function chooseEqu(equ: IEquipmentInfo, toggle = false) {
      return (event: Event) => {
        event.preventDefault()
        selectEquip.value = equ.id
        if (!only_read.value) {
          if (equ.type?.includes("融合")) {
            const id = equ.id as number
            const list = basicStore.equipment_info?.fusion ?? []
            if (configStore.fusion_list.includes(id)) {
              configStore.fusion_list.splice(configStore.fusion_list.indexOf(id), 1)
            } else {
              // 移除同部位
              const cur_position = list.filter(a => a.id == id)?.[0].part
              const to_remove = list.filter(item => item.part == cur_position) ?? []
              to_remove.forEach(a => {
                if (configStore.fusion_list.includes(a.id as number)) {
                  configStore.fusion_list.splice(configStore.fusion_list.indexOf(a.id as number), 1)
                }
              })
              configStore.fusion_list.push(id)
            }
          } else {
            configStore.addSingle(equ.id, toggle)
          }
        }
      }
    }

    function isChoose(equ: IEquipmentInfo) {
      return configStore.single_set.includes(equ.id) || configStore.fusion_list.includes(equ.id)
    }

    const total = computed(() => equips.value.length)
    const total_page = computed(() => Math.ceil(total.value / pagination.pageSize))

    watch(total_page, () => {
      pagination.page = 1
    })

    syncRef(
      computed(() => {
        return equips.value.filter(a => configStore.single_set.includes(a.id) && !a.type?.includes("融合"))?.[0]?.id ?? show_list.value[0]?.id
      }),
      selectEquip,
      { direction: "ltr" }
    )

    function labelTag(value: number) {
      const feat = featureList.find(e => e.value == value)
      if (!feat) {
        return <span></span>
      }

      function removeFeature() {
        const index = choose_feature.value.indexOf(value)
        if (index > -1) {
          choose_feature.value.splice(index, 1)
        }
      }
      return (
        <span class="cursor-pointer h-4 mt-1 mr-2 leading-4 inline-block calc-tag" onClick={removeFeature}>
            #{feat.label}
        </span>
      )
    }

    function search() {
      keyword.value = keyword.cache
      pagination.page = 1
    }

    const cur_equ = computed(() => {
      let list = basicStore.equipment_list.filter(item => Number.parseInt(item.id?.toString() ?? "0") < 100000) ?? []
      list = [...(basicStore.equipment_info?.fusion ?? []), ...list]
      return list.filter(a => a.id?.toString() == selectEquip.value?.toString())[0] ?? list[0]
    })

    const show_count = computed(() => {
      const parts = Array.from(new Set(equips.value.map(a => a.part)))
      let count = 0
      parts.forEach(part => {
        let temp = 0
        temp
            // 固定装备
            = Math.ceil((equips.value.filter(a => a.part == part && a.alternative.length == 0 && !a.type?.includes("融合"))?.length ?? 0) / 6)
            // 自定义装备
            + Math.ceil((equips.value.filter(a => a.part == part && a.alternative.length > 0 && !a.type?.includes("融合"))?.length ?? 0) / 6)
            // 融合装备
            + Math.ceil((equips.value.filter(a => a.part == part && a.type?.includes("融合"))?.length ?? 0) / 6)
            + 1
        count += temp
      })
      return count * 6
    })

    function equipInfo() {
      const alternative = (([...basicStore.equipment_list, ...(basicStore.equipment_info?.fusion ?? [])]).filter(a => a.id == selectEquip.value)?.[0]?.alternative ?? []).length > 0
      return (
        <div class="h-full bg-hex-0d0d0d w-52% s-left overflow-y-auto cus">
          <div class={"flex flex-col p-10px pb-0"}>
            <div class="flex h-30px">
              <EquipIcon eq={cur_equ.value}></EquipIcon>
              <div class="flex flex-col ml-8px w-100%">
                <div class={["text-xs flex items-center justify-between", rarityClass(cur_equ.value?.rarity ?? "")]} style="white-space: nowrap;text-overflow: ellipsis;">
                  {cur_equ.value?.name}

                  {props.simple && cur_equ.value.alternative.length > 0 && <calc-button onClick={() => (cuscomVisible.value = true)} title="对比自定义设置" icon="plus"></calc-button>}
                </div>

                <div class="flex items-center justify-between">
                  {cur_equ.value?.part == "武器" ? (
                    <div class="flex items-center justify-end">
                      <div class={`text-hex-${showMerge.value ? "5b5b5b" : "e9c558"}`}>信息</div>
                      <calc-checkbox round v-model={showMerge.value}></calc-checkbox>
                      {cur_equ.value?.lv == 105 ? (<div class={`text-hex-${!showMerge.value ? "5b5b5b" : "e9c558"}`}>融合</div>) : <div class={`text-hex-${!showMerge.value ? "5b5b5b" : "e9c558"}`}>雾神</div>}
                    </div>
                  ) : (
                    <>
                      <div class="text-hex-8ED531">
                        {cur_equ.value.suit.length > 0 && renderList([cur_equ.value.suit[0]], suit => (`${suit} `))}
                      </div>
                    </>
                  )}
                  <div class="text-xs text-right text-hex-8a6f36">{`${cur_equ.value?.part}`}</div>
                </div>
              </div>
            </div>
            {(alternative || cur_equ.value?.type == "融合石") && <div style="border-bottom:1px solid #303030;margin:6px 0;"></div>}
          </div>


          {cur_equ.value?.part == "武器" && showMerge.value ? (
            cur_equ.value?.lv == 105 ? (<MergeList class="py-5px" calc={false} eid={selectEquip.value} />) : (<AsrahanList eid={selectEquip.value}></AsrahanList>)
          ) : alternative ? (
            cur_equ.value?.type == "融合石" ? (<StoneList eid={selectEquip.value?.toString() ?? "0"} />) : (<List calc={props.cusCalc} eid={selectEquip.value?.toString() ?? "0"} />)
          ) : (
            cur_equ.value?.type == "融合石" ?  (<StoneList eid={selectEquip.value?.toString() ?? "0"} />) : <EquipInfo showSuits={true} class="!pt-0" withHead={false} eid={selectEquip.value} isShow={false} />
          )}
        </div>
      )
    }

    const recommendVisible = ref(false)
    const favoritesVisible = ref(false)
    const featureVisible = ref(false)
    const triggerVisible = ref(false)
    const drugVisible = ref(false)

    async function showRecommend() {
      recommendVisible.value = true
    }

    async function showFeature() {
      featureVisible.value = true
    }

    async function showTrigger() {
      triggerVisible.value = true
    }

    async function showDrug() {
      drugVisible.value = true
    }

    async function showFavorites() {
      favoritesVisible.value = true
    }

    const equ_version = computed({
      get() {
        return globalStore.global_set_details[1] != globalStore.global_set_info[1].items[0].value
      },
      set(val) {
        globalStore.global_set_details[1] = !val ? globalStore.global_set_info[1].items[0].value : globalStore.global_set_info[1].items[1].value
        if (window.pywebview) {
          api.saveGlobalSet(globalStore.global_set_details as [number, number[]]).then(_r => characterStore.reload())
        } else {
          localStorage.setItem("dcalc/global", JSON.stringify(globalStore.global_set_details))
          characterStore.reload()
        }
      }
    })

    const selected_consumable = computed({
      get() {
        return configStore.consumable_list
      },
      set(val: number[]) {
        configStore.consumable_list = val
      }
    })

    const consumable = computed(() => basicStore.equipment_info?.consumable ?? [])

    return () => (
      <>
        <div class="flex singleset">
          {!props.simple ? (
            <>
              <calc-dialog lazy header="流派推荐(玩家上传)" v-model:visible={recommendVisible.value}>
                <RecommendsVue></RecommendsVue>
              </calc-dialog>
              <calc-dialog lazy header="收藏的装备搭配" v-model:visible={favoritesVisible.value}>
                <FavoritesVue></FavoritesVue>
              </calc-dialog>
              <calc-dialog lazy header="特性系统" v-model:visible={featureVisible.value} cache={false}>
                <FeaturesVue simple></FeaturesVue>
              </calc-dialog>
              <calc-dialog lazy header="装备条件" v-model:visible={triggerVisible.value}>
                <TriggerVue ></TriggerVue>
              </calc-dialog>
              <calc-dialog lazy class="bg-hex-000" header="药剂设置" v-model:visible={drugVisible.value}>
                <div class="w-270px flex items-center justify-center">
                  <EquipList class="equ-else-sort" list={consumable.value} v-model:selected={selected_consumable.value} showTips={false} withTitle={false} title="药剂" />
                </div>

              </calc-dialog>
            </>
          ) : (
            <calc-dialog lazy header="对比自定义设置" v-model:visible={cuscomVisible.value}>
              <div class="w-100 h-120 overflow-y-auto bg-hex-000000 p-10px">
                <div class="flex flex-col p-10px">
                  <div class="flex h-30px">
                    <EquipIcon eq={cur_equ.value}></EquipIcon>
                    <div class="flex flex-col ml-8px w-100%">
                      <div class={["text-xs flex items-center justify-between", rarityClass(cur_equ.value?.rarity ?? "")]}>{cur_equ.value?.name} - 对照</div>
                      <div class="text-xs text-right text-hex-8a6f36">{`${cur_equ.value?.part}`}</div>
                    </div>
                  </div>
                  <div style="border-bottom:1px solid #303030;margin:8px 0;"></div>
                </div>
                <List eid={(100000 + ((selectEquip.value as number) ?? 0))?.toString()} />
              </div>
            </calc-dialog>
          )}

          <div class="flex flex-col mb-0">
            {/* class={`w-${props.simple ? 113 : 125}` */}
            <div class="w-125">
              <div class=" w-full">
                <div class="w-full pb-1.5">
                  <div class="bg-hex-000000/45 py-2 px-2 justify-between items-center">
                    <div class="flex space-x-2 mb-2 items-center ">
                      <calc-cascader class="!h-5 !max-w-10 flex-1 " v-model={choose_item.value} items={items.value} placeholder="请输入名称搜索"></calc-cascader>
                      {false && !props.simple && (
                        <>
                          {" "}
                          <calc-select class="!h-5 !max-w-10" v-show={characterStore.is_delear} v-model={rarity.value} placeholder="品质">
                            <calc-option value={""}>全部</calc-option>
                            {/* <calc-option value="智慧产物">智慧产物</calc-option> */}
                            <calc-option value="史诗">史诗</calc-option>
                            {/* <calc-option value="神话">神话</calc-option> */}
                            <calc-option value="传说">传说</calc-option>
                            <calc-option value="稀有">稀有</calc-option>
                          </calc-select>
                        </>
                      )}
                      <calc-checkbox round v-model={filterMode.value}>
                          过滤
                      </calc-checkbox>
                      <calc-checkbox round v-model={show_name.value}>
                          名称
                      </calc-checkbox>
                      {!props.simple && (
                        <calc-checkbox round v-model={only_read.value}>
                            字典
                        </calc-checkbox>
                      )}

                      <calc-autocomplete onEnter={search} placeholder="请输入关键字搜索" class="flex-1 !h-5" v-model={keyword.cache}></calc-autocomplete>
                      <calc-button onClick={search} title="搜索" class="ml-2" icon="search"></calc-button>
                      <calc-button onClick={reset} title="重置" class="ml-4" icon="reset"></calc-button>
                    </div>
                    {!props.simple && (
                      <div class="flex justify-between">
                        <calc-select
                          input-class="calc-tags-input"
                          label={labelTag}
                          multiple
                          multiple-limit={5}
                          class="!w-50% !h-5"
                          v-model={choose_feature.value}
                          emptyLabel="请选择#标签"
                        >
                          {renderList(featureList, item => (
                            <calc-option value={item.value}></calc-option>
                          ))}
                        </calc-select>
                        {globalStore.global_set_info?.[1].items.length > 1 && (
                          <div class="flex items-center justify-center ml-5px">
                            <div class={`text-hex-${equ_version.value ? "5b5b5b" : "e9c558"}`}>国服</div>
                            <calc-checkbox round v-model={equ_version.value}></calc-checkbox>
                            <div class={`text-hex-${!equ_version.value ? "5b5b5b" : "e9c558"}`}>前瞻</div>
                          </div>
                        )}

                        <calc-button onClick={showDrug} icon="menu-drug" title="药剂" small>
                        </calc-button>

                        <calc-button title="特性系统" icon="menu-specificity" onClick={showFeature} small >
                        </calc-button>

                        <calc-button title="装备触发条件" onClick={showTrigger} icon="menu-set" small>
                        </calc-button>

                        {/* <calc-button small class="ml-2" onClick={clearFeature}>
                            清空
                        </calc-button> */}
                        <calc-button title="收藏" onClick={showFavorites} icon="menu-favourite" small >

                        </calc-button>
                        <calc-button title="流派推荐" onClick={showRecommend} icon="menu-recommend" small>

                        </calc-button>
                      </div>
                    )}
                  </div>
                </div>
                {/* <div class={`flex h-${props.simple ? 142.5 : 142}  w-full`}> */}
                <div class={"flex h-150 w-full"}>
                  {show_name.value ? (
                    <div class="h-full bg-hex-0d0d0d mx-2px w-48%">
                      <calc-selection v-model={selectEquip.value} active-class="equip-line-selected" class="h-[calc(100%-2.5rem)]">
                        {renderList(show_list.value, item => {
                          return (
                            <calc-item title="右键点击穿戴" onContextmenu={chooseEqu(item)} value={item?.id} class="flex h-9 mb-2px px-1 justify-between items-center equip-line relative box-border">
                              <div class="h-full w-full top-0 left-0 absolute mask"></div>
                              <EquipIcon onClick={chooseEqu(item, true)} eq={item}></EquipIcon>
                              <span class={["text-xs", "ml-4", rarityClass(item?.rarity ?? "")]}>{item?.name}</span>
                              {/* <span class={["h-4 w-6"].concat( ? "icon-checked" : "")}></span> */}
                              <calc-checkbox modelValue={isChoose(item)} style="z-index:999" class="h-4 w-6" onClick={chooseEqu(item, true)}></calc-checkbox>
                            </calc-item>
                          )
                        })}
                        {renderList(pagination.pageSize - show_list.value.length, () => (
                          <div class="flex h-9 mb-2px px-1 justify-between items-center equip-line relative box-border"></div>
                        ))}
                      </calc-selection>
                      <calc-pagination disabled={recommendVisible.value} v-model:page={pagination.page} total-page={total_page.value} v-show={total_page.value > 0}></calc-pagination>
                    </div>
                  ) : (
                    <>
                      <div class="h-full bg-hex-0d0d0d mx-2px w-48% overflow-y-auto max-h-150" style="position:relative">
                        <div style="position:absolute" class="flex flex-wrap pl-6px">
                          {renderList(show_count.value, () => {
                            return (
                              <div class="eq-icon w-30px h-30px ml-6px mt-3px">
                                <div class="w-28px h-28px" style="border:1px solid rgba(122, 122, 122, 0.5)"></div>
                              </div>
                            )
                          })}
                        </div>
                        {renderList(Array.from(new Set(equips.value.map(a => a.part))), part => {
                          return (
                            <>
                              <div class="flex flex-wrap pl-6px">
                                {renderList(
                                  equips.value.filter(a => a.part == part && a.alternative.length <= 0 && !a.type?.includes("融合") && !a.name.includes("焚烬龙焰")),
                                  item => {
                                    return (
                                      <EquipIcon
                                        class="ml-6px mt-3px"
                                        active={configStore.single_set.includes(item.id) || configStore.fusion_list.includes(item.id)}
                                        onClick={chooseEqu(item, true)}
                                        eq={item}
                                      ></EquipIcon>
                                    )
                                  }
                                )}
                              </div>
                              <div class="flex flex-wrap pl-6px">
                                {renderList(
                                  equips.value.filter(a => a.part == part && a.alternative.length > 0 && !a.type?.includes("融合")),
                                  item => {
                                    return (
                                      <EquipIcon
                                        class="ml-6px mt-3px"
                                        active={configStore.single_set.includes(item.id) || configStore.fusion_list.includes(item.id)}
                                        onClick={chooseEqu(item, true)}
                                        eq={item}
                                      ></EquipIcon>
                                    )
                                  }
                                )}
                              </div>
                              <div class="flex flex-wrap pl-6px  mb-33px">
                                {renderList(
                                  equips.value.filter(a => a.part == part && a.type?.includes("融合")),
                                  item => {
                                    return (
                                      <EquipIcon
                                        class="ml-6px mt-3px"
                                        active={configStore.single_set.includes(item.id) || configStore.fusion_list.includes(item.id)}
                                        onClick={chooseEqu(item, true)}
                                        eq={item}
                                      ></EquipIcon>
                                    )
                                  }
                                )}
                              </div>
                            </>
                          )
                        })}
                      </div>
                    </>
                  )}
                  {equipInfo()}
                </div>
              </div>
            </div>
          </div>
        </div>
      </>
    )
  }
})
</script>

<style lang="scss">
.equip-line {
  border: 1px solid transparent;
  background-image: url("@/assets/img/control/dictionary_line.png");
  background-repeat: no-repeat;
  background-size: 100% 100%;

  &:hover {
    .mask {
      background-image: url("@/assets/img/control/hover_mask.png");
      background-repeat: no-repeat;
      background-size: 100% 100%;
    }
  }

  &-selected {
    border: 1px solid #ffb400;
  }
}

.icon-checked {
  background-image: url("@/assets/img/control/item_checked.png");
  background-size: 100% 100%;
  background-repeat: no-repeat;
  background-position: center;
}

.equ {
  display: flex;
  flex-wrap: wrap;
  padding: 5px;
  background-color: rgba(0, 0, 0, 0.45);

  .equ-item {
    width: 30px;
    height: 30px;
    background-color: rgba(0, 0, 0, 0.5);
    border: 1px solid #1a1a1a;
    margin-right: 4px;
    margin-bottom: 4px;
  }
}

.s-left {
  .approved-form {
    width: calc(100% - 23px);
  }
}

.calc-tags-input {
  .calc-tag {
    text-decoration: underline;
    text-underline-offset: 2px;
    color: #ffb400 !important;

    &:hover {
      color: #fff000 !important;
    }
  }
}
</style>
