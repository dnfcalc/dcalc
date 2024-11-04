import { defineStore } from "pinia"
import { useBasicInfoStore } from "./basicInfo"
import { useAppStore } from "./app"
import { useGlobalStore } from "./global"
import api from "@/api"
import type { ICharacterInfo } from "@/api/character/type"
import { useConfigStore } from "@/store/config"

export interface CharacterInfo extends ICharacterInfo {
  // 基础信息
  calc_token: string
  alter_detail: string
  equ_version: string
}

export const useCharacterStore = defineStore("CharacterInfo", {
  state(): CharacterInfo {
    return {
      specificity: [],
      especificity: [],
      asrahan: [],
      alter: "",
      name: "",
      skills: [],
      individuation: [],
      character: "",
      role: "delear",
      weapon_types: [],
      carry_type_list: [],
      armor: "",
      armor_mastery: [],
      buff_ratio: 0,
      rune: [],
      platinum: [],
      config: "set",
      clothes_coat: [],
      clothes_pants: [],
      talisman: [],
      calc_token: "",
      version: "",
      enchanting: [],
      emblem: [],
      dress: {},
      jade: [],
      sundries: [],
      char_optiopns: [],
      alter_detail: "",
      equ_version: ""
    }
  },
  getters: {
    is_buffer(state) {
      return state.role === "buffer"
    },
    is_delear(state) {
      return state.role !== "buffer"
    }
  },
  actions: {
    async newCharacter(alter: string, version?: string, equVersion?: string) {
      const configStore = useConfigStore()
      const info = useBasicInfoStore()
      const token = await api.getToken(alter, version, equVersion)
      configStore.$patch({ token })

      configStore.$patch({ alter, name: "set" })

      Promise.all([api.getCharacter(), info.load(), configStore.load()]).then(res => {
        this.$patch(res[0])
      })

      useAppStore().userInfo;

      this.alter_detail = alter
    },
    async reload() {
      const configStore = useConfigStore()
      const globalStore = useGlobalStore()
      configStore.save()
      globalStore.global_set_details = await globalStore.execute()
      await this.newCharacter(this.alter_detail, "", globalStore.global_set_details[1].toString())
    },
    calc() {
      this.calc_token = new Date().getTime().toString()
    },
    async load() {
      const state = await api.getCharacter()
      this.$patch(state)
    }
  }
})
