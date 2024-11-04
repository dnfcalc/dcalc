<script lang="tsx">
import { computed, defineComponent, onMounted, reactive, ref } from "vue"
import api from "@/api"
import { useDialog } from "@/components/hooks/dialog"
import { useOpenWindow } from "@/hooks/open"
import { format_bytes } from "@/utils"
import { sleep } from "@/utils/sync"

export default defineComponent({
  setup() {
    const { alert, show } = useDialog()
    const openUrl = useOpenWindow()
    const updateData = reactive({ current: 0, total: 0 })

    const isComplete = ref(false)
    const visible = ref(false)

    const progress = computed(() => {
      if (updateData.current == 0) {
        return 0
      }
      return (updateData.current / updateData.total) * 100
    })

    function complete() {
      visible.value = false
      if (window.pywebview) {
        window.pywebview.api.invoke("restart")
      } else {
        api.restart()
      }
    }

    onMounted(async () => {
      // if (window.pywebview && !import.meta.env.DEV) {
      if (window.pywebview && !import.meta.env.DEV) {
        try {
          if (!(await api.checkUpdate(APP_VERSION))) {
            return
          }
          const res = await show({
            content: (
              <div class="text-left w-full px-4 justify-center">
                检测到更新，是否自动更新？
                <br />
                自动更新将在下次启动时生效。
              </div>
            ),
            rejectButton: "手动更新",
            okButton: "自动更新",
            cancelButton: "取消"
          })
          if (res.isReject) {
            openUrl("https://wwn.lanzout.com/s/dcalc")
          } else if (res.isOk) {
            await autoUpdate()
          }
        } catch (err) {
          console.error(err)
          await alert({
            content: "自动检查更新错误,请手动检查更新"
          })
        }
      }
    })

    async function autoUpdate() {
      isComplete.value = false
      visible.value = true
      api.autoUpdate().then(() => (isComplete.value = true))
      let checkTimer: NodeJS.Timeout
      let stopCheck = false
      const fn = async () => {
        if (stopCheck) {
          return
        }
        const [current, total] = await api.getUpdateProgress()
        updateData.current = current
        updateData.total = total

        if (current == 0 || current < total) {
          await sleep(200)
          await fn()
        } else {
          stopCheck = true
          clearTimeout(checkTimer)
        }
      }
      checkTimer = setTimeout(() => {
        if (updateData.current == 0) {
          stopCheck = true
          alert({ content: "自动更新失败,请手动完成更新" })
        }
      }, 10 * 1000)
      await fn()
    }

    return () => {
      return (
        <calc-dialog close-button={false} header="自动更新" visible={visible.value}>
          <div class="flex flex-col py-2 px-4 items-center justify-center">
            <calc-progress value={updateData.current} total={updateData.total} class="w-40"></calc-progress>
            <div class="flex my-1 text-white w-40 justify-between">
              <div>
                {format_bytes(updateData.current)} / {format_bytes(updateData.total)}
              </div>
              <div> {progress.value.toFixed(2)}%</div>
            </div>
            <calc-button onClick={complete} disabled={!isComplete.value}>
              {!isComplete.value ? "更新中" : "完成"}
            </calc-button>
          </div>
        </calc-dialog>
      )
    }
  }
})
</script>

<style></style>
