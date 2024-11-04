<script lang="tsx">
import type { CSSProperties, PropType } from "vue";
import { computed, defineComponent, ref, renderList } from "vue";
import EquipTips from "@/components/internal/equip/eq-icon-tips.vue";
import { useCharacterStore, useGlobalStore } from "@/store";
import { to_percent } from "@/utils";

interface DelearProperties {
  技能攻击力: number
  面板技能攻击力: number
  攻击强化: number
  百分比攻击强化: number
  MP消耗量: number
  伤害比例: number[]
  伤害系数: number[]
  无色消耗: number
  攻击速度: number
  其他攻击速度: number
  施放速度: number
  移动速度: number
  出血抗性: number
  中毒抗性: number
  灼伤抗性: number
  感电抗性: number
  冰冻抗性: number
  减速抗性: number
  眩晕抗性: number
  诅咒抗性: number
  失明抗性: number
  石化抗性: number
  睡眠抗性: number
  混乱抗性: number
  束缚抗性: number
  cdr: [string, number]
  冷却缩减: number
  冷却恢复: number
  技能范围: number
  "技能范围∏": number
  保护罩: number
  era: number
  defense: number
  defense_ratio: number
  hurted_ratio: number
}

interface BufferProperties {
  buffer_power: number
  buffer_power_value: number
  buffer_power_per: number
  buff_name: string
  buff_level: number
  awake_name: string
  awake_level: number
  apply_value: number
}

interface IDetail {
  name?: string
  alter?: string

  fame?: number

  站街?: {
    智力?: number
    力量?: number
    体力?: number
    精神?: number
    物理攻击?: number
    魔法攻击?: number
    独立攻击?: number
    火?: number
    冰?: number
    光?: number
    暗?: number
    火抗?: number
    冰抗?: number
    光抗?: number
    暗抗?: number
  }
  jintu?: {
    智力?: number
    力量?: number
    物理攻击?: number
    魔法攻击?: number
    独立攻击?: number
    火?: number
    冰?: number
    光?: number
    暗?: number
    火抗?: number
    冰抗?: number
    光抗?: number
    暗抗?: number
  }
  properties?: DelearProperties & BufferProperties
  buffer_addition: [number, number, number, number]
}

enum ICONS {
  "力量",
  "智力",
  "物理攻击",
  "魔法攻击",
  "物理暴击",
  "魔法暴击",
  "攻击速度",
  "施放速度",
  "移动速度",
  "命中率",
  "独立攻击",
  "攻击属性",
  "体力",
  "精神"
}

export default defineComponent({
  name: "Detail",
  components: { EquipTips },
  props: {
    showCD: {
      type: Boolean,
      default: true
    },
    withStandard:{
      type: Boolean,
      default: false
    },
    details: {
      type: Object as PropType<IDetail>,
      default: () => {
        return {
          fame: 0,
          站街: {
            火: 0,
            冰: 0,
            光: 0,
            暗: 0,
            火抗: 0,
            冰抗: 0,
            光抗: 0,
            暗抗: 0
          },
          role: "delear",
          properties: {
            技能攻击力: 0,
            攻击强化: 0,
            百分比攻击强化: 0,
            MP消耗量: 0,
            伤害比例: [1, 0, 0, 0, 0],
            伤害系数: [1, 1, 1, 1, 1]
          },
          buffer_addition: [0, 0, 0, 0]
        };
      }
    },
    role: {
      type: String as PropType<"delear" | "buffer">,
      default: () => "delear"
    },
    totalData: {
      type: Array as PropType<number[]>,
      default: () => {
        return [0];
      }
    },
    standardData: {
      type: Array as PropType<number[]>,
      default: () => {
        return [0];
      }
    },
    showSubDetail: {
      type: Boolean,
      default: true
    }
  },
  setup(props) {
    // let details = props.details as IDetail

    const details = computed(() => (props.details as IDetail) ?? undefined);
    const globalStore = useGlobalStore()
    // details.站街 = {
    //   火: 999,
    //   冰: 999,
    //   光: 999,
    //   an: 999
    // }

    const current_data = computed(() => props.totalData?.[0] ?? 0);
    const standard_data = computed(() => props.standardData?.[0] ?? 0);
    // const globalStore = useGlobalStore()

    const result = computed(() => {
      const current = current_data.value;
      const standard = standard_data.value;

      if(props.withStandard && !standard) {
        return [" -- ", "white"];
      }

      if (current) {
        if (standard) {
          return current == standard
            ? ["无变化", "white"]
            : [
                to_percent(current / standard - 1, 0, "%", true),
                current > standard ? "#3ea74e" : "red"
              ];
        }
        if (props.role == "buffer") {
          return [to_percent(current / 100, 0, "%", true), "green"];
        }
        return [current.round(0).toLocaleString(), "white"];
      }
      return [" -- ", "white"];
    });

    const characterStore = useCharacterStore();
    const skill_cd = ref(0);

    const triggerRef = ref<HTMLElement>();

    const showCDR = ref(false);

    // 下拉框位置
    const dropdownStyle = computed<CSSProperties>(() => {
      let x = 0;
      let t = 0;
      if (triggerRef.value) {
        const { width, left, top } = triggerRef.value.getBoundingClientRect();
        x = left + width;
        t = top;
      }

      return {
        left: `${x + 2}px`,
        top: `${t - 80}px`,
        width: "200px",
        height: "390px",
        position: "absolute",
        overflow: "hidden",
        backgroundColor: "rgba(0, 0, 0, 0.6)",
        zIndex: 5,
        border: "1px solid rgba(255, 255, 255, 0.1)",
        borderRadius: "5px"
      };
    });

    function get_skill_cd() {
      if (skill_cd.value >= 0) {
        const item = details.value?.properties?.cdr?.[skill_cd.value];
        if (item) {
          return (
            <div
              class={
                item[1] > 0
                  ? "text-hex-3ea74e"
                  : item[1] == 0
                    ? "text-hex-5b5b5b"
                    : "text-hex-ff0000"
              }
            >
              {item[2]?.toFixed(1)}s [{(item[1] * 100).toFixed(1)}%]
            </div>
          );
        }
      } else {
        return <div></div>;
      }
    }

    function renderDelearProperties() {
      const properties = details.value?.properties;
      const town = details.value?.站街;
      if (!properties || !town) {
        return [];
      }

      return (
        <>
          <div class="details" ref={triggerRef}>
            {town.力量 && (
              <div class="de-item !pl-0 ">
                <div class="flex items-center">
                  <div class="w-15px h-15px flex items-center justify-center">
                    <div class={`common-icon-${ICONS.力量}`} />
                  </div>
                  <div class="text-hex-836832 name">力量</div>
                </div>
                <div class="text-hex-3ea74e">
                  {details.value?.站街?.力量?.toFixed(0)}
                </div>
              </div>
            )}
            {town.智力 && (
              <div class="de-item  !pl-0">
                <div class="flex items-center">
                  <div class="w-15px h-15px flex items-center justify-center">
                    <div class={`common-icon-${ICONS.智力}`} />
                  </div>
                  <div class="text-hex-836832 name">智力</div>
                </div>
                <div class="text-hex-3ea74e">
                  {details.value?.站街?.智力?.toFixed(0)}
                </div>
              </div>
            )}

            {town.物理攻击 && (
              <div class="de-item  !pl-0">
                <div class="flex items-center">
                  <div class="w-15px h-15px flex items-center justify-center">
                    <div class={`common-icon-${ICONS.物理攻击}`} />
                  </div>
                  <div class="text-hex-836832 name">物理攻击</div>
                </div>
                <div class="text-hex-3ea74e">
                  {details.value?.站街?.物理攻击?.toFixed(0)}
                </div>
              </div>
            )}

            {town.魔法攻击 && (
              <div class="de-item  !pl-0">
                <div class="flex items-center">
                  <div class="w-15px h-15px flex items-center justify-center">
                    <div class={`common-icon-${ICONS.魔法攻击}`} />
                  </div>
                  <div class="text-hex-836832 name">魔法攻击</div>
                </div>
                <div class="text-hex-3ea74e">
                  {details.value?.站街?.魔法攻击?.toFixed(0)}
                </div>
              </div>
            )}

            {town.独立攻击 && (
              <div class="de-item  !pl-0">
                <div class="flex items-center">
                  <div class="w-15px h-15px flex items-center justify-center">
                    <div class={`common-icon-${ICONS.独立攻击}`} />
                  </div>
                  <div class="text-hex-836832 name">独立攻击</div>
                </div>
                <div class="text-hex-3ea74e">
                  {details.value?.站街?.独立攻击?.toFixed(0)}
                </div>
              </div>
            )}

            <div class="w-100% de-item !pl-0">
              <div class="flex items-center">
                <div class="w-15px h-15px flex items-center justify-center">
                  <div class={`common-icon-${ICONS.攻击属性}`} />
                </div>
                <div class="text-hex-836832 name">攻击属性</div>
              </div>
              <div class="text-hex-3ea74e">{`火(${details.value?.站街?.火?.toFixed(
                0
              )})/冰(${details.value?.站街?.冰?.toFixed(
                0
              )})/光(${details.value?.站街?.光?.toFixed(
                0
              )})/暗(${details.value?.站街?.暗?.toFixed(0)})`}</div>
            </div>
          </div>
          <div class="details">
            <calc-tooltip class="de-item" position="bottom">
              {{
                default() {
                  return (
                    <>
                      <div class="text-hex-836832">
                        技能伤害
                      </div>
                      <div class="text-hex-3ea74e">{`${(
                        properties.面板技能攻击力 ?? 0
                      ).toFixed(2)}%`}</div>
                    </>
                  );
                },
                popper() {
                  return (
                    <div class="text-white py-1 px-2">{`实际技能攻击力:${`${properties.技能攻击力?.toFixed(
                      2
                    )}%`}`}</div>
                  );
                }
              }}
            </calc-tooltip>
            {(properties.伤害比例?.[0] ?? 1) > 0 && (
              <div class="de-item">
                <div class=" text-hex-836832">直伤</div>
                <div class="text-hex-3ea74e">{`${(
                  (properties.伤害比例?.[0] ?? 1) * 100
                ).toFixed(0)}%`}</div>
              </div>
            )}
            <div class="de-item">
              <div class="text-hex-836832">攻强</div>
              <div class="text-hex-3ea74e">{`${
                properties.攻击强化?.toFixed(1)
              }%(${properties.百分比攻击强化}%)`}</div>
            </div>
            {/* <div class="de-item">
              <div class=" text-hex-836832">攻击强化%</div>
              <div class="text-hex-3ea74e">{`${properties.百分比攻击强化?.toFixed(2)}%`}</div>
            </div> */}
            {
              //   <div class="de-item">
              //   <div class=" text-hex-836832">无色消耗</div>
              //   <div class="text-hex-3ea74e">{properties.无色消耗}</div>
              // </div>
            }
            <div class="de-item">
              <div class=" text-hex-836832">MP消耗量%</div>
              <div class="text-hex-3ea74e">{`${properties.MP消耗量?.toFixed(
                2
              )}%`}</div>
            </div>
            <div class="de-item">
              <div class="text-hex-836832">技能范围</div>
              <div class="text-hex-3ea74e">{`${(
                properties.技能范围 * 100
              ).toFixed(0)}%[${(
                properties["技能范围∏"] * 100 - 100
              ).toFixed(0)}%]`}</div>
            </div>
            {properties.保护罩 > 0 && (
              <div class="de-item">
                <div class=" text-hex-836832">保护罩</div>
                <div class="text-hex-3ea74e">{`${(
                  properties.保护罩 * 100
                ).toFixed(2)}%`}</div>
              </div>
            )}
            <calc-tooltip class="de-item" position="bottom">
              {{
                default() {
                  return (
                    <>
                      <div class="text-hex-836832">装备CD减少</div>
                      <div class="text-hex-3ea74e">{`${(
                        (1 - properties.冷却缩减 / (1 + properties.冷却恢复))
                        * 100
                      )?.toFixed(2)}%`}</div>
                    </>
                  );
                },
                popper() {
                  return (
                    <>
                      <div class="text-white pt-1  px-2">
                        仅统计Lv1~100技能冷却缩减/恢复
                      </div>
                      <div class="text-white px-2">{`技能冷却缩减:${(
                        100
                        - properties.冷却缩减 * 100
                      )?.toFixed(2)}%`}</div>
                      <div class="text-white pb-1 px-2">{`技能冷却恢复:${(
                        properties.冷却恢复 * 100
                      )?.toFixed(2)}%`}</div>
                    </>
                  );
                }
              }}
            </calc-tooltip>
            <calc-tooltip class="de-item" position="bottom">
              {{
                default() {
                  return (
                    <>
                      <div class="text-hex-836832">装备防御率</div>
                      <div class="text-hex-3ea74e">{`${(
                        properties.era
                      )?.toFixed(2)}%`}</div>
                    </>
                  );
                },
                popper() {
                  return (
                    <>
                      <div class="text-white pt-1  px-2">
                        仅统计装备提供的相关防御
                      </div>
                      <div class="text-white px-2">{`防御力:${(
                        properties.defense
                      ).toFixed(0)}(+${(properties.defense_ratio * 100)?.toFixed(0)}%)`}</div>
                      <div class="text-white pb-1 px-2">{`所受伤害减少量:${(
                        properties.hurted_ratio * 100
                      )?.toFixed(0)}%`}</div>
                    </>
                  );
                }
              }}
            </calc-tooltip>
            <div class="w-100% de-item !pl-0">
              <div class="flex items-center w-65px">
                <div class="ml-5px text-hex-836832 name">装备速度</div>
              </div>
              <div class="text-hex-3ea74e flex flex-1 items-center justify-between">
                <div class="flex flex-1 items-center justify-around">
                  <div class="w-15px h-15px flex items-center justify-center">
                    <div class={`common-icon-${ICONS.攻击速度}`} />
                  </div>
                  <div>{`${(
                    properties.攻击速度 * 100
                  ).toFixed(2)}%`}</div>
                  <div>{`(+${
                    (properties.其他攻击速度 * 100
                    ).toFixed(0)
                  }%)`}</div>
                </div>
                <div class="flex flex-1 items-center justify-around">
                  <div class="w-15px h-15px flex items-center justify-center">
                    <div class={`common-icon-${ICONS.施放速度}`} />
                  </div>
                  <div>{`${(
                    properties.施放速度 * 100
                  ).toFixed(2)}%`}</div>
                </div>
                <div class="flex flex-1 items-center justify-around">
                  <div class="w-15px h-15px flex items-center justify-center">
                    <div class={`common-icon-${ICONS.移动速度}`} />
                  </div>
                  <div>{`${(
                    properties.移动速度 * 100
                  ).toFixed(2)}%`}</div>
                </div>

              </div>
            </div>
          </div>
          <div class="details">
            {renderList(["中毒", "灼伤", "感电", "出血"], (item, index) =>
              (
                <div class="de-item">
                  <div class=" text-hex-836832">{item}伤害</div>
                  <div
                    class={
                      (properties.伤害比例?.[index + 1] ?? 0) == 0
                        ? "text-hex-5b5b5b"
                        : "text-hex-3ea74e"
                    }
                  >{`${((properties.伤害比例?.[index + 1] ?? 0) * 100).toFixed(
                      0
                    )}%(+${(
                      (properties.伤害系数?.[index + 1] ?? 0) * 100
                    ).toFixed(0)}%)`}</div>
                </div>
              )
            )}
          </div>
          {props.showSubDetail && (
            <div class="details">
              <div class="w-100% de-item !pl-0">
                <div class="flex items-center">
                  <div class="ml-5px text-hex-836832 name">属性抗性</div>
                </div>
                <div class="text-hex-3ea74e">{`火(${details.value?.站街?.火抗?.toFixed(
                  0
                )})/冰(${details.value?.站街?.冰抗?.toFixed(
                  0
                )})/光(${details.value?.站街?.光抗?.toFixed(
                  0
                )})/暗(${details.value?.站街?.暗抗?.toFixed(0)})`}</div>
              </div>
              {renderList(
                [
                  "出血",
                  "中毒",
                  "灼伤",
                  "感电",
                  "",
                  "",
                  "冰冻",
                  "减速",
                  "眩晕",
                  "诅咒",
                  "失明",
                  "石化",
                  "睡眠",
                  "混乱",
                  "束缚"
                ],
                (item) => {
                  if (item == "") {
                    return <div class="w-33.33% de-item !min-w-33.33%"></div>;
                  }
                  const num = properties[`${item}抗性`] ?? 0;
                  return (
                    <div class="w-33.33% de-item !min-w-33.33%">
                      <div class="text-hex-836832">{item}</div>
                      <div
                        class={
                          num > 0
                            ? "text-hex-3ea74e"
                            : num == 0
                              ? "text-hex-5b5b5b"
                              : "text-hex-ff0000"
                        }
                      >{`${num?.toFixed(2)}%`}</div>
                    </div>
                  );
                }
              )}
            </div>
          )}
          {props.showCD && (<div class="my-4px mx-5px flex items-center">
            <div class="w-25% flex text-hex-e9c558">
              技能冷却
              <calc-iconselect
                class="talisman"
                emptyLabel="冷却"
                columnNum={Math.min(
                  Math.round((properties?.cdr ?? []).length / 2),
                  10
                )}
                v-model={skill_cd.value}
              >
                {renderList(
                  (properties?.cdr ?? []).map((a) => a[0]) ?? [],
                  (a, index) => (
                    <calc-option value={index}>
                      <div
                        class={`character-icon-${
                          characterStore.alter
                        }-${a.replace(/[().·，：]+/g, "")}`}
                      />
                    </calc-option>
                  )
                )}
              </calc-iconselect>
            </div>
            {/*
              <calc-select v-model={skill_cd.value} class="!w-40%">
                {renderList((properties?.cdr ?? []).map(a => a[0]) ?? [], (a, index) => (
                  <calc-option value={index}>{a}</calc-option>
                ))}
              </calc-select> */}
            <div class="!w-35% flex items-center justify-center">
              {get_skill_cd()}
            </div>
            <calc-button
              class="h-20px !w-40%"
              onClick={() => (showCDR.value = !showCDR.value)}
            >
              技能冷却详情
            </calc-button>
          </div>)}
          <div style={dropdownStyle.value} v-show={showCDR.value}>
            <div style="background-color: rgba(0, 0, 0, 0.5);margin:5px;border:1px solid rgba(255, 255, 255, 0.1);overflow-y: auto;height:378px">
              <div class="w-full text-center text-hex-B29632 my-5px">
                技能冷却缩减情况
              </div>
              {renderList(properties?.cdr, (item) => (
                <div class="flex items-center justify-between mx-5px my-5px">
                  <div
                    class={`character-icon-${
                      characterStore.alter
                    }-${item[0].replace(/[().·，：]+/g, "")}`}
                  />
                  <div class="text-hex-b1a785">{item[2].toFixed(1)}s</div>
                  <div
                    class={
                      item[1] > 0
                        ? "text-hex-3ea74e"
                        : item[1] == 0
                          ? "text-hex-5b5b5b"
                          : "text-hex-ff0000"
                    }
                  >
                    {(item[1] * 100).toFixed(1)}%
                  </div>
                </div>
              ))}
            </div>
          </div>
        </>
      );
    }

    function renderBufferProperties() {
      if (!details.value) {
        return [];
      }
      const properties = details.value?.properties;
      const town = details.value.站街;
      if (!properties || !town) {
        return [];
      }

      return (
        <>
          <div class="details" ref={triggerRef}>
            {town.智力 && (
              <calc-tooltip class="de-item" position="bottom">
                {{
                  default() {
                    return (
                      <>
                        <div class="flex items-center">
                          <div class="w-15px h-15px flex items-center justify-center">
                            <div class={`common-icon-${ICONS.智力}`} />
                          </div>
                          <div class="text-hex-836832 name">智力</div>
                        </div>
                        <div class="text-hex-3ea74e">
                          {town.智力?.toFixed(0)}
                        </div>
                      </>
                    );
                  },
                  popper() {
                    return (
                      <div class="text-white py-1 px-2">{`适用数值:${properties.apply_value}`}</div>
                    );
                  }
                }}
              </calc-tooltip>
            )}

            {town.体力 && (
              <calc-tooltip class="de-item" position="bottom">
                {{
                  default() {
                    return (
                      <>
                        <div class="flex items-center">
                          <div class="w-15px h-15px flex items-center justify-center">
                            <div class={`common-icon-${ICONS.体力}`} />
                          </div>
                          <div class="text-hex-836832 name">体力</div>
                        </div>
                        <div class="text-hex-3ea74e">
                          {town.体力?.toFixed(0)}
                        </div>
                      </>
                    );
                  },
                  popper() {
                    return (
                      <div class="text-white py-1 px-2">{`适用数值:${properties.apply_value}`}</div>
                    );
                  }
                }}
              </calc-tooltip>
            )}

            {town.精神 && (
              <calc-tooltip class="de-item" position="bottom">
                {{
                  default() {
                    return (
                      <>
                        <div class="flex items-center">
                          <div class="w-15px h-15px flex items-center justify-center">
                            <div class={`common-icon-${ICONS.精神}`} />
                          </div>
                          <div class="text-hex-836832 name">精神</div>
                        </div>
                        <div class="text-hex-3ea74e">
                          {town.精神?.toFixed(0)}
                        </div>
                      </>
                    );
                  },
                  popper() {
                    return (
                      <div class="text-white py-1 px-2">{`适用数值:${properties.apply_value}`}</div>
                    );
                  }
                }}
              </calc-tooltip>
            )}

            <calc-tooltip class="de-item" position="bottom">
              {{
                default() {
                  return (
                    <>
                      <div class="text-hex-836832">增益量</div>
                      <div class="text-hex-3ea74e">
                        {properties.buffer_power?.round(0)}
                      </div>
                    </>
                  );
                },
                popper() {
                  return (
                    <div class="text-white py-1 px-2">{`增益量:${properties.buffer_power_value}(+${properties.buffer_power_per}%)`}</div>
                  );
                }
              }}
            </calc-tooltip>
            <calc-tooltip position="bottom" class="de-item">
              {{
                default() {
                  return (
                    <>
                      <div class=" text-hex-836832">Buff技能等级</div>
                      <div class="text-hex-3ea74e">{properties.buff_level}</div>
                    </>
                  );
                }
                // popper() {
                //   return (
                //     <div class="text-white py-1 px-2">
                //       <div>{`${properties.buff_name} Lv.${properties.buff_level}`}</div>
                //     </div>
                //   )
                // }
              }}
            </calc-tooltip>
            <calc-tooltip position="bottom" class="de-item">
              {{
                default() {
                  return (
                    <>
                      <div class=" text-hex-836832">觉醒技能等级</div>
                      <div class="text-hex-3ea74e">
                        {properties.awake_level}
                      </div>
                    </>
                  );
                }
              }}
            </calc-tooltip>
            <div class="de-item">
              <div class=" text-hex-836832">力智加成</div>
              <div class="text-hex-3ea74e">{props.totalData[2]?.round(0)}</div>
            </div>
            <div class="de-item">
              <div class=" text-hex-836832">三攻加成</div>
              <div class="text-hex-3ea74e">{props.totalData[3]?.round(0)}</div>
            </div>
            <calc-tooltip class="de-item" position="bottom">
              {{
                default() {
                  return (
                    <>
                      <div class="text-hex-836832">装备CD减少</div>
                      <div class="text-hex-3ea74e">{`${(
                        (1 - properties.冷却缩减 / (1 + properties.冷却恢复))
                        * 100
                      ).toFixed(2)}%`}</div>
                    </>
                  );
                },
                popper() {
                  return (
                    <>
                      <div class="text-white pt-1 px-2">
                        仅统计Lv1~100技能冷却缩减/恢复
                      </div>
                      <div class="text-white px-2">{`技能冷却缩减:${(
                        100
                        - properties.冷却缩减 * 100
                      ).toFixed(2)}%`}</div>
                      <div class="text-white pb-1 px-2">{`技能冷却恢复:${(
                        properties.冷却恢复 * 100
                      ).toFixed(2)}%`}</div>
                    </>
                  );
                }
              }}
            </calc-tooltip>
            <calc-tooltip class="de-item" position="bottom">
              {{
                default() {
                  return (
                    <>
                      <div class="text-hex-836832">装备防御率</div>
                      <div class="text-hex-3ea74e">{`${(
                        properties.era
                      )?.toFixed(2)}%`}</div>
                    </>
                  );
                },
                popper() {
                  return (
                    <>
                      <div class="text-white pt-1  px-2">
                        仅统计装备提供的相关防御
                      </div>
                      <div class="text-white px-2">{`防御力:${(
                        properties.defense
                      ).toFixed(0)}(+${(properties.defense_ratio * 100)?.toFixed(0)}%)`}</div>
                      <div class="text-white pb-1 px-2">{`所受伤害减少量:${(
                        properties.hurted_ratio * 100
                      )?.toFixed(0)}%`}</div>
                    </>
                  );
                }
              }}
            </calc-tooltip>
            <div class="de-item">
              <div class="text-hex-836832">技能范围</div>
              <div class="text-hex-3ea74e">{`${(
                properties["技能范围∏"] * 100 - 100
              ).toFixed(0)}%`}%</div>
            </div>
            {properties.保护罩 > 0 && (
              <div class="de-item">
                <div class=" text-hex-836832">保护罩</div>
                <div class="text-hex-3ea74e">{`${(
                  properties.保护罩 * 100
                ).toFixed(2)}%`}</div>
              </div>
            )}
            <div class="w-100% de-item !pl-0">
              <div class="flex items-center w-65px">
                <div class="ml-5px text-hex-836832 name">装备速度</div>
              </div>
              <div class="text-hex-3ea74e flex flex-1 items-center justify-between">
                <div class="flex flex-1 items-center justify-around">
                  <div class="w-15px h-15px flex items-center justify-center">
                    <div class={`common-icon-${ICONS.攻击速度}`} />
                  </div>
                  <div>{`${(
                    properties.攻击速度 * 100
                  ).toFixed(2)}%`}</div>
                  <div>{`(+${
                    (properties.其他攻击速度 * 100
                    ).toFixed(0)
                  }%)`}</div>
                </div>
                <div class="flex flex-1 items-center justify-around">
                  <div class="w-15px h-15px flex items-center justify-center">
                    <div class={`common-icon-${ICONS.施放速度}`} />
                  </div>
                  <div>{`${(
                    properties.施放速度 * 100
                  ).toFixed(2)}%`}</div>
                </div>
                <div class="flex flex-1 items-center justify-around">
                  <div class="w-15px h-15px flex items-center justify-center">
                    <div class={`common-icon-${ICONS.移动速度}`} />
                  </div>
                  <div>{`${(
                    properties.移动速度 * 100
                  ).toFixed(2)}%`}</div>
                </div>

              </div>
            </div>

          </div>
          <div class="details">
            <div class="w-100% de-item !pl-0">
              <div class="flex items-center">
                <div class="ml-5px text-hex-836832 name">属性抗性</div>
              </div>
              <div class="text-hex-3ea74e">{`火(${details.value?.站街?.火抗?.toFixed(
                0
              )})/冰(${details.value?.站街?.冰抗?.toFixed(
                0
              )})/光(${details.value?.站街?.光抗?.toFixed(
                0
              )})/暗(${details.value?.站街?.暗抗?.toFixed(0)})`}</div>
            </div>
            {renderList(
              [
                "出血",
                "中毒",
                "灼伤",
                "感电",
                "",
                "",
                "冰冻",
                "减速",
                "眩晕",
                "诅咒",
                "失明",
                "石化",
                "睡眠",
                "混乱",
                "束缚"
              ],
              (item) => {
                if (item == "") {
                  return <div class="w-33.33% de-item !min-w-33.33%"></div>;
                }
                const num = properties[`${item}抗性`] ?? 0;
                return (
                  <div class="w-33.33% de-item !min-w-33.33%">
                    <div class="text-hex-836832">{item}</div>
                    <div
                      class={
                        num > 0
                          ? "text-hex-3ea74e"
                          : num == 0
                            ? "text-hex-5b5b5b"
                            : "text-hex-ff0000"
                      }
                    >{`${num?.toFixed(2)}%`}</div>
                  </div>
                );
              }
            )}
          </div>
          {props.showCD && (<div class="my-4px mx-5px flex items-center">
            <div class="w-25% flex text-hex-e9c558">
              技能冷却
              <calc-iconselect
                class="talisman"
                emptyLabel="冷却"
                columnNum={Math.min(
                  Math.round((properties?.cdr ?? []).length / 2),
                  10
                )}
                v-model={skill_cd.value}
              >
                {renderList(
                  (properties?.cdr ?? []).map((a) => a[0]) ?? [],
                  (a, index) => (
                    <calc-option value={index}>
                      <div
                        class={`character-icon-${
                          characterStore.alter
                        }-${a.replace(/[().·，：]+/g, "")}`}
                      />
                    </calc-option>
                  )
                )}
              </calc-iconselect>
            </div>
            {/*
              <calc-select v-model={skill_cd.value} class="!w-40%">
                {renderList((properties?.cdr ?? []).map(a => a[0]) ?? [], (a, index) => (
                  <calc-option value={index}>{a}</calc-option>
                ))}
              </calc-select> */}
            <div class="!w-35% flex items-center justify-center">
              {get_skill_cd()}
            </div>
            <calc-button
              class="h-20px !w-40%"
              onClick={() => (showCDR.value = !showCDR.value)}
            >
              技能冷却详情
            </calc-button>
          </div>)}
          <div style={dropdownStyle.value} v-show={showCDR.value}>
            <div style="background-color: rgba(0, 0, 0, 0.5);margin:5px;border:1px solid rgba(255, 255, 255, 0.1);overflow-y: auto;height:378px">
              <div class="w-full text-center text-hex-B29632 my-5px">
                技能冷却缩减情况
              </div>
              {renderList(properties?.cdr, (item) => (
                <div class="flex items-center justify-between mx-5px my-5px">
                  <div
                    class={`character-icon-${
                      characterStore.alter
                    }-${item[0].replace(/[().·，：]+/g, "")}`}
                  />
                  <div class="text-hex-b1a785">{item[2].toFixed(1)}s</div>
                  <div
                    class={
                      item[1] > 0
                        ? "text-hex-3ea74e"
                        : item[1] == 0
                          ? "text-hex-5b5b5b"
                          : "text-hex-ff0000"
                    }
                  >
                    {(item[1] * 100).toFixed(1)}%
                  </div>
                </div>
              ))}
            </div>
          </div>
        </>
      );
    }

    return () => {
      return (
        <>
          <div class="detail_head">
            {props.role == "delear"
              ? renderDelearProperties()
              : renderBufferProperties()}

            {
              <div class="sum" style={`color:${result.value[1]}`}>
                {result.value[0]}
              </div>
            }
          </div>
        </>

      );
    };
  }
});
</script>

<style lang="scss">
.detail_head{
  background-color: #000000bf;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}
.details {
  // border-left: 1px solid rgba(255, 255, 255, 0.1);
  // border-right: 1px solid rgba(255, 255, 255, 0.1);
  max-height: 160px;
  overflow-y: auto;
  padding-top: 2px;
  padding-bottom: 2px;
  display: flex;
  flex-wrap: wrap;

  -webkit-font-smoothing: none;
  // background-color: rgba(0, 0, 0, 0.8);
  margin-top: 2px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);

  .de-item {
    height: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    min-width: 50%;
    padding: 0 5px;
    box-sizing: border-box;

    img {
      padding-left: 5px;
      padding-right: 3px;
      width: 15px;
      height: 15px;
    }

    .name {
      width: 50px;
    }
  }
}

.sum {
  height: 50px;
  // border-top: 1px solid rgba(255, 255, 255, 0.1);
  // border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  border-top: 1px solid;
  border-image-source: linear-gradient(to right, #644f23, #d8b04f, #644f23);
  margin-left: 5px;
  margin-right: 5px;
  border-image-slice: 1;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 25px;
}
</style>
