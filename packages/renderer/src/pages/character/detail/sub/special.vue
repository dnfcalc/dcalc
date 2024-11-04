<script lang="tsx">
import { computed, defineComponent, renderList } from "vue"
import { useCharacterStore, useConfigStore } from "@/store"

export default defineComponent({
  name: "Special",
  setup() {
    const configStore = useConfigStore()
    const equipInfo = function<T>(part: string, name: string, defaultValue?: T) {
      return computed<string | number>({
        get() {
          return configStore.getForge(part, name) ?? defaultValue ?? 0
        },
        set(val) {
          if (val == undefined) {
            return
          }
          configStore.setForge(part, name, val)
        }
      })
    }

    // 副武器
    const second_weapon = equipInfo("副武器", "cursed_number")

    return () => (
      <div class="flex flex-wrap equ-profile">
        <div class="equ-profile-item">
          <div class="row-name">副武器</div>
          <calc-select disabled={useCharacterStore().alter != "vegabond"} v-model={second_weapon.value} class="flex-1 !h-20px">
            {renderList(32, i => (
              <calc-option value={i - 1}>{i - 1}</calc-option>
            ))}
          </calc-select>
        </div>
      </div>
    )
  }
})
</script>
