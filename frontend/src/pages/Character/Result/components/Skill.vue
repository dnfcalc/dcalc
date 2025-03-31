<template>
  <div class="flex flex-col" v-if="data && data.length > 0">
    <div class="flex gap-2 text-white items-center" v-for="skill in data" :key="skill.name">
      <div>
        <img :src="getImageURL(skill.icon)" alt="" class="w-8 h-8" />
      </div>
      <div>{{ skill.name }}</div>
      <div>{{ skill.lv }}</div>
      <div>{{ skill.damage.toFixed(0) }}</div>
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
