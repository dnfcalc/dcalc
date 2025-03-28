import { getImageURL } from '@/utils/images'
import type { ISkill } from '@/api/info/type'
import { useVModel } from '@vueuse/core'
import './style.scss'
import CalcButton from '@/components/calc/button/index.vue'

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
  },
  setup(props) {
    const skills = computed(() => props.skills)
    const lvInfo = useVModel(props, 'lvInfo')

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

    const columns = [...new Array(9).keys()]

    const activeSkill = ref<number>(-1)

    const chooseSkill = (skill?: ISkill, operation: string = 'add') => {
      if (!skill) {
        activeSkill.value = -1
        return
      }
      if (activeSkill.value == skill.id) actionSkillLv(skill, operation)
      else activeSkill.value = skill.id
    }

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

    const renderSkill = (skill: ISkill, index: number) => (
      <>
        <div class="relative w-35px h-55px">
          {activeSkill.value == skill.id && renderSkillAction(skill)}
          <div
            class="w-34px absolute h-auto flex flex-col gap-2px py-2px items-center bg-#2c2d2c rounded-2px z-2 top-1px left-1px"
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
              class={['h-30px w-30px', skill.type === 'passive' ? 'passive' : '']}
              src={getImageURL(skill.icon)}
            ></img>
            <div class="w-30px mx-2px bg-black text-white flex items-center justify-center rounded-2px">
              {lvInfo.value?.[skill.id.toString()]?.lv ?? 0}
            </div>
          </div>
        </div>
      </>
    )

    const renderSkillAction = (skill: ISkill) => (
      <>
        <>
          <div class="absolute">
            <div class="w-36px h-55px bg-gradient-linear bg-gradient-[180deg,#f8e26c_0%,#f87c43_94.34%] z-1"></div>
            <div class="flex bottom--5px relative z-2 transform -translate-x-1/4">
              <CalcButton onClick={(e:Event) => {e.stopPropagation();actionSkillLv(skill, 'subMax')}}>&lt;</CalcButton>
              <CalcButton onClick={(e:Event) => {e.stopPropagation();actionSkillLv(skill, 'sub')}}>-</CalcButton>
              <CalcButton icon="plus" onClick={(e:Event) => {e.stopPropagation();actionSkillLv(skill, 'add')}}></CalcButton>
              <CalcButton icon="next" onClick={(e:Event) => {e.stopPropagation();actionSkillLv(skill, 'addMax')}}></CalcButton>
            </div>
          </div>
        </>
      </>
    )

    return () => (
      <>
        <div onClick={() => (activeSkill.value = -1)}>
          <div class="skill-tree-line flex items-center gap-10px px-10px">
            <div class="w-34px h-34px flex items-center justify-center text-white">
              其<br />余
            </div>
            {((getSkill(0, 15, -1) ?? []) as ISkill[])?.map((skill, index) =>
              renderSkill(skill, index),
            )}
          </div>
          {lvList.map((lv, index) => (
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
              <div class="w-34px h-34px" onClick={() => (activeSkill.value = -1)}></div>
            </div>
          ))}
        </div>
      </>
    )
  },
})
