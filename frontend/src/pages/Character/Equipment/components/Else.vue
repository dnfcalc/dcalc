<!-- 每排总计6+4+4,共计14个排列 -->

<template>
  <div class="flex flex-wrap gap-4px content-start" :style="{ width: `${rowCount * 32}px` }">
    <template v-for="(equ, _) in equs" :key="_">
      <EquipmentIcon
        :equipment="equ"
        :inactive="configStore.config.equips[equ?.itemDetailType ?? '']?.id != equ?.id"
        @click="configStore.chooseEqu(equ)"
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

const equs = computed(() => {
  const items = infoStore.equips.filter((equip) => ['称号', '宠物'].includes(equip.itemDetailType))
  const res: (IEquipment | undefined)[] = []
  Array.from(new Set(items.map((item) => item.itemDetailType))).forEach((type) => {
    const equList = items.filter((item) => item.itemDetailType === type)
    equList.sort((a, b) => {
      if (a.itemType !== b.itemType) {
        return b.itemType.localeCompare(a.itemType)
      }
      const rarityOrder = ['传说', '神器', '稀有']
      return rarityOrder.indexOf(a.rarity) - rarityOrder.indexOf(b.rarity)
    })
    res.push(...equList)
    const remind = rowCount - (res.length % rowCount)
    res.push(...Array(remind + rowCount).fill(undefined))
  })
  const treasure = infoStore.equips.filter((equip) => equip.categorize.includes('秘宝'))
  res.push(...treasure, ...Array(rowCount - treasure.length).fill(undefined))
  return res
})
</script>
