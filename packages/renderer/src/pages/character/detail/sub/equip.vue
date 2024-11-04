<script lang="tsx">
import { computed, defineComponent, ref, renderList } from "vue"
import type { IEnchantingInfo } from "@/api/info/type"
import { useBasicInfoStore, useConfigStore, useDetailsStore } from "@/store"
export default defineComponent({
  name: "Equip",
  props: {
    part: {
      type: String,
      default: "头肩"
    }
  },
  setup(props) {
    const detailsStore = useDetailsStore()
    const configStore = useConfigStore()
    const can_upgrade = computed(() => {
      return !["称号", "宠物"].includes(props.part as string)
    })

    // const globalStore = useGlobalStore()

    const has_socket = computed(() => !["称号", "宠物", "耳环", "武器"].includes(props.part as string))
    const has_socket_right = computed(() => has_socket.value && !["辅助装备", "魔法石"].includes(props.part as string))
    const has_wisdom = computed(() => !["称号", "宠物", "武器"].includes(props.part as string))
    const basicInfoStore = useBasicInfoStore()

    const enchanting_list = computed<IEnchantingInfo[] | undefined>(() => {
      return basicInfoStore.details?.enchanting
        ?.filter(item => item.position.includes(props.part) && !item.position.includes("武器装扮") && !item.position.includes("宠物装备"))
        .sort((a, b) => b.rate - a.rate)
    })

    const emblem_list = computed<IEnchantingInfo[] | undefined>(() => {
      return basicInfoStore.details?.emblem?.filter(item => item.position.includes(props.part))
    })

    const global_change = ref(false)

    const currentInfo = function<T>(name: string, defaultValue?: T) {
      return computed<string | number>({
        get() {
          return configStore.getForge(props.part, name) ?? defaultValue ?? 0
        },
        set(val) {
          if (val == undefined) {
            return
          }
          if (name == "socket_right" && !has_socket_right.value) {
            configStore.setForge(props.part, name, 0)
            return
          }

          let parts: string[] = []

          if (global_change.value) {
            if (name === "enchanting") {
              const enchant = basicInfoStore.details?.enchanting?.find(item => item.id == val) as IEnchantingInfo | undefined
              if (enchant?.position) {
                parts = enchant.position
              }
            }
            if (["socket_left", "socket_right"].includes(name)) {
              const emblem = basicInfoStore.details?.emblem?.find(item => item.id.toString() == val.toString()) as IEnchantingInfo | undefined
              if (emblem?.position) {
                parts = emblem.position.filter(item => !["皮肤", "武器装扮", "光环"].includes(item))
              }
            }
            if (["cursed_type", "cursed_number"].includes(name)) {
              parts = detailsStore.display_parts.filter(e => !["称号", "宠物"].includes(e))
            }

            if (["growth_first", "growth_second", "growth_third", "growth_fourth"].includes(name)) {
              parts = detailsStore.display_parts.filter(e => !["称号", "宠物"].includes(e))
            }

            if (["growth_cs_first", "growth_cs_second", "growth_cs_third", "growth_cs_fourth"].includes(name)) {
              parts = detailsStore.display_parts.filter(e => !["称号", "宠物"].includes(e))
            }

            if (name == "growth_sj") {
              parts = detailsStore.display_parts.filter(e => !["称号", "宠物"].includes(e))
            }

            if (name == "fusion_upgrade") {
              parts = ["手镯", "项链", "戒指", "辅助装备", "魔法石", "耳环"]
            }
          } else {
            parts = [props.part]
          }

          for (const part of parts) {
            if (part == "武器" && name == "growth_sj") {
              configStore.setForge(part, name, Math.min(40, val as number))
            } else if (part == "武器" && name.includes("growth_cs")) {
              configStore.setForge(part, name, Math.min(70, val as number))
            } else { configStore.setForge(part, name, val) }
          }
        }
      })
    }

    // 附魔
    const enchanting = currentInfo<string | number>("enchanting")

    // 镶嵌栏1
    const socket_left = currentInfo<string | number>("socket_left", 0)

    // 镶嵌栏2
    const socket_right = currentInfo<string | number>("socket_right")

    // 增幅
    const cursed_type = currentInfo<string | number>("cursed_type", 1)

    // 增幅数值
    const cursed_number = currentInfo<string | number>("cursed_number")

    // 智慧产物等级
    const wisdom_number = currentInfo<string | number>("wisdom_number")

    // 锻造数值
    const dz_number = currentInfo<string | number>("dz_number")

    // 成长1
    const growth_first = currentInfo<string | number>("growth_first", 80)

    // 成长2
    const growth_second = currentInfo<string | number>("growth_second", 80)

    // 成长3
    const growth_third = currentInfo<string | number>("growth_third", 80)

    // 成长4
    const growth_fourth = currentInfo<string | number>("growth_fourth", 80)

    // 成长1
    const growth_cs_first = currentInfo<string | number>("growth_cs_first", 50)

    // 成长2
    const growth_cs_second = currentInfo<string | number>("growth_cs_second", 50)

    // 成长3
    const growth_cs_third = currentInfo<string | number>("growth_cs_third", 50)

    // 成长4
    const growth_cs_fourth = currentInfo<string | number>("growth_cs_fourth", 50)

    const growth_sj = currentInfo<string | number>("growth_sj", 0)

    const fusion_upgrade = currentInfo<boolean>("fusion_upgrade", true)

    const changeable = currentInfo<boolean>("changeable", true)

    /**
       * 同步成长属性1到其他成长属性
       * @param val
       */
    function changeGrowth(val: number) {
      growth_second.value = val
      growth_third.value = val
      growth_fourth.value = val
    }

    function changeCSGrowth(val: number) {
      growth_cs_second.value = val
      growth_cs_third.value = val
      growth_cs_fourth.value = val
      if (val != 80) {
        growth_sj.value = 0
      }
    }

    /**
       * 同步徽章1到徽章2
       * @param val
       */
    function changeSocket(val: number) {
      if (has_socket_right.value) {
        socket_right.value = val
      }
    }

    return () => {
      return (
        <div class="flex flex-wrap equ-profile">
          <div class="equ-profile-item">
            <div class="mr-10px row-name">当前部位</div>
            <span> {props.part}</span>
            {can_upgrade.value ? <calc-checkbox style="margin-left:auto" v-model={global_change.value} label="全局修改"></calc-checkbox> : <div></div>}
          </div>
          {can_upgrade.value ? (
            <div class="equ-profile-item">
              <div class="row-name">增幅</div>
              <calc-select v-model={cursed_type.value} class="flex-1 !h-20px">
                <calc-option value={1}>增幅</calc-option>
                <calc-option value={2}>强化</calc-option>
              </calc-select>
              <calc-select v-model={cursed_number.value} class="flex-1 !h-20px">
                {renderList(32, i => (
                  <calc-option value={i - 1}>{i - 1}</calc-option>
                ))}
              </calc-select>
              {has_wisdom.value ? (
                <calc-select v-model={wisdom_number.value} class="flex-1 !h-20px">
                  {renderList(32, i => (
                    <calc-option value={i - 1}>改造+ {i - 1}</calc-option>
                  ))}
                </calc-select>
              ) : (
                <calc-select v-model={dz_number.value} class="flex-1 !h-20px">
                  {renderList(9, i => (
                    <calc-option value={i - 1}>锻造+ {i - 1}</calc-option>
                  ))}
                </calc-select>
              )}
            </div>
          ) : (
            <div></div>
          )}
          <div class="equ-profile-item">
            <div class="row-name">附魔</div>
            <calc-select v-model={enchanting.value} class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              {renderList(enchanting_list.value ?? [], item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>
          </div>
          {has_socket.value ? (
            <div class="equ-profile-item">
              <div class="row-name">徽章</div>
              <calc-select onChange={changeSocket} v-model={socket_left.value} class="flex-1 !h-20px">
                <calc-option value={0}>无</calc-option>
                {renderList(emblem_list.value ?? [], item => (
                  <calc-option value={item.id}>{`${item.rarity}${item.type}徽章[${item.props}]`}</calc-option>
                ))}
              </calc-select>
              {has_socket_right.value && (
                <calc-select v-model={socket_right.value} class="flex-1 !h-20px">
                  <calc-option value={0}>无</calc-option>
                  {renderList(emblem_list.value ?? [], item => (
                    <calc-option value={item.id}>{`${item.rarity}${item.type}徽章[${item.props}]`}</calc-option>
                  ))}
                </calc-select>
              )}
            </div>
          ) : (
            <div></div>
          )}
          {can_upgrade.value ? (
            <>
              {/* <div class="equ-profile-item">
                <div class="row-name">成长属性</div>
                <calc-select onChange={changeGrowth} v-model={growth_first.value} class="flex-1 !h-20px">
                  {renderList(80, i => (
                    <calc-option value={i}>
                       Lv{i}
                    </calc-option>
                  ))}
                </calc-select>
                {false && (
                  <>
                    <calc-select v-model={growth_second.value} class="flex-1 !h-20px">
                      {renderList(80, i => (
                        <calc-option value={i}>属性2 Lv{i}</calc-option>
                      ))}
                    </calc-select>
                    <calc-select v-model={growth_third.value} class="flex-1 !h-20px">
                      {renderList(80, i => (
                        <calc-option value={i}>属性3 Lv{i}</calc-option>
                      ))}
                    </calc-select>
                    <calc-select v-model={growth_fourth.value} class="flex-1 !h-20px">
                      {renderList(80, i => (
                        <calc-option value={i}>属性4 Lv{i}</calc-option>
                      ))}
                    </calc-select>
                  </>
                )}
              </div> */}
              {/* <div class="equ-profile-item">
                <div class="row-name">传说成长</div>
                <calc-select onChange={changeCSGrowth} v-model={growth_cs_first.value} class="flex-1 !h-20px">
                  {renderList(props.part == "武器" ? 70 : 80, i => (
                    <calc-option value={i}>
                      {false && "属性1"} Lv{i}
                    </calc-option>
                  ))}
                </calc-select>
                {false && (
                  <>
                    <calc-select v-model={growth_cs_second.value} class="flex-1 !h-20px">
                      {renderList(70, i => (
                        <calc-option value={i}>属性2 Lv{i}</calc-option>
                      ))}
                    </calc-select>

                    <calc-select v-model={growth_cs_third.value} class="flex-1 !h-20px">
                      {renderList(70, i => (
                        <calc-option value={i}>属性3 Lv{i}</calc-option>
                      ))}
                    </calc-select>
                    <calc-select v-model={growth_cs_fourth.value} class="flex-1 !h-20px">
                      {renderList(70, i => (
                        <calc-option value={i}>属性4 Lv{i}</calc-option>
                      ))}
                    </calc-select>
                  </>
                )}
              </div> */}

              <div class="equ-profile-item">
                {/* <div class="row-name">神界等级</div>
                <calc-select
                  onChange={() => {
                    growth_first.value = 80
                    changeGrowth(80)
                  }}
                  v-model={growth_sj.value}
                  class="flex-1 !h-20px"
                >
                  {renderList(props.part == "武器" ? 41 : 61, i => (
                    <calc-option value={i - 1}>Lv{i - 1}</calc-option>
                  ))}
                </calc-select> */}
                <calc-checkbox label="星辰百变装备" v-model={changeable.value}></calc-checkbox>
                {["手镯", "项链", "戒指", "辅助装备", "魔法石", "耳环"].includes(props.part) && <calc-checkbox label="融合升级" v-model={fusion_upgrade.value}></calc-checkbox>}
              </div>

            </>
          ) : (
            <div></div>
          )}
        </div>
      )
    }
  }
})
</script>

<style lang="scss"></style>
