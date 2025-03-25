<script lang="tsx">
import { defineComponent, renderSlot } from "vue"
import { HiItem, selectionItemProps } from "hoci"

export default defineComponent({
  name: "CalcTab",
  props: {
    ...selectionItemProps
  },
  setup(props, { slots }) {
    return () => {
      return <HiItem {...props}>{renderSlot(slots, "default")}</HiItem>
    }
  }
})
</script>
