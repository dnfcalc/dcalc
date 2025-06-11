#41f1cdc2ff58bb5fdc287be0db2a8df3
from core.basic.skill import PassiveSkill, ActiveSkill, get_data,characterLv
from core.basic.character import Character
prefix = "swordman_male/weapon_master/cn/skillDetail"


class ActiveSkill(ActiveSkill):
    totalhit = 0
    """总hit"""
    thrustcount = 0
    """刺伤层数"""
    swordnum = 0
    """穿云刺落剑数"""

    def skillInfo(self, mode = None):
        return super().skillInfo(mode) + (self.swordnum,self.totalhit,self.thrustcount,)

# 疾影手
# swordman_male/weapon_master/dcd536f1674630f01fc9667bb202b851
# 41f1cdc2ff58bb5fdc287be0db2a8df3/dcd536f1674630f01fc9667bb202b851
class Skill0(PassiveSkill):
    """
    减少切换武器的冷却时间， 并且在切换其它系列武器时， 可以增加攻击速度和移动速度， 效果持续一定时间。
    """
    name = "疾影手"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "dcd536f1674630f01fc9667bb202b851"
    hasVP = False
    hasUP = False

    # 武器切换冷却时间减少量 : {value0}%
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    # 攻击速度和移动速度增加量 : {value1}%
    data1 = get_data(f"{prefix}/{uuid}", 1, lambda x = None: x)
    # 增益效果持续时间 : {value2}秒
    data2 = get_data(f"{prefix}/{uuid}", 2, lambda x = None: x)


# 基础精通
# swordman_male/weapon_master/5a56514f35cf0270ae8d6c65f8fefd78
# 41f1cdc2ff58bb5fdc287be0db2a8df3/5a56514f35cf0270ae8d6c65f8fefd78
class Skill1(PassiveSkill):
    """
    增加基本攻击、 前冲攻击、 跳跃攻击、 [上挑]、 [连突刺]的攻击力。\n
    在决斗场中， 增益/减益技能、 被动技能的技能攻击力增加效果对[基础精通]无影响。
    """
    name = "基础精通"
    icon = "$common/$name"
    learnLv = 1
    masterLv = characterLv
    maxLv = 200
    position = 1
    rangeLv = 1
    damage = False
    type = "passive"
    uuid = "5a56514f35cf0270ae8d6c65f8fefd78"
    icon = "$common/$uuid"
    # 基本攻击力变化率 : {value0}%
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    associate = [{"type":"*skillRation","data":[i-100 if i>0 else 0 for i in data0],"skills":["里 · 鬼剑术","空中连斩"]}]

# 空之连刃
# swordman_male/weapon_master/78bd107acd474518b606be1e4fd38239
# 41f1cdc2ff58bb5fdc287be0db2a8df3/78bd107acd474518b606be1e4fd38239
class Skill2(ActiveSkill):
    """
    在空中向敌人发出强威力的连续斩击。\n
    但需从第二斩击开始， 才能适用空之连刃技能的攻击力。\n
    转职为狂战士后， 施放[狂暴之力]时变更为独立攻击力。\n
    会根据[基础精通]增加伤害。
    """
    name = "空中连斩"
    learnLv = 5
    masterLv = 1
    maxLv = 11
    position = 10 #todo
    rangeLv = 1
    mp = [5, 7]
    uuid = "78bd107acd474518b606be1e4fd38239"

    # 两刀，实际第二刀才出伤害 为了统计hit
    # 攻击力 : {value0}%
    data0 = [0, 195, 209, 221, 234, 247, 260, 275, 286, 299, 312, 326]# noqa: E501
    hit0 = 2
    power0 = 0.5

    # 太刀
    data1 = [i - 100 if i > 100 else i for i in data0]
    hit1 = 2
    power1 = 1

    def skillInfo(self, mode = None):
        if self.char.GetWeaponType() == "太刀":
            self.hit0 = 0
        else:
            self.hit1 = 0
        return super().skillInfo(mode)

# 光剑精通
# swordman_male/weapon_master/717f1e2104fe4b796f800352fa143ecc
# 41f1cdc2ff58bb5fdc287be0db2a8df3/717f1e2104fe4b796f800352fa143ecc
class Skill3(PassiveSkill):
    """
    装备光剑系武器时， 增加攻击力和命中率。\n
    [转职为剑魂后]\n
    - 3级 : 使用[连突刺]则可以出现光剑气； 使用[里 · 鬼剑术]和光剑气攻击时， 追加感电状态\n
    - 5级 : [三段刃]增加攻击次数， 最后一击还可以浮空敌人\n
    - 7级 : 使用[拔刀斩]时， 可以追加攻击， 并有一定几率使敌人进入感电状态； 使用[幻影剑舞]可以增加斩击次数和速度， 减少斩击攻击力\n
    - 9级 : 使用[猛龙断空斩]时， 有一定几率使敌人进入感电状态\n
    [装备传世武器后]\n
    适用独立的攻击力/命中率增加数值。
    """
    name = "光剑精通"
    learnLv = 15
    masterLv = 1
    maxLv = 40
    position = 2
    rangeLv = 3
    uuid = "717f1e2104fe4b796f800352fa143ecc"

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    # 魔法攻击力增加率 : {value1}%
    data1 = get_data(f"{prefix}/{uuid}", 1, lambda x = None: x)
    # 命中率增加 : {value2}%
    data2 = get_data(f"{prefix}/{uuid}", 2, lambda x = None: x)
    # [剑魂特殊附加效果]
    # [里 · 鬼剑术]感电几率 : {value3}%
    data3 = get_data(f"{prefix}/{uuid}", 3, lambda x = None: x)
    # [连突刺]光剑气感电几率 : {value4}%
    data4 = get_data(f"{prefix}/{uuid}", 4, lambda x = None: x)
    # [里 · 鬼剑术]感电持续时间 : {value5}秒
    data5 = get_data(f"{prefix}/{uuid}", 5, lambda x = None: x)
    # [连突刺]光剑气感电持续时间 : {value6}秒
    data6 = get_data(f"{prefix}/{uuid}", 6, lambda x = None: x)
    # 感电攻击力 : {value7}%
    data7 = get_data(f"{prefix}/{uuid}", 7, lambda x = None: x)
    # [连突刺]光剑气攻击力 : {value8}%
    data8 = get_data(f"{prefix}/{uuid}", 8, lambda x = None: x)
    # [三段刃]最后一击浮空力 : {value9}
    data9 = get_data(f"{prefix}/{uuid}", 9, lambda x = None: x)
    # [猛龙断空斩]感电几率 : {value10}%
    data10 = get_data(f"{prefix}/{uuid}", 10, lambda x = None: x)
    # [猛龙断空斩]感电持续时间 : {value11}秒
    data11 = get_data(f"{prefix}/{uuid}", 11, lambda x = None: x)
    # [猛龙断空斩]感电攻击力 : {value12}%
    data12 = get_data(f"{prefix}/{uuid}", 12, lambda x = None: x)
    # [拔刀斩]追击时感电几率 : {value13}%
    data13 = get_data(f"{prefix}/{uuid}", 13, lambda x = None: x)
    # [拔刀斩]追击时感电持续时间 : {value14}秒
    data14 = get_data(f"{prefix}/{uuid}", 14, lambda x = None: x)
    # [拔刀斩]追击时感电攻击力 : {value15}%
    data15 = get_data(f"{prefix}/{uuid}", 15, lambda x = None: x)
    # [装备传世武器后]
    # 物理攻击力增加率 : {value16}%
    data16 = get_data(f"{prefix}/{uuid}", 16, lambda x = None: x)
    # 魔法攻击力增加率 : {value17}%
    data17 = get_data(f"{prefix}/{uuid}", 17, lambda x = None: x)
    # 命中率增加 : {value18}%
    data18 = get_data(f"{prefix}/{uuid}", 18, lambda x = None: x)

    def effect(self, old, new):
        weapon = self.char.GetWeaponType()
        if weapon[0] != "光剑":
            return
        data = self.data0
        if weapon[1] == "传世武器":
            data = self.data16
        self.associate = [{"type":"$*PAtkP","data":data}]
        return super().effect(old, new)

# 三段刃 단공참
# https://api.neople.co.kr/df/skills/41f1cdc2ff58bb5fdc287be0db2a8df3/f2fb27162beb0b87a7cb9af7900e95f2?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill4(ActiveSkill):
    name = "三段刃"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 6
    mp = [12, 120]
    damage = False
    uuid = "f2fb27162beb0b87a7cb9af7900e95f2"

    # [5次连续攻击的攻击力]
    # 第1击~第4击 : {value0}%
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    # 第5击 : {value1}%
    data1 = get_data(f"{prefix}/{uuid}", 1, lambda x = None: x)
    # [7次连续攻击的攻击力]
    # 第1击~第5击 : {value2}%
    data2 = get_data(f"{prefix}/{uuid}", 2, lambda x = None: x)
    # 第6击 : {value3}%
    data3 = get_data(f"{prefix}/{uuid}", 3, lambda x = None: x)
    # 第7击 : {value4}%
    # data4 = get_data(f"{prefix}/{uuid}", 4, lambda x = None: x)
    data4 = [0, 1753, 1931, 2108, 2286, 2464, 2642, 2820, 2998, 3175, 3353, 3531, 3709, 3887, 4065, 4242, 4420, 4598, 4776, 4954, 5131, 5309, 5487, 5665, 5843, 6021, 6198, 6376, 6554, 6732, 6910, 7088, 7265, 7443, 7621, 7799, 7977, 8154, 8332, 8510, 8688, 8866, 9044, 9221, 9399, 9577, 9755, 9933, 10111, 10288, 10466, 10644, 10822, 11000, 11177, 11355, 11533, 11711, 11889, 12067, 12244, 12422, 12600, 12778, 12956, 13134, 13311, 13489, 13667, 13845, 14023]# noqa: E501


# 短剑精通
# swordman_male/weapon_master/01c3a2fb793d293a25ed8dc7a0d70c1a
# 41f1cdc2ff58bb5fdc287be0db2a8df3/01c3a2fb793d293a25ed8dc7a0d70c1a
class Skill5(PassiveSkill):
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
    masterLv = 1
    maxLv = 40
    line = 10
    position = 0 #TODO
    rangeLv = 3
    uuid = "01c3a2fb793d293a25ed8dc7a0d70c1a"
    hasUP = False

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    # 魔法攻击力增加率 : {value1}%
    data1 = get_data(f"{prefix}/{uuid}", 1, lambda x = None: x)
    # 命中率增加 : {value2}%
    data2 = get_data(f"{prefix}/{uuid}", 2, lambda x = None: x)
    # [剑魂特殊附加效果]
    # [里 · 鬼剑术]剑气攻击力 : {value3}%
    data3 = get_data(f"{prefix}/{uuid}", 3, lambda x = None: x)
    # [格挡]冲击波攻击力 : {value4}%
    data4 = get_data(f"{prefix}/{uuid}", 4, lambda x = None: x)
    # [格挡]冲击波眩晕几率 : {value5}%
    data5 = get_data(f"{prefix}/{uuid}", 5, lambda x = None: x)
    # [格挡]冲击波眩晕持续时间 : {value6}秒
    data6 = get_data(f"{prefix}/{uuid}", 6, lambda x = None: x)
    # [上挑]第1击攻击力增加率 : {value7}%
    data7 = get_data(f"{prefix}/{uuid}", 7, lambda x = None: x)
    # [上挑]第2击攻击力增加率 : {value8}%
    data8 = get_data(f"{prefix}/{uuid}", 8, lambda x = None: x)
    # [上挑]浮空力 : {value9}%
    data9 = get_data(f"{prefix}/{uuid}", 9, lambda x = None: x)
    # [三段刃]攻击力增加率 : {value10}%
    data10 = get_data(f"{prefix}/{uuid}", 10, lambda x = None: x)
    # [破军升龙击]攻击力增加率 : {value11}%
    data11 = get_data(f"{prefix}/{uuid}", 11, lambda x = None: x)
    # [猛龙断空斩]攻击力增加率 : {value12}%
    data12 = get_data(f"{prefix}/{uuid}", 12, lambda x = None: x)
    # [装备传世武器后]
    # 物理攻击力增加率 : {value13}%
    data13 = get_data(f"{prefix}/{uuid}", 13, lambda x = None: x)
    # 魔法攻击力增加率 : {value14}%
    data14 = get_data(f"{prefix}/{uuid}", 14, lambda x = None: x)
    # 命中率增加 : {value15}%
    data15 = get_data(f"{prefix}/{uuid}", 15, lambda x = None: x)


    def effect(self, old, new):
        weapon = self.char.GetWeaponType()
        if weapon[0] != "短剑":
            return
        data = self.data0
        if weapon[1] == "传世武器":
            data = self.data13
        self.associate = [
            {"type":"$*PAtkP","data":data},
            {"type":"+dataplus0","data":self.data3,"skills":["里 · 鬼剑术"],"ratio":1},
            {"type":"*skillRation","data":self.data11,"skills":["破军升龙击"]},
            {"type":"*skillRation","data":self.data12,"skills":["猛龙断空斩"]},
        ]
        return super().effect(old, new)


# 太刀精通
# swordman_male/weapon_master/8f73f243041c2d27739fe7696f02bf9b
# 41f1cdc2ff58bb5fdc287be0db2a8df3/8f73f243041c2d27739fe7696f02bf9b
class Skill6(ActiveSkill):
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
    masterLv = 1
    maxLv = 40
    line = 10
    position = 1 #TODO
    rangeLv = 3
    type = "passive"
    uuid = "8f73f243041c2d27739fe7696f02bf9b"
    hasUP = False

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    # 魔法攻击力增加率 : {value1}%
    data1 = get_data(f"{prefix}/{uuid}", 1, lambda x = None: x)
    # 命中率增加 : {value2}%
    data2 = get_data(f"{prefix}/{uuid}", 2, lambda x = None: x)
    # [剑魂特殊附加效果]
    # 刺伤几率 : {value3}%
    data3 = get_data(f"{prefix}/{uuid}", 3, lambda x = None: x)
    # 刺伤持续时间 : {value4}秒
    data4 = get_data(f"{prefix}/{uuid}", 4, lambda x = None: x)
    # 刺伤爆炸攻击力 : {value5}% ~ {value6}%
    data5 = get_data(f"{prefix}/{uuid}", 5, lambda x = None: x)
    data6 = get_data(f"{prefix}/{uuid}", 6, lambda x = None: x)
    # 刺伤持续攻击力 : {value7}%
    data7 = get_data(f"{prefix}/{uuid}", 7, lambda x = None: x)
    # [空之连刃]附加攻击力 : {value8}%
    data8 = get_data(f"{prefix}/{uuid}", 8, lambda x = None: x)
    # [空之连刃]对刺伤状态的敌人的攻击力增加率 : {value9}%
    data9 = get_data(f"{prefix}/{uuid}", 9, lambda x = None: x)
    # [装备传世武器后]
    # 物理攻击力增加率 : {value10}%
    data10 = get_data(f"{prefix}/{uuid}", 10, lambda x = None: x)
    # 魔法攻击力增加率 : {value11}%
    data11 = get_data(f"{prefix}/{uuid}", 11, lambda x = None: x)
    # 命中率增加 : {value12}%
    data12 = get_data(f"{prefix}/{uuid}", 12, lambda x = None: x)

    def effect(self, old, new):
        weapon = self.char.GetWeaponType()
        if weapon[0] != "太刀":
            return
        data = self.data0
        if weapon[1] == "传世武器":
            data = self.data10
        self.associate = [
            {"type":"$*PAtkP","data":data},
            {"type":"*power1","data":[i-100 if i>100 else 0 for i in self.data9],"skills":["空中连斩"]},
        ]
        return super().effect(old, new)

    def getSkillData(self, lv = 0):
        weapon = self.char.GetWeaponType()
        if weapon[0] != "太刀":
            return 0
        # 刺伤期望伤害 (17层引爆上限) / 17 (17层结算1次爆炸) * 刺伤触发几率
        return self.data6[lv] * 1 / 17 * self.data4[lv] / 100

    def getSkillCD(self,mode=None):
        return 1.0

# 巨剑精通
# swordman_male/weapon_master/8c2379737c5acc935c1731f67f607655
# 41f1cdc2ff58bb5fdc287be0db2a8df3/8c2379737c5acc935c1731f67f607655
class Skill7(PassiveSkill):
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
    masterLv = 1
    maxLv = 40
    line = 10
    position = 0 #TODO
    rangeLv = 3
    uuid = "8c2379737c5acc935c1731f67f607655"

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    # 魔法攻击力增加率 : {value1}%
    data1 = get_data(f"{prefix}/{uuid}", 1, lambda x = None: x)
    # 命中率增加 : {value2}%
    data2 = get_data(f"{prefix}/{uuid}", 2, lambda x = None: x)
    # [剑魂特殊附加效果]
    # [格挡]冲击波攻击力 : {value3}%
    data3 = get_data(f"{prefix}/{uuid}", 3, lambda x = None: x)
    # [格挡]冲击波眩晕几率 : {value4}%
    data4 = get_data(f"{prefix}/{uuid}", 4, lambda x = None: x)
    # [格挡]冲击波眩晕持续时间 : {value5}秒
    data5 = get_data(f"{prefix}/{uuid}", 5, lambda x = None: x)
    # [银光落刃]多段攻击力 : {value6}%
    data6 = get_data(f"{prefix}/{uuid}", 6, lambda x = None: x)
    # [里 · 鬼剑术]达蓄气上限时攻击力增加率 : {value7}%
    data7 = get_data(f"{prefix}/{uuid}", 7, lambda x = None: x)
    # [拔刀斩]达蓄气上限时攻击力增加率 : {value8}%
    data8 = get_data(f"{prefix}/{uuid}", 8, lambda x = None: x)
    # [装备传世武器后]
    # 物理攻击力增加率 : {value9}%
    data9 = get_data(f"{prefix}/{uuid}", 9, lambda x = None: x)
    # 魔法攻击力增加率 : {value10}%
    data10 = get_data(f"{prefix}/{uuid}", 10, lambda x = None: x)
    # 命中率增加 : {value11}%
    data11 = get_data(f"{prefix}/{uuid}", 11, lambda x = None: x)

    def effect(self, old, new):
        weapon = self.char.GetWeaponType()
        if weapon[0] != "巨剑":
            return
        data = self.data0
        if weapon[1] == "传世武器":
            data = self.data9
        self.associate = [
            {"type":"$*PAtkP","data":data},
            {"type":"+dataplus0","data":self.data3,"skills":["里 · 鬼剑术"],"ratio":1},
            {"type":"+power12","data":[i - 100 if i > 100 else i for i in self.data8],"skills":["拔刀斩"]},
        ]
        return super().effect(old, new)

# 钝器精通
# swordman_male/weapon_master/9cb6f9ed646fa87f9b7680a42ce83d1a
# 41f1cdc2ff58bb5fdc287be0db2a8df3/9cb6f9ed646fa87f9b7680a42ce83d1a
class Skill8(PassiveSkill):
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
    masterLv = 1
    maxLv = 40
    line = 10
    position = 1 #TODO
    rangeLv = 3
    uuid = "9cb6f9ed646fa87f9b7680a42ce83d1a"

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    # 魔法攻击力增加率 : {value1}%
    data1 = get_data(f"{prefix}/{uuid}", 1, lambda x = None: x)
    # 命中率增加 : {value2}%
    data2 = get_data(f"{prefix}/{uuid}", 2, lambda x = None: x)
    # [剑魂特殊附加效果]
    # [后跳斩]浮空力 : {value3}
    data3 = get_data(f"{prefix}/{uuid}", 3, lambda x = None: x)
    # [后跳斩]冲击波攻击力 : {value4}%
    data4 = get_data(f"{prefix}/{uuid}", 4, lambda x = None: x)
    # 对眩晕状态的敌人造成的[里 · 鬼剑术]攻击力增加率 : {value5}%
    data5 = get_data(f"{prefix}/{uuid}", 5, lambda x = None: x)
    # 跳跃攻击时的浮空力 : {value6}
    data6 = get_data(f"{prefix}/{uuid}", 6, lambda x = None: x)
    # 跳跃攻击时的冲击波攻击力 : {value7}%
    data7 = get_data(f"{prefix}/{uuid}", 7, lambda x = None: x)
    # [后跳斩]攻击力增加率 : {value8}%
    data8 = get_data(f"{prefix}/{uuid}", 8, lambda x = None: x)
    # [装备传世武器后]
    # 物理攻击力增加率 : {value9}%
    data9 = get_data(f"{prefix}/{uuid}", 9, lambda x = None: x)
    # 魔法攻击力增加率 : {value10}%
    data10 = get_data(f"{prefix}/{uuid}", 10, lambda x = None: x)
    # 命中率增加 : {value11}%
    data11 = get_data(f"{prefix}/{uuid}", 11, lambda x = None: x)

    def effect(self, old, new):
        weapon = self.char.GetWeaponType()
        if weapon[0] != "钝器":
            return
        data = self.data0
        if weapon[1] == "传世武器":
            data = self.data9
        self.associate = [{"type":"$*PAtkP","data":data},]
        return super().effect(old, new)

# 武器奥义
# swordman_male/weapon_master/8ee0099656df08a0b39225f8a21d514b
# 41f1cdc2ff58bb5fdc287be0db2a8df3/8ee0099656df08a0b39225f8a21d514b
class Skill9(PassiveSkill):
    """
    领悟武器奥义， 学习后， 可增加所有武器的精通等级。\n
    1级时， 可使所有武器精通各提升2级； 以后技能每提升1级时， 武器精通提升1级。
    """
    name = "武器奥义"
    learnLv = 15
    masterLv = 20
    maxLv = 30
    position = 1
    rangeLv = 3
    uuid = "8ee0099656df08a0b39225f8a21d514b"

    associate = [{"type":"+lv","data":[i + 1 if i > 0 else i for i in range(0, maxLv + 2)],"ratio":1,"skills":["光剑精通","钝器精通","太刀精通","巨剑精通","短剑精通"]}] #TODO

# 光剑掌握
# swordman_male/weapon_master/bb34e8854a93fd250347a1c64119f7ab
# 41f1cdc2ff58bb5fdc287be0db2a8df3/bb34e8854a93fd250347a1c64119f7ab
class Skill10(PassiveSkill):
    """
    可以使用光剑系武器攻击敌人， 使用光剑系武器时， 可以增加攻击速度， 减少除[极 · 鬼剑术 (暴风式)]、 [万剑归宗]、 [万剑极诣·开天斩]以外技能的冷却时间。
    """
    name = "光剑掌握"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 9 #TODO
    rangeLv = 3
    uuid = "bb34e8854a93fd250347a1c64119f7ab"

    # 使用光剑时， 技能冷却时间减少率 : {value0}%
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    # 使用光剑时， 攻击速度增加率 : {value1}%
    data1 = get_data(f"{prefix}/{uuid}", 1, lambda x = None: x)

    associate = [
        {"type":"*cdReduce","data":data0,"exceptSkills":["极 · 鬼剑术 (暴风式)", "万剑归宗", "万剑极诣·开天斩"],"weapon":["光剑"]},
    ]

# 里 · 鬼剑术
# swordman_male/weapon_master/51a08fd0c90f0a5276cd552047fac93d
# 41f1cdc2ff58bb5fdc287be0db2a8df3/51a08fd0c90f0a5276cd552047fac93d
class Skill11(ActiveSkill):
    """
    剑魂特有的鬼剑术； 施放技能时， 使用的武器不同， 出现的攻击效果也不同。\n
    可以与基本攻击形成连击， 但无法连接[里 · 鬼剑术]的最后一击。\n
    可强制中断[里·鬼剑术]， 并施放其它的转职技能。
    """
    name = "里 · 鬼剑术"
    learnLv = 15
    masterLv = 1
    maxLv = 11
    position = 4 #TODO
    rangeLv = 15
    mp = [6, 140]
    uuid = "51a08fd0c90f0a5276cd552047fac93d"
    thrusthit = 8

    @property
    def swordnum(self):
        list = {"短剑": 3, "光剑": 3, "巨剑": 2, "钝器": 4, "太刀": 4}
        return list.get(self.char.GetWeaponType(), 3)

    data0 = [0] + [0] * 11
    ratio = [0, 0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]# noqa: E501
    dataplus0 = 0

    basic = {
        "短剑": (1 + 1 + 1) * 100,
        "光剑": (1.433 + 1.707 + 2.235)* 100,
        # 巨剑第二下蓄力5.2
        "巨剑": (3.027 + 2.301 * 5.2) * 100,
        "太刀": (1.415 + 1.688 + 1.942 + 2.225) * 2,
        # 钝器第三下眩晕率极高,眩晕了就是3倍里鬼
        "钝器": (2.301 + 2.923 + 1.801 * 3 + 4.366) * 100,
    }

    def getSkillData(self, lv = 0):
        if lv == 0:
            return 0
        weapon = self.char.GetWeaponType()
        basic = self.basic.get(weapon, 3)
        ratio = self.ratio[self.lv] / 100 + 1
        data = basic * ratio + self.dataplus0
        return data

# 流心
# swordman_male/weapon_master/c5a2956d8ed3af1746ed2f76ca971a09
# 41f1cdc2ff58bb5fdc287be0db2a8df3/c5a2956d8ed3af1746ed2f76ca971a09
class Skill12(ActiveSkill):
    """
    施放后， 进入[流心]状态。\n
    可以强制中断基本攻击、 [里 · 鬼剑术]、 [逆转反击]、  [三段刃]， 并立即施放[流心]。\n
    [流心 : 狂]只能在施放[流心]后才能使用； 可以通过ON/OFF控制[流心 : 狂]连击状态的效果。\n
    [流心]状态和[流心 : 跃]施放过程中， 无法用[强化 - 后跳]强制中断。\n
    学习[极 · 神剑术]后， 施放过程中进入霸体状态。
    """
    name = "流心"
    learnLv = 20
    masterLv = 1
    maxLv = 1
    position = 6 #TODO
    rangeLv = 2
    cd = 1
    mp = [20, 20]
    uuid = "c5a2956d8ed3af1746ed2f76ca971a09"

    damage = False
# 流心 : 刺
# swordman_male/weapon_master/2a0a39184de92acf1c1375e00b77404c
# 41f1cdc2ff58bb5fdc287be0db2a8df3/2a0a39184de92acf1c1375e00b77404c
class Skill13(ActiveSkill):
    """
    对前方敌人发动强威力的突刺。\n
    未施放[流心]技能时， 也可使用[流心 : 刺]。 使用[流心 : 刺]后， 可以立即施放[连突刺]或[三段刃]。 使用除钝器以外的武器时， 在空中按流心键可以发动空中形态。\n
    若已掌握[极 · 神剑术]则在施放过程中进入霸体状态。\n
    学习[无形剑意]后， 装备短剑、 巨剑、 钝器时附加特殊效果。\n
    [武器附加效果]\n
    太刀、 光剑 :  增加多段攻击次数\n
    钝器 : 增加攻击力； 附加眩晕效果\n
    巨剑、 短剑 : 突刺后按技能键追加下斩\n
    技能达到20级后， 装备太刀时可以增加刺伤数量
    """
    name = "流心 : 刺"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    line = 25
    position = 4 #TODO
    rangeLv = 2
    cd = 8
    mp = [30, 280]
    uuid = "2a0a39184de92acf1c1375e00b77404c"
    thrusthit = 4

    # 基本攻击力 : {value0}%
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    hit0 = 2
    # 多段攻击次数 : {value1}
    data1 = get_data(f"{prefix}/{uuid}", 1, lambda x = None: x)
    # 短剑 - 在空中施放时， 多段攻击次数增加量 : 1
    # 短剑、 巨剑 - 追加下斩攻击力 : 基本攻击力的{value2}%
    data2 = get_data(f"{prefix}/{uuid}", 2, lambda x = None: x)
    # 太刀 - 刺伤效果几率 : {value3}%
    data3 = get_data(f"{prefix}/{uuid}", 3, lambda x = None: x)
    # 太刀 - 刺伤效果数 : {value4}个
    data4 = get_data(f"{prefix}/{uuid}", 4, lambda x = None: x)
    # 太刀 - 刺伤持续时间 : {value5}秒
    data5 = get_data(f"{prefix}/{uuid}", 5, lambda x = None: x)
    # 太刀、 光剑 - 多段攻击次数 : {value6}
    data6 = get_data(f"{prefix}/{uuid}", 6, lambda x = None: x)
    # 太刀、 光剑 - 多段攻击力 : 基本攻击力的{value7}%
    data7 = get_data(f"{prefix}/{uuid}", 7, lambda x = None: x)
    # 钝器 - 攻击力增加率 : {value8}%
    data8 = get_data(f"{prefix}/{uuid}", 8, lambda x = None: x)
    # 钝器 - 眩晕几率 : {value9}%
    data9 = get_data(f"{prefix}/{uuid}", 9, lambda x = None: x)
    # 钝器 - 眩晕时间 : {value10}秒
    data10 = get_data(f"{prefix}/{uuid}", 10, lambda x = None: x)
    # [范围信息]
    # 范围比率 : {value11}%
    data11 = get_data(f"{prefix}/{uuid}", 11, lambda x = None: x)

    # 地面与空中伤害已一致
    def setMode(self,mode):
        weapon = self.char.GetWeaponType()
        if weapon[0] == "光剑" or weapon[0] == "太刀":
            self.hit0 = 4
            self.power0 *= 0.63
        elif weapon[0] == "巨剑" or weapon[0] == "短剑":
            self.hit0 = 3
        elif weapon[0] == "钝器":
            self.power0 *= 1.25

    def getWeaponCDRatio(self):
        return 1.0


# 无我剑气
# swordman_male/weapon_master/c47b66efd27845ef14954928ea2f95c8
# 41f1cdc2ff58bb5fdc287be0db2a8df3/c47b66efd27845ef14954928ea2f95c8
class Skill14(PassiveSkill):
    """
    达到无我境界， 增加基本攻击力和技能攻击力。
    """
    name = "无我剑气"
    learnLv = 20
    masterLv = 5
    maxLv = 15
    position = 9 #TODO
    rangeLv = 3
    uuid = "c47b66efd27845ef14954928ea2f95c8"

    data0 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]# noqa: E501
    associate = [{"type":"*skillRation","data":data0}]

# 破极兵刃
# swordman_male/weapon_master/762c4e6d030eaf0abbfe1fec2b298574
# 41f1cdc2ff58bb5fdc287be0db2a8df3/762c4e6d030eaf0abbfe1fec2b298574
class Skill15(ActiveSkill):
    """
    使武器突破极限， 增加物理暴击率、 基本攻击力和技能攻击力， 效果持续一定时间。
    """
    name = "破极兵刃"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 2 #TODO
    rangeLv = 3
    cd = 5
    mp = [271, 2570]
    uuid = "762c4e6d030eaf0abbfe1fec2b298574"
    # 持续时间 : {value0}秒
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    # 增加基本攻击力和技能攻击力 : {value1}%
    data1 = get_data(f"{prefix}/{uuid}", 1, lambda x = None: x)
    # 增加物理暴击率 : {value2}%
    data2 = get_data(f"{prefix}/{uuid}", 2, lambda x = None: x)
    damage = False

# 流心 : 跃
# swordman_male/weapon_master/9dc8438e4572d39243c97da31c113acc
# 41f1cdc2ff58bb5fdc287be0db2a8df3/9dc8438e4572d39243c97da31c113acc
class Skill16(ActiveSkill):
    """
    向前轻轻跳跃， 发出斩击。\n
    在施放[流心]技能状态下， 向前轻轻跳跃， 在跳跃状态下可通过追加操作向敌人发出砍击。\n
    使用方向键可以进行Y轴移动； 如果不进行追加操作， 则跳跃后会回到[流心]技能初始状态。\n
    学习[极 · 神剑术]后， 施放时进入霸体状态。\n
    学习[无形剑意]后， 使用短剑、 太刀、 光剑、 钝器时， 附加特殊效果。\n
    [各武器效果]\n
    光剑 : 附加感电效果\n
    短剑 : 施放横向砍击\n
    太刀 : 施放横向砍击， 附加刺伤效果\n
    钝器 : 生成冲击波； 在空中按流心键和攻击键， 可以在空中发动[流心 : 跃]； 在空中施放时， 增加攻击力。
    """
    name = "流心 : 跃"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 8
    mp = [30, 350]
    uuid = "9dc8438e4572d39243c97da31c113acc"

    # 基本攻击力 : {value0}%
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    hit0 = 1
    # 短剑、 太刀 - 多段攻击次数 : {value1}次
    data1 = get_data(f"{prefix}/{uuid}", 1, lambda x = None: x)
    # 短剑、 太刀 - 多段攻击力 : 基本攻击力的{value2}%
    data2 = get_data(f"{prefix}/{uuid}", 2, lambda x = None: x)
    # 太刀 - 刺伤效果几率 : {value3}%
    data3 = get_data(f"{prefix}/{uuid}", 3, lambda x = None: x)
    # 太刀 - 刺伤效果数 : {value4}个
    data4 = get_data(f"{prefix}/{uuid}", 4, lambda x = None: x)
    # 太刀 - 刺伤持续时间 : {value5}秒
    data5 = get_data(f"{prefix}/{uuid}", 5, lambda x = None: x)
    # 光剑 - 感电攻击力 : {value6}%
    data6 = get_data(f"{prefix}/{uuid}", 6, lambda x = None: x)
    # 光剑 - 感电几率 : {value7}%
    data7 = get_data(f"{prefix}/{uuid}", 7, lambda x = None: x)
    # 光剑 - 感电持续时间 : {value8}秒
    data8 = get_data(f"{prefix}/{uuid}", 8, lambda x = None: x)
    # 钝器 - 冲击波攻击力 : {value9}%
    data9 = get_data(f"{prefix}/{uuid}", 9, lambda x = None: x)
    # 钝器 - 空中发动[流心 ： 跃]时， 攻击力增加率 : {value10}%
    data10 = get_data(f"{prefix}/{uuid}", 10, lambda x = None: x)
    # 钝器 - 冲击波大小比率 : {value11}%
    data11 = get_data(f"{prefix}/{uuid}", 11, lambda x = None: x)
    # [范围信息]
    # 范围比率 : {value12}%
    data12 = get_data(f"{prefix}/{uuid}", 12, lambda x = None: x)

    mode = ["地面","空中"]

    def setMode(self,mode):
        weapon = self.char.GetWeaponType()
        if weapon[0] == "钝器" and mode == "空中":
            self.skillRation *= 1.2
        else:
            pass

    def getWeaponCDRatio(self):
        return 1.0


# 逆转反击
# swordman_male/weapon_master/c9664191611af31142e052dfaef84530
# 41f1cdc2ff58bb5fdc287be0db2a8df3/c9664191611af31142e052dfaef84530
class Skill17(ActiveSkill):
    """
    自身背后遭受攻击时， 可以进行反击； 每隔一段时间反击时不会受到伤害。
    """
    name = "逆转反击"
    learnLv = 30
    masterLv = 20
    maxLv = 30
    position = 2 #TODO
    rangeLv = 3
    cd = [0, 15, 14.7, 14.4, 14.2, 13.9, 13.6, 13.3, 13.1, 12.8, 12.5, 12.2, 12, 11.7, 11.4, 11.1, 10.9, 10.6, 10.3, 10, 9.8, 9.5, 9.2, 8.9, 8.7, 8.4, 8.1, 7.8, 7.6, 7.3, 7]
    uuid = "c9664191611af31142e052dfaef84530"

    damage = False
    # 攻击力 : {value0}%
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    # 保护冷却时间 : {value1}秒
    data1 = get_data(f"{prefix}/{uuid}", 1, lambda x = None: x)
    # [范围信息]
    # 范围比率 : {value2}%
    data2 = get_data(f"{prefix}/{uuid}", 2, lambda x = None: x)

# 破军升龙击
# swordman_male/weapon_master/28b583c75a49103a1d8aabf799c000a4
# 41f1cdc2ff58bb5fdc287be0db2a8df3/28b583c75a49103a1d8aabf799c000a4
class Skill18(ActiveSkill):
    """
    以冲撞击退敌人的同时向敌人发出单手上斩， 可以使敌人浮空。\n
    若已掌握[极 · 神剑术]则会发动阿甘左的暴风式。\n
    [武器附加效果]\n
    太刀 : 增加上斩攻击次数； 技能达到4级以上时， 附加刺伤效果\n
    光剑 : 增加冲撞攻击次数， 减少冲撞攻击力\n
    巨剑 : 上斩后可以追加攻击\n
    钝器 : 上斩后可以追加攻击， 追加攻击会生成冲击波 (被追加攻击命中的敌人， 不会受到冲击波的伤害)
    """
    name = "破军升龙击"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 10
    mp = [70, 700]
    uuid = "28b583c75a49103a1d8aabf799c000a4"

    # 肩撞攻击力 : {value0}%
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    hit0 = 2
    # 上斩攻击力 : {value1}%
    data1 = get_data(f"{prefix}/{uuid}", 1, lambda x = None: x)
    hit1 = 1
    # 太刀 - 上斩额外攻击次数 : {value2}
    data2 = get_data(f"{prefix}/{uuid}", 2, lambda x = None: x)
    # 太刀 - 附加刺伤几率 : {value3}%
    data3 = get_data(f"{prefix}/{uuid}", 3, lambda x = None: x)
    # 太刀 - 附加刺伤层数 : {value4}层
    data4 = get_data(f"{prefix}/{uuid}", 4, lambda x = None: x)
    # 太刀 - 刺伤持续时间 : {value5}秒
    data5 = get_data(f"{prefix}/{uuid}", 5, lambda x = None: x)
    # 光剑 - 肩撞额外攻击次数 : {value6}次
    data6 = get_data(f"{prefix}/{uuid}", 6, lambda x = None: x)
    # 光剑 - 肩撞攻击力减少率 : {value7}%
    data7 = get_data(f"{prefix}/{uuid}", 7, lambda x = None: x)
    # 巨剑、 钝器 - 下锤的蓄气时间上限 : {value8}秒
    data8 = get_data(f"{prefix}/{uuid}", 8, lambda x = None: x)
    # 巨剑、 钝器 - 下锤攻击力 : 上斩攻击力的{value9}%
    data9 = get_data(f"{prefix}/{uuid}", 9, lambda x = None: x)
    # 钝器 - 下锤冲击波攻击力 : 上斩攻击力的{value10}%
    data10 = get_data(f"{prefix}/{uuid}", 10, lambda x = None: x)
    # [范围信息]
    # 范围比率 : {value11}%
    data11 = get_data(f"{prefix}/{uuid}", 11, lambda x = None: x)

    # 巨剑 钝器追加部分
    data12 = data1
    hit12 = 0
    # 75被动追加部分
    data13 = data1
    hit13 = 1
    power13 = 0

    def setMode(self,mode):
        weapon = self.char.GetWeaponType()
        if weapon[0] == "光剑":
            self.hit0 += 2
            # 光剑肩撞伤害减少
            self.power0 -= 0.114
        elif weapon[0] == "太刀":
            self.hit1 += 1
        elif weapon[0] == "钝器" or weapon[0] == "巨剑":
            self.hit12 = 1


# 流心 : 升
# swordman_male/weapon_master/3fb8395ae3b81bd608e0c4223a8eb534
# 41f1cdc2ff58bb5fdc287be0db2a8df3/3fb8395ae3b81bd608e0c4223a8eb534
class Skill19(ActiveSkill):
    """
    向上跳跃的同时对敌人发出上挑攻击。\n
    若已掌握[极 · 神剑术]则在施放过程中进入霸体状态。\n
    学习[无形剑意]后， 装备太刀、 光剑、 巨剑时附加特殊效果。\n
    [武器附加效果]\n
    太刀 : 可以进行多段攻击， 但减少多段攻击力； 技能达到15级以上时， 造成额外刺伤效果\n
    光剑 : 可以进行多段攻击， 但减少多段攻击力\n
    短剑、 巨剑、 钝器 : 对浮空的敌人或者霸体状态、 没有浮空的敌人造成更高的攻击力\n
    巨剑 : 减少攻击时的跳跃力
    """
    name = "流心 : 升"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cd = 8
    mp = [50, 490]
    uuid = "3fb8395ae3b81bd608e0c4223a8eb534"

    def getWeaponCDRatio(self):
        return 1.0

    # 基本攻击力 : {value0}%
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    # 太刀 - 刺伤效果几率 : {value1}%
    data1 = get_data(f"{prefix}/{uuid}", 1, lambda x = None: x)
    # 太刀 - 刺伤效果数 : {value2}个
    data2 = get_data(f"{prefix}/{uuid}", 2, lambda x = None: x)
    # 太刀 - 刺伤持续时间 : {value3}秒
    data3 = get_data(f"{prefix}/{uuid}", 3, lambda x = None: x)
    # 光剑、 太刀 - 多段攻击次数 : {value4}次
    data4 = get_data(f"{prefix}/{uuid}", 4, lambda x = None: x)
    # 装备光剑、 太刀时， 攻击力比率 : 80%
    # 钝器、 短剑和巨剑 - 对浮空的敌人、 霸体状态的敌人、 没有浮空的敌人攻击力增加率 : {value5}%
    data5 = get_data(f"{prefix}/{uuid}", 5, lambda x = None: x)
    # [范围信息]
    # 范围比率 : {value6}%
    data6 = get_data(f"{prefix}/{uuid}", 6, lambda x = None: x)

    def setMode(self,mode):
        weapon = self.char.GetWeaponType()
        if weapon[0] == "光剑" or weapon[0] == "太刀":
            self.hit0 = 3
            self.skillRation *= 0.8
        elif weapon[0] == "钝器" or weapon[0] == "巨剑" or weapon[0] == "短剑":
            self.skillRation *= 1 + 1.1


# 流心 : 狂
# swordman_male/weapon_master/5806440d21e7546d50007a5ba11f8024
# 41f1cdc2ff58bb5fdc287be0db2a8df3/5806440d21e7546d50007a5ba11f8024
class Skill20(ActiveSkill):
    """
    施放[流心]技能后可以使用； 施放时， 增加[流心 : 刺]、 [流心 : 跃]、 [流心 : 升]的攻击力和物理暴击率。\n
    [流心 : 狂]连击状态\n
    学习[极 · 神剑术]后， 施放[流心 : 狂]后可以连接施放[流心 : 刺]、 [流心 : 跃]、 [流心 : 升]。(流心技能可以使用开启/关闭进行设置)\n
    连接施放[流心 : 刺]、 [流心 : 跃]、 [流心 : 升]时， 增加各技能的施放速度。\n
    [连接施放快捷键]\n
    [流心 : 刺] : X\n
    [流心 : 跃] : C + C 或 C + X\n
    [流心 : 升] : Z
    """
    name = "流心 : 狂"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 6 #TODO
    rangeLv = 3
    cd = 5
    mp = [20, 168]
    uuid = "5806440d21e7546d50007a5ba11f8024"
    damage = False

    # 持续时间 : {value0}秒
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    # 可蓄气时间上限 : {value1}秒
    data1 = get_data(f"{prefix}/{uuid}", 1, lambda x = None: x)
    # [流心 ： 刺/跃/升] - 攻击力增加率 : {value2}%
    data2 = get_data(f"{prefix}/{uuid}", 2, lambda x = None: x)
    # 物理暴击率增加 : {value3}%
    data3 = get_data(f"{prefix}/{uuid}", 3, lambda x = None: x)

    associate = [
        {"type":"*skillRation","data":data2,"skills":["流心 : 升","流心 : 刺","流心 : 跃"]}
    ]


    def getWeaponCDRatio(self):
        return 1.0

# 拔刀斩
# swordman_male/weapon_master/cfacda0647b9a0f595df2c2aad30c18d
# 41f1cdc2ff58bb5fdc287be0db2a8df3/cfacda0647b9a0f595df2c2aad30c18d
class Skill21(ActiveSkill):
    """
    拔刀并快速向周围敌人发出强威力的斩击。\n
    [武器附加效果]\n
    短剑 : [短剑精通]达到7级时， 生成剑气\n
    太刀、 光剑 : [太刀精通]或[光剑精通]达到7级时， 再次按技能键发动追加攻击\n
    太刀 : 技能达到5级以上时， 造成额外刺伤效果\n
    巨剑 : [巨剑精通]达到3级时， 长按技能键可以蓄气， 最大蓄气时增加攻击力\n
    钝器 : 可以使敌人倒地并对倒地敌人追加伤害
    """
    name = "拔刀斩"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [110, 924]
    uuid = "cfacda0647b9a0f595df2c2aad30c18d"
    vps = [{"name": "拔刀奥义", "desc": "施放时间减少<br/>范围增加<br/>发动[神影手]<br/>强化[神影手]速度增益"}, {"name": "冲击之刃", "desc": "取消僵直<br/>施放时间减少"}] # noqa: E501
    # [拔刀斩]攻击力 : {value0}%
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    hit0 = 1
    # 短剑 - 剑气攻击力 : 拔刀斩的{value1}%
    data1 = get_data(f"{prefix}/{uuid}", 1, lambda x = None: x)
    # 太刀 - 追加斩击攻击力 : 拔刀斩的{value2}%
    data2 = get_data(f"{prefix}/{uuid}", 2, lambda x = None: x)
    # 太刀 - 刺伤效果几率 : {value3}%
    data3 = get_data(f"{prefix}/{uuid}", 3, lambda x = None: x)
    # 太刀 - 刺伤效果数 : {value4}个
    data4 = get_data(f"{prefix}/{uuid}", 4, lambda x = None: x)
    # 太刀 - 刺伤持续时间 : {value5}秒
    data5 = get_data(f"{prefix}/{uuid}", 5, lambda x = None: x)
    # 太刀 - 追加斩击刺伤效果触发几率 : {value6}%
    data6 = get_data(f"{prefix}/{uuid}", 6, lambda x = None: x)
    # 太刀 - 追加斩击刺伤效果触发层数 : {value7}层
    data7 = get_data(f"{prefix}/{uuid}", 7, lambda x = None: x)
    # 太刀 - 追加斩击刺伤持续时间 : {value8}秒
    data8 = get_data(f"{prefix}/{uuid}", 8, lambda x = None: x)
    # 光剑 - 追加斩击攻击力 : 拔刀斩的{value9}%
    data9 = get_data(f"{prefix}/{uuid}", 9, lambda x = None: x)
    # 钝器 - 对倒地敌人和无法倒地敌人的追加攻击力 : 拔刀斩的{value10}%
    data10 = get_data(f"{prefix}/{uuid}", 10, lambda x = None: x)
    # [范围信息]
    # 范围比率 : {value11}%
    data11 = get_data(f"{prefix}/{uuid}", 11, lambda x = None: x)

    data12 = data0
    hit12 = 1
    power12 = 0

    def setMode(self,mode=None):
        weapon = self.char.GetWeaponType()
        if weapon[0] == "光剑" or weapon[0] == "钝器":
            self.power12 += 0.3
        elif weapon[0] == "太刀":
            self.power12 += 0.25
        elif weapon[0] == "短剑":
            self.power12 += 0.4

    def vp_1(self):
        """
        [拔刀斩]\n
        准备动作时间 -30%\n
        攻击范围 +45%\n
        [神影手]\n
        [拔刀斩]命中时， 获得以下效果\n
        - 发动[神影手]效果\n
        - 每次拔刀最多发动1次\n
        攻击速度和移动速度增加量 +70%
        """
        ...

    def vp_2(self):
        """
        [拔刀斩]\n
        可以强制中断转职技能的施放后僵直并施放 (觉醒技能除外)\n
        根据穿戴的武器， 发动时触发以下效果\n
        - 短剑、 钝器 : 攻击后僵直 -40%\n
        - 太刀、 光剑 : 同时发动拔刀追加攻击\n
        - 巨剑 : 立即以最大蓄气状态施放
        """
        ...

# 猛龙断空斩
# swordman_male/weapon_master/669f1428193f61f9d92c743b72438c4d
# 41f1cdc2ff58bb5fdc287be0db2a8df3/669f1428193f61f9d92c743b72438c4d
class Skill42(ActiveSkill):
    """
    向前方快速移动并斩击敌人。\n
    可以上下左右移动着斩击敌人； 起始斩击后可以通过再次按技能键追加斩击。\n
    最后一击为可以使敌人浮空的单手上斩。\n
    若已掌握[极 · 神剑术]， 则会出现巴恩的飓风\n
    若已学9级以上的[光剑精通]并使用光剑系武器， 则可以使敌人进入感电状态。
    """
    name = "猛龙断空斩"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [25, 420]
    uuid = "669f1428193f61f9d92c743b72438c4d"
    hasVP = True
    hasUP = True
    vps = [{"name": "猛龙过江", "desc": "追踪<br/>范围增加"}, {"name": "闪龙破空", "desc": "取消僵直<br/>所受伤害减少<br/>施放时间减少"}] # noqa: E501
    # 斩击次数上限 : {value0}次
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    # 突进斩击攻击力 : {value1}%
    data1 = get_data(f"{prefix}/{uuid}", 1, lambda x = None: x)
    hit1 = 2
    # 突进上斩攻击力 : {value2}%
    data2 = get_data(f"{prefix}/{uuid}", 2, lambda x = None: x)
    hit2 = 2
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f"{prefix}/{uuid}", 3, lambda x = None: x)

    data4 = data1
    hit4 = 8
    power4 = 0

    def vp_1(self):
        """
        [猛龙断空斩]\n
        突进上斩动作结束时生成旋风\n
        [极·神剑术]\n
        巴恩的飓风强化\n
        - 移动时追击周围敌人\n
        - 大小 +70%\n
        - 持续时间 +1秒\n
        - 多段攻击次数上限 +7次\n
        - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [猛龙断空斩]\n
        突进过程中可以通过[流心]强制中断技能\n
        突进过程中被击时， 招架敌人的攻击， 所受伤害 -90%\n
        攻击次数上限变更为1次\n
        - 固定施放突进上斩动作\n
        - 总攻击力相同
        """
        ...

# 破军斩龙击
# swordman_male/weapon_master/2c9d9a36c8401bddff6cdb80fab8dc24
# 41f1cdc2ff58bb5fdc287be0db2a8df3/2c9d9a36c8401bddff6cdb80fab8dc24
class Skill23(ActiveSkill):
    """
    向前进并把周围敌人推向前方， 然后转身继续前进， 把敌人聚到一处后， 上挑攻击使敌人浮空。\n
    第一击可以使敌人眩晕。\n
    使用太刀时， 可以同时叠加多个刺伤效果。
    """
    name = "破军斩龙击"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [30, 450]
    uuid = "2c9d9a36c8401bddff6cdb80fab8dc24"
    hasVP = True
    hasUP = True
    vps = [{"name": "心念合一", "desc": "变更为单次攻击<br/>攻击力和冷却时间增加<br/>范围增加"}, {"name": "剑龙噬渊", "desc": "聚集敌人<br/>取消僵直"}] # noqa: E501

    # 肩撞攻击力 : {value0}%
    data0 = get_data(f"{prefix}/{uuid}", 0, lambda x = None: x)
    hit0 = 1
    # 刺击物理攻击力 : {value1}%
    data1 = get_data(f"{prefix}/{uuid}", 1, lambda x = None: x)
    hit1 = 1
    # 上斩攻击力 : {value2}%
    data2 = get_data(f"{prefix}/{uuid}", 2, lambda x = None: x)
    hit2 = 1
    # 上斩浮空力 : {value3}
    data3 = get_data(f"{prefix}/{uuid}", 3, lambda x = None: x)
    # 眩晕几率 : {value4}%
    data4 = get_data(f"{prefix}/{uuid}", 4, lambda x = None: x)
    # 眩晕持续时间 : {value5}秒
    data5 = get_data(f"{prefix}/{uuid}", 5, lambda x = None: x)
    # 太刀 - 刺伤效果几率 : {value6}%
    data6 = get_data(f"{prefix}/{uuid}", 6, lambda x = None: x)
    # 太刀 - 刺伤效果数 : {value7}个
    data7 = get_data(f"{prefix}/{uuid}", 7, lambda x = None: x)
    # 太刀 - 刺伤持续时间 : {value8}秒
    data8 = get_data(f"{prefix}/{uuid}", 8, lambda x = None: x)
    # [范围信息]
    # 范围比率 : {value9}%
    data9 = get_data(f"{prefix}/{uuid}", 9, lambda x = None: x)

    def vp_1(self):
        """
        [破军斩龙击]\n
        变更为集中意念后上斩的技能\n
        - 删除肩撞攻击和刺击攻击\n
        - 总攻击力 +60%\n
        - 基本冷却时间变更为40秒\n
        - 上斩范围 +35%\n
        - 浮空力 +30%\n
        - 删除附加眩晕效果
        """
        self.cd = 40
        self.skillRation *= 1.6
        ...

    def vp_2(self):
        """
        [破军斩龙击]\n
        可以吸附处于霸体状态及无法抓取状态的敌人\n
        可以强制中断[破军升龙击]技能的施放后僵直并发动\n
        [破军升龙击]\n
        肩撞攻击会将敌人击退\n
        可以强制中断[破军斩龙击]技能的施放后僵直并发动\n
        [三段刃]\n
        可以在施放过程中强制中断技能， 并施放[破军升龙击]和[破军斩龙击]
        """
        ...

# 幻影剑舞
# swordman_male/weapon_master/8510294202d0e042dd29a2422fc6770d
# 41f1cdc2ff58bb5fdc287be0db2a8df3/8510294202d0e042dd29a2422fc6770d
class Skill24(ActiveSkill):
    """
    在原地向敌人发出迅猛的连续斩击， 每次斩击时发出剑气， 飞向前方后消失。\n
    斩击过程中连按技能键或攻击键时， 可以增加斩击速度。\n
    可以按上下方向键控制剑气的方向。\n
    若已掌握[极 · 神剑术]则会触发索德罗斯的幻影攻击效果。 (钝器系武器的最后一击不会发出剑气， 但会生成冲击波)\n
    [武器附加效果]\n
    短剑 : 增加剑气攻击力； [短剑精通]达到7级时， 增加剑气多段攻击次数\n
    太刀 : 造成额外刺伤效果\n
    太刀、 光剑 : [太刀精通]或[光剑精通]达到7级时， 增加斩击次数和攻击速度， 减少攻击力\n
    巨剑 : 增加斩击攻击力\n
    钝器 : [钝器精通]达到7级时， 不会发出剑气， 但会生成冲击波
    """
    name = "幻影剑舞"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [360, 3024]
    uuid = "8510294202d0e042dd29a2422fc6770d"
    hasVP = True
    hasUP = True
    vps = [{'name': '无形剑舞', 'desc': '范围增加<br/>所受伤害减少<br/>每个武器赋予异常状态'}, {'name': '残影剑舞', 'desc': '召唤无形剑<br/>施放时间减少<br/>可以在其他动作中施放<br/>适用最大连击效果'}] # noqa: E501

    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 12
    # 基础斩击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 3
    # 剑气攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 0
    # 剑气多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 短剑 - 斩击攻击力减少率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 短剑 - 剑气攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 短剑 - 剑气的多段攻击次数 : {value6}次
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # [太刀精通]、 [光剑精通]达到7级后， 斩击次数 : {value7}次
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    # [太刀精通]、 [光剑精通]达到7级后， 斩击攻击力减少率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)
    # 太刀 - 刺伤效果几率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9, lambda x = None: x)
    # 太刀 - 刺伤效果数 : {value10}个
    data10 = get_data(f'{prefix}/{uuid}', 10, lambda x = None: x)
    # 太刀 - 刺伤持续时间 : {value11}秒
    data11 = get_data(f'{prefix}/{uuid}', 11, lambda x = None: x)
    # 光剑 - 感电几率 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12, lambda x = None: x)
    # 光剑 - 感电攻击力 : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13, lambda x = None: x)
    # 巨剑 - 斩击攻击力增加率 : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14, lambda x = None: x)
    # 钝器 - 冲击波攻击力 : {value15}%
    data15 = get_data(f'{prefix}/{uuid}', 15, lambda x = None: x)
    # [范围信息]
    # 范围比率 : {value16}%
    data16 = get_data(f'{prefix}/{uuid}', 16, lambda x = None: x)
    # 75被动影子斩击部分
    data17 = data0
    power17 = 0
    hit17 = 4

    # 75被动影子剑气部分
    data18 = data1
    power18 = 0
    hit18 = 3

    # 75被动钝器冲击波部分
    data19 = data2
    power19 = 0
    hit19 = 1

    def setMode(self, mode=None):
        weapon = self.char.GetWeaponType()
        if weapon[0] == "光剑" or weapon[0] == "太刀":
            # 减少斩击攻击力 增加斩击次数
            self.hit0 = 24
            self.power0 *= 1 - 0.25
        elif weapon[0] == "短剑":
            # 减少斩击攻击力
            self.power0 *= 1 - 0.1
            # 增加剑气攻击力和次数
            self.power1 *= 1.2
            self.hit1 = self.hit4 = 4
        elif weapon[0] == "巨剑":
            # 增加斩击攻击力
            self.power0 *= 1 + 0.5
        elif weapon[0] == "钝器":
            # 不会产生剑气 变成冲击波
            self.hit2 = self.hit5 = 1
            self.hit1 = self.hit4 = 0
        pass

# 极 · 鬼剑术 (斩铁式) 극 귀검술 : 참철식
# https://api.neople.co.kr/df/skills/41f1cdc2ff58bb5fdc287be0db2a8df3/5152480fdde81362575a488d4cec4af9?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill25(PassiveSkill):
    name = "极 · 鬼剑术 (斩铁式)"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 3
    uuid = "5152480fdde81362575a488d4cec4af9"

    data0 = [0, 4.5, 6.5, 8.5, 10.5, 12.5, 14.5, 16.5, 18.5, 20.5, 22.5, 24.5, 26.5, 28.5, 30.5, 32.5, 34.5, 36.5, 38.5, 40.5, 42.5, 44.5, 46.5, 48.5, 50.5, 52.5, 54.5, 56.5, 58.5, 60.5, 62.5, 64.5, 66.5, 68.5, 70.5, 72.5, 74.5, 76.5, 78.5, 80.5, 82.5, 84.5, 86.5, 88.5, 90.5, 92.5, 94.5, 96.5, 98.5, 100.5, 102.5]# noqa: E501

    associate = [{"type":"*skillRation","data":data0}]


# 极 · 鬼剑术 (暴风式) 극 귀검술 : 폭풍식
# https://api.neople.co.kr/df/skills/41f1cdc2ff58bb5fdc287be0db2a8df3/4f2e001e9a19eb7bae50ad1840dfb329?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill26(ActiveSkill):
    name = "极 · 鬼剑术 (暴风式)"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [980, 8232]
    uuid = "4f2e001e9a19eb7bae50ad1840dfb329"

    data0 = [0, 6010, 7401, 8795, 10189, 11584, 12977, 14372, 15766, 17160, 18552, 19949, 21341, 22735, 24130, 25526, 26920, 28310, 29704, 31099, 32491, 33884, 35278, 36674, 38070, 39461, 40855, 42252, 43643, 45037, 46433, 47826, 49222, 50612, 52004, 53398, 54795, 56187, 57578, 58975, 60366, 61763, 63157, 64552, 65946, 67338, 68732, 70127, 71521, 72913, 74306]# noqa: E501
    data0 = [int(i * 1.1 )if index > 9 else i for index, i in enumerate(data0)]
    hit0 = 1 #TODO

    data1 = [0, 2860, 3526, 4186, 4853, 5512, 6182, 6842, 7505, 8172, 8834, 9497, 10163, 10825, 11491, 12156, 12817, 13479, 14145, 14809, 15472, 16135, 16802, 17461, 18128, 18788, 19456, 20115, 20781, 21445, 22111, 22774, 23436, 24101, 24764, 25425, 26093, 26754, 27419, 28081, 28746, 29409, 30074, 30739, 31401, 32065, 32727, 33392, 34056, 34720, 35382]# noqa: E501
    data0 = [int(i * 1.1 )if index > 9 else i for index, i in enumerate(data1)]
    hit1 = 24

    data2 = [0, 11159, 13750, 16340, 18929, 21512, 24104, 26694, 29281, 31867, 34457, 37048, 39636, 42222, 44811, 47403, 49989, 52579, 55167, 57756, 60344, 62930, 65522, 68111, 70698, 73284, 75874, 78466, 81052, 83642, 86228, 88819, 91406, 93997, 96585, 99174, 101761, 104347, 106939, 109523, 112115, 114702, 117290, 119878, 122469, 125055, 127646, 130234, 132823, 135414, 137998]# noqa: E501
    data0 = [int(i * 1.1 )if index > 9 else i for index, i in enumerate(data2)]
    hit2 = 1 #TODO


# 极 · 神剑术 (流星落) 극 귀검술 : 유성락
# https://api.neople.co.kr/df/skills/41f1cdc2ff58bb5fdc287be0db2a8df3/0c262dac3ec41ff79e359ada9c7a7faf?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill27(ActiveSkill):
    name = "极 · 神剑术 (流星落)"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 2
    cube = 1
    cd = 35
    mp = [420, 1200]
    uuid = "0c262dac3ec41ff79e359ada9c7a7faf"
    vps = [
          {
            "name": "流星审判",
            "desc": "无敌强化<br/>强制控制功能强化<br/>范围增加",
            "explain": "[极·神剑术 (流星落)]<br/>无敌效果强化<br/>- 跳跃动作变更为无敌状态<br/>- 落地后无敌时间 + 1秒<br/><br/>跳跃冲击波攻击可以强制控制敌人1.5秒<br/><br/>流星剑功能强化<br/>- 投掷流星剑前置准备时间 -50%<br/>- 攻击范围 55%<br/><br/>[极·神剑术]<br/>流星之天剑功能强化<br/>- 强制控制持续时间 + 60%<br/>- 攻击范围 55%"
          },
          {
            "name": "天道瞬斩",
            "desc": "变更为投掷剑的技能<br/>追踪",
            "explain": "[极·神剑术 (流星落)]<br/>施放时向空中投掷流星剑和流星之天剑<br/>- 流星剑和流星之天剑会追踪最强的敌人<br/>- 删除跳跃冲击波及地面冲撞攻击<br/>- 总攻击力相同"
          }
        ]
    data0 = [0, 6540, 7209, 7869, 8537, 9197, 9866, 10524, 11190, 11855, 12516, 13182, 13848, 14508, 15174, 15840, 16500, 17165, 17834, 18492, 19157, 19821, 20487, 21149, 21815, 22473, 23141, 23805, 24468, 25128, 25794, 26462, 27122, 27789, 28452, 29109, 29778, 30441, 31110, 31770, 32436, 33095, 33764, 34430, 35088, 35756, 36417, 37077, 37743, 38414, 39074]# noqa: E501
    hit0 = 1 #TODO

    data1 = [0, 1200, 1325, 1449, 1571, 1691, 1817, 1938, 2060, 2184, 2304, 2432, 2547, 2676, 2798, 2918, 3041, 3162, 3282, 3401, 3530, 3650, 3767, 3899, 4020, 4139, 4263, 4383, 4506, 4628, 4752, 4872, 4998, 5118, 5240, 5361, 5483, 5604, 5729, 5855, 5975, 6099, 6219, 6339, 6464, 6584, 6702, 6831, 6950, 7074, 7199]# noqa: E501
    hit1 = 38

    data2 = [0, 13086, 14417, 15741, 17067, 18401, 19725, 21053, 22385, 23709, 25034, 26370, 27690, 29016, 30351, 31679, 33003, 34335, 35661, 36986, 38321, 39641, 40968, 42299, 43626, 44952, 46286, 47610, 48932, 50262, 51593, 52916, 54251, 55577, 56900, 58232, 59561, 60882, 62219, 63543, 64874, 66198, 67524, 68853, 70181, 71513, 72837, 74168, 75494, 76821, 78149]# noqa: E501
    hit2 = 1 #TODO

    # 75被动追加天剑部分
    dataplus0 = 0
    hitplus0 = 3
    powerplus0 = 1
    # 75被动追加冲击波部分
    dataplus1 = 0
    hitplus1 = 3
    powerplus1 = 1

    data5 = [0, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59, 62, 65, 68, 71, 74, 77, 80, 83, 86, 89, 92, 95, 98, 101, 104, 107, 110, 113, 116, 119, 122, 125, 128, 131, 134, 137, 140, 143, 146, 149, 152, 155, 158, 161, 164, 167, 170, 173, 176]# noqa: E501

    data6 = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]# noqa: E501


# 破空拔刀斩 극초발도
# https://api.neople.co.kr/df/skills/41f1cdc2ff58bb5fdc287be0db2a8df3/2ba299855fc22192cba4f73db75e9d0e?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill28(ActiveSkill):
    name = "破空拔刀斩"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [800, 1680]
    uuid = "2ba299855fc22192cba4f73db75e9d0e"
    vps = [
          {
            "name": "破空一刀",
            "desc": "剑气攻击力补正<br/>施放时间减少",
            "explain": "[破空拔刀斩]<br/>剑气攻击力变更为与斩击攻击力相同<br/><br/>增加斩击速度<br/>- 准备动作时间 -40%<br/>- 剑气生成后僵直 -20%"
          },
          {
            "name": "流动之刃",
            "desc": "范围增加<br/>可多次发动",
            "explain": "[破空拔刀斩]<br/>剑气移动距离 + 500%<br/><br/>变更为可填充2次的技能<br/>- 每次填充冷却时间 : 25秒<br/>- 单次攻击力 -50%"
          }
        ]
    data0 = [0, 72104, 79419, 86734, 94049, 101364, 108678, 115993, 123308, 130623, 137938, 145253, 152568, 159883, 167198, 174513, 181827, 189142, 196457, 203772, 211087, 218402, 225717, 233032, 240347, 247662, 254976, 262291, 269606, 276921, 284236, 291551, 298866, 306181, 313496, 320811, 328125, 335440, 342755, 350070, 357385, 364700, 372015, 379330, 386645, 393960, 401274, 408589, 415904, 423219, 430534]# noqa: E501
    hit0 = 1 #TODO

    data1 = [0, 64894, 71477, 78060, 84644, 91227, 97811, 104394, 110977, 117561, 124144, 130728, 137311, 143895, 150478, 157061, 163645, 170228, 176812, 183395, 189978, 196562, 203145, 209729, 216312, 222895, 229479, 236062, 242646, 249229, 255812, 262396, 268979, 275563, 282146, 288729, 295313, 301896, 308480, 315063, 321647, 328230, 334813, 341397, 347980, 354564, 361147, 367730, 374314, 380897, 387481]# noqa: E501
    hit1 = 0

    mode = ["斩击","剑气"]

    def setMode(self,mode=None):
        if mode == "剑气":
            self.hit0 = 0
            self.hit1 = 1

    def vp_1(self):
        self.setMode("斩击")

    def vp_2(self):
        self.cd = 25
        self.skillRation *= 0.5

    data2 = [0, 31, 35, 39, 43, 47, 51, 55, 59, 63, 67, 71, 75, 79, 83, 87, 91, 95, 99, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]# noqa: E501

    data3 = [0, 3, 3, 3, 5, 5, 5, 7, 7, 7, 9, 9, 9, 11, 11, 11, 13, 13, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]# noqa: E501

# 神影手 신기의 손놀림
# https://api.neople.co.kr/df/skills/41f1cdc2ff58bb5fdc287be0db2a8df3/0fc47245af1f21c3e9217d03aa9fff0a?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill29(PassiveSkill):
    name = "神影手"
    learnLv = 70
    masterLv = 1
    maxLv = 1
    position = 9
    rangeLv = 1
    uuid = "0fc47245af1f21c3e9217d03aa9fff0a"

    data1 = [0, 4080]# noqa: E501
    hit1 = 1 #TODO



# 极 · 神剑术 (破空斩) 극 귀검술 : 심검
# https://api.neople.co.kr/df/skills/41f1cdc2ff58bb5fdc287be0db2a8df3/b501ae53638d33a32351904f31cb6aa3?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill30(ActiveSkill):
    name = "极 · 神剑术 (破空斩)"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 3
    cd = 35
    mp = [580, 4500]
    uuid = "b501ae53638d33a32351904f31cb6aa3"
    vps = [
          {
            "name": "一合残像",
            "desc": "范围增加<br/>无敌强化",
            "explain": "[极 · 神剑术 (破空斩)]<br/>斩击范围增加<br/>斩击时， 生成2个使用[极·神剑术 (破空斩)]的残影<br/>- X轴攻击范围 + 50%<br/><br/>施放时， 立即无敌"
          },
          {
            "name": "破灭神剑",
            "desc": "施放时间减少<br/>攻击失败补正<br/>斩击攻击并入爆炸<br/>部分技能攻击中自动生效",
            "explain": "[极 · 神剑术 (破空斩)]<br/>施放前僵直 -40%<br/><br/>没有斩击目标时， 冷却时间减少至4秒<br/><br/>对被斩击的敌人附加在一定时间后爆炸的剑痕<br/>- 删除多段攻击<br/>- 总攻击力相同<br/><br/>[神影手]<br/>冲击波攻击强化<br/>- 范围 + 35%<br/>- 冲击波发动时， 同时适用[极·神剑术（破空斩）]攻击 ([极·神剑术（破空斩）]可施放时适用)"
          }
        ]
    data0 = [0, 7692, 8472, 9253, 10033, 10813, 11594, 12374, 13154, 13935, 14715, 15495, 16276, 17056, 17837, 18617, 19397, 20178, 20958, 21738, 22519, 23299, 24079, 24860, 25640, 26420, 27201, 27981, 28761, 29542, 30322, 31102, 31883, 32663, 33443, 34224, 35004, 35785, 36565, 37345, 38126, 38906, 39686, 40467, 41247, 42027, 42808, 43588, 44368, 45149, 45929]# noqa: E501
    hit0 = 5

    data1 = [0, 25640, 28241, 30842, 33443, 36045, 38646, 41247, 43848, 46449, 49050, 51652, 54253, 56854, 59455, 62056, 64657, 67259, 69860, 72461, 75062, 77663, 80264, 82866, 85467, 88068, 90669, 93270, 95871, 98472, 101074, 103675, 106276, 108877, 111478, 114079, 116681, 119282, 121883, 124484, 127085, 129686, 132288, 134889, 137490, 140091, 142692, 145293, 147894, 150496, 153097]# noqa: E501
    hit1 = 1

    def setMode(self,mode=None):
        weapon = self.char.GetWeaponType()
        if weapon[0] == "光剑" or weapon[0] == "太刀":
            # 减少斩击攻击力 增加斩击次数
            self.hit0 = 6
        elif weapon[0] == "巨剑":
            # 增加斩击攻击力
            self.power0 *= 1 + 0.08
            self.power1 *= 1 + 0.08

    data4 = [0, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 145, 147, 149, 151]# noqa: E501

    data5 = [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]# noqa: E501



# 极 · 神剑术 극한의 경지
# https://api.neople.co.kr/df/skills/41f1cdc2ff58bb5fdc287be0db2a8df3/3af805da8505fe6234a95b535610f064?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill31(PassiveSkill):
    name = "极 · 神剑术"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 3
    uuid = "3af805da8505fe6234a95b535610f064"

    data0 = [0, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122]# noqa: E501
    # 后跳斩
    data1 = [0, 737, 854, 972, 1089, 1206, 1324, 1441, 1559, 1676, 1794, 1911, 2028, 2146, 2263, 2381, 2498, 2616, 2733, 2851, 2968, 3085, 3203, 3320, 3438, 3555, 3673, 3790, 3907, 4025, 4142, 4260, 4377, 4495, 4612, 4729, 4847, 4964, 5082, 5199, 5317, 5434, 5552, 5669, 5786, 5904, 6021, 6139, 6256, 6374, 6491]# noqa: E501
    # 破军升龙击 暴风式冲击波 
    data2 = [0, 40, 44, 48, 52, 56, 60, 64, 68, 72, 76, 80, 84, 88, 92, 96, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144, 148, 152, 156, 160, 164, 168, 172, 176, 180, 184, 188, 192, 196, 200, 204, 208, 212, 216, 220, 224, 228, 232, 236]# noqa: E501
    #猛龙断空斩 飓风
    data3 = [0, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99, 101, 103, 105, 107, 109, 111, 113, 115, 117, 119]# noqa: E501
    # 幻影剑舞 幻影斩击
    data4 = [0, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300]# noqa: E501
    # 幻影剑舞 幻影剑气
    data5 = [0, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200, 205, 210, 215, 220, 225, 230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300]# noqa: E501
    # 幻影剑舞 幻影钝器冲击波
    data6 = [0, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96, 101, 106, 111, 116, 121, 126, 131, 136, 141, 146, 151, 156, 161, 166, 171, 176, 181, 186, 191, 196, 201, 206, 211, 216, 221, 226, 231, 236, 241, 246, 251, 256, 261, 266, 271, 276, 281, 286]# noqa: E501
    # 流星落 流星之天剑
    data7 = [0, 4698, 5447, 6196, 6945, 7694, 8443, 9192, 9941, 10690, 11439, 12188, 12937, 13685, 14434, 15183, 15932, 16681, 17430, 18179, 18928, 19677, 20426, 21175, 21924, 22673, 23422, 24171, 24920, 25669, 26418, 27167, 27916, 28665, 29414, 30163, 30911, 31660, 32409, 33158, 33907, 34656, 35405, 36154, 36903, 37652, 38401, 39150, 39899, 40648, 41397]# noqa: E501
    # 流星落 太刀刺伤
    data12 = [0, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]# noqa: E501
    # 流星落 可附加的刺伤数量
    data13 = [0, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 11, 11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]# noqa: E501
    # 流星落 光剑 地面冲击波 
    data15 = [0, 1885, 2185, 2486, 2786, 3087, 3387, 3688, 3988, 4289, 4589, 4890, 5190, 5491, 5791, 6092, 6392, 6693, 6993, 7294, 7594, 7894, 8195, 8495, 8796, 9096, 9397, 9697, 9998, 10298, 10599, 10899, 11200, 11500, 11801, 12101, 12402, 12702, 13003, 13303, 13604, 13904, 14205, 14505, 14806, 15106, 15406, 15707, 16007, 16308, 16608]# noqa: E501
    # 巨剑 攻击力增加
    data19 = [0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]# noqa: E501
    # 钝器 地面冲击波
    data20 = [0, 1944, 2253, 2563, 2873, 3183, 3493, 3803, 4112, 4422, 4732, 5042, 5352, 5662, 5972, 6281, 6591, 6901, 7211, 7521, 7831, 8140, 8450, 8760, 9070, 9380, 9690, 9999, 10309, 10619, 10929, 11239, 11549, 11859, 12168, 12478, 12788, 13098, 13408, 13718, 14027, 14337, 14647, 14957, 15267, 15577, 15887, 16196, 16506, 16816, 17126]# noqa: E501
    # 破空斩 爆炸攻击力
    data23 = [0, 60, 66, 72, 78, 84, 90, 96, 102, 108, 114, 120, 126, 132, 138, 144, 150, 156, 162, 168, 174, 180, 186, 192, 198, 204, 210, 216, 222, 228, 234, 240, 246, 252, 258, 264, 270, 276, 282, 288, 294, 300, 306, 312, 318, 324, 330, 336, 342, 348, 354]# noqa: E501
    associate = [
        {"type":"*skillRation","data":data0,"skills":["拔刀斩", "破军斩龙击", "极 · 鬼剑术 (暴风式)", "破空拔刀斩","极 · 神剑术 (瞬斩)", "万剑归宗", "极 · 神剑术 (无形斩)", "万剑极诣·开天斩"]},
        {"type":"+power13","data":data2,"skills":["破军升龙击"]},
        {"type":"+power4","data":data3,"skills":["猛龙断空斩"]},
        {"type":"+power17","data":data4,"skills":["幻影剑舞"]},
        {"type":"+power18","data":data5,"skills":["幻影剑舞"]},
        {"type":"+power19","data":data6,"skills":["幻影剑舞"],"weapon":["钝器"]},
        {"type":"+dataplus0","data":data7,"skills":["极 · 神剑术 (流星落)"],"ratio":1},
        {"type":"+dataplus1","data":data15,"skills":["极 · 神剑术 (流星落)"],"weapon":["光剑"],"ratio":1},
        {"type":"*powerplus0","data":data19,"skills":["极 · 神剑术 (流星落)"],"weapon":["巨剑"]},
        {"type":"+dataplus1","data":data20,"skills":["极 · 神剑术 (流星落)"],"weapon":["钝器"],"ratio":1},
        {"type":"*power1","data":data23,"skills":["极 · 神剑术 (破空斩)"]}
        ]



# 极 · 神剑术 (瞬斩) 극 발검술 : 섬단
# https://api.neople.co.kr/df/skills/41f1cdc2ff58bb5fdc287be0db2a8df3/d8ff976e2aaa4720272a5175d1eb9126?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill32(ActiveSkill):
    name = "极 · 神剑术 (瞬斩)"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 2
    cube = 5
    cd = 50
    mp = [800, 6000]
    uuid = "d8ff976e2aaa4720272a5175d1eb9126"
    vps = [
          {
            "name": "最后一斩",
            "desc": "施放时间减少<br/>取消僵直",
            "explain": "[极 · 神剑术 (瞬斩)]<br/>拔剑斩击准备时间 -40%<br/><br/>拔剑斩击命中时， 可强制中断施放后僵直并使用转职技能<br/>中断施放后僵直时， 角色会转换方向并使用技能"
          },
          {
            "name": "一刃闪",
            "desc": "可以在空中施放<br/>范围增加<br/>攻击时间减少<br/>变更为单次攻击",
            "explain": "[极 · 神剑术 (瞬斩)]<br/>可以在175px以下的空中施放<br/><br/>拔剑斩击范围增加<br/>- 前进距离 +60%<br/>- Y轴攻击范围 +60%<br/><br/>删除拔剑斩击攻击及剑气多段攻击<br/>- 总攻击力相同"
          }
        ]
    data0 = [0, 20101, 22139, 24178, 26217, 28256, 30295, 32338, 34374, 36416, 38454, 40492, 42531, 44571, 46610, 48648, 50687, 52726, 54765, 56806, 58846, 60883, 62923, 64962, 67002, 69041, 71083, 73117, 75162, 77195, 79238, 81277, 83316, 85355, 87395, 89432, 91471, 93514, 95549, 97592, 99630, 101671, 103705, 105748, 107786, 109823, 111864, 113903, 115940, 117980, 120023]# noqa: E501
    hit0 = 1 #TODO

    data1 = [0, 3289, 3623, 3951, 4288, 4622, 4957, 5289, 5624, 5957, 6289, 6625, 6959, 7293, 7625, 7961, 8294, 8626, 8961, 9295, 9628, 9962, 10297, 10628, 10964, 11299, 11629, 11964, 12299, 12633, 12966, 13300, 13631, 13965, 14298, 14633, 14968, 15300, 15637, 15968, 16302, 16636, 16968, 17305, 17639, 17969, 18305, 18640, 18968, 19304, 19641]# noqa: E501
    hit1 = 5

    data3 = [0, 54818, 60381, 65941, 71503, 77065, 82628, 88188, 93750, 99310, 104872, 110435, 115995, 121555, 127117, 132680, 138241, 143802, 149362, 154925, 160491, 166050, 171612, 177173, 182734, 188297, 193853, 199418, 204979, 210542, 216103, 221666, 227227, 232788, 238350, 243912, 249471, 255033, 260592, 266156, 271719, 277280, 282839, 288404, 293961, 299524, 305087, 310648, 316207, 321772, 327331]# noqa: E501
    hit3 = 1 #TODO



# 万剑归宗 이기어검술
# https://api.neople.co.kr/df/skills/41f1cdc2ff58bb5fdc287be0db2a8df3/0f638da961acf7958ac6070b7aaed013?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill33(ActiveSkill):
    name = "万剑归宗"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "0f638da961acf7958ac6070b7aaed013"

    data1 = [0, 1568, 1931, 2296, 2661, 3022, 3382, 3752, 4111, 4476, 4842, 5202, 5565, 5929, 6293, 6657, 7020, 7383, 7746, 8110, 8474, 8837, 9201, 9566, 9928, 10294, 10655, 11016, 11381, 11744, 12110, 12474, 12836, 13202, 13565, 13926, 14291, 14657, 15018, 15379, 15743, 16111, 16471, 16833, 17201, 17561, 17925, 18292, 18653, 19016, 19380]# noqa: E501
    hit1 = 1 #TODO

    data2 = [0, 7264, 8956, 10643, 12324, 14013, 15701, 17381, 19073, 20753, 22435, 24131, 25812, 27494, 29176, 30870, 32555, 34235, 35920, 37616, 39296, 40977, 42665, 44348, 46038, 47726, 49410, 51091, 52786, 54469, 56148, 57831, 59528, 61207, 62891, 64578, 66261, 67953, 69634, 71327, 73006, 74693, 76382, 78066, 79745, 81430, 83122, 84806, 86487, 88172, 89868]# noqa: E501
    hit2 = 14

    data3 = [0, 29033, 35769, 42507, 49243, 55964, 62701, 69436, 76177, 82902, 89642, 96376, 103113, 109837, 116571, 123309, 130044, 136776, 143511, 150246, 156971, 163706, 170443, 177179, 183914, 190642, 197378, 204110, 210838, 217578, 224311, 231045, 237780, 244512, 251245, 257980, 264709, 271444, 278183, 284917, 291651, 298377, 305114, 311849, 318580, 325315, 332048, 338785, 345511, 352248, 358982]# noqa: E501
    hit3 = 2

    mode = ["终结","穿云剑"]

    def setMode(self,mode=None):
        if mode == "终结":
            self.hit1 = 0
        if mode == "穿云剑":
            self.hit2 = self.hit3 = 0


# 无形剑意 무형지경
# https://api.neople.co.kr/df/skills/41f1cdc2ff58bb5fdc287be0db2a8df3/7ec521d063d2190e1fcc5bd229af9bcf?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill34(PassiveSkill):
    name = "无形剑意"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "7ec521d063d2190e1fcc5bd229af9bcf"

    data0 = [0, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118]# noqa: E501

    # 对流系技能存在技能形态变动，但是实际加成和其他技能一致，这里简单化处理
    associate = [{"type":"*skillRation","data":data0}]

# 极 · 神剑术 (无形斩) 극 발검술 : 무형참
# https://api.neople.co.kr/df/skills/41f1cdc2ff58bb5fdc287be0db2a8df3/0113c8b1306ca76d208f83f2d093dd62?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill35(ActiveSkill):
    name = "极 · 神剑术 (无形斩)"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [960, 7200]
    uuid = "0113c8b1306ca76d208f83f2d093dd62"

    data0 = [0, 30185, 33250, 36312, 39374, 42438, 45500, 48561, 51625, 54687, 57750, 60812, 63875, 66936, 70000, 73063, 76124, 79187, 82251, 85311, 88374, 91437, 94500, 97561, 100626, 103688, 106749, 109812, 112876, 115937, 119001, 122062, 125124, 128188, 131251, 134311, 137375, 140438, 143500, 146563, 149626, 152687, 155750, 158813, 161876, 164937, 168001, 171062, 174126, 177188, 180250]# noqa: E501
    hit0 = 1 #TODO

    data1 = [0, 4312, 4749, 5186, 5623, 6061, 6500, 6937, 7374, 7811, 8250, 8687, 9126, 9561, 10000, 10437, 10874, 11310, 11748, 12186, 12624, 13061, 13499, 13937, 14374, 14812, 15249, 15688, 16124, 16562, 16999, 17437, 17875, 18313, 18749, 19187, 19625, 20064, 20498, 20936, 21374, 21813, 22250, 22687, 23125, 23562, 23999, 24437, 24875, 25312, 25749]# noqa: E501
    hit1 = 13

    data3 = [0, 57500, 63332, 69166, 74999, 80833, 86665, 92498, 98332, 104165, 109999, 115833, 121667, 127499, 133334, 139168, 145000, 150833, 156666, 162500, 168332, 174166, 180000, 185834, 191665, 197499, 203333, 209165, 214999, 220832, 226668, 232503, 238334, 244168, 250001, 255834, 261667, 267502, 273336, 279168, 285001, 290835, 296668, 302501, 308335, 314169, 320001, 325835, 331668, 337501, 343334]# noqa: E501
    hit3 = 1 #TODO


# 万剑极诣·开天斩 천제극섬
# https://api.neople.co.kr/df/skills/41f1cdc2ff58bb5fdc287be0db2a8df3/8b08f9504167a9c0f3a1d29d71b7943e?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill36(ActiveSkill):
    name = "万剑极诣·开天斩"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "8b08f9504167a9c0f3a1d29d71b7943e"

    data0 = [0, 68275, 84108, 99940, 115772, 131603, 147435, 163267, 179099, 194930, 210763, 226594, 242427, 258257, 274089, 289923, 305755, 321587, 337420, 353251, 369081, 384914, 400746, 416579, 432409, 448243, 464075, 479905, 495737, 511570, 527401, 543233, 559066, 574899, 590726, 606560, 622390, 638223, 654056, 669888, 685719, 701552, 717384, 733215, 749049, 764879, 780711, 796542, 812376, 828208, 844038]# noqa: E501
    hit0 = 1 #TODO

    data1 = [0, 89283, 109985, 130689, 151394, 172097, 192799, 213502, 234207, 254909, 275612, 296315, 317019, 337723, 358427, 379129, 399832, 420538, 441242, 461945, 482645, 503350, 524055, 544757, 565461, 586164, 606865, 627569, 648274, 668975, 689680, 710382, 731087, 751789, 772490, 793197, 813899, 834602, 855308, 876009, 896709, 917416, 938120, 958821, 979526, 1000230, 1020932, 1041636, 1062340, 1083042, 1103746]# noqa: E501
    hit1 = 1 #TODO

    data2 = [0, 12253, 15095, 17937, 20777, 23621, 26461, 29304, 32145, 34989, 37830, 40669, 43512, 46354, 49196, 52037, 54879, 57720, 60562, 63404, 66243, 69085, 71929, 74772, 77610, 80454, 83295, 86136, 88976, 91821, 94659, 97501, 100342, 103183, 106026, 108869, 111712, 114553, 117395, 120235, 123075, 125918, 128760, 131602, 134444, 137285, 140127, 142969, 145809, 148651, 151493]# noqa: E501
    hit2 = 6

    data4 = [0, 16805, 20704, 24598, 28497, 32394, 36291, 40189, 44085, 47983, 51880, 55775, 59674, 63570, 67466, 71365, 75262, 79160, 83057, 86954, 90850, 94746, 98644, 102540, 106439, 110336, 114234, 118131, 122030, 125923, 129822, 133719, 137613, 141514, 145409, 149303, 153204, 157100, 160996, 164896, 168792, 172689, 176586, 180484, 184379, 188278, 192174, 196071, 199968, 203866, 207763]# noqa: E501
    hit4 = 5

    data6 = [0, 210078, 258790, 307505, 356218, 404933, 453646, 502360, 551075, 599788, 648503, 697216, 745931, 794644, 843358, 892070, 940786, 989499, 1038213, 1086924, 1135639, 1184353, 1233067, 1281781, 1330496, 1379208, 1427923, 1476636, 1525351, 1574064, 1622778, 1671490, 1720205, 1768920, 1817632, 1866348, 1915061, 1963772, 2012490, 2061203, 2109915, 2158630, 2207344, 2256058, 2304772, 2353484, 2402197, 2450911, 2499625, 2548339, 2597053]# noqa: E501
    hit6 = 1 #TODO

class classChange(Character):
    def __init__(self, equVersion):

        self.name = "weapon_master"
        self.nameCN = "极诣·剑魂"
        self.role = "swordman_male"

        self.武器选项 = ["光剑","太刀", "钝器", "巨剑", "短剑"]
        self.输出类型选项 = ["物理百分比"]
        self.输出类型 = "物理百分比"
        self.防具精通属性 = ["力量"]
        self.防具类型 = "轻甲"
        self.buff = 1.86

        self.角色 = "鬼剑士(男)"

        self.职业 = "剑魂"

        super().__init__(equVersion, __name__)

    def AddSkillLv(self, min: int, max: int, lv: int, type=-1, exceptSkills:list[str]=[]) -> None:
        """
        增加技能等级
        type: -1 全部, 0 被动, 1 主动
        """
        for skill in self.skills:
            # 四个武器精通不享受技能范围等级加成
            if min <= skill.learnLv <= max and skill.name not in  ["太刀精通", "巨剑精通", "短剑精通", "钝器精通", "光剑精通"] + exceptSkills:
                skillType = "all" if type == -1 else ("active" if type == 1 else "passive")
                if (skillType == "all" or skill.type == skillType) and skill.lv > 0:
                    skill.lv += lv