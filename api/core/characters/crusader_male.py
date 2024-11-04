
from copy import deepcopy
from typing import List

from core.basic.buffer.property import *
from core.basic.buffer.character import Character


class 男圣骑士护石0:
    def __init__(self):
        self.name = '绝对壁垒'
        self.skill = '圣光球'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.06)
        pass


class 男圣骑士护石1:
    def __init__(self):
        self.name = '附庸的生命'
        self.skill = '忏悔之锤'

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.06)


class 男圣骑士护石2:
    def __init__(self):
        self.name = '米歇尔的审判'
        self.skill = '正义审判'
        pass

    def effect(self, 角色: Buffer):
        角色.get_skill_by_name("圣愈之风").CDR *= 0.84
        角色.辅助属性加成(buff百分比力智=0.04)


class 男圣骑士护石3:
    def __init__(self):
        self.name = '圣光奇袭'
        self.skill = '圣光突袭'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.08)


class 男圣骑士护石4:
    def __init__(self):
        self.name = '神圣操控'
        self.skill = '神圣之矛'
        pass

    def effect(self, 角色: Buffer):
        角色.get_skill_by_name("天启之珠").CD -= 25
        角色.辅助属性加成(buff百分比力智=0.04)


class 男圣骑士护石5:
    def __init__(self):
        self.name = '天堂结界'
        self.skill = '圣佑结界'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.08)


class 男圣骑士护石6:
    def __init__(self):
        self.name = '神圣守护'
        self.skill = '神圣之光'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.06)


男圣骑士护石组合 = (男圣骑士护石0(), 男圣骑士护石1(), 男圣骑士护石2(),
            男圣骑士护石3(), 男圣骑士护石4(), 男圣骑士护石5(), 男圣骑士护石6())


class 神启·圣骑士技能0(辅助职业被动技能):
    名称 = '守护恩赐'
    所在等级 = 15
    等级精通 = 50
    等级上限 = 60
    学习间隔 = 3
    额外体精 = 0
    站街生效 = 1

    体力 = [0, 220, 224, 228, 232, 236, 241, 246, 251, 257, 263, 269, 275, 281, 288, 295, 303, 311, 319, 327, 335, 344, 353, 363, 372, 382, 392, 403, 413, 424, 435, 447, 459, 471, 483, 495, 509, 522, 535, 549, 563, 577, 591, 607, 621, 637, 653, 669, 685, 701, 718, 732, 748, 764, 780, 796, 811, 827, 843, 859, 875, 890, 906, 922, 937, 953, 969, 985, 1001, 1016, 1032]
    精神 = [0, 266, 270, 274, 278, 282, 287, 292, 297, 303, 309, 315, 321, 327, 334, 341, 349, 357, 365, 373, 381, 390, 399, 409, 418, 428, 438, 449, 459, 470, 481, 493, 505, 517, 529, 541, 555, 568, 581, 595, 609, 623, 637, 653, 667, 683, 699, 715, 731, 747, 764, 778, 794, 810, 826, 842, 857, 873, 889, 905, 921, 936, 952, 968, 983, 999, 1015, 1031, 1047, 1062, 1078]

    def 体力加成(self):
        return self.体力[self.等级] + self.额外体精 + self.进图加成

    def 精神加成(self):
        return self.精神[self.等级] + self.额外体精 + self.进图加成

    def 结算统计(self, context: Buffer):
        return [0, 0, 0, self.体力加成(), self.精神加成()]
        # 智力 体力 精神  力量  智力  物攻  魔攻 独立


class 神启·圣骑士技能1(辅助职业主动技能):
    名称 = '圣光十字'
    所在等级 = 25
    等级精通 = 50
    等级上限 = 60
    学习间隔 = 2
    三攻 = [0, 5, 6, 7, 8, 9, 10, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 64, 65, 66, 67, 68, 69]
    CD = 8

    def 三攻加成(self):
        return self.三攻[self.等级]

    def 结算统计(self, context):
        return [0, self.三攻加成(), 0, 0, 0]


class 神启·圣骑士技能2(辅助职业主动技能):
    名称 = '荣誉祝福'
    所在等级 = 30
    等级精通 = 10
    等级上限 = 40
    学习间隔 = 3

    BUFF力智per = 1.0
    BUFF三攻per = 1.0

    BUFF力智 = 0
    BUFF三攻 = 0

    倍率 = 1.0

    三攻 = [0, 41, 42, 44, 45, 46, 48, 50, 51, 53, 55, 56, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 81, 83, 85, 86, 88, 90, 91, 93, 94, 95, 97, 99, 100, 103]
    力智 = [0, 161, 171, 181, 193, 204, 214, 224, 236, 247, 258, 269, 279, 291, 301, 313, 322, 333, 345, 356, 366, 377, 389, 399, 410, 421, 431, 442, 454, 464, 474, 486, 497, 508, 518, 531, 540, 551, 562, 572, 584]

    CD = 10

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


class 神启·圣骑士技能3(辅助职业主动技能):
    名称 = '守护徽章'
    所在等级 = 25
    等级精通 = 10
    等级上限 = 20
    学习间隔 = 2
    增幅倍率 = 0.15
    数值 = [0, 94, 98, 102, 107, 112, 116, 122, 127, 131, 137, 141, 147, 153, 158, 163, 169, 175, 181, 187, 192]

    CD = 10

    def 体精加成(self):
        return int(self.数值[self.等级] * (1 + self.增幅倍率))

    def 结算统计(self, context: Buffer):
        return [0, 0, 0, self.体精加成(), self.体精加成()]


class 神启·圣骑士技能4(辅助职业被动技能):
    名称 = '信念光环'
    所在等级 = 48
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 3
    额外体精 = 0
    力智 = [0, 40, 48, 58, 67, 77, 87, 98, 109, 120, 133, 144, 157, 171, 184, 198, 212, 226, 242, 258, 273, 290, 306, 323, 341, 359, 378, 397, 416, 436, 456, 476, 498, 518, 541, 562, 586, 609, 632, 654, 678, 702, 726, 750, 774, 798, 823, 848, 873, 898, 923]
    体精 = [0, 10, 29, 48, 67, 86, 105, 124, 143, 162, 181, 200, 219, 238, 257, 276, 295, 314, 333, 352, 371, 390, 409, 428, 447, 466, 489, 511, 534, 556, 579, 601, 624, 646, 669, 691, 714, 736, 759, 781, 804, 826, 849, 871, 894, 916, 939, 961, 984, 1006, 1029]

    def 力智加成(self):
        return self.力智[self.等级]

    def 体精加成(self):
        return self.体精[self.等级] + self.额外体精

    def 结算统计(self, context: Buffer):
        return [self.力智加成(), 0, 0, self.体精加成(), self.体精加成()]


class 神启·圣骑士技能5(辅助职业觉醒技能):
    名称 = '天启之珠'
    CD = 170
    pass

class 神启·圣骑士技能6(辅助职业主动技能):
    名称 = '神圣之光'
    所在等级 = 75
    等级精通 = 40
    等级上限 = 50
    学习间隔 = 3
    数值 = [0, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640]

    CD = 20

    def 体精加成(self):
        return int(self.数值[self.等级])

    def 结算统计(self, context: Buffer):
        return [0, 0, 0, self.体精加成(), self.体精加成()]

class 神启·圣骑士技能7(辅助职业主动技能):
    名称 = '神圣洗礼：信仰之翼'
    所在等级 = 85
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 5
    增幅倍率 = 0.12
    CD = 180

    def 结算统计(self, context: Buffer):
        buff = context.get_skill_by_name('BUFF')
        if buff.是否启用:
            values = buff.结算统计(context)
            return [int(round(i * self.增幅倍率)) for i in values]
        return [0]*5


class 神启·圣骑士技能8(辅助职业被动技能):
    名称 = '神之代行者'
    所在等级 = 95
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 3
    站街生效 = 1
    体精 = [0, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650]

    def 体精加成(self):
        return self.体精[self.等级]

    def 结算统计(self, context: Buffer):
        return [0, 0, 0,  self.体精加成(), self.体精加成()]
        # 力智 三攻 智力 体精


class 神启·圣骑士技能9(辅助职业三觉技能):
    名称 = '生命礼赞：神威'
    关联技能 = ['神圣洗礼：信仰之翼']
    CD = 290
    pass

class 神启·圣骑士技能10(辅助职业主动技能):
    名称 = '缓慢愈合'
    所在等级 = 5
    等级上限 = 70
    等级精通 = 60
    学习间隔 = 2
    CD = 8

    def 结算统计(self, context):
        return [0, 0, 0, 0, 0]

class 神启·圣骑士技能11(辅助职业主动技能):
    名称 = '生命源泉'
    所在等级 = 40
    等级上限 = 50
    等级精通 = 40
    学习间隔 = 2
    CD = 60

    def 结算统计(self, context):
        return [0, 0, 0, 0, 0]

class 神启·圣骑士技能12(辅助职业主动技能):
    名称 = '圣愈之风'
    所在等级 = 45
    等级上限 = 30
    等级精通 = 20
    学习间隔 = 2
    CD = 60

    def 结算统计(self, context):
        return [0, 0, 0, 0, 0]


class 神启·圣骑士技能13(辅助职业主动技能):
    名称 = '圣佑结界'
    所在等级 = 75
    等级上限 = 50
    等级精通 = 40
    学习间隔 = 2
    CD = 40

    def 结算统计(self, context):
        return [0, 0, 0, 0, 0]



class classChange(Character):
    def __init__(self, equVersion=""):

        self.技能序号 = {}
        技能栏 = []
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
        self.护石技能 = [i.skill for i in 男圣骑士护石组合]

        self.实际名称 = 'crusader_male'
        self.名称 = '神启·圣骑士'
        self.角色 = '圣职者(男)'

        self.类型 = '辅助'
        self.职业 = '圣骑士'
        self.转职 = '圣骑士(男)'
        self.武器选项 = ['十字架']
        self.输出类型选项 = ['魔法固伤']
        self.防具精通属性 = ['体力', '精神']
        self.武器类型 = '十字架'
        self.防具类型 = '板甲'
        self.适用属性 = '体力'
        self.被动增伤倍率 = 1.135

        super().__init__(equVersion)

    def set_skill_info(self, info, rune_except=[], clothes_pants=[], rune_start_lv=20) -> None:
        super().set_skill_info(info,rune_except=['荣誉祝福','守护徽章','守护恩赐','生命源泉'],rune_start_lv=10)

    def 护石计算(self):
        for 护石 in 男圣骑士护石组合:
            if 护石.skill in self.护石栏:
                护石.effect(self)

    def 职业特殊计算(self):
        for skill in self.技能栏:
            data = skill.结算统计(self)
            info = []

            if (data[3] > 0):
                info.append({
                    'type': '体力',
                    'info': [data[3]],
                    'percent': False
                })
            if (data[4] > 0):
                info.append({
                    'type': '精神',
                    'info': [data[4]],
                    'percent': False
                })
            self.skills_passive[skill.名称]['info'] = info
        pass

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

    def 设置觉醒技能(self):
        self.觉醒技能 = ['神启之珠','生命礼赞：神威','神圣洗礼：信仰之翼']