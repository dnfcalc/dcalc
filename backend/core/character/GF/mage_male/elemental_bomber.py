#a5ccbaf5538981c6ef99b236c0a60b73
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "mage_male/elemental_bomber/cn/skillDetail"


# 魔法冰球
# mage_male/elemental_bomber/5dc7008b12a459325b548b0715c6b73c
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
    position = 4
    rangeLv = 2
    cd = 2
    mp = [10, 84]
    uuid = "5dc7008b12a459325b548b0715c6b73c"
    hasVP = False
    hasUP = False

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冰球大小 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 不死之身
# mage_male/elemental_bomber/bb34e8854a93fd250347a1c64119f7ab
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
    position = 1
    rangeLv = 3
    uuid = "bb34e8854a93fd250347a1c64119f7ab"
    hasVP = False
    hasUP = False

    # 恢复模式下所受伤害增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 死亡时立即恢复的生命值量 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 恢复模式持续时间(普通地下城) : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 恢复模式持续时间(亡者峡谷) : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 黑暗之眼
# mage_male/elemental_bomber/6e33d47e6622ce03b6defdd912140270
# a5ccbaf5538981c6ef99b236c0a60b73/6e33d47e6622ce03b6defdd912140270
class Skill3(PassiveSkill):
    """
    增加魔法师的魔法值最大值； 若魔法值低于一定比率时， 还可增加魔法值恢复速度。
    """
    name = "黑暗之眼"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 2
    rangeLv = 1
    uuid = "6e33d47e6622ce03b6defdd912140270"
    hasVP = False
    hasUP = False

    # 魔法值最大值增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 可触发恢复效果时的魔法值比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 魔法值恢复速度增加 : {value2}倍
    data2 = get_data(f'{prefix}/{uuid}', 2)


# 基础精通
# mage_male/elemental_bomber/5a56514f35cf0270ae8d6c65f8fefd78
# a5ccbaf5538981c6ef99b236c0a60b73/5a56514f35cf0270ae8d6c65f8fefd78
class Skill5(PassiveSkill):
    """
    增加基本攻击、 前冲攻击、 跳跃攻击、 [魔法旋风]的攻击力。\n
    在决斗场中， 增益/减益技能、 被动技能的技能攻击力增加效果对[基础精通]无影响。
    """
    name = "基础精通"
    learnLv = 1
    masterLv = 115
    maxLv = 200
    position = 1
    rangeLv = 1
    uuid = "5a56514f35cf0270ae8d6c65f8fefd78"
    icon = "$common/$uuid"
    hasVP = False
    hasUP = False

    # 基本攻击力变化率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 前冲攻击力变化率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 跳跃攻击力变化率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)


# 魔球连射
# mage_male/elemental_bomber/a5fa08f5d509e6ff2ebc68856a470b5a
# a5ccbaf5538981c6ef99b236c0a60b73/a5fa08f5d509e6ff2ebc68856a470b5a
class Skill9(ActiveSkill):
    """
    快速生成多个魔法球并向前连续发射。\n
    转职为元素爆破师后， 减少技能冷却时间， 发射[属性变换]中所选属性的魔法球。
    """
    name = "魔球连射"
    learnLv = 5
    masterLv = 1
    maxLv = 11
    position = 6
    rangeLv = 2
    cd = 3 - 1
    mp = [22, 183]
    uuid = "a5fa08f5d509e6ff2ebc68856a470b5a"
    hasVP = False
    hasUP = False

    # 魔法球数量 : {value0}个
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    data1 = [i+100 if i > 0 else 0 for i in data1]
    hit1 = 5
    power1 = 0
    # -  [转职为元素爆破师后附加效果]  -
    # 冷却时间减少 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 幽冥火
# mage_male/elemental_bomber/cfacda0647b9a0f595df2c2aad30c18d
# a5ccbaf5538981c6ef99b236c0a60b73/cfacda0647b9a0f595df2c2aad30c18d
class Skill10(ActiveSkill):
    """
    生成两团幽冥火， 可以增加自身的物理和魔法防御力， 且造成一定伤害， 效果持续一定时间。\n
    转职成次元行者时， 可以学习[虚妄之火]技能。\n
    学习[虚妄之火]后， 持续时间变更为无限， 且无法发动攻击。
    """
    name = "幽冥火"
    learnLv = 10
    masterLv = 10
    maxLv = 20
    position = 2
    rangeLv = 3
    cd = 10
    mp = [30, 345]
    uuid = "cfacda0647b9a0f595df2c2aad30c18d"
    hasVP = False
    hasUP = False

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


# 旋火盾
# mage_male/elemental_bomber/8ee0099656df08a0b39225f8a21d514b
# a5ccbaf5538981c6ef99b236c0a60b73/8ee0099656df08a0b39225f8a21d514b
class Skill12(ActiveSkill):
    """
    生成火焰盾牌并向前发射， 使其攻击敌人。 \n
    持续输入按键可维持持盾状态， 减少敌人远程攻击的伤害。
    """
    name = "旋火盾"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cd = 4
    mp = [31, 259]
    uuid = "8ee0099656df08a0b39225f8a21d514b"
    hasVP = False
    hasUP = False

    # 盾牌攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 所受伤害减少率 (远程) : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 盾牌前进距离 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 属性变换
# mage_male/elemental_bomber/eb71e1d82d92c7e1d40500a0dcd77aa6
# a5ccbaf5538981c6ef99b236c0a60b73/eb71e1d82d92c7e1d40500a0dcd77aa6
class Skill15(ActiveSkill):
    """
    可以变换魔法球的属性。 从四种属性中任意选择一种作为魔法球的属性。 一定时间后， 魔法球恢复无属性。
    """
    name = "属性变换"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 5
    cd = 5
    mp = [181, 3134]
    uuid = "eb71e1d82d92c7e1d40500a0dcd77aa6"
    hasVP = False
    hasUP = False

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 火属性攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 冰属性攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 暗属性攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 光属性攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    associate = [
        {"data":data1,"type":"+power1","skills":["魔球连射"]},
        {"data":data1,"type":"+power0","skills":["元素炮"]},
        ]

# 冰魄剑
# mage_male/elemental_bomber/f2fb27162beb0b87a7cb9af7900e95f2
# a5ccbaf5538981c6ef99b236c0a60b73/f2fb27162beb0b87a7cb9af7900e95f2
class Skill16(ActiveSkill):
    """
    生成冰魄剑连续攻击敌人。 第1击和第2击使敌人进入僵直状态， 第3击则可以击退敌人， 并有一定几率使敌人进入减速状态。\n
    转职成为冰结师时， 才可以强制中断基本攻击动作， 并立即施放该技能。
    """
    name = "冰魄剑"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 10
    rangeLv = 2
    cd = 5
    mp = [30, 280]
    uuid = "f2fb27162beb0b87a7cb9af7900e95f2"
    hasVP = False
    hasUP = True

    # 第1击和第2击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 第3击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [减速效果]
    # 减速几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 减速持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 元素炮
# mage_male/elemental_bomber/d085127b0edd719782bd618d5688f4a1
# a5ccbaf5538981c6ef99b236c0a60b73/d085127b0edd719782bd618d5688f4a1
class Skill17(ActiveSkill):
    """
    生成强力的元素炮给予敌人伤害。\n
    元素炮的攻击力、 属性以及附加效果受[属性变换]的影响。\n
    该技能可以在空中使用， 在空中攻击时可以利用方向键调整发射方向以及发射后自身反弹的方向。\n
    可以强制中断当前进行的普通攻击动作或[魔球连射]， 并立即施放该技能。
    """
    name = "元素炮"
    learnLv = 15
    masterLv = 1
    maxLv = 11
    position = 9
    rangeLv = 2
    cd = 5
    mp = [31, 259]
    uuid = "d085127b0edd719782bd618d5688f4a1"
    hasVP = False
    hasUP = False

    # [属性变换]魔法球攻击力变换率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    data0 = [i+100 if i > 0 else 0 for i in data0]
    hit0 = 1
    power0 = 0
    # [范围信息]
    # 爆炸大小比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 元素融合
# mage_male/elemental_bomber/1dad88963abdc96b091fcab185a8820d
# a5ccbaf5538981c6ef99b236c0a60b73/1dad88963abdc96b091fcab185a8820d
class Skill18(PassiveSkill):
    """
    施放[属性变换]后， 可增加所选属性外的其它3种属性的抗性， 并增加属性攻击力。\n
    在决斗场中， 不增加属性攻击力。
    """
    name = "元素融合"
    learnLv = 15
    masterLv = 1
    maxLv = 11
    position = 2
    rangeLv = 3
    uuid = "1dad88963abdc96b091fcab185a8820d"
    hasVP = False
    hasUP = False

    # 属性抗性增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 属性攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"data":data1}]

# 冰晶坠
# mage_male/elemental_bomber/0969cd4054d93da07708108c0cc1c4b5
# a5ccbaf5538981c6ef99b236c0a60b73/0969cd4054d93da07708108c0cc1c4b5
class Skill19(ActiveSkill):
    """
    在角色上方生成冰柱直线攻击下方敌人。\n
    被冰柱命中的敌人， 会受到冰属性魔法伤害。
    """
    name = "冰晶坠"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 8
    mp = [60, 616]
    uuid = "0969cd4054d93da07708108c0cc1c4b5"
    hasVP = False
    hasUP = True

    # 冰柱攻击力 : {value0}% x{value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 7
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 水晶大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 元素之力
# mage_male/elemental_bomber/b163d099c8cc27fdb6fd3639c2ee6df9
# a5ccbaf5538981c6ef99b236c0a60b73/b163d099c8cc27fdb6fd3639c2ee6df9
class Skill20(PassiveSkill):
    """
    使用元素技能成功进行攻击时， [元素之力]将会蓄力。\n
    [元素之力]蓄好力的状态下使用[元素炮]， 则会消耗蓄好的[元素之力]增加[元素炮]的攻击力和爆炸大小， 消耗的[元素之力]越多， 增加的也越多。\n
    [元素之力蓄力技能目录]\n
    基本攻击第4下、 [魔球连射]、 [冰晶坠]、 [地炎]、 [雷光链]、 [暗域扩张]、 [冰晶之浴]、 [旋炎破]、 [雷光屏障]、 [黑暗禁域]、 [元素轰炸]、 [幻魔四重奏]、 [元素浓缩球]、 [元素幻灭]、 [元素禁域]、 [聚能魔炮]、 [末日湮灭]、 [聚魔轰击]、 [启源·微观宇宙]
    """
    name = "元素之力"
    learnLv = 20
    masterLv = 1
    maxLv = 11
    position = 9
    rangeLv = 5
    uuid = "b163d099c8cc27fdb6fd3639c2ee6df9"
    hasVP = False
    hasUP = False

    # [元素之力]最大蓄力数量 : {value0}个
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 每个[元素之力]增加的[元素炮]攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 每个[元素之力]增加的[元素炮]大小增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    associate = [{"data":[i*5 for i in data1],"skills":["元素炮"]},]


# 地炎
# mage_male/elemental_bomber/4655101518604f874721b3cc249aae10
# a5ccbaf5538981c6ef99b236c0a60b73/4655101518604f874721b3cc249aae10
class Skill22(ActiveSkill):
    """
    在前方地面生成多个火柱攻击敌人。
    """
    name = "地炎"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 5
    mp = [45, 476]
    uuid = "4655101518604f874721b3cc249aae10"
    hasVP = False
    hasUP = True

    # 火焰攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 12
    # 火焰攻击次数 : {value1}次 x2
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 元素环绕
# mage_male/elemental_bomber/42c82812f86ff6704ae9952a2e6093a4
# a5ccbaf5538981c6ef99b236c0a60b73/42c82812f86ff6704ae9952a2e6093a4
class Skill23(ActiveSkill):
    """
    生成各种元素护盾环绕在自身周围。\n
    元素保护持续时间内， 增加元素爆破师的物理/魔法防御力和属性攻击力 。\n
    在[元素环绕]激活的状态下， 若再次按技能键， 则护盾和保护效果消失。
    """
    name = "元素环绕"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 8
    rangeLv = 2
    cd = 5
    mp = [60, 546]
    uuid = "42c82812f86ff6704ae9952a2e6093a4"
    hasVP = False
    hasUP = False

    # 护盾持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理防御力增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 魔法防御力增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 属性攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    associate = [{"data":data3}]

# 魔力燃烧
# mage_male/elemental_bomber/9bff7f2559e003766fee2853dca00631
# a5ccbaf5538981c6ef99b236c0a60b73/9bff7f2559e003766fee2853dca00631
class Skill24(ActiveSkill):
    """
    使魔力的流动加速， 增加元素爆破师的基本攻击力、 技能攻击力和施放技能时的魔法值消耗量。
    """
    name = "魔力燃烧"
    learnLv = 25
    masterLv = 20
    maxLv = 30
    position = 2
    rangeLv = 2
    cd = 5
    uuid = "9bff7f2559e003766fee2853dca00631"
    hasVP = False
    hasUP = False

    # 攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法值消耗增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 元素禁断
# mage_male/elemental_bomber/ca75c965f20a150f99f54155a37400df
# a5ccbaf5538981c6ef99b236c0a60b73/ca75c965f20a150f99f54155a37400df
class Skill25(PassiveSkill):
    """
    可以强制中断元素爆破师的部分转职技能， 并增加施放速度、 减少转职技能的冷却时间。\n
    可强制中断的技能种类随[元素禁断]技能等级的增加而增加。\n
    强制中断[雷光链]施放其他技能时， 电流连接将会中断。\n
    无法强制中断[元素轰炸]， 并施放其他技能。\n
    [幻魔四重奏]、 [末日湮灭]、 [启源·微观宇宙]不适用[元素禁断]减少冷却时间的效果。
    """
    name = "元素禁断"
    learnLv = 25
    masterLv = 1
    maxLv = 5
    position = 7
    rangeLv = 5
    uuid = "ca75c965f20a150f99f54155a37400df"
    hasVP = False
    hasUP = False

    # 施放速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 转职技能冷却时间减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"data":data1,"type":"*cdReduce","exceptSkills":['幻魔四重奏', '末日湮灭', '启源·微观宇宙']}]
    # [可强制中断的技能列表]
    # 掌握技能等级1时 : [元素炮]、 [冰晶坠]、 [地炎]
    # 掌握技能等级2时 : [暗域扩张]、 [雷光链]
    # 掌握技能等级3时 : [旋炎破]、 [冰晶之浴]
    # 掌握技能等级4时 : [黑暗禁域]、 [雷光屏障]、 [元素轰炸]
    # 掌握技能等级5时 : [元素浓缩球]、 [元素幻灭]

# 雷光链
# mage_male/elemental_bomber/9dda3f4a849dba1a288dd65e116860f2
# a5ccbaf5538981c6ef99b236c0a60b73/9dda3f4a849dba1a288dd65e116860f2
class Skill26(ActiveSkill):
    """
    向前方发射光属性电流， 使敌人受到4次电流伤害。 电流在攻击敌人的同时， 会随机传导给周围的其他敌人， 并使其受到伤害。
    """
    name = "雷光链"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 12
    mp = [100, 1050]
    uuid = "9dda3f4a849dba1a288dd65e116860f2"
    hasVP = False
    hasUP = True

    # 电流攻击力 : {value0}% x{value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 电流传导次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [学习异瞳后]
    # 闪电球体爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 暗域扩张
# mage_male/elemental_bomber/717f1e2104fe4b796f800352fa143ecc
# a5ccbaf5538981c6ef99b236c0a60b73/717f1e2104fe4b796f800352fa143ecc
class Skill27(ActiveSkill):
    """
    在前方释放黑暗能量， 对一定范围内的敌人造成伤害， 并使画面内角色面对方向的所有敌人进入失明状态。\n
    施放技能时按向下方向键， 在以自身为中心的圆圈范围内释放黑暗能量， 并使画面内的所有敌人进入失明状态。\n
    在决斗场中， 不受方向键影响， 在以自身为中心的圆圈范围内释放黑暗能量。
    """
    name = "暗域扩张"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 15
    mp = [80, 980]
    uuid = "717f1e2104fe4b796f800352fa143ecc"
    hasVP = False
    hasUP = True

    # 暗黑能量攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 失明几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 失明持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # [暗域扩张]范围 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 元素循环
# mage_male/elemental_bomber/573723c8c0614f5b1218ca9ff992115b
# a5ccbaf5538981c6ef99b236c0a60b73/573723c8c0614f5b1218ca9ff992115b
class Skill28(PassiveSkill):
    """
    对元素本质有了更深入的理解， 领悟了高效的元素循环， 增加基本攻击力、 转职技能攻击力和命中率。
    """
    name = "元素循环"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 8
    rangeLv = 3
    uuid = "573723c8c0614f5b1218ca9ff992115b"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]
    # 命中率增加量 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 旋炎破
# mage_male/elemental_bomber/45442bbbe33540b4deeec29437dae70c
# a5ccbaf5538981c6ef99b236c0a60b73/45442bbbe33540b4deeec29437dae70c
class Skill29(ActiveSkill):
    """
    在前方生成高速旋转的火环， 攻击敌人。\n
    施放技能时按向下方向键， 生成以自身为中心旋转的火环， 使周围敌人受到伤害， 然后引爆火环将其击飞。 在该情况下， 如果在旋转时连续按X键或技能键， 可以加快火环旋转速度。\n
    普通施放时不适用连按加速效果。\n
    在决斗场中， 不受方向键影响， 生成以自身为中心旋转的火环。
    """
    name = "旋炎破"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [150, 1148]
    uuid = "45442bbbe33540b4deeec29437dae70c"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 前方火环攻击力 : {value0}% x{value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 自身中心火环攻击力 : {value2}% x{value3}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 6
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 自身中心火环爆炸攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # [范围信息]
    # 攻击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [旋炎破]\n
        对周围一定范围内最强的敌人生成旋炎破\n
         - 对敌人生成的旋炎破会跟随敌人旋转并爆炸\n
         - 不受方向键的影响， 以相同方式施放\n
         - 若寻敌范围内没有敌人， 则无法施放\n
        旋转速度 +30%
        """
        ...

    def vp_2(self):
        """
        [旋炎破]\n
        向前方发射旋转的旋炎破\n
         - 多段攻击次数减少为3次\n
         - 删除爆炸攻击\n
         - 总攻击力相同\n
        旋转半径 +50%
        """
        ...

# 冰晶之浴
# mage_male/elemental_bomber/8c2379737c5acc935c1731f67f607655
# a5ccbaf5538981c6ef99b236c0a60b73/8c2379737c5acc935c1731f67f607655
class Skill30(ActiveSkill):
    """
    在前方生成魔法阵， 并召唤出大量冰柱， 使其下落攻击敌人。\n
    在决斗场中， 武器的攻击属性不影响技能的攻击属性。
    """
    name = "冰晶之浴"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 9
    mp = [150, 1148]
    uuid = "8c2379737c5acc935c1731f67f607655"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 冰柱攻击力 : {value0}% x{value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 14
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 冰冻几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 冰冻持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 魔法阵大小比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [冰晶之浴]\n
        在前方空中生成巨大的冰块并使其坠落\n
         - 删除魔法阵\n
         - 坠落期间， 周围敌人会被吸附至落点\n
        冰块碰撞地面后破碎， 并对周围造成1次伤害\n
         - 删除对敌人附加冰冻的功能\n
         - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [冰晶之浴]\n
        变更为可填充2次的技能\n
         - 每次填充冷却时间 : 4.5秒\n
         - 魔法阵持续时间 -50%\n
         - 冰柱多段攻击次数 -50%\n
        魔法阵大小 +20%
        """
        self.cd = 4.5
        self.skillRation *= 1 - 0.5
        ...

# 黑暗禁域
# mage_male/elemental_bomber/506e7ed77d517419a6e1c437a2cedb17
# a5ccbaf5538981c6ef99b236c0a60b73/506e7ed77d517419a6e1c437a2cedb17
class Skill31(ActiveSkill):
    """
    在前方生成黑暗气息地带， 黑暗气息会凝聚成球体将周围的敌人吸附进来， 并使敌人进入减速状态。 将敌人聚到一处后， 使敌人进入强制控制状态， 最后球体发生爆破， 使敌人受到巨大伤害。\n
    在决斗场中不会吸附敌人， 球体内部的僵直不会强制控制敌人， 但会使敌人浮空。
    """
    name = "黑暗禁域"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [300, 2520]
    uuid = "506e7ed77d517419a6e1c437a2cedb17"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 暗黑球体爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 减速持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 吸附范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [黑暗禁域]\n
        球体吸附敌人后立即爆炸\n
         - 不会强制控制敌人\n
        吸附敌人的范围 +40%
        """
        ...

    def vp_2(self):
        """
        [黑暗禁域]\n
        以自身为中心展开黑暗气息， 随后在黑暗气息范围内的所有敌人身上生成黑暗球体\n
         - 球体不再吸附敌人\n
         - 黑暗气息范围 +50%\n
         - 暗黑球体爆炸攻击变更为1:1攻击\n
        暗黑球体生成速度 +100%
        """
        ...

# 雷光屏障
# mage_male/elemental_bomber/da6e37c1e3f0e8867f70007d89c239ff
# a5ccbaf5538981c6ef99b236c0a60b73/da6e37c1e3f0e8867f70007d89c239ff
class Skill32(ActiveSkill):
    """
    生成雷光屏障， 并向前快速推移攻击敌人， 对敌人造成光属性伤害。
    """
    name = "雷光屏障"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [350, 3080]
    uuid = "da6e37c1e3f0e8867f70007d89c239ff"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 雷光屏障攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # [雷光屏障]大小比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [雷光屏障]\n
        在两侧额外生成2道屏障并发射\n
         - 最多仅造成1次攻击\n
        屏障生成速度 +50%\n
        屏障移动速度 +30%
        """
        ...

    def vp_2(self):
        """
        [雷光屏障]\n
        在前方一定范围内生成方形的屏障围栏\n
        生成的围栏会在短暂延迟后向中心收缩， 聚集敌人并爆炸
        """
        ...

# 元素轰炸
# mage_male/elemental_bomber/a6c8f69107f8c4f5d1a0c7a57d000290
# a5ccbaf5538981c6ef99b236c0a60b73/a6c8f69107f8c4f5d1a0c7a57d000290
class Skill33(ActiveSkill):
    """
    瞬间移动到空中， 在空中向敌人连续抛出各种属性的小魔法球， 最后生成大型魔法球砸向地面并引发爆炸。 魔法球的属性为所有属性。\n
    施放技能途中若按下Z键， 则直接施放大型魔法球； 若按下跳跃键， 则中断技能。
    """
    name = "元素轰炸"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [360, 3149]
    uuid = "a6c8f69107f8c4f5d1a0c7a57d000290"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 小魔法球攻击力 : {value0}% x{value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 40
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后大魔法球碰撞攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 最后大魔法球爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 最后小魔法球攻击力 : {value4}% x{value5}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 5
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 大爆炸范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [元素轰炸]\n
        在空中生成魔法球后使其逐渐变大， 然后向地面发射后引爆\n
         - 删除小魔法球攻击\n
         - 总攻击力相同\n
        可以利用[元素禁断]强制中断
        """
        ...

    def vp_2(self):
        """
        [元素轰炸]\n
        使前方大范围的地面分裂， 从裂缝中涌出大量的元素球后爆炸\n
         - 总攻击力相同
        """
        ...

# 元素爆发
# mage_male/elemental_bomber/1fadde0eece18649caddbca7bd58cc2f
# a5ccbaf5538981c6ef99b236c0a60b73/1fadde0eece18649caddbca7bd58cc2f
class Skill34(PassiveSkill):
    """
    理解元素的流动、 能熟练控制其中不稳定部分， 将元素的效率发挥到极致， 对敌人造成更强力、 致命的伤害。\n
    掌握该技能后， 增加魔皇的魔法暴击伤害和魔法暴击率。
    """
    name = "元素爆发"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    uuid = "1fadde0eece18649caddbca7bd58cc2f"
    hasVP = False
    hasUP = False

    # 暴击伤害增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"data":data0}]

# 幻魔四重奏
# mage_male/elemental_bomber/c27418ae613c647527200a7ca17d97fd
# a5ccbaf5538981c6ef99b236c0a60b73/c27418ae613c647527200a7ca17d97fd
class Skill35(ActiveSkill):
    """
    凝聚带有属性的气息并引发爆炸； 4次爆炸效果分别带有4种不同属性。\n
    最后一次爆炸效果更强烈， 并且受最近一次施放[属性变换]中选择的属性影响。\n
    掌握[黑瞳]后， 适用[元素禁断]效果。 \n
    但施放[幻魔四重奏]时， 无法强制中断后使用其他技能， 并且不适用减少冷却时间的效果。
    """
    name = "幻魔四重奏"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [600, 5040]
    uuid = "c27418ae613c647527200a7ca17d97fd"
    hasVP = False
    hasUP = False

    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 30
    # 爆炸次数 : 4次
    # 最后爆炸次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 元素浓缩球
# mage_male/elemental_bomber/faf9cd66281078b51be2ee0b0f6c5530
# a5ccbaf5538981c6ef99b236c0a60b73/faf9cd66281078b51be2ee0b0f6c5530
class Skill36(ActiveSkill):
    """
    凝聚属性力量， 生成魔法球并向前抛出。 抛出的魔法球在弹落一定次数后引起爆炸。 爆炸属性受[属性变换]的影响。
    """
    name = "元素浓缩球"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [450, 1260]
    uuid = "faf9cd66281078b51be2ee0b0f6c5530"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 弹落攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 弹落次数 : 1次
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 爆炸范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [元素浓缩球]\n
        抛出的魔法球触碰地面时立即爆炸\n
         - 总攻击力相同\n
        爆炸攻击不会击飞敌人\n
        爆炸范围 +30%
        """
        ...

    def vp_2(self):
        """
        [元素浓缩球]\n
        魔法球可以弹跳7次\n
         - 对单个敌人最多造成2次攻击\n
         - 总攻击力相同\n
        弹跳攻击范围 +50%\n
        被攻击的敌人不会被击飞， 而是被聚集到魔法球弹跳的位置
        """
        ...

# 元素幻灭
# mage_male/elemental_bomber/1721e94897e9961d5c98130a13392f17
# a5ccbaf5538981c6ef99b236c0a60b73/1721e94897e9961d5c98130a13392f17
class Skill37(ActiveSkill):
    """
    在空中生成5个大魔法球并砸向地面。 魔法球落地时生成魔法阵并引发强烈爆炸。 魔法球的属性受最近一次施放[属性变换]中选择的属性影响。
    """
    name = "元素幻灭"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [935, 1960]
    uuid = "1721e94897e9961d5c98130a13392f17"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 魔法球攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [元素幻灭]\n
        魔法阵汇聚时将敌人向中心聚拢\n
        魔法球及魔法阵大小 +45%\n
        [元素幻灭]攻击速度 +30%
        """
        ...

    def vp_2(self):
        """
        [元素幻灭]\n
        删除魔法球生成过程， 立即发生爆炸\n
         - 总攻击力相同\n
        在其他技能施放过程中施放[元素幻灭]时， 无施放动作直接施放
        """
        ...

# 黑瞳
# mage_male/elemental_bomber/51a08fd0c90f0a5276cd552047fac93d
# a5ccbaf5538981c6ef99b236c0a60b73/51a08fd0c90f0a5276cd552047fac93d
class Skill38(PassiveSkill):
    """
    眼睛变黑的元素爆破师以更强大的魔力为基础进行转职后， [元素禁断]可以连接使用所有技能， 并增加基本攻击力和技能攻击力。\n
    进入地下城时， 自动施放[元素环绕]技能。 而且， [幻魔四重奏]的攻击属性将变更为全属性攻击。\n
    部分技能强制中断后施放时， 有附加效果。\n
    - [元素禁断可以额外强制中断的技能] -\n
    [魔球连射]、 [幻魔四重奏]、 [元素禁域]、 [聚能魔炮]、 [末日湮灭]\n
    - [攻击力增加的技能] -\n
    [属性变换]、 [冰晶坠]、 [雷光链]、 [暗域扩张]、 [旋炎破]、 [雷光屏障]、 [黑暗禁域]、 [元素轰炸]、 [幻魔四重奏]、 [元素浓缩球]、 [元素幻灭]、 [聚能魔炮]、 [元素禁域]、 [末日湮灭]、 [聚魔轰击]、 [启源·微观宇宙]\n
    - [有附加效果的技能] -\n
    [元素炮] - 增加魔法球体及爆炸大小\n
    [地炎] - 增加火柱施放速度\n
    [冰晶之浴] - 增加攻击范围及冰块大小\n
    [暗域扩张] - 增加攻击范围\n
    [旋炎破] - 增加攻击范围
    """
    name = "黑瞳"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 3
    uuid = "51a08fd0c90f0a5276cd552047fac93d"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [技能连接附加效果]
    # 技能魔法值减少 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [元素炮]魔法球、 爆炸大小变化率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [地炎]火柱速度变化率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [冰晶之浴]范围、 冰块大小变化率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [暗域扩张]范围增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [旋炎破]范围增加 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    associate = [{"data":data0}]

# 元素禁域
# mage_male/elemental_bomber/f0cc2c950f3bdf4103c75fa496bcac34
# a5ccbaf5538981c6ef99b236c0a60b73/f0cc2c950f3bdf4103c75fa496bcac34
class Skill39(ActiveSkill):
    """
    让元素爆炸后， 展开[元素禁域]。\n
    [元素禁域]展开时， 领域内的敌人将会受到所有属性的魔法伤害。\n
    [元素禁域]持续一定时间， 且一定时间内使部分固定属性技能适用所有属性。\n
    学习[黑瞳]后会受到[元素禁断]的效果。\n
    - [适用所有属性的技能] -\n
    [冰晶坠]、 [冰晶之浴]、 [闪电链]、 [雷光屏障]、 [地炎]、 [旋炎破]、 [暗域扩张]、 [黑暗禁域]
    """
    name = "元素禁域"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [800, 6000]
    uuid = "f0cc2c950f3bdf4103c75fa496bcac34"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # [元素禁域]持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 适用所有属性效果持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [元素禁域]攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # [元素禁域]范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [元素禁域]\n
        施放其他技能过程中施放[元素禁域]时， 可以取消施放动作， 立即施放。\n
        禁域范围 +10%\n
        在禁域内赋予以下效果\n
         - 所有速度 +20%\n
         - 所受伤害 -50%
        """
        ...

    def vp_2(self):
        """
        [元素禁域]\n
        在禁域内使用瞬移技能可以连接元素禁断\n
         - 瞬移前后攻击技能可强制中断连接\n
         - 强制中断连接时可根据方向键输入调整技能使用方向\n
        禁域持续时间 +5秒\n
        禁域范围 +20%\n
        在禁域内进入霸体状态\n
        [瞬移]\n
        在元素禁域内移动距离 -30%\n
        在元素禁域内冷却时间 -50%
        """
        ...

# 聚能魔炮
# mage_male/elemental_bomber/28b583c75a49103a1d8aabf799c000a4
# a5ccbaf5538981c6ef99b236c0a60b73/28b583c75a49103a1d8aabf799c000a4
class Skill40(ActiveSkill):
    """
    融合火、 冰、 光、 暗四个属性后制造出强力的元素球体， 快速射向前方并引起爆炸。\n
    被球体碰到的敌人会被拖到爆炸地点， 达到一定距离后， 就会引起强烈的爆炸， 对敌人造成所有属性的伤害。\n
    按向前方向键， 可以减少后退距离； 到达最大射程前按下技能键可以立即引发爆炸。\n
    [聚能魔炮]命中敌人后， 5个[元素之力]将会充电。\n
    学习[黑瞳]后会受到[元素禁断]的效果， 可以强制中断其他技能的使用并立即施放[聚能魔炮]。 但是[聚能魔炮]施放过程中， 无法强制中断[聚能魔炮]并施放其他技能。
    """
    name = "聚能魔炮"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [580, 4500]
    uuid = "28b583c75a49103a1d8aabf799c000a4"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # [聚能魔炮]爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [聚能魔炮]\n
        更加频繁的发射强大的浓缩元素球\n
        强化后的元素球体施放时不爆炸， 攻击范围内的敌人后贯穿敌人\n
        元素球体大小 +20%\n
        施放技能时进入无敌状态
        """
        ...

    def vp_2(self):
        """
        [聚能魔炮]\n
        不发射元素球， 在生成的位置引发爆炸\n
         - 角色不会因反作用力向后移动\n
        爆炸范围 +30%\n
        可以利用[元素禁断]强制中断
        """
        ...

# 末日湮灭
# mage_male/elemental_bomber/147d005ac868e0de52b1f255eea35d62
# a5ccbaf5538981c6ef99b236c0a60b73/147d005ac868e0de52b1f255eea35d62
class Skill41(ActiveSkill):
    """
    聚集元素气息射向天空后进行融合， 制造出巨大的元素行星。\n
    融合后的元素行星垂直降落， 使碰到的敌人进入束缚状态， 并对敌人造成多段攻击伤害。\n
    随后穿透进地面的行星引起巨大的爆炸， 对范围内的敌人造成全属性的伤害。\n
    掌握[黑瞳]后会受到[元素禁断]的效果。 但是[末日湮灭]使用过程中无法强制中断并施放其他技能。
    """
    name = "末日湮灭"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "147d005ac868e0de52b1f255eea35d62"
    hasVP = False
    hasUP = False

    # 元素行星冲撞攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 元素行星多段攻击攻击力 : {value1}% x{value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 12
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 元素行星爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1

# 异瞳
# mage_male/elemental_bomber/b8257acad8c7c379aba91ee63c0bd015
# a5ccbaf5538981c6ef99b236c0a60b73/b8257acad8c7c379aba91ee63c0bd015
class Skill42(PassiveSkill):
    """
    知源·元素爆破师掌握黑暗之眼的新力量， 在自己的内心融入小宇宙。\n
    因此而溢出的魔力， 使其中一只眼睛变为异色瞳。\n
    利用[元素禁断]可以连接使用所有转职技能， 并增加基本攻击力和除[雷光链]之外的转职技能攻击力。 同时， 部分技能附加特殊效果。\n
    [元素禁断新增可强制中断的技能]\n
    [聚魔轰击]、 [启源·微观宇宙]\n
    [冰晶坠]\n
    发射全属性的水晶， 将敌人击退至前方一定距离。\n
    [雷光链]\n
    施放时， 发光球在敌人之间快速弹射， 留下雷光球后消失。 \n
    发光球体消失后， 雷光球相互连接， 引发爆炸。
    """
    name = "异瞳"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "b8257acad8c7c379aba91ee63c0bd015"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [雷光链]雷光球爆炸攻击力 : 总攻击力的{value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"data":data0}]

# 聚魔轰击
# mage_male/elemental_bomber/9767a375672d9519f6c1c5dff19b7c15
# a5ccbaf5538981c6ef99b236c0a60b73/9767a375672d9519f6c1c5dff19b7c15
class Skill43(ActiveSkill):
    """
    在自身周围生成小宇宙的黑暗深渊珠。 然后， 向前方释放自身黑暗之眼的魔力和深渊珠的魔力， 攻击敌人。\n
    [聚魔轰击]命中时， 增加5个元素之力。\n
    学习[异瞳]后获得[元素禁断]效果， 可以强制中断其他技能并立即使用[聚魔轰击]， 但无法强制中断[聚魔轰击]后施放其他技能。
    """
    name = "聚魔轰击"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [800, 6667]
    uuid = "9767a375672d9519f6c1c5dff19b7c15"
    hasVP = False
    hasUP = False

    # 能量释放多段攻击力 : {value0}% x{value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 20
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 启源·微观宇宙
# mage_male/elemental_bomber/d58681f38f393dbfd22ffdb049d97002
# a5ccbaf5538981c6ef99b236c0a60b73/d58681f38f393dbfd22ffdb049d97002
class Skill44(ActiveSkill):
    """
    瞬间激活黑暗之眼， 吸收周围的元素能量后， 知源·元素爆破师引爆全身的能量， 引发宇宙的诞生——大爆炸。\n
    学习[异瞳]后获得[元素禁断]效果， 可以强制中断其他技能并立即使用[启源·微观宇宙]， 但无法强制中断[启源·微观宇宙]后施放其他技能。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "启源·微观宇宙"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "d58681f38f393dbfd22ffdb049d97002"
    hasVP = False
    hasUP = False

    # 黑暗之眼激活攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 元素能量吸收多段攻击力 : {value1}% x{value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 12
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 大爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'elemental_bomber'
        self.nameCN = '知源·元素爆破师'
        self.role = 'mage_male'
        self.角色 = '魔法师(男)'
        self.职业 = '元素爆破师'
        self.jobId = 'a5ccbaf5538981c6ef99b236c0a60b73'
        self.jobGrowId = '37495b941da3b1661bc900e68ef3b2c6'

        self.武器选项 = ['矛', '魔杖', '法杖', '棍棒']
        self.输出类型选项 = ['魔法百分比']
        self.输出类型 = '魔法百分比' # TODO
        self.防具精通属性 = ['智力'] # TODO
        self.防具类型 = '布甲'
        self.buff = 2.155

        super().__init__(equVersion, __name__)
