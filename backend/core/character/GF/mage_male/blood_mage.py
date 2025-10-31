#a5ccbaf5538981c6ef99b236c0a60b73
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "mage_male/blood_mage/cn/skillDetail"

# 魔法旋风
# mage_male/blood_mage/3c5604bdbb0240b8f130f59ab40509c3
# a5ccbaf5538981c6ef99b236c0a60b73/3c5604bdbb0240b8f130f59ab40509c3
class Skill0(ActiveSkill):
    """
    向敌人发出无属性旋风并使其浮空。\n
    转职为次元行者后， 技能类型变为独立攻击力。\n
    - [转职为猩红法师时附加效果] -\n
    外形发生变化， 可以吸收猩红气息。\n
    - [转职为逐风者时附加效果] -\n
    增加攻击力， 可以按<X>键进行追加操作。
    """
    name = "魔法旋风"
    learnLv = 1
    masterLv = 10
    maxLv = 20
    position = 4 #TODO
    rangeLv = 3
    cd = 2
    uuid = "3c5604bdbb0240b8f130f59ab40509c3"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 浮空力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # - [转职为猩红法师后] -
    # 猩红气息吸收率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # - [转职为逐风者后] -
    # 攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 魔法冰球
# mage_male/blood_mage/5dc7008b12a459325b548b0715c6b73c
# a5ccbaf5538981c6ef99b236c0a60b73/5dc7008b12a459325b548b0715c6b73c
class Skill1(ActiveSkill):
    """
    向前方发射魔法冰球。\n
    在决斗场内， 冰球大小随技能等级增加而增大。
    """
    name = "魔法冰球"
    learnLv = 1
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cd = 2
    mp = [10, 84]
    uuid = "5dc7008b12a459325b548b0715c6b73c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冰球大小 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 不死之身
# mage_male/blood_mage/bb34e8854a93fd250347a1c64119f7ab
# a5ccbaf5538981c6ef99b236c0a60b73/bb34e8854a93fd250347a1c64119f7ab
class Skill2(PassiveSkill):
    """
    角色死亡后带着少量生命值原地复活， 并且进入自动恢复生命值模式。\n
    自动恢复生命值模式下， 角色的生命值值可以在一定时间内自动恢复至100%， 但无法借用任何道具或其它途径恢复生命值， 且所受到的伤害还会加剧。\n
    若在恢复模式下死亡， 则无法再次通过该技能复活。
    """
    name = "不死之身"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 3
    uuid = "bb34e8854a93fd250347a1c64119f7ab"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 恢复模式下所受伤害增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 死亡时立即恢复的生命值量 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 恢复模式持续时间(普通地下城) : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 恢复模式持续时间(亡者峡谷) : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 黑暗之眼
# mage_male/blood_mage/6e33d47e6622ce03b6defdd912140270
# a5ccbaf5538981c6ef99b236c0a60b73/6e33d47e6622ce03b6defdd912140270
class Skill3(PassiveSkill):
    """
    增加魔法师的魔法值最大值； 若魔法值低于一定比率时， 还可增加魔法值恢复速度。
    """
    name = "黑暗之眼"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "6e33d47e6622ce03b6defdd912140270"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 魔法值最大值增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 可触发恢复效果时的魔法值比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 魔法值恢复速度增加 : {value2}倍
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 赤影步
# mage_male/blood_mage/ac21c02567f04a92b54dd85c091d1e5a
# a5ccbaf5538981c6ef99b236c0a60b73/ac21c02567f04a92b54dd85c091d1e5a
class Skill4(ActiveSkill):
    """
    快速移动到前方最远处敌人的身后。\n
    使用向前方向键时， 可移动到最大距离。\n
    在决斗场内， 无论前方有无敌人， 都会移动到最大距离。
    """
    name = "赤影步"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 6 #TODO
    rangeLv = 2
    cd = 1.5
    mp = [51, 51]
    uuid = "ac21c02567f04a92b54dd85c091d1e5a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 移动距离上限 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 敌人无法发觉的时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)


# 基础精通
# mage_male/blood_mage/5a56514f35cf0270ae8d6c65f8fefd78
# a5ccbaf5538981c6ef99b236c0a60b73/5a56514f35cf0270ae8d6c65f8fefd78
class Skill6(PassiveSkill):
    """
    增加基本攻击、 前冲攻击、 跳跃攻击、 [魔法旋风]的攻击力。\n
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


# 幽冥火
# mage_male/blood_mage/cfacda0647b9a0f595df2c2aad30c18d
# a5ccbaf5538981c6ef99b236c0a60b73/cfacda0647b9a0f595df2c2aad30c18d
class Skill11(ActiveSkill):
    """
    生成两团幽冥火， 可以增加自身的物理和魔法防御力， 且造成一定伤害， 效果持续一定时间。\n
    转职成次元行者时， 可以学习[虚妄之火]技能。\n
    学习[虚妄之火]后， 持续时间变更为无限， 且无法发动攻击。
    """
    name = "幽冥火"
    learnLv = 10
    masterLv = 10
    maxLv = 20
    position = 9 #TODO
    rangeLv = 3
    cd = 10
    mp = [30, 345]
    uuid = "cfacda0647b9a0f595df2c2aad30c18d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 每个火球增加物理防御力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 每个火球增加魔法防御力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 每个火球的攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # - [虚妄之火效果] -
    # 物理防御力增加 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 魔法防御力增加 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 血蝠之袭
# mage_male/blood_mage/d429147c372b549c3dadcabcba50787f
# a5ccbaf5538981c6ef99b236c0a60b73/d429147c372b549c3dadcabcba50787f
class Skill16(ActiveSkill):
    """
    召唤蝙蝠冲向敌人造成多段伤害并吸取猩红气息。
    """
    name = "血蝠之袭"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 5
    mp = [24, 240]
    uuid = "d429147c372b549c3dadcabcba50787f"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 15
    # 多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 猩红气息吸收量 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 鲜血融合
# mage_male/blood_mage/0113c8b1306ca76d208f83f2d093dd62
# a5ccbaf5538981c6ef99b236c0a60b73/0113c8b1306ca76d208f83f2d093dd62
class Skill17(PassiveSkill):
    """
    从攻击的敌人身上吸取力量， 与黑暗之眼进行融合， 产生新的力量之源——猩红气息。 猩红法师的命中率因猩红探测能力而增加。\n
    当猩红气息蓄满时， 角色会进入一种兴奋状态， 增加物理武器攻击力、 减少猩红气息消耗系技能的冷却时间。\n
    猩红气息可以用吸收系技能吸收， 并在吸收状态下， 减少猩红气息消耗系技能的消耗量。\n
    猩红气息不足时， 可以消耗生命值施放猩红气息消耗系技能。
    """
    name = "鲜血融合"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    uuid = "0113c8b1306ca76d208f83f2d093dd62"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # [学习技能时效果]
    # 命中率增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 吸收状态持续时间增加 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [猩红气息高涨状态]
    # 物理武器攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 猩红气息消耗系技能冷却时间减少率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [猩红气息吸收状态下]消耗系技能附加效果
    # 猩红气息消耗量减少率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [猩红气息不足时]
    # 消耗生命值比率 : 猩红气息消耗量的{value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    associate = [
        {"data":data2,"type":"$*PAtkP"},
        {"data":data3,"type":"*cdReduce","skills":["血翼突击","鲜血长枪","猩红狩猎","狱血之牙","绯红之狱","隐行之噬","血翼绽放","死亡之握","血翼蔽空"]}
        ]

# 鲜血之誓
# mage_male/blood_mage/8b08f9504167a9c0f3a1d29d71b7943e
# a5ccbaf5538981c6ef99b236c0a60b73/8b08f9504167a9c0f3a1d29d71b7943e
class Skill18(PassiveSkill):
    """
    将穿戴的武器和猩红气息融合到一起， 像身体的一部分一样操控自如。\n
    改变基本攻击、 冲刺攻击、 跳跃攻击、 [魔法旋风]的攻击效果； 攻击时敌人时， 可以吸收猩红气息。
    """
    name = "鲜血之誓"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 8 #TODO
    rangeLv = 2
    uuid = "8b08f9504167a9c0f3a1d29d71b7943e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 第1击猩红气息吸收量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 第2击猩红气息吸收量 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 第3击猩红气息吸收量 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 第4击猩红气息吸收量 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 冲刺攻击猩红气息吸收量 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 跳跃攻击猩红气息吸收量 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 血翼突击
# mage_male/blood_mage/ab6fc3303df03b58911967dfca2b5d07
# a5ccbaf5538981c6ef99b236c0a60b73/ab6fc3303df03b58911967dfca2b5d07
class Skill19(ActiveSkill):
    """
    消耗猩红气息， 将双臂变形为翅膀形状的利刃， 冲向前方的敌人。\n
    该技能可以击退敌人。\n
    可以在空中施放该技能， 利用方向键可以指定降落地点。
    """
    name = "血翼突击"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 5
    uuid = "ab6fc3303df03b58911967dfca2b5d07"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 猩红气息消耗量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 自身冲撞攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 血翼斩击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 鲜血长枪
# mage_male/blood_mage/002cbdd9bfd0f0b970451ae8d48d029e
# a5ccbaf5538981c6ef99b236c0a60b73/002cbdd9bfd0f0b970451ae8d48d029e
class Skill20(ActiveSkill):
    """
    用猩红气息之枪刺穿敌人后举起。\n
    举起状态可以持续一定时间， 若再按下技能键， 则把敌人砸向地面。\n
    对无法抓取的敌人不适用抓取和控制效果。
    """
    name = "鲜血长枪"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 6
    uuid = "002cbdd9bfd0f0b970451ae8d48d029e"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 猩红气息消耗量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 刺击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 举起状态持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 砸向地面攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hie3 = 1
    # 对无法抓取的敌人攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 攻击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 血之共鸣
# mage_male/blood_mage/95b58ec89893dd9e50da1281ebe57175
# a5ccbaf5538981c6ef99b236c0a60b73/95b58ec89893dd9e50da1281ebe57175
class Skill22(PassiveSkill):
    """
    精通鲜血的力量并与之共鸣。
    """
    name = "血之共鸣"
    learnLv = 20
    masterLv = 1
    maxLv = 11
    position = 0 #TODO
    rangeLv = 3
    uuid = "95b58ec89893dd9e50da1281ebe57175"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]

# 血蝠之舞
# mage_male/blood_mage/c91a62dc0a18360acf5031ac0ebf09f5
# a5ccbaf5538981c6ef99b236c0a60b73/c91a62dc0a18360acf5031ac0ebf09f5
class Skill23(ActiveSkill):
    """
    召唤蝙蝠群， 使范围内的敌人受到多段伤害并吸取猩红气息。
    """
    name = "血蝠之舞"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 6
    mp = [80, 800]
    uuid = "c91a62dc0a18360acf5031ac0ebf09f5"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 51
    # 持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 猩红气息吸收量 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 猩红狩猎
# mage_male/blood_mage/0c3a468aee1f7ce06bf91eb3319518c1
# a5ccbaf5538981c6ef99b236c0a60b73/0c3a468aee1f7ce06bf91eb3319518c1
class Skill24(ActiveSkill):
    """
    在前方生成猩红之池， 从中射出针刺攻击敌人。\n
    施放时， 输入向下/后方向键时， 则针刺就会从背后攻击敌人。
    """
    name = "猩红狩猎"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 8
    uuid = "0c3a468aee1f7ce06bf91eb3319518c1"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 猩红气息消耗量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 针刺攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit0 = 5
    # 多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 赤红燃烧
# mage_male/blood_mage/5cac3411ccef1af333953e0ded5e942d
# a5ccbaf5538981c6ef99b236c0a60b73/5cac3411ccef1af333953e0ded5e942d
class Skill25(ActiveSkill):
    """
    增加攻击力。
    """
    name = "赤红燃烧"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 8 #TODO
    rangeLv = 3
    cd = 5
    uuid = "5cac3411ccef1af333953e0ded5e942d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 狱血之犬
# mage_male/blood_mage/85f7c810ad503790e8626439fe936d56
# a5ccbaf5538981c6ef99b236c0a60b73/85f7c810ad503790e8626439fe936d56
class Skill26(ActiveSkill):
    """
    利用猩红气息生成犬形怪物咬住敌人， 使其无法动弹， 然后撕咬敌人造成多段伤害并吸取猩红气息。\n
    施放时输入下方向键 ， 可以缩短犬形怪物的突进距离。
    """
    name = "狱血之犬"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 10
    mp = [112, 1120]
    uuid = "85f7c810ad503790e8626439fe936d56"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 物理攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 撕咬多段攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 13
    # 撕咬攻击持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 撕咬攻击多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 猩红气息吸收量 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 攻击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 狱血之牙
# mage_male/blood_mage/31823197cc0b04d4c5dcf8f928d9220c
# a5ccbaf5538981c6ef99b236c0a60b73/31823197cc0b04d4c5dcf8f928d9220c
class Skill27(ActiveSkill):
    """
    利用猩红气息生成巨大的尖齿撕咬敌人。\n
    施放时， 输入向前方向键， 则可以在更远处生成尖齿。
    """
    name = "狱血之牙"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 12
    uuid = "31823197cc0b04d4c5dcf8f928d9220c"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 猩红气息消耗量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 撕咬攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 绯红之狱
# mage_male/blood_mage/dac8d8207618150c162e4c6f9e168527
# a5ccbaf5538981c6ef99b236c0a60b73/dac8d8207618150c162e4c6f9e168527
class Skill28(ActiveSkill):
    """
    爆发出旋转的猩红气息， 对周围的敌人造成多段攻击伤害。
    """
    name = "绯红之狱"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cube = 1
    cd = 18
    uuid = "dac8d8207618150c162e4c6f9e168527"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 猩红气息消耗量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 多段攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 10
    # 多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [绯红之狱]\n
        不再生成猩红气息， 而是展开猩红地狱攻击更大范围\n
        猩红地狱展开期间所受伤害减少， 并从接触猩红地狱的敌人身上汲取生命值\n
         - 攻击时间增加\n
         - 攻击过程中所受伤害 -70%\n
         - 猩红地狱每次命中敌人时， 恢复1%的生命值 (最多恢复10%)
        """
        ...

    def vp_2(self):
        """
        [绯红之狱]\n
        冷却时间变更为6秒\n
        总攻击力 -66.6%\n
         - 猩红气息消耗量 -66.6%\n
        固定在前方生成猩红气息\n
         - 施放技能后可以移动\n
        召唤猩红气息时， 同时召唤蝙蝠群\n
         - [血蝠之舞]技能不在冷却时间时， 施放该技能会同时施放[血蝠之舞]
        """
        self.cd = 6
        self.skillRation *= 1 - 0.666
        ...

# 噬魂囚笼
# mage_male/blood_mage/8e358ecf99ac9df31a6132aeafe378a9
# a5ccbaf5538981c6ef99b236c0a60b73/8e358ecf99ac9df31a6132aeafe378a9
class Skill29(ActiveSkill):
    """
    在地面生成巨大的猩红之池， 从外围开始往中心喷射向上的猩红气息。\n
    向上喷射的血气将敌人击退至猩红之池中心， 并吸取血气。
    """
    name = "噬魂囚笼"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [192, 1920]
    uuid = "8e358ecf99ac9df31a6132aeafe378a9"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 24
    # 持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 猩红气息吸收量 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [噬魂囚笼]\n
        使用强化过的力量施放技能\n
         - 攻击范围 +50%\n
         - 设置僵直减少\n
         - 吸附力增加\n
        怨魂会抓住敌人， 附加减速效果\n
         - 攻击速度和移动速度 -50%
        """
        ...

    def vp_2(self):
        """
        [噬魂囚笼]\n
        存在正在被吸收猩红气息的敌人时可以施放\n
         - 将对方的灵魂抽出变成铃铛\n
         - 将抽出的灵魂附着在敌人身上\n
        删除向上攻击\n
         - 5秒后铃铛破碎， 对灵魂被抽出的敌人造成单次伤害\n
        存在铃铛的状态下施放[猩红狩猎]技能时， 使用猩红之枪穿透铃铛\n
         - 铃铛立即破碎， 适用[猩红狩猎]技能和该技能的伤害\n
         - 总攻击力相同
        """
        ...

# 隐行之噬
# mage_male/blood_mage/78b86e64fbb74c1db1b71c50a5ac21cd
# a5ccbaf5538981c6ef99b236c0a60b73/78b86e64fbb74c1db1b71c50a5ac21cd
class Skill30(ActiveSkill):
    """
    向前潜行一段距离并抓取一个敌人吸取大量的猩红气息。\n
    施放技能时消耗一定的猩红气息， 但是通过技能可以吸取更多猩红气息。
    """
    name = "隐行之噬"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cube = 2
    cd = 40
    uuid = "78b86e64fbb74c1db1b71c50a5ac21cd"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 猩红气息消耗量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 猩红气息吸收量 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 吸血次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 吸血目标攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 吸血目标范围攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 对无法抓取的目标吸血攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 对无法抓取的目标吸血范围攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 吸血结束后无敌时间 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [范围信息]
    # 攻击范围比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

    def vp_1(self):
        """
        [隐行之噬]\n
        不存在目标的情况下无法施放\n
        不再向敌人突进， 而是融入黑暗进行攻击\n
         - 追踪前方一定范围内的敌人
        """
        ...

    def vp_2(self):
        """
        [隐行之噬]\n
        更加残忍地从敌人体内夺取体力\n
         - 不再撕咬敌人， 而是用猩红之爪迅速进行更大范围的攻击\n
         - 恢复所消耗生命值的20%\n
        吸收猩红气息， 一定时间内增加活力\n
         - 30秒内移动速度 +10%
        """
        ...

# 赤狱之力
# mage_male/blood_mage/f4a561e272cc434a4905b3aa0c0de090
# a5ccbaf5538981c6ef99b236c0a60b73/f4a561e272cc434a4905b3aa0c0de090
class Skill31(PassiveSkill):
    """
    猩红法师觉醒为赤狱伯爵， 可以使猩红气息发挥出更强的效果。\n
    进入地下城时，猩红气息系列技能始终处于高涨状态， 技能形态发生变化， 并增加攻击力。
    """
    name = "赤狱之力"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 3
    uuid = "f4a561e272cc434a4905b3aa0c0de090"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]

# 伯爵之歌
# mage_male/blood_mage/0e409ac3e1c1f3976b3ef2bfe4c13069
# a5ccbaf5538981c6ef99b236c0a60b73/0e409ac3e1c1f3976b3ef2bfe4c13069
class Skill32(ActiveSkill):
    """
    赤狱伯爵爆发体内的力量， 变成猩红之湖，将眼前的所有东西用猩红之枪穿刺掉，并吸收血气。\n
    [成为锐利之枪， 穿刺敌人吧！]
    """
    name = "伯爵之歌"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    uuid = "0e409ac3e1c1f3976b3ef2bfe4c13069"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 猩红气息消耗量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 多段攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 14
    # 多段攻击次数 : {value2}次秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最终一击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 猩红气息吸收量 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 魔仆召唤 : 狱犬
# mage_male/blood_mage/2e2b7efe778656690f9c8cb6e47c3932
# a5ccbaf5538981c6ef99b236c0a60b73/2e2b7efe778656690f9c8cb6e47c3932
class Skill33(ActiveSkill):
    """
    在前方的猩红之池中召唤魔犬军团攻击范围内的敌人。\n
    魔犬来回跳跃撕咬敌人并吸取猩红气息。\n
    施放时， 输入向前方向键， 则可以在更远处生成猩红之池。
    """
    name = "魔仆召唤 : 狱犬"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 2 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [640, 1920]
    uuid = "2e2b7efe778656690f9c8cb6e47c3932"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 17
    # 多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 猩红气息吸收量 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [魔仆召唤 : 狱犬]\n
        召唤覆盖更大范围的狱犬\n
        四只狱犬冲向沼泽中央， 将敌人聚集到中心位置\n
         - 随后血口出现在沼泽中央， 吞噬敌人\n
         - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [魔仆召唤 : 狱犬]\n
        变更为可填充2次的技能\n
         - 每次填充冷却时间 : 12.5秒\n
         - 单次攻击力 -50%\n
        召唤准备时间 -50%\n
        在前方一定范围内最强敌人下方召唤沼泽， 追踪目标\n
         - 沼泽可以追踪敌人到一定高度
        """
        self.cd = 12.5
        self.skillRation *= 1 - 0.5
        ...

# 血翼绽放
# mage_male/blood_mage/902a016f6978f13740f237e4740a5646
# a5ccbaf5538981c6ef99b236c0a60b73/902a016f6978f13740f237e4740a5646
class Skill34(ActiveSkill):
    """
    化作蝙蝠群瞬移到前方， 然后向周围散发蝙蝠群冲击波和猩红之翼攻击敌人。\n
    蝙蝠群冲击波可以将敌人汇聚到角色身边。\n
    施放时， 可以利用向前/下方向键调整瞬移距离。
    """
    name = "血翼绽放"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 2
    cube = 2
    cd = 50
    uuid = "902a016f6978f13740f237e4740a5646"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 猩红气息消耗量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 蝙蝠群冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 猩红之翼攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [血翼绽放]\n
        瞬移前， 可以长按技能键蓄气\n
         - 蓄力时间上限 : 0.35秒\n
         - 蓄气过程中无敌\n
        根据蓄气时间增加攻击范围\n
         - 最大蓄气时增加40%
        """
        ...

    def vp_2(self):
        """
        [血翼绽放]\n
        可以在空中施放技能\n
        瞬移后， 可以强制中断僵直并施放其他转职技能
        """
        ...

# 地狱冥犬
# mage_male/blood_mage/4c5271b0ecce120d7fc113f377fae76f
# a5ccbaf5538981c6ef99b236c0a60b73/4c5271b0ecce120d7fc113f377fae76f
class Skill35(ActiveSkill):
    """
    利用猩红气息和蝙蝠群生成巨大的犬形怪撕咬敌人， 并吸收猩红气息。\n
    施放时， 输入向前方向键， 可以撕咬更远处的敌人。
    """
    name = "地狱冥犬"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 2 #TODO
    rangeLv = 2
    cube = 3
    cd = 30
    mp = [1066, 2133]
    uuid = "4c5271b0ecce120d7fc113f377fae76f"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 撕咬攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 20
    # 撕咬次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 冲向地面攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 猩红气息吸收量 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [地狱冥犬]\n
        召唤地狱冥犬， 攻击大范围敌人\n
         - 删除撕咬攻击\n
         - 变更冲向地面的攻击范围\n
         - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [地狱冥犬]\n
        基本冷却时间变更为60秒\n
        总攻击力 +100%\n
        在第一只冥犬的对面额外召唤一只冥犬， 同时进行攻击\n
         - 猩红气息吸收量 +100%
        """
        ...

# 鲜血之殇
# mage_male/blood_mage/370586038cf40378f20d338d507a780c
# a5ccbaf5538981c6ef99b236c0a60b73/370586038cf40378f20d338d507a780c
class Skill36(PassiveSkill):
    """
    赤狱君主领悟了猩红真谛， 可以给敌人造成更大的致命伤。 在猩红气息蓄满的状态下吸收气息时， 可以恢复体力。
    """
    name = "鲜血之殇"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 8 #TODO
    rangeLv = 3
    uuid = "370586038cf40378f20d338d507a780c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 暴击伤害增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 猩红气息吸收量与生命值恢复量比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    associate = [{"data":data0}]

# 死亡之握
# mage_male/blood_mage/dd32a9825ec1af42a91f2223be6658e5
# a5ccbaf5538981c6ef99b236c0a60b73/dd32a9825ec1af42a91f2223be6658e5
class Skill37(ActiveSkill):
    """
    形成猩红气息湖泊， 将上面的目标吸附到猩红法师的前方。 然后向敌人身上插入猩红气息之刺使其进入眩晕状态， 然后将刺和精气一起拔出。
    """
    name = "死亡之握"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 2
    cube = 5
    cd = 50
    uuid = "dd32a9825ec1af42a91f2223be6658e5"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 猩红气息消耗量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 拔出精气时攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [死亡之握]\n
        攻击范围变更为猩红湖水的范围\n
         - 删除聚集敌人功能\n
         - 攻击接触到猩红湖水的所有敌人
        """
        ...

    def vp_2(self):
        """
        [死亡之握]\n
        删除按住技能键后调整攻击时机的功能\n
         - 攻击准备时间 +0.5秒\n
        攻击准备时， 可以施放部分技能， 将力量储存在湖泊中\n
         - 提取精气时， 结算所储存技能的伤害\n
        [可储存的技能] (6种)\n
         - [血蝠之袭]、 [鲜血长枪]、 [血蝠之舞]、[猩红狩猎]、 [狱血之犬]、 [狱血之牙]
        """
        ...

# 血界彼岸
# mage_male/blood_mage/fa3ee243b36699e9d3fc34328adf6417
# a5ccbaf5538981c6ef99b236c0a60b73/fa3ee243b36699e9d3fc34328adf6417
class Skill38(ActiveSkill):
    """
    赤狱君主释放体内的力量， 生成龙卷风攻击敌人并吸取猩红气息。\n
    连续按攻击键或技能键， 可以加快攻击速度。\n
    [和我融为一体吧！]
    """
    name = "血界彼岸"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    uuid = "fa3ee243b36699e9d3fc34328adf6417"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 猩红气息消耗量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 猩红气息吸收量 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 多段攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 34
    # 多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 最终一击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1

# 猩红之眼
# mage_male/blood_mage/3cb633d00f8f6ee088682c9171020d26
# a5ccbaf5538981c6ef99b236c0a60b73/3cb633d00f8f6ee088682c9171020d26
class Skill39(PassiveSkill):
    """
    知源·猩红法师自身的心脏和生命——黑暗之眼与猩红气息彻底同化， 再生出一个完整的“猩红之眼”。\n
    凭借猩红之眼的力量， 增加基本攻击力和转职技能攻击力， 增加猩红气息的吸收量和吸收持续时间， 部分技能获得附加效果。\n
    [血蝠之袭]\n
    召唤大量血蝠群攻击敌人， 最多可以攻击10个敌人。\n
    [狱血之牙]\n
    存在猩红气息吸收的敌人时， 在敌人位置生成尖齿， 造成更大范围的伤害。
    """
    name = "猩红之眼"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "3cb633d00f8f6ee088682c9171020d26"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本、 技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 猩红气息吸收量增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 吸收持续时间增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [狱血之牙]探索范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)
    associate = [{"data":data0}]

# 血翼蔽空
# mage_male/blood_mage/6d7c9a15c08cc41d70125083e869e1a1
# a5ccbaf5538981c6ef99b236c0a60b73/6d7c9a15c08cc41d70125083e869e1a1
class Skill40(ActiveSkill):
    """
    生成血翼， 原地旋转的同时大幅挥动血翼， 击飞前方的敌人。\n
    角色后方的敌人被击时， 被击退至向角色前方一定距离。
    """
    name = "血翼蔽空"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    uuid = "6d7c9a15c08cc41d70125083e869e1a1"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 猩红气息消耗量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 猩红之翼斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

# 血域帷幕·陨灭
# mage_male/blood_mage/1ff42548e611b94781a1ae8f063dd679
# a5ccbaf5538981c6ef99b236c0a60b73/1ff42548e611b94781a1ae8f063dd679
class Skill41(ActiveSkill):
    """
    消耗剩余的所有猩红气息展开猩红气息帷幕， 从敌人体内抽取生命根源的猩红气息并束缚敌人。\n
    然后， 将抽取的猩红气息凝集成结晶体后将其打碎， 对敌人造成致命的伤害。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "血域帷幕·陨灭"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    uuid = "1ff42548e611b94781a1ae8f063dd679"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 猩红气息帷幕攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 猩红气息吸收多段攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 20
    # 猩红气息吸收多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 终结爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'blood_mage'
        self.nameCN = '知源·血法师'
        self.role = 'mage_male'
        self.角色 = '魔法师(男)'
        self.职业 = '血法师'
        self.jobId = 'a5ccbaf5538981c6ef99b236c0a60b73'
        self.jobGrowId = '6d459bc74ba73ee4fe5cdc4655400193'

        self.武器选项 = ['矛', '魔杖', '法杖', '棍棒']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '皮甲'
        self.buff = 2.042

        super().__init__(equVersion, __name__)
