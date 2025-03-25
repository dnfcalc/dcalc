<script lang="tsx">
import { defineComponent, provide } from "vue"
import { selectionEmits, selectionProps, useSelectionList } from "hoci"
import { CHECKBOX_GROUP } from "../shared"

export default defineComponent({
  name: "ICheckboxGroup",
  components: {},
  props: {
    ...selectionProps,
    activeClass: {
      type: String,
      default: "checked"
    },
    unactiveClass: {
      type: String,
      default: "unchecked"
    },
    multiple: {
      type: [Boolean, Number],
      default: true
    }
  },
  emits: [...selectionEmits],

  setup(props, context) {
    provide(CHECKBOX_GROUP, true)

    const { render } = useSelectionList(props, context)

    return () => render()
  }
})
</script>

<style lang="scss">
  .i-checkbox {
    display: flex;
    align-items: center;
    &.checked {
      .i-checkbox-icon {
        background-image: url("@/assets/img/control/checkbox_checked.png");
      }
    }

    .i-checkbox-icon {
      width: 12px;
      min-width: 12px;
      height: 12px;
      margin-right: 4px;
      background-image: url("@/assets/img/control/checkbox_uncheck.png");
    }

    .i-checkbox-icon-disable {
      width: 12px;
      min-width: 12px;
      height: 12px;
      margin-right: 4px;
      background-image: url("@/assets/img/control/checkbox_disable.png");
    }

    &:hover:not(.checked) {
      .i-checkbox-icon {
        background-image: url("@/assets/img/control/checkbox_hover.png");
      }
    }

    .i-checkbox-label {
      line-height: 24px;
      color: #937639;
    }
  }
</style>
