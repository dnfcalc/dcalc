#986c2b3d72ee0e4a0b7fcfbe786d4e02
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "gunblader/trouble_shooter/cn/skillDetail"

# 弦月斩
# gunblader/trouble_shooter/3c5604bdbb0240b8f130f59ab40509c3
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/3c5604bdbb0240b8f130f59ab40509c3
class Skill0(ActiveSkill):
    """
    用剑划出新月形状， 使命中的敌人浮空。\n
    浮空力随技能等级的增加而增加。
    """
    name = "弦月斩"
    learnLv = 1
    masterLv = 10
    maxLv = 20
    position = 3
    rangeLv = 3
    cd = 2
    uuid = "3c5604bdbb0240b8f130f59ab40509c3"
    hasVP = False
    hasUP = False

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 浮空力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 穿透射击
# gunblader/trouble_shooter/92360eab6e1f378902018eca681ac629
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
    position = 2
    rangeLv = 2
    cd = 5
    mp = [6, 40]
    uuid = "92360eab6e1f378902018eca681ac629"
    hasVP = False
    hasUP = False

    # 射击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [转职为暗刃时]
    # 发射次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 射击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 子弹发射距离比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 基础精通
# gunblader/trouble_shooter/5a56514f35cf0270ae8d6c65f8fefd78
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/5a56514f35cf0270ae8d6c65f8fefd78
class Skill3(PassiveSkill):
    """
    增加基本攻击、 前冲攻击、 跳跃攻击和[弦月斩]的攻击力。\n
    在决斗场中， 增益/减益技能、 被动技能的技能攻击力增加效果对[基础精通]无影响。
    """
    name = "基础精通"
    learnLv = 1
    masterLv = 190
    maxLv = 200
    position = 1
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


# 重劈
# gunblader/trouble_shooter/1fadde0eece18649caddbca7bd58cc2f
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/1fadde0eece18649caddbca7bd58cc2f
class Skill6(ActiveSkill):
    """
    [剑术]\n
    强力劈砍地面， 引发冲击波。\n
    向下劈砍敌人， 用击打地面的剑和剑产生的冲击波的力量使敌人浮空。
    """
    name = "重劈"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 4
    mp = [20, 200]
    uuid = "1fadde0eece18649caddbca7bd58cc2f"
    hasVP = False
    hasUP = False

    # 劈砍攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

# G型手榴弹
# gunblader/trouble_shooter/d085127b0edd719782bd618d5688f4a1
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/d085127b0edd719782bd618d5688f4a1
class Skill7(ActiveSkill):
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
    position = 8
    rangeLv = 2
    cd = 6
    mp = [20, 200]
    uuid = "d085127b0edd719782bd618d5688f4a1"
    hasVP = False
    hasUP = False

    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # - [转职为战线佣兵后] -
    # 攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸范围增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    associate = [ {"data":data1,"type":"+power0","skills":["G型手榴弹"]}, ]

# 瞬击
# gunblader/trouble_shooter/4b2c90ec226fd40e967875aa5eabefb2
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/4b2c90ec226fd40e967875aa5eabefb2
class Skill8(ActiveSkill):
    """
    挥舞枪身击打敌人后颈， 把击中的敌人拖到自己身前， 最后挥剑斩击拉过来的敌人。\n
    对无法抓取的敌人不适用控制效果。
    """
    name = "瞬击"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 5
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

# 浮空连击
# gunblader/trouble_shooter/d0cdaca82892e54097f22a1f60817048
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/d0cdaca82892e54097f22a1f60817048
class Skill9(ActiveSkill):
    """
    [剑术]\n
    以迅雷不及掩耳之势快速连击两次。\n
    第二次上挑攻击命中时使敌人浮空， 有利于连接下一次攻击。
    """
    name = "浮空连击"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 4.5
    mp = [12, 125]
    uuid = "d0cdaca82892e54097f22a1f60817048"
    hasVP = False
    hasUP = False

    # 下斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 上挑攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

# 源光斩
# gunblader/trouble_shooter/1803b6a67047cafb9e289b4f33cc507b
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/1803b6a67047cafb9e289b4f33cc507b
class Skill10(ActiveSkill):
    """
    用源能动力源向剑注入能量后， 向前发动斩击。 斩击后， 能量残留一定时间， 对敌人造成多段伤害。\n
    - [转职为源能专家时] -\n
    装备源力剑时， 无需注入源能直接发动斩击。
    """
    name = "源光斩"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 9
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


# 纯熟战技
# gunblader/trouble_shooter/3d8f3d438405d79f8d3ed68072674d1e
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/3d8f3d438405d79f8d3ed68072674d1e
class Skill13(PassiveSkill):
    """
    身经百战的战线佣兵独特的战斗技巧， 基本攻击变更为3次攻击， 并增加移动速度。\n
    战线佣兵擅长使用非常危险的特殊火药和巨大重剑， 用引火物质CTF制造的炸弹可以使敌人进入特殊灼伤状态， 并能强控敌人一定时间。
    """
    name = "纯熟战技"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 2
    rangeLv = 2
    uuid = "3d8f3d438405d79f8d3ed68072674d1e"
    hasVP = False
    hasUP = False

    # 移动速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

# 矫捷翻滚
# gunblader/trouble_shooter/ade01c1d6afc8a05055225045e89fe49
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/ade01c1d6afc8a05055225045e89fe49
class Skill14(ActiveSkill):
    """
    战线佣兵专用移动技能。 快速向前翻滚移动。\n
    滚动过程中， 适用无敌判定。\n
    滚动结束后， 按攻击键或技能键， 可以用剑上挑攻击敌人。\n
    上挑攻击的攻击力受[基础精通]的影响。\n
    按住与滚动方向相反的方向键， 再次按键或施放技能， 将朝相反方向发动攻击。\n
    战线佣兵的转职技能攻击结束后， 可以强制中断并向任意方向施放[矫捷翻滚]。\n
    但是， 无法强制中断[爆弹罗网]、 [G型烬灭榴弹]、 [终焉 : 硝烟狂欢]后施放[矫捷翻滚]。
    """
    name = "矫捷翻滚"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 6
    rangeLv = 2
    cd = 5
    mp = [150, 150]
    uuid = "ade01c1d6afc8a05055225045e89fe49"
    hasVP = False
    hasUP = False

    # 移动距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 上挑攻击力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 双重散射
# gunblader/trouble_shooter/78be08a3f8c834d3b06fa20c6a08c5a5
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/78be08a3f8c834d3b06fa20c6a08c5a5
class Skill15(ActiveSkill):
    """
    以坐姿快速连续发射霰弹， 对敌人造成2次伤害。
    """
    name = "双重散射"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 5
    mp = [30, 300]
    uuid = "78be08a3f8c834d3b06fa20c6a08c5a5"
    hasVP = False
    hasUP = True

    # 第1次射击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第2次射击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 射击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 源能护盾
# gunblader/trouble_shooter/0232c151ef3731c2dede51931a374723
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/0232c151ef3731c2dede51931a374723
class Skill16(ActiveSkill):
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
    position = 9
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
    hit2= 1
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

# 重剑精通
# gunblader/trouble_shooter/ff171dc487807bb9aa28900ca9a46b41
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/ff171dc487807bb9aa28900ca9a46b41
class Skill17(PassiveSkill):
    """
    增加物理攻击力。 使用重剑系武器攻击敌人时， 可以增加战线佣兵的攻击速度、 命中率和僵直度。\n
    [不是所有剑都只是为了挥斩而存在的， 朋友。]
    """
    name = "重剑精通"
    learnLv = 20
    masterLv = 20
    maxLv = 30
    position = 2
    rangeLv = 3
    uuid = "ff171dc487807bb9aa28900ca9a46b41"
    hasVP = False
    hasUP = False

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 命中率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 僵直度增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    
    associate = [ {"type":"$*PAtkP","data":data0}]


# 爆烈斩击
# gunblader/trouble_shooter/547ab2b2bd860d3e37355a9cfbc1077c
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/547ab2b2bd860d3e37355a9cfbc1077c
class Skill18(ActiveSkill):
    """
    用剑攻击敌人的下段。\n
    被剑术击中的敌人会旋转浮空并飞向战线佣兵的前方。\n
    剑术攻击之后， 按技能键可以发射霰弹。\n
    若输入向前方向键施放技能， 则向前滑动的同时攻击敌人。
    """
    name = "爆烈斩击"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 5
    mp = [40, 400]
    uuid = "547ab2b2bd860d3e37355a9cfbc1077c"
    hasVP = False
    hasUP = True

    # 剑攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 射击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 射击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)


# 充能特饮
# gunblader/trouble_shooter/506e7ed77d517419a6e1c437a2cedb17
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/506e7ed77d517419a6e1c437a2cedb17
class Skill20(ActiveSkill):
    """
    战斗开始之前， 来一罐能量饮料振作精神。\n
    效果持续期间， 增加基本攻击力和技能攻击力。\n
    [马上要开始忙碌了， 我需要激活能量……]
    """
    name = "充能特饮"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 7
    rangeLv = 3
    cd = 5
    uuid = "506e7ed77d517419a6e1c437a2cedb17"
    hasVP = False
    hasUP = False

    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 剑刃爆弹
# gunblader/trouble_shooter/5dc7008b12a459325b548b0715c6b73c
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/5dc7008b12a459325b548b0715c6b73c
class Skill21(ActiveSkill):
    """
    把炸弹绑在剑尖， 击退前方敌人并引爆炸弹。\n
    被击中的敌人会被强制控制， 并且被吸附到角色前方。\n
    然后炸弹爆炸， 对敌人造成多段攻击伤害并使其进入特殊灼伤。\n
    在决斗场中， 解除特殊灼伤时敌人稍微浮空后倒地。
    """
    name = "剑刃爆弹"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 10
    mp = [75, 398]
    uuid = "5dc7008b12a459325b548b0715c6b73c"
    hasVP = False
    hasUP = True

    # 击退攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 3
    # 爆炸多段攻击次数 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 特殊灼伤攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 特殊灼伤持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 爆炸范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)


# 广域散射
# gunblader/trouble_shooter/a5fa08f5d509e6ff2ebc68856a470b5a
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/a5fa08f5d509e6ff2ebc68856a470b5a
class Skill22(ActiveSkill):
    """
    用强扩散性的火药制作弹药， 然后用霰弹枪发射， 对前方大范围敌人造成伤害并使其进入僵直状态。
    """
    name = "广域散射"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 7
    mp = [30, 300]
    uuid = "a5fa08f5d509e6ff2ebc68856a470b5a"
    hasVP = False
    hasUP = True

    # 射击攻击力 : {value0}% 
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 射击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 火药改良
# gunblader/trouble_shooter/8ee0099656df08a0b39225f8a21d514b
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/8ee0099656df08a0b39225f8a21d514b
class Skill23(PassiveSkill):
    """
    改良战线佣兵使用的火药性能， 增加部分技能的攻击范围， 增加基本攻击力和转职技能攻击力， 并增加部分技能攻击范围。\n
    - [增加攻击范围] -\n
    基本攻击第3击、 [双重散射]、 [爆烈斩击]、 [广域散射]、 [G型手榴弹]、 [G型火焰爆弹]、 [裂地爆刃]。
    """
    name = "火药改良"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 2
    rangeLv = 3
    uuid = "8ee0099656df08a0b39225f8a21d514b"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 目标技能攻击范围增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [ {"data":data0,"type":"*skillRation"}]

# G型火焰爆弹
# gunblader/trouble_shooter/9bff7f2559e003766fee2853dca00631
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/9bff7f2559e003766fee2853dca00631
class Skill24(ActiveSkill):
    """
    使用威力强大的引火物质制作而成的特制火焰炸弹。\n
    施放时， 向前方投掷G型火焰爆弹， 然后用霰弹枪将其打爆， 引发强烈的火焰爆炸。\n
    爆炸范围内的敌人身上会着火并进入特殊灼伤状态， 在一定时间持续受到伤害， 并且被强制控制。\n
    霰弹枪射击失败时， G型火焰爆弹经过一定时间之后自动爆炸。\n
    在决斗场中， 解除特殊灼伤时敌人稍微浮空后倒地； 若在爆炸射击前强制中断技能， 则炸弹立即爆炸。\n
    [经历岁月的磨炼， 已经能忍耐高温了……不过这也太热了吧。]
    """
    name = "G型火焰爆弹"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cd = 10
    mp = [60, 600]
    uuid = "9bff7f2559e003766fee2853dca00631"
    hasVP = False
    hasUP = True

    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 特殊灼伤攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 特殊灼伤持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 爆裂斩
# gunblader/trouble_shooter/da6e37c1e3f0e8867f70007d89c239ff
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/da6e37c1e3f0e8867f70007d89c239ff
class Skill25(ActiveSkill):
    """
    连续挥舞绑着炸弹的剑发动攻击。\n
    剑击中敌人时发生剧烈爆炸， 使敌人受到巨大伤害并被推到前方。\n
    第一次攻击后， 再次按技能键将发动下一次攻击， 最多可以攻击敌人三次。\n
    按住向前方向键的状态下施放技能， 可增加挥剑前进的距离； 按向后方向键可缩短前进距离。\n
    未击中敌人时不发生爆炸， 每次攻击结束后， 可以强制中断并立即施放[矫捷翻滚]。
    """
    name = "爆裂斩"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [70, 700]
    uuid = "da6e37c1e3f0e8867f70007d89c239ff"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 第一次爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第二次爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 第三次爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [爆裂斩]\n
        即使未命中也发生爆炸\n
        爆炸范围 +50%\n
        额外攻击输入时间增加至5秒
        """
        ...

    def vp_2(self):
        """
        [爆裂斩]\n
        删除第1次、 第2次攻击， 第3次爆炸攻击力 +100%\n
        命中后可强制中断并施放剑术系列技能
        """
        self.hit0 = self.hit1 = 0
        self.power2 = 2

# 爆弹罗网
# gunblader/trouble_shooter/a6c8f69107f8c4f5d1a0c7a57d000290
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/a6c8f69107f8c4f5d1a0c7a57d000290
class Skill26(ActiveSkill):
    """
    用霰弹枪射击前方敌人， 然后利用后坐力向后跳跃， 投掷用导爆线制作的爆弹罗网。\n
    投掷的爆弹罗网在地面展开并存在一定时间， 有敌人入网时所有爆弹同时爆炸， 对敌人造成多段伤害并使其进入特殊灼伤状态。\n
    爆弹罗网存在一定时间， 再次按技能键可以立即引爆。\n
    爆弹罗网爆炸造成的特殊灼伤只在第一次造成伤害时生效1次。\n
    在决斗场中， 解除特殊灼伤时敌人稍微浮空后倒地。
    """
    name = "爆弹罗网"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [70, 700]
    uuid = "a6c8f69107f8c4f5d1a0c7a57d000290"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 射击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 6
    # 爆炸多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 特殊灼伤攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 特殊灼伤持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 爆弹罗网持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 爆炸大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [爆弹罗网]\n
        删除射击攻击， 投掷巨大的炸弹网\n
        - 炸弹网爆炸攻击次数变更为1次\n
        - 总攻击力相同\n
        后跳和跳跃过程中可以使用\n
        爆炸范围 +20%  
        """
        ...

    def vp_2(self):
        """
        [爆弹罗网]\n
        通过启动起爆开关引爆事先设置的爆弹\n
        - 总攻击力相同
        """
        ...

# 裂地爆刃
# gunblader/trouble_shooter/3829c15bf5f520c13998a3479ba0ce7b
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/3829c15bf5f520c13998a3479ba0ce7b
class Skill27(ActiveSkill):
    """
    把威力强大的炸弹绑在剑上， 向前突进并猛力劈砍地面。\n
    劈砍的位置发生剧烈爆炸， 对大范围的敌人造成巨大伤害。\n
    突进时被击中的敌人会被推到战线佣兵的前方。\n
    施放技能后， 若按住下方向键， 则停止突进并在原地劈砍地面。
    """
    name = "裂地爆刃"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [80, 800]
    uuid = "3829c15bf5f520c13998a3479ba0ce7b"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 爆炸范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [裂地爆刃]\n
        装填时间 -50%\n
        爆炸时产生碎片， 造成多段伤害\n
        - 多段攻击次数 : 8次\n
        - 总攻击力相同\n
        施放时初始化[矫捷翻滚]的冷却时间 
        """

    def vp_2(self):
        """
        [裂地爆刃]\n
        突进时击退敌人的范围增加\n
        爆炸范围 +40%\n
        施放过程中所受伤害 -90%
        """
        ...

# 惊喜大礼
# gunblader/trouble_shooter/03bb5314ffd41e9458d67ef924fef38f
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/03bb5314ffd41e9458d67ef924fef38f
class Skill28(ActiveSkill):
    """
    从怀中取出多枚特制炸弹， 迅速向前方投掷。\n
    在炸弹接触地面之前， 发射霰弹枪击爆炸弹， 对大范围的敌人造成巨大伤害。\n
    投掷炸弹时， 靠近战线佣兵的敌人会被向后震退。\n
    在决斗场中， 靠近战线佣兵的敌人不会被向后震退。\n
    [这是我特意准备的大礼， 希望你们喜欢。]
    """
    name = "惊喜大礼"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [90, 900]
    uuid = "03bb5314ffd41e9458d67ef924fef38f"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 6
    # 爆炸多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 爆炸范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [惊喜大礼]\n
        投掷时击退敌人的范围增加\n
        投掷炸弹后可以移动\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 22.5秒\n
        - 攻击力 -50% 
        """
        self.cd = 22.5
        self.skillRation *= 0.5

    def vp_2(self):
        """
        [惊喜大礼]\n
        爆炸范围 +15%\n
        在地面上布置大量炸弹后射击引爆\n
        - 总攻击力相同\n
        爆炸后生成裂痕地带， 对接触裂痕的敌人附加减速效果\n
        - 裂痕地带持续时间 : 5秒\n
        - 减速几率 : 100%\n
        - 减速持续时间 : 5秒\n
        在裂痕地带内施放[G型火焰爆弹]技能时， 会引发更巨大的[G型火焰爆弹]爆炸
        """
        ...

# 终极火力
# gunblader/trouble_shooter/bb34e8854a93fd250347a1c64119f7ab
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/bb34e8854a93fd250347a1c64119f7ab
class Skill29(PassiveSkill):
    """
    提升战场王牌使用的所有枪械的火力。\n
    增加战场王牌的基本攻击力、 技能攻击力和物理暴击率。
    """
    name = "终极火力"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 3
    uuid = "bb34e8854a93fd250347a1c64119f7ab"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [ {"data":data0,"type":"*skillRation"}]

# G型烬灭榴弹
# gunblader/trouble_shooter/1dad88963abdc96b091fcab185a8820d
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/1dad88963abdc96b091fcab185a8820d
class Skill30(ActiveSkill):
    """
    用威力强大的G型烬灭榴弹使敌人燃烧， 然后引发爆炸使敌人受到巨大伤害。\n
    施放时， 将两种榴弹扔到空中和地面。\n
    扔到空中的榴弹在一定高度爆炸， 喷出强力引火物质， 使地面上的所有的敌人进入特殊灼伤状态， 然后射击敌人造成追加伤害。\n
    经过一定时间后， 扔到地面的炸弹发生爆炸， 对敌人造成巨大物理伤害。\n
    施放技能时， 连续按攻击键或技能键， 可以加快技能施放速度。
    """
    name = "G型烬灭榴弹"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 8
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [980, 8232]
    uuid = "1dad88963abdc96b091fcab185a8820d"
    hasVP = False
    hasUP = False

    # 首次爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 特殊灼伤攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 霰弹枪射击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 4
    # 最终爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1

    #以前3，6，9的自增伤
    skillRation =  1.1

# 完美击球
# gunblader/trouble_shooter/27bade584bb42fef68148d3a0b72bace
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/27bade584bb42fef68148d3a0b72bace
class Skill31(ActiveSkill):
    """
    把炸弹绑在剑上， 然后旋转挥剑攻击敌人。\n
    旋转轨迹上发生连锁爆炸， 爆炸范围内的敌人会被吸附战线佣兵的前方。 此时也可以吸附被强制控制的敌人。\n
    然后用重剑上劈吸附的敌人， 引起威力巨大的最终爆炸， 将敌人击飞至前方。
    """
    name = "完美击球"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [400, 1620]
    uuid = "27bade584bb42fef68148d3a0b72bace"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 旋转爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 最终爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 爆炸大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最终爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [完美击球]\n
        删除最终爆炸攻击\n
        - 总攻击力相同\n
        攻击范围 +30%\n
        旋转攻击可吸附霸体状态下的目标
        """
        ...

    def vp_2(self):
        """
        [完美击球]\n
        施放速度 +20%\n
        可以在[矫捷翻滚]施放过程中预输入该技能\n
        - 预输入时， [矫捷翻滚]终结攻击变更为[完美击球]终结攻击动作\n
        - 总攻击力相同\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 12.5秒\n
        - 攻击力 -50%  
        """
        self.cd = 12.5
        self.skillRation *= 0.5

# 夺命焰火
# gunblader/trouble_shooter/04883563896fe1adac7505c6146b5f59
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/04883563896fe1adac7505c6146b5f59
class Skill32(ActiveSkill):
    """
    填装破坏力巨大的子弹， 向前方连续射击。\n
    施放时， 将两发子弹扔向空中， 连续射击前方。\n
    然后快速填装从空中降落的子弹并同时发射两发子弹， 造成最终多段攻击伤害。\n
    最终射击的后坐力强， 射击之后战线佣兵会向后退。\n
    最终射击时， 若按向前方向键， 可以缩短后退距离。
    """
    name = "夺命焰火"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [384, 1564]
    uuid = "04883563896fe1adac7505c6146b5f59"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 第一次射击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第二次射击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 最终射击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 4
    # 最终射击多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 射击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [夺命焰火]\n
        删除装填动作\n
        减少最终射击前的僵直时间\n
        [双重散射]、 [广域散射]攻击后， 可以立即连接[夺命焰火]\n
        最终射击后， 可以立即连接[双重散射]、 [广域散射]
        """
        ...

    def vp_2(self):
        """
        [夺命焰火]\n
        删除第1次、 第2次射击\n
        施放时立即装填子弹\n
        - 装填持续时间上限 : 10秒\n
        装填子弹后按追加按键发动终结射击\n
        - 总攻击力相同\n
        装填子弹后施放[双重散射]或[广域散射]时， 以强化[夺命焰火]终结射击发动\n
        - 发动技能攻击力合算至终结射击攻击力\n
        射击范围 +20%
        """
        ...

# 无法者之歌
# gunblader/trouble_shooter/dcd536f1674630f01fc9667bb202b851
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/dcd536f1674630f01fc9667bb202b851
class Skill33(PassiveSkill):
    """
    被称为传奇佣兵的巅峰狂徒使用的武器与火药拥有更强的威力。\n
    学习后， 增加基本攻击力和技能攻击力， 强化部分转职技能。\n
    - [技能强化] -\n
    [G型手榴弹] : 爆炸范围增加10%\n
    [双重散射] : 僵直度、 射击范围增加10%\n
    [爆烈斩击] : 僵直度、 射击范围增加10%\n
    [广域散射] : 僵直度、 攻击范围增加10%\n
    [剑刃爆弹] : 爆炸范围增加10%\n
    [爆裂斩] : 爆炸范围增加10%\n
    [G型火焰爆弹] : 施放速度、 爆炸范围增加10%\n
    [爆弹罗网] : 爆炸范围增加10%\n
    [惊喜大礼] : 施放速度增加10%\n
    [完美击球] : 最终爆炸范围增加10%\n
    [夺命焰火] : 僵直度、 射击范围增加10%
    """
    name = "无法者之歌"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 3
    uuid = "dcd536f1674630f01fc9667bb202b851"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

    associate = [ {"data":data0,"type":"*skillRation"}]

# 爆弹华尔兹
# gunblader/trouble_shooter/762c4e6d030eaf0abbfe1fec2b298574
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/762c4e6d030eaf0abbfe1fec2b298574
class Skill34(ActiveSkill):
    """
    扔出大量炸弹， 然后用重剑击打炸弹引起连锁爆炸。\n
    被爆炸击中的敌人受到强大的伤害并被击退。\n
    被重剑击中的敌人会被吸附到巅峰狂徒前方， 最终爆炸能使敌人浮空。
    """
    name = "爆弹华尔兹"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "762c4e6d030eaf0abbfe1fec2b298574"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 第一次爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 第一次爆炸多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 第二次爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2  = 5
    # 第二次爆炸多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 爆炸范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [爆弹华尔兹]\n
        删除第1次爆炸， 直接施放第2次爆炸\n
        第2次爆炸多段攻击次数 +3次\n
        - 总攻击力相同\n
        施放速度 +20%
        """
        ...

    def vp_2(self):
        """
        [爆弹华尔兹]\n
        献上藏有大量炸弹的花束后， 用爆弹剑下劈引发大范围爆炸\n
        - 总攻击力相同\n
        投掷过程中施放[剑刃爆弹]技能时， 下劈动作变更为刺击动作\n
        - [剑刃爆弹]攻击力合算至爆炸攻击力\n
        - 爆炸时适用[剑刃爆弹]特殊灼伤效果 
        """
        ...

# 覆灭之枪
# gunblader/trouble_shooter/23a5e0fba03283cb1b324a847b3fe370
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/23a5e0fba03283cb1b324a847b3fe370
class Skill35(ActiveSkill):
    """
    用终极覆灭之枪轰击前方。\n
    施放时， 将重剑插在前方当作支架。\n
    固定覆灭之枪， 瞄准前方的敌人后进行射击， 对前方的敌人造成巨大伤害。\n
    [霰弹枪嘛……威力至少要达到这种程度。]  
    """
    name = "覆灭之枪"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 5
    cd = 50
    mp = [600, 5000]
    uuid = "23a5e0fba03283cb1b324a847b3fe370"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 射击攻击力 : {value0}% 
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 射击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [覆灭之枪]\n
        施放时无敌\n
        为覆灭之枪额外填充特殊火药后开火\n
        - 基本冷却时间变更为75秒\n
        - 攻击力 +50%
        """
        self.cd = 75
        self.skillRation *= 1.5

    def vp_2(self):
        """
        [覆灭之枪]\n
        施放速度 +20%\n
        可以强制中断转职技能的施放后僵直并施放\n
        射击后可以立即移动\n
        - 基本冷却时间变更为25秒\n
        - 攻击力 -50%
        """
        self.cd = 25
        self.skillRation *= 0.5

# 终焉 : 硝烟狂欢
# gunblader/trouble_shooter/0ed3148658fe37b3336ccb718dc0fdb0
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/0ed3148658fe37b3336ccb718dc0fdb0
class Skill36(ActiveSkill):
    """
    施放时， 掏出引爆线并按下起爆开关。\n
    使预先埋设的大量CTF地雷同时爆炸， 黑烟弥漫战场， 使命中的敌人进入特殊灼伤状态。\n
    黑烟消散后， 巨型炸弹露出身影。\n
    巅峰狂徒用剑劈砍起爆开关， 使巨大炸弹爆炸， 对敌人造成巨大的多段伤害。\n
    [一切尽在掌控之中， 我早就准备好了。]
    """
    name = "终焉 : 硝烟狂欢"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "0ed3148658fe37b3336ccb718dc0fdb0"
    hasVP = False
    hasUP = False

    # CTF地雷爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # CTF地雷爆炸多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 13
    # 最后爆炸多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 铁血豪情
# gunblader/trouble_shooter/2a0a39184de92acf1c1375e00b77404c
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/2a0a39184de92acf1c1375e00b77404c
class Skill37(PassiveSkill):
    """
    苍暮·战线佣兵化身豪情万丈的荒野统治者， 增加基本攻击力和转职技能攻击力， 部分转职技能附加特殊效果。\n
    [矫捷翻滚]\n
    冷却时间减少1秒； 站立时被攻击或倒地状态下， 可以使用该技能。\n
    在站立时被攻击或倒地状态下， 施放技能后追加无敌判定。\n
    [广域散射]\n
    增加射击范围， 可以强制中断爆剑术系列技能并立即使用。\n
    [可强制中断广域散射的技能]\n
    [剑刃爆弹]、 [爆裂斩]、 [裂地爆刃]、 [完美击球]、 [爆弹华尔兹]、 [铁腕爆弹]\n
    [铁血豪情？ 说的就是我。]
    """
    name = "铁血豪情"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "2a0a39184de92acf1c1375e00b77404c"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [广域散射]射击范围增加率 : {value1}% 
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [ {"data":data0,"type":"*skillRation"}]

# 铁腕爆弹
# gunblader/trouble_shooter/9dc8438e4572d39243c97da31c113acc
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/9dc8438e4572d39243c97da31c113acc
class Skill38(ActiveSkill):
    """
    将锁链连接至捆绑着炸弹的巨型重剑上， 挥动锁链， 引发大范围爆炸， 横扫周围敌人。\n
    旋转重剑时， 将命中的敌人击退至前方。
    """
    name = "铁腕爆弹"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [960, 7200]
    uuid = "9dc8438e4572d39243c97da31c113acc"
    hasVP = False
    hasUP = False

    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 爆炸多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 烽火硝烟·终末之征
# gunblader/trouble_shooter/3fb8395ae3b81bd608e0c4223a8eb534
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/3fb8395ae3b81bd608e0c4223a8eb534
class Skill39(ActiveSkill):
    """
    投掷炸弹使敌人进入特殊灼伤状态， 然后用黑烟覆盖战场， 发动特制陷阱。\n
    然后， 苍暮·战线佣兵在硝烟中骑着摩托车登场， 疾驰在正在启动的陷阱墙面上， 投掷大量的高压爆弹。\n
    陷阱完成时， 苍暮·战线佣兵脱离陷阱， 引发巨大爆炸， 将敌人与陷阱一起炸飞。\n
    [真男人从不回头看爆炸！]\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "烽火硝烟·终末之征"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4025, 8055]
    uuid = "3fb8395ae3b81bd608e0c4223a8eb534"
    hasVP = False
    hasUP = False

    # 投掷炸弹爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 投掷炸弹多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 终结爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'trouble_shooter'
        self.nameCN = '苍暮·战线佣兵'
        self.role = 'gunblader'
        self.角色 = '枪剑士'
        self.职业 = '战线佣兵'
        self.jobId = '986c2b3d72ee0e4a0b7fcfbe786d4e02'
        self.jobGrowId = '6d459bc74ba73ee4fe5cdc4655400193'

        self.武器选项 = ['长刀','小太刀','重剑','源力剑']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '重甲'
        self.buff = 2.00

        super().__init__(equVersion, __name__)
