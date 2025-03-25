<script lang="tsx">
import { onClickOutside, onKeyDown, syncRef, useDraggable, useVModel } from "@vueuse/core"
import type { PropType, RendererElement } from "vue"
import { Teleport, Transition, computed, defineComponent, provide, ref, renderSlot, watch } from "vue"
import { provideShow } from "@/components/hooks/show"

export default defineComponent({
  name: "IDialog",
  props: {
    visible: {
      type: Boolean,
      default: () => false
    },
    class: {
      type: String
    },
    mask: {
      type: Boolean,
      default: () => false
    },
    // 模态框
    modal: {
      type: Boolean,
      default: () => false
    },
    header: {
      type: [String, Boolean],
      default: () => "提示"
    },
    closeOnEsc: {
      type: Boolean,
      default: () => true
    },
    closeButton: {
      type: Boolean,
      default: () => true
    },
    cache: {
      // 维持窗口状态
      type: Boolean,
      default: () => true
    },
    lazy: {
      type: Boolean,
      default: () => false
    },
    drag: {
      type: String as PropType<"header" | "all" | "none">,
      default: () => "header"
    },
    appendTo: {
      type: [Object, String] as PropType<string | RendererElement | null | undefined>,
      default: "body"
    },
    scale: {
      type: Number,
      default: 1
    }
  },
  emits: ["close", "update:visible"],
  setup(props, { emit, slots }) {
    const dialogRef = ref<HTMLElement | null>(null)
    const headerRef = ref<HTMLElement | null>(null)

    const visible = ref(props.visible)

    provideShow(visible)

    provide("dialogRef", dialogRef)

    const loaded = ref(!props.lazy)

    const stopLoadWatch = watch(visible, val => {
      if (val) {
        loaded.value = true
        stopLoadWatch()
      }
    })

    syncRef(useVModel(props, "visible"), visible, { direction: "both" })

    onClickOutside(dialogRef, () => {
      if (props.modal) {
        close()
      }
    })

    function close() {
      visible.value = false
      emit("close")
    }

    onKeyDown(
      "Escape",
      () => {
        if (visible.value && props.closeOnEsc) {
          close()
        }
      },
      { target: document }
    )

    const init = ref(true)

    const { x, y, style } = useDraggable(
      computed(() => {
        switch (props.drag) {
          case "header":
            return headerRef.value
          case "all":
            return dialogRef.value
          case "none":
          default:
            return null
        }
      }),
      {
        initialValue: { x: 0, y: 0 }
      }
    )

    const isFixed = computed(() => x.value + y.value > 0)

    const appendToRef = computed(() => {
      return props.appendTo || "body"
    })

    return () => {
      return (
        <Teleport to={appendToRef.value}>
          <Transition name="dialog" mode="out-in">
            {loaded.value && (props.cache || visible.value) && (
              <div v-show={visible.value} class={["dialog-mask w-full h-full fixed top-0 left-0 z-999 flex justify-center items-center "].concat(props.mask ? "bg-hex-000 bg-opacity-66" : "")} style={`transform: scale(${props.scale});${x.value == 0 && y.value == 0 ?"transform-origin:center":"transform-origin:left top"}`}>
                <div ref={dialogRef} class={["h-auto border-1 border-hex-2b2b2b border-solid  shadow-sm round-1 dialog min-w-48", isFixed.value ? "fixed" : "", props.class]} style={`top:${y.value/props.scale}px;left:${x.value/props.scale}px`}>
                  {props.header && (
                    <div ref={headerRef} class="flex h-4 px-1 leading-4 z-9999 justify-center relative app-header py-2px">
                      <div class="text-xs text-shadow ">{props.header}</div>
                      {props.closeButton && (
                        <div class="flex top-0 right-0 bottom-0 items-center absolute">
                          <div onClick={close} class="cursor-pointer flex  h-4 text-center w-4  items-center close-icon"></div>
                        </div>
                      )}
                    </div>
                  )}
                  <div class="bg-hex-000 bg-opacity-80 text-white text-xs">{renderSlot(slots, "default")}</div>
                </div>
              </div>
            )}
          </Transition>
        </Teleport>
      )
    }
  }
})
</script>

<style lang="scss" scoped>
  .dialog-enter-active {
    animation: fade-in 400ms;
    .dialog {
      animation: zoom-in 400ms;
    }
  }
  .dialog-leave-active {
    animation: fade-in reverse 400ms;
    .dialog {
      animation: zoom-out 400ms;
    }
  }
</style>
