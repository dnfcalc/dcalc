#a5ccbaf5538981c6ef99b236c0a60b73
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "mage_male/glacial_master/cn/skillDetail"


# 不死之身
# mage_male/glacial_master/bb34e8854a93fd250347a1c64119f7ab
# a5ccbaf5538981c6ef99b236c0a60b73/bb34e8854a93fd250347a1c64119f7ab
class Skill2(PassiveSkill):
    """
    角色死亡后带着少量生命值原地复活， 并且进入自动恢复生命值模式。\n
    自动恢复生命值模式下， 角色的生命值值可以在一定时间内自动恢复至100%， 但无法借用任何道具或其它途径恢复生命值， 且所受到的伤害还会加剧。\n
    若在恢复模式下死亡， 则无法再次通过该技能复活。
    """
    name = "不死之身"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 3
    uuid = "bb34e8854a93fd250347a1c64119f7ab"
    hasVP = False
    hasUP = False

    # 恢复模式下所受伤害增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 死亡时立即恢复的生命值量 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 恢复模式持续时间(普通地下城) : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 恢复模式持续时间(亡者峡谷) : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

# 黑暗之眼
# mage_male/glacial_master/6e33d47e6622ce03b6defdd912140270
# a5ccbaf5538981c6ef99b236c0a60b73/6e33d47e6622ce03b6defdd912140270
class Skill3(PassiveSkill):
    """
    增加魔法师的魔法值最大值； 若魔法值低于一定比率时， 还可增加魔法值恢复速度。
    """
    name = "黑暗之眼"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "6e33d47e6622ce03b6defdd912140270"
    hasVP = False
    hasUP = False

    # 魔法值最大值增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 可触发恢复效果时的魔法值比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 魔法值恢复速度增加 : {value2}倍
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 基础精通
# mage_male/glacial_master/5a56514f35cf0270ae8d6c65f8fefd78
# a5ccbaf5538981c6ef99b236c0a60b73/5a56514f35cf0270ae8d6c65f8fefd78
class Skill5(PassiveSkill):
    """
    增加基本攻击、 前冲攻击、 跳跃攻击、 [魔法旋风]的攻击力。\n
    在决斗场中， 增益/减益技能、 被动技能的技能攻击力增加效果对[基础精通]无影响。
    """
    name = "基础精通"
    learnLv = 1
    masterLv = 115
    maxLv = 200
    position = 0 #TODO
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

# 瞬移
# mage_male/glacial_master/3d8f3d438405d79f8d3ed68072674d1e
# a5ccbaf5538981c6ef99b236c0a60b73/3d8f3d438405d79f8d3ed68072674d1e
class Skill11(ActiveSkill):
    """
    向指定方向快速移动一定距离。
    """
    name = "瞬移"
    learnLv = 10
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 2
    cd = 1.5
    mp = [40, 40]
    uuid = "3d8f3d438405d79f8d3ed68072674d1e"
    hasVP = False
    hasUP = False

    # X轴移动距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # Y轴移动距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 冰魄剑
# mage_male/glacial_master/f2fb27162beb0b87a7cb9af7900e95f2
# a5ccbaf5538981c6ef99b236c0a60b73/f2fb27162beb0b87a7cb9af7900e95f2
class Skill15(ActiveSkill):
    """
    生成冰魄剑连续攻击敌人。 第1击和第2击使敌人进入僵直状态， 第3击则可以击退敌人， 并有一定几率使敌人进入减速状态。\n
    转职成为冰结师时， 才可以强制中断基本攻击动作， 并立即施放该技能。
    """
    name = "冰魄剑"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cd = 5
    mp = [30, 280]
    uuid = "f2fb27162beb0b87a7cb9af7900e95f2"
    hasVP = False
    hasUP = True

    # 第1击和第2击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 2
    # 第3击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # [减速效果]
    # 减速几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 减速持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

# 冰之印
# mage_male/glacial_master/27bade584bb42fef68148d3a0b72bace
# a5ccbaf5538981c6ef99b236c0a60b73/27bade584bb42fef68148d3a0b72bace
class Skill16(ActiveSkill):
    """
    冰结师特有技能； 可以使基本攻击产生变化， 在跳跃攻击和前冲攻击时生成冰刺。\n
    学习此技能后， 冰结师的冰冻抗性会达到最大值。\n
    施放时， 可以开启或关闭冰结师技能所带的冰冻功能。
    """
    name = "冰之印"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 3
    rangeLv = 1
    uuid = "27bade584bb42fef68148d3a0b72bace"
    hasVP = False
    hasUP = False

    # 学习后， 冰冻抗性 : 100%

# 冰武精通
# mage_male/glacial_master/d2c6df5105577fb59fb92529a36165a0
# a5ccbaf5538981c6ef99b236c0a60b73/d2c6df5105577fb59fb92529a36165a0
class Skill17(PassiveSkill):
    """
    增加基本攻击和转职技能的攻击力。同时使[寒冰连枪]、 [冰魄旋枪]新增冰冻效果。
    """
    name = "冰武精通"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 2
    uuid = "d2c6df5105577fb59fb92529a36165a0"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    associate = [{"type":"*skillRation","data":data0}]

# 寒冰连枪
# mage_male/glacial_master/ade01c1d6afc8a05055225045e89fe49
# a5ccbaf5538981c6ef99b236c0a60b73/ade01c1d6afc8a05055225045e89fe49
class Skill18(ActiveSkill):
    """
    用寒冰凝结成长枪， 并在前冲的同时连续刺击敌人。 在地下城里按后方向键， 可减少前冲距离， 按上/下方向键可以改变移动方向。\n
    最后一击命中敌人时， 可以强制中断技能， 并连接施放[冰魄旋枪]。\n
    学习[冰武精通]后， 最后一击会产生冰冻效果。\n
    霸体状态在决斗场不适用。
    """
    name = "寒冰连枪"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 3
    mp = [20, 210]
    uuid = "ade01c1d6afc8a05055225045e89fe49"
    hasVP = False
    hasUP = True

    # 冰枪攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 5
    # 冰枪多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 前冲距离 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 按方向键时的前冲距离 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [冰武精通提升效果]
    # 冰冻几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 冰冻持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # [范围信息]
    # 攻击范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)


# 冰霜之径
# mage_male/glacial_master/c9664191611af31142e052dfaef84530
# a5ccbaf5538981c6ef99b236c0a60b73/c9664191611af31142e052dfaef84530
class Skill20(ActiveSkill):
    """
    持续增加自身属性攻击力， 并持续减少敌人的冰冻抗性。\n
    施放后， 在地面生成冰雾， 增加自身的移动速度并使接触冰雾的敌人进入减速状态。\n
    跳跃或施放其他技能时无法生成冰雾。
    """
    name = "冰霜之径"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 5
    rangeLv = 5
    cd = 5
    mp = [390, 3900]
    uuid = "c9664191611af31142e052dfaef84530"
    hasVP = False
    hasUP = False

    # [常驻效果]
    # 属性攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 敌人冰冻抗性减少 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 冰结师附近的有效范围 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 冰冻抗性减少持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [施放效果]
    # 移动速度增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # [冰雾减速效果]
    # 减速几率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 减速持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # 减速移动速度减少 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    associate = [{"type":"*skillRation","data":data0}]

# 冰之领悟
# mage_male/glacial_master/ff171dc487807bb9aa28900ca9a46b41
# a5ccbaf5538981c6ef99b236c0a60b73/ff171dc487807bb9aa28900ca9a46b41
class Skill21(PassiveSkill):
    """
    领悟黑暗之眼的力量， 增加自身的魔法攻击力、 魔法暴击率、 命中率， 并减少施放技能时的魔法值消耗量。\n
    在决斗场不会增加魔法暴击率和命中率。
    """
    name = "冰之领悟"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 7
    rangeLv = 3
    uuid = "ff171dc487807bb9aa28900ca9a46b41"
    hasVP = False
    hasUP = False

    # 魔法值减少 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 魔法攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 魔法暴击率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 命中率增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    associate = [{"type":"$*PAtkM","data":data0}]

# 冰魄旋枪
# mage_male/glacial_master/547ab2b2bd860d3e37355a9cfbc1077c
# a5ccbaf5538981c6ef99b236c0a60b73/547ab2b2bd860d3e37355a9cfbc1077c
class Skill22(ActiveSkill):
    """
    连续抛出寒冰凝结成的长枪， 使其像风车一样快速旋转。 冰枪旋转时， 可以对周围的敌人进行多段攻击。\n
    投掷动作中命中敌人时， 可以强制中断技能， 并连接施放[寒冰连枪]。\n
    学习[冰武精通]后， 每次攻击会产生冰冻效果。
    """
    name = "冰魄旋枪"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 7
    mp = [35, 350]
    uuid = "547ab2b2bd860d3e37355a9cfbc1077c"
    hasVP = False
    hasUP = True

    # 投掷攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 投掷多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [学习冰凝之魂后]
    # 大型长枪攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 8
    # 大型长枪多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [冰武精通提升效果]
    # 冰冻几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 冰冻持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # [范围信息]
    # 枪大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

# 破冰飞刃
# mage_male/glacial_master/2f5d03c7848effbc0a23f4df45d9ca46
# a5ccbaf5538981c6ef99b236c0a60b73/2f5d03c7848effbc0a23f4df45d9ca46
class Skill23(ActiveSkill):
    """
    生成带有锋利冰凌的大冰球， 然后双手轮流挥砍， 击出大量破冰碎片对周围敌人造成伤害； 破冰碎片具有穿刺效果。\n
    在地下城按下C键， 可以中断技能的施放。
    """
    name = "破冰飞刃"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 8
    mp = [60, 546]
    uuid = "2f5d03c7848effbc0a23f4df45d9ca46"
    hasVP = False
    hasUP = True

    # 碎片数量 : {value0}~{value1}个
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 碎片攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 24
    # 碎片多段攻击次数上限 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [范围信息]
    # 冰碎片大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

# 冰魄之弓
# mage_male/glacial_master/4224f9b0b8c7c903e9a1e0f9d9f6d04d
# a5ccbaf5538981c6ef99b236c0a60b73/4224f9b0b8c7c903e9a1e0f9d9f6d04d
class Skill24(ActiveSkill):
    """
    用寒冰凝结成的弯弓向敌人连续发射箭矢。\n
    发射箭矢时， 若按下跳跃键， 则结束射击。\n
    敌人身中箭矢的期间， 若再次按下技能键， 则可以发动最后一击； 箭矢消失后则无法发动。\n
    在决斗场中， 若施放最后一击前被攻击， 则无法发动最后一击， 但不会受到中毒或出血等持续性的异常状态伤害影响。
    """
    name = "冰魄之弓"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 8
    mp = [60, 546]
    uuid = "4224f9b0b8c7c903e9a1e0f9d9f6d04d"
    hasVP = False
    hasUP = True

    # 弓箭攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 3
    # 弓箭发射次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 可发动最后一击的时间间隔 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [范围信息]
    # 箭矢锁定范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 学习[冰凝之魂]后， 最后一击大小比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)

# 寒冰之境
# mage_male/glacial_master/3829c15bf5f520c13998a3479ba0ce7b
# a5ccbaf5538981c6ef99b236c0a60b73/3829c15bf5f520c13998a3479ba0ce7b
class Skill25(ActiveSkill):
    """
    使黑暗之眼与冰结师周围的魔法能量产生共鸣， 增加自身的基本攻击力和技能攻击力。
    """
    name = "寒冰之境"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 7
    rangeLv = 3
    cd = 5
    uuid = "3829c15bf5f520c13998a3479ba0ce7b"
    hasVP = False
    hasUP = False

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 基本攻击和技能攻击增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 水晶剑
# mage_male/glacial_master/0232c151ef3731c2dede51931a374723
# a5ccbaf5538981c6ef99b236c0a60b73/0232c151ef3731c2dede51931a374723
class Skill26(PassiveSkill):
    """
    移除[冰魄剑]第3击， 第1和第2击强化成[水晶剑]进行攻击。 可以把散落在上/下方的敌人聚到冰结师面前， 第2击还能让敌人进入减速状态。\n
    [水晶剑]的攻击力与[冰魄剑]的第1/2击的攻击力成比例， 减速效果与[冰魄剑]第3击的减速效果相同。\n
    最后一击命中敌人时， 可以强制中断技能并施放转职技能。
    """
    name = "水晶剑"
    learnLv = 30
    masterLv = 1
    maxLv = 11
    position = 8
    rangeLv = 1
    uuid = "0232c151ef3731c2dede51931a374723"
    hasVP = False
    hasUP = False

    # [冰魄剑]第1和第2击攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)

    associate = [
        {"type":"*skillRation","data":data0,"skills":["冰魄剑"]},
        {"type":"+hit1","data":[0] + [-1]*maxLv,"skills":["冰魄剑"],"ratio":1},
        ]

# 冰魄锤击
# mage_male/glacial_master/01c3a2fb793d293a25ed8dc7a0d70c1a
# a5ccbaf5538981c6ef99b236c0a60b73/01c3a2fb793d293a25ed8dc7a0d70c1a
class Skill27(ActiveSkill):
    """
    生成巨大的冰锤， 前冲后向下猛烈砸击。 施放过程中， 会根据输入的方向键改变移动形态。\n
    前方 : 突进到最大距离。\n
    后方 : 在原地跳跃， 向下砸击。\n
    未输入 : 锁定前方敌人进行突进。\n
        施放过程中再次输入技能键时， 不会前冲，在原地使用冰锤砸向地面。\n
        使用除[千旋冰轮破]、 [冰凌破]、 [千里冰封]外的转职系列技能命中敌人时， 可以强制中断并连接施放[冰魄锤击]， 并且使用[冰魄之弓]、 [旋冰穿刺]、 [极冰绽放]、 [冰舞乱击]、 [冰雪风暴]、 [极冰猎魔斩]时， 可以在结束动作时强制中断。
    """
    name = "冰魄锤击"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 1
    cd = 18
    mp = [185, 1526]
    uuid = "01c3a2fb793d293a25ed8dc7a0d70c1a"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 最大移动距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 冰锤攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    def vp_1(self):
        """
        [冰魄锤击]\n
        施放时， 发射大范围寒气冲击波\n
        对命中的敌人赋予冰冻异常状态\n
         - 冰冻几率 : 100%\n
         - 持续时间 : 3秒
        """
        ...

    def vp_2(self):
        """
        [冰魄锤击]\n
        固定在原地使用冰锤砸向地面\n
         - 无法再次按技能键\n
         - 删除施法过程\n
        命中时， 可以强制中断施放后僵直并施放[冰魄剑]
        """
        ...

# 旋冰穿刺
# mage_male/glacial_master/9cb6f9ed646fa87f9b7680a42ce83d1a
# a5ccbaf5538981c6ef99b236c0a60b73/9cb6f9ed646fa87f9b7680a42ce83d1a
class Skill28(ActiveSkill):
    """
    用寒冰螺旋包裹自身并向前急速旋转攻击敌人， 可以使范围内的敌人受到多段攻击伤害。\n
        对无法抓取的敌人不适用控制效果， 不会造成多段攻击伤害， 而是造成单独的1次伤害。\n
        在地下城施放技能时， 按前方向键可以移动最大距离， 不做任何操作时， 会移动较短的距离。 总伤害量相同， 与移动距离无关， 并且在决斗场总是移动最大距离。
    """
    name = "旋冰穿刺"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 15
    mp = [180, 1512]
    uuid = "9cb6f9ed646fa87f9b7680a42ce83d1a"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 突进多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 0
    # 突进多段攻击次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 对无法抓取的敌人攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 按向前方向键时移动距离 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 寒冰螺旋大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    def vp_1(self):
        """
        [旋冰穿刺]\n
        突进时， 寒冰螺旋周围会产生结晶旋风\n
         - 默认移动到最大距离\n
         - 可以吸附强制控制状态的敌人\n
         - 施放过程中所受伤害 -90%
        """
        ...

    def vp_2(self):
        """
        [旋冰穿刺]\n
        召唤寒冰螺旋并向前方发射\n
         - 可以穿透命中的敌人\n
         - 对无法抓取的敌人造成1次伤害\n
         - 默认移动到最大距离\n
         - 突进距离上限 +50%\n
        对命中的敌人赋予冰冻异常状态\n
         - 冰冻几率 : 100%\n
         - 持续时间 : 3秒\n
        [破冰飞刃]\n
        攻击过程中可以施放[旋冰穿刺]
        """
        ...

# 极冰绽放
# mage_male/glacial_master/03bb5314ffd41e9458d67ef924fef38f
# a5ccbaf5538981c6ef99b236c0a60b73/03bb5314ffd41e9458d67ef924fef38f
class Skill29(ActiveSkill):
    """
    在魔法阵内生成冰之结晶， 使阵内敌人进入强制控制状态， 并召唤出多个大冰柱乱击敌人， 最后击碎冰柱给敌人造成冰属性伤害。\n
    连续按下技能键时， 可以更快地发动强击。
    """
    name = "极冰绽放"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [160, 1344]
    uuid = "03bb5314ffd41e9458d67ef924fef38f"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 控制几率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 乱击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 5
    power1 = 1
    # 乱击多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 最后一击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    power3 = 1
    # 冰柱破碎时的攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1
    power4 = 1
    # [范围信息]
    # 攻击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)

    def vp_1(self):
        """
        [极冰绽放]\n
        在自身周围生成魔法阵\n
         - 删除指定魔法阵位置的功能\n
         - 缩短魔法阵生成时间\n
         - 无需连按技能键， 始终以最大速度发动\n
        [冰舞乱击]\n
        前冲及乱击速度 +50%\n
        可强制中断施放后僵直并施放转职技能\n
        [冰之技艺]\n
        每次攻击时发射冰枪
        """
        ...

    def vp_2(self):
        """
        [极冰绽放]\n
        施放时在前方500px内最强的敌人处生成魔法阵\n
         - 攻击范围 +50%\n
        使被破碎的冰柱命中的敌人进入冰冻状态\n
         - 冰冻几率 : 100%\n
         - 持续时间 : 3秒\n
        [冰舞乱击]\n
        施放时追踪前方500px内最强的敌人并一同攻击周围的敌人\n
        使被冲击波命中的敌人进入冰冻状态\n
         - 冰冻几率 : 100%\n
         - 持续时间 : 3秒
        """
        ...

# 冰雪风暴
# mage_male/glacial_master/8f73f243041c2d27739fe7696f02bf9b
# a5ccbaf5538981c6ef99b236c0a60b73/8f73f243041c2d27739fe7696f02bf9b
class Skill30(ActiveSkill):
    """
    生成魔法阵并召唤出强威力的寒气风暴； 寒气风暴原地旋转时给予周围敌人多段攻击伤害。 当寒气风暴聚集在一起后会产生爆炸， 并对周围敌人造成更大伤害。\n
    生成魔法阵和寒气风暴旋转时，周围的敌人会进入冰冻状态。 风暴旋转时魔法阵内的敌人会被聚集到风暴中心。\n
    在地下城连续按键时可增加风暴旋转速度， 且生成风暴后会进入无敌状态。\n
    在决斗场中， 只有在生成魔法阵时会冰冻敌人， 寒气风暴不会冰冻敌人。\n
    在决斗场中， 武器的攻击属性不影响技能的攻击属性。
    """
    name = "冰雪风暴"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [350, 3080]
    uuid = "8f73f243041c2d27739fe7696f02bf9b"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 水柱多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 12
    # 水柱多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [冰冻效果]
    # 冰冻几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 冰冻持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # [范围信息]
    # 魔法阵范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 爆炸范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

    def vp_1(self):
        """
        [冰雪风暴]\n
        技能施放时立即发动寒气风暴， 并额外生成2个寒气风暴\n
         - 寒气风暴多段攻击次数 : 24次\n
         - 总攻击力相同\n
         - 魔法阵及爆炸范围 +35%\n
         - 无需连按技能键， 始终以最大速度发动
        """
        ...

    def vp_2(self):
        """
        [冰雪风暴]\n
        在指定位置生成魔法阵， 引起寒气爆炸\n
         - 总攻击力相同\n
         - 删除冰冻效果
        """
        ...

# 冰舞乱击
# mage_male/glacial_master/202edb928046f4fa6dedf6337377efd5
# a5ccbaf5538981c6ef99b236c0a60b73/202edb928046f4fa6dedf6337377efd5
class Skill31(PassiveSkill):
    """
    学习后， [极冰绽放]技能向前方快速飞出后压缩冷气， 向抓取的敌人快速施放[冰舞乱击]。 对抓取的敌人进行乱击和强击， 对无法抓取的敌人造成冲击波攻击。 [极冰绽放]的乱击数增加时， 该技能的乱击数也会增加[极冰绽放]乱击数增加量的50%。\n
    突进时按上/下方向键可以改变突进的方向。
    """
    name = "冰舞乱击"
    learnLv = 45
    masterLv = 1
    maxLv = 1
    position = 5
    rangeLv = 1
    uuid = "202edb928046f4fa6dedf6337377efd5"
    hasVP = False
    hasUP = False

    # 乱打攻击力 : [极冰绽放]乱打攻击力的{value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 强击攻击力 : [极冰绽放]强击攻击力的{value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 冲击波攻击力 : [极冰绽放]倒下的冰柱攻击力的{value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    associate = [
        {"type":"*power1","data":[i - 100 if i > 0 else i for i in data0],"skills":["极冰绽放"]},
        {"type":"+hit1","data":[0,-1],"skills":["极冰绽放"],"ratio":1},
        {"type":"*power3","data":[i - 100 if i > 0 else i for i in data1],"skills":["极冰绽放"]},
        {"type":"+hit4","data":[0,-1],"skills":["极冰绽放"],"ratio":1},
    ]

# 冰封奥义
# mage_male/glacial_master/92360eab6e1f378902018eca681ac629
# a5ccbaf5538981c6ef99b236c0a60b73/92360eab6e1f378902018eca681ac629
class Skill32(PassiveSkill):
    """
    增加基本攻击力和转职技能攻击力。 若敌人在角色周围停留一定时间， 则会进入冰冻状态。\n
    在决斗场无法冰冻敌人。
    """
    name = "冰封奥义"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    uuid = "92360eab6e1f378902018eca681ac629"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [冰冻效果]
    # 冰冻所需时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 冰冻几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 冰冻持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [范围信息]
    # 冰冻效果范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    associate = [{"type":"*skillRation","data":data0}]

# 千旋冰轮破
# mage_male/glacial_master/78be08a3f8c834d3b06fa20c6a08c5a5
# a5ccbaf5538981c6ef99b236c0a60b73/78be08a3f8c834d3b06fa20c6a08c5a5
class Skill33(ActiveSkill):
    """
    生成带有利齿的冰轮抛向敌人。 冰轮环绕敌人并对其造成多段攻击伤害， 而后凝聚成大冰轮吸附周围的敌人， 再次对目标进行多段攻击， 最后引发爆破。\n
    大小冰轮皆按照领主、 精英怪物、 普通怪物的先后顺序进行自动攻击。\n
    若在施放技能时没有目标， 则冰轮会被立刻收回。
    """
    name = "千旋冰轮破"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [1200, 10080]
    uuid = "78be08a3f8c834d3b06fa20c6a08c5a5"
    hasVP = False
    hasUP = False

    # 小冰轮攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 35
    # 小冰轮多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 大冰轮攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 10
    # 大冰轮多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 最终爆炸攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1

# 冰凌破
# mage_male/glacial_master/bc11d28c04e01923a093d65752c55516
# a5ccbaf5538981c6ef99b236c0a60b73/bc11d28c04e01923a093d65752c55516
class Skill34(ActiveSkill):
    """
    向前平抛出带有冰凌的冰球。 冰球在移动一定距离后进行扩张并生成大量冰凌攻击敌人， 同时对目标产生吸附效果， 最后引发爆炸。 可以使用方向键控制冰球的平抛方向。
    """
    name = "冰凌破"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [400, 1120]
    uuid = "bc11d28c04e01923a093d65752c55516"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 冰凌攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 25
    # 冰凌多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 冰球移动距离 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 输入前方向键冰球移动距离 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 输入上方向键冰球移动距离 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

    def vp_1(self):
        """
        [冰凌破]\n
        [冰之印]开启后， 追踪并攻击有[冰封奥义]光环的敌人中最强的敌人\n
         - 攻击开始后不再追踪敌人\n
         - 冰球移动速度 +50%\n
         - 冰棱多段攻击间隔 -15%
        """
        ...

    def vp_2(self):
        """
        [冰凌破]\n
        移动后攻击时，持续将周围敌人吸附至冰球位置\n
         - 冰球大小 +40%\n
        每次攻击附加冰冻异常状态\n
         - 冰冻几率 : 10%\n
         - 持续时间 : 3秒
        """
        ...

# 千里冰封
# mage_male/glacial_master/d296043df164385a14cb973c8c7c4d07
# a5ccbaf5538981c6ef99b236c0a60b73/d296043df164385a14cb973c8c7c4d07
class Skill35(ActiveSkill):
    """
    在前方地面快速生成冰雾， 同时生出大量冰刺攻击敌人。 受到冰雾或冰刺攻击的敌人， 有一定几率进入冰冻状态。
    """
    name = "千里冰封"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [900, 1820]
    uuid = "d296043df164385a14cb973c8c7c4d07"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 冰刺攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 3
    # 冰刺多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [冰冻效果]
    # 冰冻几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 冰冻持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    def vp_1(self):
        """
        [千里冰封]\n
        同时生成所有冰刺\n
         - 变更为单次攻击\n
         - 总攻击力相同\n
         - 施放速度 +60%\n
         - 冰刺生成速度 +25%\n
        [冰之印]开启后， 冰冻效果变更为强制控制效果， 效果持续2秒
        """
        ...

    def vp_2(self):
        """
        [千里冰封]\n
        生成覆盖周围区域的冰雾领域， 对领域内所有敌人持续造成冰刺攻击\n
         - 领域范围 : 2000px\n
         - 领域持续时间 : 30秒\n
         - 攻击次数上限 : 12次\n
         - 自动攻击间隔 : 1秒\n
         - 冰武器系列技能命中时立即触发攻击\n
         - 冰刺攻击力 -75%\n
        冰雾领域生成时， 触发增益效果\n
         - 攻击速度和移动速度 +10%\n
         - 增益持续时间 : 30秒 (最多叠加1次)
        """
        ...

# 冰之技艺
# mage_male/glacial_master/1803b6a67047cafb9e289b4f33cc507b
# a5ccbaf5538981c6ef99b236c0a60b73/1803b6a67047cafb9e289b4f33cc507b
class Skill36(PassiveSkill):
    """
    增加基本攻击和转职系列技能的攻击力。\n
    并且与[冰魄剑]、 [冰魄旋枪]、 [寒冰连枪]、 [冰魄锤击]、 [旋冰穿刺]、 [极冰绽放]、 [碎冰破]、 [极冰猎魔斩]等技能类似的用冰武器攻击敌人的技能命中敌人时， 技能结束时会出现保留原技能部分攻击力的冰枪， 插入被原始技能命中后存活的敌人中最强的敌人。\n
        如果技能没有命中敌人， 或者敌人全部死亡， 冰枪不会出现， 并且冰枪打偏时会产生爆炸对附近敌人造成伤害。
    """
    name = "冰之技艺"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 3
    uuid = "1803b6a67047cafb9e289b4f33cc507b"
    hasVP = False
    hasUP = False

    # 基本攻击和转职系列技能的攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 冰枪攻击力占原技能攻击力百分比 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 冰枪爆炸攻击力占原技能攻击力百分比 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    associate = [
        {"type":"*skillRation","data":data0},
        {"type":"*skillRation","data":data1,"skills":["冰魄剑", "寒冰连枪", "冰魄旋枪", "旋冰穿刺", "冰魄锤击", "极冰绽放", "碎冰破", "极冰猎魔斩"]}
    ]

# 碎冰破
# mage_male/glacial_master/de3fea2d65c597f4d55c70a02b97fc79
# a5ccbaf5538981c6ef99b236c0a60b73/de3fea2d65c597f4d55c70a02b97fc79
class Skill37(ActiveSkill):
    """
    制造冰柱后破坏冰柱， 利用碎片和冲击波攻击敌人。 近距离的敌人会受到碎片和冲击波的全部伤害， 远距离的敌人只会受到冲击波伤害。\n
    冰柱生成时， 附近的敌人会进入冰冻状态。\n
    并且[千旋冰轮破]、 [冰凌破]、 [千里冰封]以外的转职技能命中敌人时， 可以强制中断技能并连接施放[碎冰破]。 [冰魄之弓]、 [旋冰穿刺]、 [极冰绽放]、 [冰舞乱击]、 [冰雪风暴]、 [极冰猎魔斩]可以在结束动作时强制中断并施放[碎冰破]。
    """
    name = "碎冰破"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 8 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "de3fea2d65c597f4d55c70a02b97fc79"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 寒冰碎片攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # [冰冻效果]
    # 冰冻几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 冰冻时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    def vp_1(self):
        """
        [碎冰破]\n
        向前方生成多个冰霜结晶\n
         - 增加冰霜碎片攻击范围\n
         - 施放速度 +50%\n
        命中时， 可以强制中断施放后僵直并施放[冰魄剑]
        """
        ...

    def vp_2(self):
        """
        [碎冰破]\n
        将寒气凝聚成臂铠引发结晶爆炸， 并生成冲击波\n
         - 总攻击力相同\n
         - 施放时， 追踪并攻击前方500px范围内最强的敌人\n
         - 基本冷却时间变更为60秒\n
        总攻击力 +50%
        """
        self.cd = 60
        self.skillRation *= 1.5
        ...

# 极冰领域
# mage_male/glacial_master/d0cdaca82892e54097f22a1f60817048
# a5ccbaf5538981c6ef99b236c0a60b73/d0cdaca82892e54097f22a1f60817048
class Skill38(ActiveSkill):
    """
    凝缩黑暗之眼的冷气后向四周喷发， 对敌人造成伤害并使敌人短时间内进入强制控制状态。 凝缩冷气过程中为无敌状态， 喷发后进入霸体状态。
    """
    name = "极冰领域"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 2
    cube = 5
    cd = 40
    mp = [800, 6000]
    uuid = "d0cdaca82892e54097f22a1f60817048"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 波动攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 控制时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    def vp_1(self):
        """
        [极冰领域]\n
        部分转职技能命中后， 可以强制中断并施放[极冰领域]\n
         - 可中断技能列表与[冰魄锤击]相同\n
        释放波动时进入无敌状态
        """
        ...

    def vp_2(self):
        """
        [极冰领域]\n
        施放转职技能过程中可以无施放动作直接发动\n
         - 觉醒技能除外\n
        变更为可填充2次的技能\n
         - 每次填充冷却时间 : 20秒\n
         - 单次攻击力 -50%
        """
        ...

# 永罪冰狱
# mage_male/glacial_master/c61f5a010370101402b05b21916c2071
# a5ccbaf5538981c6ef99b236c0a60b73/c61f5a010370101402b05b21916c2071
class Skill39(ActiveSkill):
    """
    发射用永恒之冰制造的冰箭攻击敌人， 对命中的敌人造成伤害并制造寒冰监狱， 对附近的敌人造成伤害并禁锢敌人。\n
    冰块会越来越大， 禁锢附近敌人并造成伤害， 最后爆炸。\n
    技能命中墙壁或物体也会生成冰块。
    """
    name = "永罪冰狱"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 8 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "c61f5a010370101402b05b21916c2071"
    hasVP = False
    hasUP = False

    # 冰箭攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 寒冰监狱伤害 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 0
    # 冰块扩张的攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 2
    # 爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1

# 冰凝之魂
# mage_male/glacial_master/82fc7ec7cfb2b7afa8c125a2d9420a78
# a5ccbaf5538981c6ef99b236c0a60b73/82fc7ec7cfb2b7afa8c125a2d9420a78
class Skill40(PassiveSkill):
    """
    知源·冰结师专属战斗技巧， 精通冰结魔法的同时， 磨炼操纵魔法武器的体术。 增加基本攻击力和转职技能攻击力， 变更部分技能效果。\n
    [冰魄旋枪]\n
    投枪合而为一， 在头顶快速旋转后投掷。 总攻击力与变更前相同； 动作全程附加霸体护甲。\n
    [冰魄之弓]\n
    终结攻击动作附加霸体护甲， 增加冲击波范围。 并且， 最后一击对弓箭未命中敌人造成更大伤害。
    """
    name = "冰凝之魂"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "82fc7ec7cfb2b7afa8c125a2d9420a78"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [冰魄之弓]对弓箭未命中敌人的最后一击伤害增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    associate = [{"type":"*skillRation","data":data0}]

# 极冰猎魔斩
# mage_male/glacial_master/9f57da5cb3651d81ca7dc9f78be33d01
# a5ccbaf5538981c6ef99b236c0a60b73/9f57da5cb3651d81ca7dc9f78be33d01
class Skill41(ActiveSkill):
    """
       双手汇聚寒气， 制造两把巨大的冰霜巨剑后， 斩击敌人。
    """
    name = "极冰猎魔斩"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [960, 7200]
    uuid = "9f57da5cb3651d81ca7dc9f78be33d01"
    hasVP = False
    hasUP = False

    # 冰霜巨剑斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1

# 永劫 : 纳斯特隆德
# mage_male/glacial_master/0e3da11226dd30c2aaef52e36eff7f3f
# a5ccbaf5538981c6ef99b236c0a60b73/0e3da11226dd30c2aaef52e36eff7f3f
class Skill42(ActiveSkill):
    """
    以自身武器为媒介， 生成冰霜长矛， 散播寒流， 使周围的敌人进入冻结状态。 然后， 使用冰霜长矛连续攻击， 完全破坏地面， 并引发强烈的冰霜风暴， 将浮在空中的冰霜碎片融合成冰霜巨锤， 发动终结攻击。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "永劫 : 纳斯特隆德"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4027, 8055]
    uuid = "0e3da11226dd30c2aaef52e36eff7f3f"
    hasVP = False
    hasUP = False

    # 寒流攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 长矛下劈攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 长矛狂舞第1击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 长矛狂舞第2击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # 地面破坏攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1
    # 冰霜风暴多段攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    hit5 = 5
    # 冰霜风暴多段攻击次数 : {value6}次
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # 巨大冰锤多段攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    hit7 = 6
    # 巨大冰锤多段攻击次数 : {value8}次
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)
    # 巨大冰锤爆炸攻击力 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9, lambda x = None: x)
    hit9 = 1


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'glacial_master'
        self.nameCN = '知源·冰结师'
        self.role = 'mage_male'
        self.角色 = '魔法师(男)'
        self.职业 = '冰结师'
        self.jobId = 'a5ccbaf5538981c6ef99b236c0a60b73'
        self.jobGrowId = '618326026de1a1f1cfba5dbd0b8396e7'

        self.武器选项 = ['魔杖', '法杖', '矛', '棍棒']
        self.输出类型选项 = ['魔法百分比']
        self.输出类型 = '魔法百分比'
        self.防具精通属性 = ['智力']
        self.防具类型 = '皮甲'
        self.buff = 1.872

        super().__init__(equVersion, __name__)
