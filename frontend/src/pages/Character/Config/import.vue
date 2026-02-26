<script lang="tsx">
import { useAsyncState } from '@vueuse/core'
import { computed, defineComponent, ref, renderList } from 'vue'
import api from '@/api'
import { useDialog } from '@/components/hooks/dialog'
import { isShow, onShow } from '@/components/hooks/show'
import { useConfigStore } from '@/stores'

export default defineComponent({
  setup() {
    const configStore = useConfigStore()
    const uid = ref('')

    const { state, execute } = useAsyncState(
      async () => {
        const res = await api.getConfigFromHelper(uid.value)
        configStore.config.equips = res.equips
        configStore.config.avatar = res.avatars
        await alert({
          content: '导入成功',
        })
        visible.value = false
        return res
      },
      undefined,
      {
        resetOnExecute: false,
        immediate: false,
        onError: Promise.reject,
      },
    )

    onShow(
      () => {
        uid.value = ''
        state.value = undefined
      },
      { immediate: true },
    )

    const visible = isShow()

    const configList = computed(() => {
      return Object.keys(state.value ?? {}).sort()
    })

    async function importConfigs() {
      // if (window.pywebview) {
      //   const configs = {}
      //   cacheList.value.forEach(key => {
      //     configs[key] = state.value?.[key]
      //   })
      //   await api.importConfigs(configs)
      // } else {
      //   cacheList.value.forEach(key => {
      //     localStorage.setItem(key, JSON.stringify(state.value?.[key]))
      //   })
      // }
      // const { alert } = useDialog()
      // await alert({
      //   content: "导入成功"
      // })
      // visible.value = false
      // await configStore.load()
    }

    return () => {
      return (
        <>
          <div class="h-40 w-80 py-2 px-4 text-hex-e9c556">
            <div class="flex justify-around items-center">
              助手社区ID
              <calc-input class="!w-60" v-model={uid.value} />
            </div>
            <div>
              <p class="text-hex-e9c556/80">
                * 请输入助手社区ID，点击导入后会从助手社区通过OCR获取主角色打造
              </p>
              <p class="text-hex-e9c556/80">
                * 由于通过文字识别，部分打造无法完全获取，此处仅做快捷导入
              </p>
            </div>
            <div class="flex justify-around items-center">
              <calc-button onClick={execute}>导入</calc-button>
              <calc-button onClick={() => (visible.value = false)}>取消</calc-button>
            </div>
          </div>
        </>
      )
    }
  },
})
</script>
