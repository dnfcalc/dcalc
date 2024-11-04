<script lang="tsx">
import { computed, defineComponent, renderList } from "vue"

import { useCharacterStore, useConfigStore } from "@/store"
export default defineComponent({
  name: "Cp",
  props:{
    edit: {
      type: Boolean,
      default: true
    }
  },

  setup(props) {
    // 紫 红 绿 蓝
    const runeColor = ["#a128f4", "red", "green", "#006bff", "orange"]
    const characterStore = useCharacterStore()
    const configStore = useConfigStore()

    const talismanList = computed(() => {
      return (index: number): string[] => {
        return characterStore.talisman?.filter(a => !configStore.talisman_set.filter((b, c) => c != index).includes(a)) ?? []
      }
    })
    return () => (
      <div>
        {props.edit && <div class="head-sec">护石设置</div>}
        <div class="body-sec">
          {renderList(3, item => (
            <div>
              <div class="cp">
                <calc-iconselect disabled={!props.edit} class="talisman" emptyLabel="点击" columnNum={1} v-model={configStore.talisman_set[item - 1]}>
                  {renderList(talismanList.value(item - 1), (talisman) => (
                    <calc-option value={talisman}>
                      <div class={`character-icon-${characterStore.alter}-${talisman.replace(/[().·，：]+/g, "")}`} />
                    </calc-option>
                  ))}
                </calc-iconselect>
                {renderList(3, runeItem => (
                  <calc-iconselect disabled={!props.edit} emptyLabel="点击" columnNum={5} class="rune" v-model={configStore.rune_set[(item - 1) * 3 + runeItem - 1]}>
                    {renderList(characterStore.rune, (rune) => (
                      <>
                        {renderList(runeColor.length, colorindex => (
                          <>
                            <calc-option value={rune + colorindex}>
                              <div style="position: relative;display: inline-block;">
                                <div style={`background-color: ${runeColor[colorindex - 1]}; width:26px;height:26px;top:1px;left:1px;position:absolute;z-index:5;mix-blend-mode: hue;opacity`}>
                                </div>
                                <div style="filter:brightness(1) contrast(1) saturate(1.5)" class={`character-icon-${characterStore.alter}-${rune.replace(/[().·，：]+/g, "")}`} />
                              </div>
                            </calc-option>
                          </>
                        ))}
                      </>
                    ))}
                  </calc-iconselect>
                ))}
              </div>
            </div>
          ))}
        </div>
      </div>
    )
  }
})
</script>

<style lang="scss">
  .cp {
    background-image: url("@/assets/img/talisman.png");
    height: 52px;
    width: 168px;
    margin: 0 auto;
    margin-top: 5px;
    display: flex;
    .talisman {
      width: 28px;
      margin-left: 9px;
      margin-top: 11px;
    }
    .rune {
      width: 28px;
      margin-left: 5px;
      margin-top: 12px;
    }
    .rune:nth-child(2) {
      margin-left: 21px;
    }

    .i-select-label{
      padding-top: 2px;
    }
  }
</style>
