<script lang="tsx">
import { defineComponent, renderList } from "vue"
import { useCharacterStore, useConfigStore } from "@/store"
export default defineComponent({
  name: "Cp",
  components: {},
  setup() {
    const characterStore = useCharacterStore()
    const configStore = useConfigStore()
    return () => (
      <div class="flex flex-col ml-20px">
        {renderList(characterStore.char_optiopns, (item, index) => (
          <div class="flex items-center mb-10px">
            <div class="w-150px">{item.name}</div>
            <calc-select class="!h-20px" v-model={configStore.individuation[index]}>
              {renderList(item.option, (option, count) => (
                <calc-option value={count}>{option}</calc-option>
              ))}
            </calc-select>
          </div>
        ))}
      </div>
    )
  }
})
</script>
