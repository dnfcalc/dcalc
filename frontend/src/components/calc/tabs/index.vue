<script lang="tsx">
import { HiSelection, selectionProps } from "hoci"
import type { PropType } from "vue";
import { computed, defineComponent, renderSlot } from "vue"
import type { LocationQuery } from "vue-router";
import { parseQuery, useRouter } from "vue-router"
import type { BaseType } from "@/components/hooks/types"

export default defineComponent({
  name: "CalcTabs",
  props: {
    ...selectionProps,
    vertical: {
      type: Boolean
    },
    route: {
      type: Boolean
    },
    query: {
      type: [Object, String] as PropType<string | LocationQuery>
    }
  },
  setup(props, { emit, slots }) {
    const router = useRouter()

    const routeQuery = computed(() => {
      if (typeof props.query == "string") {
        return parseQuery(props.query)
      }
      return props.query ?? {}
    })

    const modelValue = computed<BaseType>({
      get() {
        let val = props.modelValue
        if (props.route) {
          val = val ?? router.currentRoute.value.path
        }
        return val
      },
      set(val) {
        if (props.route && val) {
          val = decodeURIComponent(val.toString())
          router.push({ path: val, query: routeQuery.value })
        }
        emit("update:modelValue", val)
        emit("change", val)
      }
    })

    return () => {
      return (
        <HiSelection v-model={modelValue.value} class={{ "i-tabs": true, "vertical": !!props.vertical }} activeClass="active" itemClass={["i-tab cursor-pointer"].concat(props.itemClass)}>
          {renderSlot(slots, "default")}
        </HiSelection>
      )
    }
  }
})
</script>

<style lang="scss">
.i-tabs {
    display: flex;
    list-style: none;
    align-items: flex-end;
    border-bottom: 1px solid #4f4838;
    width: 100%;

    font-size: 14px;

    color: #c6b083;
    margin: 0;
    padding: 0;

    a {
      text-decoration: none;
      color: #c6b083;
      &:visited {
        color: currentColor;
      }
    }

    &.vertical {
      flex-direction: column;

      .i-tab {
        border-radius: 0;
      }
    }

    .i-tab {
      // font-size: 12px;
      margin-left: 1px;

      width: 120px;
      height: 20px;
      line-height: 20px;
      text-align: center;
      text-decoration: none;

      &:visited {
        color: currentColor;
      }

      border: #4f4838 1px solid;
      border-bottom: none;
      border-radius: 5px 5px 0 0;
      background: linear-gradient(to top, rgba(6, 6, 6, 0.9), rgba(52, 52, 52, 0.9));
      transition: all 0.4s ease-in-out;

      &:hover {
        background: linear-gradient(#4a4b4e, #1d1e22);
      }

      &.active {
        background: linear-gradient(#574d38, #25221d);
        border-image: url("@/assets/img/control/active_top.png") 1 fill stretch;
        // color: #ffb400;
      }
    }
  }
</style>
