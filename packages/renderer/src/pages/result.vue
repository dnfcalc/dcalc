<script lang="tsx">
import { computed, defineComponent, renderList, watch } from "vue"
import { useRoute } from "vue-router"
import api from "@/api"
import type { IAnyResultInfo } from "@/api/character/type"
import Profile from "@/components/internal/profile/index.vue"
import { useAppStore, useCharacterStore, useConfigStore, useGlobalStore } from "@/store"
import { toMap, to_percent } from "@/utils"
import Watermark from "@/components/watermark/index.vue"

interface ISkillResult {
  cd?: number
  cd_o?: number
  count: number
  damage: string[]
  avg: string[]
  dps: string[]
  mix: string
  order: number
  name: string
}

interface ISkillPassive {
  lv: number
  name: string
  info: {
    type: string
    info: (string | number)[]
    percent?: boolean
  }[]
}

export default defineComponent({
  async setup() {
    const route = useRoute()
    const uid = (route.query.res as string) ?? ""
    const standardId = (route.query.standard as string) ?? ""
    const characterStore = useCharacterStore()
    const appStore = useAppStore()
    const globalStore = useGlobalStore()
    const configStore = useConfigStore()


    const app = useAppStore()

    window.pywebview && watch(() => app.userInfo, () => {
      appStore.title = `${app.uid > 0 ? `${app.userInfo?.userName}(${app.uid}) ` : ""}请勿用于打桩排名等节奏`
    })

    let standards: IAnyResultInfo
    let result: IAnyResultInfo

    if (window.pywebview) {
      standards = standardId ? await api.getResult(standardId) : ({} as IAnyResultInfo)
      result = await api.getResult(uid)
    } else {
      standards = standardId ? (JSON.parse(sessionStorage.getItem(standardId) ?? "{}") as IAnyResultInfo) : ({} as IAnyResultInfo)
      result = JSON.parse(sessionStorage.getItem(uid) ?? "{}") as IAnyResultInfo
    }

    configStore.$patch({ token: result.token ?? configStore.token })

    const res = toMap(result, ["info", "skills", "skills_passive", "equips_forge", "merge_list", "customize", "merge", "specificity", "talisman_set", "rune_set"]) as IAnyResultInfo
    await characterStore.load()
    // characterStore.$patch({ alter: res.alter, name: res.name })
    configStore.merge = res.merge_list ?? {}
    configStore.forge_set = res.forge_set ?? {}
    configStore.customize = res.customize ?? {}
    configStore.specificity = res.specificity ?? {}
    configStore.fusion_list = res.fusion_list ?? []
    configStore.talisman_set = (res as any).talisman_set ?? []
    configStore.rune_set = (res as any).rune_set ?? []

    function skill_tooltip(skill: string) {
      if (res.role == "buffer") {
        return <div></div>
      }
      const delearSkills = res.skills[skill]
      return (
        <div class="tooltip-skill">
          <div class="name">
            {skill} Lv {delearSkills.level}
          </div>
          <div class="info">冷却时间:{delearSkills.cd.toFixed(2)}秒</div>
          <div class="info">MP消耗:{delearSkills.mp?.toFixed(0)}</div>
          <div class="info">无色消耗:{delearSkills.cosume_cube_frag}</div>
          <div class="info">百分比:{`${delearSkills.atk_rate?.toFixed(0)}%`}</div>
        </div>
      )
    }

    function transformNum(num = 0, digit = 0) {
      return num <= 0 ? "-" : num.round(digit).toLocaleString()
    }

    function skill_passive_tooltip(skill: ISkillPassive) {
      return (
        <div class="tooltip-skill">
          <div class="name">
            {skill.name} Lv {skill.lv}
          </div>
          {renderList(skill.info, item => {
            const percent = item.percent ?? true
            return (
              <>
                <div class="info">
                  {item.type}:{item.info[0]}
                  {percent && "%"}
                  <div></div>
                </div>
                <div class="info">
                    关联技能:{item.info[1]}
                  {item.info[2] != "无" && item.info[2] != "" && item.info[2] != 0 && <div class="text-hex-696969">({item.info[2]}除外)</div>}
                </div>
              </>
            )
          })}
        </div>
      )
    }

    function renderSkills() {
      if (res.role == "buffer") {
        return renderList(Object.values(res.skills), skill => {
          return (
            <tr>
              <td style="width:12%" class="h-7">
                <calc-tooltip class="flex justify-center" position="right">
                  {{
                    default() {
                      return <div class={`character-icon-${characterStore.alter}-${skill.name.replace(/[().·，：]+/g, "")}`} />
                    },
                    popper() {
                      return skill_tooltip(skill.name)
                    }
                  }}
                </calc-tooltip>
              </td>
              <td style="width:12%">{skill.level}</td>
              <td style="width:16%">
                <div class="flex items-center justify-center">
                  <div class="w-50% flex items-center justify-center">{skill.cd}{skill.cd == "-" ? "" : "s"}</div>
                  <div class="text-hex-3ea74e w-50% flex items-center justify-center">
                    {skill.cd_p}{skill.cd == "-" ? "" : "%"}
                  </div>

                </div>

              </td>


              <td style="width:16%">{transformNum(skill.data[0])}</td>
              <td style="width:16%">{transformNum(skill.data[1])}</td>
            </tr>
          )
        })
      }
      const temp: ISkillResult[] = []

      Object.keys(res.skills).forEach(skill => {
        let display_damage = ["", "white"]
        let avg = []
        let dps = []
        const standard_skill = standards?.skills?.[skill] as (typeof res.skills)[string]
        const standard_damage = standard_skill?.damage as number

        const current_damage = res.skills[skill].damage

        if (standard_damage) {
          display_damage = standard_damage == current_damage ? ["无变化", "white"] : [to_percent(current_damage / standard_damage - 1, 0, "%", true), current_damage > standard_damage ? "#3ea74e" : "red"]
        } else if ((standards?.total_data?.[0] ?? 0) > 0) {
          display_damage = ["新增技能", "#3ea74e"]
        } else {
          display_damage = [Math.round(current_damage).toLocaleString(), "white"]
        }

        if ((standard_damage && standards.role == "delear")) {
          if (standard_damage / standards.skills[skill].count == res.skills[skill].damage / res.skills[skill].count) {
            avg = ["无变化", "white"]
          } else {
            avg = [
              to_percent(res.skills[skill].damage / res.skills[skill].count / (standards.skills[skill].damage / standards.skills[skill].count) - 1, 0, "%", true),
              res.skills[skill].damage / res.skills[skill].count > standards.skills[skill].damage / standards.skills[skill].count ? "#3ea74e" : "red"
            ]
          }
        } else if ((standards?.total_data?.[0] ?? 0) > 0) {
          avg = ["新增技能", "#3ea74e"]
        } else {
          avg = [Math.round(res.skills[skill].damage / res.skills[skill].count).toLocaleString(), "white"]
        }


        if (standard_damage && standards.role == "delear") {
          if (standard_damage / standards.skills[skill].count / standards.skills[skill].cd == res.skills[skill].damage / res.skills[skill].count / res.skills[skill].cd) {
            dps = ["无变化", "white"]
          } else {
            dps = [
              to_percent(res.skills[skill].damage / res.skills[skill].count / res.skills[skill].cd / (standards.skills[skill].damage / standards.skills[skill].count / standards.skills[skill].cd) - 1, 0, "%", true),
              res.skills[skill].damage / res.skills[skill].count / res.skills[skill].cd > standards.skills[skill].damage / standards.skills[skill].count / standards.skills[skill].cd ? "#3ea74e" : "red"
            ]
          }
        } else if ((standards?.total_data?.[0] ?? 0) > 0) {
          dps = ["新增技能", "#3ea74e"]
        } else {
          dps = [Math.round(res.skills[skill].damage / res.skills[skill].count / res.skills[skill].cd).toLocaleString(), "white"]
        }


        temp.push({
          name: skill,
          cd: res.skills[skill].cd,
          cd_o: res.skills[skill].cd_o,
          count: res.skills[skill].count,
          damage: display_damage,
          avg,
          dps,
          mix: to_percent(res.skills[skill].damage / res.total_data[0], 0, "%"),
          order: res.skills[skill].damage
        })
      })
      temp.sort((a, b) => b.order - a.order)
      return renderList(temp, skill => (
        <tr>
          <td style="width:10%" class="h-7 text-center">
            <calc-tooltip class="flex items-center justify-center" position="right">
              {{
                default() {
                  return (
                    <>
                      <div style="position:relative" class="h-28px w-28px">
                        <div class={`character-icon-${characterStore.alter}-${skill.name.replace(/[().·，：]+/g, "")}`} />
                        <div class="size-11" data-text={`Lv ${res.skills[skill.name].level}`}>
                            Lv&nbsp;{res.skills[skill.name].level}
                        </div>
                      </div>
                    </>
                  )
                },
                popper() {
                  return skill_tooltip(skill.name)
                }
              }}
            </calc-tooltip>
          </td>
          <td style="width:18%" class="h-7 text-center leading-7">
            <div class="flex w-full h-full">
              <div class="w-60%">{skill.cd?.toFixed(1)}s</div>
              <div class={`text-hex-${(skill.cd ?? 0) < (skill.cd_o ?? 0) ? "3ea74e" : "ff0000"} w-40%`}>
                {skill.cd?.toFixed(1) == skill.cd_o?.toFixed(1) || skill.cd_o == 0 ? "" : `${((1 - (skill.cd ?? 0) / (skill.cd_o ?? 0)) * 100).toFixed(1)}%`}
              </div>
            </div>
          </td>
          <td style="width:10%" class="h-7 text-center leading-7">
            {skill.count}
          </td>
          <td class="h-7 leading-7 text-center" style={`width:18%;color:${skill.damage[1]}`}>
            {skill.damage[0]}
          </td>
          <td class="h-7 leading-7" style={`width:17%;color:${skill.avg[1]}`}>
            {skill.avg[0]}
          </td>
          <td class="h-7 leading-7" style={`width:17%;color:${skill.dps[1]}`}>
            {skill.dps[0]}
          </td>
          <td style="width:10%" class="h-7  pr-2 leading-7 text-center">
            {to_percent(skill.order / res.total_data[0], 0, "%")}
          </td>
        </tr>
      ))
    }

    function renderTotal() {
      if (res.role == "buffer") {
        return (
          <tr>
            <td style="width:12%" class="h-5">
                总和
            </td>
            <td style="width:12%">-</td>
            <td style="width:16%">-</td>
            <td style="width:16%">{transformNum(res.total_data[2])}</td>
            <td style="width:16%">{transformNum(res.total_data[3])}</td>
          </tr>
        )
      }
      return (
        <tr>
          <td style="width:10%" class="h-5 leading-5">
              总和
          </td>
          <td style="width:18%" class="h-5 text-center">
              -
          </td>
          <td style="width:10%" class="h-5 text-center">
              -
          </td>
          <td style="width:18%" class="h-5">
            {standards?.total_data ? `${(res.total_data[0] / standards.total_data[0] * 100 - 100).toFixed(2)}%` : transformNum(res.total_data[0])}
          </td>
          <td style="width:17%" class="h-5">
              -
          </td>
          <td style="width:17%" class="h-5">
              -
          </td>
          <td style="width:10%" class="h-5  pr-2">
              -
          </td>
        </tr>
      )
    }

    const skill_passive = computed(() => {
      const temp: ISkillPassive[] = []
      Object.keys(res.skills_passive).forEach(name => {
        const skill = res.skills_passive[name]
        //   console.log(skill.info)
        //   console.log(res.skills_passive[name])
        if (skill.info.length > 0) {
          temp.push({
            name,
            lv: skill.lv,
            info: skill.info
          })
        }
      })
      return temp
    })

    const headers = computed(() => {
      if (res.role == "delear") {
        return [
          {
            title: "技能",
            width: "10%"
          },
          {
            title: "CD",
            width: "18%"
          },
          {
            title: "次数",
            width: "10%"
          },
          {
            title: "总伤害",
            width: "18%"
          },
          {
            title: "平均伤害",
            width: "17%"
          },
          {
            title: "秒伤",
            width: "17%"
          },
          {
            title: "占比",
            width: "10%"
          }
        ]
      } else {
        return [
          {
            title: "技能",
            width: "12%"
          },
          {
            title: "等级",
            width: "12%"
          },
          {
            title: "CD",
            width: "16%"
          },
          {
            title: "力智",
            width: "16%"
          },
          {
            title: "三攻",
            width: "16%"
          }
        ]
      }
    })

    const mergeInfo = computed(() => {
      const cur = res.equips?.filter(a => a.part == "武器")?.[0]
      return {
        weaponType: cur?.type,
        merges: res.merge_list[cur?.id ?? ""] ?? []
      }
    })

    return () => (
      <>
        <Watermark content={(appStore.userInfo.uid ?? -1) > 0 ? appStore.userInfo.uid.toString() : "纸飞机计算器"} color= "rgba(255,255,255,0.2)" fontSize={14} class="flex h-full m-0 overflow-hidden detail" style={`background: url('${import.meta.env.BASE_URL}images/result.jpg') no-repeat;background-size:cover`}>
          <div class="flex h-full w-266px justify-center">
            {res && (
              <Profile
                total-data={res.total_data}
                role={res.role}
                equList={res.equips}
                class="!m-0 !p-0"
                details={res.info}
                withStandard={!!standards?.id}
                standard-data={standards?.total_data}
                equips_forge={res.equips_forge}
                canChoose={false}
                showCD={false}
                share={res}
                fusionList={res.fusion_list}
                showTM={((globalStore.global_set_details[2] ?? []) as number[]).includes(0)}
                showZF={((globalStore.global_set_details[2] ?? []) as number[]).includes(1)}
                tipInfo={globalStore.global_set_details[3] as number[]}
                mergeInfo={mergeInfo.value}
              ></Profile>
            )}
          </div>
          <table class="h-full bg-hex-000000/60 flex-1 ml-1 p-4 block overflow-hidden" style="border:1px solid rgba(255,255,255,0.15);">
            <thead class="bg-hex-000000/40 text-white w-full" style="border-left:1px solid rgba(255,255,255,0.15);border-right:1px solid rgba(255,255,255,0.15)">
              <tr class="bg-hex-000000/40 h-4 !text-hex-B2966B">
                {renderList(headers.value, head => {
                  return (
                    <th class="item-head" style={`width:${head.width}`}>
                      {head.title}
                    </th>
                  )
                })}
              </tr>
            </thead>

            <tbody class="bg-hex-000000/40 m-0 text-white w-full p-0 skills overflow-y-auto block" style="height:calc(100% - 86px);border:1px solid rgba(255,255,255,0.15);border-top:none">
              {renderSkills()}
            </tbody>

            <tbody class="bg-hex-000000/40 h-6 m-0 text-white w-full p-0 block" style="border-left:1px solid rgba(255,255,255,0.15);border-right:1px solid rgba(255,255,255,0.15)">
              {renderTotal()}
            </tbody>

            <tr class="bg-hex-000000/40 bottom h-10 m-0 w-full p-0 block">
              <div class="flex h-10 ml-1 items-center">
                {renderList(skill_passive.value, skill => (
                  <div class="mr-1">
                    <calc-tooltip z={9} position="top">
                      {{
                        default() {
                          return (
                            <div style="position:relative">
                              <div class={`character-icon-${characterStore.alter}-${skill.name.replace(/[().·，：]+/g, "")}`} />
                              <div class="size-11" data-text={`Lv ${skill.lv}`}>
                                  Lv&nbsp;{skill.lv}
                              </div>
                            </div>
                          )
                        },
                        popper() {
                          return skill_passive_tooltip(skill)
                        }
                      }}
                    </calc-tooltip>
                  </div>
                ))}
              </div>
            </tr>
          </table>
        </Watermark>
      </>
    )
  }
})
</script>

<style lang="scss" scoped>
  table thead,
  tbody tr {
    display: table;
    width: 100%;
    table-layout: fixed;

    td {
      text-align: center;
    }
  }

  .item-head {
    background: linear-gradient(#2b2817, #171407);
    // font-size: 12px;
    border-top: 1px solid #423d2c;
    border-bottom: 1px solid #211d15;
  }

  .bottom {
    border: 1px solid rgba(255, 255, 255, 0.15);
  }

  .size-11 {
    position: absolute;
    z-index: 0;
    top: -3px;
    right: -4px;
    font-size: 12px;
    transform: scale(0.7);
    color: black;
    text-shadow: none;
    font-weight: bolder;
    font-family: Arial;
  }

  .size-11::before {
    // text-shadow: #37fa38 2px 0 0, #37fa38 0 2px 0, #37fa38 -2px 0 0, #37fa38 0 -2px 0;
    // -webkit-text-stroke-width: 1px;
    // -webkit-text-stroke-color: #37fa38;
    content: attr(data-text);
    position: absolute;
    -webkit-text-stroke: 2.5px #37fa38;
    font-family: Arial;
    text-shadow: none;
    z-index: -1;
  }

  //   .size-11 {
  //     position: absolute;
  //     top: -3px;
  //     right: -2px;
  //     font-size: 12px;
  //     transform: scale(0.78);
  //     font-weight: 650;
  //     font-family: Arial;
  //     color: #fee86b;
  //     text-shadow: #000 2px 0 0, #000 0 2px 0, #000 -2px 0 0, #000 0 -2px 0;
  //     -webkit-font-smoothing: antialiased;
  //   }
</style>
