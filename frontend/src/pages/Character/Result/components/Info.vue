<template>
  <div class="bg-#000000bf w-264px">
    <div class="h-177px">
      <EquList :detail="props.equs" :with-sub-weapon="infoStore.infos?.alter.includes('vegabond')"></EquList>
    </div>
    <div class="flex flex-wrap border-y-1px my-1px border-y-solid border-#FFFF/10 gap-1% px-1%">
      <template v-for="info in props.info" :key="info.id">
        <div
          class="flex box-border mt-2px"
          :style="{ width: info.value.toString().includes('/') ? '100%' : '49%' }"
        >
          <div class="w-60px text-hex-836832">{{ info.name }}</div>
          <div class="ml-auto text-hex-3ea74e">{{ info.value }}</div>
        </div>
      </template>
    </div>
    <div class="border-y-1px border-y-solid my-1px border-#FFFF/10 bg-black">
      <template v-for="suit in props.suits" :key="suit.id">
        <div class="flex items-center px-5px">
          <img
            :src="getImageURL(`/equipment${suit.imageUrl}`)"
            alt=""
            class="w-20px h-20px object-contain"
          />
          <div class="flex px-5px flex-1 justify-between" :class="rarityClass(suit.rarity)">
            <span>{{ suit.name }} 套装</span>
            <span>{{ suit.rarity }} {{ lvFormat(suit.level, suit.rarity) }}</span>
            <span>{{ suit.point }}点</span>
          </div>
        </div>
      </template>
    </div>
    <div class="border-y-1px border-y-solid my-1px border-#FFFF/10">
      <div class="flex">
        <div class="flex-1 flex items-center justify-center bg-#221A08 text-#9A7E4A">
          穿戴装备信息
        </div>
      </div>
      <template v-for="part in partOrder" :key="part">
        <div class="flex p-2px partItem gap-5px">
          <img
            :src="getImageURL(`/equipment/part/${part}.png`)"
            alt=""
            class="w-20px h-20px object-contain"
          />
          <div class="flex items-center justify-center" v-if="adaptation(part) > 0">
            <img :src="getImageURL(`/equipment/adaptation/${adaptation(part)}.png`)" alt="" class="w-11px h-10px object-contain" />
          </div>
          <div
            class="flex items-center"
            :class="props.equs[part]?.reinforceType == 1 ? 'artifact' : 'advanced'"
          >
            +{{ props.equs[part]?.reinforce }}
          </div>
          <div class="rare" v-if="props.equs[part]?.refine > 0">({{ props.equs[part]?.refine }})</div>
          <div :class="rarityClass(equ(props.equs?.[part]?.id)?.rarity ?? '')">{{equ(props.equs?.[part]?.id)?.name}}</div>
        </div>
      </template>
    </div>
    <div class="h-40px w-full"></div>
  </div>
</template>

<script setup lang="ts" name="Info">
import { getImageURL } from '@/utils/images'
import { rarityClass } from '@/utils'
import type { IResultUserInfo, IResultSuit } from '@/api/calc/type'
import EquList from '@/components/dnf/Equipment/List/index.vue'
import type { IConfigEquip } from '@/stores/config'
import { useInfoStore } from '@/stores'

const props = defineProps<{
  info: IResultUserInfo[]
  suits: IResultSuit[]
  equs: Record<string, IConfigEquip>
}>()

const partOrder = [
  '武器',
  '上衣',
  '下装',
  '头肩',
  '腰带',
  '鞋',
  '项链',
  '手镯',
  '戒指',
  '辅助装备',
  '魔法石',
  '耳环',
]
const infoStore = useInfoStore()

const equ = (id: string) => {
  return infoStore.equips.find((e) => e.id == id)
}

const adaptation = (part: string) => {
  return Math.min(equ(props.equs?.[part]?.id)?.max_adaptation ?? 0, props.equs[part]?.adaptation ?? 0)
}

const lvFormat = (lv: number, rarity: string) => {
  if (rarity == '太初') return ''
  switch (lv) {
    case 1:
      return 'I'
    case 2:
      return 'II'
    case 3:
      return 'III'
    case 4:
      return 'IV'
    case 5:
      return 'V'
    default:
      return ''
  }
}
</script>

<style scoped lang="scss">
.partItem {
  display: flex;
  align-items: center;
}

.partItem:nth-child(2n + 1) {
  background-color: #0b090b;
}

.partItem:nth-child(2n) {
  background-color: #000100;
}
</style>
