<script lang="tsx">
import { useAsyncState, useClipboard } from "@vueuse/core"
import { computed, defineComponent, ref, renderList } from "vue"
import api from "@/api"
import { useDialog } from "@/components/hooks/dialog"
import { isShow, onShow } from "@/components/hooks/show"
import { useConfigStore } from "@/store"

export default defineComponent({
  setup() {
    const expire = ref(3)
    const cacheList = ref<string[]>([])
    const configStore = useConfigStore()
    const link = ref("")

    const { state, execute } = useAsyncState(
      async () => {
        const res = await configStore.getAllConfig()
        // 默认全选
        cacheList.value = Object.keys(res)
        link.value = ""
        return res
      },
      {},
      {
        resetOnExecute: false,
        immediate: false,
        onError: Promise.reject
      }
    )

    onShow(execute, { immediate: true })

    const visible = isShow()

    const configList = computed(() => {
      return Object.keys(state.value).sort()
    })

    async function share() {
      const infos = {}
      cacheList.value.forEach(key => {
        infos[key] = state.value[key]
      })
      link.value = await api.shareConfigs(infos, expire.value)
    }

    const { copy, isSupported } = useClipboard()
    const { alert } = useDialog()

    async function copyLink() {
      try {
        await copy(link.value)
        await alert({
          content: "拷贝成功"
        })
        visible.value = false
      } catch (e) {
        await alert({
          content: "系统不支持,请手动拷贝"
        })
      }
    }

    return () => {
      return link.value == "" ? (
        <>
          <div class="h-105 py-2 px-4 text-hex-e9c556 w-80">
            <div class="h-90  overflow-y-auto">
              <calc-checkbox-group v-model={cacheList.value}>
                {renderList(configList.value, item => (
                  <calc-checkbox value={item}>{item}</calc-checkbox>
                ))}
              </calc-checkbox-group>
            </div>
            <div class="flex h-30px justify-center items-center">
                存档分享时间：
              <calc-checkbox-group class="flex w-58 justify-around" multiple={false} v-model={expire.value}>
                <calc-checkbox value={3}>3小时</calc-checkbox>
                <calc-checkbox value={6}>6小时</calc-checkbox>
                <calc-checkbox value={12}>12小时</calc-checkbox>
                <calc-checkbox value={24}>24小时</calc-checkbox>
              </calc-checkbox-group>
            </div>
            <div class="flex py-5px justify-around items-center">
              <calc-button onClick={share}>确定</calc-button>
              <calc-button onClick={() => (visible.value = false)}>取消</calc-button>
            </div>
          </div>
        </>
      ) : (
        <>
          <div class="h-15 py-2 px-4 text-hex-e9c556 w-80">
            <div class="flex justify-around items-center">
                分享🐎
              <calc-input class="!w-65" readonly v-model={link.value} />
            </div>
            <div class="flex pt-10px justify-around items-center">
              <calc-button disabled={!isSupported} onClick={copyLink}>
                  拷贝
              </calc-button>
              <calc-button onClick={() => (visible.value = false)}>取消</calc-button>
            </div>
          </div>
        </>
      )
    }
  }
})
</script>
