<template>
  <div class="w-340px bg-black flex flex-col h-90vh">
    <!-- 头部 选择是装备还是融合石 -->
    <div class="flex bg-#101012 h-40px text-#6C5E4A font-bold">
      <div
        class="flex-1 text-15px flex items-center justify-center"
        @click="chooseCategory('equ')"
        :class="{ active: type === 'equ' }"
      >
        装备
      </div>
      <div class="w-auto text-18px flex items-center justify-center !font-normal">|</div>
      <div
        class="flex-1 text-15px flex items-center justify-center"
        @click="chooseCategory('stone')"
        :class="{ active: type === 'stone' }"
      >
        融合石
      </div>
    </div>
    <div
      class="w-full h-1px bg-gradient-to-r from-[rgba(52,43,27,0.05)] via-[rgba(52,43,27,1)] to-[rgba(52,43,27,0.05)]"
    ></div>
    <div class="p-1 space-y-1 mt-10px">
      <div class="flex w-full">
        <div class="flex flex-1 items-center">
          部位：<part-select class="!max-w-25 !w-25" v-model:partList="choose_part"></part-select>
        </div>
        <div class="flex flex-1 items-center">
          品质：<EquipmentRaritySelect v-model="curRarity" />
        </div>
      </div>
      <div class="flex flex-1 items-center">
        <div class="flex items-center">
          套装：
          <div class="flex items-center justify-center gap-2px">
            <template v-for="(suit, _) in suitList" :key="_">
              <img
                class="w-auto h-15px"
                :src="getImageURL('equipment' + suit.imageUrl)"
                :alt="suit.name"
                :style="{
                  filter: curSuit == suit.value ? '' : 'grayscale(100%)',
                }"
                @click="curSuit = suit.value"
              />
            </template>
          </div>
        </div>
      </div>
    </div>
    <div class="overflow-y-auto gap-1 p-1 flex flex-col items-center flex-1 h-0">
        <template v-for="item in equs" :key="item.name">
          <template v-if="item.equs.length > 0">
            <div class="item-head w-full">{{ item.name }}</div>
            <div class="flex flex-wrap gap-4px justify-around w-full">
              <template v-for="(equ, _) in item.equs" :key="_">
                <EquipmentIcon
                  :inactive="!isActive(equ)"
                  :equipment="equ"
                  @click="chooseEqu(equ)"
                />
              </template>
            </div>
          </template>
        </template>
      </div>
  </div>
  <div class="px-5px flex flex-col">
    <div class="flex flex-col overflow-hidden bg-black" v-if="curEquInfo">
      <div class="item-head">基础信息</div>
      <div class="flex-1 overflow-y-auto overflow-x-hidden bg-black w-240px">
        <Info v-if="curEquInfo" :equipment="curEquInfo" />
      </div>
    </div>
    <div class="flex flex-col flex-1 overflow-hidden bg-black" v-if="curSuitInfo">
      <div class="item-head">套装信息</div>
      <div class="flex bg-#191918 items-center justify-center gap-2px p-5px">
        <calc-button
          :disabled="raritiyList.findIndex((rarity) => rarity === curSuitLv.rarity) <= 0"
          icon="min-little"
          @click="changeSuitLv('preRarity')"
        ></calc-button>
        <calc-button
          icon="reduce-little"
          :disabled="
            raritiyList.findIndex((rarity) => rarity === curSuitLv.rarity) <= 0 && curSuitLv.lv <= 1
          "
          @click="changeSuitLv('preLv')"
        ></calc-button>
        <div class="flex px-20px gap-x-10px" :class="rarityClass(curSuitLv.rarity)">
          <span>{{ curSuitLv.rarity }}</span>
          <span>{{ formatLv(curSuitLv.lv, curSuitLv.rarity) }}</span>
        </div>
        <calc-button
          :disabled="
            raritiyList.findIndex((rarity) => rarity === curSuitLv.rarity) >= raritiyList.length - 1
          "
          @click="changeSuitLv('nextLv')"
          icon="increase-little"
        ></calc-button>
        <calc-button
          :disabled="
            raritiyList.findIndex((rarity) => rarity === curSuitLv.rarity) >= raritiyList.length - 1
          "
          @click="changeSuitLv('nextRarity')"
          icon="max-little"
        ></calc-button>
      </div>
      <div
        class="w-80% m-auto h-1px bg-gradient-to-r from-[rgba(52,43,27,0.05)] via-[rgba(52,43,27,1)] to-[rgba(52,43,27,0.05)]"
      ></div>
      <div class="flex-1 overflow-y-auto overflow-x-hidden bg-black w-240px">
        <SuitInfo v-if="curSuitInfo" :suit="curSuitInfo" />
      </div>
    </div>
  </div>
</template>
<script lang="ts" setup>
import { useConfigStore, useInfoStore } from '@/stores'
import PartSelect from '@/components/dnf/Equipment/PartSelect/index.vue'
import EquipmentRaritySelect from '@/components/dnf/Equipment/RaritySelect/index.vue'
import { getImageURL } from '@/utils/images'
import { rarityClass } from '@/utils'
import type { IEquipment } from '@/api/info/type'
import EquipmentIcon from '@/components/dnf/Equipment/Icon/index.vue'
import Info from '@/components/dnf/Equipment/Info/index.vue'
import SuitInfo from '@/components/dnf/Equipment/SuitInfo/index.vue'
import { formatEqu, formatStone } from './formatData'

const infoStore = useInfoStore()
const type = ref('equ')
const curRarity = ref('')
const curSuit = ref(16203)
const curEquId = ref()
const curSuitLv = ref({
  rarity: '史诗',
  lv: 1,
})

const raritiyList = ['稀有', '神器', '传说', '史诗', '太初']

const formatLv = (number: number, raritiy?: string) => {
  if (raritiy == '太初') return ''
  const greekNumerals = ['Ι', 'ΙΙ', 'ΙΙΙ', 'ΙV', 'V', 'VΙ', 'VΙΙ', 'VΙΙΙ', 'ΙX', 'X']
  return greekNumerals[number - 1] || number.toString()
}

const changeSuitLv = (
  type: 'preRarity' | 'nextRarity' | 'preLv' | 'nextLv',
  resetLv: boolean = true,
) => {
  if (type == 'preRarity') {
    const index = raritiyList.findIndex((a) => a == curSuitLv.value.rarity)
    if (index > 0) {
      curSuitLv.value.rarity = raritiyList[index - 1]
      curSuitLv.value.lv = resetLv ? 1 : 5
      return
    }
  } else if (type == 'nextRarity') {
    const index = raritiyList.findIndex((a) => a == curSuitLv.value.rarity)
    if (index < raritiyList.length - 1) {
      curSuitLv.value.rarity = raritiyList[index + 1]
      curSuitLv.value.lv = 1
      return
    }
  } else if (type == 'preLv') {
    if (curSuitLv.value.lv > 1) {
      curSuitLv.value.lv--
      return
    } else {
      changeSuitLv('preRarity', false)
    }
  } else if (type == 'nextLv') {
    if (curSuitLv.value.lv < 5) {
      curSuitLv.value.lv++
      return
    } else {
      changeSuitLv('nextRarity')
    }
  }
}

const choose_part = ref<string[]>([])

const curEquInfo = computed(() => {
  if (type.value == 'equ') {
    return infoStore.equips.find((a) => a.id == curEquId.value)
  } else {
    return infoStore.stones.find((a) => a.id == curEquId.value)
  }
})

const curSuitInfo = computed(() => {
  if (curEquInfo.value?.suit.length != 1) {
    return undefined
  }
  return infoStore.suits.find(
    (a) =>
      a.suitId.toString() == curEquInfo.value?.suit[0] &&
      a.rarity == curSuitLv.value.rarity &&
      a.level == curSuitLv.value.lv,
  )
})

const chooseCategory = (cat: string) => {
  type.value = cat
  if (type.value == 'stone' && curSuit.value == -1) {
    curSuit.value = 16203
  }
}

const configStore = useConfigStore()

const suitList = computed(() => {
  const uniqueSuits = new Map<number, { name: string; value: number; imageUrl: string }>()
  infoStore.suits.forEach((a) => {
    if (!uniqueSuits.has(a.suitId)) {
      uniqueSuits.set(a.suitId, {
        name: a.suitName,
        value: a.suitId,
        imageUrl: a.imageUrl.replace('/suit/', '/suit/icon/'),
      })
    }
  })
  const res = Array.from(uniqueSuits.values())
  if (type.value == 'equ') res.push({ name: '通宝', value: -1, imageUrl: '/suit/icon/-1.png' })
  return res
})

const equs = computed(() => {
  // 筛选出装备
  const total = (type.value == 'equ' ? infoStore.equips : infoStore.stones).filter(
    (a) =>
      (!curRarity.value || a.rarity === curRarity.value) &&
      (choose_part.value.length === 0 ||
        choose_part.value.includes(a.itemDetailType || a.itemType)) &&
      (a.suit.length == 0 ||
        (curSuit.value == -1 && a.suit.length > 1 && type.value == 'equ') ||
        (a.suit.length > 1 && type.value == 'stone') ||
        (a.suit.includes(curSuit.value.toString()) && a.suit.length === 1)),
  )

  if (type.value == 'equ') {
    return formatEqu(
      total,
      infoStore.infos?.subweapons,
      suitList.value.find((a) => a.value == curSuit.value)?.name,
    )
  } else {
    return formatStone(total, suitList.value.find((a) => a.value == curSuit.value)?.name)
  }
})

const isActive = computed(() => {
  return (item?: IEquipment) => {
    if (!item) return false
    if (type.value == 'equ') {
      if (item.itemType.includes('武器')) {
        return configStore.config.equips[item.itemType].id == item.id
      } else {
        return configStore.config.equips[item.itemDetailType].id == item.id
      }
    } else {
      return configStore.config.equips[item.itemDetailType].fusion == item.id
    }
  }
})

const chooseEqu = (item?: IEquipment) => {
  if (!item) return
  curEquId.value = item.id
  const target =
    type.value === 'equ'
      ? configStore.config.equips[
          item.itemType.includes('武器') ? item.itemType : item.itemDetailType
        ]
      : configStore.config.equips[item.itemDetailType]
  target[type.value === 'equ' ? 'id' : 'fusion'] = isActive.value(item) ? '' : item.id
}
</script>

<style lang="scss" scoped>
.active {
  color: #ccc088;
  position: relative;

  &::before {
    content: '';
    position: absolute;
    width: 60px;
    height: 15px;
    opacity: 0.35;
    background: #bf8d20;
    filter: blur(7px);
    z-index: 2;
  }

  &::after {
    content: '';
    position: absolute;
    background: url('@/assets/img/active.png') no-repeat;
    width: 148px;
    height: 16px;
    bottom: 2px;
    transform: translate(0, 50%);
  }
}

.item-head {
  background: linear-gradient(#2b2817, #171407);
  border-top: 1px solid #423d2c;
  border-bottom: 1px solid #211d15;
  text-align: center;
}
</style>
