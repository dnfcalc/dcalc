#a5ccbaf5538981c6ef99b236c0a60b73
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "mage_male/swift_master/cn/skillDetail"

# 魔法旋风
# mage_male/swift_master/3c5604bdbb0240b8f130f59ab40509c3
# a5ccbaf5538981c6ef99b236c0a60b73/3c5604bdbb0240b8f130f59ab40509c3
class Skill0(ActiveSkill):
    """
    向敌人发出无属性旋风并使其浮空。\n
    转职为次元行者后， 技能类型变为独立攻击力。\n
    - [转职为猩红法师时附加效果] -\n
    外形发生变化， 可以吸收猩红气息。\n
    - [转职为逐风者时附加效果] -\n
    增加攻击力， 可以按<X>键进行追加操作。
    """
    name = "魔法旋风"
    learnLv = 1
    masterLv = 10
    maxLv = 20
    position = 4
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
    # - [转职为猩红法师后] -
    # 猩红气息吸收率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # - [转职为逐风者后] -
    # 攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    skillRation = 1.1


# 不死之身
# mage_male/swift_master/bb34e8854a93fd250347a1c64119f7ab
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
    position = 8
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
# mage_male/swift_master/6e33d47e6622ce03b6defdd912140270
# a5ccbaf5538981c6ef99b236c0a60b73/6e33d47e6622ce03b6defdd912140270
class Skill3(PassiveSkill):
    """
    增加魔法师的魔法值最大值； 若魔法值低于一定比率时， 还可增加魔法值恢复速度。
    """
    name = "黑暗之眼"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 6
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
# mage_male/swift_master/5a56514f35cf0270ae8d6c65f8fefd78
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
    position = 1
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
# mage_male/swift_master/3d8f3d438405d79f8d3ed68072674d1e
# a5ccbaf5538981c6ef99b236c0a60b73/3d8f3d438405d79f8d3ed68072674d1e
class Skill11(ActiveSkill):
    """
    向指定方向快速移动一定距离。
    """
    name = "瞬移"
    learnLv = 10
    masterLv = 1
    maxLv = 1
    position = 9
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

# 疾风掌控
# mage_male/swift_master/47bd4871f29defc2a0021ee9261d7a5b
# a5ccbaf5538981c6ef99b236c0a60b73/47bd4871f29defc2a0021ee9261d7a5b
class Skill16(PassiveSkill):
    """
    熟练使用风的力量， 掌握该技能后会增加移动速度， 施放[魔法旋风]后可以通过X键追加攻击， 还可以在空中进行冲刺攻击以及追加跳跃。\n
    使用追加跳跃后， 连续按下跳跃键可以缓慢降落。\n
    逐风者掌握了高机动性战斗技巧， 在进行基本攻击、 跳跃攻击、 冲刺攻击时， 在自身周围产生旋风。\n
    在决斗场内， 无法使用追加跳跃以及缓慢降落。
    """
    name = "疾风掌控"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 2
    rangeLv = 1
    uuid = "47bd4871f29defc2a0021ee9261d7a5b"
    hasVP = False
    hasUP = False

    # 移动速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 空中冲刺冷却时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 可施放空中冲刺的最低高度 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 狂风冲刺
# mage_male/swift_master/669f1428193f61f9d92c743b72438c4d
# a5ccbaf5538981c6ef99b236c0a60b73/669f1428193f61f9d92c743b72438c4d
class Skill17(ActiveSkill):
    """
    利用风的力量， 瞬间冲刺一段距离。 在空中也可以施放， 冲刺过程中， 将对碰到的敌人给予伤害和僵直效果， 并在一定时间内， 可通过追加操作再进行冲刺。 可强制中断当前施放中的技能， 并立即施放[狂风冲刺]。\n
    在决斗场中， 无法在空中施放。
    """
    name = "狂风冲刺"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 5
    mp = [31, 185]
    uuid = "669f1428193f61f9d92c743b72438c4d"
    hasVP = False
    hasUP = True

    # 冲刺攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 9
    # 攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 追加操作时间限制 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 可追加操作次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 冲刺距离 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

# 回风斩
# mage_male/swift_master/8510294202d0e042dd29a2422fc6770d
# a5ccbaf5538981c6ef99b236c0a60b73/8510294202d0e042dd29a2422fc6770d
class Skill18(ActiveSkill):
    """
    引发锋利的寒风攻击周围的敌人。
    """
    name = "回风斩"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 5.5
    mp = [38, 227]
    uuid = "8510294202d0e042dd29a2422fc6770d"
    hasVP = False
    hasUP = True

    # 风击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 4
    # 攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # 大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 疾风之棍棒精通
# mage_male/swift_master/087d1068ff506d090710566608a17760
# a5ccbaf5538981c6ef99b236c0a60b73/087d1068ff506d090710566608a17760
class Skill19(PassiveSkill):
    """
    增加武器的物理攻击力， 减少除[万象风龙阵]、 [无限风域]、 [风之极·永坠]之外技能的冷却时间。 使用棍棒系列武器攻击敌人时， 武器上凝聚风之力， 可以增加命中率、 攻击速度和物理暴击率
    """
    name = "疾风之棍棒精通"
    learnLv = 15
    masterLv = 20
    maxLv = 30
    position = 8
    rangeLv = 3
    uuid = "087d1068ff506d090710566608a17760"
    hasVP = False
    hasUP = False

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 命中率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 攻击速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 冷却时间减少率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 物理暴击率增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    associate = [
        {"data":data0,"type":"$*PAtkP"},
        {"data":data3,"type":"*cdReduce","exceptSkills":["万象风龙阵","无限风域","风之极·永坠"]},
        ]

# 流风诀
# mage_male/swift_master/38612d8f2561edc2eb68d5057a837bfa
# a5ccbaf5538981c6ef99b236c0a60b73/38612d8f2561edc2eb68d5057a837bfa
class Skill20(ActiveSkill):
    """
    在逐风者周围聚集风的力量， 增加攻击力以及防御能力。增加自身回避率， 并且增加物理/魔法防御力。
    """
    name = "流风诀"
    learnLv = 20
    masterLv = 20
    maxLv = 30
    position = 5
    rangeLv = 3
    cd = 5
    uuid = "38612d8f2561edc2eb68d5057a837bfa"
    hasVP = False
    hasUP = False

    # 基本攻击和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 回避率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 物理防御力增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 魔法防御力增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

# 朔风牵引
# mage_male/swift_master/a2d943797daca862a6f321aca6ac9bfa
# a5ccbaf5538981c6ef99b236c0a60b73/a2d943797daca862a6f321aca6ac9bfa
class Skill21(ActiveSkill):
    """
    在前方产生逆风， 将敌人吸附到角色周围， 甚至可以将倒地状态的敌人吸附过来。 逆风效果只对地面上的敌人有效。 可以强制中断逆风并立即施放其他技能， 或反之也可以。\n
    在决斗场中， 无法拉起倒地状态的敌人。\n
    - [可强制中断的技能] -\n
    [狂风冲刺]、 [回风斩]、 [游离之风]、 [风鸣冲击]、 [双翼风刃]、 [风暴之眼]、 [真空旋风破]、 [风暴之拳]、 [疾风瞬影闪]、 [风卷残云]
    """
    name = "朔风牵引"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 10
    mp = [45, 268]
    uuid = "a2d943797daca862a6f321aca6ac9bfa"
    hasVP = False
    hasUP = True

    # 逆风攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 9
    # 多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # 大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)


# 游离之风
# mage_male/swift_master/b3659936a9a74c4ed6f7faf07cca1f9e
# a5ccbaf5538981c6ef99b236c0a60b73/b3659936a9a74c4ed6f7faf07cca1f9e
class Skill23(ActiveSkill):
    """
    生成向前方移动的旋风攻击敌人。 旋风能将敌人旋转起来， 给敌人造成伤害后消失。
    """
    name = "游离之风"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 7
    mp = [45, 268]
    uuid = "b3659936a9a74c4ed6f7faf07cca1f9e"
    hasVP = False
    hasUP = True

    # 旋风攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 3 + 1
    # 旋风攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # 大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 风鸣冲击
# mage_male/swift_master/6a1d1f08a6572be420bb3a256c44c015
# a5ccbaf5538981c6ef99b236c0a60b73/6a1d1f08a6572be420bb3a256c44c015
class Skill24(ActiveSkill):
    """
    将风聚集在手中向前方发射， 击退受到伤害的敌人。\n
    在决斗场中， 无法击退霸体状态的敌人。
    """
    name = "风鸣冲击"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 8.5
    mp = [61, 366]
    uuid = "6a1d1f08a6572be420bb3a256c44c015"
    hasVP = False
    hasUP = True

    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # [范围信息]
    # 大小比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 双翼风刃
# mage_male/swift_master/c7bf7ccab413009640e65ca6f2f0263a
# a5ccbaf5538981c6ef99b236c0a60b73/c7bf7ccab413009640e65ca6f2f0263a
class Skill25(ActiveSkill):
    """
    双手连续发射旋风。 敌人会被吸附到旋风中心。
    """
    name = "双翼风刃"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 14
    mp = [91, 545]
    uuid = "c7bf7ccab413009640e65ca6f2f0263a"
    hasVP = False
    hasUP = True

    # 旋风攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 4
    # 旋风攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # 大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 风之意志
# mage_male/swift_master/5f4c55fe2ebdf0623bd76d4fda872ddc
# a5ccbaf5538981c6ef99b236c0a60b73/5f4c55fe2ebdf0623bd76d4fda872ddc
class Skill26(PassiveSkill):
    """
    逐风者运用风的力量， 增加基本攻击力和转职技能攻击力。
    """
    name = "风之意志"
    learnLv = 30
    masterLv = 5
    maxLv = 15
    position = 4
    rangeLv = 3
    uuid = "5f4c55fe2ebdf0623bd76d4fda872ddc"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    associate = [{"data":data0}]

# 刃风
# mage_male/swift_master/128b9ddef2262f40723deae4407bdb42
# a5ccbaf5538981c6ef99b236c0a60b73/128b9ddef2262f40723deae4407bdb42
class Skill27(ActiveSkill):
    """
    将风环绕在身体周围， 瞬间加速靠近附近一定范围内最强的敌人 (领主 > 稀有 > 普通) 的后方并攻击敌人。\n
    在敌人发现自己之前， 出现在另一边， 发动锋利的风刃攻击， 然后将移动路径上留下的风凝缩并引爆， 对周围敌人造成伤害。\n
    该技能可以在空中施放。\n
    风刃命中时， 可以强制中断当前动作并立即施放其他技能； 也可以强制中断其他技能并立即施放[刃风]。\n
    - [可强制中断的技能] -\n
    [狂风冲刺]、 [回风斩]、 [游离之风]、 [风鸣冲击]、 [朔风牵引]、 [双翼风刃]、 [风暴之眼]、 [真空旋风破]、 [风暴之拳]、 [疾风瞬影闪]、 [风卷残云]、 [怒风狂涌]
    """
    name = "刃风"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 1
    cd = 18
    mp = [132, 1108]
    uuid = "128b9ddef2262f40723deae4407bdb42"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 近距离攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 空中切割攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 地上切割攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 凝缩爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # [范围信息]
    # 风刃大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    def vp_1(self):
        """
        [刃风]\n
        抓取过程中进入无敌状态\n
        追踪范围 +20%
        """
        ...

    def vp_2(self):
        """
        [刃风]\n
        施放后命中敌人时， 对目标发动刃风剑气\n
         - 可以在其他动作中施放\n
         - 发动刃风剑气后， 可以再次施放\n
         - 发动刃风剑气时， 初始化[狂风冲刺]冷却时间\n
         - 总攻击力相同\n
        变更为可填充3次的技能\n
         - 攻击力 -67%
        """
        self.cd = 6
        self.skillRation *= 1 - 0.67  # noqa: E501
        ...

# 风暴之眼
# mage_male/swift_master/ecc23c980ea71450c0ad0c3fd232f329
# a5ccbaf5538981c6ef99b236c0a60b73/ecc23c980ea71450c0ad0c3fd232f329
class Skill28(ActiveSkill):
    """
    在自身周围生成小型风暴吸附敌人， 然后爆发出风暴的力量， 给敌人造成伤害并浮空。
    """
    name = "风暴之眼"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cube = 1
    cd = 16
    mp = [128, 766]
    uuid = "ecc23c980ea71450c0ad0c3fd232f329"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 风暴攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # [范围信息]
    # 大小比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    def vp_1(self):
        """
        [风暴之眼]\n
        直接爆发风暴的力量\n
        冷却时间及攻击力 +100%
        """
        self.cd *= 2  # noqa: E501
        self.skillRation *= 2  # noqa: E501
        ...

    def vp_2(self):
        """
        [风暴之眼]\n
        大小 +50%\n
        结束后生成持续吸附敌人的风暴
        """
        ...

# 真空旋风破
# mage_male/swift_master/1b1cfab062e0768bcc889e33e1f30dbf
# a5ccbaf5538981c6ef99b236c0a60b73/1b1cfab062e0768bcc889e33e1f30dbf
class Skill29(ActiveSkill):
    """
    生成龙卷风制压敌人。 施放后先将敌人吸附到龙卷风中心， 然后引发爆炸并给敌人造成伤害。
    """
    name = "真空旋风破"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [164, 983]
    uuid = "1b1cfab062e0768bcc889e33e1f30dbf"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 龙卷风攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 8
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 龙卷风多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [范围信息]
    # 大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [真空旋风破]\n
        施放技能后可以移动\n
        攻击时间 -30%\n
        大小 +30%
        """
        ...

    def vp_2(self):
        """
        [真空旋风破]\n
        在一定范围内最强敌人的位置生成龙卷风\n
         - 龙卷风持续追踪敌人\n
         - 删除强制控制和聚集敌人的功能
        """
        ...

# 风暴之拳
# mage_male/swift_master/c77a417c43de80c4ce32c1ed405d174a
# a5ccbaf5538981c6ef99b236c0a60b73/c77a417c43de80c4ce32c1ed405d174a
class Skill30(ActiveSkill):
    """
    聚集风的力量， 施展致命的重拳。 若被重拳命中， 则会引发风暴并给予多段伤害。 若使用方向键， 可以向前突进并施展重拳。
    """
    name = "风暴之拳"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [311, 1866]
    uuid = "c77a417c43de80c4ce32c1ed405d174a"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 重拳攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 风暴多段攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 5
    # 风暴多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [范围信息]
    # 大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [风暴之拳]\n
        聚集前方的敌人后施展重拳\n
        删除风暴攻击\n
         - 总攻击力相同\n
        大小 +30%
        """
        ...

    def vp_2(self):
        """
        [风暴之拳]\n
        在原地施放\n
        删除重拳攻击伤害\n
         - 总攻击力相同\n
        在准备重拳时再次按部分技能键， 将生成强化风暴\n
         - 目标技能 : [风卷残云]、 [游龙惊风破]、 [九霄风雷]\n
         - 并入再次按下的技能伤害量
        """
        ...

# 御风之力
# mage_male/swift_master/852f8ad797db4dca1405cb3e77198401
# a5ccbaf5538981c6ef99b236c0a60b73/852f8ad797db4dca1405cb3e77198401
class Skill31(PassiveSkill):
    """
    接受风神的力量， 变得更加锐利和敏捷。\n
    增加暴击伤害和移动速度。
    """
    name = "御风之力"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    uuid = "852f8ad797db4dca1405cb3e77198401"
    hasVP = False
    hasUP = False

    # 暴击攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 移动速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    associate = [{"data":data0}]

# 万象风龙阵
# mage_male/swift_master/0b8db1e10b3abbd24d38564e708675d5
# a5ccbaf5538981c6ef99b236c0a60b73/0b8db1e10b3abbd24d38564e708675d5
class Skill32(ActiveSkill):
    """
    召唤飓风， 将地面上的所有敌人横扫一空。 飓风飞速旋转并粉碎敌人。
    """
    name = "万象风龙阵"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [600, 5040]
    uuid = "0b8db1e10b3abbd24d38564e708675d5"
    hasVP = False
    hasUP = False

    # 飓风攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 56
    # 飓风爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 4
    # 飓风多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 飓风爆炸次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

# 疾风瞬影闪
# mage_male/swift_master/dcb31a63ef58954f44ff2070c42a9a98
# a5ccbaf5538981c6ef99b236c0a60b73/dcb31a63ef58954f44ff2070c42a9a98
class Skill33(ActiveSkill):
    """
    生成风之剑， 向前突进并疯狂砍伤敌人。 被风刃割伤的敌人， 会追加受到疾风的伤害。 按向前方向键时， 可以增加突进距离。
    """
    name = "疾风瞬影闪"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [220, 1320]
    uuid = "dcb31a63ef58954f44ff2070c42a9a98"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 风之剑攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 8
    # 风之剑多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # 大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    def vp_1(self):
        """
        [疾风瞬影闪]\n
        在原地生成疾风\n
         - 总攻击力相同\n
        生成疾风后可以移动
        """
        ...

    def vp_2(self):
        """
        [疾风瞬影闪]\n
        按向前方向键时， 移动距离 +100%\n
        施放时间 -20%\n
        大小 +50%
        """
        ...

# 风卷残云
# mage_male/swift_master/8572675ec6a1f50b6eff6a867376c2de
# a5ccbaf5538981c6ef99b236c0a60b73/8572675ec6a1f50b6eff6a867376c2de
class Skill34(ActiveSkill):
    """
    在自身周围生成强力的风暴后， 向前抛出。 周围的敌人会吸附到风暴中心。\n
    向前方抛出的风暴持续一定时间后爆炸。 按方向键时， 可以抛出更远的距离。
    """
    name = "风卷残云"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [551, 3305]
    uuid = "8572675ec6a1f50b6eff6a867376c2de"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 旋转风暴攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 10
    # 旋转爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 旋转风暴多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [范围信息]
    # 大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [风卷残云]\n
        删除强控敌人效果\n
        大小 +50%\n
        - 追加雷电风暴攻击\n
        攻击时间 -30%
        """
        ...

    def vp_2(self):
        """
        [风卷残云]\n
        旋转风暴持续时间增加\n
        每次攻击恢复2%的魔法值
        """
        ...

# 风神诀
# mage_male/swift_master/b5e3d014f75f3d17abdea52cca57f7e9
# a5ccbaf5538981c6ef99b236c0a60b73/b5e3d014f75f3d17abdea52cca57f7e9
class Skill35(PassiveSkill):
    """
    攻击时造成额外的多段伤害。
    """
    name = "风神诀"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 3
    uuid = "b5e3d014f75f3d17abdea52cca57f7e9"
    hasVP = False
    hasUP = False

    # 追加伤害比率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    associate = [{"data":data0}]

# 游龙惊风破
# mage_male/swift_master/d110449993fb973f1a62c62c695003db
# a5ccbaf5538981c6ef99b236c0a60b73/d110449993fb973f1a62c62c695003db
class Skill36(ActiveSkill):
    """
    向前方抛出压缩后的飓风， 然后利用超强的旋转力量引发巨大的爆炸。 若飓风没有触碰到敌人， 角色则不会突进， 飓风将自动爆炸。
    """
    name = "游龙惊风破"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "d110449993fb973f1a62c62c695003db"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 12
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [范围信息]
    # 大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [游龙惊风破]\n
        追击最强大的敌人， 使用浓缩的风暴之力攻击地面并引发爆炸\n
         - 探索范围内不存在追击对象时， 不激活技能\n
         - 可以在空中施放\n
         - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [游龙惊风破]\n
        投掷自动旋转的风暴\n
        可以发动风暴旋转的距离 +25%\n
        可以强制中断施放后僵直， 并施放[狂风冲刺]
        """
        ...

# 九霄风雷
# mage_male/swift_master/b799700ee73e99e0ac27aaa307492033
# a5ccbaf5538981c6ef99b236c0a60b73/b799700ee73e99e0ac27aaa307492033
class Skill37(ActiveSkill):
    """
    和龙卷风合为一体， 攻击指定位置的敌人。施放时， 可以指定龙卷风降临的位置， 然后和龙卷风合为一体给予敌人多段伤害并引发爆炸造成巨大伤害。 龙卷风降临的位置只能选择角色前方。 选择位置过程中， 再次按攻击键 (x) 或技能键可以立即开始冲撞。 可以在空中施放该技能。
    """
    name = "九霄风雷"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "b799700ee73e99e0ac27aaa307492033"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 14
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [范围信息]
    # 大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [九霄风雷]\n
        风暴降临后可以移动\n
        攻击时间 -30%
        """
        ...

    def vp_2(self):
        """
        [九霄风雷]\n
        可以强制中断部分技能的僵直， 并施放[九霄风雷]\n
        强制中断后技能结束时， 被击所损失生命值的25%由魔法值代偿， 效果持续15秒
        """
        ...

# 无限风域
# mage_male/swift_master/5ece7efb92358406e59338ef66479010
# a5ccbaf5538981c6ef99b236c0a60b73/5ece7efb92358406e59338ef66479010
class Skill38(ActiveSkill):
    """
    借助狂风之力， 在风暴中心内快速飞行并攻击敌人。 被命中的敌人处于僵直状态， 最后向范围内最强的敌人(领主 > 稀有 > 深渊 > 普通怪物)施展最后一击。 攻击期间， 若连续按攻击键或技能键， 会减少攻击时间。 可以在空中施放该技能。
    """
    name = "无限风域"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [1500, 5000]
    uuid = "5ece7efb92358406e59338ef66479010"
    hasVP = False
    hasUP = False

    # 狂风攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 飞行攻击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 8
    # 最后刺击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 最后爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # 飞行攻击多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

# 初始之风
# mage_male/swift_master/05ee4433394678e5014c67dafee798ff
# a5ccbaf5538981c6ef99b236c0a60b73/05ee4433394678e5014c67dafee798ff
class Skill39(PassiveSkill):
    """
    知源·逐风者将黑暗之眼的力量在体内同化， 与风化为一体， 展现撕裂一切、 不被任何东西束缚的危险而自由的力量。\n
    增加基本攻击力和转职技能攻击力， 部分技能效果变更并获得新的能力。\n
    [游离之风]\n
    旋风击中敌人时引发巨大风暴， 攻击大范围的敌人。\n
    [狂风冲刺]\n
    被攻击或倒地状态下施放时， 可以躲避敌人的攻击。 (存在单独冷却时间)\n
    施放过程中， 按方向键可以指定躲避方向。
    """
    name = "初始之风"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    uuid = "05ee4433394678e5014c67dafee798ff"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    associate = [{"data":data0}]

# 怒风狂涌
# mage_male/swift_master/29c0b8b3eed7252b3bdcddc2b4e9e3a0
# a5ccbaf5538981c6ef99b236c0a60b73/29c0b8b3eed7252b3bdcddc2b4e9e3a0
class Skill40(ActiveSkill):
    """
    逐风者在天空中呼唤飓风， 与风暴同化， 向四面八方呼啸而过， 将命中的敌人拉到中央， 生成狂乱气流。\n
    然后， 逐风者再次现身， 使气流汇聚成风暴后升空， 与台风的碰撞， 引发强烈爆炸。\n
    逐风者再次现身后才能强制中断技能； 强制中断技能后， 已经生成的气流和风暴不会消失。 
    """
    name = "怒风狂涌"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [773, 6000]
    uuid = "29c0b8b3eed7252b3bdcddc2b4e9e3a0"
    hasVP = False
    hasUP = False

    # 狂乱气流风暴攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 6
    # 气流风暴多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 龙卷风攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 4
    # 龙卷风多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 终结爆炸攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1

# 风之极·永坠
# mage_male/swift_master/e0578e280d5de3aa6d59b9ec7498a19b
# a5ccbaf5538981c6ef99b236c0a60b73/e0578e280d5de3aa6d59b9ec7498a19b
class Skill41(ActiveSkill):
    """
    逐风者化身风暴， 升至空中， 俯瞰地面， 随后向地面俯冲， 脚下生成强烈狂风， 粉碎一切抵抗风暴之神的愚蠢敌人， 不留一丝痕迹。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "风之极·永坠"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "e0578e280d5de3aa6d59b9ec7498a19b"
    hasVP = False
    hasUP = False

    # 跳跃攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 地面攻击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 狂风多段攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 25
    # 狂风多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'swift_master'
        self.nameCN = '知源·逐风者'
        self.role = 'mage_male'
        self.角色 = '魔法师(男)'
        self.职业 = '逐风者'
        self.jobId = 'a5ccbaf5538981c6ef99b236c0a60b73'
        self.jobGrowId = 'c9b492038ee3ca8d27d7004cf58d59f3'

        self.武器选项 = ['矛', '魔杖', '法杖', '棍棒']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '皮甲'
        self.buff = 2.195

        super().__init__(equVersion, __name__)
