<!-- 每排总计6+4+4,共计14个排列 -->

<template>
  <div class="flex flex-wrap gap-4px content-start" :style="{width: `${rowCount * 32}px`}">
    <template v-for="(equip,_) in equs" :key="_">
        <EquipmentIcon :inactive="configStore.config.equips[equip?.itemDetailType ?? '']?.fusion != equip?.id"  :equipment="equip" @click="configStore.chooseEqu(equip,true)" />
    </template>
  </div>
</template>

<script lang="ts" setup StoneUniversal>
import type { IEquipment } from '@/api/info/type'
import { useConfigStore, useInfoStore } from '@/stores'
import { getImageURL } from '@/utils/images'
import EquipmentIcon from '@/components/dnf/Equipment/Icon/index.vue'

const props = defineProps<{
  rowCount ?:number
}>()

const rowCount = Math.max(props.rowCount ?? 0, 14)
const infoStore = useInfoStore()
const configStore = useConfigStore()

const equs = computed(() => {
  const items = infoStore.stones.filter(
    (equip) => equip.categorize.includes('通宝'),
  )
  const res: (IEquipment | undefined)[] = []
  const raritiyList = ['神器','史诗']
  const categorize = Array.from(new Set(items.map((item) => item.categorize)))
  raritiyList.forEach((rarity) => {
    categorize.forEach((cat) => {
      const equ : (IEquipment | undefined)[]  = items.filter((a) => a.rarity === rarity && a.categorize === cat)
      equ.splice(5,0,undefined)
      res.push(
        ...equ,
        ...Array(Math.max(0,rowCount - equ.length)).fill(undefined),
      )
    })
  })
  return res
})
</script>
