<script lang="tsx">
import { computed, defineComponent, ref, renderList } from "vue"
import Trigger from "./trigger.vue"
import { useBasicInfoStore, useConfigStore } from "@/store"
import featureList from "@/utils/featureList"

import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"
// import EquipFusion from "@/components/internal/equip/equip-fusion.vue"
import EquipList from "@/components/internal/equip/equip-list.vue"
export default defineComponent({
  components: { EquipTips, EquipList },
  async setup() {
    const basicStore = useBasicInfoStore()
    const choose_feature = ref(0)

    const equips = computed(() => basicStore.equipment_info?.lv110.filter(a => Number.parseInt(a.id?.toString() ?? "0") < 100000) ?? [])

    const highlight = computed<ID[]>({
      get() {
        return equips.value.map(e => (e.features?.includes(choose_feature.value) ? e.id : 0)).filter(e => ((e as number) ?? 0) > 0)
      },
      set(val) {
        if (val.length === 0) {
          choose_feature.value = 0
        }
      }
    })


    const configStore = useConfigStore()


    const weapons = computed(() => basicStore.equipment_info?.weapon.filter(item => Number.parseInt(item.id?.toString() ?? "0") < 100000) ?? [])

    const pets = computed(() => Array.from(basicStore.equipment_info?.pet ?? []).sort((a, b) => Number(b.type) - Number(a.type)) ?? [])
    const titles = computed(() => Array.from(basicStore.equipment_info?.title ?? []).sort((a, b) => Number(b.type) - Number(a.type)) ?? [])
    const consumable = computed(() => basicStore.equipment_info?.consumable ?? [])
    // const fusion = computed(() => basicStore.equipment_info?.fusion ?? [])

    const selected_110 = computed({
      get() {
        return configStore.lv110_list
      },
      set(val: number[]) {
        configStore.lv110_list = val
      }
    })

    const selected_weapons = computed({
      get() {
        return configStore.weapons_list
      },
      set(val: number[]) {
        configStore.weapons_list = val
      }
    })

    const selected_consumable = computed({
      get() {
        return configStore.consumable_list
      },
      set(val: number[]) {
        configStore.consumable_list = val
      }
    })

    const selected_pet = computed({
      get() {
        return configStore.pet_list
      },
      set(val: number[]) {
        configStore.pet_list = val
      }
    })

    const selected_title = computed({
      get() {
        return configStore.title_list
      },
      set(val: number[]) {
        configStore.title_list = val
      }
    })

    // const selected_fusion = computed({
    //   get() {
    //     return configStore.fusion_list
    //   },
    //   set(val: number[]) {
    //     configStore.fusion_list = val
    //   }
    // })

    // 没有的就补，多的就删

    // watch(triggers, val => {
    //   characterStore.trigger_set = val
    //   console.log(characterStore.trigger_set)
    // })

    // let equi_choose = computed<EquiChooseState[]>(() => {
    //   let list = [] as EquiChooseState[]
    //   basic_info.value?.public_110_equ?.forEach(item => {
    //     if (item.state) {
    //       list.push({ id: item.id, state: false })
    //     }
    //   })
    //   return list
    // })

    return () => (
      <div class="flex">
        <EquipList v-model:selected={selected_110.value} class="equ-105" v-model:highlight={highlight.value} showHighlight={choose_feature.value > 0} list={equips.value} title="Lv110装备">
          {{
            header() {
              return (
                <calc-select v-model:modelValue={choose_feature.value} class="ownSelect" emptyLabel="特性选择">
                  <calc-option value={0}>全部特性</calc-option>
                  {renderList(featureList, item => (
                    <calc-option value={item.value}>{item.label}</calc-option>
                  ))}
                </calc-select>
              )
            }
          }}
        </EquipList>
        <div class="equ-else">
          {/* <EquipList v-model:selected={selected_myths.value} class="equ-else-sort" list={myths.value} title="神话装备" />
            <EquipList v-model:selected={selected_wisdom.value} class="equ-else-sort" list={wisdoms.value} title="智慧产物" /> */}
          <EquipList v-model:selected={selected_weapons.value} class="equ-else-sort" list={weapons.value} title="武器列表" />
          <EquipList class="equ-else-sort" v-model:selected={selected_title.value} list={titles.value} title="称号" />
          <EquipList class="equ-else-sort" v-model:selected={selected_pet.value} list={pets.value} title="宠物" />
          <EquipList class="equ-else-sort" list={consumable.value} v-model:selected={selected_consumable.value} showTips={false} title="药剂" />
        </div>
        <div class="flex flex-col ml-5px w-390px pt-3px">
          <Trigger/>
          {/* <div class="flex w-100%">
              {fusion.value.filter(i => i.type == "融合-伊斯大陆").length > 0 && (
                <EquipFusion class="equ-fusion-sort" v-model:selected={selected_fusion.value} list={fusion.value.filter(i => i.type == "融合-伊斯大陆")} title="伊斯大陆" />
              )}
              {fusion.value.filter(i => i.type == "融合-机械革命").length > 0 && (
                <EquipFusion class="equ-fusion-sort !ml-5px !w-170px" v-model:selected={selected_fusion.value} list={fusion.value.filter(i => i.type == "融合-机械革命")} title="机械革命：开战" />
              )}
            </div> */}
        </div>
      </div>
    )
  }
})
</script>

<style lang="scss">
.equ-105 {
  margin: 5px;
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  width: 420px;
  background-color: rgba(255, 255, 255, 0.1);

  .item {
    width: 30px;
    height: 34px;
    margin-left: 6px;

    &:nth-child(11n + 6),
    &:nth-child(11n + 9) {
      margin-left: 15px;
    }
  }
}

.ownSelect {
  height: calc(100% - 2px) !important;
  width: 200px !important;
  margin-right: 3px;
}

.ownSelect-2 {
  height: 24px !important;
  width: calc(50% - 10px) !important;
  margin: 2px;
}

.equ-else {
  display: flex;
  flex-direction: column;
  width: 260px;
  margin-bottom: 5px;
}

.equ-else-sort {
  margin-top: 5px;

  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  background-color: rgba(255, 255, 255, 0.1);

  .item {
    width: 30px;
    height: 34px;
    margin-left: 6px;
    // &:nth-child(7n + 1) {
    //   margin-left: 0px;
    // }
  }
}

.equ-fusion-sort {
  margin-top: 5px;
  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  width: 100px;

  background-color: rgba(255, 255, 255, 0.1);

  .item {
    width: 30px;
    height: 34px;
    margin-left: 3px;
  }
}

.consumable-sort {
  margin-top: 5px;

  display: flex;
  flex-wrap: wrap;
  align-content: flex-start;
  background-color: rgba(255, 255, 255, 0.1);

  .item {
    width: 30px;
    height: 34px;
    margin-left: 5px;
    // &:nth-child(7n + 1) {
    //   margin-left: 0px;
    // }
  }
}



.imgcover::after {
  content: "";
  width: 28px;
  height: 28px;
  background-color: rgba(50, 50, 50, 0.75);
  z-index: 999;
}
</style>
