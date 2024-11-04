<script lang="tsx">
import { computed, defineComponent } from "vue"

export default defineComponent({
  props: {
    value: {
      type: [Number, String],
      default: 0
    },

    total: {
      type: [Number, String],
      default: 100
    }
  },
  setup(props) {
    const progress = computed(() => {
      if (props.value == 0) {
        return 0
      }
      return (Number(props.value) / Number(props.total)) * 100
    })

    return () => (
      <div class="border-solid bg-hex-171717 border-hex-272521 border-2">
        <div class="border-transparent border-solid border-2">
          <div style={progress.value == 0 ? "width:0" : `width:${progress.value.toFixed(2)}%`} class="h-2 duration-200 calc-progress"></div>
        </div>
      </div>
    )
  }
})
</script>

<style lang="scss" scoped>
  .calc-progress {
    background: linear-gradient(to bottom, #48d0eb 0%, #6cf4fe 15%, #4fbdfe 30%, #3080fe 40%, #1d5bfe 55%, #3283fd 70%, #000456 100%);
  }
</style>
