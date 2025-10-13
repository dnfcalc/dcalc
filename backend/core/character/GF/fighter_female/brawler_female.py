#a7a059ebe9e6054c0644b40ef316d6e9
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "fighter_female/brawler_female/cn/skillDetail"

# 上勾拳
# fighter_female/brawler_female/eb71e1d82d92c7e1d40500a0dcd77aa6
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
    position = 0 #TODO
    rangeLv = 3
    cd = 2
    uuid = "eb71e1d82d92c7e1d40500a0dcd77aa6"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 浮空攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 浮空力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 发动速度增加量 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 剧毒抵抗
# fighter_female/brawler_female/03bb5314ffd41e9458d67ef924fef38f
# a7a059ebe9e6054c0644b40ef316d6e9/03bb5314ffd41e9458d67ef924fef38f
class Skill1(PassiveSkill):
    """
        通过对毒的修炼， 减少自身受到的中毒伤害。
    """
    name = "剧毒抵抗"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "03bb5314ffd41e9458d67ef924fef38f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 中毒伤害减少率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

# 毒攻掌握
# fighter_female/brawler_female/bb34e8854a93fd250347a1c64119f7ab
# a7a059ebe9e6054c0644b40ef316d6e9/bb34e8854a93fd250347a1c64119f7ab
class Skill2(PassiveSkill):
    """
        修炼在传统格斗家严重视为邪道的毒门武功， 使用强大的毒气将全身经脉打通， 从而达到内外兼修的效果， 但稍有不慎， 便会走火入魔。\n
        力量和智力、 物理暴击率和魔法暴击率中会按照一定比率相互补正。\n
        使用念气系列技能 ([念气波]、 [分身]) 时， 有一定的几率使自身进入眩晕状态。
    """
    name = "毒攻掌握"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "bb34e8854a93fd250347a1c64119f7ab"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 力量和智力补正比率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理暴击率和魔法暴击率补正比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 施放念气系列技能时眩晕几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 前踢
# fighter_female/brawler_female/fc7a3f4c2852c832a2f20af63d5d212f
# a7a059ebe9e6054c0644b40ef316d6e9/fc7a3f4c2852c832a2f20af63d5d212f
class Skill3(ActiveSkill):
    """
        向敌人发出强威力的踢腿， 可以踢飞敌人。
    """
    name = "前踢"
    learnLv = 1
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 3
    mp = [10, 112]
    uuid = "fc7a3f4c2852c832a2f20af63d5d212f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 踢击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 击飞力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 后跳
# fighter_female/brawler_female/7822d6d52e10964a6755f142c666b494
# a7a059ebe9e6054c0644b40ef316d6e9/7822d6d52e10964a6755f142c666b494
class Skill4(ActiveSkill):
    """
        使自身向后方小跳并避开敌人的攻击。
    """
    name = "后跳"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    mp = [1, 1]
    uuid = "7822d6d52e10964a6755f142c666b494"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

# 基础精通
# fighter_female/brawler_female/5a56514f35cf0270ae8d6c65f8fefd78
# a7a059ebe9e6054c0644b40ef316d6e9/5a56514f35cf0270ae8d6c65f8fefd78
class Skill5(PassiveSkill):
    """
        增加基本攻击、 前冲攻击、 跳跃攻击、 [上勾拳]的攻击力。\n
        在决斗场中， 增益/减益技能、 被动技能的技能攻击力增加效果对[基础精通]无影响。
    """
    name = "基础精通"
    learnLv = 1
    masterLv = 115
    maxLv = 200
    position = 0 #TODO
    rangeLv = 1
    uuid = "5a56514f35cf0270ae8d6c65f8fefd78"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力变化率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 前冲攻击力变化率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 跳跃攻击力变化率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 受身蹲伏
# fighter_female/brawler_female/ce26c6b69d02a440a81b552bec94f03b
# a7a059ebe9e6054c0644b40ef316d6e9/ce26c6b69d02a440a81b552bec94f03b
class Skill6(ActiveSkill):
    """
        使自身在倒地状态下迅速起身并采取蹲伏姿势； 蹲伏状态下， 自身会进入无敌状态， 效果持续一定时间。
    """
    name = "受身蹲伏"
    learnLv = 1
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 1
    cd = 5
    mp = [1, 1]
    uuid = "ce26c6b69d02a440a81b552bec94f03b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 蹲伏姿势最短无敌时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 蹲伏姿势最长无敌时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 起身时霸体时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 攻击类型转换
# fighter_female/brawler_female/12dca7fbf791e882b025a0d916181673
# a7a059ebe9e6054c0644b40ef316d6e9/12dca7fbf791e882b025a0d916181673
class Skill7(PassiveSkill):
    """
        可以把基本攻击和技能的攻击类型转换成物理攻击或魔法攻击。\n
        每次点击技能窗口的技能图标时， 转换攻击类型。\n
        在决斗场中， 无法转换攻击类型， 适用技能固有的攻击类型。
    """
    name = "攻击类型转换"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "12dca7fbf791e882b025a0d916181673"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

# 防具精通
# fighter_female/brawler_female/892ef624d8bf3d7fc045f84825fd6104
# a7a059ebe9e6054c0644b40ef316d6e9/892ef624d8bf3d7fc045f84825fd6104
class Skill8(PassiveSkill):
    """
        穿戴防具时， 可以增加各种属性。\n
        穿戴的防具越多， 效果越强； 可根据转职， 增加不同的属性种类及数值。
    """
    name = "防具精通"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "892ef624d8bf3d7fc045f84825fd6104"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

# 下段踢
# fighter_female/brawler_female/4655101518604f874721b3cc249aae10
# a7a059ebe9e6054c0644b40ef316d6e9/4655101518604f874721b3cc249aae10
class Skill9(ActiveSkill):
    """
        格斗家特有的快速下段踢。\n
        命中时引发冲击波， 对周围敌人造成伤害。
    """
    name = "下段踢"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 2
    mp = [10, 112]
    uuid = "4655101518604f874721b3cc249aae10"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 下段踢攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 发动速度增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 冲击波大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 分身
# fighter_female/brawler_female/f2fb27162beb0b87a7cb9af7900e95f2
# a7a059ebe9e6054c0644b40ef316d6e9/f2fb27162beb0b87a7cb9af7900e95f2
class Skill10(ActiveSkill):
    """
        生成分身扰乱敌人的攻击或阻挡子弹。\n
        经过一定时间或受一定伤害后， 生成的分身就会消失。\n
        转职为气功师后， 分身仿照施放者的样子。\n
        在决斗场中，转职为气功师后， 增加分身的持续时间。
    """
    name = "分身"
    learnLv = 5
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 2
    cd = 7
    mp = [6, 84]
    uuid = "f2fb27162beb0b87a7cb9af7900e95f2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 分身生成数 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 分身持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 气功师分身持续时间 : 5秒

# 背摔
# fighter_female/brawler_female/cfacda0647b9a0f595df2c2aad30c18d
# a7a059ebe9e6054c0644b40ef316d6e9/cfacda0647b9a0f595df2c2aad30c18d
class Skill11(ActiveSkill):
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
    position = 0 #TODO
    rangeLv = 2
    cd = 5
    mp = [20, 168]
    uuid = "cfacda0647b9a0f595df2c2aad30c18d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 冲击波大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 学习[雷霆背摔]后， 闪电大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 蹲伏
# fighter_female/brawler_female/9dda3f4a849dba1a288dd65e116860f2
# a7a059ebe9e6054c0644b40ef316d6e9/9dda3f4a849dba1a288dd65e116860f2
class Skill12(ActiveSkill):
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
# fighter_female/brawler_female/c9664191611af31142e052dfaef84530
# a7a059ebe9e6054c0644b40ef316d6e9/c9664191611af31142e052dfaef84530
class Skill13(PassiveSkill):
    """
        使自身的身体强悍如钢铁， 并增加一定的物防和体力。\n
        被攻击时， 有一定几率进入霸体状态。
    """
    name = "钢筋铁骨"
    learnLv = 10
    masterLv = 50
    maxLv = 60
    position = 0 #TODO
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
# fighter_female/brawler_female/8f73f243041c2d27739fe7696f02bf9b
# a7a059ebe9e6054c0644b40ef316d6e9/8f73f243041c2d27739fe7696f02bf9b
class Skill14(ActiveSkill):
    """
        卑鄙地抛出沙子攻击敌人。\n
        攻击时， 有一定几率使敌人进入失明状态。\n
        转职为街霸后， 可中断基本攻击使用
    """
    name = "抛沙"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 3
    mp = [15, 154]
    uuid = "8f73f243041c2d27739fe7696f02bf9b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 沙尘攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
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
# fighter_female/brawler_female/78bd107acd474518b606be1e4fd38239
# a7a059ebe9e6054c0644b40ef316d6e9/78bd107acd474518b606be1e4fd38239
class Skill15(ActiveSkill):
    """
        在空中跳跃着踩踏敌人并给予敌人一定伤害。\n
    可以连续对敌人进行一定次数的踩踏， 技能的冷却时间从最后一次踩踏结束落地时开始计算。
    """
    name = "鹰踏"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
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

# 疾风追击
# fighter_female/brawler_female/dcb31a63ef58954f44ff2070c42a9a98
# a7a059ebe9e6054c0644b40ef316d6e9/dcb31a63ef58954f44ff2070c42a9a98
class Skill16(ActiveSkill):
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
    position = 0 #TODO
    rangeLv = 2
    cd = 2
    mp = [8, 67]
    uuid = "dcb31a63ef58954f44ff2070c42a9a98"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 第3击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 第4击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 金刚碎
# fighter_female/brawler_female/4f2e001e9a19eb7bae50ad1840dfb329
# a7a059ebe9e6054c0644b40ef316d6e9/4f2e001e9a19eb7bae50ad1840dfb329
class Skill17(ActiveSkill):
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
    position = 0 #TODO
    rangeLv = 2
    cd = 5
    mp = [20, 238]
    uuid = "4f2e001e9a19eb7bae50ad1840dfb329"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 浮空力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 施放后的僵直时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 强化 - 后跳
# fighter_female/brawler_female/2b340542e776818b78f3212af184bd6b
# a7a059ebe9e6054c0644b40ef316d6e9/2b340542e776818b78f3212af184bd6b
class Skill18(PassiveSkill):
    """
    施放技能期间、 被击或倒地的状态下， 可以施放无敌状态的[后跳]。\n
    该能力适用与[后跳]不同的冷却时间， 并且不受冷却时间减少效果的影响。\n
    根据施放情况的不同(强制中断技能和被敌人攻击)， 进入不同冷却时间。\n
    无法强制中断觉醒技能和跳跃超过一定高度的技能。
    """
    name = "强化 - 后跳"
    learnLv = 10
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    cd = 30
    uuid = "2b340542e776818b78f3212af184bd6b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 强制中断技能时的冷却时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 被击或倒地期间施放时的冷却时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 跃翔
# fighter_female/brawler_female/1fea5a626f15230237946a11a9d11582
# a7a059ebe9e6054c0644b40ef316d6e9/1fea5a626f15230237946a11a9d11582
class Skill19(ActiveSkill):
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

# 擒月炎
# fighter_female/brawler_female/0969cd4054d93da07708108c0cc1c4b5
# a7a059ebe9e6054c0644b40ef316d6e9/0969cd4054d93da07708108c0cc1c4b5
class Skill20(ActiveSkill):
    """
        用摆拳攻击并抓取1名敌人， 引爆手中猛毒火药。\n
        抓取敌人时吸附周围的敌人， 再次按技能键可以提前引爆。\n
        对无法抓取的敌人不适用控制效果， 命中时立即爆炸。\n
        爆炸时， 使被击中的敌人进入中毒和减速状态。\n
        攻击处于异常状态的敌人时， 造成更大的伤害。 (最多叠加3次)\n
        在决斗场中， 攻击无法抓取的敌人时不会爆炸。
    """
    name = "擒月炎"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 5.5
    mp = [30, 280]
    uuid = "0969cd4054d93da07708108c0cc1c4b5"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 摆拳攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 每个异常状态附加攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [灼伤效果]
    # 灼伤攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 灼伤几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 灼伤持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # - [发动涂毒时附加中毒攻击力] -
    # 摆拳攻击时中毒攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 爆炸攻击时中毒攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [范围信息]
    # 爆炸范围比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

# 念气波
# fighter_female/brawler_female/01c3a2fb793d293a25ed8dc7a0d70c1a
# a7a059ebe9e6054c0644b40ef316d6e9/01c3a2fb793d293a25ed8dc7a0d70c1a
class Skill21(ActiveSkill):
    """
        使念气实体化后向前方敌人发射。\n
        念气波对周围敌人具有诱导性， 在命中时爆炸， 对附近的敌人造成光属性伤害并进入感电状态。\n
        转职为气功师后， 可以强制中断基本攻击动作施放， 并大幅度减少冷却时间。
    """
    name = "念气波"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 1
    mp = [15, 154]
    uuid = "01c3a2fb793d293a25ed8dc7a0d70c1a"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 诱导性比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 感电几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 感电持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 感电攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [转职为气功师后]
    # 念气波冷却时间减少率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 念气波大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 射程距离 : {value7}px
    data7 = get_data(f'{prefix}/{uuid}', 7)

# 涂毒
# fighter_female/brawler_female/762c4e6d030eaf0abbfe1fec2b298574
# a7a059ebe9e6054c0644b40ef316d6e9/762c4e6d030eaf0abbfe1fec2b298574
class Skill22(ActiveSkill):
    """
        把毒涂抹在武器上攻击敌人， 使用基本攻击和转职后的技能时可使敌人进入中毒状态。\n
        技能攻击适用[发动涂毒时附加中毒攻击力]； 基本攻击适用另外的中毒攻击力。
    """
    name = "涂毒"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    cd = 5
    uuid = "762c4e6d030eaf0abbfe1fec2b298574"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [中毒效果]
    # 基本攻击时中毒攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 中毒几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 中毒持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 技能中包含的[涂毒]中毒攻击力变化率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 袭刺
# fighter_female/brawler_female/dde3b443bd5e61d90c34e5ee771e2c28
# a7a059ebe9e6054c0644b40ef316d6e9/dde3b443bd5e61d90c34e5ee771e2c28
class Skill23(ActiveSkill):
    """
        向前方快速移动。\n
        向敌人刺入不被察觉的细针， 施加出血异常状态。\n
        可以在[蹲伏]施放中施放。\n
        可以强制中断并施放转职技能； 移动中， 按反方向键施放转职技能时， 向反方向攻击。
    """
    name = "袭刺"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 5
    mp = [40, 239]
    uuid = "dde3b443bd5e61d90c34e5ee771e2c28"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 移动距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 针攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [出血效果]
    # 出血攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 出血几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 出血持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [涂毒发动时额外毒攻击力]
    # 针攻击时毒攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [学习猛毒之伤后]
    # 中毒攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 中毒几率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 中毒持续时间 : {value8}秒
    data8 = get_data(f'{prefix}/{uuid}', 8)

# 双重投掷
# fighter_female/brawler_female/4b2c90ec226fd40e967875aa5eabefb2
# a7a059ebe9e6054c0644b40ef316d6e9/4b2c90ec226fd40e967875aa5eabefb2
class Skill24(ActiveSkill):
    """
        施放该技能后， 向敌人发动[抛沙]、 [街头风暴]或投掷道具时可以连续投掷两个。\n
        投掷道具时将消耗两个投掷道具， 且投掷速度会变成原来的2倍。\n
        增加[擒月炎]、 [天罗地网]、 [毒雷引爆]、 [猛毒擒月炎]、 [爆碎砖袭]的大小比率， 同时增加[毒雷引爆]的毒雷投掷距离。
    """
    name = "双重投掷"
    learnLv = 20
    masterLv = 20
    maxLv = 30
    position = 0 #TODO
    rangeLv = 3
    cd = 5
    mp = [194, 1840]
    uuid = "4b2c90ec226fd40e967875aa5eabefb2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [擒月炎]爆炸范围增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [天罗地网]罗网大小增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [毒雷引爆]毒雷投掷距离增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [毒雷引爆]毒雷爆炸范围增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [猛毒擒月炎]爆炸范围增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [爆碎砖袭]爆炸范围增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

# 毒影针
# fighter_female/brawler_female/38612d8f2561edc2eb68d5057a837bfa
# a7a059ebe9e6054c0644b40ef316d6e9/38612d8f2561edc2eb68d5057a837bfa
class Skill25(ActiveSkill):
    """
        向敌人刺入具有肌肉僵硬效果的注射器。\n
        使敌人受到伤害的同时减少硬直， 有一定几率使敌人进入出血、 减速、 中毒状态。\n
        在决斗场内， 不出现减速、 中毒状态。
    """
    name = "毒影针"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 6
    mp = [50, 420]
    uuid = "38612d8f2561edc2eb68d5057a837bfa"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 毒针攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [僵直效果]
    # 僵直减少 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 减少僵直持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 稀有、 领主怪物持续时间变化率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 人形护甲持续时间变化率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [出血效果]
    # 出血攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 出血几率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 出血持续时间 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [中毒效果]
    # 中毒攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 中毒几率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 中毒持续时间 : {value10}秒
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # [减速效果]
    # 减速几率 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 减速持续时间 : {value12}秒
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # [发动涂毒时附加中毒攻击力]
    # 中毒攻击力 : {value13}% 
    data13 = get_data(f'{prefix}/{uuid}', 13)

# 疾风连击
# fighter_female/brawler_female/8572675ec6a1f50b6eff6a867376c2de
# a7a059ebe9e6054c0644b40ef316d6e9/8572675ec6a1f50b6eff6a867376c2de
class Skill26(PassiveSkill):
    """
        施放[疾风追击]时， 可以向敌人发出第3、 4击。
    """
    name = "疾风连击"
    learnLv = 20
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "8572675ec6a1f50b6eff6a867376c2de"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

# 暴击
# fighter_female/brawler_female/fc1262c19f3d0477ee8eda47b8db8696
# a7a059ebe9e6054c0644b40ef316d6e9/fc1262c19f3d0477ee8eda47b8db8696
class Skill27(PassiveSkill):
    """
        集中精神， 提升物理/魔法暴击率。
    """
    name = "暴击"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    uuid = "fc1262c19f3d0477ee8eda47b8db8696"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 物理/魔法暴击率增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

# 爪精通
# fighter_female/brawler_female/e4c354a89c337310aeb7041d5e742828
# a7a059ebe9e6054c0644b40ef316d6e9/e4c354a89c337310aeb7041d5e742828
class Skill28(PassiveSkill):
    """
        增加物理攻击力和魔法攻击力。\n
        使用爪系列武器时， 增加僵直率和命中率， 并有一定几率使敌人进入出血状态。\n
        使用鼠标右键， 可以打开/关闭出血效果。
    """
    name = "爪精通"
    learnLv = 25
    masterLv = 20
    maxLv = 30
    position = 0 #TODO
    rangeLv = 3
    uuid = "e4c354a89c337310aeb7041d5e742828"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 僵直率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 增加命中率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [出血效果]
    # 出血攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 出血几率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 出血持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)

# 砖袭
# fighter_female/brawler_female/bc11d28c04e01923a093d65752c55516
# a7a059ebe9e6054c0644b40ef316d6e9/bc11d28c04e01923a093d65752c55516
class Skill29(ActiveSkill):
    """
        用砖块攻击敌人。\n
        命中后砖块会碎裂并给予周围敌人伤害。\n
        攻击时， 有一定几率使敌人进入眩晕状态。\n
        砖块背击敌人时， 使敌人眩晕的几率是原来的2倍。
    """
    name = "砖袭"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 6
    mp = [50, 420]
    uuid = "bc11d28c04e01923a093d65752c55516"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 砖块攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 砖碎块攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [眩晕效果]
    # 砖块眩晕几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 砖块眩晕持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 砖碎块眩晕几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 砖碎块眩晕持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [发动涂毒时附加中毒攻击力]
    # 砖块攻击时中毒攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 砖碎块攻击时中毒攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [范围信息]
    # 碎块范围比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

# 伏虎霸王拳
# fighter_female/brawler_female/8c2379737c5acc935c1731f67f607655
# a7a059ebe9e6054c0644b40ef316d6e9/8c2379737c5acc935c1731f67f607655
class Skill30(ActiveSkill):
    """
        击倒敌人后骑上去发起连续攻击， 然后蓄力发起最后一击并生成冲击波。 \n
        连续攻击中按跳跃键可进行重击。\n
        抓取失败时砸向地面。\n
        对无法抓取的敌人不适用控制效果。
    """
    name = "伏虎霸王拳"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 15
    mp = [80, 672]
    uuid = "8c2379737c5acc935c1731f67f607655"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 连击攻击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 连击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 抓取失败时， 冲击波攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [发动涂毒时附加中毒攻击力]
    # 连击时， 中毒攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 最后一击时， 中毒攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 抓取失败时， 冲击波中毒攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 冲击波范围比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

# 旋风腿
# fighter_female/brawler_female/202edb928046f4fa6dedf6337377efd5
# a7a059ebe9e6054c0644b40ef316d6e9/202edb928046f4fa6dedf6337377efd5
class Skill31(ActiveSkill):
    """
        快速旋转身体向前移动并用连续的扫腿攻击周围的敌人； 可以在地面或空中使用， 最后的扫腿还可以击倒敌人。\n
        施放后， 可以按上/下方向键改变移动方向， 或按跳跃键中断技能。\n
        转职成为散打时， 可以强制中断基本攻击动作， 并立即施放该技能。
    """
    name = "旋风腿"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 8
    mp = [50, 420]
    uuid = "202edb928046f4fa6dedf6337377efd5"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 回旋踢攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 挑衅
# fighter_female/brawler_female/e49e57b2e8fbeceb0a2c56a0c63fe6c5
# a7a059ebe9e6054c0644b40ef316d6e9/e49e57b2e8fbeceb0a2c56a0c63fe6c5
class Skill32(ActiveSkill):
    """
        学习后， 持续减少一定范围内敌人的控制型异常状态抗性， 并增加对敌人造成的伤害。\n
        施放技能时， 向自身周围的敌人发出挑衅， 使被挑衅的敌人优先攻击自己并减少命中率。\n
        减少命中率的技能效果叠加时， 只适用数值最高的效果。\n
        在决斗场中， 减少降低控制型异常状态抗性光环的范围。
    """
    name = "挑衅"
    learnLv = 35
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    cd = 5
    mp = [60, 252]
    uuid = "e49e57b2e8fbeceb0a2c56a0c63fe6c5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # [持续效果]
    # 控制型异常状态抗性减少 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 伤害增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 挑衅持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 命中率减少率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 控制型异常状态抗性减少及挑衅范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [决斗场]
    # [范围信息]
    # 控制型异常状态抗性减少范围 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 天罗地网
# fighter_female/brawler_female/d0cdaca82892e54097f22a1f60817048
# a7a059ebe9e6054c0644b40ef316d6e9/d0cdaca82892e54097f22a1f60817048
class Skill33(ActiveSkill):
    """
        向前方投掷罗网， 将敌人拉到面前。\n
        罗网命中时， 使敌人进入束缚状态并强控敌人。\n
        施放时按向下方向键， 投掷罗网后不会把敌人拉到面前。\n
        罗网攻击力和罗网命中时中毒攻击力受[基础精通]影响。\n
        在决斗场中， 不适用霸体和强制控制效果。
    """
    name = "天罗地网"
    learnLv = 35
    masterLv = 1
    maxLv = 11
    position = 0 #TODO
    rangeLv = 3
    cd = 11
    mp = [180, 180]
    uuid = "d0cdaca82892e54097f22a1f60817048"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 罗网攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 强制控制持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [束缚效果]
    # 束缚几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 束缚持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [发动涂毒时附加中毒攻击力]
    # 罗网攻击时中毒攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [天罗地网]\n
        投掷附有金属片的罗网， 投掷后不会回收\n
        - 删除下方向键输入功能\n
        - 使敌人进入出血状态\n
        可以强制中断施放后僵直并施放部分技能\n
        - 可用技能 : [抛沙]、 [毒影针]、 [砖袭]\n
        可以强制中断部分技能的施放后僵直并施放该技能\n
        - 可用技能 : [毒影针]、 [砖袭]\n
        基本冷却时间变更为5.5秒\n
        - 总攻击力 -50%
        """
        ...

    def vp_2(self):
        """
        [天罗地网]\n
        投掷巨大的罗网\n
        - 删除下方向键输入功能\n
        控制持续时间 +2秒
        """
        ...

# 裂地飞沙
# fighter_female/brawler_female/e0a072e8cef2d77893aad5f68aeed56a
# a7a059ebe9e6054c0644b40ef316d6e9/e0a072e8cef2d77893aad5f68aeed56a
class Skill34(ActiveSkill):
    """
        蓄气后， 对准地面奋力一踢， 激起地上的沙石袭击敌人。\n
        攻击时， 有一定几率使敌人进入失明状态和眩晕状态。\n
        攻击无法抓取的敌人时增加攻击力。
    """
    name = "裂地飞沙"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [200, 1820]
    uuid = "e0a072e8cef2d77893aad5f68aeed56a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 踢击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 对无法抓取的敌人攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [失明效果]
    # 失明几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 失明持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [眩晕效果]
    # 眩晕几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 眩晕持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [发动涂毒时附加中毒攻击力]
    # 踢击命中时， 中毒攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 攻击范围比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    def vp_1(self):
        """
        [裂地飞沙]\n
        施放前僵直减少\n
        命中时可强制中断施放后僵直并施放转职技能
        """
        ...

    def vp_2(self):
        """
        [裂地飞沙]\n
        基本冷却时间变更为40秒\n
        - 总攻击力 +100%\n
        攻击范围 +50%
        """
        ...

# 狂 · 霸王拳
# fighter_female/brawler_female/b3659936a9a74c4ed6f7faf07cca1f9e
# a7a059ebe9e6054c0644b40ef316d6e9/b3659936a9a74c4ed6f7faf07cca1f9e
class Skill35(PassiveSkill):
    """
        增加[伏虎霸王拳]的连击次数， 连击也会产生冲击波。\n
        增加连击、 最后一击的攻击力和冲击波范围。\n
        对无法抓取的敌人适用控制效果， 立即发动最后一击， 并大幅增加攻击力。\n
        攻击处于异常状态的敌人时， 根据敌人的异常状态个数增加攻击力和冲击波范围。 (最多叠加3次)
    """
    name = "狂 · 霸王拳"
    learnLv = 40
    masterLv = 1
    maxLv = 11
    position = 0 #TODO
    rangeLv = 3
    cube = 1
    uuid = "b3659936a9a74c4ed6f7faf07cca1f9e"
    hasVP = True
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 连击攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 最后一击攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 对不可抓取敌人的最后一击攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 每个异常状态攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 每个异常状态额外增加冲击波范围 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 连击时， 冲击波范围增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 最后一击时， 冲击波范围增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [发动涂毒时附加中毒攻击力]
    # 连击时， 中毒攻击力增加率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 最后一击时， 中毒攻击力增加率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 最后一击命中无法抓取的敌人时， 中毒攻击力增加率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)

    def vp_1(self):
        """
        [狂·霸王拳]\n
        追踪成功时， 以无法抓取形态发动\n
        命中时， 发动即爆之血， 立即爆发自身中毒异常状态伤害
        """
        ...

    def vp_2(self):
        """
        [狂·霸王拳]\n
        追踪成功时， 以可抓取形态发动\n
        - 连击次数 -6次\n
        - 总攻击力相同\n
        - 每次连击攻击均合算[万毒噬心诀]基本攻击第1击的攻击力\n
        在技能施放过程中输入[擒月炎]、 [毒影针]、 [砖袭]时， 最后一击生成毒气爆炸\n
        - 合算输入技能的攻击力\n
        根据输入的技能立即附加异常状态\n
        - [擒月炎] : 灼伤\n
        - [毒影针] : 中毒/出血\n
        - [砖袭] : 眩晕
        """
        ...

# 毒雷引爆
# fighter_female/brawler_female/6a1d1f08a6572be420bb3a256c44c015
# a7a059ebe9e6054c0644b40ef316d6e9/6a1d1f08a6572be420bb3a256c44c015
class Skill36(ActiveSkill):
    """
        向周围抛出毒地雷。\n
        毒地雷一段时间后爆炸并喷发毒气柱， 使敌人进入中毒状态。\n
        在地下城中， 可以强制中断基本攻击并施放该技能。
    """
    name = "毒雷引爆"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cube = 1
    cd = 24
    mp = [180, 1512]
    uuid = "6a1d1f08a6572be420bb3a256c44c015"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 毒气柱攻击次数上限 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 毒气柱攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [中毒效果]
    # 中毒攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 中毒几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 中毒持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [发动涂毒时附加中毒攻击力]
    # 毒气柱攻击时中毒攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 毒气柱爆炸范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [毒雷引爆]\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 12秒\n
        - 单次攻击力 -50%\n
        毒气柱爆炸范围 +40%
        """
        ...

    def vp_2(self):
        """
        [毒雷引爆]\n
        施放除觉醒技能外的转职技能时， 可以施放[毒雷引爆]\n
        - 删除施放动作\n
        跳跃状态和被击过程中， 可以施放[毒雷引爆]\n
        - 删除施放动作
        """
        ...

# 街头风暴
# fighter_female/brawler_female/a2d943797daca862a6f321aca6ac9bfa
# a7a059ebe9e6054c0644b40ef316d6e9/a2d943797daca862a6f321aca6ac9bfa
class Skill37(ActiveSkill):
    """
        向周围敌人抛投各种生活用品， 使敌人进入强制控制状态。\n
        最后投掷炸药引发爆炸使敌人进入灼伤状态。\n
        连续按攻击键可以加快旋转速度， 按跳跃键可以立即投掷炸药。\n
        在决斗场中， 无法按跳跃键立即投掷炸药； 击中敌人时可以使敌人稍微浮空。
    """
    name = "街头风暴"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [450, 3780]
    uuid = "a2d943797daca862a6f321aca6ac9bfa"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 生活用品攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 生活用品多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 炸药爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [灼伤效果]
    # 灼伤攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 灼伤几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 灼伤持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # - [发动涂毒时附加中毒攻击力] -
    # 生活用品攻击时中毒攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 炸药爆炸攻击时中毒攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [范围信息]
    # 生活用品大小比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 炸药爆炸范围比率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)

    def vp_1(self):
        """
        [街头风暴]\n
        增加旋转速度\n
        - 删除连续按键功能\n
        炸药爆炸后， 强控2秒\n
        生活用品大小 +30%\n
        炸药爆炸范围 +30%
        """
        ...

    def vp_2(self):
        """
        [街头风暴]\n
        施放时进入无敌状态\n
        施放时引发风暴， 吸附敌人
        """
        ...

# 猛毒之血
# fighter_female/brawler_female/6e33d47e6622ce03b6defdd912140270
# a7a059ebe9e6054c0644b40ef316d6e9/6e33d47e6622ce03b6defdd912140270
class Skill38(PassiveSkill):
    """
        攻击敌人或被攻击时， 有一定几率向敌人喷射猛毒使其进入中毒状态， 并增加基本攻击力和技能攻击力。\n
        若处于出血状态下， 则喷出猛毒的几率是原来的2倍。\n
        增加攻击速度、 移动速度、 基本攻击力和技能攻击力。\n
        可以通过鼠标右键设置开启/关闭喷射猛毒功能。
    """
    name = "猛毒之血"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 3
    uuid = "6e33d47e6622ce03b6defdd912140270"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 移动速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [中毒效果]
    # 中毒攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 被击时中毒生成几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 攻击时中毒几率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 中毒生成持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)

# 死亡毒雾
# fighter_female/brawler_female/ca75c965f20a150f99f54155a37400df
# a7a059ebe9e6054c0644b40ef316d6e9/ca75c965f20a150f99f54155a37400df
class Skill39(ActiveSkill):
    """
        跳跃至空中， 向地面投掷毒药包引发爆炸。\n
        毒雾扩散后， 形成毒地带。\n
        一段时间后引发毒雾爆炸。\n
        可以在地面和空中施放。\n
        毒雾中， 减少敌人控制型异常状态抗性并引发中毒状态。\n
        毒雾中， 增加毒王的攻击速度和移动速度； 敌人无法看见在毒雾内移动的毒王。
    """
    name = "死亡毒雾"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [900, 7559]
    uuid = "ca75c965f20a150f99f54155a37400df"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 毒雾持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 毒雾中毒攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 毒雾中毒持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 毒雾爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 毒雾爆炸多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 毒雾大小比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [毒雾附加效果]
    # 敌人控制型异常状态抗性减少率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 攻击速度、 移动速度增加 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [发动涂毒时附加中毒攻击力]
    # 毒雾爆炸时攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

# 猛毒擒月炎
# fighter_female/brawler_female/b89c9ab317bc0a443f6497b7cca2f6a8
# a7a059ebe9e6054c0644b40ef316d6e9/b89c9ab317bc0a443f6497b7cca2f6a8
class Skill40(ActiveSkill):
    """
        用摆拳攻击并抓取1名敌人， 引爆手中猛毒火药。\n
        抓取敌人时吸附周围的敌人， 再次按技能键可以提前引爆。\n
        对无法抓取的敌人不适用控制效果， 命中时立即爆炸。\n
        爆炸时， 使被击中的敌人进入中毒和减速状态。\n
        攻击处于异常状态的敌人时， 造成更大的伤害。 (最多叠加3次)
    """
    name = "猛毒擒月炎"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [280, 784]
    uuid = "b89c9ab317bc0a443f6497b7cca2f6a8"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 摆拳攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 每个异常状态攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [中毒效果]
    # 中毒攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 中毒几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 中毒持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [减速效果]
    # 减速几率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 减速持续时间 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 移动速度减少率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 攻击速度减少率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [发动涂毒时附加中毒攻击力]
    # 摆拳攻击时中毒攻击力 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 爆炸攻击时中毒攻击力 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # [范围信息]
    # 爆炸范围比率 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)

    def vp_1(self):
        """
        [猛毒擒月炎]\n
        命中时， 发动即爆之血， 立即爆发自身中毒异常状态伤害\n
        爆炸后， 附加强制控制状态1秒\n
        爆炸范围 +20%
        """
        ...

    def vp_2(self):
        """
        [猛毒擒月炎]\n
        删除根据异常状态适用数量增加攻击力的功能\n
        - 攻击力 +60%\n
        如果没有命中的敌人， 剩余冷却时间缩短为4秒
        """
        ...

# 爆碎砖袭
# fighter_female/brawler_female/0fbb8de70002ad34f046c94c2cb3e863
# a7a059ebe9e6054c0644b40ef316d6e9/0fbb8de70002ad34f046c94c2cb3e863
class Skill41(ActiveSkill):
    """
        跳跃并强力锤击地面， 使地面迸出镶嵌着炸药的砖块。\n
        再用拳头向前击飞砖块引发爆炸， 使敌人进入强制控制状态。\n
        按方向键可调整跳跃距离。\n
        后/下方向键 : 原地\n
        方向键(无操作) : 中距离\n
        前方向键 : 长距离
    """
    name = "爆碎砖袭"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [800, 1680]
    uuid = "0fbb8de70002ad34f046c94c2cb3e863"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 冲击波攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 砖块攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 砖块爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 砖块爆炸多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 砖块爆炸时强制控制持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [发动涂毒时附加中毒攻击力]
    # 冲击波中毒攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 砖块攻击时中毒攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 砖块爆炸时中毒攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [范围信息]
    # 砖块爆炸大小比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

    def vp_1(self):
        """
        [爆碎砖袭]\n
        砖块向正面飞去并爆炸\n
        - 从强力锤击地面开始强控\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 25秒\n
        - 每次攻击力 -50%\n
        可以在空中施放
        """
        ...

    def vp_2(self):
        """
        [爆碎砖袭]\n
        变更为具有定时功能的炸药砖块， 在一定时间后自动爆炸\n
        - 锤击地面之后角色可以行动\n
        - 总攻击力相同\n
        可以强制中断转职技能的施放后僵直并施放 (觉醒技能除外)
        """
        ...

# 猛毒之伤
# fighter_female/brawler_female/1803b6a67047cafb9e289b4f33cc507b
# a7a059ebe9e6054c0644b40ef316d6e9/1803b6a67047cafb9e289b4f33cc507b
class Skill42(PassiveSkill):
    """
        攻击中毒状态的敌人时， 增加物理、 魔法暴击率以及基本攻击力和技能攻击力， 并且部分技能发生变更。\n
    [袭刺]\n
        施放时进入霸体状态， 引发中毒异常状态。\n
    [双重投掷]\n
        进入地下城时， 自动施放[双重投掷]。\n
    [伏虎霸王拳]\n
        施放时毒气扩散， 探索后追击可抓取的最强敌人
    """
    name = "猛毒之伤"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 3
    uuid = "1803b6a67047cafb9e289b4f33cc507b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理、 魔法暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 基本攻击力和技能攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 连环毒爆弹
# fighter_female/brawler_female/faf9cd66281078b51be2ee0b0f6c5530
# a7a059ebe9e6054c0644b40ef316d6e9/faf9cd66281078b51be2ee0b0f6c5530
class Skill43(ActiveSkill):
    """
        在敌人身上装置毒爆弹。\n
        一定时间后， 毒爆弹会爆炸， 使敌人进入中毒、 灼伤状态， 同时转移到周围其他敌人身上。\n
        该转移对曾经被毒爆弹命中的敌人无效。\n
        被装置毒爆弹的敌人将会减少移动速度和攻击速度。\n
        对无法抓取的敌人不适用控制效果。
    """
    name = "连环毒爆弹"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "faf9cd66281078b51be2ee0b0f6c5530"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 踢击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 毒爆弹爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 毒爆弹第1次转移人数上限 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 第1次转移时， 攻击力减少率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 毒爆弹第2次转移人数上限 : {value4}个
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 第2次转移时， 攻击力减少率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 被装置爆毒弹时， 移动速度减少率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 被装置爆毒弹时， 攻击速度减少率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [中毒效果]
    # 中毒攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 中毒几率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 中毒持续时间 : {value10}秒
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # [灼伤效果]
    # 灼伤攻击力 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 灼伤几率 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 灼伤持续时间 : {value13}秒
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # [发动涂毒时附加中毒攻击力]
    # 踢击时中毒攻击力 : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # 毒爆弹爆炸时中毒攻击力 : {value15}%
    data15 = get_data(f'{prefix}/{uuid}', 15)
    # [范围信息]
    # 爆炸范围比率 : {value16}%
    data16 = get_data(f'{prefix}/{uuid}', 16)

    def vp_1(self):
        """
        [连环毒爆弹]\n
        后空翻距离 -50%\n
        后空翻过程中， 可以施放所有可以空中使用的转职技能
        """
        ...

    def vp_2(self):
        """
        [连环毒爆弹]\n
        施放时， 删除踢击攻击力\n
        - 总攻击力相同\n
        部分转职技能施放过程中输入[连环毒爆弹]时， 可以对命中的敌人同时引发毒爆弹爆炸\n
        - 删除[连环毒爆弹]施放动作， 合算攻击力\n
        - 可施放的技能 : [袭刺]、 [擒月炎]、 [毒影针]、 [砖袭]、 [伏虎霸王拳]、 [猛毒擒月炎]\n
        [连环毒爆弹]爆炸时， 初始化[袭刺]的冷却时间\n
        - [袭刺]攻击力 -11%
        """
        ...

# 毒龙轰天雷
# fighter_female/brawler_female/2391a27457b5a8c6fa4b4670a91bdd11
# a7a059ebe9e6054c0644b40ef316d6e9/2391a27457b5a8c6fa4b4670a91bdd11
class Skill44(ActiveSkill):
    """
        使用最强暗器——轰天雷攻击敌人。\n
        该技能可以在地面和空中使用。\n
        轰天雷爆炸时， 犹如毒龙冲天并给予敌人5次伤害， 使其进入中毒状态。\n
        爆炸后会在地面上形成猛毒地带， 该范围内的敌人将进入减速状态， 效果持续一定时间。\n
        按向下键时会在原地施放。
    """
    name = "毒龙轰天雷"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "2391a27457b5a8c6fa4b4670a91bdd11"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 落地攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 轰天雷爆炸多段攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 轰天雷爆炸多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 猛毒地带攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 猛毒地带持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 猛毒地带移动速度减少率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [中毒效果]
    # 中毒攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 中毒几率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 中毒持续时间 : {value8}秒
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [发动涂毒时附加中毒攻击力]
    # 落地攻击时中毒攻击力 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 轰天雷爆炸时中毒攻击力 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # [范围信息]
    # 攻击范围比率 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)

    def vp_1(self):
        """
        [毒龙轰天雷]\n
        技能效果变更为投掷爆弹箱， 落地后爆炸\n
        - 猛毒地带持续时间 -50%\n
        - 总攻击力相同\n
        - 施放时进入无敌状态
        """
        ...

    def vp_2(self):
        """
        [毒龙轰天雷]\n
        生成毒气沸腾的猛毒地带\n
        - 猛毒地带持续时间 +100%\n
        - 总攻击力相同\n
        位于猛毒地带内时， 适用速度增益\n
        - 攻击速度 +15%\n
        - 移动速度 +15%\n
        攻击范围 +50%
        """
        ...

# 秘制毒爆弹
# fighter_female/brawler_female/0113c8b1306ca76d208f83f2d093dd62
# a7a059ebe9e6054c0644b40ef316d6e9/0113c8b1306ca76d208f83f2d093dd62
class Skill45(PassiveSkill):
    """
        重新组合爆毒的成分， 取消毒爆弹的转移及减速效果， 但会造成更加强大的爆炸。\n
        踢击只能对1个抓取的敌人造成伤害， 爆炸会对范围内的所有敌人造成伤害。
    """
    name = "秘制毒爆弹"
    learnLv = 80
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 2
    uuid = "0113c8b1306ca76d208f83f2d093dd62"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 踢击攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 毒爆弹爆炸攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 毒爆弹爆炸攻击时中毒攻击力变化率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 万毒噬心诀
# fighter_female/brawler_female/2a3c96b88d02372505692da0a8b54743
# a7a059ebe9e6054c0644b40ef316d6e9/2a3c96b88d02372505692da0a8b54743
class Skill46(ActiveSkill):
    """
        用毒神绝的独特战术“万毒噬心诀”压制敌人。\n
        学习[万毒噬心诀]后， 增加[挑衅]的控制型异常状态抗性减少值。\n
        发动后， 基本攻击、 前冲攻击、 跳跃攻击方式将会产生变化。 攻击时， 附带蛇形攻击。 并增加技能攻击力。\n
        其他技能施放过程中可以使用[万毒噬心诀]。 使用时， 会在没有准备动作及冲击波的情况下立即施放。 
    """
    name = "万毒噬心诀"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 5
    cube = 10
    cd = 60
    mp = [2445, 34577]
    uuid = "2a3c96b88d02372505692da0a8b54743"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # [持续效果]
    # [挑衅]控制型异常状态抗性额外减少 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [万毒噬心诀]持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 施放技能时爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 基本攻击第1击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 基本攻击第2击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 基本攻击第3击攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 基本攻击第4击攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 基本攻击第5击攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 前冲攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 跳跃攻击力 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 技能攻击力增加率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # [发动涂毒时附加中毒攻击力]
    # 基本攻击第1击攻击时中毒攻击力 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 基本攻击第2击攻击时中毒攻击力 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 基本攻击第3击攻击时中毒攻击力 : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # 基本攻击第4击攻击时中毒攻击力 : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # 基本攻击第5击攻击时中毒攻击力 : {value15}%
    data15 = get_data(f'{prefix}/{uuid}', 15)
    # 前冲攻击攻击时中毒攻击力 : {value16}%
    data16 = get_data(f'{prefix}/{uuid}', 16)
    # 跳跃攻击攻击时中毒攻击力 : {value17}%
    data17 = get_data(f'{prefix}/{uuid}', 17)

# 禁技 : 万毒蛇窟
# fighter_female/brawler_female/8b08f9504167a9c0f3a1d29d71b7943e
# a7a059ebe9e6054c0644b40ef316d6e9/8b08f9504167a9c0f3a1d29d71b7943e
class Skill47(ActiveSkill):
    """
        释放利用[万毒噬心诀]获取的剧毒气息， 释放的毒气变化为蛇的形状。 \n
        [万毒噬心诀]状态下， 可以在地面和空中施放。\n
        并且可以用方向键控制降落的位置。\n
        下方向键 : 原地\n
        方向键(无操作) : 中距离\n
        前方向键 : 长距离
    """
    name = "禁技 : 万毒蛇窟"
    learnLv = 85
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 5
    cd = 180
    mp = [1900, 1900]
    uuid = "8b08f9504167a9c0f3a1d29d71b7943e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # [禁技 ： 万毒蛇窟]攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [禁技 ： 万毒蛇窟]多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [发动涂毒时附加中毒攻击力]
    # [禁技 ： 万毒蛇窟]攻击时中毒攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 身化万毒
# fighter_female/brawler_female/78b86e64fbb74c1db1b71c50a5ac21cd
# a7a059ebe9e6054c0644b40ef316d6e9/78b86e64fbb74c1db1b71c50a5ac21cd
class Skill48(PassiveSkill):
    """
        只有超越界限化为万毒本身者才能使用的独门秘技。\n
        增加基本攻击力和转职技能攻击力， 变更部分技能效果。\n
    [擒月炎]\n
        攻击可抓取敌人时， 删除抓取动作， 将火药附着到命中的敌人身上， 短暂控制敌人后引爆火药。 \n
    [毒影针]\n
        发动[万毒噬心诀]后施放时， 向前方投掷蛇形毒气。
    """
    name = "身化万毒"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 3
    uuid = "78b86e64fbb74c1db1b71c50a5ac21cd"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [擒月炎]攻击可抓取敌人时的控制持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 钻心毒爆
# fighter_female/brawler_female/f4a561e272cc434a4905b3aa0c0de090
# a7a059ebe9e6054c0644b40ef316d6e9/f4a561e272cc434a4905b3aa0c0de090
class Skill49(ActiveSkill):
    """
        取出装有爆炸物的箱械， 向敌人跳跃并进行攻击， 同时引爆箱械。\n
        该技能可以在地面和空中使用。\n
        按向前方向键可以跳得更远。\n
        攻击命中时使敌人进入出血状态。\n
        爆炸攻击使敌人进入中毒和灼伤状态。\n
        未命中敌人时， 向地面下砸并引爆箱械。
    """
    name = "钻心毒爆"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [960, 7200]
    uuid = "f4a561e272cc434a4905b3aa0c0de090"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 命中敌人时攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击地面时攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 箱械爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 箱械爆炸多段攻击次数上限 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [出血效果]
    # 出血攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 出血几率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 出血持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [中毒效果]
    # 中毒攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 中毒几率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 中毒持续时间 : {value9}秒
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [灼伤效果]
    # 灼伤攻击力 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 灼伤几率 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 灼伤持续时间 : {value12}秒
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # [发动涂毒时附加中毒攻击力]
    # 命中敌人时中毒攻击力 : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # 攻击地面时中毒攻击力 : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # 箱械爆炸攻击时中毒攻击力 : {value15}%
    data15 = get_data(f'{prefix}/{uuid}', 15)

# 万毒噬心诀 : 毒龙吞天
# fighter_female/brawler_female/0e409ac3e1c1f3976b3ef2bfe4c13069
# a7a059ebe9e6054c0644b40ef316d6e9/0e409ac3e1c1f3976b3ef2bfe4c13069
class Skill50(ActiveSkill):
    """
        万毒噬心诀的终极奥义， 解除手臂的束缚， 将恐怖的万毒全部释放。\n
        攻击敌人中的最强者， 并释放毒蛇群。\n
        随后万毒化龙， 吞噬所有生灵。\n
        可以在地面和空中施放。\n
        解除束缚时， 使敌人进入中毒状态。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "万毒噬心诀 : 毒龙吞天"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4025, 8055]
    uuid = "0e409ac3e1c1f3976b3ef2bfe4c13069"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 解除束缚时攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 对可抓取敌人膝踢攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 对可抓取敌人下劈攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 对无法抓取敌人的下劈攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 毒蛇群多段攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 毒蛇群多段攻击次数上限 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 最后一击毒龙攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [中毒效果]
    # 中毒攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 中毒持续时间 : {value8}秒
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 中毒几率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [发动涂毒时附加中毒攻击力]
    # 对可抓取敌人的膝踢攻击时中毒攻击力 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 对可抓取敌人的下劈攻击时中毒攻击力 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 对无法抓取敌人的下劈攻击时中毒攻击力 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 毒蛇群多段攻击中毒攻击力 : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # 最后一击毒龙攻击时中毒攻击力 : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'brawler_female'
        self.nameCN = '归元·街霸'
        self.role = 'fighter_female'
        self.角色 = '格斗家(女)'
        self.职业 = '街霸'
        self.jobId = 'a7a059ebe9e6054c0644b40ef316d6e9'
        self.jobGrowId = '6d459bc74ba73ee4fe5cdc4655400193'

        self.武器选项 = [] # TODO
        self.输出类型选项 = [] # TODO
        self.输出类型 = '' # TODO
        self.防具精通属性 = [''] # TODO
        self.防具类型 = ''
        self.buff = ... # TODO

        super().__init__(equVersion, __name__)
