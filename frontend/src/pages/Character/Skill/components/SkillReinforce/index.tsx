import { getImageURL, getLocalImageURL } from '@/utils/images'
import type { ISkill } from '@/api/info/type'
import { useVModel } from '@vueuse/core'
import CalcButton from '@/components/calc/button/index.vue'
import CalcCheckbox from '@/components/calc/checkbox/index.vue'
import CaclIconSelect from '@/components/calc/iconselect/index.vue'
import CalcOption from '@/components/calc/option/index.vue'
import { render, renderList } from 'vue'
import './style.scss'

export default defineComponent({
  name: 'SkillTree',
  props: {
    skills: {
      type: Array as PropType<ISkill[]>,
      default: () => [],
    },
    lvInfo: {
      type: Object as PropType<Record<string, { lv: number; reinforce: number }>>,
      default: () => ({}),
    },
  },
  setup(props) {
    const lvInfo = useVModel(props, 'lvInfo')

    const skills = (index: number = 0) => {
      index -= 1
      const reinforceList = Object.keys(lvInfo.value).filter(
        (a) => !!lvInfo.value[a].reinforce && lvInfo.value[a].reinforce > 0,
      )
      const currentReinforceSkill = index >= 0 ? reinforceList[index] : undefined
      return computed(() =>
        props.skills
          .filter(
            (a) =>
              a.id.toString() === currentReinforceSkill ||
              (a.hasReinforce &&
                (!lvInfo.value[a.id]?.reinforce || lvInfo.value[a.id]?.reinforce == 0) && lvInfo.value[a.id].lv > 0),
          )
          .sort((a, b) => a.learnLv - b.learnLv),
      )
    }

    const itemChecked = (index: number, reinforce: number) => {
      index -= 1
      return computed<string | undefined>({
        get() {
          const reinforceList = Object.keys(lvInfo.value).filter(
            (a) => !!lvInfo.value[a].reinforce && lvInfo.value[a].reinforce > 0,
          )
          const currentReinforceSkill = reinforceList[index]
          const currentReinforce = lvInfo.value[currentReinforceSkill]?.reinforce
          console.log(currentReinforce, reinforce)
          return currentReinforce == reinforce ? currentReinforceSkill : undefined
        },
        set(value: string | undefined) {
          if (!value) return
          const reinforceList = Object.keys(lvInfo.value).filter(
            (a) => !!lvInfo.value[a].reinforce && lvInfo.value[a].reinforce > 0,
          )
          const currentReinforceSkill = reinforceList[index]
          currentReinforceSkill && (lvInfo.value[currentReinforceSkill].reinforce = 0)
          if (!value) {
            currentReinforceSkill && (lvInfo.value[currentReinforceSkill].reinforce = 0)
          } else {
            lvInfo.value[value].reinforce = reinforce
          }
        },
      })
    }

    const exchange = (index: number) => {
      const skill = itemChecked(index, 1).value || itemChecked(index, 2).value
      if (!skill) return
      lvInfo.value[skill].reinforce = lvInfo.value[skill].reinforce == 1 ? 2 : 1
    }

    return () => (
      <>
        {lvInfo.value && Object.keys(lvInfo.value).length > 0 ? (
          <div class="flex pt-10px bg-black">
            <div class="skill-reinforce relative">
              <div class="absolute left-76px top-137px w-250px flex flex-col gap-21.5px">
                {renderList(3, (index) => (
                  <>
                    <div class="w-169px h-36px flex items-center justify-between">
                      <div class="m-4px w-28px h-28px">
                        <CaclIconSelect
                          v-model:modelValue={itemChecked(index, 1).value}
                          class="!bg-white/0 !border-white/0 m-4px"
                          columnNum={4}
                        >
                          {renderList(skills(index).value, (item) => (
                            <>
                              <CalcOption value={item.id.toString()}>
                                <img src={getImageURL(item.icon)} alt={item.name} />
                              </CalcOption>
                            </>
                          ))}
                        </CaclIconSelect>
                      </div>
                      <CalcButton icon="exchange" onClick={() => exchange(index)}></CalcButton>
                      <div class="m-4px w-28px h-28px">
                        <CaclIconSelect
                          v-model:modelValue={itemChecked(index, 2).value}
                          class=" !bg-white/0 !border-white/0"
                          columnNum={4}
                        >
                          {renderList(skills(index).value, (item) => (
                            <>
                              <CalcOption value={item.id.toString()}>
                                <img src={getImageURL(item.icon)} alt={item.name} />
                              </CalcOption>
                            </>
                          ))}
                        </CaclIconSelect>
                      </div>
                    </div>
                  </>
                ))}
              </div>
              <div class="absolute top-70px left-310px w-320px h-270px py-5px px-30px box-border flex flex-col">
                <div class="flex flex-wrap gap-10px content-start h-120px overflow-y-auto mb-10px">
                  {renderList(skills().value, (item) => (
                    <div
                      key={item.id}
                      class="w-[28px] h-[28px] rounded-[1px] border-[1px] border-solid border-[#6d4e2b] bg-[linear-gradient(180deg,_#191919_0%,_#000000_100%)] [box-shadow:0px_4px_4px_#00000040_inset] rounded-4px"
                    >
                      <img src={getImageURL(item.icon)} alt={item.name} />
                    </div>
                  ))}
                  {renderList(36 - skills().value.length, (item) => (
                    <div
                      key={item}
                      class="w-[28px] h-[28px] rounded-[1px] border-[1px] border-solid border-[#6d4e2b] bg-[linear-gradient(180deg,_#191919_0%,_#000000_100%)] [box-shadow:0px_4px_4px_#00000040_inset] rounded-4px"
                    ></div>
                  ))}
                </div>
                <div class="flex flex-col gap-10px">
                  {renderList(
                    Object.keys(lvInfo.value).filter(
                      (a) => !!lvInfo.value[a].reinforce && lvInfo.value[a].reinforce > 0,
                    ),
                    (index) => {
                      const skill = props.skills.find((a) => a.id.toString() === index)
                      let tooltip = ''
                      if (skill) {
                        if (lvInfo.value[skill.id.toString()].reinforce == 1) {
                          tooltip = `技能攻击力   +${skill.learnLv < 35 ? '60' : 55}%`
                        }
                        if (lvInfo.value[skill.id.toString()].reinforce == 2) {
                          tooltip = `技能攻击力 +${skill.learnLv < 35 ? '43' : 38}%<br/>技能冷却时间 -15%`
                        }
                      }

                      return skill ? (
                        <div class="flex gap-5px items-center">
                          <div class="w-[28px] h-[28px] rounded-[1px] border-[1px] border-solid border-[#6d4e2b] bg-[linear-gradient(180deg,_#191919_0%,_#000000_100%)] [box-shadow:0px_4px_4px_#00000040_inset] rounded-4px">
                            <img src={getImageURL(skill?.icon)} alt={skill.name} />
                          </div>
                          <div class="text-#947E4E" v-html={tooltip}></div>
                        </div>
                      ) : (
                        <></>
                      )
                    },
                  )}
                </div>
              </div>
            </div>
          </div>
        ) : (
          <></>
        )}
      </>
    )
  },
})
