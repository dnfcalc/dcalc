#986c2b3d72ee0e4a0b7fcfbe786d4e02
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "gunblader/agent/cn/skillDetail"

# 弦月斩
# gunblader/agent/3c5604bdbb0240b8f130f59ab40509c3
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
    position = 6 #TODO
    rangeLv = 3
    cd = 2
    uuid = "3c5604bdbb0240b8f130f59ab40509c3"
    hasVP = False
    hasUP = False

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 浮空力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 穿透射击
# gunblader/agent/92360eab6e1f378902018eca681ac629
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
    hit0 = 1
    # [转职为暗刃时]
    # 发射次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 射击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [范围信息]
    # 子弹发射距离比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)


# 基础精通
# gunblader/agent/5a56514f35cf0270ae8d6c65f8fefd78
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

    associate = [{"type":"*skillRation","data":[i-100 if i>0 else 0 for i in data0],"skills":["斩射"]}]



# 重劈
# gunblader/agent/1fadde0eece18649caddbca7bd58cc2f
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
    position = 2 #TODO
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

# 瞬击
# gunblader/agent/4b2c90ec226fd40e967875aa5eabefb2
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
    position = 4 #TODO
    rangeLv = 2
    cd = 6
    mp = [1, 100]
    uuid = "4b2c90ec226fd40e967875aa5eabefb2"
    hasVP = False
    hasUP = False

    # 挥舞枪身攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1

# 浮空连击
# gunblader/agent/d0cdaca82892e54097f22a1f60817048
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
    position = 2 #TODO
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

# 迅步突袭
# gunblader/agent/9dda3f4a849dba1a288dd65e116860f2
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/9dda3f4a849dba1a288dd65e116860f2
class Skill13(ActiveSkill):
    """
    快速向前方敌人突进。\n
    施放过程中， 再次按技能键、 Z (技能) 键或X (攻击) 键， 可以发动追加攻击。
    """
    name = "迅步突袭"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 8 #TODO
    rangeLv = 2
    cd = 6
    mp = [12, 500]
    uuid = "9dda3f4a849dba1a288dd65e116860f2"
    hasVP = False
    hasUP = True

    # 追加攻击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1

# 连续射击
# gunblader/agent/0969cd4054d93da07708108c0cc1c4b5
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/0969cd4054d93da07708108c0cc1c4b5
class Skill14(ActiveSkill):
    """
    连续射击3次， 对前方的敌人造成伤害。\n
    按向下方向键 + 技能键， 可以向下射击。
    """
    name = "连续射击"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 6
    mp = [40, 292]
    uuid = "0969cd4054d93da07708108c0cc1c4b5"
    hasVP = False
    hasUP = True

    # 第1击和第2击射击攻击力 : {value0}% X 2次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 2
    # 最后射击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 特工秘技
# gunblader/agent/01384bbfc346775d1267fa0bc4ca605f
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/01384bbfc346775d1267fa0bc4ca605f
class Skill15(PassiveSkill):
    """
    主要执行谍战行动的特工的战斗技能。\n
    变更基本攻击、 前冲攻击、 跳跃攻击， 后跳过程中可以一边射击一边与敌人拉开距离。\n
    额外增加物理暴击率与暴击伤害。
    """
    name = "特工秘技"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 1 #TODO
    rangeLv = 3
    uuid = "01384bbfc346775d1267fa0bc4ca605f"
    hasVP = False
    hasUP = False

    # 后跳攻击冷却时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 物理暴击率增加量 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 暴击伤害增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    associate = [ {"type":"*skillRation","data":data2} ]

# 源能护盾
# gunblader/agent/0232c151ef3731c2dede51931a374723
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
    position = 0 #TODO
    rangeLv = 2
    cd = 10
    mp = [23, 241]
    uuid = "0232c151ef3731c2dede51931a374723"
    hasVP = False
    hasUP = True

    # 护盾生命值 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 护盾持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 护盾爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2= 1
    # - 发动[源能提炼]时 -
    # 护盾大小和爆炸范围增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 护盾持续时间增加 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 护盾生命值增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # [源能提炼]叠加数消耗量 : {value6}个
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # 蓄气动作持续时间上限 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    # [范围信息]
    # 护盾大小比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)
    # 爆炸范围比率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9, lambda x = None: x)

# 斩射
# gunblader/agent/0113c8b1306ca76d208f83f2d093dd62
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/0113c8b1306ca76d208f83f2d093dd62
class Skill17(ActiveSkill):
    """
    根据与敌人的距离发动斩击或射击。\n
    可以强制中断技能并发动其他技能， 同时也可以强制中断其他技能后发动该技能。\n
    斩击和射击的攻击力受[基础精通]影响。
    """
    name = "斩射"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 6 #TODO
    rangeLv = 2
    cd = 3
    mp = [199, 199]
    uuid = "0113c8b1306ca76d208f83f2d093dd62"
    hasVP = False
    hasUP = True

    # 斩击/射击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 2
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 迅步闪避
# gunblader/agent/717f1e2104fe4b796f800352fa143ecc
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/717f1e2104fe4b796f800352fa143ecc
class Skill18(PassiveSkill):
    """
    若在[迅步突袭]过程中受到攻击， 则发动[迅步闪避]躲避敌人的攻击。\n
    在[迅步闪避]过程中按[迅步突袭]键或Z (技能) 键、 X (基本攻击) 键， 可以发动具有[迅步突袭]攻击力的追加攻击。\n
    [迅步突袭]过程中也可以通过C (跳跃) 键手动发动。\n
    学习[迅步闪避]后， 可以强制中断特工的各种技能并发动[迅步突袭]。\n
    [可以强制中断的技能]\n
    [弦月斩]、 [瞬击]、 [连续射击]、 [双弦斩]、 [月光挥斩]、 [精准射击]、 [满月斩]、 [锁定射击]、 [枪刃旋杀]终结攻击、 [终极锁定]、 [月相轮舞]
    """
    name = "迅步闪避"
    learnLv = 20
    masterLv = 1
    maxLv = 1
    position = 8 #TODO
    rangeLv = 1
    uuid = "717f1e2104fe4b796f800352fa143ecc"
    hasVP = False
    hasUP = False

    # 发动迅步闪避后无敌时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)

# 双弦斩
# gunblader/agent/eb71e1d82d92c7e1d40500a0dcd77aa6
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/eb71e1d82d92c7e1d40500a0dcd77aa6
class Skill19(ActiveSkill):
    """
    施展2次可发出半月形剑气的剑术攻击敌人。\n
    可以将第一击命中的敌人沿Y轴聚拢。\n
    <连按效果>\n
    在发动第一击后的僵直状态下， 按技能快捷键可以立即连接第二击。
    """
    name = "双弦斩"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 6
    mp = [40, 292]
    uuid = "eb71e1d82d92c7e1d40500a0dcd77aa6"
    hasVP = False
    hasUP = True

    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 小太刀精通
# gunblader/agent/dc1ffbe7bfcc6dc2be737951960da9ad
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/dc1ffbe7bfcc6dc2be737951960da9ad
class Skill20(PassiveSkill):
    """
    精通潜伏的特工擅长使用小太刀。 增加物理攻击力。 装备小太刀时， 增加命中率。
    """
    name = "小太刀精通"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    uuid = "dc1ffbe7bfcc6dc2be737951960da9ad"
    hasVP = False
    hasUP = False

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 命中率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    associate = [
        {"type":"$*PAtkP","data":data1}]

# 月光挥斩
# gunblader/agent/4655101518604f874721b3cc249aae10
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/4655101518604f874721b3cc249aae10
class Skill22(ActiveSkill):
    """
    两手握剑向前突进， 发动交叉斩击。\n
    按向前方向键可以突进更远的距离。
    """
    name = "月光挥斩"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 7
    mp = [15, 300]
    uuid = "4655101518604f874721b3cc249aae10"
    hasVP = False
    hasUP = True

    # 攻击力 : {value0}% X {value1}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 2
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 精准射击
# gunblader/agent/c9664191611af31142e052dfaef84530
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/c9664191611af31142e052dfaef84530
class Skill23(ActiveSkill):
    """
    对前方的敌人自动进行瞄准射击， 造成致命的伤害。\n
    按向下方向键， 可以以坐姿进行瞄准， 此时可以攻击倒地的敌人。\n
    可以强制中断[迅步突袭]并施放[精准射击]。\n
    - [追踪目标]标记附加效果 -\n
    按住技能快捷键， 可以对前方一定范围内的TARGET标记对象进行精准射击。
    """
    name = "精准射击"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 8
    mp = [30, 500]
    uuid = "c9664191611af31142e052dfaef84530"
    hasVP = False
    hasUP = True

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 穿刺几率 : 100%
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 追踪目标
# gunblader/agent/e4c354a89c337310aeb7041d5e742828
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/e4c354a89c337310aeb7041d5e742828
class Skill24(ActiveSkill):
    """
    给稀有、 领主和深渊怪物留下目标标记。\n
    标记自动分配， 普通怪物不会被标记。\n
    存在多个稀有、 领主、 深渊怪物时， 按技能快捷键即可变更标记对象。\n
    长按技能快捷键可以取消标记。\n
    部分技能对有目标标记的敌人发动特殊效果。\n
    [有标记附加效果的技能]\n
    [精准射击]、 [月影秘步]、 [锁定射击]、 [毁灭绝击]、 [终极锁定]、 [夜影迷踪]
    """
    name = "追踪目标"
    learnLv = 30
    masterLv = 1
    maxLv = 1
    position = 3 #TODO
    rangeLv = 3
    uuid = "e4c354a89c337310aeb7041d5e742828"
    hasVP = False
    hasUP = False


# 特工使命
# gunblader/agent/fc7a3f4c2852c832a2f20af63d5d212f
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/fc7a3f4c2852c832a2f20af63d5d212f
class Skill25(ActiveSkill):
    """
    看起来非常普通的特工， 一旦开始执行任务就会变得异于常人。\n
    任务开始的瞬间提升专注力， 增加基本攻击力和技能攻击力。
    """
    name = "特工使命"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 1 #TODO
    rangeLv = 3
    cd = 5
    uuid = "fc7a3f4c2852c832a2f20af63d5d212f"
    hasVP = False
    hasUP = False

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 月影秘步
# gunblader/agent/f2fb27162beb0b87a7cb9af7900e95f2
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/f2fb27162beb0b87a7cb9af7900e95f2
class Skill26(ActiveSkill):
    """
    施展特工的潜行秘技“月影秘步”， 悄悄攻击敌人。\n
    若[月影秘步]施放动作击中敌人， 则对其周围3名敌人发动组合攻击。\n
    [月影秘步]由3套组合攻击组成， 每套组合有2次攻击。 第1套组合攻击成功时， 剩下2套组合攻击可以通过再次按技能键来发动。\n
    可以强制中断每套组合攻击的最后动作并施放其他技能， 施放其他技能过程中也可以强制中断并发动[月影秘步]。\n
    - [追踪目标]标记附加效果 -\n
    每个[月影秘步]组合的最后一击会优先搜索有追踪标记的敌人。\n
    - [可以强制中断的技能] -\n
    [弦月斩]、 [瞬击]、 [连续射击]、 [双弦斩]、 [月光挥斩]、 [精准射击]、 [满月斩]、 [锁定射击]、 [枪刃旋杀]终结攻击、 [终极锁定]、 [月相轮舞]、 [夜影迷踪]
    """
    name = "月影秘步"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 8 #TODO
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [60, 850]
    uuid = "f2fb27162beb0b87a7cb9af7900e95f2"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 每次攻击的攻击力 : {value0}% X {value1}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 18
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 可发动下一套组合攻击的最大有效时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 可搜索目标的最大范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [范围信息]
    # 施放攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    def vp_1(self):
        """
        [月影秘步]\n
        可发动下一套组合攻击的最大有效时间 +4.5秒\n
        取消施放动作， 直接移动到有“TARGET”标记的敌人身边发动攻击\n
        - 若寻敌范围内没有带“TARGET”标记的敌人， 则不会发动\n
        - 变更为只攻击带“TARGET”标记的敌人
        """
        ...

    def vp_2(self):
        """
        [月影秘步]\n
        对一定范围内的敌人发动一套组合攻击\n
        - 对范围内最多10个敌人各进行2次攻击\n
        - 总攻击力相同\n
        - 删除填充效果\n
        - 角色周围1200px内存在敌人时可以施放
        """
        ...

# 满月斩
# gunblader/agent/cfacda0647b9a0f595df2c2aad30c18d
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/cfacda0647b9a0f595df2c2aad30c18d
class Skill27(ActiveSkill):
    """
    持双剑发动旋转攻击， 聚拢周围的敌人后， 发动满月斩造成致命伤害。
    """
    name = "满月斩"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [100, 850]
    uuid = "cfacda0647b9a0f595df2c2aad30c18d"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 旋转攻击攻击力 : {value0}% X {value1}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 3
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 满月斩物理攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [满月斩]\n
        可以强制中断特工转职技能的施放后僵直并施放 (觉醒技能除外)\n
        删除旋转斩击， 直接施放满月斩\n
        - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [满月斩]\n
        旋转攻击吸附力 +30%\n
        旋转攻击吸附范围 +33%\n
        满月斩范围 +40%
        """
        ...

# 锁定射击
# gunblader/agent/e49e57b2e8fbeceb0a2c56a0c63fe6c5
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/e49e57b2e8fbeceb0a2c56a0c63fe6c5
class Skill28(ActiveSkill):
    """
    锁定范围内最近的敌人为目标进行射击。\n
    连续按技能快捷键， 最多可以连续发射12发子弹。\n
    - [追踪目标]标记附加效果 -\n
    优先攻击有追踪标记的敌人。\n
    <连按效果>\n
    各射击和更换弹匣后的僵直状态下， 按技能快捷键可以立即连接下一个[锁定射击]动作。
    """
    name = "锁定射击"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [150, 1260]
    uuid = "e49e57b2e8fbeceb0a2c56a0c63fe6c5"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 12
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 射击高度上限 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [范围信息]
    # 目标锁定范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [锁定射击]\n
        当[锁定射击]的弹匣处于激活状态下施放[毁灭狂欢]时， 额外增加1个弹匣\n
        - [锁定射击]攻击力 -12%\n
        - 最多持有2个弹匣\n
        对周围敌人发动攻击 (包括带“TARGET”标记的敌人)\n
        长按[锁定射击]技能键时自动连续射击
        """
        self.skillRation *= 0.88
        ...

    def vp_2(self):
        """
        [锁定射击]\n
        弹药数量上限变更为6发\n
        - 总攻击力相同\n
        在施放[月影秘步、 [目标锁定]、 [月光镇魂曲]过程中可以使用[锁定射击]\n
        - 使用该功能时， 可以无射击动作进行射击
        """
        ...

# 枪刃旋杀
# gunblader/agent/45442bbbe33540b4deeec29437dae70c
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/45442bbbe33540b4deeec29437dae70c
class Skill29(ActiveSkill):
    """
    向前投掷在旋转中旋转射出子弹的枪， 然后投掷剑刃， 与手枪结合形成枪刃。\n
    枪刃在原地猛烈旋转， 对周围敌人造成伤害并吸附敌人。 枪刃合体后， 经过一定时间后消失。\n
    施放技能时， 按向前方向键时， 可以增加枪和剑刃的投掷距离。\n
    <追加操作>\n
    枪刃消失之前， 再按一次技能键可以发动终结攻击。 终结攻击在施放其他技能过程中也可以发动， 强制中断并施放的技能与[月影秘步]相同。
    """
    name = "枪刃旋杀"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [250, 2500]
    uuid = "45442bbbe33540b4deeec29437dae70c"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 枪投掷攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 剑刃投掷攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 枪刃多段攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 16
    # 终结攻击攻击力 : {value3}% X {value4}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 2
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # [范围信息]
    # 攻击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)

    def vp_1(self):
        """
        [枪刃旋杀]\n
        删除[枪刃旋杀]终结攻击及追加输入功能\n
        - 总攻击力相同\n
        枪刃大小 +30%\n
        枪刃旋杀吸附力 +30%
        """

    def vp_2(self):
        """
        [枪刃旋杀]\n
        [枪刃旋杀]追踪最强的敌人\n
        - 优先攻击带“TARGET标志”的敌人\n
        枪刃旋杀攻击力减少， 但终结一击攻击力增加\n
        - 总攻击力相同
        """
        ...

# 使命觉悟
# gunblader/agent/c27418ae613c647527200a7ca17d97fd
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/c27418ae613c647527200a7ca17d97fd
class Skill30(PassiveSkill):
    """
    增加基本攻击力和技能攻击力， 并增加部分射击技能的寻敌范围。\n
    - [增加寻敌范围的技能] -\n
    [精准射击]、 [终极锁定]
    """
    name = "使命觉悟"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 3
    uuid = "c27418ae613c647527200a7ca17d97fd"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 寻敌范围增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    associate = [ {"data":data0,"type":"*skillRation"}]

# 毁灭绝击
# gunblader/agent/01c3a2fb793d293a25ed8dc7a0d70c1a
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/01c3a2fb793d293a25ed8dc7a0d70c1a
class Skill31(ActiveSkill):
    """
    迅速靠近前方的敌人并抓住目标， 然后发动强力攻击。\n
    - [追踪目标]目标标记附加效果 -\n
    若一定范围内存在被留下目标标记的敌人， 则向有标记的敌人靠近。 攻击[追踪目标]标记的敌人时， 攻击力增加10%。
    """
    name = "毁灭绝击"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [881, 7403]
    uuid = "01c3a2fb793d293a25ed8dc7a0d70c1a"
    hasVP = False
    hasUP = False

    # 攻击力 : {value0}% X 2次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 2
    power0 = 1.1 #以前记录的10%增加

# 终极锁定
# gunblader/agent/8f73f243041c2d27739fe7696f02bf9b
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/8f73f243041c2d27739fe7696f02bf9b
class Skill32(ActiveSkill):
    """
    快速靠近前方一定范围内最近的敌人进行射击， 然后用剑术攻击敌人。\n
    - [追踪目标]标记附加效果 -\n
    优先将前方有追踪标记的敌人设为攻击目标。
    """
    name = "终极锁定"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 8 #TODO
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [400, 1620]
    uuid = "8f73f243041c2d27739fe7696f02bf9b"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 每次攻击的攻击力 : {value0}% X 4次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 4
    # [范围信息]
    # 搜索范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    def vp_1(self):
        """
        [终极锁定]\n
        寻敌角度增加， 对寻敌范围内的所有敌人进行3次射击， 并接近带“TARGET标志”的敌人发动终结斩击\n
        - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [终极锁定]\n
        [终极锁定]施放后， 若突进目标是带“TARGET”标志的敌人， 则留下枪伤标志\n
        - 枪伤标志持续时间 : 10秒\n
        - 向有枪伤标志的方向进行特定射击时， 变更为自动命中\n
        - ([连续射击]、 [精准射击]、 [锁定射击])
        """
        ...

# 月相轮舞
# gunblader/agent/8c2379737c5acc935c1731f67f607655
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/8c2379737c5acc935c1731f67f607655
class Skill33(ActiveSkill):
    """
    模拟月亮的位相变化， 连续发动剑击。\n
    <连按效果>\n
    每次发动剑术后的僵直状态下， 按技能快捷键或X (攻击) 键可以立即连接下一个动作。
    """
    name = "月相轮舞"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 8 #TODO
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [800, 1680]
    uuid = "8c2379737c5acc935c1731f67f607655"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 新月攻击力 : {value0}% X {value1}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 2
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 半月攻击力 : {value2}% X {value3}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 2
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 满月攻击力 : {value4}% X {value5}次
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 2
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # [范围信息]
    # 大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

    def vp_1(self):
        """
        [月相轮舞]\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 25秒\n
        - 单次攻击力 -50%\n
        攻击范围 +50%
        """
        self.cd = 25
        self.skillRation *= 0.5

    def vp_2(self):
        """
        [月相轮舞]\n
        直接施放[满月斩]\n
        - 施放[满月斩]时， 在施放位置出现满月后造成伤害\n
        - 总攻击力相同
        """
        ...

# 冷酷敌意
# gunblader/agent/2f5d03c7848effbc0a23f4df45d9ca46
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/2f5d03c7848effbc0a23f4df45d9ca46
class Skill34(PassiveSkill):
    """
    经过严格训练的特工在任何时候都能冷静地做出判断。\n
    这种特质在危机中更显突出， 使他们能够顺利地完成任务。\n
    增加物理暴击率和暴击伤害。\n
    同时， 减少[迅步突袭]的冷却时间， 以站立状态遭到攻击时， 按Z (技能) 键或[迅步突袭]键可以触发[迅步闪避]。\n
    [冷静的头脑， 冰冷的心]
    """
    name = "冷酷敌意"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 3
    uuid = "2f5d03c7848effbc0a23f4df45d9ca46"
    hasVP = False
    hasUP = False

    # 物理暴击率增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 暴击伤害增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 迅步突袭冷却时间缩短 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    associate = [
        {"type":"*skillRation","data":data1},
        {"type":"+cd","data":[0] + [-1]*maxLv,"skills":["迅步突袭"],"ratio":1},
    ]

# 月光镇魂曲
# gunblader/agent/9cb6f9ed646fa87f9b7680a42ce83d1a
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/9cb6f9ed646fa87f9b7680a42ce83d1a
class Skill35(ActiveSkill):
    """
    전방의 적을 낚아채 잡은 뒤, 날카롭고 치명적인 연속 공격을 가해 처치한다.\n
    <연타 효과>\n
    각 검술/사격 동작의 후 딜레이를 스킬 단축키, X(공격)키 입력을 통해 다음 동작으로 캔슬할 수 있다.
    """
    name = "月光镇魂曲"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "9cb6f9ed646fa87f9b7680a42ce83d1a"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 乱舞攻击力 : {value0}% X {value1}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 9
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [月光镇魂曲]\n
        向带“TARGET”标记的敌人移动并攻击\n
        - 若寻敌范围内没有符合的对象时， 则不会发动该属性效果\n
        - 乱舞攻击次数 -3次\n
        - 总攻击力相同\n
        攻击范围 +10%
        """
        ...

    def vp_2(self):
        """
        [月光镇魂曲]\n
        即使没有命中目标， 也会在原地快速发动月光乱舞， 攻击大范围敌人\n
        - 施放技能时进入无敌状态\n
        - 固定以最快速度发动
        """
        ...

# 毁灭狂欢
# gunblader/agent/4224f9b0b8c7c903e9a1e0f9d9f6d04d
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/4224f9b0b8c7c903e9a1e0f9d9f6d04d
class Skill36(ActiveSkill):
    """
    同时将前方大范围的敌人设为目标， 然后用双枪快速乱射， 歼灭敌人。\n
    - [追踪目标]目标标记附加效果 -\n
    对被留下目标标记的敌人发动追加射击。\n
    <连按效果>\n
    连续按技能快捷键或者X (攻击) 键， 可以加快技能施放速度。
    """
    name = "毁灭狂欢"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [600, 5000]
    uuid = "4224f9b0b8c7c903e9a1e0f9d9f6d04d"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 多段攻击攻击力 : {value0}% X 9次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 11
    # [追踪目标]追加射击次数 : 2次
    # 最后射击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 射击高度上限 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [毁灭狂欢]\n
        向自身周围带<追踪目标>标记的敌人进行乱射攻击\n
        - 无需连按技能键也可以以最大施放速度乱射\n
        Y轴攻击范围 +42%
        """
        ...

    def vp_2(self):
        """
        [毁灭狂欢]\n
        施放[毁灭狂欢]时， 进入射击准备动作8秒， 持续时间结束或再次按下技能键时， 立即施放终结射击\n
        - 删除[毁灭狂欢]多段射击\n
        - 合算至终结射击攻击力\n
        - 总攻击力相同\n
        在射击准备动作中， 可以自由施放部分射击技能代替现有的[毁灭狂欢]多段射击\n
        - 射击准备动作中施放的技能范围适用[毁灭狂欢]的范围， 对范围内所有敌人造成伤害\n
        - 此时使用的射击技能可以取消射击间隔， 伤害与原技能伤害相同\n
        - ([连续射击]、 [精准射击]、 [锁定射击])
        """
        ...

# 月相天陨
# gunblader/agent/78bd107acd474518b606be1e4fd38239
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/78bd107acd474518b606be1e4fd38239
class Skill37(ActiveSkill):
    """
    释放月蚀形态的剑气， 然后在黑暗中乱射剑光与子弹， 将敌人一网打尽。\n
    <连按效果>\n
    连续按技能快捷键或X (攻击) 键， 可以加快技能施放速度。
    """
    name = "月相天陨"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "78bd107acd474518b606be1e4fd38239"
    hasVP = False
    hasUP = False

    # 剑光多段攻击攻击力 : {value0}% X {value1}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 12
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 射击多段攻击攻击力 : {value2}% X {value3}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 9
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 最后一击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1

# 无瑕
# gunblader/agent/0fbb8de70002ad34f046c94c2cb3e863
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/0fbb8de70002ad34f046c94c2cb3e863
class Skill38(PassiveSkill):
    """
    拥有众多能力和强力绝技的人很多， 但没有缺点的人极少。 因此， 苍暮·特工比任何人都更受信赖， 同时也为人所忌惮。\n
    增加基本攻击力和转职技能攻击力， 部分技能附加特殊效果。\n
    [双弦斩]\n
    施展1次斩击， 同时生成2把半月形剑气， 将击中的敌人拉到特工身前。\n
    [精准射击]\n
    瞄准大范围的敌人进行射击， 以相同攻击力对范围内的所有敌人造成伤害。
    """
    name = "无瑕"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "0fbb8de70002ad34f046c94c2cb3e863"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)

    associate = [ {"type":"*skillRation","data":data0}]

# 夜影迷踪
# gunblader/agent/c5a2956d8ed3af1746ed2f76ca971a09
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/c5a2956d8ed3af1746ed2f76ca971a09
class Skill39(ActiveSkill):
    """
    苍暮·特工向前方大幅斩击， 然后融入黑色剑气中隐藏身影。 稍后， 特工出现在剑气命中的敌人中最强大的敌人后方， 发动连续斩击。\n
    - [追踪目标]标记附加效果 -\n
    优先将有追踪标记的敌人设为追踪目标。
    """
    name = "夜影迷踪"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [960, 7200]
    uuid = "c5a2956d8ed3af1746ed2f76ca971a09"
    hasVP = False
    hasUP = False

    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 第3击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1

# 月夜 : 终极行动
# gunblader/agent/e0a072e8cef2d77893aad5f68aeed56a
# 986c2b3d72ee0e4a0b7fcfbe786d4e02/e0a072e8cef2d77893aad5f68aeed56a
class Skill40(ActiveSkill):
    """
    黑暗完全笼罩在苍暮·特工与周围所有敌人身上。 片刻间刀光剑影过后， 特工冷酷地执行完任务， 从黑暗中显露身影并查看时间， 宣告终极行动圆满完成。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "月夜 : 终极行动"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "e0a072e8cef2d77893aad5f68aeed56a"
    hasVP = False
    hasUP = False

    # 多段攻击攻击力 : {value0}% X {value1}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 11
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 终结攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1

class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'agent'
        self.nameCN = '苍暮·特工'
        self.role = 'gunblader'
        self.角色 = '枪剑士'
        self.职业 = '特工'
        self.jobId = '986c2b3d72ee0e4a0b7fcfbe786d4e02'
        self.jobGrowId = '618326026de1a1f1cfba5dbd0b8396e7'

        self.武器选项 = ['长刀','小太刀','重剑','源力剑']
        self.输出类型选项 = ['物理百分比'] # TODO
        self.输出类型 = '物理百分比' # TODO
        self.防具精通属性 = ['力量'] # TODO
        self.防具类型 = '皮甲'
        self.buff = 2.00 # TODO

        super().__init__(equVersion, __name__)
