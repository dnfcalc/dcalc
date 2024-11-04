from core.equipment.property import 武器MP系数, 武器冷却惩罚


角色等级 = 110


class 技能:
    名称 = ''
    备注 = ''
    所在等级 = 0
    等级上限 = 0
    等级 = 0
    基础等级 = 0
    等级溢出 = 0
    自定义描述 = 0
    学习间隔 = 1
    等级精通 = 60

    倍率 = 1.0

    关联技能 = ['无']
    关联技能1 = ['无']
    关联技能2 = ['无']
    关联技能3 = ['无']
    非关联技能 = ['无']
    非关联技能1 = ['无']
    非关联技能2 = ['无']
    非关联技能3 = ['无']
    冷却关联技能 = ['无']
    冷却关联技能1 = ['无']
    冷却关联技能2 = ['无']
    冷却关联技能3 = ['无']
    冷却类型 = 0
    冷却类型1 = 0
    冷却类型2 = 0
    冷却类型3 = 0
    非冷却关联技能 = ['无']
    非冷却关联技能1 = ['无']
    非冷却关联技能2 = ['无']
    非冷却关联技能3 = ['无']

    MP = [0, 0]
    手搓 = False
    手搓收益 = 1.0
    手搓指令数 = 0
    无色消耗 = 0
    技能栏位置 = -1

    def 等级加成(self, x, char={}):
        if self.等级 != 0:
            if self.等级 + x > self.等级上限:
                self.等级 = self.等级上限
                # if self.基础等级 != self.等级上限 and self.关联技能 != ['无']:
                #     self.等级溢出 = 1
            else:
                self.等级 += int(x)

    def TP等级加成(self, x, char={}):
        pass

    def 物理攻击力倍率(self, 武器类型):
        return 1.0

    def 魔法攻击力倍率(self, 武器类型):
        return 1.0

    def 独立攻击力倍率(self, 武器类型):
        return 1.0

    def 物理攻击力倍率进图(self, 武器类型):
        return 1.0

    def 魔法攻击力倍率进图(self, 武器类型):
        return 1.0

    def 独立攻击力倍率进图(self, 武器类型):
        return 1.0

    def MP消耗(self, **argv):
        pass

    def 基础等级计算(self):
        if self.基础等级 == 0:
            self.基础等级 = min(int((角色等级 + 5 - self.所在等级) / self.学习间隔 + 1),
                            self.等级精通)

    def 加成倍率(self, 武器类型):
        return 1.0

    def 加成描述(self, 武器类型):
        return [round((self.加成倍率(武器类型) - 1)*100, 1), ",".join(self.关联技能), ",".join(self.非关联技能)]

    def 加成倍率1(self, 武器类型):
        return 1.0

    def 加成描述1(self, 武器类型):
        return [round((self.加成倍率1(武器类型) - 1)*100, 1), ",".join(self.关联技能1), ",".join(self.非关联技能1)]

    def 加成倍率2(self, 武器类型):
        return 1.0

    def 加成描述2(self, 武器类型):
        return [round((self.加成倍率2(武器类型) - 1)*100, 1), ",".join(self.关联技能2), ",".join(self.非关联技能2)]

    def 加成倍率3(self, 武器类型):
        return 1.0

    def 加成描述3(self, 武器类型):
        return [round((self.加成倍率3(武器类型) - 1)*100, 1), ",".join(self.关联技能3), ",".join(self.非关联技能3)]

    def CD缩减倍率(self, 武器类型):
        return 1.0

    def CD缩减描述(self, 武器类型):
        return [round((1-self.CD缩减倍率(武器类型))*100, 1), ",".join(self.冷却关联技能), ",".join(self.非冷却关联技能)]


    def CD缩减描述1(self, 武器类型):
        return [round((1-self.CD缩减倍率1(武器类型))*100, 1), ",".join(self.冷却关联技能1), ",".join(self.非冷却关联技能1)]

    def CD缩减倍率2(self, 武器类型):
        return 1.0

    def CD缩减描述2(self, 武器类型):
        return [round((1-self.CD缩减倍率2(武器类型))*100, 1), ",".join(self.冷却关联技能2), ",".join(self.非冷却关联技能2)]

    def CD缩减倍率3(self, 武器类型):
        return 1.0

    def CD缩减描述3(self, 武器类型):
        return [round((1-self.CD缩减倍率3(武器类型))*100, 1), ",".join(self.冷却关联技能3), ",".join(self.非冷却关联技能3)]


class 主动技能(技能):
    # 如果需要继续扩展，可以在各自职业类内继承后自行扩展，同时需要重写下等效百分比函数
    # 固伤在填写基础及成长的时候需要注意，技能面板/独立得到的成长及数值需要*100
    CD = 0.0
    CDR = 1.0
    CD固定缩减 = 0
    CDR_O = 1.0
    TP成长 = 0.0
    TP上限 = 0
    TP等级 = 0
    是否主动 = 1
    是否有伤害 = 1
    恢复 = 1.0
    倍率 = 1.0
    技攻 = 1.0
    被动倍率 = 1.0
    基础施放次数 = 0
    演出时间 = 0
    是否有护石 = 0
    武器倍率 = {}
    形态 = []
    国服特色 = 1.0

    data0 = []
    hit0 = 1
    power0 = 1

    感电data0 = []
    感电hit0 = 0
    感电power0 = 1

    灼伤data0 = []
    灼伤hit0 = 0
    灼伤power0 = 1

    中毒data0 = []
    中毒hit0 = 0
    中毒power0 = 1

    出血data0 = []
    出血hit0 = 0
    出血power0 = 1

    def __init__(self) -> None:
        super().__init__()
        # self.倍率 = 1.0

    def TP等级加成(self, x, char={}):
        if self.TP等级 != 0:
            self.TP等级 = min(self.TP等级+x, self.TP上限+2)

    def 形态变更(self, 形态, char):
        if 形态 == '' and len(self.形态) > 0:
            形态 = self.形态[0]
        pass

    def TP加成(self):
        return 1 + self.TP成长 * self.TP等级

    def 基础百分比(self, 类型, 等级):
        if 类型 == '直伤':
            name = ''
        else:
            name = 类型
        百分比 = 0.0
        for i in range(0, 8):
            data = getattr(self, '{}data{}'.format(name, i), [])
            if 等级 < len(data) and 等级 > 0:
                hit = getattr(self, '{}hit{}'.format(name, i), 1)
                power = getattr(self, '{}power{}'.format(name, i), 1)
                百分比 += data[等级] * hit * power
        return 百分比 * self.国服特色

    def 武器百分比修正(self, 武器类型):
        return self.武器倍率.get(武器类型, 1.0)

    def 等效百分比(self, **argv):
        # 武器类型 额外等级 额外倍率 伤害类型 形态
        武器类型 = argv.get('武器类型', '')
        额外等级 = argv.get('额外等级', 0)
        额外倍率 = argv.get('额外倍率', 1.0)
        伤害类型 = argv.get('伤害类型', '直伤')
        形态 = argv.get('形态', '')
        char = argv.get('char', {})

        self.形态变更(形态, char)
        等级 = min(self.等级 + 额外等级, self.等级上限)

        if 等级 == 0:
            return 0

        百分比 = self.基础百分比(伤害类型, 等级)

        return 百分比 * self.TP加成() * self.技攻 * self.倍率 * 额外倍率 * self.武器百分比修正(武器类型)

    def 武器CD系数(self, 武器类型, 输出类型):
        return 武器冷却惩罚(武器类型, 输出类型)

    def 手搓CD(self):
        cdr = 0
        if self.手搓:
            if self.所在等级 >= 15 and self.所在等级 <= 30:
                cdr = 0.01 * self.手搓收益
            if self.所在等级 >= 35 and self.所在等级 <= 70:
                cdr = 0.02 * self.手搓收益
            if self.所在等级 >= 75 and self.所在等级 <= 100:
                cdr = 0.05 * self.手搓收益
            if self.所在等级 in [50, 85, 100]:
                cdr = 0.05 * self.手搓收益
        return cdr

    def 等效CD(self, **argv):
        # 武器类型 输出类型 额外CDR 手搓收益 恢复
        武器类型 = argv.get('武器类型', '')
        输出类型 = argv.get('输出类型', '')
        额外CDR = argv.get('额外CDR', 1.0)
        # 手搓收益 = argv.get('手搓收益', 1.0)
        面板显示 = argv.get('面板显示', False)
        额外恢复 = argv.get('额外恢复', 0)
        cdr = self.手搓CD()
        形态 = argv.get('形态', '')
        char = argv.get('char', {})
        self.形态变更(形态, char)

        return max(0,round(max(self.CD * self.CDR * 额外CDR / ((self.恢复 + 额外恢复) if not 面板显示 else 1) * (self.武器CD系数(武器类型, 输出类型) - (cdr if not 面板显示 else 0)), self.CD * 0.3) * self.CDR_O, 1) - self.CD固定缩减 / ((self.恢复 + 额外恢复) if not 面板显示 else 1) )

    def MP消耗(self, **argv):
        # 武器类型 输出类型 额外CDR 手搓收益 恢复=True
        武器类型 = argv.get('武器类型', '')
        输出类型 = argv.get('输出类型', '')
        额外倍率 = argv.get('额外倍率', 1.0)
        if self.MP  is None:
            self.MP = [0, 0]
        if self.等级上限 > 1:
            mpnum = int(self.MP[0] + (self.等级 - 1) *
                        (self.MP[1] - self.MP[0]) / (self.等级上限 - 1))
        else:
            mpnum = self.MP[0]
        return round(mpnum * 武器MP系数(武器类型, 输出类型) * 额外倍率, 0)


class 被动技能(技能):
    是否主动 = 0
    是否有伤害 = 0
    关联技能 = ['所有']
