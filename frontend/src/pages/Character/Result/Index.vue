<template>
  <div class="flex gap-2" v-if="configStore.result.state">
    <Info :suits="configStore.result.state.suits" :info="configStore.result.state.info" :equs="configStore.config.equips"></Info>
    <Skill :data="configStore.result.state.skills"></Skill>
  </div>
</template>

<script setup lang="ts">
import { useConfigStore } from '@/stores';
import Info from './components/Info.vue';
import Skill from './components/Skill.vue';

const configStore = useConfigStore();
</script>

<style scoped lang="scss">

</style>
