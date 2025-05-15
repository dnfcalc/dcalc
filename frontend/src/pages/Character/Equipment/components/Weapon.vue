<!-- 每排总计6+4+4,共计14个排列 -->

<template>
  <div class="flex flex-wrap gap-4px content-start" :style="{ width: `${rowCount * 32}px` }">
    <template v-for="(weapon, _) in weapons" :key="_">
      <EquipmentIcon
        :equipment="weapon"
        :inactive="configStore.config.equips['武器']?.id != weapon?.id"
        @click="configStore.chooseEqu(weapon)"
      />
    </template>
  </div>
</template>

<script lang="ts" setup>
import type { IEquipment } from '@/api/info/type'
import { useConfigStore, useInfoStore } from '@/stores'
import { getImageURL } from '@/utils/images'
import EquipmentIcon from '@/components/dnf/Equipment/Icon/index.vue'

const props = defineProps<{
  rowCount?: number
}>()

const rowCount = Math.max(props.rowCount ?? 0, 14)
const infoStore = useInfoStore()
const configStore = useConfigStore()

const weapons = computed(() => {
  const items = infoStore.equips.filter(
    (equip) => equip.itemType === '武器' && infoStore.infos?.weapons.includes(equip.itemDetailType),
  )
  const res: (IEquipment | undefined)[] = []
  Array.from(new Set(items.map((item) => item.itemDetailType))).forEach((type) => {
    const weapon = items.filter((item) => item.itemDetailType === type)
    res.push(
      ...weapon.filter((item) => item.categorize === '制式武器'),
      undefined,
      ...weapon.filter((item) => item.categorize === '传世武器'),
    )
    const remind = rowCount - (res.length % rowCount)
    res.push(...Array(remind).fill(undefined))
  })
  return res
})
</script>
