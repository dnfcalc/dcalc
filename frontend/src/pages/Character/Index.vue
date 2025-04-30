<template>
  <div class="w-100% h-100% main flex" :class="infoStore.infos?.alter">
    <div class="header">
      <calc-tabs route>
        <calc-tab :value="`/character/equipment/${props.alter}`">装备设置</calc-tab>
        <calc-tab :value="`/character/skill/${props.alter}`">技能设置</calc-tab>
        <calc-tab :value="`/character/forge/${props.alter}`">打造设置</calc-tab>
      </calc-tabs>
    </div>
    <div class="content flex">
      <div class="flex h-auto p-1 overflow-y-hidden" v-if="!!infoStore.infos?.alter">
        <RouterView></RouterView>
      </div>
      <div class="p-1 ml-auto h-auto overflow-y-auto z-2">
        <Result></Result>
      </div>
    </div>
    <div class="footer flex"></div>
  </div>
</template>

<script lang="ts" setup name="Index">
import { useInfoStore } from '@/stores/info'
import { useConfigStore } from '@/stores'
import Result from './Result/Index.vue'
const props = defineProps<{
  alter: string
}>()
const infoStore = useInfoStore()
const configStore = useConfigStore()

const stopWatch = watch<any>(
  () => {
    return JSON.stringify(configStore.config)
  },
  useDebounceFn(async () => {
    ;(await configStore.result).execute()
  }, 800),
)

onMounted(async () => {
  await infoStore.createCharacter(props.alter, '0')
  window.addEventListener('beforeunload', () => {
    configStore.saveConfig()
  })
})

onUnmounted(() => {
  stopWatch()
  window.removeEventListener('beforeunload', () => {
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
    overflow-y: hidden;
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
