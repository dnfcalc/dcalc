<script lang="tsx">
import { defineComponent, renderList } from "vue"
import { useConfigStore } from "@/store"

export default defineComponent({
  name: "Special",
  setup() {
    const configStore = useConfigStore()
    const items = ["四维", "三攻", "技攻", "攻速", "攻击强化", "攻击强化百分比", "BUFF量", "BUFF量百分比", "火强", "光强", "冰强", "暗强", "火抗", "光抗", "冰抗", "暗抗", "出血抗性", "中毒抗性", "灼伤抗性", "感电抗性", "冰冻抗性", "减速抗性", "眩晕抗性", "诅咒抗性", "失明抗性", "石化抗性", "睡眠抗性", "混乱抗性", "束缚抗性", "技能范围Σ", "MP消耗量"]

    return () => (
      <div class="flex flex-wrap">
        {renderList(items, item => {
          return (
            <div class="w-25% flex items-center h-20px mt-5px mb-5px ">
              <div class="w-50% ml-5px mr-5px">{item.replace("百分比", "%")}</div>
              <calc-input
                onChange={() => (configStore.corrections[item] = configStore.corrections[item] == "" ? 0 : configStore.corrections[item])}
                type="number"
                v-model={configStore.corrections[item]}
                class="!min-w-10 !w-4%"
              />
            </div>
          )
        })}
      </div>
    )
  }
})
</script>
