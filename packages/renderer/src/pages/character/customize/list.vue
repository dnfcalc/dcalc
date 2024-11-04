<script lang="tsx">
import { useAsyncState, useDebounceFn } from "@vueuse/core"
import { computed, defineComponent, ref, renderList, watch } from "vue"
import { useBasicInfoStore, useCharacterStore, useConfigStore, useGlobalStore } from "@/store"
import { padding } from "@/utils"
import Watermark from "@/components/watermark/index.vue"


export interface ICusUpgrade {
  id: string
  damage: number
  percent: string
  color: string
}

export default defineComponent({
  name: "Others",
  props: {
    eid: {
      type: String,
      default: "0"
    },
    calc: {
      type: Boolean,
      default: true
    },
    onlyShowInfo: {
      type: Boolean,
      default: false
    }
  },
  setup(props) {
    const configStore = useConfigStore()
    const basicStore = useBasicInfoStore()
    const characterStore = useCharacterStore()
    const globalStore = useGlobalStore()

    const selectEquip = ref<ID>(props.eid)
    const colspans = ref([false, true, true, true, true, true, true, true])
    const selectEquipProps = ref<number[]>([0, 0, 0, 0])
    const filterProps = ref(!props.onlyShowInfo)
    // const selectPropsCheckedList = ref<Record<string, boolean>>({})

    const result = useAsyncState(
      () => {
        return configStore.calc(true, false, alternative_list(selectEquip.value, -1).length >= 0 && characterStore.is_delear ? Number.parseInt(selectEquip.value as string) : 0)
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
        cus: undefined,
        fusion_list: [],
        merge_list: {}
      },
      {
        resetOnExecute: false,
        immediate: false
      }
    )


    const cus_up = computed(() => {
      const cur_equ = selectEquip.value
      const temp: ICusUpgrade[] = []
      if (!result.state.value.cus) {
        return temp
      }
      if (!((cur_equ?.toString() ?? "") in result.state.value.cus)) {
        return temp
      }
      if ((configStore.customize?.[selectEquip.value ?? ""]?.filter(a => a != 0)?.length ?? 0) > 3) {
        return temp
      }
      const damage = result.state.value.total_data[0]
      if (damage == 0) {
        return temp
      }
      for (const key in result.state.value.cus[cur_equ?.toString() ?? ""]) {
        temp.push({
          id: key,
          damage: result.state.value.cus[cur_equ?.toString() ?? ""][key],
          percent: `${((result.state.value.cus[cur_equ?.toString() ?? ""][key] / damage) * 100 - 100).toFixed(2)}%`,
          color: ""
        })
      }
      temp
        .sort((a, b) => b.damage - a.damage)
        .forEach((item, index) => {
          const x = index / (result.state.value.cus[cur_equ?.toString() ?? ""].length ?? 1) - 2
          const y = 1 / (1 + Math.exp(-x))
          item.color = `rgb(${Math.trunc(255 - 80 * y)},${Math.trunc(245 - 80 * y)},${Math.trunc(0 + 100 * y)})`
        })
      return temp ?? []
    })

    const keyword = ref("")

    function alternative_list(id: ID, type = -1, filter: string = "") {
      let temp = basicStore.equipment_list.filter(item => item.id == id)?.[0]?.alternative ?? []
      if (filterProps.value == true) {
        if (characterStore.is_delear) {
          temp = temp.filter(a => basicStore.entry_list?.[a]?.filter == filter)
          if (filter == "其余") {
            temp = temp.sort((a, b) => (basicStore.entry_list?.[b]?.attack ?? 0) - (basicStore.entry_list?.[a]?.attack ?? 0))
          }
          return temp
        } else { return temp.filter(a => basicStore.entry_list?.[a]?.buff == Number.parseInt(filter)) }
      }
      // 共有词条
      if (type == 2) {
        temp = temp.filter(a => basicStore.entry_list?.[a]?.type == 1)
        // temp = temp.filter(a => props_public.includes(a))
      }
      // 部位专属词条
      if (type == 1) {
        temp = temp.filter(a => [2, 3, 4, 5, 6, 7, 8].includes(basicStore.entry_list?.[a]?.type ?? 0))
        // temp = temp.filter(a => props_armors.includes(a) || props_jewels.includes(a) || props_specials.includes(a))
      }
      // 专属词条
      if (type == 0) {
        temp = temp.filter(a => (basicStore.entry_list?.[a]?.type ?? 0) > 10000)
        // temp = temp.filter(a => !props_public.includes(a) && !props_armors.includes(a) && !props_jewels.includes(a) && !props_specials.includes(a))
      }

      // if ((cus_up.value ?? []).length > 0) {
      //   temp.sort((a, b) => cus_up.value.findIndex(c => c.id == a.toString()) - cus_up.value.findIndex(c => c.id == b.toString()))
      // }
      // if (keyword.value != "") {
      //   temp = temp.filter(a => (entry(a)?.props ?? []).join(",").indexOf(keyword.value) >= 0)
      // }
      return temp
    }

    function chooseProp(id: number) {
      return async (event: Event) => {
        event.stopPropagation()
        let index = selectEquipProps.value.indexOf(id)
        if (index < 0) {
          index = selectEquipProps.value.indexOf(0)
        } else {
          id = 0
        }
        if (index >= 0) {
          selectEquipProps.value[index] = id
        }
        configStore.customize[selectEquip.value ?? ""] = selectEquipProps.value
      }
    }

    const entry = (index: number) => {
      return basicStore.entry_list?.[index]
    }

    const calc = async () => {
      if (!props.calc) {
        return
      }
      if (!characterStore.is_delear) {
        return
      }
      if (configStore.single_set.includes(Number(selectEquip.value)) && (configStore.customize?.[selectEquip.value ?? ""]?.filter(a => a != 0)?.length ?? 0) < 4) {
        await result.execute()
      }
    }

    // watch(() => (configStore.single_set.indexOf(selectEquip.value) < 0 ? [0, 0, 0, 0] : (configStore.customize[selectEquip.value ?? ""] ?? [0, 0, 0, 0]).map(Number)))

    watch(
      () => configStore.customize,
      useDebounceFn(async () => {
        await calc()
      }, 700),
      {
        // immediate: true,
        deep: true
      }
    )

    watch(
      () => props.eid,
      async (val: ID) => {
        selectEquip.value = val
        colspans.value = [false, true, true, true, true, true, true, true, true, true]
        const temp = (configStore.customize[val ?? ""] ?? [0, 0, 0, 0]).map(Number)
        const entries = basicStore.equipment_list.filter(item => item.id == val)?.[0]?.alternative ?? []
        selectEquipProps.value = temp.map(a => {
          if (a != 0 && !entries.includes(a)) {
            a = 0
          }
          return a
        }).map(Number)
        await calc()
        // cus_up_calc()
        // alternative_list(val).forEach(a => (selectPropsCheckedList.value[a] = selectEquipProps.value.indexOf(a) >= 0))
      },
      {
        immediate: true
      }
    )

    const filterList = computed(() =>
      filterProps.value ? (characterStore.is_delear ? ["伤害", "CD", "速度", "其余"] : ["514", "509", "504", "499", "494", "489", "484", "479", "474", "464"]) : ["专属", "部位", "公共"]
    )

    // const isChoose = computed(() => {
    //   ;(item: number) => {
    //     selectEquipProps.value.indexOf(item) >= 0
    //   }
    // })

    return () => (
      <Watermark>
        <div class="w-full">
          <div class="px-2 justify-between items-center">
            <div class="flex space-x-2 mb-2 items-center ">
              <calc-autocomplete placeholder="请输入关键字搜索" class="flex-1 !h-5" v-model={keyword.value}></calc-autocomplete>
              <calc-checkbox v-model={filterProps.value}>词条分类</calc-checkbox>
              <calc-button onClick={() => (keyword.value = "")} title="重置" class="ml-4" icon="reset"></calc-button>
            </div>
          </div>
        </div>
        {/* <calc-loading class="w-100%" loading={isLoading.value}> */}
        {renderList(filterList.value, (type, index) => {
          let alternative = alternative_list(selectEquip.value, index, type)
          if ((cus_up.value ?? []).length > 0) {
            alternative.sort((a, b) => {
              let a_index = cus_up.value.findIndex(c => c.id == a.toString())
              let b_index = cus_up.value.findIndex(c => c.id == b.toString())
              if (a_index < 0) {
                a_index = selectEquipProps.value.includes(a) ? -1 : (cus_up.value ?? []).length + (entry(a)?.attack ?? 0);
              }
              if (b_index < 0) {
                b_index = selectEquipProps.value.includes(b) ? -1 : (cus_up.value ?? []).length + (entry(b)?.attack ?? 0);
              }
              return a_index - b_index
            })
          } else {
            alternative.sort((a, b) => {
              let a_index = selectEquipProps.value.indexOf(a)
              let b_index = selectEquipProps.value.indexOf(b)
              if (a_index < 0) {
                a_index = (cus_up.value ?? []).length + (entry(a)?.attack ?? 0)
              }
              if (b_index < 0) {
                b_index = (cus_up.value ?? []).length + (entry(b)?.attack ?? 0)
              }
              return a_index - b_index
            })
          }
          if (keyword.value != "") {
            alternative = alternative.filter(a => (entry(a)?.props ?? []).join(",").includes(keyword.value))
          }
          if (alternative.length > 0) {
            return (
              <>
                <div onClick={() => (colspans.value[index] = !colspans.value[index])} class="m-10px text-hex-3e8848 mb-2px">{` < ${type}属性 > - 共计${padding(alternative.length, 2)}条 点击${colspans.value[index] ? "展开" : "折叠"}`}</div>
                <div class={["transition-all", "ease-out-in", "h-auto", "overflow-hidden"].concat(!colspans.value[index] ? [""] : ["max-h-0"])}>
                  {renderList(alternative, item => {
                    const entry_info = entry(item)
                    const disabled: boolean = props.onlyShowInfo || (!selectEquipProps.value.includes(item) && selectEquipProps.value.filter(a => a == 0)?.length == 0)
                    const seleted = selectEquipProps.value.includes(item)
                    return (
                      <div class="h-auto m-5px mr-8px ml-8px">
                        <>
                          <div class="flex w-100% items-center">
                            <calc-checkbox modelValue={seleted} key={item} class="!h-auto" disabled={disabled} onClick={chooseProp(item)}>
                              {() => (
                                <>
                                  <div class={["flex ml-5px", disabled ? "text-hex-5b5b5b" : "text-hex-8a6f36"]}>
                                    <div>攻击强化 +{entry_info?.attack}%</div>
                                    <div class="ml-10px">增益量 {entry_info?.buff}</div>
                                  </div>
                                  {renderList(entry_info?.props, prop => (
                                    <div class={["ml-5px", disabled ? "text-hex-5b5b5b" : "text-hex-b1a785"]} v-html={(prop as string).replaceAll(/@([^@]*)@/g, (m, _index) => `<span style="color:#3ea74e">${m.slice(1, -1)}</span>`)}></div>
                                  ))}
                                  {(cus_up.value ?? []).length > 0 && (cus_up.value ?? []).findIndex(a => a.id == item.toString()) >= 0 && (
                                    <div class="ml-5px flex text-hex-3ea74e">
                                      提升参考
                                      {(() => {
                                        const temp = cus_up.value.find(a => a.id == item.toString())
                                        // return <div style={"color:" + temp?.color}>{temp?.percent}</div>
                                        return <div class="ml-5px">{temp?.percent}</div>
                                      })()}
                                    </div>
                                  )}
                                </>
                              )}
                            </calc-checkbox>
                          </div>
                        </>
                      </div>
                    )
                  })}
                </div>
              </>
            )
          }
        })}
        {/* </calc-loading> */}
      </Watermark>
    )
  }
})
</script>
