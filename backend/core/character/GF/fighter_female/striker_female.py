#a7a059ebe9e6054c0644b40ef316d6e9
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "fighter_female/striker_female/cn/skillDetail"


# 下段踢
# fighter_female/striker_female/4655101518604f874721b3cc249aae10
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
# fighter_female/striker_female/cfacda0647b9a0f595df2c2aad30c18d
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
# fighter_female/striker_female/9dda3f4a849dba1a288dd65e116860f2
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
    position = 6
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
# fighter_female/striker_female/c9664191611af31142e052dfaef84530
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
# fighter_female/striker_female/8f73f243041c2d27739fe7696f02bf9b
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
# fighter_female/striker_female/78bd107acd474518b606be1e4fd38239
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
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 踩踏次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后踩踏攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

# 疾风追击
# fighter_female/striker_female/dcb31a63ef58954f44ff2070c42a9a98
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
# fighter_female/striker_female/4f2e001e9a19eb7bae50ad1840dfb329
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


# 拳套掌握
# fighter_female/striker_female/1dad88963abdc96b091fcab185a8820d
# a7a059ebe9e6054c0644b40ef316d6e9/1dad88963abdc96b091fcab185a8820d
class Skill18(PassiveSkill):
    """
        可以装备拳套系列武器。\n
        减少除[武神强踢]、 [极尽 : 霸皇断空拳]、 [陨星灭天击]之外的散打技能的冷却时间。
    """
    name = "拳套掌握"
    learnLv = 15
    masterLv = 1
    maxLv = 10
    position = 1
    rangeLv = 3
    uuid = "1dad88963abdc96b091fcab185a8820d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 冷却时间减少率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0,"type":"*cdReduce","exceptSkills":["武神强踢","极尽 : 霸皇断空拳","陨星灭天击"]}]

# 强拳
# fighter_female/striker_female/dcd536f1674630f01fc9667bb202b851
# a7a059ebe9e6054c0644b40ef316d6e9/dcd536f1674630f01fc9667bb202b851
class Skill19(ActiveSkill):
    """
        集中体内的能量， 增加命中敌人的僵直比率和自身暴击伤害， 效果持续一定时间。\n
        在决斗场中施放时， 减少攻击速度。
    """
    name = "强拳"
    learnLv = 15
    masterLv = 20
    maxLv = 30
    position = 5
    rangeLv = 3
    cd = 5
    uuid = "dcd536f1674630f01fc9667bb202b851"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 敌人的僵直比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 暴击伤害增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 决斗场攻击速度减少 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 崩拳
# fighter_female/striker_female/c77a417c43de80c4ce32c1ed405d174a
# a7a059ebe9e6054c0644b40ef316d6e9/c77a417c43de80c4ce32c1ed405d174a
class Skill20(ActiveSkill):
    """
        快速出拳对敌人造成伤害并使敌人进入僵直状态。\n
        施放时， 可以利用方向键使自身向相应的方向移动或在原地进行攻击。\n
        三觉后， 攻击命中时引发冲击波， 对周围的敌人造成相同的伤害。
    """
    name = "崩拳"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 6
    mp = [30, 252]
    uuid = "c77a417c43de80c4ce32c1ed405d174a"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 拳击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 敌人僵直比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 发动速度增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 冲击波大小 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 霸体护甲
# fighter_female/striker_female/3d8f3d438405d79f8d3ed68072674d1e
# a7a059ebe9e6054c0644b40ef316d6e9/3d8f3d438405d79f8d3ed68072674d1e
class Skill21(ActiveSkill):
    """
        可以使自身增加物理/魔法防御力和体力， 而且被攻击后不会倒地， 但仍会受到伤害， 效果持续一定时间。
    """
    name = "霸体护甲"
    learnLv = 20
    masterLv = 20
    maxLv = 30
    position = 3
    rangeLv = 3
    cd = 30
    mp = [40, 336]
    uuid = "3d8f3d438405d79f8d3ed68072674d1e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理、 魔法防御力增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 体力增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [决斗场]
    # 移动速度减少 : 10%

# 疾风连击
# fighter_female/striker_female/8572675ec6a1f50b6eff6a867376c2de
# a7a059ebe9e6054c0644b40ef316d6e9/8572675ec6a1f50b6eff6a867376c2de
class Skill22(PassiveSkill):
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


# 铁山靠
# fighter_female/striker_female/3c5604bdbb0240b8f130f59ab40509c3
# a7a059ebe9e6054c0644b40ef316d6e9/3c5604bdbb0240b8f130f59ab40509c3
class Skill24(ActiveSkill):
    """
        向前滑行用肩部对敌人进行猛力的攻击。\n
        按前方向键， 可以滑行得更远进行攻击。
    """
    name = "铁山靠"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 7
    mp = [50, 420]
    uuid = "3c5604bdbb0240b8f130f59ab40509c3"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 肩撞攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 碎骨
# fighter_female/striker_female/717f1e2104fe4b796f800352fa143ecc
# a7a059ebe9e6054c0644b40ef316d6e9/717f1e2104fe4b796f800352fa143ecc
class Skill25(ActiveSkill):
    """
        向敌人发出强威力的下段踢。\n
        有一定几率使命中的敌人进入减速状态。\n
        攻击成功时产生冲击波， 对周围敌人造成伤害。
    """
    name = "碎骨"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 7
    mp = [50, 420]
    uuid = "717f1e2104fe4b796f800352fa143ecc"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 下段踢攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 发动速度增加量 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 减速几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 减速持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 移动速度减少率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 攻击速度减少率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 冲击波大小 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

# 弱点感知
# fighter_female/striker_female/23a5e0fba03283cb1b324a847b3fe370
# a7a059ebe9e6054c0644b40ef316d6e9/23a5e0fba03283cb1b324a847b3fe370
class Skill26(PassiveSkill):
    """
        感知敌人的弱点。\n
    增加散打的物理暴击率和命中率， 增加基本攻击力和转职技能的攻击力。\n
        在决斗场中， 不会增加基本攻击力和技能攻击力。
    """
    name = "弱点感知"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 5
    rangeLv = 3
    uuid = "23a5e0fba03283cb1b324a847b3fe370"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 暴击率增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 命中率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 基本攻击力和转职技能攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    associate = [{"data":data2}]

# 旋风腿
# fighter_female/striker_female/202edb928046f4fa6dedf6337377efd5
# a7a059ebe9e6054c0644b40ef316d6e9/202edb928046f4fa6dedf6337377efd5
class Skill27(ActiveSkill):
    """
        快速旋转身体向前移动并用连续的扫腿攻击周围的敌人； 可以在地面或空中使用， 最后的扫腿还可以击倒敌人。\n
        施放后， 可以按上/下方向键改变移动方向， 或按跳跃键中断技能。\n
        转职成为散打时， 可以强制中断基本攻击动作， 并立即施放该技能。
    """
    name = "旋风腿"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 7
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

# 柔化肌肉
# fighter_female/striker_female/5152480fdde81362575a488d4cec4af9
# a7a059ebe9e6054c0644b40ef316d6e9/5152480fdde81362575a488d4cec4af9
class Skill28(PassiveSkill):
    """
        增加转职技能攻击力。\n
        暂时让身体变得灵活， 可以强制中断当前的转职技能并立即施放其他转职技能。\n
        强制中断次数有限制， 消耗的强制中断次数经过一段时间后可再次恢复。\n
        使用[柔化肌肉]强制中断并施放技能时， 如果该技能命中敌人， 则增加已激活的霸体状态持续时间。\n
    [可以强制中断的技能]\n
    - [上勾拳]、 [前踢]、 [下段踢]、 [鹰踏]、 [疾风连击]、 [旋风腿]、 [崩拳]、 [铁山靠]、 [碎骨]、 [升龙拳]、 [寸拳]、 [闪电之舞]、 [纷影连环踢]、 [破碎拳]、 [回天连环击]、 [虎啸神拳]、 [无影脚]、 [雷霆之舞]、 [武神强踢]、 [极尽 : 霸皇断空拳]\n
        在决斗场中有起始冷却时间， 经过一定时间后自动激活。 技能攻击力增加率效果仅适用于柔化后使用的技能。
    """
    name = "柔化肌肉"
    learnLv = 30
    masterLv = 5
    maxLv = 15
    position = 3
    rangeLv = 5
    uuid = "5152480fdde81362575a488d4cec4af9"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 强制中断次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 强制中断次数自动恢复时间: {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 霸体持续时间增加 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 霸体持续时间上限 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [决斗场]
    # 起始冷却时间 : 10秒
    associate = [{"data":data0}]

# 寸拳
# fighter_female/striker_female/42c82812f86ff6704ae9952a2e6093a4
# a7a059ebe9e6054c0644b40ef316d6e9/42c82812f86ff6704ae9952a2e6093a4
class Skill29(ActiveSkill):
    """
        相传为一位爱穿鲜黄色武斗服的神秘武斗家的成名技， 可以发出极强威力的一拳攻击近身的敌人， 而且可以引发冲击波并对后方的多个敌人造成伤害。\n
        决斗场增加攻击后僵直。
    """
    name = "寸拳"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [130, 1092]
    uuid = "42c82812f86ff6704ae9952a2e6093a4"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 发动速度增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 拳击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 冲击波攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 冲击波大小 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [寸拳]\n
        用经过长期实战磨练的技巧进行攻击\n
        - 拳击攻击范围 +100%\n
        - 冲击波攻击范围 +70%\n
        - 冲击波生成延迟减少\n
        攻击未命中敌人时熟练应对\n
        - 冷却时间补正为2秒
        """
        ...

    def vp_2(self):
        """
        [寸拳]\n
        不再用拳头攻击敌人， 大喝一声使周围的敌人进入僵直状态\n
        - 不适用拳击攻击力\n
        - 集中的力量可以持续30秒\n
        再次使用时可以集中更强的力量\n
        - 更新持续时间\n
        - 提升集中阶段\n
        - 集中阶段最多可提升至3阶段\n
        [破碎拳]\n
        在集中力量状态下使用[破碎拳]技能时，  会消耗所有积攒力量造成额外伤害\n
        - 额外伤害量与集中的拳击攻击力的总和相同
        """
        ...

# 升龙拳
# fighter_female/striker_female/852f8ad797db4dca1405cb3e77198401
# a7a059ebe9e6054c0644b40ef316d6e9/852f8ad797db4dca1405cb3e77198401
class Skill30(ActiveSkill):
    """
        掀起风暴吸附周围的敌人后， 跳到空中发出强力上勾拳， 使敌人受到多段伤害并浮空。\n
        在最高点发动下锤击， 将浮空的敌人打倒在地并生成冲击波。\n
        在决斗场中， 不会吸附敌人， 施放动作时进入霸体状态。
    """
    name = "升龙拳"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [170, 1428]
    uuid = "852f8ad797db4dca1405cb3e77198401"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 发动速度增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 下劈攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 风压地带范围 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [升龙拳]\n
        跳跃高度和速度增加\n
         - 风压地带及下劈范围增加\n
        [霸体护甲]\n
        施放技能时， 若[霸体护甲]技能不在冷却时间中\n
         - 自动适用[霸体护甲]技能效果， 并适用冷却时间
        """
        ...

    def vp_2(self):
        """
        [升龙拳]\n
        取消跳跃动作， 转为迅速肘击后连接上勾拳发射风压\n
         - 删除聚集敌人效果\n
         - 风压攻击次数 : 4次\n
         - 总攻击力相同
        """
        ...

# 闪电之舞
# fighter_female/striker_female/28b583c75a49103a1d8aabf799c000a4
# a7a059ebe9e6054c0644b40ef316d6e9/28b583c75a49103a1d8aabf799c000a4
class Skill31(ActiveSkill):
    """
        向前方敌人发出强威力的踢脚， 并利用反作用力闪电般地在一定范围内的多个敌人间移动且对这些敌人造成伤害。\n
        周围没有敌人或移动攻击达到一定次数后就会停止移动。\n
        无法攻击处于透明、 无敌、 伪装状态或一定高度以上的敌人。
    """
    name = "闪电之舞"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [180, 1512]
    uuid = "28b583c75a49103a1d8aabf799c000a4"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 移动攻击次数上限 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 每次移动时攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 7
    # [范围信息]
    # 移动距离 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [闪电之舞]\n
        增加攻击次数\n
        - 移动距离 +30%\n
        - 移动次数 +4次\n
        - 总攻击力相同\n
        最后一次移动攻击会攻击范围内最强的敌人\n
        - 移动攻击次数全部耗尽时， 会移动到目标面前， 但不发动攻击\n
        未命中时冷却时间缩短为3秒
        """
        ...

    def vp_2(self):
        """
        [闪电之舞]\n
        在首次攻击目标的左右快速移动并重复攻击\n
         - 移动次数 -4次\n
         - 总攻击力相同\n
        即使敌人脱离搜索范围也不会中断攻击\n
         - 目标死亡时移动到其他敌人位置\n
        使命中的敌人进入感电状态
        """
        ...

# 纷影连环踢
# fighter_female/striker_female/0b8db1e10b3abbd24d38564e708675d5
# a7a059ebe9e6054c0644b40ef316d6e9/0b8db1e10b3abbd24d38564e708675d5
class Skill32(ActiveSkill):
    """
        用极快的连续踢击使敌人受到伤害并进入僵直状态， 再强力抽打敌人。\n
        连续踢击的过程中可以利用方向键移动， 抽打时按前方向键， 可以跳向前方。\n
        抽打命中时引发冲击波， 对周围敌人造成相同的伤害。
    """
    name = "纷影连环踢"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [400, 3360]
    uuid = "0b8db1e10b3abbd24d38564e708675d5"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 连续踢击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 10
    # 连续踢击多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 抽打攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 冲击波大小 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [纷影连环踢]\n
        删除抽打攻击\n
        连环踢多段攻击次数 -50%\n
        变更为可填充3次的技能\n
         - 每次填充冷却时间 : 13.2秒\n
        在以下条件下省略准备动作\n
         - 连环踢过程中再次施放时\n
         - [柔化肌肉]强制中断施放时
        """
        self.cd = 13.2
        self.skillRation *= 1 - 0.5
        ...

    def vp_2(self):
        """
        [纷影连环踢]\n
        基本冷却时间变更为60秒\n
        总攻击力 +50%\n
        以风暴般的强力连续踢击攻击敌人\n
         - 连环踢过程中移动速度 -50%
        """
        self.cd = 60
        self.skillRation *= 1.5
        ...

# 武神步
# fighter_female/striker_female/147d005ac868e0de52b1f255eea35d62
# a7a059ebe9e6054c0644b40ef316d6e9/147d005ac868e0de52b1f255eea35d62
class Skill33(PassiveSkill):
    """
        强力震踏地面， 利用反作用力快速发动攻击。\n
        增加武神的基本攻击力和技能攻击力、 移动速度。
    """
    name = "武神步"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    uuid = "147d005ac868e0de52b1f255eea35d62"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和所有技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 移动速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"data":data0}]

# 武神强踢
# fighter_female/striker_female/47bd4871f29defc2a0021ee9261d7a5b
# a7a059ebe9e6054c0644b40ef316d6e9/47bd4871f29defc2a0021ee9261d7a5b
class Skill34(ActiveSkill):
    """
        强力震踏地面， 使敌人进入短暂的僵直状态并把敌人吸附到身边， 然后再聚集全身之力向敌人发出最强威力的下段踢。\n
        吸附敌人时， 自身无法移动； 若连续按基本攻击键， 则可以更快地吸附敌人。\n
        等待一段时间或按技能键， 则可以发动攻击。\n
        可以大幅度降低武神周围敌人的攻击速度。
    """
    name = "武神强踢"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [900, 7559]
    uuid = "47bd4871f29defc2a0021ee9261d7a5b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 武神强踢攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 吸附敌人的范围 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 吸附敌人时间上限 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 敌人攻击速度减少率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 敌人攻击速度减少范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 破碎拳
# fighter_female/striker_female/e5c09f9132a48dc1d695968592cc5878
# a7a059ebe9e6054c0644b40ef316d6e9/e5c09f9132a48dc1d695968592cc5878
class Skill35(ActiveSkill):
    """
        蓄力后用强劲的直拳攻击敌人。\n
        命中时产生冲击波攻击周围敌人。\n
        蓄力时， 可以按前/后/下方向键移动后攻击， 或者在原地攻击。
    """
    name = "破碎拳"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [450, 1260]
    uuid = "e5c09f9132a48dc1d695968592cc5878"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 拳击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 出拳速度增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 冲击波大小 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [破碎拳]\n
        不直接攻击敌人， 而是凭空挥拳发动攻击\n
         - 即使未命中敌人也会生成冲击波\n
        强化后的冲击波对前方大范围造成伤害\n
         - 冲击波攻击力 +25%\n
         - 冲击波大小 +50%
        """
        ...

    def vp_2(self):
        """
        [破碎拳]\n
        变更为可填充2次的技能\n
         - 每次填充冷却时间 : 15秒\n
         - 单次攻击力 -50%\n
        蓄力时间 -30%\n
         - [柔化肌肉]强制中断施放时额外 -30%
        """
        self.cd = 15
        self.skillRation *= 0.5
        ...

# 回天连环击
# fighter_female/striker_female/e0daa922b19cdc35de879e938361464e
# a7a059ebe9e6054c0644b40ef316d6e9/e0daa922b19cdc35de879e938361464e
class Skill36(ActiveSkill):
    """
        横扫地面后快速发动寸劲、 正拳和环绕攻击。\n
        横扫攻击能使命中的敌人浮空； 若敌人是霸体状态等无法浮空的情况下， 则使敌人进入减速状态。\n
        寸劲、 正拳、 环绕攻击命中敌人时引发冲击波， 对周围敌人造成伤害。\n
        若施放时按前方向键， 则前进后发动攻击。
    """
    name = "回天连环击"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [935, 1960]
    uuid = "e0daa922b19cdc35de879e938361464e"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 横扫地面攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 寸劲攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 正拳攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 环绕攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 寸劲冲击波攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 正拳冲击波攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 环绕冲击波攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 减速持续时间 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 速度减少 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [范围信息]
    # 范围比率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)

    def vp_1(self):
        """
        [回天连环击]\n
        不再用横扫地面攻击敌人， 而是生成旋风将周围的敌人吸附到前方\n
         - 删除横扫地面攻击力\n
        强制控制被寸劲、 正拳命中的敌人后， 发出强化的环绕攻击\n
         - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [回天连环击]\n
        横扫地面后向前方突进一小段距离并进行环绕攻击\n
         - 删除寸劲、 正拳攻击\n
         - 命中敌人时停止\n
         - 总攻击力相同\n
        进行环绕攻击时， 长按向前方向键\n
         - 可以绕过敌人\n
         - 会出现在前方一定距离处， 并向先前位置发动环绕攻击
        """
        ...

# 神武之力
# fighter_female/striker_female/8ee0099656df08a0b39225f8a21d514b
# a7a059ebe9e6054c0644b40ef316d6e9/8ee0099656df08a0b39225f8a21d514b
class Skill37(PassiveSkill):
    """
        克服身体与精神的极限， 发挥更加强力、 迅速、 强韧的力量。\n
        增加极武圣的基本攻击力和技能攻击力， 并强化部分技能。\n
    [柔化肌肉]\n
        增加可强制中断的次数， 减少柔化次数的恢复时间。\n
    [强拳]\n
        增加命中敌人的僵直几率。\n
    [霸体护甲]\n
        增加移动速度。
    """
    name = "神武之力"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 3
    uuid = "8ee0099656df08a0b39225f8a21d514b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 柔化次数恢复时间减少 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [柔化肌肉]可强制中断的次数增加 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [强拳]被命中敌人的僵直几率增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [霸体护甲]移动速度增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    associate = [{"data":data0}]

# 虎啸神拳
# fighter_female/striker_female/128b9ddef2262f40723deae4407bdb42
# a7a059ebe9e6054c0644b40ef316d6e9/128b9ddef2262f40723deae4407bdb42
class Skill38(ActiveSkill):
    """
        施展一系列的虎啸神拳攻击敌人。 虎啸神拳一共由2个招式组成。\n
    [白虎神武击] : 像猛虎一样快速攻击15次。\n
    [天虎旋风脚] : 用旋风脚踢飞敌人。\n
        攻击时， 可利用前/后方向键前进， 或在原地进行攻击。
    """
    name = "虎啸神拳"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "128b9ddef2262f40723deae4407bdb42"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # [白虎神武击]攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 15
    # [白虎神武击]攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [天虎旋风脚]直接打击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [天虎旋风脚]旋风攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1

    def vp_1(self):
        """
        [虎啸神拳]\n
        像猛虎一样对敌人施展猛烈攻击\n
        [白虎神武击]攻击次数 +5次\n
         - 连按<X>键时， 增加攻击速度\n
         - 总攻击力相同\n
        [白虎神武击]施放中功能强化\n
         - 将周围的敌人拉至面前\n
         - 所受伤害 -70%\n
         - 可以沿Y轴移动\n
         - 攻击时移动速度增加\n
        [白虎神武击]过程中按跳跃键时， 可立即发动[天虎旋风脚]
        """
        ...

    def vp_2(self):
        """
        [虎啸神拳]\n
        强化招式之间的连击， 让动作更加行云流水\n
        [白虎神武击]攻击次数 -5次\n
         - 总攻击力相同\n
        施放[天虎旋风脚]时， 根据[白虎神武击]的攻击次数， 赋予增加所有速度的增益\n
         - 攻击速度和移动速度增加\n
         - 增益持续时间 : 40秒\n
        通过[柔化肌肉]强制中断[白虎神武击]时， 会在施放[天虎旋风脚]后中断
        """
        ...

# 无影脚
# fighter_female/striker_female/9bff7f2559e003766fee2853dca00631
# a7a059ebe9e6054c0644b40ef316d6e9/9bff7f2559e003766fee2853dca00631
class Skill39(ActiveSkill):
    """
        以连影子都看不清的极快速度连续踢击敌人。\n
        先跳起扫腿攻击敌人， 最后再强力抽打敌人。 最后一击命中时产生冲击波， 对周围的敌人造成伤害。\n
        可利用前/后方向键前进， 或在原地进行攻击。
    """
    name = "无影脚"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "9bff7f2559e003766fee2853dca00631"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 扫腿攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 第3击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 抽打攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 冲击波大小 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [无影脚]\n
        快速追踪前方敌人， 发动强力的抽打攻击\n
        - 前方存在追踪目标时才能施放\n
        - 删除扫腿、 第2击、 第3击攻击\n
        - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [无影脚]\n
        通过灵活的动作强化连击\n
         - 降低抽打攻击高度\n
         - 抽打攻击后， 可以立即通过[柔化肌肉]强制中断并连接技能\n
        强化冲击波\n
         - 攻击范围 +40%\n
        通过[柔化肌肉]强制中断后施放时\n
         - 施放时间 -30%
        """
        ...

# 极尽 : 霸皇断空拳
# fighter_female/striker_female/78be08a3f8c834d3b06fa20c6a08c5a5
# a7a059ebe9e6054c0644b40ef316d6e9/78be08a3f8c834d3b06fa20c6a08c5a5
class Skill40(ActiveSkill):
    """
        大喝一声震慑住敌人， 将敌人吸附并歼灭。\n
        蓄气时， 可以将被压制的敌人拉到极武圣身前。\n
        断空拳击中敌人时产生强力冲击波， 对范围内的敌人造成巨大伤害。 若断空拳未击中敌人， 则产生强大风压对敌人造成伤害。
    """
    name = "极尽 : 霸皇断空拳"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "78be08a3f8c834d3b06fa20c6a08c5a5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 霸皇断空拳攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 风压攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 疾风劲
# fighter_female/striker_female/31823197cc0b04d4c5dcf8f928d9220c
# a7a059ebe9e6054c0644b40ef316d6e9/31823197cc0b04d4c5dcf8f928d9220c
class Skill41(PassiveSkill):
    """
        归元·散打将基础锻炼到极致， 拳脚变得更加强大。\n
        增加基本攻击力和转职技能攻击力， 部分技能附加额外效果。\n
    [崩拳]\n
        攻击成功时产生冲击波， 对周围敌人造成伤害。\n
    [碎骨]\n
        冲击波的大小增加， 对周围敌人造成与直接攻击相同的伤害。
    """
    name = "疾风劲"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "31823197cc0b04d4c5dcf8f928d9220c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]

# 雷霆之舞
# fighter_female/striker_female/dac8d8207618150c162e4c6f9e168527
# a7a059ebe9e6054c0644b40ef316d6e9/dac8d8207618150c162e4c6f9e168527
class Skill42(ActiveSkill):
    """
        追击范围内的敌人， 如电光石火般移动， 发动如雷霆般狂风骤雨的攻击。\n
        最后一击时， 在可移动的范围内追踪最强大的敌人发动攻击。\n
        每次攻击成功时产生冲击波， 对周围敌人造成伤害。
    """
    name = "雷霆之舞"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [870, 6750]
    uuid = "dac8d8207618150c162e4c6f9e168527"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 第1~7击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 7
    # 最后一击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 第1~7击冲击波攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最后一击冲击波攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 陨星灭天击
# fighter_female/striker_female/8e358ecf99ac9df31a6132aeafe378a9
# a7a059ebe9e6054c0644b40ef316d6e9/8e358ecf99ac9df31a6132aeafe378a9
class Skill43(ActiveSkill):
    """
        在经历极致的锻炼之后， 领悟了毁天灭地的新奥义。\n
        快速突进攻击敌人， 使敌人进入僵直状态后， 追踪并捶击其中最强大的敌人。\n
        接着将敌人踢到空中后跳跃， 再集中全部力量发动回旋踢。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "陨星灭天击"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "8e358ecf99ac9df31a6132aeafe378a9"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 突进攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 地面强击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 上踢攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 回旋踢攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 终结攻击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'striker_female'
        self.nameCN = '归元·散打'
        self.role = 'fighter_female'

        self.武器选项 = ['手套', '臂铠','爪','拳套','东方棍']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '轻甲'
        self.buff = 2.215

        self.角色 = '格斗家(女)'

        self.职业 = '散打'

        super().__init__(equVersion, __name__)
