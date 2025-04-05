<template>
  <div>
  <template v-for="key in ['0','1','2','3']" :key="key">
    <div class="flex gap-2 mt-5px">
      <calc-select class="flex-1 !h-20px" v-model="configStore.config.jades[key].id">
        <calc-option v-for="(item, index) in infoStore.jades" :key="item.id" :value="item.id">
          {{item.name}}
        </calc-option>
      </calc-select>
      <calc-select class="flex-1 !h-20px" v-model="configStore.config.jades[key].value">
        <calc-option v-for="(item, index) in valueList(configStore.config.jades[key].id)" :key="item.id" :value="item.id">
          {{item.value}}
        </calc-option>
      </calc-select>
    </div>
  </template>
</div>
</template>

<script setup lang="ts">
import type { IJade } from '@/api/info/type'
import { useConfigStore } from '@/stores'
import { useInfoStore } from '@/stores'
import { getFloat } from '@/utils'

const configStore = useConfigStore()
const infoStore = useInfoStore()

const valueList = computed(() => {
  return function (id: number = -1) {
        if (id == -1) {
          return undefined
        } else {
          const res = []
          const cur = infoStore.jades?.find(e => e.id == id) as IJade
          if (cur) {
            const { max, min, unit, pre } = cur
            //
            if (pre == 0) {
              res.push({
                id: 1,
                value: unit
              })
            } else {
              for (let i = Number(max) as number; i >= Number(min);) {
                if (i != 0) {
                  res.push({
                    id: i,
                    value: (i > 0 ? "+" : "") + getFloat(i, 1) + unit
                  })
                }
                i = Number((i - Number(pre)).toFixed(1))
              }
            }
            return res
          }
        }
      }
    })
</script>
