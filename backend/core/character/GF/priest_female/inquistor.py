#0c1b401bb09241570d364420b3ba3fd7
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "priest_female/inquistor/cn/skillDetail"

# 升空斩
# priest_female/inquistor/3c5604bdbb0240b8f130f59ab40509c3
# 0c1b401bb09241570d364420b3ba3fd7/3c5604bdbb0240b8f130f59ab40509c3
class Skill0(ActiveSkill):
    """
        使用巨兵挥击敌人， 使敌人浮空。\n
        浮空力随技能等级的增加而增加。\n
        转职为光明骑士时， 技能类型变为独立攻击力。
    """
    name = "升空斩"
    learnLv = 1
    masterLv = 10
    maxLv = 20
    position = 2 #TODO
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

# 审判锤击
# priest_female/inquistor/c9664191611af31142e052dfaef84530
# 0c1b401bb09241570d364420b3ba3fd7/c9664191611af31142e052dfaef84530
class Skill1(ActiveSkill):
    """
        向巨兵凝聚神圣之力， 锤击前方。\n
        被命中的敌人会浮空。
    """
    name = "审判锤击"
    learnLv = 1
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 4
    mp = [15, 154]
    uuid = "c9664191611af31142e052dfaef84530"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1


# 基础精通
# priest_female/inquistor/5a56514f35cf0270ae8d6c65f8fefd78
# 0c1b401bb09241570d364420b3ba3fd7/5a56514f35cf0270ae8d6c65f8fefd78
class Skill3(PassiveSkill):
    """
        增加基本攻击、 前冲攻击、 跳跃攻击、 [升空斩]的攻击力。\n
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
    associate = [{"type":"*skillDamage","data":[i-100 if i>0 else 0 for i in data0],"skills":["神焰"]}]


# 空中锤击
# priest_female/inquistor/9dda3f4a849dba1a288dd65e116860f2
# 0c1b401bb09241570d364420b3ba3fd7/9dda3f4a849dba1a288dd65e116860f2
class Skill6(ActiveSkill):
    """
        从空中快速向地面俯冲并用巨兵锤击地面， 向后跳跃。\n
        只能在一定高度以上时才能使用。
    """
    name = "空中锤击"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 4
    mp = [10, 120]
    uuid = "9dda3f4a849dba1a288dd65e116860f2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 可以施放技能的最小高度 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 冲击波大小 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)


# 武器格挡
# priest_female/inquistor/eb71e1d82d92c7e1d40500a0dcd77aa6
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
    position = 2 #TODO
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
# priest_female/inquistor/f2fb27162beb0b87a7cb9af7900e95f2
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
    position = 8 #TODO
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
# priest_female/inquistor/01c3a2fb793d293a25ed8dc7a0d70c1a
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
    position = 8 #TODO
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

# 审判者的裁决
# priest_female/inquistor/dcd536f1674630f01fc9667bb202b851
# 0c1b401bb09241570d364420b3ba3fd7/dcd536f1674630f01fc9667bb202b851
class Skill16(PassiveSkill):
    """
        掌握此战术后， 正义审判者可以自如操控战斧和神圣的火焰。 基本攻击会发生变化， 可以在后跳时使用[净化火焰瓶]、 [火焰精华]和跳跃攻击。\n
        可以更加灵活得使用神圣的火焰， 从而使火属性强化值与光属性强化值同步调整为两者中更高的一项数值。
    """
    name = "审判者的裁决"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 2
    uuid = "dcd536f1674630f01fc9667bb202b851"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 后跳攻击的冷却时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 移动速度增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 净化火焰瓶
# priest_female/inquistor/23a5e0fba03283cb1b324a847b3fe370
# 0c1b401bb09241570d364420b3ba3fd7/23a5e0fba03283cb1b324a847b3fe370
class Skill17(ActiveSkill):
    """
        投掷装有地狱火河的火流的火焰瓶。 碰到地面或物体后， 火焰瓶会爆炸， 给敌人造成爆炸伤害和持续伤害。\n
        可以与[火焰精华]一同使用， 触发焚烧效果。\n
        命中敌人时， 造成神焰持续伤害效果。 在[神焰]状态下施放时， 消耗1层神焰能量， 增加攻击力。\n
        [地狱火河的火焰可以焚烧罪恶。 在地狱中， 罪人要承受灵魂被焚烧的痛苦， 罪孽有多深， 要承受的时间就多长。 经过数千年的燃烧， 灵魂烧成灰烬后， 会称那灰烬的重量。 根据重量的大小， 要在罪业的地狱中继续受相应的惩罚。]
    """
    name = "净化火焰瓶"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 6
    mp = [40, 292]
    uuid = "23a5e0fba03283cb1b324a847b3fe370"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 爆炸范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 学习[定罪法则]后， 喷洒范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 惩戒十字
# priest_female/inquistor/0ed3148658fe37b3336ccb718dc0fdb0
# 0c1b401bb09241570d364420b3ba3fd7/0ed3148658fe37b3336ccb718dc0fdb0
class Skill18(ActiveSkill):
    """
        以十字形态进行二段斩击， 惩戒罪恶。\n
        在[神焰]状态下施放时， 消耗1层神焰能量， 给敌人造成持续伤害。\n
        [该技术为教团巨兵战术的基础技术， 礼官的信念越虔诚， 就可以施展出更加精准的十字二段斩。 因此， 这也是教团中常用的体罚动作之一， 教官会让受罚的人一直重复这个动作， 直到挥出让人满意的十字为止。 这也是那些礼官们讨厌这个动作的原因。]
    """
    name = "惩戒十字"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 6
    mp = [40, 292]
    uuid = "0ed3148658fe37b3336ccb718dc0fdb0"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

# 战斧精通
# priest_female/inquistor/762c4e6d030eaf0abbfe1fec2b298574
# 0c1b401bb09241570d364420b3ba3fd7/762c4e6d030eaf0abbfe1fec2b298574
class Skill19(PassiveSkill):
    """
        接受高强度训练的正义审判者可以自如挥舞巨大的战斧。\n
        增加物理武器攻击力， 使用战斧系列武器攻击敌人时， 可以增加攻击速度、 命中率。
    """
    name = "战斧精通"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    uuid = "762c4e6d030eaf0abbfe1fec2b298574"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击速度增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 命中率增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [{"type":"$*PAtkP","data":data0}]

# 裁决之击
# priest_female/inquistor/01384bbfc346775d1267fa0bc4ca605f
# 0c1b401bb09241570d364420b3ba3fd7/01384bbfc346775d1267fa0bc4ca605f
class Skill20(ActiveSkill):
    """
        跳起后， 利用巨兵的重量， 将敌人劈成两半。 下劈时， 可以将周围的敌人击退到打击地点。 可以在空中和后跳中施放， 在空中施放时， 会旋转一圈后捶击前方的敌人。\n
        在[神焰]状态下施放时， 可以额外造成持续伤害， 并消耗1层神焰能量。\n
        地面施放时， 按向前方向键可以跳得更远。\n
        在决斗场中， 无法在一定高度以上施放， 且无法利用方向键增加前进距离。
    """
    name = "裁决之击"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 8
    mp = [30, 252]
    uuid = "01384bbfc346775d1267fa0bc4ca605f"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 火焰精华
# priest_female/inquistor/dc1ffbe7bfcc6dc2be737951960da9ad
# 0c1b401bb09241570d364420b3ba3fd7/dc1ffbe7bfcc6dc2be737951960da9ad
class Skill21(ActiveSkill):
    """
        投掷装有地狱火河之精华的瓶子。 附着精华的敌人受到神焰攻击效果时， 发生爆炸并使敌人进入焚烧状态。\n
    当敌人因[神焰]受到持续伤害时， 用[火焰精华]命中敌人， 会引起强烈的爆炸， 被爆炸波及到的敌人会进入焚烧状态。\n
    [焚烧状态]\n
        敌人会被强烈的神焰所围绕， 同时会被束缚住， 效果持续一定时间。\n
        当敌人进入焚烧状态时， 会一次性受到剩余的神焰持续伤害量。\n
        若瓶子没有击中敌人， 而是掉落地面时， 将形成存在一定时间的精华之坑。\n
        敌人如果碰到精华之坑， 会给敌人沾上精华后消失， 如果对精华之坑发动神焰持续伤害攻击， 可以引爆精华之坑。
    """
    name = "火焰精华"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 3
    cd = 8
    mp = [10, 120]
    uuid = "dc1ffbe7bfcc6dc2be737951960da9ad"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # [神焰]爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 精华持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 焚烧状态的持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 精华之坑持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 精华爆炸范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 学习[神焰恩泽]后， 洒出范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)



# 神焰
# priest_female/inquistor/4b2c90ec226fd40e967875aa5eabefb2
# 0c1b401bb09241570d364420b3ba3fd7/4b2c90ec226fd40e967875aa5eabefb2
class Skill23(ActiveSkill):
    """
        向涂有火焰精华的武器注入神力， 将神焰缠绕在武器上。 在[神焰]状态下， [神焰]的发动攻击力受[基础精通]的影响， 赋予武器光属性和火属性。\n
        学习后， 增加除[火焰精华]之外的基本攻击和转职技能攻击力， 正义审判者使用转职后的技能时， 可以施加与技能攻击力对应的持续伤害， 并消耗1层神焰能量。\n
        在神焰效果下， 若攻击命中敌人， 可以搭配[火焰精华]， 触发焚烧状态， 被击中的敌人进入灼伤状态。\n
        正义审判者施放特定技能后， 可以取消技能僵直， 强制使用[神焰]。\n
    [可以强制使用[神焰]的技能]\n
    [惩戒十字]、 [裁决之击]、 [审判重击]、 [神焰疾降]、 [神焰斩]、 [神焰怒火]、 [净化之焰]、 [行刑]、 [神焰漩涡]、 [逆炎灭罪]、 [裁决轮回斩]、 [补赎逆十字]
    """
    name = "神焰"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 6 #TODO
    rangeLv = 5
    cd = 7
    mp = [30, 252]
    uuid = "4b2c90ec226fd40e967875aa5eabefb2"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 神焰能量层数 : {value0}个
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [神焰]持续伤害攻击力 : 技能攻击力的{value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 神焰伤害持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 施放时攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 除[火焰精华]之外的基本攻击和转职技能攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [灼伤效果]
    # 灼伤攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 灼伤几率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 灼伤持续时间 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [范围信息]
    # 攻击范围比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

    associate = [
        {"data":data1},
        {"data":data4,"exceptSkills":["火焰精华"]}
    ]

# 狂热信仰
# priest_female/inquistor/e49e57b2e8fbeceb0a2c56a0c63fe6c5
# 0c1b401bb09241570d364420b3ba3fd7/e49e57b2e8fbeceb0a2c56a0c63fe6c5
class Skill24(ActiveSkill):
    """
        通过狂热信仰增加物理暴击率和物理暴击伤害。\n
        [信仰带来生命与希望， 忠诚引领未来和方向。]
    """
    name = "狂热信仰"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 4 #TODO
    rangeLv = 3
    cd = 5
    uuid = "e49e57b2e8fbeceb0a2c56a0c63fe6c5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理暴击伤害增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 物理暴击率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 审判重击
# priest_female/inquistor/e4c354a89c337310aeb7041d5e742828
# 0c1b401bb09241570d364420b3ba3fd7/e4c354a89c337310aeb7041d5e742828
class Skill25(ActiveSkill):
    """
        垂直挥舞巨兵， 捶击前方的敌人。\n
        巨兵捶击敌人时， 给敌人造成伤害， 巨兵砸到地面后产生的冲击波会对周围的敌人造成伤害。\n
        在[神焰]状态下施放时， 消耗1层神焰能量， 并额外造成持续伤害。
    """
    name = "审判重击"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 10
    mp = [30, 500]
    uuid = "e4c354a89c337310aeb7041d5e742828"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 下劈攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 冲击波大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 神焰恩泽
# priest_female/inquistor/d53301bb328baf12a3ae482cc6a565dd
# 0c1b401bb09241570d364420b3ba3fd7/d53301bb328baf12a3ae482cc6a565dd
class Skill26(PassiveSkill):
    """
        按住向前键的同时使用[火焰精华]， 可以向前方大范围洒出精华。\n
        配合[神焰]、 [净化火焰瓶]、 [神焰洗礼]的持续伤害效果， 可以引起小型爆炸， 并使敌人进入焚烧状态。
    """
    name = "神焰恩泽"
    learnLv = 30
    masterLv = 1
    maxLv = 1
    position = 6 #TODO
    rangeLv = 2
    uuid = "d53301bb328baf12a3ae482cc6a565dd"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

# 神焰疾降
# priest_female/inquistor/8c10cefa65364880451e389bb74d3600
# 0c1b401bb09241570d364420b3ba3fd7/8c10cefa65364880451e389bb74d3600
class Skill27(ActiveSkill):
    """
        大幅度横向挥动巨兵， 发动大范围斩击审判敌人。\n
        在[神焰]状态下施放时， 消耗1层神焰能量， 增加攻击范围， 并额外造成持续伤害。
    """
    name = "神焰疾降"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 8
    mp = [68, 364]
    uuid = "8c10cefa65364880451e389bb74d3600"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 横斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 神焰洗礼
# priest_female/inquistor/fc7a3f4c2852c832a2f20af63d5d212f
# 0c1b401bb09241570d364420b3ba3fd7/fc7a3f4c2852c832a2f20af63d5d212f
class Skill28(ActiveSkill):
    """
        在审判者的周围洒出精华后， 使用神力点燃精华， 对周围的所有敌人造成伤害， 并触发焚烧状态。\n
        特定技能 (可以用[神焰]强制取消施放后僵直的技能) 可以取消施放后僵直， 并使用[神焰洗礼]。\n
        可以搭配[火焰精华]触发焚烧状态。\n
        命中敌人时， 造成神焰持续伤害效果。  在[神焰]状态下施放时， 消耗1层神焰能量， 可以大幅增加持续伤害的攻击力。\n
        在决斗场中， 不适用[神焰洗礼]洒出精华造成的焚烧状态。
    """
    name = "神焰洗礼"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [45, 850]
    uuid = "fc7a3f4c2852c832a2f20af63d5d212f"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [神焰洗礼]\n
        洒出精华后自动点燃精华\n
         - 洒出后可立即移动\n
        变更为可填充2次的技能\n
         - 每次填充冷却时间 : 7.5秒\n
         - 单次攻击力 -50%\n
         - [净化之焰]攻击力相同
        """
        self.cd = 7.5
        self.skillRation *= 1 - 0.5
        ...

    def vp_2(self):
        """
        [神焰洗礼]\n
        大范围洒出大量精华\n
         - 大幅增加攻击范围\n
         - 施放时自动施放[火焰精华]技能\n
         - 攻击时同时适用[火焰精华]的伤害\n
         - 若[火焰精华]处于冷却时间， 则不发动效果\n
        施放过程中所受伤害 -50%\n
        普通施放时， 攻击范围 +20%
        """
        ...

# 神焰斩
# priest_female/inquistor/128b9ddef2262f40723deae4407bdb42
# 0c1b401bb09241570d364420b3ba3fd7/128b9ddef2262f40723deae4407bdb42
class Skill29(ActiveSkill):
    """
        刺穿前方的敌人后， 大幅度挥舞武器进行处决。 若被刺中的敌人处于焚烧状态， 会给敌人致命一击， 将敌人垂直分为两半。\n
        在[神焰]状态下施放时， 可以消耗1层神焰能量， 额外造成持续伤害。
    """
    name = "神焰斩"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [45, 850]
    uuid = "128b9ddef2262f40723deae4407bdb42"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 刺击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 挥斩攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 0
    # 焚烧状态斩击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 挥斩范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 焚烧状态斩击攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    mode = ["焚烧","常规"]

    def setMode(self, mode):
        if self.vp == 1:
            mode = "焚烧"
        elif self.vp == 2:
            mode = "常规"
        if mode == "焚烧":
            self.hit0 = 1
            self.hit1 = 0
            self.hit2 = 1
        elif mode == "常规":
            self.hit0 = 1
            self.hit1 = 1
            self.hit2 = 0

    def vp_1(self):
        """
        [神焰斩]\n
        仅发动挥斩攻击\n
         - 总攻击力相同\n
         - 挥斩范围 +50%
        """
        ...

    def vp_2(self):
        """
        [神焰斩]\n
        刺击命中时， 固定发动焚烧状态斩击\n
         - 仅限在[神焰]状态下发动\n
         - 斩击攻击后增加无敌判定\n
        刺击y轴范围 +80%
        """
        self.setMode("焚烧")
        ...

# 神焰怒火
# priest_female/inquistor/78be08a3f8c834d3b06fa20c6a08c5a5
# 0c1b401bb09241570d364420b3ba3fd7/78be08a3f8c834d3b06fa20c6a08c5a5
class Skill30(ActiveSkill):
    """
        被激怒的正义审判者施放的连续攻击。 向前方快速连续斩击后， 施放强力的最后一击。\n
        在[神焰]状态下施放时， 消耗1层神焰能量， 并额外造成持续伤害。\n
        攻击过程中按跳跃键， 可以中断攻击。\n
        在决斗场中， 无法用跳跃键中断攻击。
    """
    name = "神焰怒火"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [150, 1260]
    uuid = "78be08a3f8c834d3b06fa20c6a08c5a5"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 连续斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 连斩多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [神焰怒火]\n
        连续斩击命中的敌人将被吸附至正义审判者身前\n
        攻击范围 +30%\n
        施放过程中所受伤害 -90%
        """
        ...

    def vp_2(self):
        """
        [神焰怒火]\n
        连续斩击中可以预输入[审判重击]或[神焰疾降]技能\n
         - 在最后一击发动预输入的技能\n
         - 同时适用现有最后一击的伤害\n
        施放速度 +30%
        """
        ...

# 净化之焰
# priest_female/inquistor/1803b6a67047cafb9e289b4f33cc507b
# 0c1b401bb09241570d364420b3ba3fd7/1803b6a67047cafb9e289b4f33cc507b
class Skill31(ActiveSkill):
    """
        用净化之焰点燃受到[神焰]持续伤害的敌人， 并使触碰到的敌人进入焚烧状态。 只能对受[神焰]持续伤害或处于焚烧状态的敌人使用， 并且在施放动作中处于无敌状态。\n
        [净化之焰]攻击力部分适用[神焰洗礼]的攻击力。\n
        [净化之焰]的施放后僵直可以用转职技能强制取消， 也可以在使用其他技能时， 强制施放[净化之焰]。\n
    [无法强制取消的技能]\n
    [火之净化]、 [炎狱祭坛 : 炮烙]、 [无间业火 : 罪灭神威]、 其他浮空状态的技能。
    """
    name = "净化之焰"
    learnLv = 40
    masterLv = 1
    maxLv = 1
    position = 6 #TODO
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [231, 231]
    uuid = "1803b6a67047cafb9e289b4f33cc507b"
    hasVP = True
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆炸攻击力 : [神焰洗礼]攻击力的 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [范围信息]
    # 爆炸大小比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def skillInfo(self, mode: str | None = None):
        pre = self.char.GetSkillByName("神焰洗礼")
        cd = self.getSkillCD(mode)
        return pre[0] * 0.3 * self.skillRation, self.skillDamage, cd


    def vp_1(self):
        """
        [净化之焰]\n
        施放时， 对600px范围内没有接触到神焰的敌人也产生爆炸\n
         - 爆炸时， 焚烧持续时间 +1秒\n
         - 施放时不消耗神焰能量
        """
        ...

    def vp_2(self):
        """
        [净化之焰]\n
        凝聚神焰之力， 引发巨型爆炸\n
         - 施放时自动施放[神焰]技能\n
         - 同时适用神焰攻击伤害\n
         - 删除焚烧效果\n
         - [神焰]处于冷却时间时不会发动
        """
        ...

# 行刑
# priest_female/inquistor/c27418ae613c647527200a7ca17d97fd
# 0c1b401bb09241570d364420b3ba3fd7/c27418ae613c647527200a7ca17d97fd
class Skill32(ActiveSkill):
    """
        凝聚全身的力量斜向挥舞武器攻击敌人。\n
        在[神焰]状态下施放时， 消耗1层神焰能量， 并额外造成持续伤害。
    """
    name = "行刑"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [250, 2500]
    uuid = "c27418ae613c647527200a7ca17d97fd"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [行刑]\n
        攻击受到神焰持续伤害的敌人时， 将一次性造成剩余的神焰持续伤害量\n
        被命中的敌人进入持续2秒的控制状态\n
         - 仅限在[神焰]状态下发动\n
        施放技能时进入无敌状态\n
        可以蓄气施放\n
         - 维持时间上限 : 1秒
        """
        ...

    def vp_2(self):
        """
        [行刑]\n
        将强大的神焰之力注入武器， 挥动武器行刑\n
         - 仅限在[神焰]状态下发动\n
         - 按向前方向键施放时， 向前移动攻击\n
         - 基本冷却时间变更为67.5秒\n
        总攻击力 +50%
        """
        self.cd = 67.5
        self.skillDamage *= 1.5

# 异徒烙印
# priest_female/inquistor/92360eab6e1f378902018eca681ac629
# 0c1b401bb09241570d364420b3ba3fd7/92360eab6e1f378902018eca681ac629
class Skill33(PassiveSkill):
    """
        增加神焰能量的层数上限， 增加自身基本攻击力和技能攻击力。\n
        在[神焰]状态下攻击命中时， 给敌人画上异徒烙印。
    """
    name = "异徒烙印"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 3
    uuid = "92360eab6e1f378902018eca681ac629"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 神焰能量层数上限 : {value0}层
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [ {"data":data1,"type":"*skillDamage"}]

# 火之净化
# priest_female/inquistor/1fadde0eece18649caddbca7bd58cc2f
# 0c1b401bb09241570d364420b3ba3fd7/1fadde0eece18649caddbca7bd58cc2f
class Skill34(ActiveSkill):
    """
        大幅度挥舞巨兵， 将附近的敌人拽过来绑到火之净化台后， 进行净化。\n
        命中敌人时， 造成神焰持续伤害效果。 在[神焰]状态下施放时， 增加攻击力， 并消耗1层神焰能量。\n
        [恶魔是没有眼泪的， 所以眼泪才是人类纯真的最好证明。 但是， 眼泪却无法证明站在火之净化台上的那个人不是异徒。\n
        哭泣吧， 恶魔！ 来证明你的无辜吧。]
    """
    name = "火之净化"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [881, 7403]
    uuid = "1fadde0eece18649caddbca7bd58cc2f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 挥击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 捶击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [火之净化]攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 15
    # [火之净化]多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 神焰漩涡
# priest_female/inquistor/d0cdaca82892e54097f22a1f60817048
# 0c1b401bb09241570d364420b3ba3fd7/d0cdaca82892e54097f22a1f60817048
class Skill35(ActiveSkill):
    """
        快速旋转巨兵， 斩击周围的敌人。  连续按攻击键或技能键时， 增加旋转圈数和旋转速度， 可以将命中的敌人吸附到前方。 在[神焰]状态下施放时， 可以追加持续伤害， 并消耗1层神焰能量。
    """
    name = "神焰漩涡"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [400, 1620]
    uuid = "d0cdaca82892e54097f22a1f60817048"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 旋转斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 9
    # 旋转多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 连击时多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最后一击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [神焰漩涡]\n
        旋转2圈后可以移动\n
         - 仅限在[神焰]状态下发动\n
         - 固定以最大连击标准发动\n
        攻击范围 +40%
        """
        ...

    def vp_2(self):
        """
        [神焰漩涡]\n
        仅发动旋转斩击攻击\n
         - 总攻击力相同\n
         - 旋转时移动速度 +40%\n
         - 固定以最大连击标准发动\n
        变更为可填充2次的技能\n
         - 每次填充冷却时间 : 12.5秒\n
         - 单次攻击力 -50%
        """
        self.cd = 12.5
        self.skillRation *= 0.5

# 逆炎灭罪
# priest_female/inquistor/38805520deffc10fac2e8f881ab7682b
# 0c1b401bb09241570d364420b3ba3fd7/38805520deffc10fac2e8f881ab7682b
class Skill36(ActiveSkill):
    """
        旋转巨兵向上挥劈后， 使用强力的横斩给背叛者狠狠一击。\n
        旋转巨兵时， 被击中的敌人会被聚集到正义审判者身前， 按向前方向键施放技能时， 可以移动到前方施放技能。\n
        在[神焰]状态下施放时， 可以消耗1层神焰能量， 额外造成持续伤害。
    """
    name = "逆炎灭罪"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [390, 1598]
    uuid = "38805520deffc10fac2e8f881ab7682b"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 向上挥劈攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 横斩攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [逆炎灭罪]\n
        固定使用横斩攻击\n
         - 总攻击力相同\n
        可以强制中断转职技能施放后僵直并施放该技能； 可以强制中断横斩施放后僵直并施放转职技能
        """
        ...

    def vp_2(self):
        """
        [逆炎灭罪]\n
        上挥劈时， 地狱之火的斩击会贯穿前方敌人\n
         - 总攻击力相同\n
         - 斩击前进距离 : 800px\n
        施放时自动进入[神焰]状态\n
         - 将神焰能量层数补充到上限
        """
        ...

# 定罪法则
# priest_female/inquistor/fc458e449ee00b01dbf88d09aae65462
# 0c1b401bb09241570d364420b3ba3fd7/fc458e449ee00b01dbf88d09aae65462
class Skill37(PassiveSkill):
    """
        记录着消灭异徒和魔物方法的手册。 可以学到更有效的战斗技能， 并增加技能攻击力。([火焰精华]技能攻击力以独立的数值增加)\n
        [神焰]\n
        施放动作时进入霸体状态； 减少技能的冷却时间。\n
        [净化火焰瓶]\n
        利用方向键可以强化效果。\n
        [火焰精华]\n
        冷却时间减少， 可以强制中断[神焰]技能的僵直时间， 并且施放[火焰精华]。\n
        增加攻击力 - 提高基本攻击、 跳跃攻击、 冲刺攻击以及正义审判者使用的技能的攻击力。
    """
    name = "定罪法则"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 3
    uuid = "fc458e449ee00b01dbf88d09aae65462"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # [火焰精华]攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 其余所有技能的攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [神焰]、 [火焰精华]技能冷却时间减少率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [
        {"data":data0,"type":"*skillDamage","Skills":["火焰精华"]},
        {"data":data1,"type":"*skillDamage","exceptSkills":["火焰精华"]},
        {"data":data2,"type":"*cdReduce","Skills":["神焰","火焰精华"]}
                 ]

# 裁决轮回斩
# priest_female/inquistor/1812a1ece67bb37b6b44b54766450064
# 0c1b401bb09241570d364420b3ba3fd7/1812a1ece67bb37b6b44b54766450064
class Skill38(ActiveSkill):
    """
        向上挥动武器， 在空中快速旋进行斩击， 然后利用离心力全力劈砍。 劈砍会产生冲击波， 对周围敌人发动攻击。\n
        后跳状态和空中也能使用。 在空中使用时， 从回旋斩击动作开始施展。\n
        在[神焰]状态下施放时， 消耗1层神焰能量， 并额外造成持续伤害。
    """
    name = "裁决轮回斩"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "1812a1ece67bb37b6b44b54766450064"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 回旋斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 回旋斩击多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 劈斩攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 下劈范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [裁决轮回斩]\n
        始终发动空中施放动作\n
         - 空中回转次数 -1次\n
         - 被劈斩命中的敌人将被吸附至中心位置\n
        下劈后触发火焰， 造成多段伤害\n
         - 仅限在[神焰]状态下发动\n
         - 多段攻击次数 : 10次\n
         - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [裁决轮回斩]\n
        向前方跳跃后， 全力劈斩造成伤害\n
         - 总攻击力相同\n
         - 输入前方方向键时增加跳跃距离\n
         - 在[神焰]状态下施放时， 爆发[神焰]的火焰并向周围扩散\n
         - 使被火焰命中的敌人进入焚烧状态
        """
        ...

# 车轮刑
# priest_female/inquistor/d89f26862e348a801b30bb9fd7125db5
# 0c1b401bb09241570d364420b3ba3fd7/d89f26862e348a801b30bb9fd7125db5
class Skill39(ActiveSkill):
    """
        利用燃烧的车轮消灭前方敌人。\n
        从地面抽出巨大的车轮， 然后注入神焰使其滚动， 进行多段攻击， 同时将触碰到的敌人拖拽至车轮的中心。\n
        如果把[火焰精华]浇在车轮上， 可以使被攻击到的敌人进入焚烧状态。\n
        命中敌人时， 造成神焰持续伤害效果。 在[神焰]状态下施放时， 消耗1层神焰能量， 增加攻击力。
    """
    name = "车轮刑"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 2 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [600, 5000]
    uuid = "d89f26862e348a801b30bb9fd7125db5"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 向上攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 车轮攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 25
    # 车轮多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最终爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 车轮大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [车轮刑]\n
        车轮滚动速度 +70%\n
        车轮攻击变更为可以拖拽控制和霸体状态的对象\n
        车轮大小 +20% 
        """
        ...

    def vp_2(self):
        """
        [车轮刑]\n
        可以在[审判重击]、 [裁决轮回斩]、 [补赎逆十字]技能施放过程中预输入施放\n
         - 预输入施放时， 在目标技能的最后一击后， 车轮从地面弹起\n
        基本冷却时间变更为22.5秒\n
        总攻击力 -50%
        """
        self.cd = 22.5
        self.skillRation *= 0.5

# 炎狱祭坛 : 炮烙
# priest_female/inquistor/2ba299855fc22192cba4f73db75e9d0e
# 0c1b401bb09241570d364420b3ba3fd7/2ba299855fc22192cba4f73db75e9d0e
class Skill40(ActiveSkill):
    """
        使用最精粹的神焰形成炎狱祭坛 : 炮烙净化敌人。\n
        命中敌人时， 产生神焰持续伤害效果。 在[神焰]状态下施放时， 消耗1层神焰能量， 增加攻击力。
    """
    name = "炎狱祭坛 : 炮烙"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "2ba299855fc22192cba4f73db75e9d0e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 冲击波攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 冲击波多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后一击斩击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

# 狂炎告解
# priest_female/inquistor/ab6fc3303df03b58911967dfca2b5d07
# 0c1b401bb09241570d364420b3ba3fd7/ab6fc3303df03b58911967dfca2b5d07
class Skill41(PassiveSkill):
    """
        正义审判者投身于神焰， 进行狂热的告解圣事。\n
        完成告解的光启·正义审判者， 不顾自己也会被神焰吞噬的危险， 审判敌人。\n
        增加[神焰]能量层数上限， 增加基本攻击力和转职技能攻击力 ([裁决之击]、 [审判重击]除外)， 部分技能附加特殊效果。\n
    [裁决之击]\n
        在地面上施放技能时， 发动前冲攻击； 前冲攻击后再次按技能键， 发动跳跃攻击。 此时可利用左右方向键控制跳跃攻击的方向。\n
    [审判重击]\n
        在[神焰]状态下施放时， 在攻击范围内生成多段伤害的烈炎地带， 效果持续一段时间。\n
        [若神能宽恕我的忏悔， 那我就不会燃烧； 否则， 我也是必须被焚烧的异徒。 我又怎么会惧怕火焰呢？]
    """
    name = "狂炎告解"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "ab6fc3303df03b58911967dfca2b5d07"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 神焰能量增加 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [裁决之击]
    # [裁决之击]前冲攻击力 : 总攻击力的{value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [审判重击]
    # [审判重击]火焰地带多段攻击力 : 总攻击力的{value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [审判重击]火焰地带多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [审判重击]火焰地带持续时间 : 2秒

    associate = [
        {"data":data0,"type":"*skillDamage"},
        {"data":data3*data4,"type":"*skillDamage","Skills":["审判重击"]}
                 ]

# 补赎逆十字
# priest_female/inquistor/c91a62dc0a18360acf5031ac0ebf09f5
# 0c1b401bb09241570d364420b3ba3fd7/c91a62dc0a18360acf5031ac0ebf09f5
class Skill42(ActiveSkill):
    """
        将强大到足以吞噬自己的神焰之力注入武器， 挥动武器， 对敌人处以燃烧的逆十字刑罚。\n
        挥击命中时， 将敌人击退到前方出现的逆十字位置， 逆十字命中时使敌人无法移动， 直到逆十字消失。\n
        如果把[火焰精华]浇在逆十字上， 可以使命中的敌人进入焚烧状态。\n
        命中敌人时， 造成神焰持续伤害效果。\n
        在[神焰]状态下施放时， 消耗1层神焰能量， 增加攻击力。
    """
    name = "补赎逆十字"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [800, 6667]
    uuid = "c91a62dc0a18360acf5031ac0ebf09f5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 横向挥击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 纵向挥击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 逆十字攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 20
    # 逆十字多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 逆十字持续时间 : 2秒

# 无间业火 : 罪灭神威
# priest_female/inquistor/0c3a468aee1f7ce06bf91eb3319518c1
# 0c1b401bb09241570d364420b3ba3fd7/0c3a468aee1f7ce06bf91eb3319518c1
class Skill43(ActiveSkill):
    """
        光启·正义审判者召唤出业火祭坛束缚敌人， 默念神下达的神圣使命。\n
        然后， 在熊熊燃烧的地狱劫火中， 审判敌人的肉身和罪恶。\n
        施放后， 自动进入神焰状态， 并将神焰能量层数补充到上限。\n
        在神焰状态下施放时， 额外造成持续伤害， 并消耗1层神焰能量。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "无间业火 : 罪灭神威"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "0c3a468aee1f7ce06bf91eb3319518c1"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 业火祭坛攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 挥击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 下捶攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 终结多段攻击力: {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 8
    # 终结多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'inquistor'
        self.nameCN = '神启·异端审判者'
        self.role = 'priest_female'
        self.角色 = '圣职者(女)'
        self.职业 = '异端审判者'
        self.jobId = '0c1b401bb09241570d364420b3ba3fd7'
        self.jobGrowId = '618326026de1a1f1cfba5dbd0b8396e7'

        self.武器选项 = ['光杖','念珠','图腾','镰刀','战斧']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '重甲'
        self.buff = 2.002

        super().__init__(equVersion, __name__)
