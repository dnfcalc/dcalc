export interface IResult {
  skills: IResultSkill[]
}

export interface IResultSkill {
  name: string
  icon: string
  lv: number
  data: number
  ratio: number
  cd: number
  damage: number
}
