<template>
  <div>
    <div class="flex bg-#101012 h-40px text-#6C5E4A font-bold">
      <div
        class="flex-1 text-15px flex items-center justify-center"
        @click="tab = 0"
        :class="{ active: tab === 0 }"
      >
        技能加点
      </div>
      <div class="w-auto text-18px flex items-center justify-center !font-normal">|</div>
      <div
        class="flex-1 text-15px flex items-center justify-center"
        @click="tab = 1"
        :class="{ active: tab === 1 }"
      >
        技能VP
      </div>
      <!-- <div class="w-auto text-18px flex items-center justify-center !font-normal">|</div>
      <div
        class="flex-1 text-15px flex items-center justify-center"
        @click="tab = 2"
        :class="{ active: tab === 2 }"
      >
        技能突破
      </div> -->
    </div>
    <!-- <calc-tabs v-model="tab">
      <calc-tab :value="0">技能加点</calc-tab>
      <calc-tab :value="1">技能VP</calc-tab>
      <calc-tab :value="2">技能突破</calc-tab>
    </calc-tabs> -->
    <div class="h-90vh w-620px overflow-x-hidden bg-#202020">
      <div class="overflow-y-auto h-full" v-if="tab === 0">
        <SkillTree
          :skills="infoStore.skills"
          v-model:lvInfo="configStore.config.skills"
          v-model:bindAwake="configStore.config.bindAwake"
        ></SkillTree>
      </div>
      <div v-if="tab === 1" class="flex flex-col overflow-y-hidden h-full">
        <SkillReinforce
          class="flex-1"
          :skills="infoStore.skills"
          v-model:lvInfo="configStore.config.skills"
          v-model:bindAwake="configStore.config.bindAwake"
        ></SkillReinforce>
        <div class="flex-1 overflow-y-auto w-full">
          <SkillVP
            :skills="infoStore.skills"
            v-model:lvInfo="configStore.config.skills"
            v-model:bindAwake="configStore.config.bindAwake"
          ></SkillVP>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup name="Index">
import { useInfoStore } from '@/stores/info'
import SkillTree from './components/SkillTree'
import SkillVP from './components/SkillVP'
import SkillReinforce from './components/SkillReinforce'
import { useConfigStore } from '@/stores'
const props = defineProps<{
  alter: string
}>()
const tab = ref(0)
const infoStore = useInfoStore()
const configStore = useConfigStore()
</script>

<style lang="scss" scoped>
.active {
  color: #ccc088;
  position: relative;

  &::before {
    content: '';
    position: absolute;
    width: 80px;
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
  }
}
</style>
