<script lang="tsx">
import { useAsyncState, useDebounceFn } from "@vueuse/core";
import { computed, defineComponent, ref, renderList, watch } from "vue";
import {
  useBasicInfoStore,
  useCharacterStore,
  useConfigStore,
  useGlobalStore,
} from "@/store";
import Watermark from "@/components/watermark/index.vue";
import { formatStr, rarityClass } from "@/utils";

export interface ICusUpgrade {
  id: string;
  damage: number;
  percent: string;
  color: string;
}

export default defineComponent({
  name: "Others",
  props: {
    eid: {
      type: String,
      default: "0",
    }
  },
  setup(props) {
    const configStore = useConfigStore();
    const basicStore = useBasicInfoStore();

    const selectEquip = ref<Num>(props.eid);
    const colspans = ref([false, true, true]);
    const selectEquipProps = ref<number[]>([0, 0, 0]);
    // const selectPropsCheckedList = ref<Record<string, boolean>>({})

    function chooseProp(id: number, index: number) {
      return async (event: Event) => {
        event.stopPropagation();
        selectEquipProps.value[index] = selectEquipProps.value[index] == id ? 0 : id;
        configStore.customize[selectEquip.value ?? ""] = selectEquipProps.value;
      };
    }

    const equInfo = computed(() => {
      let a = (([...basicStore.equipment_list, ...(basicStore.equipment_info?.fusion ?? [])]).find(a => a.id == selectEquip.value))
      return a
    })

    const entry = (index: number) => {
      return basicStore.entry_list?.[index.toString()];
    };

    const entries = computed(() => basicStore.equipment_info?.fusion.filter((item) => item.id == selectEquip.value)?.[0]?.alternative ?? [])

    const LvClass = (lv: number) => {
      if (lv == 1)
        return rarityClass("高级")
      if (lv == 2)
        return rarityClass("稀有")
      if (lv == 3)
        return rarityClass("史诗")
      else
        return ""
    }

    const formatProps = (entry: any, lv: number) => {
      const { props } = entry
      try{
        if (!entry.template || !entry.params || !entry?.params?.[lv]) {
        return props.join("<br/>").replaceAll(/@([^@]*)@/g, (m, _index) => `<span style="color:#3ea74e">${m.slice(1, -1)}</span>`).split("<br/>")
      }
      const { params, template } = entry
      const nums = params[lv].map(x => `<span class='${LvClass(lv)}'>${x}</span>`)
      const str = formatStr(template, nums)
      return str.replaceAll(/@([^@]*)@/g, (m, _index) => `<span style="color:#3ea74e">${m.slice(1, -1)}</span>`).split("<br/>")
      }
      catch(e){
        return props.join("<br/>").replaceAll(/@([^@]*)@/g, (m, _index) => `<span style="color:#3ea74e">${m.slice(1, -1)}</span>`).split("<br/>")
      }
    }

    watch(
      () => props.eid,
      (val: ID) => {
        selectEquip.value = val ?? "";
        colspans.value = [false, true, true];
        let temp = (configStore.customize[val ?? ""] ?? [0, 0, 0]).map(
          Number
        );
        if (temp.length < 3)
          temp = [...temp, ...(new Array(3 - temp.length).fill(0))]
        selectEquipProps.value = temp
          .map((a) => {
            if (a != 0 && !entries.value.includes(a)) {
              a = 0;
            }
            return a;
          })
          .map(Number);
        temp = (configStore.stone_set[val ?? ""] ?? [0, 0, 0]).map(Number)
        if (temp.length < 3)
          temp = [0, 0, 0]
        configStore.stone_set[val ?? ""] = temp
      },
      {
        immediate: true
      }
    );

    return () => (
      <Watermark>
        <div>
          {(equInfo.value?.alternative.length ?? 0) > 0 && renderList(3, (index) => (
            <>
              <div class="mx-10px my-5px">
                <div class="flex items-center justify-between" >
                  <div class="flex items-center">
                    <div class="prop-icon"></div>
                    <div class="ml-8px text-hex-b59834">{`属性 ${index}`}</div>
                  </div>
                  {
                    index == 1 && (
                      <div class="flex">
                    <calc-button icon="reduce" disabled={configStore.stone_set[selectEquip.value][index - 1] <= 0} onClick={() => configStore.stone_set[selectEquip.value] = [0,0,0]}></calc-button>
                    <div class={`lvInfoActive`}>
                      <div class="w-12px h-14px ml-15px pt-1.5px flex items-center justify-center text-10px">
                        {configStore.stone_set[selectEquip.value][index - 1]}
                      </div>
                    </div>
                    <calc-button icon="increase" disabled={configStore.stone_set[selectEquip.value].reduce(function (prev, curr, idx, arr) { return prev + curr; }) >= 3} onClick={() => configStore.stone_set[selectEquip.value] = [3,0,0]}></calc-button>
                  </div>
                  )
                  }
                  <div onClick={() => { colspans.value[index - 1] = !colspans.value[index - 1] }} class="text-hex-3e8848 mb-2px">{!colspans.value[index - 1] ? "展开" : "折叠"}</div>
                </div>
                <div class={["transition-all", "ease-out-in", "h-auto", "overflow-hidden"].concat(!colspans.value[index - 1] ? [""] : ["max-h-0"])}>
                  {renderList(entries.value, (id: number) => (
                    <div class="flex w-100% items-center mt-1">
                      <calc-checkbox modelValue={selectEquipProps.value[index - 1] == id} key={index * 100 + id} class="!h-auto" onClick={chooseProp(id, index - 1)}>
                        {renderList(formatProps(entry(id), configStore.stone_set[selectEquip.value][index - 1]), prop => (
                          <div style="min-height: 5px;white-space: pre-wrap;" class={["ml-5px", "text-hex-b1a785"]} v-html={prop}></div>))}
                      </calc-checkbox>
                    </div>
                  ))}
                </div>
              </div>
            </>
          ))}
          {(equInfo.value?.stable.length ?? 0) > 0 && renderList(equInfo.value?.stable, (id, index) => (
            <>
              <div class="mx-10px my-5px">
                {(entry(id)?.params?.length ?? 0 > 0) && (<div class="flex items-center justify-between">
                  <div class="flex items-center">
                    <div class=" text-hex-b59834">{`属性 ${index + 1}`}</div>
                  </div>
                  {
                    index == 0 && (
                      <div class="flex">
                    <calc-button icon="reduce" disabled={configStore.stone_set[selectEquip.value][index] <= 0} onClick={() => configStore.stone_set[selectEquip.value]=[0,0,0]}></calc-button>
                    <div class={`lvInfoActive`}>
                      <div class="w-12px h-14px ml-15px pt-1.5px flex items-center justify-center text-10px">
                        {configStore.stone_set[selectEquip.value][index]}
                      </div>
                    </div>
                    <calc-button icon="increase" disabled={configStore.stone_set[selectEquip.value].reduce(function (prev, curr, idx, arr) { return prev + curr; }) >= 3} onClick={() => configStore.stone_set[selectEquip.value]=[3,0,0]}></calc-button>
                  </div>
                    )
                  }
                </div>)}
                <>{(entry(id)?.attack ?? 0) > 0 && (<div class='text-hex-b1a785 min-h-5px'>攻击强化 +{entry(id)?.attack.toFixed(1)}%</div>)}</>
                <>{(entry(id)?.buff ?? 0) > 0 && (<div class='text-hex-b1a785 min-h-5px'>增益量 {entry(id)?.buff.toFixed(0)}</div>)}</>
                <div>
                  <div key={selectEquip.value} class="w-100% items-center mt-1">
                    {renderList(formatProps(entry(id), configStore.stone_set[selectEquip.value][index]), prop => (
                      <div style="min-height: 5px;white-space: pre-wrap;" class={["text-hex-b1a785"]} v-html={(prop as string).replaceAll(/@([^@]*)@/g, (m, _index) => `<span style="color:#3ea74e">${m.slice(1, -1)}</span>`)}></div>))}
                  </div>
                </div>
              </div>
            </>
          ))}
        </div>
      </Watermark>
    );
  },
});
</script>

<style lang="scss">
.prop-icon {
  content: "";
  display: inline-block;
  width: 12px;
  height: 12px;
  background-image: url(@/assets/img/icon/switch.png);
}
</style>
