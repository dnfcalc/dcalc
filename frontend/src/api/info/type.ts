export interface IAdventureInfo {
  title: string
  name: string
  children: IAlterInfo[]
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
  class?: string
}

export interface ICharacterInfo {
  role:string
  alter: string
  name: string
  equVersion: string
  equips: IEquipment[]
  weapons: string[]
  skills: ISkill[]
  suits: ISuit[]
}

export interface IEquipment {
  id: string
  imageUrl: string
  itemType: string
  itemDetailType: string
  name: string
  categorize:string
  suit:  number[]
  rarity:string
}

export interface ISkill {
  icon: string
  name: string
  id: number
  learnLv: number
  position: number
  type: string
  maxLearnLv: number
}

export interface ISuit {
  id: number
  name: string
  imageUrl: string
  suitId: number
}
