export {}

declare module "pako"

declare global {
  type Num = string | number

  type ID = Num | undefined
  interface Window {
    // Expose some Api through preload script
    pywebview:{
      api: import("electron").IpcRenderer
      _bridge:any
    }
    removeLoading: () => void
    flag: boolean
  }

  interface PagingData<T> {
    data: T[]
    totalCount: number
    pageSize: number
    pageIndex: number
  }

  interface Number {
    plus(value: number): number

    minus(value: number): number

    multiply(value: number): number

    divide(value: number): number

    perMulti(value: number): number

    round(digit?: number): number

    floor(digit?: number): number

    exactlyDivide(value: number): number
  }

  interface Array<T> {
    min(callback: (t: T) => number): [number, T | undefined]
    max(callback: (t: T) => number): [number, T | undefined]
  }

  const APP_VERSION: string
}
