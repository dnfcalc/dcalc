<script lang="tsx">
import { computed, defineComponent, ref, renderList } from 'vue'
import type { IEnchantingInfo } from '@/api/info/type'
import { useInfoStore, useConfigStore } from '@/stores'
import EquList from '@/components/dnf/Equipment/List/index.vue'
export default defineComponent({
  name: 'Equip',
  setup(props) {
    const configStore = useConfigStore()
    const part = ref('头肩')
    const can_upgrade = computed(() => {
      return !['称号', '宠物'].includes(part.value as string)
    })

    // const globalStore = useGlobalStore()

    /** 是否有徽章 */
    const has_socket = computed(
      () => !['称号', '宠物', '耳环', '武器'].includes(part.value as string),
    )
    /** 是否有右侧徽章 */
    const has_emblem_1 = computed(
      () => has_socket.value && !['辅助装备', '魔法石'].includes(part.value as string),
    )
    /** 是否可以设置秘宝精度 */
    const can_set_secret = computed(() => {
      return ['辅助装备', '魔法石','耳环'].includes(part.value as string)
    })
    const basicInfoStore = useInfoStore()

    const enchant_list = computed<IEnchantingInfo[] | undefined>(() => {
      return basicInfoStore.enchants
        ?.filter(
          (item) =>
            item.position.includes(part.value) &&
            !item.position.includes('武器装扮') &&
            !item.position.includes('宠物装备'),
        )
        .sort((a, b) => (b.fame ?? 0) - (a.fame ?? 0))
    })

    const emblem_list = computed<IEnchantingInfo[] | undefined>(() => {
      return basicInfoStore.emblems.filter((item) => item.position.includes(part.value))
    })

    const global_change = ref(false)

    const currentInfo = function <T>(name: string, defaultValue?: T) {
      return computed<string | number>({
        get() {
          return (
            (configStore.config.equips?.[part.value] as Record<string, any>)?.[name] ??
            defaultValue ??
            0
          )
        },
        set(val) {
          if (val == undefined) {
            return
          }
          if (name == 'emblem_1' && !has_emblem_1.value) {
            // configStore.setForge(part.value, name, 0)
            return
          }

          let parts: string[] = []

          if (global_change.value) {
            if (name === 'enchant') {
              const enchant = basicInfoStore?.enchants?.find((item) => item.id == val) as
                | IEnchantingInfo
                | undefined
              if (enchant?.position) {
                parts = enchant.position
              }
            }
            if (['emblem_0', 'emblem_1'].includes(name)) {
              const emblem = basicInfoStore?.emblems?.find(
                (item) => item.id.toString() == val.toString(),
              ) as IEnchantingInfo | undefined
              if (emblem?.position) {
                parts = emblem.position.filter(
                  (item) => !['皮肤', '武器装扮', '光环'].includes(item),
                )
              }
            }
            if (['reinforceType', 'reinforce','adaptation'].includes(name)) {
              parts = basicInfoStore.parts.filter((e) => !['称号', '宠物'].includes(e))
            }
          } else {
            parts = [part.value]
          }
          for (const part of parts) {
            if (configStore.config.equips[part]) {
              (configStore.config.equips[part] as Record<string, any>)[name] = val
            }
          }
        },
      })
    }

    // 附魔
    const enchant = currentInfo<string | number>('enchant')

    // 镶嵌栏1
    const emblem_0 = currentInfo<string | number>('emblem_0', 0)

    // 镶嵌栏2
    const emblem_1 = currentInfo<string | number>('emblem_1')

    // 增幅
    const reinforce_type = currentInfo<string | number>('reinforceType', 1)

    // 增幅数值
    const reinforce = currentInfo<string | number>('reinforce')

    // 锻造数值
    const refine = currentInfo<string | number>('refine')

    // 调适
    const adaptation = currentInfo<string | number>('adaptation')

    //精度
    const precision = currentInfo<number>('precision',0)
    /**
     * 同步徽章1到徽章2
     * @param val
     */
    function changeSocket(val: number) {
      if (has_emblem_1.value) {
        emblem_1.value = val
      }
    }

    return () => {
      return (
        <>
        <div class="h-150px flex justify-center items-center">
          <EquList v-model:part={part.value} withBg={false} withPet={false}/></div>

        <div class="flex flex-wrap equ-profile">
          <div class="equ-profile-item">
            <div class="mr-10px row-name">当前部位</div>
            <span> {part.value}</span>
            {can_upgrade.value ? (
              <calc-checkbox
                style="margin-left:auto"
                v-model={global_change.value}
                label="全局修改"
              ></calc-checkbox>
            ) : (
              <div></div>
            )}
          </div>
          {can_upgrade.value ? (
            <div class="equ-profile-item">
              <div class="row-name">增幅</div>
              <calc-select v-model={reinforce_type.value} class="flex-1 !h-20px">
                <calc-option value={0}>强化</calc-option>
                <calc-option value={1}>增幅</calc-option>
              </calc-select>
              <calc-select v-model={reinforce.value} class="flex-1 !h-20px">
                {renderList(31, (i) => (
                  <calc-option value={i - 1}>{i - 1}</calc-option>
                ))}
              </calc-select>
              {part.value == '武器' && (
                <calc-select v-model={refine.value} class="flex-1 !h-20px">
                  {renderList(9, (i) => (
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
            <calc-select v-model={enchant.value} class="flex-1 !h-20px">
              <calc-option value={""}>无</calc-option>
              {renderList(enchant_list.value ?? [], (item) => (
                <calc-option value={item.id}>{item.detail}</calc-option>
              ))}
            </calc-select>
          </div>
          {has_socket.value ? (
            <div class="equ-profile-item">
              <div class="row-name">徽章</div>
              <calc-select
                onChange={changeSocket}
                v-model={emblem_0.value}
                class="flex-1 !h-20px"
              >
                <calc-option value={""}>无</calc-option>
                {renderList(emblem_list.value ?? [], (item) => (
                  <calc-option
                    value={item.id}
                  >{`${item.rarity}${item.categorize}徽章[${item.detail}]`}</calc-option>
                ))}
              </calc-select>
              {has_emblem_1.value && (
                <calc-select v-model={emblem_1.value} class="flex-1 !h-20px">
                  <calc-option value={""}>无</calc-option>
                  {renderList(emblem_list.value ?? [], (item) => (
                    <calc-option
                      value={item.id}
                    >{`${item.rarity}${item.categorize}徽章[${item.detail}]`}</calc-option>
                  ))}
                </calc-select>
              )}
            </div>
          ) : (
            <div></div>
          )}

          {can_upgrade.value ? (
            <div class="equ-profile-item">
              <div class="row-name">调适</div>
              {/* <calc-slider
                showValue={true}
                showPercent={false}
                v-model={adaptation.value}
                min={0}
                max={3}
                step={1}
                class="flex-1 !h-20px"
              /> */}
              <calc-select v-model={adaptation.value} class="flex-1 !h-20px">
                {renderList(4, (i) => (
                  <calc-option value={i - 1}>{i - 1}</calc-option>
                ))}
              </calc-select>
            </div>
          ) : (
            <div></div>
          )}
          {
            can_set_secret.value ? (<>
            <div class="equ-profile-item">
              <div class="row-name">秘宝</div>
              <calc-slider
                showPercent={true}
                showValue={false}
                v-model={precision.value}
                min={0}
                max={100}
                step={1}
                class="flex-1 !h-20px"
              />
            </div>
            </>) : <div></div>
          }
        </div>
        </>
      )
    }
  },
})
</script>

<style lang="scss"></style>
