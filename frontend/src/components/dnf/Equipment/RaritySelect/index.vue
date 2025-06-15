<template>
  <div class="flex gap-8px">
    <template v-for="(rarity, _) in rarities" :key="_">
      <div
        class="w-14px h-14px shadow-[0px_0px_3px_#ffffff_inset,0px_0px_1px_#ffffff40]"
        :style="{ background: rarity.background }"
        @click="choose(rarity.value)"
      >
        <div class="w-14px h-14px" :class="{ active: value === rarity.value }"></div>
      </div>
    </template>
  </div>
</template>

<script lang="ts" setup>
const props = defineProps({})

const value = defineModel<string>()

const rarities = [
  {
    value: '稀有',
    background: '#9879da',
  },
  {
    value: '神器',
    background: '#ef28c1',
  },
  {
    value: '传说',
    background: '#fc8711',
  },
  {
    value: '史诗',
    background: '#fcb600',
  },
  {
    value: '太初',
    background: 'linear-gradient(to bottom, #58fa84 20%, #58decc 40%, #58c6ff 60%)',
  },
]

const choose = (rarity: string) => {
  if (value.value === rarity) {
    value.value = undefined
  } else {
    value.value = rarity
  }
}
</script>

<style lang="scss" scoped>
.active {
  background: url('@/assets/img/control/item_checked.png') no-repeat center;
  background-size: 12px 10px;
}
</style>
