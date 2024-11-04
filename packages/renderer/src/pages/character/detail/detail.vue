<script lang="tsx">
import { defineComponent, ref } from "vue"
import Clothes from "./sub/clothes.vue"
import Equip from "./sub/equip.vue"
import Jade from "./sub/jade.vue"
import Others from "./sub/others.vue"
import Petequ from "./sub/petequ.vue"
import Special from "./sub/special.vue"
import Corrections from "./sub/corrections.vue"
import Medal from "./sub/medal.vue"
import EquipmentsVue from "@/components/internal/profile/equipments.vue"
export default defineComponent({
  components: { EquipmentsVue, Equip, Jade, Clothes, Others, Petequ, Special },
  setup() {
    const part = ref("头肩")

    return () => (
      <div class="detail-body">
        <div>
          <div class="bg-hex-00000078 w-510px">
            <div class="w-100% flex items-center justify-center">
              <EquipmentsVue v-model:part={part.value} canChoose={true} showSpe={false}>
              </EquipmentsVue>
            </div>
          </div>
          <calc-collapse class="w-510px" title="装备打造(点击人物部位切换)">
            <Equip part={part.value} />
          </calc-collapse>
          <calc-collapse class="w-510px" title="装扮部分">
            <Clothes />
          </calc-collapse>
          <calc-collapse class="w-510px" title="职业特殊">
            <Special />
          </calc-collapse>
        </div>
        <div class="pl-20px">
          <calc-collapse class="w-510px" title="宠物装备">
            <Petequ />
          </calc-collapse>
          <calc-collapse class="w-510px" title="辟邪玉">
            <Jade />
          </calc-collapse>
          <calc-collapse class="w-510px" title="勋章">
            <Medal />
          </calc-collapse>
          <calc-collapse class="w-510px" title="其它">
            <Others />
          </calc-collapse>
          <calc-collapse class="w-510px" title="属性修正">
            <Corrections />
          </calc-collapse>
        </div>
      </div>
    )
  }
})
</script>

<style lang="scss">
  .detail-body {
    display: flex;
    width: 100%;
    margin-left: 25px;
    margin-right: 25px;
  }

  .equ-profile {
    width: 100%;

    .equ-profile-item {
      width: 100%;
      height: 20px;
      display: flex;
      margin-top: 5px;
      margin-bottom: 5px;
      align-items: center;

      .row-name {
        flex: 0 0 50px;
        text-align: center;
      }

      :not(:last-child) {
        margin-right: 10px !important;
      }

      .i-select-label {
        margin-right: 0px !important;
      }
    }
  }
</style>
