<script lang="tsx">
import { debouncedWatch, onClickOutside, useVModel } from "@vueuse/core"
import type { CSSProperties, PropType } from "vue";
import { Teleport, Transition, computed, defineComponent, onDeactivated, ref, renderList, watch } from "vue"

  type HandleChangeFunction = (value: string | number) => string[] | Promise<string[]>

export default defineComponent({
  props: {
    modelValue: {
      type: [String, Number] as PropType<string | number>,
      default: () => ""
    },
    placeholder: {
      type: String,
      default: ""
    },
    handleChange: {
      type: Function as PropType<HandleChangeFunction>,
      default: () => () => []
    },
    delay: {
      type: Number,
      default: 300
    }
  },
  setup(props, { emit }) {
    const modelValue = useVModel(props, "modelValue")

    const isOpen = ref(false)
    const triggerRef = ref<HTMLElement>()

    watch(isOpen, onResize)

    // 下拉框位置
    const dropdownPosition = ref({ x: 0, y: 0, w: 0 })
    // 下拉框位置
    const dropdownStyle = computed<CSSProperties>(() => {
      return {
        left: `${dropdownPosition.value.x}px`,
        top: `${dropdownPosition.value.y}px`,
        width: `${dropdownPosition.value.w}px`
      }
    })

    function onResize() {
      if (triggerRef.value) {
        const { width, height, left, top } = triggerRef.value.getBoundingClientRect()
        dropdownPosition.value = {
          w: width,
          x: left,
          y: top + height + 2
        }
      }
    }

    onClickOutside(triggerRef, () => (isOpen.value = false))

    window.addEventListener("resize", onResize)
    window.addEventListener("scroll", onResize)

    onDeactivated(() => {
      window.removeEventListener("resize", onResize)
      window.removeEventListener("scroll", onResize)
    })

    function selectItem(item: string) {
      return () => {
        modelValue.value = item
      }
    }

    const delay = computed(() => props.delay)

    const droplist = ref<string[]>([])

    debouncedWatch(modelValue, async value => (droplist.value = await props.handleChange(value)), {
      debounce: delay
    })

    function handleInput() {
      isOpen.value = droplist.value.length > 0
    }

    function handleKeyPress(event: KeyboardEvent) {
      if (event.code == "Enter") {
        emit("enter", modelValue.value)
      }
    }

    return () => {
      return (
        <div class="i-autocomplete">
          <div class="i-autocomplete-trigger" ref={triggerRef}>
            <input onKeypress={handleKeyPress} class="i-autocomplete-input" onFocus={handleInput} onInput={handleInput} type="text" v-model={modelValue.value} placeholder={props.placeholder} />
          </div>
          <Teleport to="body">
            <Transition name="dropdown" mode="out-in">
              <div class="i-autocomplete-dropdown" style={dropdownStyle.value} v-show={isOpen.value}>
                {renderList(droplist.value, item => (
                  <div class="i-autocomplete-dropdown-item" onClick={selectItem(item)}>
                    {item}
                  </div>
                ))}
              </div>
            </Transition>
          </Teleport>
        </div>
      )
    }
  }
})
</script>

<style scoped lang="scss">
  $text-color: #937639;
  .i-autocomplete {
    min-width: 80px;
    width: 160px;
    user-select: none;
    outline: none;
    height: 24px;
    min-height: 16px;
    line-height: 100%;
    // font-size: 12px;
    color: $text-color;
    background-color: rgba(0, 0, 0, 1);
    border: 1px solid #5b472a;
    border-radius: 2px;
    display: block;

    .i-autocomplete-trigger {
      display: flex;
      height: 100%;
      opacity: 0.8;
      justify-content: space-between;
      align-items: center;

      .i-autocomplete-input {
        padding-left: 8px;
        width: 100%;
        border: none;
        outline: none;
        color: inherit;
        // font-size: 12px;
        background-color: black;
        font-family: SimSun;
      }

      &.disabled {
        color: gray;

        .i-select-down-icon {
          background-image: url("./img/select_down_disabled.png");
        }
      }
    }

    .i-autocomplete-trigger:hover {
      opacity: 1;
    }
  }

  .i-autocomplete-dropdown {
    position: fixed;
    max-height: 160px;
    overflow-y: auto;
    background: black;
    // font-size: 12px;
    z-index: 888;

    $hoverColor: #002947;
    $activeColor: color.scale($hoverColor, $lightness: 5%);
    color: $text-color;

    .i-autocomplete-dropdown-item {
      // font-size: 12px;
      height: 20px;
      line-height: 20px;
      margin: 0;
      padding: 0 8px;
      border: none;
      outline: none;
      appearance: none;
      display: block;
      overflow: hidden;

      &.active {
        background-color: $activeColor;
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
