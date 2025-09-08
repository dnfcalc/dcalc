#944b9aab492c15a8474f96947ceeb9e4
from core.basic.skill import PassiveBufferSkill,ActiveBufferSkill,ActiveSkill,PassiveSkill, get_data
from core.basic.character import Character
prefix = "gunner_female/paramedic/cn/skillDetail"

# 系统常量 · 战斗服
# gunner_female/paramedic/dce00e1ce90e34ef5c36ea869ad171bd
# 944b9aab492c15a8474f96947ceeb9e4/dce00e1ce90e34ef5c36ea869ad171bd
class Skill5(PassiveSkill):
    """
    协战师进入战场时穿戴的战斗服。 平时会内置于医神设备中， 该服装设计注重行动便利性， 具备处理战场信息和最小化所受伤害的功能。\n
        协战师动作均切换至战斗服[近战]模式， 适用物理独立攻击力。
    """
    name = "系统常量 · 战斗服"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 1 #TODO
    rangeLv = 3
    uuid = "dce00e1ce90e34ef5c36ea869ad171bd"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 防御力增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)



# 近战 · 锁定连射
# gunner_female/paramedic/452be74df1c43b4d3080e1b09ed32e08
# 944b9aab492c15a8474f96947ceeb9e4/452be74df1c43b4d3080e1b09ed32e08
class Skill7(ActiveSkill):
    """
    向前方最近的敌人射击2次。
    """
    name = "近战 · 锁定连射"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 9 #TODO
    rangeLv = 2
    cd = 6
    mp = [35, 188]
    uuid = "452be74df1c43b4d3080e1b09ed32e08"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 射击攻击力 : {value0} X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2  # 射击次数
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 每次攻击的信息获取率 : 15%
    # [范围信息]
    # 探索范围 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)


# 系统常量 · 同步
# gunner_female/paramedic/f48b0983de6b83180f7d82f0a5882496
# 944b9aab492c15a8474f96947ceeb9e4/f48b0983de6b83180f7d82f0a5882496
class Skill13(PassiveSkill):
    """
    协战师为小队提供的强袭支援模件。\n
        可提升基本攻击力、 技能攻击力， 并将所有强化效果同步至每个队员。\n
    [同步]\n
        无论队员处于哪个位置， 涵盖个别地图， 都能获得增益效果。 当队员从无法战斗状态中恢复时， 将重新获得已赋予其他存活队员的强化效果， 保护模件除外。\n
    [同步对象]\n
    [保护模件 (缓冲)]\n
    [保护模件 (净化)]\n
    [装甲强化]\n
    [军械强化]\n
    [机动强化]\n
    [军械强化(进阶)]\n
    [强袭策略 : 区域肃清]\n
    [保护模件 (黄金复苏)]\n
    [空袭策略 : 神兵天降]
    """
    name = "系统常量 · 同步"
    learnLv = 15
    masterLv = 1
    maxLv = 11
    position = 0 #TODO
    rangeLv = 3
    uuid = "f48b0983de6b83180f7d82f0a5882496"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]  # 协战师技能关联

# 系统 · 战场信息
# gunner_female/paramedic/6235960237fdb1b77f2c82b33614dcf4
# 944b9aab492c15a8474f96947ceeb9e4/6235960237fdb1b77f2c82b33614dcf4
class Skill14(PassiveBufferSkill):
    """
    进入地下城时， 将配备无人机用于分析交战信息并提供支援， 该无人机可从医神设备中分离， 协助协战师执行任务。\n
        分析的信息在提供部分模件时会被消耗， 可通过使用转职技能或基本攻击与敌人交战来收集补充。\n
        为协战师提供精神辅助增益， 并在其命中敌人时减弱敌人的属性伤害抗性。\n
        效果可持续存在一段时间， 最多可叠加至特定次数。\n
        该技能效果不与光明骑士 (男) 的[惩罚之锤]、 光明骑士 (女) 的[圣光灌注]、 小魔女的[冥月绽放]、 缪斯的[多彩感性]技能效果叠加。\n
        执行独立作战时， 不适用属性伤害增加效果， 仅适用独立作战专属效果。 消耗信息层数时， 对范围内敌人进行激光轰炸， 造成多段伤害。 该激光轰炸受[基础精通]的影响， 在使用[军械强化 (进阶)]技能时， 会追加轰炸。
    """
    name = "系统 · 战场信息"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 3
    uuid = "6235960237fdb1b77f2c82b33614dcf4"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 能量最高累计 : {value0}层
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 精神增加量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 属性伤害量增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 属性伤害量增加持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 属性伤害量叠加上限 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [独立作战专属]
    # 独立攻击力增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 技能冷却时间减少 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 激光攻击力 : {value7} X {value8}
    data7 = get_data(f'{prefix}/{uuid}', 7)
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 使用[军械强化 (进阶)]时的追加轰炸次数 : {value9}次
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [激光炮击目标技能]
    # [保护模件 (缓冲)]
    # [保护模件 (净化)]
    # [机动强化]
    # [军械强化 (进阶)]
    # [保护模件 (黄金复苏)]
    Spirit = data1
    associate = [{"data":data1,"type":"$+Spirit","ratio":1}]
    CarryRatio = [0]+ [(1.055 ** 3) * 100 - 100]*maxLv# noqa: E501

# 战服 · 强袭目标
# gunner_female/paramedic/0db0405a229a667e0ae97108fc5111c4
# 944b9aab492c15a8474f96947ceeb9e4/0db0405a229a667e0ae97108fc5111c4
class Skill15(ActiveBufferSkill):
    """
    持枪向前方滑行， 进行威慑射击。\n
        施放后立即为队员提供强化后的[保护模件 (缓冲)]效果。\n
    [保护模件 (缓冲) 强化效果]\n
        降低所受伤害、 进入霸体状态
    """
    name = "战服 · 强袭目标"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cd = 6
    mp = [56, 303]
    uuid = "0db0405a229a667e0ae97108fc5111c4"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    buffer = True

    # 射击攻击力 : {value0} X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 强化保护罩充能量 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 强化保护罩的伤害减少率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 强化保护罩持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 前方射击范围 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 机动强化
# gunner_female/paramedic/4e431eaadc1c4563fe33d03c072564f0
# 944b9aab492c15a8474f96947ceeb9e4/4e431eaadc1c4563fe33d03c072564f0
class Skill16(ActiveBufferSkill):
    """
    协战师为小队提供的强化模件。 基于战场信息， 强化中枢神经机能， 全方位提升速度。\n
        提升攻击速度、 移动速度和技能施放速度， 效果持续一定时间。\n
        需要先完成该模件的战场信息分析， 之后可利用医神设备在其他动作中施放。
    """
    name = "机动强化"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 1 #TODO
    rangeLv = 3
    cd = 0.1
    mp = [25, 56]
    uuid = "4e431eaadc1c4563fe33d03c072564f0"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    buffer = True
    buffType = "buff"

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 移动速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 施放速度增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)


# 保护模件 (净化)
# gunner_female/paramedic/6b557a0a96ccd83b37ddb77c550f6a68
# 944b9aab492c15a8474f96947ceeb9e4/6b557a0a96ccd83b37ddb77c550f6a68
class Skill18(ActiveBufferSkill):
    """
    协战师为小队提供的净化模件。 基于已分析的战场信息， 解除异常状态。\n
        需要先完成该模件的战场信息分析， 之后可利用医神设备在其他动作中施放。
    """
    name = "保护模件 (净化)"
    learnLv = 20
    masterLv = 1
    maxLv = 11
    position = 1 #TODO
    rangeLv = 3
    cd = 0.1
    mp = [17, 27]
    uuid = "6b557a0a96ccd83b37ddb77c550f6a68"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    buffer = True

    # 可解除异常状态数量上限 : {value0}个
    data0 = get_data(f'{prefix}/{uuid}', 0)

# 战服 · 机动打击
# gunner_female/paramedic/9e86a1210874dc2b0c83a4a5a54a7222
# 944b9aab492c15a8474f96947ceeb9e4/9e86a1210874dc2b0c83a4a5a54a7222
class Skill19(ActiveBufferSkill):
    """
    快速突进至前方， 施展上踢攻击。 成功命中敌人后追加攻击。
    """
    name = "战服 · 机动打击"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 8
    mp = [50, 267]
    uuid = "9e86a1210874dc2b0c83a4a5a54a7222"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 上踢攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 追加攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 近战 · 闪退射击
# gunner_female/paramedic/d2cc06a46cf7b6020ccc50c30f86ab25
# 944b9aab492c15a8474f96947ceeb9e4/d2cc06a46cf7b6020ccc50c30f86ab25
class Skill20(ActiveSkill):
    """
    挥舞战斗服上装备的刀刃， 再短距离地后撤， 进行2次牵制射击。
    """
    name = "近战 · 闪退射击"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 8 #TODO
    rangeLv = 2
    cd = 8
    mp = [76, 409]
    uuid = "d2cc06a46cf7b6020ccc50c30f86ab25"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 刀刃攻击力 : {value0} X 2
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 射击攻击力 : {value1} X 2
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 每次攻击的信息获取率 : 10%
    # [范围信息]
    # 攻击范围 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 学习[系统 · 临战编程]后
    # 强化保护罩充能量 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 强化保护罩的伤害减少率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 强化保护罩持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 装甲强化
# gunner_female/paramedic/7ccc03c65d676c4d8a7e6a1821409ad0
# 944b9aab492c15a8474f96947ceeb9e4/7ccc03c65d676c4d8a7e6a1821409ad0
class Skill21(ActiveBufferSkill):
    """
    协战师为小队提供的强化模件。 基于战场信息， 强化防御能力。\n
        提升队员的生命值最大值、 魔法值最大值、 物理防御力、 魔法防御力、 体力、 精神。\n
        可利用医神设备在其他动作中施放。\n
        该技能效果不与光明骑士 (男) 的[天籁之音]和[守护徽章]、 光明骑士 (女) 的[守护祝福]、 小魔女的[小魔女的偏爱]、 缪斯的[主角登场]技能效果叠加。
    """
    name = "装甲强化"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 0
    rangeLv = 3
    cd = 10
    mp = [428, 944]
    uuid = "7ccc03c65d676c4d8a7e6a1821409ad0"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    buffer = True

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 生命值最大值增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 魔法值最大值增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 物理防御力增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 魔法防御力增加 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 体力增加 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 精神增加 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)

    Spirit = data6
    associate = [{"data": data6,"type": "$+Spirit","ratio":1}]  # type: ignore

# 军械强化
# gunner_female/paramedic/e73e980e87591bc98940afb1ac0fe522
# 944b9aab492c15a8474f96947ceeb9e4/e73e980e87591bc98940afb1ac0fe522
class Skill22(ActiveBufferSkill):
    """
    协战师为小队提供的强化模件。 基于战场信息， 强化攻击能力。\n
        提升协战师自身的基本攻击力和技能攻击力， 同时强化其他队员的力量、 智力、 命中率、 以及物理/魔法/独立攻击力。\n
        达到20级以上后， 不再增加自身基本攻击力和技能攻击力， 且物理/魔法/独立攻击力、 力量、 智力增加效果不适用于自身。\n
        施放者的精神越高， 力量、 智力、 物理/魔法/独立攻击力的增加量越多。\n
        可利用医神设备在其他动作中施放。\n
        该技能效果不与光明骑士 (男) 的[荣誉祝福]、 光明骑士 (女) 的[勇气祝福]、 小魔女的[禁术吟咏]、 缪斯的[可爱节拍]技能效果叠加。
    """
    name = "军械强化"
    learnLv = 30
    masterLv = 10
    maxLv = 40
    position = 0 #TODO
    rangeLv = 3
    cd = 10
    mp = [529, 1166]
    uuid = "e73e980e87591bc98940afb1ac0fe522"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    buffer = True
    buffType = "buff"

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 命中率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [协战师专属效果]
    # 基本攻击力和技能攻击力增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [队员专属效果]
    # 力量增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 智力增加 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 物理攻击力增加 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 魔法攻击力增加 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 独立攻击力增加 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)

    ATK = data5
    STRINT = data3

# 近战 · 指定射击
# gunner_female/paramedic/50359daccd728ba338d18d9b71ac97e5
# 944b9aab492c15a8474f96947ceeb9e4/50359daccd728ba338d18d9b71ac97e5
class Skill23(ActiveSkill):
    """
    获取交战区域敌人的位置信息后， 进行6次射击。\n
        优先按怪物等级排序， 其次根据距离远近锁定更近的目标。\n
        若射击目标死亡， 则自动锁定其他存活的敌人； 若范围内没有敌人或敌人处于无敌状态， 则射击结束。
    """
    name = "近战 · 指定射击"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 9 #TODO
    rangeLv = 2
    cd = 13
    mp = [136, 732]
    uuid = "50359daccd728ba338d18d9b71ac97e5"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 射击攻击力 : {value0} X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 每次攻击的信息获取率 : 15%
    # [范围信息]
    # 探索范围 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 保护模件 (缓冲)
# gunner_female/paramedic/fc30c667a58e1dd54b5d214e04f4f23c
# 944b9aab492c15a8474f96947ceeb9e4/fc30c667a58e1dd54b5d214e04f4f23c
class Skill24(ActiveBufferSkill):
    """
    协战师为小队提供的保护模件。 基于已分析的战场信息， 生成可代受伤害的保护罩。 保护罩可累积， 当所受伤害量超过累积的保护罩能量上限时， 超出部分的伤害量将直接扣除生命值。\n
        需要先完成该模件的战场信息分析， 之后可利用医神设备在其他动作中施放。
    """
    name = "保护模件 (缓冲)"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 1 #TODO
    rangeLv = 3
    cd = 0.1
    mp = [36, 195]
    uuid = "fc30c667a58e1dd54b5d214e04f4f23c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    buffer = True

    # 保护罩持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 保护罩充能量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 保护罩能量上限 : 目标最大生命值的{value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 近战 · 爆刃突袭
# gunner_female/paramedic/1c1cf47273c67ff26eb60b375ace2062
# 944b9aab492c15a8474f96947ceeb9e4/1c1cf47273c67ff26eb60b375ace2062
class Skill25(ActiveSkill):
    """
    挥舞战斗服上装备的刀刃， 将敌人拉至身前。 发起连续攻击后， 沿直线方向返回原位。
    """
    name = "近战 · 爆刃突袭"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 8 #TODO
    rangeLv = 2
    cube = 1
    cd = 18
    mp = [226, 1218]
    uuid = "1c1cf47273c67ff26eb60b375ace2062"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 刀刃攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 后方刀刃穿刺攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 射击攻击力 : {value2} X 2
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 扫腿攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 终结踢击攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 爆炸攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 第一击攻击范围 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [近战 · 爆刃突袭]\n
        删除部分攻击， 合算至最后一击\n
        未命中时， 剩余冷却时间缩短为2秒\n
        总攻击力相同\n
        [保护模块 (黄金复苏)]\n
        协战师死亡后可以施放技能\n
        协战师可以为自己施放复活技能\n
        单人挑战时可复活次数 : 1次
        """
        ...

    def vp_2(self):
        """
        [近战 · 爆刃突袭]\n
        删除部分攻击， 合算至最后一击\n
        追踪前方500px范围内的敌人\n
        总攻击力相同\n
        [保护模块 (黄金复苏)]\n
        协战师死亡后可以施放技能\n
        协战师可以为自己施放复活技能\n
        单人挑战时可复活次数 : 1次
        """
        ...

# 军械强化 (进阶)
# gunner_female/paramedic/1c9cf3b27d9d6ee5e024e2592cad24a5
# 944b9aab492c15a8474f96947ceeb9e4/1c9cf3b27d9d6ee5e024e2592cad24a5
class Skill26(ActiveBufferSkill):
    """
    协战师为小队提供的强化模件。 基于已收集的信息， 重新定义[军械强化]效果， 提供更加优化的增益。
    """
    name = "军械强化 (进阶)"
    learnLv = 40
    masterLv = 1
    maxLv = 1
    position = 1 #TODO
    rangeLv = 3
    cd = 0.1
    mp = [40, 40]
    uuid = "1c9cf3b27d9d6ee5e024e2592cad24a5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    buffer = True
    buffType = "buffSub"

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [军械强化]增幅率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def skillInfo(self):
        prep = self.char.BuffSkill.skillInfo()
        ratio = self.data1[self.lv] / 100
        return prep[0] * ratio, [prep[1][0]*ratio,prep[1][1],prep[1][2]*ratio], [prep[2][0]*ratio,prep[2][1],prep[2][2]*ratio],0,self.getSkillCD()

# 战服 · 护盾冲击
# gunner_female/paramedic/1fd827a816f1d00450bcb2cf298a157a
# 944b9aab492c15a8474f96947ceeb9e4/1fd827a816f1d00450bcb2cf298a157a
class Skill27(ActiveBufferSkill):
    """
    开启战斗服的内置护盾， 向前冲撞。 护盾撞击到的敌人会受到伤害并被击退。\n
        施放后立即为队员提供强化后的[保护模件 (缓冲)]效果。\n
    [保护模件 (缓冲) 强化效果]\n
        降低所受伤害、 进入霸体状态
    """
    name = "战服 · 护盾冲击"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [356, 1917]
    uuid = "1fd827a816f1d00450bcb2cf298a157a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501
    buffer = True

    # 冲撞攻击力 : {value0} X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 强化保护罩充能量 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 强化保护罩的伤害减少率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 强化保护罩持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 护盾大小 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [战服 · 护盾冲击]\n
        删除突进动作， 向前方发射护盾\n
        护盾大小 +30%\n
        [保护模件 (缓冲)]\n
        保护罩恢复量 +10%\n
        保护罩充能量上限额外 +10%
        """
        ...

    def vp_2(self):
        """
        [战服 · 护盾冲击]\n
        向前方跳跃并展开护盾下劈\n
        - 护盾在地面设置电流线， 使敌人进入减速和感电状态\n
        - 减速 : 攻击速度和移动速度 -30%\n
        - 电流线持续时间 : 5秒\n
        总攻击力相同\n
        [保护模件 (缓冲)]\n
        保护罩恢复量 +10%\n
        保护罩充能量上限额外 +10%
        """
        ...

# 战服 · 开拓射线
# gunner_female/paramedic/68c20fbed9e68d3cb677072c9274736f
# 944b9aab492c15a8474f96947ceeb9e4/68c20fbed9e68d3cb677072c9274736f
class Skill28(ActiveSkill):
    """
    开启战斗服的内置手炮， 向前方发射激光。\n
        激光对敌人造成多段伤害， 且激光所掠过的地面会即刻引爆， 造成额外伤害。
    """
    name = "战服 · 开拓射线"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [502, 2701]
    uuid = "68c20fbed9e68d3cb677072c9274736f"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 레이저 공격력 : {value1} X {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 지면 폭발 공격력 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 타격 당 정보 습득률 : 10%
    # [범위 정보]
    # 레이저 굵기 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [战服 · 开拓射线]\n
        施放速度增加\n
        沿着激光路径将左右范围的敌人聚集成一列\n
        激光宽度 +15%\n
        [强袭策略 : 区域肃清]\n
        满足条件时， 冷却时间减少1秒 (最多25秒)\n
        1. [保护模件 (缓冲)]\n
        - 对队友施加效果时\n
        2. [军械强化 (进阶)]\n
        - 对队友施加效果时\n
        3. [系统 · 战场信息]\n
        - 适用属性伤害增加效果时 (冷却时间5秒)\n
        4. [系统 · 作战应对]\n
        - 增益效果持续时间更新时
        """
        ...

    def vp_2(self):
        """
        [战服 · 开拓射线]\n
        激光划过的地面引发巨大爆炸， 造成多段攻击伤害\n
        冷却时间 +50%\n
        - 追加爆炸多段攻击次数 : 4次\n
        总攻击力 +50%\n
        [强袭策略 : 区域肃清]\n
        满足条件时， 冷却时间减少1秒 (最多25秒)\n
        1. [保护模件 (缓冲)]\n
        - 对队友施加效果时\n
        2. [军械强化 (进阶)]\n
        - 对队友施加效果时\n
        3. [系统 · 战场信息]\n
        - 适用属性伤害增加效果时 (冷却时间5秒)\n
        4. [系统 · 作战应对]\n
        - 增益效果持续时间更新时
        """
        ...

# 系统 · 作战应对
# gunner_female/paramedic/a8574a8efa365e8e46e805a6e1d7bfef
# 944b9aab492c15a8474f96947ceeb9e4/a8574a8efa365e8e46e805a6e1d7bfef
class Skill29(PassiveBufferSkill):
    """
    교전 지역에 대한 분대원의 방어체계 모듈을 추가한다.\n
    스키퍼의 기본/스킬 공격력이 증가하고, 자신을 포함한 분대원들의 힘, 지능, 체력, 정신력, 공격 속도, 이동 속도가 증가한다.\n
    스키퍼의 정신력 스탯은 힘 스탯보다 높은 경우, 정신력 스탯만큼 힘 스탯을 보정해주는 기능이 추가된다. (스탯 % 증가 효과는 제외하고 보정된다.)\n
    또한 정보 스택을 소모하는 분대 강화 스킬 시전 시 현재 적용중인 squad::무기강화();squad::장갑강화();의 지속시간이 증가한다.
    """
    name = "系统 · 作战应对"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 3
    uuid = "a8574a8efa365e8e46e805a6e1d7bfef"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 力量、 智力增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 体力、 精神增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击速度、 移动速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 消耗信息时[军械强化]、 [装甲强化]持续时间延长 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [协战师专属效果]
    # 基本攻击力和技能攻击力增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    STRINT = data0
    Spirit = data1
    associate = [{"data": data1,"type": "$+Spirit","ratio":1}]  # type: ignore

# 强袭策略 : 区域肃清
# gunner_female/paramedic/ca0cc360e00e5f13e33027bf5fc53d5d
# 944b9aab492c15a8474f96947ceeb9e4/ca0cc360e00e5f13e33027bf5fc53d5d
class Skill30(ActiveBufferSkill):
    """
    开启部署在强袭区域上空的医神设备， 执行清除区域内敌人的任务。 医神设备从空中对目标区域进行火力支援， 同时协战师将该区域信息同步共享给队员。 将在一定时间内， 提升队员的力量、 智力、 攻击速度和移动速度， 对范围内敌人造成多段伤害。 但施放者自身不受此力量、 智力提升效果影响。\n
        该技能效果不与光明骑士 (男) 的[天启之光]、 光明骑士 (女) 的[圣光天启]、 小魔女的[开幕！人偶剧场]、 缪斯的[梦想的舞台]技能效果叠加。
    """
    name = "强袭策略 : 区域肃清"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 5
    cube = 5
    cd = 170
    mp = [1727, 7104]
    uuid = "ca0cc360e00e5f13e33027bf5fc53d5d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    buffType = 'awake'

    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 力量增加量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 智力增加量 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 攻击速度增加量 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 移动速度增加量 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 激光炮击攻击力 : {value5} X {value6}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 力场爆炸攻击力 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)

    STRINT = data1

# 保护模件 (黄金复苏)
# gunner_female/paramedic/da29a96a20a75aa0cd8fd7f526bdb107
# 944b9aab492c15a8474f96947ceeb9e4/da29a96a20a75aa0cd8fd7f526bdb107
class Skill31(ActiveSkill):
    """
    协战师为小队提供的保护模件， 可使心跳骤停的队员恢复生命体征。\n
        协战师的队员们心跳骤停时， 存在黄金时间。\n
        在黄金时间内， 仍维持现有增益效果。 通过该技能对停止跳动的心脏进行冲击， 可恢复部分生命值和魔法值， 使队员迅速重返战斗。\n
    为没有进入心跳骤停状态的队员， 赋予实时更新生命体征的保护模件。 该模件持续时间内， 队员进入心跳骤停状态时， 医神无人机会从空中降下， 立即对停止跳动的心脏进行冲击， 可恢复部分生命值和魔法值， 使队员迅速重返战斗。\n
        黄金时间内， 可用复活币进行复活。
    """
    name = "保护模件 (黄金复苏)"
    learnLv = 60
    masterLv = 1
    maxLv = 11
    position = 1 #TODO
    rangeLv = 3
    cube = 2
    cd = 2
    mp = [17, 27]
    uuid = "da29a96a20a75aa0cd8fd7f526bdb107"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 골든 타임 : 9초
    # 생체 정보 갱신 지속시간 : {value1}초
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 제세동 대상 HP/MP 회복량 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 系统 · 区域防御
# gunner_female/paramedic/8403ffaa9106bbfc1fd2e078e54d2e81
# 944b9aab492c15a8474f96947ceeb9e4/8403ffaa9106bbfc1fd2e078e54d2e81
class Skill32(ActiveSkill):
    """
    无人机启动强大的力场， 对敌人造成伤害。 力场存续期间， 协战师免疫所有伤害。 力场被无人机回收时， 将再次对敌人造成伤害。
    """
    name = "系统 · 区域防御"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 2 #TODO
    rangeLv = 2
    cube = 2
    cd = 30
    mp = [347, 1428]
    uuid = "8403ffaa9106bbfc1fd2e078e54d2e81"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 力场启动攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 力场回收攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 无敌状态持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 无敌状态持续时间同步率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [系统 · 区域防御]\n
        施放时， 恢复15%的魔法值\n
        力场持续时间 +0.3秒\n
        队员的同步率 +50%\n
        初始化[近战 · 爆刃突袭]的冷却时间\n
        - [近战 · 爆刃突袭]攻击力 -33%
        """
        ...

    def vp_2(self):
        """
        [系统 · 区域防御]\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 15秒\n
        - 攻击力 -50%\n
        力场持续时间 -0.2秒\n
        队员的同步率 +50%
        """
        ...

# 战服 · 歼灭行动
# gunner_female/paramedic/26a9454eb0d175ebeac162d68814238b
# 944b9aab492c15a8474f96947ceeb9e4/26a9454eb0d175ebeac162d68814238b
class Skill33(ActiveSkill):
    """
    立即从战斗服召唤6架小无人机， 向前方发射直线激光。 随后协战师空翻撤至后方， 回收无人机并挥舞， 造成二次伤害。
    """
    name = "战服 · 歼灭行动"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 8 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [416, 1710]
    uuid = "26a9454eb0d175ebeac162d68814238b"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 直线激光攻击力 : {value0} X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 激光挥舞攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [战服 · 歼灭行动]\n
        可以在其他动作中施放\n
        命中时, 使目标进入减速状态\n
        - 减速效果 : 攻击速度和移动速度 -50%\n
        - 减速持续时间 : 7秒\n
        [机动强化]\n
        增益效果持续时间 +5秒\n
        所有速度 +10%
        """
        ...

    def vp_2(self):
        """
        [战服 · 歼灭行动]\n
        立即施放最后一击\n
        - 总攻击力相同\n
        命中时， 使目标进入强制控制状态3秒\n
        [机动强化]\n
        增益效果持续时间 +5秒\n
        所有速度 +10%
        """
        ...

# 系统 · 限制解除
# gunner_female/paramedic/a354f4930334e70b0275f5d92668ce3d
# 944b9aab492c15a8474f96947ceeb9e4/a354f4930334e70b0275f5d92668ce3d
class Skill34(PassiveBufferSkill):
    """
    历经无数实战考验， 完成极限训练的战勤统帅， 方可解禁战勤系统限制代码。\n
        提升战勤统帅的精神、 基本攻击力和技能攻击力、 物理暴击率， 并增加[保护模件 (缓冲)]的单次生成数量和最大累积上限。
    """
    name = "系统 · 限制解除"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 3
    uuid = "a354f4930334e70b0275f5d92668ce3d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 精神增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 物理暴击率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 学习[保护模件 (缓冲)]后
    # 保护罩额外生成 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 保护罩最大累积量上限 : 目标生命值上限的{value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 强化保护罩额外生成 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 强化保护罩额外降低伤害 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    Spirit = data0
    associate = [{"data": data0,"type": "$+Spirit","ratio":1}]  # type: ignore

# 战服 · 超限压制
# gunner_female/paramedic/9559c99a9596b20d031de1ce2649b326
# 944b9aab492c15a8474f96947ceeb9e4/9559c99a9596b20d031de1ce2649b326
class Skill35(ActiveSkill):
    """
    启动战斗服的超负荷极限输出程序， 突进追踪前方射程范围内的所有敌人， 造成高额伤害， 随后回归原位。
    """
    name = "战服 · 超限压制"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [982, 4038]
    uuid = "9559c99a9596b20d031de1ce2649b326"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 压制攻击力 : {value0} X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [战服 · 超限压制]\n
        直接向前方突进\n
        - 施放时进入无敌状态\n
        [保护模件 (净化)]\n
        施放时， 队员和自身恢复生命值最大值10%的生命值\n
        免疫一次解除的减益效果， 持续10秒
        """
        ...

    def vp_2(self):
        """
        [战服 · 超限压制]\n
        删除寻敌功能\n
        快速包围前方圆形范围进行攻击\n
        - 被包围的敌人被推到中心位置\n
        - 无敌持续时间增加\n
        [保护模件 (净化)]\n
        施放时， 队员和自身恢复生命值最大值10%的生命值\n
        免疫一次解除的减益效果， 持续10秒
        """
        ...

# 战服 · 超负荷炮
# gunner_female/paramedic/955eb7e828c2517131a80f580186838c
# 944b9aab492c15a8474f96947ceeb9e4/955eb7e828c2517131a80f580186838c
class Skill36(ActiveSkill):
    """
    取出战斗服内置的遥控兵器并部署于前方， 为其超负荷充能后， 以强烈的冲击力向前方发射， 对敌人造成伤害。\n
        施放后立即为队员提供强化后的[保护模件 (缓冲)]效果。\n
    [保护模件 (缓冲) 强化效果]\n
        降低所受伤害、 进入霸体状态
    """
    name = "战服 · 超负荷炮"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [1185, 4873]
    uuid = "955eb7e828c2517131a80f580186838c"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 能量炮发射攻击力 : {value0} X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 强化保护罩充能量 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 强化保护罩降低伤害率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [战服 · 超负荷炮]\n
        改变激光输出方式\n
        - 以施放者为中心画圆进行发射\n
        总攻击力相同\n
        [系统 · 限制解除]\n
        强化保护罩持续时间 +3秒\n
        所受伤害减少量 +5%
        """
        ...

    def vp_2(self):
        """
        [战服 · 超负荷炮]\n
        改变激光输出方式\n
        - 医神设备自动施放\n
        可以在其他动作中施放\n
        激光多段攻击次数 +5次\n
        总攻击力相同\n
        [系统 · 限制解除]\n
        强化保护罩持续时间 +3秒\n
        所受伤害减少量 +5%
        """
        ...

# 绝境策略 : 极限歼灭
# gunner_female/paramedic/c6eaf15c287d9154479d1714cad5b4e0
# 944b9aab492c15a8474f96947ceeb9e4/c6eaf15c287d9154479d1714cad5b4e0
class Skill37(ActiveSkill):
    """
    战勤统帅在判断小队即将全灭时， 可启用的机密战术程序。 该程序需通过战勤统帅的权限启用， 执行时激活自律神经系统约3秒， 随后调用战斗服内置的所有兵器， 发动毁天灭地的攻势。
    """
    name = "绝境策略 : 极限歼灭"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2327, 9573]
    uuid = "c6eaf15c287d9154479d1714cad5b4e0"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 爪攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 无人机协同攻击力 : {value1} X {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 护盾砸击攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 超负荷炮攻击力 : {value4} X {value5}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 系统常量 · 战斗服 (改良型)
# gunner_female/paramedic/6bdcefb90e5e4387d4faa3633b4b587c
# 944b9aab492c15a8474f96947ceeb9e4/6bdcefb90e5e4387d4faa3633b4b587c
class Skill38(PassiveSkill):
    """
    重霄·协战师的战斗服， 不仅具备顶尖的战斗功能， 还兼顾了外出旅行的需求。\n
        进入地下城时， 重霄·协战师的战斗服外形将会改变。
    """
    name = "系统常量 · 战斗服 (改良型)"
    learnLv = 95
    masterLv = 1
    maxLv = 1
    position = 1 #TODO
    rangeLv = 3
    uuid = "6bdcefb90e5e4387d4faa3633b4b587c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 系统 · 临战编程
# gunner_female/paramedic/5fed75723a5d5d373c9f54fba1c7dc06
# 944b9aab492c15a8474f96947ceeb9e4/5fed75723a5d5d373c9f54fba1c7dc06
class Skill39(PassiveBufferSkill):
    """
    在瞬息万变的战场， 重霄·协战师面对危急状况时， 常常临时起意修改战术程序。 这些令人胆寒的代码， 连编制者本人都不敢执行。 在未来的战斗中， 这些程序或许还将不断修改。\n
        提升重霄·协战师的基本攻击力、 转职技能攻击力和精神， 部分技能在程序修改后会进一步强化。\n
        [战服 · 机动打击] : 施放后即刻发动第二击。\n
        [近战 · 闪退射击] : 施放后立即为队员提供强化后的[保护模件 (缓冲)]效果。
    """
    name = "系统 · 临战编程"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 3
    uuid = "5fed75723a5d5d373c9f54fba1c7dc06"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 精神增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)

    Spirit = data1
    associate = [{"data": data1,"type": "$+Spirit","ratio":1}]  # type: ignore

# 系统 · 孤军突破
# gunner_female/paramedic/56ef36c1980e67dd2bb50b180a925b89
# 944b9aab492c15a8474f96947ceeb9e4/56ef36c1980e67dd2bb50b180a925b89
class Skill40(ActiveSkill):
    """
    작전 중 다양한 요인으로, 적으로 둘러싸인 경우. 진(眞) 패러메딕은 즉시 천계군 사령부에 연락을 취한 뒤 전장 상공에 수집 중인 APIUS를 불러들여 돌파 프로세스를 시행한다.\n
    결합 된 APIUS는 수집된 정보를 계산하여 1회 소모 가능한 전장 정보를 지급한다. 이후 고립부 지역의 적 정보를 산출한 뒤 에너지를 방출하여 주변 적들에게 피해를 입힌다.\n
    승인 대기 중인 상태에서 받는 모든 피해는 막거나 피해낸다.
    """
    name = "系统 · 孤军突破"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 2 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [1336, 5493]
    uuid = "56ef36c1980e67dd2bb50b180a925b89"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 폭발 공격력 : {value1} X {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 타격 당 정보 습득률 : 40%
    # [범위 정보]
    # 폭발 범위 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 空袭策略 : 神兵天降
# gunner_female/paramedic/d40a932ac818bf4fa044dc1e4f8b2708
# 944b9aab492c15a8474f96947ceeb9e4/d40a932ac818bf4fa044dc1e4f8b2708
class Skill41(ActiveBufferSkill):
    """
    从交战区域上空俯冲而下， 执行超高空速降程序。\n
        重霄·协战师抵达交战区域上空， 为队员们提供强化效果， 随后倾尽全力发动强袭歼灭行动。\n
        增益效果根据[强袭策略 : 区域肃清]的一定比率生效。\n
        强袭流程会根据关联的觉醒技能而变化。\n
    选择[强袭策略 : 区域肃清]时 :\n
        为队员们提供持续一段时间的增益效果。\n
    选择[绝境策略 : 极限歼灭]时 :\n
        提供[强袭策略 : 区域肃清]增益效果和可重复生效的增益效果。 强袭前预输入[强袭策略 : 区域肃清]技能， 可无需施放动作直接施放； 通过预输入施放时， [强袭策略 : 区域肃清]的攻击力将以一定比率合算至[空袭策略 : 神兵天降]的激光攻击力中。\n
        2种关联均适用同步化流程。\n
        [三次觉醒技能]\n
        施放三次觉醒技能时， 与关联技能共享冷却时间。\n
        若关联技能还在冷却中， 则无法施放三次觉醒技能。
    """
    name = "空袭策略 : 神兵天降"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [3258, 13402]
    uuid = "d40a932ac818bf4fa044dc1e4f8b2708"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    buffType = 'awakeSub'

    # 激光多段攻击力 : {value0} X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 连锁爆炸多段攻击力 : {value2} X {value3}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 选择[强袭策略 ： 区域肃清]时效果
    # 力量/智力增加 : [强袭策略 ： 区域肃清]的{value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 攻击/移动速度增加 : [强袭策略 ： 区域肃清]的{value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 效果持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 选择[绝境策略 ： 极限歼灭]时效果
    # 力量/智力增加 : [强袭策略 ： 区域肃清]的{value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 效果持续时间 : {value8}秒
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 预输入[强袭策略 ： 区域肃清]时攻击力合算比率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)


    def skillInfo(self):
        """技能信息"""
        prep = self.char.AwakeSkill.skillInfo()
        ratio = 0
        # 绑定一觉时，替代一觉
        if self.char.bindAwake == 50:
            ratio = self.data4[self.lv] / 100
        if self.char.bindAwake == 85:
            ratio = self.data7[self.lv] / 100
        return prep[0] * ratio, [prep[1][0]*ratio,prep[1][1],prep[1][2]*ratio], [prep[2][0]*ratio,prep[2][1],prep[2][2]*ratio],0,self.getSkillCD()

class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'paramedic'
        self.nameCN = '重霄·协战师'
        self.role = 'gunner_female'
        self.角色 = '神枪手(女)'
        self.职业 = '协战师'
        self.jobId = '944b9aab492c15a8474f96947ceeb9e4'
        self.jobGrowId = '92da05ec93fb43406e193ffb9a2a629b'

        self.武器选项 = ['手弩', '步枪','左轮枪','自动手枪','手炮'] # TODO
        self.输出类型选项 = ["魔法固伤"] # TODO
        self.输出类型 = '魔法固伤' # TODO
        self.防具精通属性 = ['精神'] # TODO
        self.防具类型 = '板甲'
        self.buff = ... # TODO

        self.buffer = True

        self.适用属性 = '精神'

        super().__init__(equVersion, __name__)

    def load_skills(self):
        super().load_skills()
        for skill in self.skills:
            if skill.buffer and skill.buffType == 'buff' and skill.learnLv == 30:
                self.BuffSkill = skill
            if skill.buffer and skill.buffType == 'awake':
                self.AwakeSkill = skill
