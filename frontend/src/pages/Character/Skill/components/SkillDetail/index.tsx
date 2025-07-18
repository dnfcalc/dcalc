import { asyncComputed } from '@vueuse/core'
import api from '@/api'
import './style.scss'
import CalcTabs from '@/components/calc/tabs/index.vue'
import CalcTab from '@/components/calc/tab/index.vue'

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

    const curTab = ref(0)

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

    const desc = computed(() => skillInfo.value?.descDetail.split('\n'))

    const detail = computed(() => {
      const items =
        skillInfo.value?.attribute.optionDesc?.split('\n').filter((item) => !!item) ?? []
      const details = items?.map((a) => {
        const beforeReplace = a.match(/^(.+?)\s*(\{value\d+\}.*)$/);
        if (beforeReplace) {
          a = `${beforeReplace[1]}<span class="skill_info_value">${beforeReplace[2]}</span>`
        }
        const matches = a.match(/{([^}]+)}/g)
        if (matches) {
          matches.forEach((match) => {
            const key = match.replace(/[{}]/g, '')
            // Only access if key matches the expected pattern
            if (/^value.+/.test(key)) {
              const value = skillInfo.value?.attribute.optionValue[key as `value${string}`] ?? '-'
              if (value) {
                a = a.replace(match, `<span style="padding:0px 2px;color:#4AA256">${value}</span>`)
              }
            }
          })
        }
        return a
      })
      return details || []
    })

    const renderSkillDetail = () => (
      <>
        <div class="skill_title">基本信息</div>
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
        <div class="skill_title">技能描述</div>
        <div class="h-auto max-h-200px">
          <div class="h-full overflow-y-auto bg-#161816 p-2px">
            {desc.value?.map((item) =>
              // item.startsWith('[') || item.startsWith('-') || item.startsWith('<') ? (
              //   <div class="min-h-10px">{item}</div>
              // ) :
              (
                <div class="min-h-10px" style="text-indent:20px;">
                  {item}
                </div>
              ),
            )}
          </div>
        </div>
        {(detail.value.length > 0 ) && (
          <>
            <div class="skill_title">技能属性</div>
            <div class="flex-1 overflow-y-auto">
              <div class=" flex flex-col gap-2px">
                {detail.value.map((item) => (
                  <div class="flex justify-between item items-center" v-html={item}></div>
                ))}
              </div>
            </div>
          </>
        )}
      </>
    )

    const renderSkillVp = () => (
      <>
        <div class="h-auto">
          <div class="h-full flex flex-col gap-5px">
            {skillInfo.value?.evolution?.map((item) => (
              <>
                <div class="flex flex-col gap-2px">
                  <div class="skill_vp_title">{item.name}</div>
                  <div class="skill_title">技能描述</div>
                  <div class="h-auto bg-#161816 max-h-300px overflow-y-auto">
                    <div class="h-auto  p-2px" style="white-space: pre-wrap;">
                      {item.descDetail}
                    </div>
                  </div>
                </div>
              </>
            ))}
          </div>
        </div>
      </>
    )

    onMounted(() => {
      watchEffect(() => {
        ;(skillInfo.value?.evolution?.length ?? 0) == 0 && (curTab.value = 0)
      })
    })

    return () => (
      <>
        <div class="flex flex-col gap-2px mx-2px text-#907B54 h-full">
          <div class="skill_name h-20px">{skillInfo.value?.name}</div>
          <div class="relative">
            <CalcTabs v-model={curTab.value}>
              <CalcTab class="flex-1 flex justify-center" value={0}>
                技能信息
              </CalcTab>
              <CalcTab
                class="flex-1 flex justify-center"
                value={1}
                disabled={!skillInfo.value?.evolution?.length}
              >
                技能进化
              </CalcTab>
            </CalcTabs>
          </div>
          {curTab.value === 0 && renderSkillDetail()}
          {curTab.value === 1 && renderSkillVp()}
        </div>
      </>
    )
  },
})
