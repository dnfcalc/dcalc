import type { IEquipment } from "@/api/info/type"

export const rowCount = 10

export const formatEqu = (total: IEquipment[],subweapons?:string[],curSuit
  ?:string) => {
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
    total.filter((a) => subweapons?.includes(a.itemDetailType)) ?? []
  ).sort((a, b) => {
    if (a.categorize == b.categorize) {
      return a.itemDetailType.localeCompare(b.itemDetailType)
    }
    return b.categorize.localeCompare(a.categorize)
  })
  if (item_sub_weapon.length > 0) {
    subWeapons.push(
      ...item_sub_weapon.map((a) => ({ ...a, itemType: '副武器' })),
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
    if (suits.length % rowCount > 0) {
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
      name: `${curSuit} 套装`,
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
}

export const formatStone = (total: IEquipment[],curSuit?:string) => {
  // 套装
  const item_suits = total.filter((equip) => equip.suit.length == 1)
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
    if (suits.length % rowCount > 0) {
      suits.push(...Array(rowCount - (suits.length % rowCount)).fill(undefined))
    }
  })

  const item_suits_wns = total.filter((equip) => equip.categorize.includes('维纳斯通宝'))
  const wns: (IEquipment | undefined)[] = []
  const categorizeList = Array.from(new Set(item_suits_wns.map((item) => item.categorize)))
  categorizeList.forEach((categorize) => {
    ;['神器', '史诗'].forEach((raritiy) => {
      const temp = item_suits_wns.filter(
        (item) => item.categorize === categorize && item.rarity === raritiy,
      )
      const remind = temp.length % (rowCount / 2)
      wns.push(...temp, ...Array(temp.length == 0 ? rowCount / 2 - remind : remind).fill(undefined))
    })
  })

  const item_suits_nbe = total.filter((equip) => equip.categorize.includes('纳波尔通宝'))
  const nbes: (IEquipment | undefined)[] = []
  const nbeList = Array.from(new Set(item_suits_nbe.map((item) => item.categorize)))
  nbeList.forEach((categorize) => {
    ;['神器', '史诗'].forEach((raritiy) => {
      const temp = item_suits_nbe.filter(
        (item) => item.categorize === categorize && item.rarity === raritiy,
      )
      const remind = temp.length % (rowCount / 2)
      nbes.push(
        ...temp,
        ...Array(temp.length == 0 ? rowCount / 2 - remind : remind - 1).fill(undefined),
      )
    })
  })

  const items_suits_rzs = total.filter((equip) => equip.categorize.includes('人造神'))
  const rzs: (IEquipment | undefined)[] = []
  const partList = Array.from(new Set(items_suits_rzs.map((item) => item.itemDetailType)))
  // const raritiy = Array.from(new Set(items_suits_rzs.map((item) => item.rarity)))
  partList.forEach((part) => {
    raritiyList.forEach((rarity) => {
      const temp = items_suits_rzs.filter(
        (item) => item.itemDetailType === part && item.rarity === rarity,
      )
      temp.length > 0 && rzs.push(...temp, ...Array(rowCount - temp.length).fill(undefined))
    })
    // const temp = items_suits_rzs.filter((item) => item.itemDetailType === part)
    // const remind = temp.length % rowCount
    // rzs.push(...temp, ...Array(temp.length == 0 ? rowCount-remind : remind).fill(undefined))
  })
  return [
    {
      name: `${curSuit} 套装`,
      equs: suits,
    },
    {
      name: '维纳斯通宝',
      equs: wns,
    },
    {
      name: '纳波尔通宝',
      equs: nbes,
    },
    {
      name: '人造神',
      equs: rzs,
    },
  ]
}
