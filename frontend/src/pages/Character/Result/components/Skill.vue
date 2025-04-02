<template>
  <div class="flex flex-col gap-1" v-if="data && data.length > 0">
    <div class="flex gap-2 text-white items-center jus" v-for="skill in data" :key="skill.name">
      <div class="flex-1 flex items-center">
        <img :src="getImageURL(skill.icon)" alt="" class="w-8 h-8" />
      </div>
      <div class="w-150px">{{ skill.name }}</div>
      <div class="flex-1">{{ skill.cd.toFixed(2) }}s</div>
      <div class="flex-1">{{ skill.damage.toFixed(0) }}</div>
    </div>
  </div>
</template>

<script setup lang="ts" name="Skill">
import type { IResultSkill } from '@/api/calc/type'
import { getImageURL } from '@/utils/images'
const props = defineProps<{
  data: IResultSkill[]
}>()

const data = computed(() => {
  return props.data.sort((a,b)=>b.damage - a.damage)
})
</script>

<style scoped lang="scss"></style>
