<!-- 每排总计6+4+4,共计14个排列 -->

<template>
  <div class="flex flex-wrap gap-4px content-start" :style="{width: `${rowCount * 32}px`}">
    <template v-for="(equ,_) in equs" :key="_">
        <EquipmentIcon :equipment="equ" />
    </template>
  </div>
</template>

<script lang="ts" setup>
import type { IEquipment } from '@/api/info/type'
import { useInfoStore } from '@/stores'
import { getImageURL } from '@/utils/images'
import EquipmentIcon from '@/components/dnf/Equipment/Icon/index.vue'

const props = defineProps<{
  rowCount ?:number
}>()

const rowCount = Math.max(props.rowCount ?? 0, 14)
const infoStore = useInfoStore()

const equs = computed(() => {
  const items = infoStore.equips.filter(
    (equip) => equip.categorize === '通宝装备' || equip.categorize === '稀有装备 套装',
  )
  const res: (IEquipment | undefined)[] = []
  const raritiyList = ['稀有','神器','传说','史诗']
  raritiyList.forEach((rarity) => {
    const equ : (IEquipment | undefined)[]  = items.filter((a) => a.rarity === rarity)
    equ.splice(5,0,undefined)
    equ.splice(9,0,undefined)
    res.push(
      ...equ,
      ...Array(Math.max(0,rowCount - equ.length)).fill(undefined),
    )
  })
  return res
})
</script>
