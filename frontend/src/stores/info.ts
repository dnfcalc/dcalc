import api from '@/api'
import type { ICharacterInfo } from '@/api/info/type'
import { defineStore } from 'pinia'
import { useConfigStore } from './config'
import type { IResult, IResultSkill, IResultSkillCount } from '@/api/calc/type'

export const useInfoStore = defineStore('infoStore', () => {
  const alter_token = ref<string>('')
  const infos = ref<ICharacterInfo | null>(null)

  const skills = computed(() => infos.value?.skills ?? [])

  const equips = computed(() => infos.value?.equips ?? [])

  const suits = computed(() => infos.value?.suits ?? [])

  const enchants = computed(() => infos.value?.enchants ?? [])

  const emblems = computed(() => infos.value?.emblems ?? [])

  const stones = computed(() => infos.value?.stones ?? [])

  const avatars = computed(() => infos.value?.avatar ?? {})

  const jades = computed(() => infos.value?.jades ?? [])

  const sundries = computed(() => infos.value?.sundry ?? {})

  const standardUUID = ref<string>()

  const setStandard = (result?: IResult,skillCount?:{
    count: number;
    mode: string;
    name: string;
}[]) => {
    if (!result) {
      !!standardUUID.value && sessionStorage.removeItem(standardUUID.value)
      standardUUID.value = undefined
    } else {
      standardUUID.value = result.uuid
      sessionStorage.setItem(result.uuid, JSON.stringify({skills:result.skills,skillCount}))
    }
  }

  const standard = computed(()=>{
    const value = sessionStorage.getItem(standardUUID.value ?? '')
    if(!value) return undefined
    else return JSON.parse(value) as {skills:IResultSkill[],skillCount:IResultSkillCount[]}
  })

  const parts = [
    '头肩',
    '上衣',
    '下装',
    '腰带',
    '鞋',
    '武器',
    '称号',
    '手镯',
    '项链',
    '辅助装备',
    '戒指',
    '耳环',
    '魔法石',
    '宠物',
  ]

  const avatarParts = [
    '武器装扮',
    '头发',
    '帽子',
    '脸部',
    '光环',
    '胸部',
    '上衣',
    '皮肤',
    '快捷栏装备',
    '腰带',
    '下装',
    '鞋',
    '宠物',
    '宠物装备-红',
    '宠物装备-绿',
    '宠物装备-蓝',
  ]

  const createCharacter = async (alter: string, equVersion?: string) => {
    const time = new Date().getTime()
    alter_token.value = btoa(JSON.stringify({ alter, equVersion, time }))
    infos.value = await api.characterInfo()
    useConfigStore().loadConfig()
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
    parts,
    stones,
    avatarParts,
    avatars,
    jades,
    setStandard,
    standard,
    sundries
  }
})
