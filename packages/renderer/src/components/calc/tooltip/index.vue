<script lang="tsx">
import { defineComponent } from "vue"
import { NTooltip } from "@/components/base"

import { tooltipProps } from "@/components/base/tooltip"

export default defineComponent({
  name: "ITooltip",
  components: { NTooltip },
  props: {
    ...tooltipProps
  },
  setup(props, { slots }) {
    return () => {
      return (
        <n-tooltip {...props} pop-class="i-popper z-999 fixed top-0 left-0 bg-black bg-opacity-90 border-1.5 border-hex-272928 rounded-2px border-solid">
          {slots}
        </n-tooltip>
      )
    }
  }
})
</script>

<style lang="scss"></style>
