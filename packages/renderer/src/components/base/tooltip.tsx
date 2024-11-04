import { syncRefs, useVModel } from "@vueuse/core"
import type { CSSProperties, PropType } from "vue";
import { Teleport, Transition, computed, defineComponent, nextTick, reactive, ref, renderSlot, watch } from "vue"
import { provideShow } from "../hooks/show"

export const tooltipProps = {
  popClass: {
    type: String
  },
  position: {
    type: String as PropType<"bottom" | "top" | "left" | "right" | "auto">,
    default: () => "auto"
  },
  offset: {
    type: Number,
    default: () => 8
  },
  lazy: {
    type: Boolean,
    default: () => false
  },
  visible: {
    type: Boolean,
    default: () => false
  },
  disabled: {
    type: Boolean,
    default: () => false
  }
}

export default defineComponent({
  name: "ITooltip",
  props: tooltipProps,
  emits: ["change", "update:visible"],
  setup(props, { slots, emit }) {
    const isOpen = ref(props.visible)

    syncRefs(useVModel(props, "visible"), isOpen)

    provideShow(isOpen)

    let timer: NodeJS.Timeout

    const triggerRef = ref<HTMLElement>()
    const popupRef = ref<HTMLElement>()

    const dropdownPosition = reactive({ x: 0, y: 0 })

    const isShow = computed(() => isOpen.value && triggerRef.value && popupRef.value && dropdownPosition.x + dropdownPosition.y > 0)

    const dropdownStyle = computed<CSSProperties>(() => {
      return {
        left: `${dropdownPosition.x}px`,
        top: `${dropdownPosition.y}px`,
        visibility: isShow.value ? "visible" : "hidden"
      }
    })

    const mounted = ref(false)

    function onMouseover() {
      if (props.disabled) {
        return
      }
      timer = setTimeout(
        () => {
          isOpen.value = true
          emit("change", true)
        },
        props.lazy ? 800 : 100
      )
    }

    function onMouseout() {
      if (props.disabled) {
        return
      }
      clearTimeout(timer)
      isOpen.value = false
      emit("change", false)
    }

    function resize() {
      const trigger = triggerRef.value
      const popup = popupRef.value

      if (!!trigger && !!popup) {
        const { width, height, left, top } = trigger.getBoundingClientRect()

        const { clientWidth: pWidth, clientHeight: pHeight } = popup

        let x = 0
        let y = 0

        const offset = props.offset

        switch (props.position) {
          case "auto":
          case "bottom":
            x = left + width / 2
            y = top + height + offset
            break
          case "top":
            x = left
            y = top - pHeight - offset
            break
          case "left":
            x = left - pWidth - offset
            y = top
            break
          case "right":
            x = left + width + offset
            y = top
            break
        }
        if (props.position == "auto") {
          x = window.innerWidth - x > 500 ? x + 20 : x - 20 - 310
          y = window.innerHeight - y > popup.offsetHeight + 50 ? y : window.innerHeight - (popup.offsetHeight + 50)
        }
        dropdownPosition.x = x
        dropdownPosition.y = y
      }
    }

    watch(isOpen, val => {
      if (val) {
        mounted.value = true
      }
      nextTick(resize)
    })

    return () => {
      return (
        <div {...{ onMouseout, onMouseover }} ref={triggerRef}>
          {renderSlot(slots, "default")}
          <Teleport to="body">
            <Transition name="dropdown" mode="out-in">
              {mounted.value && !props.disabled && (
                <div class={["i-popper z-999", props.popClass]} style={dropdownStyle.value} ref={popupRef}>
                  {renderSlot(slots, "popper")}
                </div>
              )}
            </Transition>
          </Teleport>
        </div>
      )
    }
  }
})
