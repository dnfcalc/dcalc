<script lang="tsx">
import { useAsyncState, useDebounceFn } from "@vueuse/core"
import { computed, defineComponent, reactive, ref, renderList } from "vue"
import type { IRecommendInfo, IRecommendRequest } from "@/api/info/type"
import { useDialog } from "@/components/hooks/dialog"
import { isShow, onShow } from "@/components/hooks/show"
import EqIconVue from "@/components/internal/equip/eq-icon.vue"
import ProfileVue from "@/components/internal/profile/equipments.vue"
import { useBasicInfoStore, useCharacterStore, useConfigStore, useGlobalStore } from "@/store"
export default defineComponent({
  setup() {
    const globalStore = useGlobalStore()
    const characterStore = useCharacterStore()
    const configStore = useConfigStore()
    const basicStore = useBasicInfoStore()

    const params = reactive<IRecommendRequest>({
      page: 1,
      size: 5,
      keyword: "",
      alter: characterStore.alter
    })

    const curEquList = computed(() => {
      return basicStore.equipment_list.filter(item => configStore.single_set.includes(item.id)).sort((a, b) => Number(a.id) - Number(b.id))
    })

    const { state, execute, isLoading } = useAsyncState(
      () => configStore.getFavorites(params),
      {
        data: [],
        pageIndex: 1,
        pageSize: 5,
        totalCount: 1
      },
      {
        resetOnExecute: false,
        immediate: false,
        onError: Promise.reject
      }
    )

    const visible = isShow()

    onShow(execute, { immediate: true })

    const totalPage = computed(() => Math.ceil(state.value.totalCount / params.size))

    function apply(item: IRecommendInfo) {
      return () => {
        configStore.importSingle(item.equips.map(r => Number.parseInt(r.id?.toString() ?? "0")).sort())
        configStore.fusion_list = item.fusion ?? []
        !Array.isArray(item.specificity) && (configStore.specificity = item.specificity ?? {})
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
        visible.value = false
      }
    }

    function remove(id: ID) {
      return async () => {
        await configStore.deleteFavorite(id)
        await execute()
      }
    }

    const onPageChange = useDebounceFn(() => execute(), 200)

    const { alert } = useDialog()

    const name = ref("")

    async function add() {
      if (!name.value) {
        await alert({
          content: "请输入搭配名称"
        })
        return
      }
      params.keyword = ""
      await execute()
      // for (let i = 0; i < state.value.totalCount; i++) {
      //   if (
      //     state.value.data[i].equips
      //       .map(a => a.id)
      //       .sort()
      //       .join("-") == configStore.single_set.sort().join("-")
      //   ) {
      //     await alert({
      //       content: "已存在相同的收藏"
      //     })
      //     return
      //   }
      // }
      await configStore.addFavorite(name.value)
      await execute()
    }

    return () => {
      return (
        <div class="h-137 py-2 px-8 text-hex-e9c556 duration-200 overflow-y-auto">
          <div class="flex py-4">
            <div>
              <div class="flex space-x-4 mb-4 w-full box-border items-center">
                <calc-autocomplete class="flex-1" placeholder="输入关键字搜索流派搭配" v-model={params.keyword}></calc-autocomplete>
                <calc-button onClick={execute}>搜索</calc-button>
              </div>
              <calc-loading class="space-y-2 h-108 w-101" loading={isLoading.value}>
                {renderList(state.value.data, item => {
                  return (
                    <div>
                      <div class="flex h-12 text-sm leading-12 items-center justify-between">
                        <span>{item.name}</span>
                        <div class="flex space-x-2">
                          <calc-button onClick={remove(item.id)}>删除</calc-button>
                          <calc-button onClick={apply(item)}>应用</calc-button>
                        </div>
                      </div>
                      <div class="flex space-x-1 w-full items-center ">
                        {renderList(item.equips.slice(0, 12), eq => {
                          return <EqIconVue eid={eq.id}></EqIconVue>
                        })}
                      </div>
                    </div>
                  )
                })}
              </calc-loading>
              <calc-pagination disabled={!visible.value} class="h-8" v-model:page={params.page} onChange={onPageChange} totalPage={totalPage.value}></calc-pagination>
            </div>
            <div class="bg-hex-5b472a h-128 mx-6 w-1px"></div>
            <div>
              <ProfileVue
                class="!p-0"
                fusionList={configStore.fusion_list}
                equ-list={curEquList.value}

                showZF={false}
                tipInfo={globalStore.global_set_details[3] as number[]}
              ></ProfileVue>
              <div class="h-8 leading-8">搭配名称</div>
              <calc-input v-model={name.value} placeholder="请输入搭配名称"></calc-input>
              <calc-button onClick={add} class="my-4">
                  保存
              </calc-button>
            </div>
          </div>
        </div>
      )
    }
  }
})
</script>
