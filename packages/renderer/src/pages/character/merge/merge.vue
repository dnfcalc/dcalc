<script lang="tsx">
import { computed, defineComponent, reactive, ref, renderList } from "vue"
import List from "./list.vue"
import EquipIcon from "@/components/internal/equip/eq-icon.vue"
import { useBasicInfoStore, useConfigStore } from "@/store"
import { rarityClass } from "@/utils"
import EquipFusion from "@/components/internal/equip/equip-fusion.vue"

export interface IMergeUpgrade {
  id: string
  damage: number
  percent: string
  color: string
}

export default defineComponent({
  async setup() {
    const basicStore = useBasicInfoStore()
    const configStore = useConfigStore()
    const fusion = computed(() => basicStore.equipment_info?.fusion ?? [])

    const selected_fusion = computed<ID[]>({
      get(): ID[] {
        return configStore.fusion_list
      },
      set(val: ID[]) {
        configStore.fusion_list = val
      }
    })

    const equips = computed(() => {
      const list = basicStore.equipment_list.filter(item => item.part == "武器" && Number.parseInt(item.id?.toString() ?? "0") < 100000 && item.lv != 110) ?? [] ?? []
      return list
    })

    const pagination = reactive({
      page: 1,
      pageSize: 15
    })

    const show_list = computed(() => {
      const start = (pagination.page - 1) * pagination.pageSize
      const end = start + pagination.pageSize
      return equips.value.slice(start, end)
    })

    const selectEquip = ref<ID>()

    const total = computed(() => equips.value.length)
    const total_page = computed(() => Math.ceil(total.value / pagination.pageSize))

    return () => (
      <div class="flex">
        <div class="flex flex-col ml-5px w-260px">
          {(fusion.value.filter(i => i.type == "融合-雾神") ?? []).length > 0 && (
            <EquipFusion
              colNumber={5}
              class="equ-fusion-sort"
              v-model:selected={selected_fusion.value}
              list={(fusion.value.filter(i => i.type == "融合-雾神") ?? [])}
              title="雾神"
            />
          )}
          {(fusion.value.filter(i => i.type == "融合-幽暗岛") ?? []).length > 0 && (
            <EquipFusion
              colNumber={6}
              class="equ-fusion-sort !w-245px"
              v-model:selected={selected_fusion.value}
              list={(fusion.value.filter(i => i.type == "融合-幽暗岛") ?? []).sort((a, b) => a.order - b.order)}
              title="幽暗岛"
            />
          )}
          {fusion.value.filter(i => i.type == "融合-伊斯大陆").length > 0 && (
            <EquipFusion class="equ-fusion-sort" v-model:selected={selected_fusion.value} list={fusion.value.filter(i => i.type == "融合-伊斯大陆")} title="伊斯大陆" />
          )}
          {fusion.value.filter(i => i.type == "融合-机械革命").length > 0 && (
            <EquipFusion class="equ-fusion-sort" v-model:selected={selected_fusion.value} list={fusion.value.filter(i => i.type == "融合-机械革命")} title="机械革命：开战" />
          )}
          {fusion.value.filter(i => i.type == "融合-次元回廊").length > 0 && (
            <EquipFusion class="equ-fusion-sort" v-model:selected={selected_fusion.value} list={fusion.value.filter(i => i.type == "融合-次元回廊")} title="大魔法师的次元回廊" />
          )}
        </div>
        <div class="flex flex-col h-full mt-5px w-870px">
          <calc-button>武器融合</calc-button>
          <div class="flex h-650px pt-5px">
            <div class="h-full bg-hex-0d0d0d mx-2px w-30%">
              <calc-selection v-model={selectEquip.value} active-class="equip-line-selected" class="h-[calc(100%-2.5rem)]">
                {renderList(show_list.value, item => {
                  return (
                    <calc-item value={item.id} class="flex h-9 mb-2px px-1 justify-between items-center equip-line relative box-border">
                      <div class="h-full w-full top-0 left-0 absolute mask"></div>
                      <EquipIcon eq={item}></EquipIcon>
                      <span class={["text-xs", "ml-4", rarityClass(item.rarity ?? "")]}>{item.name}</span>
                      <span class={["h-4 w-6"]}></span>
                    </calc-item>
                  )
                })}
                {renderList(pagination.pageSize - show_list.value.length, () => (
                  <div class="flex h-9 mb-2px px-1 justify-between items-center equip-line relative box-border"></div>
                ))}
              </calc-selection>
              <calc-pagination v-model:page={pagination.page} total-page={total_page.value} v-show={total_page.value > 0}></calc-pagination>
            </div>
            <div class="h-full bg-hex-0d0d0d w-70% s-left" style="overflow-x:auto">
              {selectEquip.value && <List class="py-10px" eid={selectEquip.value.toString()}></List>}
            </div>
          </div>
        </div>
      </div>
    )
  }
})
</script>

<style lang="scss">
  .calc-tags-input {
    .calc-tag {
      text-decoration: underline;
      text-underline-offset: 2px;
      color: #ffb400 !important;

      &:hover {
        color: #fff000 !important;
      }
    }
  }

  .i-checkbox {
    display: flex;
    align-items: flex-start !important;

    .i-checkbox-icon {
      margin-top: 5px !important;
    }

    .i-checkbox-icon-disable {
      margin-top: 5px !important;
    }

    .i-checkbox-label {
      line-height: 22px !important;
    }
  }
</style>

<style lang="scss" scoped>
  .prop-icon {
    content: "";
    display: inline-block;
    width: 12px;
    height: 12px;
    background-image: url(@/assets/img/icon/switch.png);
  }

  .equip-line {
    border: 1px solid transparent;
    background-image: url("@/assets/img/control/dictionary_line.png");
    background-repeat: no-repeat;
    background-size: 100% 100%;

    &:hover {
      .mask {
        background-image: url("@/assets/img/control/hover_mask.png");
        background-repeat: no-repeat;
        background-size: 100% 100%;
      }
    }

    &-selected {
      border: 1px solid #ffb400;
    }
  }
</style>
