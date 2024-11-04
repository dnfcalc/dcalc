<script lang="tsx">
import { computed, defineComponent, renderList } from "vue"
import { useBasicInfoStore, useConfigStore } from "@/store"

export default defineComponent({
  name: "Petequ",
  setup() {
    const configStore = useConfigStore()
    const basicInfoStore = useBasicInfoStore()
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

    // 红
    const red = equipInfo("宠物装备-红", "enchanting")
    // 绿
    const green = equipInfo("宠物装备-绿", "enchanting")
    // 蓝
    const blue = equipInfo("宠物装备-蓝", "enchanting")

    return () => (
      <div class="flex flex-wrap equ-profile">
        <div class="equ-profile-item">
          <div class="row-name">红色</div>
          <calc-select v-model={red.value} class="flex-1 !h-20px">
            <calc-option value={0}>无</calc-option>
            {renderList(basicInfoStore.details?.enchanting?.filter(item => item.position.includes("宠物装备-红")) ?? [], item => (
              <calc-option value={item.id}>{item.props}</calc-option>
            ))}
          </calc-select>
        </div>
        <div class="equ-profile-item">
          <div class="row-name">绿色</div>
          <calc-select v-model={green.value} class="flex-1 !h-20px">
            <calc-option value={0}>无</calc-option>
            {renderList(basicInfoStore.details?.enchanting?.filter(item => item.position.includes("宠物装备-绿")) ?? [], item => (
              <calc-option value={item.id}>{item.props}</calc-option>
            ))}
          </calc-select>
        </div>
        <div class="equ-profile-item">
          <div class="row-name">蓝色</div>
          <calc-select v-model={blue.value} class="flex-1 !h-20px">
            <calc-option value={0}>无</calc-option>
            {renderList(basicInfoStore.details?.enchanting?.filter(item => item.position.includes("宠物装备-蓝")) ?? [], item => (
              <calc-option value={item.id}>{item.props}</calc-option>
            ))}
          </calc-select>
        </div>
      </div>
    )
  }
})
</script>
