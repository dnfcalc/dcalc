#f6a4ad30555b99b499c07835f87ce522
from core.basic.skill import PassiveSkill, ActiveSkill, get_data, ActiveBufferSkill, PassiveBufferSkill
from core.basic.character import Character
prefix = "priest_male/crusader_male/cn/skillDetail"

# 空斩打
# priest_male/crusader_male/3c5604bdbb0240b8f130f59ab40509c3
# f6a4ad30555b99b499c07835f87ce522/3c5604bdbb0240b8f130f59ab40509c3
class Skill0(ActiveSkill):
    """
        用巨兵向敌人发出攻击并使其浮空， 发动时有霸体判定。 \n
        在[意念驱动]已施放状态下， 将无法使用此技能。\n
        转职为光明骑士后， 技能类型变为独立攻击力。\n
        转职为驱魔师后， 可以蓄气攻击。
    """
    name = "空斩打"
    learnLv = 1
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    cd = 2
    uuid = "3c5604bdbb0240b8f130f59ab40509c3"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 浮空力比率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)



# 神的恩赐
# priest_male/crusader_male/0232c151ef3731c2dede51931a374723
# f6a4ad30555b99b499c07835f87ce522/0232c151ef3731c2dede51931a374723
class Skill2(PassiveBufferSkill):
    """
        获得神的恩泽， 增加所有异常状态的抗性。
    """
    name = "神的恩赐"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "0232c151ef3731c2dede51931a374723"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 所有异常状态抗性增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)


# 缓慢愈合
# priest_male/crusader_male/1fadde0eece18649caddbca7bd58cc2f
# f6a4ad30555b99b499c07835f87ce522/1fadde0eece18649caddbca7bd58cc2f
class Skill7(ActiveBufferSkill):
    """
        选择一定范围内的队员恢复生命值。
    """
    name = "缓慢愈合"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 3
    cd = 8
    mp = [28, 308]
    uuid = "1fadde0eece18649caddbca7bd58cc2f"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 生命值恢复时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 生命值恢复量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 队员选择范围 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)


# 净化
# priest_male/crusader_male/d0cdaca82892e54097f22a1f60817048
# f6a4ad30555b99b499c07835f87ce522/d0cdaca82892e54097f22a1f60817048
class Skill9(ActiveBufferSkill):
    """
        使一定范围内的队员消除异常状态。
    """
    name = "净化"
    learnLv = 10
    masterLv = 1
    maxLv = 11
    position = 0 #TODO
    rangeLv = 5
    cd = 15
    mp = [22, 238]
    uuid = "d0cdaca82892e54097f22a1f60817048"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 消除异常状态数量 : {value0}个
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [范围信息]
    # [净化]适用范围 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)


# 落凤锤
# priest_male/crusader_male/45442bbbe33540b4deeec29437dae70c
# f6a4ad30555b99b499c07835f87ce522/45442bbbe33540b4deeec29437dae70c
class Skill13(ActiveSkill):
    """
        跳跃后把巨兵砸向地面引发冲击波并使周围敌人受到一定伤害。\n
        跳跃时可以移动， 但蓝拳使者在[意念驱动]已施放状态下， 无法使用此技能。\n
        转职成为驱魔师时， 增加20%的攻击力， 增加冲击波范围、 跳跃高度和跳跃速度。\n
        而且， 下劈后可以强制中断动作并施放部分驱魔师巨兵系技能。\n
    - [可施放技能] -\n
    [疾风打]\n
    [星落打]\n
    [狂乱锤击]\n
    [疾空旋风破]\n
    [无双击]\n
    [逆鳞震]\n
    [逆龙七杀]
    """
    name = "落凤锤"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 6
    mp = [28, 308]
    uuid = "45442bbbe33540b4deeec29437dae70c"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 巨兵打击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 冲击波范围 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 冲击波攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 转职成为驱魔师时， 冲击波范围增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 纯白之刃
# priest_male/crusader_male/4b2c90ec226fd40e967875aa5eabefb2
# f6a4ad30555b99b499c07835f87ce522/4b2c90ec226fd40e967875aa5eabefb2
class Skill14(ActiveSkill):
    """
        凝聚力量用双臂划出十字形刀刃攻击前方敌人。
    """
    name = "纯白之刃"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 2
    mp = [27, 294]
    uuid = "4b2c90ec226fd40e967875aa5eabefb2"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 发动速度增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 刀刃攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 敌人僵直时间比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 勇气恩赐
# priest_male/crusader_male/2ba299855fc22192cba4f73db75e9d0e
# f6a4ad30555b99b499c07835f87ce522/2ba299855fc22192cba4f73db75e9d0e
class Skill15(PassiveSkill):
    """
    只有崇高信仰的光明骑士才能获得的恩赐。 守护的意志转化为勇气之光， 使其能更加专注于战斗。\n
        学习后， 角色定位由辅助变为输出， 且无法学习[守护恩赐]。\n
        增加自身的基本攻击力和技能攻击力， 并变更部分技能的功能。\n
    [信念光环]\n
    不发动光环效果。\n
    [天启之光]\n
    冷却时间缩短为145秒， 不发动祝福增益效果。\n
    [神圣之光]\n
    只能对自身使用。\n
    [神圣洗礼 : 信仰之翼]\n
    无法施放。\n
    [生命礼赞 : 神威]\n
    仅发动[信仰之翼 : 裁决]， 不适用增益效果。
    """
    name = "勇气恩赐"
    learnLv = 15
    masterLv = 15
    maxLv = 25
    position = 0 #TODO
    rangeLv = 3
    uuid = "2ba299855fc22192cba4f73db75e9d0e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

# 守护恩赐
# priest_male/crusader_male/2c9d9a36c8401bddff6cdb80fab8dc24
# f6a4ad30555b99b499c07835f87ce522/2c9d9a36c8401bddff6cdb80fab8dc24
class Skill16(PassiveBufferSkill):
    """
        只有崇高信仰的光明骑士才能获得的恩赐。\n
        学习后， 无法学习[勇气恩赐]； 增加体力与精神， 使被光明骑士命中的敌人进入所受属性伤害增加的减益状态。\n
        属性伤害增加效果持续一段时间， 该效果可以叠加一定次数。\n
        属性伤害增加效果无法与光明骑士 (女) 的[圣光灌注]、 小魔女的[冥月绽放]、 缪斯的[多彩感性]、 协战师的[系统 · 战场信息]效果叠加。\n
        单人挑战时， 不适用属性伤害增加效果， 且如果体力或精神高于智力， 则智力提升至与体力或精神一致， 并适用单人挑战专属效果。
    """
    name = "守护恩赐"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 3
    uuid = "2c9d9a36c8401bddff6cdb80fab8dc24"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 体力增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 精神增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 属性伤害量增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 属性伤害量增加持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 属性伤害量增加最大叠加数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [单人挑战专属效果]
    # 独立攻击力增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 技能冷却时间减少率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    Vitality = data0
    Spirit = data1

    associate = [
        {"data":data0,"type":"$+Vitality","ratio":1},
        {"data":data1,"type":"$+Spirit","ratio":1}
    ]
    CarryRatio = [0, (1.055 ** 3) * 100 - 100]# noqa: E501

# 光之正义
# priest_male/crusader_male/547ab2b2bd860d3e37355a9cfbc1077c
# f6a4ad30555b99b499c07835f87ce522/547ab2b2bd860d3e37355a9cfbc1077c
class Skill17(ActiveSkill):
    """
        赋予在被击或攻击时， 有一定几率落下闪电的增益效果。\n
        闪电攻击受[基础精通]影响。
    """
    name = "光之正义"
    learnLv = 20
    masterLv = 1
    maxLv = 11
    position = 0 #TODO
    rangeLv = 2
    cd = 10
    mp = [45, 469]
    uuid = "547ab2b2bd860d3e37355a9cfbc1077c"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 闪电攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [攻击时信息]
    # 闪电触发几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 闪电冷却时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [被击时信息]
    # 受魔法伤害时闪电触发几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 受物理伤害时闪电触发几率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 闪电冷却时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [被击时的感电效果]
    # 感电攻击力 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 感电几率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 感电持续时间 : {value9}秒
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [范围信息]
    # 闪电大小比率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)

# 灵魂牺牲
# priest_male/crusader_male/a5fa08f5d509e6ff2ebc68856a470b5a
# f6a4ad30555b99b499c07835f87ce522/a5fa08f5d509e6ff2ebc68856a470b5a
class Skill18(PassiveSkill):
    """
        灵魂修炼到极致， 增加移动速度、 施放速度、 基本攻击力和技能攻击力。\n
        光明骑士死亡时， 恢复一定范围内队员的生命值和魔法值。
    """
    name = "灵魂牺牲"
    learnLv = 20
    masterLv = 1
    maxLv = 6
    position = 0 #TODO
    rangeLv = 3
    uuid = "a5fa08f5d509e6ff2ebc68856a470b5a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 移动速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 施放速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 基本攻击力和技能攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [死亡时附加效果]
    # 队员恢复效果适用范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 队员生命值恢复量 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 队员魔法值恢复量 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 胜利之矛
# priest_male/crusader_male/8510294202d0e042dd29a2422fc6770d
# f6a4ad30555b99b499c07835f87ce522/8510294202d0e042dd29a2422fc6770d
class Skill19(ActiveSkill):
    """
        向敌人投掷由神圣之力凝聚成的矛。\n
        蓄气时， 增加穿刺攻击力和穿刺敌人数量。
    """
    name = "胜利之矛"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 6.6
    mp = [32, 343]
    uuid = "8510294202d0e042dd29a2422fc6770d"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 蓄气时间上限 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 穿刺攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最大蓄气时攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 穿刺敌人数量上限 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 最大蓄气时穿刺数量上限 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 大小比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)


# 圣灵之槌
# priest_male/crusader_male/d8ff976e2aaa4720272a5175d1eb9126
# f6a4ad30555b99b499c07835f87ce522/d8ff976e2aaa4720272a5175d1eb9126
class Skill21(ActiveSkill):
    """
    召唤出凝聚圣灵之力的战槌， 改变基本攻击。\n
        基本攻击第3击和[空斩打]攻击力受[基础精通]影响。\n
        增加基本攻击力、 技能攻击力、 所有速度和命中率。
    """
    name = "圣灵之槌"
    learnLv = 20
    masterLv = 20
    maxLv = 30
    position = 0 #TODO
    rangeLv = 2
    cd = 5
    uuid = "d8ff976e2aaa4720272a5175d1eb9126"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 移动速度增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 施放速度增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 命中率增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [技能附加信息]
    # 基本攻击第3击冲击波攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [空斩打]冲击波攻击力 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [落凤锤]冲击波攻击力 : {value8}
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [范围信息]
    # 基本攻击第3击冲击波大小增加率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [空斩打]冲击波大小增加率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # [落凤锤]冲击波大小增加率 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)

# 守护徽章
# priest_male/crusader_male/3d8f3d438405d79f8d3ed68072674d1e
# f6a4ad30555b99b499c07835f87ce522/3d8f3d438405d79f8d3ed68072674d1e
class Skill22(ActiveBufferSkill):
    """
        使一定范围内的队员们增加物防、 魔防、 体力、 精神和生命值/魔法值最大值。\n
        该技能效果不与光明骑士 (女) 的[守护祝福]、 小魔女的[小魔女的偏爱]技能、 缪斯的[主角登场]、 协战师的[装甲强化]效果叠加。
    """
    name = "守护徽章"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    cd = 10
    mp = [201, 262]
    uuid = "3d8f3d438405d79f8d3ed68072674d1e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理防御力增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 魔法防御力增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 体力增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 精神增加 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 生命值最大值增加 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 魔法值最大值增加 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 增益效果范围 : {value7}px
    data7 = get_data(f'{prefix}/{uuid}', 7)

    Vitality = data3
    Spirit = data4

    associate = [{"type":"$+Vitality","value":data3},{"type":"$+Spirit","value":data4}]

# 圣光守护
# priest_male/crusader_male/ff171dc487807bb9aa28900ca9a46b41
# f6a4ad30555b99b499c07835f87ce522/ff171dc487807bb9aa28900ca9a46b41
class Skill23(ActiveSkill):
    """
        选择一定范围内的队员， 使队员置身于神圣的光晕中。\n
        神圣光晕护盾的生命值等于光明骑士生命值的一定比率， 持续期间代替角色承受物理、 魔法伤害； 神圣光晕护盾的生命值耗尽时， 神圣光晕护盾将消失。\n
        使用消耗品增加的生命值不会提升护盾效果。\n
        在决斗场中， 只能吸收物理伤害。
    """
    name = "圣光守护"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    cd = 15
    mp = [85, 154]
    uuid = "ff171dc487807bb9aa28900ca9a46b41"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 屏障持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 屏障生命值比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 队员选择范围 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 快速愈合
# priest_male/crusader_male/d2c6df5105577fb59fb92529a36165a0
# f6a4ad30555b99b499c07835f87ce522/d2c6df5105577fb59fb92529a36165a0
class Skill24(PassiveSkill):
    """
        缩短[缓慢愈合]的生命值恢复时间， 提高生命值恢复比率。
    """
    name = "快速愈合"
    learnLv = 25
    masterLv = 1
    maxLv = 6
    position = 0 #TODO
    rangeLv = 2
    uuid = "d2c6df5105577fb59fb92529a36165a0"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # [缓慢愈合]生命值恢复时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [缓慢愈合]生命值恢复比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 圣光十字
# priest_male/crusader_male/2a0a39184de92acf1c1375e00b77404c
# f6a4ad30555b99b499c07835f87ce522/2a0a39184de92acf1c1375e00b77404c
class Skill25(ActiveBufferSkill):
    """
        发射神圣十字。\n
        攻击成功时爆炸， 赋予光明骑士神圣之力， 增加所有速度。\n
        学习[守护恩赐]后， 对魔法阵内的自身和队友额外发动所有速度增加增益效果。
    """
    name = "圣光十字"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 8
    mp = [32, 343]
    uuid = "2a0a39184de92acf1c1375e00b77404c"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 光杖攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 光杖爆炸攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [增益效果]
    # 持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 攻击/移动/施放速度增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [学习守护恩赐后增益效果信息]
    # 持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 攻击/移动/施放速度增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 光杖和魔法阵大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

# 圣光沁盾
# priest_male/crusader_male/8ee0099656df08a0b39225f8a21d514b
# f6a4ad30555b99b499c07835f87ce522/8ee0099656df08a0b39225f8a21d514b
class Skill26(ActiveSkill):
    """
        使用神圣之力生成盾壁， 抵挡远程攻击。\n
        队员可以通过盾壁， 但敌方无法通过。 
    """
    name = "圣光沁盾"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 8
    mp = [91, 763]
    uuid = "8ee0099656df08a0b39225f8a21d514b"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 盾壁的生命值 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 盾壁持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 撞击攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 荣誉祝福
# priest_male/crusader_male/e4c354a89c337310aeb7041d5e742828
# f6a4ad30555b99b499c07835f87ce522/e4c354a89c337310aeb7041d5e742828
class Skill27(ActiveBufferSkill):
    """
    使一定范围内除自身以外的队友增加物理攻击力、 魔法攻击力、 独立攻击力、 力量、 智力和命中率； 增加自身基本攻击力和技能攻击力。\n
        物理/魔法/独立攻击力和力量/智力的增加量， 随施放者的体力或精神值提高而增加， 以体力与精神二者中较高值为标准。\n
        达到20级以上后， 增加基本攻击力和技能攻击力效果保持不变。\n
        效果不与光明骑士 (女) 的[勇气祝福]、 小魔女的[禁术吟咏]、 缪斯的[可爱节拍]、 协战师的[军械强化]效果叠加。
    """
    name = "荣誉祝福"
    learnLv = 30
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 3
    cd = 10
    uuid = "e4c354a89c337310aeb7041d5e742828"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    buffer = True
    buffType = "buff"

    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理攻击力增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 魔法攻击力增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 独立攻击力增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 力量增加 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 智力增加 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 命中率增加 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 基本攻击力和技能攻击力增加率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [范围信息]
    # 增益效果范围 : {value8}px
    data8 = get_data(f'{prefix}/{uuid}', 8)

    ATK = data1
    STRINT = data4

# 双子沁盾
# priest_male/crusader_male/3fb8395ae3b81bd608e0c4223a8eb534
# f6a4ad30555b99b499c07835f87ce522/3fb8395ae3b81bd608e0c4223a8eb534
class Skill28(PassiveSkill):
    """
        使用神圣之力生成2个盾壁， 抵挡远程攻击。\n
        队友可以通过盾壁， 但敌人无法通过。\n
        盾壁生命值以[圣光沁盾]生命值的一定比例适用。
    """
    name = "双子沁盾"
    learnLv = 30
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 0
    uuid = "3fb8395ae3b81bd608e0c4223a8eb534"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 盾壁的生命值 : [圣光沁盾]的{value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 盾壁持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 撞击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 坚定信念
# priest_male/crusader_male/030663e99462f628b4c9f813e1406c4e
# f6a4ad30555b99b499c07835f87ce522/030663e99462f628b4c9f813e1406c4e
class Skill29(PassiveSkill):
    """
        信仰虔诚的光明骑士意志更加坚强， 不易被摧毁。\n
        学习技能后， 增加基本攻击力、 转职技能攻击力和魔法暴击率。
    """
    name = "坚定信念"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    uuid = "030663e99462f628b4c9f813e1406c4e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 圣光球
# priest_male/crusader_male/9bff7f2559e003766fee2853dca00631
# f6a4ad30555b99b499c07835f87ce522/9bff7f2559e003766fee2853dca00631
class Skill30(ActiveSkill):
    """
        向前方发射一个移动的光球。\n
        光球消失时造成眩晕效果。\n
        按前方向键时， 可以在远处生成光球。\n
        在决斗场中， 面向光球的敌人进入眩晕状态。
    """
    name = "圣光球"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cube = 1
    cd = 14.4
    mp = [150, 1260]
    uuid = "9bff7f2559e003766fee2853dca00631"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 球体攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 球体多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 眩晕持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 球体大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 眩晕范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [圣光球]\n
        施放除觉醒技能外的转职技能时， 可以施放[圣光球]\n
        - 删除施放动作\n
        球体多段攻击次数 -8次\n
        - 总攻击力相同\n
        眩晕持续时间 +20%\n
        眩晕范围 +20%\n
        [圣光琉璃碎]\n
        施放除觉醒技能外的转职技能时， 可以施放[圣光琉璃碎]\n
        - 删除施放动作\n
        眩晕持续时间 +20%\n
        眩晕范围 +20%\n
        [圣光守护]\n
        变更为范围效果\n
        - 屏障持续时间变更为2.5秒\n
        - 屏障生命值比率 +30%\n
        - 增益效果适用范围 -25%
        """
        ...

    def vp_2(self):
        """
        [圣光球]\n
        施放时， 生成追踪范围内最强敌人的球体\n
        - 范围内不存在敌人时， 无法使用技能\n
        球体大小 +30%\n
        [圣光琉璃碎]\n
        施放时， 生成追踪范围内最强敌人的球体并引发爆炸\n
        - 范围内不存在敌人时， 无法使用技能\n
        球体大小 +30%\n
        [圣光守护]\n
        变更为范围效果\n
        - 屏障持续时间变更为2.5秒\n
        - 屏障生命值比率 +30%\n
        - 增益效果适用范围 -25%
        """
        ...

# 圣光琉璃碎
# priest_male/crusader_male/9dc8438e4572d39243c97da31c113acc
# f6a4ad30555b99b499c07835f87ce522/9dc8438e4572d39243c97da31c113acc
class Skill31(PassiveSkill):
    """
        生成光球向前方移动后爆炸。\n
        球体爆炸时触发眩晕效果。\n
        按前方向键， 可以在远处生成光球。
    """
    name = "圣光琉璃碎"
    learnLv = 35
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 0
    uuid = "9dc8438e4572d39243c97da31c113acc"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 球体爆炸攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 球体持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 眩晕持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 球体大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 眩晕范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 圣光聚合
# priest_male/crusader_male/dacd5c2848a1eb33489e5471f1a73759
# f6a4ad30555b99b499c07835f87ce522/dacd5c2848a1eb33489e5471f1a73759
class Skill32(ActiveSkill):
    """
        用身体吸收神圣的洗礼光柱之后引发爆炸。\n
        发生爆炸时， 吸附周围的敌人。
    """
    name = "圣光聚合"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 10
    mp = [32, 343]
    uuid = "dacd5c2848a1eb33489e5471f1a73759"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 光柱攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 光撞击地面攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 光柱大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [圣光聚合]\n
        聚集圣光之力， 一次性引发爆炸\n
        - 命中时， 可以吸附霸体状态的敌人\n
        - 总攻击力相同\n
        爆炸范围 +50%\n
        [缓慢愈合]\n
        变更为范围效果\n
        - 生命值恢复量 -30%\n
        - 增益效果范围 -10%\n
        - 学习[勇气恩赐]后不生效效
        """
        ...

    def vp_2(self):
        """
        [圣光聚合]\n
        施放时， 初始化[神圣之光]技能冷却时间\n
        [神圣之光]攻击力 -50%\n
        学习[勇气恩赐]后， [圣光聚合]技能施放过程中， 可以施放[神圣之光]\n
        - 删除[神圣之光]施放动作， 合算攻击力\n
        [缓慢愈合]\n
        变更为范围效果\n
        - 生命值恢复量 -30%\n
        - 增益效果范围 -10%\n
        - 学习[圣灵之槌]后不生效
        """
        ...

# 生命源泉
# priest_male/crusader_male/ade01c1d6afc8a05055225045e89fe49
# f6a4ad30555b99b499c07835f87ce522/ade01c1d6afc8a05055225045e89fe49
class Skill33(ActiveBufferSkill):
    """
        选择一定范围内的队员， 赋予增加生命值恢复和死亡时复活的增益效果。\n
        复活效果发动后， 增益效果立即消失。\n
        选择队员的状态下， 按跳跃键可以立即取消技能。\n
        仅在存在队员时可以使用， 决斗场中无法使用。
    """
    name = "生命源泉"
    learnLv = 40
    masterLv = 1
    maxLv = 11
    position = 0 #TODO
    rangeLv = 2
    cube = 2
    cd = 60
    mp = [521, 665]
    uuid = "ade01c1d6afc8a05055225045e89fe49"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 每分钟生命值恢复量增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 复活后生命值恢复量 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 队员选择范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 忏悔之锤
# priest_male/crusader_male/b3659936a9a74c4ed6f7faf07cca1f9e
# f6a4ad30555b99b499c07835f87ce522/b3659936a9a74c4ed6f7faf07cca1f9e
class Skill34(ActiveSkill):
    """
        向前方敌人挥动由神圣之力凝聚成的巨大锤子。 命中时， 会有一定几率使敌人进入忏悔状态并攻击周围的同类。\n
        对领主、 稀有、 深渊怪物和人类型怪物， 会降低持续时间和忏悔几率。\n
        决斗场中不适用忏悔效果。
    """
    name = "忏悔之锤"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cube = 1
    cd = 14.4
    mp = [160, 1344]
    uuid = "b3659936a9a74c4ed6f7faf07cca1f9e"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 巨锤攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 巨锤冲击波攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [忏悔效果]
    # 忏悔几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 忏悔持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 巨锤大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [忏悔之锤]\n
        绘制圣印， 从天上落下米歇尔之锤\n
        - 总攻击力相同\n
        [圣光十字]\n
        学习[守护恩赐]后， 所有速度额外 +15%
        """
        ...

    def vp_2(self):
        """
        [忏悔之锤]\n
        基本冷却时间变更为28.8秒\n
        总攻击力 +100%\n
        施放过程中所受伤害 -90%\n
        [圣光十字]\n
        学习[守护恩赐]后， 所有速度额外 +15%
        """
        ...

# 圣愈之风
# priest_male/crusader_male/5dc7008b12a459325b548b0715c6b73c
# f6a4ad30555b99b499c07835f87ce522/5dc7008b12a459325b548b0715c6b73c
class Skill35(ActiveBufferSkill):
    """
        使一定范围内的队员恢复生命值和魔法值， 并设置屏障。\n
        屏障的生命值为光明骑士生命值的一定比例。\n
        队员离开技能范围或生命值耗尽时， 屏障消失。\n
        通过消耗品提升的生命值不会提升屏障效果。\n
        施放过程中按跳跃键时， 可以中断技能。
    """
    name = "圣愈之风"
    learnLv = 45
    masterLv = 1
    maxLv = 11
    position = 0 #TODO
    rangeLv = 2
    cube = 2
    cd = 60
    mp = [806, 1159]
    uuid = "5dc7008b12a459325b548b0715c6b73c"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 生命值和魔法值恢复时间 : {value0}秒 
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 生命值恢复量 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 魔法值恢复量 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 屏障生命值比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 屏障持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 生命值和魔法值恢复范围 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 屏障适用范围 : {value6}px
    data6 = get_data(f'{prefix}/{uuid}', 6)

# 正义审判
# priest_male/crusader_male/ecc23c980ea71450c0ad0c3fd232f329
# f6a4ad30555b99b499c07835f87ce522/ecc23c980ea71450c0ad0c3fd232f329
class Skill36(ActiveSkill):
    """
        开启神圣魔法阵， 使其从空中飞下光刃， 最后出现正义天使投掷发光的长矛。\n
        光刃飞下过程中按跳跃键， 可以立即出现正义天使。
    """
    name = "正义审判"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [350, 2940]
    uuid = "ecc23c980ea71450c0ad0c3fd232f329"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 光刃攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 光刃多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 长矛爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [正义审判]\n
        施放圣者米歇尔的正义审判\n
        - 施放时进入无敌状态\n
        - 米歇尔的光刃多段攻击次数 : 10次\n
        - 总攻击力相同\n
        [圣愈之风]\n
        改为对队友赋予屏障\n
        - 赋予屏障后角色可以行动\n
        生命值/魔法值恢复量比率额外 +15%
        """
        ...

    def vp_2(self):
        """
        [正义审判]\n
        召唤光环向范围内所有敌人发射正义之矛后爆炸\n
        - 总攻击力相同\n
        施放除觉醒技能外的转职技能时， 可以施放[正义审判]\n
        - 删除施放动作\n
        [圣愈之风]\n
        改为对队友赋予屏障\n
        - 赋予屏障后角色可以行动\n
        生命值/魔法值恢复量比率额外 +15%
        """
        ...

# 信念光环
# priest_male/crusader_male/4f2e001e9a19eb7bae50ad1840dfb329
# f6a4ad30555b99b499c07835f87ce522/4f2e001e9a19eb7bae50ad1840dfb329
class Skill37(PassiveBufferSkill):
    """
        坚定的信仰， 为天启者赋予信念的权威。\n
        增加自身的基本攻击力与技能攻击力， 并生成使一定范围内的队员， 触发增加力量、 智力、 体力、 精神、 攻击速度、 移动速度、 施放速度和物理/魔法/独立攻击力增益效果的光环。\n
        物理/魔法/独立攻击力的增加效果仅对除自身以外的队友生效。\n
        学习[勇气恩赐]后， 不会发动光环效果。
    """
    name = "信念光环"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 3
    uuid = "4f2e001e9a19eb7bae50ad1840dfb329"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [光环效果]
    # 力量、 智力增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 体力、 精神增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 攻击、 移动、 施放速度增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 队员物理、 魔法、 独立攻击力增加 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 光环范围 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)

    STRINT = data1
    Vitality = data2
    Spirit = data2
    ATK = data4

# 天启之光
# priest_male/crusader_male/dcb31a63ef58954f44ff2070c42a9a98
# f6a4ad30555b99b499c07835f87ce522/dcb31a63ef58954f44ff2070c42a9a98
class Skill38(ActiveBufferSkill):
    """
        使出神圣之力破开天空， 降下闪电与光之长矛， 对敌人进行审判。\n
        充满神圣之力的光芒降临到队友身上， 给予他们祝福， 增加力量、 智力、 攻击速度、 移动速度和施放速度。\n
        力量/智力的增加量， 随施放者的体力或精神值提高而增加， 以体力与精神二者中较高值为标准。\n
        力量、 智力提升效果对自身无效。\n
        效果不与光明骑士 (女) 的[圣光天启]、 小魔女的[开幕！ 人偶剧场]、 缪斯的[梦想的舞台]、 协战师的[强袭策略 : 区域肃清]的效果叠加。\n
        学习[勇气恩赐]后， 天空中将不会降下充满神圣之力的光芒。
    """
    name = "天启之光"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 5
    cube = 5
    cd = 170
    mp = [1200, 10080]
    uuid = "dcb31a63ef58954f44ff2070c42a9a98"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    buffType = 'awake'

    # 闪电和光属性长矛多段攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 闪电和光属性长矛多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 光属性长矛爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [祝福效果信息]
    # 持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 力量增加 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 智力增加 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 攻击速度增加 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 移动速度增加 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 施放速度增加 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

    STRINT = data4

# 圣念
# priest_male/crusader_male/56aa7844a2da23f5bea9b585aea5ae45
# f6a4ad30555b99b499c07835f87ce522/56aa7844a2da23f5bea9b585aea5ae45
class Skill39(PassiveSkill):
    """
        天启者的体力和精神补正为两者中数值较高的一方、 物理暴击率和魔法暴击率补正为两者中数值较高的一方。
    """
    name = "圣念"
    learnLv = 50
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 3
    uuid = "56aa7844a2da23f5bea9b585aea5ae45"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 圣光突袭
# priest_male/crusader_male/c47b66efd27845ef14954928ea2f95c8
# f6a4ad30555b99b499c07835f87ce522/c47b66efd27845ef14954928ea2f95c8
class Skill40(ActiveSkill):
    """
        携神圣之力向前突进， 然后挥舞巨兵。
    """
    name = "圣光突袭"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [400, 1000]
    uuid = "c47b66efd27845ef14954928ea2f95c8"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 突进攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 突进多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 终结攻击攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 突进距离 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 光杖大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [圣光突袭]\n
        突进后， 删除终结攻击\n
        - 总攻击力相同\n
        突进距离 +50%\n
        光杖大小 +50%\n
        [净化]\n
        消除所有异常状态\n
        - 3秒内所有异常状态抗性 +100%\n
        - 增益适用范围 +50%\n
        - 学习[勇气恩赐]后不生效
        """
        ...

    def vp_2(self):
        """
        [圣光突袭]\n
        突进距离 -90%， 变更为单次攻击\n
        - 总攻击力相同\n
        在突进位置自动施放[圣光沁盾]\n
        - [圣光沁盾]进入冷却时间时无法施放\n
        [净化]\n
        消除所有异常状态\n
        - 3秒内所有异常状态抗性 +100%\n
        - 增益适用范围 +50%\n
        - 学习[勇气恩赐]后不生效
        """
        ...

# 神圣之矛
# priest_male/crusader_male/1c1a9606eb702ebe5a7bb4397f3aeae0
# f6a4ad30555b99b499c07835f87ce522/1c1a9606eb702ebe5a7bb4397f3aeae0
class Skill41(ActiveSkill):
    """
        生成远古神圣之矛并将其投掷出去。\n
        投掷时击退近距离的敌人， 然后神圣之矛垂直下落， 引发爆炸。
    """
    name = "神圣之矛"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [860, 1500]
    uuid = "1c1a9606eb702ebe5a7bb4397f3aeae0"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 下落攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 撞击地面攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 爆炸多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [神圣之矛]\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 20秒\n
        - 单次攻击力 -50%\n
        大小 +30%\n
        [天启之光]\n
        满足以下条件时当前冷却时间减少1秒 (最多25秒)\n
        - 使用[神圣之光]增加增益效果持续时间时\n
        - [圣愈之风]、 [圣佑结界]施加恢复效果时\n
        - 适用[守护恩赐]属性伤害量增加减益效果时 (冷却时间5秒)\n
        - 学习[勇气恩赐]后不生效
        """
        ...

    def vp_2(self):
        """
        [神圣之矛]\n
        向天空投掷两把神圣之矛后， 飞向最强敌人并将其贯穿\n
        - 角色前方范围内不存在敌人时， 无法施放技能\n
        - 总攻击力相同\n
        [天启之光]\n
        满足以下条件时当前冷却时间减少1秒 (最多25秒)\n
        - 使用[神圣之光]增加增益效果持续时间时\n
        - [圣愈之风]、 [圣佑结界]施加恢复效果时\n
        - 适用[守护恩赐]属性伤害量增加减益效果时 (冷却时间5秒)\n
        - 学习[勇气恩赐]后不生效
        """
        ...

# 圣佑结界
# priest_male/crusader_male/3af805da8505fe6234a95b535610f064
# f6a4ad30555b99b499c07835f87ce522/3af805da8505fe6234a95b535610f064
class Skill42(ActiveBufferSkill):
    """
        生成圣佑结界。\n
        结界闪烁引发爆炸后， 使队员恢复生命值， 并解除异常状态。\n
        可以利用方向键调整魔法阵生成位置。
    """
    name = "圣佑结界"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "3af805da8505fe6234a95b535610f064"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 生命值恢复量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 爆炸攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最终爆炸攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 魔法阵大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [圣佑结界]\n
        魔法阵大小 +40%\n
        删除多段攻击\n
        - 总攻击力相同\n
        - 总生命值恢复量相同\n
        [学习守护恩赐后生效]\n
        在指定位置发生爆炸后， 生成恢复生命值的圣域\n
        - 圣域生命值恢复持续时间 : 5.5秒
        """
        ...

    def vp_2(self):
        """
        [圣佑结界]\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 20秒\n
        - 单次攻击力 -50%\n
        - 单次生命值恢复量 -50%\n
        [学习勇气恩赐后追加效果]\n
        生命值恢复效果仅对自身适用\n
        - 多段攻击次数变更为2次\n
        - 生命值恢复量 +100%\n
        [学习守护恩赐后生效]\n
        在指定位置发生爆炸后， 生成恢复生命值的圣域\n
        - 圣域生命值恢复持续时间 : 5.5秒
        """
        ...

# 神圣之光
# priest_male/crusader_male/c4a5b868f1e8e60cd1867a2cfab4a242
# f6a4ad30555b99b499c07835f87ce522/c4a5b868f1e8e60cd1867a2cfab4a242
class Skill43(ActiveBufferSkill):
    """
        增加自身的体力和精神。\n
        选择一定范围内的队员， 使其受到神圣之光的庇佑， 减少所受伤害并引发爆炸。\n
        增加队员以及光明骑士自身增益效果的持续时间。\n
    [可增加持续时间的技能]\n
        [守护徽章]、 [荣誉祝福]。
    """
    name = "神圣之光"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 3
    cube = 3
    cd = 20
    mp = [348, 2700]
    uuid = "c4a5b868f1e8e60cd1867a2cfab4a242"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 体力、 精神增加量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 爆炸攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [获得增益时]
    # 持续时间增加 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 所受伤害减少率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 所受伤害减少持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 队员选择范围 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 爆炸大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    Vitality = data0
    Spirit = data0

    associate = [{"data": Vitality, "type": "$+Vitality"}, {"data": Spirit, "type": "$+Spirit"}]

    def vp_1(self):
        """
        [神圣之光]\n
        删除无色小晶块消耗量\n
        适用增益效果时， 所受伤害减少效果持续时间 +4.2秒\n
        [神圣洗礼 : 信仰之翼]\n
        队员适用信仰效果时， 自身也适用信仰效果\n
        - 信仰效果持续时间 -20秒\n
        - 信仰效果持续时间内所受伤害 -10%
        """
        ...

    def vp_2(self):
        """
        [神圣之光]\n
        爆炸范围 +40%\n
        学习[勇气恩赐]后获得速度增加增益\n
        - 增益持续时间 : 10秒\n
        - 所有速度 +10%\n
        [神圣洗礼 : 信仰之翼]\n
        队员适用信仰效果时， 自身也适用信仰效果\n
        - 信仰效果持续时间 -20秒\n
        - 信仰效果持续时间内所受伤害 -10%
        """
        ...

# 惩罚之锤
# priest_male/crusader_male/8d996a242c5c0efd8cfe6cb4bc6defcc
# f6a4ad30555b99b499c07835f87ce522/8d996a242c5c0efd8cfe6cb4bc6defcc
class Skill44(ActiveSkill):
    """
        装备至高无上的神之武器——惩罚之锤攻击敌人。\n
        装备时增加基本攻击力和技能攻击力， 并变更基本攻击和部分技能。\n
    [基本攻击/空斩打]\n
    - 基本攻击变更并适用光属性\n
    - 基本攻击最后一击和[空斩打]攻击时触发[神圣冲击]\n
    - 前冲攻击时触发[神圣闪光]\n
    - [神圣冲击]与[神圣闪光]攻击力受[基础精通]影响\n
    [落凤锤]\n
    - 变更为[雷霆粉碎]\n
    [光之正义]\n
    - 无法施放技能\n
    - 施放[惩罚之锤]时自动施放
    """
    name = "惩罚之锤"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "8d996a242c5c0efd8cfe6cb4bc6defcc"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 装备[惩罚之锤]后持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [基本攻击信息]
    # [神圣冲击]光柱攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [神圣冲击]冲击波攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [神圣闪光]攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [神圣闪光]多段攻击次数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [空斩打信息]
    # [神圣冲击]光柱攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [神圣冲击]冲击波攻击力 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [落凤锤信息]
    # [雷霆粉碎]攻击力 : {value8}
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [雷霆粉碎]冲击波攻击力 : {value9}
    data9 = get_data(f'{prefix}/{uuid}', 9)

# 神圣洗礼 : 信仰之翼
# priest_male/crusader_male/c524c4f378d1cd0ff99e4580750a4567
# f6a4ad30555b99b499c07835f87ce522/c524c4f378d1cd0ff99e4580750a4567
class Skill45(ActiveBufferSkill):
    """
    发动[神圣洗礼 : 信仰之翼]， 开始聚集神圣之力。\n
        施放转职技能或攻击敌人时都会聚集神圣之力。 \n
        每次聚集神圣之力时， 都会增加神思者的[荣誉祝福]增益效果。\n
    [施放时可积攒神圣之力的技能]\n
        [缓慢愈合]、 [净化]、 [光之正义]、 [守护徽章]、 [圣光守护]、 [荣誉祝福]、 [生命源泉]、 [圣愈之风]、 [天启之光]、 [神圣之光]、 [惩罚之锤 : 天怒]、 [生命礼赞 : 神威]\n
    [攻击时可积攒神圣之力的技能]\n
        [纯白之刃]、 [胜利之矛]、 [圣光十字]、 [圣光沁盾]、 [圣光球]、 [圣光琉璃碎]、 [圣光聚合]、 [忏悔之锤]、 [正义审判]、 [圣光突袭]、 [神圣之矛]、 [圣佑结界]、 [惩罚之锤]\n
        对队友使用[神圣之光]时， 生成信仰效果， 增加神圣之力持续时间。\n
        每名队员最多生成1层信仰效果， 对自身使用时不生成。
    """
    name = "神圣洗礼 : 信仰之翼"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "c524c4f378d1cd0ff99e4580750a4567"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    buffer = True
    buffType = "buffSub"

    # 神圣之力持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 神圣之力积攒上限 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 每点神圣之力可增加的[荣誉祝福]增益效果增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [信仰效果]
    # 持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 1层信仰效果时神圣之力持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 2层信仰效果时神圣之力持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 3层信仰效果时神圣之力持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def skillInfo(self):
        prep = self.char.BuffSkill.skillInfo()
        ratio = self.data2[self.lv] * 5 / 100
        return prep[0] * ratio, [prep[1][0]*ratio,prep[1][1],prep[1][2]*ratio], [prep[2][0]*ratio,prep[2][1],prep[2][2]*ratio],0,self.getSkillCD()

# 信仰之翼 : 裁决
# priest_male/crusader_male/481348575c1e141925c836b59c5db3ca
# f6a4ad30555b99b499c07835f87ce522/481348575c1e141925c836b59c5db3ca
class Skill46(ActiveSkill):
    """
        神思者跳到空中， 裁决地上的敌人。\n
        在[神圣洗礼 : 信仰之翼]已激活的状态下使用技能， 则[神圣洗礼 : 信仰之翼]与[信仰之翼 : 裁决]技能一起结束。
    """
    name = "信仰之翼 : 裁决"
    learnLv = 85
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 2500]
    uuid = "481348575c1e141925c836b59c5db3ca"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 爆炸攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 爆炸多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 终结爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 惩罚之锤 : 天怒
# priest_male/crusader_male/89c505581267af77c6d58dc49b710550
# f6a4ad30555b99b499c07835f87ce522/89c505581267af77c6d58dc49b710550
class Skill47(ActiveSkill):
    """
        该技能只能在装备[惩罚之锤]的状态下发动。\n
        注入圣遗物的力量， 在划出十字的瞬间， 生成光之翼， 将惩罚之锤强化为天怒之锤。\n
        光启·光明骑士高高跃起， 使用天怒之锤下劈， 使地面裂开并产生冲击波， 释放光芒后产生爆炸。\n
        展开光之翼时， 增加一定范围内队员的信仰效果时间。\n
        按向前方向键， 可以增加跳跃距离。
    """
    name = "惩罚之锤 : 天怒"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [1065, 8000]
    uuid = "89c505581267af77c6d58dc49b710550"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 信仰效果适用范围 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 信仰效果持续时间增加 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 冲击波攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 爆炸攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 神之代行者
# priest_male/crusader_male/89a4529234904fcbb3abe289e281f2fd
# f6a4ad30555b99b499c07835f87ce522/89a4529234904fcbb3abe289e281f2fd
class Skill48(PassiveBufferSkill):
    """
        被雷米迪奥斯所选择的光启·光明骑士， 使用生命之圣遗物 : 雷米迪奥斯之泪， 践行神的意志。\n
        增加基本攻击力和转职技能攻击力、 体力、 精神， 变更部分技能效果。\n
        [胜利之矛]\n
        施放技能时直接以最大蓄气的状态发动， 增加矛的大小， 并且矛刺中后可通过再次按键立即引爆。\n
        学习[圣灵之槌]后控制时间固定。\n
        [圣光十字]\n
        发射蕴含圣遗物之力的光杖并引爆。\n
        增加光杖的大小和魔法阵范围， 攻击敌人时生成的魔法阵也适用增益效果。\n
        攻击失败时， 会在自身位置生成魔法阵。
    """
    name = "神之代行者"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 3
    uuid = "89a4529234904fcbb3abe289e281f2fd"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 体力、 精神增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [胜利之矛]
    # 矛的大小额外增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    Vitality = Spirit = data1

    associate = [{"data": Vitality, "type": "$+Vitality"}, {"data": Spirit, "type": "$+Spirit"}]

# 生命礼赞 : 神威
# priest_male/crusader_male/a81e5b7defa1819263ed8e86f69fd06f
# f6a4ad30555b99b499c07835f87ce522/a81e5b7defa1819263ed8e86f69fd06f
class Skill49(ActiveBufferSkill):
    """
        以圣十字之名向神祈祷， 然后释放生命之圣遗物所具有的力量。\n
        生命之圣遗物激发神圣之光和雷米迪奥斯的权能， 祝福队友、 审判敌人。\n
        根据添加为发动技能的觉醒技能， 发动不同的能力。\n
        效果以[天启之光]的一定比率适用。\n
    选择[天启之光]时 : 祝福\n
        圣遗物升至空中并凝聚神圣力， 变为神圣的太阳。\n
    - 赋予队友效果， 持续一定时间。 (移动到其他房间时维持效果)\n
    选择[信仰之翼 : 裁决]时 : 审判\n
        圣遗物与天怒之锤融合， 激发天怒之锤真正的力量。\n
    - 赋予队友效果， 持续一定时间。 (移动到其他房间时解除效果)\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "生命礼赞 : 神威"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4025, 8055]
    uuid = "a81e5b7defa1819263ed8e86f69fd06f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    buffType = 'awakeSub'

    # 审判攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 审判多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 选择[天启之光]时效果
    # 持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 力量、 智力增加 : [天启之光]数值的{value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 攻击、 移动、 施放速度增加 : [天启之光]数值的{value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 选择[信仰之翼 : 裁决]时效果
    # 持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 力量、 智力增加 : [天启之光]数值的{value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def skillInfo(self):
        """技能信息"""
        prep = self.char.AwakeSkill.skillInfo()
        ratio = 0
        # 绑定一觉时，替代一觉
        if self.char.bindAwake == 50:
            ratio = self.data3[self.lv] / 100
        if self.char.bindAwake == 85:
            ratio = self.data6[self.lv] / 100
        return prep[0] * ratio, [prep[1][0]*ratio,prep[1][1],prep[1][2]*ratio], [prep[2][0]*ratio,prep[2][1],prep[2][2]*ratio],0,self.getSkillCD()

class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'crusader_male'
        self.nameCN = '神启·圣职者'
        self.role = 'priest_male'

        self.武器选项 = ['十字架','镰刀', '念珠', '战斧','图腾' ]
        self.输出类型选项 = ['魔法固伤']
        self.输出类型 = '魔法固伤'
        self.防具精通属性 = ['智力']
        self.防具类型 = '板甲'
        self.buff = 2.335

        self.角色 = '圣职者(男)'

        self.职业 = '圣骑士'

        self.buffer = True

        self.适用属性 = '体力'

        super().__init__(equVersion, __name__)


    def load_skills(self):
        super().load_skills()
        for skill in self.skills:
            if skill.buffer and skill.buffType == 'buff' and skill.learnLv == 30:
                self.BuffSkill = skill
            if skill.buffer and skill.buffType == 'awake':
                self.AwakeSkill = skill
