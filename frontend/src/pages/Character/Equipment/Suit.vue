<!-- 每排总计6+4+4,共计14个排列 -->

<template>
  <div>
    <div class="flex gao-10px">
    <!-- 套装选择tab -->
    <div class="flex flex-wrap w-300px">
      <template v-for="(suit, _) in suits" :key="_">
        <div class="flex items-center justify-center">
          <img
            class="w-40px h-40px object-contain"
            :src="getImageURL('equipment' + suit.imageUrl)"
            :alt="suit.name"
            :style="{ filter: curSuit === suit.value ? '' : 'grayscale(100%)' }"
            @click="curSuit = suit.value"
          />
        </div>
      </template>
    </div>
    <EquipmentRaritySelect v-model="curRarity" />
    </div>

    <div class="flex flex-wrap gap-4px content-start" :style="{width: `${rowCount * 32}px`}">
    <template v-for="(equip,_) in suitEquipments" :key="_">
      <EquipmentIcon :equipment="equip" />
    </template>
  </div>
  </div>
</template>

<script lang="ts" setup>
import type { IEquipment } from '@/api/info/type'
import { useInfoStore } from '@/stores'
import { getImageURL } from '@/utils/images'
import EquipmentIcon from '@/components/dnf/Equipment/Icon/index.vue'
import EquipmentRaritySelect from '@/components/dnf/Equipment/RaritySelect/index.vue'
const infoStore = useInfoStore()
const curSuit = ref(16201)

const curRarity = ref()

const props = defineProps<{
  rowCount?:number
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
  const equs =  infoStore.equips.filter((a) => a.suit.includes(curSuit.value) && a.suit.length === 1)

  const res: (IEquipment | undefined)[] = []
  const raritiyList = ['神器','传说','史诗']
  raritiyList.forEach((rarity) => {
    const equ : (IEquipment | undefined)[]  = equs.filter((a) => a.rarity === rarity && !a.name.includes('黑牙'))
    equ.splice(5,0,undefined)
    equ.splice(9,0,undefined)
    res.push(
      ...equ,
      ...Array(Math.max(0,rowCount - equ.length)).fill(undefined),
    )
  })
  const remind = equs.filter(a=>a.rarity == '太初' || a.name.includes('黑牙')).sort((a,b)=>(a.rarity == '太初' ? 1 : 0) - (b.rarity == '太初' ? 1 : 0))
  res.push(undefined,undefined,...remind.filter(a=>a.itemDetailType == '项链'),undefined,...remind.filter(a=>a.itemDetailType == '手镯'),undefined,...remind.filter(a=>a.itemDetailType == '戒指'),...Array(Math.max(0,rowCount - remind.length -4)).fill(undefined))
  return res
  // const raritiyList = [['神器'],['传说'],['史诗','太初']]
  // const partList = ['上衣','下装','头肩','腰带','鞋','项链','手镯','辅助装备','魔法石','耳环']
  // // 一个品质占3行
  // // 第一行 防具5+空+特殊3
  // // 第二行 首饰3+3+3
  // // 第三行 全空行
  // partList.forEach((part) => {
  //   const equ = equs.filter((a) => a.itemDetailType === part)
  //   res.push(
  //     ...equ,
  //     ...Array(rowCount - equ.length).fill(undefined),
  //   )
  // })
  // return res
})


</script>
