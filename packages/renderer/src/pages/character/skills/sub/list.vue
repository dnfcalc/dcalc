<script lang="tsx">
import { defineComponent, renderList } from "vue"
import type { ISkillInfo } from "@/api/character/type"
import { useCharacterStore, useConfigStore } from "@/store"

function skill_tooltip(skill: ISkillInfo) {
  if (skill.type == 1) {
    return (
      <div class="tooltip-skill">
        <div class="name">
          {skill.name} Lv {skill.current_level}
        </div>
        <div class="text-right info">冷却时间:{skill.cooldown}秒</div>
        <div class="info">学习等级:{+skill.need_level}</div>
        <div class="info">精通等级:{+skill.level_master}</div>
        <div class="info">上限等级:{+skill.level_max}</div>
        <div class="info">技能倍率:{+skill.data.toFixed(0)}%</div>
      </div>
    )
  } else {
    return (
      <div class="tooltip-skill">
        <div class="name-p">
          {skill.name} Lv {skill.current_level}
        </div>
        <div class="info">学习等级:{+skill.need_level}</div>
        <div class="info">精通等级:{+skill.level_master}</div>
        <div class="info">上限等级:{+skill.level_max}</div>
      </div>
    )
  }
}

export default defineComponent({
  name: "Skill",
  components: {},
  setup() {
    const characterStore = useCharacterStore()
    const configStore = useConfigStore()

    configStore.skill_set = characterStore.skills
      .sort((a, b) => a.need_level - b.need_level)
      .map(item => {
        const temp = configStore.skill_set.find(r => r.name == item.name)
        return temp || { name: item.name, tp: 0, count: 0, pet: 0, direct: false, level: item.current_level, directNumber: 0, damage: item.type == 1, mode: item.mode };
      })

    function highlight(index: number) {
      if (configStore.skill_set[index].level > characterStore.skills[index].current_level) {
        return "warn"
      }
      if (configStore.skill_set[index].level < characterStore.skills[index].current_level) {
        return "remind"
      }
    }

    function skillTips(index: number) {
      const minus = configStore.skill_set[index].level - characterStore.skills[index].current_level
      if (minus != 0) {
        return `${minus > 0 ? "超出" : "低于"}标准Lv${Math.abs(minus)}`
      }
    }

    const skillQueChange = (skill: ISkillInfo) => {
      return (event: any) => {
        const count = Number(event.target.value)
        const indexs = configStore.skill_que
          .map((s, i) => (s.name == skill.name ? i : -1))
          .filter(i => i > -1)
          .sort((a, b) => b - a)
        if (indexs.length > count) {
          // 删除后几位
          for (let i = 0; i < indexs.length - count; i++) {
            configStore.skill_que.splice(indexs[i] as number, 1)
          }
        } else {
          for (let i = 0; i < count - indexs.length; i++) {
            configStore.addSkillQueue(skill)
          }
        }
      }
    }

    function getCount(skill_name: string) {
      return configStore.skill_que.filter(r => r.name == skill_name).length
    }

    return () => (
      <div class="flex">
        {characterStore.is_delear && (
          <div class="flex-column">
            <div class="flex h-31px items-center">
              <div class="w-28px">技能</div>
              <div class="text-center w-50px !ml-10px">Lv</div>
              <div class="text-center w-50px !ml-5px">TP</div>
              {
                <div class="text-center w-50px !ml-5px">次数</div>
                // <div class="text-center w-50px !ml-5px">宠物次数</div>
              }
              <div class="text-center w-68px !ml-10px">手搓相关</div>
            </div>
            {renderList(
              characterStore.skills.sort((a, b) => a.need_level - b.need_level),
              (skill, index) =>
                skill.type == 1 && (
                  <div class="flex mt-3px mb-3px items-center">
                    <div>
                      <calc-tooltip position="right" offset={5}>
                        {{
                          default() {
                            return <div class={`character-icon-${characterStore.alter}-${skill.name.replace(/[().·，：]+/g, "")}`} />
                          },
                          popper() {
                            return skill_tooltip(skill)
                          }
                        }}
                      </calc-tooltip>
                    </div>
                    <calc-select v-model={configStore.skill_set[index].level} title={skillTips(index)} highlight={highlight(index)} class="!h-20px !ml-10px !min-w-45px !w-45px">
                      {renderList(skill.level_max + 1, item => (
                        <calc-option value={item - 1}>
                          <span>{item - 1}</span>
                        </calc-option>
                      ))}
                    </calc-select>
                    {(skill.tp_max as number) > 0 ? (
                      <calc-select v-model={configStore.skill_set[index].tp} class="!h-20px !ml-5px !min-w-45px !w-45px">
                        {renderList((skill.tp_max as number) + 1, item => (
                          <calc-option value={item - 1}>
                            <span>{item - 1}</span>
                          </calc-option>
                        ))}
                      </calc-select>
                    ) : (
                      <div class="!h-20px !ml-5px !w-50px"></div>
                    )}
                    {
                      // <calc-select modelValue={getCount(skill.name)} onChange={skillQueChange(skill)} class="!h-20px !ml-5px !min-w-45px !w-45px">
                      //   {renderList(100, item => (
                      //     <calc-option value={item - 1}>
                      //       <span>{item - 1}</span>
                      //     </calc-option>
                      //   ))}
                      // </calc-select>
                      <calc-autocomplete onChange={skillQueChange(skill)} class="!h-20px !ml-5px !min-w-45px !w-45px" modelValue={getCount(skill.name)}></calc-autocomplete>
                    }
                    <div class="w-20px justify-center !ml-5px">
                      <calc-checkbox v-model={configStore.skill_set[index].direct}></calc-checkbox>
                    </div>

                    <calc-select v-model={configStore.skill_set[index].directNumber} disabled={!configStore.skill_set[index].direct} class={"!w-45px !min-w-45px !h-20px !mr-5px"}>
                      {renderList(5, item => (
                        <calc-option value={item - 1}>
                          <span>{item - 1}</span>
                        </calc-option>
                      ))}
                    </calc-select>
                  </div>
                )
            )}
          </div>
        )}
        <div class="flex-column w-150px">
          <div class="h-31px"></div>
          {renderList(
            characterStore.skills,
            (skill, index) =>
              skill.type == 0 && (
                <div class="flex mt-3px  mb-3px items-center justify-center">
                  <div>
                    <calc-tooltip position="right" offset={5}>
                      {{
                        default() {
                          return <div class={`character-icon-${characterStore.alter}-${skill.name.replace(/[().·，：]+/g, "")}`} />
                        },
                        popper() {
                          return skill_tooltip(skill)
                        }
                      }}
                    </calc-tooltip>
                  </div>
                  <calc-select v-model={configStore.skill_set[index].level} highlight={highlight(index)} class={"!w-45px !min-w-45px !h-20px !ml-10px"}>
                    {renderList(skill.level_max + 1, item => (
                      <calc-option value={item - 1}>
                        <span>{item - 1}</span>
                      </calc-option>
                    ))}
                  </calc-select>
                </div>
              )
          )}
          {characterStore.is_delear && (
            <div class="flex mt-20px items-center justify-center">
              <div class={`character-icon-${characterStore.alter}-BUFF`} />
              <calc-autocomplete class="ml-10px !min-w-45px !w-50px" v-model={configStore.buff_ratio}></calc-autocomplete>
            </div>
          )}
        </div>
      </div>
    )
  }
})
</script>

<style lang="scss">
  .waken::after {
    content: "";
    width: 38px;
    height: 50px;
    position: absolute;
    top: 0;
    left: 0;
    background-color: rgba(0, 0, 0, 0.4);
  }
</style>
