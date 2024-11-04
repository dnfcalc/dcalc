<script lang="tsx">
import { onKeyStroke, useDebounceFn } from "@vueuse/core"
import { defineComponent, ref, renderList } from "vue"
import Cp from "./sub/cp.vue"
import Options from "./sub/options.vue"
import SkillList from "./sub/list.vue"
import Que from "./sub/que.vue"
import { useCharacterStore, useConfigStore } from "@/store"
import Draggable from "@/components/vuedraggable/vuedraggable"
import { useDialog } from "@/components/hooks/dialog"

const upline = ["Q", "W", "E", "R", "T", "Y"]
const downline = ["A", "S", "D", "F", "G", "H"]
const keys = [...upline, "Ctrl", ...downline, "Alt"]
const hotKeys = [...keys, ...upline.concat(downline).map(r => r.toLowerCase()), "Control"]

export default defineComponent({
  setup() {
    const characterStore = useCharacterStore()
    const configStore = useConfigStore()
    const { confirm } = useDialog()

    const skillList = (index: number) => {
      return characterStore.skills.filter(skill => skill.type == 1 && !configStore.hotkey_set.filter((a, b) => b != index).includes(skill.name))
    }

    onKeyStroke(
      hotKeys,
      useDebounceFn(event => {
        event.preventDefault()
        let { key } = event
        if (key.length == 1) {
          key = key.toUpperCase()
        } else if (key == "Control") {
          key = "Ctrl"
        }
        if (characterStore.alter == "dark_knight") {
          const index = [...upline, ...downline].indexOf(key)
          if (index > -1) {
            // 上排技能
            if (index <= 5) {
              const skill_name = configStore.hotkey_set[index]
              if (skill_name) {
                const skill = characterStore.skills.find(skill => skill.name == skill_name)
                if (skill) {
                  configStore.addSkillQueue(skill)
                }
              }
            } else {
              for (let i = 0; i < 5; i++) {
                const skill_name = configStore.hotkey_set[index + i * 6]
                if (skill_name) {
                  const skill = characterStore.skills.find(skill => skill.name == skill_name)
                  if (skill) {
                    configStore.addSkillQueue(skill)
                  }
                }
              }
            }
          }
        } else {
          const index = keys.indexOf(key)
          if (index > -1) {
            const skill_name = configStore.hotkey_set[index]
            if (skill_name) {
              const skill = characterStore.skills.find(skill => skill.name == skill_name)
              if (skill) {
                configStore.addSkillQueue(skill)
              }
            }
          }
        }
      }, 20),
      {}
    )

    // onKeyStroke(
    //   "Backspace",
    //   event => {
    //     event.preventDefault()
    //     resetQueue()
    //   },
    //   {}
    // )

    const colors = ["#fee86b", "#75ae1b", "#1bae83", "#1b63ae", "#b920c3", "c3207c"]

    const changeMode = (skill: { name: string; id: number; mode: string; modes: string[] | undefined }) => {
      return () => {
        let index = skill.modes?.indexOf(skill.mode) ?? 0
        index = index >= 0 ? (index + 1 >= (skill.modes?.length ?? 0) ? 0 : index + 1) : 0
        skill.mode = skill.modes?.[index] ?? ""
      }
    }

    const item = (item: any) => {
      const skill = item.element as { name: string; id: number; mode: string; modes: string[] | undefined }
      return (
        <div
          class="h-7 m-2px w-7"
          title={skill.mode ? `${skill.name}[${skill.mode}]` : skill.name}
          style={"position: relative;"}
          onClick={changeMode(skill)}
        >
          <div style={`${(skill.modes?.length ?? 0) > 0 ? ((skill.modes?.indexOf(skill.mode) ?? 0) > 0 ? `background-color: ${colors[skill.modes?.indexOf(skill.mode) ?? 0]}` : 0) : ""};width:26px;height:26px;top:1px;left:1px;position:absolute;z-index:5;mix-blend-mode: hue;`}></div>
          <div
            class={`character-icon-${characterStore.alter}-${skill.name.replace(/[().·，：]+/g, "")}`}
          />
          {skill.modes && skill.modes.length > 0 && <div class="size-11">{skill.mode}</div>}
        </div>
      // <div class="list-group-item">{item.element.name}</div>
      )
    }

    async function resetQueue() {
      if (configStore.skill_que.length == 0) {
        return
      }
      const rs = await confirm({ content: "请确认要初始化技能队列吗？" })
      if (rs.isOk) {
        configStore.skill_que.length = 0
      }
    }

    const setsVisible = ref(false)

    const hotkey = () => {
      if (characterStore.alter == "dark_knight") {
        return (
          <>
            {
            // 上排技能
              renderList(upline, (item, i) => (
                <div class="h-7 m-1.5 w-7 skill-slot-item relative">
                  <calc-iconselect columnNum={6} v-model={configStore.hotkey_set[i]}>
                    <calc-option class="bg-hex-000000 h-28px w-28px items-center justify-center !flex" value=""></calc-option>
                    <calc-option class="bg-hex-000000 h-28px w-28px items-center justify-center !flex" value="其它">
                        其它
                    </calc-option>
                    {renderList(skillList(i), skill => (
                      <calc-option value={skill.name}>
                        <div class={`character-icon-${characterStore.alter}-${skill.name.replace(/[().·，：]+/g, "")}`} />
                      </calc-option>
                    ))}
                  </calc-iconselect>
                  <div class="right-0 bottom--.5 absolute ">{upline[i]}</div>
                </div>
              ))
            }
            <div class="w-full pl-4 h-5 flex items-center">连击技能</div>
            {renderList(5, row => (
              <>
                {renderList(downline, (item, i) => (
                  <div class="h-8 m-1.5 w-8 skill-slot-item relative">
                    <calc-iconselect columnNum={6} v-model={configStore.hotkey_set[6 * row + i]}>
                      <calc-option class="bg-hex-000000 h-28px w-28px items-center justify-center !flex" value=""></calc-option>
                      {renderList(skillList(6 * row + i), skill => (
                        <>
                          {skill.need_level != 85 && skill.need_level != 100 && (
                            <calc-option value={skill.name}>
                              <div class={`character-icon-${characterStore.alter}-${skill.name.replace(/[().·，：]+/g, "")}`} />
                            </calc-option>
                          )}
                        </>
                      ))}
                    </calc-iconselect>
                    <div class="right-0 bottom--.5 absolute">{downline[i]}</div>
                  </div>
                ))}
              </>
            ))}
          </>
        )
      } else {
        return renderList(keys, (item, i) => (
          <div class="h-7 m-1 w-7 skill-slot-item relative">
            <calc-iconselect columnNum={5} v-model={configStore.hotkey_set[i]}>
              <calc-option class="bg-hex-000000 h-28px w-28px items-center justify-center !flex" value=""></calc-option>
              <calc-option class="bg-hex-000000 h-28px w-28px items-center justify-center !flex" value="其它">
                  其它
              </calc-option>
              {renderList(skillList(i), skill => (
                <calc-option value={skill.name}>
                  <div class={`character-icon-${characterStore.alter}-${skill.name.replace(/[().·，：]+/g, "")}`} />
                </calc-option>
              ))}
            </calc-iconselect>
            <div class="right-0 bottom--.5 absolute">{keys[i]}</div>
          </div>
        ))
      }
    }

    return () => (
      <div class="flex space-x-4 py-2 px-4 character">
        <calc-dialog lazy header="技能队列快捷设置" v-model:visible={setsVisible.value}>
          <Que></Que>
        </calc-dialog>
        <div class="flex p-1">
          <SkillList></SkillList>
        </div>

        <div class="w-70">
          <div class="h-220px subitem isolate">
            <Cp></Cp>
          </div>
          {characterStore.is_delear && (
            <>
              <div class="mt-1 subitem">
                <div class="head-sec">快捷键</div>
                <div class="py-2 px-1 body-sec ">
                  <div class="flex flex-wrap flex-1 w-full justify-center">{hotkey()}</div>
                </div>
              </div>
              <div class="mt-1 w-full">
                <div class="h-70 skill-slots subitem  overflow-y-auto">
                  <div class="flex px-1 head-sec items-center justify-between">
                    <div class="w-11"></div>
                    <div>技能队列</div>
                    <div class="flex">
                      <calc-button onClick={resetQueue} icon="reset" title="初始化(Backspace)"></calc-button>
                      <calc-button onClick={() => (setsVisible.value = true)} icon="set" title="形态快捷设置"></calc-button>
                    </div>
                  </div>
                  <div class="body-sec">
                    <Draggable class="flex flex-wrap isolate" v-model:list={configStore.skill_que} itemKey="id">
                      {{
                        item
                      }}
                    </Draggable>
                  </div>
                </div>
              </div>
            </>
          )}
        </div>

        <div class="w-79">
          <Options></Options>
        </div>
      </div>
    )
  }
})
</script>

<style lang="scss">
.skill-slot-item {
    height: 28px;
    width: 28px;
    background-color: black;
    border: rgb(29, 29, 29) solid 1px;
    .i-icon-select .i-select-trigger {
      padding-top: 1px !important;
    }
  }
  .size-11 {
    position: absolute;
    top: -5px;
    right: -5px;
    font-size: 12px;
    transform: scale(0.7);
    text-wrap: nowrap;
    color: white;
    text-shadow: 0 0 1px #000, 0 0 1px #000, 0 0 1px #000, 0 0 1px #000,
    0 0 1px #000, 0 0 1px #000, 0 0 1px #000, 0 0 1px #000, 0 0 1px #000,
    0 0 1px #000, 0 0 1px #000, 0 0 1px #000, 0 0 1px #000, 0 0 1px #000,
    0 0 1px #000, 0 0 1px #000, 0 0 1px #000, 0 0 1px #000, 0 0 1px #000,
    0 0 1px #000, 0 0 1px #000, 0 0 1px #000, 0 0 1px #000, 0 0 1px #000,
    0 0 1px #000, 0 0 1px #000, 0 0 1px #000, 0 0 1px #000, 0 0 1px #000,
    0 0 1px #000, 0 0 1px #000, 0 0 1px #000, 0 0 1px #000, 0 0 1px #000;
    -webkit-font-smoothing: antialiased;
  }
</style>
