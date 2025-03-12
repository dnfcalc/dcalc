<template>
  <div class="relative w-550px h-auto">
    <template v-for="item in infoStore.skills" :key="item.id">
      <div
        class="absolute w-34px h-auto flex flex-col gap-2px py-2px items-center bg-#2c2d2c rounded-2px"
        :style="skillPositon(item.learnLv, item.positon)"
      >
        <img class="w-30px h-30px" :src="getImageURL(item.icon)" :alt="item.name" />
        <div class="flex-1 bg-black text-white">100级</div>
      </div>
    </template>
    <template v-for="lv of 21" :key="lv">
      <div class="skill-tree-line flex items-center px-20px text-#373837">
        {{ lv % 2 === 1 ?  Math.max(1, (lv - 1) * 5) :'' }}
      </div>
    </template>
  </div>
</template>

<script lang="ts" setup>
import { useInfoStore } from '@/stores'
import { getImageURL } from '@/utils/images'

const infoStore = useInfoStore()

const skillPositon = (learnLv: number, positon: number) => {
  return {
    positon: 'absolute',
    left: `${positon * 50 + 50}px`,
    top: `${Math.floor(learnLv / 5) * 80 + 8}px`,
  }
}
</script>

<style lang="scss" scoped>
.skill-tree-line {
  height: 80px;
  width: auto;
  &:nth-child(n + 1) {
    background-color: #000000;
  }
  &:nth-child(2n + 1) {
    background-color: #202020;
    backdrop-filter: blur(1px);
  }
}
</style>
