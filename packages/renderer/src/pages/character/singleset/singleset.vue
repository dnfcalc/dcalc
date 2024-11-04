<script lang="tsx">
import { useAsyncState, useDebounceFn } from "@vueuse/core"
import { computed, defineComponent, onUnmounted, ref, renderList, watch } from "vue"
import Dictionary from "./edictionary.vue"
import Profile from "@/components/internal/profile/index.vue"
import { useAppStore, useBasicInfoStore, useCharacterStore, useConfigStore, useDetailsStore, useGlobalStore } from "@/store"
import { useOpenWindow } from "@/hooks/open"
import { toObj } from "@/utils"
import Watermark from "@/components/watermark/index.vue"

export interface IJadeUpgrade {
  id: number
  name: string
  damage: number
  percent: string
  color: string
  order: number
}

export default defineComponent({
  async setup() {
    const configStore = useConfigStore()
    const basicStore = useBasicInfoStore()
    const detailsStore = useDetailsStore()
    const characterStore = useCharacterStore()
    const globalStore = useGlobalStore()

    const choose_part = ref("-1")

    const selectEquip = ref<ID>()

    const result = useAsyncState(
      () => {
        return configStore.calc(true, false)
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
        merge_list: {},
        specificity: {}
      },
      { resetOnExecute: false }
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
    watch<any>(
      () => {
        return [...configStore.single_set.map(Number)].sort().join(",")
      },
      useDebounceFn(async () => {
        await result.execute()
      }, 500)
    )

    watch(
      () => {
        return JSON.stringify(configStore.specificity_list)
      },
      useDebounceFn(async () => {
        await result.execute()
      }, 500)
    )

    watch(
      () => {
        return JSON.stringify(configStore.stone_set)
      },
      useDebounceFn(async () => {
        await result.execute()
      }, 500)
    )

    watch(
      () => {
        return JSON.stringify(configStore.specificity)
      },
      useDebounceFn(async () => {
        await result.execute()
      }, 500)
    )

    watch(
      () => {
        return JSON.stringify(configStore.asrahan)
      },
      useDebounceFn(async () => {
        await result.execute()
      }, 500)
    )

    watch(
      () => {
        return JSON.stringify(configStore.trigger_set)
      },
      useDebounceFn(async () => {
        await result.execute()
      }, 500)
    )

    watch(
      () => {
        return JSON.stringify(configStore.consumable_list
        )
      },
      useDebounceFn(async () => {
        await result.execute()
      }, 500)
    )



    // 自定义词条变化计算
    watch<string>(
      () => {
        return JSON.stringify(configStore.customize)
      },
      useDebounceFn(async (newV, oldV) => {
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
          if (configStore.single_set.includes(a) || configStore.fusion_list.includes(a)) {
            toCalc = true
          }
        })
        toCalc && (await result.execute())
      }, 500),
      {
        deep: true
      }
    )

    // 贴膜变化
    watch(
      () => [...configStore.fusion_list],
      useDebounceFn(async () => {
        await result.execute()
      }, 500)
    )

    // 融合变化
    watch(
      () => {
        return JSON.stringify(configStore.merge)
      },
      useDebounceFn(async () => {
        await result.execute()
      }, 500)
    )

    const openUrl = useOpenWindow()

    const app = useAppStore()

    const info = computed(() => {
      return app.uid > 0 ? `${app.userInfo?.userName}(${app.uid})` : ""
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

    function setStandard() {
      if (result.state.value.total_data[0] > 0) {
        sessionStorage.setItem(result.state.value.id?.toString() ?? "", JSON.stringify(result.state.value))
        detailsStore.setStandard(result.state.value.id)
      }
    }

    const jade = computed(() => {
      const damage = result.state.value.total_data[0]
      return Array.from(result.state.value.jade ?? [])
        .sort((a, b) => b.damage - a.damage)
        .map((item, index) => {
          const x = (index / (result.state.value.jade?.length ?? 1)) * 10 - 3
          const y = 1 / (1 + Math.exp(-x))
          return {
            id: item.id,
            name: item.name,
            damage: item.damage,
            percent: damage == 0 ? "- -" : `${((item.damage.round(0) / damage.round(0)) * 100 - 100).toFixed(2)}%`,
            color: `rgb(${Math.trunc(255 - 80 * y)},${Math.trunc(245 - 100 * y)},${Math.trunc(0 + 150 * y)})`,
            order: item.order
          }
        })
        .sort((a, b) => a.id - b.id)
        .sort((a, b) => a.order - b.order)
    })

    const singleRef = ref<HTMLElement | null>(null)

    const mergeInfo = computed(() => {
      const cur = curEquList.value.filter(a => a.part == "武器")?.[0]
      return {
        weaponType: cur?.type,
        merges: configStore.merge[cur?.id ?? ""] ?? []
      }
    })

    const showDetail = computed(() => {
      return (useAppStore().userInfo?.show ?? false) || characterStore.is_buffer || process.env.NODE_ENV == "development" || import.meta.env.MODE == "show"
    })

    return () => (
      <div class="flex singleset" ref={singleRef}>
        <div class="p-7px pb-1">
          <Dictionary cusCalc={true} v-model:choosePart={choose_part.value} v-model:selectEquip={selectEquip.value}></Dictionary>
        </div>

        <div class="flex flex-col pt-7px">
          <div class="flex h-24px items-center justify-between !mr-8px !ml-8px">
            <calc-button class="!w-30% flex justify-center items-center" onClick={setStandard}>
              设为基准
            </calc-button>
            <calc-button class="!w-30%" disabled={!showDetail.value} onClick={() => showDetail.value && detailsStore.setStandard(undefined)}>
                显示伤害
            </calc-button>
            <calc-button class="!w-30%" onClick={() => openDetail()}>
                查看详情
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
              class="!pb-0"
              equips_forge={result.state.value.equips_forge}
              v-model:part={choose_part.value}
              canChoose={true}
              share={result.state.value}
              fusionList={configStore.fusion_list}
              showTM={((globalStore.global_set_details[2] ?? []) as number[]).includes(0)}
              showZF={false}
              tipInfo={globalStore.global_set_details[3] as number[]}
              mergeInfo={mergeInfo.value}
            ></Profile>

          </Watermark>
        </div>
        {false && result.state.value.jade && (
          <div class="flex flex-col justify-between ml-2px w-350px items-center">
            <div class="flex h-30px w-100% justify-center items-center">辟邪玉提升率(理论值仅供参考)</div>
            {renderList(jade.value ?? [], item => (
              <div class="flex h-30px w-100%" style={`color:${item.color}`}>
                <div class="flex w-70% items-center justify-center">{item.name}</div>
                <div class="flex w-30% items-center justify-center">{item.percent}</div>
              </div>
            ))}
          </div>
        )}
      </div>
    )
  }
})
</script>

<style lang="scss">
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
</style>

<style lang="scss" scoped>
  .icon-checked {
    background-image: url("@/assets/img/control/item_checked.png");
    background-size: 100% 100%;
    background-repeat: no-repeat;
    background-position: center;
  }
</style>
