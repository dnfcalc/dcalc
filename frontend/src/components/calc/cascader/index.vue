<script lang="tsx">
import { selectionListEmits, selectionListProps } from "hoci"
import type { CSSProperties, PropType } from "vue";
import { Teleport, Transition, computed, defineComponent, onDeactivated, ref, watch } from "vue"

import { onClickOutside, useVModel } from "@vueuse/core"
interface ICascaderItem {
  label: string
  id?: string | number
  value?: any
  children?: ICascaderItem[]
  onSelect?: () => void
}

export default defineComponent({
  name: "ICascader",
  props: {
    ...selectionListProps,
    disabled: {
      type: Boolean,
      default: false
    },
    width: {
      type: Number,
      default: 120
    },
    emptyLabel: {
      type: String
    },
    highlight: {
      type: String,
      // warn remind
      default: ""
    },
    items: {
      type: Array as PropType<ICascaderItem[]>,
      default: () => []
    }
  },
  emits: [...selectionListEmits, "select"],
  setup(props, { emit }) {
    const modelValue = useVModel(props, "modelValue")

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
          width: `${dropdownPosition.value.w}px`
        }
      } else {
        return {
          left: `${dropdownPosition.value.x}px`,
          bottom: `${dropdownPosition.value.z}px`,
          width: `${dropdownPosition.value.w}px`
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
            z: 0
          }
        } else {
          dropdownPosition.value = {
            w: width,
            x: left,
            z: window.innerHeight - top + 2,
            y: 0
          }
        }
      }
    }


    window.addEventListener("resize", onResize)
    window.addEventListener("scroll", onResize)

    onDeactivated(() => {
      window.removeEventListener("resize", onResize)
      window.removeEventListener("scroll", onResize)
    })

    const selectItem = ref<ICascaderItem>()

    function onSelect(item: ICascaderItem) {
      if (!item.children?.length) {
        isOpen.value = false
      }
      selectItem.value = item
      emit("select", item.value)
    }

    function loadNode(item: ICascaderItem) {
      const value = props.modelValue ?? props.defaultValue
      if ((selectItem.value == null || selectItem.value == undefined) && value == item.value) {
        selectItem.value = item
      }
    }

    onClickOutside(triggerRef, () => (isOpen.value = false), { ignore: [dropdownRef] })

    return () => {
      return (
        <div class={["min-w-20 w-40 i-cascader"].concat(props.highlight)} onClick={collapse} ref={selectRef}>
          <div
            class={{
              "i-cascader-trigger": true,
              "disabled": props.disabled
            }}
            ref={triggerRef}
          >
            <span class="i-cascader-label">{selectItem.value?.label}</span>
            <calc-button icon="dropdown"></calc-button>
          </div>
          <Teleport to="body">
            <Transition name="dropdown" mode="out-in">
              <calc-tree
                {...props}
                v-model={modelValue.value}
                class="py-1 i-cascader-dropdown"
                style={dropdownStyle.value}
                v-show={isOpen.value}
                ref={dropdownRef}
                onLoad={loadNode}
                onSelect={onSelect}
                data={props.items}
              />
            </Transition>
          </Teleport>
        </div>
      )
    }
  }
})
</script>

<style lang="scss">
$text-color: #937639;
  .i-cascader {
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

    .i-cascader-trigger {
      padding: 0;
      display: flex;
      height: 100%;
      opacity: 0.9;

      justify-content: space-between;
      align-items: center;

      .i-cascader-label {
        padding-left: 5px;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
        max-width: calc(100% - 20px);
      }

      .i-cascader-down-icon {
        background-image: url("./img/select_down.png");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        border-radius: 2px;
        width: 15px;
        height: 14px;
      }

      .i-cascader-down-icon:active {
        background-image: url("./img/select_down_clicked.png");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
        border-radius: 2px;
        width: 15px;
        height: 14px;
      }

      &.disabled {
        color: gray;

        .i-cascader-down-icon {
          background-image: url("./img/select_down_disabled.png");
        }
      }
    }

    .i-cascader-trigger:hover {
      opacity: 1;
    }
  }

  .remind {
    color: #32e432 !important;
    border: 1px solid #aa8651;
  }

  .i-cascader-dropdown {
    position: fixed;
    max-height: 160px;
    overflow-y: auto;
    overflow-x: hidden;
    background: black;
    // font-size: 12px;
    z-index: 888;

    $hoverColor: #002947;
    $activeColor: lighten($hoverColor, 5%);
    color: $text-color;
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
