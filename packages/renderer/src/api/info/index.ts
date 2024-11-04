import { defineRequest } from "../common"
import type { IAdventureInfo, IDetailsInfo, IEquipmentList, IMonster, IRank, IRankadventure, IRecommendInfo, IRecommendRequest, ISkillInfo, ITools, ITrigger } from "./type"

export default defineRequest(request => {
  return {
    rankList(alter: string, pageNum: number, tags: string[]) {
      return request.get<IRank[][]>(`/rank/${alter}?pageNum=${pageNum}&tags=${tags.join(",")}`)
    },
    skillInfoList(alter: string) {
      return request.get<ISkillInfo[]>(`/skills/${alter}`).then(r => r.data)
    },
    useCount(alter: string) {
      return request.get<Record<string, { count: number; id: string }>>(`/usecount/${alter}`).then(r => r.data)
    },
    rankAdventure() {
      return request.get<IRankadventure[]>("/adventure/rank")
    },
    adventures() {
      return request.get<IAdventureInfo[]>("/adventure")
    },
    answers() {
      return request.get<[]>("/answers")
    },
    tools() {
      return request.get<ITools[]>("/tools")
    },
    monsters() {
      return request.get<IMonster[]>("/monster").then(r => r.data)
    },
    scenes() {
      return request.get<IMonster[]>("/scene").then(r => r.data)
    },
    equips() {
      return request.get<IEquipmentList>("/equip/list").then(r => r.data)
    },
    equipmentDetail(equipId: ID, sj: boolean, carry: boolean, fusion_upgrade: boolean) {
      return request.get<any>(`/equip/${String(equipId)}?sj=${sj}&carry=${carry}&fusion_upgrade=${fusion_upgrade}`)
    },
    triggers() {
      return request.get<ITrigger[]>("/triggers").then(r => r.data)
    },
    entries() {
      return request.post<Record<string, { attack: number; buff: number; props: string[]; type: number; order?: number; filter?: string; abbr?: string }>>("/entries").then(r => r.data)
    },
    recommends(params: IRecommendRequest, source: string = "skycity") {
      if (source == "colg") {
        return request.get<PagingData<IRecommendInfo>>("/colg/recommend", { params }).then(r => r as unknown as PagingData<IRecommendInfo>)
      }
      return request.get<PagingData<IRecommendInfo>>("/skycity/recommend", { params }).then(r => r as unknown as PagingData<IRecommendInfo>)
    },
    detailList() {
      return request.get<IDetailsInfo>("/details")
    },
    favorites(params: IRecommendRequest) {
      return request.get<PagingData<IRecommendInfo>>("/favorites/list", { params }).then(r => r as unknown as PagingData<IRecommendInfo>)
    },
    combinations(alter: string) {
      return request.get<IRecommendInfo[]>(`/combinations/${alter}`).then(r => r.data as unknown as IRecommendInfo[])
    },
    addFavorites(favorite: Omit<IRecommendInfo, "id">) {
      return request.post("/favorites/add", favorite)
    },
    deleteFavorites(id: ID) {
      return request.post(`/favorites/delete/${id}`, {})
    }
  }
})
