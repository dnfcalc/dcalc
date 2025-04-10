<script lang="tsx">
import { useVModel } from '@vueuse/core'
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'IInput',
  props: {
    modelValue: {
      type: [String, Number],
      default: '',
    },
    type: {
      type: String,
      default: 'text',
    },
    min: {
      type: Number,
      default: 0,
    },
  },
  setup(props) {
    const modelValue = useVModel(props, 'modelValue')
    return () => (
      <div class="flex min-w-80px h-15px border-1 border-solid border-[#5b472a] rounded-[2px] bg-[#000000] px-2px">
        <input
          class="flex-1 border-none w-full outline-none h-auto line-height-100% text-[#ffe2ac] m-0 bg-[#000000]"
          type={props.type}
          v-model={modelValue.value}
        />
        {props.type == 'number' && (
          <div class="h-full">
            <div
              class="input-number-upper h-50% w-10px"
              onClick={() => (modelValue.value = Number(modelValue.value) + 1)}
            ></div>
            <div
              class="input-number-lower h-50% w-10px"
              onClick={() => (modelValue.value = Math.max(Number(modelValue.value) - 1, props.min))}
            ></div>
          </div>
        )}
      </div>
    )
  },
})
</script>

<style lang="scss">
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  appearance: none;
  margin: 0;
}

.input-number-upper {
  background-image: url('@/assets/img/icon/input_upper.png');
  background-size: 8px auto;
  background-position: bottom 1px center;
  background-repeat: no-repeat;
}

.input-number-lower {
  background-image: url('@/assets/img/icon/input_lower.png');
  background-size: 8px auto;
  background-position: top 1px center;
  background-repeat: no-repeat;
}
</style>
