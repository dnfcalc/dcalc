<script lang="tsx">
import { computed, defineComponent, onMounted, ref, renderList } from "vue"
import { useCharacterStore, useConfigStore } from "@/store"
import type { ISpecificityInfo } from "@/api/info/type"

export default defineComponent({
  props: {
    simple: {
      type: Boolean,
      default: false
    }
  },
  setup(props) {
    const characterStore = useCharacterStore()
    const configStore = useConfigStore()

    const title = ["异常状态", "魔法值管理", "功能", "技能", "控制/生存", "辅助"]
    const need_lv = [1, 120, 240, 360, 480]

    if (configStore.specificity_list.length < 5) {
      configStore.specificity_list = [...configStore.specificity_list, ...Array(5 - configStore.specificity_list.length).fill(-1)]
    }

    const change_specificity = (no: number, detail: ISpecificityInfo) => {
      configStore.specificity_list[no] = configStore.specificity_list[no] == detail?.id ? -1 : detail?.id;
    }

    const title_index = ref(0)

    const change_title = (index: number) => {
      if (index == 5 && characterStore.is_delear) {
        return
      }
      if (index != title_index.value) {
        title_index.value = index
        configStore.specificity_list = [-1, -1, -1, -1, -1]
      }
    }

    onMounted(() => {
      title_index.value = (characterStore.specificity as ISpecificityInfo[])?.filter(b => configStore.specificity_list.includes(b.id))?.[0]?.title ?? 0
    })

    const details = computed(() => {
      const temp: ISpecificityInfo[] = []
      configStore.specificity_list.forEach(a => {
        const detail = (characterStore.specificity as ISpecificityInfo[])?.filter(b => b.id == a)?.[0]
        temp.push(detail)
      })
      return temp
    })
    return () => {
      return (
        <>
          <div class="w-100% bg-hex-000 bg-opacity-80 h-100% flex flex-col" style={`max-width:${props.simple ? "850px" : "100%"}`}>
            <div class={`flex items-center justify-center py-${props.simple ? 5 : 10}px`}>
              {renderList(6, index => (
                <div class="flex flex-col items-center" onClick={() => change_title(index - 1)} style={`width:${props.simple ? 60 : 80}px;height:${props.simple ? 60 : 90}px;${characterStore.is_delear && index == 6 ? "mix-blend-mode: luminosity;" : ""}`}>
                  <div class="w-100% h-100% flex items-center justify-center">
                    <div style={props.simple ? "transform: scale(0.8);" : "transform: scale(1.25);"} class={`specificity-icon-title-${index - 1}_${index - 1 == title_index.value ? "checked" : "unchecked"}`}></div>
                  </div>
                  {!props.simple && <div class={`w-100% flex items-center justify-center ${index - 1 == title_index.value ? "text-hex-D1C08E" : "text-hex-806F4A"}`}>{title[index - 1]}</div>}
                </div>
              ))}
            </div>
            <div class="flex-1 bg_specificity" style={`background-image: url('${import.meta.env.BASE_URL}images/specificity.png');border-top: 1px solid rgba(117, 95, 68,0.4);padding:${props.simple ? 20 : 40}px;padding-left:${props.simple ? 20 : 100}px;padding-right:${props.simple ? 20 : 100}px;`}>
              <div class="flex">
                <div class="w-50px text-hex-92846A flex items-center justify-center">Lv</div>
                {/* <div>{des[title_index.value]}</div> */}
                {/* {!props.simple && <div class="flex items-center justify-center flex-1 text-xl text-hex-3ea74e underline mt--30px" onClick={() => openUrl("https://bbs.colg.cn/page_collect/173.html?click_from=dcalc")}>更多神界更新情报尽在COLG</div>} */}
              </div>
              {renderList(5, index => (
                <div class={`h-${props.simple ? 40 : 90}px flex items-center`}>
                  <div class="w-50px text-hex-92846A flex items-center justify-center">{need_lv[index - 1]}</div>
                  <div class="flex items-center justify-center">
                    <div class=" w-248px flex items-center justify-center">
                      {renderList(4, item => {
                        const cur = `${index}-${item}`
                        const detail = (characterStore.specificity as ISpecificityInfo[])?.filter(a => a.position == cur && a.title == title_index.value)?.[0]
                        if (!detail) {
                          return <></>
                        }
                        return (
                          <>
                            <calc-tooltip position="bottom">
                              {{
                                default() {
                                  return (
                                    <>
                                      <div
                                        onClick={() => change_specificity(index - 1, detail)}
                                        class={`mx-10px specificity-icon-${title_index.value}-${detail.index}_${configStore.specificity_list.includes(detail?.id) ? "checked" : "unchecked"}`}
                                        style={props.simple ? "margin:0 !important;" : "transform: scale(1.25);"}
                                      >
                                        <div class={`w-100% h-100% ${configStore.specificity_list.includes(detail?.id) ? `specificity_check_${index == 1 ? 0 : 1}` : ""}`}></div>
                                      </div>
                                    </>
                                  )
                                },
                                popper() {
                                  return (
                                    <div class="min-w-250px m-5px text-hex-9f8d59" style="border:1px soild gray;border-radius:5px">
                                      <div class="text-hex-B0A48C">{detail?.name && `[${detail?.name}]`}</div>
                                      {renderList(detail?.desc, item => (
                                        <div class={`${item.includes("*") ? "text-gray" : ""}`}>{item}</div>
                                      ))}
                                    </div>
                                  )
                                }
                              }}
                            </calc-tooltip>
                          </>
                        )
                      })}
                    </div>
                    <div class="flex flex-col justify-center ml-15px h-90px" style={`width:${props.simple ? 400 : 560}px;${details.value[index - 1] ? "border-top: 1px solid rgba(128,128,128,0.2);" : ""}`}>
                      <div class="min-w-250px m-5px text-hex-9f8d59" style="border:1px soild gray;border-radius:5px">
                        <div class="text-hex-B0A48C">{details.value[index - 1]?.name && `[${details.value[index - 1]?.name}]`}</div>
                        {renderList(details.value[index - 1]?.desc, item => (
                          <div class={`${item.includes("*") ? "text-gray" : ""}`}>{item}</div>
                        ))}
                      </div>
                    </div>
                  </div>
                </div>
              ))}

              {/* {!props.simple && renderList(2, _index => (
                <div class="h-90px flex items-center">
                  <div class="w-50px"></div>
                  <div class="flex">
                    {renderList(4, _item => {
                      return (
                        <>
                          <div class="mx-10px specificity_none" style="mix-blend-mode: luminosity;transform:scale(1.25)"></div>
                        </>
                      )
                    })}
                  </div>
                </div>
              ))} */}
            </div>
          </div>
        </>
      )
    }
  }
})
</script>

<style lang="scss">
.specificity_check_0 {
  background-image: url("@/assets/img/specificity/select_0.png");
  z-index: 10;
}

.specificity_check_1 {
  background-image: url("@/assets/img/specificity/select_1.png");
  z-index: 10;
}

.specificity_none {
  background-image: url("@/assets/img/specificity/none.png");
  width: 49px;
  height: 49px;
}

.bg_specificity {
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
