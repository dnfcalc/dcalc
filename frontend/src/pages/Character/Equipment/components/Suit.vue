<!-- 每排总计6+4+4,共计14个排列 -->

<template>
  <div>
    <div class="flex flex-col gap-10px pb-10px">
      <!-- 套装选择tab -->
      <div class="flex flex-wrap w-100%">
        <template v-for="(suit, _) in suits" :key="_">
          <div class="flex items-center justify-center">
            <img
              class="w-35px h-35px object-contain"
              :src="getImageURL('equipment' + suit.imageUrl)"
              :alt="suit.name"
              :style="{ filter: curSuit === suit.value ? '' : 'grayscale(100%)' }"
              @click="curSuit = suit.value"
              @dblclick="handleDoubleClick"
            />
          </div>
        </template>
      </div>
      <EquipmentRaritySelect v-model="curRarity" />
    </div>

    <div class="flex flex-wrap gap-4px content-start" :style="{ width: `${rowCount * 32}px` }">
      <template v-for="(equip, _) in suitEquipments" :key="_">
        <template v-if="equip?.rarity == curRarity || !curRarity">
          <EquipmentIcon
            :equipment="equip"
            :inactive="configStore.config.equips[equip?.itemDetailType ?? '']?.id != equip?.id"
            @click="configStore.chooseEqu(equip)"
          />
        </template>

        <template v-else>
          <EquipmentIcon />
        </template>
      </template>
    </div>
  </div>
</template>

<script lang="ts" setup>
import type { IEquipment } from '@/api/info/type'
import { useConfigStore, useInfoStore } from '@/stores'
import { getImageURL } from '@/utils/images'
import EquipmentIcon from '@/components/dnf/Equipment/Icon/index.vue'
import EquipmentRaritySelect from '@/components/dnf/Equipment/RaritySelect/index.vue'
const infoStore = useInfoStore()
const configStore = useConfigStore()
const curSuit = ref(16201)

const curRarity = ref()

const props = defineProps<{
  rowCount?: number
}>()

const rowCount = Math.max(props.rowCount ?? 0, 14)

const suits = computed(() => {
  const uniqueSuits = new Map<number, { name: string; value: number; imageUrl: string }>()
  infoStore.suits.forEach((a) => {
    if (!uniqueSuits.has(a.suitId)) {
      uniqueSuits.set(a.suitId, { name: a.name, value: a.suitId, imageUrl: a.imageUrl })
    }
  })
  return Array.from(uniqueSuits.values())
})

const suitEquipments = computed(() => {
  const equs = infoStore.equips.filter(
    (a) => a.suit.includes(curSuit.value.toString()) && a.suit.length === 1,
  )

  const res: (IEquipment | undefined)[] = []
  const raritiyList = ['神器', '传说', '史诗']
  raritiyList.forEach((rarity) => {
    const equ: (IEquipment | undefined)[] = equs.filter(
      (a) => a.rarity === rarity && !a.name.includes('黑牙'),
    )
    equ.splice(5, 0, undefined)
    equ.splice(9, 0, undefined)
    res.push(...equ, ...Array(Math.max(0, rowCount - equ.length)).fill(undefined))
  })
  const remind = equs
    .filter((a) => a.rarity == '太初' || a.name.includes('黑牙'))
    .sort((a, b) => (a.rarity == '太初' ? 1 : 0) - (b.rarity == '太初' ? 1 : 0))
  res.push(
    undefined,
    undefined,
    ...remind.filter((a) => a.itemDetailType == '项链'),
    undefined,
    ...remind.filter((a) => a.itemDetailType == '手镯'),
    undefined,
    ...remind.filter((a) => a.itemDetailType == '戒指'),
    ...Array(Math.max(0, rowCount - remind.length - 4)).fill(undefined),
  )
  return res
})

const handleDoubleClick = () => {
  if (!curRarity.value) return
  if (curRarity.value == '太初') return
  suitEquipments.value
    .filter((a) => !!a && a.rarity == curRarity.value)
    .splice(0, 11)
    .forEach((a) => {
      configStore.chooseEqu(a)
    })
}
</script>
