import type { IConfig } from '@/stores'
import { defineRequest } from '../common'
import type { IResult } from './type'
export default defineRequest((request) => {
  return {
    async calc(config: IConfig) {
      const res = await request.post<IResult>('/calc', config)
      return res.data
    },
  }
})
// Compare this snippet from frontend/src/api/common/index.ts:
