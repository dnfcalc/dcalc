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
    const skills = computed(() =>
      props.skills.filter((a) => a.hasReinforce && (!lvInfo.value[a.id]?.reinforce || lvInfo.value[a.id]?.reinforce == 0)).sort((a, b) => a.learnLv - b.learnLv),
    )

    const reinforce = (type: number, id: number) => {
      return computed({
        get() {
          return lvInfo.value[id].reinforce
        },
        set(value) {},
      })
    }

    return () => (
      <>
        <div class="flex pt-10px bg-black">
          <div class="skill-reinforce relative">
            <div class="absolute left-55px top-150px w-250px flex flex-col gap-25px">
              {renderList(3, (index) => (
                <>
                  <div class="w-180px h-40px flex items-center justify-between pl-10px pr-10px">
                    <CaclIconSelect class="!mt-3px !ml--1px !bg-white/0 !border-white/0" columnNum={4} >
                      {renderList(skills.value, (item) => (
                        <>
                        <CalcOption value={item.id} key={item.id}>
                          <img  src={getImageURL(item.icon)} alt={item.name} />
                        </CalcOption>
                        </>
                      ))}
                    </CaclIconSelect>
                    <CalcButton icon="exchange"></CalcButton>
                    <CaclIconSelect class="!mt-3px !bg-white/0 !border-white/0" columnNum={4} >
                      {renderList(skills.value, (item) => (
                        <>
                        <CalcOption value={item.id} key={item.id}>
                          <img  src={getImageURL(item.icon)} alt={item.name} />
                        </CalcOption>
                        </>
                      ))}
                      </CaclIconSelect>
                  </div>
                </>
              ))}
            </div>
            <div class="absolute top-80px left-300px w-320px h-270px flex flex-wrap content-start gap-15px py-5px px-30px box-border">
              {renderList(skills.value, (item) => (
                <div
                  key={item.id}
                  class="w-28px h-28px border-1px border-solid border-#3C2E1D rounded-4px"
                >
                  <img src={getImageURL(item.icon)} alt={item.name} />
                </div>
              ))}
              {renderList(36 - skills.value.length, (item) => (
                <div
                  key={item}
                  class="w-28px h-28px border-1px border-solid border-#3C2E1D rounded-4px bg-#0B0D0A"
                ></div>
              ))}
            </div>
          </div>
        </div>
      </>
    )
  },
})
