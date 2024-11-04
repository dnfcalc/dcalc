<script lang="tsx">
import { defineComponent, onMounted, reactive, renderList } from "vue"
import SkillIcon from "./skill-icon.vue"
import type { ISkillInfoForSkillPanel, ISkillTreeForSkillPanel } from "./skill-set";
import { skills as spSkills } from "./skill-set"
import type { ICharacterInfo } from "@/api/character/type"
import { useCharacterStore } from "@/store"


interface IConfigForSkillPanel {
  ey: number
  ex: number
  sy: number
  sx: number
  s: ISkillInfoForSkillPanel
  b: ISkillInfoForSkillPanel
}

export default defineComponent({
  name: "SkillPanel",
  components: { SkillIcon },
  props: {
    character: {
      type: String,
      default: "重霄·弹药专家·女"
    }
  },
  setup(props) {
    const skills = reactive<ISkillTreeForSkillPanel[]>([])
    const baseSkills = reactive<ISkillInfoForSkillPanel[]>([])

    async function initSkills() {
      const characterInfoState = useCharacterStore()
      const basicInfo = characterInfoState[props.character]?.basicInfo as ICharacterInfo

      const sks = spSkills.get(props.character)
      if (sks && sks.length > 0) {
        for (const item of sks) {
          const tk = basicInfo.skills.find(x => x.name == item.name)
          if (tk) {
            item.master = tk.level_master
            item.max = tk.level_max
            item.learnMax = tk.current_level
            item.skills = tk
            item.icon = `/images/characters/${props.character}/skill/${item.name}.png`
          } else {
            // 这里需要修改成一个默认图标
            item.icon = "https://101.43.64.95/dnfstatic/images/equipment/title/484.png"
          }

          if (item.tp) {
            item.tp.learn = 0
            item.tp.default = 0
          }

          let ios = skills.find(x => x.lv == item.row)
          if (!ios) {
            ios = { lv: item.row, sks: [] }
            skills.push(ios)
          }
          ios.sks.push(item)
        }
      }

      const bks = spSkills.get("通用技能")
      if (bks && bks.length > 0) {
        for (const item of bks) {
          baseSkills.push(item)
        }
      }
    }

    function initDrawData() {
      const ss = [] as ISkillInfoForSkillPanel[]
      const data = [] as IConfigForSkillPanel[]
      let scjx = null
      for (let i = 0; i < skills.length; i++) {
        const group = skills[i]
        for (const s of group.sks) {
          if (s.before) {
            for (const bb of s.before) {
              const b = ss.find(x => x.id == bb.id)
              if (b) {
                data.push({
                  ey: i,
                  ex: s.col,
                  sy: b.y ?? 0,
                  sx: b.col,
                  s,
                  b
                })
              }
            }
          }
          s.y = i
          s.learn = s.learnMax
          ss.push(s)
        }

        if (group.lv == 100) {
          scjx = group
        }
      }
      return { data, scjx }
    }

    const config = {
      cols: 11, // 总列数
      lineW: 6, // 连线宽度
      marginLeft: 30, // 左侧等级标识列宽度
      row: {
        h: 56 + 10 + 10, // 单元格高度 + 单元格上下间距
        padding: 10, // 单元格上下间距

        w: 36 + 20, // 单元格宽度 : icon 宽度 + 间距
        margin: 20 // 单元格左右间距
      },
      icon: {
        ih: 56, // 74, // icon 高度
        iw: 36 // icon 宽度
      }
    }

    async function draw() {
      await initSkills()

      const canvas = document.querySelector("#canvas-for-skill-back") as HTMLCanvasElement
      const ctx = canvas.getContext("2d")
      canvas.width = config.cols * config.row.w + config.marginLeft
      canvas.height = skills.length * config.row.h
      if (ctx) {
        for (let i = 0; i < skills.length; i++) {
          ctx.fillStyle = i % 2 == 0 ? "rgba(0, 0, 0, 0.3)" : "rgba(30, 30, 30, 0.3)"
          ctx.fillRect(0, i * config.row.h, canvas.width, config.row.h)
        }
        ctx.fillStyle = "#593D22"
        const { data } = initDrawData()

        // 绘制前置技能连线
        for (const item of data) {
          let x = (item.sx - 1) * config.row.w + config.icon.iw / 2 + config.marginLeft - config.lineW / 2 + 1
          let y = item.sy * config.row.h + (config.row.h - config.row.padding) // - 18;
          const h = (item.ey - item.sy) * config.row.h - config.icon.ih - config.lineW // + 18;
          let w = (item.ex - item.sx) * config.row.w

          if (h < 0) {
            x = x + config.icon.iw / 2 + config.lineW / 2
            y = y + h / 2
            w = w - config.icon.iw - config.lineW
            ctx.fillRect(x, y, w, config.lineW)

            ctx.beginPath()
            ctx.moveTo(x + w, y - config.lineW + 1)
            ctx.lineTo(x + w, y + config.lineW * 2 - 1)
            ctx.lineTo(x + w + config.lineW, y + config.lineW / 2)
            ctx.closePath()
            ctx.fill()
          } else {
            ctx.fillRect(x, y, config.lineW, h / 2)
            ctx.fillRect(x, y + h / 2, w, config.lineW)
            ctx.fillRect(x + w, y + h / 2, config.lineW, h / 2)

            ctx.beginPath()
            ctx.moveTo(x + w - config.lineW + 1, y + h)
            ctx.lineTo(x + w + config.lineW * 2 - 1, y + h)
            ctx.lineTo(x + w + config.lineW / 2, y + h + config.lineW)
            ctx.closePath()
            ctx.fill()
          }
        }
        // 绘制三次觉醒技能连线
        // let item = scjx;
        // let x = (item.sx - 1) * config.row.w + config.icon.iw / 2 + config.marginLeft - config.lineW / 2 + 1;
        // let y = item.sy * config.row.h + (config.row.h - config.row.padding);
        // let h = (item.ey - item.sy) * config.row.h - config.icon.ih - config.lineW;
        // let w = (item.ex - item.sx) * config.row.w;
        // x = x + config.icon.iw / 2 + config.lineW / 2;
        // y = y + h / 2;
        // w = w - config.icon.iw - config.lineW
        // ctx.fillRect(x, y, w, config.lineW);
      }
    }

    onMounted(draw)

    return () => {
      return (
        <div class="skill-panel">
          <div class="skill-types">
            <div class="skill-type-item">SP技能学习</div>
            <div class="skill-type-item">TP技能学习</div>
          </div>
          <div class="base-skill-panel">
            <div class="skills-group" style={`height: ${config.row.h}px`}>
              <div class="lv-tips">1</div>
              {renderList(baseSkills, (s) => (
                <skill-icon skill={s} class="skill-item" style={`left: ${(s.col - 1) * config.row.w + config.marginLeft}px`}></skill-icon>
              ))}
            </div>
          </div>
          <div>
            <canvas id="canvas-for-skill-back"></canvas>
            {renderList(skills, skm => (
              <div class="skills-group" style={`height: ${config.row.h}px`}>
                <div class="lv-tips">{skm.lv % 10 == 0 || skm.lv == 1 ? skm.lv : ""}</div>
                {renderList(skm.sks, (s) => (
                  <skill-icon skill={s} class="skill-item" style={`left: ${(s.col - 1) * config.row.w + config.marginLeft}px`}></skill-icon>
                ))}
              </div>
            ))}
          </div>
          <div></div>
        </div>
      )
    }
  }
})
</script>

<style scoped lang="scss">
  .skill-panel {
    position: relative;
    // font-size: 12px;

    .skill-types {
      display: flex;
      .skill-type-item {
        width: 200px;
        border: 1px solid #221a05;
        margin-right: 5px;
        padding: 5px;
      }
    }

    .skills-group {
      position: relative;

      .lv-tips {
        padding: 10px;
        position: absolute;
      }

      .skill-item {
        position: absolute;
        top: 10px;
      }
    }

    #canvas-for-skill-back {
      float: left;
    }
  }
</style>
