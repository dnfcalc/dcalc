import { defineRequest } from "../common"

export default defineRequest(req => {
  return {
    getConfig(name: string) {
      return req.get<Record<string, any>>(`/config/get/${name}`).then(r => r.data)
    },
    getConfigList() {
      return req.get<string[]>("/config/list").then(r => r.data)
    },
    switchConfig(name: string) {
      return req.post("/config/switch", name).then(r => r.data)
    },
    saveConfig(params: any) {
      return req.post("/config/save", params).then(r => r.data)
    },
    checkConfig(setInfo: any) {
      return req.post("/config/check", setInfo).then(r => r.data)
    },
    defaultConfig(alter: string) {
      return req.get<Record<string, any>>(`/config/default/${alter}`).then(r => r.data)
    },
    getToken(alter: string, version?: string, equVersion?: string) {
      return req.get<string>(`/token/get/${alter}`, { params: { version, equVersion } }).then(r => r.data)
    },
    clearToken() {
      return req.post("/token/clear")
    },
    getGlobalDetail(detail?: [number, number[]]) {
      return req.post<(number | number[])[]>("global/detail", detail).then(r => r.data)
    },
    getGlobalInfo() {
      return req.get<{ id: number; items: { value: number; label: string }[]; multi: boolean; name: string; remark: string }[]>("/global/info").then(r => r.data)
    },
    saveGlobalSet(info: [number, number[]]) {
      return req.post<string>("/global/save", info).then(r => r.data)
    },
    getAllConfig() {
      return req.get<Record<string, any>>("/config/all").then(r => r.data)
    },
    shareConfigs(configs: any, expire: number) {
      return req.post<string>("/config/share", { configs, expire }).then(r => r.data)
    },
    getShareConfigs(link: string) {
      return req.get<Record<string, any>>(`/share/${link}`).then(r => r.data)
    },
    importConfigs(configs: Record<string, any>) {
      return req.post<number>("/config/import", configs).then(r => r.data)
    },
    importLocalConfigs() {
      return req.post<number>("/config/import/local").then(r => r.data)
    }
  }
})
