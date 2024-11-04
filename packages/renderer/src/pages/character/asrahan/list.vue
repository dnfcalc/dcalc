<script lang="tsx">
import type { PropType } from "vue";
import { computed, defineComponent, onMounted, ref, renderList, watch } from "vue"
import Watermark from "@/components/watermark/index.vue"
import { useBasicInfoStore, useCharacterStore, useConfigStore } from "@/store";
import { formatStr } from "@/utils";


export default defineComponent({
  name: "Others",
  props: {
    eid: {
      type: [Number, String] as PropType<ID>,
      default: "0"
    }
  },
  setup(props) {
    const selectEquip = ref<ID>(props.eid)
    const basicStore = useBasicInfoStore()
    const charStore = useCharacterStore()
    const configStore = useConfigStore()

    const clickList = computed(() => {
      const list: number[] = []

      const name = basicStore.equipment_list.filter(item => item.id == props.eid)?.[0]?.name ?? "";

      ["雷", "风", "霜", "焰", "雨", "失衡"].forEach((item, index) => {
        if (name.startsWith(`${item} :`) || (name.startsWith("跨越之忆") && index != 5)) {
          list.push(index)
        }
      })
      return list
    })

    const maxAdditional = computed(() => {
      return configStore.asrahan.lv == 0 ? 0 : (Math.floor(configStore.asrahan.lv / 5) + 2);
    })

    onMounted(() => {
      if(!configStore.asrahan.type || !clickList.value.includes(configStore.asrahan.type))
        configStore.asrahan.type = clickList.value[0] ?? 0
    })

    watch(() => props.eid, () => {
      if(!configStore.asrahan.type || !clickList.value.includes(configStore.asrahan.type))
        configStore.asrahan.type = clickList.value[0] ?? 0
    })

    const curInfo = computed(() => {
      const info = charStore.asrahan.find(a => a.type == configStore.asrahan.type)
      const lv = (configStore.asrahan.lv ?? 0) + (configStore.asrahan.additional ?? 0)
      return !info || lv <= 0 ? ""
        : formatStr(info.desc, info.lvinfo[lv - 1].params.map(a => `<span style='color:#4aa256'>${a}</span>`))
          .replaceAll(/(\d)(?=(\d{3})+(?!\d))/g, "$1,")
          .replaceAll(/@([^@]*)@/g, (m, _index) => `<span style="color:#99844f">${m.slice(1, -1)}</span>`)
          .split("<br/><br/>").filter((a, index) => index == 0 || !a.includes("<span style='color:#4aa256'>0</span>")).join("<br/><br/>")
          .split("<br/>").filter(a => !a.includes("<span style='color:#4aa256'>0</span>"))
    })

    const maxInfo = computed(() => {
      const info = charStore.asrahan.find(a => a.type == configStore.asrahan.type)
      return (!info || !info?.max) ? []: (info?.max ?? "")
          .replaceAll(/(\d)(?=(\d{3})+(?!\d))/g, "$1,")
          .replaceAll(/@([^@]*)@/g, (m, _index) => `<span style="color:#4aa256">${m.slice(1, -1)}</span>`)
          .split("<br/>")
    })


    return () => (
      <Watermark>
        {selectEquip.value && (
          <div class="w-full">
            <div class="flex">
              {renderList(6, (index) => (
                <>
                  {clickList.value.includes(index - 1) && (<div onClick={() => configStore.asrahan.type = index - 1} style={configStore.asrahan.type == index - 1 ? "" : "filter:grayscale(100%)"} class="w-20% flex items-center justify-center h-12">
                    <div style="zoom:0.4" class={`asrahan-icon-${index - 1}`}></div>
                  </div>)}
                </>
              ))}
            </div>
            <div class="flex h-5 items-center m-2 my-1.5">
              <div class="flex flex-1 items-center">
                星团等级<calc-button disabled={configStore.asrahan.lv <= 0} onClick={() => configStore.asrahan.lv -= 1} icon="reduce"></calc-button>
                <div class={`lvInfo${configStore.asrahan.lv == 15 ? "Master" : "Active"}`}>
                  <div class="w-12px h-14px ml-15px pt-1.5px flex items-center justify-center text-10px">
                    {configStore.asrahan.lv}</div>
                </div>
                <calc-button disabled={configStore.asrahan.lv >= 15 } onClick={() => configStore.asrahan.lv += 1} icon="increase"></calc-button>
              </div>
              <div class="flex flex-1 items-center">
                梦境等级<calc-button disabled={configStore.asrahan.additional <= 0} onClick={() => configStore.asrahan.additional -= 1} icon="reduce"></calc-button>
                <div class={`lvInfo${configStore.asrahan.additional == 5 ? "Master" : "Active"}`}>
                  <div class="w-12px h-14px ml-15px pt-1.5px flex items-center justify-center text-10px">
                    {configStore.asrahan.additional}</div>
                </div>
                <calc-button disabled={configStore.asrahan.additional >= maxAdditional.value || configStore.asrahan.lv == 0 } onClick={() => configStore.asrahan.additional += 1} icon="increase"></calc-button>
              </div>
            </div>
            {
              configStore.asrahan.lv > 0
              && (
                <>
                  <div class="text-hex-B1A785 mx-2 mb-1.5">{charStore.asrahan.find(a => a.type == configStore.asrahan.type)?.name}之星团(点亮阶段 : <span class="text-hex-4aa256">{configStore.asrahan.lv + configStore.asrahan.additional}</span>)</div>
                  <div class="text-hex-99844f mx-2">
                    <div>
                      {renderList(curInfo.value, item => (<div style="min-height:5px;line-height:14px;white-space: pre-wrap" v-html={item}></div>))}
                    </div>
                  </div></>
              )
            }
            {configStore.asrahan.additional > 0
              && (<>
                <div class="text-hex-99844f mx-2 mt-2">[雾神梦境]</div>
                <div class="text-hex-99844f mx-2">
                  <div>技能伤害 +<span class="text-hex-4aa256">{configStore.asrahan.additional}</span>%</div>
                  <div>增益量 <span class="text-hex-4aa256">{190 * configStore.asrahan.additional}</span></div>
                </div>
              </>)}

              {(configStore.asrahan.lv + configStore.asrahan.additional) >= 20 && maxInfo.value.length > 0
              && (<>
              <div class="text-hex-B1A785 mx-2 mt-2.5 mb-1.5">崇高的表象</div>
              <div class="text-hex-99844f mx-2">
                    <div>
                      {renderList(maxInfo.value, item => (<div style="min-height:5px;line-height:16px;white-space: pre-wrap" v-html={item}></div>))}
                    </div>
                  </div>
              </>)}


          </div>
        )}
      </Watermark>)
  }
}
)
</script>
