<template>
  <div class="flex gap-1" v-if="configStore.result.state">
    <div class="flex flex-col justify-between">
      <div class="flex gap-5 items-center">
        <calc-button class="flex-1" @click="setStandard">设为基准</calc-button>
        <calc-button class="flex-1" @click="clearStandard">清空基准</calc-button>
      </div>
      <div class="flex bg-#101012 h-40px text-#6C5E4A font-bold z-10">
        <div
          class="flex-1 text-15px flex items-center justify-center"
          @click="chooseCategory('equ')"
          :class="{ active: type === 'equ' }"
        >
          装备
        </div>
        <div class="w-auto text-18px flex items-center justify-center !font-normal">|</div>
        <div
          class="flex-1 text-15px flex items-center justify-center"
          @click="chooseCategory('oath')"
          :class="{ active: type === 'oath' }"
        >
          誓约
        </div>
      </div>
      <Info
        :suits="configStore.result.state.suits"
        :info="configStore.result.state.info"
        :equs="configStore.config.equips"
        :avatar="configStore.config.avatarLink"
        :oaths="configStore.config.oaths"
        :display="type"
      ></Info>
    </div>
    <Skill
      v-if="!configStore.result.state.buffer"
      :data="configStore.result.state.skills"
      :standard="infoStore.standard"
    ></Skill>
    <BufferSkill
      v-else
      :data="configStore.result.state.skills"
      :stadard="infoStore.standard"
      :standard="infoStore.standard"
    ></BufferSkill>
  </div>
</template>

<script setup lang="ts">
import { useConfigStore, useInfoStore } from '@/stores'
import Info from './components/Info.vue'
import Skill from './components/Skill.vue'
import BufferSkill from './components/BufferSkill.vue'

const configStore = useConfigStore()
const infoStore = useInfoStore()
const type = ref<'equ' | 'oath'>('equ')

const setStandard = () => {
  if (!configStore?.result?.state?.uuid) return
  infoStore.setStandard(configStore.result.state, configStore.skillCountConfig)
}

const clearStandard = () => {
  infoStore.setStandard(undefined)
}

const chooseCategory = (cat: 'equ' | 'oath') => {
  type.value = cat
  console.log(type.value)
}
</script>

<style lang="scss" scoped>
.active {
  color: #ccc088;
  position: relative;

  &::before {
    content: '';
    position: absolute;
    width: 60px;
    height: 15px;
    opacity: 0.35;
    background: #bf8d20;
    filter: blur(7px);
    z-index: 2;
  }

  &::after {
    content: '';
    position: absolute;
    background: url('@/assets/img/active.png') no-repeat;
    width: 148px;
    height: 16px;
    bottom: 2px;
    transform: translate(0, 50%);
    z-index: 4;
  }
}

.item-head {
  background: linear-gradient(#2b2817, #171407);
  border-top: 1px solid #423d2c;
  border-bottom: 1px solid #211d15;
  text-align: center;
}
</style>
