<script lang="tsx">
import { computed, defineComponent, onMounted, renderList, watch } from "vue"
import { useRoute } from "vue-router"
import { asyncComputed } from "@vueuse/core"
import api from "@/api"
import { useAppStore, useBasicInfoStore, useConfigStore } from "@/store"
import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"
import { useOpenWindow } from "@/hooks/open"
import type { IRankList } from "@/api/character/type"

export default defineComponent({
  setup() {
    const route = useRoute()
    const uid = (route.query.res as string) ?? ""
    const appStore = useAppStore()
    const configStore = useConfigStore()
    const basicStore = useBasicInfoStore()
    const openUrl = useOpenWindow()

    const ranks = asyncComputed<IRankList>(() => {
      if (window.pywebview) {
        return api.getRank(uid)
      }
      return JSON.parse(sessionStorage.getItem(uid) ?? "{}")
    }, {} as IRankList)

    const token = computed(() => {
      return ranks.value.token
    })

    watch(token, val => {
      configStore.$patch({ token: val })
      !basicStore.entry_list && basicStore.loadEntries()
      !basicStore.equipment_info && basicStore.loadEquips()
    })

    appStore.title = "排行数据(仅供参考)"

    const max = computed(() => {
      return ranks.value.rank[0][0][0]
    })

    onMounted(() => {
      window.removeLoading()
    })

    function equInfo(id: number) {
      return basicStore.equipment_list.filter(item => item.id == id)[0] ?? undefined
    }

    async function calc(ids: number[]) {
      ranks.value.setInfo.single_set = ids
      const saveData = await api.calc(
        {
          setInfo: ranks.value.setInfo
        },
        true
      )
      if (!window.pywebview) {
        saveData.forge_set = ranks.value.setInfo.forge_set
        saveData.merge_list = ranks.value.setInfo.merge
        saveData.fusion_list = ranks.value.setInfo.fusion_list as number[]
        saveData.customize = ranks.value.setInfo.customize
        saveData.specificity_list = ranks.value.setInfo.specificity_list
        saveData.equips = basicStore.equipment_list.filter(a => ranks.value.setInfo.single_set.includes(a.id)) ?? []
        sessionStorage.setItem(saveData.id?.toString() ?? "", JSON.stringify(saveData))
      }
      openUrl(`/result?res=${saveData.id}`, { width: 890, height: 650, scale: Math.max(Math.min((window.innerHeight * 0.85 / 750), (window.innerWidth * 0.9 / 1100)), 1), title: "请勿用于打桩排名等节奏" })
    }

    return () => (
      <>
        <div class="flex flex-col h-full m-0 rank">
          {renderList(ranks.value.rank, item => (
            <div class="item">
              {renderList(item[1], equ => (
                <EquipTips style={item[2].includes(equInfo(equ)?.part ?? "") ? "filter:grayscale(100%)" : ""} class="mr-5px" eq={equInfo(equ)} canClick={false} show-tips={false}></EquipTips>
              ))}
              <calc-button class="w-120px h-30px ml-20px" onClick={() => calc(item[1])}>
                {(item[0][0] / 1000000 > 1 ? item[0][0] / 1000000 : item[0][0]).toFixed(0)} | {((item[0][0] / max.value) * 100).toFixed(2)}%
              </calc-button>
            </div>
          ))}
        </div>
      </>
    )
  }
})
</script>

<style lang="scss" scoped>
  .rank {
    background-color: rgba(0, 0, 0, 0.75);
    overflow-y: auto;
    .item {
      text-shadow: none !important;
      height: 40px;
      line-height: 40px;
      display: flex;
      align-items: center;
      margin: 10px;

      :nth-child(3) {
        padding-left: 10px;
      }

      :nth-child(4) {
        padding-left: 10px;
      }

      :nth-child(9) {
        padding-left: 10px;
      }

      :nth-child(12) {
        padding-left: 10px;
      }
    }
  }
</style>
