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
      type: Object as PropType<Record<string, { lv: number, reinforce:number }>>,
      default: () => ({}),
    },
  },
  setup(props) {
    const lvInfo = useVModel(props, 'lvInfo')
    const skills = computed(() => props.skills.filter((a) => a.hasReinforce).sort((a, b) => a.learnLv - b.learnLv))

    const reinforce = (type:number,id:number)=>{
      return computed({
        get(){
          return lvInfo.value[id].reinforce
        },
        set(value){

        }
      })
    }

    return () => (
      <>
        <div class="flex">
          <div></div>
          <div></div>
          <div></div>
        </div>
      </>
    )
  },
})
