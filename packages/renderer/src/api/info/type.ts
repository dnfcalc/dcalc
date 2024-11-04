export interface IAdventureInfo {
  title: string
  name: string
  children: IAlterInfo[]
}

export interface ITools {
  name: string
  tooltips: string
  link: string
  end?: Date
  target:"_blank" | "_self"
}

export interface IMonster {
  id: number
  name: string
}

export interface IAlterOption {
  name: string
  title: string
  class?: string
}

export interface IAlterInfo {
  name: string
  url?: string
  title: string
  default_value: string
  options?: IAlterOption[]
  open?: boolean
  comment?: string
}

export interface IEquipmentInfo {
  groupId: number
  id: ID
  type?: string
  rarity?: string
  part: string
  name: string
  icon: string
  state?: boolean
  features?: ID[]
  alternative: number[]
  order?: number
  growth: ID[]
  stable: ID[]
  suit: string[]
  lv: number
}

export interface IEquipmentList {
  lv110: IEquipmentInfo[]
  myth: IEquipmentInfo[]
  weapon: IEquipmentInfo[]
  wisdom: IEquipmentInfo[]
  title: IEquipmentInfo[]
  pet: IEquipmentInfo[]
  consumable: IEquipmentInfo[]
  fusion: IEquipmentInfo[]
  merge: IEquipmentInfo[]
}

export interface IEnchantingInfo {
  id: string | number
  maxFame: number | undefined
  position: string[]
  props: string
  type: string | undefined
  rarity: string | undefined
  rate: number
}

export interface IJadeInfo {
  id: string | number
  min: string | number
  max: string | number
  props: string
  pre: number
  maxFame: string | number
  unit: string
}

export interface ISItemInfo {
  id: number
  name: string
  desc: string
  lvinfo: {
    lv: number
    cost: number
    needprecost: number
    params: number[]
    buffer: number
    remark: string[]
  }[]
  master: number
  masterWith?: number[]
  masterWithMax?: number
  x: number
  y: number
  preconditions: {
    id: number
    needLv: number
  }[]
  conflict?: number[]
}

export interface ISpecificityInfo {
  id: number
  title: number
  index: number
  position: string
  desc: string[]
  name: string
}

export interface ISpecificity {
  type: number
  name: string
  desc: string
  detail: ISItemInfo[]
}

export interface IAsrahan {
  name: string
  type: number
  desc: string
  max:string
  lvinfo: {
    lv: number
    params: string[]
  }[]
}



export interface ITrigger {
  id: number
  selectList: string[]
  "multi-select": boolean
}

export interface TriggerSet {
  id: number
  select: number | number[]
}

export interface Dress {
  id: number
  options: string[]
  part: string
  rarity: string
  suit?: string
  name: string
}

export interface KTV<T> {
  [key: number | string]: T
}

export interface BaseSkill {
  name: string

  mode?: string[]
}

export interface SkillSet {
  // 技能名
  name: string

  // 技能等级
  level: number

  // tp
  tp: number

  // 是否手搓
  direct: boolean

  // 方向键数目
  directNumber: number

  // 技能次数
  count: number | string

  // 宠物次数
  pet: number | string

  // 是否有伤害
  damage: boolean

  mode?: string[]
}
interface SkillQueue {
  name: string
  mode?: string
  modes?: string[]
}

export interface ICharacterSet {
  skill_set: SkillSet[]
  skill_que: SkillQueue[]

  forge_set: Record<string, Map<string, any>>

  equip_list: number[]

  comparison: number[]

  wisdom_list: number[]

  myths_list: number[]

  weapons_list: number[]

  lv110_list: number[]

  fusion_list: ID[]

  consumable_list: number[]

  title_list: number[]
  pet_list: number[]

  dress_set: Record<string, { id?: number; option?: string }>

  single_set: ID[]

  carry_type: string

  attack_attribute: number

  trigger_set: Record<string, number[] | number>

  customize: Record<string, number[]>

  merge: Record<string, number[]>

  rune_set: string[]

  talisman_set: string[]

  buff_ratio: number

  hotkey_set: string[]

  stone_set: Record<string, number[]>

  monster: number

  scene: number

  individuation: number[]

  specificity_list: number[]

  specificity: Record<string, number>

  corrections: {
    四维?: number
    三攻?: number
    技攻?: number
    攻击强化?: number
    BUFF量?: number
    攻击强化百分比?: number
    BUFF量百分比?: number
    攻速?: number
    火强?: number
    光强?: number
    冰强?: number
    暗强?: number
    火抗?: number
    冰抗?: number
    暗抗?: number
    光抗?: number
  }

  asrahan: {
    lv: number
    type: number
    additional: number
  }
}

export interface IRecommendRequest {
  page: number
  size: number
  alter?: string
  keyword?: string
}

export interface IRecommendEquip {
  id: ID
  props?: ID[]
  merge?: ID[]
}

export interface IRecommendInfo {
  id: ID
  name: string
  alter?: string
  author?: string
  equips: IRecommendEquip[]
  fusions?: {
    id: ID
  }[]
  fusion?: ID[]
  specificity?: Record<string, number>
}

export interface IDetailsInfo {
  enchanting: IEnchantingInfo[]
  emblem: IEnchantingInfo[]
  jade: IJadeInfo[]
  specificity?: ISpecificityInfo[] | ISpecificity[]
  especificity?: ISpecificity[]
  sundries: IEnchantingInfo[]
  dress: Record<string, Dress[]>
}

export interface IRank {
  icon: string
  id: string
  name: string
  pos: string
  props?: string[]
  upgradeInfo: {
    icon: string
    id: string
    name: string
  }
}

export interface IRankadventure {
  name: string
  title: string
  children: {
    name: string
    title: string
  }[]
}

export interface ISkillDetail {
  name: string
  need_level: number
  lv: number
  data: number
  cd: number
  mode: string
  original_data?: number
  original_cd?: number
  cost?: number
  tp?: number
  remark?: string
  type?: string
}

export interface ISkillInfo {
  type: string
  weapon: string
  buff: number
  skills_active: ISkillDetail[]
  skills_passive: ISkillDetail[]
  skills_cp: ISkillDetail[]
}
