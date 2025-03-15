import { getImageURL } from '@/utils/images'
import type { ISkill } from '@/api/info/type'
import {useVModel} from '@vueuse/core'
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

    return () => (
      <>
        <div>
          <div class="skill-tree-line flex items-center gap-10px px-10px">
            <div class="w-34px h-34px flex items-center justify-center text-white">其<br/>余</div>
            {((getSkill(0, 15, -1) ?? []) as ISkill[])?.map((skill, index) => (
              <div class="w-34px h-auto flex flex-col gap-2px py-2px items-center bg-#2c2d2c rounded-2px" key={index}>
              <img
                class={['h-30px w-30px', skill.type === 'passive' ? 'passive' : '']}
                src={getImageURL(skill.icon)}
              ></img>
              <div class="w-30px mx-2px bg-black text-white flex items-center justify-center rounded-2px">
                {lvInfo.value?.[skill.id.toString()]?.lv ?? 0}
              </div>
              </div>
            ))}
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
                return skill ? (
                  <div class="w-34px h-auto flex flex-col gap-2px py-2px items-center bg-#2c2d2c rounded-2px">
                    <img
                      class={['h-30px w-30px', skill.type === 'passive' ? 'passive' : '']}
                      src={getImageURL(skill.icon)}
                    ></img>
                    <div class="w-30px mx-2px bg-black text-white flex items-center justify-center rounded-2px">
                      {lvInfo.value?.[skill.id.toString()]?.lv ?? 0}
                    </div>
                  </div>
                ) : (
                  <div class="w-34px h-34px"></div>
                )
              })}
              <div class="w-34px h-34px"></div>
            </div>
          ))}
        </div>
      </>
    )
  },
})
