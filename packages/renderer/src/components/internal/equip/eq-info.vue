<script lang="tsx">
import { asyncComputed } from "@vueuse/core"
import type { PropType } from "vue"
import { computed, defineComponent, reactive, renderList, watch } from "vue"

import EqIcon from "./eq-icon.vue"
import { formatStr, rarityClass } from "@/utils"
import { useBasicInfoStore, useCharacterStore } from "@/store"
import Watermark from "@/components/watermark/index.vue"

interface Status {
  id: number
  label: string
  num: number
  isRate: boolean
  info: string
  linebreak?: boolean
}

interface BadgeItem {
  type: number
  props: string[]
}

  type classNames = (id: number) => string | string[] | undefined

const propNames = ["力量", "智力", "体力", "精神", "物理攻击力", "魔法攻击力", "独立攻击力"]
const badgeNames = ["白金徽章镶嵌栏", "红色徽章镶嵌栏", "绿色徽章镶嵌栏", "蓝色徽章镶嵌栏", "黄色徽章镶嵌栏"]
const badgeClass = ["kong-baijin", "kong-red", "kong-green", "kong-blue", "kong-yellow"]
const eqBagdes = {
  上衣: 2,
  下装: 2,
  头肩: 4,
  项链: 4,
  腰带: 1,
  戒指: 1,
  鞋: 3,
  手镯: 3,
  辅助装备: 0,
  魔法石: 0
}

export default defineComponent({
  name: "InfoDialog",
  components: { EqIcon },
  props: {
    eid: {
      type: [Number, String] as PropType<ID>
    },
    simple: {
      type: Boolean,
      default: false
    },
    colums: {
      type: Boolean,
      default: false
    },
    small: {
      type: Boolean,
      default: false
    },
    forge: {
      type: Object,
      default: () => {}
    },
    pps: {
      type: Array,
      default: () => []
    },
    withTransform: {
      type: Boolean,
      default: false
    },
    isShow: {
      type: [Boolean, Object],
      default: false
    },
    withHead: {
      type: Boolean,
      default: true
    },
    merges: { type: Array, default: () => [] },
    sj: {
      type: Boolean,
      default: false
    },
    upgrade: {
      type: Boolean,
      default: false
    },
    showSuits: {
      type: Boolean,
      default: false
    }
  },
  setup(props) {
    const basicStore = useBasicInfoStore()
    const characterStore = useCharacterStore()
    // const globalStore = useGlobalStore()

    const transform = reactive({
      tips: [] as string[],
      enchanting: [] as string[], // ["所有属性强化 +30"], // 附魔
      reinforce: 0, // 18, // 增幅、强化数值
      type: 1,
      refine: 0, // 8, // 锻造
      reinforceInfo: {
        reinforce: [0, 0, 0, 0, 0, 0, 0], // [0, 91, 91, 0, 0, 0, 0], //增幅
        strengthen: [0, 0, 0, 0, 0, 0, 0], // [29, 29, 0, 29, 0, 0, 0], //强化
        refine: [0, 0, 0, 0, 0, 0, 0], // [0, 0, 0, 0, 0, 0, 539]// 锻造
        refineSW: 0 // [0, 0, 0, 0, 0, 0, 539]// 锻造
      },
      growthLvs: [1, 1, 1, 1], // 词条等级
      growthAttacks: [0, 0, 0, 0], // 词条等级
      growthBuffers: [0, 0, 0, 0], // 词条等级
      badges: [] as BadgeItem[] // [ { type: 1,  props: [ "智力 +30", ] }, { type: 2,  props: [ "智力+30 魔爆+3%", ] }, { type: 3,  props: [ "物攻 +20", ] },
      // { type: 4,  props: [ "智力 +15", ] }, { type: 0,  props: [  "四维+8 [冰之领悟]技能Lv+1", ] }, ], // 徽章
    })

    const is_buffer = computed(() => characterStore.is_buffer)

    const sum_lv = computed(() => {
      return transform.growthLvs.reduce((a, b) => a + b)
    })
    const equip = asyncComputed(async () => {
      if (props.eid != undefined && (typeof props.eid == "number" || typeof props.eid == "string")) {
        const temp = await basicStore.get_equipment_detail(props.eid, props.sj || props.upgrade, characterStore.is_delear, props.upgrade)
        if (props.withTransform) {
          loadTransform(temp)
        }
        return temp
      }
    })

    const tipInfo = computed(() => {
      return props.forge?.show ?? [true, true, true]
    })

    function renderStatus(rowClass?: classNames, spanClass?: classNames, withTransform?: boolean) {
      return ({ id, label, num, isRate, linebreak }: Status, indexForStatus: number) => {
        let array: JSX.Element[] = []

        label = label.replaceAll(/@([^@]*)@/g, (m, _index) => `<span style="color:#3ea74e">${m.slice(1, -1)}</span>`)

        // if (is_buffer.value && (label.includes("奶系") || label.includes("增益量"))) {
        //   array.push(<span style={num ? "margin-right: 5px" : undefined} v-html={label}></span>)
        // } else {
        //   if (!label.includes("奶系") && !label.includes("增益量")) {
        //     array.push(<span style={num ? "margin-right: 5px" : undefined} v-html={label}></span>)
        //   }
        // }

        array.push(<span style={num ? "margin-right: 5px" : undefined} v-html={label}></span>)

        const rowClassNames = rowClass?.(id)
        // const spanClassNames = spanClass?.(id)
        if (num) {
          let text: any = num
          if (isRate) {
            text = (num * 100).toFixed(0)
            text = `${num > 0 ? "+" : ""}${text}%`
          }
          // array.push(<span class={spanClassNames}>{text}</span>)
          array.push(<span v-html={text}></span>)
        }
        let result: JSX.Element = (
          <div style={linebreak ?? false ? "min-height:5px" : ""} class={[rowClassNames]}>
            {array}
          </div>
        )
        if (withTransform) {
          const nameIndex = propNames.findIndex(x => x == label)
          if (nameIndex > -1 && (transform.refine > 0 || transform.reinforce > 0)) {
            const arr = setTransform(nameIndex)
            array = array.concat(arr)

            const beforeArr = []
            // 往前查漏补缺
            for (let i = nameIndex - 1; i >= 0; i--) {
              if (isWithTransform(i)) {
                const name = propNames[i]
                const index = equip.value.prop.base.findIndex(({ label }: Status) => label == name)
                if (index >= 0) {
                  break
                } else {
                  const tArr = setTransform(i, name)
                  beforeArr.push(
                    <div style={linebreak ?? false ? "min-height:5px" : ""} class={[rowClassNames]}>
                      {tArr}
                    </div>
                  )
                }
              }
            }
            const arrterArr = []
            // 最后一个， 往后查漏补缺
            if (indexForStatus == equip.value.prop.base.length - 1) {
              for (let i = nameIndex + 1; i < propNames.length; i++) {
                if (isWithTransform(i)) {
                  const name = propNames[i]
                  const index = equip.value.prop.base.findIndex(({ label }: Status) => label == name)
                  if (index < 0) {
                    const tArr = setTransform(i, name)
                    arrterArr.push(
                      <div style={linebreak ?? false ? "min-height:5px" : ""} class={[rowClassNames]}>
                        {tArr}
                      </div>
                    )
                  }
                }
              }
            }
            result = (
              <div>
                {beforeArr}
                <div class={[rowClassNames]}>{array}</div>
                {arrterArr}
              </div>
            )
          }
        }
        return result
      }
    }

    function isWithTransform(i: number) {
      return transform.reinforceInfo.strengthen[i] > 0 || transform.reinforceInfo.reinforce[i] > 0 || transform.reinforceInfo.refine[i] > 0
    }

    function setTransform(index: number, name?: string) {
      const array: JSX.Element[] = []
      if (transform.reinforceInfo.strengthen[index] > 0) {
        // 强化
        if (name) {
          array.push(
            <span class="advanced">{name}</span>,
            <span style="margin-left: 5px" class="advanced">
              {transform.reinforceInfo.strengthen[index]}
            </span>
          )
        } else {
          array.push(
            <span style="margin-left: 5px" class="advanced">
                +{transform.reinforceInfo.strengthen[index]}
            </span>
          )
        }
      }
      if (transform.reinforceInfo.reinforce[index] > 0) {
        // 增幅
        if (name && transform.reinforceInfo.strengthen[index] <= 0) {
          array.push(
            <span class="artifact">{name}</span>,
            <span style="margin-left: 5px" class="artifact">
              {transform.reinforceInfo.reinforce[index]}
            </span>
          )
        } else {
          array.push(
            <span style="margin-left: 5px" class="artifact">
                +{transform.reinforceInfo.reinforce[index]}
            </span>
          )
        }
      }
      if (transform.reinforceInfo.refine[index] > 0) {
        // 锻造
        if (name && transform.reinforceInfo.strengthen[index] <= 0 && transform.reinforceInfo.reinforce[index] <= 0) {
          array.push(
            <span class="rare">{name}</span>,
            <span style="margin-left: 5px" class="rare">
              {transform.reinforceInfo.refine[index]}
            </span>
          )
        } else {
          array.push(
            <span style="margin-left: 5px" class="rare">
                +{transform.reinforceInfo.refine[index]}
            </span>
          )
        }
      }
      return array
    }

    const effectClass = function (id: number) {
      if (id > 13) {
        return "strong"
      }
    }

    const sum_buffer = computed(() => {
      let s = 0
      if (transform.growthBuffers && transform.growthBuffers.length > 0) {
        const a = equip.value.prop.growthProps

        for (let i = 0; i < transform.growthBuffers.length; i++) {
          const item = a == null ? null : a[i]
          s += transform.growthBuffers[i] ?? item?.buffer ?? 0
        }
      }
      if (s == 0) {
        for (let i = 0; i < 4; i++) {
          const item = equip.value.prop.growthProps && equip.value.prop.growthProps.length > i ? equip.value.prop.growthProps[i] : null
          s += item?.buffer ?? 0
        }
      }

      return s
    })

    const sum_attack = computed(() => {
      let s = 0
      if (transform.growthBuffers && transform.growthBuffers.length > 0) {
        const a = equip.value.prop.growthProps

        for (let i = 0; i < transform.growthBuffers.length; i++) {
          const item = a == null ? null : a[i]
          s += transform.growthAttacks[i] ?? item?.attack ?? 0
        }
      }
      if (s == 0) {
        for (let i = 0; i < 4; i++) {
          const item = (equip.value.prop.growthProps && equip.value.prop.growthProps.length > i ? equip.value.prop.growthProps[i] : null) || props.pps?.[i]
          s += item?.attack ?? 0
        }
      }
      return s
    })

    function loadTransform(eq: any) {
      if (props.forge && props.forge.info) {
        transform.growthLvs = props.forge.info?.["成长词条等级"] ?? [1, 1, 1, 1]
        transform.growthAttacks = props.forge.data?.attack ?? [0, 0, 0, 0]
        transform.growthBuffers = props.forge.data?.buffer ?? [0, 0, 0, 0]
        transform.reinforce = props.forge.info?.["强化数值"] ?? 0
        transform.refine = props.forge.info?.["锻造数值"] ?? 0
        transform.enchanting = props.forge.info?.["附魔"] ?? []

        transform.type = props.forge.info?.["强化类型"] ?? 1
        transform.tips = props.forge.data?.tips ?? []

        // 处理徽章
        transform.badges = []
        if (eq && eq.position) {
          const types = eq.position.split("(")
          const type = types[0]
          let position = type
          if (types.length > 1) {
            position = types[1].split(")")[0]
          }
          const bgs = props.forge.info["徽章"] ?? []
          for (const b of bgs) {
            if (b) {
              transform.badges.push({
                type: (eqBagdes as any)[position] ?? 0,
                props: [b]
              })
            }
          }
        }

        // 处理强化增幅数据
        transform.reinforceInfo.reinforce = [0, 0, 0, 0, 0, 0, 0]
        transform.reinforceInfo.strengthen = [0, 0, 0, 0, 0, 0, 0]
        if (transform.reinforce > 0) {
          if (transform.type == 1 && props.forge.data?.["增幅四维"] && props.forge.data?.["增幅四维"].length > 0) {
            // 增幅
            for (let i = 0; i < props.forge.data?.["增幅四维"].length; i++) {
              transform.reinforceInfo.reinforce[i] = props.forge.data?.["增幅四维"][i]
            }
          }
          if (props.forge.data?.["强化四维"] && props.forge.data?.["强化四维"].length > 0) {
            for (let i = 0; i < props.forge.data?.["强化四维"].length; i++) {
              transform.reinforceInfo.strengthen[i] = props.forge.data?.["强化四维"][i]
            }
          }
          if (props.forge.data?.["强化攻击力"] && props.forge.data?.["强化攻击力"].length > 0) {
            for (let i = 0; i < props.forge.data?.["强化攻击力"].length; i++) {
              transform.reinforceInfo.strengthen[i + 4] = props.forge.data?.["强化攻击力"][i]
            }
          }
        }
        // 处理强化锻造数据
        transform.reinforceInfo.refine = [0, 0, 0, 0, 0, 0, 0]
        transform.reinforceInfo.refineSW = 0
        if (transform.refine > 0) {
          const dz = props.forge.data?.["锻造加成"]
          if (dz && dz.length > 0) {
            transform.reinforceInfo.refine[6] = dz[0]
          }
          if (dz && dz.length > 1) {
            transform.reinforceInfo.refineSW = dz[1]
          }
        }
      }
    }

    function formatProp(strs: string[], template: string, i: number, withleft: boolean = false, _withTop: boolean = false, _lineBreak = false) {
      if (props.forge && props.forge.data && props.forge.data.params && props.forge.data.params.length > i && props.forge.data.params[i] && template) {
        const params = props.forge.data.params[i]
        const nums = []
        for (const x of params) {
          nums.push(`<span class='${classForNum(i)}'>+${x}%</span>`)
        }
        const str = formatStr(template, nums)

        strs = str.split("<br>")
      } else {
        strs = strs.map(a => a.replaceAll(/攻击强化\s\+\d+.?\d+%/g, (m, _index) => `攻击强化 <span style="color:#8a6f36">${m.slice(5)}</span>`))
      }
      return renderList(strs, s => {
        s = s.replaceAll(/(\d)(?=(\d{3})+(?!\d))/g, "$1,").replaceAll(/@([^@]*)@/g, (m, _index) => `<span style="color:#b59834">${m.slice(1, -1)}</span>`)
        if (s == "" && strs.length == 1) {
          return <div></div>
        } else {
          return (
            <div style={_lineBreak ? "min-height:5px" : ""} class={["strong"].concat([withleft ? "paddleft" : ""])}>
              <span v-html={s}></span>
            </div>
          )
        }
      })
    }

    watch(props, () => {
      if (props.isShow) {
        loadTransform(equip.value) // 加载打造数据
      }
    })

    const iconBages = computed(() => {
      const x = transform.badges && transform.badges.length > 0 ? { color: [transform.badges[0]?.type, transform.badges[1]?.type], num: transform.badges.length } : null
      return x
    })

    function classForNum(i: number) {
      // let c = (transform.growthLvs[i] ?? 1) <= 20 ? "" : transform.growthLvs[i] <= 50 ? "advanced" : transform.growthLvs[i] < 80 ? "rare" : transform.growthLvs[i] == 100 ? "epic" : "artifact"
      return LvClass(transform.growthLvs[i] ?? 1)
    }

    function LvClass(i: number) {
      if (equip.value.rarity == "史诗" && !equip.value.name.startsWith("跨越之忆")) {
        // 升级神
        // 1~19 高级 20~29 稀有 30~39 神器 40~49 传说 50~59 勇者 60 史诗
        // 不升级神
        // 1~19 无变化 20~49 高级 50~79 稀有 80 神器
        if (i <= 19) {
          return ""
        }
        if (i <= 49) {
          return rarityClass("高级")
        }
        if (i <= 79) {
          return rarityClass("稀有")
        }
        if (i == 80) {
          return rarityClass("神器")
        }
        if (i <= 80 + 19) {
          return rarityClass("高级")
        }
        if (i <= 80 + 29) {
          return rarityClass("稀有")
        }
        if (i <= 80 + 39) {
          return rarityClass("神器")
        }
        if (i <= 80 + 49) {
          return rarityClass("传说")
        }
        if (i <= 80 + 59) {
          return rarityClass("勇者")
        }
        if (i <= 80 + 69) {
          return rarityClass("史诗")
        }
      } else {
        // 传说
        // 1~19 无变化 20~39 高级 40~49 稀有 50~69 神器 70~79 传说 80 勇者
        if (i <= 19) {
          return ""
        }
        if (i <= 39) {
          return rarityClass("高级")
        }
        if (i <= 49) {
          return rarityClass("稀有")
        }
        if (i <= 69) {
          return rarityClass("神器")
        }
        if (i <= 79) {
          return rarityClass("传说")
        }
        if (i == 80) {
          return rarityClass("勇者")
        }
      }
    }

    function renderLevel(i: number, left: boolean, x: any = undefined) {
      const a = (equip.value.prop.growthProps && equip.value.prop.growthProps.length > i ? equip.value.prop.growthProps[i] : null) || x
      return is_buffer.value ? (
        <div class={["text-hex-8a6f36"].concat(left ? "paddleft" : "")}>
          <span style="margin-right: 10px;">增益量</span>
          <span class={classForNum(i)}>{(transform.growthBuffers[i] || a?.buffer || 0).toFixed(0)}</span>
        </div>
      ) : (
        <>
          <div class={["text-hex-8a6f36"].concat(left ? "paddleft" : "")}>
            <span style="margin-right: 10px;">攻击强化</span>
            <span class={classForNum(i)}>{`${(transform.growthAttacks[i] || a?.attack || 0).toFixed(1)}%`}</span>
          </div>
        </>
      )
    }

    // const openUrl = useOpenWindow()

    return () => {
      if (!equip.value) {
        return <div></div>
      }
      return (
        <Watermark class={["approved-form"].concat([props.colums ? "with-colums" : ""])}>
          {props.withHead && (
            <div class="epic title" style="display: flex">
              <eq-icon eq={equip.value} badges={iconBages.value}></eq-icon>
              <div class="eq-name" style="width: 100%; margin-left: 8px">
                <div>
                  <span style="display: flex" class={rarityClass(equip.value.rarity)}>
                    {transform.reinforce > 0 ? <span style="margin-right: 4px">+{transform.reinforce}</span> : <span></span>}
                    {transform.refine > 0 ? <span>({transform.refine})</span> : <span></span>}
                    <span>
                      {sum_lv.value > 320 && equip.value.lv == 105 ? "神：" : ""}
                      {equip.value.name}
                    </span>
                  </span>
                </div>
                <div class="flex items-center justify-between w-100%">
                  {/* <div class="text-hex-5b5b5b flex-1">纸飞机计算器</div> */}
                  <div class="text-hex-8ED531">
                    {equip.value.suit.length > 0 && renderList([equip.value.suit[0]], suit => (`${suit} `))}
                  </div>
                  <div class="eq-name yellow" style="w-50% text-align: right">
                    <span>{equip.value.position}</span>
                  </div>
                </div>
              </div>
            </div>
          )}

          {props.merges.length > 0 && equip.value.part.includes("融合") && (
            <>
              <div>
                <div class="hr"></div>
                <div class="green" style="padding-top: 5px"> &lt;融合石属性&gt; </div>
              </div>
              {renderList(props.merges, (x: any, i: number) =>
                x != null ? (
                  <>
                    <div style="padding-top: 5px">
                      {formatProp(x.props, x.template, i, false, false, x.linebreak)}
                    </div>
                  </>
                ) : (
                  <div style="padding-top: 5px">
                    <span>请选择 [融合石] 词条</span>
                  </div>
                )
              )
              }
            </>
          )
          }

          {props.merges.length > 0 && !equip.value.part.includes("融合") ? (
            <>
              <div>
                <div class="hr"></div>
                <div class="green" style="padding-top: 5px"> &lt;巴卡尔融合属性&gt; </div>
              </div>
              {props.merges != null && props.merges.length > 0
                ? renderList(props.merges, (x: any, i: number) =>
                  x != null && x.type > 0 ? (
                    <>
                      <div class={`${x.type != 10 ? "props-bakal" : "props-bakal-raid"}`} style="padding-top: 5px">
                        {/* <div class="yellow"> {`${x.type != 10 ? "[普通]" : "[龙焰]"}`} </div> */}
                        {(is_buffer.value ? x?.buffer > 0 : x?.attack > 0) && renderLevel(i, false, x)}
                        {formatProp(x.props, x.template, i, false, false, x.linebreak)}
                      </div>
                    </>
                  ) : (
                    <div class="suiji-props gey" style="padding-top: 5px">
                      <span>请选择 [武器融合] 词条</span>
                    </div>
                  )
                )
                : renderList(equip.value.prop.growthProps, (p, i: number) => (
                  <div style="padding-top: 5px">
                    {p.props && p.props.length > 0 ? (
                      <>

                        {/* <div class="yellow">
                          <span>
                                属性 {i + 1} - Lv{transform.growthLvs[i] || 1}
                          </span>
                        </div> */}
                        {renderLevel(i, true)}
                        {formatProp(p.props, p.template, i, true, false, p.linebreak)}
                      </>
                    ) : (
                      <div class="paddleft suiji-props gey">
                        <span>随机属性</span>
                      </div>
                    )}
                  </div>
                ))}
            </>
          ) : (
            <>
              {" "}
              {tipInfo.value[0] && transform.badges && transform.badges.length > 0 ? (
                <div>
                  <div class="hr"></div>
                  <div style="display: flex">
                    {renderList(transform.badges, (bs, i) => (
                      <div style={i > 0 ? "margin-left: 20px" : ""}>
                        <div class={badgeClass[bs.type]}>[{badgeNames[bs.type]}]</div>
                        {renderList(bs.props, b => (
                          <div>{b}</div>
                        ))}
                      </div>
                    ))}
                  </div>
                </div>
              ) : (
                <div></div>
              )}
              {tipInfo.value[1] && !equip.value.part.includes("融合") && (
                <>
                  <div class="hr"></div>
                  {transform.reinforce > 0 || transform.refine > 0 ? (
                    <span>
                      {transform.reinforce > 0 ? (
                        <span style="margin-right: 5px">
                          {transform.type == 1 ? (
                            <span>
                              <span class="advanced">+{transform.reinforce} 强化</span>/<span class="artifact">增幅</span>
                            </span>
                          ) : (
                            <span class="advanced">+{transform.reinforce} 强化</span>
                          )}
                        </span>
                      ) : (
                        <span></span>
                      )}
                      {transform.refine > 0 ? (
                        <span style="margin-right: 5px" class="rare">
                            +{transform.refine} 锻造
                        </span>
                      ) : (
                        <span></span>
                      )}
                      <span>性能适用</span>
                    </span>
                  ) : (
                    <span></span>
                  )}

                  {equip.value.prop.base.map(renderStatus(undefined, undefined, true))}
                </>
              )}
              {tipInfo.value[2] && transform.enchanting != null && transform.enchanting.length > 0 && (
                <>
                  <div class="hr"></div>
                  <div class="text-hex-9A812C"> &lt;附魔&gt; </div>
                  {/* { ? ( */}
                  <div class="enchanting" style="margin-top:6px">
                    {renderList(transform.enchanting, e => (
                      <div>{e.replace("(", " +").replace(")", "")}</div>
                    ))}
                  </div>
                  {/* ) : (
                    <div class="gey">未赋予魔法能力</div>
                  )} */}
                </>
              )}
              {equip.value.prop.effect && equip.value.prop.effect.length > 0 && (
                <div>
                  <div class="hr"></div>
                  {equip.value.prop.effect.map(renderStatus(effectClass))}
                </div>
              )}
              {transform.reinforceInfo.refineSW > 0 ? (
                <div>
                  <div class="hr"></div>
                  <div class="green"> &lt;辅助职业专属属性&gt; </div>
                  <div class="rare">力量/智力/体力/精神 +{transform.reinforceInfo.refineSW}</div>
                </div>
              ) : (
                <span></span>
              )}
              {transform.tips.length > 0 && (
                <div>
                  <div class="hr"></div>
                  <div style="margin-top:6px;color:rgb(255,85,85)">
                    {renderList([...new Set(transform.tips)], e => (
                      <div>{e.replace(".0", "")}</div>
                    ))}
                  </div>
                </div>
              )}
              {(sum_attack.value > 0 || sum_buffer.value > 0 || (props.pps != null && props.pps.length > 0)) && (
                <div>
                  <div class="hr"></div>
                  <div class="text-hex-9A812C "> &lt;{equip.value.type == 0 ? "固定属性" : "定制属性"}&gt; </div>
                  {!props.simple && (
                    <div>
                      {is_buffer.value ? (
                        <div class="flex text-hex-8a6f36">
                            增益量 <div class={`${LvClass(sum_lv.value / 4)} ml-5px`}> {sum_buffer.value.toFixed(0)}</div>
                        </div>
                      ) : (
                        <>
                          <div class="flex text-hex-8a6f36">
                            攻击强化<div class={`${LvClass(sum_lv.value / 4)} ml-5px`}> +{(sum_attack.value).toFixed(1)}%</div>
                          </div>
                        </>
                      )}
                    </div>
                  )}
                  {/* {!props.simple && (
                    <div class="flex text-hex-8a6f36">
                       等级<div class={`${LvClass(sum_lv.value / 4)} ml-5px`}>{` ${sum_lv.value / 4 > 80 ? sum_lv.value / 4 - 80 : sum_lv.value / 4}`}</div>
                    </div>
                  )} */}
                </div>
              )}
              {props.pps != null && props.pps.length > 0
                ? renderList(props.pps, (x: any, i: number) =>
                  x != null && x.id ? (
                    <div class="suiji-props">
                      {/* <div class="yellow flex">{`属性${i + 1}`}&nbsp;{renderLevel(i, false, x)} */}
                      <div class="yellow flex">{renderLevel(i, false, x)}
                      </div>

                      {formatProp(x.props, x.template, i, false, false, x.linebreak ?? false)}
                    </div>
                  ) : (
                    <div class="suiji-props gey">
                      {/* <div class="yellow">
                        {`属性 ${i + 1}${sum_lv.value / 4 > 80 ? "" : ` - Lv${transform.growthLvs[i] || 1}`}`}
                      </div> */}
                      <span>请切换到 [定制史诗] 页面选择属性</span>
                    </div>
                  )
                )
                : renderList(equip.value.prop.growthProps, (p: { props: []; template: string; linebreak: boolean }, i: number) => (
                  <div style={ p.props && p.props.length > 0 && ((p.props as string[])?.[0]?.indexOf("- ") == 0 || ((p.props as string[]).length == 1 && (p.props as string[])?.[0] == "")) ? "" : "padding-top: 5px" }>
                    {p.props && p.props.length > 0 ? (
                      <>
                        <div>{formatProp(p.props, p.template, i, false, false, p.linebreak ?? false)}</div>
                      </>
                    ) : (
                      <div class="paddleft suiji-props gey">
                        <span>随机属性</span>
                      </div>
                    )}
                  </div>
                ))}
              {
                props.showSuits && equip.value.suitDetail.length > 0 && (<>
                  {/* <div class="text-hex-9A812C "> &lt;套装属性&gt; </div> */}
                  {renderList([equip.value.suitDetail[0]], suit => (<>
                    <div class="hr"></div>
                    <div class="text-hex-8ED531 mt-5px">{`${suit.name} 套装`}</div>
                    {
                      renderList(suit.info, item => (
                        <>
                          <div class="mt-5px">
                            <div class="text-hex-8ED531">{`[${item.need_num}]套装效果`}</div>
                            <div class="text-hex-997F48 ">
                              {renderList(item.props, prop => (
                                <div style="min-height:5px">{ prop }</div>
                              ))}

                            </div>
                          </div>
                        </>
                      ))
                    }
                  </>))}
                </>)
              }
            </>
          )}
        </Watermark>
      )
    }
  }
})
</script>

<style src="./eq-info.scss" scoped></style>
