#3909d0b188e9c95311399f776e331da5
from core.basic.skill import PassiveBufferSkill,ActiveBufferSkill,ActiveSkill,PassiveSkill, get_data
from core.basic.character import Character
prefix = "mage_female/enchantress/cn/skillDetail"


# 魔法护盾
# mage_female/enchantress/dcd536f1674630f01fc9667bb202b851
# 3909d0b188e9c95311399f776e331da5/dcd536f1674630f01fc9667bb202b851
class Skill10(ActiveSkill):
    """
        施放魔法护盾， 增加自身物理/魔法防御力。\n
        魔法护盾激活时按技能键可解除魔法护盾。\n
        转职为战斗法师后， 可学习[魔法护盾强化]， 加强能力。
    """
    name = "魔法护盾"
    learnLv = 5
    masterLv = 10
    maxLv = 20
    position = 3 #TODO
    rangeLv = 3
    cd = 5
    mp = [10, 14]
    uuid = "dcd536f1674630f01fc9667bb202b851"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 物理防御力增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法防御力增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 别过来！
# mage_female/enchantress/c9603b05632f362bb23cae18374e37cf
# 3909d0b188e9c95311399f776e331da5/c9603b05632f362bb23cae18374e37cf
class Skill11(ActiveSkill):
    """
        将箴言人偶附着在敌人身上， 使敌人无法移动， 然后引爆箴言人偶。\n
        施放技能后施放者进入无敌状态， 直到箴言人偶爆炸。\n
        对无法抓取的敌人不适用控制效果， 箴言人偶不附着在敌人身上， 直接爆炸； 即使附着成功也不会进入无敌状态。
    """
    name = "别过来！"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 8 #TODO
    rangeLv = 2
    cd = 6
    mp = [10, 120]
    uuid = "c9603b05632f362bb23cae18374e37cf"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 箴言人偶爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

# 替身草人
# mage_female/enchantress/0969cd4054d93da07708108c0cc1c4b5
# 3909d0b188e9c95311399f776e331da5/0969cd4054d93da07708108c0cc1c4b5
class Skill12(ActiveSkill):
    """
        在受到敌人攻击或倒地时可以瞬移避开敌人的追击。\n
        瞬移时， 可以按方向键移动到相应方向； 若不按方向键， 则默认向后瞬移。\n
        瞬移后有0.5秒无敌时间， 但自身会出现一定时间的僵直。\n
        角色可以靠近原地留下的稻草人吃掉， 吃掉后增加移动速度、 攻击速度。\n
        在自身被抓取、 冰冻、 眩晕、 石化、 睡眠和束缚状态下， 无法使用此技能。\n
        转职为战斗法师后， 可以学习[替身草人]， 改变启动方式。\n
        在普通决斗场根据转职而产生不同的冷却时间。
    """
    name = "替身草人"
    learnLv = 10
    masterLv = 10
    maxLv = 20
    position = 3 #TODO
    rangeLv = 3
    cd = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
    mp = [20, 70]
    uuid = "0969cd4054d93da07708108c0cc1c4b5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 瞬移后僵直时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 角色增益效果持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 增加角色移动速度 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 增加角色攻击速度 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 召唤兽增益效果持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 增加召唤兽移动速度 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 增加召唤兽攻击速度 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 增加召唤兽力量 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 增加召唤兽智力 : {value8}
    data8 = get_data(f'{prefix}/{uuid}', 8)

# 玫瑰藤蔓
# mage_female/enchantress/f3d425f6b8186f9b170fd1aab778fa0d
# 3909d0b188e9c95311399f776e331da5/f3d425f6b8186f9b170fd1aab778fa0d
class Skill18(ActiveSkill):
    """
        往地面注入黑魔法， 生成玫瑰藤蔓向前方延伸。
    """
    name = "玫瑰藤蔓"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 9 #TODO
    rangeLv = 2
    cd = 5
    mp = [30, 252]
    uuid = "f3d425f6b8186f9b170fd1aab778fa0d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 藤蔓多段攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 出血攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 出血持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 攻击大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 驱散魔法
# mage_female/enchantress/9bff7f2559e003766fee2853dca00631
# 3909d0b188e9c95311399f776e331da5/9bff7f2559e003766fee2853dca00631
class Skill20(ActiveSkill):
    """
        驱散范围内敌人的增益效果， 减少敌人的施放速度， 并使其进入减速状态。\n
        驱散敌人的增益效果时， 提升自身的力量和智力， 每驱散1个， 可以额外提升。
    """
    name = "驱散魔法"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 2 #TODO
    rangeLv = 3
    cd = [20, 19.5, 19.1, 18.6, 18.1, 17.6, 17.2, 16.7, 16.2, 15.7, 15.3, 14.8, 14.3, 13.8, 13.4, 12.9, 12.4, 11.9, 11.5, 11]
    mp = [30, 126]
    uuid = "9bff7f2559e003766fee2853dca00631"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 减益效果数量上限 : {value0}个
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 增加力量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 增加智力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 增加力量、 智力的持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 减速几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 敌人攻击速度减少率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 敌人移动速度减少 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 敌人施放速度减少 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 减少敌人攻击速度、 移动速度、 施放速度的持续时间 : {value8}秒
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [范围信息]
    # 减益效果范围 : {value9}px
    data9 = get_data(f'{prefix}/{uuid}', 9)


# 细心缝补
# mage_female/enchantress/e7e39aa9fcf182c8db543235c8af7dac
# 3909d0b188e9c95311399f776e331da5/e7e39aa9fcf182c8db543235c8af7dac
class Skill22(ActiveBufferSkill):
    """
        小魔女细心缝补坏坏兔身上的破洞。 同时恢复一定范围内所有队友的生命值， 消除异常状态。\n
        额外增加[小魔女的偏爱]对象的恢复量。\n
        [细心缝补]施放过程中， 小魔女所受伤害减少10%， 按跳跃键可以立即结束技能。
    """
    name = "细心缝补"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 3
    cd = 15
    mp = [15, 154]
    uuid = "e7e39aa9fcf182c8db543235c8af7dac"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 初次缝补时生命值恢复 : <pnumber>
    # 每追加缝补1次的生命值恢复 : <pnumber>
    # 追加缝补次数上限 : 3次
    # 异常状态消除数量上限 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 施放期间所受伤害减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 效果生效范围 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 黑魔法扫把
# mage_female/enchantress/14c573777542b4ee3cdca35501b06c97
# 3909d0b188e9c95311399f776e331da5/14c573777542b4ee3cdca35501b06c97
class Skill23(PassiveSkill):
    """
        学习后， 精通黑魔法， 可以装备扫把， 且装备扫把时增加施放速度和命中率。 \n
        [给我最好的。 太重？ 没关系！ 疯疯熊会替我拿着。]
    """
    name = "黑魔法扫把"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 7 #TODO
    rangeLv = 3
    uuid = "14c573777542b4ee3cdca35501b06c97"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 装备扫把时施放速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 装备扫把时命中率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 人偶操纵者
# mage_female/enchantress/8d8981a94b8bdd4e3ffad5bc05042080
# 3909d0b188e9c95311399f776e331da5/8d8981a94b8bdd4e3ffad5bc05042080
class Skill24(PassiveBufferSkill):
    """
        学习后， 将拥有人偶术士的资质， 可以使用人偶技能。 同时， 小魔女对诅咒免疫， 攻击属性变为暗属性。\n
        小魔女的智力随技能等级增加而增加。\n
    注意 : 下列因素增加的智力值不会提升效果。\n
        装备的条件性触发效果、 光环属性、 消耗品、 角色的主动技能。\n
        [来， 跟我可爱的孩子们打个招呼吧！ 这是‘坏坏兔’和‘疯疯熊’。]
    """
    name = "人偶操纵者"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 3
    uuid = "8d8981a94b8bdd4e3ffad5bc05042080"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 智力增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)

    INT = data0
    associate = [{"data":INT,"type":"$+INT","ratio":1}]

# 疯狂乱抓
# mage_female/enchantress/6bbf76bcd2ed3ca25f21b760db4342ad
# 3909d0b188e9c95311399f776e331da5/6bbf76bcd2ed3ca25f21b760db4342ad
class Skill25(ActiveSkill):
    """
        疯疯熊挥舞前掌， 用锋利的指甲攻击前方的敌人两次。\n
        不论小魔女处于什么状态， 都可以施放该技能。
    """
    name = "疯狂乱抓"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 3
    mp = [27, 294]
    uuid = "6bbf76bcd2ed3ca25f21b760db4342ad"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 第1击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 第2击攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 攻击大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)


# 小魔女的偏爱
# mage_female/enchantress/04c7b4361ca81f041e868169ff044252
# 3909d0b188e9c95311399f776e331da5/04c7b4361ca81f041e868169ff044252
class Skill27(ActiveBufferSkill):
    """
        小魔女抱着坏坏兔表达喜爱， 温馨的气息扩散到周围， 增加全体队员的生命值最大值、 魔法值最大值、 物理防御力、 魔法防御力、 体力和精神。\n
        而且， 小魔女可以选择一名偏爱的队友， 赋予其更高的属性加成， 并提升该队友获得的其他增益技能的效果。若偏爱的对象为疯疯熊， 则增加除觉醒技能之外的疯疯熊系列技能的攻击力。\n
        另外， 偏爱的对象将无视[禁术吟咏]和[林中小屋]减少生命值的效果。使用[永恒的占据]复活偏爱的对象时， 偏爱的对象可获得拥有额外生命值的保护罩。\n
        [小魔女的偏爱]效果不与光明骑士 (男/女)的[天籁之音]、 [守护徽章]、[守护祝福]、 缪斯的[主角登场]、 协战师的[装甲强化]效果叠加。\n
        - [偏爱对象的增益效果增幅] -\n
        禁术吟咏 : 增益效果 +15%\n
        火热的爱意 : 增益效果 +20%\n
        细心缝补 : 生命值恢复量 +20%\n
        爱之急救 : 生命值恢复量 +20%
    """
    name = "小魔女的偏爱"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 6 #TODO
    rangeLv = 3
    cd = 10
    mp = [35, 392]
    buffer = True
    buffType = "buffSub"
    uuid = "04c7b4361ca81f041e868169ff044252"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 队友生命值最大值增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 队友魔法值最大值增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 队友物理防御力增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 队友魔法防御力增加 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 队友体力增加 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 队友精神增加 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 疯疯熊系列技能攻击力增加率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # - [偏爱对象的效果增加率] -
    # [禁术吟咏]效果增加率 : 15%
    # [火热的爱意]效果增加率 : 20%
    # [细心缝补]生命值恢复量增加率 : 20%
    # [爱之急救]生命值恢复量增加率 : 20%

    def skillInfo(self):
        prep = self.char.BuffSkill.skillInfo()
        if self.lv > 0:
            ratio = 20 / 100
        else:
            ratio = 0
        return prep[0] * ratio, [prep[1][0]*ratio,prep[1][1],prep[1][2]*ratio], [prep[2][0]*ratio,prep[2][1],prep[2][2]*ratio],0,self.getSkillCD()

# 邪恶的好奇心
# mage_female/enchantress/653b35b5b59d29daffca47df43b2b0e3
# 3909d0b188e9c95311399f776e331da5/653b35b5b59d29daffca47df43b2b0e3
class Skill28(PassiveSkill):
    """
        增加小魔女的技能攻击力和魔法暴击率。\n
        [小魔女的好奇心对某些人来说是个悲剧。 当然她自己并不在意这个事实……]
    """
    name = "邪恶的好奇心"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 7 #TODO
    rangeLv = 3
    uuid = "653b35b5b59d29daffca47df43b2b0e3"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 疯熊火箭拳
# mage_female/enchantress/4b22172f4e00d9735ff44d333a86653d
# 3909d0b188e9c95311399f776e331da5/4b22172f4e00d9735ff44d333a86653d
class Skill29(ActiveSkill):
    """
        疯疯熊发射用傀儡线连接的拳套。 拳套命中敌人时， 会产生冲击波。\n
        不论小魔女处于什么状态， 都可以施放该技能。
    """
    name = "疯熊火箭拳"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 6
    mp = [32, 343]
    uuid = "4b22172f4e00d9735ff44d333a86653d"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 拳套冲击波攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [范围信息]
    # 拳套冲击波大小比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 人偶篮子
# mage_female/enchantress/67e7dd8996b5735e788c9420730c077d
# 3909d0b188e9c95311399f776e331da5/67e7dd8996b5735e788c9420730c077d
class Skill30(PassiveSkill):
    """
        可以学习并使用箴言人偶系列技能。 可以通过[蔷薇藤鞭]、 [苦痛庭院]、 [挚爱囚笼]补充箴言人偶数量。\n
        每消耗1个箴言人偶， [禁术吟咏]和[小魔女的偏爱]增益效果持续时间增加10秒。\n
    - [箴言人偶系列技能] -\n
        [火热的爱意]、 [疯狂召唤]、 [林中小屋]、 [人偶戏法]、 [永恒的占据]\n
        箴言人偶系列技能的“适用于敌人的效果”可以在[人偶篮子]技能中通过On/Off开启或关闭。
    """
    name = "人偶篮子"
    learnLv = 25
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 3
    uuid = "67e7dd8996b5735e788c9420730c077d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 进入地下城时箴言人偶数量 : {value0}个
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 箴言人偶可累积数量上限 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 火热的爱意
# mage_female/enchantress/e862146efac2fce3de3a12f038f4116b
# 3909d0b188e9c95311399f776e331da5/e862146efac2fce3de3a12f038f4116b
class Skill31(ActiveSkill):
    """
        在箴言人偶脚下点燃火焰。 该诅咒对范围内的队友和敌人分别发挥不同效果。\n
    [适用于队友的效果]\n
    箴言人偶身上的火焰转移到队友脚下， 队友受到惊吓， 增加攻击速度、 移动速度和施放速度。 如果该队友不努力跑动而是站立不动维持一定时间， 则会受到脚下火焰伤害。\n
        偏爱的对象会受到更强的诅咒， 效果增加， 且受到小魔女的爱意保护， 不会受到火焰伤害。\n
        技能叠加使用时， 增益效果持续时间在原有时间上累加。\n
    [适用于敌人的效果]\n
    箴言人偶身上火焰的热气传到敌人身上， 使敌人受到伤害。\n
        在决斗场中， 火焰无法转移到一定高度以上或无敌状态的敌人身上。
    """
    name = "火热的爱意"
    learnLv = 25
    masterLv = 40
    maxLv = 50
    position = 1 #TODO
    rangeLv = 3
    mp = [32, 343]
    uuid = "e862146efac2fce3de3a12f038f4116b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 箴言人偶消耗 : 1个
    # 效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 移动速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 施放速度增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 火焰热气攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 火焰热气多段攻击次数 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 效果生效范围 : {value6}px
    data6 = get_data(f'{prefix}/{uuid}', 6)

# 蔷薇藤鞭
# mage_female/enchantress/5f11bba71728448bb64de0dba2b252cf
# 3909d0b188e9c95311399f776e331da5/5f11bba71728448bb64de0dba2b252cf
class Skill32(ActiveSkill):
    """
        召唤魔力凝聚而成的荆棘藤攻击敌人， 然后把敌人拉到身前。\n
        荆棘藤击中敌人时， 可以吸收敌人的魔力收获箴言人偶。\n
        不论击中多少敌人， 都只能收获1个箴言人偶。
    """
    name = "蔷薇藤鞭"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 8 #TODO
    rangeLv = 3
    cd = 10
    mp = [32, 343]
    uuid = "5f11bba71728448bb64de0dba2b252cf"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 箴言人偶收获数量 : 1个
    # 鞭打攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 拉回攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 攻击大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 疯熊守护
# mage_female/enchantress/854997c3bdfc3a2b498b4c4001f69e06
# 3909d0b188e9c95311399f776e331da5/854997c3bdfc3a2b498b4c4001f69e06
class Skill33(ActiveSkill):
    """
        疯熊对距小魔女最近的敌人发动捶击， 守护小魔女。\n
        只要施放范围内存在敌人， 不论小魔女处于什么状态， 都可以施放该技能。
    """
    name = "疯熊守护"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 10
    mp = [91, 763]
    uuid = "854997c3bdfc3a2b498b4c4001f69e06"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 捶击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [范围信息]
    # 可施放距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 禁术吟咏
# mage_female/enchantress/61c8cb33dd20b4ff335e8deed70d3d9c
# 3909d0b188e9c95311399f776e331da5/61c8cb33dd20b4ff335e8deed70d3d9c
class Skill34(ActiveBufferSkill):
    """
        以坏坏兔为媒介， 向周围散播厄运的气息。 对范围内的队友施加禁术吟咏， 以队友的生命力为担保， 使其获取强大的力量。\n
        禁术吟咏可以提升队友的物攻、 魔攻、 独立攻击力、 力量、 智力和命中率， 并对偏爱的对象赋予更强的力量。 同时， 增加自身的基本攻击力、 技能攻击力和命中率。\n
        达到20级以上后， 不再增加自身基本攻击力和技能攻击力， 且物理/魔法/独立攻击力、 力量、 智力增加效果不适用于自身。\n
        施放者的智力越高， 物攻、 魔攻、 独立攻击力、 力量、 智力提升量越高。\n
        小魔女的[禁术吟咏]效果不与光明骑士 (男/女) 的[勇气祝福]、 [荣誉祝福]、 缪斯的[可爱节拍]、 协战师的[军械强化]的技能效果叠加。\n
        从厄运剩余20秒开始， 开始出现厄运的副作用。\n
        - [厄运副作用] -\n
        强行激发力量的厄运气息会蚕食厄运对象的生命力， 每5秒减少厄运对象5%的生命值。\n
        厄运结束或者再次施放技能更新持续时间时， 副作用会解除。 小魔女自身和偏爱的对象不受副作用影响。
    """
    name = "禁术吟咏"
    learnLv = 30
    masterLv = 30
    maxLv = 40
    position = 6 #TODO
    rangeLv = 3
    cd = 10
    buffer = True
    buffType = "buff"
    uuid = "61c8cb33dd20b4ff335e8deed70d3d9c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # - [适用于小魔女的效果] -
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 命中率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # - [适用于队友的效果] -
    # 物理攻击力增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 魔法攻击力增加 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 独立攻击力增加 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 力量增加 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 智力增加 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 命中率增加 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [范围信息]
    # 增益效果范围 : {value9}px
    data9 = get_data(f'{prefix}/{uuid}', 9)

    ATK = data3
    STRINT = data6

# 御敌之刺
# mage_female/enchantress/dce00e1ce90e34ef5c36ea869ad171bd
# 3909d0b188e9c95311399f776e331da5/dce00e1ce90e34ef5c36ea869ad171bd
class Skill35(ActiveSkill):
    """
        从地面召唤多棵荆棘， 刺穿范围内的敌人， 将其聚集到前方。 荆棘每次攻击都会将命中的敌人移动到小魔女前方， 并使刺伤的敌人进入出血状态。 
    """
    name = "御敌之刺"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 9 #TODO
    rangeLv = 2
    cd = 10
    mp = [69, 724]
    uuid = "dce00e1ce90e34ef5c36ea869ad171bd"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 尖刺攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 尖刺多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 出血攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 出血持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 疯疯熊坠击
# mage_female/enchantress/38c485cc41f46a7959ae4336325aa45c
# 3909d0b188e9c95311399f776e331da5/38c485cc41f46a7959ae4336325aa45c
class Skill36(ActiveSkill):
    """
        疯疯熊将全身的弹力发挥到极致， 跳到高空中后下坠， 落地时造成强力冲击波， 将敌人吸附到落地处。 冲击波可以使命中的敌人受到伤害并浮空。\n
        施放时按向前方向键， 可以让疯疯熊落到更远的位置。 不论疯疯熊当前位置在哪里， 都可以立即施放该技能。\n
        不论小魔女处于什么状态， 都可以施放该技能。\n
    决斗场中无法吸附敌人。
    """
    name = "疯疯熊坠击"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cube = 1
    cd = 12
    mp = [130, 1092]
    uuid = "38c485cc41f46a7959ae4336325aa45c"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 落地冲击波攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [范围信息]
    # 攻击大小比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [疯疯熊坠击]\n
        技能施放速度 +30%\n
        攻击范围 +50%\n
        聚集敌人范围 +50%\n
        [爱之急救]\n
        对范围内所有队友缠上绷带， 小魔女的技能结束之前， 即使队友离开魔法阵范围也会维持恢复效果\n
        恢复魔法阵大小 +20%
        """
        ...

    def vp_2(self):
        """
        [疯疯熊坠击]\n
        小魔女可以附着在跳跃的疯疯熊身上， 进入无敌状态\n
        能直接指定落地位置\n
        [开幕！ 人偶剧场]和[终幕！ 人偶剧场]过程中也同样进入无敌状态\n
        可以强制中断施放过程中的疯疯熊系列技能； 在[开幕！ 人偶剧场]和[终幕！ 人偶剧场]过程中施放时， 可以强制中断所有正在施放的技能\n
        [爱之急救]\n
        对范围内所有队友缠上绷带， 小魔女的技能结束之前， 即使队友离开魔法阵范围也会维持恢复效果\n
        恢复魔法阵大小 +20%
        """
        ...

# 疯狂召唤
# mage_female/enchantress/7a3fc9d473e8ffe21dd900ddf228a437
# 3909d0b188e9c95311399f776e331da5/7a3fc9d473e8ffe21dd900ddf228a437
class Skill37(ActiveSkill):
    """
        释放箴言人偶， 召唤拥有特殊能力的箴言人偶和跳跳人偶。 该技能对范围内的队友和敌人分别发挥不同效果。\n
    - [适用于队友的效果] -\n
    生成特殊箴言人偶附着在队友身上， 增强[禁术吟咏]的效果。 特殊箴言人偶生成数量与施放时范围内存在的队友数量相同。\n
        技能叠加使用时， 增益效果持续时间在原有时间上累加。\n
    - [适用于敌人的效果] -\n
    生成跳跳人偶跳到敌人身上后爆炸。 跳跳人偶生成数量与施放时范围内存在的敌人数量相同， 但最多不超过5个。\n
        在决斗场中， 无法探索一定高度以上或无敌状态的敌人。
    """
    name = "疯狂召唤"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 1 #TODO
    rangeLv = 3
    cube = 1
    mp = [160, 1344]
    uuid = "7a3fc9d473e8ffe21dd900ddf228a437"
    hasVP = True
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501
    buffer = True
    buffType = "buffSub"

    # 箴言人偶消耗 : 2个
    # [箴言人偶]
    # 箴言人偶附着时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [禁术吟咏]效果增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [跳跳人偶]
    # 爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 生成数量上限 : {value3}个
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 箴言人偶/跳跳人偶探索范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def skillInfo(self):
        prep = self.char.BuffSkill.skillInfo()
        ratio = self.data1[self.lv] / 100
        return prep[0] * ratio, [prep[1][0]*ratio,prep[1][1],prep[1][2]*ratio], [prep[2][0]*ratio,prep[2][1],prep[2][2]*ratio],0,self.getSkillCD()

    def vp_1(self):
        """
        [疯狂召唤]\n
        范围内敌人数量少于跳跳人偶的数量时， 剩余的跳跳人偶会围绕在小魔女周围\n
        敌人进入范围内时， 小魔女周围的跳跳人偶会附着到敌人身上\n
        跳跳人偶围绕在小魔女周围期间， 会获得增加小魔女移动速度的增益效果\n
        跳跳人偶持续时间小魔女移动速度增加率 : 20%\n
        跳跳人偶围绕时间 : 8秒\n
        跳跳人偶适用范围 +10%\n
        跳跳人偶生成数量上限 +3个\n
        跳跳人偶移动速度 +50%\n
        [疯狂召唤]\n
        箴言人偶在地面停留2秒， 若队友在箴言人偶消失前进入到范围内， 则箴言人偶会附在该队友身上\n
        箴言人偶适用范围 +10%
        """
        ...

    def vp_2(self):
        """
        [疯狂召唤]\n
        从地面涌出大量的跳跳人偶， 成群结队地奔跑； 奔跑的跳跳人偶分别附着在附近的敌人身上并爆炸\n
        存在被跳跳人偶击败的敌人时， 可以获得箴言人偶\n
        - 可寻敌数量 : 10\n
        - 存在被击败的敌人时， 箴言人偶获得量 : 1个\n
        [疯狂召唤]\n
        箴言人偶在地面停留2秒， 若队友在箴言人偶消失前进入到范围内， 则箴言人偶会附在该队友身上\n
        箴言人偶适用范围 +10%
        """
        ...

# 蔷薇囚狱
# mage_female/enchantress/94c450d6214cafdc673f763badceeaf1
# 3909d0b188e9c95311399f776e331da5/94c450d6214cafdc673f763badceeaf1
class Skill38(ActiveSkill):
    """
        用魔力浸染前方地带， 生成荆棘禁锢踏入该地带的敌人， 并使敌人受到伤害。\n
        进入荆棘地带的敌人会被强制控制， 在此期间蔷薇在敌人身上绽放后爆炸。\n
        技能持续期间再次按技能键， 可以立即发动爆炸。
    """
    name = "蔷薇囚狱"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 8 #TODO
    rangeLv = 2
    cube = 1
    cd = 18
    mp = [160, 1344]
    uuid = "94c450d6214cafdc673f763badceeaf1"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 荆棘攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 荆棘多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 出血攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 出血持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 攻击大小比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [蔷薇囚狱]\n
        攻击范围逐渐向中心缩小， 可以聚集范围内的敌人\n
        攻击范围 +30%\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 9秒\n
        - 单次攻击力 -50%\n
        [蔷薇藤鞭]\n
        小魔女在施放其他技能过程中施放时， 由疯疯熊代替施放[蔷薇藤鞭]
        """
        ...

    def vp_2(self):
        """
        [蔷薇囚狱]\n
        技能攻击范围以小魔女为中心生成\n
        - 攻击范围 +50%\n
        可以与[苦痛庭院]、 [挚爱囚笼]同时施放； 同时施放时， 后施放的技能的施放动作会被省略\n
        [蔷薇藤鞭]\n
        小魔女在施放其他技能过程中施放时， 由疯疯熊代替施放[蔷薇藤鞭]
        """
        ...

# 爱之急救
# mage_female/enchantress/a99040fc36c75e998aa3ed012b7759c5
# 3909d0b188e9c95311399f776e331da5/a99040fc36c75e998aa3ed012b7759c5
class Skill39(ActiveBufferSkill):
    """
        给坏坏兔缠上充满爱和魔力的绷带。\n
        使范围内的队友持续恢复生命值， 且施放时立即解除所有异常状态。 偏爱的对象可恢复更多生命值。\n
        施放过程中， 小魔女对异常状态免疫， 且所受伤害减少10%。\n
        施放过程中， 按跳跃键可以结束技能。
    """
    name = "爱之急救"
    learnLv = 40
    masterLv = 1
    maxLv = 11
    position = 6 #TODO
    rangeLv = 2
    cube = 1
    cd = 40
    mp = [350, 2940]
    uuid = "a99040fc36c75e998aa3ed012b7759c5"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 魔法阵持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 小魔女所受伤害减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 生命值恢复量 : 每秒 <pnumber>%
    # 可同时解除的异常状态数量 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 魔法阵范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 变大吧！ 疯疯熊
# mage_female/enchantress/b39ccc3dadab9d94569430e39cdf7d60
# 3909d0b188e9c95311399f776e331da5/b39ccc3dadab9d94569430e39cdf7d60
class Skill40(ActiveSkill):
    """
        对疯疯熊注入魔力， 使其瞬间变大。 变大后的疯疯熊对前方发动狂抓和捶击攻击。\n
        施放该技能时进入无敌状态， 并且可以无施放动作立即使用[细心缝补]和[爱之急救]。\n
        狂抓攻击过程中， 可以以缓慢速度移动， 连续按技能键或<X>键可以加快攻击速度。\n
        施放过程中按跳跃键可以结束技能， 同时使用的其他技能也会立即结束。
    """
    name = "变大吧！ 疯疯熊"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [338, 2839]
    uuid = "b39ccc3dadab9d94569430e39cdf7d60"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 狂抓攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 狂抓多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 双臂捶击攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 双臂捶击攻击大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [变大吧！ 疯疯熊]\n
        可以强制控制命中的敌人\n
        [变大吧！ 疯疯熊]搭乘状态下施放[细心缝补]、 [爱之急救]时， [变大吧！ 疯疯熊]技能结束后[细心缝补]、 [爱之急救]的恢复效果依然保留\n
        技能攻击范围 +10%\n
        施放中移动速度 +50%\n
        [小魔女的偏爱]\n
        非偏爱对象的队友不再因[火热的爱意]、 [禁术吟咏]、 [林中小屋]的影响而减少生命值\n
        非偏爱对象的队员所受伤害减少率额外 +5%
        """
        ...

    def vp_2(self):
        """
        [变大吧！ 疯疯熊]\n
        小魔女不再骑乘疯疯熊， 疯疯熊自行攻击\n
        疯疯熊攻击速度 +30%\n
        [小魔女的偏爱]\n
        非偏爱对象的队友不再因[火热的爱意]、 [禁术吟咏]、 [林中小屋]的影响而减少生命值\n
        非偏爱对象的队员所受伤害减少率额外 +5%
        """
        ...

# 林中小屋
# mage_female/enchantress/696721534394b40e78ac96e880f19e5a
# 3909d0b188e9c95311399f776e331da5/696721534394b40e78ac96e880f19e5a
class Skill41(ActiveSkill):
    """
        将注入魔力的箴言人偶献祭， 召唤任何人都无法入侵的荆棘屋。 该诅咒对范围内的队友和敌人分别发挥不同效果。\n
    - [适用于队友的效果] -\n
    进入荆棘屋后不受外部伤害， 但荆棘屋晃动时会受到生命值最大值5%的伤害。 在荆棘屋入口处跳跃即可进入荆棘屋， 再次按跳跃键可以跳出荆棘屋。 偏爱的对象不会减少生命值。\n
    - [适用于敌人的效果] -\n
    敌人靠近荆棘屋时会被小屋外的尖刺刺伤， 并被击退。
    """
    name = "林中小屋"
    learnLv = 45
    masterLv = 1
    maxLv = 11
    position = 1 #TODO
    rangeLv = 2
    cube = 2
    mp = [1645, 1645]
    uuid = "696721534394b40e78ac96e880f19e5a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 箴言人偶消耗 : 1个
    # [林中小屋]持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 荆棘多段攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 荆棘多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 队友生命值减少量 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # [林中小屋]大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 少女的爱
# mage_female/enchantress/0dbdeaf846356f8b9380f8fbb8e97377
# 3909d0b188e9c95311399f776e331da5/0dbdeaf846356f8b9380f8fbb8e97377
class Skill42(PassiveBufferSkill):
    """
        增加包括小魔女在内的所有队友的攻击速度、 移动速度、 力量、 智力、 体力和精神， 并增加自身基本攻击力及技能攻击力。\n
        [她的微笑后面藏着什么小把戏呢？]
    """
    name = "少女的爱"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 3
    uuid = "0dbdeaf846356f8b9380f8fbb8e97377"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 移动速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 力量、 智力增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 体力、 精神增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 基本攻击和技能攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    INT = data2
    STRINT = data2

    associate = [{"data":INT,"type":"$+INT","ratio":1}]

# 开幕！ 人偶剧场
# mage_female/enchantress/56fca6cff74d828e92301a40cd2148b9
# 3909d0b188e9c95311399f776e331da5/56fca6cff74d828e92301a40cd2148b9
class Skill43(ActiveBufferSkill):
    """
        小魔女将画面内的所有敌人和队友变为主人公出演人偶剧。\n
        人偶剧持续期间， 暗黑少女操纵疯疯熊行动， 疯疯熊进行其他动作时， 如果施放尖刺系列技能， 跟随小魔女动作的人偶会替代施放技能。\n
        人偶剧持续期间， 提升队友的力量、 智力、 攻击速度和移动速度， 并减少10%的所受伤害、 免疫控制型异常状态。\n
        操纵疯疯熊的状态下， 可以使用小魔女系列技能、 主动增益技能和[替身草人]。 疯疯熊死亡时可以消耗1个箴言人偶立即复活， 仅首次可以获得箴言人偶层数。 同时， 可以放置使用[细心缝补]和[爱之急救]技能。\n
        技能持续时间结束或再次按技能键时， 人偶剧立即结束， 此时变大的疯疯熊的挥爪划破帷幕， 对画面内的所有敌人造成伤害。\n
        力量、 智力提升效果对自身无效。\n
        增益效果不与光明骑士 (男/女) 的[圣光天启]、 [天启之光]、 缪斯的[梦想的舞台]、 协战师的[强袭策略 : 区域肃清]效果叠加。
    """
    name = "开幕！ 人偶剧场"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 5
    cd = 170
    mp = [1200, 10080]
    buffType = 'awake'
    uuid = "56fca6cff74d828e92301a40cd2148b9"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 效果范围 : - px
    # [开幕！ 人偶剧场]持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 力量增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 智力增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 攻击速度增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 移动速度增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 最后挥爪攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)

    STRINT = data1

# 人偶戏法
# mage_female/enchantress/6166762c62f234c5f50c2d2ebc5e48d0
# 3909d0b188e9c95311399f776e331da5/6166762c62f234c5f50c2d2ebc5e48d0
class Skill44(ActiveSkill):
    """
        施放时， 在前方生成箴言人偶， 同时将附近的敌人变成人偶。 小魔女将钉子钉入箴言人偶的身体中， 变成人偶的敌人体内也会被钉入钉子。 钉钉子期间敌人进入强制控制状态。\n
        连续按<X>键可以加快钉钉子的速度。
    """
    name = "人偶戏法"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 1 #TODO
    rangeLv = 2
    cube = 2
    mp = [400, 1000]
    uuid = "6166762c62f234c5f50c2d2ebc5e48d0"
    hasVP = True
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 箴言人偶消耗 : 1个
    # 钉钉子攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 钉钉子多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后一钉攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # [人偶戏法]效果范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [人偶戏法]\n
        施放时直接发动最后一钉， 然后恢复站立状态\n
        [永恒的占据]\n
        复活对象搜寻范围 +20%\n
        [永恒的占据]复活的队友的生命值/魔法值 +15% (偏爱对象额外 +5%)
        """
        ...

    def vp_2(self):
        """
        [人偶戏法]\n
        不再消耗箴言人偶数量， 变为具有单独攻击力和冷却时间的技能\n
        - 总攻击力 +42.8%\n
        - 技能冷却时间 : 15秒\n
        最后一击命中的敌人， 对其附加减少移动速度/攻击速度的减益效果\n
        - 减益效果持续时间 : 10秒\n
        - 移动速度 -30%\n
        - 攻击速度 -30%\n
        技能效果范围 +30%\n
        [永恒的占据]\n
        复活对象搜寻范围 +20%\n
        [永恒的占据]复活的队友的生命值/魔法值 +15% (偏爱对象额外 +5%)
        """
        ...

# 爱之刺痛
# mage_female/enchantress/452be74df1c43b4d3080e1b09ed32e08
# 3909d0b188e9c95311399f776e331da5/452be74df1c43b4d3080e1b09ed32e08
class Skill45(ActiveSkill):
    """
        小魔女紧紧拥抱坏坏兔， 背后生长饱含爱意的荆棘藤蔓。 然后， 从荆棘藤蔓上生成无数尖刺向地面倾泻而下， 使尖刺命中的敌人进入出血状态。\n
        施放期间， 可以按跳跃键结束技能。 
    """
    name = "爱之刺痛"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 9 #TODO
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [378, 1058]
    uuid = "452be74df1c43b4d3080e1b09ed32e08"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 尖刺攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 尖刺多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 出血攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 出血持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [爱之刺痛]\n
        施放技能时小魔女所受伤害 -90%\n
        基本冷却时间变更为45秒\n
        总攻击力 +50%\n
        攻击范围 +30%\n
        [火热的爱意]\n
        增益效果持续时间 +50%\n
        偏爱对象速度增益效果增幅率 +10%
        """
        ...

    def vp_2(self):
        """
        [爱之刺痛]\n
        施放时， 会在周围最强敌人的前方生长出荆棘藤蔓进行攻击\n
        在荆棘藤蔓生成后， 小魔女可以自由行动\n
        [火热的爱意]\n
        增益效果持续时间 +50%\n
        偏爱对象速度增益效果增幅率 +10%
        """
        ...

# 永恒的占据
# mage_female/enchantress/d59c9840f65381bde8487757f1753c71
# 3909d0b188e9c95311399f776e331da5/d59c9840f65381bde8487757f1753c71
class Skill46(ActiveSkill):
    """
        用傀儡线强制将1名死亡的队友拉起， 使其复活。\n
        与小魔女组队的队友死亡时， 会在一定时间内躺在地上保持死亡状态。\n
        死亡状态下， 该队友的效果不消失。 此时， 若小魔女施放[永恒的占据]， 则该队友会复活， 并恢复一定量的生命值和魔法值， 但不会重置技能冷却时间。\n
        使用[永恒的占据]复活偏爱的对象时， 会生成拥有额外生命值的保护罩。\n
        队友在死亡状态下可以用复活币复活， 但身上的效果会消失。
    """
    name = "永恒的占据"
    learnLv = 70
    masterLv = 1
    maxLv = 11
    position = 1 #TODO
    rangeLv = 2
    cube = 2
    mp = [200, 1680]
    uuid = "d59c9840f65381bde8487757f1753c71"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 箴言人偶消耗 : 1个
    # 队友死亡状态持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 队友复活后生命值、 魔法值恢复率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 偏爱对象的保护罩生命值 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # [永恒的占据]效果范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 哇咔咔！
# mage_female/enchantress/bbc15561bec24f9c1e79e23d715b1dd2
# 3909d0b188e9c95311399f776e331da5/bbc15561bec24f9c1e79e23d715b1dd2
class Skill47(ActiveSkill):
    """
        疯疯熊将附近的敌人吸附到身边， 然后瞬间变大发出蕴含强大魔力的咆哮。
    """
    name = "哇咔咔！"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [860, 1500]
    uuid = "bbc15561bec24f9c1e79e23d715b1dd2"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 咆哮攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 咆哮多段攻击次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 吸附范围 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 攻击大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [哇咔咔！]\n
        施放时按向前方向键， 疯疯熊可以前进并施放技能\n
        - 疯疯熊前进距离 : 200px\n
        施放时小魔女省略施放动作\n
        吸附敌人范围 +10%\n
        [开幕！ 人偶剧场]\n
        满足以下条件时当前冷却时间减少1秒 (最多25秒)\n
        - [冥月绽放] : 属性伤害量增加效果持续5秒时\n
        - 消耗1个箴言人偶数量时\n
        - 使用[细心缝补]、 [爱之急救]对队友施加恢复效果时
        """
        ...

    def vp_2(self):
        """
        [哇咔咔！]\n
        疯疯熊发出向四周扩散的咆哮\n
        - 多段攻击次数 : 5次\n
        - 总攻击力相同\n
        - 删除吸附敌人的功能\n
        [开幕！ 人偶剧场]\n
        满足以下条件时当前冷却时间减少1秒 (最多25秒)\n
        - [冥月绽放] : 属性伤害量增加效果持续5秒时\n
        - 消耗1个箴言人偶数量时\n
        - 使用[细心缝补]、 [爱之急救]对队友施加恢复效果时
        """
        ...

# 冥月绽放
# mage_female/enchantress/de20372767d014d62dc7361ac686834e
# 3909d0b188e9c95311399f776e331da5/de20372767d014d62dc7361ac686834e
class Skill48(PassiveBufferSkill):
    """
        增加自身智力和技能攻击力， 增加进入地下城时的箴言人偶初始数量， 被小魔女击中的敌人适用增加属性伤害的减益效果。\n
        无法与光明骑士(男)的[惩罚之锤]、 光明骑士(女)的[圣光灌注]、缪斯的[多彩感性]、 协战师的[系统 · 战场信息]效果重复适用。\n
        单人挑战时， 对敌人不适用增加属性伤害的减益效果， 而是适用单人挑战专属效果。\n
        [你永远都是属于我的。]
    """
    name = "冥月绽放"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 3
    uuid = "de20372767d014d62dc7361ac686834e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 智力增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 箴言人偶初始数量增加量 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 属性伤害量增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 属性伤害量增加持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 属性伤害量增加重叠次数上限 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [单人挑战专属效果]
    # 独立攻击力增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 技能冷却时间减少率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    INT = data0
    associate = [{"data":INT ,"type":"$+INT","ratio":1}]
    CarryRatio = [0]+ [(1.05 ** 3) * 100 - 100]*maxLv# noqa: E501

# 苦痛庭院
# mage_female/enchantress/3a691a432c58abebc08211df45c4f4bd
# 3909d0b188e9c95311399f776e331da5/3a691a432c58abebc08211df45c4f4bd
class Skill49(ActiveSkill):
    """
        召唤长满魔力荆棘藤的苦痛庭院， 攻击范围内的敌人， 并捆住敌人的脚， 使其进入束缚状态。\n
        荆棘藤击中敌人时， 可以吸收敌人的魔力收获箴言人偶。\n
        不论击中多少敌人， 都只能收获1个箴言人偶。
    """
    name = "苦痛庭院"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 8 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "3a691a432c58abebc08211df45c4f4bd"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 箴言人偶收获数量 : 1个
    # 荆棘攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 荆棘多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 蔷薇花爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 出血攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 出血持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 束缚几率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 束缚持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 攻击大小比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    def vp_1(self):
        """
        [苦痛庭院]\n
        施放时进入无敌状态\n
        技能命中的敌人时， 恢复生命值\n
        - 每命中1名敌人生命值恢复量 : 10%\n
        [细心缝补]\n
        删除额外缝补动作， 根据额外缝补的总生命值恢复量， 增加第1次缝补的生命值恢复量\n
        生命值恢复量 +10%
        """
        ...

    def vp_2(self):
        """
        [苦痛庭院]\n
        技能命中的敌人时， 额外增加箴言人偶数量\n
        - 箴言人偶额外增加量 : 1个\n
        攻击范围 +50%\n
        [细心缝补]\n
        删除额外缝补动作， 根据额外缝补的总生命值恢复量， 增加第1次缝补的生命值恢复量\n
        生命值恢复量 +10%
        """
        ...

# 咆哮吧！ 疯疯熊
# mage_female/enchantress/25c0018b82c644f6e20d728f1478e671
# 3909d0b188e9c95311399f776e331da5/25c0018b82c644f6e20d728f1478e671
class Skill50(ActiveSkill):
    """
        疯疯熊瞬间变大， 深吸一口气后向前方喷吐强烈的诅咒气息。\n
        吐息经过的地面会变成浮动诅咒气息的诅咒地带。 队友进入诅咒地带时可以增加[禁术吟咏]和[小魔女的偏爱]的持续时间。
    """
    name = "咆哮吧！ 疯疯熊"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [860, 1500]
    uuid = "25c0018b82c644f6e20d728f1478e671"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 诅咒吐息攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 诅咒吐息多段攻击次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 诅咒地带持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 队友增益效果持续时间增加量 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [咆哮吧！ 疯疯熊]\n
        诅咒地带持续散发吸引周围敌人的气息， 并对接触诅咒地带的队员/敌人赋予不同的增益/减益效果\n
        - 队员 : 攻击速度、移动速度、施放速度 +20%\n
        - 敌人 : 攻击速度及移动速度 -50%\n
        - 增益/减益效果持续时间 : 5秒\n
        - 增益及减益无法刷新， 仅适用首次接触诅咒地带\n
        - 诅咒地带范围 +70%\n\n
        [林中小屋]\n
        林中小屋入口生成快速进入的光环， 可以从更远的位置进入\n\n
        进入地下城或角色复活后， 首次施放技能时， 不消耗箴言人偶
        """
        ...

    def vp_2(self):
        """
        [咆哮吧！ 疯疯熊]\n
        疯疯熊将移动到小魔女的后方， 发射覆盖前方大范围的强化吐息\n
        强化吐息不再生成诅咒地带， 大幅增加直接接触到吐息的队员的[禁术吟咏]和[小魔女的偏爱]持续时间\n
        - 队友增益效果持续时间额外增加量 : 90秒\n
        [林中小屋]\n
        林中小屋入口生成快速进入的光环， 可以从更远的位置进入\n
        进入地下城或角色复活后， 首次施放技能时， 不消耗箴言人偶
        """
        ...

# 欢迎光临人偶之森
# mage_female/enchantress/48d7d6b7617e6ed24027d1478f460c00
# 3909d0b188e9c95311399f776e331da5/48d7d6b7617e6ed24027d1478f460c00
class Skill51(ActiveSkill):
    """
        小魔女使用终极黑魔法将自身所处空间变成人偶之森的最深处的模样。 短时间后超巨大的疯疯熊登场， 毁灭眼前所有的敌人。\n
        在[开幕！ 人偶剧场]施放过程中使用[欢迎光临人偶之森]时， [开幕！ 人偶剧场]的技能持续不会影响[欢迎光临人偶之森]， 且效果会一直持续到[欢迎光临人偶之森]技能结束。
    """
    name = "欢迎光临人偶之森"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "48d7d6b7617e6ed24027d1478f460c00"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 技能持续时间 : 7秒
    # 吐息攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 吐息多段攻击次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 单手捶击攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 双手捶击攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 不祥的微笑
# mage_female/enchantress/2575e479271da5c46990ab0bb88dd677
# 3909d0b188e9c95311399f776e331da5/2575e479271da5c46990ab0bb88dd677
class Skill52(PassiveBufferSkill):
    """
        小魔女达到更高的境界， 变得从容不迫。 她的笑意比以前更加深不可测。\n
        增加基本攻击力和转职技能攻击力， 增加小魔女的智力。 部分技能附加额外效果。\n
    [蔷薇藤鞭]\n
        施放技能时， 若未命中敌人， 则技能冷却时间减少至1秒。 冷却时间减少后， 若再次施放[蔷薇藤鞭]依然未命中敌人， 则适用[蔷薇藤鞭]原来的技能冷却时间。\n
    [疯熊守护]\n
        忠实的护卫疯疯熊可以抵御1次小魔女受到的伤害， 并击退小魔女前方的敌人。 为了时刻准备抵御小魔女受到的攻击， 疯疯熊全身散发着阴森的气息， 震慑敌人。\n
        [疯熊守护]技能可通过On/Off设置是否激活防御功能。
    """
    name = "不祥的微笑"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 3
    uuid = "2575e479271da5c46990ab0bb88dd677"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 智力增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [疯熊守护]防御冷却时间 : 30秒

    INT = data1
    associate = [{"data": data1,"type": "$+INT","ratio":1}]

# 挚爱囚笼
# mage_female/enchantress/a080c9958fc2e4f87d6c55a727eb62b2
# 3909d0b188e9c95311399f776e331da5/a080c9958fc2e4f87d6c55a727eb62b2
class Skill53(ActiveSkill):
    """
        小魔女编织荆棘藤， 创造出巨大鸟笼。 为了表现对猎物的喜爱， 在鸟笼持续时间内， 小魔女会将其进行展览。 展览时间结束后， 鸟笼会向中央收缩， 将展览的敌人聚集在鸟笼中央后消失。\n
        若鸟笼中存在敌人， 则从敌人身上收获释放的魔力， 增加箴言人偶个数。\n
        不论命中多少敌人， 最多只增加1个箴言人偶。\n
        与[苦痛庭院]同时使用时， 可装饰出更加华丽恐怖的庭院， 此时可省略下一个技能的施放动作。\n
        再次按技能键， 鸟笼立即收缩后消失。
    """
    name = "挚爱囚笼"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 8 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [773, 6000]
    uuid = "a080c9958fc2e4f87d6c55a727eb62b2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 箴言人偶收获数量 : 1个
    # 生成鸟笼时攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 生成鸟笼时多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 展览时持续攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 展览时多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 鸟笼收缩时攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 鸟笼收缩时多段攻击次数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 终幕！ 人偶剧场
# mage_female/enchantress/caef38e23a8ae551466f8a8eb039df22
# 3909d0b188e9c95311399f776e331da5/caef38e23a8ae551466f8a8eb039df22
class Skill54(ActiveBufferSkill):
    """
        描绘贸然闯入人偶之森的敌人结局的人偶剧， 拉开终幕剧的帷幕。\n
        根据关联的觉醒技能， 展开不同的舞台。\n
        效果以[开幕！人偶剧场]的一定比率适用。\n
    选择[开幕！人偶剧场]时\n
        上演长篇终幕剧。\n
        长篇剧演出期间， 玩家将操纵疯疯熊， 赋予强化队友能力的效果。持续时间内， 减少50%的所受伤害， 并免疫控制型异常状态。疯疯熊状态下， 可以使用小魔女系列技能、 主动增益技能、 [替身草人]技能； 死亡时， 可以消耗1次箴言人偶并复活。同时， 可以放置使用[细心缝补]、 [爱之急救]技能； 荆棘藤系列技能攻击范围增加10%。小疯疯熊状态下， 可以强制中断当前动作， 并立即施放其他疯疯熊技能。\n
        (移动房间时， 维持效果)\n
    选择[欢迎光临人偶之森]时\n
        上演终幕剧的短篇舞台。\n
        舞台持续期间， 发动队友强化效果， 并可以与[开幕！人偶剧场]效果叠加。舞台结束后的一段时间内， [终幕！ 人偶剧场]的残骸在地图上消失之前， [终幕！ 人偶剧场]效果不会消失。\n
        (切换房间时， 效果解除)\n
        拉开帷幕前， 预输入[开幕！人偶剧场]技能键， 可以无施放动作， 立即发动[开幕！人偶剧场]， 上演更华丽的开幕剧。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "终幕！ 人偶剧场"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "caef38e23a8ae551466f8a8eb039df22"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    buffType = 'awakeSub'

    # 火焰攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 火焰多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 火焰终结攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 巨型疯疯熊攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 选择[开幕！人偶剧场]时效果
    # 力量、 智力增加 : [开幕！人偶剧场]的{value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 攻击、 移动速度增加 : [开幕！人偶剧场]的{value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 增益效果持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 选择[欢迎光临人偶之森]时效果
    # 力量、 智力增加 : [开幕！人偶剧场]的{value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 增益效果持续时间 : {value8}秒
    data8 = get_data(f'{prefix}/{uuid}', 8)

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

        self.name = 'enchantress'
        self.nameCN = '知源·小魔女'
        self.role = 'mage_female'
        self.角色 = '魔法师(女)'
        self.职业 = '小魔女'
        self.jobId = '3909d0b188e9c95311399f776e331da5'
        self.jobGrowId = '92da05ec93fb43406e193ffb9a2a629b'

        self.武器选项 = ['扫把','魔杖', '法杖', '矛', '棍棒'] # TODO
        self.输出类型选项 = ["魔法固伤"] # TODO
        self.输出类型 = '魔法固伤' # TODO
        self.防具精通属性 = ['智力'] # TODO
        self.防具类型 = '板甲'
        self.buff = ... # TODO

        self.buffer = True

        self.适用属性 = '智力'

        super().__init__(equVersion, __name__)

    def load_skills(self):
        super().load_skills()
        for skill in self.skills:
            if skill.buffer and skill.buffType == 'buff' and skill.learnLv == 30:
                self.BuffSkill = skill
            if skill.buffer and skill.buffType == 'awake':
                self.AwakeSkill = skill