import { defineStore } from 'pinia'
import { useInfoStore } from './info'
import api from '@/api'
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
  equips: Record<string,
    { id: string,
      reinforce: number,
      reinforceType: number,
      enchat: number,
      emblems: string[],
      upgrade: number,
      refine: number,
      adaptation:number
     }
  >
}

const defaultEqusConfig = {
  id: '',
  reinforce: 0,
  reinforceType: 0,
  enchat: 0,
  emblems: [],
  upgrade: 0,
  refine: 0,
  adaptation: 0
}

export const useConfigStore = defineStore('configStore', () => {
  const config = ref<IConfig>({
    skills: {},
    equips: {}
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
    if(!config.value) config.value = {
      skills: {},
      equips: {}
    }
    if(!config.value?.equips) config.value.equips = {}
    if(!config.value?.skills) config.value.skills = {}

    const part = infoStore.parts.filter(a => !config.value?.equips.hasOwnProperty(a))

    const skillIDs = infoStore.skills.map(skill => skill.id.toString()).filter(a => !config.value?.skills.hasOwnProperty(a))

    part.forEach(p => {
      config.value && (config.value.equips[p] = { ...defaultEqusConfig })
    });

    skillIDs.forEach(id => {
      config.value && (config.value.skills[id] = { lv: infoStore.skills.find(skill => skill.id.toString() === id)?.maxLearnLv ?? 0 })
    });
  }

  const saveConfig = () => {
    const infoStore = useInfoStore()
    const alter = infoStore.infos?.alter
    if (alter) {
      localStorage.setItem(`dcalc/${alter}/config`, JSON.stringify(config.value))
    }
  }

  const calc = async()=>{
    await api.calc(config.value)
  }

  return {
    config,
    loadConfig,
    saveConfig,
    calc
  }
})
