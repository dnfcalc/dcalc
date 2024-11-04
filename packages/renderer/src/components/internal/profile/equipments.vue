<script lang="tsx">
import { useVModel } from "@vueuse/core";
import type { PropType } from "vue";
import { computed, defineComponent, onMounted, renderList } from "vue";
import type { IEquipmentInfo } from "@/api/info/type";
import EquipTips from "@/components/internal/equip/eq-icon-tips.vue";
import EquipIcon from "@/components/internal/equip/eq-icon.vue";
import { useOpenWindow } from "@/hooks/open";
import {
  useBasicInfoStore,
  useCharacterStore,
  useConfigStore,
  useDetailsStore,
} from "@/store";
import type { IResultInfo } from "@/api/character/type";

interface MergeInfo {
  weaponType?: string;
  merges: ID[];
}

export default defineComponent({
  name: "Profile",
  components: { EquipTips },
  props: {
    charName: {
      type: String,
      default: null,
    },
    share: {
      type: Object as PropType<IResultInfo<"delear" | "buffer">>,
      default: undefined,
    },
    canChoose: {
      type: Boolean,
      default: false,
    },
    equList: {
      type: Array as PropType<IEquipmentInfo[]>,
      default: () => [],
    },
    fusionList: {
      type: Array as PropType<ID[]>,
      default: () => [],
    },
    // eslint-disable-next-line vue/prop-name-casing
    equips_forge: {
      type: Object,
      default: undefined,
    },
    part: {
      type: String,
      default: "",
    },
    showZF: {
      type: Boolean,
      default: true,
    },
    showTM: {
      type: Boolean,
      default: true,
    },
    tipInfo: {
      type: Array as PropType<number[]>,
      default: () => [0, 1, 2],
    },
    mergeInfo: {
      type: Object as PropType<MergeInfo>,
    },
    showTips: {
      type: Boolean,
      default: true,
    },
    withBG: {
      type: Boolean,
      default: true,
    },
    showSpe:{
      type: Boolean,
      default: true
    }
  },
  emits: ["partChange"],
  setup(props, { emit }) {
    const partModelValue = useVModel(props, "part", emit, { passive: true });

    const configStore = useConfigStore();
    const characterStore = useCharacterStore();
    const detailsStore = useDetailsStore();
    const basicStore = useBasicInfoStore();
    const display_parts = detailsStore.display_parts;
    const openUrl = useOpenWindow();

    const equips_forge = function (index: string) {
      const limit = getEqu(index).rarity == "传说" ? 80 : 80;
      // console.log(props.equips_forge)
      const infos = configStore.forge_set[index];
      const details = basicStore.details;
      if (!infos || !details) {
        return undefined;
      }

      let growth_first =
        getEqu(index).rarity == "传说"
          ? Math.min(limit, infos.get("growth_cs_first") ?? 1)
          : Math.min(limit, infos.get("growth_first") ?? 1);
      let growth_second =
        getEqu(index).rarity == "传说"
          ? Math.min(limit, infos.get("growth_cs_second") ?? 1)
          : Math.min(limit, infos.get("growth_second") ?? 1);
      let growth_third =
        getEqu(index).rarity == "传说"
          ? Math.min(limit, infos.get("growth_cs_third") ?? 1)
          : Math.min(limit, infos.get("growth_third") ?? 1);
      let growth_fourth =
        getEqu(index).rarity == "传说"
          ? Math.min(limit, infos.get("growth_cs_fourth") ?? 1)
          : Math.min(limit, infos.get("growth_fourth") ?? 1);
      let growth_sj =
        getEqu(index).rarity == "传说"
          ? 0
          : Math.min(60, infos.get("growth_sj") ?? 0);

      if (
        getEqu(index).name.startsWith("霜 :") ||
        getEqu(index).name.startsWith("雨 :") ||
        getEqu(index).name.startsWith("雷 :") ||
        getEqu(index).name.startsWith("风 :") ||
        getEqu(index).name.startsWith("焰 :") ||
        getEqu(index).name.startsWith("失衡 :")
      ) {
        growth_first = 80;
        growth_second = 80;
        growth_third = 80;
        growth_fourth = 80;
        growth_sj = 40;
      }
      if (getEqu(index).name.startsWith("跨越之忆")) {
        growth_first = 70;
        growth_second = 70;
        growth_third = 70;
        growth_fourth = 70;
        growth_sj = 0;
      }

      const cursed_type = infos.get("cursed_type") ?? 1;
      const cursed_number = infos.get("cursed_number") ?? 0;
      const dz_number = infos.get("dz_number") ?? 0;
      const enchanting_id = infos.get("enchanting") ?? 0;
      const enchanting = details.enchanting
        .find((e) => e.id == enchanting_id)
        ?.props.split("|");
      const socket_left = infos.get("socket_left") ?? 0;
      const socket_right = infos.get("socket_right") ?? 0;
      const socket = [
        details.emblem.find((e) => e.id == socket_left)?.props,
        details.emblem.find((e) => e.id == socket_right)?.props,
      ];

      return {
        info: {
          成长词条等级: [
            growth_first + growth_sj,
            growth_second + growth_sj,
            growth_third + growth_sj,
            growth_fourth + growth_sj,
          ],
          // 1增幅 2强化
          强化类型: cursed_type,
          强化数值: cursed_number,
          锻造数值: dz_number,
          附魔: enchanting,
          徽章: socket,
          tips: (props.equips_forge?.[index]?.tips ?? []) as string[],
        },
        data: props.equips_forge?.[index],
        show: [
          props.tipInfo.includes(0),
          props.tipInfo.includes(1),
          props.tipInfo.includes(2),
        ],
      };
    };

    const openShare = () => {
      const res = props.share;
      if (!res) {
        return;
      }

      res.merge = props.mergeInfo;
      res.merge_list = configStore.merge;
      res.fusion_list = props.fusionList as number[];
      res.customize = configStore.customize;
      res.specificity = configStore.specificity;
      (res as any).talisman_set = configStore.talisman_set;
      (res as any).rune_set = configStore.rune_set;
      res.equips = props.equList;
      sessionStorage.setItem(res.id?.toString() ?? "", JSON.stringify(res));
      openUrl(`/share?res=${props.share?.id}`, { width: 405, height: 635 });
    };

    function currentInfo(part: string) {
      if (["称号", "宠物"].includes(part)) {
        return "";
      }
      let num = configStore.getForge(part, "cursed_number") ?? 0;
      if (getEqu(part)?.type == "智慧产物") {
        num = configStore.getForge(part, "wisdom_number") ?? 0;
      }
      return `+${num}`;
    }

    onMounted(() => {
      !basicStore.entry_list && basicStore.loadEntries();
      !basicStore.equipment_info && basicStore.loadEquips();
    });

    function currentFusion(part: string) {
      if (part == "武器") {
        let temp;
        if (
          props.mergeInfo?.weaponType &&
          (props.mergeInfo?.merges.map(Number).filter((a) => a > 0) ?? [])
            .length > 0
        ) {
          temp = basicStore.equipment_info?.merge?.filter(
            (a) => a.type == props.mergeInfo?.weaponType
          )?.[0];
        }
        return temp;
      } else {
        return basicStore.equipment_info?.fusion
          .filter((a) => a.part == part)
          ?.filter((a) => props.fusionList.includes(Number(a.id)))?.[0];
      }
    }

    function upgrade(part: string) {
      return computed(() => {
        return {
          fusion_upgrade: configStore.getForge(part, "fusion_upgrade") ?? false,
          upgrade: configStore.getForge(part, "growth_sj") > 0 ?? false,
        };
      });
    }

    function currentFusionPPs(part: string) {
      if (part == "武器") {
        let temp;
        if (
          props.mergeInfo?.weaponType &&
          (props.mergeInfo?.merges.map(Number).filter((a) => a > 0) ?? [])
            .length > 0
        ) {
          const customs = props.mergeInfo?.merges;
          temp = [];
          customs?.forEach((index) => {
            temp.push(basicStore.entry_list?.[index?.toString() ?? ""]);
          });
        }
        return temp;
      } else {
        const id = basicStore.equipment_info?.fusion
          .filter((a) => a.part == part)
          ?.filter((a) => props.fusionList.includes(Number(a.id)))?.[0]?.id;
        if (id) {
          const customs = configStore.customize[id];
          const temp: any = [];
          customs?.forEach((index) => {
            temp.push(basicStore.entry_list?.[index.toString()]);
          });
          return temp.slice(0, 3);
        } else {
          return [];
        }
      }
    }

    function infoStyle(part: string) {
      let x = 28;
      let y = 5;
      let index = display_parts.findIndex((p) => p == part);
      let type = configStore.getForge(part, "cursed_type");
      if (getEqu(part)?.type == "智慧产物") {
        type = 3;
      }
      if (index == 13) {
        index -= 7;
      } else if (index >= 5 && index <= 12) {
        x += 179;
        index -= 5;
      }

      x += (index % 2) * 39;
      y += Math.floor(index / 2) * 34;

      const num = configStore.getForge(part, "cursed_number");

      const style = {
        display: num == 0 && type == 2 ? "none" : "",
        left: `${x}px`,
        top: `${y}px`,
        zIndex: 6,
        color: type == 2 ? "#19C7EA" : type == 3 ? "orange" : "#E458A9",
        fontWeight: 900,
        // backgroundColor: "rgba(0,0,0,0.5)"
      };

      return style;
    }

    function partIconStyle(part: string) {
      let x = 11;
      let y = 11;
      let index = display_parts.findIndex((p) => p == part);

      if (index >= 5 && index <= 12) {
        x += 179;
        index -= 5;
      }

      if (index == 13) {
        index = 5;
      }

      x += (index % 2) * 39;
      y += Math.floor(index / 2) * 34;

      return {
        left: `${x}px`,
        top: `${y}px`,
        zIndex: 3,
      };
    }

    function fusionStyle(part: string) {
      let x = 0;
      let y = 20;
      let index = display_parts.findIndex((p) => p == part);

      if (index >= 5 && index <= 12) {
        x += 179;
        index -= 5;
      }

      if (index == 13) {
        index = 5;
      }

      x += (index % 2) * 39;
      y += Math.floor(index / 2) * 34;

      return {
        left: `${x}px`,
        top: `${y}px`,
        zIndex: 5,
        transform: "scale(0.6)",
      };
    }

    function setPart(part: string) {
      return () => {
        if (!props.canChoose) {
          return;
        }
        // activeIndex.value = index
        partModelValue.value = part;
        emit("partChange", part);
      };
    }

    function getEqu(part: string) {
      return props.equList.filter((item) => item.part == part)[0] ?? undefined;
    }

    function getEquCustom(part: string) {
      const id = (
        props.equList.filter((item) => item.part == part)[0] ?? undefined
      ).id;
      if (id) {
        const customs = configStore.customize[id.toString()];
        const temp: any = [];
        customs?.forEach((index) => {
          temp.push(basicStore.entry_list?.[index.toString()]);
        });
        return temp;
      } else {
        return [];
      }
    }

    const specificity = computed(() => {
      const keys = Object.keys(configStore.specificity);
      if (keys.length == 0) {
        return -1;
      }
      return Math.floor(
        (Number.parseInt(Object.keys(configStore.specificity)?.[0] ?? "20000") -
          20000) /
          100
      );
    });

    const infos = computed(
      () =>
        (characterStore.especificity ?? []).find(
          (a) => a.type == specificity.value
        )?.detail ?? []
    );


    const colors = [
    "#03a9f4",
    "#f44336",
    "#4caf50",
    "#ffc107"

    ];

    return () => {
      return (
        <div
          class="char-back"
          style={props.withBG ? "" : "background:none;border:none"}
        >
          <div
            class={props.withBG ? "head common-icon-head" : "head"}
            style={`position:relative;${
              props.withBG ? "" : "background:none;border:none"
            }`}
          >
            {props.showSpe && specificity.value >= 0 && (
              <div
                class="flex items-center justify-center"
                style="position: absolute;bottom:10px;left:10px;z-index:10"
              >
                <div class="flex flex-wrap spe" style="">
                  {renderList(infos.value, (item) => {
                    return <>
                    <div style={`position:absolute;left:${item.x * 12 + 10 - 8}px;top:${item.y * 15 + 10 - 2.5}px;background-color:${
                      configStore.specificity[item.id] ? colors[specificity.value] : "#404040"
                    }`} class="flex flex-col ml-2px items-center w-8px h-8px"></div></>;
                  })}
                </div>
              </div>
            )}
            <div
              class="flex h-170px w-266px char"
              style="position: absolute;z-index:3"
            >
              <div>
                <div class="flex items-center justify-center text-hex-9CEC9E flex-1">
                  纸飞机计算器
                </div>
                <div>[{characterStore.name}]</div>
              </div>
              {renderList(display_parts, (part) => (
                <>
                  {props.showZF && (
                    <div
                      onClick={setPart(part)}
                      class="absolute"
                      style={infoStyle(part)}
                    >
                      {currentInfo(part)}
                    </div>
                  )}
                  <div
                    onClick={setPart(part)}
                    class="absolute "
                    style={partIconStyle(part)}
                  >
                    <div class="h-full w-full relative overflow-hidden">
                      {getEqu(part) ? (
                        <EquipTips
                          hightlight={part == partModelValue.value}
                          class="h-full w-full"
                          forge={equips_forge(part)}
                          eq={getEqu(part)}
                          pps={getEquCustom(part)}
                          canClick={false}
                          show-tips={props.showTips}
                          style={
                            (equips_forge(part)?.info?.tips?.length ?? 0) > 0
                              ? "filter:grayscale(100%)"
                              : ""
                          }
                        ></EquipTips>
                      ) : (
                        <EquipIcon hightlight={part == partModelValue.value} />
                      )}
                    </div>
                  </div>
                  {props.showTM && currentFusion(part) && (
                    <div
                      onClick={setPart(part)}
                      class="absolute"
                      style={fusionStyle(part)}
                    >
                      <div class="h-full w-full relative overflow-hidden">
                        {
                          <EquipTips
                            hightlight={false}
                            class="h-full w-full"
                            merges={currentFusionPPs(part)}
                            eq={currentFusion(part)}
                            canClick={false}
                            show-tips={props.showTips}
                            forge={upgrade(part).value}
                          ></EquipTips>
                        }
                      </div>
                    </div>
                  )}
                </>
              ))}
            </div>
            <div class="h-150px w-266px common-icon-equ-back"></div>
            {props.share && (
              <div
                style="width:10px;height:20px;position: absolute;top:150px;right:5px;z-index:10"
                onClick={openShare}
                class="icon-detail"
              ></div>
            )}

            <div
              class={`character-icon-${characterStore.alter}-profile h-170px`}
              style="position: absolute;bottom: 10px;z-index: 1;"
            ></div>
          </div>
        </div>
      );
    };
  },
});
</script>

<style lang="scss">
.spe {
  display: flex;
  flex-wrap: wrap;
  width: 45px;
  height: 58px;
  justify-content: center;
  align-items: center;
  padding: 3px;
  border: 1px solid #404040;
  zoom: 0.6;
  background-color: black;

  .item {
    width: 6px;
    height: 6px;
    margin: 1px;
  }
}

.char-back {
  background-color: rgba(0, 0, 0, 0.75);
  border-left: 1px solid rgba(255, 255, 255, 0.1);
  border-right: 1px solid rgba(255, 255, 255, 0.1);

  .head {
    background-repeat: no-repeat;
    height: 177px;
    display: flex;
    justify-content: center;
    // background-color: rgba(0, 0, 0, 0.8);
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);

    .char {
      display: flex;
      justify-content: center;
      align-items: flex-end;
      color: white;
    }
  }
}
</style>
