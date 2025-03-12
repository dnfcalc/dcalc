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
  class?:string
}

export interface ICharacterInfo {
  alter: string
  name: string
  equVersion: string
  equips: IEquipment[]
  weapons: string[]
  skills: ISkill[]
  suits: ISuit[]
}

export interface IEquipment {}

export interface ISkill {
  icon: string
  name: string
  id: number
  learnLv:number
  positon:number
}

export interface ISuit {}
