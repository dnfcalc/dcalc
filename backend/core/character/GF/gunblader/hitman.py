#986c2b3d72ee0e4a0b7fcfbe786d4e02
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "gunblader/hitman/cn/skillDetail"

# 穿透射击
# gunblader/hitman/92360eab6e1f378902018eca681ac629
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/92360eab6e1f378902018eca681ac629
class Skill1(ActiveSkill):
    """
    [射击]\n
    快速拔枪射击前方敌人。\n
    子弹100%穿透目标。 转职为暗刃后， 增加发射次数并应用单独的攻击力。
    """
    name = "穿透射击"
    learnLv = 1
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 5
    mp = [6, 40]
    uuid = "92360eab6e1f378902018eca681ac629"
    hasVP = False
    hasUP = False

    # 射击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [转职为暗刃时]
    # 发射次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 射击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 5
    # [范围信息]
    # 子弹发射距离比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

# 幽灵近战术
# gunblader/hitman/de3fea2d65c597f4d55c70a02b97fc79
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/de3fea2d65c597f4d55c70a02b97fc79
class Skill2(PassiveSkill):
    """
    将暗刃的基本枪械幽灵5号与近身战斗秘技C.Q.B结合， 形成独特的战斗技巧。\n
    转职时， 基本攻击、 前冲攻击和跳跃攻击变更为暗刃专用攻击。
    """
    name = "幽灵近战术"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 6 #TODO
    rangeLv = 3
    uuid = "de3fea2d65c597f4d55c70a02b97fc79"
    hasVP = False
    hasUP = False


# 基础精通
# gunblader/hitman/5a56514f35cf0270ae8d6c65f8fefd78
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/5a56514f35cf0270ae8d6c65f8fefd78
class Skill4(PassiveSkill):
    """
    增加基本攻击、 前冲攻击、 跳跃攻击和[弦月斩]的攻击力。\n
    在决斗场中， 增益/减益技能、 被动技能的技能攻击力增加效果对[基础精通]无影响。
    """
    name = "基础精通"
    learnLv = 1
    masterLv = 190
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


# 重劈
# gunblader/hitman/1fadde0eece18649caddbca7bd58cc2f
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/1fadde0eece18649caddbca7bd58cc2f
class Skill7(ActiveSkill):
    """
    [剑术]\n
    强力劈砍地面， 引发冲击波。\n
    向下劈砍敌人， 用击打地面的剑和剑产生的冲击波的力量使敌人浮空。
    """
    name = "重劈"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 1 #TODO
    rangeLv = 2
    cd = 4
    mp = [20, 200]
    uuid = "1fadde0eece18649caddbca7bd58cc2f"
    hasVP = False
    hasUP = False

    # 劈砍攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1

# G型手榴弹
# gunblader/hitman/d085127b0edd719782bd618d5688f4a1
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/d085127b0edd719782bd618d5688f4a1
class Skill8(ActiveSkill):
    """
    取出G型手榴弹， 拔掉保险环后扔向前方。\n
    G型手榴弹飞出一定距离后触地爆炸， 对敌人造成伤害并使其浮空。\n
    手榴弹飞行过程中碰到敌人时立即爆炸。\n
    转职为战线佣兵后， 增加攻击力与爆炸范围。
    """
    name = "G型手榴弹"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 6
    mp = [20, 200]
    uuid = "d085127b0edd719782bd618d5688f4a1"
    hasVP = False
    hasUP = False

    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # - [转职为战线佣兵后] -
    # 攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 爆炸范围增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [范围信息]
    # 爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

# 瞬击
# gunblader/hitman/4b2c90ec226fd40e967875aa5eabefb2
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
    position = 4 #TODO
    rangeLv = 2
    cd = 6
    mp = [1, 100]
    uuid = "4b2c90ec226fd40e967875aa5eabefb2"
    hasVP = False
    hasUP = False

    # 挥舞枪身攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 =1
    # 斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1

# 浮空连击
# gunblader/hitman/d0cdaca82892e54097f22a1f60817048
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/d0cdaca82892e54097f22a1f60817048
class Skill10(ActiveSkill):
    """
    [剑术]\n
    以迅雷不及掩耳之势快速连击两次。\n
    第二次上挑攻击命中时使敌人浮空， 有利于连接下一次攻击。
    """
    name = "浮空连击"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 1 #TODO
    rangeLv = 2
    cd = 4.5
    mp = [12, 125]
    uuid = "d0cdaca82892e54097f22a1f60817048"
    hasVP = False
    hasUP = False

    # 下斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 上挑攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1


# 长刀精通
# gunblader/hitman/c61f5a010370101402b05b21916c2071
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/c61f5a010370101402b05b21916c2071
class Skill15(PassiveSkill):
    """
    增加物理攻击力， 并减少技能冷却时间， 但觉醒技能除外。 装备长刀时，增加命中率。 \n
    在决斗场中， 不适用冷却时间减少效果。\n
    [一开始是想用剑的长度来弥补剑术的缺陷， 但现在已经像自己的双手一样运用自如了。]
    """
    name = "长刀精通"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 4 #TODO
    rangeLv = 3
    uuid = "c61f5a010370101402b05b21916c2071"
    hasVP = False
    hasUP = False

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 命中率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 冷却时间减少率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    associate = [
        {"type":"$*PAtkP","data":data0},
        {"type":"*cdReduce","data":data2,"exceptSkills":['电光飞掠', '集结·暮光之翼', '暮光密令 : 黎明决战']},
    ]

# 捷影步
# gunblader/hitman/202edb928046f4fa6dedf6337377efd5
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/202edb928046f4fa6dedf6337377efd5
class Skill16(ActiveSkill):
    """
    [混合]\n
    为了在战场上迅速移动而开发的暗刃专用移动技能。\n
    在[捷影步]过程中再次按技能键、 攻击键、 或<Z>键， 向敌人发动横斩并连接射击击退敌人。
    """
    name = "捷影步"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 5
    mp = [21, 220]
    uuid = "202edb928046f4fa6dedf6337377efd5"
    hasVP = False
    hasUP = True

    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 射击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 4
    # 射击多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 掩护射击
# gunblader/hitman/2a3c96b88d02372505692da0a8b54743
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/2a3c96b88d02372505692da0a8b54743
class Skill17(ActiveSkill):
    """
    [射击]\n
    向左右快速射击， 对前方敌人造成伤害。\n
    可以在[后跳]过程中施放， 敌人每次被击中都会沿Y轴小幅移动。
    """
    name = "掩护射击"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 6
    mp = [21, 220]
    uuid = "2a3c96b88d02372505692da0a8b54743"
    hasVP = False
    hasUP = True

    # 对单个敌人攻击次数上限 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 射击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 10
    # [范围信息]
    # 子弹发射距离比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 剑刃突刺
# gunblader/hitman/bc11d28c04e01923a093d65752c55516
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/bc11d28c04e01923a093d65752c55516
class Skill18(ActiveSkill):
    """
    [剑术]\n
    以极快的速度对附近敌人发动连续突刺， 然后在射击的同时横斩击飞敌人。\n
    按住向前方向键施放技能， 发动终结攻击时， 可以小幅向前移动并进行攻击。\n
    在决斗场中， 发动终结攻击后不会向前方移动。\n
    [用敌人来不及反应的超快的速度突袭敌人， 这是基础阶段的近身战斗术。]
    """
    name = "剑刃突刺"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 6
    mp = [33, 346]
    uuid = "bc11d28c04e01923a093d65752c55516"
    hasVP = False
    hasUP = True

    # 突刺次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 突刺攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 4
    # 终结横斩攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 终结射击对单个敌人攻击次数上限 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 终结射击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 3
    # [范围信息]
    # 子弹发射距离比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)

# 轮盘连射
# gunblader/hitman/faf9cd66281078b51be2ee0b0f6c5530
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/faf9cd66281078b51be2ee0b0f6c5530
class Skill19(ActiveSkill):
    """
    [混合]\n
    上挑攻击地面的敌人， 使敌人浮空， 然后进行射击造成伤害。\n
    对于无法抓取的敌人， 上挑后直接下劈攻击敌人。
    """
    name = "轮盘连射"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 8
    mp = [33, 346]
    uuid = "faf9cd66281078b51be2ee0b0f6c5530"
    hasVP = False
    hasUP = True

    # 射击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 上挑攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 射击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 10
    # power2 = 3.72 倍率写在三觉被动上
    # 下劈攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [范围信息]
    # 射击 x轴范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 射击 y轴范围 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)

    data6 = data2
    hit6 = 0
    power6 = 0

# 暴击
# gunblader/hitman/fc1262c19f3d0477ee8eda47b8db8696
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/fc1262c19f3d0477ee8eda47b8db8696
class Skill20(PassiveSkill):
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

# 利刃旋斩
# gunblader/hitman/d296043df164385a14cb973c8c7c4d07
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/d296043df164385a14cb973c8c7c4d07
class Skill21(ActiveSkill):
    """
    [剑术]\n
    左右斩击敌人2次， 然后利用弹力腾空旋转并发动连续斩击， 落地后大幅度挥剑， 发动近身连续斩击。
    """
    name = "利刃旋斩"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 7
    mp = [33, 346]
    uuid = "d296043df164385a14cb973c8c7c4d07"
    hasVP = False
    hasUP = True

    # 旋转斩击多段攻击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 左右斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 2
    # 旋转斩击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 5
    # 最终旋斩攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1

# 暗刃战略
# gunblader/hitman/ca75c965f20a150f99f54155a37400df
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/ca75c965f20a150f99f54155a37400df
class Skill22(PassiveSkill):
    """
    施放射击系技能后， 可以取消僵直， 立即施放剑术、 混合系技能 (部分通用技能除外)。\n
    增加物理暴击伤害， 物理暴击率。\n
    - [无法取消僵直的通用技能] -\n
    [瞬击]、 [源光斩]、 [G型手榴弹]、 [源能护盾]\n
    [射击系技能]\n
    [穿透射击]、 [掩护射击]、 [潜行射击]、 [游弹枪袭]、 [全方位射击]\n
    [剑术系技能]\n
    [毁灭强击]、 [浮空连击]、 [剑刃突刺]、 [利刃旋斩]、 [枪刃乱舞]、 [疾光斩]、 [碧波瞬斩]\n
    [混合系技能]\n
    [捷影步]、 [轮盘连射]、 [回旋飞剑]、 [近敌灭杀]、 [大回旋坠斩]、 [燃情协战]
    """
    name = "暗刃战略"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 1 #TODO
    rangeLv = 3
    uuid = "ca75c965f20a150f99f54155a37400df"
    hasVP = False
    hasUP = False

    # 物理暴击伤害增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 物理暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    associate = [ {"data":data0,"type":"*skillRation"}]

# 潜行射击
# gunblader/hitman/6e33d47e6622ce03b6defdd912140270
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/6e33d47e6622ce03b6defdd912140270
class Skill23(ActiveSkill):
    """
    [射击]\n
    快速移动一定距离并进行射击， 按向后或下方向键时， 可以进行短距离滑行并减少推力。\n
    可以强制中断射击技能施放后僵直并施放该技能。
    """
    name = "潜行射击"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 6
    mp = [61, 255]
    uuid = "6e33d47e6622ce03b6defdd912140270"
    hasVP = False
    hasUP = True

    # 射击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 基本移动距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 15
    # 按下方向键时 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 射击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [范围信息]
    # 子弹发射距离比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

# 战术指示
# gunblader/hitman/1721e94897e9961d5c98130a13392f17
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/1721e94897e9961d5c98130a13392f17
class Skill24(ActiveSkill):
    """
    暗刃身为组织的最强王牌兼指挥官， 发挥出色的战斗能力， 增加自身基本攻击力和技能攻击力， 并凭借优秀的指挥能力， 提升包括自身在内所有队员的攻击速度、 移动速度和施放速度。
    """
    name = "战术指示"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 7 #TODO
    rangeLv = 3
    cd = 5
    uuid = "1721e94897e9961d5c98130a13392f17"
    hasVP = False
    hasUP = False

    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 基本攻击力和技能攻击力增加比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 攻击速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 移动速度增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 施放速度增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 队友攻击速度增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 队友移动速度增加 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # 队友施放速度增加 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)

# 游弹枪袭
# gunblader/hitman/b163d099c8cc27fdb6fd3639c2ee6df9
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/b163d099c8cc27fdb6fd3639c2ee6df9
class Skill25(ActiveSkill):
    """
    [射击]\n
    向前面的敌人发动无差别射击， 直到打光幽灵5号的子弹。\n
    射击过程中按跳跃键， 可以中断技能。
    """
    name = "游弹枪袭"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 8
    mp = [62, 651]
    uuid = "b163d099c8cc27fdb6fd3639c2ee6df9"
    hasVP = False
    hasUP = True

    # 射击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 30
    # 射击多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # 子弹发射距离比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 全方位射击
# gunblader/hitman/51a08fd0c90f0a5276cd552047fac93d
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/51a08fd0c90f0a5276cd552047fac93d
class Skill26(ActiveSkill):
    """
    [射击]\n
    向周围敌人发动无差别射击。\n
    按住技能键或攻击键可以增加连射速度。\n
    射击的过程中按跳跃键可以中断技能。\n
    [这是暗刃闯进敌阵时先发制人的射击术， 当周围都是敌人时最有效。]
    """
    name = "全方位射击"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [131, 1100]
    uuid = "51a08fd0c90f0a5276cd552047fac93d"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 周围射击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 周围射击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 15
    # 最终射击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 最终射击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 6
    # [范围信息]
    # 打击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    def vp_1(self):
        """
        [알파 스트라이크]\n
        브랜드가 나타나 히트맨 대신 공격\n
        황혼의 날개, 여명의 비상을 제외한 다른 스킬 도중 시전 가능, 이 경우 시전 모션 없이 즉시 발동
        """
        ...

    def vp_2(self):
        """
        [全方位射击]\n
        比尔和布兰德出现， 和暗刃一起乱射枪击清扫战场\n
        - 总攻击力相同\n
        固定以最大连击数为标准进行射击\n
        可以强制中断射击技能施放后僵直并施放
        """
        ...

# 回旋飞剑
# gunblader/hitman/28b583c75a49103a1d8aabf799c000a4
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/28b583c75a49103a1d8aabf799c000a4
class Skill27(ActiveSkill):
    """
    [混合]\n
    旋转并向前方投掷长刀， 在长刀飞回之前持续进行射击。\n
    长刀飞出一定距离后自动飞回， 对范围内的敌人造成伤害并将敌人推向攻击方向。\n
    [此战斗术的灵感来自阿拉德的飞剑流剑士。]
    """
    name = "回旋飞剑"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [62, 651]
    uuid = "28b583c75a49103a1d8aabf799c000a4"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 投掷前的旋转上挑攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 长刀飞出时的攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 长刀飞回时的攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 长刀旋转攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 8
    # 射击攻击次数上限 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 射击攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    hit5 = 5
    # [范围信息]
    # 长刀大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

    def vp_1(self):
        """
        [回旋飞剑]\n
        删除上挑， 射击的同时投掷长刀\n
        投掷出的长刀在前方旋转， 吸引范围内敌人 (包括霸体状态的敌人)， 被命中的敌人会进入强制控制状态3秒\n
        - 总攻击力相同\n
        长刀旋转大小 +30%
        """
        ...

    def vp_2(self):
        """
        [回旋飞剑]\n
        施放技能过程中所受伤害 -70%\n
        - 基本冷却时间变更为18秒\n
        - 总攻击力 -10%\n
        [游弹枪袭]处于可施放的状态时， 比尔会出现并施放[游弹枪袭]
        """
        self.cd = 18
        self.skillRation *= 0.9

# 枪刃乱舞
# gunblader/hitman/f0cc2c950f3bdf4103c75fa496bcac34
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/f0cc2c950f3bdf4103c75fa496bcac34
class Skill28(ActiveSkill):
    """
    [剑术]\n
    以肉眼看不见的速度发动斩击和射击， 横扫敌人。\n
    在一定范围内快速连续攻击， 然后用强力横斩将敌人击飞。\n
    连按技能键或攻击键， 可以加快斩击与射击区间的施放速度。
    """
    name = "枪刃乱舞"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [174, 1461]
    uuid = "f0cc2c950f3bdf4103c75fa496bcac34"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 斩击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 10
    # 射击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 射击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 15
    # 最终横斩攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1
    # [范围信息]
    # 斩击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 射击范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

    def vp_1(self):
        """
        [枪刃乱舞]\n
        斩击速度 +30%\n
        斩击命中时强制控制敌人， 霸体状态的目标也会被吸附到前方\n
        无论是否输入技能键， 都固定以最大连击速度为标准施放
        """
        ...

    def vp_2(self):
        """
        [枪刃乱舞]\n
        下达命令让组织成员肃清前方\n
        随后出现下级暗刃清扫敌人\n
        [某下级暗刃 : 这可是个露脸的好机会， 得让老大好好记住我！]
        """
        ...

# 疾光斩
# gunblader/hitman/147d005ac868e0de52b1f255eea35d62
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/147d005ac868e0de52b1f255eea35d62
class Skill29(ActiveSkill):
    """
    [剑术]\n
    聚集力量向前方发动疾光斩。
    """
    name = "疾光斩"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [305, 2562]
    uuid = "147d005ac868e0de52b1f255eea35d62"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 横斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # [范围信息]
    # 斩击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    def vp_1(self):
        """
        [疾光斩]\n
        发动速度 +50%\n
        命中后可强制中断并施放暗刃的转职技能
        """
        ...

    def vp_2(self):
        """
        [疾光斩]\n
        施放技能时进入无敌状态\n
        斩击范围 +30%
        """
        ...

# B.G枪刃改造
# gunblader/hitman/47bd4871f29defc2a0021ee9261d7a5b
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/47bd4871f29defc2a0021ee9261d7a5b
class Skill30(PassiveSkill):
    """
    对暗刃视如己命的长刀与幽灵5号进行加工， 可以更有效地使用技能。\n
     增加基本攻击力和技能攻击力。
    """
    name = "B.G枪刃改造"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 1 #TODO
    rangeLv = 3
    uuid = "47bd4871f29defc2a0021ee9261d7a5b"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)

    associate = [ {"data":data0,"type":"*skillRation"}]

# 电光飞掠
# gunblader/hitman/669f1428193f61f9d92c743b72438c4d
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/669f1428193f61f9d92c743b72438c4d
class Skill31(ActiveSkill):
    """
    左右大幅移动， 用剑术和射击蹂躏敌人。\n
    移动过程中每次击中敌人时， 都会使敌人向攻击范围的中心地点小幅移动。\n
    第四次旋转剑击后， 向前方敌人连续射击， 对敌人造成伤害并使其浮空。
    """
    name = "电光飞掠"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [1018, 8551]
    uuid = "669f1428193f61f9d92c743b72438c4d"
    hasVP = False
    hasUP = False

    # 每次攻击移动距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 剑术攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 射击攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 最终射击攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 剑术攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 13
    # 射击攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    hit5 = 8
    # 最终射击攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    hit6 = 8

# 近敌灭杀
# gunblader/hitman/8510294202d0e042dd29a2422fc6770d
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/8510294202d0e042dd29a2422fc6770d
class Skill32(ActiveSkill):
    """
    [混合]\n
    爆发性地射出剑气刺向多名敌人， 然后将敌人拉到前方进行零距离射击。\n
    被刺中的敌人会被强制控制， 直到射击结束为止都无法移动。\n
    射击过程中按跳跃键， 可以立即结束射击。
    """
    name = "近敌灭杀"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 2
    cube = 2
    cd = 25
    mp = [340, 952]
    uuid = "8510294202d0e042dd29a2422fc6770d"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 刺击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 射击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 射击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 20
    # [范围信息]
    # 刺击距离比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [近敌灭杀]\n
        刺击距离 +20%\n
        刺击准备动作变更为无敌状态\n
        射击结束后增加无敌时间
        """
        ...

    def vp_2(self):
        """
        [近敌灭杀]\n
        暗刃、 比尔和布兰德一起射击前方的敌人\n
        随后罗朗加入， 与暗刃一起对大范围敌人发起斩击\n
        - 总攻击力相同\n
        [暮光之翼， 集结。]
        """
        ...

# 大回旋坠斩
# gunblader/hitman/b3659936a9a74c4ed6f7faf07cca1f9e
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/b3659936a9a74c4ed6f7faf07cca1f9e
class Skill33(ActiveSkill):
    """
    [混合]\n
    为了在战场上突袭敌人而开发的技能。 螺旋形旋转斩击周围敌人， 同时进行射击。\n
    旋转斩击命中敌人时会将敌人推向角色移动方向， 最终坠斩使敌人受到伤害的同时使其浮空。\n
    施放技能时按向前方向键， 可以旋转更远的距离。
    """
    name = "大回旋坠斩"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [699, 1467]
    uuid = "b3659936a9a74c4ed6f7faf07cca1f9e"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 射击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 射击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 10
    # 旋转斩击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 旋转斩击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 10
    # 最终坠斩攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1
    # [范围信息]
    # 最后一击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)

    def vp_1(self):
        """
        [大回旋坠斩]\n
        准备动作后直接发动最终坠斩\n
        - 删除射击和旋转斩击\n
        - 总攻击力相同\n
        可以在空中或后跳中施放\n
        最终坠斩攻击范围 +30%
        """
        ...

    def vp_2(self):
        """
        [大回旋坠斩]\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 25秒\n
        - 攻击力 -50%\n
        固定向前方旋转突进， 攻击周围敌人后落地\n
        删除最后一击\n
        - 总攻击力相同\n
        可以强制中断落地后僵直并施放[潜行射击]\n
        - 强制中断时可以变更施放方向\n
        施放时， 初始化[潜行射击]技能冷却时间\n
        [潜行射击]攻击力 -50%
        """
        self.cd = 25
        self.skillRation *= 0.5

# B.C精锐特训
# gunblader/hitman/38612d8f2561edc2eb68d5057a837bfa
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/38612d8f2561edc2eb68d5057a837bfa
class Skill34(PassiveSkill):
    """
    通过持续的战斗指挥训练， 大幅提升角色在战场上的战斗能力。\n
    增加基本攻击力和技能攻击力， 增加可以取消僵直的技能， 而且这些技能在施放过程中， 可以强制中断并立即连接其他技能。\n
    - [可取消僵直的技能] -\n
    [回旋飞剑]、 [近敌灭杀]
    """
    name = "B.C精锐特训"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 1 #TODO
    rangeLv = 3
    uuid = "38612d8f2561edc2eb68d5057a837bfa"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)

    associate = [ {"data":data0,"type":"*skillRation"}]

# 致命焰火
# gunblader/hitman/6a1d1f08a6572be420bb3a256c44c015
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/6a1d1f08a6572be420bb3a256c44c015
class Skill35(ActiveSkill):
    """
    [射击]\n
    把幽灵5号的弹匣扔到一定距离之外， 然后一边射击一边移动到弹匣位置。\n
    移动过程中击中敌人时， 都会使敌人向暗刃的攻击方向小幅移动。\n
    在弹匣位置更换弹匣后进行原地大范围射击， 若在更换弹匣前按向后方向键， 则转身向后方射击。\n
    连续按技能键或攻击键可以增加射击速度。
    """
    name = "致命焰火"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 2 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [579, 4487]
    uuid = "6a1d1f08a6572be420bb3a256c44c015"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 前方移动距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 移动射击次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 移动射击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 10
    # 原地范围射击攻击次数上限 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 原地范围射击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 10
    # 后方射击次数上限 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 后方射击攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    hit6 = 0
    # [范围信息]
    # 打击范围增加比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)

    mode = ['原地','后方']

    def setMode(self, mode):
        if mode == "原地":
            self.hit2 = 10
            self.hit4 = 10
            self.hit6 = 0
        elif mode == "后方":
            self.hit2 = 10
            self.hit4 = 0
            self.hit6 = 15

    def vp_1(self):
        """
        [致命焰火]\n
        将弹匣散布至周围后装填， 并在原地快速射击\n
        - 总攻击力相同\n
        可以强制中断暗刃的转职技能的施放后僵直， 并施放该技能
        """
        ...

    def vp_2(self):
        """
        [致命焰火]\n
        施放过程中按键可以向对角线方向移动\n
        - 删除原地范围射击、 后方射击\n
        - 总攻击力相同\n
        移动射击攻击范围 +50%\n
        删除按技能键时增加攻击速度的功能\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 20秒\n
        - 攻击力 -50%
        """
        self.cd = 20
        self.skillRation *= 0.5

    def effect(self, old, new):
        if self.vp == 2:
            self.associate = [{"type":"*skillRation","data":[0] + [-50]*self.maxLv,"skills":["潜行射击"]}]
        return super().effect(old, new)

# 碧波瞬斩
# gunblader/hitman/a2d943797daca862a6f321aca6ac9bfa
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/a2d943797daca862a6f321aca6ac9bfa
class Skill36(ActiveSkill):
    """
    [剑术]\n
    瞬间发动迅捷无比的连续斩击。\n
    向前方敌人同时发动连续斩击， 对敌人造成伤害。\n
    被击中的敌人会僵直一段时间， 无法行动。\n
    [此剑术源自阿拉德一位无名剑士的奥义， 变形化用为独特风格的剑术。]
    """
    name = "碧波瞬斩"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [1240, 4072]
    uuid = "a2d943797daca862a6f321aca6ac9bfa"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # [碧波瞬斩]每一击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 3
    # [碧波瞬斩]攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # [碧波瞬斩]斩击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    def vp_1(self):
        """
        [碧波瞬斩]\n
        施放过程中所受伤害 -70%\n
        蓄力后强力一闪进行1次攻击\n
        - 总攻击力相同\n
        - 基本冷却时间变更为58.5秒\n
        - 总攻击力 +30%
        """
        self.cd = 58.5
        self.skillRation *= 1.3

    def vp_2(self):
        """
        [碧波瞬斩]\n
        施放时， 罗朗会出现在对面一起施放[碧波瞬斩]\n
        - 总攻击力相同\n
        技能命中时， 可以强制中断并施放[疾光斩]技能\n
        - 连接施放该技能时， 罗朗会一起施放[疾光斩]
        """
        ...

# 集结·暮光之翼
# gunblader/hitman/c7bf7ccab413009640e65ca6f2f0263a
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/c7bf7ccab413009640e65ca6f2f0263a
class Skill37(ActiveSkill):
    """
    快速移动， 利用剑术与射击攻击敌人， 然后站在战场中间召唤暮光之翼队员布兰德与比尔， 与他们一起向周围敌人发动溃灭射击。
    """
    name = "集结·暮光之翼"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "c7bf7ccab413009640e65ca6f2f0263a"
    hasVP = False
    hasUP = False

    # 剑术攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 4
    # 射击攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 射击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 11
    # 最终齐射攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 最终齐射攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 20
    # 最终齐射爆炸攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    hit5 = 1

# 暮光战略
# gunblader/hitman/7f80b887a09e88e2c4728c898bd73654
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/7f80b887a09e88e2c4728c898bd73654
class Skill38(PassiveSkill):
    """
    紧急呼叫退役的暮光之翼队员罗朗， 用暮光之翼专属的终极组织战术“D.Tactics”指挥战友。\n
    增加基本攻击力和除[轮盘连射]之外的转职技能攻击力， 变更部分技能效果。\n
    [轮盘连射]\n
    暗刃快速上挑并进行射击的瞬间， 罗朗出现并出剑下劈， 在敌人身上留下伤痕， 短时间内强控敌人。 对无法抓取的敌人也发动相同的攻击。\n
    [游弹枪袭]\n
    前方射击时， 比尔从对面登场进行支援射击， 将敌人推到暗刃的交火距离内。\n
    [没想到会在这种情况下再见， 你说是吗？]
    """
    name = "暮光战略"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "7f80b887a09e88e2c4728c898bd73654"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [轮盘连射]暗刃射击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [轮盘连射]暗刃射击攻击力 : 原射击攻击力的{value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [轮盘连射]罗朗斩击攻击力 : [轮盘连射]攻击力总和的{value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    associate = [
        {"data":data0,"type":"*skillRation"},
        {"data":data1,"type":"=hit2","skills":["轮盘连射"],"ratio":1},
        {"data":[i - 100 if i >0 else 0 for i in data2],"type":"*power2","skills":["轮盘连射"]}
        ]

# 燃情协战
# gunblader/hitman/e5c09f9132a48dc1d695968592cc5878
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/e5c09f9132a48dc1d695968592cc5878
class Skill39(ActiveSkill):
    """
    [混合]\n
    暗刃在后方支援射击， 罗朗出现并向前冲， 快速斩击周围敌人。\n
    按向前方向键施放时， 比尔在后方进行支援射击， 同时暗刃突进， 横扫前方敌人。\n
    未学习[暮光战略]的状态下， 罗朗不会出现并发动。
    """
    name = "燃情协战"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [1007, 7550]
    uuid = "e5c09f9132a48dc1d695968592cc5878"
    hasVP = False
    hasUP = False

    # [普通施放时]
    # 暗刃支援射击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 10
    # 暗刃支援射击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 罗朗斩击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 6
    # 罗朗斩击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [前方突进时]
    # 比尔支援射击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 0
    # 比尔支援射击次数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 暗刃旋转斩击攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    hit6 = 0
    # 暗刃旋转斩击次数 : {value7}次
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    # 暗刃终结斩击攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)
    hit8 = 0

    mode = ['常规','突进']

    def setMode(self, mode):
        if mode == "常规":
            self.hit0 = 10
            self.hit2 = 6
            self.hit4 = self.hit6 = self.hit8 = 0
        elif mode == "突进":
            self.hit0 = self.hit2 = 0
            self.hit4 = 10
            self.hit6 = 5
            self.hit8 = 1


# 暮光密令 : 黎明决战
# gunblader/hitman/e0daa922b19cdc35de879e938361464e
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/e0daa922b19cdc35de879e938361464e
class Skill40(ActiveSkill):
    """
    比尔和布兰德接到苍暮·暗刃的密令， 对周围发动无差别射击， 扬起尘土， 隐藏所有人的身影。\n
    稍后， 暗刃和罗朗现身， 无情斩击敌人。\n
    然后， 所有暮光之翼队员集结在一起， 发动终结一击。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "暮光密令 : 黎明决战"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "e0daa922b19cdc35de879e938361464e"
    hasVP = False
    hasUP = False

    # 比尔、 布兰德射击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 22
    # 比尔、 布兰德射击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 暗刃、 罗朗登场攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 2
    # 暗刃、 罗朗登场攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 暗刃、 罗朗乱舞斩击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 4
    # 暗刃、 罗朗乱舞斩击次数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 比尔、 布兰德乱射攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    hit6 = 16
    # 比尔、 布兰德乱射次数 : {value7}次
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    # 终结一击攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)
    hit8 = 1

class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'hitman'
        self.nameCN = '苍暮·暗刃'
        self.role = 'gunblader'
        self.角色 = '枪剑士'
        self.职业 = '暗刃'
        self.jobId = '986c2b3d72ee0e4a0b7fcfbe786d4e02'
        self.jobGrowId = '37495b941da3b1661bc900e68ef3b2c6'

        self.武器选项 = ['长刀','小太刀','重剑','源力剑']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '轻甲'
        self.buff = 1.85

        super().__init__(equVersion, __name__)
