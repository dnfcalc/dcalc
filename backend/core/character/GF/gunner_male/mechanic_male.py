#afdf3b989339de478e85b614d274d1ef
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "gunner_male/mechanic_male/cn/skillDetail"


# RX-78追击者
# gunner_male/mechanic_male/8ee0099656df08a0b39225f8a21d514b
# afdf3b989339de478e85b614d274d1ef/8ee0099656df08a0b39225f8a21d514b
class Skill7(ActiveSkill):
    """
        设置诱导型爆炸机器人RX-78追击者， 使其跟踪敌人后爆炸并对周围敌人造成火属性魔法伤害。\n
        对建筑型护甲的敌人可以造成125%的伤害。
    """
    name = "RX-78追击者"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 2.5
    mp = [10, 82]
    uuid = "8ee0099656df08a0b39225f8a21d514b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)


# EZ-8爆破者
# gunner_male/mechanic_male/9bff7f2559e003766fee2853dca00631
# afdf3b989339de478e85b614d274d1ef/9bff7f2559e003766fee2853dca00631
class Skill19(ActiveSkill):
    """
        设置固定型爆破机器人EZ-8爆破者， 使其经过一定时间后在原地爆炸并给予周围敌人火属性魔法伤害。\n
        设置机器人时， 按住技能键就可以蓄气， 蓄气越多机器人的爆破延迟时间就会越长。
    """
    name = "EZ-8爆破者"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 6.5
    mp = [41, 347]
    uuid = "9bff7f2559e003766fee2853dca00631"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 爆炸延迟时间 : 8秒
    # 爆炸延迟时间上限 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 爆炸大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)


# 机械改良
# gunner_male/mechanic_male/fc7a3f4c2852c832a2f20af63d5d212f
# afdf3b989339de478e85b614d274d1ef/fc7a3f4c2852c832a2f20af63d5d212f
class Skill21(ActiveSkill):
    """
        增加机械师的基本攻击力和技能攻击力， 并增强我方机器人的威力和移动速度， 效果持续一定时间。\n
        在决斗场中， 同时增加机器人生命值上限。
    """
    name = "机械改良"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 5
    rangeLv = 3
    cd = 5
    uuid = "fc7a3f4c2852c832a2f20af63d5d212f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 机器人移动速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 机器人生命值最大值增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 机械引爆
# gunner_male/mechanic_male/92360eab6e1f378902018eca681ac629
# afdf3b989339de478e85b614d274d1ef/92360eab6e1f378902018eca681ac629
class Skill22(ActiveSkill):
    """
        普通引爆 : 强制引爆自身周围的[RX-78追击者]、 [EZ-8爆破者]、 [RX-60陷阱追击者]、 [红色破坏者]、 [钢铁机器人]、 [修复者莱格]、 [神力雷克斯]、 [拦截机工厂]、 [EZ-10反击者]、 [TX-45特攻队]， 并给予周围敌人爆炸伤害。\n
        瞄准引爆 : 按住技能键后就会出现光标， 若移动光标后松开技能键， 则机器人会向光标方向突进并爆炸。\n
    [学习索菲亚后]\n
        瞄准引爆时， 所有机器人立即瞬移到指定位置并爆炸。 各技能分别发生爆炸， 合并技能伤害造成1次打击。
    """
    name = "机械引爆"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 3
    rangeLv = 3
    cd = 1
    mp = [4, 12]
    uuid = "92360eab6e1f378902018eca681ac629"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 引爆范围 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 爆炸伤害变化率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [
        {"data":[i-100 if i > 100 else i for i in data1],"skills":["RX-78追击者","Ez-8自爆者","RX-60陷阱追击者","空投支援", "EZ-10反击者", "TX-45特攻队"]},
        # 光能不享受引爆
        {"type":"*power1","data":[i-100 if i > 100 else i for i in data1],"skills":["拦截机工厂"]},
        {"type":"+power2","data":[i-100 if i > 100 else i for i in data1],"skills":["空战机械 : 风暴"]}
    ]

# G-14手雷
# gunner_male/mechanic_male/de3fea2d65c597f4d55c70a02b97fc79
# afdf3b989339de478e85b614d274d1ef/de3fea2d65c597f4d55c70a02b97fc79
class Skill23(ActiveSkill):
    """
        向前方投掷G-14手雷， 使一定范围内的所有敌人受到伤害。\n
        G-14手雷有最大填装数和填装冷却时间， 按上、 下方向键后施放技能时， 可以调整投掷位置。 转职成为弹药专家时， 可以强制中断基本攻击动作， 投掷G-14手雷。
    """
    name = "G-14手雷"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 9
    rangeLv = 2
    cd = 4
    mp = [20, 160]
    uuid = "de3fea2d65c597f4d55c70a02b97fc79"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 最大填装数 : {value0}发
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 地面投掷时的冷却时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 空中投掷时的冷却时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 爆炸范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 机械概论
# gunner_male/mechanic_male/67e7dd8996b5735e788c9420730c077d
# afdf3b989339de478e85b614d274d1ef/67e7dd8996b5735e788c9420730c077d
class Skill24(PassiveSkill):
    """
        利用对机器人的深刻理解， 强化其性能， 增加基本攻击力和转职技能攻击力 ([G-1科罗纳]、 [G-2旋雷者]、 [G-3捕食者]除外)。
    """
    name = "机械概论"
    learnLv = 15
    masterLv = 1
    maxLv = 11
    position = 1
    rangeLv = 3
    uuid = "67e7dd8996b5735e788c9420730c077d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]

# 嗜战追击者
# gunner_male/mechanic_male/dc1ffbe7bfcc6dc2be737951960da9ad
# afdf3b989339de478e85b614d274d1ef/dc1ffbe7bfcc6dc2be737951960da9ad
class Skill25(PassiveSkill):
    """
        设置追击者时或被敌人攻击时， 有一定几率出现RX-78追击者对敌人进行攻击。\n
        出现的RX-78追击者与当前[RX-78追击者]召唤出的一致。\n
        出现的追击者与冷却时间无关。
    """
    name = "嗜战追击者"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 2
    rangeLv = 3
    cd = 7
    uuid = "dc1ffbe7bfcc6dc2be737951960da9ad"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 设置时追加出现几率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 被击时出现几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"data":data0,"skills":["RX-78追击者"]}]

# G-1科罗纳
# gunner_male/mechanic_male/1b1cfab062e0768bcc889e33e1f30dbf
# afdf3b989339de478e85b614d274d1ef/1b1cfab062e0768bcc889e33e1f30dbf
class Skill26(ActiveSkill):
    """
        在背后设置周期性发射光属性子弹的辅助机器人科罗纳。\n
        科罗纳会在场一段时间， 在设置科罗纳的状态下， 可以按相应技能键把科罗纳改装成[G-2旋雷者]或[G-3捕食者]。\n
        随科罗纳的技能等级提升， 增加[G-2旋雷者]和[G-3捕食者]的攻击力， 同时提升被击敌人的僵直时间比率。\n
        改装为其他G系列机器人后持续时间会延长， 但不会超过G系列基础持续时间。
    """
    name = "G-1科罗纳"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = [50, 50.6, 51.1, 51.7, 52.2, 52.8, 53.4, 53.9, 54.5, 55, 55.6, 56.1, 56.7, 57.3, 57.8, 58.4, 58.9, 59.5, 60.1, 60.6, 61.2, 61.7, 62.3, 62.9, 63.4, 64, 64.5, 65.1, 65.7, 66.2, 66.8, 67.3, 67.9, 68.4, 69, 69.6, 70.1, 70.7, 71.2, 71.8, 72.4, 72.9, 73.5, 74, 74.6, 75.2, 75.7, 76.3, 76.8, 77.4, 78, 78.5, 79.1, 79.6, 80.2, 80.7, 81.3, 81.9, 82.4, 83, 83.5, 84.1, 84.7, 85.2, 85.8, 86.3, 86.9, 87.5, 88, 88.6]
    mp = [39, 409]
    uuid = "1b1cfab062e0768bcc889e33e1f30dbf"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2/0.5
    # 发射冷却时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 敌人僵直时间比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # G系列基础持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 改装冷却时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 改装时延长持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [G-2旋雷者]攻击力增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [G-3捕食者]攻击力增加率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [范围信息]
    # 炸弹爆炸大小比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

    associate = [{"data":data7,"type":"+power0","skills":["改装 : G-2旋雷者","改装 : G-3捕食者"]}]

    def getSkillCD(self,mode=None):
        return 1.0


# 快速拔枪
# gunner_male/mechanic_male/45442bbbe33540b4deeec29437dae70c
# afdf3b989339de478e85b614d274d1ef/45442bbbe33540b4deeec29437dae70c
class Skill28(PassiveSkill):
    """
        快速拔枪攻击敌人， 发动后可以增加攻击速度和普通射击的攻击力。 转职为漫游枪手后增加精通等级。
    """
    name = "快速拔枪"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    uuid = "45442bbbe33540b4deeec29437dae70c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 拔枪速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 普通射击的攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# EX-S毒蛇炮
# gunner_male/mechanic_male/da6e37c1e3f0e8867f70007d89c239ff
# afdf3b989339de478e85b614d274d1ef/da6e37c1e3f0e8867f70007d89c239ff
class Skill29(ActiveSkill):
    """
        召唤出火力支援机器人EX-S毒蛇炮。\n
        召唤的机器人会在一段时间内持续向前方发射火属性子弹。
    """
    name = "EX-S毒蛇炮"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cd = 3.5
    mp = [39, 328]
    uuid = "da6e37c1e3f0e8867f70007d89c239ff"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 子弹攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 30
    # 每秒发射子弹数 : {value1}发
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 子弹穿刺几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 设置数量上限 : {value4}个
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 子弹大小比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 改装 : G-2旋雷者
# gunner_male/mechanic_male/c77a417c43de80c4ce32c1ed405d174a
# afdf3b989339de478e85b614d274d1ef/c77a417c43de80c4ce32c1ed405d174a
class Skill30(ActiveSkill):
    """
        将已设置的G系列机器人改装为3台旋雷者。\n
        每个旋雷者在充电状态下才能进行攻击， 每次旋转时， 用静电对附近敌人造成光属性伤害； 按技能键时， 向前方发射电波， 造成光属性伤害。\n
        旋雷者状态下， 可以按相应技能键把旋雷者改装成G-1科罗纳或G-3捕食者。\n
        旋雷者的攻击力， 随旋雷者的技能等级增加而增加。\n
        G-2旋雷者的持续时间和改装冷却时间与G-1科罗纳一致， 改装后持续时间会延长， 但不会超过G系列基础持续时间。
    """
    name = "改装 : G-2旋雷者"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    mp = [40, 336]
    uuid = "c77a417c43de80c4ce32c1ed405d174a"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 静电攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1/2
    # 静电多段攻击间隔 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 电波攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 充电冷却时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # G-1科罗纳攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # G-3捕食者攻击力增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 改装时延长持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 电波前方攻击范围比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    def getSkillCD(self,mode=None):
        return 1.0

    associate = [{"data":data4,"type":"+power0","skills":["G-1科罗纳","改装 : G-3捕食者"]}]

# 方舟反应堆
# gunner_male/mechanic_male/b1ccbd90d0b40f543ece3b18fcef827f
# afdf3b989339de478e85b614d274d1ef/b1ccbd90d0b40f543ece3b18fcef827f
class Skill31(PassiveSkill):
    """
        利用能量反应技术， 增加基本攻击力、 技能攻击力和魔法暴击率。
    """
    name = "方舟反应堆"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 5
    rangeLv = 2
    uuid = "b1ccbd90d0b40f543ece3b18fcef827f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法暴击率增加量 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"data":data0}]

# 伪装
# gunner_male/mechanic_male/4b2c90ec226fd40e967875aa5eabefb2
# afdf3b989339de478e85b614d274d1ef/4b2c90ec226fd40e967875aa5eabefb2
class Skill32(ActiveSkill):
    """
        学习后， 增加物理/魔法防御力。\n
        技能施放过程中， 以最尖端科技使自身和周围的所有队员进入伪装状态， 使敌人无法看见伪装状态的角色， 并增加回避率， 效果持续一定时间。\n
        持续时间内若作出移动以外的动作， 则会暂时解除伪装状态； 再次移动则又会进入伪装状态。
    """
    name = "伪装"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 3
    rangeLv = 3
    cd = 60
    mp = [100, 350]
    uuid = "4b2c90ec226fd40e967875aa5eabefb2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 物理防御力增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法防御力增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # - [施放技能时] -
    # 范围 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 回避率增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 改装 : G-3捕食者
# gunner_male/mechanic_male/ecc23c980ea71450c0ad0c3fd232f329
# afdf3b989339de478e85b614d274d1ef/ecc23c980ea71450c0ad0c3fd232f329
class Skill33(ActiveSkill):
    """
        将已设置的G系列机器人改装为6台捕食者。\n
        按技能键时， 捕食者会追击周围的敌人， 持续造成光属性伤害。\n
        每个敌人都会被2台捕食者缠住， 按住技能键一短时间后可以回收缠住敌人的捕食者。\n
        捕食者状态下， 可以按相应技能键改装成G-1科罗纳或G-2旋雷者。\n
        捕食者的攻击力， 随科罗纳和旋雷者的技能等级增加而增加。\n
        G-3 捕食者的持续时间和改装冷却时间与G-1科罗纳一致， 改装后持续时间会延长， 但不会超过G系列基础持续时间。\n
        在决斗场中， 捕食者可以被攻击， 生命值耗尽后， 一段时间内无法进行攻击。
    """
    name = "改装 : G-3捕食者"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    mp = [50, 420]
    uuid = "ecc23c980ea71450c0ad0c3fd232f329"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2/0.5
    # 攻击间隔时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 捕食者生命值 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 生命值耗尽后无法攻击时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 改装时延长持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [G-1科罗纳]攻击力增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [G-2旋雷者]攻击力增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 捕食者可移动范围 : {value7}px
    data7 = get_data(f'{prefix}/{uuid}', 7)

    associate = [{"data":data5,"type":"+power0","skills":["G-1科罗纳","改装 : G-2旋雷者"]}]

    def getSkillCD(self,mode=None):
        return 1.0

# 火焰电压
# gunner_male/mechanic_male/65827d506df24a870ef7d2e1aefbfeb7
# afdf3b989339de478e85b614d274d1ef/65827d506df24a870ef7d2e1aefbfeb7
class Skill34(PassiveSkill):
    """
    可以使[G-1科罗纳]、 [改装 : G-2旋雷者]、 [改装 : G-3捕食者]、 [光反应能量模块]、 [盖波加之拳]、 [EX-S零式毒蛇炮]转换为火属性。
    """
    name = "火焰电压"
    learnLv = 30
    masterLv = 1
    maxLv = 1
    position = 2
    rangeLv = 3
    uuid = "65827d506df24a870ef7d2e1aefbfeb7"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

# 机械指令
# gunner_male/mechanic_male/1c1a9606eb702ebe5a7bb4397f3aeae0
# afdf3b989339de478e85b614d274d1ef/1c1a9606eb702ebe5a7bb4397f3aeae0
class Skill35(ActiveSkill):
    """
        禁止设置的机器人进行攻击。\n
        除部分技能之外， 适用于所有主动机器人技能。\n
        仅限有持续时间的机器人技能， 当持续时间结束或生命值变为0时失效。 不适用于觉醒技和[改装 : G-2旋雷者]。\n
    - [不适用的机器人技能] -\n
    [改装 : G-2旋雷者]、 [光反应能量模块]、 [盖波加之拳]、 [超时空行军]
    """
    name = "机械指令"
    learnLv = 30
    masterLv = 1
    maxLv = 5
    position = 7
    rangeLv = 2
    cd = 1
    uuid = "1c1a9606eb702ebe5a7bb4397f3aeae0"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

# RX-60陷阱追击者
# gunner_male/mechanic_male/96e72ec364dada85600c907ecd95a140
# afdf3b989339de478e85b614d274d1ef/96e72ec364dada85600c907ecd95a140
class Skill36(ActiveSkill):
    """
        设置机器人RX-60陷阱追击者。\n
        在持续时间内， 设置的机器人会将一定范围内的敌人拉向自己。\n
        若蓄气后施放， 则在一定时间内不受[机械引爆]的影响。
    """
    name = "RX-60陷阱追击者"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 12
    mp = [88, 741]
    uuid = "96e72ec364dada85600c907ecd95a140"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 蓄气后施放时不受[机械引爆]影响的时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]]
    # 爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 陷阱范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 空战机械 : 风暴
# gunner_male/mechanic_male/d296043df164385a14cb973c8c7c4d07
# afdf3b989339de478e85b614d274d1ef/d296043df164385a14cb973c8c7c4d07
class Skill37(ActiveSkill):
    """
        召唤出空中战斗机器人风暴协助自身攻击敌人。\n
        召唤出的风暴可以在空中移动， 并使用机枪和导弹攻击空中或地面的敌人。 经过一定时间后， 召唤出新的风暴机器人后， 或者机械师死亡后， 风暴会爆炸并给予周围敌人一定伤害。\n
        可以通过On/Off功能设置是否使用[机械引爆]。
    """
    name = "空战机械 : 风暴"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [200, 1680]
    uuid = "d296043df164385a14cb973c8c7c4d07"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 机枪攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 0
    # 导弹攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 0
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 爆炸大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    mode = ["爆炸","秒伤"]

    def setMode(self, mode):
        if mode == "秒伤":
            self.hit0 = 1 / 60 * 17
            self.hit1 = 1 / 60 * 20
            self.hit2 = 0
            if self.vp == 2:
                self.skillRation *= 0
        elif mode == "爆炸":
            self.hit0 = 0
            self.hit1 = 0
            self.hit2 = 1
            if self.vp == 1:
                self.skillRation *= 0

    def getSkillCD(self, mode=None):
        if self.vp == 1:
            mode = "秒伤"
        elif self.vp == 2:
            mode = "爆炸"
        if mode == "秒伤":
            return 1.0
        return super().getSkillCD(mode)

    def vp_1(self):
        """
        [空战机械 : 风暴]\n
        风暴的持续时间变更为无限制\n
        风暴得到强化\n
         - 移动速度增加\n
         - 变更为移动中可发射导弹\n
         - 导弹发射寻敌范围 +100%\n
         - 机枪攻击范围 +30%
        """
        ...

    def vp_2(self):
        """
        [空战机械 : 风暴]\n
        风暴会受到[机械引爆]的影响\n
         - 施放[HS-1全息机械猎手]时， 可生成全息机器人\n
        设置数量上限增加及持续时间减少\n
         - 设置数量上限 : 20\n
         - 持续时间 : 8秒\n
        原冷却时间变更为15秒\n
        持续时间内， 风暴不再使用机枪攻击和导弹攻击\n
        总攻击力相同\n
         - 以持续时间8秒内的总攻击力为基准\n
        爆炸范围 +30%
        """
        self.cd = 15
        self.skillRation *= 14.66
        # self.power2 = 1
        ...

# 空投支援
# gunner_male/mechanic_male/2a3c96b88d02372505692da0a8b54743
# afdf3b989339de478e85b614d274d1ef/2a3c96b88d02372505692da0a8b54743
class Skill38(ActiveSkill):
    """
        召唤出轰炸机， 使其在一定范围内投下红色破坏者、 钢铁机器人、 修复者莱格、 神力雷克斯。\n
        在地下城中， 不会被敌人击中。
    """
    name = "空投支援"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 2
    cd = 30
    mp = [300, 2520]
    uuid = "2a3c96b88d02372505692da0a8b54743"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 机器人爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 20
    # 红色破坏者攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 空投范围 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 空投机器人数量 : {value3}个
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 爆炸范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [空投支援]\n
        轰炸机飞行过程中， 为机械师展开防御矩阵， 进入无敌状态\n
        必定投下红色破坏者和修复者莱格\n
         - 红色破坏者和修复者莱格的生命值/魔法值恢复量 5% 
        """
        ...

    def vp_2(self):
        """
        [空投支援]\n
        索菲亚按照机械师的命令， 召唤出轰炸机\n
         - 删除[空投支援]的施放动作\n
        同时投放所有机器人\n
        机器人投放间隔 -30%
        """
        ...

# 拦截机工厂
# gunner_male/mechanic_male/852f8ad797db4dca1405cb3e77198401
# afdf3b989339de478e85b614d274d1ef/852f8ad797db4dca1405cb3e77198401
class Skill39(ActiveSkill):
    """
        设置拦截机工厂， 生产出多架小型拦截机。\n
        经过一定时间后， 拦截机工厂爆炸， 剩下的拦截机飞向敌人后爆炸。\n
        拦截机被破坏后， 每隔一段时间工厂会继续生产出新的拦截机。\n
        使用[机械引爆]时， 拦截机飞向一定范围内等级最高的怪物并爆炸。
    """
    name = "拦截机工厂"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [355, 2981]
    uuid = "852f8ad797db4dca1405cb3e77198401"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 拦截机等级 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 拦截机爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 8
    # 拦截机召唤数量上限 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 锁定目标范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 光反应能量模块攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 0
    # [范围信息]
    # 拦截机爆炸范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 学习[光反应能量模块]后， 攻击范围比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    def vp_1(self):
        """
        [拦截机工厂]\n
        工厂生产出来的拦截机在角色周围徘徊\n
         - 拦截机存在15秒\n
         - 在地下城中切换房间时拦截机不会消失\n
         - [机械引爆]时， 每次引爆2架\n
        在拦截机存在期间， 每存在1架拦截机所受伤害 -5%
        """
        ...

    def vp_2(self):
        """
        [拦截机工厂]\n
        变更为由机械师直接发动的技能， 施放时召唤的拦截机编队向前方飞行， 对大范围进行轰炸\n
         - 轰炸多段攻击次数 : 8次\n
        自动适用[机械引爆]的伤害增加效果
        """
        ...

# 光反应能量模块
# gunner_male/mechanic_male/56aa7844a2da23f5bea9b585aea5ae45
# afdf3b989339de478e85b614d274d1ef/56aa7844a2da23f5bea9b585aea5ae45
class Skill40(PassiveSkill):
    """
        将拦截机互相连结， 生成能量散热板。\n
        能量散热板蓄积能量并向前方发射， 然后消失。
    """
    name = "光反应能量模块"
    learnLv = 45
    masterLv = 1
    maxLv = 1
    position = 4
    rangeLv = 1
    uuid = "56aa7844a2da23f5bea9b585aea5ae45"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    associate = [{"type":"+hit1","data":[0,-8],"ratio":1,"skills":["拦截机工厂"]},{"type":"+hit5","data":[0,1],"ratio":1,"skills":["拦截机工厂"]}]

# 斗志之歌
# gunner_male/mechanic_male/28b583c75a49103a1d8aabf799c000a4
# afdf3b989339de478e85b614d274d1ef/28b583c75a49103a1d8aabf799c000a4
class Skill41(PassiveSkill):
    """
        召唤出吟唱斗志之歌的斗志机器人， 增加基本攻击力和技能攻击力。\n
        斗志机器人不会受到伤害。
    """
    name = "斗志之歌"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    cd = 1
    uuid = "28b583c75a49103a1d8aabf799c000a4"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]

# 盖波加之拳
# gunner_male/mechanic_male/51a08fd0c90f0a5276cd552047fac93d
# afdf3b989339de478e85b614d274d1ef/51a08fd0c90f0a5276cd552047fac93d
class Skill42(ActiveSkill):
    """
        设置异界空间移动裂口， 并从中召唤出盖波加之拳给予周围敌人强威力攻击。
    """
    name = "盖波加之拳"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [881, 7403]
    uuid = "51a08fd0c90f0a5276cd552047fac93d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}% x {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    data1 = get_data(f'{prefix}/{uuid}', 1)

# EZ-10反击者
# gunner_male/mechanic_male/c5a2956d8ed3af1746ed2f76ca971a09
# afdf3b989339de478e85b614d274d1ef/c5a2956d8ed3af1746ed2f76ca971a09
class Skill43(ActiveSkill):
    """
        设置固定型爆破机器人EZ-10反击者， 使其经过一定时间后在原地爆炸并给予周围敌人火属性魔法伤害； 同时在原地生成EZ-8爆破者。\n
        设置机器人时， 按住技能键就可以蓄气， 蓄气时间越长机器人的存在时间就越长。\n
        对建筑型护甲的敌人可以造成125%伤害。
    """
    name = "EZ-10反击者"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 2
    cube = 2
    cd = 30
    mp = [122, 1027]
    uuid = "c5a2956d8ed3af1746ed2f76ca971a09"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # [反击者]爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [EZ-8爆破者]爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 3
    # 生成的[EZ-8爆破者]数量 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 延迟时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 延迟时间上限 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # [反击者]爆炸大小比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [EZ-8爆破者]爆炸大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [EZ-10反击者]\n
        反击者爆炸后不生成爆破者\n
         - 总攻击力相同\n
        反击者大小 +95%\n
         - 爆炸范围 +30%
        """
        ...

    def vp_2(self):
        """
        [EZ-10反击者]\n
        按技能键时， 可以指定位置设置爆破者， 并且机械师也移动到该位置\n
         - 可利用方向键指定位置\n
         - 总攻击力相同\n
        无法使用蓄气功能
        """
        ...

# EX-S零式毒蛇炮
# gunner_male/mechanic_male/e0a072e8cef2d77893aad5f68aeed56a
# afdf3b989339de478e85b614d274d1ef/e0a072e8cef2d77893aad5f68aeed56a
class Skill44(ActiveSkill):
    """
        召唤出火力支援机器人EX-S零式毒蛇炮， 向敌人发射子弹和激光。\n
        经过一段时间后， EX-S零式毒蛇炮会爆炸。
    """
    name = "EX-S零式毒蛇炮"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 8
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [218, 1830]
    uuid = "e0a072e8cef2d77893aad5f68aeed56a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 子弹攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 40
    # 激光攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 18
    # 每秒子弹发射数 : {value2}发
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 激光射击间隔 : 0.3秒
    # 持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 激光大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [EX-S零式毒蛇炮]\n
        不再发射子弹， 连射激光\n
         - 总攻击力相同\n
         - 激光多段攻击次数 : 15次\n
         - 激光大小 +45%
        """
        ...

    def vp_2(self):
        """
        [EX-S零式毒蛇炮]\n
        毒蛇炮向天空发射追踪最强敌人并坠落的炮弹\n
         - 总攻击力相同\n
         - 发射间隔 : 1秒\n
         - 发射次数上限 : 5次\n
         - 寻敌范围 : 2000px\n
        不存在敌人的情况下， 毒蛇炮会在持续时间结束后破坏， 最多持续15秒
        """
        ...

# HS-1机械助手
# gunner_male/mechanic_male/5cac3411ccef1af333953e0ded5e942d
# afdf3b989339de478e85b614d274d1ef/5cac3411ccef1af333953e0ded5e942d
class Skill45(PassiveSkill):
    """
        位于机械元首左右两侧的HS-1机械助手会代替机械元首设置机械装置。\n
        因HS-1机械助手拥有自我意识， 所以无法超负荷运作。\n
        当身边没有闲置的HS-1机械助手时， 机械元首只能亲自去设置机械装置。\n
    - HS-1机械助手能够设置的机械装置 -\n
    [RX-78追击者]、 [EZ-8爆破者]、 [EX-S毒蛇炮]、 [RX-60陷阱追击者]、 [空战机械 : 风暴]、 [拦截机工厂]、 [EZ-10反击者]、 [EX-S零式毒蛇炮]、 [TX-45特攻队]\n
        增加基本攻击力和机械技能的攻击力， 并增加爆炸范围。\n
        减少除[盖波加之拳]、 [超时空行军]、 [GW-16瓦尔德斯坦]之外技能的冷却时间。
    """
    name = "HS-1机械助手"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 1
    rangeLv = 3
    uuid = "5cac3411ccef1af333953e0ded5e942d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 施放速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 冷却时间减少比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 基本攻击力和技能攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 爆炸范围增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    associate = [{"type":"*cdReduce","data": data1,"exceptSkills":['盖波加之拳', '超时空行军', 'GW-16 瓦尔·德斯坦']}, {"data": data2}]

# TN-80终结者
# gunner_male/mechanic_male/002cbdd9bfd0f0b970451ae8d48d029e
# afdf3b989339de478e85b614d274d1ef/002cbdd9bfd0f0b970451ae8d48d029e
class Skill46(ActiveSkill):
    """
        召唤TN-80终结者轰击前方。\n
        施放技能时， 在指定位置召唤TN-80终结者。\n
        召唤出来的TN-80终结者向前方发射导弹， 然后向一定范围内级别最高的敌人突进后爆炸。\n
        不受[机械引爆]的影响。
    """
    name = "TN-80终结者"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "002cbdd9bfd0f0b970451ae8d48d029e"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 导弹攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 18
    # 导弹数量 : {value1}发
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 导弹发射范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 爆炸锁定范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 爆炸范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [TN-80终结者]\n
        减少召唤出终结者所需时间， 发射的导弹拥有诱导功能\n
         - 召唤时间 -30%\n
        向前方550px以内的敌人中等级最高的敌人发射9枚导弹\n
         - 总攻击力相同\n
        导弹发射速度 +20%\n
        突进速度 +50%
        """
        ...

    def vp_2(self):
        """
        [TN-80终结者]\n
        从次元中召唤出专门用于近身格斗的新型次元战士\n
        - 被召唤出的次元战士发现敌人时， 会以强袭模式快速接近后， 并进行霰弹枪射击\n
        - 总攻击力相同\n
        所有子弹耗尽或持续时间结束后， 向敌人突进并自爆\n
        - 霰弹枪射击次数 : 8发\n
        - 次元战士持续时间 : 15秒\n
        霰弹枪攻击时使敌人进入眩晕状态\n
        - 眩晕几率 : 100%\n
        - 持续时间 : 3秒\n
        次元战士在切换房间的情况下也会跟随机械师
        """
        ...

# TX-45特攻队
# gunner_male/mechanic_male/85f7c810ad503790e8626439fe936d56
# afdf3b989339de478e85b614d274d1ef/85f7c810ad503790e8626439fe936d56
class Skill47(ActiveSkill):
    """
        通过HS-1机械助手设置诱导型爆炸机械特攻队。\n
        设置的机械可以跟踪敌人并爆炸， 对周围敌人造成火属性魔法伤害。\n
        学习技能[HS-1机械助手]后才能使用。\n
        机械助手全部处于使用状态下， 无法使用该技能。
    """
    name = "TX-45特攻队"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [580, 4500]
    uuid = "85f7c810ad503790e8626439fe936d56"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # H1攻击力: {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # G1攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # D1攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # S1攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # T1攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # 机械持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 爆炸范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [TX-45特攻队]\n
        不会引爆H1机器人， 自动设置当前可设置的[RX-78追击者]和[EZ-8爆破者]\n
         - 总攻击力相同\n
         - 自动设置持续时间 : 15秒\n
        被机器人爆炸命中的敌人会进入强制控制状态3秒\n
         - 因爆炸进入的强制控制状态下， 即使再次发生爆炸， 也不会更新强制控制时间\n
        爆炸范围 +30%\n
        H1机器人在切换房间的情况下也会跟随机械师
        """
        ...

    def vp_2(self):
        """
        [TX-45特攻队]\n
        设置特工队时， 追踪地图上最强敌人， 瞬移至目标位置后立即爆炸\n
         - 追击范围 : 1000px\n
        爆炸后发送目标信息信号， 在一定时间内施放[机械引爆]时， 将自动瞄准该敌人\n
         - 持续时间15秒\n
        自动适用[机械引爆]的伤害增加效果
        """
        ...

# 超时空行军
# gunner_male/mechanic_male/31823197cc0b04d4c5dcf8f928d9220c
# afdf3b989339de478e85b614d274d1ef/31823197cc0b04d4c5dcf8f928d9220c
class Skill48(ActiveSkill):
    """
        从异次元空间中召唤机器人部队进行攻击。\n
        战斗机器人行进过程中会践踏碾压路径上的一切敌对目标。\n
        该技能不受[机械引爆]的影响。
    """
    name = "超时空行军"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 8000]
    uuid = "31823197cc0b04d4c5dcf8f928d9220c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 9
    # 爆炸攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 行进步数  : {value2}步
    data2 = get_data(f'{prefix}/{uuid}', 2)

# HS-1全息机械猎手
# gunner_male/mechanic_male/89a4529234904fcbb3abe289e281f2fd
# afdf3b989339de478e85b614d274d1ef/89a4529234904fcbb3abe289e281f2fd
class Skill49(ActiveSkill):
    """
        只有已学习[HS-1机械助手]、  [索菲亚]的状态下才能使用该技能。\n
        HS-1机械助手转换为全息机器人生成模式。 模式结束时全息机器人转换为实体并爆炸， 全息粒子会追加产生爆炸。\n
        再次使用技能时可以强制结束模式， 长按技能键时出现光标， 可以指定位置后发生爆炸。\n
        设置除[空战机械 : 风暴]外可以[机械引爆]的机器人时， 消耗能量生成全息机器人。\n
        全息机器人产生与追加相同爆炸范围的爆炸， 爆炸伤害适用[机械引爆]爆炸伤害变化率。\n
        根据能量消耗量增加追加爆炸伤害， 若未消耗能量就结束模式， 则不会发动追加爆炸。
    """
    name = "HS-1全息机械猎手"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [773, 6000]
    uuid = "89a4529234904fcbb3abe289e281f2fd"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 追加爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 消耗所有能量时追加爆炸攻击力上限 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 模式持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 可用能量上限 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 设置机器人时消耗能量 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 索菲亚
# gunner_male/mechanic_male/87a918bb22cfc959a16e0bf939bb6c24
# afdf3b989339de478e85b614d274d1ef/87a918bb22cfc959a16e0bf939bb6c24
class Skill50(PassiveSkill):
    """
        将高度发达的人工智能“索菲亚”搭载在HS-1机械助手上， 根据机械元首的指示， 对其他机器人进行精细控制。\n
        增加基本攻击和转职技能攻击力， 部分技能赋予额外效果。\n
        未学习[HS-1机械助手]的状态下， 不适用部分技能的额外效果\n
    [EX-S毒蛇炮] : 将所有已放置的毒蛇炮的位置同步到最后放置的毒蛇炮的位置。\n
    [机械引爆] : 瞄准引爆时， 所有机器人立即瞬移到指定位置并爆炸。 各技能分别发生爆炸， 合并技能伤害造成1次打击。
    """
    name = "索菲亚"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "87a918bb22cfc959a16e0bf939bb6c24"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]

# GW-16瓦尔德斯坦
# gunner_male/mechanic_male/515b442ffbf61a82371abb645c149a31
# afdf3b989339de478e85b614d274d1ef/515b442ffbf61a82371abb645c149a31
class Skill51(ActiveSkill):
    """
        只有已学习[HS-1机械助手]、  [索菲亚]的状态下才能使用该技能。\n
        召唤巨型机器人GW-16瓦尔德斯坦， 与HS-1机械助手与一起搭乘。 向进入机器人中枢系统的机械助手下达命令操纵机器人， 发动瓦尔德斯坦才有的致命攻击。\n
        若正在施放[HS-1全息机械猎手]， 则强制结束全息机器人生成模式。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "GW-16瓦尔德斯坦"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 12889]
    uuid = "515b442ffbf61a82371abb645c149a31"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 落地冲击波攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 能量场释放攻击力 : {value1}% x {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 7
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 终结拳头捶击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 终结爆炸攻击力 : {value4}% x {value5}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 14
    data5 = get_data(f'{prefix}/{uuid}', 5)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'mechanic_male'
        self.nameCN = '重霄·机械师'
        self.role = 'gunner_male'
        self.角色 = '神枪手(男)'
        self.职业 = '机械师'
        self.jobId = 'afdf3b989339de478e85b614d274d1ef'
        self.jobGrowId = '6d459bc74ba73ee4fe5cdc4655400193'

        self.武器选项 = ['手弩', '步枪','左轮枪','自动手枪','手炮']
        self.输出类型选项 = ['魔法百分比']
        self.输出类型 = '魔法百分比'
        self.防具精通属性 = ['智力']
        self.防具类型 = '布甲'
        self.buff = 1.922

        super().__init__(equVersion, __name__)
