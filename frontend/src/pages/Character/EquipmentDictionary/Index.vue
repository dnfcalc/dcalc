<template>
  <div class="w-330px bg-black">
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
    <div class="p-1 space-y-1">
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
          <template v-for="(suit, _) in suits" :key="_">
            <div class="flex items-center justify-center gap-2">
              <img
                class="w-20px h-auto object-cover"
                :src="getImageURL('equipment' + suit.imageUrl)"
                :alt="suit.name"
                :style="{
                  filter: curSuit == suit.value ? '' : 'grayscale(100%)',
                }"
                @click="curSuit = suit.value"
              />
            </div>
          </template>
        </div>
      </div>
      <template v-for="item in equs" :key="item.name">
        <template v-if="item.equs.length > 0">
          <div class="item-head">{{ item.name }}</div>
          <div class="flex flex-wrap gap-4px content-start w-full">
            <template v-for="(weapon, _) in item.equs" :key="_">
              <EquipmentIcon :equipment="weapon" />
            </template>
          </div>
        </template>
      </template>
    </div>

    <!-- 筛选条件 -->
    <!-- 装备列表 -->
  </div>
</template>
<script lang="ts" setup>
import { useInfoStore } from '@/stores'
import PartSelect from '@/components/dnf/Equipment/PartSelect/index.vue'
import EquipmentRaritySelect from '@/components/dnf/Equipment/RaritySelect/index.vue'
import { getImageURL } from '@/utils/images'
import type { IEquipment } from '@/api/info/type'
import EquipmentIcon from '@/components/dnf/Equipment/Icon/index.vue'

const infoStore = useInfoStore()
const type = ref('equ')
const curRarity = ref('')
const curSuit = ref(16203)

const choose_part = ref<string[]>([])

const chooseCategory = (cat: string) => {
  type.value = cat
}

const rowCount = 10

const suits = computed(() => {
  const uniqueSuits = new Map<number, { name: string; value: number; imageUrl: string }>()
  infoStore.suits.forEach((a) => {
    if (!uniqueSuits.has(a.suitId)) {
      uniqueSuits.set(a.suitId, {
        name: a.name,
        value: a.suitId,
        imageUrl: a.imageUrl.replace('/suit', '/suit/little'),
      })
    }
  })
  const res = Array.from(uniqueSuits.values())
  res.push({
    name: '通宝',
    value: -1,
    imageUrl: '/suit/little/-1.png',
  })
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
        (curSuit.value == -1 && a.suit.length > 1) ||
        (a.suit.includes(curSuit.value.toString()) && a.suit.length === 1)),
  )

  // 武器
  const item_weapon = total.filter((a) => a.itemType == '武器') ?? []
  const weapons: (IEquipment | undefined)[] = []
  if (item_weapon.length > 0) {
    Array.from(new Set(item_weapon.map((item) => item.rarity))).forEach((rarity) => {
      const weapon = item_weapon
        .filter((item) => item.rarity === rarity)
        .sort((a, b) => {
          if (a.categorize == b.categorize) {
            return a.itemDetailType.localeCompare(b.itemDetailType)
          }
          return b.categorize.localeCompare(a.categorize)
        })
      weapons.push(...weapon)
      const remind = weapons.length % rowCount
      remind > 0 && weapons.push(...Array(rowCount - remind).fill(undefined))
    })
  }

  // # region 副武器
  const subWeapons: (IEquipment | undefined)[] = []
  const item_sub_weapon = (
    total.filter((a) => infoStore.infos?.subweapons?.includes(a.itemDetailType)) ?? []
  ).sort((a, b) => {
    if (a.categorize == b.categorize) {
      return a.itemDetailType.localeCompare(b.itemDetailType)
    }
    return b.categorize.localeCompare(a.categorize)
  })
  if (item_sub_weapon.length > 0) {
    subWeapons.push(
      ...item_sub_weapon,
      ...Array(rowCount - (item_sub_weapon.length % rowCount)).fill(undefined),
    )
  }
  // # endregion

  // 秘宝
  const item_treasure = total.filter((equip) => equip.categorize.includes('秘宝'))
  const treasures: (IEquipment | undefined)[] = []
  if (item_treasure.length > 0) {
    treasures.push(
      ...item_treasure,
      ...Array(rowCount - (item_treasure.length % rowCount)).fill(undefined),
    )
  }
  // 套装
  const item_suits = total.filter(
    (equip) => equip.categorize.includes('套装') || equip.categorize.includes('通宝'),
  )
  const suits: (IEquipment | undefined)[] = []
  const raritiyList = Array.from(new Set(item_suits.map((item) => item.rarity)))
  raritiyList.forEach((rarity) => {
    const armor = item_suits.filter((item) => item.rarity === rarity && item.itemType === '防具')
    if (armor.length > 0) {
      suits.push(...armor, undefined)
    }

    const special = item_suits.filter(
      (item) => item.rarity === rarity && item.itemType === '特殊装备',
    )
    if (special.length > 0) {
      suits.push(...special)
      if (suits.length % rowCount > 0) {
        suits.push(...Array(rowCount - (suits.length % rowCount)).fill(undefined))
      }
    }

    const jewelry = item_suits.filter((item) => item.rarity === rarity && item.itemType === '首饰')
    const jewelryNormal = jewelry.filter((a) => !a.name.includes('黑牙')) ?? []
    const jewelryHY = jewelry.filter((a) => a.name.includes('黑牙')) ?? []
    if (jewelry.length > 0) {
      suits.push(
        ...Array(3 - jewelryHY.length + 2).fill(undefined),
        ...jewelryHY,
        undefined,
        ...jewelryNormal,
      )
      suits.push(...Array(rowCount - (suits.length % rowCount)).fill(undefined))
    }
  })
  // 称号
  const item_title = total.filter((equip) => equip.itemDetailType == '称号')
  const title: (IEquipment | undefined)[] = []
  if (item_title.length > 0) {
    title.push(...item_title, ...Array(rowCount - (item_title.length % rowCount)).fill(undefined))
  }
  // 宠物
  const item_pets = total.filter((equip) => equip.itemDetailType == '宠物')
  const pet: (IEquipment | undefined)[] = []
  if (item_pets.length > 0) {
    pet.push(...item_pets, ...Array(rowCount - (item_pets.length % rowCount)).fill(undefined))
  }

  // 称号
  return [
    {
      name: '武器',
      equs: weapons,
    },
    {
      name: '副武器',
      equs: subWeapons,
    },
    {
      name: '秘宝',
      equs: treasures,
    },
    {
      name: '套装',
      equs: suits,
    },
    {
      name: '称号',
      equs: title,
    },
    {
      name: '宠物',
      equs: pet,
    },
  ]
})
</script>

<style lang="scss" scoped>
.active {
  color: #ccc088;

  &::after {
    content: '';
    position: absolute;
    width: 60px;
    height: 15px;
    opacity: 0.35;
    background: #bf8d20;
    filter: blur(7px);
  }
}

.item-head {
  background: linear-gradient(#2b2817, #171407);
  border-top: 1px solid #423d2c;
  border-bottom: 1px solid #211d15;
  text-align: center;
}
</style>
