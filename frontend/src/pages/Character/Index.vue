<template>
  <div class="w-100% h-100% main" :class="props.alter.split('.').slice(-1)">
    <div class="header"></div>
    <div class="content flex">
      <div class="flex flex-col gap-20px mx-10px">
        <Weapon></Weapon>
        <Suit></Suit>
        <Universal></Universal>
      </div>

      <div class="h-90vh w-auto overflow-y-auto overflow-x-hidden">
        <SkillTree :skills="infoStore.skills" :lvInfo="configStore.config?.skills"></SkillTree>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup name="Index">
import { useInfoStore } from '@/stores/info'
import { getImageURL } from '@/utils/images'
import SkillTree from './Skill/SkillTree/index'
import Suit from './Equipment/Suit.vue'
import Weapon from './Equipment/Weapon.vue'
import Universal from './Equipment/Universal.vue'
import { useConfigStore } from '@/stores'
const props = defineProps<{
  alter: string
}>()
const infoStore = useInfoStore()
const configStore = useConfigStore()

onMounted(async () => {
  await infoStore.createCharacter(props.alter, '0')
  configStore.loadConfig()
  console.log(configStore.config)
})
</script>

<style lang="scss">
.main {
  display: flex;
  flex-direction: column;
  height: 100%;
  width: 100%;
  background-repeat: no-repeat;
  background-size: cover;
  background-color: black;

  color: #e9c558;
  // font-size: 12px;

  .header {
    display: flex;
    align-items: flex-end;
    z-index: 2;
    height: 26px;
  }

  .footer {
    display: flex;
    align-items: center;
    justify-content: end;
    z-index: 2;
    height: 40px;
  }

  .content {
    flex: 1;
    overflow-y: auto;
    overflow-x: hidden;
    z-index: 2;
    width: 100%;
  }
}

.main::after {
  content: '';
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background-color: rgba(50, 50, 50, 0.75);
}
</style>
