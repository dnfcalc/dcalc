<template>
  <div class="bg-hex-000000/60 p-2 border-solid border-#FFFF/15" v-if="data && data.length > 0">
    <div class="bg-hex-000000/40 text-white border-solid border-#FFFF/15 border-t-0">
      <div class="flex px-1px gap-1px">
        <div
          v-for="(header, key) in [
            { label: '技能', width: 180, sortKey: 'name' },
            { label: 'CD', width: 50 },
            { label: '适用加成', width: 80, sortKey: 'MAIN' },
            { label: '三攻', width: 80, sortKey: 'ATK' },
            { label: '力智', width: 80, sortKey: 'STRINT' },
            { label: '额外增伤', width: 80, sortKey: 'ratio' },
          ]"
          :key="key"
          class="item-head"
          :style="{ width: `${header.width}px` }"
          @click="header.sortKey && sortValue(header.sortKey)"
        >
          {{ header.label }}
          <template v-if="header.sortKey && sort === header.sortKey">
            <span>{{ order === 'desc' ? '△' : '▽' }}</span>
          </template>
        </div>
      </div>
      <div class="overflow-y-auto max-h-600px">
        <div class="flex px-1px gap-1px h-8.5" v-for="(skill, _) in data" :key="_">
          <div class="flex w-180px items-center gap-10px">
            <div class="w-28px h-28px relative">
              <img :src="getImageURL(skill.icon)" alt="" :class="['h-28px w-28px', skill.type === 'passive' ? 'passive' : '']" />
              <div v-if="skill.lv" class="skill-lv-min" :data-text="`${skill.lv}`">
                {{ skill.lv }}
              </div>
            </div>
            <div>{{ skill.name }}</div>
          </div>
          <div class="w-50px flex items-center justify-center">
            {{ typeof skill.cd === 'number' ? `${skill.cd.toFixed(1)}s` : '-' }}
          </div>
          <component :is="formatDamage(skill)"></component>
        </div>
      </div>
      <!-- <div
        v-if="!totalStandard"
        class="h-40px flex items-center justify-center text-18px border-t-1px border-t-solid border-t-#FFFF/15"
      >
        {{ showTotal.toFixed(0) }}
      </div>
      <div
        v-else
        class="h-40px flex items-center justify-center text-18px border-t-1px border-t-solid border-t-#FFFF/15"
        :style="{ color: showTotal >= 0 ? '#37fa38' : '#ff0000' }"
      >
        {{ showTotal.toFixed(2) }}%
      </div> -->
    </div>
  </div>
</template>

<script setup lang="ts" name="Skill">
import type { IResultSkill, IResultSkillCount } from '@/api/calc/type'
import { useConfigStore } from '@/stores'
import { getImageURL } from '@/utils/images'
import { h } from 'vue'
const props = defineProps<{
  data: IResultSkill[]
  standard?: {
    skills: IResultSkill[]
    skillCount: IResultSkillCount[]
  }
}>()

const sort = ref<string>('STRINT')
const order = ref<'asc' | 'desc'>('desc')

const config = useConfigStore()

const data = computed(() => {
  return props.data.sort((a, b) => {
    let aValue = 0
    let bValue = 0
    if (['cd', 'name'].includes(sort.value)) {
      // @ts-ignore
      aValue = a[sort.value]
      // @ts-ignore
      bValue = b[sort.value]
    }
    const key = ['MAIN', 'ATK', 'STRINT', 'ratio'].findIndex((a) => sort.value == a)

    aValue = a.buff?.[key]
    bValue = b.buff?.[key]

    return order.value == 'asc' ? aValue - bValue : bValue - aValue
  })
})

const sortValue = (key: string) => {
  if (sort.value == key) {
    order.value = order.value == 'asc' ? 'desc' : 'asc'
  } else {
    order.value = 'desc'
  }
  sort.value = key
}

const skillCount = (skill: IResultSkill) => {
  return computed({
    get() {
      let countConfig = config.skillCountConfig.find(
        (a) => a.name == skill.name && a.mode == skill.mode,
      )
      if (!countConfig) {
        countConfig = { name: skill.name, mode: skill.mode, count: 1 }
        config.skillCountConfig.push(countConfig)
      }
      return countConfig.count
    },
    set(val) {
      const index = config.skillCountConfig.findIndex(
        (a) => a.name == skill.name && a.mode == skill.mode,
      )
      if (index > -1) {
        config.skillCountConfig[index].count = val
      } else {
        config.skillCountConfig.push({ name: skill.name, mode: skill.mode, count: val })
      }
    },
  })
}

const total = computed(() => {
  return [0, 1, 2, 3].map((index) =>
    props.data.reduce((acc, skill) => {
      return acc + skill.buff?.[index]
    }, 0),
  )
})

const totalStandard = computed(() => {
  if (!props.standard) return undefined
  return [0, 1, 2, 3].map((index) =>
    props.standard?.skills.reduce((acc, skill) => {
      return acc + skill.buff?.[index]
    }, 0),
  )
})

const formatDamage = (skill: IResultSkill) => {
  const standardSkill = props.standard?.skills?.find((a) => a.name == skill.name)
  if (standardSkill) {
    return h(
      'div',
      {
        class: 'flex items-center justify-center',
      },
      [0, 1, 2, 3].map((index) => {
        const value = skill.buff?.[index] - standardSkill.buff?.[index]
        return h(
          'div',
          {
            style: {
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              width: '80px',
              color: value >= 0 ? '#37fa38' : '#ff0000',
            },
          },
          `${value >= 0 ? '+' : ''}${
            index == 3
              ? `${Math.round(value).toLocaleString()}%`
              : Math.round(value).toLocaleString()
          }`,
        )
      }),
    )
  } else {
    return h(
      'div',
      {
        class: 'flex items-center justify-center',
      },
      [0, 1, 2, 3].map((index) => {
        const value = skill.buff?.[index]
        return h(
          'div',
          {
            style: {
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              width: '80px',
            },
          },
          index == 3
            ? `${Math.round(value).toLocaleString()}%`
            : Math.round(value).toLocaleString(),
        )
      }),
    )
  }
}
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
  content: attr(data-text);
  position: absolute;
  -webkit-text-stroke: 2.5px #37fa38;
  font-family: Arial;
  text-shadow: none;
  z-index: -1;
}
</style>
