<script lang="tsx">
import { HiSelection, selectionProps } from 'hoci'
import { useVModel } from '@vueuse/core'
import type { PropType } from 'vue'
import { computed, defineComponent, renderList, watch } from 'vue'
import CalcTreeNode from './node.vue'
import type { TreeNode } from './types'
import { labelPropType, valuePropType } from '@/components/hooks/types'

const Tree = defineComponent({
  name: 'CalcTree',
  props: {
    ...selectionProps,
    modelValue: {
      type: valuePropType,
      default: () => null,
    },
    activeItem: {
      type: Object as PropType<TreeNode>,
      default: () => null,
    },
    idKey: {
      type: String,
      default: 'id',
    },
    label: {
      type: labelPropType,
    },
    data: {
      type: Array as PropType<TreeNode[]>,
      default: () => [],
    },
    depth: {
      type: [Number, String] as PropType<number>,
      default: () => 0,
    },
    depthStyle: {
      type: Function as PropType<(depth: number) => string>,
    },
  },
  setup(props, { emit }) {
    const modelValue = useVModel(props, 'modelValue')

    function onSelect(item?: TreeNode) {
      if (item) {
        emit('select', item)
        item.onSelect?.()
      }
    }

    function loadItem(total: TreeNode[], items: TreeNode[]) {
      items?.forEach((item) => {
        if (item.children) {
          loadItem(total, item.children)
        }
        total.push(item)
      })
      return total
    }

    const children = computed(() => {
      return loadItem([], props.data)
    })

    watch(modelValue, (val) => {
      val = val ?? props.defaultValue
      const item = children.value.find((item) => item.value === val)
      onSelect(item)
    })

    return () => {
      return (
        <HiSelection
          {...props}
          activeClass="i-tree-node-active"
          v-model={modelValue.value}
          class="i-tree"
        >
          {renderList(props.data, (item) => {
            return (
              <CalcTreeNode
                {...item}
                onSelect={onSelect}
                depth-style={props.depthStyle}
                depth={props.depth}
              />
            )
          })}
        </HiSelection>
      )
    }
  },
})

export default Tree
</script>

<style>
.i-tree {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
</style>
