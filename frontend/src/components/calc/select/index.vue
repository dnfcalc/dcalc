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
  renderList,
  renderSlot,
  watch,
} from 'vue'

import { onClickOutside, useVModel } from '@vueuse/core'
import { classPropType, labelPropType } from '@/components/hooks/types'

export default defineComponent({
  name: 'ISelect',
  props: {
    ...selectionProps,
    disabled: {
      type: Boolean,
      default: false,
    },
    width: {
      type: Number,
      default: 120,
    },
    emptyLabel: {
      type: labelPropType,
    },
    highlight: {
      type: String,
      // warn remind
      default: '',
    },
    labelClass: {
      type: String,
      default: '',
    },
    inputClass: {
      type: classPropType,
      default: '',
    },
    appendTo: {
      type: [Object, String] as PropType<string | RendererElement | null | undefined>,
      default() {
        return 'body'
      },
    },
  },
  emits: [...selectionEmits],
  setup(props, context) {
    const modelValue = useVModel(props, 'modelValue', context.emit, { passive: true })

    const { renderItem } = useSelectionList(() => {
      return {
        ...props,
        modelValue: modelValue.value,
        itemClass: 'i-select-dropdown-item',
        activeClass: 'active',
        unactiveClass: 'unactive',
      }
    }, context)

    const isOpen = ref(false)
    const triggerRef = ref<HTMLElement>()
    const selectRef = ref<HTMLElement>()
    const dropdownRef = ref<HTMLElement>()

    watch(isOpen, onResize)

    function collapse() {
      isOpen.value = !isOpen.value && !props.disabled
    }

    // 下拉框位置
    const dropdownPosition = ref({ x: 0, y: 0, w: 0, z: 0 })
    // 下拉框位置
    const dropdownStyle = computed<CSSProperties>(() => {
      if (dropdownPosition.value.z == 0) {
        return {
          left: `${dropdownPosition.value.x}px`,
          top: `${dropdownPosition.value.y}px`,
          width: `${dropdownPosition.value.w}px`,
        }
      } else {
        return {
          left: `${dropdownPosition.value.x}px`,
          bottom: `${dropdownPosition.value.z}px`,
          width: `${dropdownPosition.value.w}px`,
        }
      }
    })

    function onResize() {
      if (triggerRef.value) {
        const { width, height, left, top } = triggerRef.value.getBoundingClientRect()
        if (window.innerHeight - top > 160) {
          dropdownPosition.value = {
            w: width,
            x: left,
            y: top + height + 2,
            z: 0,
          }
        } else {
          dropdownPosition.value = {
            w: width,
            x: left,
            z: window.innerHeight - top + 2,
            y: 0,
          }
        }
      }
    }

    const appendToRef = computed(() => {
      return props.appendTo || 'body'
    })

    onClickOutside(triggerRef, () => (isOpen.value = false))

    window.addEventListener('resize', onResize)
    window.addEventListener('scroll', onResize)

    onDeactivated(() => {
      window.removeEventListener('resize', onResize)
      window.removeEventListener('scroll', onResize)
    })

    const { slots } = context

    function renderLabel() {
      const children = renderItem()
      if (children) {
        if (!Array.isArray(children)) {
          return <span class={['i-select-input'].concat(props.inputClass)}>{children}</span>
        } else if (children.length > 0) {
          return (
            <span class={['i-select-input space-x-1'].concat(props.inputClass)}>
              {renderList(children, (item) => (
                <span>{item}</span>
              ))}
            </span>
          )
        }
      }
      const emptyLabel =
        typeof props.emptyLabel == 'function' ? props.emptyLabel() : props.emptyLabel
      return <span class="w-full pl-2 i-select-input i-select-empty-label">{emptyLabel}</span>
    }

    return () => {
      return (
        <div
          class={['min-w-20 w-40 i-select '].concat(props.highlight)}
          onClick={collapse}
          ref={selectRef}
        >
          <div
            class={{
              'i-select-trigger': true,
              disabled: props.disabled,
            }}
            ref={triggerRef}
          >
            {renderLabel()}
            <calc-button
              disabled={props.disabled}
              icon="dropdown"
              class="cursor-pointer"
            ></calc-button>
          </div>
          <Teleport to={appendToRef.value}>
            <Transition name="dropdown" mode="out-in">
              <div
                class="i-select-dropdown"
                style={dropdownStyle.value}
                v-show={isOpen.value}
                ref={dropdownRef}
              >
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
$text-color: #937639;
.i-select {
  min-width: 80px;
  width: 160px;
  user-select: none;
  outline: none;
  height: 16px;
  min-height: 16px;
  line-height: 100%;
  // font-size: 12px;
  color: $text-color;
  background-color: rgba(0, 0, 0, 1);
  border: 1px solid #5b472a;
  border-radius: 2px;
  padding: 0;
  padding-right: 3px;
  margin: 0;
  display: block;

  .i-select-trigger {
    padding: 0;
    display: flex;
    height: 100%;

    justify-content: space-between;
    align-items: center;

    .i-select-input {
      padding-left: 8px;
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
      max-width: calc(100% - 20px);
    }

    .i-select-empty-label {
      color: #5e5e5e;
    }

    &:hover {
      .i-select-empty-label {
        color: #757575;
      }
    }

    &.disabled {
      color: gray;
    }
  }

  .i-select-trigger:hover {
    opacity: 1;
  }
}

.warn {
  color: red !important;
  border: 1px solid #aa8651;
}

.remind {
  color: #32e432 !important;
  border: 1px solid #aa8651;
}

.i-select-dropdown {
  position: fixed;
  max-height: 160px;
  overflow-y: auto;
  background: black;
  // font-size: 12px;
  z-index: 888;

  $hoverColor: #002947;
  $activeColor: color.scale($hoverColor, $lightness: 5%);
  color: $text-color;

  .i-select-dropdown-item {
    // font-size: 12px;
    height: 20px;
    line-height: 20px;
    margin: 0;
    padding: 0 5px;
    border: none;
    outline: none;
    appearance: none;
    display: block;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;

    &.active {
      // background-color: $activeColor;
      color: #e9c556;
    }
    &.active::after {
      content: '✓';
      position: absolute;
      right: 5px;
    }

    &:hover:not(.active) {
      // font-size: 12px;
      background-color: $hoverColor;
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
