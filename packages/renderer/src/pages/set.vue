<script lang="tsx">
import { computed, defineComponent, renderList } from "vue"
import api from "@/api"
import { useDialog } from "@/components/hooks/dialog"
import { useGlobalStore } from "@/store"
export default defineComponent(async () => {
  const globalStore = useGlobalStore()
  const details = computed(() => globalStore.global_set_details)
  const { alert } = useDialog()
  function set() {
    return () => {
      if (window.pywebview) {
        api.saveGlobalSet(details.value as [number, number[]]).then(() => {
          // appStore._global_detail = details.value as [number, number[]]
          alert({
            content: "保存成功,请刷新页面!"
          })
        })
      } else {
        localStorage.setItem("dcalc/global", JSON.stringify(details.value))
        // alert({
        //   content: "保存成功,请刷新页面!"
        // })
        window.parent.postMessage("close", "*")
      }
    }
  }
  return () => (
    <div
      class="bg-cover bg-no-repeat h-100% pt-8 pb-8 pl-4 pr-4 flex flex-col justify-between"
      style={`background-image: url('${import.meta.env.BASE_URL}images/home.jpg');max-height: calc(100% - 4rem);background-size: 100% 100%;`}
    >
      <div class="flex flex-col set">
        {renderList(globalStore.global_set_info, (set, index: number) => {
          return (
            <>
              {(index != 0 || window.pywebview) && (
                <div class="item">
                  {index}.{set.remark}
                  <div class="ml-10px flex items-center">
                    <div class="w-100px">{set.name}</div>
                    <calc-select class="!h-20px !ml-10px" multiple={set.multi ?? false} v-model={details.value[index]}>
                      {renderList(set.items, item => (
                        <calc-option value={item.value}>{item.label}</calc-option>
                      ))}
                    </calc-select>
                  </div>
                </div>
              )}
            </>
          )
        })}
      </div>
      <div class="h-2rem w-100% flex justify-center items-center">
        <calc-button onClick={set()}>保存</calc-button>
      </div>
    </div>
  )
})
</script>

<style lang="scss">
  .set {
    color: rgba(190, 163, 71, 1);
    overflow-y: auto;

    .item {
      display: flex;
      padding-left: 20px;
      flex-direction: column;
      line-height: 30px;
    }
  }
</style>
