from typing import Union
from xmlrpc.client import Boolean

from core.basic.skill import 主动技能, 技能, 被动技能


class CharacterProperty:

    评分: float = 0

    类型: str

    适用属性: str = "智力"

    def 基础属性加成(self,
               物理攻击力=0.00, 魔法攻击力=0.00, 独立攻击力=0.00, 三攻=0.00,
               力量=0.00, 智力=0.00, 力智=0.00, 体力=0.00, 精神=0.00, 体精=0.00, 四维=0.00,
               物理暴击率=0.00, 魔法暴击率=0.00, 暴击率=0.00,
               攻击速度=0.00, 施放速度=0.00, 移动速度=0.00, 三速=0.00, 火属性抗性=0, 光属性抗性=0, 冰属性抗性=0, 暗属性抗性=0, 所有属性抗性=0, 所有异常抗性=0, 所有职业异常抗性=0, 进图力量=0.00, 进图智力=0.00, **kwargs):
        物理攻击力 += 三攻
        魔法攻击力 += 三攻
        独立攻击力 += 三攻

        力量 += 力智 + 四维 + 进图力量
        智力 += 力智 + 四维 + 进图智力
        体力 += 体精 + 四维
        精神 += 体精 + 四维

        物理暴击率 += 暴击率
        魔法暴击率 += 暴击率

        if (self.类型 == "辅助"):
            if (self.适用属性 == '体力'):
                if (体力 > 0):
                    self.评分 += 体力 * 15
            elif (self.适用属性 == '精神'):
                if (精神 > 0):
                    self.评分 += 精神 * 15
            elif (self.适用属性 == '智力'):
                if (智力 > 0):
                    self.评分 += 智力 * 15
        elif (self.类型 == "物理百分比"):
            if 力量 > 0:
                self.评分 += 力量 * 5
            if 物理攻击力 > 0:
                self.评分 += 物理攻击力 * 10
            if 物理暴击率 > 0:
                self.评分 += 物理暴击率
        elif (self.类型 == "魔法百分比"):
            if 智力 > 0:
                self.评分 += 智力 * 5
            if 魔法攻击力 > 0:
                self.评分 += 魔法攻击力 * 10
            if 魔法暴击率 > 0:
                self.评分 += 魔法暴击率
        elif (self.类型 == "物理固伤"):
            if 力量 > 0:
                self.评分 += 力量 * 5
            if 独立攻击力 > 0:
                self.评分 += 独立攻击力 * 10
            if 物理暴击率 > 0:
                self.评分 += 物理暴击率
        elif self.类型 == "魔法固伤":
            if 智力 > 0:
                self.评分 += 智力 * 5
            if 独立攻击力 > 0:
                self.评分 += 独立攻击力 * 10
            if 魔法暴击率 > 0:
                self.评分 += 魔法暴击率
        pass

    def 攻击强化加成(self, x=0):
        if self.类型 != "辅助":
            self.评分 += x * 1000
        pass

    def 百分比攻击强化加成(self, x=0.0):
        if self.类型 != "辅助":
            self.评分 = (self.评分 + 2000) * (1 + x * 1000)

    def 技能攻击力加成(self, x=0, 辟邪玉加成=1, 适用累加=1, part='', show=True):
        if self.类型 != "辅助":
            self.评分 = (self.评分 + 2000) * (1 + x * 2000)

    def 辅助属性加成(self, buff固定力智=0, buff百分比力智=0.0, buff固定三攻=0, buff百分比三攻=0.0, 觉醒固定力智=0, 觉醒百分比力智=0.0, buff量=0, 百分比buff量=0.0):
        if self.类型 == '辅助':
            self.评分 += buff固定力智
            self.评分 *= 1.0 + buff百分比力智
            self.评分 += buff固定三攻
            self.评分 *= 1.0 + buff百分比三攻
            self.评分 += 觉醒固定力智
            self.评分 *= 1.0 + 觉醒百分比力智
            self.评分 += buff量 / 100
            self.评分 *= 1.0 + 百分比buff量

    def 技能等级加成(self, 加成类型: str, min: int, max: int, lv: int, exc=[],excName=[]) -> None:
        if self.类型 == "辅助":
            if 加成类型 == '主动':
                if min < 30 and max >= 30:
                    self.评分 += 2000 * (lv + 1)
                if min <= 50 and max >= 50:
                    self.评分 += 1000 * (lv + 1)

        if 加成类型 == '所有':
            self.评分 += 1000 * (lv + 1)

        self.评分 += 100 * (lv + 1)
        pass

    def 评分开始(self):
        self.评分 = 0

    def 评分结束(self):
        评分 = self.评分
        self.评分 = 0
        return 评分
    #     def get_skill_by_name(self, name) -> 技能 | 主动技能 | 被动技能:

    def get_skill_by_name(self, name) -> Union[技能, 主动技能, 被动技能]:
        pass

    def 已穿戴神话(self):
        pass

    def 穿戴低于105(self):
        pass

    def 获取强化等级(self, part=[]):
        pass

    def 获取改造等级(self, part=[]):
        pass

    def check_fun_by_id(self, id: int) -> Boolean:
        pass

    def check_equ_by_name(self, name: str) -> Boolean:
        pass

    # region 词条属性

    def set_eq_params(self,key,value):
        pass

    def get_eq_params(self,key)-> float:
        pass

    def 基础精通加成(self, x: float) -> None:
        pass

    def 百分比防御减少(self, x: float) -> None:
        pass

    def 固定防御减少(self, x: int) -> None:
        pass

    def 伤害类型转化(self, 类型1: str, 类型2: str, x: float) -> None:
        pass

    def 异常增伤(self, 类型: str, x: float) -> None:
        pass

    def 异常抗性加成(self, 类型: str, x: float, mode: int = 1) -> None:
        pass

    def 异常抗性获取(self, 类型: str, mode: int = 1) -> float:
        pass

    def 属性攻击(self, 类型: str) -> None:
        pass

    def 所有异常抗性加成(self, x: float) -> None:
        pass

    def 条件技攻加成(self, 类型: str, x: float) -> None:
        pass

    def 条件冷却加成(self, 类型: str, x: float) -> None:
        pass

    def 条件冷却恢复加成(self, 类型: str, x: float) -> None:
        pass

    def 指令效果加成(self, 类型: str, x: float) -> None:
        pass

    def 指令技攻加成(self, x: float, min=1, max=100, exc=[50, 85, 100],excName=[]) -> None:
        pass

    def MP消耗量加成(self, x: float) -> None:
        pass

    def buff量加成(self, x: float) -> None:
        pass

    def 附加伤害加成(self, x: float, 辟邪玉加成=1) -> None:
        pass

    def 持续伤害加成(self, x: float) -> None:
        pass

    def 属性附加加成(self, x: float) -> None:
        pass

    def 暴击伤害加成(self, x: float, 辟邪玉加成=1) -> None:
        pass

    def 伤害增加加成(self, x: float, 辟邪玉加成=1) -> None:
        pass

    def 最终伤害加成(self, x: float, 辟邪玉加成=1) -> None:
        pass

    def 百分比力智加成(self, x: float, 辟邪玉加成=1) -> None:
        pass

    def 百分比三攻加成(self, x: float, 辟邪玉加成=1) -> None:
        pass

    def 火属性强化加成(self, x: float, 辟邪玉加成=1, mode=0) -> None:
        pass

    def 冰属性强化加成(self, x: float, 辟邪玉加成=1, mode=0) -> None:
        pass

    def 光属性强化加成(self, x: float, 辟邪玉加成=1, mode=0) -> None:
        pass

    def 暗属性强化加成(self, x: float, 辟邪玉加成=1, mode=0) -> None:
        pass

    def 所有属性强化加成(self, 所有属性强化=0, 火属性强化=0, 冰属性强化=0, 光属性强化=0, 暗属性强化=0, 辟邪玉加成=1, mode=0) -> None:
        if self.类型 != '辅助':
            光属性强化 += 所有属性强化
            暗属性强化 += 所有属性强化
            火属性强化 += 所有属性强化
            冰属性强化 += 所有属性强化
            self.评分 += max(光属性强化, 暗属性强化, 火属性强化, 冰属性强化) * 100
        pass

    def 火属性抗性加成(self, x: int) -> None:
        pass

    def 冰属性抗性加成(self, x: int) -> None:
        pass

    def 光属性抗性加成(self, x: int) -> None:
        pass

    def 暗属性抗性加成(self, x: int) -> None:
        pass

    def 所有属性抗性加成(self, x: int) -> None:
        pass

    def 攻击速度增加(self, x: float, part: str = '') -> None:
        pass

    def 攻击速度(self) -> float:
        pass

    def 移动速度增加(self, x: float) -> None:
        pass

    def 施放速度增加(self, x: float) -> None:
        pass

    def 所有速度增加(self, x: float, part: str = '') -> None:
        pass

    def 命中率增加(self, x: float) -> None:
        pass

    def 回避率增加(self, x: float) -> None:
        pass

    def 物理暴击率增加(self, x: float) -> None:
        pass

    def 魔法暴击率增加(self, x: float) -> None:
        pass

    def 暴击率增加(self, x: float) -> None:
        pass

    def buff技能等级加成(self, LV: int, lv: int) -> None:
        pass

    def 特殊主动等级加成(self, Lv: int, lv: int) -> None:
        pass

    def 技能获取(self, min: int, max: int, exc=[]) -> None:
        pass

    def 技能冷却缩减(self, min: int, max: int, x: float, exc=[],excName=[]) -> None:
        pass

    def 加算冷却缩减(self, x: float) -> None:
        pass

    def 技能恢复加成(self, min: int, max: int, x: float, exc=[],excName=[]) -> None:
        pass

    def 技能倍率加成(self, min: int, max: int, x: float, exc=[], type="all",excName=[],changeSkill = False) -> None:
        pass

    def 单技能加成(self, 名称: str, 倍率=1.0, CD=1.0, lv=0) -> None:
        pass

    def __所有属性强化(self, x: float) -> None:
        pass

    def 斗神宠物加成(self, x: float) -> None:
        pass

    # endregion
