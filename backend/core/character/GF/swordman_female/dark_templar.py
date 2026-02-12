#1645c45aabb008c98406b3a16447040d
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "swordman_female/dark_templar/cn/skillDetail"

# 暗黑斩
# swordman_female/dark_templar/3c5604bdbb0240b8f130f59ab40509c3
# 1645c45aabb008c98406b3a16447040d/3c5604bdbb0240b8f130f59ab40509c3
class Skill0(ActiveSkill):
    """
        借助魔人的力量， 向前方敌人发出强威力的斩击。
    """
    name = "暗黑斩"
    learnLv = 1
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 6
    mp = [20, 250]
    uuid = "3c5604bdbb0240b8f130f59ab40509c3"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1


# 冥思
# swordman_female/dark_templar/d89f26862e348a801b30bb9fd7125db5
# 1645c45aabb008c98406b3a16447040d/d89f26862e348a801b30bb9fd7125db5
class Skill2(PassiveSkill):
    """
        进行战斗期间， 将根据连击数按比例增加物理或魔法暴击率。\n
        增益效果可以重复触发， 但是有触发次数上限。 增益效果重复触发时， 更新现有增益效果的持续时间。
    """
    name = "冥思"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 5
    rangeLv = 3
    uuid = "d89f26862e348a801b30bb9fd7125db5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 触发增益效果所需连击数 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 暴击率增加上限 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 增益效果持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)


# 基础精通
# swordman_female/dark_templar/5a56514f35cf0270ae8d6c65f8fefd78
# 1645c45aabb008c98406b3a16447040d/5a56514f35cf0270ae8d6c65f8fefd78
class Skill4(PassiveSkill):
    """
        增加基本攻击、 前冲攻击、 跳跃攻击、 [浮空击]的攻击力。\n
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
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力变化率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 前冲攻击力变化率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 跳跃攻击力变化率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [{"type":"*skillDamage","data":[i-100 if i>0 else 0 for i in data0],"skills":["影刃"]}]


# 波动斩
# swordman_female/dark_templar/0969cd4054d93da07708108c0cc1c4b5
# 1645c45aabb008c98406b3a16447040d/0969cd4054d93da07708108c0cc1c4b5
class Skill7(ActiveSkill):
    """
        向前方发射一定次数的剑气波动。
    """
    name = "波动斩"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 3
    mp = [17, 150]
    uuid = "0969cd4054d93da07708108c0cc1c4b5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 剑气多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 剑气发射次数 : 2次

# 影刃
# swordman_female/dark_templar/1721e94897e9961d5c98130a13392f17
# 1645c45aabb008c98406b3a16447040d/1721e94897e9961d5c98130a13392f17
class Skill17(PassiveSkill):
    """
        普通或跳跃攻击、 前冲攻击的最后一击时， 可以施放影刃给敌人造成暗属性伤害。
    """
    name = "影刃"
    learnLv = 15
    masterLv = 1
    maxLv = 3
    position = 3
    rangeLv = 2
    uuid = "1721e94897e9961d5c98130a13392f17"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击时， 影刃攻击力增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 前冲攻击时， 影刃攻击力增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 跳跃攻击时， 影刃攻击力增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 暗影之矛
# swordman_female/dark_templar/d296043df164385a14cb973c8c7c4d07
# 1645c45aabb008c98406b3a16447040d/d296043df164385a14cb973c8c7c4d07
class Skill18(ActiveSkill):
    """
        将乌希尔的力量幻化成暗影长矛， 给予敌人暗属性伤害。\n
        可以按左右方向键来控制移动距离。\n
        可以对敌人造成多段攻击的同时击退敌人。
    """
    name = "暗影之矛"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 0
    rangeLv = 2
    cd = 5
    mp = [30, 300]
    uuid = "d296043df164385a14cb973c8c7c4d07"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 多段攻击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 多段攻击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 8
    # [范围信息]
    # 大小 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 乌希尔的诅咒
# swordman_female/dark_templar/7dd85dccf7ae1f65609c36d66e2e1c95
# 1645c45aabb008c98406b3a16447040d/7dd85dccf7ae1f65609c36d66e2e1c95
class Skill19(PassiveSkill):
    """
        进入地下城时， 对怪物施加“乌希尔的诅咒”， 增加自身转职后技能的攻击力。
    """
    name = "乌希尔的诅咒"
    learnLv = 15
    masterLv = 1
    maxLv = 11
    position = 5
    rangeLv = 2
    uuid = "7dd85dccf7ae1f65609c36d66e2e1c95"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 转职后技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"type":"*skillDamage","data":data0}]# noqa: E501

# 暗影遁行
# swordman_female/dark_templar/bc11d28c04e01923a093d65752c55516
# 1645c45aabb008c98406b3a16447040d/bc11d28c04e01923a093d65752c55516
class Skill20(ActiveSkill):
    """
        躲避敌人的攻击， 隐藏到暗影内进行移动。\n
        再次按下技能键或技能持续时间结束后， 可现出人形态。
    """
    name = "暗影遁行"
    learnLv = 20
    masterLv = 1
    maxLv = 11
    position = 2
    rangeLv = 2
    cd = 5
    mp = [40, 330]
    uuid = "bc11d28c04e01923a093d65752c55516"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 可移动时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 可移动距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 暗影缠袭
# swordman_female/dark_templar/faf9cd66281078b51be2ee0b0f6c5530
# 1645c45aabb008c98406b3a16447040d/faf9cd66281078b51be2ee0b0f6c5530
class Skill21(ActiveSkill):
    """
        向前方发射蕴含魔物的暗影， 束缚敌人并使其进入失明状态。\n
        若在暗影持续时间内再次按下技能键、 离开暗影周围或者靠近暗影时， 都可以发动终结攻击。\n
        若暗影上只存在无法控制的敌人， 则立即发动终结攻击。
    """
    name = "暗影缠袭"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 0
    rangeLv = 2
    cd = 7
    mp = [40, 350]
    uuid = "faf9cd66281078b51be2ee0b0f6c5530"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 暗影多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 6
    # 最后一击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 3
    # 暗影多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 暗影束缚持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 失明几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 失明命中率减少量 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 失明视野减少率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 失明持续时间 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [范围信息]
    # 范围 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

# 暗影漩涡
# swordman_female/dark_templar/ca75c965f20a150f99f54155a37400df
# 1645c45aabb008c98406b3a16447040d/ca75c965f20a150f99f54155a37400df
class Skill22(ActiveSkill):
    """
        将乌希尔的力量汇聚到剑上， 然后将剑抛向地面， 造成暗属性伤害。\n
        以剑为中心会生成魔法阵， 魔法阵存在期间对敌人造成多段魔法伤害。\n
        在跳跃或者后跳的过程中， 也能使用技能。\n
        可以通过On/Off功能开启或关闭吸入功能。
    """
    name = "暗影漩涡"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 6
    mp = [15, 330]
    uuid = "ca75c965f20a150f99f54155a37400df"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 灵魂吸收攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 魔法阵持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 魔法阵多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 魔法阵多段攻击间隔 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 魔法阵多段攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 6
    # [范围信息]
    # 魔法阵范围 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 幻影摄取
# swordman_female/dark_templar/0ed3148658fe37b3336ccb718dc0fdb0
# 1645c45aabb008c98406b3a16447040d/0ed3148658fe37b3336ccb718dc0fdb0
class Skill24(ActiveSkill):
    """
        利用幻影抓取前方的敌人后， 持续为敌人带来伤害， 同时吸收敌人的灵能。
    """
    name = "幻影摄取"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 8
    mp = [25, 550]
    uuid = "0ed3148658fe37b3336ccb718dc0fdb0"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 多段攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit0 = 10
    # 多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最高抓取数量 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 灵能吸收的攻击次数 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 攻击范围 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 汲魂之力
# swordman_female/dark_templar/6e33d47e6622ce03b6defdd912140270
# 1645c45aabb008c98406b3a16447040d/6e33d47e6622ce03b6defdd912140270
class Skill25(PassiveSkill):
    """
        借用乌希尔的力量， 增加基本攻击力和技能攻击力。\n
        可以吸收敌人的灵魂并利用灵魂攻击敌人， 或消耗一定数量的灵魂增加特定技能的攻击力。
    """
    name = "汲魂之力"
    learnLv = 25
    masterLv = 20
    maxLv = 30
    position = 2
    rangeLv = 2
    uuid = "6e33d47e6622ce03b6defdd912140270"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 使用转职技能攻击时的灵魂吸收率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 吸收灵魂上限 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [
        {"type":"*skillDamage","data":data0},
        {"type":"*skillDamage","data":[0]+[100]*maxLv,"skills":["释魂飞弹"]},
        {"type":"*power0","data":[0]+[15]*maxLv,"skills":["罚罪之光"]},
        {"type":"*skillDamage","data":[0]+[15]*maxLv,"skills":["天罚之剑"]},
        {"type":"*skillDamage","data":[0]+[10]*maxLv,"skills":["神罚 · 灭世裁决"]},
        ]# noqa: E501

# 暗影禁锢
# swordman_female/dark_templar/51a08fd0c90f0a5276cd552047fac93d
# 1645c45aabb008c98406b3a16447040d/51a08fd0c90f0a5276cd552047fac93d
class Skill26(ActiveSkill):
    """
        将乌希尔的力量汇聚到手中形成球体， 然后向前发射将敌人禁锢的同时， 给予其暗属性伤害并使其进入失明状态。\n
        可以将一定范围内的所有敌人禁锢住， 一段时间后球体会爆炸， 并使敌人受到暗属性伤害。\n
        禁锢无法控制的敌人时， 立即爆炸。
    """
    name = "暗影禁锢"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 12
    mp = [60, 390]
    uuid = "51a08fd0c90f0a5276cd552047fac93d"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 冲击波攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 失明几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 失明命中率减少量 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 失明视野减少率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 失明持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 目标锁定X轴范围 : {value7}px
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 目标锁定Y轴范围 : {value8}px
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 目标锁定Z轴范围 : {value9}px
    data9 = get_data(f'{prefix}/{uuid}', 9)

# 释魂飞弹
# swordman_female/dark_templar/b163d099c8cc27fdb6fd3639c2ee6df9
# 1645c45aabb008c98406b3a16447040d/b163d099c8cc27fdb6fd3639c2ee6df9
class Skill27(ActiveSkill):
    """
        将[汲魂之力]吸收到的灵魂注入敌人体内， 并发射可追踪攻击的能量飞弹， 以攻击带有灵魂印记的敌人， 使其受到暗属性伤害。\n
        能量飞弹皆按照领主、 稀有或精英、 普通怪物的先后顺序进行自动攻击； 若飞弹发射数多于敌人数， 则会重复攻击同一个目标。
    """
    name = "释魂飞弹"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 3
    cd = 5
    mp = [65, 450]
    uuid = "b163d099c8cc27fdb6fd3639c2ee6df9"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 每个飞弹所消耗的灵魂数量 : {value0}个
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 飞弹最低发射数 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 飞弹最高发射数 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 每个灵魂的攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 4
    # 每个敌人所承受的飞弹数上限 : {value4}个
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 锁定距离上限 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 爆炸大小: {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

# 魅影暗魂斩
# swordman_female/dark_templar/28b583c75a49103a1d8aabf799c000a4
# 1645c45aabb008c98406b3a16447040d/28b583c75a49103a1d8aabf799c000a4
class Skill28(ActiveSkill):
    """
        在前方一定距离处召唤魅影， 魅影攻击敌人后将其聚集到主人附近， 主人施放剑气， 给予敌人暗属性攻击。\n
        被魅影攻击的敌人会先被吸附到主人前方， 然后再被剑气的多段攻击所击退。
    """
    name = "魅影暗魂斩"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 11
    mp = [70, 400]
    uuid = "28b583c75a49103a1d8aabf799c000a4"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 魅影攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 剑气持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 剑气攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 4
    # 剑气多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 剑气大小 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 释魂狂怒
# swordman_female/dark_templar/4b2c90ec226fd40e967875aa5eabefb2
# 1645c45aabb008c98406b3a16447040d/4b2c90ec226fd40e967875aa5eabefb2
class Skill29(ActiveSkill):
    """
        生成魔法阵后束缚敌人， 然后发射灵魂， 对魔法阵内的敌人进行攻击。\n
        魔法阵内的敌人会浮在空中进入被抓取状态， 随后暗殿骑士会在拥有的灵魂中消耗一部分灵魂进行攻击。\n
        没有灵魂的时候， 无法使用技能。
    """
    name = "释魂狂怒"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 15
    mp = [100, 900]
    uuid = "4b2c90ec226fd40e967875aa5eabefb2"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 消耗的灵魂个数 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 灵魂恢复数量 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 魔法阵范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [释魂狂怒]\n
        变更为在前方近距离位置生成魔法阵\n
        魔法阵大小 +70%\n
        自动施放[释魂飞弹]， 合算至[释魂狂怒]的伤害中
        """
        ...

    def vp_2(self):
        """
        [释魂狂怒]\n
        施放时不消耗灵魂\n
        施放时间 -30%
        """
        ...

# 魔镜幻影阵
# swordman_female/dark_templar/f0cc2c950f3bdf4103c75fa496bcac34
# 1645c45aabb008c98406b3a16447040d/f0cc2c950f3bdf4103c75fa496bcac34
class Skill30(ActiveSkill):
    """
        在前方生成镜阵限制敌人的移动范围， 并给予其暗属性伤害。\n
        镜阵生成后， 会使周围敌人受到伤害并且行动受限； 直到镜阵生命值为0或者阵内幻影攻击结束后， 敌人才能自由移动。\n
        若角色处在镜阵范围内， 则身上会有减少所受伤害的防护罩。\n
        在决斗场中， 不适用吸附效果及僵直效果， 且无法限制敌人的移动。 而且减慢受到[魔镜幻影阵]效果的暗殿骑士和我军的移动速度。
    """
    name = "魔镜幻影阵"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 0
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [110, 924]
    uuid = "f0cc2c950f3bdf4103c75fa496bcac34"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 镜阵生成时的攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 镜阵生命值 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 幻影的攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 12
    # 幻影多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 防护罩的持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 防护罩的防御次数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 所受伤害减少率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 大小 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [决斗场]
    # 移动速度减少率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

    def vp_1(self):
        """
        [魔镜幻影阵]\n
        防护罩持续时间内适用以下效果\n
         - 移动速度 +15%\n
        防护罩持续时间 +3秒
        """
        ...

    def vp_2(self):
        """
        [魔镜幻影阵]\n
        镜阵攻击次数 -1次\n
         - 总攻击力相同\n
        施放时， 立即在暗殿骑士周围生成镜阵\n
        镜阵大小 +50%
        """
        ...

# 暗影蓄能
# swordman_female/dark_templar/6a1d1f08a6572be420bb3a256c44c015
# 1645c45aabb008c98406b3a16447040d/6a1d1f08a6572be420bb3a256c44c015
class Skill31(ActiveSkill):
    """
        在一定时间内激发自身实力， 增加基本攻击力和技能攻击力。
    """
    name = "暗影蓄能"
    learnLv = 35
    masterLv = 1
    maxLv = 11
    position = 4
    rangeLv = 3
    cd = 5
    uuid = "6a1d1f08a6572be420bb3a256c44c015"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 增益效果持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 暗影囚笼
# swordman_female/dark_templar/147d005ac868e0de52b1f255eea35d62
# 1645c45aabb008c98406b3a16447040d/147d005ac868e0de52b1f255eea35d62
class Skill32(ActiveSkill):
    """
        抛出死亡斗篷将敌人禁锢在黑色球体中， 给予其暗属性攻击伤害。\n
        按下跳跃键， 可以在连击中施放最后一击。\n
        使用技能时， 要是使用释魂飞弹， 则冷却时间会减少。\n
        对无法抓取的敌人不适用控制效果， 无法将其禁锢在黑色球体中。
    """
    name = "暗影囚笼"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [60, 830]
    uuid = "147d005ac868e0de52b1f255eea35d62"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 多段攻击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 多段攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 14
    # 终结一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 失明几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 失明命中率减少量 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 失明视野减少率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 失明持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 释魂飞弹的冷却时间减少量 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7)

    def vp_1(self):
        """
        [暗影囚笼]\n
        斩击多段攻击次数 -9次\n
        斩击多段攻击速度 +20%\n
        最后一击强制控制敌人1.5秒\n
        最后一击强制控制结束后造成额外伤害\n
         - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [暗影囚笼]\n
        每次攻击必定使敌人进入失明状态\n
        每2次斩击恢复1个灵魂\n
        施放过程中所受伤害 -70%
        """
        ...

# 暗影盛宴
# swordman_female/dark_templar/47bd4871f29defc2a0021ee9261d7a5b
# 1645c45aabb008c98406b3a16447040d/47bd4871f29defc2a0021ee9261d7a5b
class Skill33(ActiveSkill):
    """
        高高跃起后， 向地面发射暗属性剑气并引发爆炸攻击周围敌人。\n
        可在跳跃时使用， 爆炸攻击命中时可以额外累积一定量的灵魂。\n
        在决斗场中， 无法在跳跃过程中使用。
    """
    name = "暗影盛宴"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 0
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [120, 2024]
    uuid = "47bd4871f29defc2a0021ee9261d7a5b"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆炸攻击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 15
    # 爆炸攻击时， 额外的灵魂累积数 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 攻击范围 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [暗影盛宴]\n
        用投掷暗影球代替剑气乱舞\n
         - 变更为单次攻击\n
         - 总攻击力相同\n
        可以在地面和空中施放
        """
        ...

    def vp_2(self):
        """
        [暗影盛宴]\n
        施放时进入无敌状态\n
        技能结束时灵魂恢复至最大值
        """
        ...

# 灵魂傀儡
# swordman_female/dark_templar/38612d8f2561edc2eb68d5057a837bfa
# 1645c45aabb008c98406b3a16447040d/38612d8f2561edc2eb68d5057a837bfa
class Skill34(PassiveSkill):
    """
        傀儡提升暗帝的魔法暴击率和暴击伤害， 并且攻击时， 有一定几率黏在敌人身上吸收敌人的灵魂。\n
        黏在敌人身上的傀儡会以一定的间隔吸收敌人的灵魂并传送给暗帝。
    """
    name = "灵魂傀儡"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 0
    rangeLv = 3
    uuid = "38612d8f2561edc2eb68d5057a837bfa"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 附着傀儡的几率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 吸收敌人灵魂的时间间隔 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 同一个敌人再次变成傀儡所需的时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 魔法暴击率增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 暴击伤害增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    associate = [
        {"type":"*skillDamage","data":data5},
    ]

# 末日狂战
# swordman_female/dark_templar/b3659936a9a74c4ed6f7faf07cca1f9e
# 1645c45aabb008c98406b3a16447040d/b3659936a9a74c4ed6f7faf07cca1f9e
class Skill35(ActiveSkill):
    """
        借用冥王乌希尔的权能生成暗属性魔法剑向前刺击， 并将敌人汇聚到黑暗球体内， 同时球体会召唤出魅影一起向敌人施展暗属性攻击。\n
        被刺中的敌人会受到伤害， 与球体召唤的魅影面对面施放魅影连击后， 吸收魅影之力攻击敌人。 随后， 黑暗球体会爆炸。结束施放后， 在一定时间内使用[释魂飞弹]将不消耗灵魂。
    """
    name = "末日狂战"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 0
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [900, 7559]
    uuid = "b3659936a9a74c4ed6f7faf07cca1f9e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 刺击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 魅影连击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 5
    # 最终一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 5
    # 魅影连击多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 最终一击多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 爆炸攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # [释魂飞弹]无消耗状态的持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)

# 魔影轰杀
# swordman_female/dark_templar/a2d943797daca862a6f321aca6ac9bfa
# 1645c45aabb008c98406b3a16447040d/a2d943797daca862a6f321aca6ac9bfa
class Skill36(ActiveSkill):
    """
        将蕴含乌希尔气息的剑刺向地面， 使敌人受到暗属性伤害。\n
        抓住目标后追踪敌人并爆炸， 爆炸时会对周围的敌人造成伤害。\n
        可以多次更换目标进行追踪并爆炸， 若没有目标则向前方移动并爆炸。
    """
    name = "魔影轰杀"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [600, 1840]
    uuid = "a2d943797daca862a6f321aca6ac9bfa"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆炸次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 4
    # [范围信息]
    # 攻击距离 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 爆炸范围 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [魔影轰杀]\n
        魔影由追踪敌人变更为环绕在自身周围\n
        再次按技能键时， 发射全部魔影\n
         - 锁定射程增加
        """
        ...

    def vp_2(self):
        """
        [魔影轰杀]\n
        从空中降下魔影\n
         - 向周围600px内最强敌人降下\n
        删除施放动作， 可以在其他动作中施放
        """
        ...

# 黑暗献祭
# swordman_female/dark_templar/c7bf7ccab413009640e65ca6f2f0263a
# 1645c45aabb008c98406b3a16447040d/c7bf7ccab413009640e65ca6f2f0263a
class Skill37(ActiveSkill):
    """
        在角色周围生成暗属性魔法阵， 使敌人进入减速状态， 并且在造成多段伤害后引爆。
    """
    name = "黑暗献祭"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [1200, 2520]
    uuid = "c7bf7ccab413009640e65ca6f2f0263a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 减速几率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击、 移动速度减少 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击、 移动速度减少的持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 初始攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 多段攻击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 10
    # 爆炸攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # 多段攻击次数 : {value6}次
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 魔法阵范围 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    def vp_1(self):
        """
        [黑暗献祭]\n
        在前方召唤幻影， 替代自身生成魔法阵\n
        增加以幻影为中心吸附敌人的功能\n
        幻影生成魔法阵时， 可以移动
        """
        ...

    def vp_2(self):
        """
        [黑暗献祭]\n
        在前方生成吸收[释魂飞弹]的黑暗之花\n
        - 强制控制领域内的敌人\n
        再次按技能键或持续时间结束时， 领域爆炸\n
        - 总攻击力相同\n
        - 合算累积的飞弹伤害\n
        发动[幽冥圣域]时， 施放[释魂飞弹]， 不会消耗灵魂
        """
        ...

# 罚罪之光
# swordman_female/dark_templar/e0a072e8cef2d77893aad5f68aeed56a
# 1645c45aabb008c98406b3a16447040d/e0a072e8cef2d77893aad5f68aeed56a
class Skill38(ActiveSkill):
    """
        死亡之光， 裁决之力。\n
        在剑尖上聚集裁决的力量， 向前方发射死亡之光。\n
        施放技能时若拥有灵魂， 则根据蓄气时间的长短消耗一定数量的灵魂， 消耗的灵魂数量越多， 攻击力越高。
    """
    name = "罚罪之光"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "e0a072e8cef2d77893aad5f68aeed56a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # [罚罪之光]攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 最小蓄气时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 消耗灵魂数量上限 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 吸收灵魂时间间隔 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 每消耗1个灵魂攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 吸收灵魂后延迟时间上限 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 范围 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [罚罪之光]\n
        额外发射4个小型能量炮\n
        不填充灵魂， 立即发射能量炮\n
         - 立即最多消耗10个灵魂
        """
        ...

    def vp_2(self):
        """
        [罚罪之光]\n
        灵魂数量上限 +10个\n
        施放时额外消耗10个灵魂\n
         - 攻击速度 +10%， 效果持续10秒\n
        每拥有1个灵魂， 暗殿骑士的攻击速度 +0.4%
        """
        ...

# 薄暮
# swordman_female/dark_templar/2a0a39184de92acf1c1375e00b77404c
# 1645c45aabb008c98406b3a16447040d/2a0a39184de92acf1c1375e00b77404c
class Skill39(PassiveSkill):
    """
        战斗前， 通过祈祷变更部分技能功能， 强化部分消耗灵魂技能的附加效果。\n
        [攻击力增加]\n
        基本攻击、 [暗影之矛]、 [暗影缠袭]、 [幻影摄取]、 [魅影暗魂斩]、 [暗影禁锢]、 [暗影漩涡]、 [魔镜幻影阵]、 [暗影囚笼]、 [末日狂战]、 [魔影轰杀]、 [黑暗献祭]、 [暗影盛宴]、 [罚罪之光]、 [天罚之剑]、 [神罚 · 灭世裁决]、 [暗影绽放 : 死亡荆棘]、 [冥王降临 : 净土救赎]\n
        [效果变更]\n
        [魅影暗魂斩] : 取消发射剑气前的魅影， 增加技能攻击力， 增加的攻击力相当于魅影的攻击力。\n
        [消耗灵魂的附加效果强化]\n
    [释魂狂怒]、 [罚罪之光]、 [天罚之剑]
    """
    name = "薄暮"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 1
    rangeLv = 3
    uuid = "2a0a39184de92acf1c1375e00b77404c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # [释魂飞弹、 释魂狂怒除外]
    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 消耗灵魂时， 附加效果增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [
        {"type": "*skillDamage", "data": data0,"exceptSkills":['释魂飞弹', '释魂狂怒']},
    ]

# 天罚之剑
# swordman_female/dark_templar/c5a2956d8ed3af1746ed2f76ca971a09
# 1645c45aabb008c98406b3a16447040d/c5a2956d8ed3af1746ed2f76ca971a09
class Skill40(ActiveSkill):
    """
        代表神圣战争的天罚之剑。\n
        利用技能键和方向键， 可将天罚之剑召唤到指定的位置。\n
        剑落下的地方将发生剧烈的爆炸。\n
        施放技能时若拥有灵魂， 则每消耗1个灵魂可以增加一定攻击力。 消耗的灵魂数量越多， 攻击力越高。
    """
    name = "天罚之剑"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [580, 4500]
    uuid = "c5a2956d8ed3af1746ed2f76ca971a09"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 剑爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 剑冲击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 该技能可消耗的灵魂数量上限 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 每消耗1个灵魂时， 攻击力增加量 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 大小 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [天罚之剑]\n
        向一定范围内最强敌人落剑\n
         - 仅在范围内存在敌人时激活技能\n
        不消耗灵魂， 固定适用最大攻击力
        """
        ...

    def vp_2(self):
        """
        [天罚之剑]\n
        挥剑向前方发射剑气\n
         - 总攻击力相同\n
        可以在地面和空中施放\n
        部分技能可以相互强制中断施放\n
         - 目标技能 : [暗影囚笼]、 [暗影盛宴]、 [暗影绽放 : 死亡荆棘]
        """
        ...

# 神罚 · 灭世裁决
# swordman_female/dark_templar/0fbb8de70002ad34f046c94c2cb3e863
# 1645c45aabb008c98406b3a16447040d/0fbb8de70002ad34f046c94c2cb3e863
class Skill41(ActiveSkill):
    """
        裁决异徒的坚定信念。\n
        在前方生成魔法阵束缚敌人并进行攻击。\n
        施放技能时若拥有灵魂， 则每消耗1个灵魂可以增加一定攻击力。 消耗的灵魂数量越多， 攻击力越高。\n
        连续按技能键， 可以加快攻击速度。
    """
    name = "神罚 · 灭世裁决"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "0fbb8de70002ad34f046c94c2cb3e863"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 魔法阵范围 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 乱舞攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 7
    # 最终一击爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 乱舞多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 灵魂消耗量上限 : {value4}个
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 每消耗1个灵魂时， 攻击力增加量 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 暗影绽放 : 死亡荆棘
# swordman_female/dark_templar/e4c354a89c337310aeb7041d5e742828
# 1645c45aabb008c98406b3a16447040d/e4c354a89c337310aeb7041d5e742828
class Skill42(ActiveSkill):
    """
        使用影刃创造死亡之荆棘并向前方刺击， 然后撕裂敌人的灵魂。\n
        攻击命中时， 从敌人身上吸收一部分撕裂的灵魂。
    """
    name = "暗影绽放 : 死亡荆棘"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [773, 6000]
    uuid = "e4c354a89c337310aeb7041d5e742828"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 灵魂刺击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 爆炸攻击命中时， 额外吸收灵魂的数量 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 以身载灵
# swordman_female/dark_templar/c27418ae613c647527200a7ca17d97fd
# 1645c45aabb008c98406b3a16447040d/c27418ae613c647527200a7ca17d97fd
class Skill43(PassiveSkill):
    """
        将自身的灵魂作为容器， 迎接死神， 以践行乌希尔的教导。\n
        增加基本攻击力和技能攻击力 ([暗影漩涡]、 [魅影暗魂斩]除外)， 部分技能赋予特殊效果。\n
    [汲魂之力] - 进入地下城时， 初始灵魂数量为15个。\n
    [暗影漩涡] - 魔法剑的持续时间结束时， 产生爆炸伤害。\n
    [魅影暗魂斩] - 在前方召唤幻影一起发射剑气。
    """
    name = "以身载灵"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "c27418ae613c647527200a7ca17d97fd"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和转职技能攻击力增加率 ([暗影漩涡]、[魅影暗魂斩]除外) : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [汲魂之力]灵魂数量增加量 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [暗影漩涡]魔法剑爆炸攻击力 : 总攻击力的{value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [魅影暗魂斩]幻影的剑气攻击力 : 剑气攻击力的{value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    associate = [
        {"type":"*skillDamage","data":data0},
        {"type":"+hit0","data":[0]+[-1]*maxLv,"skills":["魅影暗魂斩"],"ratio":1}
    ]

# 冥王降临 : 净土救赎
# swordman_female/dark_templar/0e3da11226dd30c2aaef52e36eff7f3f
# 1645c45aabb008c98406b3a16447040d/0e3da11226dd30c2aaef52e36eff7f3f
class Skill44(ActiveSkill):
    """
        使用影刃创造乌希尔的领域后囚禁敌人。 乌希尔降临后， 利用神之权能吸收领域内敌人的灵魂， 然后将其引爆。\n
    [三次觉醒技能]\n
        施放三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "冥王降临 : 净土救赎"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4027, 8054]
    uuid = "0e3da11226dd30c2aaef52e36eff7f3f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 吸收灵魂时多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 10
    # 灵魂爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 吸收灵魂时多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'dark_templar'
        self.nameCN = '极诣·暗殿骑士'
        self.role = 'swordman_female'
        self.角色 = '鬼剑士(女)'
        self.职业 = '暗殿骑士'
        self.jobId = '1645c45aabb008c98406b3a16447040d'
        self.jobGrowId = '618326026de1a1f1cfba5dbd0b8396e7'

        self.武器选项 = ['巨剑', '钝器', '太刀', '短剑']
        self.输出类型选项 = ['魔法百分比']
        self.输出类型 = '魔法百分比'
        self.防具精通属性 = ['智力']
        self.防具类型 = '板甲'
        self.buff = 1.72

        super().__init__(equVersion, __name__)
