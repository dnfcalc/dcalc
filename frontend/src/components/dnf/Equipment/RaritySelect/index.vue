<template>
  <div class="flex gap-8px">
    <template v-for="(rarity,_) in rarities" :key="_">
      <div class="w-14px h-14px shadow-[0px_0px_3px_#ffffff_inset,0px_0px_1px_#ffffff40]" :style="{background: rarity.background}" @click="value=rarity.value">
        <div class="w-14px h-14px" :class="{'active': value === rarity.value}"></div>
      </div>
    </template>
  </div>
</template>

<script lang="ts" setup>

const value = defineModel<string>()

const rarities = [{
  value: '稀有',
  background: '#d06eff',
},{
  value: '神器',
  background: '#fe11ff',
},{
  value: '传说',
  background: '#fc8711',
},{
  value: '史诗',
  background: '#feca11',
},{
  value: '太初',
  background: 'linear-gradient(180deg, #70faa7 0%, #7bfefe 100%)',
}]

</script>

<style lang="scss" scoped>

.active{
  background: url('@/assets/img/control/item_checked.png') no-repeat center;
  background-size: 12px 10px;
}
</style>
