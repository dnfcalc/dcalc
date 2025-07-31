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
      <!-- 装备图标 装备名称 -->
      <div class="flex w-full items-center justify-center gap-5px">
        <div>
          <img
            :src="getImageURL('equipment' + props.suit?.imageUrl.replace('/suit/', '/suit/icon/'))"
            alt="装备图标"
          />
        </div>
        <div :class="rarity">{{ props.suit?.name }}</div>
        <div :class="rarity">{{ props.suit?.point }}点</div>
      </div>
      <div class="divide"></div>
      <!-- 装备基础信息 -->
      <div
        class="flex flex-col items-start my-1px"
        style="white-space: pre-wrap; line-height: 15px"
      >
        <div class="text-#908150" v-html="mainAttr"></div>
      </div>
      <!-- 装备属性 -->
      <div class="divide"></div>
      <div class="flex flex-col items-start my-1px whitespace-pre-wrap leading-15px">
        <div class="text-#DED29A py-4px whitespace-pre-wrap" v-html="detail"></div>
      </div>

      <template v-if="bufferDetail">
        <div class="divide"></div>
        <div class="flex flex-col items-start my-1px whitespace-pre-wrap leading-15px">
          <div class="text-#A48B2E mb-10px pt-4px">辅助职业专属属性</div>
          <div class="text-#DED29A pb-10px whitespace-pre-wrap" v-html="bufferDetail"></div>
        </div>
      </template>
    </div>
  </div>

  <!-- 奶系专属 -->
</template>

<script lang="ts" setup>
import type { IEquipment, ISuit } from '@/api/info/type'
import { getImageURL } from '@/utils/images'
import { formatAttr, rarityClass } from '@/utils'

const props = defineProps<{
  suit?: ISuit
}>()

const rarity = computed(() => rarityClass(props.suit?.rarity ?? ''))

const mainAttr = computed(() => {
  const attrs: (keyof ISuit)[] = ['SkillAttack', 'Buffer']
  let info = ''
  for (const attr of attrs) {
    const item = props.suit?.[attr] as number
    if (item) {
      info += `${formatAttr(attr, item)}\n`
    }
  }
  return info
})

const detail = computed(() =>
  props.suit?.value.replace(/\[([^\[\]技能]+?)\]/g, '<span style="color:#3d9147">[$1]</span>'),
)

const bufferDetail = computed(() => {
  const detail = props.suit?.bufferValue
  if (!detail || detail == '-') return undefined
  return props.suit?.bufferValue.replace(
    /\[(?![^\]]*技能)[^\[\]]+\]/g, match => `<span style="color:#3d9147">${match}</span>`
  )
})
</script>

<style lang="scss" scoped>
.divide {
  border-top: 1px solid rgba(243, 244, 246, 0.3);
  margin: 2px 0;
}
</style>
