<template>
  <div
    class="pos-relative w-264px h-full"
    :style="{ backgroundImage: withBg ? `url(${getImageURL('/common/oath/head.png')})` : 'none' }"
  >
    <template v-for="part in parts" :key="part">
      <div
        class="pos-absolute text-white/50 w-26px h-26px border-1px border-solid border-#7a7a7a/50 flex items-center justify-center"
        :style="infoStyle(part)"
        @click="choosePart(part)"
      >
        <template v-if="detail?.[part]?.id">
          <EquipmentIcon :equipment="equ(detail[part].id, part)" useDisplayUrl />
        </template>
        <template v-else-if="!withBg">
          {{ part != '11' ? '星蕴' : '誓约' }}
        </template>
      </div>
      <!-- <div v-if="detail?.[part]?.fusion" class="pos-absolute" :style="fusionStyle(part)">
        <EquipmentIcon :equipment="oaths(detail[part].fusion)" />
      </div> -->
    </template>
    <!-- <img
      v-if="props.avatar"
      :src="props.avatar"
      alt="Avatar"
      class="pos-absolute w-70% left-1/2 translate-x--1/2 -bottom-10px"
    /> -->
  </div>
</template>

<script lang="ts" setup name="EquList">
import { getImageURL } from '@/utils/images'
import EquipmentIcon from '@/components/dnf/Equipment/Icon/index.vue'
import { useInfoStore, type IConfigOath } from '@/stores'

const props = defineProps({
  withBg: {
    type: Boolean,
    default: true,
  },
  detail: {
    type: Object as PropType<Record<string, IConfigOath>>,
  },
})
const partModelValue = defineModel('part', { default: '0' })
const infoStore = useInfoStore()

const parts = computed(() => {
  const parts = infoStore.oathParts
  return parts
})

const equ = (id: string, part: string) => {
  return infoStore.oaths.find((e) => e.id == id && e.oathPos == part)
}

const position = [
  {
    x: 30,
    y: 12,
  },
  {
    x: 30,
    y: 46,
  },
  {
    x: 30,
    y: 80.5,
  },
  {
    x: 30,
    y: 114,
  },
  {
    x: 206,
    y: 12,
  },
  {
    x: 206,
    y: 46,
  },
  {
    x: 206,
    y: 80.5,
  },
  {
    x: 206,
    y: 114,
  },
  {
    x: 74,
    y: 131.5,
  },
  {
    x: 118,
    y: 145.5,
  },
  {
    x: 162,
    y: 131.5,
  },
  {
    x: 118,
    y: 111,
  },
]

const positionSimple = [
  {
    x: 30,
    y: 12,
  },
  {
    x: 30,
    y: 46,
  },
  {
    x: 30,
    y: 80.5,
  },
  {
    x: 30,
    y: 114,
  },
  {
    x: 206,
    y: 12,
  },
  {
    x: 206,
    y: 46,
  },
  {
    x: 206,
    y: 80.5,
  },
  {
    x: 206,
    y: 114,
  },
  {
    x: 74,
    y: 114,
  },
  {
    x: 118,
    y: 114,
  },
  {
    x: 162,
    y: 114,
  },
  {
    x: 118,
    y: 80.5,
  },
]

const infoStyle = (part: string) => {
  if (props.withBg)
    return {
      left: `${position[parseInt(part)].x}px`,
      top: `${position[parseInt(part)].y}px`,
      zIndex: 6,
      // fontWeight: 900,
    }
  else
    return {
      left: `${positionSimple[parseInt(part)].x}px`,
      top: `${positionSimple[parseInt(part)].y}px`,
      zIndex: 6,
      // fontWeight: 900,
    }
}

const choosePart = (part: string) => {
  partModelValue.value = part
}
</script>

<style lang="scss" scoped></style>
