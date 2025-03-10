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
  target: '_blank' | '_self'
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
