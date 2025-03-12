<template>
  <div class="w-100% h-100% main" :class="props.alter.split('.').slice(-1)">
    <div class="header"></div>
    <div class="content flex">
      <Weapon></Weapon>
      <div class="h-90vh w-560px overflow-y-auto overflow-x-hidden">

      <SkillTree></SkillTree>

  </div>
    </div>


  </div>
</template>

<script lang="ts" setup name="Index">
import { useInfoStore } from '@/stores/info'
import { getImageURL } from '@/utils/images'
import SkillTree from './Skill/SkillTree.vue';
import Weapon from './Equipment/Weapon.vue';
const props = defineProps<{
  alter: string
}>()
const infoStore = useInfoStore()
onMounted(() => {
  infoStore.createCharacter(props.alter, '0')
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
    content: "";
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    left: 0;
    background-color: rgba(50, 50, 50, 0.75);
  }
</style>
