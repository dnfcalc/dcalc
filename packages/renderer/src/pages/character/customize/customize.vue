<script lang="tsx">
import { computed, defineComponent, reactive, ref, renderList, watch } from "vue"
import List from "./list.vue"
import type { IEquipmentInfo } from "@/api/info/type"
import EquipIcon from "@/components/internal/equip/eq-icon.vue"
import { useBasicInfoStore, useConfigStore } from "@/store"
import { rarityClass } from "@/utils"
import Watermark from "@/components/watermark/index.vue"

export interface ICusUpgrade {
  id: string
  damage: number
  percent: string
  color: string
}

  type FilterFunction = (e: IEquipmentInfo) => boolean

export default defineComponent({
  async setup() {
    const configStore = useConfigStore()
    const basicStore = useBasicInfoStore()
    const filter = ref<FilterFunction | null>()

    const keyword = reactive({
      value: "",
      cache: ""
    })

    const equips = computed(() => {
      let list = basicStore.equipment_list.filter(item => item.alternative.length > 0 && Number.parseInt(item.id?.toString() ?? "0") < 100000) ?? [] ?? []
      let props: any[] = []
      Object.keys(basicStore.entry_list ?? {}).forEach(index => {
        if ((basicStore.entry_list?.[index]?.props.join(";").indexOf(keyword.value.trim()) ?? -1) >= 0) {
          props.push(index)
        }
      })
      props = props.map(Number)
      list = list.filter(r => {
        return r.name.includes(keyword.value.trim()) || [...r.alternative, ...r.growth, ...r.stable].map(Number).filter(item => props.includes(item))?.length > 0
      })
      if (!!filter.value && filter.value instanceof Function) {
        list = list.filter(filter.value)
      }
      return list
    })

    const selectEquip = ref<ID>()

    const cur_equ = computed(() => basicStore.equipment_list.filter(a => a.id == selectEquip.value)[0])

    const pagination = reactive({
      page: 1,
      pageSize: 15
    })

    const show_list = computed(() => {
      const start = (pagination.page - 1) * pagination.pageSize
      const end = start + pagination.pageSize
      return equips.value.slice(start, end)
    })

    function reset() {
      keyword.cache = ""
      keyword.value = ""
      pagination.page = 1
    }

    const selectEquipProps = computed(() => {
      const temp = configStore.customize[selectEquip.value ?? ""] ?? [0, 0, 0, 0]
      return temp.map(Number)
    })

    /**
       *  显示列表发生变化时，自动选中第一项，并清空属性选择
       * 有BUG 后续修复
       */
    // watch(
    //   show_list,
    //   () => {
    //     selectEquip.value = show_list.value[0]?.id
    //     selectEquipProps.value = [0, 0, 0, 0]
    //   },
    //   { immediate: true }
    // )

    function chooseEqu(equ: IEquipmentInfo) {
      return (event: Event) => {
        event.preventDefault()
        selectEquip.value = equ.id
      }
    }

    const total = computed(() => equips.value.length)
    const total_page = computed(() => Math.ceil(total.value / pagination.pageSize))

    watch(total_page, () => {
      pagination.page = 1
    })

    function search() {
      keyword.value = keyword.cache
      pagination.page = 0
    }

    const entry = (index: number) => {
      return basicStore.entry_list?.[index]
    }

    const singleRef = ref<HTMLElement | null>(null)

    return () => (
      <div class="flex singleset" ref={singleRef}>
        <div class="flex flex-col m-7px mb-0 w-full">
          <div class=" w-full">
            <div class="w-full pb-1.5">
              <div class="bg-hex-000000/45 py-2 px-2 justify-between items-center">
                <div class="flex space-x-2 mb-2 items-center ">
                  <calc-autocomplete onEnter={search} placeholder="请输入关键字搜索" class="flex-1 !h-5" v-model={keyword.cache}></calc-autocomplete>
                  <calc-button onClick={search} title="搜索" class="ml-2" icon="search"></calc-button>
                  <calc-button onClick={reset} title="重置" class="ml-4" icon="reset"></calc-button>
                </div>
              </div>
            </div>
            <div class="flex h-155  w-full">
              <div class="h-full bg-hex-0d0d0d mx-2px w-25%">
                <calc-selection v-model={selectEquip.value} active-class="equip-line-selected" class="h-[calc(100%-2.5rem)]">
                  {renderList(show_list.value, item => {
                    return (
                      <calc-item value={item.id} onClick={chooseEqu(item)} class="flex h-9 mb-2px px-1 justify-between items-center equip-line relative box-border">
                        <div class="h-full w-full top-0 left-0 absolute mask"></div>
                        <EquipIcon eq={item}></EquipIcon>
                        <span class={["text-xs", "ml-4", rarityClass(item.rarity ?? "")]}>{item.name}</span>
                        <span class={["h-4 w-6"]}></span>
                      </calc-item>
                    )
                  })}
                  {renderList(pagination.pageSize - show_list.value.length, () => (
                    <div class="flex h-9 mb-2px px-1 justify-between items-center equip-line relative box-border"></div>
                  ))}
                </calc-selection>
                <calc-pagination v-model:page={pagination.page} total-page={total_page.value} v-show={total_page.value > 0}></calc-pagination>
              </div>

              <div class="h-full bg-hex-0d0d0d w-75% s-left">
                {selectEquip.value && (
                  <>
                    <div class="flex flex-col p-10px">
                      <div class="flex h-30px">
                        <EquipIcon eq={cur_equ.value}></EquipIcon>
                        <div class="flex flex-col ml-8px w-100%">
                          <div class={["text-xs", rarityClass(cur_equ.value.rarity ?? "")]}>{cur_equ.value.name}</div>
                          <div class="text-xs text-right text-hex-8a6f36">{`${cur_equ.value.type}(${cur_equ.value.part})`}</div>
                        </div>
                      </div>
                      <div style="border-bottom:1px solid #303030;margin:8px 0;"></div>
                    </div>
                    <div class="flex h-89%">
                      <div class="flex flex-col h-full w-60% overflow-y-auto !max-w-60%" style="border-right:1px solid #303030">
                        <List eid={selectEquip.value.toString()} />
                      </div>
                      <Watermark class="flex flex-col h-full w-40% overflow-y-auto !max-w-40%" style="line-height:22px">
                        <div class="m-10px">
                          <div class="text-hex-4aa256">{" <成长属性> "}</div>

                          {renderList(selectEquipProps.value, (propID, index) => {
                            if (propID == 0) {
                              return (
                                <>
                                  <div class="flex items-center">
                                    <div class="prop-icon"></div>
                                    <div class="ml-8px text-hex-b59834">{`属性 ${index + 1} - Lv1`}</div>
                                  </div>
                                  <div class="ml-20px text-hex-5b5b5b">随机属性，请在左侧进行选择</div>
                                </>
                              )
                            } else {
                              const entry_info = entry(propID)
                              return (
                                <>
                                  <div class="flex items-center">
                                    <div class="prop-icon"></div>
                                    <div class="ml-8px text-hex-b59834">{`属性 ${index + 1} - Lv1`}</div>
                                  </div>
                                  <div class="ml-20px text-hex-8a6f36">
                                    <div>{"攻击强化 "}{entry_info?.attack}%</div>
                                    <div>增益量 {entry_info?.buff}</div>
                                  </div>
                                  {renderList(entry_info?.props, prop => (
                                    <div class={["ml-20px", "text-hex-b1a785"]}>{prop}</div>
                                  ))}
                                </>
                              )
                            }
                          })}
                        </div>
                      </Watermark>
                    </div>
                  </>
                )}
              </div>
            </div>
          </div>
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

  .i-checkbox {
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
</style>

<style lang="scss" scoped>
  .prop-icon {
    content: "";
    display: inline-block;
    width: 12px;
    height: 12px;
    background-image: url(@/assets/img/icon/switch.png);
  }

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

  .singleset {
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

        // &:hover {
        //   width: 30px;
        //   height: 30px;
        //   z-index: 3;
        //   background-image: url(@/assets/img/item_hover.png);
        //   background-size: 100% 100%;
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
