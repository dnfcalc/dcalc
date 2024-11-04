<script lang="tsx">
import { debouncedWatch, useAsyncState } from "@vueuse/core"
import { computed, defineComponent, h, onUnmounted, ref, renderList, watch } from "vue"
import Dictionary from "../singleset/edictionary.vue"
import Profile from "@/components/internal/profile/index.vue"
import { useAppStore, useBasicInfoStore, useCharacterStore, useConfigStore, useDetailsStore, useGlobalStore } from "@/store"
import EquipList from "@/components/internal/equip/equip-list.vue"

import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"

import { useOpenWindow } from "@/hooks/open"
import { rarityClass, toObj } from "@/utils"

import { useDialog } from "@/components/hooks/dialog"
import Watermark from "@/components/watermark/index.vue"

export default defineComponent({
  async setup() {
    const configStore = useConfigStore()
    const basicStore = useBasicInfoStore()
    const detailsStore = useDetailsStore()
    const characterStore = useCharacterStore()
    const globalStore = useGlobalStore()

    // const filterMode = ref(characterStore.is_delear)

    const choose_part = ref("-1")
    const compare_list = ref<number[]>([])
    const cur_id = ref(0)

    const selectEquip = ref<ID>()

    const result = useAsyncState(
      () => {
        const comparisonList = {}
        const curEqus = basicStore.equipment_list.find(a => configStore.single_set.includes(a.id) && a.part == choose_part.value)
        if ((curEqus?.alternative ?? []).length > 0 && (configStore.customize[(Number.parseInt(curEqus?.id?.toString() ?? "0") + 100000)?.toString() ?? ""]?.filter(a => a != 0)?.length ?? 0) == 4) {
          compare_list.value.push(Number.parseInt(curEqus?.id?.toString() ?? "0") + 100000)
        }
        if (compare_list.value.length > 0) {
          let index = -1
          index = configStore.single_set.findIndex(a => basicStore.equipment_list.filter(b => b.part == choose_part.value && b.id == a)?.length > 0)
          compare_list.value.forEach(a => {
            const temp = [...configStore.single_set]
            temp[index] = a
            comparisonList[a.toString()] = temp
          })
        }
        return configStore.calc(true, false, 0, 0, comparisonList, cur_id.value)
      },
      {
        id: undefined,
        equips: [],
        role: "delear",
        name: "",
        alter: "",
        skills: {},
        total_data: [0],
        info: undefined,
        skills_passive: undefined,
        jade: undefined,
        equips_forge: {},
        customize: {},
        fusion_list: [],
        tip_part: [],
        merge_list: {},
        analysis: {
          min: 0,
          cus: []
        }
      },
      { resetOnExecute: false }
    )

    const min_cus = computed(() => result.state.value.analysis?.min ?? 0)

    const analysis_cus = computed(() => result.state.value.analysis?.cus.filter(a => a[1] >= result.state.value.total_data[0]) ?? [])

    const { state: combinations } = useAsyncState(
      () => {
        const res = configStore.getCombinations(characterStore.alter)
        return res
      },
      [],
      {
        resetOnExecute: false,
        immediate: true,
        onError: Promise.reject
      }
    )

    const stopWatch = watch(
      () => characterStore.calc_token,
      () => {
        result.execute()
      }
    )

    onUnmounted(() => {
      stopWatch()
    })

    const curEquList = computed(() => {
      return basicStore.equipment_list.filter(item => configStore.single_set.includes(item.id)).sort((a, b) => Number(a.id) - Number(b.id))
    })

    // 切换装备计算
    debouncedWatch(
      () => {
        return [...configStore.single_set.map(Number)].sort().join(",")
      },
      async () => {
        await result.execute()
      },
      {
        debounce: 500
      }
    )

    // 自定义词条变化计算
    debouncedWatch<string>(
      () => {
        return JSON.stringify(configStore.customize)
      },
      async (newV, oldV) => {
        const newValue = JSON.parse(newV)
        const oldValue = JSON.parse(oldV)
        const ids: number[] = []
        Object.keys(newValue).forEach(key => {
          if ((newValue[key] ?? []).map(Number).sort().join(",") != (oldValue[key] ?? []).map(Number).sort().join(",")) {
            ids.push(Number(key))
          }
        })
        let toCalc = false
        ids.forEach(a => {
          if (configStore.single_set.includes(a)) {
            toCalc = true
          }
        })
        toCalc && (await result.execute())
      },
      {
        deep: true,
        debounce: 500
      }
    )

    debouncedWatch(
      () => [...configStore.fusion_list],
      async () => {
        await result.execute()
      },
      {
        debounce: 500
      }
    )

    watch(choose_part, () => {
      compare_list.value = []
      result.state.value.compar = {}
    })

    const openUrl = useOpenWindow()

    const app = useAppStore()

    const info = computed(() => {
      return app.uid > 0 ? `${app.userInfo.userName}(${app.uid})` : ""
    })

    const openDetail = () => {
      if (result.state.value && result.state.value.id) {
        result.state.value.forge_set = toObj(configStore).forge_set
        result.state.value.merge_list = configStore.merge
        result.state.value.fusion_list = configStore.fusion_list as number[]
        result.state.value.customize = configStore.customize
        result.state.value.specificity = configStore.specificity;
        (result.state.value as any).talisman_set = configStore.talisman_set;
        (result.state.value as any).rune_set = configStore.rune_set;
        result.state.value.equips = basicStore.equipment_list.filter(a => configStore.single_set.includes(a.id)) ?? []
        sessionStorage.setItem(result.state.value.id?.toString() ?? "", JSON.stringify(result.state.value))
        openUrl("/result", { query: { res: `${result.state.value.id}`, standard: `${detailsStore.standard_uuid}` }, width: 890, height: 635, title: `${info.value} 请勿用于打桩排名等节奏` })
      }
    }

    function getEquCustom(id: string) {
      if (Number.parseInt(id) > 100000) {
        const customs = configStore.customize[id.toString()]
        const temp: any = []
        customs?.forEach(index => {
          temp.push(basicStore.entry_list?.[index.toString()])
        })
        return temp
      } else {
        return []
      }
    }

    const compare_equs = computed(() => {
      if (choose_part.value != "-1") {
        const list = basicStore.equipment_list.filter(a => a.part == choose_part.value && !configStore.single_set.includes(a.id) && (a.id as number) < 30000) ?? []
        // if (filterMode.value) {
        //   list = list.filter(a => a.common)
        //   // list.filter(a=>a.id in )
        // }
        return list
      } else {
        return []
      }
    })

    function apply(index: string) {
      const item = combinations.value.filter(a => a.id == index)?.[0]
      configStore.importSingle(item.equips.map(r => Number.parseInt(r.id?.toString() ?? "0")).sort())
      configStore.fusion_list = item.fusion ?? []
      item.equips.forEach(eq => {
        eq.props = eq.props?.map(Number) ?? []
        if (eq.props.length > 0) {
          configStore.customize[Number.parseInt(eq.id?.toString() ?? "0")] = eq.props as number[]
        }
        eq.merge = eq.merge?.map(Number) ?? []
        if (eq.merge.length > 0) {
          configStore.merge[Number.parseInt(eq.id?.toString() ?? "0")] = eq.merge as number[]
        }
      })
    }

    const { alert, confirm } = useDialog()
    const cur_tab = ref(0)

    const calc_compare = async () => {
      if (choose_part.value == "-1") {
        await alert({
          content: "请先选择对比部位"
        })
        return
      }
      const curEqus = basicStore.equipment_list.find(a => configStore.single_set.includes(a.id) && a.part == choose_part.value)
      if (!curEqus) {
        await alert({
          content: "请先设置当前部位装备"
        })
        return
      }
      if (curEqus.alternative.length == 0 && compare_list.value.length == 0) {
        await alert({
          content: "当前部位为固定史诗且未选择对比装备"
        })
        return
      }

      if (curEqus.alternative.length > 0 && (configStore.customize[curEqus.id?.toString() ?? ""]?.filter(a => a != 0)?.length ?? 0) < 4) {
        await alert({
          content: "当前部位设置的定制史诗词条不足四条"
        })
        return
      }
      if ((result.state.value.tip_part?.length ?? 0) > 0) {
        const res = await confirm({
          content: () =>
            h(
              "div",
              { class: "justify-center text-center my-10px", style: "white-space:pre-wrap;width:250px;color:white" },
              "当前搭配存在未能完全触发的【灰色装备】\n鼠标移动上去可查看缺少条件\n可能会影响到词条对比,是否继续？"
            )
        })
        if (!res.isOk) {
          return
        }
      }
      cur_id.value = curEqus.alternative.length > 0 ? (curEqus.id as number) : 0
      await result.execute()
      cur_tab.value = curEqus.alternative.length > 0 ? 0 : 1
    }

    const mergeInfo = computed(() => {
      const cur = curEquList.value.filter(a => a.part == "武器")?.[0]
      return {
        weaponType: cur?.type,
        merges: configStore.merge[cur?.id ?? ""] ?? []
      }
    })

    return () => (
      <div class="flex comparison">
        <div class="flex flex-col justify-between w-280px">
          <div class="flex h-24px mt-7px items-center justify-between !mr-8px !ml-8px ">
            <calc-select class="!h-22px !w-40%" onChange={(val: any) => apply(val)}>
              {renderList(combinations.value, item => (
                <calc-option value={item.id}>{item.name}</calc-option>
              ))}
            </calc-select>
            <calc-button class="!w-25%" onClick={() => openDetail()}>
                查看详情
            </calc-button>
            <calc-button class="!w-25%" onClick={calc_compare}>
                计算分析
            </calc-button>
          </div>
          <Watermark content={app.uid > 0 ? app.uid.toString() : "纸飞机计算器"}>
            <Profile
              withStandard={!!detailsStore.standard_uuid}
              standard-data={detailsStore.standard?.total_data}
              details={result.state.value.info}
              total-data={result.state.value.total_data}
              role={characterStore.role}
              equ-list={curEquList.value}
              class="m-5px !mt-0 !mr-2px !ml-2px !mb-2px"
              equips_forge={result.state.value.equips_forge}
              v-model:part={choose_part.value}
              canChoose={true}
              share={result.state.value}
              fusionList={configStore.fusion_list}
              showTM={((globalStore.global_set_details[2] ?? []) as number[]).includes(0)}
              showZF={false}
              showSubDetail={false}
              tipInfo={globalStore.global_set_details[3] as number[]}
              mergeInfo={mergeInfo.value}
            ></Profile>
          </Watermark>

          <div class="subitem w-265px ml-7px">
            <div class="head-sec">对比装备设置</div>
            <div class="body-sec !pt-2px h-75px overflow-y-auto">
              {choose_part.value != "-1" && <EquipList class="mx-7px equ-com" v-model:selected={compare_list.value} list={compare_equs.value} withTitle={false} />}
            </div>
          </div>
        </div>
        <div class="p-7px !pb-0">
          <Dictionary class="!mt-10px" simple={true} v-model:choosePart={choose_part.value} v-model:selectEquip={selectEquip.value}></Dictionary>
        </div>

        <div class="w-90 flex flex-col pt-7px">
          <calc-tabs v-model={cur_tab.value}>
            <calc-tab value={0}>定制史诗评估</calc-tab>
            <calc-tab value={1}>装备对比</calc-tab>
          </calc-tabs>
          {cur_tab.value == 1 && (
            <div class="h-150 overflow-y-auto">
              {renderList(
                Object.keys(result.state.value.compar ?? {}).sort((a, b) => (result.state.value.compar ?? {})[b] - (result.state.value.compar ?? {})[a]),
                key => {
                  const cur = basicStore.equipment_list.filter(a => a.id?.toString() == key)[0]
                  const res = (result.state.value.compar?.[key] ?? 0) >= result.state.value.total_data[0]
                  return (
                    <>
                      <div class="flex justify-between items-center h-45px">
                        <EquipTips eq={cur} forge={{ show: [false, false, false] }} showTips={true} pps={getEquCustom(cur.id?.toString() ?? "0")}></EquipTips>
                        <div class="flex flex-col ml-8px w-100%">
                          <div class={["text-xs", rarityClass(cur?.rarity ?? "")]}>{cur?.name}</div>
                        </div>
                        <div style="font-size:13.5px;font-weight:bolder" class={`text-hex-${res ? "3ea74e" : "ff0000"}`}>
                          {res ? "+" : ""}
                          {(((result.state.value.compar?.[key] ?? 0) / result.state.value.total_data[0] - 1) * 100).toFixed(2)}%
                        </div>
                      </div>
                    </>
                  )
                }
              )}
            </div>
          )}
          {cur_tab.value == 0 && (
            <div class="h-155 mt-1 overflow-y-disabled">
              <div class="bg-hex-0d0d0d p-1px h-55" style="border:1px solid #2C2525">
                <div class="h-8 flex items-center justify-center text-hex-E2B019 text-xs bg-hex-291808" style="font-weight:bolder">
                    当前提升最低词条
                </div>
                {min_cus.value > 0 && (
                  <div class="flex h-42 items-center leading-relaxed">
                    <div class="m-5px mr-10px ml-10p">
                      <div class="flex w-100% items-center">
                        <calc-checkbox disabled></calc-checkbox>
                        <div class="ml-5px">
                          <div class="flex text-hex-8a6f36">
                            <div>攻击强化:{basicStore.entry_list?.[min_cus.value]?.attack}</div>
                            <div class="ml-5px">增益量:{basicStore.entry_list?.[min_cus.value]?.buff}</div>
                          </div>
                          {renderList(basicStore.entry_list?.[min_cus.value].props, prop => (
                            <div class="text-hex-b1a785">{prop}</div>
                          ))}
                        </div>
                      </div>
                    </div>
                  </div>
                )}
              </div>

              <div class="bg-hex-0d0d0d p-1px h-100" style="border:1px solid #2C2525">
                <div class="h-8 flex items-center justify-center text-hex-E2B019 text-xs bg-hex-181818" style="font-weight:bolder">
                    可替换词条
                </div>
                {analysis_cus.value.length > 0 && (
                  <div class="overflow-y-auto max-h-90 leading-relaxed">
                    {renderList(analysis_cus.value, item => {
                      return (
                        <>
                          <div class="m-5px mr-10px ml-10p">
                            <div class="flex w-100% items-center">
                              <calc-checkbox disabled></calc-checkbox>
                              <div class="ml-5px">
                                <div class="flex text-hex-8a6f36">
                                  <div>攻击强化:{basicStore.entry_list?.[Number.parseInt(item[0])]?.attack}</div>
                                  <div class="ml-5px">增益量:{basicStore.entry_list?.[Number.parseInt(item[0])]?.buff}</div>
                                </div>
                                {renderList(basicStore.entry_list?.[Number.parseInt(item[0])].props, prop => (
                                  <div class="text-hex-b1a785">{prop}</div>
                                ))}
                                <div class="text-hex-3ea74e mt-2px">提升参考 {((item[1] / result.state.value.total_data[0] - 1) * 100).toFixed(2)}%</div>
                              </div>
                            </div>
                          </div>
                        </>
                      )
                    })}
                  </div>
                )}
              </div>
            </div>
          )}
        </div>
      </div>
    )
  }
})
</script>

<style lang="scss">
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

  .cus .i-checkbox {
    display: flex;
    align-items: flex-start !important;

    .i-checkbox-icon {
      margin-top: 5px !important;
    }

    .i-checkbox-icon-disable {
      margin-top: 5px !important;
    }

    .i-checkbox-label {
      line-height: 22px !important;
    }
  }

  .comparison {
    .equ-com {
      margin-top: 5px;

      display: flex;
      flex-wrap: wrap;
      align-content: flex-start;

      .item {
        width: 30px;
        height: 34px;
        margin-left: 4px;
        // &:nth-child(7n + 1) {
        //   margin-left: 0px;
        // }
      }
    }

    .s-left {
      .approved-form {
        width: calc(100% - 23px);
      }
    }
  }
</style>

<style lang="scss" scoped>
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
</style>
