import api from "@/api"
import type { ICharacterInfo } from "@/api/info/type"
import { defineStore } from "pinia"

export const useInfoStore = defineStore("infoStore", ()=>{

  const alter_token = ref<string>("")
  const infos = ref<ICharacterInfo | null>(null)

  const skills = computed(()=>infos.value?.skills ?? [])

  const equips = computed(()=>infos.value?.equips ?? [])

  const suits = computed(()=>infos.value?.suits ?? [])

  const enchants = computed(()=>infos.value?.enchants ?? [])

  const emblems = computed(()=>infos.value?.emblems?? [])

  const parts = ['上衣', '头肩', '下装', '腰带', '鞋', '手镯', '项链', '戒指', '耳环', '辅助装备', '魔法石', '武器']

  const createCharacter = async (alter: string, equVersion?: string) => {
    const time = new Date().getTime()
    alter_token.value = btoa(JSON.stringify({alter, equVersion, time}))
    infos.value = await api.characterInfo()
  }

  return {
    alter_token,
    infos,
    skills,
    equips,
    suits,
    createCharacter,
    enchants,
    emblems,
    parts
  }
})
