import { defineStore } from "pinia"
import { computed } from "vue"
import { asyncComputed, useAsyncState } from "@vueuse/core"
import { useCharacterStore } from "./character"
import api from "@/api"

export const useBasicInfoStore = defineStore("basicInfo", () => {
  const { state: equipment_info, execute: loadEquips } = useAsyncState(api.equips,
    null,
    { immediate: false, resetOnExecute: false }
  )


  const equipment_list = computed(() => {
    const info = equipment_info.value
    return info ? [...(info?.lv110 ?? []), ...(info?.myth ?? []), ...(info?.weapon ?? []), ...(info?.wisdom ?? []), ...(info?.title ?? []), ...(info?.pet ?? [])] : []
  })


  const equipment_ids = computed(() => equipment_list.value.map(item => item.id))

  const { state: trigger_list, execute: loadTriggers } = useAsyncState(api.triggers,
    null,
    { immediate: false, resetOnExecute: false }
  )

  const { state: entry_list, execute: loadEntries } = useAsyncState(api.entries,
    null,
    { immediate: false, resetOnExecute: false }
  )

  const use_count = asyncComputed(async () => await api.useCount(useCharacterStore().alter), null, { lazy: true })

  const details = computed(() => {
    const { platinum, jade, dress, sundries, emblem, enchanting } = useCharacterStore()
    return { jade, sundries, dress, emblem, enchanting, platinum }
  })

  const { state: monster_list, execute: loadMonsters } = useAsyncState(api.monsters,
    null,
    { immediate: false, resetOnExecute: false }
  )

  const { state: scenes_list, execute: loadScenes } = useAsyncState(api.scenes,
    null,
    { immediate: false, resetOnExecute: false }
  )

  const get_equipment_detail = async (equ_id: ID, sj: boolean, carry: boolean, fusion_upgrade: boolean) => (await api.equipmentDetail(equ_id, sj, carry, fusion_upgrade))?.data

  const getEquip = (id?: ID) => {
    if (id) {
      return equipment_list.value.find(e => e.id == id)
    }
  }

  const load = () => {
    return Promise.all([
      loadEquips(),
      loadTriggers(),
      loadEntries(),
      loadMonsters(),
      loadScenes()
    ])
  }

  return {
    loadEquips,
    loadEntries,
    equipment_info,
    equipment_list,
    equipment_ids,
    trigger_list,
    entry_list,
    details,
    monster_list,
    scenes_list,
    get_equipment_detail,
    getEquip,
    load,
    use_count
  }
})
