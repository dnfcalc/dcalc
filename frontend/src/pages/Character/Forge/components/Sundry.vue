<template>
  <div class="flex flex-wrap equ-profile">
    <div class="equ-profile-item">
      <div class="row-name">勋章</div>
      <calc-select
        v-for="(key, index) in ['medal_rarity', 'medal_reinforce']"
        :key="index"
        v-model="sundryData[key as keyof typeof sundryData]"
        class="flex-1 !h-20px"
      >
        <calc-option v-for="(item, idx) in list(key)" :key="idx" :value="item.value">
          {{ item.name }}
        </calc-option>
      </calc-select>
    </div>
    <div class="equ-profile-item">
      <div class="row-name">宝石</div>
      <calc-select
        v-for="(key, index) in ['medal_gem_0', 'medal_gem_1', 'medal_gem_2', 'medal_gem_3']"
        :key="index"
        v-model="sundryData[key as keyof typeof sundryData]"
        class="flex-1 !h-20px !min-w-10"
      >
        <calc-option v-for="(item, idx) in list(key)" :key="idx" :value="item.value">
          {{ item.name }}
        </calc-option>
      </calc-select>
    </div>
    <div class="equ-profile-item">
      <div class="row-name">冒险团</div>
      <calc-select v-model="sundryData['adventure']" class="flex-1 !h-20px">
        <calc-option v-for="(item, idx) in list('adventure')" :key="idx" :value="item.value">
          {{ item.name }}
        </calc-option>
      </calc-select>
    </div>
    <div class="equ-profile-item">
      <div class="row-name">结婚系统</div>
      <calc-select
        v-for="(key, index) in ['marriage_house', 'marriage_ring']"
        :key="index"
        v-model="sundryData[key as keyof typeof sundryData]"
        class="flex-1 !h-20px !min-w-10"
      >
        <calc-option v-for="(item, idx) in list(key)" :key="idx" :value="item.value">
          {{ item.name }}
        </calc-option>
      </calc-select>
    </div>
    <div class="equ-profile-item">
      <div class="row-name">晶体契约</div>
      <calc-select v-model="sundryData['contract']" class="flex-1 !h-20px">
        <calc-option v-for="(item, idx) in list('contract')" :key="idx" :value="item.value">
          {{ item.name }}
        </calc-option>
      </calc-select>
    </div>
    <div class="equ-profile-item">
      <div class="row-name">收集箱</div>
      <calc-select
        v-for="(key, index) in ['collection_type', 'collection_num_0', 'collection_num_1']"
        :key="index"
        v-model="sundryData[key as keyof typeof sundryData]"
        class="flex-1 !h-20px !min-w-10"
      >
        <calc-option v-for="(item, idx) in list(key)" :key="idx" :value="item.value">
          {{ item.name }}
        </calc-option>
      </calc-select>
    </div>
    <div class="equ-profile-item">
      <div class="row-name">名称装扮</div>
      <calc-select v-model="sundryData['costume_card']" class="flex-1 !h-20px !min-w-10">
        <calc-option v-for="(item, idx) in list('costume_card')" :key="idx" :value="item.value">
          {{ item.name }}
        </calc-option>
      </calc-select>
    </div>
  </div>
</template>

<script setup lang="ts">
import { useConfigStore, useInfoStore } from '@/stores'

const configStore = useConfigStore()
const infoStore = useInfoStore()
const currentInfo = function <T>(name: string, defaultValue?: T) {
  return computed<string | number>({
    get() {
      return configStore.config.sundry?.[name] ?? defaultValue ?? 0
    },
    set(val) {
      if (val == undefined) {
        return
      }
      configStore.config.sundry[name] = val
    },
  })
}

const list = computed(() => {
  return (key: string) => {
    return infoStore.sundries[key].options
  }
})

const sundryData = reactive({
  medal_rarity: currentInfo('medal_rarity', 5),
  medal_reinforce: currentInfo('medal_reinforce', 12),
  medal_gem_0: currentInfo('medal_gem_0', 4),
  medal_gem_1: currentInfo('medal_gem_1', 4),
  medal_gem_2: currentInfo('medal_gem_2', 4),
  medal_gem_3: currentInfo('medal_gem_3', 4),
  adventure: currentInfo('adventure', 30),
  marriage_house: currentInfo('marriage_house', 4),
  marriage_ring: currentInfo('marriage_ring', 2),
  contract: currentInfo('contract', 1),
  collection_type: currentInfo('collection_type', 1),
  collection_num_0: currentInfo('collection_num_0', 5),
  collection_num_1: currentInfo('collection_num_1', 5),
  costume_card: currentInfo('costume_card', 1),
})
</script>
