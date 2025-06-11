import { getImageURL, getLocalImageURL } from '@/utils/images'
import type { ISkill } from '@/api/info/type'
import { useVModel } from '@vueuse/core'
import CalcButton from '@/components/calc/button/index.vue'
import CalcCheckbox from '@/components/calc/checkbox/index.vue'
import { renderList } from 'vue'
import './style.scss'
export default defineComponent({
  name: 'SkillVP',
  props: {
    skills: {
      type: Array as PropType<ISkill[]>,
      default: () => [],
    },
    lvInfo: {
      type: Object as PropType<Record<string, { lv: number; vp: number }>>,
      default: () => ({}),
    },
  },
  emits: ['chooseSkill'],
  setup(props,{ emit }) {
    const lvInfo = useVModel(props, 'lvInfo')
    const skills = computed(() =>
      props.skills.filter((a) => a.hasVP && lvInfo).sort((a, b) => a.learnLv - b.learnLv),
    )

    const currentUsedVP = computed(() => {
      return Object.keys(lvInfo.value)
        .map((a) => lvInfo.value[a].vp)
        .filter((a) => !!a && a > 0).length
    })

    const itemChecked = (skillID: string, vp: number) => {
      return computed<boolean>({
        get() {
          if (!lvInfo.value[skillID].vp) {
            lvInfo.value[skillID].vp = 0
          }
          return lvInfo.value[skillID]?.vp == vp
        },
        set(value: boolean) {
          // 选中当前VP形态 并且当前已选VP大于5 并且当前技能没有VP
          if (value && currentUsedVP.value >= 5 && lvInfo.value[skillID]?.vp == 0) {
            return
          }
          if (value) {
            lvInfo.value[skillID].vp = vp
          } else {
            lvInfo.value[skillID].vp = 0
          }
        },
      })
    }

    return () => (
      <>
        <div class="h-auto py-2 flex flex-col bg-#080808 box-content">
          {renderList(skills.value, (item) => (
            <div class="h-140px flex items-center vp pl-26px pr-16px box-content">
              <div class="w-30px text-center text-#816f4c">{item.learnLv}</div>
              <div class="w-150px flex gap-5px items-center">
                <div class="border-1px border-solid border-#3F382E rounded-4px w-28px h-28px">
                  <img class="w-28px h-28px" src={getImageURL(item.icon)} alt={item.name} />
                </div>
                <div class="skill-name">{item.name}</div>
              </div>
              {renderList(2, (index) => (
                <div
                  class={[
                    'flex items-center flex-col vp-item py-10px',
                    index == 1 ? 'ml-auto' : 'ml-2px',
                  ]}
                  onClick={() => {
                    emit("chooseSkill");
                    itemChecked(item.id.toString(), index).value = !itemChecked(
                      item.id.toString(),
                      index,
                    ).value
                  }}
                > <div class={["box-border w-full h-full pt-5px m-2px",itemChecked(item.id.toString(), index).value ? "selected": ""]} >
                  <div class="flex justify-between w-full h-30px px-10px box-border">

                    <div class="flex items-start">
                      <CalcCheckbox
                        modelValue={itemChecked(item.id.toString(), index).value}
                        disabled={
                          currentUsedVP.value >= 5 && lvInfo.value[item.id.toString()]?.vp == 0
                        }
                      />
                    </div>
                    <div class="relative inline-block border-1px border-solid border-#3F382E rounded-4px w-28px h-28px">
                      <div
                        class="bg-#a128f4 w-26px h-26px top-1px left-1px absolute z-5"
                        style="mix-blend-mode: hue;"
                      ></div>
                      <img
                        style="filter:brightness(1) contrast(1) saturate(1.5)"
                        class="w-28px h-28px"
                        src={getImageURL(item.icon)}
                        alt={item.name}
                      />
                      <div class={`vp_${index} absolute bottom--8px left-5px z-10`}></div>
                    </div>
                    <div class="w-16px"></div>
                  </div>
                  <div class="text-13px mt-5px text-center selected-name">{item.vps[index - 1]?.name}</div>
                  {renderList(item.vps[index - 1]?.desc.split('<br/>') ?? [], (desc) => (
                    <div class="text-12px text-#816f4c text-center leading-none">{desc}</div>
                  ))}
                  </div>
                </div>
              ))}
            </div>
          ))}
        </div>
      </>
    )
  },
})
