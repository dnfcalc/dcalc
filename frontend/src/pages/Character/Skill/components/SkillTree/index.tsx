import { getImageURL, getLocalImageURL } from '@/utils/images'
import type { ISkill } from '@/api/info/type'
import { useVModel } from '@vueuse/core'
import './style.scss'

export default defineComponent({
  name: 'SkillTree',
  props: {
    skills: {
      type: Array as PropType<ISkill[]>,
      default: () => [],
    },
    lvInfo: {
      type: Object as PropType<Record<string, { lv: number }>>,
      default: () => ({}),
    },
    bindAwake: {
      type: Number,
      default: ()=>50,
    },
  },
  setup(props) {
    const skills = computed(() => props.skills)
    const lvInfo = useVModel(props, 'lvInfo')
    const bindAwake = useVModel(props, 'bindAwake')

    const getSkill = (lvStart: number, lvEnd: number, position: number) => {
      if (position >= 0)
        return skills.value.find(
          (item) =>
            item.learnLv > lvStart - 5 &&
            item.learnLv <= Math.max(lvEnd - 5, 1) &&
            item.position == position,
        )
      else
        return skills.value.filter(
          (item) => item.learnLv > lvStart - 5 && item.learnLv <= Math.max(lvEnd - 5, 1),
        )
    }

    const lvList = [15, 20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100]

    const columns = [...new Array(10).keys()]

    const activeSkill = ref<number>(-1)

    const chooseSkill = (skill?: ISkill, operation: string = 'add') => {
      if (!skill) {
        activeSkill.value = -1
        return
      }
      if (activeSkill.value == skill.id) actionSkillLv(skill, operation)
      else activeSkill.value = skill.id
    }

    const awakeSkill_1 = computed(() =>
      skills.value.find((item) => item.learnLv == 50 && item.type == 'active'),
    )
    const awakeSkill_2 = computed(() =>
      skills.value.find((item) => item.learnLv == 85 && item.type == 'active'),
    )

    const actionSkillLv = (skill: ISkill, operation: string) => {
      if (operation == 'add') {
        lvInfo.value[skill.id.toString()] = {
          lv: Math.min(lvInfo.value[skill.id.toString()]?.lv + 1, skill.maxLv),
        }
        return
      }
      if (operation == 'addMax') {
        lvInfo.value[skill.id.toString()] = { lv: skill.maxLearnLv }
        return
      }
      if (operation == 'sub') {
        lvInfo.value[skill.id.toString()] = {
          lv: Math.max(lvInfo.value[skill.id.toString()]?.lv - 1, 0),
        }
        return
      }
      if (operation == 'subMax') {
        lvInfo.value[skill.id.toString()] = { lv: 0 }
        return
      }
    }

    const chooseBindAwake = (lv:number) => {
        bindAwake.value = lv
        console.log(bindAwake.value,lv)
    }

    const renderSkill = (skill: ISkill, index: number) => {
      const info = lvInfo.value?.[skill.id.toString()]
      let color = 'white'
      if (info?.lv < skill.maxLearnLv) color = '#32E432'
      if (info?.lv > skill.maxLearnLv) color = '#58E0FC'
      return (
        <>
          <div class="relative w-35px h-55px">
            {activeSkill.value == skill.id && renderSkillAction(skill)}
            <div
              class={["w-36px absolute h-48px flex flex-col box-border items-center py-3px z-2",skill.learnLv == 100 ? '' : 'skill']}
              onClick={(e) => {
                e.stopPropagation()
                chooseSkill(skill)
              }}
              onContextmenu={(e) => {
                e.stopPropagation()
                e.preventDefault()
                chooseSkill(skill, 'sub')
              }}
              key={index}
            >
              <img
                class={['h-28px w-28px', skill.type === 'passive' ? 'passive' : '']}
                src={getImageURL(skill.icon)}
              ></img>
              <div class="w-100% flex flex-1 justify-center" style={{ color }}>
                {info?.lv ?? 0}
              </div>
            </div>
            {skill.learnLv == 100 && (
              <>
                <div class={`pos-absolute w-196px h-54px box-border translate-x--50% left-18px top--3px flex justify-between items-center py-2px px-3px awake_${bindAwake.value}`}>
                  <div class="w-36px flex flex-col box-border items-center py-2px z-2" onClick={()=>chooseBindAwake(50)}>
                    <img
                      class="h-28px w-28px mt-2px"
                      src={getImageURL(awakeSkill_1.value?.icon ?? '')}
                    ></img>
                    <div class="w-100% mt-1px flex items-center justify-center text-#ffc701">1次</div>
                  </div>
                  <div class="w-36px flex flex-col box-border items-center py-2px z-2" onClick={()=>chooseBindAwake(85)}>
                    <img
                      class="h-28px w-28px mt-1px"
                      src={getImageURL(awakeSkill_2.value?.icon ?? '')}
                    ></img>
                    <div class="w-100% mt-1px flex items-center justify-center text-#ffc701">2次</div>
                  </div>
                </div>
              </>
            )}
          </div>
        </>
      )
    }

    const renderSkillAction = (skill: ISkill) => (
      <>
        <>
          <div class="absolute skill-active w-88px h-78px translate-x--50% left-16px top--1px">
              <div class="flex justify-between px-5px relative top-55px">
                <img
                  src={`${new URL('./img/min.svg', import.meta.url).href}`}
                  onClick={(e: Event) => {
                    e.stopPropagation()
                    actionSkillLv(skill, 'subMax')
                  }}
                ></img>
                <img
                  src={`${new URL('./img/sub.svg', import.meta.url).href}`}
                  onClick={(e: Event) => {
                    e.stopPropagation()
                    actionSkillLv(skill, 'sub')
                  }}
                ></img>
                <img
                  src={`${new URL('./img/add.svg', import.meta.url).href}`}
                  onClick={(e: Event) => {
                    e.stopPropagation()
                    actionSkillLv(skill, 'add')
                  }}
                ></img>
                <img
                  src={`${new URL('./img/max.svg', import.meta.url).href}`}
                  onClick={(e: Event) => {
                    e.stopPropagation()
                    actionSkillLv(skill, 'addMax')
                  }}
                ></img>
              </div>
          </div>
        </>
      </>
    )

    return () => (
      <>
        <div onClick={() => (activeSkill.value = -1)}>
          {((getSkill(0, 15, -1) ?? []) as ISkill[]).length > 0 && (
            <>
              <div class="skill-tree-line flex items-center gap-10px px-10px">
                <div class="w-34px h-34px flex items-center justify-center text-white">
                  其<br />余
                </div>
                {((getSkill(0, 15, -1) ?? []) as ISkill[])?.map((skill, index) =>
                  renderSkill(skill, index),
                )}
              </div>
            </>
          )}

          {lvList.map((lv, index) =>
            ((getSkill(lv, lvList[index + 1] ?? 150, -1) as ISkill[])?.length ?? 0) > 0 ? (
              <div class="skill-tree-line flex items-center gap-10px px-10px" key={index}>
                {lv == 1 || lv % 10 == 0 ? (
                  <div class="w-34px h-34px flex items-center justify-center text-white">{lv}</div>
                ) : (
                  <div class="w-34px h-34px"></div>
                )}
                {columns.map((column, i) => {
                  const skill = getSkill(lv, lvList[index + 1] ?? 150, column) as ISkill
                  return skill ? renderSkill(skill, index) : <div class="w-34px h-34px"></div>
                })}
                <div class="w-20px h-34px" onClick={() => (activeSkill.value = -1)}></div>
              </div>
            ) : (
              <></>
            ),
          )}
        </div>
      </>
    )
  },
})
