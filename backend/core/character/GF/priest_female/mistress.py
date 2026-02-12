#0c1b401bb09241570d364420b3ba3fd7
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "priest_female/mistress/cn/skillDetail"


# 钩颈斩
# priest_female/mistress/cfacda0647b9a0f595df2c2aad30c18d
# 0c1b401bb09241570d364420b3ba3fd7/cfacda0647b9a0f595df2c2aad30c18d
class Skill8(ActiveSkill):
    """
        大幅度挥动巨兵， 勾起敌人后砸向地面。\n
        对可抓取的敌人成功勾起后， 进入无敌状态。 随后按下向后键， 可将敌人扔向后方。\n
        对无法抓取的敌人不适用控制效果。\n
        堕落的七宗罪状态下使用时， 将被勾起的敌人拉到角色位置后砸向地面。\n
        转职为光明骑士后， 技能类型变为独立攻击力。
    """
    name = "钩颈斩"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 5
    mp = [10, 120]
    uuid = "cfacda0647b9a0f595df2c2aad30c18d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 勾拽攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 下劈攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

# 武器格挡
# priest_female/mistress/eb71e1d82d92c7e1d40500a0dcd77aa6
# 0c1b401bb09241570d364420b3ba3fd7/eb71e1d82d92c7e1d40500a0dcd77aa6
class Skill9(ActiveSkill):
    """
        竖起武器， 抵挡来自前方的攻击， 减少所受伤害。\n
        按住技能键可以维持防御姿态。 抵挡前方的攻击后， 可以强制使用其他技能。
    """
    name = "武器格挡"
    learnLv = 10
    masterLv = 5
    maxLv = 15
    position = 5
    rangeLv = 5
    cd = 2
    mp = [3, 4]
    uuid = "eb71e1d82d92c7e1d40500a0dcd77aa6"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 所受伤害减少率 (物理) : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 所受伤害减少率 (魔法) : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)


# 罪业加身
# priest_female/mistress/f2fb27162beb0b87a7cb9af7900e95f2
# 0c1b401bb09241570d364420b3ba3fd7/f2fb27162beb0b87a7cb9af7900e95f2
class Skill11(ActiveSkill):
    """
        向前方发出蕴含原罪之力的冲击波攻击。\n
        在[七宗罪]增益效果状态下攻击成功时， 恢复生命值和魔法值， 并使敌人进入强制控制状态。\n
        [我甘愿承担这些罪业。]
    """
    name = "罪业加身"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 6
    mp = [30, 252]
    uuid = "f2fb27162beb0b87a7cb9af7900e95f2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 冲击波攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)


# 冲刺斩
# priest_female/mistress/01c3a2fb793d293a25ed8dc7a0d70c1a
# 0c1b401bb09241570d364420b3ba3fd7/01c3a2fb793d293a25ed8dc7a0d70c1a
class Skill15(ActiveSkill):
    """
        施放技能时， 会向前方冲刺。 冲刺过程中， 按Z键或X键， 会向前方进行上斩攻击。\n
        转职成为除恶者时， 增加1次连续冲刺次数； 转职成为驱魔师时， 无法使用该技能。\n
        冲刺过程中， 再次按技能键可以连续冲刺， 可以利用按后方向键控制移动方向。\n
        学习[原罪之初]后， 施放时获得霸体护甲， 2次前冲后再次按技能键， 变身为恶魔发动前冲斩。\n
        按住向后方向键并再次按技能键， 可以向后转身发动前冲斩； 前冲斩击攻击力和[冲刺斩]的上斩攻击力相同。
    """
    name = "冲刺斩"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 6
    mp = [12, 500]
    uuid = "01c3a2fb793d293a25ed8dc7a0d70c1a"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 上斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 可冲刺次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 转职成为除恶者时， 可冲刺次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 双重切割
# priest_female/mistress/28b583c75a49103a1d8aabf799c000a4
# 0c1b401bb09241570d364420b3ba3fd7/28b583c75a49103a1d8aabf799c000a4
class Skill16(ActiveSkill):
    """
        第一击斩击中端， 第二击斩击下端。\n
        按前进键时， 施放第一击时， 向前移动。\n
        [原罪释放·净化]状态下施放时， 一次性造成2次攻击。
    """
    name = "双重切割"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 6
    mp = [12, 120]
    uuid = "28b583c75a49103a1d8aabf799c000a4"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 罪业诱惑
# priest_female/mistress/c77a417c43de80c4ce32c1ed405d174a
# 0c1b401bb09241570d364420b3ba3fd7/c77a417c43de80c4ce32c1ed405d174a
class Skill17(PassiveSkill):
    """
        掌握该技能后， 基本攻击变为除恶者专属攻击方式， 增加基本攻击力和技能攻击力。\n
        背负着原罪的肉身会不断引诱周围的敌人； 被引诱的敌人会降低命中率， 并向除恶者靠拢。\n
        利用诱惑来聚拢敌人的效果可以在已学技能栏中用鼠标右键设置开启/关闭\n
        减少命中率的技能效果叠加时， 只适用数值最高的效果。
    """
    name = "罪业诱惑"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 2
    rangeLv = 3
    uuid = "c77a417c43de80c4ce32c1ed405d174a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 敌人的命中率减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"data":data0}]

# 负罪者镰刀精通
# priest_female/mistress/ecc23c980ea71450c0ad0c3fd232f329
# 0c1b401bb09241570d364420b3ba3fd7/ecc23c980ea71450c0ad0c3fd232f329
class Skill18(PassiveSkill):
    """
        掌握该技能后， 增加魔法攻击力。\n
        使用镰刀系列武器攻击敌人时， 增加攻击速度、 移动速度和命中率； 且在施放镰刀系列技能后， 可以取消技能僵直， 强制使用其他镰刀系列技能。\n
    - [可以强制使用的技能] -\n
    [钩颈斩]、 [罪业加身]、 [双重切割]、 [冲刺斩]、 [镰勾旋击]、 [粉碎回旋击]、 [终结战镰]
    """
    name = "负罪者镰刀精通"
    learnLv = 15
    masterLv = 20
    maxLv = 30
    position = 1
    rangeLv = 3
    uuid = "ecc23c980ea71450c0ad0c3fd232f329"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 魔法攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [装备镰刀时]
    # 攻击速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 移动速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 命中率增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    associate = [{"type":"$*PAtkM","data":data0}]

# 镰勾旋击
# priest_female/mistress/f0cc2c950f3bdf4103c75fa496bcac34
# 0c1b401bb09241570d364420b3ba3fd7/f0cc2c950f3bdf4103c75fa496bcac34
class Skill19(ActiveSkill):
    """
        向前方发出斩击， 镰刀勾住敌人后， 跳到被勾住的敌人身上， 再施放旋转斩击。\n
        向前斩击命中时进入无敌状态， 被镰刀勾住的敌人会被强制控制。
    """
    name = "镰勾旋击"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 8
    mp = [65, 616]
    uuid = "f0cc2c950f3bdf4103c75fa496bcac34"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 向前斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 旋转斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 旋转斩击后的无敌时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 欲望之手
# priest_female/mistress/147d005ac868e0de52b1f255eea35d62
# 0c1b401bb09241570d364420b3ba3fd7/147d005ac868e0de52b1f255eea35d62
class Skill20(ActiveSkill):
    """
        施放时， 变身为恶魔向前方伸出指甲刺穿敌人后， 快速靠近僵直的敌人， 用镰刀划伤。\n
        消耗罪业层数时， 增加技能攻击力和移动速度， 效果持续一段时间。\n
        [人类的欲望本身并不是一种罪， 但沉醉于无节制的享乐， 便构成淫乐之罪。]
    """
    name = "欲望之手"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 8
    mp = [65, 616]
    uuid = "147d005ac868e0de52b1f255eea35d62"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 刺击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 上斩攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 七宗罪
# priest_female/mistress/0b8db1e10b3abbd24d38564e708675d5
# 0c1b401bb09241570d364420b3ba3fd7/0b8db1e10b3abbd24d38564e708675d5
class Skill21(ActiveSkill):
    """
        积累[七宗罪]，对自身使用各种增益/减益效果， 消耗罪业叠加层数强化部分技能。\n
    [增益效果]\n
        攻击时造成附加伤害， 有一定几率获得罪业层数。\n
        [罪业加身]技能攻击时， 恢复生命值和魔法值， 增加[罪业诱惑]技能引诱敌人的范围。\n
    [减益效果]\n
        施放时， 减少整体生命值和魔法值、 攻击速度、 移动速度、 命中率、 回避率、 属性抗性。\n
    [消耗罪业层数时的效果]\n
    - 通用 : 增加技能攻击力\n
    - [欲望之手] : 增加移动速度\n
    - [傲慢之堕] : 减少敌人回避率\n
    - [怠惰之息] : 使敌人进入减速状态\n
    - [贪婪之刺] : 增加攻击范围\n
    - [愤怒之袭] : 增加攻击速度\n
    - [嫉妒之吻] : 增加魅惑时间\n
    - [暴食之噬] : 增加生命值恢复量
    """
    name = "七宗罪"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 4
    rangeLv = 3
    cd = 5
    uuid = "0b8db1e10b3abbd24d38564e708675d5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [增益效果]
    # 攻击时附加伤害比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击时， 获得1层罪业的几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 罪业层数叠加冷却时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 罪业层数叠加次数上限 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [罪业加身] - 强制控制持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [罪业加身] - 命中时生命值和魔法值恢复量 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [罪业诱惑] - 诱敌范围增加率: {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [自身减益效果]
    # 施放时整体生命值和魔法值减少率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 攻击速度和移动速度减少 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 命中率和回避率减少 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 属性抗性减少 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # [消耗罪业层数时获得效果]
    # [通用] - 技能攻击力增加率 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # [欲望之手] - 罪业层数消耗量 : {value13}
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # [欲望之手] - 移动速度增加 : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # [欲望之手] - 效果持续时间 : {value15}秒
    data15 = get_data(f'{prefix}/{uuid}', 15)
    # [傲慢之堕] = 罪业层数消耗量 : {value16}
    data16 = get_data(f'{prefix}/{uuid}', 16)
    # [傲慢之堕] = 敌人回避率减少 : {value17}%
    data17 = get_data(f'{prefix}/{uuid}', 17)
    # [傲慢之堕] = 效果持续时间 : {value18}秒
    data18 = get_data(f'{prefix}/{uuid}', 18)
    # [怠惰之息] - 罪业层数消耗量 : {value19}
    data19 = get_data(f'{prefix}/{uuid}', 19)
    # [怠惰之息] - 敌人减速状态几率 : {value20}%
    data20 = get_data(f'{prefix}/{uuid}', 20)
    # [怠惰之息] - 敌人减速状态速度减少 : {value21}%
    data21 = get_data(f'{prefix}/{uuid}', 21)
    # [怠惰之息] - 效果持续时间 : {value22}秒
    data22 = get_data(f'{prefix}/{uuid}', 22)
    # [贪婪之刺] - 罪业层数消耗量 : {value23}
    data23 = get_data(f'{prefix}/{uuid}', 23)
    # [贪婪之刺] - 攻击范围增加率 : {value24}%
    data24 = get_data(f'{prefix}/{uuid}', 24)
    # [愤怒之袭] - 罪业层数消耗量 : {value25}
    data25 = get_data(f'{prefix}/{uuid}', 25)
    # [愤怒之袭] - 攻击速度增加: {value26}%
    data26 = get_data(f'{prefix}/{uuid}', 26)
    # [愤怒之袭] - 效果持续时间 : {value27}秒
    data27 = get_data(f'{prefix}/{uuid}', 27)
    # [嫉妒之吻] - 罪业层数消耗量 : {value28}
    data28 = get_data(f'{prefix}/{uuid}', 28)
    # [嫉妒之吻] - 魅惑时间增加率: {value29}%
    data29 = get_data(f'{prefix}/{uuid}', 29)
    # [暴食之噬] - 罪业层数消耗量: {value30}
    data30 = get_data(f'{prefix}/{uuid}', 30)
    # [暴食之噬] - 生命值恢复量增加率 : {value31}%
    data31 = get_data(f'{prefix}/{uuid}', 31)

    associate = [
        {"data":data12,"skills":['欲望之手', '傲慢之堕', '怠惰之息', '贪婪之刺', '愤怒之袭', '嫉妒之吻', '暴食之噬']}
    ]

# 傲慢之堕
# priest_female/mistress/47bd4871f29defc2a0021ee9261d7a5b
# 0c1b401bb09241570d364420b3ba3fd7/47bd4871f29defc2a0021ee9261d7a5b
class Skill23(ActiveSkill):
    """
        变成恶魔快速跃向空中后， 俯冲并发射强烈的冲击波。\n
        消耗罪业层数时， 增加技能攻击力； 减少敌人回避率， 效果持续一定时间。\n
        施放技能时， 可用方向键调整俯冲位置， 可以在空中使用。\n
        在决斗场中， 无法沿Y轴移动， 并且无法在一定高度以上施放。\n
        [傲慢滋生出原罪， 原罪又助长其他罪业， 所以， 傲慢才是万恶之源。]
    """
    name = "傲慢之堕"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 3
    cd = 10
    mp = [65, 630]
    uuid = "47bd4871f29defc2a0021ee9261d7a5b"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 冲击波攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 粉碎回旋击
# priest_female/mistress/669f1428193f61f9d92c743b72438c4d
# 0c1b401bb09241570d364420b3ba3fd7/669f1428193f61f9d92c743b72438c4d
class Skill24(ActiveSkill):
    """
        跳向前方， 旋转身体对敌人造成多段伤害后， 落地并发动最后一击。\n
        施放时， 按向前方向键可以跳得更远， 可以在空中施放。\n
        在决斗场中， 无法在空中施放。
    """
    name = "粉碎回旋击"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 12
    mp = [47, 700]
    uuid = "669f1428193f61f9d92c743b72438c4d"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 多段旋转攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 多段旋转次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 怠惰之息
# priest_female/mistress/8510294202d0e042dd29a2422fc6770d
# 0c1b401bb09241570d364420b3ba3fd7/8510294202d0e042dd29a2422fc6770d
class Skill25(ActiveSkill):
    """
        变身为恶魔， 强化身体， 一定时间内防御异常状态和敌人的攻击。\n
        防御时再次按技能键或Z键， 会向前方发出强力的刺击。\n
        消耗罪业层数时， 增加技能攻击力， 使命中的敌人进入减速状态。\n
        在正确的时机精准防御敌人的攻击， 可以吸收全部伤害， 并发动破招冲击波， 使周围敌人进入眩晕状态。\n
        防御时可以吸附周围的敌人， 按跳跃键会立即解除防御状态。\n
        在决斗场中， 按跳跃键无法解除防御状态， 即使在正确的时机防御也不会完全吸收伤害。\n
        学习[原罪之初]后， 增加吸附敌人的范围和速度； 按向下方向键， 并再次按技能键或者<Z>键时， 在附近生成冲击波。 (冲击波攻击力与刺击相同)\n
        [检讨自己的人生并学会尊重自己时， 方能从怠惰的沼泽中挣脱出来……]
    """
    name = "怠惰之息"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cd = 15
    mp = [27, 308]
    uuid = "8510294202d0e042dd29a2422fc6770d"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 刺击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 普通防御持续期间的所有异常状态抗性增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 普通防御时， 所受伤害减少率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 精准防御时， 所受伤害减少率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 精准防御时， 冲击波攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 精准防御时， 冲击波眩晕几率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 精准防御时， 冲击波眩晕时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 范围比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

# 贪婪之刺
# priest_female/mistress/b3659936a9a74c4ed6f7faf07cca1f9e
# 0c1b401bb09241570d364420b3ba3fd7/b3659936a9a74c4ed6f7faf07cca1f9e
class Skill26(ActiveSkill):
    """
        变身为恶魔冲击地面， 向地面注入贪婪残影。\n
        用残影刺穿地面的敌人， 使敌人进入强制控制状态并造成多段伤害后吞噬掉。\n
        消耗罪业层数时， 增加技能攻击力和攻击范围。\n
        残影生成时， 吸附Y轴的敌人， 并使被残影穿刺的敌人进入无法抓取状态； 残影生成结束时， 再次按技能键可以立即吞噬敌人。\n
     [贪欲也就是‘过分的欲望’。 试图得到本不该属于自己的， 均属于贪欲……] 
    """
    name = "贪婪之刺"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [140, 1176]
    uuid = "b3659936a9a74c4ed6f7faf07cca1f9e"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 多段攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 9
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [贪婪之刺]\n
        可以在施放恶魔系技能过程中发动\n
        基本冷却时间变更为40秒\n
        吞噬效果强化， 残影生成结束后造成多段伤害\n
        - 残影持续时间 +1秒\n
        - 吞噬时造成多段伤害\n
        - 多段攻击次数上限 +9次\n
        - 总攻击力 +100%
        """
        self.skillRation *= 1 + 1
        self.cd = 40
        ...

    def vp_2(self):
        """
        [贪婪之刺]\n
        生成影子时， 将敌人拉向技能中心\n
        变更为影子在范围内最强敌人所处位置生成\n
        - 索敌范围 : 与[罪业诱惑]引诱范围相同\n
        - 范围内没有敌人时无法使用技能
        """
        ...

# 诱魔之手
# priest_female/mistress/3fb8395ae3b81bd608e0c4223a8eb534
# 0c1b401bb09241570d364420b3ba3fd7/3fb8395ae3b81bd608e0c4223a8eb534
class Skill27(ActiveSkill):
    """
        变身为恶魔发动攻击， 唤醒敌人内心堆积的罪业， 然后引爆罪业。\n
        爆炸攻击时， 可吸收敌人的罪业， 增加罪业层数。   
    """
    name = "诱魔之手"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [105, 882]
    uuid = "3fb8395ae3b81bd608e0c4223a8eb534"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 打击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 罪业层数增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [诱魔之手]\n
        未命中时， 冷却时间缩短为2秒\n
        [原罪释放·净化]\n
        恶魔状态下[诱魔之手]命中时， 适用以下效果\n
        - 变身持续时间 +12秒\n
        - 不超过变身持续时间上限
        """
        ...

    def vp_2(self):
        """
        [诱魔之手]\n
        攻击准备时间 -50%\n
        命中一定时间后自动发动爆炸攻击\n
        罪业层数增加量 +2\n
        [罪业加身]\n
        [诱魔之手]命中后自动施放该技能\n
        - 仅在[罪业加身]技能可施放状态下发动\n
        - 自动施放时[七宗罪]技能的[罪业加身]生命值和魔法值恢复效果额外 +7%
        """
        ...

# 终结战镰
# priest_female/mistress/38612d8f2561edc2eb68d5057a837bfa
# 0c1b401bb09241570d364420b3ba3fd7/38612d8f2561edc2eb68d5057a837bfa
class Skill28(ActiveSkill):
    """
        在原地旋转并挥舞镰刀乱击敌人后， 使用离心力攻击周围的敌人。\n
        旋转过程中可以利用方向键移动， 连按攻击键或技能快捷键可以增加乱击旋转速度， 旋转中可以利用跳跃键强制中断攻击。\n
        在决斗场中， 无法用跳跃键强制中断攻击。
    """
    name = "终结战镰"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [180, 1512]
    uuid = "38612d8f2561edc2eb68d5057a837bfa"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 斩击攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 9
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [终结战镰]\n
        - 旋转斩击攻击强化\n
        - 攻击范围 +70%\n
        - 多段斩击可以吸附敌人\n
        - 旋转次数 +9次\n
        - 总攻击力相同\n
        - 旋转过程中移动速度 +700%\n
        - 旋转过程中连按攻击键或技能快捷键时， 不会增加旋转速度
        """
        ...

    def vp_2(self):
        """
        [终结战镰]\n
        强制中断镰刀系列技能的施放后僵直立即施放时， 适用以下效果: \n
        - 省略准备动作\n
        - 多段攻击次数 -3次\n
        - 总攻击力相同\n
        [粉碎回旋击]\n
        强制中断镰刀系列技能的施放后僵直立即施放时， 适用以下效果: \n
        - 施放过程中减少前进距离\n
        - 省略准备动作\n
        - 旋转多段攻击次数 -2次\n
        - 总攻击力相同
        """
        ...

# 愤怒之袭
# priest_female/mistress/6a1d1f08a6572be420bb3a256c44c015
# 0c1b401bb09241570d364420b3ba3fd7/6a1d1f08a6572be420bb3a256c44c015
class Skill29(ActiveSkill):
    """
        变身为恶魔， 用爆发性的力量和速度掠过敌人， 给敌人造成伤害。\n
        消耗罪业层数时， 增加技能攻击力； 增加攻击速度， 效果持续一定时间。\n
        施放时， 按前进键可以移动更远距离。\n
        [和平的另一面并不是战争。 也许， 压抑住愤怒， 人类才会迎来真正的和平。]
    """
    name = "愤怒之袭"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [400, 3360]
    uuid = "6a1d1f08a6572be420bb3a256c44c015"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [愤怒之袭]\n
        移动功能强化\n
        - 斩击时可以沿Y轴移动\n
        - 可以在175px以下的空中施放\n
        - 前进距离 +30%\n
        攻击范围 +30%\n
        施放过程中， 再次按技能键可以追击瞬间斩击命中的敌人
        """
        ...

    def vp_2(self):
        """
        [愤怒之袭]\n
        当罪业层数在3层以上时施放， 消耗所有罪业层数\n
        [七宗罪]\n
        强化[愤怒之袭]消耗罪业层数时的效果\n
        (根据消耗的层数， 增加攻击速度增加率和持续时间)\n
        - 消耗4层 : +17%\n
        - 消耗5层 : +37%\n
        - 消耗6层 : +57%\n
        - 消耗7层 : +77%\n
        [傲慢之堕]\n
        可以在[愤怒之袭]施放过程中施放， 此时适用以下效果\n
        - 在[愤怒之袭]技能路径上生成冲击波\n
        - 不消耗罪业层数\n
        - 消耗罪业层数时适用效果
        """
        ...

# 罪业宣告
# priest_female/mistress/852f8ad797db4dca1405cb3e77198401
# 0c1b401bb09241570d364420b3ba3fd7/852f8ad797db4dca1405cb3e77198401
class Skill30(PassiveSkill):
    """
        可以强制中断转职技能的施放后僵直并施放； 攻击时， 增加暴击伤害和魔法暴击率， 效果持续一定时间。\n
        在决斗场中， 不适用强制中断功能。\n
        [恬不知耻的恶魔啊！ 神会将你们的罪业宣之于众！]
    """
    name = "罪业宣告"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 3
    uuid = "852f8ad797db4dca1405cb3e77198401"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 暴击伤害增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 魔法暴击率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [{"data":data1}]

# 原罪释放·净化
# priest_female/mistress/a2d943797daca862a6f321aca6ac9bfa
# 0c1b401bb09241570d364420b3ba3fd7/a2d943797daca862a6f321aca6ac9bfa
class Skill31(ActiveSkill):
    """
        变身为实体化的原罪， 效果持续一定时间。\n
        如果在施放恶魔系技能的过程中使用[原罪释放·净化]， 可以立即变身。\n
        变身持续时间内拥有霸体效果， 增加攻击速度、 移动速度、 防御力、 生命值魔法值恢复力、 控制型异常状态抗性。\n
        变身持续时间内， 变更基本攻击和镰刀系技能， 并且无法使用部分技能。\n
    无法使用的技能] : [空中锤击]、 [治愈祈祷]、 [审判锤击]、 [武器格挡]、 [净化]、 [唤雷符]
    """
    name = "原罪释放·净化"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 5
    cube = 7
    cd = 140
    mp = [1500, 12600]
    uuid = "a2d943797daca862a6f321aca6ac9bfa"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 变身持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [变身时附加效果]
    # 攻击速度和移动速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 防御力增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 生命值/魔法值恢复量增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 控制型异常状态抗性增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 净化之花
# priest_female/mistress/9dc8438e4572d39243c97da31c113acc
# 0c1b401bb09241570d364420b3ba3fd7/9dc8438e4572d39243c97da31c113acc
class Skill32(ActiveSkill):
    """
        变身为恶魔，向最强的敌人绽放净化之花， 造成多段伤害并强控敌人后， 净化之花会发生爆炸。\n
        学习后， 技能等级补正为与[原罪释放·净化]相同。
    """
    name = "净化之花"
    learnLv = 50
    masterLv = 1
    maxLv = 50
    position = 4
    rangeLv = 5
    cd = 140
    mp = [1500, 3500]
    uuid = "9dc8438e4572d39243c97da31c113acc"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 15
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

    def skillInfo(self, mode: str | None = None):
        self.lv = self.char.GetSkillByName("原罪释放·净化").lv
        return super().skillInfo(mode)

# 嫉妒之吻
# priest_female/mistress/c7bf7ccab413009640e65ca6f2f0263a
# 0c1b401bb09241570d364420b3ba3fd7/c7bf7ccab413009640e65ca6f2f0263a
class Skill33(ActiveSkill):
    """
        变身为恶魔， 散发魅惑气息， 被魅惑气息命中的敌人会僵直并进入魅惑状态， 效果持续一定时间。\n
        若存在被魅惑气息命中的敌人， 再次按技能键， 可以移动到敌人身后发动斩击。\n
        消耗罪业层数时， 增加技能攻击力和魅惑时间。\n
        若敌人未被魅惑， 会在一定时间内对敌人附加印记。 此时， 再次按技能键， 可以移动到被附加印记或被魅惑的敌人身后， 将其撕裂。\n
        [妒忌是未拥有者对拥有者的羡慕， 嫉妒是拥有者对失去的恐惧。]
    """
    name = "嫉妒之吻"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [400, 1120]
    uuid = "c7bf7ccab413009640e65ca6f2f0263a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 控制持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魅惑持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 斩击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [嫉妒之吻]\n
        魅惑气息移动功能强化\n
        - 追踪前方的敌人\n
        - 移动速度 +30%\n
        魅惑效果强化\n
        - 最后一击可发动距离 +80%\n
        - 敌人僵直时间 +100%\n
        - 魅惑时间 +60%\n
        - 魅惑气息命中时， 魅惑时间内所受伤害 -20%
        """
        ...

    def vp_2(self):
        """
        [嫉妒之吻]\n
        施放时， 使周围的所有敌人陷入魅惑\n
        - 魅惑范围 : 与[罪业诱惑]诱惑范围相同\n
        - 范围内没有敌人时无法使用\n
        - 再次按技能键时， 引爆魅惑\n
        - 总攻击力相同\n
        [罪业诱惑]\n
        诱惑范围 +20%
        """
        ...

# 暴食之噬
# priest_female/mistress/1b1cfab062e0768bcc889e33e1f30dbf
# 0c1b401bb09241570d364420b3ba3fd7/1b1cfab062e0768bcc889e33e1f30dbf
class Skill34(ActiveSkill):
    """
        唤醒暴食之原罪， 吸附前方的敌人后， 向前方释放吸收到的能量。\n
        消耗罪业层数时， 增加技能攻击力和生命值恢复量。\n
        可以通过按住技能键， 增加吸收能量的时间。 吸收成功时， 可以恢复自身的生命值并增加罪业层数。\n
        [减少自己的粮食， 进而禁食， 将那些粮食分给穷苦的人们， 此为积德之行为。]
    """
    name = "暴食之噬"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [800, 1680]
    uuid = "1b1cfab062e0768bcc889e33e1f30dbf"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 吸收时， 多段攻击力 : {value0}% X {value1}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 每吸收1次， 生命值恢复率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 每次吸收攻击时罪业层数增加量 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 吸收蓄气时间上限 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 最后一击多段攻击力 : {value5}% X {value6}次
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 4
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 范围比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    def vp_1(self):
        """
        [暴食之噬]\n
        攻击范围 +30%\n
        吸收攻击强化\n
        - 吸附力 +30%\n
        - 生命值恢复量 +30%\n
        - 每次攻击罪业层数增加量 +1
        """
        ...

    def vp_2(self):
        """
        [暴食之噬]\n
        对周围范围内的敌人进行攻击\n
        [七宗罪]\n
        消耗罪业层数时， 分身代替施放
        """
        ...

# 智慧起源 : 原罪结晶
# priest_female/mistress/e5c09f9132a48dc1d695968592cc5878
# 0c1b401bb09241570d364420b3ba3fd7/e5c09f9132a48dc1d695968592cc5878
class Skill35(ActiveSkill):
    """
        领悟宇宙初始的智慧， 增加基本攻击力和技能攻击力， 并增加[原罪释放·净化]变身时间， 魔化状态下攻击时， 对周围进行光环攻击。\n
        而且， 在原罪的影响下， 叠加的罪业数量不会降到1以下， 获得罪业层数时减少[原罪释放·净化]冷却时间。\n
        在人类形态下使用恶魔系技能命中目标时， [罪业诱惑]的光环散发紫色光辉， 对范围内所有的敌人造成伤害， [原罪释放·净化]变身状态下所有攻击发动光环光辉攻击。\n
        [传说中诞下所有人类罪业的禁断结晶……原罪、 苹果、 禁断之果、 普拉那， 无数词语在描述这个东西。]
    """
    name = "智慧起源 : 原罪结晶"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 3
    uuid = "e5c09f9132a48dc1d695968592cc5878"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    type = "passive"
    cd = 2

    # 基本攻击力和技能攻击力增加量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 光环光辉攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 光辉冷却时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [原罪释放·净化]变身时间增加 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [获得罪业层数时]
    # [原罪释放·净化]冷却时间减少 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [原罪释放·净化]冷却时间最大减少 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)

    associate = [{"data":data0}]

    def getSkillCD(self, mode=None):
        return 2.0

# 灵魂烙印 : 原罪冲击
# priest_female/mistress/e0daa922b19cdc35de879e938361464e
# 0c1b401bb09241570d364420b3ba3fd7/e0daa922b19cdc35de879e938361464e
class Skill36(ActiveSkill):
    """
        用镰刀把周围敌人驱赶到一处， 然后断开原罪印章， 高高跳跃后落到地面， 引起强烈的爆炸。\n
        原罪爆炸攻击时， 吸收原罪并增加罪业层数。\n
        [人类无法隔断原罪？ 是因为人类从原罪诞生？ 还是因为人因原罪才能称为人。]
    """
    name = "灵魂烙印 : 原罪冲击"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "e0daa922b19cdc35de879e938361464e"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 驱赶攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 原罪爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 原罪爆炸攻击时罪业层数增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [灵魂烙印 : 原罪冲击]\n
        施放时立即发动驱赶敌人攻击\n
        终结原罪爆炸攻击变更为原地下劈动作\n
        攻击范围 +50%
        """
        ...

    def vp_2(self):
        """
        [灵魂烙印 : 原罪冲击]\n
        施放时， 变身为恶魔后将罪业附于武器， 向前方砸击\n
        - 向前方砸击时引发原罪爆炸\n
        - 总攻击力相同\n
        变更为消耗3个罪业层数的技能， 消耗罪业层数时， 适用以下效果\n
        - 施放技能时进入无敌状态\n
        - 移动速度增加17%， 效果持续17秒
        """
        ...

# 肋骨重塑 : 原罪战矛
# priest_female/mistress/0fbb8de70002ad34f046c94c2cb3e863
# 0c1b401bb09241570d364420b3ba3fd7/0fbb8de70002ad34f046c94c2cb3e863
class Skill37(ActiveSkill):
    """
        把刻在后背的原罪烙印具现化为7根骨刺刺向前方， 随后触手散开刺向敌人。\n
        刺击时， 进入无敌状态； 吸附刺击命中的敌人并使其进入强制控制状态。\n
        [今天仍没有领悟到自己罪孽的人们……唯有与神相连的证据才能拯救他们。]
    """
    name = "肋骨重塑 : 原罪战矛"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "0fbb8de70002ad34f046c94c2cb3e863"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 刺击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 触手散开斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 3
    # [范围信息]
    # 范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [肋骨重塑 : 原罪战矛]\n
         施放时， 立即进入无敌状态\n
        刺击持续时间 +1秒\n
        再次按技能键时， 可立即发动终结攻击\n
        最后一击触手散开施放速度 +25%
        """
        ...

    def vp_2(self):
        """
        [肋骨重塑 : 原罪战矛]\n
        将原罪烙印向地面广泛扩散， 用7根尖刺刺向天空后撕裂\n
        [七宗罪]\n
        [肋骨重塑 : 原罪战矛]的终结攻击触手散开攻击命中时， 吸收敌人的原罪， 适用以下效果\n
        - 7秒内罪业层数不会下降到7以下
        """
        ...

# 失乐园
# priest_female/mistress/c5a2956d8ed3af1746ed2f76ca971a09
# 0c1b401bb09241570d364420b3ba3fd7/c5a2956d8ed3af1746ed2f76ca971a09
class Skill38(ActiveSkill):
    """
        提取禁忌之力移动到最强大的敌人面前， 转嫁罪业后使敌人爆炸。\n
        周围存在敌人时才可以施放， 提取禁忌之力的瞬间， 罪业层数达到最大值， 转嫁给敌人后罪业层数减少到最小值。\n
        [湮灭， 之后将有乐园降临。 神啊， 求您把悔改的灵魂们带到乐园……]
    """
    name = "失乐园"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [1500, 5000]
    uuid = "c5a2956d8ed3af1746ed2f76ca971a09"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 罪业转嫁攻击力 : {value0}% X {value1}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 7
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 禁忌之力爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

# 原罪之初
# priest_female/mistress/0113c8b1306ca76d208f83f2d093dd62
# 0c1b401bb09241570d364420b3ba3fd7/0113c8b1306ca76d208f83f2d093dd62
class Skill39(PassiveSkill):
    """
        除恶者超越人类可以背负的原罪限界， 可以使用更加强大的原罪之力。\n
        学习后， 增加基本攻击力和转职技能攻击力， 部分技能附加特殊效果。\n
    [冲刺斩]\n
        施放时获得霸体护甲， 2次前冲后再次按技能键， 变身为恶魔发动前冲斩。\n
        按住向后方向键并再次按技能键， 可以向后转身发动前冲斩。 前冲斩击攻击力和[冲刺斩]的上斩攻击力相同。\n
    [怠惰之息]\n
        增加聚拢敌人的范围和速度， 按下方向键并再次按技能键或Z键时， 向周围发动冲击波攻击。 (冲击波攻击力和[怠惰之息]的突刺攻击力相同)\n
        [我们只能背负原罪而生吗？ 所有原罪之初， 如果我们能领悟其本质……]
    """
    name = "原罪之初"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "0113c8b1306ca76d208f83f2d093dd62"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [怠惰之息] - 聚拢敌人速度和范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"data":data0}]

# 至高之刑
# priest_female/mistress/8b08f9504167a9c0f3a1d29d71b7943e
# 0c1b401bb09241570d364420b3ba3fd7/8b08f9504167a9c0f3a1d29d71b7943e
class Skill40(ActiveSkill):
    """
        变身为恶魔， 用铭刻七宗罪之力的镰刀审判敌人。 共进行7次审判， 令敌人赎罪。 \n
        施放中连按攻击键或技能快捷键， 可增加攻击速度。 \n
        [愚蠢之人， 珍惜赐予你救赎的机会， 虔诚地忏悔吧。]
    """
    name = "至高之刑"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [1066, 8000]
    uuid = "8b08f9504167a9c0f3a1d29d71b7943e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 多段斩击攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 6
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 终结斩击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

# 原罪之翼·永息
# priest_female/mistress/ac21c02567f04a92b54dd85c091d1e5a
# 0c1b401bb09241570d364420b3ba3fd7/ac21c02567f04a92b54dd85c091d1e5a
class Skill41(ActiveSkill):
    """
        除恶者将敌人引诱到原罪之沼， 用沉重的罪业碾压并强控敌人， 然后吸收周围的一切罪业。\n
        超越原罪限界的除恶者维持着神圣性， 将背负所有原罪化为羽翼和尾巴的形态。 由无数原罪结晶体构成的羽翼和尾巴覆盖整个世界， 赦免背负的原罪， 引导所有人进入永远的安息。\n
        吸收周围的罪业时， 罪业层数增加到最大值。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。\n
        [神啊……所有的罪业都由我来背负。 请赦免他们的罪业， 允许他们永恒地安息吧……]
    """
    name = "原罪之翼·永息"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "ac21c02567f04a92b54dd85c091d1e5a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'mistress'
        self.nameCN = '神启·诱魔者'
        self.role = 'priest_female'
        self.角色 = '圣职者(女)'
        self.职业 = '诱魔者'
        self.jobId = '0c1b401bb09241570d364420b3ba3fd7'
        self.jobGrowId = 'c9b492038ee3ca8d27d7004cf58d59f3'

        self.武器选项 = ['光杖','念珠','图腾','镰刀','战斧']
        self.输出类型选项 = ['魔法百分比']
        self.输出类型 = '魔法百分比'
        self.防具精通属性 = ['智力']
        self.防具类型 = '重甲'
        self.buff = 1.947

        super().__init__(equVersion, __name__)
