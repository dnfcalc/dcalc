#a7a059ebe9e6054c0644b40ef316d6e9
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "fighter_female/grappler_female/cn/skillDetail"

# 上勾拳
# fighter_female/grappler_female/eb71e1d82d92c7e1d40500a0dcd77aa6
# a7a059ebe9e6054c0644b40ef316d6e9/eb71e1d82d92c7e1d40500a0dcd77aa6
class Skill0(ActiveSkill):
    """
        向敌人发出上勾拳并使其浮空， 施放的瞬间有霸体判定。\n
        转职为柔道家后， 技能类型变为独立攻击力。
    """
    name = "上勾拳"
    learnLv = 1
    masterLv = 10
    maxLv = 20
    position = 3
    rangeLv = 3
    cd = 2
    uuid = "eb71e1d82d92c7e1d40500a0dcd77aa6"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 浮空攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 浮空力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 发动速度增加量 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 前踢
# fighter_female/grappler_female/fc7a3f4c2852c832a2f20af63d5d212f
# a7a059ebe9e6054c0644b40ef316d6e9/fc7a3f4c2852c832a2f20af63d5d212f
class Skill1(ActiveSkill):
    """
        向敌人发出强威力的踢腿， 可以踢飞敌人。
    """
    name = "前踢"
    learnLv = 1
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 3
    mp = [10, 112]
    uuid = "fc7a3f4c2852c832a2f20af63d5d212f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 踢击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 击飞力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)



# 下段踢
# fighter_female/grappler_female/4655101518604f874721b3cc249aae10
# a7a059ebe9e6054c0644b40ef316d6e9/4655101518604f874721b3cc249aae10
class Skill6(ActiveSkill):
    """
        格斗家特有的快速下段踢。\n
        命中时引发冲击波， 对周围敌人造成伤害。
    """
    name = "下段踢"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 2
    mp = [10, 112]
    uuid = "4655101518604f874721b3cc249aae10"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 下段踢攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 发动速度增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 冲击波大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)


# 背摔
# fighter_female/grappler_female/cfacda0647b9a0f595df2c2aad30c18d
# a7a059ebe9e6054c0644b40ef316d6e9/cfacda0647b9a0f595df2c2aad30c18d
class Skill8(ActiveSkill):
    """
        抓住前方敌人并猛力把其倒摔向背后地面。\n
        施放[背摔]时有无敌判定， 把敌人摔到地面的瞬间生成冲击波， 可以对周围的敌人造成伤害。\n
        可以抓取霸体和防御状态的敌人， 但对无法抓取的敌人不适用抓取和控制效果。\n
        转职为柔道家后， 技能类型变为独立攻击力， 并根据抓取的敌人大小， 增加冲击波大小， 冲击波攻击力与抓取的敌人攻击力相同。\n
        此外， 因受抓轰炮效果， 可以攻击无法抓取的敌人， 这时可以大幅击退敌人进行攻击。
    """
    name = "背摔"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 5
    mp = [20, 168]
    uuid = "cfacda0647b9a0f595df2c2aad30c18d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 冲击波大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 学习[雷霆背摔]后， 闪电大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 蹲伏
# fighter_female/grappler_female/9dda3f4a849dba1a288dd65e116860f2
# a7a059ebe9e6054c0644b40ef316d6e9/9dda3f4a849dba1a288dd65e116860f2
class Skill9(ActiveSkill):
    """
        蹲下并避开敌人的上段判定式攻击。\n
        若在前冲中使用此技能， 可以边向前滑行边蹲下。\n
        蹲下时进入无敌状态， 起身的瞬间也会进入无敌状态。\n
        [蹲伏]姿势中按攻击键， 可以用肩尖撞击敌人； 经过一定时间或按跳跃键可以中断蹲伏状态。
    """
    name = "蹲伏"
    learnLv = 10
    masterLv = 1
    maxLv = 11
    position = 0 #TODO
    rangeLv = 1
    cd = 3
    mp = [3, 4]
    uuid = "9dda3f4a849dba1a288dd65e116860f2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 姿势持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 肩撞攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 钢筋铁骨
# fighter_female/grappler_female/c9664191611af31142e052dfaef84530
# a7a059ebe9e6054c0644b40ef316d6e9/c9664191611af31142e052dfaef84530
class Skill10(PassiveSkill):
    """
        使自身的身体强悍如钢铁， 并增加一定的物防和体力。\n
        被攻击时， 有一定几率进入霸体状态。
    """
    name = "钢筋铁骨"
    learnLv = 10
    masterLv = 50
    maxLv = 60
    position = 5
    rangeLv = 3
    uuid = "c9664191611af31142e052dfaef84530"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 物理防御力增加量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 体力增加量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 霸体状态发动几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 抛沙
# fighter_female/grappler_female/8f73f243041c2d27739fe7696f02bf9b
# a7a059ebe9e6054c0644b40ef316d6e9/8f73f243041c2d27739fe7696f02bf9b
class Skill11(ActiveSkill):
    """
        卑鄙地抛出沙子攻击敌人。\n
        攻击时， 有一定几率使敌人进入失明状态。\n
        转职为街霸后， 可中断基本攻击使用
    """
    name = "抛沙"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 3
    mp = [15, 154]
    uuid = "8f73f243041c2d27739fe7696f02bf9b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 沙尘攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [失明效果]
    # 失明几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 失明持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 视野减少率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 命中率减少率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [发动涂毒时附加中毒攻击力]
    # 沙尘命中时中毒攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 沙尘大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

# 鹰踏
# fighter_female/grappler_female/78bd107acd474518b606be1e4fd38239
# a7a059ebe9e6054c0644b40ef316d6e9/78bd107acd474518b606be1e4fd38239
class Skill12(ActiveSkill):
    """
        在空中跳跃着踩踏敌人并给予敌人一定伤害。\n
    可以连续对敌人进行一定次数的踩踏， 技能的冷却时间从最后一次踩踏结束落地时开始计算。
    """
    name = "鹰踏"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cd = 7
    mp = [10, 97]
    uuid = "78bd107acd474518b606be1e4fd38239"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 踩踏攻击力 : {value0}%
    # data0 = get_data(f'{prefix}/{uuid}', 0)
    data0 = [0, 605, 667, 728, 789, 851, 912, 974, 1035, 1096, 1158, 1219, 1281, 1342, 1403, 1465, 1526, 1588, 1649, 1710, 1772, 1833, 1895, 1956, 2017, 2079, 2140, 2202, 2263, 2324, 2386, 2447, 2509, 2570, 2631, 2693, 2754, 2816, 2877, 2938, 3000, 3061, 3123, 3184, 3245, 3307, 3368, 3430, 3491, 3552, 3614, 3675, 3737, 3798, 3859, 3921, 3982, 4044, 4105, 4166, 4228, 4289, 4351, 4412, 4473, 4535, 4596, 4658, 4719, 4780, 4842]# noqa: E501
    hit0 = 1
    # 踩踏次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后踩踏攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

# 疾风追击
# fighter_female/grappler_female/dcb31a63ef58954f44ff2070c42a9a98
# a7a059ebe9e6054c0644b40ef316d6e9/dcb31a63ef58954f44ff2070c42a9a98
class Skill13(ActiveSkill):
    """
        如同老虎一样发动快速的连续攻击。\n
        学习后， 前冲攻击不会使敌人倒地。\n
        前冲攻击后， 按攻击键或技能键， 可以进行追击， 但每一击会消耗自身一定量的魔法值。\n
        学习[疾风连击]后可再追加第3、 第4次攻击。
    """
    name = "疾风追击"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 9
    rangeLv = 2
    cd = 2
    mp = [8, 67]
    uuid = "dcb31a63ef58954f44ff2070c42a9a98"
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

# 金刚碎
# fighter_female/grappler_female/4f2e001e9a19eb7bae50ad1840dfb329
# a7a059ebe9e6054c0644b40ef316d6e9/4f2e001e9a19eb7bae50ad1840dfb329
class Skill14(ActiveSkill):
    """
        向前方小跳后用拳猛击地面， 引发冲击波使敌人受到伤害并倒地。\n
        施放时， 可以用上下方向键控制攻击地点。\n
        在决斗场中， 浮空力和施放后僵直时间根据技能等级发生变化。\n
        转职为柔道家后， 可以强制中断基本攻击并立即施放[金刚碎]， 并且还可以中断[金刚碎]并立即施放[霹雳肘击]。
    """
    name = "金刚碎"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 1
    rangeLv = 2
    cd = 5
    mp = [20, 238]
    uuid = "4f2e001e9a19eb7bae50ad1840dfb329"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 浮空力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 施放后的僵直时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 摔技强化
# fighter_female/grappler_female/ff171dc487807bb9aa28900ca9a46b41
# a7a059ebe9e6054c0644b40ef316d6e9/ff171dc487807bb9aa28900ca9a46b41
class Skill18(PassiveSkill):
    """
        增加基本攻击力和技能攻击力。\n
        使用[背摔]、 [抛投]、 [霹雳肘击]、 [空绞锤]、 [螺旋彗星落]、 [地狱摇篮]、 [裂石破天]、 [末日风暴]、 [死亡摇篮]、 [末日摇篮]技能时， 可以增加冲击波和攻击范围。
    """
    name = "摔技强化"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 7
    rangeLv = 3
    uuid = "ff171dc487807bb9aa28900ca9a46b41"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 周围攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [{"data":data0}]

# 抛投
# fighter_female/grappler_female/c27418ae613c647527200a7ca17d97fd
# a7a059ebe9e6054c0644b40ef316d6e9/c27418ae613c647527200a7ca17d97fd
class Skill19(ActiveSkill):
    """
        抓取敌人并向前方抛摔。\n
        抓取敌人后， 再次按技能键或抓取时间结束就可以抛摔敌人。 抛摔敌人时会进入无敌状态， 此时可以通过方向键指定抛摔方向。\n
        被抛摔的敌人撞到墙壁或地面时会产生冲击波， 对周围敌人也造成伤害。 根据抓取的敌人大小增加冲击波大小， 撞到墙壁落地时不会再出现冲击波。\n
        抓轰炮发动后， 与敌人力量制衡一定时间后强力推开造成伤害。\n
        在决斗场中， 技能等级越高， 抓取持续时间越长。
    """
    name = "抛投"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 8.5
    mp = [30, 336]
    uuid = "c27418ae613c647527200a7ca17d97fd"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 抓取时间上限 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 撞到地面时的冲撞攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 撞到墙壁时的冲撞攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 冲击波大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 暴力抓取
# fighter_female/grappler_female/92360eab6e1f378902018eca681ac629
# a7a059ebe9e6054c0644b40ef316d6e9/92360eab6e1f378902018eca681ac629
class Skill20(ActiveSkill):
    """
        使[背摔]、 [抛投]、 [霹雳肘击]、 [空绞锤]、 [螺旋彗星落]、 [地狱摇篮]、 [裂石破天]、 [末日风暴]、 [死亡摇篮]、 [末日摇篮]、 [风暴之舞]、 [苍宇彗星落]、 [送葬舞步]的技能抓取动作出现霸体判定， 并且抓取命中率变成100%， 同时还增加基本攻击和抓取类技能的攻击力， 效果持续一定时间。
    """
    name = "暴力抓取"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 4
    rangeLv = 3
    cd = 5
    uuid = "92360eab6e1f378902018eca681ac629"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击和抓取技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 滑行抓取
# fighter_female/grappler_female/1fadde0eece18649caddbca7bd58cc2f
# a7a059ebe9e6054c0644b40ef316d6e9/1fadde0eece18649caddbca7bd58cc2f
class Skill21(PassiveSkill):
    """
        在前冲状态下使用[背摔]、 [抛投]、 [空绞锤]、 [地狱摇篮]、 [末日风暴]、 [死亡摇篮]、 [苍宇彗星落]、 [送葬舞步]技能时， 可以滑行抓取敌人。\n
        滑行抓取敌人时， 可以用方向键进行上下滑行； 技能等级越高， 滑行速度越快。
    """
    name = "滑行抓取"
    learnLv = 15
    masterLv = 1
    maxLv = 11
    position = 2
    rangeLv = 3
    uuid = "1fadde0eece18649caddbca7bd58cc2f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 滑行速度 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

# 抓轰炮
# fighter_female/grappler_female/d2c6df5105577fb59fb92529a36165a0
# a7a059ebe9e6054c0644b40ef316d6e9/d2c6df5105577fb59fb92529a36165a0
class Skill22(PassiveSkill):
    """
        学习后， 对无法抓取或固定型敌人进行抓取时， 发动抓轰炮效果， 给予敌人强力伤害。 抓轰炮攻击时会产生冲击波， 对周围敌人造成伤害。\n
    [发动抓轰炮效果的技能]\n
    [背摔]、 [抛投]、 [空绞锤]、 [霹雳肘击]、 [螺旋彗星落]、 [地狱摇篮]、 [死亡摇篮]、 [末日摇篮]\n
        抓轰炮的攻击力相当于各技能的抓起攻击力总和。
    """
    name = "抓轰炮"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 1
    rangeLv = 1
    uuid = "d2c6df5105577fb59fb92529a36165a0"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

# 强力抱摔
# fighter_female/grappler_female/2f5d03c7848effbc0a23f4df45d9ca46
# a7a059ebe9e6054c0644b40ef316d6e9/2f5d03c7848effbc0a23f4df45d9ca46
class Skill23(PassiveSkill):
    """
        强化柔道家的基本攻击和抓取技能， 增加攻击力和对敌人造成致命一击的概率。\n
    攻击力增加的技能 : [背摔]、 [抛投]、 [霹雳肘击]、 [空绞锤]、 [螺旋彗星落]、 [地狱摇篮]、 [裂石破天]、 [末日风暴]、 [死亡摇篮]、 [末日摇篮]、 [风暴之舞]、 [苍宇彗星落]、 [送葬舞步]、 [女皇时代·辉煌舞台]。
    """
    name = "强力抱摔"
    learnLv = 20
    masterLv = 1
    maxLv = 11
    position = 6
    rangeLv = 5
    uuid = "2f5d03c7848effbc0a23f4df45d9ca46"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击和抓取技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [{"data":data0,"skills":["背摔","抛投","霹雳肘击","空绞锤","螺旋彗星落","地狱摇篮","裂石破天","末日风暴","死亡摇篮","末日摇篮","风暴之舞","苍宇彗星落","送葬舞步","女皇时代·辉煌舞台"]}]# noqa: E501

# 折颈
# fighter_female/grappler_female/ecc23c980ea71450c0ad0c3fd232f329
# a7a059ebe9e6054c0644b40ef316d6e9/ecc23c980ea71450c0ad0c3fd232f329
class Skill24(ActiveSkill):
    """
        可以强制被自身击中的敌人转身， 并短暂的强制控制转身后的敌人。\n
        无法使固定型敌人转身。\n
        在决斗场中， 命中时使敌人浮空并强控敌人。
    """
    name = "折颈"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 7.7
    mp = [30, 336]
    uuid = "ecc23c980ea71450c0ad0c3fd232f329"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 敌人强制控制时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [各类型敌人的强制控制时间比率]
    # 稀有/领主/人形护甲 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 疾风连击
# fighter_female/grappler_female/8572675ec6a1f50b6eff6a867376c2de
# a7a059ebe9e6054c0644b40ef316d6e9/8572675ec6a1f50b6eff6a867376c2de
class Skill25(PassiveSkill):
    """
        施放[疾风追击]时， 可以向敌人发出第3、 4击。
    """
    name = "疾风连击"
    learnLv = 20
    masterLv = 1
    maxLv = 1
    position = 9
    rangeLv = 1
    uuid = "8572675ec6a1f50b6eff6a867376c2de"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

# 无情抓取
# fighter_female/grappler_female/7ec521d063d2190e1fcc5bd229af9bcf
# a7a059ebe9e6054c0644b40ef316d6e9/7ec521d063d2190e1fcc5bd229af9bcf
class Skill26(ActiveSkill):
    """
        [抓轰炮]施放过程中可以使用的技能。 攻击成功时， 使敌人进入控制状态， 并且可以连接使用[折颈]、 [霹雳冲击]或其他抓取类技能。\n
        在地面或空中施放时， 拥有不同的攻击姿态。\n
    [地面施放时]\n
     - 暴力拦截 : 使用肩膀大力冲撞敌人。\n
    [空中施放时]\n
     - 抓取空翻 : 抓取敌人后， 施展强力的空翻踢。\n
     - 暴力关节 : 空翻后， 在一段时间内追加按下技能键时， 快速地从空中向下拳击。\n
        拥有特有的重复等待时间， 并且拥有最大可使用次数。\n
        消耗最大可使用次数后， 一段时间后会自动恢复。
    """
    name = "无情抓取"
    learnLv = 20
    masterLv = 1
    maxLv = 1
    position = 1
    rangeLv = 2
    mp = [30, 30]
    uuid = "7ec521d063d2190e1fcc5bd229af9bcf"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # [无情抓取]最大储存次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [无情抓取]恢复所需时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)


# 野蛮冲撞
# fighter_female/grappler_female/0232c151ef3731c2dede51931a374723
# a7a059ebe9e6054c0644b40ef316d6e9/0232c151ef3731c2dede51931a374723
class Skill28(ActiveSkill):
    """
        向前滑行的同时用肩部猛力撞击敌人。\n
        命中敌人后， 可以立即连接除[蹲伏]和[空中抓取]之外的转职技能。\n
        长按技能键可蓄气， 蓄气后可以向敌人发出更快更威力的撞击， 达最大蓄气时有霸体判定。\n
        若前冲时使用， 则可以边向前滑行边蓄气。
    """
    name = "野蛮冲撞"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 8
    mp = [50, 420]
    uuid = "0232c151ef3731c2dede51931a374723"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 蓄气时间上限 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

# 旋风腿
# fighter_female/grappler_female/202edb928046f4fa6dedf6337377efd5
# a7a059ebe9e6054c0644b40ef316d6e9/202edb928046f4fa6dedf6337377efd5
class Skill29(ActiveSkill):
    """
        快速旋转身体向前移动并用连续的扫腿攻击周围的敌人； 可以在地面或空中使用， 最后的扫腿还可以击倒敌人。\n
        施放后， 可以按上/下方向键改变移动方向， 或按跳跃键中断技能。\n
        转职成为散打时， 可以强制中断基本攻击动作， 并立即施放该技能。
    """
    name = "旋风腿"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 9
    rangeLv = 2
    cd = 8
    mp = [50, 420]
    uuid = "202edb928046f4fa6dedf6337377efd5"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 回旋踢攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 空绞锤
# fighter_female/grappler_female/1721e94897e9961d5c98130a13392f17
# a7a059ebe9e6054c0644b40ef316d6e9/1721e94897e9961d5c98130a13392f17
class Skill30(ActiveSkill):
    """
        在空中用双腿夹住敌人并砸向地面。\n
        冲击波的范围随敌人的体型增加。 抓取失败时， 剩余冷却时间变更为1秒。\n
        发动[抓轰炮]时， 踢中敌人后向上跳起造成伤害。\n
        决斗场中无法在[后跳]中施放。
    """
    name = "空绞锤"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cd = 7
    mp = [50, 420]
    uuid = "1721e94897e9961d5c98130a13392f17"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 抓取失败时剩余技能冷却时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 冲击波大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 霹雳肘击
# fighter_female/grappler_female/b8f4966608e4ebb3cc80ba4eac3649bb
# a7a059ebe9e6054c0644b40ef316d6e9/b8f4966608e4ebb3cc80ba4eac3649bb
class Skill31(ActiveSkill):
    """
        抓起倒地的敌人， 并用强劲的肘击攻击该敌人使其受到巨大伤害， 同时还会生成冲击波使周围的敌人受到一定的伤害。\n
        抓轰炮发动后， 用肘击对敌人造成大伤害。\n
        施放后僵直时间较长。
    """
    name = "霹雳肘击"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 12
    mp = [50, 420]
    uuid = "b8f4966608e4ebb3cc80ba4eac3649bb"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 冲击波扩大率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 螺旋彗星落
# fighter_female/grappler_female/d085127b0edd719782bd618d5688f4a1
# a7a059ebe9e6054c0644b40ef316d6e9/d085127b0edd719782bd618d5688f4a1
class Skill32(ActiveSkill):
    """
        旋转一圈， 并抓取一定范围内的所有敌人向空中跳跃， 然后再将敌人用力砸向地面使其受到极大伤害。\n
        跳跃时可以按方向键改变方向； 砸到地面时产生的冲击波会对周围被冲击波命中的敌人造成伤害； 根据抓取的敌人大小， 增加冲击波大小。\n
        长按技能键， 跳跃高度会随着持续时间增加， 可以跳得更高。\n
        抓轰炮发动后， 在旋转中强控敌人后强力推开敌人。
    """
    name = "螺旋彗星落"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [150, 1260]
    uuid = "d085127b0edd719782bd618d5688f4a1"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 冲击波大小比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [螺旋彗星落]\n
        抓取、 冲击波范围 +50%\n
        跳跃及下砸速度 +30%\n
        跳跃中移动速度 +30%
        """
        ...

    def vp_2(self):
        """
        [螺旋彗星落]\n
        抓取成功时， 旋转后开始立即攻击\n
         - 删除长按技能键功能\n
         - 滑行抓取过程中成功抓取敌人时， 会靠近敌人后停止移动并立即开始攻击\n
        发动[抓轰炮]时， 恢复1次[无情抓取]使用次数
        """
        ...

# 格斗专精
# fighter_female/grappler_female/d429147c372b549c3dadcabcba50787f
# a7a059ebe9e6054c0644b40ef316d6e9/d429147c372b549c3dadcabcba50787f
class Skill33(PassiveSkill):
    """
        学习技能后， [金刚碎]、 [折颈]、 [野蛮冲撞]、 [霹雳冲击]、 [旋风轰击]可以获得以下技能效果。\n
    - [强力抱摔]\n
    - [暴力抓取]\n
    - [抓取奥义]\n
    - [极手奥义]\n
        以下技能连续抓取敌人时变得更加有利。\n
    [背摔] : 攻击中可以强制中断并施放[霹雳肘击]。\n
    [霹雳肘击] : 减少把敌人击飞的力量和攻击后的延迟。\n
    [空绞锤] : 被向下捶击击倒的敌人更久地躺在地上。
    """
    name = "格斗专精"
    learnLv = 35
    masterLv = 1
    maxLv = 1
    position = 4
    rangeLv = 2
    uuid = "d429147c372b549c3dadcabcba50787f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

# 霹雳冲击
# fighter_female/grappler_female/ac21c02567f04a92b54dd85c091d1e5a
# a7a059ebe9e6054c0644b40ef316d6e9/ac21c02567f04a92b54dd85c091d1e5a
class Skill34(ActiveSkill):
    """
        用肘部攻击前方敌人， 然后旋转跳起， 用膝盖撞击敌人。\n
        攻击成功时， 产生强力冲击波， 对周围敌人造成伤害。 直接命中的敌人不受冲击波伤害。\n
        肘部攻击和膝盖撞击前， 按向前方向键， 可以增加前进距离。\n
        肘部攻击成功时， 角色停止移动； 膝盖撞击成功时， 可以强制中断释放后僵直并立即连接可在空中施放的技能。\n
    [可以强制中断的技能]\n
    [旋风腿]、 [野蛮冲撞]、 [空绞锤]、 [裂石破天]、 [旋风轰击]、 [死亡摇篮] (随机应变)、 [风暴之舞]、 [苍宇彗星落] (随机应变)、 [送葬舞步]、 [女皇时代·辉煌舞台]
    """
    name = "霹雳冲击"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [150, 1260]
    uuid = "ac21c02567f04a92b54dd85c091d1e5a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 肘击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 膝撞攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [霹雳冲击]\n
        向前方一定范围内最强敌人的位置突进\n
         - 寻敌范围内不存在敌人时， 无法使用技能\n
        被肘击命中的敌人会进入强制控制状态1.5秒
        """
        ...

    def vp_2(self):
        """
        [霹雳冲击]\n
        肘击后不再跳跃， 旋转身体后进行强力踢击\n
         - 强力踢击命中时， 可以强制中断施放后僵直， 并施放可以在地面施放的转职技能\n
        直接攻击的Y轴攻击范围 +20%\n
        冲击波Y轴攻击范围 +70%
        """
        ...

# 地狱摇篮
# fighter_female/grappler_female/7e904ea3d2a9faa054604e55120a9268
# a7a059ebe9e6054c0644b40ef316d6e9/7e904ea3d2a9faa054604e55120a9268
class Skill35(ActiveSkill):
    """
        抓住敌人发动数次[背摔]造成伤害后， 跳跃踢出强力的最后一击。\n
        通过[背摔]旋转途中， 可按方向键移动， 最后一击动作途中可取消施放后僵直后发动空中技能， 并根据抓取的敌人大小， 增加冲击波大小。\n
        抓轰炮发动时， 进行冲撞及旋转攻击后发动相当于所有[背摔]旋转攻击力的最后一击。 抓取动作中按技能键时， 立即发动最后一击。\n
    [可以强制中断的技能]\n
    [旋风腿]、 [野蛮冲撞]、 [空绞锤]、 [裂石破天]、 [旋风轰击]、 [死亡摇篮] (随机应变)、 [风暴之舞]、 [苍宇彗星落] (随机应变)、 [送葬舞步]、 [女皇时代·辉煌舞台]
    """
    name = "地狱摇篮"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [220, 1988]
    uuid = "7e904ea3d2a9faa054604e55120a9268"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # [背摔]旋转攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 旋转次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 旋转中移动速度增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最后一击攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 冲击波扩大率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [地狱摇篮]\n
        抓取失败时剩余冷却时间变更为4秒\n
        旋转速度 +30%\n
        旋转中移动速度 +100%\n
        发动[抓轰炮]时施放最后一击\n
        旋转、 最后一击冲击波范围 +30%
        """
        ...

    def vp_2(self):
        """
        [地狱摇篮]\n
        变更为可以在空中施放\n
        可以强制中断转职技能的施放后僵直并施放[地狱摇篮]
        """
        ...

# 裂石破天
# fighter_female/grappler_female/d53301bb328baf12a3ae482cc6a565dd
# a7a059ebe9e6054c0644b40ef316d6e9/d53301bb328baf12a3ae482cc6a565dd
class Skill36(ActiveSkill):
    """
        快速从空中下坠并抓取一名敌人， 用力砸向地面。 拖行一段距离时， 使敌人受到多段攻击伤害； 最后巨岩会爆炸， 对敌人造成巨大的伤害。\n
        根据抓取的敌人大小， 增加攻击范围， 落地前或落地时， 输入向后或下方向键， 可以大幅减少下降角度和抓取敌人后的移动距离。\n
        无法抓取的敌人无法向前拖行， 但可以强制控制攻击范围内的敌人。 爆炸结束后， 解除强制控制并造成伤害。 这时地面多段攻击力会相加到最后爆炸攻击力。\n
    [随机应变]\n
        学习后， 抓取判定消失， 用力锤击地面击起岩石， 对范围内敌人造成大量伤害。 落地前或落地时， 输入向后或下方向键， 可以减少下降角度。
    """
    name = "裂石破天"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [360, 3024]
    uuid = "d53301bb328baf12a3ae482cc6a565dd"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 地面冲撞冲击波攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 地面多段攻击力 : {value1} x {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 3
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最后岩石生成攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 最后岩石爆炸攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # [随机应变]
    # 攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 0
    # [范围信息]
    # 攻击范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    useAdapt = 0

    def setMode(self, mode = None):
        if self.useAdapt:
            self.hit5 = 1
            self.hit0 = self.hit1 = self.hit3 = self.hit4 = 0

    def vp_1(self):
        """
        [裂石破天]\n
        变更为可填充2次的技能\n
         - 每次填充冷却时间 : 22.5秒\n
         - 单次攻击力 -50%\n
        [普通]\n
        最初生成岩石后角色可以移动\n
        最后一击岩石生成数量 +2\n
        [随机应变]\n
        施放时立即发动[极手奥义]效果\n
        攻击范围 +50%
        """
        ...
        self.cd = 22.5
        self.skillRation *= 1 - 0.5

    def vp_2(self):
        """
        [裂石破天]\n
        - 基本冷却时间变更为67.5秒\n
        总攻击力 +50%\n
        [普通]\n
        无论是否抓取成功， 技能施放技能时进入无敌状态\n
        [随机应变]\n
        技能施放技能时进入无敌状态
        """
        ...
        self.cd = 67.5
        self.skillRation *= 1 + 0.5

# 抓取奥义
# fighter_female/grappler_female/b163d099c8cc27fdb6fd3639c2ee6df9
# a7a059ebe9e6054c0644b40ef316d6e9/b163d099c8cc27fdb6fd3639c2ee6df9
class Skill37(PassiveSkill):
    """
        将抓取动作提升到极致， 增加暴风眼的基本攻击、 抓取类技能的攻击力、 物理暴击率、 命中率和抓取时的回避率。
    """
    name = "抓取奥义"
    learnLv = 48
    masterLv = 30
    maxLv = 40
    position = 4
    rangeLv = 3
    uuid = "b163d099c8cc27fdb6fd3639c2ee6df9"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击和抓取技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理暴击率增加量 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 命中率增加量 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 抓取准备动作时回避率增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    associate = [{"data":data0}]

# 末日风暴
# fighter_female/grappler_female/d296043df164385a14cb973c8c7c4d07
# a7a059ebe9e6054c0644b40ef316d6e9/d296043df164385a14cb973c8c7c4d07
class Skill38(ActiveSkill):
    """
        抓取一名敌人后快速旋转并在自身周围生成一个巨大风暴， 风暴周围的敌人也会卷进来， 并受到持续伤害。\n
        随后， 暴风眼跃入空中， 以强力终结一拳下砸敌人并产生冲击波， 对敌人造成巨大伤害。\n
        抓取敌人后， 可以用方向键移动， 并吸附周围的敌人。 无法抓取的敌人无法移动， 抓取对象为建筑型时， 角色也无法移动， 但增加吸附周围敌人的范围。\n
        旋转中连按<X>键时， 增加旋转速度、 减少多段攻击间隔； 按技能键或<Z>键时， 立即发动最后一击。
    """
    name = "末日风暴"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 5
    cube = 5
    cd = 140
    mp = [900, 7559]
    uuid = "d296043df164385a14cb973c8c7c4d07"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 风暴攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 13
    # 回旋持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 风暴多段攻击间隔 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最后一击攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 最后一击冲击波范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 旋风轰击
# fighter_female/grappler_female/7f80b887a09e88e2c4728c898bd73654
# a7a059ebe9e6054c0644b40ef316d6e9/7f80b887a09e88e2c4728c898bd73654
class Skill39(ActiveSkill):
    """
        猛踏地面， 跃起旋转后快速下冲， 引发强力冲击波， 对范围内敌人造成伤害。\n
        下降前按前方向键可朝前方突进。\n
        引发冲击波后可以强制中断施放后僵直并施放转职系列技能， 此时按住后方向键可向后施放技能。\n
        空中也可施放技能， 此时立即开始旋转。
    """
    name = "旋风轰击"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [292, 988]
    uuid = "7f80b887a09e88e2c4728c898bd73654"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 冲击波攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [旋风轰击]\n
        变更为可填充2次的技能\n
         - 每次填充冷却时间 : 12.5秒\n
         - 单次攻击力 -50%\n
        冲击波范围 +30%
        """
        self.cd = 12.5
        self.skillRation *= 1 - 0.5
        ...

    def vp_2(self):
        """
        [旋风轰击]\n
        技能施放技能时进入无敌状态\n
        被冲击波命中的敌人会进入眩晕状态3秒
        """
        ...

# 死亡摇篮
# fighter_female/grappler_female/c5a2956d8ed3af1746ed2f76ca971a09
# a7a059ebe9e6054c0644b40ef316d6e9/c5a2956d8ed3af1746ed2f76ca971a09
class Skill40(ActiveSkill):
    """
        抓取敌人， 跳跃后砸向地面并开始旋转， 然后吸附所有旋转移动路径上的敌人， 用强力的跳跃踢技对敌人造成巨大伤害。\n
        旋转时可以用方向键控制左右移动方向， 按下方向键可以在原地旋转并发动最后一击。\n
        根据抓取的敌人大小， 增加冲击波大小， 最后一击动作途中可取消施放后僵直， 发动空中技能。\n
        抓轰炮发动时， 进行冲撞及旋转攻击后， 发动相当于所有旋转攻击力总和的最后一击。\n
    [可以强制中断的技能]\n
    [旋风腿]、 [野蛮冲撞]、 [空绞锤]、 [裂石破天]、 [旋风轰击]、 [风暴之舞]、 [苍宇彗星落] (随机应变)、 [送葬舞步]、 [女皇时代·辉煌舞台]\n
    [随机应变]\n
        学习后， 抓取判定消失， 旋转并腾空跳起攻击敌人。 按下方向键可以在原地发动攻击力。 可以在空中使用。
    """
    name = "死亡摇篮"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [840, 1764]
    uuid = "c5a2956d8ed3af1746ed2f76ca971a09"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 翻转攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 最后一击攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [学习随机应变后]
    # 旋转攻击攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 0
    # [范围信息]
    # 冲击波大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    useAdapt = 0

    def setMode(self, mode = None):
        if self.useAdapt and not self.vp == 1:
            self.hit2 = 1
            self.hit0 = self.hit1 = 0

    def vp_1(self):
        """
        [死亡摇篮]\n
        不再受[随机应变]的影响\n
        删除抓取动作， 施放时立即在原地旋转并吸附周围的敌人\n
         - 删除翻转攻击力\n
         - 总攻击力相同\n
         - 方向键输入功能无效
        """
        ...

    def vp_2(self):
        """
        [死亡摇篮]\n
        [普通]\n
        通过[滑行抓取]施放时， 向前方一定范围内最强敌人的位置突进\n
        最后一击攻击后再次按技能键时， 快速落地\n
        [随机应变]\n
        追踪并下踢前方范围内最强的敌人\n
        施放时立即发动[极手奥义]效果\n
        攻击后再次按技能键时快速落地
        """
        ...

# 极手奥义
# fighter_female/grappler_female/5892d1fa4462e561ac8f8d2c74892b0a
# a7a059ebe9e6054c0644b40ef316d6e9/5892d1fa4462e561ac8f8d2c74892b0a
class Skill41(PassiveSkill):
    """
        抓取成功时， 可增加基本攻击力和抓取技能的攻击力， 该效果持续一定时间。\n
    [效果适用技能]\n
    [背摔]、 [抛投]、 [霹雳肘击]、 [空绞锤]、 [螺旋彗星落]、 [裂石破天]、 [末日风暴]、 [死亡摇篮]、 [末日摇篮]、 [风暴之舞]、 [苍宇彗星落]、 [送葬舞步]、 [女皇时代·辉煌舞台]
    """
    name = "极手奥义"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 3
    uuid = "5892d1fa4462e561ac8f8d2c74892b0a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 增益效果持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 效果叠加次数上限 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    associate = [{"data":data0}]

# 末日摇篮
# fighter_female/grappler_female/fc458e449ee00b01dbf88d09aae65462
# a7a059ebe9e6054c0644b40ef316d6e9/fc458e449ee00b01dbf88d09aae65462
class Skill42(ActiveSkill):
    """
        向前方旋转并抓取敌人， 然后继续旋转并造成伤害， 最后将敌人摔到地上， 产生冲击波。\n
        扔出敌人之前若按向下方向键， 则原地扔出敌人； 若按向前方向键， 则能将敌人扔得更远。\n
        攻击可抓取敌人时， 旋转过程中按方向键可立即扔出敌人， 冲击波范围根据敌人体型增加。\n
        发动[抓轰炮]时， 第一次攻击时会强控敌人， 旋转一圈后施放合计所有旋转攻击力的最后一击。\n
    [随机应变]\n
        学习后， 抓取判定删除， 旋转攻击并吸附周围敌人， 然后发动最后一击。
    """
    name = "末日摇篮"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "fc458e449ee00b01dbf88d09aae65462"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 首次旋转攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 额外旋转攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 5
    # 额外旋转次数 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最后冲击波攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [随机应变]
    # 旋转攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 0
    # 最后冲击波攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 0
    # [范围信息]
    # 最后冲击波大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    useAdapt = 0

    def setMode(self, mode = None):
        if self.useAdapt:
            self.hit4 = self.hit5 = 1
            self.hit0 = self.hit1 = self.hit3 = 0

    def vp_1(self):
        """
        [末日摇篮]\n
        [普通]\n
        旋转攻击范围 +30%\n
        在冲击波生成位置生成旋风， 吸附周围的敌人并进行多段攻击， 持续1.5秒\n
         - 旋风多段攻击次数 : 15次\n
         - 总攻击力相同\n
        固定向柔道家的前方投掷敌人\n
        [随机应变]\n
        生成持续1.5秒的旋风， 吸附周围的敌人并进行多段攻击\n
         - 删除旋转攻击和终结冲击波攻击\n
         - 旋风多段攻击次数 : 15次\n
         - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [末日摇篮]\n
        旋转途中可以预输入[螺旋彗星落]， 在最后一击时出现莱茜或露西， 进行协同攻击\n
        - 莱茜或露西的攻击力与[螺旋彗星落]攻击力相同\n
        [普通]\n
        露西在空中出现， 施放[螺旋飞扑]\n
        发动[抓轰炮]时， 莱茜在柔道家的对面施放[碎骨飞身踢]\n
        [随机应变]\n
        露西或莱茜在空中出现， 施放[终极飞身踢]\n
        使被[终极飞身踢]命中的敌人进入强制控制状态， 效果持续3秒
        """
        ...

# 随机应变
# fighter_female/grappler_female/2a0a39184de92acf1c1375e00b77404c
# a7a059ebe9e6054c0644b40ef316d6e9/2a0a39184de92acf1c1375e00b77404c
class Skill43(PassiveSkill):
    """
        精通抓取技的风暴女皇可以根据敌人的状态控制自己的技能。\n
        学习该技能后， 部分抓取技能变更为攻击技能。\n
        即使变更为攻击技能， 转职和觉醒被动效果依然生效。\n
    变更的技能 : [裂石破天]、 [死亡摇篮]、 [末日摇篮]、 [苍宇彗星落]
    """
    name = "随机应变"
    learnLv = 75
    masterLv = 1
    maxLv = 1
    position = 10
    rangeLv = 3
    uuid = "2a0a39184de92acf1c1375e00b77404c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    associate = [
        {"type":"+useAdapt","skills":["裂石破天","死亡摇篮","末日摇篮","苍宇彗星落"],"data":[0,100]}
    ]


# 风暴之舞
# fighter_female/grappler_female/1812a1ece67bb37b6b44b54766450064
# a7a059ebe9e6054c0644b40ef316d6e9/1812a1ece67bb37b6b44b54766450064
class Skill44(ActiveSkill):
    """
        围绕敌人高速旋转并攻击其关节， 在一段时间后对敌人造成大量伤害。\n
        可以在空中使用。
    """
    name = "风暴之舞"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "1812a1ece67bb37b6b44b54766450064"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 旋绕速度 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 爆炸攻击力 : {value1} x {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 6
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最后爆炸攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 冲击波大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [风暴之舞]\n
        向前方一定范围内最强敌人的位置突进\n
         - 寻敌范围内不存在敌人时， 无法施放技能\n
        抓住敌人后立即引发爆炸， 且爆炸发生间隔减少\n
         - 爆炸次数 +6次\n
         - 总攻击力相同\n
        爆炸结束后， 被抓取的敌人进入强制控制状态1秒
        """
        ...

    def vp_2(self):
        """
        [风暴之舞]\n
        返回施放技能的方向， 通过金臂勾产生强烈的冲击波后， 落地到与敌人相近的位置\n
         - 冲击波为单次攻击\n
         - 总攻击力相同
        """
        ...

# 苍宇彗星落
# fighter_female/grappler_female/d89f26862e348a801b30bb9fd7125db5
# a7a059ebe9e6054c0644b40ef316d6e9/d89f26862e348a801b30bb9fd7125db5
class Skill45(ActiveSkill):
    """
        抓取敌人并使用暴力上勾拳将其打向高空， 然后高高跃起， 抱住敌人一起疾速旋转后将其用力砸向地面使其受到极大伤害。\n
        上勾拳以后连续按下技能键， 可以更快地把敌人砸向地面。\n
        对无法抓取敌人施放时， 直接发动最后一击。\n
    - [随机应变] -\n
        学习后抓取判定消失， 跳起强力下砸攻击敌人。 在空中也可以施放。
    """
    name = "苍宇彗星落"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "d89f26862e348a801b30bb9fd7125db5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 暴力上勾拳攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 砸向地面的攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [随机应变]
    # 踢击攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 0
    # 下砸攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 0

    useAdapt = 0

    def setMode(self, mode = None):
        if self.useAdapt:
            self.hit2 = self.hit3 = 1
            self.hit0 = self.hit1  = 0

# 送葬舞步
# fighter_female/grappler_female/ab6fc3303df03b58911967dfca2b5d07
# a7a059ebe9e6054c0644b40ef316d6e9/ab6fc3303df03b58911967dfca2b5d07
class Skill46(ActiveSkill):
    """
        光芒之翼莱茜&露西组合的招牌动作。\n
        柔道家将敌人过肩摔后， 莱茜和露西交替攻击， 对敌人发动终结攻击。\n
        根据抓取敌人的状态变更技能效果。\n
        跳跃过程中也可以使用该技能。\n
    [可抓取]\n
        柔道家将敌人过肩摔后， 莱茜突进后用金臂勾将敌人击飞到空中， 然后露西快速抓取浮空的敌人后使出翻滚打桩摔。\n
        每次攻击时会产生冲击波， 对周围敌人造成相同伤害。\n
        过肩摔时， 可以按上方键将莱茜的金臂勾变更为飞身踢， 远远踢飞敌人。\n
    [抓轰炮]\n
        柔道家旋转攻击敌人， 莱茜突进后使出金臂勾， 然后露西对敌人使出飞身压。
    """
    name = "送葬舞步"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [960, 7200]
    uuid = "ab6fc3303df03b58911967dfca2b5d07"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 柔道家攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 莱茜攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 露西攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

# 光芒之翼
# fighter_female/grappler_female/0c3a468aee1f7ce06bf91eb3319518c1
# a7a059ebe9e6054c0644b40ef316d6e9/0c3a468aee1f7ce06bf91eb3319518c1
class Skill47(PassiveSkill):
    """
        战斗舞台的女皇——归元·柔道家与她的弟子莱茜&露西姐妹组成的终极组合。\n
        她们为观众展现更加华丽和超凡的战斗。\n
        增加除[背摔]以外的基本攻击和转职技能攻击力， 部分技能附加额外效果。\n
    [背摔]\n
        可抓取敌人 : 莱茜向倒地的敌人使出月面宙反， 造成额外伤害后弹回。\n
        无法抓取敌人 : 露西向命中的敌人使出飞身踢， 造成额外伤害后延长控制时间。\n
    [野蛮冲撞]\n
        不论是否蓄气， 抓取时均发动霸体护甲， 在空中时也可以使用该技能。\n
        空中施放时， 沿斜线落下， 向敌人踢击， 攻击后可以立即中断并使用空中抓取技能。\n
        准备动作时按方向键可以调整落下角度。
    """
    name = "光芒之翼"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "0c3a468aee1f7ce06bf91eb3319518c1"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 除[背摔]以外的基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [背摔]
    # 莱茜月面宙反攻击力 : [背摔]攻击力的{value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 露西飞身踢攻击力 : [背摔]攻击力的{value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    associate = [{"data":data0}]

# 女皇时代·辉煌舞台
# fighter_female/grappler_female/c91a62dc0a18360acf5031ac0ebf09f5
# a7a059ebe9e6054c0644b40ef316d6e9/c91a62dc0a18360acf5031ac0ebf09f5
class Skill48(ActiveSkill):
    """
        身在战斗舞台上的女皇使出最后的终结技。\n
        施放时， 向地面发动致命捶击， 产生冲击波， 强制控制命中的敌人， 然后隐藏踪迹。\n
        随后莱茜&露西向最强的敌人发动双人飞身踢， U.F.E特设舞台出现。\n
        然后， 幕后女皇登场， 发动终极金臂勾， 对敌人造成巨大伤害。\n
        终结攻击时， 敌人的控制状态解除。\n
        跳跃过程中也可以施放该技能。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "女皇时代·辉煌舞台"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4025, 8055]
    uuid = "c91a62dc0a18360acf5031ac0ebf09f5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 莱茜&露西搜寻敌人范围 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 第一次冲击波攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 莱茜&露西双人飞身踢攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 金臂勾攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 金臂勾冲击波攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # 终结爆炸攻击力 : {value5} x {value6}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 6
    data6 = get_data(f'{prefix}/{uuid}', 6)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'grappler_female'
        self.nameCN = '归元·柔道家'
        self.role = 'fighter_female'
        self.角色 = '格斗家(女)'
        self.职业 = '柔道家'
        self.jobId = 'a7a059ebe9e6054c0644b40ef316d6e9'
        self.jobGrowId = 'c9b492038ee3ca8d27d7004cf58d59f3'

        self.武器选项 = ['手套', '臂铠','爪','东方棍']
        self.输出类型选项 = ['物理固伤']
        self.输出类型 = '物理固伤'
        self.防具精通属性 = ['力量']
        self.防具类型 = '轻甲'
        self.buff =  2.215

        super().__init__(equVersion, __name__)
