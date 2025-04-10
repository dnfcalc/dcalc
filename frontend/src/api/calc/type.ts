export interface IResult {
  uuid: string
  skills: IResultSkill[]
  info:IResultUserInfo[]
  suits:IResultSuit[]
}

export interface IResultSkill {
  name: string
  icon: string
  lv: number
  data: number
  ratio: number
  cd: number
  damage: number
  mode: string
}

export interface IResultUserInfo {
  name:string
  value:string|number
}

export interface IResultSuit{
  id:number
  count:number
  imageUrl:string
  level:number
  name:string
  point:number
  rarity:string
  value:string
}

export interface IResultSkillCount {
  count: number
  mode: string
  name: string
}
