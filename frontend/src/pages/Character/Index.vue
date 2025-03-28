<template>
  <div class="w-100% h-100% main" :class="props.alter.split('.').slice(-1)">
    <div class="header">
      <calc-tabs route>
      <calc-tab :value="`/character/equipment/${props.alter}`">装备设置</calc-tab>
      <calc-tab :value="`/character/skill/${props.alter}`">技能设置</calc-tab>
      <calc-tab :value="`/character/forge/${props.alter}`">打造设置</calc-tab>
    </calc-tabs>
    </div>
    <div class="content flex">
      <RouterView></RouterView>
    </div>
  </div>
</template>

<script lang="ts" setup name="Index">
import { useInfoStore } from '@/stores/info'
import { useConfigStore } from '@/stores'
const props = defineProps<{
  alter: string
}>()
const infoStore = useInfoStore()
const configStore = useConfigStore()

onMounted(async () => {
  await infoStore.createCharacter(props.alter, '0')
  configStore.loadConfig()
  console.log("~~~~~~~~")
  window.addEventListener('beforeunload', () => {
    configStore.saveConfig()
  })
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
