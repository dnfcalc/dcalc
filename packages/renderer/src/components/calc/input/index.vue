<script lang="tsx">
import { useVModel } from "@vueuse/core"
import { defineComponent } from "vue"

export default defineComponent({
  name: "IInput",
  props: {
    modelValue: {
      type: [String, Number],
      default: ""
    }
  },
  setup(props) {
    const modelValue = useVModel(props, "modelValue")
    return () => <input v-model={modelValue.value} class="i-input" />
  }
})
</script>

<style lang="scss">
  .i-input {
    min-width: 80px;
    width: 178px;
    user-select: none;
    outline: none;
    height: 20px;
    min-height: 16px;
    line-height: 100%;
    // font-size: 12px;
    color: #937639;
    background-color: rgba(0, 0, 0, 1);
    border: 1px solid #5b472a;
    border-radius: 2px;
    margin: 0;
    padding-left: 10px;
  }

  input::-webkit-outer-spin-button,
  input::-webkit-inner-spin-button {
    -webkit-appearance: none;
    appearance: none;
    margin: 0;
  }
</style>
