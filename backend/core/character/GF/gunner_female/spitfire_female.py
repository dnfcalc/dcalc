#944b9aab492c15a8474f96947ceeb9e4
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "gunner_female/spitfire_female/cn/skillDetail"


# 跃翔
# gunner_female/spitfire_female/1fea5a626f15230237946a11a9d11582
# 944b9aab492c15a8474f96947ceeb9e4/1fea5a626f15230237946a11a9d11582
class Skill16(ActiveSkill):
    """
        增加自身20%的跳跃力， 效果持续一定时间。\n
        效果持续期间内， 再次按技能键可以结束。
    """
    name = "跃翔"
    learnLv = 10
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 3
    cd = 5
    mp = [13, 13]
    uuid = "1fea5a626f15230237946a11a9d11582"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)


# 特性弹
# gunner_female/spitfire_female/9dda3f4a849dba1a288dd65e116860f2
# 944b9aab492c15a8474f96947ceeb9e4/9dda3f4a849dba1a288dd65e116860f2
class Skill18(ActiveSkill):
    """
        可以在[超负荷装填]状态下使用， 使[超负荷装填]造成的属性效果以特性的形式体现， 使命中对象进入异常状态。\n
    [火属性] : 灼伤\n
    [冰属性] : 冰冻\n
    [光属性] : 感电\n
    [无属性] : 眩晕\n
        无法和[贯穿弹]、 [爆裂弹]同时使用。\n
        该技能即时受装备的影响。\n
        在决斗场中， 适用单独的持续时间； 灼伤异常状态触发几率变更为100%。
    """
    name = "特性弹"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 4
    rangeLv = 3
    cd = 5
    mp = [126, 975]
    uuid = "9dda3f4a849dba1a288dd65e116860f2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 异常状态发动率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 灼伤持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 灼伤攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 冰冻持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 感电持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 感电攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 眩晕持续时间 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 增益效果持续时间 : {value8}秒
    data8 = get_data(f'{prefix}/{uuid}', 8)


# 单兵推进器
# gunner_female/spitfire_female/4224f9b0b8c7c903e9a1e0f9d9f6d04d
# 944b9aab492c15a8474f96947ceeb9e4/4224f9b0b8c7c903e9a1e0f9d9f6d04d
class Skill21(PassiveSkill):
    """
        弹药专家在跳跃状态下， 可利用装备在腰部的单兵推进器控制空中动作。 可在空中自由移动或使用技能， 且增加有子弹效果的射击攻击力和射击技能攻击力。\n
    - [射击技能] -\n
    [交叉射击]、 [聚合弹]、 [凝固汽油弹]、 [超真空弹 : 切利]。\n
        可以强制中断基本攻击并跳跃。 空中射击技能冷却时间变更为5秒， 持续时间无限制并且变更为立即施放技能。\n
        学习后， 增加[空中射击]等级。\n
    - [可在空中使用的动作] -\n
    - 垂直上升 : 在跳跃状态下垂直向上移动。\n
    (跳跃状态下) + C\n
    - 水平移动 : 在跳跃状态下左/右水平移动。\n
    (跳跃状态下) ←或→ + C\n
    - 迅速降落 : 在跳跃状态下快速落地。\n
    (跳跃状态下) + 空格键\n
    - 姿态恢复 : 在跳跃状态下被敌人攻击时， 可从被击状态恢复到正常的跳跃状态。\n
    (被攻击中) + C\n
    - 施放技能 : 可以在空中施放技能。
    """
    name = "单兵推进器"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 8
    rangeLv = 1
    uuid = "4224f9b0b8c7c903e9a1e0f9d9f6d04d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 子弹效果攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 射击技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 每次跳跃时使用次数上限 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 跳跃状态下位移动作冷却时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 高速落地消耗使用次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 姿态恢复消耗使用次数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 后跳使用时， 消耗使用次数 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)

    associate = [
        {'data': data0, 'skills': ['交叉射击', '聚合弹', '凝固汽油弹', '超真空弹：切利']},
        {'data': data1, 'skills': ['爆裂弹']}
    ]

# 空中射击
# gunner_female/spitfire_female/bb34e8854a93fd250347a1c64119f7ab
# 944b9aab492c15a8474f96947ceeb9e4/bb34e8854a93fd250347a1c64119f7ab
class Skill22(ActiveSkill):
    """
        增加跳跃攻击的空中停留时间以及跳跃射击的攻击力和射击次数上限， 效果持续一定时间。
    """
    name = "空中射击"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 8
    rangeLv = 3
    cd = 40
    mp = [40, 168]
    uuid = "bb34e8854a93fd250347a1c64119f7ab"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 空中射击攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 增加发射子弹数上限 : 左轮枪{value2}发、 自动手枪{value3}发、 步枪{value4}发、 手炮{value5}发、 手弩{value6}发
    data2 = get_data(f'{prefix}/{uuid}', 2)
    data3 = get_data(f'{prefix}/{uuid}', 3)
    data4 = get_data(f'{prefix}/{uuid}', 4)
    data5 = get_data(f'{prefix}/{uuid}', 5)
    data6 = get_data(f'{prefix}/{uuid}', 6)

# G-14手雷
# gunner_female/spitfire_female/de3fea2d65c597f4d55c70a02b97fc79
# 944b9aab492c15a8474f96947ceeb9e4/de3fea2d65c597f4d55c70a02b97fc79
class Skill23(ActiveSkill):
    """
        向前方投掷G-14手雷， 使一定范围内的所有敌人受到伤害。\n
        G-14手雷有最大填装数和填装冷却时间， 按上、 下方向键后施放技能时， 可以调整投掷位置。 转职成为弹药专家时， 可以强制中断基本攻击动作， 投掷G-14手雷。
    """
    name = "G-14手雷"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 2
    mp = [20, 160]
    uuid = "de3fea2d65c597f4d55c70a02b97fc79"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 最大填装数 : {value0}发
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 地面投掷时的冷却时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 空中投掷时的冷却时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 爆炸范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)

    mode = ['普通','强化']

    def setMode(self, mode):
        if mode == '普通':
            return
        if mode == '强化':
            self.skillRation *= 1.2
            return

# 超负荷装填
# gunner_female/spitfire_female/c47b66efd27845ef14954928ea2f95c8
# 944b9aab492c15a8474f96947ceeb9e4/c47b66efd27845ef14954928ea2f95c8
class Skill24(ActiveSkill):
    """
        在子弹中填装特殊弹药， 增加基本攻击力和技能攻击力。
    """
    name = "超负荷装填"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 3
    rangeLv = 3
    cd = 5
    uuid = "c47b66efd27845ef14954928ea2f95c8"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

# 弹药改良
# gunner_female/spitfire_female/3829c15bf5f520c13998a3479ba0ce7b
# 944b9aab492c15a8474f96947ceeb9e4/3829c15bf5f520c13998a3479ba0ce7b
class Skill25(PassiveSkill):
    """
        学习技能后， 增加自身和队伍中其他神枪手的射击穿刺力和敌人的僵直时间。 转职为弹药专家后， 增加暴击率、 暴击伤害， 施放[超负荷装填]的状态下， 增加基本攻击力和技能攻击力。\n
        如在[超负荷装填]中选择无属性， 增加基本攻击的弹速。
    """
    name = "弹药改良"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 1
    rangeLv = 3
    uuid = "3829c15bf5f520c13998a3479ba0ce7b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 敌人僵直时间增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 穿刺率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 选择无属性时的基本攻击弹速增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 基本攻击力和技能攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 暴击攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 暴击率增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    associate = [
        {'data': data3, 'type': '*skillDamage'},
        {'data': data4, 'type': '*skillDamage'}
    ]

# 手雷精通
# gunner_female/spitfire_female/0113c8b1306ca76d208f83f2d093dd62
# 944b9aab492c15a8474f96947ceeb9e4/0113c8b1306ca76d208f83f2d093dd62
class Skill26(PassiveSkill):
    """
        增加[G-14手雷]、 [G-35L感电手雷]、 [G-18C冰冻手雷]的攻击力。
    """
    name = "手雷精通"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 3
    uuid = "0113c8b1306ca76d208f83f2d093dd62"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

    associate = [
        {'type': '*skillDamage', 'data': data0, 'skills': ['G-14手雷','G-35L感电手雷','G-18C冰冻手雷']},
    ]


# 兵器研究
# gunner_female/spitfire_female/bae12a6dc7d22a5cf149673e88ddda28
# 944b9aab492c15a8474f96947ceeb9e4/bae12a6dc7d22a5cf149673e88ddda28
class Skill28(PassiveSkill):
    """
        学习后， 增加物理、 魔法、 独立攻击力， 减少转职后技能的冷却时间。 装备步枪、 手弩时， 增加攻击速度、 技能施放速度和填装速度； 增加集弹率和空中射击的后坐力。
    """
    name = "兵器研究"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 0
    rangeLv = 3
    uuid = "bae12a6dc7d22a5cf149673e88ddda28"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 物理、 魔法攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 独立攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 转职后技能冷却时间减少率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 攻击速度增加 : {value0}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 施放速度增加 : {value1}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # (冷却时间减少效果不适用于一次、 二次、 三次觉醒技能)
    # 填装速度增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    associate = [
        {'data': data0, 'type': '$*PAtkI'},
        {'data': data2, 'type': '*cdReduce', 'exceptSkills': ['EMP磁暴','决战之日','终解·制空霸权']}
        ]

# M18阔剑地雷
# gunner_female/spitfire_female/2ff50c35efcf0f287c4c418c8454da48
# 944b9aab492c15a8474f96947ceeb9e4/2ff50c35efcf0f287c4c418c8454da48
class Skill29(ActiveSkill):
    """
        设置M18阔剑地雷。\n
        阔剑地雷能感知范围内的敌人， 然后爆炸使敌人受到伤害。\n
        爆炸能使敌人进入眩晕状态， 并将其击退。\n
        在决斗场中无法手动引爆阔剑地雷。 经过一定时间后， 阔剑地雷自动爆炸， 爆炸前追加僵直时间。
    """
    name = "M18阔剑地雷"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cd = 6
    mp = [70, 588]
    uuid = "2ff50c35efcf0f287c4c418c8454da48"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 多段攻击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 多段攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 3
    # 眩晕几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 眩晕持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 阔剑地雷持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 索敌及爆炸范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 快速拔枪
# gunner_female/spitfire_female/45442bbbe33540b4deeec29437dae70c
# 944b9aab492c15a8474f96947ceeb9e4/45442bbbe33540b4deeec29437dae70c
class Skill30(PassiveSkill):
    """
        快速拔枪攻击敌人， 发动后可以增加攻击速度和普通射击的攻击力。 转职为漫游枪手后增加精通等级。
    """
    name = "快速拔枪"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 9
    rangeLv = 3
    uuid = "45442bbbe33540b4deeec29437dae70c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 拔枪速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 普通射击的攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 交叉射击
# gunner_female/spitfire_female/78be08a3f8c834d3b06fa20c6a08c5a5
# 944b9aab492c15a8474f96947ceeb9e4/78be08a3f8c834d3b06fa20c6a08c5a5
class Skill31(ActiveSkill):
    """
        双手交叉向前方进行大范围射击， 使敌人受到多段攻击伤害。\n
        可以在[超负荷装填]状态下使用， 射击属性为在[超负荷装填]中选择的属性。
    """
    name = "交叉射击"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 8
    mp = [70, 588]
    uuid = "78be08a3f8c834d3b06fa20c6a08c5a5"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 多段攻击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 3
    # 对象僵直时间比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 射击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# G-35L感电手雷
# gunner_female/spitfire_female/c61f5a010370101402b05b21916c2071
# 944b9aab492c15a8474f96947ceeb9e4/c61f5a010370101402b05b21916c2071
class Skill32(ActiveSkill):
    """
        向前方投掷G-35L感电手雷， 使一定范围内的所有敌人受到伤害， 并使敌人进入感电状态。\n
        G-35L感电手雷有最大填装数和填装冷却时间， 按上、 下方向键后施放技能时， 可以调整投掷位置。\n
        在决斗场中， 不适用感电效果。 
    """
    name = "G-35L感电手雷"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 3
    mp = [40, 350]
    uuid = "c61f5a010370101402b05b21916c2071"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 最大填装数 : {value0}发
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 感电攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 感电持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 地面投掷时的冷却时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 空中投掷时的冷却时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 爆炸范围 : {value6}px
    data6 = get_data(f'{prefix}/{uuid}', 6)

    mode = ['普通','强化']

    def setMode(self, mode):
        if mode == '普通':
            return
        if mode == '强化':
            self.skillRation *= 1.2
            return
# 爆裂弹
# gunner_female/spitfire_female/3c5604bdbb0240b8f130f59ab40509c3
# 944b9aab492c15a8474f96947ceeb9e4/3c5604bdbb0240b8f130f59ab40509c3
class Skill33(ActiveSkill):
    """
        在弹头中插入爆炸型弹芯， 基本射击第一发子弹射出后爆炸。\n
        可以在[超负荷装填]状态下使用， 射击属性为[超负荷装填]中选择的属性， 无法与[特性弹]、 [贯穿弹]同时施放。\n
        该技能即时受装备的影响。\n
        在决斗场中适用单独的持续时间。
    """
    name = "爆裂弹"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 4
    rangeLv = 3
    cd = 5
    mp = [357, 2765]
    uuid = "3c5604bdbb0240b8f130f59ab40509c3"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 爆炸攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 子弹增益效果持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]

    def getSkillCD(self,mode=None):
        if self.char.charEquipInfo['武器'].equInfo is None:
            return 0.14
        if self.char.charEquipInfo['武器'].equInfo.itemDetailType == '手弩':
            return 0.115
        return 0.14

# 贯穿弹
# gunner_female/spitfire_female/d0cdaca82892e54097f22a1f60817048
# 944b9aab492c15a8474f96947ceeb9e4/d0cdaca82892e54097f22a1f60817048
class Skill34(ActiveSkill):
    """
        给弹头套上穿透力极强的器械装置， 提升基本射击的攻击力、 穿刺力、 射程和子弹速度。\n
        可以在[超负荷装填]状态下使用， 射击属性为[超负荷装填]中选择的属性， 无法与[特性弹]、 [爆裂弹]同时施放。\n
        该技能即时受装备的影响。\n
        在决斗场中适用单独的持续时间。
    """
    name = "贯穿弹"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 2
    rangeLv = 3
    cd = 5
    mp = [357, 2765]
    uuid = "d0cdaca82892e54097f22a1f60817048"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 贯穿力增加值 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 射程增加值 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 子弹速度增加值 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 子弹增益效果持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def getSkillCD(self,mode=None):
        if self.char.charEquipInfo['武器'].equInfo is None:
            return 0.14
        if self.char.charEquipInfo['武器'].equInfo.itemDetailType == '手弩':
            return 0.115
        return 0.14

# G-18C冰冻手雷
# gunner_female/spitfire_female/202edb928046f4fa6dedf6337377efd5
# 944b9aab492c15a8474f96947ceeb9e4/202edb928046f4fa6dedf6337377efd5
class Skill35(ActiveSkill):
    """
        向前方投掷G-18C冰冻手雷， 使一定范围内的所有敌人受到伤害， 并使敌人进入冰冻状态。\n
        G-18C冰冻手雷有最大填装数和填装冷却时间， 按上、 下方向键后施放技能时， 可以调整投掷位置。
    """
    name = "G-18C冰冻手雷"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 4
    mp = [70, 560]
    uuid = "202edb928046f4fa6dedf6337377efd5"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 最大填装数 : {value0}发
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 冰冻几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 冰冻持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 地面投掷时的冷却时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 空中投掷时的冷却时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 爆炸范围 : {value6}px
    data6 = get_data(f'{prefix}/{uuid}', 6)

    mode = ['普通','强化']

    def setMode(self, mode):
        if mode == '普通':
            return
        if mode == '强化':
            self.skillRation *= 1.2
            return

# C4飞弹
# gunner_female/spitfire_female/a2d943797daca862a6f321aca6ac9bfa
# 944b9aab492c15a8474f96947ceeb9e4/a2d943797daca862a6f321aca6ac9bfa
class Skill36(ActiveSkill):
    """
        向前方投掷搭载爆炸物C4的飞弹。\n
        飞盘在飞行轨迹上的敌人之间反弹， 并在每个被击中的敌人身上安装C4， 使其进入减速状态。\n
        C4安装完成后， 持续时间结束或再次按技能键， 则C4爆炸。\n
        在决斗场中， 即使经过一定时间C4也不会自动爆炸。
    """
    name = "C4飞弹"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cd = 20
    mp = [150, 1232]
    uuid = "a2d943797daca862a6f321aca6ac9bfa"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # C4持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # C4可安装个数上限 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 减速几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 攻击速度减少率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 移动速度减少率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [C4飞弹]\n
        C4安装后立即爆炸\n
        投掷时， 飞弹自动追踪第一个目标\n
         - Y轴追踪范围 : 200px
        """
        ...

    def vp_2(self):
        """
        [C4飞弹]\n
        投掷C4时， 不消耗单兵推进器使用次数\n
        空中投掷C4时， 恢复1次单兵推进器使用次数\n
        空中额外输入成功引爆时， 恢复1次单兵推进器使用次数
        """
        ...

# 聚合弹
# gunner_female/spitfire_female/3fb8395ae3b81bd608e0c4223a8eb534
# 944b9aab492c15a8474f96947ceeb9e4/3fb8395ae3b81bd608e0c4223a8eb534
class Skill37(ActiveSkill):
    """
        对前方进行小范围集中射击， 使敌人受到伤害。\n
        可以在[超负荷装填]状态下使用， 射击属性为[超负荷装填]中选择的属性。
    """
    name = "聚合弹"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 18
    mp = [150, 1232]
    uuid = "3fb8395ae3b81bd608e0c4223a8eb534"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1

    def vp_1(self):
        """
        [聚合弹]\n
        空中施放时，向正下方地面发射爆炸的火属性特殊弹药\n
         - 攻击大范围敌人\n
         - 被击中的敌人会被推向爆炸的外围
        """
        ...

    def vp_2(self):
        """
        [聚合弹]\n
        空中施放时， 不消耗单兵推进器使用次数\n
        投放光学伪装并急速俯冲向地面， 随后在地面进行射击\n
         - 在落向地面的过程及落下后进入无敌状态
        """
        ...

# 地狱烈炎
# gunner_female/spitfire_female/1803b6a67047cafb9e289b4f33cc507b
# 944b9aab492c15a8474f96947ceeb9e4/1803b6a67047cafb9e289b4f33cc507b
class Skill38(ActiveSkill):
    """
        向地面发射凝固汽油弹， 引发爆炸， 生成属性地带， 对敌人造成多段攻击伤害。\n
        可以在[超负荷装填]状态下使用， 爆炸和地带属性为[超负荷装填]中选择的属性。\n
        在决斗场中， 不发动霸体护甲。
    """
    name = "凝固汽油弹"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [200, 1812]
    uuid = "1803b6a67047cafb9e289b4f33cc507b"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆炸攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 属性地带持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 属性地带多段攻击间隔 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 属性地带攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 15
    # [范围信息]
    # 爆炸范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [凝固汽油弹]\n
        删除地面攻击\n
        地面攻击力合算至爆炸攻击力\n
        攻击范围 +30%
        """
        ...

    def vp_2(self):
        """
        [凝固汽油弹]\n
        发射子弹生成巨大的火属性地带\n
         - 删除爆炸攻击\n
         - 爆炸攻击力合算至地面攻击力\n
         - 地面攻击力 +50%\n
         - 地面攻击次数 -5次\n
         - 地面攻击持续时间 -1秒\n
         - 攻击范围大幅增加
        """
        ...

# 镭射狙击
# gunner_female/spitfire_female/845e0ce3235e19f60cc82a082d072cba
# 944b9aab492c15a8474f96947ceeb9e4/845e0ce3235e19f60cc82a082d072cba
class Skill39(ActiveSkill):
    """
        投掷激光信号弹， 锁定追踪范围内的敌人， 诱导支援攻击。\n
        支援攻击将对被锁定对象发动一定次数的攻击， 而且可使其进入眩晕状态。\n
        在决斗场中施放时， 霸体不生效， 而且减少探索范围、 无法使敌人眩晕。
    """
    name = "镭射狙击"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [400, 3360]
    uuid = "845e0ce3235e19f60cc82a082d072cba"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0} X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 眩晕几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 眩晕持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 狙击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [镭射狙击]\n
        用支援炮击替代支援攻击\n
         - 攻击范围 +10%\n
        支援炮击过程中从空中补给强袭装甲\n
         - 获得强袭装甲时， 进入无敌状态， 效果持续2秒
        """
        ...

    def vp_2(self):
        """
        [镭射狙击]\n
        施放技能时， 进入自动瞄准状态， 效果持续10秒\n
         - 可以在所有动作过程中施放\n
         - 向被施放者的技能攻击命中的敌人进行狙击\n
         - 每个技能可发动1次\n
         - 多个敌人同时被命中时， 攻击最强敌人\n
         - 最多发动5次， 每次射击之间的冷却时间为0.5秒
        """
        ...

# 弹药强化
# gunner_female/spitfire_female/b89c9ab317bc0a443f6497b7cca2f6a8
# 944b9aab492c15a8474f96947ceeb9e4/b89c9ab317bc0a443f6497b7cca2f6a8
class Skill40(PassiveSkill):
    """
        强化弹药， 自身所有攻击都能使敌人进入过电流状态。\n
        过电流状态下的敌人受到伤害时， 会额外受到所受伤害一定比例的伤害。
    """
    name = "弹药强化"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 3
    uuid = "b89c9ab317bc0a443f6497b7cca2f6a8"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 额外伤害比率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 过电流持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{'type': '*skillDamage', 'data': data0}]

# EMP磁暴
# gunner_female/spitfire_female/2c9d9a36c8401bddff6cdb80fab8dc24
# 944b9aab492c15a8474f96947ceeb9e4/2c9d9a36c8401bddff6cdb80fab8dc24
class Skill41(ActiveSkill):
    """
        在前方设置EMP机动装置。 机动装置落下时， 形成冲击波和电磁场， 使敌人受到伤害并强控敌人， 发动多段攻击和电磁波攻击后爆炸。
    """
    name = "EMP磁暴"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [880, 7392]
    uuid = "2c9d9a36c8401bddff6cdb80fab8dc24"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 机动装置落下攻击 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 电磁场攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 电磁波多段攻击力 : {value2} X {value3}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 20
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 机动装置爆炸攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1

# G-61重力手雷
# gunner_female/spitfire_female/e0daa922b19cdc35de879e938361464e
# 944b9aab492c15a8474f96947ceeb9e4/e0daa922b19cdc35de879e938361464e
class Skill42(ActiveSkill):
    """
        向前方投掷重力手雷， 将范围内的敌人聚集到一处后爆炸， 对敌人造成伤害。
    """
    name = "G-61重力手雷"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 2
    cube = 2
    cd = 20
    mp = [400, 1120]
    uuid = "e0daa922b19cdc35de879e938361464e"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 重力场持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 重力场多段攻击间隔 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 重力场多段攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 29
    # 重力场爆炸攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 重力场范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 爆炸范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [G-61重力手雷]\n
        重力场持续时间 -50%\n
        重力场大小 +30%\n
        吸附力 +150%
        """
        ...

    def vp_2(self):
        """
        [G-61重力手雷]\n
        删除多段攻击力\n
        多段攻击力合算至终结攻击力\n
        重力场持续时间 +100%\n
        可通过额外输入立即爆炸
        """
        ...

# 超真空弹 : 切利
# gunner_female/spitfire_female/1bf9711f3f15865e38d7dce51c6b5a8c
# 944b9aab492c15a8474f96947ceeb9e4/1bf9711f3f15865e38d7dce51c6b5a8c
class Skill43(ActiveSkill):
    """
        发射超真空弹， 在命中的敌人脚下生成真空洞。 真空洞吸附周围敌人并持续造成伤害， 此时按下技能键或持续时间结束后， 瞬间吸收周围热量并爆炸造成伤害。\n
        真空洞附近弹药专家投掷的G-14手雷、 G-35L感电手雷、 G-18C冰冻手雷将移动到真空洞中心， 并产生爆炸。\n
        若超真空弹未命中， 则在地面放置真空洞； 若敌人踩中真空洞， 则附着在敌人脚下。
    """
    name = "超真空弹 : 切利"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 3
    cd = 30
    mp = [800, 1680]
    uuid = "1bf9711f3f15865e38d7dce51c6b5a8c"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 真空攻击力 : {value0} X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 20
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 真空热量吸收攻击力 : {value2} X {value3}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 5
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 真空爆炸攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # [范围信息]
    # 真空洞范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [超真空弹 : 切利]\n
        手雷吸收功能强化\n
         - 手雷靠近真空洞时被吸收\n
         - 被吸收的手雷在真空洞爆炸时一起爆炸\n
        真空洞和爆炸范围 +40%
        """
        ...

    def vp_2(self):
        """
        [超真空弹 : 切利]\n
        接触地面时立即引发气流爆炸\n
        气流爆炸范围500px内将产生喷射气流\n
         - 处于喷射气流范围内时， 单兵推进器的移动间隔冷却时间缩短\n
         - 空中施放后僵直减少\n
         - 下落移动速度 +50%\n
         - 喷射气流持续5秒
        """
        ...

# 制空掌握
# gunner_female/spitfire_female/f45301a5590cccefbe0becf2f8d029f5
# 944b9aab492c15a8474f96947ceeb9e4/f45301a5590cccefbe0becf2f8d029f5
class Skill44(PassiveSkill):
    """
        芙蕾雅独一无二的战斗技术。\n
        通过制空， 可更加容易发现敌人的破绽， 使基本攻击力和技能造成更高的伤害。
    """
    name = "制空掌握"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 1
    rangeLv = 3
    uuid = "f45301a5590cccefbe0becf2f8d029f5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

    associate = [{'type': '*skillDamage', 'data': data0}]

# 开火
# gunner_female/spitfire_female/9ceb0c55f40f1fc0fe0fcc65c8fee3a0
# 944b9aab492c15a8474f96947ceeb9e4/9ceb0c55f40f1fc0fe0fcc65c8fee3a0
class Skill45(ActiveSkill):
    """
        跳到空中， 将持有的所有手雷一次性扔向前方。\n
        在空中也可以施放。
    """
    name = "开火"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 8
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [160, 1600]
    uuid = "9ceb0c55f40f1fc0fe0fcc65c8fee3a0"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆炸攻击力 : {value0} X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 6
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 爆炸范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [开火]\n
        施放技能时， 投掷所有手雷\n
         - 消耗的手雷适用各自的攻击力
        """
        ...

    def vp_2(self):
        """
        [开火]\n
        施放技能时跳跃进入[全面轰炸]状态\n
         - 轰炸持续1秒\n
         - 轰炸过程中， 可以在自己脚下进行轰炸\n
         - 可以利用方向键在X、 Y轴自由移动\n
         - 轰炸状态下所受伤害 -70%
        """
        ...

# 光子霰雷发射器
# gunner_female/spitfire_female/3736fe00a26b0086c23db9a4426a5641
# 944b9aab492c15a8474f96947ceeb9e4/3736fe00a26b0086c23db9a4426a5641
class Skill46(ActiveSkill):
    """
        跳跃至空中投掷多枚光子手雷， 并向地面发射具有强力磁性的弹药。 悬浮在空中的光子手雷移动到落地的位置后， 引发爆炸并造成伤害。
    """
    name = "光子霰雷发射器"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "3736fe00a26b0086c23db9a4426a5641"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 光子手雷爆炸攻击力 : {value0} X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 8
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 爆炸范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [光子霰雷发射器]\n
        投掷更多的光子手雷\n
         - 光子手雷爆炸攻击次数变更为1次\n
         - 攻击范围 +20%\n
         - 基本冷却时间变更为67.5秒\n
         - 攻击力 +50%
        """
        self.cd = 67.5
        self.skillRation *= 1.5
        ...

    def vp_2(self):
        """
        [光子霰雷发射器]\n
        直接投掷光子手雷\n
         - 适用空中投掷及地上投掷冷却时间\n
         - 变更为可填充3次的技能\n
         - 每次填充冷却时间 : 15秒\n
         - 单次攻击力 -66%
        """
        self.cd = 15
        self.skillRation /= 3
        ...

# 决战之日
# gunner_female/spitfire_female/13a759aad5bb7fb7f08fae8f88c1cdbb
# 944b9aab492c15a8474f96947ceeb9e4/13a759aad5bb7fb7f08fae8f88c1cdbb
class Skill47(ActiveSkill):
    """
        向前方投掷一颗信号弹， 随后炮兵部队和战争女神机动队会集中火力支援信号弹指定的位置。\n
        可在空中投掷。
    """
    name = "决战之日"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 8000]
    uuid = "13a759aad5bb7fb7f08fae8f88c1cdbb"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0} X {value1}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 40
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 单兵推进器-02X
# gunner_female/spitfire_female/34e1bda921012f6018709f1c1a12b04d
# 944b9aab492c15a8474f96947ceeb9e4/34e1bda921012f6018709f1c1a12b04d
class Skill48(PassiveSkill):
    """
        重霄·弹药专家获得凝结天界技术的单兵推进器-02X， 以更高的机动力轰炸敌人， [单兵推进器]空中动作使用次数增加1次， 增加基本攻击力和转职技能攻击力， 部分技能获得附加效果。\n
    [M18阔剑地雷] : 投掷包含弹头的圆盘型M18阔剑地雷， 坠落至地面的阔剑地雷探测到敌人时自动爆炸， 再次按技能键则可以立即引爆。 减少爆炸时的击退距离。\n
    [手雷精通] : 提升技能攻击力增加率， [G-14手雷]、 [G-35L感电手雷]、 [G-18C冰冻手雷]中同系列的手雷投掷两次时， 强化下一次投掷的同系列手雷， 造成更高伤害。
    """
    name = "单兵推进器-02X"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "34e1bda921012f6018709f1c1a12b04d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [手雷精通]附加攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 强化手雷攻击力 : 手雷攻击力的{value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [{'type': '*skillDamage', 'data': data0}]

# 空袭战略
# gunner_female/spitfire_female/c591d1827cfbe224031c704e21d07932
# 944b9aab492c15a8474f96947ceeb9e4/c591d1827cfbe224031c704e21d07932
class Skill49(ActiveSkill):
    """
        装备单兵推进器-02X的身体部件， 为空中轰炸做准备。 在地面或特定高度以下使用时， 跳跃并飞至空中发动轰炸； 空中使用时， 在当前高度开始轰炸。\n
        在一段时间内， 不减少单兵推进器的使用次数， 可以悬浮在空中， 使用可在空中施放的技能。\n
        此时， 在单兵推进器-02X身体部件的作用下， 施放技能时后坐力消失。 删除[G-14手雷]、 [G-35L感电手雷]、 [G-18C冰冻手雷]的空中投掷冷却时间， 弹药数量不会降到1以下， 长按技能键时自动投掷手雷。\n
        再次按技能键或持续时间结束时， 投掷过载的单兵推进器-02X身体部件， 引发强大的终结爆炸。\n
        [空袭战略]持续期间， 施放[终解·制空霸权]技能时， 立即向地面投掷过载的单兵推进器-02X身体部件， 对敌人造成伤害。\n
        [空袭战略]悬浮期间，  可以按C键向前方冲刺， 但无法使用迅速降落(SPACE)的动作。 
    """
    name = "空袭战略"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 30
    mp = [400, 3000]
    uuid = "c591d1827cfbe224031c704e21d07932"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # [空袭战略]持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 终结爆炸攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

# 终解·制空霸权
# gunner_female/spitfire_female/8ad90fd01b5844edd692fff54d9f74e7
# 944b9aab492c15a8474f96947ceeb9e4/8ad90fd01b5844edd692fff54d9f74e7
class Skill50(ActiveSkill):
    """
        快速升到空中， 装备单兵推进器-02X。 然后飞向战场， 装备飞翼元件， 开始第1次轰炸， 对敌人造成伤害。\n
        第1次轰炸后， 装备单兵推进器-02X附加元件并开启全部武装， 执行终结轰炸， 然后返回地面。\n
        [单兵推进器]有使用次数时， 可以在空中施放。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "终解·制空霸权"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "8ad90fd01b5844edd692fff54d9f74e7"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 第1次轰炸攻击力 : {value0} x {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 7
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 终结轰炸攻击力 : {value2} x {value3}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 5
    data3 = get_data(f'{prefix}/{uuid}', 3)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'spitfire_female'
        self.nameCN = '重霄·弹药专家'
        self.role = 'gunner_female'
        self.角色 = '神枪手(女)'
        self.职业 = '弹药专家'
        self.jobId = '944b9aab492c15a8474f96947ceeb9e4'
        self.jobGrowId = 'c9b492038ee3ca8d27d7004cf58d59f3'

        self.武器选项 = ['手弩', '步枪','左轮枪','自动手枪','手炮']
        self.输出类型选项 = ['物理固伤','魔法固伤']
        self.输出类型 = '物理固伤'
        self.防具精通属性 = ['智力', '力量']
        self.防具类型 = '皮甲'
        self.buff = 1.911

        super().__init__(equVersion, __name__)
