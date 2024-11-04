<script lang="tsx">
import type { PropType } from "vue";
import { computed, defineComponent, reactive, renderList, renderSlot, watch } from "vue"
import type { IEquipmentInfo } from "@/api/info/type"
import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"

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
    // 需要高亮的
    highlight: {
      type: Array as PropType<ID[]>,
      default: () => []
    },
    // 是不是有筛选
    showHighlight: {
      type: Boolean,
      default: false
    },
    showTips: {
      type: Boolean,
      default: true
    },
    withTitle: {
      type: Boolean,
      default: true
    }
  },

  setup(props, { emit, slots }) {
    const selected = reactive<ID[]>(props.selected)

    watch(props.selected, () => {
      selected.splice(0, selected.length, ...props.selected)
    })


    const highlightSelectedCount = computed(() => {
      return selected.filter(item => props.highlight.includes(item)).length
    })

    function selectAll() {
      const new_arr = props.showHighlight
        ? highlightSelectedCount.value > props.highlight.length / 2
          ? selected.filter(item => !props.highlight.includes(item))
          : Array.from([...selected, ...props.highlight])
        : selected.length > props.list.length / 2
          ? []
          : props.list.map(item => item.id)
      selected.splice(0, selected.length, ...new_arr)
      props.showHighlight ?? emit("update:highlight", [])
      emit("update:selected", selected)
    }

    function changeState(id: ID) {
      return () => {
        if (selected.includes(id)) {
          selected.splice(selected.indexOf(id), 1)
        } else {
          selected.push(id)
        }
        emit("update:selected", selected)
      }
    }

    return () => {
      return (
        <div>
          {props.withTitle && (
            <div class="flex mb-1 w-full items-center">
              {renderSlot(slots, "header")}
              <calc-button class="flex-1" onClick={selectAll}>
                {props.title}
              </calc-button>
            </div>
          )}
          <div class="flex flex-wrap w-full">
            {renderList(props.list, equ => (
              <EquipTips
                class="item"
                eq={equ}
                canClick={true}
                showTips={props.showTips}
                active={selected.includes(equ.id)}
                hightlight={props.highlight.includes(equ.id)}
                onUpdate:active={changeState(equ.id)}
              ></EquipTips>
            ))}
          </div>
        </div>
      )
    }
  }
})
</script>
