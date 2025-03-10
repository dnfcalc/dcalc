import { defineRequest } from '../common'
import type { IAdventureInfo } from './type'

export default defineRequest((request) => {
  return {
    adventures() {
      return request.get<IAdventureInfo[]>('/adventure').then((res) => res.data)
    },
  }
})
