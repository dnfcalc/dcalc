import { defineStore } from 'pinia'
import { useInfoStore } from './info'
import api from '@/api'
import type { IEquipment } from '@/api/info/type'
// | '上衣'
// | '头肩'
// | '下装'
// | '腰带'
// | '鞋'
// | '手镯'
// | '项链'
// | '戒指'
// | '耳环'
// | '辅助装备'
// | '魔法石'
// | '武器',
export interface IConfig {
  skills: Record<string, { lv: number }>
  equips: Record<
    string,
    {
      id: string
      reinforce: number
      reinforceType: number
      enchant: number
      emblem_0: string
      emblem_1: string
      upgrade: number
      refine: number
      adaptation: number
      fusion: string
    }
  >
  jades: Record<string, number>
}

const defaultEqusConfig = {
  id: '',
  reinforce: 0,
  reinforceType: 0,
  enchant: 0,
  emblem_0: "0",
  emblem_1: "0",
  upgrade: 0,
  refine: 0,
  adaptation: 0,
  fusion: '',
}

export const useConfigStore = defineStore('configStore', () => {
  const config = ref<IConfig>({
    skills: {},
    equips: {},
    jades: {},
  })

  const loadConfig = () => {
    const infoStore = useInfoStore()
    const alter = infoStore.infos?.alter

    if (alter) {
      const localConfig = localStorage.getItem(`dcalc/${alter}/config`)
      if (localConfig) {
        config.value = JSON.parse(localConfig)
      }
    }
    if (!config.value)
      config.value = {
        skills: {},
        equips: {},
        jades: {},
      }
    if (!config.value?.equips) config.value.equips = {}
    if (!config.value?.skills) config.value.skills = {}
    if (!config.value?.jades) config.value.jades = {}

    const part = infoStore.parts.filter((a) => !config.value?.equips.hasOwnProperty(a))

    const skillIDs = infoStore.skills
      .map((skill) => skill.id.toString())
      .filter((a) => !config.value?.skills.hasOwnProperty(a))

    part.forEach((p) => {
      config.value && (config.value.equips[p] = { ...defaultEqusConfig })
    })

    skillIDs.forEach((id) => {
      config.value &&
        (config.value.skills[id] = {
          lv: infoStore.skills.find((skill) => skill.id.toString() === id)?.maxLearnLv ?? 0,
        })
    })
  }

  const saveConfig = () => {
    const infoStore = useInfoStore()
    const alter = infoStore.infos?.alter
    if (alter) {
      localStorage.setItem(`dcalc/${alter}/config`, JSON.stringify(config.value))
    }
  }

  const calc = async () => {
    if(!useInfoStore().infos?.alter) return undefined
    return await api.calc(config.value)
  }

  const chooseEqu = async(equip: IEquipment | undefined,isFusion:boolean = false) => {
    if (equip && config.value.equips[equip.itemDetailType]) {
      const key = isFusion ? 'fusion' : 'id'
      if (config.value.equips[equip.itemDetailType][key] == equip.id) {
        config.value.equips[equip.itemDetailType][key] = ""
      } else {
        config.value.equips[equip.itemDetailType][key] = equip.id
      }
    }
  }


  const result = useAsyncState(
    () => {
      return calc()
    },
    {
      skills:[]
    },
    { resetOnExecute: false },
  )


  return {
    config,
    loadConfig,
    saveConfig,
    calc,
    result,
    chooseEqu
  }
})
