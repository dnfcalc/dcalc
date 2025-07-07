#986c2b3d72ee0e4a0b7fcfbe786d4e02
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "gunblader/specialist/cn/skillDetail"

# 源能提炼
# gunblader/specialist/c77a417c43de80c4ce32c1ed405d174a
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/c77a417c43de80c4ce32c1ed405d174a
class Skill2(PassiveSkill):
    """
    利用[源能提炼]可以强化部分技能， 攻击时可以补充[源能提炼]能量槽。\n
    - [源能提炼]可增加范围的技能 -\n
    [源能护盾]、 [源能波刃]、 [引力源光弹]\n
    - [源能提炼]可增加控制时间的技能 -\n
    [镭射源能枪]、 [电磁领域]、 [超能场域]、 [能量禁锢]\n
    - 使用[源能提炼]后追加操作消失的技能 - \n
    [临界源能弹]
    """
    name = "源能提炼"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 2 #TODO
    rangeLv = 2
    uuid = "c77a417c43de80c4ce32c1ed405d174a"
    hasVP = False
    hasUP = False

    # [源能提炼]累积数上限 : {value0}个
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [源能提炼]基本累积数 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # - [各技能能量值获得量] -
    # 基本攻击 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 前冲攻击 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 跳跃攻击 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [源光斩] : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [源能护盾] : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [旋转源能波] : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [镭射源能枪] : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [源能波刃] : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [能量飞鱼弹] : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # [脉冲斩] : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # [电磁领域] : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # [引力源光弹] : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # [光裂斩] : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # [光导裂地斩] : {value15}%
    data15 = get_data(f'{prefix}/{uuid}', 15)
    # [超能场域] : {value16}%
    data16 = get_data(f'{prefix}/{uuid}', 16)
    # [能量禁锢] : {value17}%
    data17 = get_data(f'{prefix}/{uuid}', 17)
    # [离散能量波] : {value18}%
    data18 = get_data(f'{prefix}/{uuid}', 18)
    # [临界源能弹] : {value19}%
    data19 = get_data(f'{prefix}/{uuid}', 19)
    # [源能场域 : 黑暗边缘] : {value20}%
    data20 = get_data(f'{prefix}/{uuid}', 20)


# 基础精通
# gunblader/specialist/5a56514f35cf0270ae8d6c65f8fefd78
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/5a56514f35cf0270ae8d6c65f8fefd78
class Skill4(PassiveSkill):
    """
    增加基本攻击、 前冲攻击、 跳跃攻击和[弦月斩]的攻击力。\n
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


# 瞬击
# gunblader/specialist/4b2c90ec226fd40e967875aa5eabefb2
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/4b2c90ec226fd40e967875aa5eabefb2
class Skill9(ActiveSkill):
    """
    挥舞枪身击打敌人后颈， 把击中的敌人拖到自己身前， 最后挥剑斩击拉过来的敌人。\n
    对无法抓取的敌人不适用控制效果。
    """
    name = "瞬击"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 6
    mp = [1, 100]
    uuid = "4b2c90ec226fd40e967875aa5eabefb2"
    hasVP = False
    hasUP = False

    # 挥舞枪身攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1


# 源光斩
# gunblader/specialist/1803b6a67047cafb9e289b4f33cc507b
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/1803b6a67047cafb9e289b4f33cc507b
class Skill11(ActiveSkill):
    """
    用源能动力源向剑注入能量后， 向前发动斩击。 斩击后， 能量残留一定时间， 对敌人造成多段伤害。\n
    - [转职为源能专家时] -\n
    装备源力剑时， 无需注入源能直接发动斩击。
    """
    name = "源光斩"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 5
    mp = [16, 161]
    uuid = "1803b6a67047cafb9e289b4f33cc507b"
    hasVP = False
    hasUP = False

    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 能量多段攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 4
    # 多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 迅步突袭
# gunblader/specialist/9dda3f4a849dba1a288dd65e116860f2
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/9dda3f4a849dba1a288dd65e116860f2
class Skill14(ActiveSkill):
    """
    快速向前方敌人突进。\n
    施放过程中， 再次按技能键、 Z (技能) 键或X (攻击) 键， 可以发动追加攻击。
    """
    name = "迅步突袭"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 6
    mp = [12, 500]
    uuid = "9dda3f4a849dba1a288dd65e116860f2"
    hasVP = False
    hasUP = True

    # 追加攻击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1

# 源能护盾
# gunblader/specialist/0232c151ef3731c2dede51931a374723
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/0232c151ef3731c2dede51931a374723
class Skill15(ActiveSkill):
    """
    向前方投掷源能动力源， 形成可阻挡敌人远距离攻击的护盾。 (无法阻挡穿透攻击)\n
    我方可穿过该护盾， 但是敌方不能。\n
    护盾的生命值降为0或者经过一定时间后自动爆炸。 再次按技能键可以手动引爆。 投掷动力源时， 按向前方向键则可扔出更远的距离。\n
    [转职为源能专家后]\n
    冷却时间缩短2秒， 可以发动[源能提炼]。\n
    [源能提炼]使用方法 : 按住技能键一定时间即可发动。\n
    [源能提炼]发动效果 : 增加护盾大小、 爆炸范围、 持续时间和生命值。\n
    在决斗场中， 被攻击和使用[受身蹲伏]时无法手动引爆。
    """
    name = "源能护盾"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cd = 10
    mp = [23, 241]
    uuid = "0232c151ef3731c2dede51931a374723"
    hasVP = False
    hasUP = True

    # 护盾生命值 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 护盾持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 护盾爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # - 发动[源能提炼]时 -
    # 护盾大小和爆炸范围增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 护盾持续时间增加 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 护盾生命值增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [源能提炼]叠加数消耗量 : {value6}个
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 蓄气动作持续时间上限 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [范围信息]
    # 护盾大小比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 爆炸范围比率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)

# 旋转源能波
# gunblader/specialist/0b8db1e10b3abbd24d38564e708675d5
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/0b8db1e10b3abbd24d38564e708675d5
class Skill16(ActiveSkill):
    """
    在前方形成源能波， 然后使力将其旋转掷出。
    """
    name = "旋转源能波"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 5
    mp = [23, 241]
    uuid = "0b8db1e10b3abbd24d38564e708675d5"
    hasVP = False
    hasUP = True

    # 源能波生成攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 源能波旋转攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 4
    # 旋转多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 源能波移动距离 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 源力剑精通
# gunblader/specialist/ecc23c980ea71450c0ad0c3fd232f329
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/ecc23c980ea71450c0ad0c3fd232f329
class Skill17(PassiveSkill):
    """
    增加魔法攻击力。 装备源力剑时， 增加命中率和攻击速度。\n
    在决斗场中， 不增加攻击速度。
    """
    name = "源力剑精通"
    learnLv = 20
    masterLv = 20
    maxLv = 30
    position = 0 #TODO
    rangeLv = 3
    uuid = "ecc23c980ea71450c0ad0c3fd232f329"
    hasVP = False
    hasUP = False

    # 魔法攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 命中率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [ {"type":"$*PAtkM","data":data0}, ]

# 镭射源能枪
# gunblader/specialist/852f8ad797db4dca1405cb3e77198401
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/852f8ad797db4dca1405cb3e77198401
class Skill18(ActiveSkill):
    """
    用源能枪发射能量攻击敌人。 命中时， 能量会扩散到命中目标周围并同时攻击附近的敌人。 一定时间后， 镭射源能枪断开连接， 以首次击中的敌人为中心发生爆炸。\n
    若范围内没有敌人， 则镭射源能枪连接失败。\n
    - [源能提炼] -\n
    [源能提炼]使用方法 : 再次按技能键或Z键\n
    (可在[镭射源能枪]连接的状态下发动)\n
    [源能提炼]发动效果 : 增加爆炸攻击的强制控制时间。
    """
    name = "镭射源能枪"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 8 #TODO
    rangeLv = 2
    cd = 8
    mp = [36, 378]
    uuid = "852f8ad797db4dca1405cb3e77198401"
    hasVP = False
    hasUP = True

    # 能量多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2
    # 多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 镭射源能枪连接持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 爆炸强制控制时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # - [源能提炼]效果 -
    # 爆炸强制控制时间增加量 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [源能提炼]累积数消耗量 : {value6}个
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 范围比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

# 源能屏障
# gunblader/specialist/8b08f9504167a9c0f3a1d29d71b7943e
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/8b08f9504167a9c0f3a1d29d71b7943e
class Skill19(ActiveSkill):
    """
    瞬间在周围展开源能， 形成屏障。 短时间内进入无敌状态。\n
    该技能可以在除被攻击状态以外的所有状态下使用。
    """
    name = "源能屏障"
    learnLv = 20
    masterLv = 1
    maxLv = 1
    position = 7 #TODO
    rangeLv = 3
    cd = 15
    mp = [74, 74]
    uuid = "8b08f9504167a9c0f3a1d29d71b7943e"
    hasVP = False
    hasUP = False

    # 屏障持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)


# 细胞弱化
# gunblader/specialist/dcb31a63ef58954f44ff2070c42a9a98
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/dcb31a63ef58954f44ff2070c42a9a98
class Skill21(PassiveSkill):
    """
    攻击时， 释放源能弱化敌人， 造成更大伤害。\n
    增加源能专家的基本攻击力和技能攻击力。
    """
    name = "细胞弱化"
    learnLv = 25
    masterLv = 1
    maxLv = 11
    position = 0 #TODO
    rangeLv = 3
    uuid = "dcb31a63ef58954f44ff2070c42a9a98"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

    associate = [ {"data":data0,"type":"*skillRation"}]

# 源能波刃
# gunblader/specialist/8572675ec6a1f50b6eff6a867376c2de
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/8572675ec6a1f50b6eff6a867376c2de
class Skill22(ActiveSkill):
    """
    斩向前方并释放源能， 然后收回释放的能量， 同时吸附敌人。\n
    - [源能提炼] -\n
    [源能提炼]使用方法 : 施放技能时， 按住技能键一定时间。\n
    ([源能提炼]累积数为0时无法蓄气)\n
    [源能提炼]发动效果 : 增加攻击范围、 吸附范围和速度。
    """
    name = "源能波刃"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 7.5
    mp = [55, 396]
    uuid = "8572675ec6a1f50b6eff6a867376c2de"
    hasVP = False
    hasUP = True

    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 吸附攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # - [源能提炼]效果 -
    # 范围增加率 : 20%
    # [源能提炼]累积数消耗量 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 蓄气动作持续时间上限 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 能量飞鱼弹
# gunblader/specialist/4f2e001e9a19eb7bae50ad1840dfb329
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/4f2e001e9a19eb7bae50ad1840dfb329
class Skill23(ActiveSkill):
    """
    对所持的枪注入源能， 向前方发射威力强大的能量炸弹。
    """
    name = "能量飞鱼弹"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 8 #TODO
    rangeLv = 2
    cd = 6.5
    mp = [52, 369]
    uuid = "4f2e001e9a19eb7bae50ad1840dfb329"
    hasVP = False
    hasUP = True

    # 炸弹攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 脉冲斩
# gunblader/specialist/b8f4966608e4ebb3cc80ba4eac3649bb
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/b8f4966608e4ebb3cc80ba4eac3649bb
class Skill24(ActiveSkill):
    """
    击打地面之后释放源能， 形成能量脉冲， 对敌人造成多段伤害。
    """
    name = "脉冲斩"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 8
    mp = [67, 475]
    uuid = "b8f4966608e4ebb3cc80ba4eac3649bb"
    hasVP = False
    hasUP = True

    # 多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 多段攻击次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 能量脉冲生成数量 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 源能应用
# gunblader/specialist/d53301bb328baf12a3ae482cc6a565dd
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/d53301bb328baf12a3ae482cc6a565dd
class Skill25(ActiveSkill):
    """
    提升源能的应用能力， 增加魔法暴击伤害和魔法暴击率， 并增加物理/魔法防御力。
    """
    name = "源能应用"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 1 #TODO
    rangeLv = 3
    cd = 5
    uuid = "d53301bb328baf12a3ae482cc6a565dd"
    hasVP = False
    hasUP = False

    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法暴击伤害增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 魔法暴击率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 物理防御力增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 魔法防御力增加 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 引力源光弹
# gunblader/specialist/dbf8b30c7057032af0d68fcfa289fdae
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/dbf8b30c7057032af0d68fcfa289fdae
class Skill26(ActiveSkill):
    """
    汇聚手枪的源能， 发射可吸附敌人的引力源光弹。 引力源光弹在一定时间内造成多段伤害后爆炸。\n
    射击时， 按向前方向键可以发射更远的距离。\n
    - [源能提炼] -\n
    [源能提炼]使用方法 : 按住技能键一定时间即可发动。\n
    ([源能提炼]累积数为0时无法蓄气)\n
    [源能提炼]发动效果 : 增加攻击范围和吸附敌人的范围。
    """
    name = "引力源光弹"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 8 #TODO
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [145, 1218]
    uuid = "dbf8b30c7057032af0d68fcfa289fdae"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 8
    # 多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 引力源光弹持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # - [源能提炼]效果 -
    # 吸附范围增加 : 40%
    # [源能提炼]累积数消耗量 : {value4}个
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 蓄气动作持续时间上限 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [引力源光弹]\n
        引力弹持续时间 -50%\n
         - 多段攻击间隔 -50%\n
        发射动作速度 +50%\n
        引力弹飞行时间 -60%\n
        基本冷却时间变更为21秒\n
        总攻击力 +40%
        """
        self.cd = 21
        self.skillRation *= 1.4

    def vp_2(self):
        """
        [引力源光弹]\n
        射出的引力弹向前方快速飞去， 吸附敌人\n
        范围 +50%\n
        吸附力 +200%
        """
        ...

# 电磁领域
# gunblader/specialist/5152480fdde81362575a488d4cec4af9
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/5152480fdde81362575a488d4cec4af9
class Skill27(ActiveSkill):
    """
    把剑插入地面释放源能， 一定时间内对周围敌人造成多段伤害， 并引发小型爆炸。 多段攻击和爆炸攻击能强控敌人。\n
    [源能提炼]\n
    [源能提炼]使用方法 : 再次按技能键或Z键\n
    (可在[电磁领域]施放过程中发动)\n
    [源能提炼]发动效果 : 增加爆炸的强制控制时间， 变更为设置型。
    """
    name = "电磁领域"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [145, 1218]
    uuid = "5152480fdde81362575a488d4cec4af9"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 能量释放强制控制时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 爆炸强制控制时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # - [源能提炼]效果 -
    # 爆炸强制控制时间增加 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [源能提炼]累积数消耗量 : {value6}个
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 范围比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    def vp_1(self):
        """
        [电磁领域]\n
        删除多段攻击， 立即发生爆炸\n
        变更为可填充2次的技能\n
         - 单次攻击力 -50%\n
         - 每次填充冷却时间 : 10秒\n
        [源能提炼]能量获得量 +50%\n
        [源能提炼]发动时控制时间增加量额外 +0.5秒
        """
        self.cd = 10
        self.skillRation *= 0.5

    def vp_2(self):
        """
        [电磁领域]\n
        删除爆炸攻击， 变更为能量释放， 不再强制控制敌人\n
        能量释放时间和多段攻击次数 +100%\n
         - 总攻击力相同\n
        处于能量释放领域内时赋予以下效果\n
         - 进入霸体状态\n
         - 所受伤害 -50%\n
        范围 +50%
        """
        ...

# 光裂斩
# gunblader/specialist/7e904ea3d2a9faa054604e55120a9268
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/7e904ea3d2a9faa054604e55120a9268
class Skill28(ActiveSkill):
    """
    释放源能形成能量长剑， 大力向前方挥斩。\n
    斩击后， 源能会残留一定时间， 对敌人造成多段伤害。\n
    蓄气动作可以持续一定时间。
    """
    name = "光裂斩"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [193, 1621]
    uuid = "7e904ea3d2a9faa054604e55120a9268"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 能量多段攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 5
    # 多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 蓄气动作持续时间上限 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [光裂斩]\n
        斩击准备时间 -50%\n
        删除能量多段攻击\n
         - 总攻击力相同\n
        蓄气动作持续时间上限 -0.5秒\n
        蓄气过程中进入无敌状态
        """
        ...

    def vp_2(self):
        """
        [光裂斩]\n
        将能量聚集到源力剑后大范围挥舞， 向前方发射能量剑气\n
         - 删除斩击攻击\n
         - 能量多段攻击次数减少为3次\n
         - 总攻击力相同\n
        长按技能键可以蓄气， 蓄气一定时间后可发动[源能提炼]\n
         - [源能提炼]层数消耗量 : 1\n
         - 能量剑气大小和射程 +30%
        """
        ...

# 光导裂地斩
# gunblader/specialist/2391a27457b5a8c6fa4b4670a91bdd11
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/2391a27457b5a8c6fa4b4670a91bdd11
class Skill29(ActiveSkill):
    """
    生成威力强大的源能剑， 向前方发动斩击劈开地面。 然后在地面下方继续释放剑的能量， 生成更强大的能量剑后向上挑击。\n
    可以强制中断向上挑击的僵直并立即施放转职技能。
    """
    name = "光导裂地斩"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [338, 2839]
    uuid = "2391a27457b5a8c6fa4b4670a91bdd11"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 下劈攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 上挑攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [光导裂地斩]\n
        下劈攻击过程中， 可以发动[脉冲斩]\n
        下劈准备时间 -20%\n
        上斩后僵直 -40%\n
        范围 +30%
        """
        ...

    def vp_2(self):
        """
        [光导裂地斩]\n
        施放后， 上斩前可以发动1个以下技能\n
         - 可发动技能 : [光裂斩]、 [离散能量波]、 [绝望圆舞]\n
        上斩时， 合算之前发动的技能的攻击力\n
        施放过程中所受伤害 -70%
        """
        ...

# 源能增幅
# gunblader/specialist/5892d1fa4462e561ac8f8d2c74892b0a
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/5892d1fa4462e561ac8f8d2c74892b0a
class Skill30(PassiveSkill):
    """
    提升源能动力源的性能， 增加[源能提炼]的累积数上限、 基本攻击力和技能的攻击力。
    """
    name = "源能增幅"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 3
    uuid = "5892d1fa4462e561ac8f8d2c74892b0a"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [源能提炼]累积数上限增加 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [ {"data":data0,"type":"*skillRation"}]

# 超能场域
# gunblader/specialist/fc458e449ee00b01dbf88d09aae65462
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/fc458e449ee00b01dbf88d09aae65462
class Skill31(ActiveSkill):
    """
    向地面释放源能， 形成超能场域。 源能使范围内敌人受到多段伤害， 一定时间后爆炸。\n
    - [源能提炼] -\n
    [源能提炼]使用方法 : 再次按技能键或Z键\n
    (可在场域持续期间发动)\n
    [源能提炼]发动效果 : 增加场域持续时间。 增加的持续时间内技能变更为设置型。
    """
    name = "超能场域"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [1129, 9483]
    uuid = "fc458e449ee00b01dbf88d09aae65462"
    hasVP = False
    hasUP = False

    # 能量多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 25
    # 能量多段攻击间隔 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 能量爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 领域持续时间 : 3秒
    # - [源能提炼]效果 -
    # 领域持续时间增加 : 1.5秒
    # [源能提炼]累积数消耗量 : {value3}个
    data3 = get_data(f'{prefix}/{uuid}', 3)

    mode = ['满','秒C']

    def setMode(self, mode):
        if mode == "满":
            self.hit0 = 25
            self.hit2 = 1
        elif mode == "秒C":
            self.hit0 = 14
            self.hit2 = 1

# 能量禁锢
# gunblader/specialist/1812a1ece67bb37b6b44b54766450064
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/1812a1ece67bb37b6b44b54766450064
class Skill32(ActiveSkill):
    """
    投掷源能动力源， 在前方生成禁锢敌人的柱子， 然后用枪注入能量。 柱子生成时， 将周围的敌人吸到柱子内， 吸收的能量对敌人造成多段伤害， 一定时间后爆炸。\n
    - [源能提炼] -\n
    [源能提炼]使用方法 : 再次按技能键或Z键\n
    (可在用枪注入能量之前发动)\n
    [源能提炼]发动效果 : 爆炸攻击追加强制控制功能
    """
    name = "能量禁锢"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [378, 1058]
    uuid = "1812a1ece67bb37b6b44b54766450064"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 14
    # 多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 柱子爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 柱子持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # - [源能提炼]效果 -
    # 爆炸攻击的强制控制时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [源能提炼]累积数消耗量 : {value5}个
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [能量禁锢]\n
        以精细计算的角度展开能量反射板后， 向准确位置发射核心能量弹\n
        能量弹在反射板之间弹跳， 攻击范围内的敌人， 最后从反射板弹开后落地并引发爆炸\n
         - 总攻击力相同\n
        发动[源能提炼]时施放速度增加\n
         - 施放速度 +20%\n
        删除强制控制功能
        """
        ...

    def vp_2(self):
        """
        [能量禁锢]\n
        投掷源动力生成能量柱后， 无需通过源能枪注入能量， 源动力自身发射能量进行多段攻击\n
         - 删除射击过程\n
        多段攻击命中的敌人会聚集到能量柱中心\n
        范围 +50%
        """
        ...

# 离散能量波
# gunblader/specialist/d89f26862e348a801b30bb9fd7125db5
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/d89f26862e348a801b30bb9fd7125db5
class Skill33(ActiveSkill):
    """
    在前方形成可以将能量分散的屏障， 一定时间内释放源能， 造成多段伤害， 最后引爆能量屏障。\n
    施放技能后， 可以强制中断并连接转职系列技能。
    """
    name = "离散能量波"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [776, 1629]
    uuid = "d89f26862e348a801b30bb9fd7125db5"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 能量释放多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 10
    # 能量释放多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 能量屏障爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [离散能量波]\n
        生成屏障后立即爆炸\n
         - 删除能量释放多段攻击\n
         - 爆炸多段攻击次数 : 3次\n
         - 总攻击力相同\n
        生成屏障时可以击退霸体状态的敌人
        """
        ...

    def vp_2(self):
        """
        [离散能量波]\n
        向前方空中投掷核心源动力后， 向核心源动力发射核心能量\n
        源动力将注入的核心能量向周围释放进行攻击， 注入能量一段时间后会超负荷并引发爆炸\n
         - 多段攻击次数 -50%\n
         - 总攻击力相同\n
        [源能提炼]能量增加量 +300%
        """
        ...

# 源力汇聚
# gunblader/specialist/2ba299855fc22192cba4f73db75e9d0e
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/2ba299855fc22192cba4f73db75e9d0e
class Skill34(PassiveSkill):
    """
    有效利用源能， 额外增加[源能提炼]的基本累积数量、 [源能提炼]能量获得量、 基本攻击力和技能攻击力以及[源能应用]的物理/魔法防御力增加量。
    """
    name = "源力汇聚"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 2 #TODO
    rangeLv = 3
    uuid = "2ba299855fc22192cba4f73db75e9d0e"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [源能提炼]基本累积数增加 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [源能提炼]能量获得量增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [源能应用]物理/魔法防御力额外增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)

    associate = [ {"data":data0,"type":"*skillRation"}]

# 绝望圆舞
# gunblader/specialist/2c9d9a36c8401bddff6cdb80fab8dc24
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/2c9d9a36c8401bddff6cdb80fab8dc24
class Skill35(ActiveSkill):
    """
    释放剑与枪的能量， 生成两柄源能长剑并发动乱舞攻击。\n
    第1击、 第4击、 第5击时同时挥舞两个源能剑发动2次攻击， 第6击时发动强有力的最终斩击。\n
    可以强制中断最终斩击的僵直并立即连接转职技能。
    """
    name = "绝望圆舞"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [642, 4975]
    uuid = "2c9d9a36c8401bddff6cdb80fab8dc24"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 乱舞攻击力 : {value0}% x{value1}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 8
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [绝望圆舞]\n
        每次攻击将吸附敌人至角色前方\n
        范围 +45%\n
        施放过程中所受伤害 -50%
        """
        ...

    def vp_2(self):
        """
        [绝望圆舞]\n
        可将乱舞第1击、 第2击以及后续连击分开使用\n
         - 施放时进行乱舞第1击、 第2击\n
         - 再次输入时进行乱舞第3击、 第4击及终结攻击\n
         - 再次输入可在首次施放后10秒内进行\n
         - 可以强制中断乱舞第2击的施放后僵直并施放转职技能\n
        施放速度 +40%
        """
        ...

# 聚能光幕
# gunblader/specialist/b89c9ab317bc0a443f6497b7cca2f6a8
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/b89c9ab317bc0a443f6497b7cca2f6a8
class Skill36(ActiveSkill):
    """
    向前方投掷可吸收源能的动力源装置——聚能光幕。 根据源能专家的多段攻击次数， 光幕以一定比例吸收源能， 攻击达到一定次数即可达到最大蓄气状态， 增加爆炸攻击力。\n
    再次按技能键或超过光幕的最大持续时间时， 光幕发生爆炸。
    """
    name = "聚能光幕"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [930, 6975]
    uuid = "b89c9ab317bc0a443f6497b7cca2f6a8"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 0
    # 最大蓄气时的爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 达到最大蓄气所需的多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 持续时间上限 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    mode = ['满蓄','不蓄']

    def setMode(self, mode):
        if mode == "满蓄":
            self.hit0 = 0
            self.hit1 = 1
        elif mode == "不蓄":
            self.hit0 = 1
            self.hit1 = 0

    def vp_1(self):
        """
        [聚能光幕]\n
        向前方一定范围内的最强敌人投掷核心源动力并附着在该敌人身上\n
         - 如果范围内没有敌人， 则投掷到半空中\n
        持续时间上限 +50%
        """
        ...

    def vp_2(self):
        """
        [聚能光幕]\n
        施放时， 如果[源能提炼]累积数在1以上， 自动消耗层数并发动以下效果\n
         - 多段攻击次数以100%充能状态发动\n
         - 持续时间上限 -75%\n
        范围 +30%
        """
        self.setMode("满蓄")

# 终焉 : 超世界崩坏
# gunblader/specialist/7cf17936a039b418660424125dc968d7
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/7cf17936a039b418660424125dc968d7
class Skill37(ActiveSkill):
    """
    释放剑与枪中的源能， 在前方形成威力强大的能量球并将其引爆。 能量球在形成期间吸附周围的敌人， 在即将爆发时开始压缩， 并强制控制敌人。 (靠近球体的敌人也会被瞬间压缩。)\n
    形成能量球时， [源能提炼]能量值与累积数暴涨， 爆炸后恢复正常。\n
    经过一定时间后， 凝缩出爆炸所需的最低限度的能量， 此时可以利用跳跃键将其引爆。 (不按跳跃键时， 一定时间后将自动爆炸。)
    """
    name = "终焉 : 超世界崩坏"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2633, 5266]
    uuid = "7cf17936a039b418660424125dc968d7"
    hasVP = False
    hasUP = False

    # 多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 14
    # 多段攻击次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 手动爆炸最短时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 奇点源核
# gunblader/specialist/5806440d21e7546d50007a5ba11f8024
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/5806440d21e7546d50007a5ba11f8024
class Skill38(PassiveSkill):
    """
    苍暮·源能专家将源核与缩退炉结合， 改良为能产生爆炸性能量的奇点源核。\n
    额外增加[源能提炼]能量获得量； 增加基本攻击力和转职技能攻击力， 部分技能附加特殊效果。\n
    [镭射源能枪]\n
    镭射源能枪以锁链形式连接范围内的所有敌人， 爆炸变更为攻击单一目标。\n
    [源能波刃]\n
    攻击范围以角色为中心形成完整圆形， 动作全程适用霸体护甲。\n
    [……XXX年X月X日。 终于成功了。 经过数十次的失败， 才将超世界崩坏能量球的源能核心以稳定期状态留存下来……(中略)……因应用了缩退炉， 即超小型黑洞， 将其命名为“奇点源核”。]
    """
    name = "奇点源核"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "5806440d21e7546d50007a5ba11f8024"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [源能提炼]能量获得额外增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [ {"data":data0,"type":"*skillRation"}]

# 临界源能弹
# gunblader/specialist/d429147c372b549c3dadcabcba50787f
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/d429147c372b549c3dadcabcba50787f
class Skill39(ActiveSkill):
    """
    向上投掷特制的大型源能动力源。 投掷的源能动力源分离为多个小型源能动力源， 悬浮在周围。\n
    小型源能动力源经过一段时间达到临界点， 引发连锁爆炸。 在到达临界点之前再次按技能键， 可以强制引爆。\n
    - [源能提炼] -\n
    [源能提炼]使用方法 : 施放技能时， 按住技能键一定时间。\n
    ([源能提炼]累积数为0时无法蓄气)\n
    [源能提炼]发动效果 : 增加攻击范围和攻击力； 无需再次按技能键， 稍后一起爆炸。\n
    [……XXX年X月X日。 改良后的源能动力源不仅能自行生产能源， 同时还能吸收周围的物质， 将其转化为能量。 该持续反应存在时间阈值， 如果善加利用， 似乎可以作为定时炸弹使用……(中略)……如果设置好储存量的极限值， 就可以强制注入能量， 或在启动时就使其处于过载状态， 直接达到临界点。]
    """
    name = "临界源能弹"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [800, 6667]
    uuid = "d429147c372b549c3dadcabcba50787f"
    hasVP = False
    hasUP = False

    # 连锁爆炸多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 连锁爆炸多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 持续时间上限 : 10秒
    # - [源能提炼]效果 -
    # 同时爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 范围增加 : 10%
    # [源能提炼]累积数消耗量 : 1个
    # 蓄气动作持续时间上限 : 3秒

    mode = ["常规","能源"]

    def setMode(self, mode):
        if mode == "常规":
            self.hit0 = 5
            self.hit2 = 0
        elif mode == "能源":
            self.hit0 = 0
            self.hit2 = 1

# 源能场域 : 黑暗边缘
# gunblader/specialist/7ec521d063d2190e1fcc5bd229af9bcf
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/7ec521d063d2190e1fcc5bd229af9bcf
class Skill40(ActiveSkill):
    """
    移动到利用源能制造的特殊空间后， 取出源能枪的奇点源核， 安装在源力剑上。 然后， 通过2个奇点源核， 挥动可释放爆炸性能量的源力剑， 沿着地平线横向斩击。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。\n
    [……XXX年X月X日。 将两个启动状态的源核放在一起， 并没有像炸弹一样爆炸， 而是像巨型源核一样释放出能量， 其能量等同于数十个源核释放的总量。 不妨作出假设， 两个源核释放能量后不会立即扩散， 而是被另一个源核的引力所吸引， 聚合在一起， 最终释放超越限界的能量……如果能善加利用， 或可应用于实战。]
    """
    name = "源能场域 : 黑暗边缘"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "7ec521d063d2190e1fcc5bd229af9bcf"
    hasVP = False
    hasUP = False

    # 横斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1

class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'specialist'
        self.nameCN = '苍暮·源能专家'
        self.role = 'gunblader'
        self.角色 = '枪剑士'
        self.职业 = '源能专家'
        self.jobId = '986c2b3d72ee0e4a0b7fcfbe786d4e02'
        self.jobGrowId = 'c9b492038ee3ca8d27d7004cf58d59f3'

        self.武器选项 = ['长刀','小太刀','重剑','源力剑'] # TODO
        self.输出类型选项 = ['魔法百分比'] # TODO
        self.输出类型 = '魔法百分比' # TODO
        self.防具精通属性 = ['智力'] # TODO
        self.防具类型 = '布甲'
        self.buff = 2.00

        super().__init__(equVersion, __name__)
