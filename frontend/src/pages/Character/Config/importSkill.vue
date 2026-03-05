<script lang="tsx">
import { useAsyncState } from '@vueuse/core'
import { defineComponent, ref } from 'vue'
import api from '@/api'
import { useDialog } from '@/components/hooks/dialog'
import { isShow, onShow } from '@/components/hooks/show'
import { useConfigStore } from '@/stores'

export default defineComponent({
  setup() {
    const configStore = useConfigStore()
    const skillCode = ref('')

    const { state, execute, isLoading } = useAsyncState(
      async () => {
        const res = await api.getSkillFromCode(skillCode.value)
        console.log(res)
        configStore.config.skills = res.skills
        const { alert } = useDialog()
        visible.value = false
        await alert({
          content: '导入成功',
        })
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
        skillCode.value = ''
        state.value = undefined
      },
      { immediate: true },
    )

    const visible = isShow()

    return () => {
      return (
        <>
          <div class="h-35 w-80 py-2 px-4 text-hex-e9c556">
            <div class="flex justify-around items-center">
              技能加点代码
              <calc-input class="!w-60" v-model={skillCode.value} />
            </div>
            <div>
              <p class="text-hex-e9c556/80">
                * 点击导入后会根据规则解析出技能加点、技能进化、技能强化
              </p>
              <p class="text-hex-e9c556/80">
                * 部分技能可能存在无法识别的情况，需要手动调整
              </p>
            </div>
            <div class="flex justify-around items-center">
              <calc-button onClick={execute} disabled={!skillCode.value || isLoading.value}>导入</calc-button>
              <calc-button onClick={() => (visible.value = false)}>取消</calc-button>
            </div>
          </div>
        </>
      )
    }
  },
})
</script>
