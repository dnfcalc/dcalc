<script lang="tsx">
import { useToggle, useVModel } from "@vueuse/core"
import { defineComponent, renderSlot } from "vue"

export default defineComponent({
  name: "ICollapse",
  props: {
    title: {
      type: String
    },
    modelValue: {
      type: Boolean,
      default: () => true
    }
  },
  setup(props, { slots, emit }) {
    const modelValue = useVModel(props, "modelValue", emit, { passive: true })

    const toggle = useToggle(modelValue)

    return () => {
      return (
        <div class="rounded h-auto bg-hex-00000078 border-1 border-hex-ffffff28 my-1 overflow-hidden">
          <div onClick={() => toggle()} v-text={props.title} class="bg-gradient-to-b flex from-hex-244281 to-hex-122438 h-6 text-xs text-center w-full items-center justify-center"></div>
          <div class={["transition-all", "ease-out-in", "h-auto"].concat(modelValue.value ? ["max-h-200"] : ["max-h-0"])}>
            <div class="p-2">{renderSlot(slots, "default")}</div>
          </div>
        </div>
      )
    }
  }
})
</script>
