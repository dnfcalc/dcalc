#0c1b401bb09241570d364420b3ba3fd7
from core.basic.skill import PassiveBufferSkill,ActiveBufferSkill,ActiveSkill,PassiveSkill, get_data
from core.basic.character import Character
prefix = "priest_female/crusader_female/cn/skillDetail"


# 圣光灌注
# priest_female/crusader_female/8f73f243041c2d27739fe7696f02bf9b
# 0c1b401bb09241570d364420b3ba3fd7/8f73f243041c2d27739fe7696f02bf9b
class Skill2(PassiveBufferSkill):
    """
        受到圣光的恩泽， 攻击变为光属性， 并增加光属性抗性和异常状态抗性， 攻击时附加属性伤害量增加的减益效果。\n
        属性伤害量增加效果持续一定时间， 最多可叠加一定次数， 且无法与光明骑士 (男) 的[守护恩赐]、 小魔女的[冥月绽放]、 缪斯的[多彩感性]、 协战师的[系统 · 战场信息]属性伤害量增加效果叠加。\n
        单人挑战时， 不适用增加属性伤害的减益效果， 而是增加自身独立攻击力， 减少技能冷却时间。
    """
    name = "圣光灌注"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 3
    rangeLv = 1
    uuid = "8f73f243041c2d27739fe7696f02bf9b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 光属性抗性增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 所有异常状态抗性增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 属性伤害量增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 属性伤害量增加持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 属性伤害量增加效果重叠次数上限 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [单人挑战专属效果]
    # 独立攻击力增加量 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 技能冷却时间减少量 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    CarryRatio = [0, (1.055 ** 3) * 100 - 100]# noqa: E501

# 启示 : 惩戒
# priest_female/crusader_female/42c82812f86ff6704ae9952a2e6093a4
# 0c1b401bb09241570d364420b3ba3fd7/42c82812f86ff6704ae9952a2e6093a4
class Skill3(PassiveSkill):
    """
        增加基本攻击、 跳跃攻击、 前冲攻击的攻击范围。\n
        增加基本攻击力、 技能攻击力、 攻击速度。
    """
    name = "启示 : 惩戒"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 4
    rangeLv = 2
    uuid = "42c82812f86ff6704ae9952a2e6093a4"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)


# 治愈祈祷
# priest_female/crusader_female/0969cd4054d93da07708108c0cc1c4b5
# 0c1b401bb09241570d364420b3ba3fd7/0969cd4054d93da07708108c0cc1c4b5
class Skill10(ActiveBufferSkill):
    """
        向神明祷告， 治疗自身的伤势， 恢复生命值。\n
        转职成为光明骑士时， 可以治疗队友， 并增加治疗量。\n
        学习[大天使的庇护]后， 施放[勇气颂歌]、 [新生颂歌]过程中可以使用该技能。
    """
    name = "治愈祈祷"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 3
    cd = 10
    mp = [15, 154]
    uuid = "0969cd4054d93da07708108c0cc1c4b5"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    upType = "heal"

    # 生命值恢复量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 转职成为光明骑士时， 生命值恢复量比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 治愈范围 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)


# 净化
# priest_female/crusader_female/4655101518604f874721b3cc249aae10
# 0c1b401bb09241570d364420b3ba3fd7/4655101518604f874721b3cc249aae10
class Skill13(ActiveBufferSkill):
    """
        使范围内的所有队员消除异常状态。
    """
    name = "净化"
    learnLv = 10
    masterLv = 1
    maxLv = 11
    position = 4
    rangeLv = 5
    cd = 15
    mp = [22, 238]
    uuid = "4655101518604f874721b3cc249aae10"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 异常状态消除数量上限 : {value0}个
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [范围信息]
    # [净化]适用范围 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)


# 圣洁之光
# priest_female/crusader_female/4224f9b0b8c7c903e9a1e0f9d9f6d04d
# 0c1b401bb09241570d364420b3ba3fd7/4224f9b0b8c7c903e9a1e0f9d9f6d04d
class Skill19(ActiveSkill):
    """
        使用圣洁之力生成光芒， 将其投向前方。\n
        光芒与敌人碰撞时会爆炸， 并给敌人造成光属性伤害。
    """
    name = "圣洁之光"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cd = 4
    mp = [27, 294]
    uuid = "4224f9b0b8c7c903e9a1e0f9d9f6d04d"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 爆炸攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [范围信息]
    # 爆炸大小比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 启示 : 颂歌
# priest_female/crusader_female/78bd107acd474518b606be1e4fd38239
# 0c1b401bb09241570d364420b3ba3fd7/78bd107acd474518b606be1e4fd38239
class Skill20(PassiveBufferSkill):
    """
        学习该技能后， 增加智力\n
        [勇气圣歌]的攻击功能可以在已学习的技能窗口上用鼠标右键设置开启/关闭。
    """
    name = "启示 : 颂歌"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 3
    uuid = "78bd107acd474518b606be1e4fd38239"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 智力增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0,"type":"$+INT","ratio":1}]

# 光杖精通
# priest_female/crusader_female/9cb6f9ed646fa87f9b7680a42ce83d1a
# 0c1b401bb09241570d364420b3ba3fd7/9cb6f9ed646fa87f9b7680a42ce83d1a
class Skill21(PassiveSkill):
    """
    독립 공격력과 마법 크리티컬 확률이 증가하고, 십자가 착용 시 캐스팅 속도가 증가한다.
    """
    name = "光杖精通"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 2
    rangeLv = 3
    uuid = "9cb6f9ed646fa87f9b7680a42ce83d1a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 独立攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [装备光杖时]
    # 施放速度增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    associate = [{"data": data0, "type": "$*PATKI"}]

# 胜利之矛
# priest_female/crusader_female/3d8f3d438405d79f8d3ed68072674d1e
# 0c1b401bb09241570d364420b3ba3fd7/3d8f3d438405d79f8d3ed68072674d1e
class Skill22(ActiveSkill):
    """
        向敌人投掷由神圣之力凝聚成的矛。\n
        矛可以穿刺敌人， 给敌人造成伤害， 并束缚敌人。 一定时间后， 矛会爆炸， 并追加伤害。\n
        若蓄气后投掷， 则增加束缚敌人的时间。\n
        当矛嵌入地面人时， 再次按技能键， 会立即引爆矛。\n
        学习[圣天使之光]后， 默认以最大蓄气状态施放。
    """
    name = "胜利之矛"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 7
    mp = [32, 343]
    uuid = "3d8f3d438405d79f8d3ed68072674d1e"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 穿刺攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 爆炸攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 蓄气时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 普通束缚时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 蓄气后束缚时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 枪大小比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 守护祝福
# priest_female/crusader_female/ade01c1d6afc8a05055225045e89fe49
# 0c1b401bb09241570d364420b3ba3fd7/ade01c1d6afc8a05055225045e89fe49
class Skill23(ActiveSkill):
    """
        祝福一定范围内的队友， 增加队友的生命值最大值、 魔法值最大值、 物防、 魔防、 体力、 精神， 效果持续一段时间。\n
        该技能效果不与光明骑士 (男) 的[守护徽章]以及小魔女的[小魔女的偏爱]、 缪斯的[主角登场]、 协战师的[装甲强化]技能效果叠加。
    """
    name = "守护祝福"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 4
    rangeLv = 3
    cd = 10
    mp = [35, 392]
    uuid = "ade01c1d6afc8a05055225045e89fe49"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 生命值/魔法值最大值增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 物理/魔法防御力增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 体力/精神增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 增益效果范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)


# 洗礼之光
# priest_female/crusader_female/ff171dc487807bb9aa28900ca9a46b41
# 0c1b401bb09241570d364420b3ba3fd7/ff171dc487807bb9aa28900ca9a46b41
class Skill25(ActiveSkill):
    """
        在前方落下神圣的洗礼之光， 给敌人造成伤害。\n
        按住向下键的同时施放该技能， 可以在更靠近自己的位置落下洗礼之光。\n
        学习[圣天使之光]后， 施放[勇气颂歌]、 [新生颂歌]过程中可以使用该技能， 此时攻击周围的敌人。
    """
    name = "洗礼之光"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cd = 7
    mp = [32, 343]
    uuid = "ff171dc487807bb9aa28900ca9a46b41"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 圣光守护
# priest_female/crusader_female/547ab2b2bd860d3e37355a9cfbc1077c
# 0c1b401bb09241570d364420b3ba3fd7/547ab2b2bd860d3e37355a9cfbc1077c
class Skill26(ActiveSkill):
    """
        使范围内的队友置身于神圣的光晕中， 效果持续一定时间。\n
        在此状态下， 光晕会减少队友受到的伤害， 且使队友被攻击时， 不会进入僵直状态， 持续时间过后， 光晕会爆炸， 给敌人造成光属性伤害。\n
        光晕持续时间内再次按技能键， 光晕立即爆炸。\n
        在施放[勇气颂歌]、 [新生颂歌]过程中， 可以使用[圣光守护]。\n
        在决斗场中， 在持续时间内减少移动速度， 同时增加[守护祝福]的增益效果。
    """
    name = "圣光守护"
    learnLv = 25
    masterLv = 50
    maxLv = 60
    position = 5
    rangeLv = 3
    cd = 20
    mp = [15, 154]
    uuid = "547ab2b2bd860d3e37355a9cfbc1077c"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 光晕持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 爆炸攻击力(自身) : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 爆炸攻击力(队员) : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 所受伤害减少率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [决斗场]
    # 移动速度减少率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [守护祝福]效果增幅率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]增益效果范围 : {value6}px
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 爆炸大小比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

# 勇气祝福
# priest_female/crusader_female/8c2379737c5acc935c1731f67f607655
# 0c1b401bb09241570d364420b3ba3fd7/8c2379737c5acc935c1731f67f607655
class Skill27(ActiveBufferSkill):
    """
        使范围内的队友增加物理/魔法/独立攻击力、 力量、 智力和命中率， 并增加自身基本攻击力和技能攻击力， 效果持续一段时间。\n
        施放者的智力越高， 物理/魔法/独立攻击力、 力量、 智力的增加量越多。\n
        达到20级以上后， 不再增加自身基本攻击力和技能攻击力， 且物理/魔法/独立攻击力、 力量、 智力增加效果不适用于自身。\n
        效果不与光明骑士 (男) 的[荣誉祝福]、 小魔女的[禁术吟咏]、 缪斯的[可爱节拍]、 协战师的[军械强化]的技能效果叠加。
    """
    name = "勇气祝福"
    learnLv = 30
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 3
    cd = 10
    uuid = "8c2379737c5acc935c1731f67f607655"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    buffer = True
    buffType = "buff"

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理/魔法/独立攻击力增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 力量/智力增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 命中率增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 基本攻击力和技能攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 增益效果范围 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)

    ATK = data1
    STRINT = data2

# 圣光烬盾
# priest_female/crusader_female/5dc7008b12a459325b548b0715c6b73c
# 0c1b401bb09241570d364420b3ba3fd7/5dc7008b12a459325b548b0715c6b73c
class Skill28(ActiveSkill):
    """
        生成神圣的光芒墙壁向前推进。\n
        光芒墙壁会推进撞到的敌人并造成持续伤害， 到达最远距离后墙壁会爆炸。
    """
    name = "圣光烬盾"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cd = 10
    mp = [91, 763]
    uuid = "5dc7008b12a459325b548b0715c6b73c"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 撞击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 爆炸攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 盾牌大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 爆炸大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 神光惩戒
# priest_female/crusader_female/7e904ea3d2a9faa054604e55120a9268
# 0c1b401bb09241570d364420b3ba3fd7/7e904ea3d2a9faa054604e55120a9268
class Skill29(ActiveSkill):
    """
        凝聚光的力量， 快速挥击3次攻击敌人。\n
        施放技能时， 按下方向键可使角色边移动边攻击敌人。\n
        攻击成功时， 可以强制中断并立即施放[神光十字]、 [忏悔重击]； [神光十字]、 [忏悔重击]命中敌人时， 可强制中断并施放[神光惩戒]。\n
        决斗场中无法强制中断并立即施放其他技能。
    """
    name = "神光惩戒"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 10
    mp = [400, 1000]
    uuid = "7e904ea3d2a9faa054604e55120a9268"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 第一击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第二击攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 第三击攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 勇气颂歌
# priest_female/crusader_female/506e7ed77d517419a6e1c437a2cedb17
# 0c1b401bb09241570d364420b3ba3fd7/506e7ed77d517419a6e1c437a2cedb17
class Skill30(ActiveBufferSkill):
    """
        颂唱勇气颂歌， 增强范围内我方的增益效果， 对敌人造成伤害。\n
        颂歌结束或离开效果范围后， 增益效果仍将持续一定时间。\n
        [勇气颂歌]持续期间， 减少光明骑士所受伤害， 并增加所有异常状态抗性。\n
        [勇气颂歌]施放过程中， 可以用方向键移动； 连续按攻击键可以减少颂歌的持续时间和多段攻击的间隔； 按跳跃键会终止[勇气颂歌]。\n
        施放过程中， 可以施放[圣光守护]、 [神之教诲]、 [圣洁之翼]、 [圣佑之阵]、 [圣言十字]； 学习[大天使的庇护]后， 可以施放[治愈祈祷]； 学习圣天使之光后， 可以施放[洗礼之光]。\n
        学习[大天使的庇护]后， 增加[勇气颂歌]范围。
    """
    name = "勇气颂歌"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 3
    cube = 1
    cd = 40
    mp = [150, 1260]
    uuid = "506e7ed77d517419a6e1c437a2cedb17"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    buffer = True
    buffType = "buffSub"

    # 颂歌持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 颂歌增益效果持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [勇气祝福]增益效果增幅率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 颂歌多段攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 颂歌的攻击次数上限 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 颂歌多段攻击间隔 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 所受伤害减少率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 所有异常状态抗性增加 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [范围信息]
    # 颂歌范围 : {value8}px
    data8 = get_data(f'{prefix}/{uuid}', 8)

    def skillInfo(self):
        prep = self.char.BuffSkill.skillInfo()
        ratio = self.data2[self.lv] / 100
        return prep[0] * ratio, [prep[1][0]*ratio,prep[1][1],prep[1][2]*ratio], [prep[2][0]*ratio,prep[2][1],prep[2][2]*ratio],0,self.getSkillCD()

    def vp_1(self):
        """
        [勇气颂歌]\n
        由大天使米迦勒代替施放[勇气颂歌]\n
        - 多段攻击间隔 -15%\n
        - 多段攻击次数 +2次\n
        - 总攻击力相同\n
        [新生圣歌]\n
        大天使乌列尔出现， 和光明骑士一起施放[新生颂歌]\n
        - 每秒生命值恢复量 +35%
        """
        ...

    def vp_2(self):
        """
        [勇气颂歌]\n
        范围 +40%\n
        施放过程中适用以下效果\n
        - 移动速度 +200%\n
        - 所受伤害减少量额外 +40%\n
        - 所有状态异常抗性增加量额外 +30%\n
        [新生圣歌]\n
        大天使乌列尔出现， 和光明骑士一起施放[新生颂歌]\n
        - 每秒生命值恢复量 +35%
        """
        ...

# 神圣锁环
# priest_female/crusader_female/8ee0099656df08a0b39225f8a21d514b
# 0c1b401bb09241570d364420b3ba3fd7/8ee0099656df08a0b39225f8a21d514b
class Skill31(ActiveSkill):
    """
        在前方召唤出神圣的光环。\n
        束缚光环范围内的敌人后向内聚拢， 造成多段攻击后爆炸。\n
        光环缩小后再次按技能键， 光环会立即爆炸。\n
        在决斗场中再次按技能键时， 光环不会爆炸。
    """
    name = "神圣锁环"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cube = 1
    cd = 18
    mp = [150, 1260]
    uuid = "8ee0099656df08a0b39225f8a21d514b"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 多段攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 13
    # 多段攻击间隔 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 环大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [神圣锁环]\n
        拉贵尔在前方进行大范围攻击后， 为光明骑士赋予一定时间的惩恶天使增益效果\n
        - 删除强制控制效果\n
        - 攻击次数 : 10次\n
        - 总攻击力相同\n
        - 增益持续时间 : 15秒\n
        [圣洁之光]\n
        惩恶天使增益效果\n
        - 范围 +25%\n
        - 穿过敌人并移动200px后爆炸\n
        - 光移动速度增加\n
        - 击退光移动路径上的敌人\n
        [圣光守护]\n
        保护罩功能强化\n
        - 保护罩持续时间 +50%\n
        - 通过再次按下技能键进行爆炸攻击时， 保护罩不会消失\n
        - 物理、 魔法伤害减少效果与[圣佑之阵]重叠
        """
        ...

    def vp_2(self):
        """
        [神圣锁环]\n
        对周围的敌人施放[神圣锁环]\n
        - 攻击范围 : 600px\n
        - 范围内存在敌人时可以施放技能\n
        可以在施放以下技能过程中施放该技能\n
        - [勇气颂歌]\n
        - [新生颂歌]\n
        [圣光守护]\n
        保护罩功能强化\n
        - 保护罩持续时间 +50%\n
        - 通过再次按下技能键进行爆炸攻击时， 保护罩不会消失\n
        - 物理、 魔法伤害减少效果与[圣佑之阵]重叠
        """
        ...

# 神之教诲
# priest_female/crusader_female/9bff7f2559e003766fee2853dca00631
# 0c1b401bb09241570d364420b3ba3fd7/9bff7f2559e003766fee2853dca00631
class Skill32(ActiveBufferSkill):
    """
        祝福范围内的队友， 大幅增加队友的移动速度， 效果持续一定时间。\n
        进入下一个房间时， 增加移动速度的效果会消失。\n
        施放[勇气颂歌]、 [新生颂歌]时， 可以使用[神之教诲]。
    """
    name = "神之教诲"
    learnLv = 35
    masterLv = 1
    maxLv = 1
    position = 5
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [630, 630]
    uuid = "9bff7f2559e003766fee2853dca00631"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 移动速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 增益效果范围 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 忏悔之雷
# priest_female/crusader_female/da6e37c1e3f0e8867f70007d89c239ff
# 0c1b401bb09241570d364420b3ba3fd7/da6e37c1e3f0e8867f70007d89c239ff
class Skill33(ActiveSkill):
    """
        在前方落下闪电， 给敌人持续造成光属性魔法伤害。\n
        被最后一道闪电击中的敌人会解除其增益效果， 有一定几率进入忏悔状态。\n
        进入忏悔状态的敌人会攻击自己的友军。\n
        对领主、 精英、 稀有、 深渊类怪物， 忏悔效果会有所缩减， 对人形怪物会大幅减少忏悔几率及忏悔持续时间。\n
        在决斗场中， 解除对敌人赋予的效果， 不适用忏悔状态。
    """
    name = "忏悔之雷"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cube = 1
    cd = 18
    mp = [160, 1344]
    uuid = "da6e37c1e3f0e8867f70007d89c239ff"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 多段落雷攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 最后一道闪电魔法攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 忏悔几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 忏悔持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [驱散魔法]解除数量上限 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 多段落雷大小比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 最后一道闪电大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [忏悔之雷]\n
        直接施放最终闪电\n
        - 删除多段闪电\n
        - 总攻击力相同\n
        - 最终闪电大小 +35%\n
        [复苏之光]\n
        大天使拉法尔降临， 和光明骑士一起施放[复苏之光]\n
        - [复苏之光]有效范围变更为全地图\n
        - [复苏之光]复活对象的生命值/魔法值恢复量 +15%
        """
        ...

    def vp_2(self):
        """
        [忏悔之雷]\n
        删除终结攻击， 多段攻击次数 +5次\n
        - 总攻击力相同\n
        可以在施放以下技能过程中施放该技能\n
        - [勇气颂歌]\n
        - [新生颂歌]\n
        施放颂歌时， 雷米尔会进行闪电攻击\n
        - 攻击范围 : 与[勇气颂歌]相同\n
        - 多段攻击次数 : 10次\n
        - 总攻击力相同\n
        [复苏之光]\n
        大天使拉法尔降临， 和光明骑士一起施放[复苏之光]\n
        - [复苏之光]有效范围变更为全地图\n
        - [复苏之光]复活对象的生命值/魔法值恢复量 +15%
        """
        ...

# 复苏之光
# priest_female/crusader_female/a6c8f69107f8c4f5d1a0c7a57d000290
# 0c1b401bb09241570d364420b3ba3fd7/a6c8f69107f8c4f5d1a0c7a57d000290
class Skill34(ActiveSkill):
    """
        使用神圣的力量， 复活死亡的队友。\n
        与光明骑士 (女) 组队时， 死亡后会躺在地面， 保持死亡待机状态一定时间。\n
        死亡待机状态下， 维持获得的增益效果， 当光明骑士 (女) 施放[复苏之光]时， 会带着一定量的生命值和魔法值原地复活。\n
        一次性可复活的队员人数有限制； 复活时， 不会初始化技能冷却时间。\n
        在死亡待机状态持续时间中输入攻击键会立即死亡， 使用复活币复活时， 复活之前获得的效果会消失。\n
    사망 대기 상태의 파티원 수가 한번에 부활 가능한 파티원 수를 초과할 경우, 크루세이더(여)와 근접한 파티원을 우선으로 부활시킨다.\n
        学习[大天使的庇护]后， 增加复活范围。
    """
    name = "复苏之光"
    learnLv = 40
    masterLv = 1
    maxLv = 11
    position = 5
    rangeLv = 2
    cube = 2
    mp = [200, 1680]
    uuid = "a6c8f69107f8c4f5d1a0c7a57d000290"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 队友死亡状态持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 队友复活时， 生命值和魔法值恢复量 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 复活队友数量上限 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 复活适用范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def getSkillCD(self,mode=None):
        return 0

# 神光十字
# priest_female/crusader_female/3829c15bf5f520c13998a3479ba0ce7b
# 0c1b401bb09241570d364420b3ba3fd7/3829c15bf5f520c13998a3479ba0ce7b
class Skill35(ActiveBufferSkill):
    """
        生成神圣的光杖， 猛力捶向前方地面。\n
        地面被光杖捶裂后， 会涌出光晕， 被命中的敌人会浮空。\n
        当队友接触到这些光晕时， 会延长当前携带的光明骑士 (女) 效果的持续时间。 (每次施放技能时只适用一次)\n
        [神光十字]命中敌人后， 可以强制中断并立即施放[神光惩戒]、 [忏悔重击]。\n
        在决斗场中无法强制中断并施放其他技能。
    """
    name = "神光十字"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [350, 2940]
    uuid = "3829c15bf5f520c13998a3479ba0ce7b"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 捶击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 增益效果持续时间增加 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 光杖大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [神光十字]\n
        神光十字攻击强化\n
        - 大小 +50%\n
        - 生成神光十字时击退附近敌人\n
        - 删除撞击攻击\n
        - 总攻击力相同\n
        - 冲击波攻击使敌人进入眩晕状态3秒\n
        光之气息流出的裂痕功能强化\n
        - 光杖地面裂痕使队友恢复20%的生命值和魔法值\n
        - 光杖地面裂痕持续时间 +5秒
        """
        ...

    def vp_2(self):
        """
        [神光十字]\n
        施放前僵直 -20%\n
        可以强制中断转职技能的施放后僵直并施放 (觉醒技能除外)\n
        光之气息流出的裂痕功能强化\n
        - 光杖地面裂痕使队友恢复20%的生命值和魔法值\n
        - 光杖地面裂痕持续时间 +5秒
        """
        ...

# 新生颂歌
# priest_female/crusader_female/03bb5314ffd41e9458d67ef924fef38f
# 0c1b401bb09241570d364420b3ba3fd7/03bb5314ffd41e9458d67ef924fef38f
class Skill36(ActiveBufferSkill):
    """
        颂唱新生颂歌， 为范围内队友解除异常状态， 并恢复队友的生命值。\n
        [新生颂歌]持续时间内， 减少光明骑士所受伤害， 并增加所有异常状态抗性。\n
        [新生颂歌]施放过程中， 可以用方向键移动； 按跳跃键会终止[新生颂歌]。\n
        施放过程中， 可以施放[圣光守护]、 [神之教诲]、 [圣洁之翼]、 [圣佑之阵]、 [圣言十字]； 学习[大天使的庇护]后， 可以施放[治愈祈祷]； 学习圣天使之光后， 可以施放[洗礼之光]。\n
        学习[大天使的庇护]后， 增加[新生颂歌]范围。
    """
    name = "新生颂歌"
    learnLv = 45
    masterLv = 1
    maxLv = 11
    position = 2
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [350, 2940]
    uuid = "03bb5314ffd41e9458d67ef924fef38f"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    upType = "heal"

    # 颂歌持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 解除异常状态数量上限 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 生命值恢复量 : 每秒<pnumber>%
    # 所受伤害减少率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 所有异常状态抗性增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 颂歌范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 虔诚信念
# priest_female/crusader_female/1dad88963abdc96b091fcab185a8820d
# 0c1b401bb09241570d364420b3ba3fd7/1dad88963abdc96b091fcab185a8820d
class Skill37(PassiveBufferSkill):
    """
        光明歌颂者的虔诚信念感动了周围的队友， 增加队友的力量、 智力、 体力、 精神、 攻击速度、 移动速度和施放速度， 并增加本人的基本攻击力和技能攻击力。\n
        光明歌颂者的技能命中敌人时， 可以延长队友携带的增益效果持续时间。
    """
    name = "虔诚信念"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 3
    uuid = "1dad88963abdc96b091fcab185a8820d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 力量/智力增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 体力/精神增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击/移动/施放速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 增益效果持续时间增加 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 基本攻击力和技能攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 光环范围 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)

    STRINT = data0
    INT = data0

    associate = [
        {"data":INT,"type":"$+INT","ratio":1}
    ]

# 圣光天启
# priest_female/crusader_female/bb34e8854a93fd250347a1c64119f7ab
# 0c1b401bb09241570d364420b3ba3fd7/bb34e8854a93fd250347a1c64119f7ab
class Skill38(ActiveBufferSkill):
    """
        光明歌颂者打开蕴含神力的圣书， 神圣的气息会飞向队友。 神圣的气息会祝福我军， 增加力量、 智力、 攻击速度、 移动速度和施放速度， 效果持续一定时间。\n
        此后， 胜利的光杖出现在空中， 光明歌颂者会抓取光杖后插在地面。 光杖会喷发耀眼的光芒， 光芒碰到敌人后会造成多段伤害， 之后光芒爆炸。\n
        技能施放过程中进入无敌状态； 胜利的光杖消失之前， 我军获得[勇气颂歌]的攻击力增幅效果。\n
        力量、 智力的增加量随施放者的智力值增加而增多； 力量、 智力提升效果对自身无效。\n
        效果不与光明骑士 (男) 的[天启之光]和小魔女的[开幕！ 人偶剧场]、  缪斯的[梦想的舞台]、 协战师的[强袭策略 : 区域肃清]的效果叠加。
    """
    name = "圣光天启"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 5
    cube = 5
    cd = 170
    mp = [1200, 10080]
    uuid = "bb34e8854a93fd250347a1c64119f7ab"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    buffType = 'awake'

    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 力量/智力增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击/移动/施放速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 多段攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 多段攻击间隔 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 爆炸攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)

    STRINT = data1

# 苦修
# priest_female/crusader_female/2a0a39184de92acf1c1375e00b77404c
# 0c1b401bb09241570d364420b3ba3fd7/2a0a39184de92acf1c1375e00b77404c
class Skill39(PassiveSkill):
    """
        掌握该技能后， 力量和物理暴击率会调整为与智力和魔法暴击率相同的数值。\n
        [苦修后获得的这股力量， 只为守护你而使用。]
    """
    name = "苦修"
    learnLv = 50
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 3
    uuid = "2a0a39184de92acf1c1375e00b77404c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 忏悔重击
# priest_female/crusader_female/27bade584bb42fef68148d3a0b72bace
# 0c1b401bb09241570d364420b3ba3fd7/27bade584bb42fef68148d3a0b72bace
class Skill40(ActiveSkill):
    """
        使用神圣之力， 生成巨大的神光惩戒， 大幅度挥动两次光杖。\n
        被击中的敌人会被拽到的前方。\n
        命中敌人时， 可强制中断并施放[神光惩戒]、 [神光十字]；[神光惩戒]、 [神光十字]命中敌人时， 可强制中断并施放[忏悔重击]。
    """
    name = "忏悔重击"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 2
    cube = 2
    cd = 30
    mp = [400, 1000]
    uuid = "27bade584bb42fef68148d3a0b72bace"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 第一击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 第二击攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 光杖大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [忏悔重击]\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 15秒\n
        - 单次攻击力 -50%\n
        神光十字攻击强化\n
        - 光杖大小 +30%\n
        - 可以吸附无法抓取的敌人\n
        - 第2次挥击命中时， 引发光之爆炸\n
        - 光之爆炸攻击力 : 第2次挥击攻击力的11%\n
        - 总攻击力相同\n
        [圣光天启]\n
        满足以下条件时当前冷却时间减少1秒 (最多25秒)\n
        - [圣光灌注] : 属性伤害量增加效果持续5秒时\n
        - [虔诚信念] : 增益效果持续时间更新效果发动时\n
        - [新生颂歌] : 对队友施加恢复效果时\n
        - [圣光普照] : 对队友施加恢复效果时
        """
        ...

    def vp_2(self):
        """
        [忏悔重击]\n
        仅发动第2次挥击攻击\n
        - 不再吸附敌人\n
        - 总攻击力相同\n
        可以强制中断施放后僵直并施放转职技能 (觉醒技能除外)\n
        [圣光天启]\n
        满足以下条件时当前冷却时间减少1秒 (最多25秒)\n
        - [圣光灌注] : 属性伤害量增加效果持续5秒时\n
        - [虔诚信念] : 增益效果持续时间更新效果发动时\n
        - [新生颂歌] : 对队友施加恢复效果时\n
        - [圣光普照] : 对队友施加恢复效果时
        """
        ...

# 圣洁之翼
# priest_female/crusader_female/04883563896fe1adac7505c6146b5f59
# 0c1b401bb09241570d364420b3ba3fd7/04883563896fe1adac7505c6146b5f59
class Skill41(ActiveBufferSkill):
    """
        祝福周围的队友， 受到祝福的队友会增加力量、 智力、 攻击速度、 移动速度和施放速度， 效果持续一定时间。\n
        祝福持续时间内， 再次按技能键时， 会在受到祝福的队友和自身周围引发强烈的爆炸， 给敌人造成伤害。\n
        祝福持续时间内， 当自身技能命中敌人时， 可以获得大天使的气息， 凝聚的大天使的气息越多， 爆炸大小越大。\n
        在施放[勇气颂歌]、 [新生颂歌]过程中， 可以使用[圣洁之翼]。\n
        力量和智力增加效果仅适用于队友， 并不适用于自身。
    """
    name = "圣洁之翼"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [860, 1500]
    uuid = "04883563896fe1adac7505c6146b5f59"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 祝福持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 力量和智力增加 (队友) : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 所有速度增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 爆炸攻击力 (自身) : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 爆炸攻击力 (队友) : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 大天使的气息叠加数量上限 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 祝福有效范围 : {value6}px
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 爆炸大小比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    def vp_1(self):
        """
        [圣洁之翼]\n
        以大天使的气息最大叠加的状态施放\n
        - 爆炸范围 +40%\n
        受到祝福的队友获得以下效果\n
        - 生成光电护盾， 持续10秒\n
        - 对周围的敌人造成光属性多段伤害\n
        - 光电护盾的攻击力 : 爆炸攻击力的1%\n
        - 总攻击力相同\n
        [神之教诲]\n
        增益持续效果强化\n
        - 切换房间后效果也不会消失\n
        - 增益效果持续时间 +2秒
        """
        ...

    def vp_2(self):
        """
        [圣洁之翼]\n
        删除追加输入技能键功能和爆炸攻击\n
        受到祝福的状态下攻击时， 吉普莉尔发动大天使的审判\n
        - 大天使的审判发动次数 : 总共10次\n
        - 大天使的审判发动冷却时间 : 0.5秒\n
        - 总攻击力相同\n
        强化自身增益效果\n
        - 在空中按跳跃键可再跳跃一次\n
        - 在空中长按技能2键时， 下降速度减少\n
        - 스킬2키는 기본적으로 'Space'로 지정되어 있으며, 게임 설정창에서 단축키 설정으로 변경 가능\n
        [神之教诲]\n
        增益持续效果强化\n
        - 切换房间后效果也不会消失\n
        - 增益效果持续时间 +2秒
        """
        ...

# 大天使的庇护
# priest_female/crusader_female/dbf8b30c7057032af0d68fcfa289fdae
# 0c1b401bb09241570d364420b3ba3fd7/dbf8b30c7057032af0d68fcfa289fdae
class Skill42(PassiveBufferSkill):
    """
        炽天使得到大天使的庇护， 增加智力、 魔法暴击率和暴击伤害， [勇气颂歌]、 [新生颂歌]、 [复苏之光]技能得到加强。\n
        神力与信念超越人类的境界， 当生命值变为0时， 大天使会出现进行复活。\n
        施放[勇气颂歌]、 [新生颂歌]过程中， 可以施放[治愈祈祷]。\n
        复活有冷却时间， 复活自身的功能可以在已学的技能栏中通过鼠标右击进行开启/关闭切换。
    """
    name = "大天使的庇护"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 3
    uuid = "dbf8b30c7057032af0d68fcfa289fdae"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 智力增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法暴击增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 暴击伤害增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [勇气颂歌]、 [新生颂歌]、 [复苏之光]范围增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 自身复活时恢复生命值 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 自身复活冷却时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)

    associate = [
        {"data":data0 ,"type":"$+INT","ratio":1}
    ]

# 圣佑之阵
# priest_female/crusader_female/5152480fdde81362575a488d4cec4af9
# 0c1b401bb09241570d364420b3ba3fd7/5152480fdde81362575a488d4cec4af9
class Skill43(ActiveBufferSkill):
    """
        布置大天使圣佑之阵， 从危险中保护自己和队友， 并给予敌人造成伤害。\n
        结界将持续一定时间， 范围内队友获得霸体状态， 并且提高攻击速度、 移动速度、 施放速度， 减少所受伤害； 施放者进入无敌状态。\n
        减伤效果与圣光守护的减伤效果不能重叠， 两者当中数值更高的一个会生效。\n
        施放[勇气颂歌]、 [新生颂歌]过程中， 可以使用[圣佑之阵]。
    """
    name = "圣佑之阵"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 3
    cd = 50
    mp = [580, 4500]
    uuid = "5152480fdde81362575a488d4cec4af9"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 结界持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 结界攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 攻击、 移动、 施放速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 队员所受伤害减少率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 结界范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [圣佑之阵]\n
        结界范围 +35%\n
        可以强制中断结界生成后僵直并移动或施放技能\n
        结界内的队友获得以下效果\n
        - 进入无敌状态1.5秒\n
        - 每次技能仅发动1次
        """
        ...

    def vp_2(self):
        """
        [圣佑之阵]\n
        施放转职技能时可以发动 (觉醒技能除外)\n
        结界持续时间变更为1.5秒\n
        自身适用的攻击/移动/施放速度增加量 +200%\n
        结界内的队友获得以下效果\n
        - 进入无敌状态1.5秒\n
        - 每次技能仅发动1次
        """
        ...

# 圣光普照
# priest_female/crusader_female/2391a27457b5a8c6fa4b4670a91bdd11
# 0c1b401bb09241570d364420b3ba3fd7/2391a27457b5a8c6fa4b4670a91bdd11
class Skill44(ActiveBufferSkill):
    """
        利用奇迹之光治疗队友并攻击敌人。\n
        圣光普照命中队友或敌人时， 不分敌我进行游移， 在队友身上产生回血效果， 给敌人造成多段攻击伤害。\n
        首次目标范围内没有队友或敌人时， 不会施放圣光普照； 没有队友，只存在一名敌人时， 圣光普照的攻击力得到强化。
    """
    name = "圣光普照"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 5
    cd = 40
    mp = [860, 1500]
    uuid = "2391a27457b5a8c6fa4b4670a91bdd11"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 光线最大移动次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 队员生命值恢复量 : <pnumber2>%
    # 队员生命值恢复间隔 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 队员生命值恢复次数 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 多段攻击攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 多段攻击间隔 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 多段攻击次数上限 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 一个敌人时的攻击力增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 首次索敌范围 (X轴) : {value7}px
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 首次索敌范围 (Y轴) : {value8}px
    data8 = get_data(f'{prefix}/{uuid}', 8)

    def vp_1(self):
        """
        [圣光普照]\n
        施放时， 召唤米迦勒的圣光球\n
        - 持续3秒， 向范围内的敌人与队友发射1次奇迹之光\n
        - 奇迹之光命中的敌人与队友适用圣光普照效果\n
        - 删除攻击个体限制， 删除仅为1名敌人时的伤害增幅功能\n
        范围 +45%
        """
        ...

    def vp_2(self):
        """
        [圣光普照]\n
        施放时， 召唤米迦勒的圣光球\n
        - 持续3秒， 向范围内的敌人与队友发射1次奇迹之光\n
        - 奇迹之光命中的敌人与队友适用圣光普照效果\n
        - 删除攻击个体限制， 删除仅攻击1名敌人时的伤害增幅功能\n
        攻击和恢复次数上限 -50%\n
        - 总攻击力/恢复量相同\n
        可以在施放以下技能过程中施放该技能\n
        - [勇气颂歌]\n
        - [新生颂歌]
        """
        ...

# 救赎彼岸 : 惩戒圣枪
# priest_female/crusader_female/5892d1fa4462e561ac8f8d2c74892b0a
# 0c1b401bb09241570d364420b3ba3fd7/5892d1fa4462e561ac8f8d2c74892b0a
class Skill45(ActiveSkill):
    """
        用蕴含神力的圣枪“布里欧纳克”歼灭邪恶。\n
        施放技能时， 用圣光长矛穿透敌人， 然后飞向天空， 朝地面投掷圣枪布里欧纳克。\n
        圣枪布里欧纳克撞到敌人后造成魔法伤害， 插入地面引发巨大的爆炸， 对敌人造成强大的魔法伤害。 \n
        施放技能时， 进入无敌状态， 被圣光长矛穿透敌人进入强制控制状态。
    """
    name = "救赎彼岸 : 惩戒圣枪"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "5892d1fa4462e561ac8f8d2c74892b0a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 长枪穿透攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 长枪爆炸攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

# 圣天使之光
# priest_female/crusader_female/5cac3411ccef1af333953e0ded5e942d
# 0c1b401bb09241570d364420b3ba3fd7/5cac3411ccef1af333953e0ded5e942d
class Skill46(PassiveBufferSkill):
    """
        增加智力、 基本攻击力和转职技能攻击力， 部分技能赋予特殊效果。\n
    [胜利之矛]\n
        不论是否蓄气， 均以最大蓄气的状态施放。\n
    [洗礼之光]\n
        施放[勇气颂歌]、 [新生颂歌]过程中可以使用该技能， 此时会攻击光明骑士周围的敌人。\n
        <大天使萨菲尔， 这是我的权能。>
    """
    name = "圣天使之光"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "5cac3411ccef1af333953e0ded5e942d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 智力增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [
        {"data":data1,"type":"$+INT","ratio":1}
    ]

# 圣言十字
# priest_female/crusader_female/85f7c810ad503790e8626439fe936d56
# 0c1b401bb09241570d364420b3ba3fd7/85f7c810ad503790e8626439fe936d56
class Skill47(ActiveSkill):
    """
        神圣的光芒从天而降， 在前方萨菲尔的光杖插入地面， 形成圣域。\n
        萨菲尔的光杖在一定时间内对周围敌人造成多段伤害， 然后爆炸。\n
        可以在[勇气颂歌]与[新生颂歌]施放过程中使用； 光杖存在期间再次按技能键， 可以立即引爆光杖。\n
        圣域内， 增加[勇气颂歌]增益效果持续时间， [新生颂歌]生命值恢复速度， [圣佑之阵]的攻击速度、 移动速度、 施放速度增加量\n
        每施放1次技能， 只能发动一次技能强化效果。 [勇气颂歌]增益效果持续时间增加效果， 适用于发动中的颂歌增益效果， 不适用于[圣光天启]和[祈愿·天使赞歌]的[勇气颂歌]增幅效果。\n
        <施惠于众生， 铲除邪恶>
    """
    name = "圣言十字"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [960, 7200]
    uuid = "85f7c810ad503790e8626439fe936d56"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 光仗落下冲击波攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 圣域多段攻击力 : {value1} x {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 20
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 光杖爆炸攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [勇气颂歌]增益效果持续时间增加 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [新生颂歌]生命值恢复速度增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [圣佑之阵]所有速度增加 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

# 祈愿·天使赞歌
# priest_female/crusader_female/002cbdd9bfd0f0b970451ae8d48d029e
# 0c1b401bb09241570d364420b3ba3fd7/002cbdd9bfd0f0b970451ae8d48d029e
class Skill48(ActiveBufferSkill):
    """
    化身大天使萨菲尔降临， 与7大天使一起向神咏唱赞歌。\n
        咏唱赞歌时， 向队友施加增益效果。 赞歌结束后， 释放出灿烂光芒， 对敌人造成强大伤害。\n
        施放时进入无敌状态， 根据关联的觉醒技能， 7大天使的演奏形态和增益效果会有所不同， 并且一定时间内[勇气颂歌]技能的勇气祝福增益效果会得到增幅。\n
    选择[圣光天启]时\n
        大天使吉普莉尔、 拉贵尔、 沙利叶、 雷米尔与萨菲尔一起， 出现在队友身后进行独奏并提供效果， 一定时间内提供力量和智力， 以及攻击速度、 移动速度和施放速度增益效果。\n
        (移动到其他房间时维持效果)\n
    选择[救赎彼岸 : 惩戒圣枪]时\n
        7大天使进行合奏， 提供力量和智力增益效果， 效果持续一段时间。 (可以与[圣光天启]增益效果叠加， 移动到其他房间时解除效果)\n
        萨菲尔降临、 呈现天国景象之前， 预输入[圣光天启]技能键， 可以省略施放动作使用该技能； 预输入时， [圣光天启]的攻击力以一定比率合并入[祈愿·天使赞歌]的终结攻击力中。\n
        [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。\n
        <全能的雷米迪奥斯啊， 请聆听我们的赞歌>
    """
    name = "祈愿·天使赞歌"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4025, 8055]
    uuid = "002cbdd9bfd0f0b970451ae8d48d029e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    buffType = 'awakeSub'

    # 终结多段攻击力 : {value0} x {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 终结爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [选择圣光天启时效果]
    # 增益效果持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 力量、 智力增加量 : [圣光天启]的{value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 攻击、 移动、 施放速度增加 : [圣光天启]的{value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [选择救赎彼岸 : 惩戒圣枪时效果]
    # 增益效果持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 力量、 智力增加量 : [圣光天启]的{value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 预输入[圣光天启]时攻击力合并计算比率 : {value8}%
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

        self.name = 'crusader_female'
        self.nameCN = '神启·圣职者'
        self.role = 'priest_female'

        self.武器选项 = ['十字架','镰刀', '念珠', '战斧','图腾' ]
        self.输出类型选项 = ['魔法固伤']
        self.输出类型 = '魔法固伤'
        self.防具精通属性 = ['智力']
        self.防具类型 = '板甲'
        self.buff = 2.335

        self.角色 = '圣职者(女)'

        self.职业 = '圣骑士'

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
