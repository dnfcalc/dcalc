import { defineStore } from 'pinia'
import { useInfoStore } from './info'
import api from '@/api'
import type { IEquipment } from '@/api/info/type'
import type { IResultSkillCount } from '@/api/calc/type'
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

export interface IConfigEquip {
  id: string
  reinforce: number
  reinforceType: number
  enchant: string
  emblem_0: string
  emblem_1: string
  upgrade: number
  refine: number
  adaptation: number
  fusion: string
  precision: number
  weaponFusion: number
}

export interface IConfig {
  skills: Record<string, { lv: number ,vp:number, up: number}>
  equips: Record<string, IConfigEquip>
  jades: Record<
    string,
    {
      id: number
      value: number
    }
  >
  avatar: Record<
    string,
    {
      id: string
      enchant: string
      emblem_0: string
      emblem_1: string
      option: string
    }
  >
  sundry: Record<string, any>
  bindAwake: number
  /** 系统奶 */
  DSB: boolean
  /** 奶 */
  BUFF: boolean
  options: Record<string, number>
}

const defaultEqusConfig = {
  id: '',
  reinforce: 0,
  reinforceType: 0,
  enchant: '',
  emblem_0: '',
  emblem_1: '',
  upgrade: 0,
  refine: 0,
  adaptation: 0,
  fusion: '',
  precision: 0,
  weaponFusion: 0,
}

const defaultAvatarConfig = {
  id: '',
  enchant: '',
  emblem_0: '',
  emblem_1: '',
  option: '0',
}

export const useConfigStore = defineStore('configStore', () => {
  const config = ref<IConfig>({
    skills: {},
    equips: {},
    jades: {},
    avatar: {},
    sundry: {},
    bindAwake: 50,
    DSB: false,
    BUFF: false,
    options:{}
  })

  const skillCountConfig = ref<IResultSkillCount[]>([])

  const loadConfig = () => {
    const infoStore = useInfoStore()
    const alter = infoStore.infos?.alter

    if (alter) {
      const localConfig = localStorage.getItem(`dcalc/${alter}/config`)
      const localSkillConfig = localStorage.getItem(`dcalc/${alter}/config/skillCount`)
      if (localConfig) {
        config.value = JSON.parse(localConfig)
      }
      if (localSkillConfig) {
        skillCountConfig.value = JSON.parse(localSkillConfig)
      }
    }
    if (!config.value)
      config.value = {
        skills: {},
        equips: {},
        jades: {},
        avatar: {},
        sundry: {},
        bindAwake: 50,
        DSB: false,
        BUFF: false,
        options:{}
      }
    if (!config.value?.equips) config.value.equips = {}
    if (!config.value?.skills) config.value.skills = {}
    if (!config.value?.jades) config.value.jades = {}
    if (!config.value?.avatar) config.value.avatar = {}
    if (!config.value?.sundry) config.value.sundry = {}
    if (!config.value?.bindAwake) config.value.bindAwake = 50
    if (!config.value?.options) config.value.options = {}

    const part = [...infoStore.parts, '宠物', '副武器'].filter(
      (a) => !config.value?.equips.hasOwnProperty(a),
    )
    const avatarPart = infoStore.avatarParts
      .filter((a) => a != '宠物')
      .filter((a) => !config.value?.avatar.hasOwnProperty(a))

    const skillIDs = infoStore.skills
      .map((skill) => skill.id.toString())
      .filter((a) => !config.value?.skills.hasOwnProperty(a))

    part.forEach((p) => {
      config.value && (config.value.equips[p] = { ...defaultEqusConfig })
    })

    avatarPart.forEach((p) => {
      config.value && (config.value.avatar[p] = { ...defaultAvatarConfig })
    })

    infoStore.options.forEach((option) => {
      if(Object.keys(config.value.options).includes(option.id.toString())) return
      config.value.options[option.id.toString()] = 0
    })

    skillIDs.forEach((id) => {
      config.value &&
        (config.value.skills[id] = {
          lv: infoStore.skills.find((skill) => skill.id.toString() === id)?.maxLearnLv ?? 0,
          vp: 0,
          up: 0,
        })
    })
    ;(
      ['0', '1', '2', '3'].filter((key) => !Object.keys(config.value.jades).includes(key)) ?? []
    ).forEach((key) => {
      config.value.jades[key] = {
        id: -1,
        value: 0,
      }
    })
  }

  const saveConfig = () => {
    const infoStore = useInfoStore()
    const alter = infoStore.infos?.alter
    if (alter) {
      localStorage.setItem(`dcalc/${alter}/config`, JSON.stringify(config.value))
      localStorage.setItem(
        `dcalc/${alter}/config/skillCount`,
        JSON.stringify(skillCountConfig.value),
      )
    }
  }

  const calc = async () => {
    if (!useInfoStore().infos?.alter) return undefined
    return await api.calc(config.value)
  }

  const chooseEqu = async (
    equip: IEquipment | undefined,
    isFusion: boolean = false,
    isSubWeapon: boolean = false,
  ) => {
    if (!equip) return
    const part = isSubWeapon ? '副武器' : equip?.itemType == '武器' ? '武器' : equip?.itemDetailType
    if (equip && config.value.equips[part]) {
      const key = isFusion ? 'fusion' : 'id'
      if (config.value.equips[part][key] == equip.id) {
        config.value.equips[part][key] = ''
      } else {
        config.value.equips[part][key] = equip.id
      }
    }
  }

  const result = useAsyncState(
    () => {
      return calc()
    },
    {
      uuid: '',
      skills: [],
      info: [],
      suits: [],
      buffer: false,
    },
    { resetOnExecute: false },
  )

  return {
    config,
    loadConfig,
    saveConfig,
    calc,
    result,
    chooseEqu,
    skillCountConfig,
  }
})
