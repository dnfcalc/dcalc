<script lang="tsx">
import type { PropType } from "vue"
import { defineComponent, renderList } from "vue"
import type { IEquipmentInfo } from "@/api/info/type"
import EquipTips from "@/components/internal/equip/eq-icon-tips.vue"
import {
  useBasicInfoStore,
  useConfigStore

} from "@/store";

import EqIcon from "@/components/internal/equip/eq-icon.vue"

export default defineComponent({
  name: "Cus",
  components: { EquipTips, EqIcon },
  props: {
    equList: {
      type: Array as PropType<IEquipmentInfo[]>,
      default: () => []
    }
  },
  setup(props, { emit }) {
    const configStore = useConfigStore();
    const basicStore = useBasicInfoStore();
    const part = ["称号", "宠物", "武器", "上衣", "下装", "头肩", "腰带", "鞋", "手镯", "项链", "戒指", "辅助装备", "魔法石", "耳环"]
    const equips = [...props.equList].sort((a, b) => {
      return part.indexOf(a.part) - part.indexOf(b.part)
    })
    return () => (
      <div class="flex flex-col cus_head ">
        {renderList(equips, equip => {
          if ((configStore.customize?.[equip.id ?? ""] ?? []).length > 0 || ((configStore.merge?.[equip.id ?? ""] ?? []).filter(a => a > 0) ?? []).length > 0) {
            return (
              <>
                <div class="flex items-center w-100% item">
                  <div class="flex flex-col justify-center items-center w-40px">
                    <eq-icon class="eq-item-icon" eq={equip} canClick={false}></eq-icon>
                  </div>
                  <div class="flex-1">
                    {equip.part == "武器" && ((configStore.merge?.[equip.id ?? ""] ?? []).filter(a => a > 0) ?? []).length > 0 && (
                      <div>
                        {(configStore.merge?.[equip.id ?? ""] ?? []).filter(a => a > 0).map(a => basicStore.entry_list?.[a]?.order ?? 0).join(",")}
                      </div>
                    )}
                    {(configStore.customize?.[equip.id ?? ""] ?? []).filter(a => a > 0).length > 0 && (
                      <div>
                        {renderList(
                          (configStore.customize?.[equip.id ?? ""] ?? []).filter(a => a > 0),
                          (a) => {
                            return (
                              <div class="props">
                                {/* <div class="text-hex-b59834">属性 {index + 1}</div> */}
                                <div>
                                  {basicStore.entry_list?.[a.toString()].abbr
                                    ? (<div class="mx-5px">
                                        <span>{basicStore.entry_list?.[a.toString()].abbr}</span>
                                      </div>) : (<>{renderList(basicStore.entry_list?.[a.toString()].props ?? [], prop => (
                                        <div class="mx-5px">
                                          <span>{prop}</span>
                                        </div>
                                      ))}</>)
                                  }

                                </div>
                              </div>
                            )
                          }
                        )}
                      </div>
                    )}
                  </div>
                </div>
              </>
            )
          }
        })}
      </div>
    )
  }
})
</script>

<style lang="scss" scoped>
.cus_head{
  background-color: #000000bf;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  height: 400px;
  max-height: 400px;
  overflow-y: auto;
  color: #B1A785;
  .item{
    margin-top: 2px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    padding-top: 1px;
    padding-bottom: 1px;
  }
}
  .props {
    position: relative;
    padding-left: 12px;
    line-height: 15px;

    &::before {
      content: "";
      display: inline-block;
      position: absolute;
      left: 0px;
      top:1.5px;
      // top: 5px;
      width: 12px;
      height: 12px;
      background-image: url(@/assets/img/icon/switch.png);
    }
  }
</style>
