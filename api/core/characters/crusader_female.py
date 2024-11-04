
from copy import deepcopy
from typing import List

from core.basic.buffer.property import *
from core.basic.buffer.character import Character


class 女圣骑士护石0:
    def __init__(self):
        self.name = '天使圣歌'
        self.skill = '勇气圣歌'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.04)
        pass


class 女圣骑士护石1:
    def __init__(self):
        self.name = '奇迹之光'
        self.skill = '忏悔之雷'

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.06)


class 女圣骑士护石2:
    def __init__(self):
        self.name = '神圣十字'
        self.skill = '神光十字'
        pass

    def effect(self, 角色: Buffer):
        角色.get_skill_by_name("神光十字").CDR *= 0.88
        角色.辅助属性加成(buff百分比力智=0.06)


class 女圣骑士护石3:
    def __init__(self):
        self.name = '乌列尔的庇佑'
        self.skill = '圣佑之阵'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.06)


class 女圣骑士护石4:
    def __init__(self):
        self.name = '光之祈祷'
        self.skill = '忏悔重击'
        pass

    def effect(self, 角色: Buffer):
        角色.get_skill_by_name("圣光天启").CD -= 25
        角色.辅助属性加成(buff百分比力智=0.04)


class 女圣骑士护石5:
    def __init__(self):
        self.name = '米迦勒的圣光球'
        self.skill = '圣光普照'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.08)


class 女圣骑士护石6:
    def __init__(self):
        self.name = '圣洁之源'
        self.skill = '圣洁之翼'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.08)


女圣骑士护石组合 = (女圣骑士护石0(), 女圣骑士护石1(), 女圣骑士护石2(),
            女圣骑士护石3(), 女圣骑士护石4(), 女圣骑士护石5(), 女圣骑士护石6())


class 神启·圣骑士技能0(辅助职业被动技能):
    名称 = '启示圣歌'
    所在等级 = 15
    等级精通 = 50
    等级上限 = 60
    学习间隔 = 3
    额外智力 = 0
    站街生效 = 1
    智力 = [0, 86, 90, 94, 98, 102, 107, 112, 117, 123, 129, 135, 141, 147, 154, 161, 169, 177, 185, 193, 201, 210, 219, 229, 238, 248, 258, 269, 279, 290, 301,
          313, 325, 337, 349, 361, 375, 388, 401, 415, 429, 443, 457, 473, 487, 503, 519, 535, 551, 567, 584, 598, 614, 630, 646, 662, 677, 693, 709, 725, 741]

    def 智力加成(self):
        return self.智力[self.等级] + self.额外智力 + self.进图加成

    def 结算统计(self, context: Buffer):
        return [0, 0, self.智力加成(), 0, 0]
        # 力智、三攻、智力、体力、精神


class 神启·圣骑士技能2(辅助职业主动技能):
    名称 = '勇气祝福'
    所在等级 = 30
    等级精通 = 10
    等级上限 = 40
    学习间隔 = 3
    CD = 10

    BUFF力智per = 1
    BUFF三攻per = 1

    BUFF力智 = 0
    BUFF三攻 = 0

    倍率 = 1.0

    三攻 = [round(i*1.02) for i in [0, 38, 40, 42, 43, 44, 46, 48, 49, 51, 52, 53, 55, 57, 58, 60, 61, 62, 64, 66, 68, 69, 70, 72, 74, 75, 77, 78, 79, 81, 83, 84, 86, 87, 88, 90, 92, 93, 95,
                                  96, 98, 100, 101, 103, 104, 105, 107, 109, 110, 112, 113, 114, 116, 118, 119, 121, 122, 123, 126, 127, 129, 130, 131, 133, 135, 136, 138, 139, 140, 143, 144]]
    力智 = [round(i*1.04) for i in [0, 148, 158, 169, 179, 189, 198, 208, 218, 228, 239, 249, 259, 269, 279, 290, 299, 309, 319, 329, 339, 349, 360, 370, 380, 390, 399, 409, 420, 430, 440, 450, 460, 470, 481,
                                  491, 500, 510, 520, 530, 541, 551, 561, 571, 581, 592, 601, 611, 621, 631, 641, 651, 662, 672, 682, 692, 701, 711, 722, 732, 742, 752, 762, 772, 783, 793, 802, 812, 822, 832, 843]]

    def 结算统计(self, context: Buffer):
        buffer_power = context.BUFF量()

        新词条倍率 = (((self.适用数值 + 4350) / 665 + 1) *
                 (buffer_power + 3500) / 26395) if buffer_power > 0 else 0

        新词条力智 = 新词条倍率 * (self.力智[self.等级])
        新词条三攻 = 新词条倍率 * (self.三攻[self.等级])

        旧词条力智 = ((self.适用数值)/665 + 1) * \
            (self.力智[self.等级]+self.BUFF力智) * self.BUFF力智per

        旧词条三攻 = ((self.适用数值)/665 + 1) * \
            (self.三攻[self.等级]+self.BUFF三攻) * self.BUFF三攻per

        倍率 = self.倍率

        力智 = int((新词条力智 + 旧词条力智) * 倍率)
        三攻 = int((新词条三攻 + 旧词条三攻) * 倍率)

        return [力智, 三攻, 0, 0, 0]
        # 力智、三攻、智力、体力、精神


class 神启·圣骑士技能3(辅助职业主动技能):
    名称 = '勇气圣歌'
    所在等级 = 35
    等级精通 = 50
    等级上限 = 60
    学习间隔 = 3
    CD = 40
    增幅倍率 = 0.15

    def 结算统计(self, context: Buffer):
        buff = context.get_skill_by_name('BUFF')
        if buff.是否启用:
            values = buff.结算统计(context)
            return [int(round(i * self.增幅倍率)) for i in values]
        return [0]*5


class 神启·圣骑士技能1(辅助职业主动技能):
    名称 = '神光十字'
    所在等级 = 45
    等级上限 = 60
    等级精通 = 50
    学习间隔 = 2
    力智 = 72
    CD = 45

    def 力智加成(self):
        return self.力智 + self.等级 * 6

    def 结算统计(self, context):
        return [self.力智加成(), 0, 0, 0, 0]


class 神启·圣骑士技能4(辅助职业被动技能):
    名称 = '虔诚信念'
    所在等级 = 48
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 3
    额外力智 = 0
    力智 = [0, 14, 37, 59, 82, 104, 127, 149, 172, 194, 217, 239, 262, 284, 307, 329, 352, 374, 397, 419, 442,
          464, 487, 509, 532, 554, 577, 599, 622, 644, 667, 689, 712, 734, 757, 779, 802, 824, 847, 869, 892]

    def 力智加成(self):
        return self.力智[self.等级] + self.额外力智

    def 结算统计(self, context: Buffer):
        return [self.力智加成(), 0, self.力智加成(), 0, 0]
        # 力智、三攻、智力、体力、精神


class 神启·圣骑士技能5(辅助职业觉醒技能):
    名称 = '圣光天启'
    CD = 170
    pass


class 神启·圣骑士技能6(辅助职业被动技能):
    名称 = '大天使的庇护'
    所在等级 = 75
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 3
    站街生效 = 1
    智力 = [0, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330,
          340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540]

    def 智力加成(self):
        return self.智力[self.等级]

    def 结算统计(self, context: Buffer):
        return [0, 0, self.智力加成(), 0, 0]
        # 力智、三攻、智力、体力、精神


class 神启·圣骑士技能7(辅助职业主动技能):
    名称 = '救赎彼岸：惩戒圣枪'
    所在等级 = 85
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 5
    CD = 180

    def 结算统计(self, context: Buffer):
        return [0]*5


class 神启·圣骑士技能8(辅助职业被动技能):
    名称 = '圣天使之光'
    所在等级 = 95
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 3
    站街生效 = 1
    智力 = [0, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340,
          350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550]

    def 智力加成(self):
        return self.智力[self.等级]

    def 结算统计(self, context: Buffer):
        return [0, 0, self.智力加成(),  0, 0]
        # 力智、三攻、智力、体力、精神


class 神启·圣骑士技能9(辅助职业三觉技能):
    名称 = '祈愿·天使赞歌'
    关联技能 = ['救赎彼岸：惩戒圣枪']
    CD = 290
    pass

class 神启·圣骑士技能10(辅助职业主动技能):
    名称 = '治愈祈祷'
    所在等级 = 5
    等级上限 = 70
    等级精通 = 60
    学习间隔 = 3
    CD = 10

    def 结算统计(self, context):
        return [0, 0, 0, 0, 0]

class 神启·圣骑士技能11(辅助职业主动技能):
    名称 = '圣光守护'
    所在等级 = 25
    等级上限 = 60
    等级精通 = 50
    学习间隔 = 2
    CD = 20

    def 结算统计(self, context):
        return [0, 0, 0, 0, 0]

class 神启·圣骑士技能12(辅助职业主动技能):
    名称 = '神之教诲'
    所在等级 = 35
    等级上限 = 1
    等级精通 = 1
    学习间隔 = 2
    CD = 20

    def 结算统计(self, context):
        return [0, 0, 0, 0, 0]

class 神启·圣骑士技能13(辅助职业主动技能):
    名称 = '新生圣歌'
    所在等级 = 45
    等级上限 = 11
    等级精通 = 1
    学习间隔 = 2
    CD = 40

    def 结算统计(self, context):
        return [0, 0, 0, 0, 0]

class 神启·圣骑士技能14(辅助职业主动技能):
    名称 = '圣洁之翼'
    所在等级 = 70
    等级上限 = 50
    等级精通 = 40
    学习间隔 = 2
    CD = 50

    def 结算统计(self, context):
        return [0, 0, 0, 0, 0]

class 神启·圣骑士技能15(辅助职业主动技能):
    名称 = '圣佑之阵'
    所在等级 = 75
    等级上限 = 50
    等级精通 = 40
    学习间隔 = 2
    CD = 50

    def 结算统计(self, context):
        return [0, 0, 0, 0, 0]

class 神启·圣骑士技能16(辅助职业主动技能):
    名称 = '圣光普照'
    所在等级 = 80
    等级上限 = 50
    等级精通 = 40
    学习间隔 = 2
    CD = 40

    def 结算统计(self, context):
        return [0, 0, 0, 0, 0]

class classChange(Character):
    def __init__(self, equVersion=""):
        self.实际名称 = 'crusader_female'
        self.名称 = '神启·圣骑士'
        self.角色 = '圣职者(女)'

        self.类型 = '辅助'
        self.职业 = '圣骑士'
        self.转职 = '圣骑士(女)'

        self.武器选项 = ['十字架']
        self.输出类型选项 = ['魔法固伤']
        self.防具精通属性 = ['智力']
        self.武器类型 = '十字架'
        self.防具类型 = '板甲'
        self.技能序号 = {}
        技能栏 = []

        self.被动增伤倍率 = 1.135

        i = 0
        while i >= 0:
            try:
                skill: 辅助职业技能 = eval("神启·圣骑士技能"+str(i)+"()")
                skill.技能序号 = i
                名称 = skill.名称
                self.技能序号[名称] = i
                if skill.所在等级 == 30:
                    名称 = 'BUFF'
                elif skill.所在等级 == 50:
                    名称 = '一次觉醒'
                elif skill.所在等级 == 85:
                    名称 = '二次觉醒'
                elif skill.所在等级 == 100:
                    名称 = '三次觉醒'
                skill.基础等级计算()
                技能栏.append(skill)
                self.技能序号[名称] = i
                i += 1
            except Exception:
                i = -1
        self.技能栏 = 技能栏
        self.buff = 1.70
        self.护石技能 = [i.skill for i in 女圣骑士护石组合]

        super().__init__(equVersion)

    def 护石计算(self):
        for 护石 in 女圣骑士护石组合:
            if 护石.skill in self.护石栏:
                护石.effect(self)

    def 职业特殊计算(self):
        for skill in self.技能栏:
            data = skill.结算统计(self)
            if (data[2] > 0):
                self.skills_passive[skill.名称]['info'] = [{
                    'type': '智力',
                    'info': [data[2]],
                    'percent': False
                }]
        pass

    def set_skill_info(self, info, rune_except=[], clothes_pants=[], rune_start_lv=20) -> None:
        super().set_skill_info(info,rune_except=['勇气祝福','神之教诲'],rune_start_lv=5)

    def 设置觉醒技能(self):
        self.觉醒技能 = ['祈愿·天使赞歌','圣光天启','救赎彼岸：惩戒圣枪']

    def 技能冷却缩减(self, min: int, max: int, x: float, exc=[],excName=[]) -> None:
        if min == 1 and max == 100:
            self.冷却缩减 *= (1-x)
        for i in self.技能栏:
            if i.所在等级 >= min and i.所在等级 <= max and i.所在等级 not in exc  and i.名称 not in excName:
                if i.是否主动 == 1:
                    i.CDR *= (1 - x)

    def 技能恢复加成(self, min: int, max: int, x: float, exc=[],excName=[]) -> None:
        if min == 1 and max == 100:
            self.冷却恢复 += x
        for i in self.技能栏:
            if i.所在等级 >= min and i.所在等级 <= max and i.所在等级 not in exc  and i.名称 not in excName:
                if i.是否主动 == 1:
                    i.恢复 += x

    def 单技能加成(self, 名称: str, 倍率=1.0, CD=1.0, lv=0) -> None:
        i = self.get_skill_by_name(名称)
        i.等级加成(lv, char=self)
        if i.是否主动 == 1:
            i.CDR *= CD