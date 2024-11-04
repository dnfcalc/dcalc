<script lang="tsx">
import { computed, defineComponent, renderList } from "vue"
import { useBasicInfoStore, useConfigStore } from "@/store"

export default defineComponent({
  name: "Others",

  setup() {
    const configStore = useConfigStore()
    const basicInfoStore = useBasicInfoStore()

    const currentInfo = function<T>(name: string, defaultValue?: T) {
      return computed<string | number>({
        get() {
          return configStore.getForge("others", name) ?? defaultValue ?? 0
        },
        set(val) {
          configStore.setForge("others", name, val)
        }
      })
    }

    function currentOptions(position: string) {
      return computed(() => basicInfoStore.details?.sundries.filter(item => item.position.includes(position)) ?? [])
    }

    const equipInfo = function<T>(part: string, name: string, defaultValue?: T) {
      return computed<string | number>({
        get() {
          return configStore.getForge(part, name) ?? defaultValue ?? 0
        },
        set(val) {
          if (val == undefined) {
            return
          }
          configStore.setForge(part, name, val)
        }
      })
    }

    // 冒险团等级
    const mxtLV = currentInfo("mxtLV")
    const mxtLV_list = currentOptions("冒险团")

    // 工会属性
    const gh = currentInfo("gh")
    const gh_list = currentOptions("工会属性")

    // 工会BUFF-四维
    const gh_buff_SW = currentInfo("gh_buff_SW")
    const gh_buff_SW_list = currentOptions("工会buff-四维强化")
    // 工会BUFF-攻击力
    const gh_buff_GJ = currentInfo("gh_buff_GJ")
    const gh_buff_GJ_list = currentOptions("工会buff-攻击力")
    // 婚房
    const HF = currentInfo("HF")
    const HF_list = currentOptions("婚房")
    // 婚戒
    const HJ = currentInfo("HJ")
    const HJ_list = currentOptions("婚戒")
    // 收集箱种类
    const SJX_TYPE = currentInfo("SJX_TYPE")
    const SJX_TYPE_list = currentOptions("收集箱")
    // 晶体契约
    const JTQY = currentInfo("JTQY", 0)
    const JTQY_list = currentOptions("晶体契约")
    // 收集箱稀有
    const SJX_XY = currentInfo("SJX_XY")
    // 收集箱神器
    const SJX_SQ = currentInfo("SJX_SQ")
    // // 勋章种类
    // const XZ_TYPE = currentInfo("XZ_TYPE")
    // const XZ_TYPE_list = currentOptions("勋章")
    // // 勋章守护珠
    // const XZ_SHZ = currentInfo("XZ_SHZ")
    // // 勋章强化
    // const XZ_QH = currentInfo("XZ_QH")
    // // 勋章攻速
    // const XZ_GS = currentInfo("XZ_GS")
    // 名称装扮卡
    const MCZBK = currentInfo("MCZBK")
    const MCZBK_list = currentOptions("名称装扮卡")
    // 快捷装备
    const KJZB = equipInfo("快捷装备", "enchanting")
    const KJZB_list = computed(() => basicInfoStore.details?.enchanting.filter(item => item.position.includes("快捷装备")) ?? [])

    const SJX_disabled = computed(() => {
      return SJX_TYPE.value == 0
    })

    return () => (
      <div class="flex flex-wrap equ-profile">
        <div class="equ-profile-item">
          <div class="row-name">冒险团等级</div>
          <calc-select v-model={mxtLV.value} class="flex-1 !h-20px">
            {renderList(mxtLV_list.value, item => (
              <calc-option value={item.id}>{item.props}</calc-option>
            ))}
          </calc-select>
        </div>
        <div class="equ-profile-item">
          <div class="row-name">工会属性</div>
          <calc-select v-model={gh.value} class="flex-1 !h-20px">
            <calc-option value="0">无</calc-option>
            {renderList(gh_list.value, item => (
              <calc-option value={item.id}>{item.props}</calc-option>
            ))}
          </calc-select>
        </div>

        <div class="equ-profile-item">
          <div class="row-name">训练官</div>
          <calc-select v-model={gh_buff_SW.value} class="flex-1 !h-20px">
            <calc-option value="0">无</calc-option>
            {renderList(gh_buff_SW_list.value, item => (
              <calc-option value={item.id}>{item.props}</calc-option>
            ))}
          </calc-select>

          <calc-select v-model={gh_buff_GJ.value} class="flex-1 !h-20px">
            <calc-option value="0">无</calc-option>
            {renderList(gh_buff_GJ_list.value, item => (
              <calc-option value={item.id}>{item.props}</calc-option>
            ))}
          </calc-select>
        </div>

        <div class="equ-profile-item">
          <div v-model={HJ.value} class="row-name">
            结婚系统
          </div>
          <calc-select v-model={HF.value} class="flex-1 !h-20px">
            <calc-option value="0">无</calc-option>
            {renderList(HF_list.value, item => (
              <calc-option value={item.id}>{item.props}</calc-option>
            ))}
          </calc-select>

          <calc-select v-model={HJ.value} class="flex-1 !h-20px">
            <calc-option value="0">无</calc-option>
            {renderList(HJ_list.value, item => (
              <calc-option value={item.id}>{item.props}</calc-option>
            ))}
          </calc-select>
        </div>

        <div class="equ-profile-item">
          <div class="row-name">晶体契约</div>
          <calc-select v-model={JTQY.value} class="flex-1 !h-20px">
            <calc-option value="0">无</calc-option>
            {renderList(JTQY_list.value, item => (
              <calc-option value={item.id}>{item.props}</calc-option>
            ))}
          </calc-select>
        </div>

        <div class="equ-profile-item">
          <div class="row-name">收集箱</div>
          <calc-select v-model={SJX_TYPE.value} emptyLabel="种类" class="flex-1 !h-20px">
            <calc-option value="0">无</calc-option>
            {renderList(SJX_TYPE_list.value, item => (
              <calc-option value={item.id}>{item.props}</calc-option>
            ))}
          </calc-select>
          <calc-select v-model={SJX_XY.value} disabled={SJX_disabled.value} class="flex-1 !h-20px">
            {renderList(6, i => (
              <calc-option value={i - 1}>稀有: {i - 1}个</calc-option>
            ))}
          </calc-select>
          <calc-select v-model={SJX_SQ.value} disabled={SJX_disabled.value} class="flex-1 !h-20px">
            {renderList(6, i => (
              <calc-option value={i - 1}>神器: {i - 1}个</calc-option>
            ))}
          </calc-select>
        </div>

        {/* {new Date() < new Date("2023-09-20") && (
          <div class="equ-profile-item">
            <div class="row-name">勋章</div>
            <calc-select v-model={XZ_TYPE.value} class="flex-1 !h-20px">
              <calc-option value="0">无</calc-option>
              {renderList(XZ_TYPE_list.value, item => (
                <calc-option value={item.id}>{item.props}</calc-option>
              ))}
            </calc-select>
            <calc-select v-model={XZ_SHZ.value} emptyLabel="属强" class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              <calc-option value={5}>属强 +5</calc-option>
              <calc-option value={7}>属强 +7</calc-option>
            </calc-select>
            <calc-select v-model={XZ_GS.value} emptyLabel="攻速" class="flex-1 !h-20px">
              <calc-option value={0}>无</calc-option>
              <calc-option value={2.4}>攻速 +2.4%</calc-option>
              <calc-option value={3}>攻速 +3%</calc-option>
            </calc-select>
            <calc-select v-model={XZ_QH.value} emptyLabel="强化" class="flex-1 !h-20px">
              {renderList(21, i => (
                <calc-option value={i - 1}>强化: {i - 1}</calc-option>
              ))}
            </calc-select>
          </div>
        )} */}

        <div class="equ-profile-item">
          <div v-model={MCZBK.value} class="row-name">
            名称装扮卡
          </div>
          <calc-select v-model={MCZBK.value} class="flex-1 !h-20px">
            <calc-option value="0">无</calc-option>
            {renderList(MCZBK_list.value, item => (
              <calc-option value={item.id}>{item.props}</calc-option>
            ))}
          </calc-select>
        </div>

        <div class="equ-profile-item">
          <div class="row-name">快捷装备</div>
          <calc-select v-model={KJZB.value} class="flex-1 !h-20px">
            <calc-option value="0">无</calc-option>
            {renderList(KJZB_list.value, item => (
              <calc-option value={item.id}>{item.props}</calc-option>
            ))}
          </calc-select>
        </div>
      </div>
    )
  }
})
</script>

<style lang="scss" scoped>
.row-name {
  flex: 0 0 60px !important;
  text-align: center;
}
</style>
