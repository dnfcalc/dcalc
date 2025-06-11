export interface IAdventureInfo {
  title: string
  name: string
  children: IAlterInfo[]
}
export interface IAlterOption {
  name: string
  title: string
  value?: string
}

export interface IAlterInfo {
  name: string
  url?: string
  title: string
  default_value: string
  options?: IAlterOption[]
  open?: boolean
  comment?: string
  value?: string
}

export interface ICharacterInfo {
  role: string
  alter: string
  name: string
  buffer: boolean
  equVersion: string
  equips: IEquipment[]
  properties: string[]
  stones: IEquipment[]
  enchants: IEnchantingInfo[]
  emblems: IEnchantingInfo[]
  weapons: string[]
  subweapons: string[]
  skills: ISkill[]
  suits: ISuit[]
  avatar: Record<string, IAvatarInfo[]>
  jades: IJade[]
  sundry: Record<string, ISundry>
  options: { id: number; name: string; options: string[] }[]
}

export interface ISundry {
  id: number
  options: {
    name: string
    value: number
  }[]
}

export interface IEquipment {
  id: string
  imageUrl: string
  itemType: string
  itemDetailType: string
  name: string
  categorize: string
  suit: string[]
  rarity: string
  max_adaptation: number
  STR: number[]
  INT: number[]
  Vitality: number[]
  Spirit: number[]
  AtkP: number[]
  AtkM: number[]
  AtkI: number[]
  SkillAttack: number[]
  Attack: number[]
  Buffer: number[]
  detail: string
  bufferDetail: string
}

export interface ISkill {
  icon: string
  name: string
  id: number
  learnLv: number
  position: number
  line: number
  type: string
  maxLearnLv: number
  maxLv: number
  bind: boolean
  hasVP: boolean
  hasUP: boolean
  vps: {
    name: string
    desc: string
  }[]
  uuid: string
  upType:'damage' |'heal'
}

export interface ISuit {
  id: number
  name: string
  imageUrl: string
  suitId: number
  suitName: string
  point: number
  rarity: string
  level: number
  SkillAttack: number
  Buffer: number
  value: string
}

export interface IEnchantingInfo {
  id: string | number
  fame: number | undefined
  position: string[]
  detail: string
  categorize: string[]
  rarity?: string
  type?: string
}

export interface IAvatarInfo {
  id: number
  options: string[]
  part: string
  rarity: string
  suit?: string
  name: string
}

export interface IJade {
  name: string
  id: number
  max: number
  min: number
  pre: number
  unit: string
}

export interface ISkillInfo {
  name: string
  type: string
  desc: string
  descDetail: string
  consumeItem: ConsumeItem
  descSpecial: string[]
  maxLevel: number
  requiredLevel: number
  requiredLevelRange: number
  preRequiredSkill: any
  jobId: string
  jobName: string
  jobGrowLevel: any[]
  evolution: Evolution[]
  enhancement: Enhancement[]
  attribute: Attribute
}

export interface ConsumeItem {
  itemId: string
  itemName: string
  value: number
}

export interface Evolution {
  type: number
  name: string
  desc: string
  descDetail: string
  skills?: string[]
}

export interface Enhancement {
  type: number
  status: Status[]
}

export interface Status {
  name: string
  value: string
}

export interface Attribute {
  optionDesc: string
  level: number
  consumeMp: number
  coolTime: number
  castingTime?: number
  optionValue: Record<`value${string}`, string>
  detail: string
}
