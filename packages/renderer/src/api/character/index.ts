import { defineRequest } from "../common"
import type { IAnyResultInfo, ICharacterInfo, IRankList } from "./type"

export default defineRequest(request => {
  return {
    getCharacter() {
      return request.get<ICharacterInfo>("/character").then(r => r.data)
    },
    calc(params: any, single: boolean = false) {
      return request.post<IAnyResultInfo>(single ? "/calc/single" : "/calc", params).then(r => r.data)
    },
    calc_m(params: any) {
      return request.post<IAnyResultInfo>("/calc/mobile", params).then(r => r.data)
    },
    getResult(id: string) {
      return request.get<IAnyResultInfo>(`/calc/result/${id}`).then(r => r.data)
    },
    getRank(id: string) {
      return request.get<IRankList>(`/calc/rank/${id}`).then(r => r.data)
    },
    getRankResult(params: any) {
      return request.post<string>("/calc/rankresult", params).then(r => r.data)
    },
    checkUID(uid?: number,r=0) {
      return request.get<{show:boolean,uid:number,reason:string,userName?:string}>(`/uid/check/${uid}?r=${r}`).then(r => r.data)
    }
  }
})
