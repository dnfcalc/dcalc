<template>
  <div class="bg-hex-000000/60 p-2 border-solid border-#FFFF/15" v-if="data && data.length > 0">
    <div class="bg-hex-000000/40 text-white border-solid border-#FFFF/15 border-t-0">
      <div class="flex px-1px gap-1px">
        <div
          v-for="(header, key) in [
            { label: '技能', width: 180, sortKey: 'learnLv' },
            { label: 'CD', width: 50, sortKey: 'cd' },
            { label: '次数', width: 50 },
            { label: '秒伤', width: 100, sortKey: 'dps' },
            { label: '总伤害', width: 110, sortKey: 'total' },
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
        <div class="item-head w-60px">占比</div>
      </div>
      <div class="overflow-y-auto max-h-600px">
        <div class="flex px-1px gap-1px h-8.5" v-for="(skill, _) in data" :key="_">
          <div class="flex w-180px items-center gap-10px">
            <div class="w-28px h-28px relative">
              <img :src="getImageURL(skill.icon)" alt="" class="w-28px h-28px" />
              <div v-if="skill.lv" class="skill-lv-min" :data-text="`Lv ${skill.lv}`">
                Lv {{ skill.lv }}
              </div>
            </div>
            <div>{{ skill.name }} {{ !skill.mode ? '' : `[${skill.mode}]` }}</div>
          </div>
          <div class="w-50px flex items-center justify-center">{{ skill.cd.toFixed(1) }}s</div>
          <div class="w-50px flex items-center justify-center">
            <calc-input
              type="number"
              class="!w-40px !min-w-40px !pl-0 flex items-center justify-center"
              v-model="skillCount(skill).value"
            ></calc-input>
          </div>
          <component :is="formatDamage(skill)"></component>
        </div>
      </div>
      <div
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
      </div>
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

const sort = ref<string>('learnLv')
const order = ref<'asc' | 'desc'>('desc')

const config = useConfigStore()

const data = computed(() => {
  return props.data.sort((a, b) => {
    let aValue = 0
    let bValue = 0
    if (['damage', 'cd', 'learnLv'].includes(sort.value)) {
      // @ts-ignore
      aValue = a[sort.value]
      // @ts-ignore
      bValue = b[sort.value]
    }
    if (sort.value == 'total') {
      aValue = a.damage * skillCount(a).value
      bValue = b.damage * skillCount(b).value
    }
    if (sort.value == 'dps') {
      aValue = a.damage / a.cd
      bValue = b.damage / b.cd
    }
    if (sort.value == 'name') {
      // @ts-ignore
      return order.value == 'asc' ? aValue.localeCompare(bValue) : bValue.localeCompare(aValue)
    }
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

const totalDamage = computed(() => {
  return props.data.reduce((acc, skill) => {
    return acc + skill.damage * skillCount(skill).value
  }, 0)
})

const totalStandard = computed(() => {
  if (!props.standard) return undefined
  return props.standard.skills.reduce((acc, skill) => {
    const standardSkillCount = props.standard?.skillCount.find(
      (a) => a.name == skill.name && a.mode == skill.mode,
    )?.count
    return acc + skill.damage * (standardSkillCount || 0)
  }, 0)
})

const showTotal = computed(() => {
  if (!totalStandard.value || totalStandard.value == 0) return totalDamage.value
  return ((totalDamage.value - totalStandard.value) / totalStandard.value) * 100
})

const formatDamage = (skill: IResultSkill) => {
  const standardSkill = props.standard?.skills?.find(
    (a) => a.name == skill.name && a.mode == skill.mode,
  )
  const standardSkillCount = props.standard?.skillCount.find(
    (a) => a.name == skill.name && a.mode == skill.mode,
  )?.count
  const rate = h(
    'div',
    {
      style: {
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        width: '60px',
      },
    },
    (((skill.damage * skillCount(skill).value) / totalDamage.value) * 100).toFixed(2) + '%',
  )
  if (standardSkill && standardSkill.damage > 0 && standardSkill.cd > 0 && !!standardSkillCount) {
    const currentSkillCount = skillCount(skill).value
    const damageValue =
      (skill.damage * currentSkillCount - standardSkill.damage * standardSkillCount) /
      (standardSkill.damage * standardSkillCount)
    const damage = h(
      'div',
      {
        style: {
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          width: '110px',
          color: damageValue >= 0 ? '#37fa38' : '#ff0000',
        },
      },
      (damageValue * 100).toFixed(2) + '%',
    )
    const dpsValue =
      (skill.damage / skill.cd - standardSkill.damage / standardSkill.cd) /
      (standardSkill.damage / standardSkill.cd)
    const dps = h(
      'div',
      {
        style: {
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          width: '110px',
          color: dpsValue >= 0 ? '#37fa38' : '#ff0000',
        },
      },
      (dpsValue * 100).toFixed(2) + '%',
    )
    return h(
      'div',
      {
        class: 'flex items-center justify-center',
      },
      [dps, damage, rate],
    )
  } else {
    const damage = h(
      'div',
      {
        style: {
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          width: '110px',
        },
      },
      Math.round(skill.damage * skillCount(skill).value).toLocaleString(),
    )
    const dps = h(
      'div',
      {
        style: {
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          width: '110px',
        },
      },
      Math.round(skill.damage / skill.cd).toLocaleString(),
    )
    return h(
      'div',
      {
        class: 'flex items-center justify-center',
      },
      [dps, damage, rate],
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
