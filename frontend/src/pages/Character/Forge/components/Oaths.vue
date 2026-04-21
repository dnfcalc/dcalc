<template>
  <div class="h-150px flex justify-center items-center">
    <Oath v-model:part="part" :withBg="false" />
  </div>
  <div class="flex flex-wrap equ-profile">
    <div class="equ-profile-item">
      <div class="mr-10px row-name">当前部位</div>
      <span>{{ part == '11' ? '誓约' : `星蕴石-${parseInt(part) + 1}` }}</span>
      <calc-checkbox
        style="margin-left: auto"
        v-model="global_change"
        label="全局修改"
      ></calc-checkbox>
    </div>
    <div class="equ-profile-item">
      <div class="row-name">调适</div>
      <calc-select v-model="adaptation" class="flex-1 !h-20px">
        <template v-for="i in Array.from({ length: 4 }, (_, i) => i)" :key="i">
          <calc-option :value="i">{{ i }}</calc-option>
        </template>
      </calc-select>
    </div>
  </div>
</template>

<script lang="ts" setup name="Oaths">
import Oath from '@/components/dnf/Equipment/Oath/index.vue'
import { useConfigStore, useInfoStore } from '@/stores'

const part = ref('0')

const global_change = ref(false)

const configStore = useConfigStore()

const infoStore = useInfoStore()

const currentInfo = function <T>(name: string, defaultValue?: T) {
  return computed<string | number>({
    get() {
      return (
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        (configStore.config.oaths?.[part.value] as Record<string, any>)?.[name] ?? defaultValue ?? 0
      )
    },
    set(val) {
      if (val == undefined) {
        return
      }
      // if (name == 'emblem_1' && !has_emblem_1.value) {
      //   // configStore.setForge(part.value, name, 0)
      //   return
      // }

      let parts: string[] = []

      if (global_change.value) {
        parts = infoStore.oathParts
      } else {
        parts = [part.value]
      }
      for (const part of parts) {
        if (!configStore.config.oaths[part]) {
          configStore.config.oaths[part] = { ...configStore.defaultOathConfig }
        }
        if (configStore.config.oaths[part]) {
          // eslint-disable-next-line @typescript-eslint/no-explicit-any
          ;(configStore.config.oaths[part] as Record<string, any>)[name] = val
        }
      }
    },
  })
}

// 调适
const adaptation = currentInfo<string | number>('adaptation')
</script>
