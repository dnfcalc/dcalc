import { asyncComputed } from '@vueuse/core'
import api from '@/api'
import './style.scss'

export default defineComponent({
  name: 'SkillDetail',
  props: {
    skillId: {
      type: String,
      required: true,
    },
    level: {
      type: Number,
      default: 1,
    },
  },
  setup(props) {
    const currentSkill = computed(() => props.skillId)
    const currentLevel = computed(() => props.level)

    const skillInfo = asyncComputed(async () => {
      if (!currentSkill.value && !currentLevel.value) return undefined
      const res = await api.skillDetail(currentSkill.value, currentLevel.value)
      return res
    })

    const basic = computed(() =>
      !skillInfo.value
        ? []
        : [
            { label: '技能等级', value: skillInfo.value?.attribute.level },
            { label: '学习等级', value: skillInfo.value?.requiredLevel },
            { label: '等级上限', value: skillInfo.value?.maxLevel },
            {
              label: '冷却时间',
              value: skillInfo.value?.attribute.coolTime
                ? `${skillInfo.value?.attribute.coolTime.toFixed(1)}秒`
                : undefined,
            },
            {
              label: '施放时间',
              value: !skillInfo.value?.attribute.castingTime
                ? '瞬发'
                : `${skillInfo.value?.attribute.castingTime.toFixed(1)}秒`,
            },
            { label: '魔法值', value: skillInfo.value?.attribute.consumeMp },
            {
              label: '消耗无色小晶块',
              value: skillInfo.value?.consumeItem?.value
                ? `${skillInfo.value?.consumeItem?.value}个`
                : undefined,
            },
          ],
    )

    const desc = computed(() => skillInfo.value?.descDetail.split('\n').filter((item) => !!item))

    const detail = computed(() => {
      const items = skillInfo.value?.attribute.optionDesc.split('\n').filter((item) => !!item)
      const details = items?.map((a) => {
        const matches = a.match(/{([^}]+)}/g)
        if (matches) {
          matches.forEach((match, index) => {
            const key = match.replace(/[{}]/g, '')
            // Only access if key matches the expected pattern
            if (/^value.+/.test(key)) {
              const value = skillInfo.value?.attribute.optionValue[key as `value${string}`]
              if (value) {
                a = a.replace(
                  match,
                  `<span style="${index == 0 ? 'margin-left:auto;' : ''};padding:0px 2px;color:#4AA256">${value}</span>`,
                )
              }
            }
          })
        }
        return a
      })
      return details || []
    })

    return () => (
      <>
        <div class="flex flex-col gap-2px mx-2px text-#907B54 h-full">
          <div class="skill_title h-20px">{skillInfo.value?.name}</div>
          <div class="title">基本信息</div>
          <div class="flex flex-col gap-2px">
            {basic.value.map(
              (item) =>
                !!item.value && (
                  <div class="flex justify-between item">
                    <span class="label">{item.label}</span>
                    <span class="value">{item.value}</span>
                  </div>
                ),
            )}
          </div>
          <div class="title">技能描述</div>
          <div class="h-auto max-h-200px">
            <div class="h-full overflow-y-auto">
              {desc.value?.map((item) => (
                <span style="white-space: pre-wrap;text-indent:20px;">{item}</span>
              ))}
            </div>
          </div>
          <div class="title">技能属性</div>
          <div class="flex-1">
            <div class="overflow-y-auto h-full flex flex-col gap-2px">
              {detail.value?.map((item) => (
                <div class="flex justify-between item items-center" v-html={item}></div>
              ))}
            </div>
          </div>
        </div>
      </>
    )
  },
})
