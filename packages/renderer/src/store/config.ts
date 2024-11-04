import { defineStore } from "pinia"
import { useAppStore, useBasicInfoStore, useCharacterStore, useDetailsStore } from "."
import api from "@/api"
import type { IResultInfo, ISkillInfo } from "@/api/character/type"
import type { ICharacterSet, IRecommendEquip, IRecommendInfo, IRecommendRequest } from "@/api/info/type"
import { getUuid, toMap, toObj } from "@/utils"
import { isLocalMode } from "@/utils/env"
import { safeParse } from "@/utils/json"
import app from "@/api/app"

interface ConfigState extends ICharacterSet {
  name: string
  alter: string
  token: string
  uid: number
  _configlist: string[] | undefined
}

function getLocalFavorites(alter: string, pagination: IRecommendRequest): PagingData<IRecommendInfo> {
  const favorites = safeParse(localStorage.getItem(`dcalc/${alter}/favorites`), []) as IRecommendInfo[]
  const totalCount = favorites.length
  const data = favorites.slice((pagination.page - 1) * pagination.size, pagination.page * pagination.size)
  return { totalCount, data, pageIndex: pagination.page, pageSize: pagination.size }
}

function addLocalFavorites(alter: string, favorite: Omit<IRecommendInfo, "id">) {
  const favorites = safeParse(localStorage.getItem(`dcalc/${alter}/favorites`), [])
  favorites.push({
    ...favorite,
    id: getUuid()
  })
  localStorage.setItem(`dcalc/${alter}/favorites`, JSON.stringify(favorites))
}

function deleteLocalFavorites(alter: string, id: ID) {
  const favorites = safeParse(localStorage.getItem(`dcalc/${alter}/favorites`), [])
  const index = favorites.findIndex((item: IRecommendInfo) => item.id == id)
  if (index > -1) {
    favorites.splice(index, 1)
    localStorage.setItem(`dcalc/${alter}/favorites`, JSON.stringify(favorites))
  }
}

export const useConfigStore = defineStore("config", {
  state: (): ConfigState => {
    return {
      name: "",
      alter: "",
      carry_type: "",
      attack_attribute: 0,
      skill_set: [],
      forge_set: {},
      dress_set: {},
      single_set: [],
      comparison: [],
      equip_list: [],
      fusion_list: [],
      wisdom_list: [],
      myths_list: [],
      lv110_list: [],
      consumable_list: [],
      weapons_list: [],
      trigger_set: {},
      skill_que: [],
      title_list: [],
      pet_list: [],
      stone_set:{},
      token: "",
      uid: -1,
      _configlist: undefined,
      customize: {},
      merge: {},
      rune_set: [],
      talisman_set: [],
      buff_ratio: 0,
      hotkey_set: [],
      monster: 2,
      scene: 1,
      individuation: [],
      specificity_list: [],
      specificity: {},
      corrections: {
        四维: 0,
        三攻: 0,
        技攻: 0,
        攻击强化: 0,
        BUFF量: 0,
        攻击强化百分比: 0,
        BUFF量百分比: 0,
        攻速: 0,
        火强: 0,
        光强: 0,
        冰强: 0,
        暗强: 0,
        火抗: 0,
        冰抗: 0,
        暗抗: 0,
        光抗: 0
      },
      asrahan: {
        lv: 0,
        type: -1,
        additional: 0
      }
    }
  },
  getters: {
    config_list(state) {
      if (!state._configlist) {
        api.getConfigList().then(res => (state._configlist = res))
      }
      state._configlist?.push("新建存档")
      return state._configlist
    },
    equ_sort(state) {
      const temp: number[][] = []
      const equs = useBasicInfoStore().equipment_list
      const parts = ["称号", "宠物", "武器", "上衣", "头肩", "下装", "腰带", "鞋", "手镯", "项链", "戒指", "辅助装备", "魔法石", "耳环"]
      const lists = [...state.wisdom_list, ...state.myths_list, ...state.lv110_list, ...this.weapons_list, ...this.pet_list, ...this.title_list]
      parts.forEach(part => {
        temp.push(equs.filter(a => a.part == part && lists.includes(a.id as number)).map(a => a.id as number) ?? [])
      })
      return temp
    },
    data(state) {
      return {
        comparison: state.comparison,
        single_set: state.single_set,
        equip_list: (this as any).equ_sort,
        fusion_list: state.fusion_list,
        stone_set:state.stone_set,
        carry_type: state.carry_type,
        attack_attribute: state.attack_attribute,
        skill_set: state.skill_set,
        forge_set: state.forge_set,
        dress_set: state.dress_set,
        trigger_set: state.trigger_set,
        skill_que: state.skill_que.map((r, id) => {
          return {
            ...r,
            id
          }
        }),
        wisdom_list: state.wisdom_list,
        myths_list: state.myths_list,
        title_list: state.title_list,
        pet_list: state.pet_list,
        weapons_list: state.weapons_list,
        lv110_list: state.lv110_list,
        consumable_list: state.consumable_list,
        customize: state.customize,
        rune_set: state.rune_set,
        talisman_set: state.talisman_set,
        buff_ratio: Number(state.buff_ratio),
        hotkey_set: state.hotkey_set,
        monster: state.monster,
        scene: state.scene,
        individuation: state.individuation,
        corrections: state.corrections,
        merge: state.merge,
        specificity_list: state.specificity_list,
        specificity: state.specificity,
        asrahan: state.asrahan
      }
    }
  },
  actions: {
    async load() {
      if (isLocalMode()) {
        const alter = this.alter.split(".").pop() ?? ""
        let data = JSON.parse(localStorage.getItem(`dcalc/${alter}/sets`) ?? "{}")
        if (Object.keys(data).length == 0 || !data?.single_set || (data?.single_set ?? [])?.length == 0 || !data.buff_ratio) {
          data = await api.defaultConfig(alter).then(res => {
            const sets = toMap(res, ["trigger_set", "customize", "buff_ratio", "dress_set", "corrections", "merge", "specificity", "asrahan","stone_set"]) as ICharacterSet
            this.$patch(sets)
            return res
          })
        }
        return await api.checkConfig(data).then(res => {
          const temp = toMap(res, ["trigger_set", "customize", "buff_ratio", "dress_set", "corrections", "merge", "specificity", "asrahan","stone_set"]) as ICharacterSet
          // data.dress_set = Object.entries(data.dress_set)
          this.$patch(temp)
          return temp
        })
      }

      return await api.getConfig("set").then(res => {
        const data = toMap(res, ["trigger_set", "customize", "buff_ratio", "dress_set", "corrections", "merge", "specificity", "asrahan","stone_set"]) as ICharacterSet
        this.$patch(data)
        return data
      })
    },
    async switch(name: string) {
      await this.save()
      this.name = name
      await api.switchConfig(this.name)
    },
    async save() {
      const data = toObj((this as any).data) as ConfigState
      if (window.pywebview) {
        if ((data.skill_que.length > 0 && data.buff_ratio > 0) || (useCharacterStore().is_buffer && data.single_set && data.single_set.length > 0)) {
          await api.saveConfig({ setName: "set", setInfo: data })
        }
      } else {
        if ((data.skill_que.length > 0 && data.buff_ratio > 0) || (useCharacterStore().is_buffer && data.single_set && data.single_set.length > 0)) {
          const alter = this.alter.split(".")
          localStorage.setItem(`dcalc/${alter.at(-1)}/sets`, JSON.stringify(data))
        }
      }
    },
    async set(name: string, item: Record<string, any>) {
      (this as any)[name] = item
    },
    async calc(
      single: boolean = false,
      _withJade: boolean = false,
      CalCusID: number = 0,
      CalMergeID: number = 0,
      ComparisonList: Record<string, ID[]> = {},
      AnalysisID: number = 0
    ): Promise<IResultInfo> {
      const limit = window.pywebview ? 1 : 12
      if (single && (this as any).data.single_set.length < limit) {
        return {
          id: undefined,
          role: "delear",
          equips: [],
          name: "",
          alter: "",
          skills: {},
          total_data: [],
          info: undefined,
          skills_passive: undefined,
          jade: undefined,
          equips_forge: {},
          customize: {},
          merge: {},
          fusion_list: [],
          merge_list: {},
          specificity: {}
        }
      }

      const res = await api.calc(
        {
          setInfo: toObj((this as any).data),
          setName: this.name,
          // withCus: withCus,
          withJade: false,
          // withMerge: withMerge,
          CalCusID: !this.single_set.includes(CalCusID) ? 0 : CalCusID,
          CalMergeID: !this.single_set.includes(CalMergeID) ? 0 : CalMergeID,
          ComparisonList,
          AnalysisID
        },
        single
      )
      const detailsStore = useDetailsStore()
      const appStore = useAppStore()
      if(! (appStore.userInfo?.show ?? false) && process.env.NODE_ENV != "development" && import.meta.env.MODE != "show" && res.role=="delear" && !detailsStore.standard_uuid && res.total_data[0] > 0){
          sessionStorage.setItem(res.id?.toString() ?? "", JSON.stringify(res))
          detailsStore.setStandard(res.id)
      }

      return res
    },
    async calc_mobile(): Promise<IResultInfo> {
      return await api.calc_m({
        single_set: this.single_set,
        merge: this.merge,
        fusion_list: this.fusion_list,
        customize: this.customize,
        specificity_list: this.specificity_list,
        specificity: this.specificity
      })
    },
    getSkill(skill: string) {
      return this.skill_set.find(item => item.name == skill)
    },
    setForge(part: string, key: string, value: any) {
      if (!this.forge_set[part]) {
        this.forge_set[part] = new Map<string, any>()
      }
      const map = this.forge_set[part]
      map.set(key, value)
    },
    getForge(part: string, key: string) {
      if (this.forge_set[part]) {
        const map = this.forge_set[part]
        return map.get(key)
      }
    },
    setDress(part: string, id: number, option: string) {
      this.dress_set[part] = { id, option }
    },
    getDress(part: string) {
      return this.dress_set[part]
    },

    addSingle(id: ID, toggle = false) {
      const basicStore = useBasicInfoStore()
      const newEquip = basicStore.getEquip(id)
      if (!newEquip) {
        return
      }
      if (toggle) {
        const index = this.single_set.indexOf(id)
        if (index > -1) {
          this.single_set.splice(index, 1)
          return
        }
      }
      this.single_set.push(id)
      this.trimSingle()
    },

    importSingle(ids: ID[]) {
      const basicStore = useBasicInfoStore()
      ids = ids.filter(id => basicStore.equipment_ids.includes(id))
      if (ids.length == 0) {
        return
      }
      this.single_set.push(...ids)
      this.trimSingle()
    },

    trimSingle() {
      const basicStore = useBasicInfoStore()
      const map = new Map<string, ID>()
      for (const id of this.single_set) {
        const equip = basicStore.getEquip(id)
        if (equip) {
          map.set(equip.part, id)
        }
      }
      this.single_set = [...map.values()].sort((a, b) => Number(a) - Number(b))
    },
    addSkillQueue(skill: ISkillInfo) {
      this.skill_que.push({ name: skill.name, mode: skill.mode?.[0] ?? "", modes: skill.mode })
    },
    async getFavorites(params: IRecommendRequest) {
      if (isLocalMode()) {
        const alter = this.alter.split(".").pop() ?? ""
        return getLocalFavorites(alter, params)
      }
      return await api.favorites(params)
    },
    async deleteFavorite(id: ID) {
      if (isLocalMode()) {
        const alter = this.alter.split(".").pop() ?? ""
        deleteLocalFavorites(alter, id)
      } else {
        await api.deleteFavorites(id)
      }
    },
    async getCombinations(alter: string) {
      return await api.combinations(alter)
    },
    async addFavorite(name: string) {
      const favorite: Omit<IRecommendInfo, "id"> = { name, equips: [], fusion: [] }
      this.single_set.forEach(item => {
        item = item ?? ""
        const temp: IRecommendEquip = { id: item }
        temp.merge = this.merge[item.toString()] ?? []
        temp.props = this.customize[item.toString()] ?? []
        favorite.equips.push(temp)
      })
      favorite.fusion = this.fusion_list
      favorite.specificity = this.specificity
      if (isLocalMode()) {
        const alter = this.alter.split(".").pop() ?? ""
        addLocalFavorites(alter, favorite)
      } else {
        await api.addFavorites(favorite)
      }
    },
    async getAllConfig() {
      if (window.pywebview) {
        return await api.getAllConfig()
      } else {
        const res = {}
        for (let i = 0; i < localStorage.length; i++) {
          const key = localStorage.key(i)
          if (key && key.includes("dcalc") && !key.includes("global")) {
            (res as any)[key] = JSON.parse(localStorage.getItem(key) ?? "{}")
          }
        }
        return res
      }
    }
  }
})
