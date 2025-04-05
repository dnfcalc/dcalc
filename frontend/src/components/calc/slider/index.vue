<script lang="tsx">
import { defineComponent, ref, computed, shallowRef, watch } from 'vue'
import { useVModel, useDraggable, clamp } from '@vueuse/core'

export default defineComponent({
  name: "ISlider",
  props: {
    modelValue: {
      type: Number,
      default: 0
    },
    min: {
      type: Number,
      default: 0
    },
    max: {
      type: Number,
      default: 100
    },
    step: {
      type: Number,
      default: 1
    },
    disabled: {
      type: Boolean,
      default: false
    },
    showPercent: {
      type: Boolean,
      default: true
    }
  },
  emits: ['update:modelValue', 'change'],
  setup(props, { emit }) {
    const buttonRef = shallowRef<HTMLDivElement | null>(null)
    const runwayRef = shallowRef<HTMLDivElement | null>(null)
    const modelValue = useVModel(props, 'modelValue', emit, { passive: true })

    const percentage = computed(() => {
      return ((modelValue.value - props.min) / (props.max - props.min)) * 100
    })

    useDraggable(buttonRef, {
      onMove(position) {
        if (!runwayRef.value || props.disabled){
          return
        }
        const runwayRect = runwayRef.value?.getBoundingClientRect()

        if (!runwayRect){
           return
        }

        // 使用runway的位置和宽度来计算百分比
        const percentage = Math.max(0, Math.min(100, ((position.x - runwayRect.left) / runwayRect.width) * 100))

        const range = props.max - props.min
        let value = (percentage * range) / 100 + props.min

        // 应用步长
        value = Math.round(value / props.step) * props.step

        // 确保值在范围内
        value = Math.max(props.min, Math.min(props.max, value))

        modelValue.value = value
        emit('change', value)
      }
    })

    return () => (
      <div
        class={[
          'w-full h-8 relative cursor-pointer flex items-center gap-3 py-2',
          { 'cursor-not-allowed': props.disabled }
        ]}
      >
        <div
          class="flex-1 h-1 bg-[#122438] rounded relative"
          ref={runwayRef}
        >
          <div
            class="h-1 bg-[#c6b083] rounded absolute left-0 top-0"
            style={{ width: `${percentage.value}%` }}
          ></div>
          <div
            class="h-6 w-6 absolute top-1/2 -translate-y-1/2 bg-transparent text-center select-none"
            style={{ left: `${percentage.value}%` }}
            ref={buttonRef}
          >
            <div class={[
              'w-4 h-4 absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2',
              'bg-gradient-to-b from-[#223768] to-[#122438]',
              'border border-[#755f44] rounded-full transition-all duration-200',
              'shadow-[0_2px_4px_rgba(0,0,0,0.2)]',
              'hover:(bg-gradient-to-b from-[#2d4e9f] to-[#153051] border-[#e3c18a] scale-110)',
              'active:(bg-gradient-to-b from-[#2d4e9f] to-[#122438] border-[#e3c18a])',
              { 'bg-gradient-to-b from-[#353535] to-[#1c1c1c] border-[#414141]': props.disabled }
            ]}></div>
          </div>
        </div>
        {props.showPercent && (
          <div class={[
            'min-w-[45px] text-right text-sm font-medium',
            props.disabled ? 'text-[#696969]' : 'text-[#e9c556]'
          ]}>
            {percentage.value.toFixed(0)}%
          </div>
        )}
      </div>
    )
  }
})
</script>

<style scoped>
.i-slider {
  width: 100%;
  height: 32px;
  position: relative;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 0;
}

.i-slider.is-disabled {
  cursor: not-allowed;
}

.i-slider.is-disabled .i-slider-button {
  background: linear-gradient(#353535, #1c1c1c);
  border-color: #414141;
}

.i-slider.is-disabled .i-slider-value {
  color: #696969;
}

.i-slider-runway {
  flex: 1;
  height: 4px;
  background-color: #122438;
  border-radius: 2px;
  position: relative;
}

.i-slider-bar {
  height: 4px;
  background: #c6b083;
  border-radius: 2px;
  position: absolute;
  left: 0;
  top: 0;
}

.i-slider-button-wrapper {
  height: 24px;
  width: 24px;
  position: absolute;
  top: 50%;
  transform: translate(-50%, -50%);
  background: transparent;
  text-align: center;
  user-select: none;
  line-height: normal;
}

.i-slider-button {
  width: 16px;
  height: 16px;
  background: linear-gradient(#223768, #122438);
  border: 1px solid #755f44;
  border-radius: 50%;
  transition: all 0.2s ease-in-out;
  user-select: none;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.i-slider-button:hover {
  background: linear-gradient(#2d4e9f, #153051);
  border-color: #e3c18a;
  transform: translate(-50%, -50%) scale(1.1);
}

.i-slider-button:active {
  background: linear-gradient(#2d4e9f, #122438);
  border-color: #e3c18a;
}

.i-slider-value {
  min-width: 45px;
  text-align: right;
  font-size: 14px;
  color: #e9c556;
  font-weight: 500;
}
</style>

