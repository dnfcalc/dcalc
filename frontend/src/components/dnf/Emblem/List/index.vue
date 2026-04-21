<template>
  <div class="pos-relative w-248px h-full" :class="props.withBg ? 'emblem-bg' : ''">
    <template v-for="part in parts" :key="part">
      <div
        class="pos-absolute text-white/50 flex items-center justify-center rounded-50%"
        :style="infoStyle(part)"
        @click="choosePart(part)"
      >
        <img
          class="w-20px h-20px"
          style="object-fit: none; object-position: hue; mix-blend-mode: screen"
          :src="rarityIcon(part)"
          v-if="part != '白金'"
        />
        <img class="pos-absolute" :style="lvStyle" :src="lvIcon(part)" v-if="part != '白金'" />
      </div>
    </template>
  </div>
</template>

<script lang="ts" setup name="EmblemList">
import { useInfoStore, type IConfigEmblem } from '@/stores'
import { getImageURL } from '@/utils/images'

const props = defineProps({
  withBg: {
    type: Boolean,
    default: true,
  },
  detail: {
    type: Object as PropType<Record<string, IConfigEmblem>>,
  },
})

const infoStore = useInfoStore()
const partModelValue = defineModel('part', { default: '彩色' })

const partIcon = computed(() => {
  return (part: string) => {
    return new URL(`../Images/part/${part}.png`, import.meta.url).href
  }
})

const rarityIcon = computed(() => {
  return (part: string) => {
    const rarity = Math.floor((props.detail?.[part]?.lv || 0) / 5)
    console.log(rarity)
    return new URL(`../Images/rarity/${rarity}.png`, import.meta.url).href
  }
})

const lvIcon = computed(() => {
  return (part: string) => {
    const lv = (props.detail?.[part]?.lv || 0) % 5
    return getImageURL(`/equipment/adaptation/${lv + 1}.png`)
  }
})

const position: Record<string, { x: number; y: number; width?: number; height?: number }> = {
  彩色: {
    x: 99,
    y: 15,
  },
  红色: {
    x: 18,
    y: 39,
  },
  蓝色: {
    x: 180,
    y: 39,
  },
  黄色: {
    x: 65,
    y: 83,
  },
  绿色: {
    x: 133,
    y: 83,
  },
  白金: {
    x: 33,
    y: 117,
    width: 24,
    height: 24,
  },
  增益: {
    x: 192,
    y: 117,
    width: 24,
    height: 24,
  },
}

const lvStyle = computed(() => {
  return {
    left: '50%',
    top: '100%',
    transform: 'translate(-50%,-100%)',
    zIndex: 7,
  }
})

const infoStyle = computed(() => {
  return (part: string) => {
    console.log(`url(${rarityIcon.value(part)}),url(${partIcon.value(part)})`)
    return {
      left: `${position[part as keyof typeof position].x}px`,
      top: `${position[part as keyof typeof position].y}px`,
      width: `${position[part as keyof typeof position]?.width ?? 50}px`,
      height: `${position[part as keyof typeof position]?.height ?? 50}px`,
      backgroundImage: `url(${partIcon.value(part)})`,
      // backgroundImage: `url(${rarityIcon.value(part)}),url(${partIcon.value(part)})`,
      // backgroundImage: `url(${partIcon.value(part)}),url(${rarityIcon.value(part)})`,
      // backgroundBlendMode: 'screen',
      zIndex: 6,
      // fontWeight: 900,
    }
  }
})

const parts = computed(() => {
  const parts = infoStore.emblemParts
  return parts
})

const choosePart = (part: string) => {
  partModelValue.value = part
}
</script>

<style lang="scss" scoped>
.emblem-bg {
  background-image: url(../Images/head.png);
}
</style>
