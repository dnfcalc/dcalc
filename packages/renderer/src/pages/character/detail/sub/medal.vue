<script lang="tsx">
import { computed, defineComponent, renderList } from "vue"
import { useConfigStore } from "@/store"

export default defineComponent({
  name: "Special",
  setup() {
    const configStore = useConfigStore()
    const currentInfo = function<T>(name: string, defaultValue?: T) {
      return computed<string | number>({
        get() {
          return configStore.getForge("others", name) ?? defaultValue ?? 0
        },
        set(val) {
          configStore.setForge("others", name, val)
        }
      })
    }

    const quality_m = ["普通", "高级", "稀有", "神器", "传说", "史诗"]
    const quality_g = ["普通", "高级", "稀有", "神器", "传说"]

    const XZ_TYPE = currentInfo("XZ_TYPE")
    const XZ_disabled = computed(() => {
      return XZ_TYPE.value != 0
    })

    // 勋章品质
    const quality = currentInfo("medal_quality", 5)
    const lv = currentInfo("medal_lv", 12)
    const gems_1 = currentInfo("medal_gems_1", 4)
    const gems_2 = currentInfo("medal_gems_2", 4)
    const gems_3 = currentInfo("medal_gems_3", 4)
    const gems_4 = currentInfo("medal_gems_4", 4)

    // 勋章强化

    return () => (
      <div class="flex flex-wrap equ-profile">
        <div class="equ-profile-item">
          <div class="row-name">勋章</div>
          <calc-select disabled={XZ_disabled.value} v-model={quality.value} class="flex-1 !h-20px">
            {renderList(quality_m, (i, index) => (
              <calc-option value={index}>品质:{i}</calc-option>
            ))}
          </calc-select>
          <calc-select disabled={XZ_disabled.value} v-model={lv.value} class="flex-1 !h-20px">
            {renderList(13, i => (
              <calc-option value={i - 1}>强化:+{i - 1}</calc-option>
            ))}
          </calc-select>
        </div>
        <div class="equ-profile-item">
          <div class="row-name">宝石</div>
          <calc-select disabled={XZ_disabled.value} v-model={gems_1.value} class="flex-1 !h-20px">
            {renderList(quality_g, (k, index) => (
              <calc-option value={index}>宝石1:{k}</calc-option>
            ))}
          </calc-select>
          <calc-select disabled={XZ_disabled.value} v-model={gems_2.value} class="flex-1 !h-20px">
            {renderList(quality_g, (k, index) => (
              <calc-option value={index}>宝石2:{k}</calc-option>
            ))}
          </calc-select>
          <calc-select disabled={XZ_disabled.value} v-model={gems_3.value} class="flex-1 !h-20px">
            {renderList(quality_g, (k, index) => (
              <calc-option value={index}>宝石3:{k}</calc-option>
            ))}
          </calc-select>
          <calc-select disabled={XZ_disabled.value} v-model={gems_4.value} class="flex-1 !h-20px">
            {renderList(quality_g, (k, index) => (
              <calc-option value={index}>宝石4:{k}</calc-option>
            ))}
          </calc-select>
        </div>
      </div>
    )
  }
})
</script>
