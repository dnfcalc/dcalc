<template>
  <div class="bg-hex-222222">
    <div
      :class="['bg-black text-shadow text-12px h-auto', 'text-hex-9D9476']"
      style="
        width: 220px;
        float: left;
        padding: 5px;
        background-size: 100%;
        background-repeat: no-repeat;
        background-position: center;
        background-color: rgb(0, 0, 0);
      "
    >
      <div class="h-30px flex items-left my-2px">
        <div style="position: relative" class="w-28px mr-2px">
          <Icon :equipment="props.equipment"></Icon>
        </div>
        <div style="line-height: 15px">
          <div :class="[rarity,'pl-5px']">{{ props.equipment?.name }}</div>
          <div class="pl-5px text-#3ea74e">{{ props.equipment?.categorize }}</div>
        </div>
      </div>
      <!-- 装备图标 装备名称 -->

      <div class="divide"></div>
      <div class="flex flex-col items-end my-1px" style="line-height: 15px">
        <div :class="rarity">{{ props.equipment?.rarity }}</div>
        <div class="text-hex-7C6430">{{ props.equipment?.itemDetailType }}</div>
      </div>
        <!-- 装备基础信息 -->
      <div class="divide"></div>
      <div class="flex flex-col items-start my-1px" style="white-space: pre-wrap; line-height: 15px">
          <div class="text-#908150" v-html="mainAttr"></div>
      </div>
      <!-- 装备属性 -->
      <div class="divide"></div>
      <div class="flex flex-col items-start my-1px" style="white-space: pre-wrap; line-height: 15px">
          <div class="text-#DED29A" v-html="detail"></div>
      </div>
      <template v-if="bufferDetail">
        <div class="divide"></div>
          <div class="flex flex-col items-start my-1px" style="white-space: pre-wrap; line-height: 15px">
          <div class="text-#A48B2E mb-10px">辅助职业专属属性</div>
          <div class="text-#DED29A" v-html="bufferDetail"></div>
        </div>
      </template>

    </div>
  </div>



  <!-- 奶系专属 -->
</template>

<script lang="ts" setup>
import type { IEquipment } from '@/api/info/type'
import Icon from '../Icon/index.vue'
import { formatAttr, rarityClass } from '@/utils'

const props = defineProps<{
  equipment?: IEquipment
}>()

const rarity = computed(() => rarityClass(props.equipment?.rarity ?? ''))

const mainAttr = computed(()=>{
  const attrs :(keyof IEquipment)[] = ['STR', 'INT', 'Vitality', 'Spirit','AtkP','AtkM','AtkI','SkillAttack','Attack','Buffer']
  let info = ""
  for (const attr of attrs) {
    const item = props.equipment?.[attr] as number[]
    if (item?.[0]) {
      info += `${formatAttr(attr,item?.[0])}\n`
    }
  }
  return info;


})

const detail = computed(()=>props.equipment?.detail.replace(/\[([^\[\]技能]+?)\]/g, '<span style="color:#3d9147">[$1]</span>'))

const bufferDetail = computed(()=>
{
  const detail = props.equipment?.bufferDetail
  if(!detail || detail == '-') return undefined
  return props.equipment?.bufferDetail.replace(/\[([^\[\]技能]+?)\]/g, '<span style="color:#3d9147">[$1]</span>')
} )

</script>

<style lang="scss" scoped>
.divide {
  border-top: 1px solid rgba(243, 244, 246, 0.3);
}
</style>
