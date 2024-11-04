<script lang="tsx">
import { computed, defineComponent, inject, ref, renderList } from "vue"
import { useCharacterStore, useConfigStore } from "@/store"

export default defineComponent({
  name: "Que",
  components: {},
  setup() {
    const configStore = useConfigStore()
    const skills = computed(() => Array.from(new Set(configStore.skill_que.filter(a => (a.modes?.length ?? 0) > 0).map(a => a.name))))
    const cur_skill = ref("")

    const cur_skill_info = computed(() => configStore.skill_que.filter(a => a.name == cur_skill.value) ?? [])

    const characterStore = useCharacterStore()
    const dialogRef = inject("dialogRef", ref(null))
    const count = ref([0, 0, 0, 0, 0])

    const set_cur_skill_cont = () => {
      count.value = [0, 0, 0, 0, 0]
      ;(cur_skill_info.value[0]?.modes ?? []).forEach((mode, index) => {
        count.value[index] = cur_skill_info.value.filter(a => a.mode == mode)?.length
      })
    }
    const set_que = () => {
      const todo = [...count.value]
      const modes = cur_skill_info.value[0]?.modes ?? []
      const indexs = configStore.skill_que
        .map((s, i) => (s.name == cur_skill.value ? i : -1))
        .filter(i => i > -1)
        .sort((a, b) => a - b)
      let index = 0
      modes.forEach((a, b) => {
        while (todo[b] > 0) {
          configStore.skill_que[indexs[index]].mode = a
          index++
          todo[b]--
        }
      })
    }

    return () => (
      <div class="w-50 h-45 que">
        <div class="flex items-center justify-center w-100%">
            选择技能：
          <calc-iconselect onChange={set_cur_skill_cont} appendTo={dialogRef.value} emptyLabel="点击" columnNum={4} v-model={cur_skill.value}>
            {renderList(skills.value, (skill) => (
              <calc-option value={skill}>
                <div class={`character-icon-${characterStore.alter}-${skill.replace(/[().·，：]+/g, "")}`} />
              </calc-option>
            ))}
          </calc-iconselect>
        </div>
        <div class="h-25 overflow-y-auto mx-1 my-2">
          {renderList(cur_skill_info.value[0]?.modes ?? [], (item, count_index) => (
            <>
              <div class="w-100% flex h-6">
                <div class="w-40%">{item}</div>
                <div class="w-50%">
                  <calc-select v-model={count.value[count_index]} appendTo={dialogRef.value} class="!w-100%">
                    {renderList(cur_skill_info.value.length + 1 - count.value.reduce((total, value) => total + value) + count.value[count_index], index => (
                      <calc-option value={index - 1}>{index - 1}次</calc-option>
                    ))}
                  </calc-select>
                </div>
              </div>
            </>
          ))}
        </div>
        <div class="flex w-100% items-center justify-center">
          <calc-button onClick={set_que}>确定</calc-button>
        </div>
      </div>
    )
  }
})
</script>

<style lang="scss">
  // .i-icon-select-dropdown {
  //   z-index: 1000 !important  ;
  // }
</style>
