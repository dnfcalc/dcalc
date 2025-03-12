import { defineRequest } from '../common'
import type { IAdventureInfo, ICharacterInfo } from './type'

export default defineRequest((request) => {
  return {
    async adventures() {
      const res = await request.get<IAdventureInfo[]>('/adventure')
      return res.data
    },
    async createToken(alter: string, equVersion?: string) {
      const res = await request.get<string>(`/token/get/${alter}`, { params: { equVersion } })
      return res.data
    },
    async characterInfo() {
      const res = await request.get<ICharacterInfo>('/character')
      return res.data
    },
  }
})
