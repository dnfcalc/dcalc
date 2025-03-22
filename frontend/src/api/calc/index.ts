import type { IConfig } from '@/stores'
import { defineRequest } from '../common'
export default defineRequest((request) => {
  return {
    async calc(config: IConfig) {
      const res = await request.post('/calc', config)
      return res.data
    }
  }
})
// Compare this snippet from frontend/src/api/common/index.ts:
