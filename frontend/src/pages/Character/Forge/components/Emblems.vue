<template>
  <div class="h-179px flex justify-center items-center">
    <EmblemList :withBg="true" v-model:part="part" :detail="configStore.config.emblems" />
  </div>
  <div class="flex flex-wrap equ-profile">
    <div class="equ-profile-item">
      <div class="mr-10px row-name">当前槽位</div>
      <span>{{ part }}</span>
    </div>
    <div class="equ-profile-item" v-if="part != '白金'">
      <div class="row-name">等级</div>
      <calc-select v-model="lv" class="flex-1 !h-20px">
        <template v-for="(i, index) in lvs" :key="index">
          <calc-option :value="index">{{ i }}</calc-option>
        </template>
      </calc-select>
    </div>
    <div class="flex w-full">
      <div class="flex-basis-50px text-center mr-10px">徽章</div>
      <div class="flex-1 grid gap-4px" :style="emblemGridStyle">
        <div
          v-for="(emblem, index) in emblemMaxCount"
          :style="emblemItemStyle(index)"
          class="flex"
          :key="index"
        >
          <calc-select v-model="emblems[index]" class="min-w-0 flex-1 !h-20px">
            <template v-for="(i, index) in lvs" :key="index">
              <calc-option :value="i">{{ i }}</calc-option>
            </template>
          </calc-select>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup name="Emblems">
import EmblemList from '@/components/dnf/Emblem/List/index.vue'
import { useConfigStore } from '@/stores'

const part = ref('彩色')

const configStore = useConfigStore()

const lvs = [
  '稀有Lv.1',
  '稀有Lv.2',
  '稀有Lv.3',
  '稀有Lv.4',
  '稀有Lv.5',
  '神器Lv.1',
  '神器Lv.2',
  '神器Lv.3',
  '神器Lv.4',
  '神器Lv.5',
  '传说Lv.1',
  '传说Lv.2',
  '传说Lv.3',
  '传说Lv.4',
  '传说Lv.5',
  '史诗Lv.1',
]

const emblemMaxCount = computed(() => {
  if (part.value == '彩色') {
    return 6
  }
  if (part.value == '白金') {
    return 2
  }
  return 4
})

const emblemGridStyle = computed(() => {
  return {
    gridTemplateColumns: 'repeat(2, minmax(0, 1fr))',
  }
})

const emblemItemStyle = (index: number) => {
  const count = emblemMaxCount.value
  const remainder = count % 2

  if (remainder === 1 && index === count - 1) {
    return {
      gridColumn: 'span 2 / span 2',
    }
  }

  return {
    gridColumn: 'span 1 / span 1',
  }
}

const currentInfo = function <T>(name: string, defaultValue?: T) {
  return computed<string | number>({
    get() {
      return (
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        (configStore.config.emblems?.[part.value] as Record<string, any>)?.[name] ??
        defaultValue ??
        0
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

      if (!configStore.config.emblems[part.value]) {
        configStore.config.emblems[part.value] = { ...configStore.defaultEmblemConfig }
      }
      if (configStore.config.emblems[part.value]) {
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        ;(configStore.config.emblems[part.value] as Record<string, any>)[name] = val
      }
      if (part.value == '彩色' && name == 'lv') {
        // 同步其他部位的等级
        const lv = val as number
        for (const p of ['红色', '蓝色', '黄色', '绿色']) {
          if (!configStore.config.emblems[p]) {
            configStore.config.emblems[p] = { ...configStore.defaultEmblemConfig }
          }
          if (configStore.config.emblems[p]) {
            configStore.config.emblems[p]['lv'] = Math.max(
              configStore.config.emblems[p]['lv'] || 0,
              lv,
            )
          }
        }
      } else if (part.value != '彩色' && name == 'lv') {
        // 同步彩色部位的等级
        const lv = val as number
        if (!configStore.config.emblems['彩色']) {
          configStore.config.emblems['彩色'] = { ...configStore.defaultEmblemConfig }
        }
        if (configStore.config.emblems['彩色']) {
          configStore.config.emblems['彩色']['lv'] = Math.min(
            configStore.config.emblems['彩色']['lv'] || 0,
            lv,
          )
        }
      }
    },
  })
}

const lv = currentInfo('lv', 0)

const emblems = currentInfo<string[]>('items', ['', '', '', '', '', '']) as unknown as Ref<string[]>
</script>
