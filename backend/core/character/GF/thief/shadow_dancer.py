#ddc49e9ad1ff72a00b53c6cff5b1e920
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "thief/shadow_dancer/cn/skillDetail"


# 基础精通
# thief/shadow_dancer/5a56514f35cf0270ae8d6c65f8fefd78
# ddc49e9ad1ff72a00b53c6cff5b1e920/5a56514f35cf0270ae8d6c65f8fefd78
class Skill3(PassiveSkill):
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
    icon = "$common/$uuid"
    hasVP = False
    hasUP = False

    # 基本攻击力变化率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 前冲攻击力变化率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 跳跃攻击力变化率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)



# 切割
# thief/shadow_dancer/9dda3f4a849dba1a288dd65e116860f2
# ddc49e9ad1ff72a00b53c6cff5b1e920/9dda3f4a849dba1a288dd65e116860f2
class Skill6(ActiveSkill):
    """
    前冲攻击中输入攻击键时， 施放追加斩击。\n
    攻击力、 攻击范围、 前进速度和前进距离随技能等级增加而增大。
    """
    name = "切割"
    learnLv = 5
    masterLv = 1
    maxLv = 6
    position = 3 #TODO
    rangeLv = 2
    cd = 2.5
    mp = [6, 56]
    uuid = "9dda3f4a849dba1a288dd65e116860f2"
    hasVP = False
    hasUP = False

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 前冲速度和距离比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)


# 影袭
# thief/shadow_dancer/c9664191611af31142e052dfaef84530
# ddc49e9ad1ff72a00b53c6cff5b1e920/c9664191611af31142e052dfaef84530
class Skill8(ActiveSkill):
    """
    以无视敌人硬直的斩击攻击敌人， 使敌人受到无属性物理伤害的同时进入僵直状态； 之后移动到敌人身后， 伺机进行下一次攻击。\n
    转职为影舞者时， 可以强制控制敌人。\n
    在决斗场中， 无法强制控制敌人， 但是相比其他暗夜使者， 可以使敌人进入更长时间的僵直状态。
    """
    name = "影袭"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 6
    mp = [15, 168]
    uuid = "c9664191611af31142e052dfaef84530"
    hasVP = False
    hasUP = False

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 敌人僵直时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # - [转职为影舞者时] -
    # 僵直时间比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)


# 骨盾
# thief/shadow_dancer/ff171dc487807bb9aa28900ca9a46b41
# ddc49e9ad1ff72a00b53c6cff5b1e920/ff171dc487807bb9aa28900ca9a46b41
class Skill11(ActiveSkill):
    """
    在自身或队员周围召唤由骨头碎片形成的骨盾， 可以增加被骨盾守护的角色的物理防御力和魔法防御力。\n
    该角色被攻击时， 骨头碎片会自动飞向敌人， 并使敌人受到无属性魔法伤害。\n
    每次被攻击时， 骨头碎片会逐块消失。 当骨头碎片全部消失时， 增加的物理防御力和魔法防御力效果就会消失。\n
    [转职为黑夜术士后功能变更]\n
    减少骨盾的持续时间。\n
    学习后减少所受伤害， 施放技能后被攻击一定次数内附加霸体护甲。\n
    可以在其他动作中施放， 不受冷却时间减少效果的影响。\n
    在决斗场中， 不适用持续时间减少和霸体护甲效果， 施放技能时减少所受伤害。
    """
    name = "骨盾"
    learnLv = 10
    masterLv = 1
    maxLv = 7
    position = 1 #TODO
    rangeLv = 3
    cd = 15
    mp = [20, 400]
    uuid = "ff171dc487807bb9aa28900ca9a46b41"
    hasVP = False
    hasUP = False

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 骨盾持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 骨头碎片数量 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 魔法防御力增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 物理防御力增加 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 发射骨头碎片冷却时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [转职为黑夜术士后]
    # 持续时间减少率 : 85%
    # 所受伤害减少率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 霸体护甲生效次数 : {value7}次
    data7 = get_data(f'{prefix}/{uuid}', 7)



# 天诛
# thief/shadow_dancer/f2fb27162beb0b87a7cb9af7900e95f2
# ddc49e9ad1ff72a00b53c6cff5b1e920/f2fb27162beb0b87a7cb9af7900e95f2
class Skill18(ActiveSkill):
    """
    抓取一名敌人后向其头部进行刺击， 被刺击命中的敌人将受到无属性伤害。\n
    若[天诛]背击敌人时， 则会追加一次刺击， 且最后还会追加一次高伤害的切割攻击。
    """
    name = "天诛"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    line = 10
    rangeLv = 2
    cd = 7
    mp = [28, 308]
    uuid = "f2fb27162beb0b87a7cb9af7900e95f2"
    hasVP = False
    hasUP = True

    # 刺击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2
    # 刺击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 切割攻击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1


# 潜行教义
# thief/shadow_dancer/e0daa922b19cdc35de879e938361464e
# ddc49e9ad1ff72a00b53c6cff5b1e920/e0daa922b19cdc35de879e938361464e
class Skill20(PassiveSkill):
    """
    影舞者特有的潜行术。 进行背后攻击时， 敌人的被击方向不会改变， 强控敌人时， 敌人的方向也不会改变。 若技能的首次攻击判定为从背后命中敌人， 则该技能施放结束为止都维持背击判定。 另外， 基本攻击、 [弧光闪]、 [天诛]、 [碎踝]的攻击效果会产生变化， 且增加暴击伤害。\n
    [弧光闪] : 移动速度不变， 通过追加操作可以进行一次追加攻击。 使用[弧光闪]进行背后攻击时， 敌人会转向攻击的方向。\n
    [天诛] : 变更最后一击的特效， 并且对无法抓取的敌人进行踢腿攻击。\n
    [碎踝] : 使被击中的敌人向后回头。\n
    影舞者基本攻击第三击 : 使被击中的敌人向后回头。
    """
    name = "潜行教义"
    learnLv = 15
    masterLv = 1
    maxLv = 11
    position = 3 #TODO
    rangeLv = 3
    uuid = "e0daa922b19cdc35de879e938361464e"
    hasVP = False
    hasUP = False

    # 暴击伤害增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]

# 追影步
# thief/shadow_dancer/0fbb8de70002ad34f046c94c2cb3e863
# ddc49e9ad1ff72a00b53c6cff5b1e920/0fbb8de70002ad34f046c94c2cb3e863
class Skill21(ActiveSkill):
    """
    向前快速移动， 若移动途中碰到敌人， 将会移动到敌人的背后。 施放该技能时， 可以强制中断某些指定技能的施放， 某些技能被强制中断时， 会制造暗袭分身完成未完成的动作。
    """
    name = "追影步"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 7 #TODO
    rangeLv = 1
    cd = 3
    mp = [50, 50]
    uuid = "0fbb8de70002ad34f046c94c2cb3e863"
    hasVP = False
    hasUP = False


# 撕裂
# thief/shadow_dancer/c5a2956d8ed3af1746ed2f76ca971a09
# ddc49e9ad1ff72a00b53c6cff5b1e920/c5a2956d8ed3af1746ed2f76ca971a09
class Skill22(ActiveSkill):
    """
    使用武器向下攻击敌人。 如果命中敌人背部， 将会进行追加攻击。 此技能可在空中使用， 在空中使用时， 会垂直下落并向下攻击敌人。 技能命中敌人后， 使用[挑空]可以与其他技能形成连招。
    """
    name = "撕裂"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 6
    mp = [30, 252]
    uuid = "c5a2956d8ed3af1746ed2f76ca971a09"
    hasVP = False
    hasUP = True

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 追加斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

# 潜行之匕首精通
# thief/shadow_dancer/e5c09f9132a48dc1d695968592cc5878
# ddc49e9ad1ff72a00b53c6cff5b1e920/e5c09f9132a48dc1d695968592cc5878
class Skill23(PassiveSkill):
    """
    增加武器物理攻击力， 使用匕首系列武器时， 增加命中率。 攻击时对敌人造成的僵直时间提高至双剑水准。\n
    在决斗场中， 不会增加僵直时间。
    """
    name = "潜行之匕首精通"
    learnLv = 20
    masterLv = 20
    maxLv = 30
    position = 3 #TODO
    rangeLv = 3
    uuid = "e5c09f9132a48dc1d695968592cc5878"
    hasVP = False
    hasUP = False

    # 武器物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 命中率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [{"data":data0,"type":"$*PAtkP"}]

# 挑空
# thief/shadow_dancer/e0a072e8cef2d77893aad5f68aeed56a
# ddc49e9ad1ff72a00b53c6cff5b1e920/e0a072e8cef2d77893aad5f68aeed56a
class Skill24(ActiveSkill):
    """
    从地面垂直对敌人发出上挑攻击。 击中倒地或者浮在低空中的敌人可以挑起对方。 被击中的敌人会进入无视硬直的僵直状态。\n
    在决斗场对倒地的敌人使用时， 不会挑起对方， 而是让敌人浮在空中。
    """
    name = "挑空"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 3
    mp = [40, 292]
    uuid = "e0a072e8cef2d77893aad5f68aeed56a"
    hasVP = False
    hasUP = True

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 可抓取高度 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 僵直时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 潜行领域
# thief/shadow_dancer/7ec521d063d2190e1fcc5bd229af9bcf
# ddc49e9ad1ff72a00b53c6cff5b1e920/7ec521d063d2190e1fcc5bd229af9bcf
class Skill25(ActiveSkill):
    """
    影舞者先贤为了弥补影舞者攻击范围不足而创造的领域技能。 指定的技能命中敌人背部时， 会召唤暗袭分身攻击附近的敌人。\n
    暗袭分身的攻击力等同于施放的技能攻击力。 再次按技能键时， 取消技能。\n
    随着技能等级的增加， 背击时可以产生暗袭分身的技能的种类也会增加。\n
    1级 - 基本攻击第4击、 [天诛]、 [撕裂]、 [挑空]\n
    2级 - [穿心]\n
    3级 - [追袭]\n
    4级 - [刃舞]、 [潜影刺击]\n
    5级 - [影戮]\n
    6级 - [瞬袭]\n
    7级 - [绝境飞刃]\n
    8级 - [八荒影杀]\n
    9级 - [死亡连舞]\n
    10级 - [摧心]、 [幽冥链狱 : 瞬逝]、 [影缚追魂锁]
    """
    name = "潜行领域"
    learnLv = 20
    masterLv = 1
    maxLv = 10
    position = 7 #TODO
    rangeLv = 5
    cd = 5
    mp = [128, 128]
    uuid = "7ec521d063d2190e1fcc5bd229af9bcf"
    hasVP = False
    hasUP = False

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击第4击的暗袭分身攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [绝境飞刃]第1击的暗袭分身攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [八荒影杀]、 [撕裂]的暗袭分身攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [穿心]的暗袭分身攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [天诛]、 [挑空]、 [追袭]、 [瞬袭]的暗袭分身最终一击攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [影戮]、 [死亡连舞]、 [幽冥链狱 : 瞬逝]、 [摧心]暗袭分身最终一击攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [刃舞]暗袭分身最终一击攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [幽冥链狱 : 瞬逝]射出锁链攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [潜影刺击]暗袭分身最终一击攻击力 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [影缚追魂锁]暗影爆炸攻击力 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)

# 穿心
# thief/shadow_dancer/2a0a39184de92acf1c1375e00b77404c
# ddc49e9ad1ff72a00b53c6cff5b1e920/2a0a39184de92acf1c1375e00b77404c
class Skill27(ActiveSkill):
    """
    以锐利的角度刺向敌人的要害。 技能命中敌人背部时， 会发动剜出敌人心脏的要害攻击， 同时让敌人进入僵直状态。\n
    被要害攻击命中的敌人将会减少硬直最大值， 并使敌人背面朝向影舞者。\n
    对无法抓取的敌人不适用控制效果。
    """
    name = "穿心"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 8
    mp = [30, 500]
    uuid = "2a0a39184de92acf1c1375e00b77404c"
    hasVP = False
    hasUP = True

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 追加斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 被追加斩击攻击的敌人的硬直度固定值 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 硬直持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 影遁
# thief/shadow_dancer/9dc8438e4572d39243c97da31c113acc
# ddc49e9ad1ff72a00b53c6cff5b1e920/9dc8438e4572d39243c97da31c113acc
class Skill28(ActiveSkill):
    """
    召唤出挑衅敌人的暗袭分身， 并且在一段时间内变为隐身状态进行突进。
    """
    name = "影遁"
    learnLv = 25
    masterLv = 1
    maxLv = 1
    position = 3 #TODO
    rangeLv = 5
    cd = 10
    mp = [150, 150]
    uuid = "9dc8438e4572d39243c97da31c113acc"
    hasVP = False
    hasUP = False

    # 分身的生命值比率 : 角色生命值的{value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 分身的挑衅范围 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 隐身状态持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 隐身状态下物理暴击率增加量 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 潜行信条
# thief/shadow_dancer/7f80b887a09e88e2c4728c898bd73654
# ddc49e9ad1ff72a00b53c6cff5b1e920/7f80b887a09e88e2c4728c898bd73654
class Skill29(ActiveSkill):
    """
    增加暴击率和暴击伤害。\n
    追踪者的五种美德。\n
    忍耐、 集中、 冷静、 沉着、 任务至上。 (节选自教科书《潜伏的定式》)
    """
    name = "潜行信条"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 3 #TODO
    rangeLv = 3
    cd = 5
    uuid = "7f80b887a09e88e2c4728c898bd73654"
    hasVP = False
    hasUP = False

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 暴击伤害增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 追袭
# thief/shadow_dancer/3fb8395ae3b81bd608e0c4223a8eb534
# ddc49e9ad1ff72a00b53c6cff5b1e920/3fb8395ae3b81bd608e0c4223a8eb534
class Skill30(ActiveSkill):
    """
    利用离心力将抓取到的敌人用力按在地面上， 同时引发冲击波。 可以在空中使用该技能。 如果技能命中敌人背部， 冲击波的攻击力和范围会增加。\n
    在地面使用技能时， 跳跃较长距离进行攻击。 通过方向键可以调整中/远距离以及Y轴的移动方向。\n
    在空中使用技能时， 会把敌人按在正前方的地面上。 [后跳]过程中也可以使用空中[追袭]。
    """
    name = "追袭"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cd = 10
    mp = [50, 420]
    uuid = "3fb8395ae3b81bd608e0c4223a8eb534"
    hasVP = False
    hasUP = True

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    power0 = 1.5
    # 背击时攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 冲击波范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 刃舞
# thief/shadow_dancer/5806440d21e7546d50007a5ba11f8024
# ddc49e9ad1ff72a00b53c6cff5b1e920/5806440d21e7546d50007a5ba11f8024
class Skill31(ActiveSkill):
    """
    猛烈挥舞手中的剑刃， 对周围的敌人进行攻击。 施放过程中， 按下Z键或跳跃键， 可以快速施放最后的斩击。
    """
    name = "刃舞"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [45, 850]
    uuid = "5806440d21e7546d50007a5ba11f8024"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 回旋斩击攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 19
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 回旋范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [刃舞]\n
        剑刃大小 +20%\n
        移动速度 +200%\n
        吸附力 +400%\n
        多段攻击次数 +100%
        """
        ...

    def vp_2(self):
        """
        [刃舞]\n
        通过[追影步]强制中断时\n
        影子会跟随施放者继续施放[刃舞]\n
        剑刃大小 +10%\n
        多段攻击次数 -6次\n
        总攻击力相同
        """
        ...

# 潜影刺击
# thief/shadow_dancer/c524c4f378d1cd0ff99e4580750a4567
# ddc49e9ad1ff72a00b53c6cff5b1e920/c524c4f378d1cd0ff99e4580750a4567
class Skill32(ActiveSkill):
    """
    快速挥斩两次后， 移动到敌人背后， 最后强力刺击敌人要害。 从背后命中敌人时， 可以造成更深的伤口。
    """
    name = "潜影刺击"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [126, 1058]
    uuid = "c524c4f378d1cd0ff99e4580750a4567"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 连续挥斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2
    # 最后一击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 背击最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

    def vp_1(self):
        """
        [潜影刺击]\n
        移动到[潜行领域]范围内的敌人后方\n
        始终以背击攻击
        """
        ...

    def vp_2(self):
        """
        [潜影刺击]\n
        隐匿身形后发动连续攻击\n
         - 聚集敌人后在原本位置现身并发动强烈一击\n
         - 隐匿身形时进入无敌状态
        """
        ...

# 影戮
# thief/shadow_dancer/d429147c372b549c3dadcabcba50787f
# ddc49e9ad1ff72a00b53c6cff5b1e920/d429147c372b549c3dadcabcba50787f
class Skill33(ActiveSkill):
    """
    通过华丽而致命的乱舞斩击毁灭敌人。\n
    命中敌人背部时， 会施放强力的斩击将敌人斩为两半。\n
    命中敌人时， 使用[追影步]可以让暗袭分身继续进行该技能的剩余动作。\n
    在决斗场中， 只有当影戮攻击命中目标时， 可以用追影步强行停止分身。
    """
    name = "影戮"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [150, 1260]
    uuid = "d429147c372b549c3dadcabcba50787f"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 乱舞攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 上斩攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 下劈攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 背击时最终一击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1

    def vp_1(self):
        """
        [影戮]\n
        [影戮]施放过程中\n
        通过[追影步]强制中断时\n
        初始化[追影步]的冷却时间\n
        最后一击攻击速度增加\n
        每次攻击都追踪被命中的敌人\n
        背击成功后立即进入无敌状态
        """
        ...

    def vp_2(self):
        """
        [影戮]\n
        生成致命的暗影， 并进行下劈攻击\n
         - 可以在其他动作中施放\n
         - 始终以背击攻击\n
        在下劈的位置生成代替[潜行领域]的强化版[潜行领域]\n
         - 在强化版[潜行领域]内攻击敌人时， 始终以背击攻击\n
         - 持续时间5秒\n
         - 技能结束时， 变回[潜行领域]\n
        基本冷却时间变更为31.25秒\n
        攻击力 +25%
        """
        self.cd = 31.25
        self.skillRation *= 1.25
        ...

# 瞬袭
# thief/shadow_dancer/0113c8b1306ca76d208f83f2d093dd62
# ddc49e9ad1ff72a00b53c6cff5b1e920/0113c8b1306ca76d208f83f2d093dd62
class Skill34(ActiveSkill):
    """
    悄无声息地接近敌人进行攻击。 被攻击的对象的生命值越少， 受到的伤害越高。
    """
    name = "瞬袭"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [250, 2500]
    uuid = "0113c8b1306ca76d208f83f2d093dd62"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 背后偷袭攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 正面偷袭攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 对生命值低的对象攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 普通怪物被击毙的生命值比率 : 低于{value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 稀有怪物被击毙的生命值比率 : 低于{value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 领主怪物被击毙的生命值比率 : 低于{value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [瞬袭]\n
        删除攻击命中后僵直\n
        Y轴攻击范围增加
        """
        ...

    def vp_2(self):
        """
        [瞬袭]\n
        触发攻击力增加效果所需的生命值比率增加\n
        普通 : 低于100%\n
        稀有 : 低于90%\n
        领主 : 低于60%\n
        攻击力增加率减少至12.5%
        """
        ...

# 潜行之心
# thief/shadow_dancer/c91a62dc0a18360acf5031ac0ebf09f5
# ddc49e9ad1ff72a00b53c6cff5b1e920/c91a62dc0a18360acf5031ac0ebf09f5
class Skill35(PassiveSkill):
    """
    死亡舞会所属要员必须掌握的潜行术， 可以准确的从背后命中目标的要害。\n
    技能命中敌人背部时， 会增加攻击力和暴击率。
    """
    name = "潜行之心"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 3
    uuid = "c91a62dc0a18360acf5031ac0ebf09f5"
    hasVP = False
    hasUP = False

    # 背击时暴击几率增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 背击时攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [{"data":data1}]

# 影斩·乱舞
# thief/shadow_dancer/8b08f9504167a9c0f3a1d29d71b7943e
# ddc49e9ad1ff72a00b53c6cff5b1e920/8b08f9504167a9c0f3a1d29d71b7943e
class Skill36(ActiveSkill):
    """
    梦魇会在大范围内进行快速移动并斩击敌人。 每次斩击都会制造一个暗袭分身进行攻击， 最后在暗袭分身和梦魇的夹击下颠覆空间。 连续按攻击键， 可以加快施放速度。 按前或下方向键， 可以在原地发动最终一击。
    """
    name = "影斩·乱舞"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 5
    cube = 7
    cd = 145
    mp = [881, 7403]
    uuid = "8b08f9504167a9c0f3a1d29d71b7943e"
    hasVP = False
    hasUP = False

    # 连续斩击攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 12
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最终一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

# 绝境飞刃
# thief/shadow_dancer/ac21c02567f04a92b54dd85c091d1e5a
# ddc49e9ad1ff72a00b53c6cff5b1e920/ac21c02567f04a92b54dd85c091d1e5a
class Skill37(ActiveSkill):
    """
    投掷匕首， 将匕首掷入敌人的身体里， 可在空中进行投掷。 匕首会在敌人身体内滞留一段时间， 此时再次输入技能键， 影舞者会接近敌人背后， 随后拔出匕首进行一次攻击。
    """
    name = "绝境飞刃"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [400, 1620]
    uuid = "ac21c02567f04a92b54dd85c091d1e5a"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 匕首滞留敌人身体的时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 投掷攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 第一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 最终一击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1

    def vp_1(self):
        """
        [绝境飞刃]\n
        可以立即中断影舞者的当前动作并拔出匕首进行攻击\n
        投掷匕首时会追踪最强的敌人\n
        Y轴追踪范围 +460%
        """
        ...

    def vp_2(self):
        """
        [绝境飞刃]\n
        向前方所有敌人投掷匕首后\n
        影子现身在敌人背后并造成伤害\n
         - 向[潜行领域]范围内的敌人投掷\n
         - 最多向10个敌人投掷\n
         - 无法追加输入\
         - 可以强制中断影舞者的当前动作， 并投掷匕首进行攻击\
         - 总攻击力相同
        """
        ...

# 八荒影杀
# thief/shadow_dancer/ab6fc3303df03b58911967dfca2b5d07
# ddc49e9ad1ff72a00b53c6cff5b1e920/ab6fc3303df03b58911967dfca2b5d07
class Skill38(ActiveSkill):
    """
    对敌人进行斩击， 随后制造暗袭分身， 从八个方向同时斩击敌人。
    """
    name = "八荒影杀"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [800, 1680]
    uuid = "ab6fc3303df03b58911967dfca2b5d07"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 分身攻击力 : {value2}% X {value3}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 7
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 背击时最终一击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1

    def vp_1(self):
        """
        [八荒影杀]\n
        召唤幽冥暗影， 对敌人发动肆意攻击\n
         - 可移动到目标敌人位置或改变敌人的位置， 与[幽冥链狱 : 瞬逝]共享指令和动作\n
        (强控、 聚集敌人、 最后一击除外)\n
         - 与[幽冥链狱 : 瞬逝]共享强制中断其他技能的功能\n
         - 始终以背击攻击\n
        变更为可填充4次的技能\n
         - 每次填充冷却时间12.5秒\n
        - 每次攻击力 -75%\n
        在[幽冥链狱 : 瞬逝]状态下， 技能命中敌人时， 消耗所有填充次数， 并发动强力的终结攻击
        """
        self.cd = 12.5
        self.skillRation *= 1 - 0.75  # noqa: E501
        ...

    def vp_2(self):
        """
        [八荒影杀]\n
        施放[八荒影杀]过程中可以施放影舞者转职技能\n
        发动该功能时， 会通过[追影步]施放该技能\n
        [幽冥链狱 : 瞬逝]状态下， 成功命中时， [幽冥链狱 : 瞬逝]持续时间 +5秒
        """
        ...

# 死亡连舞
# thief/shadow_dancer/6e33d47e6622ce03b6defdd912140270
# ddc49e9ad1ff72a00b53c6cff5b1e920/6e33d47e6622ce03b6defdd912140270
class Skill39(ActiveSkill):
    """
    抓住敌人后， 使用迅速、 干净利落的动作对要害进行连续攻击。\n
    从背后进行攻击时， 会施放强力的追加攻击。\n
    对不可抓取敌人省略部分中间动作，增加最后一击攻击力。 
    """
    name = "死亡连舞"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "6e33d47e6622ce03b6defdd912140270"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 连续攻击攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 6
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 背击追加攻击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 对无法抓取的敌人最后一击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    mode = ["抓取", "不可抓取"]  # noqa: E501

    def setMode(self, mode):
        if mode == "抓取":
            self.hit0 = 6
            self.hit2 = self.hit3 = 1
            self.hit4 = 0
        elif mode == "不可抓取":
            self.hit0 = 3
            self.hit2 = self.hit3 = 0
            self.hit4 = 1

    def vp_1(self):
        """
        [死亡连舞]\n
        成功背击且最后一击命中时\n
        初始化[追影步]的冷却时间\n
        [潜行领域]范围 +20%， 效果持续15秒 
        """
        ...

    def vp_2(self):
        """
        [死亡连舞]\n
        最后一击命中时\n
        初始化[影遁]的冷却时间\n
        以无法抓取的形态发动
        """
        self.setMode("不可抓取")  # noqa: E501
        ...

# 潜行之袭
# thief/shadow_dancer/51a08fd0c90f0a5276cd552047fac93d
# ddc49e9ad1ff72a00b53c6cff5b1e920/51a08fd0c90f0a5276cd552047fac93d
class Skill40(PassiveSkill):
    """
    增加自身基本攻击力和技能攻击力， 技能施放过程中可以使用[影遁]。
    """
    name = "潜行之袭"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 3
    uuid = "51a08fd0c90f0a5276cd552047fac93d"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]

# 摧心
# thief/shadow_dancer/b163d099c8cc27fdb6fd3639c2ee6df9
# ddc49e9ad1ff72a00b53c6cff5b1e920/b163d099c8cc27fdb6fd3639c2ee6df9
class Skill41(ActiveSkill):
    """
    用绚丽旋转的步伐对前方敌人进行攻击。 如果命中敌人的正面， 用强烈的旋转力施加重击。 如果命中敌人的背部， 则会将敌人的要害握在手里， 随后引起爆炸。
    """
    name = "摧心"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "b163d099c8cc27fdb6fd3639c2ee6df9"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 正面旋转重击的攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 背后摘取攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

    def vp_1(self):
        """
        [摧心]\n
        [潜行领域]暗袭分身向范围内最强敌人移动， 攻击其要害\n
        固定以背击命中
        """
        ...

    def vp_2(self):
        """
        [摧心]\n
        正面攻击力 -99%\n
        背击未命中时， 冷却时间缩短为5秒\n
        背击攻击命中后， [追影步]冷却时间变更为0.5秒， 效果持续4秒
        """
        ...

# 幽冥链狱 : 瞬逝
# thief/shadow_dancer/28b583c75a49103a1d8aabf799c000a4
# ddc49e9ad1ff72a00b53c6cff5b1e920/28b583c75a49103a1d8aabf799c000a4
class Skill42(ActiveSkill):
    """
    使用末端连接锁链的匕首， 对敌人进行攻击。\n
    技能的过程中按下技能键时， 可以射出锁链。 可以在空中射出锁链， 也可以强制中断特定技能后射出锁链。 如果锁链插中敌人， 可以通过追加操作进行其他的动作。\n
    未按键 : 把敌人拉到自己面前。\n
    X键 : 靠近敌人并进行攻击。\n
    X键 + 后方向键 : 靠近敌人后转换位置， 并进行强力一击。\n
    空格键 : 把锁链插到地面上， 束缚敌人一段时间。 此动作有另外的冷却时间。\n
    空格 + ↓键 : 用锁链和影分身将目标周围的敌人聚拢， 并攻击造成伤害。 该动作与按空格键的动作共享冷却时间。\n
    再次按下技能键 : 施放强力终结攻击。\n
    可以强制中断的技能 : [翔击]、 [切割]、 [弧光闪]、 [影袭]、 [碎踝]、 [追影步]、 [挑空]、 [穿心]、 [刃舞]、 [潜影刺击]、 [影斩·乱舞]\n
    可以强制中断特定技能的后僵直并发射锁链的技能 :\n
    [绝境飞刃] (最后二击)、 [摧心] (要害袭击动作)、 [瞬袭] (转刀动作)、 [影缚追魂锁] (背后暗影爆炸动作)。\n
    射出匕首命中敌人时， 增加[幽冥链狱 : 瞬逝]的持续时间。
    """
    name = "幽冥链狱 : 瞬逝"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "28b583c75a49103a1d8aabf799c000a4"
    hasVP = False
    hasUP = False

    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 射出匕首的冷却时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 锁链匕首射出攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 拉拽攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 向前冲刺攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 向后冲刺攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 最后一击的撞击攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 最后一击的终结攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 对无法抓取的敌人施放的最后一击攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 聚集敌人的多段攻击攻击力 : {value9}% x {value10}
    data9 = get_data(f'{prefix}/{uuid}', 9)
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 聚集敌人的最后一击攻击力 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 把敌人束缚在地面的冷却时间 : {value12}秒
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 把敌人束缚在地面的持续时间 : {value13}秒
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # 射出匕首命中敌人后技能持续时间增加值 : {value14}秒
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # 射出匕首命中敌人后技能持续时间最大增加值 : {value15}秒
    data15 = get_data(f'{prefix}/{uuid}', 15)

    mode = ['终结抓取', '终结非抓','锁链聚集', '锁链拉拽']  # noqa: E501

    def setMode(self, mode):
        if mode == "终结抓取":
            self.hit2 = 1
            self.hit6 = 4
            self.hit7 = 1
        elif mode == "终结非抓":
            self.hit2 = 1
            self.hit8 = 1
        elif mode == "锁链聚集":
            self.hit2 = 1
            self.hit9 = 6
            self.hit11 = 1
        elif mode == "锁链拉拽":
            self.hit2 = 1
            self.hit3 = 1

    def getSkillCD(self, mode=None):
        if mode == "锁链聚集":
            return 10.0
        elif mode == "锁链拉拽":
            return 1.0
        return super().getSkillCD(mode)

# 暗影禁忌
# thief/shadow_dancer/33ad4930f4724a7d025c3046c6f6074b
# ddc49e9ad1ff72a00b53c6cff5b1e920/33ad4930f4724a7d025c3046c6f6074b
class Skill43(PassiveSkill):
    """
    隐夜·影舞者利用他人影子施展禁忌潜行术， 在任何人都无法察觉的情况下， 除掉敌人。\n
    学习后， 增加基本攻击力和转职技能攻击力， 部分技能附加特殊效果。\n
    [潜行领域] : 增加暗影领域范围。 背击成功时若存在多个敌人， 则增加每次召唤的暗袭分身的数量。\n
    [穿心] : 影舞者的所有转职技能的终结动作时可以预输入该技能键。 预输入后发动技能的状态下， 技能完全结束或施放[追影步]时， 出现在该技能命中的敌人中最强的敌人背后， 穿刺敌人的心脏。 此效果发动的[穿心]必定为背击。
    """
    name = "暗影禁忌"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "33ad4930f4724a7d025c3046c6f6074b"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [潜行领域]暗影领域范围增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [潜行领域]暗袭分身召唤数增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    associate = [{"data":data0}]

# 影缚追魂锁
# thief/shadow_dancer/9ceb0c55f40f1fc0fe0fcc65c8fee3a0
# ddc49e9ad1ff72a00b53c6cff5b1e920/9ceb0c55f40f1fc0fe0fcc65c8fee3a0
class Skill44(ActiveSkill):
    """
    投掷暗影锁链， 抽取敌人的影子， 对其进行追魂攻击。\n
    暗影锁链命中敌人背后时， 抽取影子后快速移动， 切割影子并使其爆炸。 影子爆炸瞬间， 所有伤害都会瞬间转移到敌人本体， 造成致命伤害。\n
    背后攻击时， 若敌人的影子贴近隐夜·影舞者， 则后空翻拉开距离后再开始攻击。 
    """
    name = "影缚追魂锁"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [800, 6000]
    uuid = "9ceb0c55f40f1fc0fe0fcc65c8fee3a0"
    hasVP = False
    hasUP = False

    # 正面抽取影子攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 背后切割影子攻击力 : {value1}% x {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 4
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 背后影子爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1

# 无间影狱·噬灭
# thief/shadow_dancer/aa6dd52e1c925d87cdc0ca340056c543
# ddc49e9ad1ff72a00b53c6cff5b1e920/aa6dd52e1c925d87cdc0ca340056c543
class Skill45(ActiveSkill):
    """
    隐夜·影舞者觉醒自身暗影领域， 融入蔓延到周围的暗影地带， 隐藏身影。 用锁链环绕周围一带后， 用暗影匕首斩击敌人。 最后， 挥动暗影匕首施展3次致命攻击， 最后投掷匕首。\n
    暗影地带内的敌人都是隐夜·影舞者的攻击对象， 所有攻击均适用背后攻击。\n
    施放技能时， 无法使用[影遁]， 无法强制中断并施放影舞者转职技能。\n
    [三次觉醒技能]\n
    选择[影斩·乱舞]使用三次觉醒技能时， 与[影斩·乱舞]共享冷却时间。 \n
    选择[幽冥链狱 : 瞬逝]使用三次觉醒技能时， 可以使用三次觉醒技能代替[幽冥链狱 : 瞬逝]的终结攻击。 三次觉醒技能在冷却中、 [幽冥链狱 : 瞬逝]终结攻击已发动或[幽冥链狱 : 瞬逝]未激活的状态下， 无法使用三次觉醒技能。
    """
    name = "无间影狱·噬灭"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "aa6dd52e1c925d87cdc0ca340056c543"
    hasVP = False
    hasUP = False

    # 锁链多段攻击力 : {value0}% x {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 斩断锁链攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 暗影匕首斩击攻击力 : {value3}% x 3
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 3
    # 暗影匕首投掷攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'shadow_dancer'
        self.nameCN = '隐夜·影舞者'
        self.role = 'thief'
        self.角色 = '暗夜使者'
        self.职业 = '影舞者'
        self.jobId = 'ddc49e9ad1ff72a00b53c6cff5b1e920'
        self.jobGrowId = '4a1459a4fa3c7f59b6da2e43382ed0b9'

        self.武器选项 = ['匕首', '双剑', '手杖'] # TODO
        self.输出类型选项 = ["物理百分比"] # TODO
        self.输出类型 = '物理百分比' # TODO
        self.防具精通属性 = ['力量'] # TODO
        self.防具类型 = '皮甲'
        self.buff = 2.113

        super().__init__(equVersion, __name__)
