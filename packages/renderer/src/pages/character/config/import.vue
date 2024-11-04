<script lang="tsx">
import { useAsyncState } from "@vueuse/core"
import { computed, defineComponent, ref, renderList } from "vue"
import api from "@/api"
import { useDialog } from "@/components/hooks/dialog"
import { isShow, onShow } from "@/components/hooks/show"
import { useConfigStore } from "@/store"

export default defineComponent({
  setup() {
    const cacheList = ref<string[]>([])
    const configStore = useConfigStore()
    const link = ref("")

    const { state, execute } = useAsyncState(
      async () => {
        const res = await api.getShareConfigs(link.value)
        // 默认全选
        cacheList.value = Object.keys(res)
        return res
      },
      undefined,
      {
        resetOnExecute: false,
        immediate: false,
        onError: Promise.reject
      }
    )

    onShow(
      () => {
        link.value = ""
        state.value = undefined
      },
      { immediate: true }
    )

    const visible = isShow()

    const configList = computed(() => {
      return Object.keys(state.value ?? {}).sort()
    })

    async function importConfigs() {
      if (window.pywebview) {
        const configs = {}
        cacheList.value.forEach(key => {
          configs[key] = state.value?.[key]
        })
        await api.importConfigs(configs)
      } else {
        cacheList.value.forEach(key => {
          localStorage.setItem(key, JSON.stringify(state.value?.[key]))
        })
      }
      const { alert } = useDialog()
      await alert({
        content: "导入成功"
      })
      visible.value = false
      await configStore.load()
    }

    return () => {
      return !state.value ? (
        <>
          <div class="h-15 w-80 py-2 px-4 text-hex-e9c556">
            <div class="flex justify-around items-center">
                分享🐎
              <calc-input class="!w-65" v-model={link.value} />
            </div>
            <div class="pt-10px flex justify-around items-center">
              <calc-button onClick={execute}>导入</calc-button>
              <calc-button onClick={() => (visible.value = false)}>取消</calc-button>
            </div>
          </div>
        </>
      ) : (
        <>
          {" "}
          <div class="h-100 w-80 py-2 px-4 text-hex-e9c556">
            <div class="h-90  overflow-y-auto">
              <calc-checkbox-group v-model={cacheList.value}>
                {renderList(configList.value, item => (
                  <calc-checkbox value={item}>{item}</calc-checkbox>
                ))}
              </calc-checkbox-group>
            </div>
            <div class="pt-10px flex justify-around items-center">
              <calc-button onClick={importConfigs}>确定</calc-button>
              <calc-button onClick={() => (visible.value = false)}>取消</calc-button>
            </div>
          </div>
        </>
      )
    }
  }
})
</script>
