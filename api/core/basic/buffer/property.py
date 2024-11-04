
from core.basic.property import CharacterProperty
from core.basic.skill import 技能


class Buffer(CharacterProperty):

    def BUFF量():
        return 0

    def 辅助属性加成(self, buff固定力智=0, buff百分比力智=0.0, buff固定三攻=0, buff百分比三攻=0.0, 觉醒固定力智=0, 觉醒百分比力智=0.0, buff量=0, 百分比buff量=0.0):
        pass
    pass


class 辅助职业技能(技能):
    名称 = ''
    备注 = ''
    所在等级 = 0
    等级上限 = 0
    学习间隔 = 3
    等级 = 0
    基础等级 = 0
    是否主动 = 0
    站街生效 = 0
    等级溢出 = 0

    是否启用 = 1
    技能序号 = 0

    是否有伤害 = 0

    def 等级加成(self, x, char={}):
        if self.等级 != 0:
            if self.等级 + x > self.等级上限:
                self.等级 = self.等级上限
                if self.基础等级 != self.等级上限:
                    self.等级溢出 = 1
            else:
                self.等级 += int(x)

    def 结算统计(self, context=None):
        return [0, 0, 0, 0]
        # 力智 三攻 智力 体精


class 辅助职业被动技能(辅助职业技能):
    是否主动 = 0
    进图加成 = 0


class 辅助职业主动技能(辅助职业技能):
    是否主动 = 1
    适用数值 = 0
    CD = 0.0
    CDR_O = 1.0
    CDR = 1.0
    恢复 = 1.0
    手搓 = False

    def 武器CD系数(self, 武器类型, 输出类型):
        return 1.0

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

        return round(max(self.CD * self.CDR * 额外CDR / ((self.恢复 + 额外恢复) if not 面板显示 else 1) * (self.武器CD系数(武器类型, 输出类型) - (cdr if not 面板显示 else 0)), self.CD * 0.3)*self.CDR_O, 1)

class 辅助职业觉醒技能(辅助职业主动技能):
    所在等级 = 50
    等级精通 = 30
    等级上限 = 50
    等级精通 = 40
    基础等级 = 14
    一觉力智 = 0
    一觉力智per = 1.0
    一觉力智perTotal = 1.0
    # 28 原力智 941  测试修改为 939
    力智 = [0, 43, 57, 74, 91, 111, 131, 153, 176, 201, 228, 255, 284, 315, 346, 379, 414, 449, 487, 526, 567, 608, 651, 696, 741, 789, 838, 888,
          939, 993, 1047, 1103, 1160, 1219, 1278, 1340, 1403, 1467, 1533, 1600, 1668, 1736, 1804, 1872, 1940, 2008, 2076, 2144, 2212, 2280, 2348]

    def 结算统计(self, context: Buffer, compute_3rd_awake=False):
        buffer_power = context.BUFF量()

        三次觉醒 = context.get_skill_by_name("三次觉醒")
        if not context.check_fun_by_id(20064) and not compute_3rd_awake and self.名称 in 三次觉醒.关联技能:
            return [0] * 5
        旧词条力智 = ((self.适用数值/750 + 1) *
                 (self.力智[self.等级] + self.一觉力智))*self.一觉力智per

        新词条力智 = (((self.适用数值 + 5250) / 750 + 1) *
                 (buffer_power + 5000) * 0.000025 * self.力智[self.等级]) if buffer_power > 0 else 0
        力智 = (旧词条力智 + 新词条力智)*self.一觉力智perTotal
        return [力智, 0, 0, 0, 0]
        # 力智、三攻、智力、体力、精神


class 辅助职业三觉技能(辅助职业主动技能):
    所在等级 = 100
    等级精通 = 30
    等级上限 = 40
    学习间隔 = 5
    绑定一觉力智per = 1.08
    绑定二觉力智per = 0.23
    关联技能 = []

    def 结算统计(self, context: Buffer):
        awake = context.get_skill_by_name('一次觉醒')
        if awake.是否启用:
            values = awake.结算统计(context, True)
            倍率 = self.加成倍率(awake.名称 in self.关联技能)
            return [int(round(i * 倍率)) for i in values]
        return [0] * 5

    def 加成倍率(self, bind_awake):
        if bind_awake:
            return round(1.08 + self.等级 * 0.01, 2)
        else:
            return round(0.23 + self.等级 * 0.01, 2)


BUFF影响技能 = ['勇气祝福', '勇气圣歌', '荣誉祝福', '禁忌诅咒', '死命召唤']
