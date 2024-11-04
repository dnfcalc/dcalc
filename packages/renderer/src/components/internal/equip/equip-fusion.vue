<script lang="tsx">
import type { PropType } from "vue"
import { defineComponent, reactive, renderList, renderSlot, watch } from "vue"
import type { IEquipmentInfo } from "@/api/info/type"
import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"
import { useBasicInfoStore } from "@/store"

export default defineComponent({
  components: { EquipTips },
  props: {
    // 展示列表
    list: {
      type: Array as PropType<IEquipmentInfo[]>,
      default: () => []
    },
    // 按钮名称
    title: {
      type: String,
      default: ""
    },
    // 选中列表
    selected: {
      type: Array as PropType<ID[]>,
      default: () => []
    },
    showTips: {
      type: Boolean,
      default: true
    },
    colNumber: {
      type: Number,
      default: 5
    }
  },

  setup(props, { emit, slots }) {
    const selected = reactive<ID[]>(props.selected)
    const basicStore = useBasicInfoStore()

    watch(props.selected, () => {
      selected.splice(0, selected.length, ...props.selected)
    })

    // const isSelectAll = computed(() => {
    //   const len = props.highlight.length || props.list.length
    //   return selected.length === len
    // })

    function changeState(id: ID) {
      return () => {
        // 二次点击
        if (selected.includes(id)) {
          selected.splice(selected.indexOf(id), 1)
        } else {
          // 移除同部位
          const cur_position = basicStore.equipment_info?.fusion.filter(a => a.id == id)?.[0].part
          const to_remove = basicStore.equipment_info?.fusion.filter(item => item.part == cur_position) ?? []
          to_remove.forEach(a => {
            if (selected.includes(a.id)) {
              selected.splice(selected.indexOf(a.id), 1)
            }
          })
          selected.push(id)
        }
        emit("update:selected", selected)
      }
    }

    return () => {
      return (
        <div>
          <div class="flex mb-1 w-full items-center">
            {renderSlot(slots, "header")}
            <calc-button class="flex-1">{props.title}</calc-button>
          </div>
          <div class="flex flex-wrap w-full">
            {renderList(props.list.length / props.colNumber, col => {
              return renderList(props.colNumber, index => {
                const cur = props.list[col - 1 + (index - 1) * (props.list.length / props.colNumber)]
                return <EquipTips class="item" eq={cur} canClick={true} showTips={props.showTips} active={selected.includes(cur.id)} onUpdate:active={changeState(cur.id)}></EquipTips>
              })
            })}
          </div>
        </div>
      )
    }
  }
})
</script>

<style lang="scss" scoped>
  .equ-fusion-sort {
    margin-top: 5px;
    display: flex;
    flex-wrap: wrap;
    align-content: flex-start;
    width: 210px;

    background-color: rgba(255, 255, 255, 0.1);

    .item {
      width: 30px;
      height: 36px;
      margin-left: 10px;
      display: flex;
      justify-content: center;
      align-items: center;
    }
  }
</style>
