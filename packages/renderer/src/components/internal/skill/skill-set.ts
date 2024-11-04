import type { ISkillInfo } from "@/api/character/type"

export const skills = new Map<string, ISkillInfoForSkillPanel[]>([
  [
    "通用技能",
    [
      { id: 1, name: "后跳", sp: 0, default: 1, learnMax: 1, learn: 1, master: 1, max: 1, row: 1, col: 1, icon: "https://101.43.64.95/dnfstatic/images/equipment/title/484.png" },
      { id: 2, name: "受身蹲伏", sp: 0, default: 1, learnMax: 1, learn: 1, master: 1, max: 20, row: 1, col: 2, icon: "https://101.43.64.95/dnfstatic/images/equipment/title/484.png" },
      {
        id: 3,
        name: "基础精通",
        tp: { master: 3, max: 5, tp: 1, learn: 0, default: 0 },
        sp: 0,
        default: 110,
        learnMax: 110,
        learn: 110,
        master: 110,
        max: 200,
        row: 1,
        col: 3,
        icon: "https://101.43.64.95/dnfstatic/images/equipment/title/484.png"
      },
      { id: 4, name: "跃翔", sp: 20, default: 0, learnMax: 10, learn: 0, master: 10, max: 20, row: 1, col: 4, icon: "https://101.43.64.95/dnfstatic/images/equipment/title/484.png" },
      { id: 5, name: "暴击", sp: 20, default: 0, learnMax: 10, learn: 0, master: 10, max: 20, row: 1, col: 5, icon: "https://101.43.64.95/dnfstatic/images/equipment/title/484.png" },
      { id: 6, name: "背击", sp: 20, default: 0, learnMax: 10, learn: 0, master: 10, max: 20, row: 1, col: 6, icon: "https://101.43.64.95/dnfstatic/images/equipment/title/484.png" },
      { id: 7, name: "远古记忆", sp: 25, default: 0, learnMax: 10, learn: 0, master: 10, max: 20, row: 1, col: 7, icon: "https://101.43.64.95/dnfstatic/images/equipment/title/484.png" },
      { id: 8, name: "不屈意志", sp: 25, default: 0, learnMax: 10, learn: 0, master: 10, max: 20, row: 1, col: 8, icon: "https://101.43.64.95/dnfstatic/images/equipment/title/484.png" },
      { id: 9, name: "唤醒", sp: 0, default: 1, learnMax: 1, learn: 1, master: 1, max: 1, row: 1, col: 9, icon: "https://101.43.64.95/dnfstatic/images/equipment/title/484.png" }
    ]
  ],
  [
    "重霄·弹药专家·女",
    [
      { id: 18, name: "单兵推进器", sp: 20, default: 1, row: 20, col: 3, before: [{ id: 17, lv: 1 }] },
      { id: 21, name: "兵器研究", sp: 10, default: 0, row: 20, col: 1 },
      { id: 22, name: "弹药改良", sp: 10, default: 1, row: 20, col: 2 },
      { id: 23, name: "手雷精通", sp: 20, default: 0, row: 20, col: 7, before: [{ id: 16, lv: 1 }] },
      { id: 24, name: "M18阔剑地雷", tp: { master: 5, max: 7, tp: 2 }, sp: 25, default: 0, row: 20, col: 9 },
      { id: 25, name: "交叉射击", tp: { master: 5, max: 7, tp: 2 }, sp: 35, default: 0, row: 20, col: 4, before: [{ id: 14, lv: 1 }] },
      { id: 26, name: "G35感电手雷", sp: 35, default: 0, row: 20, col: 6, before: [{ id: 16, lv: 1 }] },
      { id: 28, name: "爆裂弹", sp: 10, default: 0, row: 30, col: 5, before: [{ id: 14, lv: 1 }] },
      { id: 29, name: "G18冰冻手雷", sp: 40, default: 0, row: 30, col: 7, before: [{ id: 26, lv: 1 }] },
      { id: 30, name: "聚合弹", tp: { master: 5, max: 7, tp: 2 }, sp: 35, default: 0, row: 30, col: 4, before: [{ id: 25, lv: 1 }] },
      { id: 31, name: "C4飞弹", tp: { master: 5, max: 7, tp: 2 }, sp: 35, default: 0, row: 30, col: 9 },
      { id: 32, name: "凝固汽油弹", tp: { master: 5, max: 7, tp: 2 }, sp: 50, default: 0, row: 40, col: 4, before: [{ id: 30, lv: 1 }] },
      { id: 33, name: "镭射狙击", tp: { master: 5, max: 7, tp: 2 }, sp: 60, default: 0, row: 40, col: 6, before: [{ id: 26, lv: 1 }] },
      { id: 34, name: "弹药强化", sp: 30, default: 1, row: 50, col: 5 },
      { id: 35, name: "EMP磁暴", sp: 0, default: 0, row: 50, col: 8 },
      { id: 36, name: "G61重力手雷", tp: { master: 5, max: 7, tp: 2 }, sp: 60, default: 0, row: 60, col: 6, before: [{ id: 33, lv: 1 }] },
      { id: 37, name: "制空掌握", sp: 45, default: 1, row: 70, col: 2 },
      { id: 38, name: "轻火力速射", tp: { master: 5, max: 7, tp: 2 }, sp: 70, default: 0, row: 70, col: 4, before: [{ id: 32, lv: 1 }] },
      { id: 39, name: "开火", sp: 80, default: 0, row: 70, col: 8, before: [{ id: 36, lv: 1 }] },
      { id: 40, name: "光子霰雷发射器", sp: 90, default: 0, row: 80, col: 5, before: [{ id: 36, lv: 1 }] },
      { id: 41, name: "决战之日", sp: 0, default: 0, row: 80, col: 7, before: [{ id: 36, lv: 1 }] },
      { id: 42, name: "单兵推进器-02X", sp: 60, default: 0, row: 90, col: 5 },
      { id: 43, name: "空袭战略", sp: 100, default: 0, row: 90, col: 7 },
      { id: 44, name: "终解·制空霸权", sp: [200, 100], default: 0, row: 100, col: 5 }
    ]
  ],
  [
    "知源·冰结师",
    [
      { id: 1, name: "冰结师皮甲专精", default: 1, row: 1, sp: 0, col: 1 },
      { id: 2, name: "不死之身", row: 1, col: 2, sp: 0, default: 1 },
      { id: 3, name: "黑暗之眼", row: 1, col: 3, sp: 0, default: 1 },
      { id: 4, name: "基础防具精通", row: 1, col: 4, sp: 0, default: 1 },
      { id: 7001, name: "魔法水球", row: 1, col: 5, sp: 15, default: 1 },
      { id: 7002, name: "魔法旋风", row: 1, col: 7, sp: 20, default: 1 },
      { id: 7003, name: "擒拿掌", col: 4, sp: 15, row: 5, default: 1 },
      { id: 7004, name: "魔球连射", col: 7, sp: 15, row: 5, default: 0 },
      { id: 7005, name: "幽冥火", col: 3, sp: 15, row: 10, default: 0 },
      { id: 7006, name: "瞬移", col: 6, sp: 25, row: 10, default: 0 },
      { id: 7007, name: "旋火盾", col: 8, sp: 20, row: 10, default: 0 },
      { id: 7008, name: "冰之印", col: 4, sp: 0, row: 15, default: 1 },
      { id: 7009, name: "冰武精通", col: 7, sp: 10, row: 15, default: 0 },
      { id: 7010, name: "冰魄剑", col: 9, sp: 15, row: 15, default: 1 },
      { id: 7011, name: "寒冰连枪", col: 5, sp: 20, row: 20, default: 0 },
      { id: 7012, name: "冰魄旋枪", col: 4, sp: 25, row: 25, default: 0 },
      { id: 7013, name: "冰霜之径", col: 6, sp: 30, row: 25, default: 0 },
      { id: 7014, name: "冰之领悟", col: 8, sp: 20, row: 25, default: 0 },
      { id: 7015, name: "冰魄之弓", col: 3, sp: 30, row: 30, default: 0, before: [{ id: 7012, lv: 1 }] },
      { id: 7016, name: "破冰飞刃", col: 5, sp: 30, row: 30, default: 0, before: [{ id: 7012, lv: 1 }] },
      { id: 7017, name: "寒冰之境", col: 8, sp: 30, row: 30, default: 0, before: [{ id: 7014, lv: 1 }] },
      { id: 7018, name: "水晶剑", col: 9, sp: 30, row: 30, default: 0, before: [{ id: 7010, lv: 1 }] },
      { id: 7019, name: "旋冰穿刺", col: 3, sp: 30, row: 35, default: 0, before: [{ id: 7015, lv: 1 }] },
      { id: 7020, name: "冰魄锤击", col: 5, sp: 40, row: 35, default: 0, before: [{ id: 7016, lv: 1 }] },
      { id: 7021, name: "极冰绽放", col: 5, sp: 20, row: 50, default: 0 },
      { id: 7022, name: "冰雪风暴", col: 4, sp: 60, row: 45, default: 0, before: [{ id: 7021, lv: 1 }] },
      { id: 7023, name: "冰舞乱击", col: 6, sp: 15, row: 45, default: 0, before: [{ id: 7021, lv: 1 }] },
      { id: 7024, name: "千旋冰轮破", col: 6, sp: 0, row: 50, default: 0 },
      { id: 7025, name: "冰封奥义", col: 7, sp: 30, row: 50, default: 1 },
      { id: 7026, name: "冰凌破", col: 6, sp: 60, row: 60, default: 0 },
      { id: 7027, name: "千里冰封", col: 5, sp: 70, row: 70, default: 0 },
      { id: 7028, name: "冰之技艺", col: 7, sp: 45, row: 70, default: 1 },
      { id: 7029, name: "碎冰破", col: 9, sp: 80, row: 70, default: 0 },
      { id: 7030, name: "极冰领域", col: 7, sp: 90, row: 80, default: 0 },
      { id: 7031, name: "永罪冰狱", col: 9, sp: 0, row: 80, default: 0 },
      { id: 7032, name: "冰凝之魂", col: 6, sp: 60, row: 90, default: 1 },
      { id: 7033, name: "极冰猎魔斩", col: 8, sp: 100, row: 90, default: 0 },
      { id: 7034, name: "永劫纳斯特隆德", col: 5, sp: [200, 100], row: 100, default: 0 }
    ]
  ]
])

// 技能树配置模型 - 技能
export interface ISkillInfoForSkillPanel {
  name: string
  id: number
  default?: number
  row: number
  col: number
  before?: ISkillBeforeForSkillPanel[]
  master?: number // 精通
  max?: number // 上限
  learnMax?: number // 学习上限
  learn?: number // 学习，不包括等级加成
  skills?: ISkillInfo
  icon?: string
  y?: number
  sp?: number | number[]
  tp?: ITPSkillInfoForSkillPanel
}

export interface ITPSkillInfoForSkillPanel {
  master?: number // 精通
  max?: number // 上限
  learn?: number // 学习，不包括等级加成
  tp?: number | number[]
  default?: number
}

export interface ISkillBeforeForSkillPanel {
  id: number
  lv: number
}

// 技能树配置模型 - 技能树
export interface ISkillTreeForSkillPanel {
  lv: number
  sks: ISkillInfoForSkillPanel[]
}
