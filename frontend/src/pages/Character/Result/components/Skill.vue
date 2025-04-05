<template>
  <div class="bg-hex-000000/60 p-4 border-solid border-#FFFF/15" v-if="data && data.length > 0">
    <div class="bg-hex-000000/40 text-white border-solid border-#FFFF/15 border-t-0">
      <div class="flex px-1px gap-1px">
        <div class="item-head w-150px">技能</div>
        <div class="item-head w-80px">CD</div>
        <div class="item-head w-150px">伤害</div>
        <div class="item-head w-150px">秒伤</div>
      </div>
      <div class="overflow-y-auto max-h-580px">
        <div class="flex px-1px gap-1px h-8.5" v-for="skill in data" :key="skill.name">
          <div class="flex w-150px items-center gap-10px">
            <div class="w-28px h-28px relative">
              <img :src="getImageURL(skill.icon)" alt="" class="w-28px h-28px" />
              <div v-if="skill.lv" class="skill-lv-min" :data-text="`Lv ${ skill.lv }`">Lv {{ skill.lv }}</div>
            </div>
            <div>{{ skill.name }}</div>
          </div>
          <div class="w-80px flex items-center justify-center">{{ skill.cd.toFixed(1) }}s</div>
          <div class="w-150px flex items-center justify-center">
            {{ Math.round(skill.damage).toLocaleString() }}
          </div>
          <div class="w-150px flex items-center justify-center">
            {{ Math.round(skill.damage / skill.cd).toLocaleString() }}
          </div>
        </div>
      </div>
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
  return props.data.sort((a, b) => b.damage - a.damage)
})
</script>

<style scoped lang="scss">
.item-head {
  background: linear-gradient(#2b2817, #171407);
  border-top: 1px solid #423d2c;
  border-bottom: 1px solid #211d15;
  text-align: center;
}

.skill-lv-min {
    position: absolute;
    z-index: 0;
    top: -3px;
    right: -4px;
    font-size: 12px;
    transform: scale(0.7);
    color: black;
    text-shadow: none;
    font-weight: bolder;
    font-family: Arial;
  }

  .skill-lv-min::before {
    // text-shadow: #37fa38 2px 0 0, #37fa38 0 2px 0, #37fa38 -2px 0 0, #37fa38 0 -2px 0;
    // -webkit-text-stroke-width: 1px;
    // -webkit-text-stroke-color: #37fa38;
    content: attr(data-text);
    position: absolute;
    -webkit-text-stroke: 2.5px #37fa38;
    font-family: Arial;
    text-shadow: none;
    z-index: -1;
  }
</style>
