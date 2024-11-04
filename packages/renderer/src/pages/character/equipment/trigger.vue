<script lang="tsx">
import { defineComponent, inject, ref, renderList } from "vue"
import { useBasicInfoStore, useConfigStore } from "@/store"


export default defineComponent({
  name: "Trigger",
  setup() {
    const basicStore = useBasicInfoStore()
    const configStore = useConfigStore()
    const dialogRef = inject("dialogRef", ref(null))

    return () => (
      <>
        <div class="equ-trigger !w-390px">
          {
            basicStore.trigger_list && renderList(basicStore.trigger_list ?? [], (trigger) => (
              <>
                {configStore.trigger_set[trigger.id] && trigger["multi-select"] ? (
                  <calc-select key={trigger.id} appendTo={dialogRef.value} emptyLabel={trigger.selectList?.[0]} multiple={trigger["multi-select"]} v-model={configStore.trigger_set[trigger.id]} class="ownSelect-2">
                    {renderList(trigger.selectList, (item, index) => (
                      <>{index > 0 && <calc-option value={index}>{item}</calc-option>}</>
                    ))}
                  </calc-select>
                ) : (
                  <calc-select key={trigger.id} appendTo={dialogRef.value} emptyLabel={trigger.selectList?.[0]} v-model={configStore.trigger_set[trigger.id][0]} class="ownSelect-2">
                    {renderList(trigger.selectList, (item, index) => (
                      <calc-option value={index}>{item}</calc-option>
                    ))}
                  </calc-select>
                )}
              </>
            ))
          }
        </div>
      </>)
  }
})
</script>

<style lang="scss">
  .equ-trigger {
    width: 400px;
    display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
  }

  .ownSelect-2 {
  height: 24px !important;
  width: calc(50% - 10px) !important;
  margin: 2px;
}
</style>
