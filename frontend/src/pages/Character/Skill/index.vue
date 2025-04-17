<template>
  <div>
    <div class="h-90vh w-auto overflow-y-auto overflow-x-hidden">
      <SkillTree :skills="infoStore.skills" v-model:lvInfo="configStore.config.skills" v-model:bindAwake="configStore.config.bindAwake"></SkillTree>
    </div>
  </div>
</template>


<script lang="ts" setup name="Index">
import { useInfoStore } from '@/stores/info'
import SkillTree from './components/SkillTree/index'
import { useConfigStore } from '@/stores'
const props = defineProps<{
  alter: string
}>()
const infoStore = useInfoStore()
const configStore = useConfigStore()
</script>
