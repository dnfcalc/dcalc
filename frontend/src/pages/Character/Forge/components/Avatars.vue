<script lang="tsx">
import { computed, defineComponent, ref, renderList } from 'vue'
import type { IEnchantingInfo } from '@/api/info/type'
import { useInfoStore, useConfigStore } from '@/stores'
import ClothList from '@/components/dnf/Avatar/List/index.vue'
export default defineComponent({
  name: 'Clothes',
  setup(props) {
    const configStore = useConfigStore()
    const part = ref('武器装扮')

    // const globalStore = useGlobalStore()

    /** 是否有徽章 */
    const has_socket = computed(() => ['武器装扮', '光环', '皮肤'].includes(part.value as string))
    const basicInfoStore = useInfoStore()
    const has_enchant = computed(() => {
      return !['头发', '帽子', '脸部', '胸部', '上衣', '腰带', '下装', '鞋'].includes(
        part.value as string,
      )
    })

    const enchant_list = computed<IEnchantingInfo[] | undefined>(() => {
      return basicInfoStore.enchants
        ?.filter((item) => item.position.includes(part.value))
        .sort((a, b) => (b.fame ?? 0) - (a.fame ?? 0))
    })

    const emblem_list = computed<IEnchantingInfo[] | undefined>(() => {
      return basicInfoStore.emblems.filter((item) => item.position.includes(part.value))
    })

    const currentInfo = function <T>(name: string, defaultValue?: T) {
      return computed<string | number>({
        get() {
          let key: 'avatar' | 'equips' = 'avatar'
          if (part.value == '宠物') key = 'equips'
          return (
            (configStore.config[key]?.[part.value] as Record<string, any>)?.[name] ??
            defaultValue ??
            0
          )
        },
        set(val) {
          if (val == undefined) {
            return
          }
          let key: 'avatar' | 'equips' = 'avatar'
          if (part.value == '宠物') key = 'equips'
          if (configStore.config[key][part.value]) {
            ;(configStore.config[key][part.value] as Record<string, any>)[name] = val
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

    // 品级
    const id = currentInfo<string | number>('id')

    // 属性
    const option = currentInfo<string | number>('option')

    /**
     * 同步徽章1到徽章2
     * @param val
     */
    function changeSocket(val: number) {
      emblem_1.value = val
    }

    return () => {
      return (
        <>
          <div class="h-120px flex justify-center items-center">
            <ClothList v-model:part={part.value} />
          </div>

          <div class="flex flex-wrap equ-profile">
            <div class="equ-profile-item">
              <div class="mr-10px row-name">当前部位</div>
              <span> {part.value}</span>
            </div>
            {has_enchant.value ? (
              <div class="equ-profile-item">
                <div class="row-name">{part.value == '宠物' ? '附魔' : '属性'}</div>
                <calc-select v-model={enchant.value} class="flex-1 !h-20px">
                  <calc-option value={0}>无</calc-option>
                  {renderList(enchant_list.value ?? [], (item) => (
                    <calc-option value={item.id}>{item.detail}</calc-option>
                  ))}
                </calc-select>
              </div>
            ) : (
              <>
                <div class="equ-profile-item">
                  <div class="row-name">品级</div>
                  <calc-select v-model={id.value} class="flex-1 !h-20px">
                    {renderList(basicInfoStore.avatars[part.value] ?? [], (item) => (
                      <calc-option value={item.id}>{item.suit}</calc-option>
                    ))}
                  </calc-select>
                </div>
                <div class="equ-profile-item">
                  <div class="row-name">属性</div>
                  <calc-select v-model={option.value} class="flex-1 !h-20px">
                    <calc-option value={0}>无</calc-option>
                    {renderList(
                      basicInfoStore.avatars[part.value].find((a) => a.id == id.value)?.options ??
                        [],
                      (item) => (
                        <calc-option value={item}>{item}</calc-option>
                      ),
                    )}
                  </calc-select>
                </div>
              </>
            )}
            {has_socket.value ? (
              <div class="equ-profile-item">
                <div class="row-name">徽章</div>
                <calc-select
                  onChange={changeSocket}
                  v-model={emblem_0.value}
                  class="flex-1 !h-20px"
                >
                  <calc-option value={0}>无</calc-option>
                  {renderList(emblem_list.value ?? [], (item) => (
                    <calc-option
                      value={item.id}
                    >{`${item.rarity}${item.categorize}徽章[${item.detail}]`}</calc-option>
                  ))}
                </calc-select>
                <calc-select v-model={emblem_1.value} class="flex-1 !h-20px">
                  <calc-option value={0}>无</calc-option>
                  {renderList(emblem_list.value ?? [], (item) => (
                    <calc-option
                      value={item.id}
                    >{`${item.rarity}${item.categorize}徽章[${item.detail}]`}</calc-option>
                  ))}
                </calc-select>
              </div>
            ) : (
              <div></div>
            )}
          </div>
        </>
      )
    }
  },
})
</script>

<style lang="scss"></style>
