import api from "@/api"
import type { ICharacterInfo } from "@/api/info/type"
import { defineStore } from "pinia"

export const useInfoStore = defineStore("infoStore", ()=>{

  const token = ref<string>("")
  const infos = ref<ICharacterInfo | null>(null)

  const skills = computed(()=>infos.value?.skills ?? [])

  const equips = computed(()=>infos.value?.equips ?? [])

  const suits = computed(()=>infos.value?.suits ?? [])

  const createCharacter = async (alter: string, equVersion?: string) => {
    token.value = await api.createToken(alter, equVersion)
    infos.value = await api.characterInfo()
  }

  return {
    token,
    infos,
    skills,
    equips,
    suits,
    createCharacter,
  }
})
