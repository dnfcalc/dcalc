

from core.basic.buffer.property import *
from core.basic.buffer.character import Character

class 护石0:
    def __init__(self):
        self.name = '跃动情思'
        self.skill = '乐章再现'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.06)
        pass


class 护石1:
    def __init__(self):
        self.name = '强力音符'
        self.skill = '音力增强'

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.06)


class 护石2:
    def __init__(self):
        self.name = '舞台魅力'
        self.skill = '缪斯之声'
        pass

    def effect(self, 角色: Buffer):
        角色.get_skill_by_name('梦想的舞台').CD -= 25
        角色.辅助属性加成(buff百分比力智=0.04)


class 护石3:
    def __init__(self):
        self.name = '活力节奏'
        self.skill = '调音放送'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.04)


class 护石4:
    def __init__(self):
        self.name = '演出技巧'
        self.skill = '闪耀旋律'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.08)


class 护石5:
    def __init__(self):
        self.name = '完美开场'
        self.skill = '巨星登场'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.08)


class 护石6:
    def __init__(self):
        self.name = '四季问安'
        self.skill = '辉光变奏'
        pass

    def effect(self, 角色: Buffer):
        角色.辅助属性加成(buff百分比力智=0.06)


护石组合 = (护石0(), 护石1(), 护石2(),
        护石3(), 护石4(), 护石5(), 护石6())


class 技能0(辅助职业被动技能):
    名称 = '多彩感性'
    所在等级 = 15
    等级精通 = 50
    等级上限 = 60
    学习间隔 = 3
    额外精神 = 0
    站街生效 = 1
    精神 = [0, 276, 280, 284, 288, 292, 297, 302, 307, 313, 319, 325, 331, 337, 344, 351, 359, 367, 375, 383, 391, 400, 409, 419, 428, 438, 448, 459, 469, 480, 491, 503, 515, 527, 539, 551,
          565, 578, 591, 605, 619, 633, 647, 663, 677, 693, 709, 725, 741, 757, 774, 788, 804, 820, 836, 852, 867, 883, 899, 915, 931, 946, 962, 978, 994, 1010, 1025, 1041, 1057, 1073, 1089]

    def 精神加成(self):
        return self.精神[self.等级] + self.额外精神 + self.进图加成

    def 结算统计(self, context: Buffer):
        return [0, 0, 0, 0, self.精神加成()]
        # 力智、三攻、智力、体力、精神


class 技能1(辅助职业主动技能):
    名称 = '主角登场'
    所在等级 = 20
    等级精通 = 10
    等级上限 = 20
    学习间隔 = 3
    额外体精 = 0
    站街生效 = 0
    进图加成 = 0
    体精 = [0, 94, 98, 102, 107, 112, 116, 122, 127, 131, 137,
          141, 147, 153, 158, 163, 169, 175, 181, 187, 192]
    CD = 10

    def 体精加成(self):
        return self.体精[self.等级] + self.额外体精 + self.进图加成

    def 结算统计(self, context: Buffer):
        return [0, 0, 0, self.体精加成(), self.体精加成()]
        # 力智、三攻、智力、体力、精神


class 技能2(辅助职业主动技能):
    名称 = '可爱节拍'
    所在等级 = 30
    等级精通 = 10
    等级上限 = 40
    学习间隔 = 3

    BUFF力智per = 1
    BUFF三攻per = 1

    BUFF力智 = 0
    BUFF三攻 = 0

    倍率 = 1.0

    三攻 = [0, 40, 42, 44, 46, 47, 49, 51, 52, 54, 55, 56, 58, 60, 61, 63, 64, 65, 67, 70,
          72, 73, 74, 76, 78, 80, 82, 83, 84, 86, 88, 89, 92, 93, 94, 96, 98, 99, 101, 102, 104]
    力智 = [0, 162, 173, 186, 196, 207, 217, 227, 239, 249, 262, 272, 283, 295, 306, 318, 328, 338, 350, 360,
          372, 382, 394, 406, 416, 428, 437, 448, 460, 471, 482, 493, 503, 516, 527, 539, 548, 559, 570, 581, 593]

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
        # 力智、三攻、智力、体力、精神


class 技能3(辅助职业被动技能):
    名称 = '燃情狂想曲'
    所在等级 = 40
    等级精通 = 1
    等级上限 = 1
    学习间隔 = 3
    增幅倍率 = 0.1

    def 结算统计(self, context: Buffer):
        buff = context.get_skill_by_name('BUFF')
        if buff.是否启用:
            values = buff.结算统计(context)
            return [int(round(i * self.增幅倍率)) for i in values]
        return [0]*5


class 技能4(辅助职业被动技能):
    名称 = '明星气场'
    所在等级 = 48
    等级精通 = 40
    等级上限 = 50
    学习间隔 = 3
    额外力智 = 0
    力智 = [0, 14, 37, 59, 82, 104, 127, 149, 172, 194, 217, 239, 262, 284, 307, 329, 352, 374, 397, 419, 442, 464, 487, 509, 532, 554,
          577, 599, 622, 644, 667, 689, 712, 734, 757, 779, 802, 824, 847, 869, 892, 914, 937, 959, 982, 1004, 1027, 1049, 1072, 1094, 1117]
    额外精神 = 0
    精神 = [0, 6, 25, 44, 63, 82, 101, 120, 139, 158, 177, 196, 215, 234, 253, 272, 291, 310, 329, 348, 367, 386, 405, 424, 443, 462,
          485, 507, 530, 552, 575, 597, 620, 642, 665, 687, 710, 732, 755, 777, 800, 822, 845, 867, 890, 912, 935, 957, 980, 1002, 1025]

    def 力智加成(self):
        return self.力智[self.等级] + self.额外力智

    def 精神加成(self):
        return self.精神[self.等级] + self.额外精神

    def 结算统计(self, context: Buffer):
        return [self.力智加成(), 0, self.力智加成(), 0, self.精神加成()]
        # 力智、三攻、智力、体力、精神


class 技能5(辅助职业觉醒技能):
    名称 = '梦想的舞台'
    CD = 170
    pass


class 技能6(辅助职业被动技能):
    名称 = '崭新曲风'
    所在等级 = 75
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 3
    站街生效 = 1
    精神 = [0, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380,
          390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640]

    def 精神加成(self):
        return self.精神[self.等级]

    def 结算统计(self, context: Buffer):
        return [0, 0, 0, 0, self.精神加成()]
        # 力智、三攻、智力、体力、精神


class 技能7(辅助职业主动技能):
    名称 = '开场：唯我璀璨'
    所在等级 = 85
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 5
    CD = 180

    def 结算统计(self, context: Buffer):
        return [0]*5


class 技能8(辅助职业被动技能):
    名称 = '和茉霓之歌'
    所在等级 = 95
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 3
    站街生效 = 1
    精神 = [0, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390,
          400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650]

    def 精神加成(self):
        return self.精神[self.等级]

    def 结算统计(self, context: Buffer):
        return [0, 0, 0,  0, self.精神加成()]
        # 力智、三攻、智力、体力、精神


class 技能9(辅助职业三觉技能):
    名称 = '终曲：霓虹蝶梦'
    关联技能 = ['开场：唯我璀璨']
    CD = 290
    pass

class 技能10(辅助职业主动技能):
    名称 = '夜与梦'
    所在等级 = 10
    等级上限 = 70
    等级精通 = 60
    学习间隔 = 3
    CD = 10

    def 结算统计(self, context):
        return [0, 0, 0, 0, 0]


class 技能11(辅助职业主动技能):
    名称 = '辉光变奏'
    所在等级 = 80
    等级上限 = 50
    等级精通 = 40
    学习间隔 = 2
    CD = 50

    def 结算统计(self, context):
        return [0, 0, 0, 0, 0]


class classChange(Character):
    def __init__(self, equVersion=""):
        self.实际名称 = 'muse'
        self.名称 = '聆风·缪斯'
        self.角色 = '弓箭手'

        self.类型 = '辅助'
        self.职业 = '缪斯'
        self.转职 = '缪斯'

        self.武器选项 = ['神弦弓']
        self.输出类型选项 = ['魔法固伤']
        self.防具精通属性 = ['精神']
        self.武器类型 = '神弦弓'
        self.防具类型 = '板甲'
        self.适用属性 = '精神'
        self.技能序号 = {}
        self.被动增伤倍率 = 1.165

        技能栏 = []
        i = 0
        while i >= 0:
            try:
                skill: 辅助职业技能 = eval("技能"+str(i)+"()")
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
        self.护石技能 = [i.skill for i in 护石组合]

        super().__init__(equVersion)

    def 护石计算(self):
        for 护石 in 护石组合:
            if 护石.skill in self.护石栏:
                护石.effect(self)
        pass

    def set_skill_info(self, info, rune_except=[], clothes_pants=[], rune_start_lv=20) -> None:
        super().set_skill_info(info,rune_except=['主角登场'],rune_start_lv=10)

    def 职业特殊计算(self):
        for skill in self.技能栏:
            data = skill.结算统计(self)
            if (data[4] > 0):
                self.skills_passive[skill.名称]['info'] = [{
                    'type': '精神',
                    'info': [data[4]],
                    'percent': False
                }]
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
        self.觉醒技能 = ['梦想的舞台','开场：唯我璀璨','终曲：霓虹蝶梦']