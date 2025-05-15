<script lang="tsx">
import { HiItem } from 'hoci'
import type { PropType } from 'vue'
import { Transition, computed, defineComponent, ref, renderList } from 'vue'
import type { TreeNode } from './types'

const NTreeNode = defineComponent({
  props: {
    label: {
      type: String,
      default: '',
    },
    value: {
      type: [String, Number, Boolean, Object, Array] as PropType<any>,
      default: () => null,
    },
    children: {
      type: Array as PropType<TreeNode[]>,
      default: () => [],
    },
    depth: {
      type: [String, Number] as PropType<number>,
      default: 0,
    },
    depthStyle: {
      type: Function as PropType<(depth: number) => string>,
    },
    depthOffset: {
      type: String,
      default: '12px',
    },
  },
  setup(props, { emit }) {
    const isOpen = ref(false)

    function open() {
      isOpen.value = !isOpen.value
      onSelect(props)
    }

    function onSelect(item: TreeNode) {
      return emit('select', item)
    }

    const depthStyle = computed(() => {
      if (props.depthStyle) {
        return props.depthStyle(props.depth)
      }
      return `padding-left: calc(${props.depth}*${props.depthOffset} + 12px);`
    })

    return () => (
      <div class="w-full i-tree-item relative">
        <HiItem
          label={props.label}
          value={props.value}
          style={depthStyle.value}
          class="flex i-tree-item-label  items-center"
          onClick={open}
        >
          <div class="top-0 right-0 bottom-0 left-0 absolute i-tree-item-active-mask"></div>
          <div class="top-0 right-0 bottom-0 left-0 absolute i-tree-item-mask"></div>
          <calc-button
            v-show={props.children?.length}
            icon={isOpen.value ? 'collapse-up' : 'collapse-down'}
          ></calc-button>
          <div class="pl-1">{props.label}</div>
        </HiItem>
        <Transition name="dropdown" mode="out-in">
          <div v-show={isOpen.value}>
            {renderList(props.children, (item) => {
              return <NTreeNode onSelect={onSelect} {...item} depth={Number(props.depth) + 1} />
            })}
          </div>
        </Transition>
      </div>
    )
  },
})

export default NTreeNode
</script>

<style lang="scss">
.i-tree-item {
  display: flex;
  flex-direction: column;
  cursor: pointer;

  border: 1px solid transparent;
  background-color: black;
}

.i-tree-item-label {
  flex: 1;
  height: 16px;
  min-height: 16px;
  color: #ddc593;
  position: relative;
  &:hover {
    .i-tree-item-mask {
      background: url('./img/item_hover.png') no-repeat;
      background-size: 100% 100%;
    }
  }

  &.i-tree-node-active {
    .i-tree-item-active-mask {
      background: url('./img/item_active.png') no-repeat;
      background-size: 100% 100%;
    }
  }
}

.icon-collapse-up {
  background-image: url('./img/collapse_up.png');
  background-size: 100% 100%;
  background-repeat: no-repeat;
  background-position: center;
  min-width: 13px !important;
  width: 13px !important;
  height: 13px !important;
}

.icon-collapse-down {
  background-image: url('./img/collapse_down.png');
  background-size: 100% 100%;
  background-repeat: no-repeat;
  background-position: center;
  min-width: 13px !important;
  width: 13px !important;
  height: 13px !important;
}

.i-tree-dropdown {
  width: 100%;
  max-height: 0;
  overflow: hidden;
  background-color: #fff;
  border-radius: 0.5rem;
  box-shadow: 0 0 0.5rem 0 rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.dropdown-active {
  animation: dropdown-enter 0.2s ease-in;
}

.dropdown-active {
  animation: dropdown-leave 0.2s ease-in;
}

.dropdown-enter-active {
  animation: dropdown-enter 0.2s ease-in;
}

.dropdown-leave-active {
  animation: dropdown-leave 0.2s ease-in;
}

.dropdown-enter-active {
  animation: dropdown-enter 0.2s ease-in;
}

.dropdown-leave-active {
  animation: dropdown-leave 0.2s ease-in;
}
</style>
