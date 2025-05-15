<template>
  <div class="flex flex-col gap-2 w-250px p-2">
    <div v-for="option in info.options" :key="option.id" class="flex items-center gap-2">
      <div class="w-60px text-end">{{ option.name }}</div>
      <calc-select class="flex-1 !h-20px" :appendTo="dialogRef" v-model="config.config.options[option.id.toString()]">
        <calc-option v-for="(item, index) in option.options" :key="index" :value="index">
          {{ item }}
        </calc-option>
      </calc-select>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { useConfigStore, useInfoStore } from '@/stores'
const dialogRef = inject("dialogRef", ref(null))
const config = useConfigStore()
const info = useInfoStore()
</script>
