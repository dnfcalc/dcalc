<template>
  <div
    class="pos-relative w-264px h-full"
    :style="{ backgroundImage: withBg ? `url(${getImageURL('/common/head.png')})` : 'none' }"
  >
    <template v-for="part in parts" :key="part">
      <div
        class="pos-absolute text-white/50 w-26px h-26px border-1px border-solid border-#7a7a7a/50 flex items-center justify-center"
        :style="infoStyle(part)"
        @click="choosePart(part)"
      >
        <template v-if="detail?.[part]?.id">
          <EquipmentIcon :equipment="equ(detail[part].id)" />
        </template>
        <template v-else>
          {{ partName(part) }}
        </template>
      </div>
      <div v-if="detail?.[part]?.fusion" class="pos-absolute" :style="fusionStyle(part)">
        <EquipmentIcon :equipment="stones(detail[part].fusion)" />
      </div>
    </template>
    <div
      v-if="props.withSubWeapon"
      class="pos-absolute text-white/50 w-26px h-26px border-1px border-solid border-#7a7a7a/50 flex items-center justify-center"
      style="left: 150px; top: 5px; z-index: 8"
      @click="choosePart('副武器')"
    >
      <template v-if="detail?.['副武器']?.id">
        <EquipmentIcon :equipment="equ(detail['副武器'].id)" />
      </template>
      <template v-else> 副武 </template>
    </div>
  </div>
</template>

<script lang="ts" setup name="EquList">
import { getImageURL } from '@/utils/images'
import { useVModel } from '@vueuse/core'
import EquipmentIcon from '@/components/dnf/Equipment/Icon/index.vue'
import { useInfoStore, useConfigStore, type IConfigEquip } from '@/stores'

const props = defineProps({
  part: {
    type: String,
    default: '',
  },
  withBg: {
    type: Boolean,
    default: true,
  },
  withPet: {
    type: Boolean,
    default: true,
  },
  detail: {
    type: Object as PropType<Record<string, IConfigEquip>>,
  },
  withSubWeapon: {
    type: Boolean,
    default: false,
  },
})
const partModelValue = useVModel(props, 'part')
const infoStore = useInfoStore()

const parts = computed(() => {
  const configStore = useConfigStore()
  const parts = infoStore.parts.filter((part) => {
    if (part == '宠物' && !props.withPet) return false
    if (configStore.config.equips[part]) {
      return true
    }
    return false
  })
  return parts
})

const equ = (id: string) => {
  return infoStore.equips.find((e) => e.id == id)
}

const stones = (id: string) => {
  return infoStore.stones.find((e) => e.id == id)
}

const infoStyle = (part: string) => {
  let x = 10
  let y = 5
  let index = infoStore.parts.findIndex((p) => p == part)
  if (index == 13) {
    index -= 7
  } else if (index >= 5 && index <= 12) {
    x += 179
    index -= 5
  }

  x += (index % 2) * 39
  y += Math.floor(index / 2) * 34

  const style = {
    left: `${x}px`,
    top: `${y}px`,
    zIndex: 6,
    // fontWeight: 900,
  }
  return style
}

const fusionStyle = (part: string) => {
  let x = 0
  let y = 15
  let index = infoStore.parts.findIndex((p) => p == part)

  if (index >= 5 && index <= 12) {
    x += 179
    index -= 5
  }

  if (index == 13) {
    index = 5
  }

  x += (index % 2) * 39
  y += Math.floor(index / 2) * 34

  return {
    left: `${x}px`,
    top: `${y}px`,
    zIndex: 7,
    transform: 'scale(0.6)',
  }
}
const choosePart = (part: string) => {
  partModelValue.value = part
}

const partName = (part: string) => {
  if (part == '辅助装备') return '左槽'
  if (part == '魔法石') return '右槽'
  return part
}
</script>

<style lang="scss" scoped></style>
