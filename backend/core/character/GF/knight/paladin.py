#0ee8fa5dc525c1a1f23fc6911e921e4a
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "knight/paladin/cn/skillDetail"


# 盾击
# knight/paladin/717f1e2104fe4b796f800352fa143ecc
# 0ee8fa5dc525c1a1f23fc6911e921e4a/717f1e2104fe4b796f800352fa143ecc
class Skill6(ActiveSkill):
    """
    挥舞盾牌对敌人进行强力攻击， 并使其进入眩晕状态。\n
    追加操作时可以提起盾牌向前突进。\n
    [厚重的盾牌本身就是一件强大的武器。 但如果你没有足够的力量的话还是放弃这个想法吧。]
    """
    name = "盾击"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 3
    mp = [5, 180]
    uuid = "717f1e2104fe4b796f800352fa143ecc"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 挥击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 眩晕几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 眩晕持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 追加操作时突进攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1


# 天使降临
# knight/paladin/2a0a39184de92acf1c1375e00b77404c
# 0ee8fa5dc525c1a1f23fc6911e921e4a/2a0a39184de92acf1c1375e00b77404c
class Skill15(PassiveSkill):
    """
    将天界之光降临到武器和盾牌上， 对武器赋予光属性。 同时， 帕拉丁的战斗动作发生变化并增加物理攻击力。 盾牌朝前方时， 受到攻击时不会倒地， 同时增加物理/魔法防御力。\n
    防御成功时进入霸体状态， 效果持续一定时间。\n
    被攻击增加的防御力在施放[圣盾]、 [神光庇护]时不适用。\n
    在决斗场中， 不适用前方防御和光属性赋予功能。
    """
    name = "天使降临"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    uuid = "2a0a39184de92acf1c1375e00b77404c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 物理/魔法防御力增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 霸体持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    associate = [{"data":data1,"type":"$*PAtkP"}]

# 天使光翼
# knight/paladin/9dc8438e4572d39243c97da31c113acc
# 0ee8fa5dc525c1a1f23fc6911e921e4a/9dc8438e4572d39243c97da31c113acc
class Skill16(PassiveSkill):
    """
    增加攻击力， 并减少技能冷却时间， 但1、 2、 3次觉醒技能除外。 同时， 自身受到的有形或无形的威胁吸收为光翼形态的能量， 然后消耗能量对自身和队友施加各种效果。\n
    [获得天使之翼]\n
    - 天使之翼攻击成功时\n
    -\n
    - 地图上有被[神光冲击]击中的敌人且自身处于防御状态时\n
    [效果发动方式]\n
    - 施放技能时， 按住技能键一定时间， 可以将天使光翼的能量注入技能并发动效果。\n
    [发动的效果]\n
    - [神光冲击] : 将敌人吸附到攻击地点。 此时， 根据消耗资源的阶段， 增加吸附范围。\n
    - 转职后攻击技能 : 触发增益效果， 增加自身和队友的攻击速度、 移动速度、 施放速度、 暴击率和命中率。 根据消耗资源的阶段， 增加增益效果持续时间。\n
    - [神光庇护] : 新增恢复自身和圣域内队友生命值的效果。 根据消耗资源的阶段， 增加生命值恢复量。\n
    [学习戒律后]\n
    进入地下城时， 天使光翼获得量增加2个。\n
    [学习荣耀之光后]\n
    - 进入地下城时， 天使光翼获得量增加4个。\n
    [学习超越之翼后]\n
    - 进入地下城时， 天使光翼获得量增加2个。 额外增加2个光翼， 最多可以拥有8个光翼。 在拥有7个及以上光翼的状态下， 发动[天使光翼]时， 效果中增加减少队友所受伤害的功能。\n
    (所受伤害减少效果不与[圣盾]、 [神光庇护]的伤害减少效果叠加)
    """
    name = "天使光翼"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 1 #TODO
    rangeLv = 3
    uuid = "9dc8438e4572d39243c97da31c113acc"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 技能冷却时间减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [吸附范围]
    # 第1阶段 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 第2阶段 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 第3阶段 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 第4阶段 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 第5阶段 : {value6}px
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 第6阶段 : {value7}px
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [效果]
    # 攻击速度增加 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 移动速度增加 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 施放速度增加 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 暴击率增加 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 命中率增加 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 队友攻击速度增加 : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # 队友移动速度增加 : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # 队友施放速度增加 : {value15}%
    data15 = get_data(f'{prefix}/{uuid}', 15)
    # 队友暴击率增加 : {value16}%
    data16 = get_data(f'{prefix}/{uuid}', 16)
    # 队友命中率增加 : {value17}%
    data17 = get_data(f'{prefix}/{uuid}', 17)
    # [效果持续时间]
    # 第1阶段 : {value18}秒
    data18 = get_data(f'{prefix}/{uuid}', 18)
    # 第2阶段 : {value19}秒
    data19 = get_data(f'{prefix}/{uuid}', 19)
    # 第3阶段 : {value20}秒
    data20 = get_data(f'{prefix}/{uuid}', 20)
    # 第4阶段 : {value21}秒
    data21 = get_data(f'{prefix}/{uuid}', 21)
    # 第5阶段 : {value22}秒
    data22 = get_data(f'{prefix}/{uuid}', 22)
    # 第6阶段 : {value23}秒
    data23 = get_data(f'{prefix}/{uuid}', 23)
    # [每秒生命值恢复率]
    # 第1阶段 : {value24}%
    data24 = get_data(f'{prefix}/{uuid}', 24)
    # 第2阶段 : {value25}%
    data25 = get_data(f'{prefix}/{uuid}', 25)
    # 第3阶段 : {value26}%
    data26 = get_data(f'{prefix}/{uuid}', 26)
    # 第4阶段 : {value27}%
    data27 = get_data(f'{prefix}/{uuid}', 27)
    # 第5阶段 : {value28}%
    data28 = get_data(f'{prefix}/{uuid}', 28)
    # 第6阶段 : {value29}%
    data29 = get_data(f'{prefix}/{uuid}', 29)
    # [神圣意志 : 大天使降临]生命值恢复效率 : {value30}%
    data30 = get_data(f'{prefix}/{uuid}', 30)
    # [队友所受伤害减少率]
    # 拥有7个天使光翼时 : 5%
    # 拥有8个天使光翼时 : 10%

    associate = [{"data":data0,"type":"$*PAtkP"},{"data":data1,"type":"*cdReduce"}]

# 神光冲击
# knight/paladin/3fb8395ae3b81bd608e0c4223a8eb534
# 0ee8fa5dc525c1a1f23fc6911e921e4a/3fb8395ae3b81bd608e0c4223a8eb534
class Skill17(ActiveSkill):
    """
    用武器捶打地面， 震荡起神光波纹。\n
    [神光冲击]攻击成功时， 可以获得少量天使光翼， 同时被击中的敌人会进入被挑衅状态， 集中攻击施放者。
    """
    name = "神光冲击"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 4
    mp = [30, 300]
    uuid = "3fb8395ae3b81bd608e0c4223a8eb534"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 挑衅持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击成功时天使光翼获得量 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 神光连击
# knight/paladin/5806440d21e7546d50007a5ba11f8024
# 0ee8fa5dc525c1a1f23fc6911e921e4a/5806440d21e7546d50007a5ba11f8024
class Skill18(ActiveSkill):
    """
    左右挥舞光之武器攻击敌人。\n
    按向前方向键， 可以向前移动并进行攻击。
    """
    name = "神光连击"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 5
    mp = [30, 300]
    uuid = "5806440d21e7546d50007a5ba11f8024"
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
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 圣盾
# knight/paladin/d429147c372b549c3dadcabcba50787f
# 0ee8fa5dc525c1a1f23fc6911e921e4a/d429147c372b549c3dadcabcba50787f
class Skill19(ActiveSkill):
    """
    将光之力集中到盾牌上， 抵御一切攻击。\n
    施放技能后， 如果继续按住技能键， 可以维持圣盾状态， 在圣盾状态下受到攻击时不会倒地， 同时大幅减少所受伤害， 免疫眩晕、 石化、 冻结和睡眠异常状态， 并且可以进行移动和短距离的前后冲刺。\n
    防御成功时进入霸体状态， 效果持续一定时间。 在正确的时机防御成功时， 使伤害完全无效， 且天使光翼汲取到最大值\n
    在决斗场中， 防御成功时不进入霸体状态、 不适用伤害无效功能， 且圣盾持续时间上限为3秒。
    """
    name = "圣盾"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 2 #TODO
    rangeLv = 2
    cd = 3
    mp = [80, 800]
    uuid = "d429147c372b549c3dadcabcba50787f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 所受伤害减少率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 霸体持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 圣盾突击
# knight/paladin/7ec521d063d2190e1fcc5bd229af9bcf
# 0ee8fa5dc525c1a1f23fc6911e921e4a/7ec521d063d2190e1fcc5bd229af9bcf
class Skill20(ActiveSkill):
    """
    将光之力集中到盾牌上， 向前突进。\n
    圣盾会击退路径上的敌人， 对敌人造成多段攻击伤害。\n
    在决斗场中， 突进攻击无法击退霸体状态的敌人。
    """
    name = "圣盾突击"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 6
    mp = [40, 400]
    uuid = "7ec521d063d2190e1fcc5bd229af9bcf"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)


# 神光喷涌
# knight/paladin/0113c8b1306ca76d208f83f2d093dd62
# 0ee8fa5dc525c1a1f23fc6911e921e4a/0113c8b1306ca76d208f83f2d093dd62
class Skill22(ActiveSkill):
    """
    将光之力集中到武器上， 然后用武器锤击地面， 喷涌神光。\n
    神光向垂直方向喷涌， 造成多段攻击伤害。\n
    按向前方向键， 可以向前移动并进行攻击。\n
    [学习超越之翼后]\n
    基本攻击变更为3次， 原来的上挑攻击力并入锤击攻击力中。\n
    锤击攻击时， 发动小型神光喷涌， 对敌人造成多段攻击伤害。\n
    小型神光喷涌的攻击力以[神光喷涌]攻击力的一定比率适用。
    """
    name = "神光喷涌"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 8
    mp = [50, 500]
    uuid = "0113c8b1306ca76d208f83f2d093dd62"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 锤击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 喷涌的神光攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 4
    # 喷涌的神光多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 神光喷涌范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    powerLittle = 0

    mode = ['','小型']

    def setMode(self, mode):
        if mode == '小型':
            self.hit0 = 0
            self.hit1 = 5
            self.skillRation *= self.powerLittle
            ...

# 信仰之念
# knight/paladin/8b08f9504167a9c0f3a1d29d71b7943e
# 0ee8fa5dc525c1a1f23fc6911e921e4a/8b08f9504167a9c0f3a1d29d71b7943e
class Skill23(ActiveSkill):
    """
    爆发光之力， 强化自身的基本攻击力和技能攻击力。
    """
    name = "信仰之念"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 7 #TODO
    rangeLv = 3
    cd = 5
    uuid = "8b08f9504167a9c0f3a1d29d71b7943e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 神光盾击
# knight/paladin/ac21c02567f04a92b54dd85c091d1e5a
# 0ee8fa5dc525c1a1f23fc6911e921e4a/ac21c02567f04a92b54dd85c091d1e5a
class Skill24(ActiveSkill):
    """
    将光之力集中到盾牌上， 然后朝地面挥动盾牌， 释放光之力。\n
    被击中的敌人会旋转飞出。
    """
    name = "神光盾击"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 8
    mp = [60, 600]
    uuid = "ac21c02567f04a92b54dd85c091d1e5a"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 第1击多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 第2击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 3
    # 第2击多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 神光释放范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 烈光
# knight/paladin/82fc7ec7cfb2b7afa8c125a2d9420a78
# 0ee8fa5dc525c1a1f23fc6911e921e4a/82fc7ec7cfb2b7afa8c125a2d9420a78
class Skill25(ActiveSkill):
    """
    将光之力集中到武器上， 从下往上挑击， 使敌人浮空， 然后用盾牌将其砸向地面。\n
    被盾牌击中的敌人会砸到地面后再弹起。
    """
    name = "烈光"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 8
    mp = [60, 600]
    uuid = "82fc7ec7cfb2b7afa8c125a2d9420a78"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 上挑攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 下砸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 神光闪耀
# knight/paladin/ab6fc3303df03b58911967dfca2b5d07
# 0ee8fa5dc525c1a1f23fc6911e921e4a/ab6fc3303df03b58911967dfca2b5d07
class Skill26(ActiveSkill):
    """
    将光之力集中到武器上， 然后释放神光能量， 对周围的敌人造成多段攻击伤害。\n
    技能施放过程中， 按跳跃键可以立即发动最后一击。\n
    按向前方向键， 可以向前移动并进行攻击。
    """
    name = "神光闪耀"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 1 #TODO
    rangeLv = 2
    cube = 1
    cd = 16
    mp = [70, 700]
    uuid = "ab6fc3303df03b58911967dfca2b5d07"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 10
    # 多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [神光闪耀]\n
        攻击过程中可以移动和前冲\n
        攻击范围 +40%
        """
        ...

    def vp_2(self):
        """
        [神光闪耀]\n
        施放过程中所受伤害 -70%\n
        可以解除控制型异常状态并施放； 施放中免疫所有异常状态
        """
        ...

# 神光闪影击
# knight/paladin/c91a62dc0a18360acf5031ac0ebf09f5
# 0ee8fa5dc525c1a1f23fc6911e921e4a/c91a62dc0a18360acf5031ac0ebf09f5
class Skill27(ActiveSkill):
    """
    将集中到武器上的光之力向正面射出， 对敌人造成多段攻击伤害， 然后挥动盾牌发射光之冲击波， 发动最后一击。\n
    按向前方向键， 可以短距离向前移动并进行攻击。 最后一击前按向后方向键， 可以在原地发动最后一击。
    """
    name = "神光闪影击"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cube = 1
    cd = 18
    mp = [70, 700]
    uuid = "c91a62dc0a18360acf5031ac0ebf09f5"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 10
    # 多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [神光闪影击]\n
        被光束命中的敌人将被移动到帕拉丁面前\n
        最后一击命中的敌人将被赋予眩晕异常状态\n
        - 眩晕几率 : 100%\n
        - 持续时间 : 3秒\n
        攻击范围 +70%
        """
        ...

    def vp_2(self):
        """
        [神光闪影击]\n
        删除光束攻击， 突进一小段距离后立即发动最后一击\n
        - 总攻击力相同\n
        [圣盾突击]\n
        可以强制中断[圣盾突击]的施放后僵直并施放该技能， 或强制中断此技能的施放后僵直并施放[圣盾突击]
        """
        ...

# 惩罚之锤
# knight/paladin/0c3a468aee1f7ce06bf91eb3319518c1
# 0ee8fa5dc525c1a1f23fc6911e921e4a/0c3a468aee1f7ce06bf91eb3319518c1
class Skill28(ActiveSkill):
    """
    垂直掉落由光凝聚而成的惩罚之锤， 引发爆炸， 对范围内的敌人造成伤害。
    """
    name = "惩罚之锤"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [80, 800]
    uuid = "0c3a468aee1f7ce06bf91eb3319518c1"
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
        [惩罚之锤]\n
        对周围600px内最强敌人落下审判之锤\n
        使命中的敌人进入眩晕异常状态\n
        - 眩晕几率 : 100%\n
        - 持续时间 : 3秒\n
        攻击范围 +40%
        """
        ...

    def vp_2(self):
        """
        [惩罚之锤]\n
        转职技能施放过程中也可以施放 (觉醒技能除外)\n
        - 删除施放动作\n
        被圣光之力强化的锤子发生爆炸， 使自身和周围队员的生命值/魔法值恢复10%
        """
        ...

# 神光之跃
# knight/paladin/5cac3411ccef1af333953e0ded5e942d
# 0ee8fa5dc525c1a1f23fc6911e921e4a/5cac3411ccef1af333953e0ded5e942d
class Skill29(ActiveSkill):
    """
    将光之力集中到武器上， 然后跳向前方锤击地面， 引发爆炸， 对范围内的敌人造成伤害。\n
    按前方向键， 可以跳得更远。
    """
    name = "神光之跃"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [90, 900]
    uuid = "5cac3411ccef1af333953e0ded5e942d"
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
        [神光之跃]\n
        施放技能时进入无敌状态\n
        大幅增加跳跃高度\n
        攻击范围 +30%
        """
        ...

    def vp_2(self):
        """
        [神光之跃]\n
        生成审判之锤砸向前方\n
        - 可以强制中断转职技能的施放后僵直并施放该技能 (觉醒技能除外)\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 22.5秒\n
        - 单次攻击力 -50%
        """
        self.cd = 22.5
        self.skillRation *= 1 - 0.5
        ...

# 荣耀之光
# knight/paladin/85f7c810ad503790e8626439fe936d56
# 0ee8fa5dc525c1a1f23fc6911e921e4a/85f7c810ad503790e8626439fe936d56
class Skill30(PassiveSkill):
    """
    天界之力进一步集中到帕拉丁身上， 增加光盾大小和物理攻击力， 并且进入地下城时可以获得一定数量的天使光翼。
    """
    name = "荣耀之光"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 3
    uuid = "85f7c810ad503790e8626439fe936d56"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 天使光翼获得量 : 2个
    associate = [{"data":data0,"type":"$*PAtkP"}]

# 信仰聚合 : 神光惩戒
# knight/paladin/002cbdd9bfd0f0b970451ae8d48d029e
# 0ee8fa5dc525c1a1f23fc6911e921e4a/002cbdd9bfd0f0b970451ae8d48d029e
class Skill31(ActiveSkill):
    """
    以绝对防御的姿态将凝聚的天界之光加速集中到武器和盾牌上， 然后向前挥动武器和盾牌， 引爆光之力。\n
    在神光集中的状态下， 获得更强大的防御力， 可以抵御一切伤害。 若持续按住技能键， 可以使该状态持续一定时间。\n
    神光爆炸时， 会消耗所有天使光翼， 使范围内的敌人受到伤害。 技能结束时， 天使光翼吸收到最大值。
    """
    name = "信仰聚合 : 神光惩戒"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [300, 3000]
    uuid = "002cbdd9bfd0f0b970451ae8d48d029e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 神光集中状态可持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

# 神光庇护
# knight/paladin/31823197cc0b04d4c5dcf8f928d9220c
# 0ee8fa5dc525c1a1f23fc6911e921e4a/31823197cc0b04d4c5dcf8f928d9220c
class Skill32(ActiveSkill):
    """
    将集中到盾牌上的光之力释放到周围， 为自己和队友抵挡受到的一切攻击。\n
    在持续时间内， 自身和范围内的队友受到攻击时不会倒地， 同时大幅减少所受伤害， 免疫眩晕、 石化、 冻结和睡眠异常状态。\n
    消耗天使光翼施放时， 恢复周围队员的生命值。\n
    在持续时间内按跳跃键可以解除神光庇护状态。
    """
    name = "神光庇护"
    learnLv = 60
    masterLv = 1
    maxLv = 1
    position = 2 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [240, 240]
    uuid = "31823197cc0b04d4c5dcf8f928d9220c"
    hasVP = True
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 所受伤害减少率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 所受伤害减少率 (队友) : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 释放范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [神光庇护]\n
        施放时， 将周围的敌人向外击退\n
        所受伤害减少量变更为50%
        """
        ...

    def vp_2(self):
        """
        [神光庇护]\n
        施放后帕拉丁可以进行其他行动\n
        - 在释放范围内施放[圣盾]时， 伤害减少效果不会叠加\n
        释放范围 +20%
        """
        ...

# 圣盾裁决
# knight/paladin/dac8d8207618150c162e4c6f9e168527
# 0ee8fa5dc525c1a1f23fc6911e921e4a/dac8d8207618150c162e4c6f9e168527
class Skill33(ActiveSkill):
    """
    将光之力集中到盾牌上， 向前推出盾牌并释放光之力。\n
    释放的光束对范围内的敌人造成伤害， 并使敌人进入眩晕状态。
    """
    name = "圣盾裁决"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [120, 1200]
    uuid = "dac8d8207618150c162e4c6f9e168527"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 眩晕几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 眩晕持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [圣盾裁决]\n
        可以强制中断转职技能的施放后僵直并施放该技能 (觉醒技能除外)\n
        施放技能后立即被击时所受伤害无效\n
        眩晕效果变更为强制控制
        """
        ...

    def vp_2(self):
        """
        [圣盾裁决]\n
        在盾牌中凝聚更强大的光之力后向前方直线发射\n
        - 总攻击力相同\n
        - 删除眩晕效果\n
        光之力经过的地方生成光明之路， 使路径上的自身和队员的移动速度增加\n
        - 持续时间 : 5秒\n
        - 移动速度增加量 : 100%
        """
        ...

# 破晓之光
# knight/paladin/8e358ecf99ac9df31a6132aeafe378a9
# 0ee8fa5dc525c1a1f23fc6911e921e4a/8e358ecf99ac9df31a6132aeafe378a9
class Skill34(ActiveSkill):
    """
    将光之力集中到自己身上， 冲上天空后快速降落到地面， 引发爆炸。\n
    爆炸时产生光之冲击波， 对范围内的敌人造成伤害。\n
    可以利用方向键调整降落地点。
    """
    name = "破晓之光"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 1 #TODO
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [140, 1400]
    uuid = "8e358ecf99ac9df31a6132aeafe378a9"
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
        [破晓之光]\n
        施放后从天空落下审判之光 (最多攻击3次)\n
        - 总攻击力相同\n
        攻击范围 +60%
        """
        ...

    def vp_2(self):
        """
        [破晓之光]\n
        变更为可以在空中施放\n
        - 被击和倒地状态下也可以施放\n
        落地动作变更为无敌状态\n
        无法填充[天使光翼]
        """
        ...

# 戒律
# knight/paladin/9f57da5cb3651d81ca7dc9f78be33d01
# 0ee8fa5dc525c1a1f23fc6911e921e4a/9f57da5cb3651d81ca7dc9f78be33d01
class Skill35(PassiveSkill):
    """
    奉行伟大意志、 执行天命的破晓女神进入地下城时， 获得更多天使光翼， 并增加基本攻击力和技能攻击力。
    """
    name = "戒律"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 3
    uuid = "9f57da5cb3651d81ca7dc9f78be33d01"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 天使光翼获得量 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [{"data":data0}]

# 神光回旋斩
# knight/paladin/0e3da11226dd30c2aaef52e36eff7f3f
# 0ee8fa5dc525c1a1f23fc6911e921e4a/0e3da11226dd30c2aaef52e36eff7f3f
class Skill36(ActiveSkill):
    """
    将盾牌中凝聚的光之力挥洒到周围， 吸附范围内的敌人， 然后挥动武器上挑攻击敌人。
    """
    name = "神光回旋斩"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 2
    cube = 5
    cd = 40
    mp = [450, 4500]
    uuid = "0e3da11226dd30c2aaef52e36eff7f3f"
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
        [神光回旋斩]\n
        向周围倾泻天堂的力量， 发动攻击并引发连锁爆炸\n
        - 总攻击力相同\n
        连锁爆炸范围 +20%
        """
        ...

    def vp_2(self):
        """
        [神光回旋斩]\n
        跳跃后追踪前方最强敌人， 突进后下劈攻击\n
        施放技能时, 可以获得并消耗最大数量的[天使光翼]， 适用增益效果
        """
        ...

# 神圣信约
# knight/paladin/3cb633d00f8f6ee088682c9171020d26
# 0ee8fa5dc525c1a1f23fc6911e921e4a/3cb633d00f8f6ee088682c9171020d26
class Skill37(ActiveSkill):
    """
    将武器中凝聚的光之力注入地面并向四周喷涌， 对敌人造成多段攻击伤害。
    """
    name = "神圣信约"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 2 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [500, 5000]
    uuid = "3cb633d00f8f6ee088682c9171020d26"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 11
    # 多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [神圣信约]\n
        将武器中蕴含的光之力量聚集到地面， 引发大爆炸\n
        攻击范围 +30%
        """
        ...

    def vp_2(self):
        """
        [神圣信约]\n
        可以在除觉醒技能外的转职技能施放过程中施放； 可以解除控制型异常状态并施放\n
        - 由大天使代替施放技能， 解除帕拉丁的负面异常状态
        """
        ...

# 神圣意志 : 大天使降临
# knight/paladin/6d7c9a15c08cc41d70125083e869e1a1
# 0ee8fa5dc525c1a1f23fc6911e921e4a/6d7c9a15c08cc41d70125083e869e1a1
class Skill38(ActiveSkill):
    """
    向前方举起盾牌， 进入意志召唤状态， 使大天使降临， 利用充溢的光之力治愈队友。 (恢复量受天使光翼的影响)\n
    按住技能键可以维持意志召唤状态， 松开技能键或者经过一定时间后， 与大天使合力向前方突进， 释放神光， 使周围敌人受到伤害。\n
    意志召唤状态下， 按向后方向键时， 在原地释放神光。\n
    技能结束时， 天使光翼汲取到最大值。
    """
    name = "神圣意志 : 大天使降临"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2000, 5000]
    uuid = "6d7c9a15c08cc41d70125083e869e1a1"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 意志召唤持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

# 超越之翼
# knight/paladin/c1dd8b776fb1dd24c6373c678ef1dd2e
# 0ee8fa5dc525c1a1f23fc6911e921e4a/c1dd8b776fb1dd24c6373c678ef1dd2e
class Skill39(PassiveSkill):
    """
    皓曦·帕拉丁获得超越者梅丹佐之力， 增加基本攻击力和转职技能攻击力， 部分技能获得附加效果。\n
    [天使光翼] : 进入地下城时， 增加天使光翼获得量； 额外增加2个新的光翼， 在拥有7个及以上光翼的状态下， 发动[天使光翼]时， 效果中增加减少队友所受伤害的功能。\n
    (伤害减少效果不与[圣盾]、 [神光庇护]的伤害减少效果叠加)\n
    [神光喷涌] : 基本攻击变更为3次， 原来的第4次上挑攻击力并入锤击攻击力中。\n
    锤击攻击时， 发动小型神光喷涌， 对敌人造成多段攻击伤害。\n
    小型神光喷涌的攻击力以[神光喷涌]攻击力的一定比率适用。
    """
    name = "超越之翼"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "c1dd8b776fb1dd24c6373c678ef1dd2e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [神光喷涌]
    # 小型神光喷涌攻击力 : 神光喷涌攻击力的{value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [天使光翼]
    # 队友所受伤害减少率 (7个) : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 队友所受伤害减少率 (8个) : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 天使光翼获得量 : {value4}个
    data4 = get_data(f'{prefix}/{uuid}', 4)

    associate = [{"data":data0},{"data":data1,"type":"+powerLittle","skills":["神光喷涌"]}]

# 神光耀世
# knight/paladin/481348575c1e141925c836b59c5db3ca
# 0ee8fa5dc525c1a1f23fc6911e921e4a/481348575c1e141925c836b59c5db3ca
class Skill40(ActiveSkill):
    """
    召唤梅丹佐的盾牌， 然后挥动盾牌， 利用神光之力攻击敌人。\n
    神光照射的地方产生光之裂缝， 然后帕拉丁用盾牌砸向地面， 使光之裂缝爆炸， 对大范围的敌人造成强力伤害。\n
    施放技能时， 在装备梅丹佐的盾牌之前， 天使光翼汲取到最大值。
    """
    name = "神光耀世"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [960, 7200]
    uuid = "481348575c1e141925c836b59c5db3ca"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 神光攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 神光多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 下砸冲击波攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 光之裂缝爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 6
    # 光之裂缝爆炸多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 启示录 : 末日救赎
# knight/paladin/5f4c55fe2ebdf0623bd76d4fda872ddc
# 0ee8fa5dc525c1a1f23fc6911e921e4a/5f4c55fe2ebdf0623bd76d4fda872ddc
class Skill41(ActiveSkill):
    """
    以超越者梅丹佐的姿态现身， 遵照最后的启示， 救赎整个世界。\n
    施放时， 神圣光辉环绕在皓曦·帕拉丁周围， 稍后， 拥有八翼的超越者梅丹佐现身。\n
    然后， 周围漂浮的梅丹佐之眼中发射光芒， 造成多段攻击伤害， 梅丹佐升上天空， 召唤巨大的梅丹佐之锤砸向地面， 对敌人造成巨大伤害。\n
    首次施放时， [天使光翼]效果以最大效果发动； 技能结束时， 天使光翼汲取到最大值。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "启示录 : 末日救赎"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4025, 8055]
    uuid = "5f4c55fe2ebdf0623bd76d4fda872ddc"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 首次爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 梅丹佐之眼攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 7
    # 梅丹佐之眼多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 梅丹佐之锤冲撞攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 终结爆炸攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 7
    # 终结爆炸多段攻击次数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'paladin'
        self.nameCN = '皓曦·帕拉丁'
        self.role = 'knight'
        self.角色 = '守护者'
        self.职业 = '帕拉丁'
        self.jobId = '0ee8fa5dc525c1a1f23fc6911e921e4a'
        self.jobGrowId = '6d459bc74ba73ee4fe5cdc4655400193'

        self.武器选项 = ['太刀', '钝器', '巨剑', '短剑']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '板甲'
        self.buff = 1.962

        super().__init__(equVersion, __name__)
