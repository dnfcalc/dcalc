<template>
  <div>
    <calc-tabs v-model="tab">
      <calc-tab :value="0">技能加点</calc-tab>
      <calc-tab :value="1">技能VP</calc-tab>
      <calc-tab :value="2">技能突破</calc-tab>
    </calc-tabs>
    <div class="h-90vh w-auto overflow-y-auto overflow-x-hidden">
      <SkillTree
        :skills="infoStore.skills"
        v-model:lvInfo="configStore.config.skills"
        v-model:bindAwake="configStore.config.bindAwake"
        v-if="tab === 0"
      ></SkillTree>
      <SkillVP
        :skills="infoStore.skills"
        v-model:lvInfo="configStore.config.skills"
        v-model:bindAwake="configStore.config.bindAwake"
        v-if="tab === 1"
      ></SkillVP>
    </div>
  </div>
</template>

<script lang="ts" setup name="Index">
import { useInfoStore } from '@/stores/info'
import SkillTree from './components/SkillTree/index'
import SkillVP from './components/SkillReinforce';
import { useConfigStore } from '@/stores'
const props = defineProps<{
  alter: string
}>()
const tab = ref(0)
const infoStore = useInfoStore()
const configStore = useConfigStore()
</script>
