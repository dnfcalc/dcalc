<template>
  <div class="flex gap-2" v-if="configStore.result.state">
    <div class="flex flex-col justify-between">
      <div class="flex gap-5 items-center">
        <calc-button class="flex-1" @click="setStandard">设为基准</calc-button>
        <calc-button class="flex-1" @click="clearStandard">清空基准</calc-button>
      </div>
      <Info
        :suits="configStore.result.state.suits"
        :info="configStore.result.state.info"
        :equs="configStore.config.equips"
      ></Info>
    </div>
    <Skill v-if="!configStore.result.state.buffer" :data="configStore.result.state.skills" :standard="infoStore.standard"></Skill>
    <BufferSkill v-else :data="configStore.result.state.skills" :stadard="infoStore.standard" :standard="infoStore.standard"></BufferSkill>
  </div>
</template>

<script setup lang="ts">
import { useConfigStore, useInfoStore } from '@/stores'
import Info from './components/Info.vue'
import Skill from './components/Skill.vue'
import BufferSkill from './components/BufferSkill.vue'
import type { IResultSkill } from '@/api/calc/type'

const configStore = useConfigStore()
const infoStore = useInfoStore()

const setStandard = () => {
  if(!configStore?.result?.state?.uuid) return
  infoStore.setStandard(configStore.result.state,configStore.skillCountConfig)
}

const clearStandard = () => {
  infoStore.setStandard(undefined)
}
</script>

<style scoped lang="scss"></style>
