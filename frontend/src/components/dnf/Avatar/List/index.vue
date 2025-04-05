<template>
  <div class="pos-relative w-300px h-full">
    <template v-for="part in infoStore.avatarParts" :key="part">
      <div
        class="pos-absolute text-white/50 w-26px h-26px border-1px border-solid border-#7a7a7a/50 flex items-center justify-center"
        :style="infoStyle(part)"
        @click="choosePart(part)"
      >
        {{ partName(part) }}
      </div>
    </template>
  </div>
</template>

<script lang="ts" setup name="EquList">
import { getImageURL } from '@/utils/images'
import { useVModel } from '@vueuse/core'
import { useInfoStore, useConfigStore } from '@/stores'

const props = defineProps({
  part: {
    type: String,
    default: '',
  },
})
const partModelValue = useVModel(props, 'part')
const infoStore = useInfoStore()

const infoStyle = (part: string) => {
  let x = 15
  let y = 5
  let index = infoStore.avatarParts.findIndex((p) => p == part)
  // if (index == 13) {
  //   index -= 7
  // } else if (index >= 5 && index <= 12) {
  //   x += 179
  //   index -= 5
  // }
  if(part == '宠物'){
    x+= 5*39
    y+= 1*40
  }
  else if (part.includes('宠物装备')) {
    x += 6 * 39
    y += (index - infoStore.avatarParts.findIndex((p) => p == '宠物装备-红')) * 40
  } else {
    x += (index % 4) * 39
    y += Math.floor(index / 4) * 40
  }

  const style = {
    left: `${x}px`,
    top: `${y}px`,
    zIndex: 6,
    // fontWeight: 900,
  }
  return style
}

const choosePart = (part: string) => {
  partModelValue.value = part
}

const partName = (part: string) => {
  if (part == '武器装扮') return '武器'
  if(part == '快捷栏装备') return '快捷'
  return part.replace('宠物装备-', '')
}
</script>

<style lang="scss" scoped></style>
