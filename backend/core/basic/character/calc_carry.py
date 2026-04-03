from ..formula import 获取基础属性
from core.basic.property import CharacterInfo
from .base import CharacterBase


class CalcCarryMixin(CharacterBase):
    """输出角色技能伤害计算相关方法"""

    # region 输出计算项

    def calc_damage_ration(self, DSB: bool, BUFF: bool):
        """计算属性系数"""
        attrs = []
        if self.输出类型 == '物理百分比':
            attrs.extend(['STR', 'AtkP', 'PAtkP'])
        if self.输出类型 == '魔法百分比':
            attrs.extend(['INT', 'AtkM', 'PAtkM'])
        if self.输出类型 == '物理固伤':
            attrs.extend(['STR', 'AtkI', 'PAtkI'])
        if self.输出类型 == '魔法固伤':
            attrs.extend(['INT', 'AtkI', 'PAtkI'])
        # 力智系数
        value0_1 = getattr(self, attrs[0])
        value0_2 = 获取基础属性(self.角色, self.职业)[0] if attrs[0] == 'STR' else 获取基础属性(self.角色, self.职业)[1]
        # 系统奶及奶系增幅
        value = value0_1 + ((value0_1 - value0_2) * 3.08 + 2886) * (1 if DSB else 0) + (170000 + 300000) * (1 if BUFF else 0)
        ratio_0: float = value / 250 + 1
        # 物理/魔法/独立攻击力
        ratio_1: float = getattr(self, attrs[1]) + 30000 * (1 if BUFF else 0)
        # 技能 物理/魔法/独立攻击力%
        ratio_2: float = getattr(self, attrs[2])
        # 属强系数
        ratio_3 = max(self.ElementDB.values()) * 0.0045 + 1.05
        # 暴击系数
        ratio_4 = 1.5
        # BUFF系数
        ratio_5 = self.buff
        # 技攻系数
        ratio_6 = self.SkillAttack * (self.jade_effect.SkillAttack + 1)
        # 攻击强化
        ratio_7 = 1 + self.Attack / 100 * (self.AttackP + self.jade_effect.AttackP)
        # 防御系数，暂定145沙袋防御
        monster_defense = 81417275817
        ratio_8 = 1 - monster_defense / (monster_defense + 200 * 100)
        # 杂项
        ratio_9 = 1.0 * self.ElementIncrease
        return (ratio_0, ratio_1, ratio_2, ratio_3, ratio_4, ratio_5, ratio_6, ratio_7, ratio_8, ratio_9)

    def calc_carry_skills(self, DSB: bool, BUFF: bool):
        skillInfos = []
        for i in self.skills:
            if i.damage and i.lv > 0:
                for mode in i.mode:
                    temp = i.skillInfo(mode)
                    if temp[0] > 0:
                        skillInfos.append(
                            {
                                'name': i.name,
                                'icon': i.icon,
                                'lv': i.lv,
                                'data': temp[0],
                                'ratio': temp[1],
                                'cd': temp[2],
                                'mode': mode,
                                'learnLv': i.learnLv,
                                'type': i.type,
                            }
                        )
        ratios = self.calc_damage_ration(DSB, BUFF)
        ratio_char_skill = ratios[0] * ratios[1] * ratios[2] * ratios[3] * ratios[4] * ratios[5] * ratios[6] * ratios[7] * ratios[8] * ratios[9] / 1000
        ratuio_equ_skill = ratios[0] * ratios[1] * ratios[3] * ratios[4] * ratios[6] * ratios[7] * ratios[8] * ratios[9] / 1000
        for i in skillInfos:
            i['damage'] = ratio_char_skill * i['data'] * i['ratio'] / 100
        for i in self.equ_effect:
            skillInfos.append({'name': i.name, 'icon': i.icon, 'lv': 0, 'data': i.data, 'ratio': 10.0, 'cd': i.cd, 'damage': ratuio_equ_skill * i.data * 10 * self.EquEffectRatio / 100, 'mode': ''})
        return skillInfos

    def get_carry_info(self):
        attrs = []
        if self.输出类型 == '物理百分比':
            attrs.extend(['STR', 'AtkP'])
        if self.输出类型 == '魔法百分比':
            attrs.extend(['INT', 'AtkM'])
        if self.输出类型 == '物理固伤':
            attrs.extend(['STR', 'AtkI'])
        if self.输出类型 == '魔法固伤':
            attrs.extend(['INT', 'AtkI'])
        info = []
        attrs.extend(['Attack', 'AttackP', 'SkillAttack', 'EquEffectRatio', 'ElementDB'])
        for attr in attrs:
            temp = getattr(CharacterInfo, attr)
            if attr.startswith('Atk'):
                info.append({'name': temp.name, 'value': temp.value(getattr(self, attr) * getattr(self, f'P{attr}'))})
            else:
                value = getattr(self, attr)
                if attr == 'SkillAttack':
                    value *= self.jade_effect.SkillAttack + 1
                if attr == 'AttackP':
                    value += self.jade_effect.AttackP
                info.append({'name': temp.name, 'value': temp.value(value)})
        return info

    # endregion
