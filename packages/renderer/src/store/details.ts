import { defineStore } from "pinia"
import type { IAnyResultInfo } from "./../api/character/type"
import api from "@/api"

interface IDetailStore {
  display_parts: string[]
  standard_uuid: ID
  _standard?: IAnyResultInfo
}

export const useDetailsStore = defineStore("details", {
  state: (): IDetailStore => {
    return {
      display_parts: ["头肩", "上衣", "下装", "腰带", "鞋", "武器", "称号", "手镯", "项链", "辅助装备", "戒指", "耳环", "魔法石", "宠物"],
      standard_uuid: undefined,
      _standard: undefined
    }
  },

  actions: {
    setStandard(uuid: ID) {
      this.standard_uuid = uuid
      this._standard = undefined
    }
  },
  getters: {
    standard(state) {
      if (!state._standard && state.standard_uuid) {
        if (window.pywebview) {
          api.getResult(state.standard_uuid as string).then(res => (state._standard = res))
        } else { state._standard = JSON.parse(sessionStorage.getItem(state.standard_uuid as string) ?? "{}") }
      }
      return state._standard
    }
  }
})
