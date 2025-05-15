<script lang="tsx">
import { defineComponent, renderSlot } from 'vue'
import { HiItem, selectionProps } from 'hoci'

export default defineComponent({
  name: 'CalcTab',
  props: {
    ...selectionProps,
  },
  setup(props, { slots }) {
    return () => {
      return <HiItem {...props}>{renderSlot(slots, 'default')}</HiItem>
    }
  },
})
</script>
