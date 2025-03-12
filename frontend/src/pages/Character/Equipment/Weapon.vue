<template>
  <div class="flex flex-wrap gap-2px">
    <template v-for="weapon in weapons" :key="weapon.id">
      <div class="w-34px h-34px bg-#2c2d2c rounded-2px flex flex-col items-center">
        <img class="w-30px h-30px" :src="getImageURL('equipment/'+weapon.imageUrl)" :alt="weapon.name" />
      </div>
    </template>
  </div>
</template>

<script lang="ts" setup>
import { useInfoStore } from '@/stores';
import { getImageURL } from '@/utils/images';

const infoStore = useInfoStore()

const weapons = computed(()=>infoStore.equips.filter((equip) => equip.itemType === '武器' && infoStore.infos?.weapons.includes(equip.itemDetailType)))
</script>
