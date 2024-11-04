<script lang="tsx">
import { computed, defineComponent, renderList } from "vue"
import type { IJadeInfo } from "@/api/info/type"
import { useBasicInfoStore, useConfigStore } from "@/store"
import { getFloat } from "@/utils"

export default defineComponent({
  name: "Jade",
  setup() {
    const basicInfoStore = useBasicInfoStore()
    const configStore = useConfigStore()

    const currentInfo = function<T>(name: string, defaultValue?: T) {
      return computed<string | number>({
        get() {
          return configStore.getForge("jade", name) ?? defaultValue ?? 0
        },
        set(val) {
          configStore.setForge("jade", name, val)
        }
      })
    }

    const valueList = computed(() => {
      return function (id: number = -1) {
        if (id == -1) {
          return undefined
        } else {
          const res = []
          const cur = basicInfoStore.details?.jade?.find(e => e.id == id) as IJadeInfo
          if (cur) {
            const { max, min, unit, pre } = cur
            //
            if (pre == 0) {
              res.push({
                id: 1,
                value: unit
              })
            } else {
              for (let i = Number(max) as number; i >= Number(min);) {
                if (i != 0) {
                  res.push({
                    id: getFloat(i, 1),
                    value: (i > 0 ? "+" : "") + getFloat(i, 1) + unit
                  })
                }
                i = Number((i - Number(pre)).toFixed(1))
              }
            }
            return res
          }
        }
      }
    })

    // 辟邪玉
    const jade_First_type = currentInfo("jade_First_type", 0)
    const jade_First_value = currentInfo("jade_First_value", 0)

    const jade_Second_type = currentInfo("jade_Second_type", 0)
    const jade_Second_value = currentInfo("jade_Second_value", 0)

    const jade_Third_type = currentInfo("jade_Third_type", 0)
    const jade_Third_value = currentInfo("jade_Third_value", 0)

    const jade_Fourth_type = currentInfo("jade_Fourth_type", 0)
    const jade_Fourth_value = currentInfo("jade_Fourth_value", 0)
    return () => (
      <div>
        <div class="flex mt-5px">
          <calc-select v-model={jade_First_type.value} class="flex-1 !h-20px !mr-10px">
            <calc-option value={0}>无</calc-option>
            {renderList(basicInfoStore.details?.jade ?? [], item => (
              <calc-option value={item.id}>{item.props}</calc-option>
            ))}
          </calc-select>

          <calc-select v-model={jade_First_value.value} class="flex-1 !h-20px">
            {renderList(valueList.value(Number(jade_First_type.value)) ?? [], item => (
              <calc-option value={item.id}>{item.value}</calc-option>
            ))}
          </calc-select>
        </div>
        <div class="flex mt-5px">
          <calc-select v-model={jade_Second_type.value} class="flex-1 !h-20px !mr-10px">
            <calc-option value={0}>无</calc-option>
            {renderList(basicInfoStore.details?.jade ?? [], item => (
              <calc-option value={item.id}>{item.props}</calc-option>
            ))}
          </calc-select>

          <calc-select v-model={jade_Second_value.value} class="flex-1 !h-20px">
            {renderList(valueList.value(Number(jade_Second_type.value)) ?? [], item => (
              <calc-option value={item.id}>{item.value}</calc-option>
            ))}
          </calc-select>
        </div>

        <div class="flex mt-5px">
          <calc-select v-model={jade_Third_type.value} class="flex-1 !h-20px !mr-10px">
            <calc-option value={0}>无</calc-option>
            {renderList(basicInfoStore.details?.jade ?? [], item => (
              <calc-option value={item.id}>{item.props}</calc-option>
            ))}
          </calc-select>

          <calc-select v-model={jade_Third_value.value} class="flex-1 !h-20px">
            {renderList(valueList.value(Number(jade_Third_type.value)) ?? [], item => (
              <calc-option value={item.id}>{item.value}</calc-option>
            ))}
          </calc-select>
        </div>

        <div class="flex mt-5px">
          <calc-select v-model={jade_Fourth_type.value} class="flex-1 !h-20px !mr-10px">
            <calc-option value={0}>无</calc-option>
            {renderList(basicInfoStore.details?.jade ?? [], item => (
              <calc-option value={item.id}>{item.props}</calc-option>
            ))}
          </calc-select>

          <calc-select v-model={jade_Fourth_value.value} class="flex-1 !h-20px">
            {renderList(valueList.value(Number(jade_Fourth_type.value)) ?? [], item => (
              <calc-option value={item.id}>{item.value}</calc-option>
            ))}
          </calc-select>
        </div>
      </div>
    )
  }
})
</script>
