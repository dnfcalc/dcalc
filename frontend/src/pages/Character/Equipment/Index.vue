<template>
    <div class="flex flex-col gap-20px mx-10px">
      <Weapon></Weapon>
      <Suit></Suit>
      <Universal></Universal>
    </div>
</template>

<script lang="ts" setup name="Index">
import { useInfoStore } from '@/stores/info'
import { getImageURL } from '@/utils/images'
import Suit from './components/Suit.vue'
import Weapon from './components/Weapon.vue'
import Universal from './components/Universal.vue'
import { useConfigStore } from '@/stores'
const props = defineProps<{
  alter: string
}>()

</script>
