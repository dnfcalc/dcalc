import api from '@/api'
import type { ICharacterInfo } from '@/api/info/type'
import { defineStore } from 'pinia'

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
    '魔法石'
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
    '腰带',
    '下装',
    '鞋',
    '宠物',
    '宠物装备-红',
    '宠物装备-绿',
    '宠物装备-蓝'
  ]

  const createCharacter = async (alter: string, equVersion?: string) => {
    const time = new Date().getTime()
    alter_token.value = btoa(JSON.stringify({ alter, equVersion, time }))
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
    parts,
    stones,
    avatarParts,
    avatars,
  }
})
