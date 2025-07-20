#3deb7be5f01953ac8b1ecaa1e25e0420
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "demonic_lancer/impaler/cn/skillDetail"

# 基础精通
# demonic_lancer/impaler/5a56514f35cf0270ae8d6c65f8fefd78
# 3deb7be5f01953ac8b1ecaa1e25e0420/5a56514f35cf0270ae8d6c65f8fefd78
class Skill3(PassiveSkill):
    """
    增加基本攻击、 前冲攻击、 跳跃攻击、 [枪挑]的攻击力。\n
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
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 前冲攻击力变化率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 跳跃攻击力变化率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 魔枪发射
# demonic_lancer/impaler/51a08fd0c90f0a5276cd552047fac93d
# 3deb7be5f01953ac8b1ecaa1e25e0420/51a08fd0c90f0a5276cd552047fac93d
class Skill10(ActiveSkill):
    """
    将气息聚集到魔枪尖端， 然后投掷魔枪。\n
    魔法枪对命中的敌人造成多段伤害后消失。
    """
    name = "魔枪发射"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 4.5
    mp = [10, 115]
    uuid = "51a08fd0c90f0a5276cd552047fac93d"
    hasVP = False
    hasUP = False

    # 魔法枪多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 4
    # 魔法枪多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)



# 暗蚀
# demonic_lancer/impaler/d53301bb328baf12a3ae482cc6a565dd
# 3deb7be5f01953ac8b1ecaa1e25e0420/d53301bb328baf12a3ae482cc6a565dd
class Skill15(PassiveSkill):
    """
    暗枪士的身体被暴走的魔枪侵蚀， 增加属性攻击力， 可以使用黑暗气息和黑雷。\n
    - [黑暗气息] -\n
    部分凝聚黑暗气息的攻击可以腐蚀敌人的身体， 使敌人进入暗蚀状态， 行动变缓慢。\n
    - [黑雷] -\n
    部分凝聚黑雷的攻击命中暗蚀状态的敌人时， 会释放黑雷， 造成额外伤害。\n
    攻击非暗蚀状态的敌人时， 将伤害量的一部分积累在敌人体内， 增加敌人所受伤害， 当敌人进入暗蚀状态时， 之前蓄积的所有伤害一次性爆发。\n
    暗蚀状态的持续时间受相应技能的影响。
    """
    name = "暗蚀"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 7 #TODO
    rangeLv = 3
    uuid = "d53301bb328baf12a3ae482cc6a565dd"
    hasVP = False
    hasUP = False

    # 属性攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 黑雷技能额外攻击力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 黑雷技能累积攻击力比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 暗蚀状态持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [暗蚀减速效果]
    # 减速几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 减速持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 减速状态下敌人攻击速度和移动速度减少率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

    associate = [
        {"data":data0,"type":"*skillRation"},
        {"data":data1,"type":"*power0","skills":["双重投射"]},
        {"data":data1,"type":"*power0","skills":["暗矛投射"]},
        {"data":data1,"type":"*power0","skills":["绝望枪"]},
        {"data":data1,"type":"*power0","skills":["连锁侵蚀"]},
        {"data":data1,"type":"*power1","skills":["连锁侵蚀"]},
        {"data":data1,"type":"*power0","skills":["暗蚀螺旋枪"]},
        {"data":data1,"type":"*power2","skills":["暗蚀螺旋枪"]},
        {"data":data1,"type":"*power0","skills":["坠蚀之雨"]},
        {"data":data1,"type":"*power0","skills":["暗蚀爆雷杀"]},
        {"data":data1,"type":"*power1","skills":["暗蚀爆雷杀"]},
        {"data":data1,"type":"*power2","skills":["暗蚀爆雷杀"]},
        {"data":data1,"type":"*power2","skills":["无尽侵蚀 : 缚魂"]},
        {"data":data1,"type":"*power0","skills":["黑蚀酷刑"]},
        {"data":data1,"type":"*power1","skills":["黑蚀酷刑"]},
        {"data":data1,"type":"*power3","skills":["黑蚀酷刑"]},
        {"data":data1,"type":"*power0","skills":["冥夜裂空"]},
        {"data":data1,"type":"*power0","skills":["冥蚀脉冲"]},
        {"data":data1,"type":"*power1","skills":["冥蚀脉冲"]},
        {"data":data1,"type":"*power3","skills":["冥蚀脉冲"]},
        {"data":data1,"type":"*power1","skills":["幽影暗蚀 : 寂灭"]},
        {"data":data1,"type":"*power0","skills":["虚空碎灭"]},
        {"data":data1,"type":"*power1","skills":["虚空碎灭"]},
        {"data":data1,"type":"*power3","skills":["虚空碎灭"]},
        {"data":data1,"type":"*power2","skills":["暗·渊灭禁绝"]},
    ]


# 帝国枪术
# demonic_lancer/impaler/7e904ea3d2a9faa054604e55120a9268
# 3deb7be5f01953ac8b1ecaa1e25e0420/7e904ea3d2a9faa054604e55120a9268
class Skill16(PassiveSkill):
    """
    帝国广泛使用的枪术。\n
    基本攻击、 前冲攻击和跳跃攻击变更为暗枪士专用攻击。\n
    基本攻击第3击时， 将黑暗气息凝聚在枪中后投掷。\n
    凝聚黑暗气息的枪击中敌人时， 使敌人进入暗蚀状态。\n
    若在[后跳]时施放技能， 则向后跳跃并投掷魔枪； 投掷瞬间按向后方向键， 可以后退更远距离。\n
    [回旋钩]增加可以抓取多名敌人的功能， 并且可以强制中断部分技能并立即施放[回旋钩]。\n
    在决斗场中， 后跳投掷有冷却时间， 且投掷时按方向键不会增加移动距离。\n
    [可以强制中断的技能]\n
    [侵蚀之矛]、 [暗矛投射]、 [暗街夺命锁]、 [绝望枪]、 [连锁侵蚀]
    """
    name = "帝国枪术"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 8 #TODO
    rangeLv = 1
    uuid = "7e904ea3d2a9faa054604e55120a9268"
    hasVP = False
    hasUP = False


# 双重投射
# demonic_lancer/impaler/dbf8b30c7057032af0d68fcfa289fdae
# 3deb7be5f01953ac8b1ecaa1e25e0420/dbf8b30c7057032af0d68fcfa289fdae
class Skill17(ActiveSkill):
    """
    [黑雷系列]\n
    连续投掷两支注入黑雷的魔枪。 魔枪不会穿刺敌人， 而是在碰到敌人的瞬间造成伤害然后消失。\n
    若在[后跳]时施放技能， 则向后跳跃并连续投掷两支魔枪； 投掷瞬间按向后方向键， 可以后退更远距离。\n
    [暗蚀附加效果]\n
    枪会爆炸， 产生更大范围的伤害。\n
    在决斗场中， 后跳投掷时按方向键不会增加移动距离。
    """
    name = "双重投射"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 6
    mp = [30, 219]
    uuid = "dbf8b30c7057032af0d68fcfa289fdae"
    hasVP = False
    hasUP = True

    # [黑雷系列]
    # 投掷攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 2
    power0 = 1
    # 投掷次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # 爆炸范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 暗蚀爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

# 侵蚀之矛
# demonic_lancer/impaler/5152480fdde81362575a488d4cec4af9
# 3deb7be5f01953ac8b1ecaa1e25e0420/5152480fdde81362575a488d4cec4af9
class Skill18(ActiveSkill):
    """
    [暗蚀系列]\n
    生成黑暗之枪向前方投掷。\n
    被击中的敌人会进入暗蚀状态。\n
    若在[后跳]时施放技能， 则向后跳跃并投掷魔枪； 投掷瞬间按向后方向键， 可以后退更远距离。\n
    在决斗场中， 后跳投掷时按方向键不会增加移动距离。
    """
    name = "侵蚀之矛"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 1 #TODO
    rangeLv = 2
    cd = 5
    mp = [30, 219]
    uuid = "5152480fdde81362575a488d4cec4af9"
    hasVP = False
    hasUP = True

    # [暗蚀系列]
    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # [范围信息]
    # 爆炸范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 暗矛投射
# demonic_lancer/impaler/2391a27457b5a8c6fa4b4670a91bdd11
# 3deb7be5f01953ac8b1ecaa1e25e0420/2391a27457b5a8c6fa4b4670a91bdd11
class Skill19(ActiveSkill):
    """
    [黑雷系列]\n
    旋转黑雷， 将黑雷缠绕在魔枪上并向前方投掷。\n
    魔枪贯穿敌人， 造成多段攻击伤害。\n
    若在[后跳]时施放技能， 则向后跳跃并投掷魔枪； 投掷瞬间按向后方向键， 可以后退更远距离。\n
    [暗蚀附加效果]\n
    发生小型爆炸， 造成额外伤害。\n
    在决斗场中， 后跳投掷时按方向键不会增加移动距离。
    """
    name = "暗矛投射"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 7
    mp = [36, 262]
    uuid = "2391a27457b5a8c6fa4b4670a91bdd11"
    hasVP = False
    hasUP = True

    # [黑雷系列]
    # 投掷攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 4
    # 投掷多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # 魔枪范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 暗矛精通
# demonic_lancer/impaler/5892d1fa4462e561ac8f8d2c74892b0a
# 3deb7be5f01953ac8b1ecaa1e25e0420/5892d1fa4462e561ac8f8d2c74892b0a
class Skill20(PassiveSkill):
    """
    蚕食的黑暗之力与投掷枪术相结合， 增加魔法武器攻击力； 使用暗矛系武器时， 增加命中率。\n
    在决斗场中不增加命中率。
    """
    name = "暗矛精通"
    learnLv = 20
    masterLv = 20
    maxLv = 30
    position = 7 #TODO
    rangeLv = 3
    uuid = "5892d1fa4462e561ac8f8d2c74892b0a"
    hasVP = False
    hasUP = False

    # 暗矛魔法攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 命中增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    associate = [ {"type":"$*PAtkM","data":data0}, ]

# 暴击
# demonic_lancer/impaler/fc1262c19f3d0477ee8eda47b8db8696
# 3deb7be5f01953ac8b1ecaa1e25e0420/fc1262c19f3d0477ee8eda47b8db8696
class Skill21(PassiveSkill):
    """
    集中精神， 提升物理/魔法暴击率。
    """
    name = "暴击"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 5 #TODO
    rangeLv = 3
    uuid = "fc1262c19f3d0477ee8eda47b8db8696"
    hasVP = False
    hasUP = False

    # 物理/魔法暴击率增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)

# 黑暗化身
# demonic_lancer/impaler/fc458e449ee00b01dbf88d09aae65462
# 3deb7be5f01953ac8b1ecaa1e25e0420/fc458e449ee00b01dbf88d09aae65462
class Skill22(ActiveSkill):
    """
    吸收魔枪的气息， 强化自身， 增加魔法暴击伤害和魔法暴击率。
    """
    name = "黑暗化身"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 8 #TODO
    rangeLv = 3
    cd = 5
    uuid = "fc458e449ee00b01dbf88d09aae65462"
    hasVP = False
    hasUP = False

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 暴击伤害增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 魔法暴击率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 暗矛贯穿
# demonic_lancer/impaler/1812a1ece67bb37b6b44b54766450064
# 3deb7be5f01953ac8b1ecaa1e25e0420/1812a1ece67bb37b6b44b54766450064
class Skill23(ActiveSkill):
    """
    [黑雷系列]\n
    向前方投掷注入黑雷的魔枪。\n
    魔枪会贯穿并吸附路径上的敌人， 对敌人造成伤害。\n
    最后魔枪插入地面时产生冲击波， 并在一定时间内释放黑雷， 强控敌人。\n
    施放技能时按前方向键， 可以将魔枪投掷得更远； 投掷瞬间按向后方向键， 可以后退更远距离。\n
    若在[后跳]时施放技能， 则向后跳跃并投掷魔枪。\n
    [暗蚀附加效果]\n
    若前进的魔枪周围有暗蚀状态的敌人， 则魔枪会用黑雷连接敌人， 对敌人造成伤害。\n
    在决斗场中， 无法强制控制被魔枪击中的敌人， 且后跳投掷时按方向键不会增加移动距离。
    """
    name = "暗矛贯穿"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 8
    mp = [35, 350]
    uuid = "1812a1ece67bb37b6b44b54766450064"
    hasVP = False
    hasUP = True

    # [黑雷系列]
    # 魔枪贯穿攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 强制控制时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [范围信息]
    # 吸附敌人范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

# 黑暗枪雨
# demonic_lancer/impaler/d89f26862e348a801b30bb9fd7125db5
# 3deb7be5f01953ac8b1ecaa1e25e0420/d89f26862e348a801b30bb9fd7125db5
class Skill24(ActiveSkill):
    """
    [暗蚀系列]\n
    向前方投掷旋转的黑暗之枪。\n
    黑暗之枪飞出时向周围挥洒黑暗气息， 使敌人进入暗蚀状态。
    """
    name = "黑暗枪雨"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 12
    mp = [78, 708]
    uuid = "d89f26862e348a801b30bb9fd7125db5"
    hasVP = False
    hasUP = True

    # [暗蚀系列]
    # 黑暗之枪攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 8
    # 黑暗之枪多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # 黑暗之枪移动距离 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 黑蚀葬礼
# demonic_lancer/impaler/2ba299855fc22192cba4f73db75e9d0e
# 3deb7be5f01953ac8b1ecaa1e25e0420/2ba299855fc22192cba4f73db75e9d0e
class Skill25(ActiveSkill):
    """
    [暗蚀 + 黑雷系列]\n
    旋转并投掷黑暗之枪。 然后投掷注入黑雷的魔枪， 并引发爆炸。\n
    被黑暗之枪击中的敌人会进入暗蚀状态。\n
    若在[后跳]时施放技能， 则向后跳跃并投掷魔枪； 投掷瞬间按向后方向键， 可以后退更远距离。\n
    在决斗场中， 后跳投掷时按方向键不会增加移动距离。
    """
    name = "黑蚀葬礼"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 10
    mp = [72, 650]
    uuid = "2ba299855fc22192cba4f73db75e9d0e"
    hasVP = False
    hasUP = True

    #  [暗蚀 + 黑雷系列]
    # 黑暗之枪爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 黑雷枪爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # [范围信息]
    # 黑暗气息范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

# 绝望枪
# demonic_lancer/impaler/ac21c02567f04a92b54dd85c091d1e5a
# 3deb7be5f01953ac8b1ecaa1e25e0420/ac21c02567f04a92b54dd85c091d1e5a
class Skill26(ActiveSkill):
    """
    [黑雷系列]\n
    连续投掷注入黑雷的魔枪， 最后同时投掷多个魔枪， 对敌人造成伤害。\n
    魔枪不会穿刺敌人， 飞出一定距离后若未击中敌人， 则会直接消失。\n
    - [暗蚀附加效果] -\n
    枪会爆炸， 产生更大范围的伤害。
    """
    name = "绝望枪"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 8
    mp = [71, 745]
    uuid = "ac21c02567f04a92b54dd85c091d1e5a"
    hasVP = False
    hasUP = True

    # [黑雷系列]
    # 投掷魔枪攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 9
    # 投掷次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # 爆炸范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 暗枪突破
# demonic_lancer/impaler/f1fdc6c2482ecc510a2a9f04201ba125
# 3deb7be5f01953ac8b1ecaa1e25e0420/f1fdc6c2482ecc510a2a9f04201ba125
class Skill27(PassiveSkill):
    """
    使魔枪的力量暴走， 引出更强大的力量， 增加基本攻击力和技能攻击力。
    """
    name = "暗枪突破"
    learnLv = 30
    masterLv = 1
    maxLv = 11
    position = 0 #TODO
    rangeLv = 3
    uuid = "f1fdc6c2482ecc510a2a9f04201ba125"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)

    associate = [ {"type":"*skillRation","data":data0} ]

# 连锁侵蚀
# demonic_lancer/impaler/2c9d9a36c8401bddff6cdb80fab8dc24
# 3deb7be5f01953ac8b1ecaa1e25e0420/2c9d9a36c8401bddff6cdb80fab8dc24
class Skill28(ActiveSkill):
    """
    [黑雷系列]\n
    投掷浓缩黑雷的魔枪， 黑雷转移到敌人身上对敌人持续造成伤害， 并强控敌人。\n
    若魔枪未命中敌人， 直接插入地面， 则在一定时间内释放黑雷， 并强控敌人。\n
    若在[后跳]时施放技能， 则向后跳跃并投掷魔枪； 投掷瞬间按向后方向键， 可以后退更远距离。\n
    [暗蚀附加效果]\n
    (1) 敌人被强制控制期间， 暗蚀状态持续时间不减少。\n
    (2) 若周围有暗蚀状态的敌人， 则黑雷会转移到敌人身上并强控敌人。\n
    (3) 攻击被黑雷转移的敌人时， 伤害会累积。\n
    (4) 对直接攻击的敌人不会累积伤害； 若攻击的同时遭到敌人攻击， 也不会对该敌人累积伤害。\n
    (5) 技能结束时发生黑雷转移， 使敌人一次性受到所有积累的伤害量。\n
    在决斗场中， 后跳投掷时按方向键不会增加移动距离； 解除控制时， 敌人稍微浮空后倒地。
    """
    name = "连锁侵蚀"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [194, 1600]
    uuid = "2c9d9a36c8401bddff6cdb80fab8dc24"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # [黑雷系列]
    # 浓缩黑雷攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 黑雷持续攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 6
    # 黑雷持续攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 强制控制持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [范围信息]
    # 黑雷转移范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    def vp_1(self):
        """
        [连锁侵蚀]\n
        变更为暗蚀+黑雷系列技能， 施放时跳跃并投掷黑暗之枪与黑雷枪\n
         - 总攻击力相同\n
         - 被黑暗之枪命中的敌人会进入暗蚀状态\n
         - 施放时， 向前方700px范围内最强敌人投掷\n
         - 删除强制控制效果
        """
        ...

    def vp_2(self):
        """
        [连锁侵蚀]\n
        始终有黑雷枪插在地面上\n
         - 总攻击力相同\n
         - 插在地面的黑雷枪领域范围 +100%\n
         - 黑雷转移范围 +20%\n
        施放速度 +20%
        """
        ...

# 暗蚀螺旋枪
# demonic_lancer/impaler/b89c9ab317bc0a443f6497b7cca2f6a8
# 3deb7be5f01953ac8b1ecaa1e25e0420/b89c9ab317bc0a443f6497b7cca2f6a8
class Skill29(ActiveSkill):
    """
    [黑雷系列]\n
    向前方投掷缠绕着旋转黑雷的魔枪。\n
    魔枪在碰到敌人或地面的瞬间会快速旋转， 造成多段伤害后爆炸。\n
    击中暗蚀状态的敌人或旋转的魔枪诱发暗蚀状态时， 发生黑雷增幅。\n
    若在[后跳]时施放技能， 则向后跳跃并投掷魔枪； 投掷瞬间按向后方向键， 可以后退更远距离。\n
    [暗蚀附加效果]\n
    发生黑雷增幅的魔枪会吸附周围敌人， 并且爆炸时造成更大范围的伤害。 \n
    在决斗场中， 后跳投掷时按方向键不会增加移动距离。
    """
    name = "暗蚀螺旋枪"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cube = 1
    cd = 18
    mp = [185, 1526]
    uuid = "b89c9ab317bc0a443f6497b7cca2f6a8"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # [黑雷系列]
    # 魔枪旋转攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 20
    # 魔枪旋转多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 最后一击爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [暗蚀螺旋枪]\n
        以黑雷增幅的状态投掷魔枪\n
        魔枪大小 +50%\n
         - 吸附力 +50%\n
         - 吸附敌人范围 +50%
        """
        ...

    def vp_2(self):
        """
        [暗蚀螺旋枪]\n
        魔枪接触敌人的瞬间立即爆炸\n
         - 变更为单次攻击\n
         - 总攻击力相同\n
        [黑蚀酷刑]\n
        可以强制中断施放后僵直并施放[暗蚀螺旋枪]
        """
        ...

# 坠蚀之雨
# demonic_lancer/impaler/7cf17936a039b418660424125dc968d7
# 3deb7be5f01953ac8b1ecaa1e25e0420/7cf17936a039b418660424125dc968d7
class Skill30(ActiveSkill):
    """
    [黑雷系列]\n
    将黑雷凝聚于魔枪中， 然后向空中投掷。\n
    魔枪在空中分裂成无数支枪， 向地面坠落， 造成多段伤害。\n
    被落下的魔枪命中的敌人会聚集在打击中心。\n
    [暗蚀附加效果]\n
    发生小爆炸， 对敌人造成额外伤害。
    """
    name = "坠蚀之雨"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cube = 1
    cd = 22
    mp = [200, 1650]
    uuid = "7cf17936a039b418660424125dc968d7"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # [黑雷系列]
    # 魔枪落下攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 20
    # 魔枪落下次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # 魔枪落下范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    def vp_1(self):
        """
        [坠蚀之雨]\n
        落下的魔枪将持续存在， 在所有魔枪落下后立即爆炸\n
         - 施放时自动施放[暗矛投射]技能\n
         - 爆炸时适用[暗矛投射]攻击力\n
         - [暗矛投射]处于冷却时间时不会发动\n
        魔枪落下次数和范围增加， 攻击暗蚀状态的敌人时， 直到攻击结束为止， 不会减少暗蚀持续时间\n
         - 魔枪落下次数 : 25次\n
         - 总攻击力相同\n
         - 魔枪落下间隔 -20%\n
         - 魔枪落下范围 +40%
        """
        ...

    def vp_2(self):
        """
        [坠蚀之雨]\n
        所有魔枪同时落下后， 额外落下巨大的黑雷枪\n
         - 总攻击力相同\n
        施放[冥蚀脉冲]时自动施放\n
         - [坠蚀之雨]进入冷却时间时， 不发动效果
        """
        ...

# 暗蚀爆雷杀
# demonic_lancer/impaler/7f80b887a09e88e2c4728c898bd73654
# 3deb7be5f01953ac8b1ecaa1e25e0420/7f80b887a09e88e2c4728c898bd73654
class Skill31(ActiveSkill):
    """
    [黑雷系列]\n
    将黑雷凝缩到极限后注入魔枪， 生成巨大的黑雷枪后投掷。\n
    魔枪前进的同时贯穿路径上的敌人， 然后插入地面产生冲击波， 对敌人造成伤害； 插入地面的魔枪震动一定时间后爆炸。\n
    攻击暗蚀状态的敌人或震动的魔枪使敌人进入暗蚀状态时， 发生黑雷增幅。\n
    [暗蚀附加效果]\n
    发生黑雷增幅的魔枪会爆炸并造成更大范围的伤害。
    """
    name = "暗蚀爆雷杀"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [350, 3080]
    uuid = "7f80b887a09e88e2c4728c898bd73654"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # [黑雷系列]
    # 贯穿攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [暗蚀爆雷杀]\n
        额外注入一次黑雷\n
         - 注入黑雷时魔枪大小 +40%\n
         - 魔枪落地瞬间爆炸\n
         - 施放技能时进入无敌状态
        """
        ...

    def vp_2(self):
        """
        [暗蚀爆雷杀]\n
        向前方直线范围投掷蕴含毁灭性黑雷的魔枪\n
         - 魔枪贯穿敌人并突进\n
        基本冷却时间变更为60秒\n
        总攻击力 +50%
        """
        self.cd = 60
        self.skillRation *= 1.5
        ...

# 黑暗支配者
# demonic_lancer/impaler/e5c09f9132a48dc1d695968592cc5878
# 3deb7be5f01953ac8b1ecaa1e25e0420/e5c09f9132a48dc1d695968592cc5878
class Skill32(PassiveSkill):
    """
    支配黑暗的气息， 激发更强大的力量。\n
    增加基本攻击力和技能攻击力， 并增加暗蚀的持续时间。\n
    在决斗场中， 不增加暗蚀持续时间。
    """
    name = "黑暗支配者"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 3
    uuid = "e5c09f9132a48dc1d695968592cc5878"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 暗蚀持续时间增加 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    associate = [ {"data":data0,"type":"*skillRation"}]

# 无尽侵蚀 : 缚魂
# demonic_lancer/impaler/e0daa922b19cdc35de879e938361464e
# 3deb7be5f01953ac8b1ecaa1e25e0420/e0daa922b19cdc35de879e938361464e
class Skill33(ActiveSkill):
    """
    [暗蚀 + 黑雷系列]\n
    生成黑暗之枪， 向周围无差别投掷。\n
    投掷出去的枪在路径上留下痕迹， 在周围纵横穿刺， 使空间产生裂缝并将枪插入其中。\n
    然后， 抬起手将黑雷注入插入空间裂缝的黑暗之枪中， 引发大规模连锁爆炸。\n
    随着技能等级提升， 附加以下特殊效果。
    """
    name = "无尽侵蚀 : 缚魂"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [1200, 10080]
    uuid = "e0daa922b19cdc35de879e938361464e"
    hasVP = False
    hasUP = False

    # [暗蚀 + 黑雷系列]
    # 黑暗之枪攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 15
    # 黑暗之枪多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 10
    # 爆炸多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

# 暗影蚀魂
# demonic_lancer/impaler/0fbb8de70002ad34f046c94c2cb3e863
# 3deb7be5f01953ac8b1ecaa1e25e0420/0fbb8de70002ad34f046c94c2cb3e863
class Skill34(ActiveSkill):
    """
    [暗蚀系列]\n
    投掷分裂的巨型黑暗之枪。 黑暗之枪分裂为命中敌人的个数， 飞出后爆炸。\n
    被爆炸命中的敌人会进入暗蚀状态。
    """
    name = "暗影蚀魂"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 2 #TODO
    rangeLv = 2
    cube = 2
    cd = 30
    mp = [400, 1120]
    uuid = "0fbb8de70002ad34f046c94c2cb3e863"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # [暗蚀系列]
    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # [范围信息]
    # 分裂的黑暗之枪识别范围 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    def vp_1(self):
        """
        [暗影蚀魂]\n
        投掷黑暗之枪时， 快速飞向前方1000px内最近的敌人\n
         - 黑暗之枪分裂寻敌范围 +10%\n
         - 大型黑暗之枪发射速度 +50%\n
         - 黑暗之枪分裂发射速度 +50%
        """
        ...

    def vp_2(self):
        """
        [暗影蚀魂]\n
        [侵蚀之矛]、 [黑暗枪雨]、 [黑蚀葬礼]技能命中时自动施放\n
         - 无法单独施放\n
         - 命中敌人时发生爆炸\n
         - 从首个命中目标处产生分裂效果\n
        变更为可填充3次的技能\n
         - 每次填充冷却时间 : 10秒\n
         - 单次攻击力 -67%
        """
        self.cd = 10
        self.skillRation *= 0.33
        ...

# 黑蚀酷刑
# demonic_lancer/impaler/c5a2956d8ed3af1746ed2f76ca971a09
# 3deb7be5f01953ac8b1ecaa1e25e0420/c5a2956d8ed3af1746ed2f76ca971a09
class Skill35(ActiveSkill):
    """
    [黑雷系列]\n
    投掷巨大的魔枪， 吸附路径上的敌人， 并穿透空间。 然后快速投掷魔枪， 与之前巨大魔枪产生共鸣， 最后拔出魔枪， 引发爆炸。\n
    攻击被巨大魔枪暗蚀的敌人时， 发生黑雷增幅， 技能持续期间敌人的暗蚀时间不减少。\n
    若将敌人穿刺到不可移动的区域， 则暗枪士向后翻滚一定距离后开始投掷魔枪。\n
    若技能过程中连续按攻击键或技能键， 可以更快地投掷魔枪。\n
    投掷小型魔枪时， 按跳跃键可以立即发动爆炸攻击。\n
    可以强制中断技能的施放后僵直， 并立即施放部分技能。\n
    [可强制中断并施放的技能]\n
    [侵蚀之矛]、 [暗矛投射]、 [暗矛贯穿]、 [绝望枪]、 [连锁侵蚀]\n
    [暗蚀特殊效果]\n
    发生黑雷增幅的魔枪会爆炸并造成更大范围的伤害。
    """
    name = "黑蚀酷刑"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [800, 1650]
    uuid = "c5a2956d8ed3af1746ed2f76ca971a09"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # [黑雷系列]
    # 巨大魔枪攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 小型魔枪攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 10
    # 小型魔枪投掷次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 最后一击爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # [范围信息]
    # 最后一击爆炸范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 最后一击暗蚀爆炸范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)

    def vp_1(self):
        """
        [黑蚀酷刑]\n
        投掷大型魔枪后立即引发共鸣爆炸\n
         - 总攻击力相同\n
         - 投掷大型魔枪后的僵直时间 -20%\n
        未命中时剩余冷却时间缩短为5秒
        """
        ...

    def vp_2(self):
        """
        [黑蚀酷刑]\n
        投掷小型魔枪时， 从黑暗裂缝中发射[绝望枪]\n
         - 命中时自动施放[绝望枪]技能\n
         - [绝望枪]处于冷却时间时不会发动\n
        固定以最大速度发动， 攻击范围增加\n
         - 巨型魔枪投掷距离 +25%\n
         - 最后一击爆炸范围 +25%\n
        [绝望枪]\n
        自动施放时射程 +50%
        """
        ...

# 黑暗本源
# demonic_lancer/impaler/d429147c372b549c3dadcabcba50787f
# 3deb7be5f01953ac8b1ecaa1e25e0420/d429147c372b549c3dadcabcba50787f
class Skill36(PassiveSkill):
    """
    超越支配黑暗的层次， 达到深渊的境界， 获得可操纵空间的力量。\n
    增加基本攻击力和技能攻击力， 并且增加部分暗蚀技能的范围。 基本攻击、 前冲攻击、 跳跃攻击命中时可以使敌人进入暗蚀状态。\n
    此外， 若部分暗蚀技能未命中敌人、 直接碰撞地面发生爆炸， 则生成暗蚀领域， 持续暗蚀领域内的怪物。 [黑蚀葬礼]必定生成暗蚀领域。\n
    - [生成暗蚀领域的技能] -\n
    [侵蚀之矛]、 [黑蚀葬礼]
    """
    name = "黑暗本源"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 3
    uuid = "d429147c372b549c3dadcabcba50787f"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [侵蚀之矛]爆炸范围增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [黑暗枪雨]黑暗气息持续时间增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [黑蚀葬礼]爆炸范围增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 暗蚀领域持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    associate = [ {"data":data0,"type":"*skillRation"}]

# 冥夜裂空
# demonic_lancer/impaler/7ec521d063d2190e1fcc5bd229af9bcf
# 3deb7be5f01953ac8b1ecaa1e25e0420/7ec521d063d2190e1fcc5bd229af9bcf
class Skill37(ActiveSkill):
    """
    [暗蚀 + 黑雷系列]\n
    刺穿虚空、 制造空间裂缝， 并暗蚀该领域， 形成黑暗空间。\n
    黑暗空间形成后， 从裂缝中喷射黑暗气息， 在地面生成暗蚀领域， 持续诱发暗蚀。\n
    一定范围内存在暗蚀状态的敌人时， 裂缝内生成的枪会刺向敌人造成伤害。\n
    枪发射一定次数后或持续时间结束时， 黑暗空间和暗蚀领域消失。\n
    黑暗空间存在的状态下， 再次使用技能时， 原有的黑暗空间消失， 生成新的空间。\n
    - [暗蚀特殊效果] -\n
    存在暗蚀状态的敌人时， 生成并发射相应数量的黑暗之枪。
    """
    name = "冥夜裂空"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "7ec521d063d2190e1fcc5bd229af9bcf"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # [暗蚀 + 黑雷系列]
    # 枪攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 20
    # 枪发射次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 枪发射时间间隔 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 黑暗空间持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [范围信息]
    # 暗蚀状态敌人的探测范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    def vp_1(self):
        """
        [冥夜裂空]\n
        生成遮蔽天空的巨大裂缝， 暗蚀大范围区域\n
         - 暗蚀范围 : 2000px\n
        被裂缝暗蚀的敌人识别范围增加\n
         - 敌人识别范围 : 2000px
        """
        ...

    def vp_2(self):
        """
        [冥夜裂空]\n
        在被裂缝暗蚀的领域范围内， 命中黑雷系列技能时， 从裂缝中落下强化的魔枪并爆炸\n
         - 总攻击力相同\n
         - 暗蚀领域范围 +100%\n
         - 黑暗空间持续时间 -50%\n
        黑暗空间生成增益效果\n
         - 攻击速度 +15%\n
         - 增益持续时间 : 15秒 (最多叠加1次)
        """
        ...

# 冥蚀脉冲
# demonic_lancer/impaler/0113c8b1306ca76d208f83f2d093dd62
# 3deb7be5f01953ac8b1ecaa1e25e0420/0113c8b1306ca76d208f83f2d093dd62
class Skill38(ActiveSkill):
    """
     [暗蚀 + 黑雷系列]\n
    暗蚀前方一定区域， 使命中的敌人进入暗蚀状态， 然后跃起， 猛力向下刺出缠绕黑雷的魔枪。\n
    黑雷注入暗蚀领域后， 从地面射出大量黑雷枪， 造成多段伤害， 最后爆炸造成范围伤害。\n
    施放时按下方向键， 可以暗蚀周围区域。
    """
    name = "冥蚀脉冲"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "0113c8b1306ca76d208f83f2d093dd62"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    #  [暗蚀 + 黑雷系列]
    # 黑暗气息攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 地面射出的黑雷枪攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 8
    # 地面射出的黑雷枪多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 最后一击爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # [范围信息]
    # 暗蚀领域范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 最后一击爆炸范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)

    def vp_1(self):
        """
        [冥蚀脉冲]\n
        直接将魔枪插入地面， 注入暗蚀\n
         - 总攻击力相同\n
        可以强制中断施放后僵直并施放部分转职技能\n
         - 目标技能与[黑蚀酷刑]相同
        """
        ...

    def vp_2(self):
        """
        [冥蚀脉冲]\n
        暗蚀领域及爆炸范围增加， 爆炸结束后维持暗蚀领域\n
         - 领域持续时间 : 3秒\n
         - 暗蚀领域范围 +35%\n
         - 最后一击爆炸范围 +35%\n
        变更为可填充2次的技能\n
         - 每次填充冷却时间 : 22.5秒\n
         - 单次攻击力 -50%
        """
        self.cd = 22.5
        self.skillRation *= 0.5
        ...

# 幽影暗蚀 : 寂灭
# demonic_lancer/impaler/8b08f9504167a9c0f3a1d29d71b7943e
# 3deb7be5f01953ac8b1ecaa1e25e0420/8b08f9504167a9c0f3a1d29d71b7943e
class Skill39(ActiveSkill):
    """
    [暗蚀 + 黑雷系列]\n
    瞬间释放所有黑暗气息， 暗蚀一切。\n
    将膨胀的黑暗气息凝聚于一点， 注入黑雷形成巨大的黑暗之枪。\n
    然后跃起并投掷黑暗之枪， 造成剧烈爆炸， 消灭前方一切事物。\n
    - [暗蚀附加效果] -\n
    可以强制控制被暗蚀的敌人。
    """
    name = "幽影暗蚀 : 寂灭"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "8b08f9504167a9c0f3a1d29d71b7943e"
    hasVP = False
    hasUP = False

    #  [暗蚀 + 黑雷系列]
    # 黑暗气息攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1

# 暗源之蚀
# demonic_lancer/impaler/dde3b443bd5e61d90c34e5ee771e2c28
# 3deb7be5f01953ac8b1ecaa1e25e0420/dde3b443bd5e61d90c34e5ee771e2c28
class Skill40(PassiveSkill):
    """
    千魂·暗枪士激发的黑暗力量能暗蚀并扭曲虚无的空间。 增加基本攻击力和转职技能攻击力， 部分技能附加额外效果。\n
    [绝望枪]\n
    投掷魔枪时， 背后生成暗蚀裂缝， 更大范围地投掷魔枪。 后跳和空中状态下， 也可以施放该技能。 后跳过程中施放技能时， 向后跳跃的同时投掷黑雷枪； 投掷瞬间按后方向键可增加后退距离。 空中施放技能时， 向斜线投掷黑雷枪。 \n
    [黑蚀葬礼]\n
    从暗枪士的身体中释放暗蚀气息， 同时投掷黑雷枪引发爆炸。 黑暗之枪爆炸攻击和黑雷枪的爆炸攻击同时进行； 后跳、 空中施放时， 适用相同效果。\n
    [撕裂自然法则， 散播绝望！]
    """
    name = "暗源之蚀"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "dde3b443bd5e61d90c34e5ee771e2c28"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [绝望枪]
    # 总投掷次数 : 15次
    # 绝望枪攻击力 : 原有[绝望枪]投掷魔枪攻击力的60%

    associate = [ {"data":data0,"type":"*skillRation"}]

# 虚空碎灭
# demonic_lancer/impaler/527cdc3ecca985e18ef819d456532b26
# 3deb7be5f01953ac8b1ecaa1e25e0420/527cdc3ecca985e18ef819d456532b26
class Skill41(ActiveSkill):
    """
    [黑雷系列]\n
    聚集黑暗之力， 投掷足以撕裂空间的凝缩黑雷枪。 黑雷枪贯穿路径上的敌人， 嵌入虚空之中， 然后剧烈旋转， 吸附周围的敌人后爆炸。\n
    后跳和空中状态下也可以施放该技能。\n
    [暗蚀特殊效果]\n
    搜寻一定范围内暗蚀状态的敌人， 在该敌人周围生成小型裂缝。 裂缝中出现黑雷枪攻击并强控敌人。 此时， 敌人不会被暗枪士投掷的黑雷枪吸附。 暗蚀效果造成的伤害与黑雷枪对非暗蚀状态敌人造成的伤害不叠加， 最多可以生成6个小型裂缝。
    """
    name = "虚空碎灭"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [960, 9600]
    uuid = "527cdc3ecca985e18ef819d456532b26"
    hasVP = False
    hasUP = False

    # [黑雷系列]
    # 贯穿攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 旋转多段攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 20
    # 旋转多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # 暗蚀状态敌人搜寻范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 暗蚀裂缝生成数量上限 : {value5}个
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)

# 暗·渊灭禁绝
# demonic_lancer/impaler/e788de1a4498c99fcc790302c4d41fed
# 3deb7be5f01953ac8b1ecaa1e25e0420/e788de1a4498c99fcc790302c4d41fed
class Skill42(ActiveSkill):
    """
    [暗蚀 + 黑雷系列]\n
    瞬间释放暗蚀的气息， 使周围的敌人进入暗蚀状态后， 使暗蚀扭曲生成数个裂隙。 然后， 千魂·暗枪士隐藏身影， 从裂缝中发射暗蚀之枪， 使一切陷入黑暗。\n
    消失的暗枪士在暗蚀空间中将黑雷枪插入地面， 生成裂缝。 黑雷枪连接敌人所在空间的裂缝， 穿透所有敌人， 引发巨大黑雷爆炸。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "暗·渊灭禁绝"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "e788de1a4498c99fcc790302c4d41fed"
    hasVP = False
    hasUP = False

    #  [暗蚀 + 黑雷系列]
    # 暗蚀之枪攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 12
    # 暗蚀之枪多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 黑雷枪攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 8
    # 黑雷枪多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'impaler'
        self.nameCN = '千魂·暗枪士'
        self.role = 'demonic_lancer'
        self.角色 = '魔枪士'
        self.职业 = '暗枪士'
        self.jobId = '3deb7be5f01953ac8b1ecaa1e25e0420'
        self.jobGrowId = 'c9b492038ee3ca8d27d7004cf58d59f3'

        self.武器选项 = ['长枪','战戟','光枪','暗矛'] # TODO
        self.输出类型选项 = ['魔法百分比'] # TODO
        self.输出类型 = '魔法百分比' # TODO
        self.防具精通属性 = ['智力'] # TODO
        self.防具类型 = '皮甲'
        self.buff = 1.93 # TODO

        super().__init__(equVersion, __name__)
