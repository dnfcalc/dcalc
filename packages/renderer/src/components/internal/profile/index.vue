<script lang="tsx">
import { useVModel } from "@vueuse/core"
import type { PropType } from "vue"
import { defineComponent, onMounted, ref } from "vue"
import Detail from "./detail.vue"
import Equipments from "./equipments.vue"
import Cus from "./cus.vue"
import type { IEquipmentInfo } from "@/api/info/type"
import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"
import type { IResultInfo } from "@/api/character/type"
import { useBasicInfoStore } from "@/store"

interface DelearProperties {
  技能攻击力: number
  面板技能攻击力: number
  攻击强化: number
  百分比攻击强化: number
  MP消耗量: number
  伤害比例: number[]
  伤害系数: number[]
  无色消耗: number
  攻击速度: number
  出血抗性: number
  中毒抗性: number
  灼伤抗性: number
  感电抗性: number
  冰冻抗性: number
  减速抗性: number
  眩晕抗性: number
  诅咒抗性: number
  失明抗性: number
  石化抗性: number
  睡眠抗性: number
  混乱抗性: number
  束缚抗性: number
  cdr: [string, number]
  冷却缩减: number
  冷却恢复: number
  技能范围: number
  保护罩: number
  施放速度: number
  移动速度: number
}

interface BufferProperties {
  buffer_power: number
  buffer_power_value: number
  buffer_power_per: number
  buff_name: string
  buff_level: number
  awake_name: string
  awake_level: number
  apply_value: number
}

interface IDetail {
  name?: string
  alter?: string

  fame?: number

  站街?: {
    智力?: number
    力量?: number
    体力?: number
    精神?: number
    物理攻击?: number
    魔法攻击?: number
    独立攻击?: number
    火?: number
    冰?: number
    光?: number
    暗?: number
    火抗?: number
    冰抗?: number
    光抗?: number
    暗抗?: number
  }
  jintu?: {
    智力?: number
    力量?: number
    物理攻击?: number
    魔法攻击?: number
    独立攻击?: number
    火?: number
    冰?: number
    光?: number
    暗?: number
    火抗?: number
    冰抗?: number
    光抗?: number
    暗抗?: number
  }
  properties?: DelearProperties & BufferProperties
  buffer_addition: [number, number, number, number]
}


interface MergeInfo {
  weaponType?: string
  merges: ID[]
}

export default defineComponent({
  name: "Profile",
  components: { EquipTips },
  props: {
    withStandard:{
      type: Boolean,
      default: true
    },
    charName: {
      type: String,
      default: null
    },
    showCD: {
      type: Boolean,
      default: true
    },
    details: {
      type: Object as PropType<IDetail>,
      default: () => {
        return {
          fame: 0,
          站街: { 火: 0, 冰: 0, 光: 0, 暗: 0, 火抗: 0, 冰抗: 0, 光抗: 0, 暗抗: 0 },
          role: "delear",
          properties: {
            技能攻击力: 0,
            攻击强化: 0,
            百分比攻击强化: 0,
            MP消耗量: 0,
            伤害比例: [1, 0, 0, 0, 0],
            伤害系数: [1, 1, 1, 1, 1]
          },
          buffer_addition: [0, 0, 0, 0]
        }
      }
    },
    share: {
      type: Object as PropType<IResultInfo<"delear" | "buffer">>,
      default: undefined
    },
    role: {
      type: String as PropType<"delear" | "buffer">,
      default: () => "delear"
    },
    canChoose: {
      type: Boolean,
      default: false
    },
    showSubDetail: {
      type: Boolean,
      default: true
    },
    equList: {
      type: Array as PropType<IEquipmentInfo[]>,
      default: () => []
    },
    fusionList: {
      type: Array as PropType<ID[]>,
      default: () => []
    },
    totalData: {
      type: Array as PropType<number[]>,
      default: () => {
        return [0]
      }
    },
    standardData: {
      type: Array as PropType<number[]>,
      default: () => {
        return [0]
      }
    },
    // eslint-disable-next-line vue/prop-name-casing
    equips_forge: {
      type: Object,
      default: undefined
    },
    part: {
      type: String,
      default: ""
    },
    showZF: {
      type: Boolean,
      default: true
    },
    showTM: {
      type: Boolean,
      default: true
    },
    tipInfo: {
      type: Array as PropType<number[]>,
      default: () => [0, 1, 2]
    },
    mergeInfo: {
      type: Object as PropType<MergeInfo>
    },
    showTips: {
      type: Boolean,
      default: true
    },
    withBG: {
      type: Boolean,
      default: true
    }
  },
  setup(props, { emit }) {
    const tab = ref("detail")
    const partModelValue = useVModel(props, "part", emit, { passive: true });
    const infoStore = useBasicInfoStore()
    onMounted(() => {
      !infoStore.entry_list && infoStore.loadEntries()
    })

    return () => (
      <div class="char-info">
        <Equipments charName={props.charName} share={props.share} canChoose={props.canChoose} equList={props.equList} fusionList={props.fusionList} equips_forge={props.equips_forge} v-model:part={partModelValue.value} showZF={props.showZF} showTM={props.showTM} tipInfo={props.tipInfo} mergeInfo={props.mergeInfo} showTips={props.showTips} withBG={props.withBG}/>
        <div class="bg-hex-000">
          <calc-tabs v-model={tab.value}>
            <calc-tab value="detail">伤害信息</calc-tab>
            <calc-tab value="cus">自定义</calc-tab>
          </calc-tabs>
        </div>
        {tab.value == "detail" && (<Detail withStandard={props.withStandard} showCD={props.showCD} details={props.details} role={props.role} totalData={props.totalData} standardData={props.standardData} showSubDetail={props.showSubDetail}/>)}
        {tab.value == "cus" && (
          <Cus equList={props.equList}/>)}
      </div>
    )
  }
})
</script>

<style lang="scss" scoped>
  .char-info {
    width: 266px;
    position: relative;
    padding: 5px;
  }

  .i-tabs {
    height: 22px;
    padding-left: 5px;
    border:none
  }
  .i-tab {
    max-width: 25%;
    min-width: 10%;
    height: 18px;
    line-height: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    &.active{
      height: 20px;
    }
  }
</style>
