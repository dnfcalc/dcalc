<template>
    <div class="flex flex-col mx-10px">
      <calc-collapse title="武器">
        <Weapon></Weapon>
      </calc-collapse>
      <calc-collapse title="套装">
        <Suit></Suit>
      </calc-collapse>
      <calc-collapse title="通宝">
        <Universal></Universal>
      </calc-collapse>
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
