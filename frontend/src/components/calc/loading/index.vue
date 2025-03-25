<script lang="tsx">
import { computed, defineComponent, renderSlot } from "vue"
import { classPropType } from "@/components/hooks/types"
export default defineComponent({
  props: {
    loading: {
      type: Boolean,
      default: () => false
    },
    class: {
      type: classPropType,
      default: () => ""
    }
  },
  setup(props, { slots }) {
    const loading = computed(() => props.loading)
    return () => {
      return (
        <div class="relative">
          <div v-show={loading.value} class="flex h-full w-full z-99 absolute items-center justify-center">
            <svg
              class="i-loading-spin"
              version="1.1"
              xmlns="http://www.w3.org/2000/svg"
              xmlns:xlink="http://www.w3.org/1999/xlink"
              width="200px"
              height="200px"
              viewBox="0 0 200 200"
              xml:space="preserve"
            >
              <g>
                <linearGradient id="right" gradientUnits="userSpaceOnUse" x1="150" y1="20" x2="150" y2="180">
                  <stop offset="0" style="stop-color:transparent" />
                  <stop offset="1" style="stop-color:currentColor" />
                </linearGradient>
                <path fill="url(#right)" d="M100,0v20c44.1,0,80,35.9,80,80c0,44.1-35.9,80-80,80v20c55.2,0,100-44.8,100-100S155.2,0,100,0z" />
                <linearGradient id="left" gradientUnits="userSpaceOnUse" x1="50" y1="0" x2="50" y2="180">
                  <stop offset="0" style="stop-color:currentColor" />
                  <stop offset="1" style="stop-color:transparent" />
                </linearGradient>
                <path fill="url(#left)" d="M20,100c0-44.1,35.9-80,80-80V0C44.8,0,0,44.8,0,100s44.8,100,100,100v-20C55.9,180,20,144.1,20,100z" />
                <circle fill="currentColor" cx="100" cy="10" r="10" />
              </g>
            </svg>
          </div>
          <div class={[props.class].concat("duration-200").concat(loading.value ? "opacity-0" : "")}>{renderSlot(slots, "default", {}, () => [])}</div>
        </div>
      )
    }
  }
})
</script>

<style lang="scss">
  .i-loading-spin {
    width: 32px;
    height: 32px;
    animation: spin infinite 1s linear;
  }

  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
</style>
