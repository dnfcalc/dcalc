#ddc49e9ad1ff72a00b53c6cff5b1e920
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "thief/kunoichi/cn/skillDetail"

class ActiveSkill(ActiveSkill):
    ninpou = 0.0  # 六道模式倍率

# 投掷苦无
# thief/kunoichi/506e7ed77d517419a6e1c437a2cedb17
# ddc49e9ad1ff72a00b53c6cff5b1e920/506e7ed77d517419a6e1c437a2cedb17
class Skill1(ActiveSkill):
    """
    向敌人投掷苦无， 使远距离的敌人受到无属性物理伤害。\n
    苦无具有略微的诱导性和穿透力， 可以在跳跃状态中投掷。\n
    技能等级越高， 被苦无命中的敌人的僵直时间越长。
    """
    name = "投掷苦无"
    learnLv = 1
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 2.5
    mp = [8, 91]
    uuid = "506e7ed77d517419a6e1c437a2cedb17"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 苦无投掷个数 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 僵直时间增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最大穿透次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 苦无大小 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 苦无掌握
# thief/kunoichi/852f8ad797db4dca1405cb3e77198401
# ddc49e9ad1ff72a00b53c6cff5b1e920/852f8ad797db4dca1405cb3e77198401
class Skill2(PassiveSkill):
    """
    可以使用苦无系列武器攻击敌人， 且基本攻击更变为魔法攻击。\n
    使用苦无系列武器时基本攻击、 跳跃攻击和前冲攻击会发射出苦无。\n
    若基本攻击中使用后方向键+攻击键时， 则可以往后空翻并投掷苦无。 
    """
    name = "苦无掌握"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 5 #TODO
    rangeLv = 1
    uuid = "852f8ad797db4dca1405cb3e77198401"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 苦无系列武器的投掷距离比率 : {value0}% 
    data0 = get_data(f'{prefix}/{uuid}', 0)


# 基础精通
# thief/kunoichi/5a56514f35cf0270ae8d6c65f8fefd78
# ddc49e9ad1ff72a00b53c6cff5b1e920/5a56514f35cf0270ae8d6c65f8fefd78
class Skill4(PassiveSkill):
    """
    增加基本攻击、 前冲攻击、 跳跃攻击、 [翔击]的攻击力。\n
    在决斗场中， 增益/减益技能、 被动技能的技能攻击力增加效果对[基础精通]无影响。
    """
    name = "基础精通"
    learnLv = 1
    masterLv = 115
    maxLv = 200
    position = 1 #TODO
    rangeLv = 1
    uuid = "5a56514f35cf0270ae8d6c65f8fefd78"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力变化率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 前冲攻击力变化率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 跳跃攻击力变化率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)


# 焰刃
# thief/kunoichi/eb71e1d82d92c7e1d40500a0dcd77aa6
# ddc49e9ad1ff72a00b53c6cff5b1e920/eb71e1d82d92c7e1d40500a0dcd77aa6
class Skill8(ActiveSkill):
    """
    火属性近身魔法技能； 聚集火焰的力量对敌人进行强力攻击并把敌人击飞。\n
    攻击力、 击飞力、 发动速度和攻击范围随技能等级增加而增大。
    """
    name = "焰刃"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 5
    mp = [15, 168]
    uuid = "eb71e1d82d92c7e1d40500a0dcd77aa6"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2
    # 击飞力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 发动速度增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 范围 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)


# 忍法 : 影分身
# thief/kunoichi/a5fa08f5d509e6ff2ebc68856a470b5a
# ddc49e9ad1ff72a00b53c6cff5b1e920/a5fa08f5d509e6ff2ebc68856a470b5a
class Skill13(ActiveSkill):
    """
    把自己的影分身留在原地的同时， 向空中瞬移， 可用左右方向键控制瞬移地点。\n
    被攻击时， 也可以使用此技能。\n
    留在地上的影分身会挑衅一定领域内的敌人； 影分身经过一段时间或受到一定伤害后， 会爆炸并使敌人受到无属性魔法伤害。
    """
    name = "忍法 : 影分身"
    learnLv = 10
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 3
    cds = [0, 30, 29.4, 28.8, 28.2, 27.6, 26.9, 26.3, 25.7, 25.1, 24.5, 23.9, 23.3, 22.7, 22, 21.4, 20.8, 20.2, 19.6, 19, 18.4, 17.8, 17.1, 16.5, 15.9, 15.3, 14.7, 14.1, 13.5, 12.9, 12.2, 11.6, 11, 10.4, 9.8, 9.2, 8.6, 8, 7.3, 6.7, 6.1, 5.5, 4.9, 4.3, 3.7, 3.1, 2.4, 1.8, 1.2, 0.6, 0]
    mp = [20, 230]
    uuid = "a5fa08f5d509e6ff2ebc68856a470b5a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 分身生命值 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 分身持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 挑衅范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def getSkillCD(self, mode=None):
        self.cd = self.cds[self.lv]
        return super().getSkillCD(mode)


# 忍法 : 飞鼠
# thief/kunoichi/4655101518604f874721b3cc249aae10
# ddc49e9ad1ff72a00b53c6cff5b1e920/4655101518604f874721b3cc249aae10
class Skill18(ActiveSkill):
    """
    快速跳向敌人并引爆炸弹， 给予敌人火属性魔法伤害的同时使敌人浮空。
    """
    name = "忍法 : 飞鼠"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 8 #TODO
    rangeLv = 2
    cd = 10
    mp = [10, 84]
    uuid = "4655101518604f874721b3cc249aae10"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 使用次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后一击浮空力比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 每次追击时攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 最后一击时攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 每次追击时爆炸范围增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 最后一击爆炸范围增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 爆炸范围比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)


# 忍术精通
# thief/kunoichi/0b8db1e10b3abbd24d38564e708675d5
# ddc49e9ad1ff72a00b53c6cff5b1e920/0b8db1e10b3abbd24d38564e708675d5
class Skill21(PassiveSkill):
    """
    忍者的专属忍术精通。\n
    学习后， 减少忍术技能的冷却时间； 施放技能时长按技能键可以结印。\n
    根据结印的数量追加技能效果。\n
    忍术技能 : [火遁 · 豪火球之术]、 [幻影手里剑]、 [火遁 · 飓风煞]、 [火遁 · 螺旋手里剑]、 [火遁 · 炎天道]、 [火遁 · 蟾蜍油炎弹]、 [火遁 · 炎舞天璇]、 [火遁·风魔手里剑]、 [八岐大蛇]、 [天照]\n
    施放速度越快， 结印速度越快。
    """
    name = "忍术精通"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 4 #TODO
    rangeLv = 15
    uuid = "0b8db1e10b3abbd24d38564e708675d5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 临、 兵、 斗、 者、 皆、 阵每个结印蓄气时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 忍术技能冷却时间减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"data":data1,"type":"*cdReduce","skills":["火遁·豪火球之术", "忍法 : 幻影手里剑", "火遁·飓风煞", "火遁·螺旋手里剑", "火遁·炎天道", "火遁·蟾蜍油炎弹", "火遁·炎舞天璇", "火遁·风魔手里剑", "八岐大蛇", "天照"]}] # noqa: E501

# 火遁·豪火球之术
# thief/kunoichi/dcb31a63ef58954f44ff2070c42a9a98
# ddc49e9ad1ff72a00b53c6cff5b1e920/dcb31a63ef58954f44ff2070c42a9a98
class Skill22(ActiveSkill):
    """
    结印后从口中吐出大型火焰。\n
    可以在空中使用该技能， 但无法结印， 只能立即施放该技能， 且持续时间减少。\n
    - [忍术精通追加效果] -\n
    增加火焰大小。
    """
    name = "火遁·豪火球之术"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 7.5
    mp = [15, 150]
    uuid = "dcb31a63ef58954f44ff2070c42a9a98"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 12
    # 最后一击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 火遁·豪火球之术喷吐时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # - [忍术精通追加效果] -
    # 达成‘临’结印时大小增加比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 达成‘兵’结印时大小增加比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 达成‘斗’结印时大小增加比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 达成‘者’结印时大小增加比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 达成‘皆’结印时大小增加比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 达成‘阵’结印时大小增加比率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [范围信息]
    # 火焰球大小 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)

    mode = ["普通","六道"]

    def setMode(self, mode):
        if mode == "六道":
            self.skillRation *= self.ninpou

# 空跃
# thief/kunoichi/d085127b0edd719782bd618d5688f4a1
# ddc49e9ad1ff72a00b53c6cff5b1e920/d085127b0edd719782bd618d5688f4a1
class Skill23(ActiveSkill):
    """
    在跳跃中进行再一次跳跃。
    """
    name = "空跃"
    learnLv = 20
    masterLv = 1
    maxLv = 1
    position = 1 #TODO
    rangeLv = 1
    uuid = "d085127b0edd719782bd618d5688f4a1"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 火遁·红莲
# thief/kunoichi/8572675ec6a1f50b6eff6a867376c2de
# ddc49e9ad1ff72a00b53c6cff5b1e920/8572675ec6a1f50b6eff6a867376c2de
class Skill24(ActiveSkill):
    """
    生成强化忍者之力的红莲之火。\n
    红莲之火在持续时间内赋予忍者武器火属性， 增加基本攻击力和技能攻击力。\n
    并在忍者周围旋转， 提高忍者的物理/魔法防御力。\n
    物理/魔法防御力增加效果即时生效。
    """
    name = "火遁·红莲"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 6 #TODO
    rangeLv = 3
    cd = 5
    uuid = "8572675ec6a1f50b6eff6a867376c2de"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 物理防御力增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 魔法防御力增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 忍法 : 幻影手里剑
# thief/kunoichi/4f2e001e9a19eb7bae50ad1840dfb329
# ddc49e9ad1ff72a00b53c6cff5b1e920/4f2e001e9a19eb7bae50ad1840dfb329
class Skill25(ActiveSkill):
    """
    召唤数个幻影， 向敌人连续投掷无数个手里剑。\n
    在空中施放时， 向地面投掷手里剑， 但无法结印。\n
    - [忍术精通追加效果] -\n
    召唤的幻影数量增加。
    """
    name = "忍法 : 幻影手里剑"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 12
    mp = [91, 910]
    uuid = "4f2e001e9a19eb7bae50ad1840dfb329"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 手里剑攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 40
    # 投掷数量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 手里剑反弹次数 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 多段攻击次数上限 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 多段攻击次数下限 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 临、 兵幻影投掷手里剑攻击力比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 斗、 者、 皆、 阵幻影投掷手里剑攻击力比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # - [忍术精通追加效果] -
    # 达成‘临’结印时召唤幻影数增加量 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 达成‘兵’结印时召唤幻影数增加量 : {value8}
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 达成‘斗’结印时召唤幻影数增加量 : {value9}
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 达成‘者’结印时召唤幻影数增加量 : {value10}
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 达成‘皆’结印时召唤幻影数增加量 : {value11}
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 达成‘阵’结印时召唤幻影数增加量 : {value12}
    data12 = get_data(f'{prefix}/{uuid}', 12)


# 忍法 : 原木分身术
# thief/kunoichi/0c262dac3ec41ff79e359ada9c7a7faf
# ddc49e9ad1ff72a00b53c6cff5b1e920/0c262dac3ec41ff79e359ada9c7a7faf
class Skill27(ActiveSkill):
    """
    忍者的固有分身术。\n
    在原地留下一块原木， 然后以肉眼看不见的速度移动一小段距离。\n
    默认向前方移动。 施放技能时按后方向键， 可以向后方移动。\n
    在空中或跳跃中施放时， 直接落地。\n
    施放技能时， 可以消耗[忍法 : 残影术]的残影数量施放， 此时减少冷却时间。
    """
    name = "忍法 : 原木分身术"
    learnLv = 20
    masterLv = 1
    maxLv = 1
    position = 7 #TODO
    rangeLv = 2
    cd = 7
    mp = [200, 200]
    uuid = "0c262dac3ec41ff79e359ada9c7a7faf"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 移动距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [忍法 ： 残影术]施放时冷却时间减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 火遁·飓风煞
# thief/kunoichi/b8f4966608e4ebb3cc80ba4eac3649bb
# ddc49e9ad1ff72a00b53c6cff5b1e920/b8f4966608e4ebb3cc80ba4eac3649bb
class Skill28(ActiveSkill):
    """
    向前方施放火焰飓风。 飓风会在一定时间后爆炸。\n
    飓风可以吸附周围敌人， 可以使用方向键控制施放方向和施放距离。 \n
    - [忍术精通追加效果] -\n
    增加飓风吸附力和大小。
    """
    name = "火遁·飓风煞"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 17
    mp = [61, 610]
    uuid = "b8f4966608e4ebb3cc80ba4eac3649bb"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 飓风攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 24
    # 飓风持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 飓风多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 飓风最后爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # - [忍术精通追加效果] -
    # 每阶段结印飓风大小增加比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 每阶段结印增加爆炸大小比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 每阶段结印吸附范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # [火遁 · 飓风煞]大小 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)


    mode = ["普通","六道"]

    def setMode(self, mode):
        if mode == "六道":
            self.skillRation *= self.ninpou

# 苦无精通
# thief/kunoichi/d53301bb328baf12a3ae482cc6a565dd
# ddc49e9ad1ff72a00b53c6cff5b1e920/d53301bb328baf12a3ae482cc6a565dd
class Skill29(PassiveSkill):
    """
    增加武器的魔法攻击力。 使用苦无系列武器时， 增加命中率， 基本攻击时有一定几率向敌人投掷苦无。
    """
    name = "苦无精通"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 3 #TODO
    rangeLv = 3
    uuid = "d53301bb328baf12a3ae482cc6a565dd"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 命中率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 基本攻击投掷出苦无的几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    associate = [{"data":data0,"type":"$PAtkM"}]

# 烈焰印记
# thief/kunoichi/374f53e8989ef04a8506c8ec99d9ecdc
# ddc49e9ad1ff72a00b53c6cff5b1e920/374f53e8989ef04a8506c8ec99d9ecdc
class Skill30(PassiveSkill):
    """
    增加忍者的基本攻击力和技能攻击力。\n
    [火遁·冥炎业火阵]与一觉前忍术技能额外造成灼伤异常状态伤害。\n
    灼伤攻击力由原技能攻击力进行折算， 且受[忍法 : 残影术]的攻击力比率影响。\n
    该伤害与实际使用的原技能伤害量无关， 成功击中时适用最高伤害量。\n
    [忍法 : 六道轮回]保存的烈焰印记的灼伤伤害不受累积影响， 仍取决于原本伤害量。\n
    烈焰印记追加灼伤的技能 - [火遁 · 豪火球之术]、 [幻影手里剑]、 [火遁 · 飓风煞]、 [火遁 · 螺旋手里剑]、 [火遁 · 炎天道]、 [火遁 · 蟾蜍油炎弹]、 [火遁 · 炎舞天璇]、 [火遁·冥炎业火阵]
    """
    name = "烈焰印记"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 5 #TODO
    rangeLv = 3
    uuid = "374f53e8989ef04a8506c8ec99d9ecdc"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 追加灼伤攻击力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 灼伤几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 灼伤持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    associate = [{"data":data0}]

# 火遁·螺旋手里剑
# thief/kunoichi/7e904ea3d2a9faa054604e55120a9268
# ddc49e9ad1ff72a00b53c6cff5b1e920/7e904ea3d2a9faa054604e55120a9268
class Skill31(ActiveSkill):
    """
    向前方投掷巨大的手里剑。\n
    手里剑会不断地旋转前进攻击沿途的敌人， 同时被手里剑攻击的敌人会被吸附到手里剑中心并受到多段伤害。\n
    - [忍术精通追加效果] -\n
    增加手里剑爆炸大小。\n
    在决斗场的空中使用时， 手里剑在地面上的持续时间会减少， 但是多段击打攻击力会增加。
    """
    name = "火遁·螺旋手里剑"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 12
    mp = [91, 910]
    uuid = "7e904ea3d2a9faa054604e55120a9268"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 旋转时多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 15
    # 最后爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # - [忍术精通追加效果] -
    # 每阶段结印增加最后爆炸大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 在空中使用时， 手里剑持续时间变换率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 在空中使用时， 手里剑多段攻击力变换率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 最后爆炸大小: {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    mode = ["普通","六道"]

    def setMode(self, mode):
        if mode == "六道":
            self.skillRation *= self.ninpou

# 忍法 : 残影术
# thief/kunoichi/dbf8b30c7057032af0d68fcfa289fdae
# ddc49e9ad1ff72a00b53c6cff5b1e920/dbf8b30c7057032af0d68fcfa289fdae
class Skill32(ActiveSkill):
    """
    施放技能时， 可以生成残影代替忍者继续施放当前技能。  \n
    进入地下城后自动发动该技能， 发动后强制取消当前技能时， 会出现残影继续代替忍者使用强制取消的技能。\n
    残影经过一段时间后会恢复， 且可以连续施放。  \n
       该技能无法享受[忍术精通]的加成。\n
    在决斗场中， 残影施放的技能会受到结印数量的影响， 并存在前置冷却时间。
    """
    name = "忍法 : 残影术"
    learnLv = 35
    masterLv = 1
    maxLv = 11
    position = 3 #TODO
    rangeLv = 5
    cd = 15
    mp = [128, 1280]
    uuid = "dbf8b30c7057032af0d68fcfa289fdae"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 残影使用技能时攻击力比率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 残影数量上限 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 残影恢复时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 决斗场前置冷却时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)

    associate = [{"data":data0}]

# 火遁·炎天道
# thief/kunoichi/5152480fdde81362575a488d4cec4af9
# ddc49e9ad1ff72a00b53c6cff5b1e920/5152480fdde81362575a488d4cec4af9
class Skill33(ActiveSkill):
    """
    在地面引发强烈爆炸使敌人浮空， 然后， 跳起将火焰球扔向地面， 引发巨大爆炸。
    """
    name = "火遁·炎天道"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cube = 1
    cd = 18
    mp = [128, 1280]
    uuid = "5152480fdde81362575a488d4cec4af9"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 地面爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 0
    # 空中生成的火焰球攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 火焰球直接打击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 火焰球爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # - [忍术精通追加效果] -
    # 达成‘临’结印时大小增加比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 达成‘兵’结印时大小增加比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 达成‘斗’结印时大小增加比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 达成‘者’结印时大小增加比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 达成‘皆’结印时大小增加比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 达成‘阵’结印时大小增加比率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [范围信息]
    # 爆炸大小 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)

    mode = ["地面","空中","六道"]

    def setMode(self, mode):
        if mode == "地面":
            self.hit0 = 1
            self.hit1 = 1
        elif mode == "空中":
            self.hit0 = 0
            self.hit1 = 1
        elif mode == "六道":
            self.hit0 = 1
            self.hit1 = 1
            self.skillRation *= self.ninpou

    def vp_1(self):
        """
        [火遁·炎天道]\n
        在爆炸点生成火焰地带\n
         - 使进入火焰地带的敌人进入强制控制状态\n
        烈焰印记灼伤伤害额外 +20%\n
         - 命中时， 始终造成技能最大伤害量50%的伤害\n
         - 伤害量不受[忍法 : 六道轮回]充能率的影响\n
         - 技能攻击力 -14%\n
        将[火遁·炎天道]记录在[忍法 : 六道轮回]时， 赋予以下效果\n
         - 施放时， 攻击、 移动、 施放速度 +10%， 持续10秒\n
         - 施放强化残影攻击时， 一次性结算剩余灼伤伤害
        """
        ...

    def vp_2(self):
        """
        [火遁·炎天道]\n
        向前方最强敌人投掷火焰球\n
         - 删除地面爆炸和空中火焰攻击\n
         - 总攻击力相同\n
        火焰球命中时恢复1个[忍法 : 残影术]残影
        """
        ...

# 忍法 : 替身术
# thief/kunoichi/2391a27457b5a8c6fa4b4670a91bdd11
# ddc49e9ad1ff72a00b53c6cff5b1e920/2391a27457b5a8c6fa4b4670a91bdd11
class Skill34(ActiveSkill):
    """
    隐身后引发爆炸， 并与周围的敌人对换位置。 对换位置时， 会为敌人附着起爆符。 换位后， 忍者会扔出苦无引爆起爆符。\n
    与附近敌人无法对换位置时， 使用木头替代自身。\n
    对无法抓取的敌人不适用控制效果。\n
    可在被击和倒地状态下忽略被击和倒地动作立即使用。\n
    与[忍法 : 影分身]共享冷却时间。\n
    在决斗场中， 无法使用该技能。
    """
    name = "忍法 : 替身术"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 3
    cd = 25
    mp = [91, 910]
    uuid = "2391a27457b5a8c6fa4b4670a91bdd11"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 地面爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 苦无攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 起爆符爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 爆炸大小: {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [忍法 : 替身术]\n
        攻击范围 +50%\n
        可记录在[忍法 : 六道轮回]\n
         - 技能攻击力 -33%\n
        追加烈焰印记灼伤伤害\n
         - 命中时， 始终造成技能最大伤害量30%的伤害\n
         - 伤害量不受[忍法 : 六道轮回]充能率的影响\n
         - 技能攻击力 -25%\n
        将[忍法 : 替身术]记录在[忍法 : 六道轮回]时， 赋予以下效果\n
         - 施放强化残影攻击时， 一次性结算剩余灼伤伤害
        """
        ...

    def vp_2(self):
        """
        [忍法 : 替身术]\n
        技能结束后适用附加效果， 效果持续5秒\n
         - 所受伤害 -50%\n
         - 进入霸体状态
        """
        ...

# 忍法 : 六道轮回
# thief/kunoichi/5892d1fa4462e561ac8f8d2c74892b0a
# ddc49e9ad1ff72a00b53c6cff5b1e920/5892d1fa4462e561ac8f8d2c74892b0a
class Skill35(ActiveSkill):
    """
    忍者领悟火焰忍术真谛后习得秘术， 学习后， 周围出现逐渐变强的燃烧火焰， 并累积残影攻击力。\n
    施放后， 在持续时间内每次施放忍术技能时凝聚火焰并累积该技能攻击力， 再次按技能键或持续时间结束时， 出现强化后的残影， 并用强大的炎舞将敌人燃烧殆尽。\n
    伤害取决于累积的忍术技能攻击力。\n
    强化的残影攻击力按施放技能前的累积程度成比例增加， 并受冷却时间相关的属性影响。\n
    同一个技能最多只能保存3次。\n
    [忍法 : 残影术]每次消耗残影时， 可保存的持续时间增加。\n
    残影为无敌状态， 无法被敌人攻击。\n
    可保存的技能 - 火遁·豪火球之术、 火遁·飓风煞、 忍法 : 幻影手里剑、 火遁·螺旋手里剑、 火遁 : 炎天道、 火遁 : 蟾蜍油炎弹、 火遁 : 炎舞天璇、 火遁·风魔手里剑、 八岐大蛇、 天照
    """
    name = "忍法 : 六道轮回"
    learnLv = 40
    masterLv = 1
    maxLv = 11
    position = 5 #TODO
    rangeLv = 3
    cd = 20
    mp = [164, 1640]
    uuid = "5892d1fa4462e561ac8f8d2c74892b0a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 保存技能个数上限 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 火焰残影攻击力最大比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最大累积时间 : 20秒
    # 可保存的持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 每次消耗残影时可保存的持续时间增加 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 范围 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    associate = [{"data":data1,"type":"+ninpou"}] # noqa: E501
    # "skills":["火遁·豪火球之术","火遁·飓风煞","忍法 : 幻影手里剑","火遁·螺旋手里剑","火遁 : 炎天道","火遁 : 蟾蜍油炎弹","火遁 : 炎舞天璇","火遁·风魔手里剑","八岐大蛇","天照"]

# 火遁·蟾蜍油炎弹
# thief/kunoichi/fc458e449ee00b01dbf88d09aae65462
# ddc49e9ad1ff72a00b53c6cff5b1e920/fc458e449ee00b01dbf88d09aae65462
class Skill36(ActiveSkill):
    """
    召唤火焰蟾蜍。\n
    蟾蜍倒吸一口气后向前发射一个大型油炎弹。 \n
    油炎弹爆炸范围随[忍术精通]技能的结印阶段增加。\n
    可在空中施放， 同时会增加火焰蟾蜍登场时的冲击波范围。\n
    - [忍术精通追加效果] -\n
    增加油炎弹的爆炸大小。
    """
    name = "火遁·蟾蜍油炎弹"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [164, 1640]
    uuid = "fc458e449ee00b01dbf88d09aae65462"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 火焰蟾蜍登场时冲击波攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 油炎弹攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 油炎弹爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 火焰蟾蜍消失时攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 在空中召唤时火焰蟾蜍登场时冲击波范围增加比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # - [忍术精通追加效果] -
    # 达成‘临’结印时油炎弹爆炸大小 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 达成‘兵’结印时油炎弹爆炸大小 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 达成‘斗’结印时油炎弹爆炸大小 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 达成‘者’结印时油炎弹爆炸大小 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 达成‘皆’结印时油炎弹爆炸大小 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 达成‘阵’结印时油炎弹爆炸大小 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # [范围信息]
    # 爆炸大小 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)

    mode = ["普通","六道"]

    def setMode(self, mode):
        if mode == "六道":
            self.skillRation *= self.ninpou

    def vp_1(self):
        """
        [火遁·蟾蜍油炎弹]\n
        变更登场位置\n
        蟾蜍大小 +50%\n
        油炎弹爆炸范围 +30%\n
        蟾蜍登场及油炎弹发射速度 +50%\n
        删除登场、 消失、 油炎弹攻击的攻击力\n
         - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [火遁·蟾蜍油炎弹]\n
        冷却时间和攻击力 +70%\n
        消耗[八尺琼勾玉]的红色勾玉时， 适用附加效果， 效果持续20秒\n
         - 攻击、 移动、 施放速度 +10%\n
         - 物理和魔法防御力 +5000
        """
        self.cd *= 1.7
        self.skillRation *= 1.7
        ...

# 火遁·炎舞天璇
# thief/kunoichi/1812a1ece67bb37b6b44b54766450064
# ddc49e9ad1ff72a00b53c6cff5b1e920/1812a1ece67bb37b6b44b54766450064
class Skill37(ActiveSkill):
    """
    施展秘笈， 以肉眼无法辨别的速度快速舞动斩击敌人， 随后绽放出如炎玉一般的红莲之花对敌人进行多段攻击。 最后一击会出现更大的红莲之花攻击敌人。\n
    多段攻击次数越多， 则最后的火焰爆炸范围越大。\n
    按跳跃键， 可中断多段攻击， 立即施放最后一击； 快速舞动斩击时， 若按跳跃键， 则可立即施放红莲之花。\n
    [忍术精通追加效果]\n
    增加斩击速度。
    """
    name = "火遁·炎舞天璇"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [311, 3110]
    uuid = "1812a1ece67bb37b6b44b54766450064"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 8
    # 红莲之花多段攻击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 25
    # 斩击多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 红莲之花多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 最后一击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # - [忍术精通追加效果] -
    # 每阶段结印增加斩击速度 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 最后爆炸大小: {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    mode = ["普通","六道"]

    def setMode(self, mode):
        if mode == "六道":
            self.skillRation *= self.ninpou

    def vp_1(self):
        """
        [火遁·炎舞天璇]\n
        斩击次数 -5次\n
         - 总攻击力相同\n
        出现火焰残影， 一起释放火焰之花\n
        增加最后一击攻击范围
        """
        ...

    def vp_2(self):
        """
        [火遁·炎舞天璇]\n
        通过[忍法 : 残影术]强制中断[火遁·炎舞天璇]时， 进入无敌状态1秒\n
        [火遁·炎舞天璇]的蓄气时间 -90%
        """
        ...

# 暗炎残星
# thief/kunoichi/d89f26862e348a801b30bb9fd7125db5
# ddc49e9ad1ff72a00b53c6cff5b1e920/d89f26862e348a801b30bb9fd7125db5
class Skill38(PassiveSkill):
    """
    掌握暗炎之术， 忍者击中的敌人时， 会将敌人标记为追踪目标。\n
    被标记为追踪目标的敌人头上会生成追踪标记。 忍者能对有追踪标记的敌人造成更高的暴击伤害。\n
    追踪标记经过一定时间后消失。\n
    [当敌人察觉到自己成为被猎杀的目标时， 他的心脏早就停止了跳动。]
    """
    name = "暗炎残星"
    learnLv = 45
    masterLv = 1
    maxLv = 11
    position = 3 #TODO
    rangeLv = 5
    uuid = "d89f26862e348a801b30bb9fd7125db5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 暴击伤害增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 追踪标记持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"data":data0}]

# 毕方之印
# thief/kunoichi/2c9d9a36c8401bddff6cdb80fab8dc24
# ddc49e9ad1ff72a00b53c6cff5b1e920/2c9d9a36c8401bddff6cdb80fab8dc24
class Skill39(ActiveSkill):
    """
    引燃毕方之炎周围敌人的灵魂并产生爆炸， 增加属性攻击力和魔法暴击率。\n
    离忍者较近的敌人会附加“炎”烙印， 较远的敌人附加“火”烙印。\n
    被附加火烙印和炎烙印的敌人会受到周期性的火属性伤害。\n
    火烙印和炎烙印消失时， 将给与敌人火属性爆炸伤害。\n
    [掌握毕方之印的毕方之炎忍术变得更精湛， 被她的火焰吞噬的敌人将消失无踪。]
    """
    name = "毕方之印"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 3
    uuid = "2c9d9a36c8401bddff6cdb80fab8dc24"
    type = "passive"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 属性攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 火烙印生成距离 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 火烙印多段攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit0 = 1 / 2.5
    # 火烙印多段攻击间隔 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 火烙印持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 火烙印爆炸攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 1
    # 炎烙印生成距离: {value7}px
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 炎烙印多段攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    hit8 = 1 / 0.5
    # 炎烙印多段攻击间隔 : {value9}秒
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 炎烙印持续时间 : {value10}秒
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 炎烙印爆炸攻击力 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    hit11 = 1

    associate = [{"data":data0}]

    def getSkillCD(self, mode=None):
        return 1.0

# 火遁·冥炎业火阵
# thief/kunoichi/2ba299855fc22192cba4f73db75e9d0e
# ddc49e9ad1ff72a00b53c6cff5b1e920/2ba299855fc22192cba4f73db75e9d0e
class Skill40(ActiveSkill):
    """
    召唤出消灭敌人的冥炎业火阵给予敌人火属性伤害。\n
    之后依次激活阵法结印， 6个结印全部激活后同时引爆毁灭敌人。
    """
    name = "火遁·冥炎业火阵"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [881, 7403]
    uuid = "2ba299855fc22192cba4f73db75e9d0e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 业火阵出现时攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 业火阵爆炸时攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 吸附敌人时火焰攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 结印出现时攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 结印爆炸时攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # 业火阵范围内攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 10
    # 业火阵多段攻击次数 : {value6}次
    data6 = get_data(f'{prefix}/{uuid}', 6)

# 忍法 : 飞燕手里剑
# thief/kunoichi/b89c9ab317bc0a443f6497b7cca2f6a8
# ddc49e9ad1ff72a00b53c6cff5b1e920/b89c9ab317bc0a443f6497b7cca2f6a8
class Skill41(ActiveSkill):
    """
    像燕子一样飞向空中后跟火焰残影一起发射手里剑。\n
    忍者闪烁移动时， 可将附近的敌人往中间聚集， 并与火焰残影一起连续发射手里剑。\n
    可以在自身被击或倒地状态下施放该技能； 若在空中施放该技能， 最后一击则更变为发射苦无。\n
    [忍法 : 飞燕手里剑]的手里剑贯穿敌人时， 可以对敌人附着封印力量的符咒， 在最终爆炸之前强控敌人。\n
    [忍法 : 六道轮回]无法记录该技能。
    """
    name = "忍法 : 飞燕手里剑"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [400, 1120]
    uuid = "b89c9ab317bc0a443f6497b7cca2f6a8"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 手里剑地面爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 闪烁移动攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 4
    # 闪烁移动时发射的穿刺手里剑攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 16
    # 闪烁移动时手里剑爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 16
    # 闪烁移动时手里剑多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 闪烁移动时发射的穿刺多段攻击次数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 闪烁移动时手里剑爆炸多段攻击次数 : {value6}次
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 最后一闪攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    hit7 = 1
    # 最后一击穿刺攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    hit8 = 10
    # 最后一击手里剑爆炸攻击力 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    hit9 = 10
    # 最后一击手里剑爆炸多段攻击次数 : {value10}次
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 被击或倒地状态下使用时攻击力增加比率 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 在空中使用时， 最后一击投掷苦无数增加量 : {value12}
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # [范围信息]
    # 最后爆炸大小 : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13)

    mode = ["地面","空中","六道"]

    def setMode(self, mode):
        if mode == "地面":
            self.hit8 = 10
            self.hit9 = 10
        elif mode == "空中":
            self.hit0 = self.hit1 = self.hit2 = self.hit3 = self.hit4 = self.hit5 = self.hit6 = self.hit7 = 0
            self.hit8 = 15
            self.hit9 = 15
        elif mode == "六道":
            self.hit8 = 10
            self.hit9 = 10
            self.skillRation *= self.ninpou if self.vp == 2 else 0

    def vp_1(self):
        """
        [忍法 : 飞燕手里剑]\n
        命中时， 初始化[忍法 : 原木分身术]的冷却时间\n
        强制控制时间 +1秒\n
        技能结束后， 额外进入0.5秒的无敌状态
        """
        ...

    def vp_2(self):
        """
        [忍法 : 飞燕手里剑]\n
        闪烁速度 +30%\n
        手里剑爆炸范围 +30%\n
        判定为忍术技能\n
         - 可记录在[忍法 : 六道轮回]\n
         - 技能攻击力 -33%
        """
        ...

# 火遁·风魔手里剑
# thief/kunoichi/7cf17936a039b418660424125dc968d7
# ddc49e9ad1ff72a00b53c6cff5b1e920/7cf17936a039b418660424125dc968d7
class Skill42(ActiveSkill):
    """
    召唤禁忌之兵器[风魔手里剑]毁灭敌人。\n
    施放时召唤4个风魔手里剑， 抓住手里剑向前方投掷。 投掷的风魔手里剑旋转飞出， 对范围内的敌人造成多段伤害， 然后自动飞回。\n
    此时， 忍者可以抓取风魔手里剑， 使其融合成巨型风魔手里剑并再次向前方投掷， 造成额外伤害。\n
    巨型风魔手里剑对范围内敌人造成多段伤害后爆炸。\n
    在空中施放[火遁 : 风魔手里剑]时， 立即投掷出巨型风魔手里剑。\n
    投掷后跳跃或施放其他技能过程中， 无法抓取飞回的风魔手里剑。\n
    [忍术精通]蓄气后施放时， 增加巨型风魔手里剑的爆炸范围。
    """
    name = "火遁·风魔手里剑"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [800, 1680]
    uuid = "7cf17936a039b418660424125dc968d7"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 风魔手里剑攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 15
    # 风魔手里剑多段攻击次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 巨型风魔手里剑攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 10
    # 巨型风魔手里剑多段攻击次数 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 巨型风魔手里剑爆炸攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # - [忍术精通追加效果] -
    # 达成‘临’、 ‘兵’、 ‘斗’结印时爆炸范围 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 达成‘者’、 ‘皆’、 ‘阵’结印时爆炸范围 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 最后爆炸大小: {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    mode = ["普通","六道"]

    def setMode(self, mode):
        if mode == "六道":
            self.skillRation *= self.ninpou

    def vp_1(self):
        """
        [火遁·风魔手里剑]\n
        立即投掷巨型风魔手里剑\n
        巨型风魔手里剑多段攻击次数 +10次\n
         - 总攻击力相同\n
        巨型风魔手里剑大小 +30%\n
        终结爆炸范围 +20%
        """
        ...

    def vp_2(self):
        """
        [火遁·风魔手里剑]\n
        基本冷却时间从50秒变更为43秒\n
         - 技能攻击力 -14%\n
        追加烈焰印记灼伤伤害\n
         - 命中时， 始终造成技能最大伤害量30%的伤害\n
         - 施放[忍法 : 六道轮回]时无效\n
         - 技能攻击力 -14%\n
        将[火遁·风魔手里剑]记录在[忍法 : 六道轮回]时， 赋予以下效果\n
         - [忍法 : 六道轮回]技能施放速度 +30%\n
         - 施放强化残影攻击时， 一次性结算剩余灼伤伤害
        """
        ...

# 八咫镜
# thief/kunoichi/f0cc2c950f3bdf4103c75fa496bcac34
# ddc49e9ad1ff72a00b53c6cff5b1e920/f0cc2c950f3bdf4103c75fa496bcac34
class Skill43(PassiveSkill):
    """
    八咫镜会强化分身、 残影类技能的特性。\n
    - [忍法 : 残影术] -\n
    增加残影数量和蓄力速度。\n
    - [忍法 : 六道轮回] -\n
    增加[忍法 : 六道轮回]技能施放速度。
    """
    name = "八咫镜"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 8 #TODO
    rangeLv = 3
    uuid = "f0cc2c950f3bdf4103c75fa496bcac34"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [忍法 ： 残影术]蓄力速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [忍法 ： 残影术]残影数量上限增加 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [忍法 ： 六道轮回]强化残影攻击速度增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)


# 八岐大蛇
# thief/kunoichi/147d005ac868e0de52b1f255eea35d62
# ddc49e9ad1ff72a00b53c6cff5b1e920/147d005ac868e0de52b1f255eea35d62
class Skill44(ActiveSkill):
    """
    召唤神兽八岐大蛇喷吐黑色火焰， 同时生成火焰毒雾。\n
    - [忍术精通追加效果] -\n
    增加毒雾持续时间。
    """
    name = "八岐大蛇"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 2
    cube = 3
    cd = 43
    mp = [600, 4500]
    uuid = "147d005ac868e0de52b1f255eea35d62"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 火焰吐息的攻击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 召唤时， 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 火焰吐息攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 10
    # 毒雾攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 23
    # 毒雾多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 结印时毒雾多段攻击次数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 火焰吐息攻击范围 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    mode = ["普通","六道"]

    def setMode(self, mode):
        if mode == "六道":
            self.skillRation *= self.ninpou

    def vp_1(self):
        """
        [八岐大蛇]\n
        八岐大蛇的大小增加\n
        变更召唤位置\n
        删除召唤时攻击力和毒雾领域\n
         - 总攻击力相同\n
        每叠加1层八尺琼勾玉， 火焰吐息范围 +5%\n
        火焰吐息范围 +20%
        """
        ...

    def vp_2(self):
        """
        [八岐大蛇]\n
        火焰吐息持续时间 -50%\n
         - 火焰吐息多段攻击次数 -5次\n
         - 追加火焰吐息爆炸攻击\n
         - 总攻击力相同\n
        增加烈焰印记灼伤伤害\n
         - 命中时， 始终造成技能最大伤害量30%的伤害\n
         - 施放[忍法 : 六道轮回]时无效\n
         - 技能攻击力 -14%\n
        将[八岐大蛇]记录在[忍法 : 六道轮回]时， 赋予以下效果\n
         - 施放[忍法 : 六道轮回]时攻击范围 +30%\n
         - 施放强化残影攻击时， 一次性结算剩余灼伤伤害
        """
        ...

# 八尺琼勾玉
# thief/kunoichi/8510294202d0e042dd29a2422fc6770d
# ddc49e9ad1ff72a00b53c6cff5b1e920/8510294202d0e042dd29a2422fc6770d
class Skill45(PassiveSkill):
    """
    召唤勾玉， 强化召唤兽的特性和能力。\n
    勾玉会在学习[火遁·蟾蜍油炎弹]、 [八岐大蛇]、 [天照]时自动激活， 并旋转在使用者身边。\n
    施放[火遁·红莲]技能时， 勾玉被火焰缠绕， 额外增加物理/魔法防御力。
    """
    name = "八尺琼勾玉"
    learnLv = 75
    masterLv = 1
    maxLv = 1
    position = 5 #TODO
    rangeLv = 1
    uuid = "8510294202d0e042dd29a2422fc6770d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 红色勾玉增加[火遁·蟾蜍油炎弹]施放速度 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 黑色勾玉增加[八岐大蛇]毒雾范围 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 黄色勾玉减少光焰弹攻击前僵直 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 施放[火遁·红莲]时物理/魔法防御力额外增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 天照
# thief/kunoichi/47bd4871f29defc2a0021ee9261d7a5b
# ddc49e9ad1ff72a00b53c6cff5b1e920/47bd4871f29defc2a0021ee9261d7a5b
class Skill46(ActiveSkill):
    """
    召唤天照发射自动追踪敌人的光焰弹。\n
    - [忍术精通追加效果] -\n
    增加攻击力。
    """
    name = "天照"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 2
    cube = 5
    cd = 51
    mp = [800, 6000]
    uuid = "47bd4871f29defc2a0021ee9261d7a5b"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 天照登场和消失时冲击波攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2
    # 光焰弹攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 8
    # 光焰弹基本发射数量 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [临兵斗]结印时攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [者皆阵]结印时攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 锁定敌人范围 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)

    associate = [{"data":data4,"skills":["天照"]}]

    mode = ["普通","六道"]

    def setMode(self, mode):
        if mode == "六道":
            self.skillRation *= self.ninpou

    def vp_1(self):
        """
        [天照]\n
        天照登场时间减少\n
        持续时间内， 向进入范围内的敌人发射光焰弹\n
        删除登场和消失攻击力\n
         - 总攻击力相同\n
        天照结印蓄气时间 -50%
        """
        ...

    def vp_2(self):
        """
        [天照]\n
        天照登场后落下火雨\n
         - 黄色勾玉效果变更为攻击范围 +10%\n
        施放[天照]过程中， 通过其他技能强制中断残影时， 立即恢复残影\n
        追加烈焰印记灼伤伤害\n
         - 命中时， 始终造成技能最大伤害量30%的伤害\n
         - 施放[忍法 : 六道轮回]时无效\n
         - 技能攻击力 -14%\n
        将[天照]记录在[忍法 : 六道轮回]时， 赋予以下效果\n
         - 施放时， 10秒内[忍法 : 残影术]残影恢复速度 +50%\n
         - 施放强化残影攻击时， 一次性结算剩余灼伤伤害
        """
        ...

# 火炎灼空 : 草雉剑
# thief/kunoichi/669f1428193f61f9d92c743b72438c4d
# ddc49e9ad1ff72a00b53c6cff5b1e920/669f1428193f61f9d92c743b72438c4d
class Skill47(ActiveSkill):
    """
    召唤出火系忍术根源的古代武器——草雉剑。\n
    使用技能后， 按<X>键可以直接装备召唤出来的草雉剑， 技能持续时间内， 基本攻击变更为火焰剑舞， 灼伤伤害增加， 烈焰印记持续时间发生改变。\n
    并且， 火焰剑舞命中时， 累积[忍法 : 六道轮回]的残影攻击力。\n
    装备草雉剑的状态下， 若再次按技能键， 则残影会投掷火焰剑并引起大爆炸。\n
    最后投掷剑和爆炸的攻击力受[忍法 : 残影术]的影响。 
    """
    name = "火炎灼空 : 草雉剑"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2800, 5000]
    uuid = "669f1428193f61f9d92c743b72438c4d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 剑下落时的攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 剑在地面散发的火焰攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后投掷剑时的攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最后的3次爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 装备草雉剑时第一次斩击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 装备草雉剑时第二次斩击攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 装备草雉剑时空中、 后跳斩击攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 斩击额外灼伤攻击力比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 斩击灼伤持续时间 : {value8}秒
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 烈焰印记灼伤持续时间适用比率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [火遁·飓风煞]卷入敌人的力量增加率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 召唤的草雉剑持续时间 : {value11}秒
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 草雉剑装备的持续时间 : {value12}秒
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 装备草雉剑时不知火的攻击速度增加 : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # 装备草雉剑后， 斩击命中时， [忍法 ： 六道轮回]攻击力累积量 : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)

    mode = ["终结","平x","跳x"]

    def setMode(self, mode):
        if mode == "终结":
            self.hit2 = 1
            self.hit3 = 3
        elif mode == "平x":
            self.hit4 = 1
            self.hit5 = 1
        elif mode == "跳x":
            self.hit6 = 2

    def getSkillCD(self, mode=None):
        if mode == "平x" or mode == "跳x":
            return 1.0
        return super().getSkillCD(mode)
# 三元刹
# thief/kunoichi/2ff50c35efcf0f287c4c418c8454da48
# ddc49e9ad1ff72a00b53c6cff5b1e920/2ff50c35efcf0f287c4c418c8454da48
class Skill48(PassiveSkill):
    """
    隐夜·忍者获得查克拉根源——八咫乌之力， 激发三神器的隐藏力量， 领悟忍术的所有知识。\n
    学习后， 增加基本攻击力和转职技能攻击力， 部分技能附加特殊效果。\n
    [忍术精通]\n
    - 减少结印时间， 施放者完成[临兵斗者皆阵]所有结印施放技能时， 适用[忍法 : 残影术]的攻击力。\n
    [火遁·螺旋手里剑]\n
    - 地面施放时\n
     - 螺旋手里剑命中敌人时再次按技能键， 移动到命中位置。\n
    - 空中施放时\n
     - 螺旋手里剑击中地面时再次按技能键， 移动到命中位置。
    """
    name = "三元刹"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "2ff50c35efcf0f287c4c418c8454da48"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 结印时间减少率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"data":data1}]

# 勾玉之火 : 镰鼬
# thief/kunoichi/845e0ce3235e19f60cc82a082d072cba
# ddc49e9ad1ff72a00b53c6cff5b1e920/845e0ce3235e19f60cc82a082d072cba
class Skill49(ActiveSkill):
    """
    激发八尺琼勾玉的所有隐藏力量， 将其变化为火焰精灵镰鼬。\n
    镰鼬用勾玉之焰席卷敌人后， 重新回到施放者周围。\n
    终结攻击命中敌人时恢复残影， 并立即造成剩余灼伤伤害。\n
    每次消耗残影， [勾玉之火 : 镰鼬]技能的剩余冷却时间减少一定比率， 施放技能前最多可减少10次。\n
    可以通过On/Off功能设置是否立即造成灼伤伤害。
    """
    name = "勾玉之火 : 镰鼬"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 7
    cd = 60 * 0.6
    mp = [960, 2000]
    uuid = "845e0ce3235e19f60cc82a082d072cba"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 火焰旋风攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 旋风多段攻击次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 终结攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 最后一击命中灼伤的敌人时恢复的残影数 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 消耗残影时剩余冷却时间减少率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 剩余冷却时间最多可减少次数 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 火源限界·八咫乌
# thief/kunoichi/6067de229738524687e5a9ee1c53d583
# ddc49e9ad1ff72a00b53c6cff5b1e920/6067de229738524687e5a9ee1c53d583
class Skill50(ActiveSkill):
    """
    激发三神器隐藏的所有力量， 创造出查克拉的根源——八咫乌， 消灭敌人。\n
    八尺琼勾玉中加上草雉剑的火焰创造出的“八咫乌”以基本形态喷射太古烈炎攻击敌人， 并通过八咫镜复制成3个。\n
    然后， 激发三神器隐藏的所有力量的3个八咫乌重新合体， 展现释放全部查克拉的最终形态。\n
    无法通过[忍法 : 残影术]和[忍法 : 六道轮回]使用。\n
    八咫乌的所有攻击受[忍法 : 残影术]的影响。\n
    [三次觉醒技能]\n
    选择[火遁·冥炎业火阵]使用三次觉醒技能时， 与[火遁·冥炎业火阵]共享冷却时间。 \n
    选择[火炎灼空 : 草雉剑]使用三次觉醒技能时， 可以使用三次觉醒技能代替[火炎灼空 : 草雉剑]的终结攻击。 三次觉醒技能在冷却中、 [火炎灼空 : 草雉剑]终结攻击已发动或未装备草雉剑的状态下， 无法使用三次觉醒技能。
    """
    name = "火源限界·八咫乌"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "6067de229738524687e5a9ee1c53d583"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 八咫乌乱舞攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 12
    # 八咫乌乱舞多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 八咫乌回归多段攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 14
    # 八咫乌回归多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 终结爆炸攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'kunoichi'
        self.nameCN = '隐夜·忍者'
        self.role = 'thief'
        self.角色 = '暗夜使者'
        self.职业 = '忍者'
        self.jobId = 'ddc49e9ad1ff72a00b53c6cff5b1e920'
        self.jobGrowId = 'a9a4ef4552d46e39cf6c874a51126410'

        self.武器选项 = ['苦无','匕首', '双剑', '手杖'] # TODO
        self.输出类型选项 = ["魔法百分比"] # TODO
        self.输出类型 = '魔法百分比' # TODO
        self.防具精通属性 = ['智力'] # TODO
        self.防具类型 = '布甲'
        self.buff = 2.123

        super().__init__(equVersion, __name__)
