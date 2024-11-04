<script lang="tsx">
import type { EmitsOptions, SetupContext } from "vue";
import { computed, defineComponent, inject, nextTick, renderSlot } from "vue"
import { selectionItemProps, switchEmits, switchProps, useSelectionItem, useSwitch } from "hoci"
import { CHECKBOX_GROUP } from "../shared"

export default defineComponent({
  name: "ICheckbox",
  components: {},
  props: {
    ...switchProps,
    ...selectionItemProps,
    label: {
      type: String
    },
    disabled: {
      type: Boolean,
      default: false
    },
    round: {
      type: Boolean,
      default: () => false
    }
  },
  emits: [...switchEmits],

  setup(props, context) {
    const inGroup = computed(() => {
      return inject(CHECKBOX_GROUP, false)
    })

    const { toggle, switchClass } = useSwitch(
      () => ({
        ...props,
        class: props.round ? "i-switch text-xs h-auto cursor-pointer" : "i-checkbox text-xs h-auto cursor-pointer",
        activeClass: "checked"
      }),
      context
    )

    const { activate, itemClass } = useSelectionItem(props, context as SetupContext<EmitsOptions>)

    const baseClass = computed(() => (props.round ? "i-switch" : "i-checkbox"))

    const { slots } = context

    async function onClick() {
      if (inGroup.value) {
        activate()
      } else {
        toggle()
      }
      await nextTick()
      // console.log(props.modelValue)
    }

    const className = computed(() => {
      return inGroup.value ? itemClass.value : switchClass.value
    })

    return () => (
      <div onClick={onClick} class={["flex", baseClass.value, className.value]}>
        <span class={!props.disabled ? "i-checkbox-icon" : "i-checkbox-icon-disable"}></span>
        <div class={["i-checkbox-label h-auto"]}>{props.label ?? renderSlot(slots, "default")}</div>
      </div>
    )
  }
})
</script>

<style lang="scss">
  .i-checkbox {
    display: flex;
    align-items: center;
    justify-content: baseline;
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

  .i-switch {
    display: flex;
    align-items: center;
    // justify-content: center;

    &.checked {
      .i-checkbox-icon {
        background-image: linear-gradient(to right, #8f6e29, #8f6e29), linear-gradient(rgb(110, 89, 61), rgb(60, 46, 30));
      }

      .i-checkbox-icon::after {
        left: 100%;
        margin-left: -14.8px;
      }
    }

    .i-checkbox-icon {
      margin: 0;
      display: inline-block;
      position: relative;
      width: 30px;
      height: 18px;

      outline: none;
      border-radius: 10px;
      box-sizing: border-box;
      background: #dcdfe6;
      cursor: pointer;
      transition: border-color 0.3s, background-color 0.3s;
      vertical-align: middle;
      // border-radius: 16px;
      border: 1.5px solid transparent;
      background-clip: padding-box, border-box;
      background-origin: padding-box, border-box;
      background-image: linear-gradient(to right, #141414, #141414), linear-gradient(rgb(110, 89, 61), rgb(60, 46, 30));
      box-shadow: inset 0 0 2px 1.5px black;
    }

    .i-checkbox-icon::after {
      content: "";
      position: absolute;
      top: 1.6px;
      left: 1px;
      border-radius: 100%;
      transition: all 0.3s;
      width: 13px;
      height: 13px;
      outline: 0.8px solid black;
      background: linear-gradient(rgb(15, 61, 116), rgb(8, 37, 71));
      box-shadow: inset 0 0 2px 0.5px rgb(255, 255, 255, 0.1);
    }

    .i-checkbox-icon-disable {
      margin: 0;
      display: inline-block;
      position: relative;
      width: 30px;
      height: 18px;

      outline: none;
      border-radius: 10px;
      box-sizing: border-box;
      background: #dcdfe6;
      cursor: pointer;
      transition: border-color 0.3s, background-color 0.3s;
      vertical-align: middle;
      // border-radius: 16px;
      border: 1.5px solid transparent;
      background-clip: padding-box, border-box;
      background-origin: padding-box, border-box;
      background-image: linear-gradient(to right, #dcdfe6, #dcdfe6), linear-gradient(rgb(110, 89, 61), rgb(60, 46, 30));
      box-shadow: inset 0 0 2px 1.5px black;
    }

    .i-checkbox-icon-disable::after {
      content: "";
      position: absolute;
      top: 1.6px;
      left: 1px;
      border-radius: 100%;
      transition: all 0.3s;
      width: 13px;
      height: 13px;
      // outline: 0.8px solid black;
      background: white;
      // box-shadow: inset 0 0 2px 0.5px rgb(255, 255, 255, 0.1);
    }

    &:hover {
      .i-checkbox-icon::after {
        background: linear-gradient(#15549f, #0e3c72);
      }
    }

    .i-checkbox-label {
      line-height: 18px;
      height: 18px;
      padding-left: 2px;
      color: #937639;
    }
  }
</style>
