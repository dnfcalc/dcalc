import { defineStore } from "pinia"
import { asyncComputed, useAsyncState } from "@vueuse/core"
import { computed } from "vue"
import api from "@/api"

export const useGlobalStore = defineStore("global", () => {
  const global_set_info = asyncComputed(async () => {
    const temp = api.getGlobalInfo()
    return temp
  })

  const global_info = useAsyncState(async () => {
    let cur_details = JSON.parse(localStorage.getItem("dcalc/global") ?? "[]")

    if (window.pywebview) {
      cur_details = []
    }
    const temp = await api.getGlobalDetail(cur_details.length == 0 ? undefined : cur_details)
    localStorage.setItem("dcalc/global", JSON.stringify(temp))
    return temp
  }, [])

  const { state: global_set_details, isReady, execute } = global_info

  const equVersion = computed(() => global_set_details.value[1] == global_set_info.value[1].items[0].value)

  return {
    global_set_info,
    global_set_details,
    isReady,
    execute,
    equVersion
  }
})
