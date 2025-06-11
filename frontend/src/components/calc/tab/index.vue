<script lang="tsx">
import { defineComponent, renderSlot } from 'vue'
import { HiItem, selectionProps } from 'hoci'

export default defineComponent({
  name: 'CalcTab',
  props: {
    ...selectionProps,
    value: {
      type: [String, Number],
      default: '',
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  setup(props, { slots }) {
    return () => {
      return <HiItem {...props}>{renderSlot(slots, 'default')}</HiItem>
    }
  },
})
</script>
