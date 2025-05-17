import { getImageURL, getLocalImageURL } from '@/utils/images'
import type { ISkill } from '@/api/info/type'
import { useVModel } from '@vueuse/core'
import CalcButton from '@/components/calc/button/index.vue'
import CalcCheckbox from '@/components/calc/checkbox/index.vue'
import { renderList } from 'vue'

export default defineComponent({
  name: 'SkillTree',
  props: {
    skills: {
      type: Array as PropType<ISkill[]>,
      default: () => [],
    },
    lvInfo: {
      type: Object as PropType<Record<string, { lv: number, vp:number }>>,
      default: () => ({}),
    },
  },
  setup(props) {
    const lvInfo = useVModel(props, 'lvInfo')
    const skills = computed(() => props.skills.filter((a) => a.hasVP).sort((a, b) => a.learnLv - b.learnLv))

    const currentUsedVP = computed(()=>{
      return Object.keys(lvInfo.value).map(a=>lvInfo.value[a].vp).filter(a=>!!a && a > 0).length
    })

    const itemChecked = (skillID:string,vp:number)=>{
      return computed<boolean>({
        get(){
          if(!lvInfo.value[skillID].vp){
            lvInfo.value[skillID].vp = 0
          }
          return lvInfo.value[skillID]?.vp == vp
        },
        set(value:boolean){
          // 选中当前VP形态 并且当前已选VP大于5 并且当前技能没有VP
          if(value && currentUsedVP.value >= 5 && lvInfo.value[skillID]?.vp == 0){
            return
          }
          if(value){
            lvInfo.value[skillID].vp = vp
          }else{
            lvInfo.value[skillID].vp = 0
          }
        }
      })
    }

    return () => (
      <>
        <div>
          {renderList(skills.value, (item) => (
            <div class="h-100px flex items-center bg-#202020 gap-2 p-1">
              <div class="w-50px text-center">{item.learnLv}</div>
              <div class="w-100px flex flex-col items-center">
                <img class="w-28px h-28px" src={getImageURL(item.icon)} alt={item.name} />
                <div class="skill-name">{item.name}</div>
              </div>
              {renderList(2, (index) => (
                <div class="w-200px h-full flex justify-center bg-black" onClick={() => {
                  itemChecked(item.id.toString(), index).value = !itemChecked(item.id.toString(), index).value
                }}>
                  <div class="flex justify-between w-full h-30px">
                    <div class="w-16px"></div>
                    <div class="relative inline-bloc">
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
                  </div>
                  <CalcCheckbox modelValue={itemChecked(item.id.toString(), index).value}/>
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
