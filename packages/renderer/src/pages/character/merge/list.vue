<script lang="tsx">
import { isDefined, useAsyncState, useDebounceFn } from "@vueuse/core"
import type { PropType } from "vue";
import { computed, defineComponent, ref, renderList, watch } from "vue"
import { useBasicInfoStore, useCharacterStore, useConfigStore, useGlobalStore } from "@/store"
import Watermark from "@/components/watermark/index.vue"


export interface IMergeUpgrade {
  id: string
  damage: number
  percent: string
  color: string
}

export default defineComponent({
  name: "Others",
  props: {
    eid: {
      type: [Number, String] as PropType<ID>,
      default: "0"
    },
    calc: {
      type: Boolean,
      default: true
    }
  },
  setup(props) {
    const mode = ref(false)
    const selectEquipProps = ref<number[]>([0, 0, 0])
    const selectEquip = ref<ID>(props.eid)
    const basicStore = useBasicInfoStore()
    const characterStore = useCharacterStore()
    const keyword = ref("")
    const configStore = useConfigStore()
    const globalStore = useGlobalStore()

    const result = useAsyncState(
      () => {
        return configStore.calc(true, false, 0, configStore.single_set.includes(Number(selectEquip.value)) && characterStore.is_delear ? Number(selectEquip.value) : 0)
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
        merge: undefined,
        fusion_list: [],
        merge_list: {}
      },
      { resetOnExecute: false, immediate: false }
    )


    const merge_up = computed(() => {
      const cur_equ = selectEquip.value
      const temp: IMergeUpgrade[] = []
      if (!props.calc) {
        return temp
      }
      if (!result.state.value.merge) {
        return temp
      }
      if (!((cur_equ?.toString() ?? "") in result.state.value.merge)) {
        return temp
      }
      if ((configStore.merge?.[selectEquip.value ?? ""]?.filter(a => a != 0)?.length ?? 0) > 2) {
        return temp
      }
      const damage = result.state.value.total_data[0]
      if (damage == 0) {
        return temp
      }
      for (const key in result.state.value.merge[cur_equ?.toString() ?? ""]) {
        temp.push({
          id: key,
          damage: result.state.value.merge[cur_equ?.toString() ?? ""][key],
          percent: `${((result.state.value.merge[cur_equ?.toString() ?? ""][key] / damage) * 100 - 100).toFixed(2)}%`,
          color: ""
        })
      }
      temp
        .sort((a, b) => b.damage - a.damage)
        .forEach((item, index) => {
          const x = index / (result.state.value.merge[cur_equ?.toString() ?? ""].length ?? 1) - 2
          const y = 1 / (1 + Math.exp(-x))
          item.color = `rgb(${Math.trunc(255 - 80 * y)},${Math.trunc(245 - 80 * y)},${Math.trunc(0 + 100 * y)})`
        })
      return temp
    })


    const entry_list = computed(() => {
      let temp
          = ((selectEquip.value as number) ?? 0) > 0
            ? Object.keys(basicStore.entry_list ?? {})
              .filter(a => [9, 10].includes(basicStore.entry_list?.[a]?.type ?? 0))
              .sort((a, b) => (basicStore.entry_list?.[a]?.order ?? -1) - (basicStore.entry_list?.[b]?.order ?? -1))
            : []
      if (merge_up.value.length > 0) {
        temp.sort((a, b) => merge_up.value.findIndex(c => c.id == a) - merge_up.value.findIndex(c => c.id == b))
      }
      if (!characterStore.is_delear) {
        temp.sort((a, b) => (basicStore.entry_list?.[b]?.buff ?? 0) - (basicStore.entry_list?.[a]?.buff ?? 0))
      }
      temp.sort((a, b) => {
        let a_index = selectEquipProps.value.indexOf(Number(a))
        let b_index = selectEquipProps.value.indexOf(Number(b))
        if (a_index < 0) {
          a_index = (merge_up.value ?? []).length + (basicStore.entry_list?.[a]?.order ?? -1)
        }
        if (b_index < 0) {
          b_index = (merge_up.value ?? []).length + (basicStore.entry_list?.[a]?.order ?? -1)
        }
        return a_index - b_index
      })
      if (keyword.value != "") {
        temp = temp.filter(
          a =>
            (`${basicStore.entry_list?.[a]?.order ?? ""}.`).toString().indexOf(keyword.value) == 0
              || (basicStore.entry_list?.[a]?.order ?? "").toString().indexOf(keyword.value) == 0
              || (basicStore.entry_list?.[a]?.props ?? []).join("").includes(keyword.value)
        )
      }
      return temp
    })

    const calc = async () => {
      if (!props.calc) {
        return
      }
      if (!characterStore.is_delear) {
        return
      }
      if (configStore.single_set.includes(Number(selectEquip.value)) && (configStore.merge?.[selectEquip.value ?? ""]?.filter(a => a != 0)?.length ?? 0) < 3) {
        await result.execute()
      }
    }


    const selectPropsInfos = computed(() => {
      const temp: number[][] = [[], []]
      selectEquipProps.value.forEach(a => {
        if (basicStore.entry_list?.[a]?.order || basicStore.entry_list?.[a]?.order == 0) {
          temp[0].push(basicStore.entry_list?.[a]?.order as number)
          temp[1].push(basicStore.entry_list?.[a]?.type as number)
        }
      })
      return temp
    })

    const merge_type = computed(() => (mode.value ? 10 : 9))

    function chooseProp(id: number) {
      return (event: Event) => {
        const entry_info = basicStore.entry_list?.[id]
        let canselect = true

        /* 判断是否类型重复 */

        canselect = canselect && !selectPropsInfos.value[0].includes(entry_info?.order ?? -1)

        /* 判断是否有位置 */

        canselect = canselect && selectPropsInfos.value[1].filter(a => a == merge_type.value)?.length < (merge_type.value == 9 ? 2 : 1)
        if (selectEquipProps.value.includes(Number(id))) {
          canselect = true
        }
        if (!canselect) {
          return
        }
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
        configStore.merge[selectEquip.value as number] = selectEquipProps.value
      }
    }

    watch(
      () => configStore.merge,
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
        if (isDefined(val)) {
          selectEquip.value = val
          const temp = configStore.merge[val ?? ""] ?? [0, 0, 0]
          selectEquipProps.value = [...new Array(3 - temp.length).fill(0), ...temp].map(Number)
          await calc()
        }
      },
      {
        immediate: true
      }
    )

    return () => (
      <Watermark>
        {selectEquip.value && (
          <div class="w-full">
            <div class="px-2 justify-between items-center">
              {/* <calc-tabs v-model={merge_type.value}>
                  <calc-tab value={9}>巴卡尔普通</calc-tab>
                  <calc-tab value={10}>巴卡尔困难</calc-tab>
                </calc-tabs> */}
              <div class="flex space-x-2 mb-2 items-center ">
                <div class="flex items-center justify-end">
                  <div class={`text-hex-${mode.value ? "5b5b5b" : "e9c558"}`}>普通</div>
                  <calc-checkbox round v-model={mode.value}></calc-checkbox>
                  <div class={`text-hex-${!mode.value ? "5b5b5b" : "e9c558"}`}>困难</div>
                </div>
                <calc-autocomplete placeholder="请输入关键字搜索" class="flex-1 !h-5" v-model={keyword.value}></calc-autocomplete>

                <calc-button onClick={() => (keyword.value = "")} title="重置" class="ml-4" icon="reset"></calc-button>
              </div>
            </div>
          </div>
        )}
        {renderList(entry_list.value, item => {
          const entry_info = basicStore.entry_list?.[item]
          let canselect = true

          /* 判断是否类型重复 */

          canselect = canselect && !selectPropsInfos.value[0].includes(entry_info?.order ?? -1)

          /* 判断是否有位置 */

          canselect = canselect && selectPropsInfos.value[1].filter(a => a == merge_type.value)?.length < (merge_type.value == 9 ? 2 : 1)
          canselect = selectEquipProps.value.includes(Number(item)) || canselect
          return (
            entry_info?.type == merge_type.value && (
              <div class="h-auto m-5px mr-10px ml-10px" key={item}>
                <div class="flex w-100% items-center">
                  <calc-checkbox modelValue={selectEquipProps.value.includes(Number(item))} class="!h-auto" disabled={!canselect} onClick={chooseProp(Number(item))}>
                    {() => (
                      <>
                        <div class={["flex ml-10px", !canselect ? "text-hex-5b5b5b" : "text-hex-8a6f36"]}>
                          <div>{entry_info?.order}.</div>
                          <div class="ml-5px">攻击强化 +{entry_info?.attack}%</div>
                          <div class="ml-10px">增益量 {entry_info?.buff}</div>
                        </div>
                        {renderList(entry_info?.props, prop => (
                          <div class={["ml-10px", !canselect ? "text-hex-5b5b5b" : "text-hex-b1a785"]}>{prop}</div>
                        ))}
                        {merge_up.value.length > 0 && merge_up.value.findIndex(a => a.id == item) >= 0 && (
                          <div class="flex ml-10px text-hex-3ea74e">
                              提升参考
                            {(() => {
                              const temp = merge_up.value?.find(a => a.id == item)
                              // return <div style={"color:" + temp?.color}>{temp?.percent}</div>
                              return <div class="ml-10px">{temp?.percent}</div>
                            })()}
                          </div>
                        )}
                      </>
                    )}
                  </calc-checkbox>
                </div>
              </div>
            )
          )
        })}
      </Watermark>
    )
  }
})
</script>
