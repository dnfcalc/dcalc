<template>
  <template v-if="props.equipment">
    <div class="relative" :class="{inactive: props.inactive}">
      <div class="w-28px h-28px " :style="{ backgroundImage: `url(${getImageURL('equipment' + props.equipment?.imageUrl)})` }">
      <img :src="getLocalImageURL(`./rarity/${rarity}.png`)" />
    </div>
    </div>
  </template>
  <template v-else>
    <div class="w-26px h-26px border-1px border-solid  border-#7a7a7a/50"></div>
  </template>

</template>


<script lang="ts" setup>
import type { IEquipment } from '@/api/info/type';
import { getImageURL } from '@/utils/images'

const props = defineProps<{
  equipment?: IEquipment
  inactive?: boolean
}>()

const rarity = computed(()=>{
  switch(props.equipment?.rarity){
    case '稀有':
      return 'rare'
    case '神器':
      return 'artifact'
    case '传说':
      return 'legend'
    case '史诗':
      return 'epic'
    case '太初':
      return 'primeval'
    default:
      return ''
  }
})

const getLocalImageURL = (url:string)=>{
  return new URL(url, import.meta.url).href
}

</script>

<style lang="scss" scoped>

// @keyframes primeval {
//   @for $i from 0 through 29 {
//     #{percentage($i / 29)} {
//       background-image: url("./effect/primeval/#{$i}.png");
//     }
//   }
// }

// .primeval_effect {
//   width: 28px;
//   height: 28px;
//   background-size: cover;
//   animation: primeval 2s infinite;
//   //  设置动画名称，持续时间，和循环次数
//   mix-blend-mode: color-dodge;
// }

.inactive {
  &::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    width: 28px;
    height: 28px;
    background-color: #00000060;
  }
}

</style>
