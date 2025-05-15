<script lang="tsx">
import { selectionEmits, selectionProps, useSelectionList } from 'hoci'
import type { CSSProperties, PropType, RendererElement } from 'vue'
import {
  Teleport,
  Transition,
  computed,
  defineComponent,
  onDeactivated,
  ref,
  renderSlot,
  watch,
} from 'vue'

import { onClickOutside } from '@vueuse/core'

export default defineComponent({
  name: 'IIconselect',
  props: {
    ...selectionProps,
    disabled: {
      type: Boolean,
      default: false,
    },
    width: {
      type: Number,
      default: 28,
    },
    emptyLabel: {
      type: String,
    },
    columnNum: {
      type: Number,
      default: 1,
    },
    appendTo: {
      type: [Object, String] as PropType<string | RendererElement | null | undefined>,
      default: 'body',
    },
  },
  emits: selectionEmits,
  setup(props, context) {
    // props.itemClass = "i-select-dropdown-item"
    // const { active } = useSelectionList({ ...props, itemClass: "i-select-dropdown-item" }, context)
    const { renderItem } = useSelectionList(() => {
      return {
        ...props,
        itemClass: 'i-option',
        activeClass: 'active',
        unactiveClass: 'unactive',
      }
    }, context)

    // const { active } = useSelectionList(props, context)
    const columnNum = computed(() => props.columnNum || 1)
    // console.log({ ...props })

    const isOpen = ref(false)
    const triggerRef = ref<HTMLElement>()

    watch(isOpen, onResize)

    const appendToRef = computed(() => {
      return props.appendTo || 'body'
    })

    function collapse() {
      isOpen.value = !isOpen.value && !props.disabled
    }

    // 下拉框位置
    const dropdownPosition = ref({ x: 0, y: 0, w: 0 })
    // 下拉框位置
    const dropdownStyle = computed<CSSProperties>(() => {
      return {
        left: `${dropdownPosition.value.x}px`,
        top: `${dropdownPosition.value.y}px`,
        width: `${columnNum.value * 32 + 11}px`,
      }
    })

    function onResize() {
      if (triggerRef.value) {
        const { width, height, left, top } = triggerRef.value.getBoundingClientRect()
        dropdownPosition.value = {
          w: width,
          x: left - 2,
          y: top + height + 2,
        }
      }
    }

    onClickOutside(triggerRef, () => (isOpen.value = false))

    window.addEventListener('resize', onResize)
    window.addEventListener('scroll', onResize)

    onDeactivated(() => {
      window.removeEventListener('resize', onResize)
      window.removeEventListener('scroll', onResize)
    })

    const { slots } = context
    // console.log(active.value?.render())
    // console.log(active.value)
    // console.log(active.value?.render() ?? props.emptyLabel)

    return () => {
      return (
        <div class="i-icon-select" onClick={collapse}>
          <div
            class={{
              'i-select-trigger': true,
              disabled: props.disabled,
            }}
            ref={triggerRef}
          >
            <span class="i-select-label">{renderItem() ?? props.emptyLabel}</span>
          </div>
          <Teleport to={appendToRef.value}>
            <Transition name="dropdown" mode="out-in">
              <div class="i-icon-select-dropdown" style={dropdownStyle.value} v-show={isOpen.value}>
                {renderSlot(slots, 'default')}
              </div>
            </Transition>
          </Teleport>
        </div>
      )
    }
  },
})
</script>

<style lang="scss">
@use 'sass:color';
$text-color: #e9c556;
.i-icon-select {
  width: 28px;
  min-width: 28px;
  user-select: none;
  outline: none;
  height: 28px;
  line-height: 100%;
  // font-size: 12px;
  color: $text-color;
  background-color: rgba(0, 0, 0, 1);
  border: 1px solid #5b472a;
  border-radius: 2px;
  padding: 0;
  margin: 0;
  display: block;

  .i-select-trigger {
    padding: 0;
    display: flex;
    height: 100%;
    opacity: 1;

    justify-content: center;
    align-items: center;

    &.disabled {
      color: gray;
    }
  }

  .i-select-trigger:hover {
    opacity: 1;
  }
}

.i-icon-select-dropdown {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  position: fixed;
  overflow-y: auto;
  overflow-x: hidden;
  max-height: 480px;
  // background: rgba(255, 255, 255, 0.1);
  // font-size: 12px;
  z-index: 888;
  min-height: 28px;

  $hoverColor: #002947;
  $activeColor: color.scale($hoverColor, $lightness: 5%);
  color: $text-color;

  .i-option {
    // font-size: 12px;
    height: 28px;
    line-height: 28px;
    margin: 1px;
    border: none;
    outline: none;
    appearance: none;
    display: block;
    overflow: hidden;
    border: gray 1px solid;

    // &.active {
    //     background-color: $activeColor;
    // }

    &.active::before {
      content: '';
      width: 28px;
      height: 28px;
      position: absolute;
      background-image: url('/src/assets/img/control/item_checked.png');
      background-size: 80% 80%;
      background-repeat: no-repeat;
      background-position: center;
      z-index: 6;
    }

    &:hover:not(.active) ::before {
      content: '';
      width: 28px;
      height: 28px;
      position: absolute;
      background-image: url('@/assets/img/control/item_hover.png');
      background-size: 100% 100%;
      z-index: 6;
    }
  }
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
