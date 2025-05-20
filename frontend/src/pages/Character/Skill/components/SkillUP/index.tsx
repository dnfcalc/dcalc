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
      type: Object as PropType<Record<string, { lv: number; up: number }>>,
      default: () => ({}),
    },
  },
  setup(props) {
    const lvInfo = useVModel(props, 'lvInfo')

    const skills = (index: number = 0) => {
      index -= 1
      const upList = Object.keys(lvInfo.value).filter(
        (a) => !!lvInfo.value[a].up && lvInfo.value[a].up > 0,
      )
      const currentUPSkill = index >= 0 ? upList[index] : undefined
      return computed(() =>
        props.skills
          .filter(
            (a) =>
              a.id.toString() === currentUPSkill ||
              (a.hasUP &&
                (!lvInfo.value[a.id]?.up || lvInfo.value[a.id]?.up == 0) &&
                lvInfo.value[a.id].lv > 0),
          )
          .sort((a, b) => a.learnLv - b.learnLv),
      )
    }

    const itemChecked = (index: number, up: number) => {
      index -= 1
      return computed<string | undefined>({
        get() {
          const upList = Object.keys(lvInfo.value).filter(
            (a) => !!lvInfo.value[a].up && lvInfo.value[a].up > 0,
          )
          const currentUPSkill = upList[index]
          const currentUP = lvInfo.value[currentUPSkill]?.up
          return currentUP == up ? currentUPSkill : undefined
        },
        set(value: string | undefined) {
          if (!value) return
          const upList = Object.keys(lvInfo.value).filter(
            (a) => !!lvInfo.value[a].up && lvInfo.value[a].up > 0,
          )
          const currentUPSkill = upList[index]
          currentUPSkill && (lvInfo.value[currentUPSkill].up = 0)
          if (!value) {
            currentUPSkill && (lvInfo.value[currentUPSkill].up = 0)
          } else {
            lvInfo.value[value].up = up
          }
        },
      })
    }

    const exchange = (index: number) => {
      const skill = itemChecked(index, 1).value || itemChecked(index, 2).value
      if (!skill) return
      lvInfo.value[skill].up = lvInfo.value[skill].up == 1 ? 2 : 1
    }

    return () => (
      <>
        {lvInfo.value && Object.keys(lvInfo.value).length > 0 ? (
          <div class="flex bg-black">
            <div class="skill-up flex justify-between">
              <div class="left">
                <div class="w-full">
                  <div class="flex justify-between">
                    <div class="up_head_1">
                      <div class="icon"></div>
                      <div class="text-14px font-bold text-center">技能攻击力增加</div>
                    </div>
                    <div class="up_head_2">
                      <div class="icon"></div>
                      <div class="text-14px font-bold text-center">
                        技能冷却时间减少
                        <br />
                        技能攻击力增加
                      </div>
                    </div>
                  </div>
                  <div class="flex flex-col gap-5px px-20px py-10px">
                  {renderList(3, (index) => (
                    <>
                      <div class="flex items-center w-full justify-between">
                        <div class={ `up_${!itemChecked(index, 1).value ? index : 'active'}`}>
                          <CaclIconSelect
                            v-model:modelValue={itemChecked(index, 1).value}
                            class="!bg-white/0 !border-white/0"
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
                        <div class={ `up_${!itemChecked(index, 2).value ? index : 'active'}`}>
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

                </div>
              </div>
              <div class="right">
                <div class="title text-16px text-center leading-48px">目标技能</div>
                <div class="flex flex-wrap gap-8px content-start h-110px overflow-y-auto mb-8px w-275px">
                  {renderList(skills().value, (item) => (
                    <div
                      key={item.id}
                      class="w-[28px] h-[28px] rounded-[1px] border-[1px] border-solid border-[#6d4e2b] bg-[linear-gradient(180deg,_#191919_0%,_#000000_100%)] [box-shadow:0px_4px_4px_#00000040_inset] rounded-4px"
                    >
                      <img src={getImageURL(item.icon)} alt={item.name} />
                    </div>
                  ))}
                  {renderList(35 - skills().value.length, (item) => (
                    <div
                      key={item}
                      class="w-[28px] h-[28px] rounded-[1px] border-[1px] border-solid border-[#6d4e2b] bg-[linear-gradient(180deg,_#191919_0%,_#000000_100%)] [box-shadow:0px_4px_4px_#00000040_inset] rounded-4px"
                    ></div>
                  ))}
                </div>
                <div class="flex flex-col gap-10px">
                  {renderList(
                    Object.keys(lvInfo.value).filter(
                      (a) => !!lvInfo.value[a].up && lvInfo.value[a].up > 0,
                    ),
                    (index) => {
                      const skill = props.skills.find((a) => a.id.toString() === index)
                      let tooltip = ''
                      if (skill) {
                        if (lvInfo.value[skill.id.toString()].up == 1) {
                          tooltip = `技能攻击力   +${skill.learnLv < 35 ? '60' : 55}%`
                        }
                        if (lvInfo.value[skill.id.toString()].up == 2) {
                          tooltip = `技能冷却时间 -15%<br/>技能攻击力 +${skill.learnLv < 35 ? '43' : 38}%`
                        }
                      }

                      return skill ? (
                        <div class="flex gap-10px items-center bg-[linear-gradient(180deg,_#1b1c1c_0%,_#000000_100%)] rounded-4px p-5px border-1px border-solid border-#2E2E2E">
                          <div class="up_1 !w-38px !h-38px">
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
              {/* <div class="absolute left-76px top-137px w-250px flex flex-col gap-21.5px">
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
                      (a) => !!lvInfo.value[a].up && lvInfo.value[a].up > 0,
                    ),
                    (index) => {
                      const skill = props.skills.find((a) => a.id.toString() === index)
                      let tooltip = ''
                      if (skill) {
                        if (lvInfo.value[skill.id.toString()].up == 1) {
                          tooltip = `技能攻击力   +${skill.learnLv < 35 ? '60' : 55}%`
                        }
                        if (lvInfo.value[skill.id.toString()].up == 2) {
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
              </div> */}
            </div>
          </div>
        ) : (
          <></>
        )}
      </>
    )
  },
})
