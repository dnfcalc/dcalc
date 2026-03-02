#f6a4ad30555b99b499c07835f87ce522
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "priest_male/infighter/cn/skillDetail"


# 虎袭
# priest_male/infighter/f2fb27162beb0b87a7cb9af7900e95f2
# f6a4ad30555b99b499c07835f87ce522/f2fb27162beb0b87a7cb9af7900e95f2
class Skill1(ActiveSkill):
    """
        抓取前方1名敌人并向前跑动一段距离后扔开， 可以对跑动中撞到的敌人造成多段攻击伤害。\n
        若在前冲中按攻击键， 则直接扔开抓住的敌人。 抓住的敌人只有在最后扔开时才有伤害判定， 掷出的敌人会对撞到的敌人造成附加伤害。\n
        抓取并掷出敌人时， 若按攻击键， 则可以给予敌人更多伤害。\n
        抓取判定 : 可以抓取霸体和防御状态的敌人， 但对无法抓取的敌人不适用抓取和控制效果。\n
        转职为光明骑士时， 技能类型变为独立攻击力。
    """
    name = "虎袭"
    learnLv = 1
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 5
    mp = [15, 154]
    uuid = "f2fb27162beb0b87a7cb9af7900e95f2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 跑动中撞到敌人时攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 跑动中攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 扔开抓住的敌人时攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 间接攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 追加操作后的攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)


# 直拳冲击
# priest_male/infighter/faf9cd66281078b51be2ee0b0f6c5530
# f6a4ad30555b99b499c07835f87ce522/faf9cd66281078b51be2ee0b0f6c5530
class Skill7(ActiveSkill):
    """
        向前方敌人发出强威力的直拳冲击， 可以形成多段攻击； 最后一击有很高的伤害和暴击率。\n
        转职成为蓝拳使者时， 才可以强制中断基本攻击动作， 并立即施放该技能。
    """
    name = "直拳冲击"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 3
    mp = [15, 154]
    uuid = "faf9cd66281078b51be2ee0b0f6c5530"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 第一击和第二击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 2
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 最后一击的物理/魔法暴击率增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)


# 勾拳追击
# priest_male/infighter/d296043df164385a14cb973c8c7c4d07
# f6a4ad30555b99b499c07835f87ce522/d296043df164385a14cb973c8c7c4d07
class Skill9(ActiveSkill):
    """
        向前方敌人发动前冲攻击后， 可以用上勾拳进行追击。
    """
    name = "勾拳追击"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 2
    mp = [10, 84]
    uuid = "d296043df164385a14cb973c8c7c4d07"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 浮空力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)


# 俯冲
# priest_male/infighter/9dda3f4a849dba1a288dd65e116860f2
# f6a4ad30555b99b499c07835f87ce522/9dda3f4a849dba1a288dd65e116860f2
class Skill13(ActiveSkill):
    """
        低身快速向前移动， 进入短暂的无敌状态\n
        无法互相强制中断[摆动]和[俯冲]。\n
        [俯冲]中再按跳跃键就可以停止移动。\n
        只能在[意念驱动]已施放的状态下使用。
    """
    name = "俯冲"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 6
    rangeLv = 1
    cd = 0.7
    mp = [1, 1]
    uuid = "9dda3f4a849dba1a288dd65e116860f2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 移动距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 移动时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 无敌时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 摆动
# priest_male/infighter/0969cd4054d93da07708108c0cc1c4b5
# f6a4ad30555b99b499c07835f87ce522/0969cd4054d93da07708108c0cc1c4b5
class Skill14(ActiveSkill):
    """
        抽身的同时快速向后退， 并进入短时间的无敌状态。\n
        无法强制中断[摆动]并立即施放[俯冲]， 也无法强制中断[俯冲]并立即施放[摆动]。\n
        移动中再次按跳跃键， 可以停止移动。\n
        只能在[意念驱动]已施放的状态下使用。
    """
    name = "摆动"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 6
    rangeLv = 1
    cd = 0.7
    mp = [1, 1]
    uuid = "0969cd4054d93da07708108c0cc1c4b5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 施放后无敌时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)


# 意念驱动
# priest_male/infighter/8f73f243041c2d27739fe7696f02bf9b
# f6a4ad30555b99b499c07835f87ce522/8f73f243041c2d27739fe7696f02bf9b
class Skill17(ActiveSkill):
    """
        把巨兵插入地面使一定范围内的敌人出现僵直， 并赋予自身巨兵之力的效果。\n
        站在[意念驱动]范围内时， 可以增加暴击伤害、 物理暴击率和命中率， 离开[意念驱动]范围一定时间后， 效果会消失。\n
        减少除[泯灭神击]、 [制裁 : 怒火疾风]、 [正义执行 : 雷米迪奥斯的圣座]外的技能冷却时间。\n
        若插入巨兵后， 按住技能键不放， 则可以直接收回巨兵。\n
        进入地下城时， 巨兵初始状态为插入地面； 在决斗场中， 巨兵初始状态为握在手中。
    """
    name = "意念驱动"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 2
    rangeLv = 3
    cd = 5
    uuid = "8f73f243041c2d27739fe7696f02bf9b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 效果领域范围 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 僵直效果范围 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 暴击伤害增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 物理暴击率增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 命中率增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 技能冷却时间减少率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 离开[意念驱动]范围后增益效果持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)

    associate = [{"data":data2},{"data":data5,"type":"*cdReduce","exceptSkills":["泯灭神击","制裁 : 怒火疾风","正义执行 : 雷米迪奥斯的圣座"]}]

# 百炼成刚
# priest_male/infighter/da6e37c1e3f0e8867f70007d89c239ff
# f6a4ad30555b99b499c07835f87ce522/da6e37c1e3f0e8867f70007d89c239ff
class Skill18(PassiveSkill):
    """
    强化身体， 提升移动速度、 攻击速度和跳跃力。 并向外散放拳气， 使[基本攻击的上钩拳]、 [勾拳追击]、 [前冲攻击]可以向更低位置的敌人发动。
    """
    name = "百炼成刚"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 0
    rangeLv = 1
    uuid = "da6e37c1e3f0e8867f70007d89c239ff"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 移动速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 跳跃力增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 俯冲直拳
# priest_male/infighter/de3fea2d65c597f4d55c70a02b97fc79
# f6a4ad30555b99b499c07835f87ce522/de3fea2d65c597f4d55c70a02b97fc79
class Skill19(ActiveSkill):
    """
        [俯冲]中向前方敌人发出直拳攻击， 可以击飞敌人。\n
        学习一定等级的[技巧精通]后， [摆动]中也可以发出攻击。
    """
    name = "俯冲直拳"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cd = 3.5
    mp = [18, 196]
    uuid = "de3fea2d65c597f4d55c70a02b97fc79"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1

# 俯冲翔拳
# priest_male/infighter/202edb928046f4fa6dedf6337377efd5
# f6a4ad30555b99b499c07835f87ce522/202edb928046f4fa6dedf6337377efd5
class Skill20(ActiveSkill):
    """
        [俯冲]中向前方敌人发出上勾拳攻击， 可以使敌人浮空。\n
        学习一定等级的[技巧精通]后， [摆动]中也可以发出攻击。
    """
    name = "俯冲翔拳"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 3.5
    mp = [18, 196]
    uuid = "202edb928046f4fa6dedf6337377efd5"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 浮空力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 技巧精通
# priest_male/infighter/8c2379737c5acc935c1731f67f607655
# f6a4ad30555b99b499c07835f87ce522/8c2379737c5acc935c1731f67f607655
class Skill21(PassiveSkill):
    """
        增加基本攻击力和转职技能攻击力。\n
        增加移动速度。\n
        下一次攻击或施放以下技能时， 增加攻击范围。\n
    - 基本攻击、 [瞬拳]、 [圣拳连击]\n
        以下技能出现附加效果 :\n
    - [俯冲直拳]、 [俯冲翔拳]和[俯冲腹拳]可在[摆动]中使用。\n
    - [破碎之锤]可在[俯冲]中使用。\n
    - [刺拳猛击]和[破碎之拳]增加吸附周围敌人的效果， 吸附力随等级增加。\n
    - [神圣反击]可使用追加操作手动发动攻击， 但手动发动攻击时攻击力会减少。\n
        以下技能的特定动作变为霸体状态。\n
    - [直拳冲击]、 [俯冲腹拳]、 [破碎之锤]、 [神圣组合拳]\n
        使用以下技能命中时， 根据原技能的攻击力附加一定比例的伤害。\n
    - [俯冲直拳]、 [俯冲腹拳]、 [俯冲翔拳]、 [圣拳连击]
    """
    name = "技巧精通"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 1
    rangeLv = 3
    uuid = "8c2379737c5acc935c1731f67f607655"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击X轴范围增加 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 基本攻击Z轴范围增加 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [圣拳连击]范围增加 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [瞬拳]范围增加 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 移动速度增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [神圣反击]手动发动攻击时攻击力比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [刺拳猛击]吸附范围 : {value7}px
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [破碎之拳]吸附周围敌人的范围 : {value8}px 
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # - [根据原技能攻击力附加伤害] -
    # 俯冲直拳 : {value9}% x {value10}
    data9 = get_data(f'{prefix}/{uuid}', 9)
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 俯冲腹拳 : {value11}% x {value12}
    data11 = get_data(f'{prefix}/{uuid}', 11)
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 俯冲翔拳 : {value13}% x {value14}
    data13 = get_data(f'{prefix}/{uuid}', 13)
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # 圣拳连击 : {value15}% x {value16}
    data15 = get_data(f'{prefix}/{uuid}', 15)
    data16 = get_data(f'{prefix}/{uuid}', 16)

    associate = [
        {"data":data0},
        {"data":[i*j for i,j in zip(data9,data10)],"skills":["俯冲直拳"]},
        {"data":[i*j for i,j in zip(data11,data12)],"skills":["俯冲腹拳"]},
        {"data":[i*j for i,j in zip(data13,data14)],"skills":["俯冲翔拳"]},
        {"data":[i*j for i,j in zip(data15,data16)],"skills":["圣拳连击"]},
        {"data":data6,type:"=preRatio", "skills":["神圣反击"]},
        ]

# 俯冲腹拳
# priest_male/infighter/c61f5a010370101402b05b21916c2071
# f6a4ad30555b99b499c07835f87ce522/c61f5a010370101402b05b21916c2071
class Skill22(ActiveSkill):
    """
        [俯冲]中向敌人腹部发出猛力拳击， 可以使敌人进入较长时间的僵直状态， 并有一定几率使其出现眩晕。\n
        学习一定等级的[技巧精通]后， [摆动]中也可以发出攻击。
    """
    name = "俯冲腹拳"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cd = 3.5
    mp = [18, 196]
    uuid = "c61f5a010370101402b05b21916c2071"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 眩晕几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 眩晕持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 圣拳锤击
# priest_male/infighter/6a1d1f08a6572be420bb3a256c44c015
# f6a4ad30555b99b499c07835f87ce522/6a1d1f08a6572be420bb3a256c44c015
class Skill23(ActiveSkill):
    """
        用拳头猛烈捶击地面， 使敌人受到伤害并引发冲击波。\n
        只能在已施放[意念驱动]的状态下使用。
    """
    name = "圣拳锤击"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 5
    mp = [12, 137]
    uuid = "6a1d1f08a6572be420bb3a256c44c015"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 直接攻击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 冲击波范围 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)


# 圣拳连击
# priest_male/infighter/3829c15bf5f520c13998a3479ba0ce7b
# f6a4ad30555b99b499c07835f87ce522/3829c15bf5f520c13998a3479ba0ce7b
class Skill26(ActiveSkill):
    """
        向前方敌人快速发出刺拳、 直拳、 摆拳三连击， 可以使敌人受到极大伤害。\n
        摆拳后可以直接使用[俯冲]或[摆动]。\n
        技能等级越高， 敌人被摆拳击中后的僵直时间越长， 但只能在[意念驱动]已施放状态下使用。
    """
    name = "圣拳连击"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 7
    mp = [45, 462]
    uuid = "3829c15bf5f520c13998a3479ba0ce7b"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击速度增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 刺拳攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 直拳攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 摆拳攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1

# 急速闪避
# priest_male/infighter/dc1ffbe7bfcc6dc2be737951960da9ad
# f6a4ad30555b99b499c07835f87ce522/dc1ffbe7bfcc6dc2be737951960da9ad
class Skill27(PassiveSkill):
    """
        使用除[幻影化身]之外的所有神击系技能时， 大幅增加自身回避率。\n
        使用[急速闪避]、 [俯冲]、 [摆动]成功回避敌人的攻击时， 增加自身的暴击率和命中率。
    """
    name = "急速闪避"
    learnLv = 25
    masterLv = 5
    maxLv = 15
    position = 9
    rangeLv = 3
    uuid = "dc1ffbe7bfcc6dc2be737951960da9ad"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # - 神击系技能回避率增加 -
    # [俯冲直拳] : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [俯冲腹拳] : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [俯冲翔拳] : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [圣拳连击] : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [神圣反击] : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [破碎之锤] : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [刺拳猛击] : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [瞬拳] : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [圣拳锤击] : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [旋涡重拳] : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # [神圣组合拳] : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # [极速飓风拳] : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # [泯灭神击] : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # [破碎之拳] : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # [破坏之拳] : {value15}%
    data15 = get_data(f'{prefix}/{uuid}', 15)
    # [仲裁怒击] : {value16}%
    data16 = get_data(f'{prefix}/{uuid}', 16)
    # [超重拳] : {value17}%
    data17 = get_data(f'{prefix}/{uuid}', 17)
    # [正义铁拳] : {value18}%
    data18 = get_data(f'{prefix}/{uuid}', 18)
    # 增益效果持续时间 : {value19}秒
    data19 = get_data(f'{prefix}/{uuid}', 19)
    # 物理暴击率增加 : {value20}%
    data20 = get_data(f'{prefix}/{uuid}', 20)
    # 命中率增加 : {value21}%
    data21 = get_data(f'{prefix}/{uuid}', 21)
    # 效果叠加次数上限 : {value22}次
    data22 = get_data(f'{prefix}/{uuid}', 22)

# 瞬拳
# priest_male/infighter/a2d943797daca862a6f321aca6ac9bfa
# f6a4ad30555b99b499c07835f87ce522/a2d943797daca862a6f321aca6ac9bfa
class Skill28(ActiveSkill):
    """
        用风一样的速度将拳头伸向远处攻击敌人。\n
        施放技能后再按技能键或攻击键， 可以发动抓取敌人的追加攻击。\n
        只能在已施放[意念驱动]的状态下使用。
    """
    name = "瞬拳"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 4
    mp = [22, 231]
    uuid = "a2d943797daca862a6f321aca6ac9bfa"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 追加攻击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 范围 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 神圣反击
# priest_male/infighter/a6c8f69107f8c4f5d1a0c7a57d000290
# f6a4ad30555b99b499c07835f87ce522/a6c8f69107f8c4f5d1a0c7a57d000290
class Skill29(ActiveSkill):
    """
        施放后使自身进入祈祷状态， 若此时受到正面攻击， 则以向前重击的方式对敌人施展腹拳。\n
        攻击力为自身掌握的[俯冲腹拳]与[神圣反击]原攻击力的总和。 被敌人攻击时， 自身伤害会有所减少， 且给予不死族、 恶魔、 精灵系列怪物125%的反击伤害。
    """
    name = "神圣反击"
    learnLv = 30
    masterLv = 1
    maxLv = 11
    position = 2
    rangeLv = 3
    cd = 6
    mp = [22, 231]
    uuid = "a6c8f69107f8c4f5d1a0c7a57d000290"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 追加攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 所受伤害减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    preRatio = 1
    power2 = 1

    mode = ["反击","手动"]

    def setMode(self, mode):
        if mode == "反击":
            self.power2 *= self.preRatio

    def skillInfo(self, mode = None):
        pre = self.char.GetSkillByName("俯冲腹拳")
        data = pre.skillInfo()[0]
        self.data2 = [0]+[data]*self.maxLv
        self.hit2 = 1
        return super().skillInfo(mode)

# 破碎之锤
# priest_male/infighter/bb34e8854a93fd250347a1c64119f7ab
# f6a4ad30555b99b499c07835f87ce522/bb34e8854a93fd250347a1c64119f7ab
class Skill30(ActiveSkill):
    """
        [摆动]后快速向前并以强威力的一拳捶击前方敌人， 可以使命中的敌人撞上地面后弹至空中。\n
        学习一定等级的[技巧精通]后， [俯冲]中也可以发出攻击。
    """
    name = "破碎之锤"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 6
    mp = [45, 462]
    uuid = "bb34e8854a93fd250347a1c64119f7ab"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 浮空力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 冲击波攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [学习绝对正义后]
    # 攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 浮空力比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 神圣之力爆炸攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 冲击波范围 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

# 幻影化身
# priest_male/infighter/27bade584bb42fef68148d3a0b72bace
# f6a4ad30555b99b499c07835f87ce522/27bade584bb42fef68148d3a0b72bace
class Skill31(ActiveSkill):
    """
        生成自身的影子分身并使其对已攻击的敌人进行追击。\n
        只能在[意念驱动]已施放状态下使用， 若发动中收回巨兵， 则会终止技能效果。\n
        使用该技能时， 无法强制中断当前进行的普通攻击动作。
    """
    name = "幻影化身"
    learnLv = 35
    masterLv = 10
    maxLv = 20
    position = 7
    rangeLv = 3
    cd = 5
    uuid = "27bade584bb42fef68148d3a0b72bace"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力比率 : 打击量的{value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 刺拳猛击
# priest_male/infighter/c7bf7ccab413009640e65ca6f2f0263a
# f6a4ad30555b99b499c07835f87ce522/c7bf7ccab413009640e65ca6f2f0263a
class Skill32(ActiveSkill):
    """
        用极快的刺拳给予敌人多次伤害， 最后再用锤击攻击前面的敌人。\n
        连按攻击键就可以更快更多地发出刺拳。\n
        在最后锤击后按攻击键， 可以发动一次追加攻击。\n
        只能在[意念驱动]已施放的状态下使用。
    """
    name = "刺拳猛击"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 10
    mp = [50, 546]
    uuid = "c7bf7ccab413009640e65ca6f2f0263a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 刺拳连击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 15
    # 最后锤击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 追击攻击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 连击攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [刺拳猛击]\n
        以肉眼看不见的速度发动爆闪刺拳， 对大范围敌人造成伤害\n
        - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [刺拳猛击]\n
        施放过程中所受伤害 -70%\n
        删除最后锤击、 追击攻击\n
        - 总攻击力相同\n
        固定以最大连击次数发动\n
        利用[干涸之泉]强制中断并连接神击系技能时， 立即恢复[干涸之泉]能量
        """
        ...

# 旋涡重拳
# priest_male/infighter/aa6dd52e1c925d87cdc0ca340056c543
# f6a4ad30555b99b499c07835f87ce522/aa6dd52e1c925d87cdc0ca340056c543
class Skill33(ActiveSkill):
    """
        快速旋转手臂吸附并控制周围敌人， 造成多段伤害， 最后发动强力拳击。\n
        只能在[意念驱动]已施放的状态下使用。\n
        可以在[俯冲]和[摆动]中使用。 \n
        在决斗场中不发动霸体护甲， 减少吸附敌人的力量和范围。
    """
    name = "旋涡重拳"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [158, 1327]
    uuid = "aa6dd52e1c925d87cdc0ca340056c543"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 旋转多段攻击力 : {value0}% x {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 10
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 吸附x轴范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 吸附y轴范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [旋涡重拳]\n
        旋转多段攻击时生成飓风， 删除最后一击\n
        - 飓风持续3秒， 并吸附周围的敌人造成多段伤害\n
        - 飓风多段攻击次数 : 10次\n
        - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [旋涡重拳]\n
        在手上汇聚力量后猛击敌人\n
        - 直拳多段攻击次数 : 10次\n
        - 总攻击力相同\n
        删除控制和聚集敌人的功能\n
        按向前方键施放时前进并发动直拳攻击\n
        可强制中断直拳攻击后僵直并施放[俯冲]、 [摆动] 
        """
        ...

# 神圣组合拳
# priest_male/infighter/38612d8f2561edc2eb68d5057a837bfa
# f6a4ad30555b99b499c07835f87ce522/38612d8f2561edc2eb68d5057a837bfa
class Skill34(ActiveSkill):
    """
        先用左右摆拳攻击敌人， 最后用强威力的直拳给予敌人猛烈一击。\n
        直拳攻击后， 可以立即连接[俯冲]、 [摆动]。\n
        只能在已施放[意念驱动]的状态下使用。
    """
    name = "神圣组合拳"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cube = 1
    cd = 16
    mp = [150, 1260]
    uuid = "38612d8f2561edc2eb68d5057a837bfa"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 第3击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 范围: {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [神圣组合拳]\n
        攻击速度 +15%\n
        在可施放[圣拳连击]的状态下， 由[幻影化身]的分身施放[圣拳连击]\n
        在[幻影化身]状态下施放技能过程中， 利用[干涸之泉]强制中断技能时， 会留下分身继续施放技能
        """
        ...

    def vp_2(self):
        """
        [神圣组合拳]\n
        第1击、 第2击攻击范围增加， 删除第3击\n
        - 总攻击力相同\n
        按前方向键时， 向前方移动攻击\n
        按上/下方向键时， 向该对角线方向滑行并攻击
        """
        ...

# 极速飓风拳
# priest_male/infighter/717f1e2104fe4b796f800352fa143ecc
# f6a4ad30555b99b499c07835f87ce522/717f1e2104fe4b796f800352fa143ecc
class Skill35(ActiveSkill):
    """
        生成飓风圈吸附周围敌人并用连续的左右摆拳快速攻击敌人， 最后的强威力上勾拳可以将敌人击飞。\n
        施放技能时可前后移动。 若施放后连续按攻击键， 则可以更快的攻击敌人。\n
        攻击中可以前后移动， 且连续按攻击键可以延长技能的持续时间， 但只能在[意念驱动]已施放状态下使用。\n
        决斗场中无法使用[干涸之泉]强制中断， 且按跳跃键无法立即发动最后一击。
    """
    name = "极速飓风拳"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [311, 2612]
    uuid = "717f1e2104fe4b796f800352fa143ecc"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 摆拳攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 10
    # 摆拳攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 上勾拳攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 吸附范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [极速飓风拳]\n
        删除上勾拳， 摆拳攻击次数 -4次\n
        - 总攻击力相同\n
        摆拳攻击速度 +25%\n
        吸附力、 速度 +30%\n
        攻击中移动速度 +100%\n
        连按技能键时， 不增加攻击速度\n
        变更为可填充3次的技能\n
        - 每次填充冷却时间 : 15秒\n
        - 单次攻击力 -66%
        """
        ...

    def vp_2(self):
        """
        [极速飓风拳]\n
        施放技能时进入无敌状态\n
        攻击敌人3次后， 发动强力上勾拳生成飓风\n
        - 总攻击力相同
        """
        ...

# 双重幻影
# priest_male/infighter/04883563896fe1adac7505c6146b5f59
# f6a4ad30555b99b499c07835f87ce522/04883563896fe1adac7505c6146b5f59
class Skill36(PassiveSkill):
    """
        增加[幻影化身]的分身数量， 但分身的攻击力将会低于该技能原有分身的攻击力。
    """
    name = "双重幻影"
    learnLv = 45
    masterLv = 1
    maxLv = 1
    position = 7
    rangeLv = 1
    uuid = "04883563896fe1adac7505c6146b5f59"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力比率 : [幻影化身]的{value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 分身数增加量 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # TODO

# 干涸之泉
# priest_male/infighter/b8f4966608e4ebb3cc80ba4eac3649bb
# f6a4ad30555b99b499c07835f87ce522/b8f4966608e4ebb3cc80ba4eac3649bb
class Skill37(PassiveSkill):
    """
        学习此技能后， 对敌人的攻击力增加， 且可强制中断当前技能并施放神击系技能。
    """
    name = "干涸之泉"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    cd = 3.5
    uuid = "b8f4966608e4ebb3cc80ba4eac3649bb"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

    associate = [{"data":data0}]

# 泯灭神击
# priest_male/infighter/dbf8b30c7057032af0d68fcfa289fdae
# f6a4ad30555b99b499c07835f87ce522/dbf8b30c7057032af0d68fcfa289fdae
class Skill38(ActiveSkill):
    """
        聚集强大力量向前方敌人发出3次攻击， 最后以极具威力的直拳击飞敌人。 最后一击可以蓄气。\n
        只能在[意念驱动]已施放的状态下使用。
    """
    name = "泯灭神击"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [800, 6720]
    uuid = "dbf8b30c7057032af0d68fcfa289fdae"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 第3击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 第4击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 使用[幻影化身]时攻击力增加倍率 : {value4}倍
    data4 = get_data(f'{prefix}/{uuid}', 4)

    skillDamage = 1.1

# 破碎之拳
# priest_male/infighter/e0daa922b19cdc35de879e938361464e
# f6a4ad30555b99b499c07835f87ce522/e0daa922b19cdc35de879e938361464e
class Skill39(ActiveSkill):
    """
        使用双手快速攻击前方的多个敌人， 最后强力下勾拳攻击敌人。 若施放后连续按攻击键， 则可以更快地攻击敌人。\n
        连击过程中按跳跃键可以立即施放最后一击。\n
        只能在[意念驱动]已施放状态下使用。
    """
    name = "破碎之拳"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 2
    cd = 35
    mp = [350, 680]
    uuid = "e0daa922b19cdc35de879e938361464e"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 连续攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 10
    # 最后下勾拳攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 连续攻击次数 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [破碎之拳]\n
        连击次数固定为5次\n
        - 总攻击力相同\n
        连击和终结攻击时发生神圣爆炸\n
        - 爆炸攻击力与连击和终结攻击力相同\n
        - 直接命中的敌人不会被爆炸攻击 
        """
        ...

    def vp_2(self):
        """
        [破碎之拳]\n
        施放过程中所受伤害 -70%\n
        连击次数增加5次， 删除最后一击和爆炸\n
        - 总攻击力相同\n
        始终以最大攻击次数和攻击速度发动\n
        命中时， 初始化[刺拳猛击]的冷却时间\n
        - [刺拳猛击]攻击力 -28.5%\n
        利用[干涸之泉]强制中断并连接神击系技能时， 立即恢复[干涸之泉]能量
        """
        ...

    def effect(self, old, new):
        if self.vp == 2:
            self.associate = [{"data":[0]+[-28.5]*self.maxLv,"skills":["刺拳猛击"]}]
        return super().effect(old, new)

# 破坏之拳
# priest_male/infighter/0fbb8de70002ad34f046c94c2cb3e863
# f6a4ad30555b99b499c07835f87ce522/0fbb8de70002ad34f046c94c2cb3e863
class Skill40(ActiveSkill):
    """
        向上发出强力一拳。 可在[俯冲]和[摆动]中使用。 \n
    攻击敌人时会发生冲击波浮空敌人。\n
        只能在[意念驱动]已施放状态下使用。
    """
    name = "破坏之拳"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 8
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [350, 2700]
    uuid = "0fbb8de70002ad34f046c94c2cb3e863"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 冲击波范围 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [破坏之拳]\n
        在以角色为圆心的600px范围内， 追踪并攻击最强敌人\n
        摆拳命中后产生冲击波， 通过[干涸之泉]强制中断时也会产生冲击波\n
        冲击波大小 +50%
        """
        ...

    def vp_2(self):
        """
        [破坏之拳]\n
        发动速度 +50%\n
        攻击时不生成冲击波\n
        - 总攻击力相同\n
        施放过程中， 可以强制中断技能并施放[仲裁怒击]、 [超重拳]， 且不消耗[干涸之泉]能量
        """
        ...

# 仲裁怒击
# priest_male/infighter/9bc30e0f6e22b0333762d04acae7d252
# f6a4ad30555b99b499c07835f87ce522/9bc30e0f6e22b0333762d04acae7d252
class Skill41(ActiveSkill):
    """
        向前方发出强力一击， 给敌人造成致命伤害。 若命中敌人， 则会产生冲击波并对后排的敌人造成伤害。\n
        仅能在[意念驱动]已施放状态下使用。
    """
    name = "仲裁怒击"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "9bc30e0f6e22b0333762d04acae7d252"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 冲击波大小、 吸附范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [仲裁怒击]\n
        攻击前僵直 -50%\n
        - 基本冷却时间变更为20秒\n
        - 总攻击力 -50%\n
        未命中时冷却时间变更为3秒\n
        成功命中时， 可用[俯冲]或[摆动]强制中断技能施放后僵直
        """
        self.skillRation *= 1 - 0.5
        self.cd = 20
        ...

    def vp_2(self):
        """
        [仲裁怒击]\n
        施放时， [幻影化身]被蓝拳使者吸收， 并将全部力量集中于拳头吸附周围敌人后进行打击， 造成巨大伤害\n
        - 基本冷却时间变更为60秒\n
        - 总攻击力 +50%
        """
        self.cd = 60
        self.skillRation *= 1 + 0.5
        ...

# 正义惩戒
# priest_male/infighter/087d1068ff506d090710566608a17760
# f6a4ad30555b99b499c07835f87ce522/087d1068ff506d090710566608a17760
class Skill42(PassiveSkill):
    """
        为了实现正义， 将身体锻炼到极致， 可以增加命中率、 基本攻击力和技能攻击力。
    """
    name = "正义惩戒"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 3
    uuid = "087d1068ff506d090710566608a17760"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 命中率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [{"data":data0}]

# 超重拳
# priest_male/infighter/d204ec03a0aed2f20211fb6ccc48d46d
# f6a4ad30555b99b499c07835f87ce522/d204ec03a0aed2f20211fb6ccc48d46d
class Skill43(ActiveSkill):
    """
        使用上勾拳使敌人浮空， 并且几乎在同一时间用拳头猛烈向下捶击， 对敌人造成巨大的伤害。\n
        [俯冲]、 [摆动]施放途中也能使用。\n
        只有在施放[意念驱动]的状态下才能使用。
    """
    name = "超重拳"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 5
    cd = 50
    mp = [800, 6000]
    uuid = "d204ec03a0aed2f20211fb6ccc48d46d"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 范围: {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [超重拳]\n
        第2击命中时引发强力冲击波， 使命中的敌人进入强制控制状态5秒\n
        - 冲击波攻击力与第2击相同\n
        - 直接命中的敌人不受冲击波伤害\n
        利用[干涸之泉]强制中断并施放[超重拳]时， 立即发动第2击 
        """
        ...

    def vp_2(self):
        """
        [超重拳]\n
        施放时， 将圣物插入地面， 引爆神圣力对周围敌人造成伤害并形成圣拳领域\n
        进入圣拳领域的敌人会受到多段攻击伤害\n
        - 圣拳领域多段攻击次数 : 25次\n
        - 总攻击力相同\n
        圣拳领域持续10秒， 领域内的蓝拳使者技能得到强化\n
        [技能强化效果]\n
        [急速闪避] - 增益持续时间变更为15秒\n
        [干涸之泉] - 能量恢复时间 -50% 
        """
        ...

# 制裁 : 怒火疾风
# priest_male/infighter/0f638da961acf7958ac6070b7aaed013
# f6a4ad30555b99b499c07835f87ce522/0f638da961acf7958ac6070b7aaed013
class Skill44(ActiveSkill):
    """
        用令人眼花缭乱的步伐快速移动并连续攻击周围敌人后， 发动强力最后一击。\n
        学习[干涸之泉]后， 可以中断其他技能使用[制裁 : 怒火疾风]， 但无法中断[制裁 : 怒火疾风]并施放其它技能。\n
        只能在已施放[意念驱动]的状态下使用。
    """
    name = "制裁 : 怒火疾风"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "0f638da961acf7958ac6070b7aaed013"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击半径 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 连续攻击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 19
    # 连续攻击次数 : 19次
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 2
    # 最后一击的直接攻击次数 : 2次
    # 最后一击的爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 绝对正义
# priest_male/infighter/515b442ffbf61a82371abb645c149a31
# f6a4ad30555b99b499c07835f87ce522/515b442ffbf61a82371abb645c149a31
class Skill45(PassiveSkill):
    """
        光启·蓝拳使者将信仰和信念传达给神， 领悟真正的正义。 被光之圣遗物所选择的光启·蓝拳使者， 获得实现绝对正义的压倒性力量。\n
       增加基本攻击力和转职技能攻击力， 变更部分技能。\n
    [俯冲腹拳]\n
    - 成功命中敌人时， 可取消施放后僵直连接[俯冲]、 [摆动]\n
    [破碎之锤]\n
    - 删除攻击敌人时产生的冲击波， 即使未攻击敌人， 捶地时也会插入巨兵， 发生神圣力爆炸
    """
    name = "绝对正义"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "515b442ffbf61a82371abb645c149a31"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]

# 正义铁拳
# priest_male/infighter/87a918bb22cfc959a16e0bf939bb6c24
# f6a4ad30555b99b499c07835f87ce522/87a918bb22cfc959a16e0bf939bb6c24
class Skill46(ActiveSkill):
    """
        将神圣之力注入拳头， 对敌人进行致命攻击使敌人浮空， 然后快速移动， 将周围的敌人聚集到一处后， 发动连续攻击。\n
        最后用强力勾拳击飞敌人。\n
    只能在[意念驱动]已施放状态下使用。
    """
    name = "正义铁拳"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [960, 7200]
    uuid = "87a918bb22cfc959a16e0bf939bb6c24"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 下捶冲击波攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 连续攻击攻击力 : {value1}% x {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 15
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最后勾拳攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1

# 正义执行 : 雷米迪奥斯的圣座
# priest_male/infighter/aa51c4ddf1659092fa9ed612b9837061
# f6a4ad30555b99b499c07835f87ce522/aa51c4ddf1659092fa9ed612b9837061
class Skill47(ActiveSkill):
    """
        释放光之圣遗物 : 雷米迪奥斯圣座的真正力量， 将周围净化为圣域。\n
        敌人在圣域内被强制拉到光启·蓝拳使者的前方， 双膝跪地忏悔罪行。\n
        光启·蓝拳使者在圣域中心的告解所祈祷， 会显现雷米迪奥斯圣座的真正形态——神圣拳铠。\n
        然后， 在神圣拳铠中注入神的意志并执行正义。\n
        只能在[意念驱动]已施放状态下使用。\n
        技能施放过程中无法利用[干涸之泉]强制中断并释放其他技能。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "正义执行 : 雷米迪奥斯的圣座"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4027, 8055]
    uuid = "aa51c4ddf1659092fa9ed612b9837061"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit2 = 1


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'infighter'
        self.nameCN = '神启·蓝拳圣使'
        self.role = 'priest_male'
        self.角色 = '圣职者(男)'
        self.职业 = '蓝拳圣使'
        self.jobId = 'f6a4ad30555b99b499c07835f87ce522'
        self.jobGrowId = '618326026de1a1f1cfba5dbd0b8396e7'

        self.武器选项 = ['图腾', '战斧', '镰刀', '念珠', '十字架']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '轻甲'
        self.buff = 2.088

        super().__init__(equVersion, __name__)
