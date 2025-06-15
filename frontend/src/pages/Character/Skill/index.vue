<template>
  <div class="flex relative" ref="skillTreeRef">
    <div class="flex flex-col">
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
          技能定制
        </div>
      </div>
      <div class="flex-1 w-550px overflow-x-hidden bg-#101012">
        <div class="overflow-y-auto h-full box-border" v-if="tab === 0">
          <SkillTree
            :skills="infoStore.skills"
            v-model:lvInfo="configStore.config.skills"
            v-model:bindAwake="configStore.config.bindAwake"
            @chooseSkill="setCurrentSkill"
          ></SkillTree>
        </div>
        <div v-if="tab === 1" class="flex flex-col overflow-y-hidden h-full">
          <div class="item-head" 角色等级>技能进化</div>
          <SkillUP
            class="flex-1"
            :skills="infoStore.skills"
            v-model:lvInfo="configStore.config.skills"
            v-model:bindAwake="configStore.config.bindAwake"
            :buffer="infoStore.infos?.buffer"
          ></SkillUP>
          <div class="item-head" 角色等级>技能突破</div>
          <div class="flex-1 overflow-y-auto w-full">
            <SkillVP
              :skills="infoStore.skills"
              v-model:lvInfo="configStore.config.skills"
              v-model:bindAwake="configStore.config.bindAwake"
              @chooseSkill="setCurrentSkill"
            ></SkillVP>
          </div>
        </div>
      </div>
    </div>

    <div
      class="absolute right--65px"
      v-if="curCurrentSkill.skillId && curCurrentSkill.level > 0 && !showSkillDetail"
    >
      <div class="text-#AE8D5A p-1px box-border flex pl-2 w-auto">
        <div
          class="border-1px border-solid border-#322E20 border-l-none flex p-1px box-border pl-0"
        >
          <div
            class="border-1px border-#514531 border-solid rounded-2px flex flex-col items-center justify-center p-5px"
            style="background: linear-gradient(to bottom, #313330 0%, #0f110f 100%)"
            @click="showSkillDetail = true"
          >
            <img class="w-30px h-30px" src="./components/img/detail.png" />
            技能详情
          </div>
        </div>
      </div>
    </div>
  </div>
  <div
    class="bg-#101012 w-300px h-full absolute"
    :style="style"
    ref="SkillDetailRef"
    v-if="curCurrentSkill.skillId && curCurrentSkill.level > 0 && showSkillDetail"
  >
    <SkillDetail :skillId="curCurrentSkill.skillId" :level="curCurrentSkill.level"></SkillDetail>
  </div>
</template>

<script lang="ts" setup name="Index">
import { useInfoStore } from '@/stores/info'
import SkillTree from './components/SkillTree'
import SkillVP from './components/SkillVP'
import SkillUP from './components/SkillUP'
import { useConfigStore } from '@/stores'
import SkillDetail from './components/SkillDetail'
import { onClickOutside } from '@vueuse/core'
const props = defineProps<{
  alter: string
}>()
const tab = ref(0)
const infoStore = useInfoStore()
const configStore = useConfigStore()

const curSkillId = ref()

const curCurrentSkill = computed(() => {
  const skill = infoStore.skills.find((skill) => skill.uuid === curSkillId.value)
  return {
    skillId: skill?.uuid ?? '',
    level: configStore.config.skills[skill?.id || 0]?.lv || 0,
  }
})

const showSkillDetail = ref(false)

const skillTreeRef = ref<HTMLHtmlElement>()
const SkillDetailRef = ref<HTMLHtmlElement>()

const style = computed(() => {
  return {
    zIndex: 99,
    height: `${skillTreeRef.value?.clientHeight ?? 0}px`,
    left: `${(skillTreeRef.value?.clientWidth ?? 0) + 5}px`,
  }
})

const setCurrentSkill = (skillId: number) => {
  curSkillId.value = infoStore.skills.find((skill) => skill.id === skillId)?.uuid || ''
}

onClickOutside(SkillDetailRef, (event) => {showSkillDetail.value = false}, {
  ignore: [skillTreeRef],
})
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

.item-head {
  background: linear-gradient(#2b2817, #171407);
  border-top: 1px solid #423d2c;
  border-bottom: 1px solid #211d15;
  text-align: center;
  // 以下后面注释掉
  height: 20px;
  line-height: 20px;
  font-weight: 14px;
}
</style>
