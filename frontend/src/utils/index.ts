export function in_range(num: number, start: number, end: number) {
  return start <= num && num <= end
}

export function to_percent(num?: number, defaultValue: number = 0, suffix = "", withPlus = false) {
  num = num ?? defaultValue
  return (num > 0 && withPlus ? "+" : "") + num?.multiply(100).round(2).toString().concat(suffix)
}

export function get_num(num?: number, defaultValue: number = 0) {
  return num ?? defaultValue
}

export function format_string(str: string, params: any = {}, ...args: any[]) {
  let num = 0
  str = str.replace(/{}/g, match => {
    return args[num++] ?? match
  })
  str = str.replace(/{\d+}/g, match => {
    const i = Number.parseInt(match.slice(1, -1))
    return args[i] ?? match
  })
  str = str.replace(/{\w+}/g, match => {
    const name = match.slice(1, -1)
    return params[name] ?? match
  })
  return str
}

export function format_bytes(bytes: number, decimals = 2) {
  if (bytes === 0) {
    return "0 Bytes"
  }
  const k = 1024
  const dm = decimals < 0 ? 0 : decimals
  const sizes = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]

  const i = Math.floor(Math.log(bytes) / Math.log(k))

  return `${Number.parseFloat((bytes / k ** i).toFixed(dm))} ${sizes[i]}`
}

export function getFloat(value: any, n: any) {
  value = Number(value)
  n = n ? Number.parseInt(n) : 0
  if (n <= 0) {
    return Math.round(value)
  }
  value = Math.round(value * 10 ** n) / 10 ** n
  value = Number(value).toFixed(n)
  return value
}

export function cartesian<T = any>(...arr: T[][]): T[][] {
  if (arr.length < 2) {
    return arr
  }
  return arr.reduce(
    (a, b) => {
      const ret: T[][] = []
      a.forEach(a => {
        b.forEach(b => {
          ret.push(a.concat([b]))
        })
      })
      return ret
    },
    [[]] as T[][]
  )
}

export function groupBy<T, K>(array: T[], callback: (t: T) => K) {
  const map = new Map<K, T[]>()
  for (let i = 0; i < array.length; i++) {
    const t = array[i]
    const key = callback(t)
    const temp: T[] = map.get(key) || []
    if (!map.has(key)) {
      map.set(key, temp)
    }
    temp.push(t)
  }

  return Array.from(map.values())
}

export function debounce_last(func: Function, wait: number) {
  let timer = Number.NaN
  return function () {
    if (timer) {
      clearTimeout(timer)
    }
    timer = setTimeout(func, wait)
  }
}

export function padding(num: number | string, length: number): string {
  if ((`${num}`).length >= length) {
    return `${num}`
  }
  return padding(`0${num}`, length)
}

export function format_float(f: number, digit: number = 2) {
  const m = 10 ** digit
  return (f * m).round(10) / m
}

export function mapRecord<T extends keyof any, K>(status: Record<T, K>, callback: (value: K, key: T) => K) {
  const new_status = {} as Record<T, K>
  for (const key in status) {
    const value = callback(status[key], key)
    if (value) {
      new_status[key] = value
    }
  }
  return new_status
}

Array.prototype.max = function<T>(callback: (t: T) => number): [number, T | undefined] {
  let rs: [number, T | undefined] = [-1, undefined]
  let max = -1
  for (let i = 0; i < this.length; i++) {
    const item = this.at(i) as T
    const count = callback(item)
    if (count > max) {
      max = count
      rs = [i, item]
    }
  }
  return rs
}

Array.prototype.min = function<T>(callback: (t: T) => number): [number, T | undefined] {
  let rs: [number, T | undefined] = [-1, undefined]
  let min = -1
  for (let i = 0; i < this.length; i++) {
    const item = this.at(i) as T
    const count = callback(item)
    if (count < min) {
      min = count
      rs = [i, item]
    }
  }
  return rs
}

Number.prototype.multiply = function (value: number) {
  return Number(this) * value
}

Number.prototype.round = function (digit?: number) {
  const m = 10 ** (digit ?? 0)
  return Math.round(Number(this) * m) / m
}

export function formatStr(template: string, ...params: any) {
  let str = template

  if (params.length == 1 && params[0].length > 0) {
    params = params[0]
  }

  for (let i = 0; i < params.length; i++) {
    str = str.replaceAll(`{${i}}`, params[i])
  }

  return str
}

export function toObj(data: any): any {
  const temp = {}
  for (const key in data) {
    try {
      if (typeof data[key] === "number" || typeof data[key] === "string") {
        Object.defineProperty(temp, key, {
          value: data[key],
          writable: true,
          enumerable: true,
          configurable: true
        })
      } else {
        Object.defineProperty(temp, key, {
          value: RecordToObj(data[key]),
          writable: true,
          enumerable: true,
          configurable: true
        })
      }
    } catch {
      Object.defineProperty(temp, key, {
        value: data[key],
        writable: true,
        enumerable: true,
        configurable: true
      })
    }
  }
  return temp
}

export function toMap(data: any, except: string[] = []) {
  const temp = {}
  for (const key in data) {
    if (typeof data[key] === "object" && data[key].constructor != Array && !except.includes(key)) {
      // 需要转换部分,不能是Array,也会被转换
      const sub = {}
      for (const subkey in data[key]) {
        Object.defineProperty(sub, subkey, {
          value: new Map(Object.entries(data[key][subkey])),
          writable: true,
          enumerable: true,
          configurable: true
        })
      }
      Object.defineProperty(temp, key, {
        value: sub,
        writable: true,
        enumerable: true,
        configurable: true
      })
    } else {
      Object.defineProperty(temp, key, {
        value: data[key],
        writable: true,
        enumerable: true,
        configurable: true
      })
    }
  }
  return temp
}

export function RecordToObj(todo: Record<string, Map<any, any>>) {
  const temp = {}
  for (const key in todo) {
    Object.defineProperty(temp, key, {
      value: Object.fromEntries(todo[key]),
      writable: true,
      enumerable: true,
      configurable: true
    })
  }
  return temp
}

export function getUuid() {
  if (typeof crypto === "object") {
    if (typeof crypto.randomUUID === "function") {
      return crypto.randomUUID()
    }
    if (typeof crypto.getRandomValues === "function" && typeof Uint8Array === "function") {
      const callback = (c: any) => {
        const num = Number(c)
        return (num ^ (crypto.getRandomValues(new Uint8Array(1))[0] & (15 >> (num / 4)))).toString(16)
      }
      return "10000000-1000-4000-8000-100000000000".replace(/[018]/g, callback)
    }
  }
  let timestamp = new Date().getTime()
  let perforNow = (typeof performance !== "undefined" && performance.now && performance.now() * 1000) || 0
  return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, c => {
    let random = Math.random() * 16
    if (timestamp > 0) {
      random = Math.trunc((timestamp + random) % 16)
      timestamp = Math.floor(timestamp / 16)
    } else {
      random = Math.trunc((perforNow + random) % 16)
      perforNow = Math.floor(perforNow / 16)
    }
    return (c === "x" ? random : (random & 0x3) | 0x8).toString(16)
  })
}


export function rarityClass(type: string) {
  switch (type) {
    case "太初":
      return "primeval"
    case "史诗":
      return "epic"
    case "神话":
      return "myth"
    case "智慧产物":
      return "epic"
    case "神器":
      return "artifact"
    case "稀有":
      return "rare"
    case "传说":
      return "legend"
    case "勇者":
      return "chronicle"
    case "高级":
      return "advanced"
    default:
      return "epic"
  }
}

export function formatAttr(type:string,value:number){
  switch(type){
    case "STR":
      return `力量 ${value}`
    case "INT":
      return `智力 ${value}`
    case "Vitality":
      return `体力 ${value}`
    case "Spirit":
      return `精神 ${value}`
    case "AtkP":
      return `物理攻击力 ${value}`
    case "AtkM":
      return `魔法攻击力 ${value}`
    case "AtkI":
      return `独立攻击力 ${value}`
    case "SkillAttack":
      return `技能伤害 +${(value * 100).toFixed(2)}%`
    case "Attack":
      return `攻击强化 +${(value).toFixed(1)}%`
    case "Buffer":
      return `增益量 ${(value)}`
    default:
      return `${type} ${value}`
  }
}


export const decrypt = (encryptedData:string)=>{
  try{
    encryptedData = decodeURIComponent(encryptedData).split("").map(a=>{
      if(a=='='){
        return a
      }
      else{
        return String.fromCharCode(a.charCodeAt(0) - 1)
      }
    }).join("")
    const decryptedData = atob(encryptedData);

    const len = decryptedData.length;
    const decryptedBinaryOffset = decryptedData.slice(0, len-13);
    const decryptedTimestamp = decryptedData.slice(len-13, len);

    return {
      uid:parseInt(decryptedBinaryOffset,2),
      time:parseInt(decryptedTimestamp)
    }
  }
  catch(e){
    console.log(e)
    return {
      uid:-1,
      time:0
    }
  }
}
