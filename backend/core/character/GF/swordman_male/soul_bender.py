#41f1cdc2ff58bb5fdc287be0db2a8df3
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "swordman_male/soul_bender/cn/skillDetail"

# 鬼斩
# swordman_male/soul_bender/eb71e1d82d92c7e1d40500a0dcd77aa6
# 41f1cdc2ff58bb5fdc287be0db2a8df3/eb71e1d82d92c7e1d40500a0dcd77aa6
class Skill0(ActiveSkill):
    """
    把鬼神召唤到武器上， 并向前方敌人发出强威力的暗属性斩击。\n
    转职为鬼泣且学习[噬灵鬼斩]后\n
    按住技能键可蓄气施放， 且通过追加操作可使用[噬灵鬼斩]。\n
    学习[鬼神冠冕]后\n
    无需蓄气， 攻击时在原地发动斩击。 利用黄泉之力， 生成幽魂之布雷德的气息。
    """
    name = "鬼斩"
    learnLv = 1
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 6
    mp = [17, 196]
    uuid = "eb71e1d82d92c7e1d40500a0dcd77aa6"
    hasVP = False
    hasUP = False

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 转职为鬼泣且学习[噬灵鬼斩]后
    # 最大蓄气时攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 鬼神追加攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [萨亚攻击时]
    # 冰冻几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 冰冻持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [普戾蒙攻击时]
    # 睡眠几率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 睡眠持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [学习鬼神冠冕后]
    # 鬼神斩击攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    hit7 = 1
    power7 = 1
    # 幽魂之布雷德攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    hit8 = 1
    power8 = 1
    # [范围信息]
    # 斩击范围比率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)


# 基础精通
# swordman_male/soul_bender/5a56514f35cf0270ae8d6c65f8fefd78
# 41f1cdc2ff58bb5fdc287be0db2a8df3/5a56514f35cf0270ae8d6c65f8fefd78
class Skill3(PassiveSkill):
    """
    增加基本攻击、 前冲攻击、 跳跃攻击、 [上挑]、 [连突刺]的攻击力。\n
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
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 前冲攻击力变化率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 跳跃攻击力变化率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    associate = [{"type":"*skillRation","data":[i-100 if i>0 else 0 for i in data0],"skills":["残影之凯贾"]}]

# 刀魂之卡赞
# swordman_male/soul_bender/a5fa08f5d509e6ff2ebc68856a470b5a
# 41f1cdc2ff58bb5fdc287be0db2a8df3/a5fa08f5d509e6ff2ebc68856a470b5a
class Skill10(ActiveSkill):
    """
    召唤出刀魂卡赞， 使在召唤领域内的我方队员增加力量和智力， 效果持续一定时间。\n
    刀魂卡赞存在的状态下， 再次施放此技能， 则原有的会消失， 并且重新在前方召唤出新的卡赞。\n
    - [转职为鬼泣后] -\n
    召唤功能消失， 增加自身技能攻击力。 (可以添加到快捷栏， 但无法使用)
    """
    name = "刀魂之卡赞"
    learnLv = 5
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 3
    cd = 6
    mp = [10, 400]
    uuid = "a5fa08f5d509e6ff2ebc68856a470b5a"
    hasVP = False
    hasUP = False

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 力量增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 智力增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # - [转职为鬼泣后] -
    # 自身技能攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 领域范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)
    associate = [{"data":data3}]

# 短剑精通
# swordman_male/soul_bender/01c3a2fb793d293a25ed8dc7a0d70c1a
# 41f1cdc2ff58bb5fdc287be0db2a8df3/01c3a2fb793d293a25ed8dc7a0d70c1a
class Skill16(PassiveSkill):
    """
    装备短剑系武器时， 增加攻击力和命中率。\n
    [转职为剑魂后]\n
    - 3级 : 使用[上挑]后可以追加一次攻击； 且使用[上挑]时会出现剑气\n
    - 5级 : [格挡]成功时， 对敌人生成冲击波， 并有一定几率使其进入眩晕状态\n
    - 6级 : 增加[破军升龙击]的攻击力\n
    - 7级 : 施放[拔刀斩]时会出现剑气； 施放[幻影剑舞]时增加剑气的攻击次数\n
    - 9级 : 增加[猛龙断空斩]的攻击力\n
    [装备传世武器后]\n
    适用独立的攻击力/命中率增加数值。
    """
    name = "短剑精通"
    learnLv = 15
    masterLv = 30
    maxLv = 40
    line = 0
    position = 0
    rangeLv = 3
    uuid = "01c3a2fb793d293a25ed8dc7a0d70c1a"
    hasVP = False
    hasUP = False

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 命中率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [剑魂特殊附加效果]
    # [里 · 鬼剑术]剑气攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [格挡]冲击波攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [格挡]冲击波眩晕几率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [格挡]冲击波眩晕持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [上挑]第1击攻击力增加率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [上挑]第2击攻击力增加率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [上挑]浮空力 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [三段刃]攻击力增加率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # [破军升龙击]攻击力增加率 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # [猛龙断空斩]攻击力增加率 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # [装备传世武器后]
    # 物理攻击力增加率 : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # 魔法攻击力增加率 : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # 命中率增加 : {value15}%
    data15 = get_data(f'{prefix}/{uuid}', 15)

    def effect(self, old, new):
        weapon = self.char.charEquipInfo["武器"].equInfo
        if weapon is None or weapon.itemDetailType != "短剑":
            return
        data = self.data1
        if weapon.categorize == "传世武器":
            data = self.data14
        self.associate = [{"type":"$*PAtkM","data":data}]
        return super().effect(old, new)


# 太刀精通
# swordman_male/soul_bender/8f73f243041c2d27739fe7696f02bf9b
# 41f1cdc2ff58bb5fdc287be0db2a8df3/8f73f243041c2d27739fe7696f02bf9b
class Skill17(PassiveSkill):
    """
    装备太刀系武器时， 增加攻击力和命中率。\n
    [转职为剑魂后]\n
    - 5级 : [三段刃]增加攻击次数， 最后一击还可以浮空敌人\n
    - 7级 :使用[拔刀斩]可以发动追加攻击； 使用[幻影剑舞]可以增加斩击次数和速度， 减少斩击攻击力\n
    - 10级 :  攻击时会附加刺伤效果， 使用[空之连刃]时， 对刺伤状态的敌人增加攻击力\n
    刺伤效果最多可以叠加17次， 达到叠加上限时， 会消耗所有刺伤效果并引爆敌人造成伤害； 刺伤效果叠加3次开始， 接下来的3秒内可以持续叠加， 若没达到叠加上限， 3秒后也会引发爆炸。\n
    [装备传世武器后]\n
    适用独立的攻击力/命中率增加数值。
    """
    name = "太刀精通"
    learnLv = 15
    masterLv = 30
    maxLv = 40
    line = 0
    position = 1
    rangeLv = 3
    uuid = "8f73f243041c2d27739fe7696f02bf9b"
    hasVP = False
    hasUP = False

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 命中率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [剑魂特殊附加效果]
    # 刺伤几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 刺伤持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 刺伤爆炸攻击力 : {value5}% ~ {value6}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 刺伤持续攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [空之连刃]附加攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [空之连刃]对刺伤状态的敌人的攻击力增加率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [装备传世武器后]
    # 物理攻击力增加率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 魔法攻击力增加率 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 命中率增加 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)


    def effect(self, old, new):
        weapon = self.char.charEquipInfo["武器"].equInfo
        if weapon is None or weapon.itemDetailType != "太刀":
            return
        data = self.data1
        if weapon.categorize == "传世武器":
            data = self.data11
        self.associate = [{"type":"$*PAtkM","data":data}]
        return super().effect(old, new)

# 巨剑精通
# swordman_male/soul_bender/8c2379737c5acc935c1731f67f607655
# 41f1cdc2ff58bb5fdc287be0db2a8df3/8c2379737c5acc935c1731f67f607655
class Skill18(PassiveSkill):
    """
    装备巨剑系武器时， 增加攻击力和命中率。\n
    [转职为剑魂后]\n
    - 3级 : 使用[银光落刃]时可以使自身进入霸体状态， 并对敌人进行多段攻击； 使用[里 · 鬼剑术]时， 第1次斩击会出现飓风， 按住技能键可以蓄气进行第2次斩击； 使用[拔刀斩]时， 按住技能键可以进行蓄气攻击\n
    - 5级 : [格挡]成功时， 对敌人生成冲击波， 并有一定几率使其进入眩晕状态\n
    - 7级 : 使用[破军升龙击]后还可以追加捶击攻击\n
    [装备传世武器后]\n
    适用独立的攻击力/命中率增加数值。
    """
    name = "巨剑精通"
    learnLv = 15
    masterLv = 30
    maxLv = 40
    line = 0
    position = 0
    rangeLv = 3
    uuid = "8c2379737c5acc935c1731f67f607655"
    hasVP = False
    hasUP = False

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 命中率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [剑魂特殊附加效果]
    # [格挡]冲击波攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [格挡]冲击波眩晕几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [格挡]冲击波眩晕持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [银光落刃]多段攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [里 · 鬼剑术]达蓄气上限时攻击力增加率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [拔刀斩]达蓄气上限时攻击力增加率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [装备传世武器后]
    # 物理攻击力增加率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 魔法攻击力增加率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 命中率增加 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)

    def effect(self, old, new):
        weapon = self.char.charEquipInfo["武器"].equInfo
        if weapon is None or weapon.itemDetailType != "巨剑":
            return
        data = self.data1
        if weapon.categorize == "传世武器":
            data = self.data10
        self.associate = [{"type":"$*PAtkM","data":data}]
        return super().effect(old, new)

# 钝器精通
# swordman_male/soul_bender/9cb6f9ed646fa87f9b7680a42ce83d1a
# 41f1cdc2ff58bb5fdc287be0db2a8df3/9cb6f9ed646fa87f9b7680a42ce83d1a
class Skill19(PassiveSkill):
    """
    装备钝器系武器时， 增加攻击力和命中率。\n
    [转职为剑魂后]\n
    - 3级 : 使用[后跳斩]时可以生成物理冲击波使敌人浮空； 使用[里 · 鬼剑术]时， 增加对眩晕状态下的敌人的攻击力。\n
    - 5级 : 进行跳跃攻击并命中敌人时可以生成物理冲击波。\n
    - 7级 : 使用[破军升龙击]后还可以追加蓄气型捶击攻击， 并生成冲击波； [幻影剑舞]最后一击由剑气变为冲击波； 通过[银光落刃]技能升级， 可以增加冲击波范围。\n
    [装备传世武器后]\n
    适用独立的攻击力/命中率增加数值。
    """
    name = "钝器精通"
    learnLv = 15
    masterLv = 30
    maxLv = 40
    line = 0
    position = 1
    rangeLv = 3
    uuid = "9cb6f9ed646fa87f9b7680a42ce83d1a"
    hasVP = False
    hasUP = False

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 命中率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [剑魂特殊附加效果]
    # [后跳斩]浮空力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [后跳斩]冲击波攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 对眩晕状态的敌人造成的[里 · 鬼剑术]攻击力增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 跳跃攻击时的浮空力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 跳跃攻击时的冲击波攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [后跳斩]攻击力增加率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [装备传世武器后]
    # 物理攻击力增加率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 魔法攻击力增加率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 命中率增加 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)

    def effect(self, old, new):
        weapon = self.char.charEquipInfo["武器"].equInfo
        if weapon is None or weapon.itemDetailType != "钝器":
            return
        data = self.data1
        if weapon.categorize == "传世武器":
            data = self.data9
        self.associate = [{"type":"$*PAtkM","data":data}]
        return super().effect(old, new)


# 暗月降临
# swordman_male/soul_bender/a6c8f69107f8c4f5d1a0c7a57d000290
# 41f1cdc2ff58bb5fdc287be0db2a8df3/a6c8f69107f8c4f5d1a0c7a57d000290
class Skill21(PassiveSkill):
    """
    持续增加自身和队员的暗属性抗性， 并增加自身属性攻击力。
    """
    name = "暗月降临"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 5
    rangeLv = 5
    uuid = "a6c8f69107f8c4f5d1a0c7a57d000290"
    hasVP = False
    hasUP = False

    # 自身和队员暗属性抗性增加量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 自身属性攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [{"data":data1}]

# 封印解除
# swordman_male/soul_bender/27bade584bb42fef68148d3a0b72bace
# 41f1cdc2ff58bb5fdc287be0db2a8df3/27bade584bb42fef68148d3a0b72bace
class Skill22(PassiveSkill):
    """
    解除鬼泣左臂封印， 释放压制的鬼神力量， 使[刀魂之卡赞]、 [冰霜之萨亚]、 [侵蚀之普戾蒙]、 [鬼斩]、 [瘟疫之罗刹]、 [冥炎之卡洛]技能各增加1级。 增加魔法暴击率和卡赞的效果范围。\n
    技能等级增加效果只能生效一次。
    """
    name = "封印解除"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 2
    rangeLv = 3
    uuid = "27bade584bb42fef68148d3a0b72bace"
    hasVP = False
    hasUP = False

    # 魔法暴击率增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 卡赞领域范围增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 施放速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [{"type":"+lv","data":[0] + [1]*maxLv,"skills":["刀魂之卡赞", "冰霜之萨亚", "侵蚀之普戾蒙", "鬼斩", "瘟疫之罗刹", "冥炎之卡洛"],"ratio":1}]# noqa: E501

# 侵蚀之普戾蒙
# swordman_male/soul_bender/01384bbfc346775d1267fa0bc4ca605f
# 41f1cdc2ff58bb5fdc287be0db2a8df3/01384bbfc346775d1267fa0bc4ca605f
class Skill23(ActiveSkill):
    """
    召唤普戾蒙， 使进入普戾蒙的领域内的敌人减少控制型异常状态抗性， 并增加自身造成的物理和魔法伤害。\n
    敌人走出普戾蒙的领域后， 普戾蒙效果仍会持续一定时间。\n
    普戾蒙存在的状态下， 再次施放此技能， 则原有的会消失， 并且重新在前方召唤出新的普戾蒙。\n
    学习[御鬼之极]时\n
    召唤功能消失， 变更为被动技能， 增加自身造成的伤害量、 减少受到攻击的敌人的控制型异常状态抗性。
    """
    name = "侵蚀之普戾蒙"
    learnLv = 15
    masterLv = 1
    maxLv = 11
    position = 6
    rangeLv = 3
    cd = 6
    mp = [40, 644]
    uuid = "01384bbfc346775d1267fa0bc4ca605f"
    hasVP = False
    hasUP = False

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 敌人控制型异常状态抗性减少 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 伤害增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 敌人离开领域后效果持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [学习御鬼之极后]
    # 控制型异常状态抗性减少效果持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 效果范围 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)
    associate  = [{"data":data2}]


# 月光斩
# swordman_male/soul_bender/a2d943797daca862a6f321aca6ac9bfa
# 41f1cdc2ff58bb5fdc287be0db2a8df3/a2d943797daca862a6f321aca6ac9bfa
class Skill25(ActiveSkill):
    """
    向敌人发出暗属性伤害的单手月形斩击， 并追加一个发动单手上斩的[月光斩]。\n
    向前方前进的同时施放[月光斩]， 可以通过方向键调整移动距离。\n
    [转职为鬼泣后]\n
    可以强制中断并施放。\n
    可掌握[满月斩]\n
    若掌握[满月斩]时， 使用单手上斩后可以追加一个双手上斩。\n
    学习[鬼神冠冕]后\n
    制造月亮并用斩击将鬼气注入到月亮之中， 然后破坏黑月攻击敌人。 破坏黑月时使敌人进入失明状态。 删除追加按键功能。
    """
    name = "月光斩"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 4
    mp = [17, 182]
    uuid = "a2d943797daca862a6f321aca6ac9bfa"
    hasVP = False
    hasUP = True

    # 月形斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 单手上斩攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 双手上斩攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 学习[鬼神冠冕]后
    # 制造月亮攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    data3 = [0, 1936, 2135, 2332, 2526, 2725, 2919, 3116, 3313, 3511, 3708, 3903, 4100, 4294, 4493, 4687, 4884, 5085, 5282, 5472, 5673, 5872, 6066, 6263, 6460, 6659, 6851, 7048, 7245, 7443, 7638, 7835, 8033, 8230, 8422, 8621, 8821, 9013, 9212, 9410, 9602, 9801, 9998, 10197, 10394, 10588, 10788, 10980, 11179, 11375, 11570, 11769, 11968, 12160, 12357, 12556, 12750, 12949, 13144, 13343, 13537, 13734, 13930, 14127, 14324, 14525, 14717, 14916, 15108, 15307, 15507]# noqa: E501
    hit3 = 1
    # 染月攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    data4 = [0, 1221, 1338, 1465, 1588, 1712, 1836, 1960, 2079, 2205, 2332, 2453, 2579, 2701, 2827, 2948, 3072, 3194, 3320, 3444, 3568, 3689, 3815, 3937, 4061, 4185, 4306, 4430, 4558, 4680, 4803, 4930, 5049, 5173, 5297, 5420, 5547, 5671, 5790, 5916, 6038, 6163, 6287, 6407, 6531, 6659, 6781, 6904, 7031, 7152, 7276, 7398, 7521, 7647, 7772, 7893, 8017, 8141, 8264, 8388, 8512, 8631, 8758, 8884, 9007, 9131, 9255, 9377, 9500, 9624, 9748]# noqa: E501
    hit4 = 1
    # 黑月爆炸攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    data5 = [0, 1379, 1520, 1658, 1799, 1936, 2077, 2220, 2360, 2502, 2637, 2780, 2919, 3058, 3198, 3337, 3480, 3618, 3759, 3896, 4036, 4175, 4316, 4459, 4595, 4740, 4881, 5018, 5160, 5297, 5438, 5576, 5719, 5860, 5996, 6137, 6276, 6418, 6554, 6695, 6839, 6979, 7120, 7259, 7398, 7538, 7677, 7820, 7959, 8097, 8238, 8378, 8515, 8655, 8798, 8940, 9078, 9217, 9357, 9498, 9639, 9780, 9920, 10057, 10198, 10338, 10477, 10617, 10758, 10900, 11036]# noqa: E501
    hit5 = 1
    # 失明几率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 失明持续时间 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 视野 : {value8}px
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 命中率减少量 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [范围信息]
    # 斩击范围比率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)

# 暗之亲和
# swordman_male/soul_bender/da6e37c1e3f0e8867f70007d89c239ff
# 41f1cdc2ff58bb5fdc287be0db2a8df3/da6e37c1e3f0e8867f70007d89c239ff
class Skill26(PassiveSkill):
    """
    强化对黑暗的亲和力， 可以增加自身的暗属性抗性， 但光属性抗性将减少。
    """
    name = "暗之亲和"
    learnLv = 18
    masterLv = 1
    maxLv = 1
    line = 15
    position = 7
    rangeLv = 1
    uuid = "da6e37c1e3f0e8867f70007d89c239ff"
    hasVP = False
    hasUP = False

    # 暗属性抗性增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 光属性抗性减少 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 残影之凯贾
# swordman_male/soul_bender/d085127b0edd719782bd618d5688f4a1
# 41f1cdc2ff58bb5fdc287be0db2a8df3/d085127b0edd719782bd618d5688f4a1
class Skill27(ActiveSkill):
    """
    借鬼神之力增加自身的暴击伤害和移动速度， 且前冲的一定时间内会进入无敌状态； 基本攻击和前冲攻击会转换成受[基础精通]影响的暗属性魔法攻击。\n
    同时， 增加物理/魔法防御力， 且被击时有一定几率进入无敌状态。
    """
    name = "残影之凯贾"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 5
    rangeLv = 3
    cd = 5
    uuid = "d085127b0edd719782bd618d5688f4a1"
    hasVP = False
    hasUP = False
    buff = True

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 无敌时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 暴击伤害增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 移动速度增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 第1击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # 第2击攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # 第3击攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 1
    # 第4击攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    hit7 = 1
    # 前冲攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 物理防御力增加量 : {value9}
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 魔法防御力增加量 : {value10}
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 回避率增加 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 被击时无敌发动几率 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 被击时无敌持续时间 : {value13}秒
    data13 = get_data(f'{prefix}/{uuid}', 13)

# 满月斩
# swordman_male/soul_bender/c77a417c43de80c4ce32c1ed405d174a
# 41f1cdc2ff58bb5fdc287be0db2a8df3/c77a417c43de80c4ce32c1ed405d174a
class Skill28(PassiveSkill):
    """
    施放月光斩的单手上斩后， 追加一个造成暗属性伤害的双手上斩。
    """
    name = "满月斩"
    learnLv = 20
    masterLv = 1
    maxLv = 1
    position = 4
    rangeLv = 1
    uuid = "c77a417c43de80c4ce32c1ed405d174a"
    hasVP = False
    hasUP = False



# 湮灭仪式
# swordman_male/soul_bender/2e9c5a06ff3fe8aea672a2a55c40fdbf
# 41f1cdc2ff58bb5fdc287be0db2a8df3/2e9c5a06ff3fe8aea672a2a55c40fdbf
class Skill30(ActiveSkill):
    """
    消除地图中的[侵蚀之普戾蒙]、 [冰霜之萨亚]、 [瘟疫之罗刹]。
    """
    name = "湮灭仪式"
    learnLv = 20
    masterLv = 1
    maxLv = 1
    position = 7
    rangeLv = 2
    cd = 1
    mp = [50, 50]
    uuid = "2e9c5a06ff3fe8aea672a2a55c40fdbf"
    hasVP = False
    hasUP = False


# 鬼神解放
# swordman_male/soul_bender/b1ccbd90d0b40f543ece3b18fcef827f
# 41f1cdc2ff58bb5fdc287be0db2a8df3/b1ccbd90d0b40f543ece3b18fcef827f
class Skill31(PassiveSkill):
    """
    施放[裂波斩]、 [鬼斩]、 [月光斩]、 [鬼影鞭]、 [死亡墓碑]、 [鬼影闪]、 [鬼斩 : 狂怒]、 [第7鬼神 : 怖拉修]、 [鬼斩 : 炼狱]、 [幽魂降临 : 式]、 [王者号令 : 吉格降临]、 [鬼神剑·黄泉摆渡]过程中， 可以无施放动作立即发动[侵蚀之普戾蒙]、 [冰霜之萨亚]、 [瘟疫之罗刹]、 [冥祭之沼]、 [幽魂之布雷德]。\n
    攻击技能倾向不同， 地板技能设置的位置也不相同。\n
    只有学习[噬灵鬼斩]、 [满月斩]后， 才能在[鬼斩]和[月光斩]施放中发动以上技能。
    """
    name = "鬼神解放"
    learnLv = 20
    masterLv = 1
    maxLv = 1
    position = 2
    rangeLv = 2
    uuid = "b1ccbd90d0b40f543ece3b18fcef827f"
    hasVP = False
    hasUP = False

    # 前方100px设置技能 : [裂波斩]、 [鬼斩]、 [月光斩]、 [鬼影鞭]、 [鬼斩 - 狂怒]、 [冥炎剑]
    # 中央设置技能 : [死亡墓碑]
    # 后方100px设置技能 : [鬼影闪]
    # 前方200px设置技能 : [第7鬼神 - 怖拉修]、 [鬼斩 - 炼狱]、 [幽魂降临 - 式]、 [王者号令 - 吉格降临]、 [鬼神剑·黄泉摆渡]

# 噬灵鬼斩
# swordman_male/soul_bender/4655101518604f874721b3cc249aae10
# 41f1cdc2ff58bb5fdc287be0db2a8df3/4655101518604f874721b3cc249aae10
class Skill32(PassiveSkill):
    """
    使用[鬼斩]后， 可追加操作施放[噬灵鬼斩]。\n
    持续按住[鬼斩]技能键可以蓄气， 使攻击力大幅度增加； 攻击后， 可通过追加操作施放[噬灵鬼斩]。\n
    当蓄气达最大值时， 可以使自身进入霸体状态， 并可通过追加操作向前推进斩击敌人并喷射鬼神冲波。\n
    鬼神冲波为卡赞、 萨亚、 普戾蒙三者中最后召唤出的鬼神； 若未召唤过任何鬼神， 则鬼神冲波默认为卡赞。\n
    按前方向键或不按方向键， 自身和鬼神一起向前推进； 按后方向键， 只有鬼神向前推进。
    """
    name = "噬灵鬼斩"
    learnLv = 25
    masterLv = 1
    maxLv = 5
    position = 3
    rangeLv = 3
    uuid = "4655101518604f874721b3cc249aae10"
    hasVP = False
    hasUP = False

    # 蓄气时间上限 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 噬灵鬼斩攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最大蓄气时霸体持续时间 : {value2}秒n[范围信息]
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 噬灵鬼斩大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    associate = [{"type":"*power7","data":data1,"skills":["鬼斩"]}]# noqa: E501


# 冰霜之萨亚
# swordman_male/soul_bender/04883563896fe1adac7505c6146b5f59
# 41f1cdc2ff58bb5fdc287be0db2a8df3/04883563896fe1adac7505c6146b5f59
class Skill34(ActiveSkill):
    """
    召唤出萨亚， 使其以一定的时间间隔给予召唤领域内的敌人冰和暗属性魔法伤害， 并使敌人进入冰冻状态， 效果持续一定时间。\n
    已经召唤萨亚的状态下施放萨亚时， 会在回收后在前方重新召唤萨亚\n
    利用ON/OFF可以开启或关闭冰冻效果。
    """
    name = "冰霜之萨亚"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 15
    mp = [150, 1260]
    uuid = "04883563896fe1adac7505c6146b5f59"
    hasVP = False
    hasUP = True

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击间隔 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 20
    # 冰冻几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 冰冻持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 领域范围 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 鬼影鞭
# swordman_male/soul_bender/d429147c372b549c3dadcabcba50787f
# 41f1cdc2ff58bb5fdc287be0db2a8df3/d429147c372b549c3dadcabcba50787f
class Skill35(ActiveSkill):
    """
    像挥鞭子一样挥舞手中的武器， 并把远距离的敌人拉到身前。\n
    若对自身在[冥炎之卡洛]状态， 则会对敌人附着冥炎。
    """
    name = "鬼影鞭"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 3
    cd = 8
    mp = [55, 700]
    uuid = "d429147c372b549c3dadcabcba50787f"
    hasVP = False
    hasUP = True

    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 僵直率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 死亡墓碑
# swordman_male/soul_bender/e49e57b2e8fbeceb0a2c56a0c63fe6c5
# 41f1cdc2ff58bb5fdc287be0db2a8df3/e49e57b2e8fbeceb0a2c56a0c63fe6c5
class Skill36(ActiveSkill):
    """
    在自身周围一定区域内落下墓碑攻击敌人， 有一定几率使被击中的敌人进入诅咒状态。\n
    墓碑掉落时， 自身会进入霸体状态并无法移动， 按跳跃键可以中断技能。\n
    按住向前方向键的状态下施放技能时， 在前方落下墓碑， 鬼神解放效果位置也变更到前方。\n
    在[冥炎之卡洛]状态下施放[死亡墓碑]时， 可以使冥炎附身在敌人身上。
    """
    name = "死亡墓碑"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 1
    cd = 18
    mp = [165, 1386]
    uuid = "e49e57b2e8fbeceb0a2c56a0c63fe6c5"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 施放范围 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 每秒掉落数量 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 诅咒几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 诅咒持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [死亡墓碑]\n
        死亡墓碑变更为吉格召集的墓碑， 可通过[鬼神解放]施放\n
        吉格召集墓碑期间， 所受伤害 -70%
        """
        ...

    def vp_2(self):
        """
        [死亡墓碑]\n
        灵魂们被引导至冥界， 其墓碑一次性落下攻击敌人\n
        - 墓碑掉落数量 +100%\n
        - 总攻击力相同\n
        - 墓碑掉落范围 +40%
        """
        ...

# 瘟疫之罗刹
# swordman_male/soul_bender/38612d8f2561edc2eb68d5057a837bfa
# 41f1cdc2ff58bb5fdc287be0db2a8df3/38612d8f2561edc2eb68d5057a837bfa
class Skill37(ActiveSkill):
    """
    制造瘟疫鬼神的领域， 召唤罗刹。\n
    罗刹会附到敌人身上， 对敌人造成腐蚀伤害， 减少硬直并使其进入减速状态， 并周期性诱发失明和诅咒状态中的任意一种异常状态。\n
     罗刹对单个敌人可以附着1个分身。\n
    召唤出罗刹的状态下， 若再次施放[瘟疫之罗刹]， 则原有的会消失， 并且重新在前方召唤出新的罗刹。\n
    在决斗场中， 敌人进入领域内时， 罗刹经过一定时间后附在敌人身上。
    """
    name = "瘟疫之罗刹"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [154, 1293]
    uuid = "38612d8f2561edc2eb68d5057a837bfa"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # [鬼神领域]
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [罗刹减益效果]
    # 分身持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 腐蚀攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 15
    # 异常状态诱发间隔 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 减速几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 减速状态下攻击速度减少率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 减速状态下移动速度减少率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 硬直减少量 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 诅咒几率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 诅咒时间 : {value9}秒
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 失明几率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 失明持续时间 : {value11}秒
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 视野 : {value12}px
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 命中率减少量 : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # [范围信息]
    # 召唤范围 : {value14}px
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # [决斗场]
    # 罗刹附在敌人身上的前置时间 : {value15}秒
    data15 = get_data(f'{prefix}/{uuid}', 15)

    def vp_1(self):
        """
        [瘟疫之罗刹]\n
        罗刹分身会离开领域范围搜寻周围敌人\n
         - 总攻击力相同\n
         - 施放时生成12个罗刹分身\n
        罗刹领域范围 +40%
        """
        ...

    def vp_2(self):
        """
        [瘟疫之罗刹]\n
        罗刹降临于现世， 根据鬼泣的攻击直接攻击敌人\n
         - 总攻击力相同\n
         - 罗刹反应技能 :  [鬼斩]、 [月光斩]、 [鬼影鞭]、 [鬼斩 : 狂怒]、 [鬼斩 : 炼狱]\n
         - 使被锚命中的敌人进入强制控制状态， 同时吸附敌人\n
         - 罗刹降临持续时间上限 : 3秒
        """
        ...

# 鬼影闪
# swordman_male/soul_bender/bc11d28c04e01923a093d65752c55516
# 41f1cdc2ff58bb5fdc287be0db2a8df3/bc11d28c04e01923a093d65752c55516
class Skill38(ActiveSkill):
    """
    以极快的速度向前移动一段距离并斩击敌人， 但只能在[残影之凯贾]使用前冲后进入无敌状态时施放。\n
    被斩击的敌人在一定时间内会进入禁锢状态， 状态结束时会对敌人造成暗属性伤害。\n
    - 学习[御鬼之极]时 -\n
    “只能在[残影之凯贾]使用前冲后进入无敌状态时施放”变更为可无条件施放， 大幅减少施放后僵直。
    """
    name = "鬼影闪"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [200, 1680]
    uuid = "bc11d28c04e01923a093d65752c55516"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 移动距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [鬼影闪]\n
        可以在施放转职技能过程中施放\n
         - 施放转职技能过程中施放时， 仅由凯贾向前移动并施放[鬼影闪]\n
        [鬼影闪]命中时， 对敌人附加[冥炎之卡洛]的黑色火焰\n
         - 只能在[冥炎之卡洛]状态下发动\n
        攻击范围 +30%
        """
        ...

    def vp_2(self):
        """
        [鬼影闪]\n
        可以强制中断部分技能并施放[鬼影闪]\n
         - 可强制中断的技能 : [鬼斩]、 [鬼斩 : 狂怒]、 [鬼斩 : 炼狱]、 [鬼神剑·黄泉摆渡]\n
        可以在空中施放[鬼影闪]\n
         - 在空中施放时， 沿对角线方向快速落下并斩击
        """
        ...

# 鬼斩 : 狂怒
# swordman_male/soul_bender/56aa7844a2da23f5bea9b585aea5ae45
# 41f1cdc2ff58bb5fdc287be0db2a8df3/56aa7844a2da23f5bea9b585aea5ae45
class Skill39(ActiveSkill):
    """
    在剑中注入鬼神之力后， 正面下斩并引发爆炸。 使被爆炸命中的敌人受到暗属性魔法伤害。
    """
    name = "鬼斩 : 狂怒"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [165, 1386]
    uuid = "56aa7844a2da23f5bea9b585aea5ae45"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [鬼斩 : 狂怒]\n
        基本冷却时间变更为40秒\n
        总攻击力 +100%\n
        攻击后生成对前方造成持续伤害的灵魂旋风\n
         - 总攻击力与原攻击力相同\n
         - 灵魂旋风命中时将敌人聚集到中心位置\n
        长按技能键可以蓄气\n
         - 最大蓄气状态维持时间 : 0.6秒\n
         - 蓄气0.2秒以上时旋风范围增加
        """
        self.cd = 40
        self.skillRation *= 2
        ...

    def vp_2(self):
        """
        [鬼斩 : 狂怒]\n
        施放时利用卡洛之力对一定范围内的所有敌人发动鬼神斩击\n
         - 总攻击力相同\n
        存在附着卡洛的黑色火焰的敌人时， 适用以下效果\n
         - 在任何位置都会受到鬼神斩击的伤害\n
         - 利用鬼神之力引发爆炸， 一次性结算卡洛的黑色火焰伤害
        """
        ...

# 冥炎之卡洛
# swordman_male/soul_bender/0b8db1e10b3abbd24d38564e708675d5
# 41f1cdc2ff58bb5fdc287be0db2a8df3/0b8db1e10b3abbd24d38564e708675d5
class Skill40(ActiveSkill):
    """
    冥炎之卡洛附身， 并向敌人发射卡洛的分身进行攻击。 受到攻击的敌人身上将会出现黑色火焰。\n
    再次施放卡洛时， 卡洛将变成紫色， 在该状态下击中敌人时， 不会触发黑色火焰。
    """
    name = "冥炎之卡洛"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cube = 2
    cd = 5
    mp = [492, 4920]
    uuid = "0b8db1e10b3abbd24d38564e708675d5"
    hasVP = False
    hasUP = False

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 分身攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 火焰攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 火焰伤害间隔 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 火焰攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 0

    mode = ["分身","冥炎"]

    def setMode(self, mode):
        if mode == "冥炎":
            self.hit1 = 0
            self.hit4 = 1
        return super().setMode(mode)

# 冥炎剑
# swordman_male/soul_bender/1c1a9606eb702ebe5a7bb4397f3aeae0
# 41f1cdc2ff58bb5fdc287be0db2a8df3/1c1a9606eb702ebe5a7bb4397f3aeae0
class Skill41(ActiveSkill):
    """
    只能在[冥炎之卡洛]状态下使用。\n
    召唤凝聚卡洛之力的冥炎剑， 以二刀流动作向前突进， 连续攻击敌人。\n
    被击中的敌人会被附着黑色火焰。
    """
    name = "冥炎剑"
    learnLv = 45
    masterLv = 1
    line = 50
    maxLv = 70
    position = 7
    rangeLv = 2
    cube = 2
    cd = 45
    uuid = "1c1a9606eb702ebe5a7bb4397f3aeae0"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

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
    # [范围信息]
    # [冥炎剑]最后一击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def skillInfo(self, mode: str | None = None):
        self.lv = self.char.GetSkillByName("冥炎之卡洛").lv
        return super().skillInfo(mode)

    def vp_1(self):
        """
        [冥炎剑]\n
        施放时召唤冥炎剑立即斩击敌人\n
         - 总攻击力相同\n
         - 按向前方向键时增加移动距离\n
        斩击攻击范围 +30%
        """
        ...

    def vp_2(self):
        """
        [冥炎剑]\n
        召唤卡洛持续一定时间， 为领域内的敌人附着上黑色火焰， 以一定时间间隔造成火/暗属性伤害\n
         - 总攻击力相同\n
         - 卡洛召唤状态下再次施放时， 回收原有的卡洛， 并在前方召唤\n
         - 可以通过鬼神解放使用
        """
        ...

# 恐惧光环
# swordman_male/soul_bender/7e904ea3d2a9faa054604e55120a9268
# 41f1cdc2ff58bb5fdc287be0db2a8df3/7e904ea3d2a9faa054604e55120a9268
class Skill42(PassiveSkill):
    """
    散发可以使周围敌人恐惧的黑暗光环， 可以增加自身技能攻击力， 每隔一定时间持续对敌人赋予减速状态。\n
    利用ON/OFF可以开启或关闭减速功能。
    """
    name = "恐惧光环"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 3
    uuid = "7e904ea3d2a9faa054604e55120a9268"
    hasVP = False
    hasUP = False

    # 光环范围 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 减速几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 敌人攻击速度减少 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 敌人移动速度减少 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 减速发生间隔 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 减速持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 技能攻击力增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    associate = [{"data":data6}]

# 第7鬼神 : 怖拉修
# swordman_male/soul_bender/b8f4966608e4ebb3cc80ba4eac3649bb
# 41f1cdc2ff58bb5fdc287be0db2a8df3/b8f4966608e4ebb3cc80ba4eac3649bb
class Skill43(ActiveSkill):
    """
    召唤出怖拉修协助自身战斗。\n
    技能施放后， 会出现范围缓缓变大的怖拉修沼泽， 当沼泽面积达到最大时， 怖拉修会出现并攻击敌人。\n
    怖拉修出现时， 会引发冲击波并使敌人受到暗属性伤害； 当他合上大颚时， 还会使敌人受到第2次暗属性伤害。\n
    减少命中率的技能效果叠加时， 只适用数值最高的效果。\n
    召唤出的鬼神越多 (最多4只)， 怖拉修造成的伤害越大。\n
    可以提升怖拉修攻击力的鬼神 : 卡赞、 普戾蒙、 萨亚、 罗刹、 凯贾、 卡洛
    """
    name = "第7鬼神 : 怖拉修"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 8
    rangeLv = 5
    cube = 5
    cd = 140
    mp = [600, 5040]
    uuid = "b8f4966608e4ebb3cc80ba4eac3649bb"
    hasVP = False
    hasUP = False

    # 冲击波攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    power0 = 1.8
    # 吞噬敌人时攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    power1 = 1.8
    # 减速、 命中率减少范围 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 减速几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 移动速度减少率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 减速持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 减速发生间隔 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 命中率减少率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 怖拉修攻击力增加率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 沼泽攻击力 : {value9}%
    hit2 = 5
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 每只鬼神对怖拉修的攻击力增加量 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 鬼神叠加数上限 : {value11} 
    data11 = get_data(f'{prefix}/{uuid}', 11)

    skillDamage = 1.1

# 鬼斩 : 炼狱
# swordman_male/soul_bender/d89f26862e348a801b30bb9fd7125db5
# 41f1cdc2ff58bb5fdc287be0db2a8df3/d89f26862e348a801b30bb9fd7125db5
class Skill44(ActiveSkill):
    """
    劈开大地， 召唤冥界刀刃， 对敌人造成暗属性魔法伤害。 被刀刃击中的敌人进入控制状态， 效果持续一定时间。
    """
    name = "鬼斩 : 炼狱"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [400, 1120]
    uuid = "d89f26862e348a801b30bb9fd7125db5"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冥界刀刃攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 2
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 控制时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 攻击次数上限 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 攻击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [鬼斩 : 炼狱]\n
        通过冥界之力， 使更多的刀刃以前方最强敌人为中心涌出\n
         - 总攻击力相同\n
         - 寻敌范围 : 700px
        """
        ...

    def vp_2(self):
        """
        [鬼斩 : 炼狱]\n
        可以强制中断转职技能的施放后僵直， 并施放[鬼斩 : 炼狱]\n
         - 可以强制中断[鬼斩 : 炼狱]施放后僵直， 并施放转职技能
        """
        ...

# 冥祭之沼
# swordman_male/soul_bender/2ff50c35efcf0f287c4c418c8454da48
# 41f1cdc2ff58bb5fdc287be0db2a8df3/2ff50c35efcf0f287c4c418c8454da48
class Skill45(ActiveSkill):
    """
    在自身周围一定区域内升起墓碑， 强制开启通往冥界之门。\n
    在持续时间内， 冥界之门将周围的敌人吸附到中央。\n
    经过一段时间或再次按技能键， 墓碑周围会发生暗属性爆炸， 同时墓碑消失。\n
    施放技能时按前、 后方向键， 可以在前、 后方设置墓碑。
    """
    name = "冥祭之沼"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [822, 1726]
    uuid = "2ff50c35efcf0f287c4c418c8454da48"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 吸附敌人持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 前方设置 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 后方设置 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 吸附敌人的范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 爆炸范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [冥祭之沼]\n
        封印的墓碑爆炸时对自身施加鬼神之力， 获得速度增加增益效果\n
         - 所有速度增加量 : 15%\n
         - 增益持续时间 : 30秒
        """
        ...

    def vp_2(self):
        """
        [冥祭之沼]\n
        可指定被封印的墓碑的召唤位置\n
        变更为可填充2次的技能\n
         - 每次填充冷却时间 : 20秒\n
         - 攻击力 -50%\n
        爆炸范围 +40%\n
        通过鬼神解放施放时， 无法指定位置
        """
        self.cd = 20
        self.skillRation *= 0.5
        ...

# 幽魂之布雷德
# swordman_male/soul_bender/c4a5b868f1e8e60cd1867a2cfab4a242
# 41f1cdc2ff58bb5fdc287be0db2a8df3/c4a5b868f1e8e60cd1867a2cfab4a242
class Skill46(ActiveSkill):
    """
    召唤出幽魂之布雷德的残影并攻击敌人。\n
    召唤阵中的幽魂攻击将附加暗属性， 并且可以对敌人造成较高的僵直。 幽魂消失时， 会发动强力的最后一击。\n
    若再按一次技能键， 会立即发动最后一击。
    """
    name = "幽魂之布雷德"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "c4a5b868f1e8e60cd1867a2cfab4a242"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 幽魂攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 32
    # 范围斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 4
    # 最后的斩击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 僵直率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 领域范围 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)

    mode = ["打满","终结"]

    def setMode(self, mode):
        if mode == "终结":
            self.hit0 = 4
        return super().setMode(mode)

    def vp_1(self):
        """
        [幽魂之布雷德]\n
        幽魂之布雷德跟随自身， 对周围敌人进行攻击\n
         - 再次按技能键时， 立即发动终结攻击\n
        领域持续时间 -2秒\n
         - 总攻击力相同\n
         - 幽魂多段攻击间隔 -75%
        """
        ...

    def vp_2(self):
        """
        [幽魂之布雷德]\n
        施放[幽魂之布雷德]时， 召唤包括卡赞和普戾蒙在内， 所有可召唤的鬼神\n
         - 卡赞 : 4.5秒内， 领域中鬼泣的所有速度 +10%\n
         - 普戾蒙 : 4.5秒内， 领域中鬼泣的回避率 +20%
        """
        ...

# 御鬼之极
# swordman_male/soul_bender/95103ae7c54eaedea3bbcf726520db6c
# 41f1cdc2ff58bb5fdc287be0db2a8df3/95103ae7c54eaedea3bbcf726520db6c
class Skill47(PassiveSkill):
    """
    掌握[御鬼之极]后， 增加[鬼斩]、 [月光斩]， 以及鬼泣的转职技能攻击力。\n
    [鬼影闪] - “只能在[残影之凯贾]使用前冲后进入无敌状态时施放”变更为可无条件施放， 并大幅减少施放后僵直。\n
    [侵蚀之普戾蒙] - 召唤功能消失， 变更为增加伤害、 减少异常状态抗性的被动技能。\n
    可使用ON/OFF功能自由开闭[死亡墓碑]、 [王者号令 : 吉格降临]的诅咒功能。
    """
    name = "御鬼之极"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "95103ae7c54eaedea3bbcf726520db6c"
    hasVP = False
    hasUP = False

    # 技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]

# 幽魂降临 : 式
# swordman_male/soul_bender/96e72ec364dada85600c907ecd95a140
# 41f1cdc2ff58bb5fdc287be0db2a8df3/96e72ec364dada85600c907ecd95a140
class Skill48(ActiveSkill):
    """
    跳跃到空中， 使幽魂之布雷德降临到自己身上， 释放强大的剑气。 剑气劈裂地面后爆炸。\n
    施放技能时， 按前方向键可以向前方跳跃、 按下方向键向后跳跃。\n
    可以在空中施放。
    """
    name = "幽魂降临 : 式"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "96e72ec364dada85600c907ecd95a140"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 最后一击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 爆炸范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [幽魂降临 : 式]\n
        可以在后跳过程中施放； 在地面施放时不再跳跃， 立即施放下劈斩击\n
        冥界之刃命中时强制控制敌人\n
        - 强制控制时间 : 1秒\n
        攻击范围 +15%
        """
        ...

    def vp_2(self):
        """
        [幽魂降临 : 式]\n
        向前方最强的敌人施以斩断灵魂的剑击\n
         - 总攻击力相同\n
        给1个命中的敌人留下鬼王的印记\n
         - 拥有鬼王印记的敌人， 在任何位置都会受到鬼神的伤害\n
         - 印记持续时间 : 8秒
        """
        ...

# 王者号令 : 吉格降临
# swordman_male/soul_bender/9bc30e0f6e22b0333762d04acae7d252
# 41f1cdc2ff58bb5fdc287be0db2a8df3/9bc30e0f6e22b0333762d04acae7d252
class Skill49(ActiveSkill):
    """
    召唤出最强鬼泣——神官吉格， 将敌人拖入冥界。\n
    与吉格一同被召唤的魑魅魍魉会攻击周围的敌人， 并将敌人拖到中心位置的同时触发诅咒状态。\n
    吉格从亡者之手中解放时， 强制使敌人僵直， 然后开启黄泉裂缝攻击周围的敌人后， 唤出亡者之手。 被亡者之手拖入地里的吉格会触发吞食效果， 使低于一定生命值的敌人立即死亡。n\n
    [最初、 最强的灵魂大师。 吉格的主人啊！]
    """
    name = "王者号令 : 吉格降临"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "9bc30e0f6e22b0333762d04acae7d252"
    hasVP = False
    hasUP = False

    # 魑魅魍魉的攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 15
    # 吉格解放时的攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 开启冥界裂缝时的攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 终结攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 诅咒几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 诅咒时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 可使吉格触发吞食效果的怪物生命值
    # 普通 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 稀有 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 深渊 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # APC : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 无法使领主立即死亡

# 鬼神冠冕
# swordman_male/soul_bender/696721534394b40e78ac96e880f19e5a
# 41f1cdc2ff58bb5fdc287be0db2a8df3/696721534394b40e78ac96e880f19e5a
class Skill50(PassiveSkill):
    """
    掌握鬼神“黄泉之门的主人卡隆”的力量， 成为真正的鬼神之王。 利用鬼神之王的力量增加转职技能攻击力， 部分技能附加特殊效果。\n
    [噬灵鬼斩]\n
    蓄气功能消失， 攻击时在原地发动斩击。 利用冥界之力， 生成幽魂之布雷德的气息。\n
    [满月斩]\n
    制造月亮并用斩击将鬼气注入到月亮之中， 然后破坏黑月攻击敌人。 删除追加按键功能。
    """
    name = "鬼神冠冕"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "696721534394b40e78ac96e880f19e5a"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]

# 鬼神剑·黄泉摆渡
# swordman_male/soul_bender/0dbdeaf846356f8b9380f8fbb8e97377
# 41f1cdc2ff58bb5fdc287be0db2a8df3/0dbdeaf846356f8b9380f8fbb8e97377
class Skill51(ActiveSkill):
    """
    使用黄泉之门的主人的卡隆之剑， 向前方挥动。 猛烈挥动产生的剑使现实的空间产生裂缝， 出现黄泉裂缝， 在亡灵从黄泉裂缝涌出之前， 使用卡隆之剑毁灭黄泉裂缝。
    """
    name = "鬼神剑·黄泉摆渡"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [1064, 7980]
    uuid = "0dbdeaf846356f8b9380f8fbb8e97377"
    hasVP = False
    hasUP = False

    # 内部空间斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 外部空间斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 卡隆之剑投掷攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 亡灵吸收多段攻击力 : {value3}% x {value4}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 5
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 黄泉裂缝毁灭攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1

# 黄泉之门 : 万鬼度灵
# swordman_male/soul_bender/56fca6cff74d828e92301a40cd2148b9
# 41f1cdc2ff58bb5fdc287be0db2a8df3/56fca6cff74d828e92301a40cd2148b9
class Skill52(ActiveSkill):
    """
    身为九大鬼神之王， 穿戴蕴含鬼神之力的铠甲， 使用卡隆之剑召唤黄泉之门。 用卡隆之剑斩断黄泉之门的结界， 将冥界亡灵释放到现界， 攻击所有敌人。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    关联的技能在冷却中时， 无法使用三次觉醒技能。
    """
    name = "黄泉之门 : 万鬼度灵"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "56fca6cff74d828e92301a40cd2148b9"
    hasVP = False
    hasUP = False

    # 黄泉之门召唤攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 黄泉之门上升多段攻击力 : {value1}% x {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 8
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 黄泉之门封印解除攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 亡灵斩击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # 亡灵吸收多段攻击力 : {value5}% x {value6}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 15
    data6 = get_data(f'{prefix}/{uuid}', 6)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'soul_bender'
        self.nameCN = '极诣·鬼泣'
        self.role = 'swordman_male'
        self.角色 = '鬼剑士(男)'
        self.职业 = '鬼泣'
        self.jobId = '41f1cdc2ff58bb5fdc287be0db2a8df3'
        self.jobGrowId = '618326026de1a1f1cfba5dbd0b8396e7'

        self.武器选项 = ['太刀', '钝器', '巨剑', '短剑']
        self.输出类型选项 = ['魔法百分比']
        self.输出类型 = '魔法百分比'
        self.防具精通属性 = ['智力']
        self.防具类型 = '布甲'
        self.buff = 1.76

        super().__init__(equVersion, __name__)
