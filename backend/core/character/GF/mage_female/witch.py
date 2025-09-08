#3909d0b188e9c95311399f776e331da5
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "mage_female/witch/cn/skillDetail"

# 魔法星弹
# mage_female/witch/45442bbbe33540b4deeec29437dae70c
# 3909d0b188e9c95311399f776e331da5/45442bbbe33540b4deeec29437dae70c
class Skill0(ActiveSkill):
    """
        向前方敌人发射魔法星弹， 可以用方向键调整魔法星弹的飞行方向。
    """
    name = "魔法星弹"
    learnLv = 1
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 0.5
    mp = [8, 91]
    uuid = "45442bbbe33540b4deeec29437dae70c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 飞行距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 基本穿刺力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 攻击范围扩大率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)


# 基础精通
# mage_female/witch/5a56514f35cf0270ae8d6c65f8fefd78
# 3909d0b188e9c95311399f776e331da5/5a56514f35cf0270ae8d6c65f8fefd78
class Skill3(PassiveSkill):
    """
        增加基本攻击、 前冲攻击、 跳跃攻击、 [天击]的攻击力。\n
        在决斗场中， 增益/减益技能、 被动技能的技能攻击力增加效果对[基础精通]无影响。
    """
    name = "基础精通"
    learnLv = 1
    masterLv = 115
    maxLv = 200
    position = 1 #TODO
    rangeLv = 1
    uuid = "5a56514f35cf0270ae8d6c65f8fefd78"
    icon = "$common/$uuid"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力变化率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 前冲攻击力变化率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 跳跃攻击力变化率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)


# 魔法护盾
# mage_female/witch/dcd536f1674630f01fc9667bb202b851
# 3909d0b188e9c95311399f776e331da5/dcd536f1674630f01fc9667bb202b851
class Skill10(ActiveSkill):
    """
        施放魔法护盾， 增加自身物理/魔法防御力。\n
        魔法护盾激活时按技能键可解除魔法护盾。\n
        转职为战斗法师后， 可学习[魔法护盾强化]， 加强能力。
    """
    name = "魔法护盾"
    learnLv = 5
    masterLv = 10
    maxLv = 20
    position = 9 #TODO
    rangeLv = 3
    cd = 5
    mp = [10, 14]
    uuid = "dcd536f1674630f01fc9667bb202b851"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 物理防御力增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法防御力增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 替身草人
# mage_female/witch/0969cd4054d93da07708108c0cc1c4b5
# 3909d0b188e9c95311399f776e331da5/0969cd4054d93da07708108c0cc1c4b5
class Skill12(ActiveSkill):
    """
        在受到敌人攻击或倒地时可以瞬移避开敌人的追击。\n
        瞬移时， 可以按方向键移动到相应方向； 若不按方向键， 则默认向后瞬移。\n
        瞬移后有0.5秒无敌时间， 但自身会出现一定时间的僵直。\n
        角色可以靠近原地留下的稻草人吃掉， 吃掉后增加移动速度、 攻击速度。\n
        在自身被抓取、 冰冻、 眩晕、 石化、 睡眠和束缚状态下， 无法使用此技能。\n
        转职为战斗法师后， 可以学习[替身草人]， 改变启动方式。\n
        在普通决斗场根据转职而产生不同的冷却时间。
    """
    name = "替身草人"
    learnLv = 10
    masterLv = 10
    maxLv = 20
    position = 8 #TODO
    rangeLv = 3
    cds = [0, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
    mp = [20, 70]
    uuid = "0969cd4054d93da07708108c0cc1c4b5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 瞬移后僵直时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 角色增益效果持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 增加角色移动速度 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 增加角色攻击速度 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 召唤兽增益效果持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 增加召唤兽移动速度 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 增加召唤兽攻击速度 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 增加召唤兽力量 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 增加召唤兽智力 : {value8}
    data8 = get_data(f'{prefix}/{uuid}', 8)

    def getSkillCD(self, mode=None):
        self.cd = self.cds[self.lv]
        return super().getSkillCD(mode)

# 冰霜雪人
# mage_female/witch/4224f9b0b8c7c903e9a1e0f9d9f6d04d
# 3909d0b188e9c95311399f776e331da5/4224f9b0b8c7c903e9a1e0f9d9f6d04d
class Skill13(ActiveSkill):
    """
        向前方发射一个冰属性的冰霜雪人， 对触碰到的敌人造成伤害。\n
        发射的冰霜雪人会在地上扑腾扑腾地弹跳移动， 每次弹跳时都会向着最近的敌人改变前进方向。\n
        发射时可按上或下方向键调整发射高度。\n
        长按技能键蓄气后发动时， 增加冰霜雪人大小和持续时间。\n
        蓄气达最大值时， 追加冰霜爆炸， 对被击中的敌人造成减速状态。 有一定概率使敌人进入冰冻状态。\n
        在决斗场中， 蓄气时间越长， 攻击力越高。
    """
    name = "冰霜雪人"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 9 #TODO
    rangeLv = 2
    cd = 1
    mp = [20, 210]
    uuid = "4224f9b0b8c7c903e9a1e0f9d9f6d04d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 最大蓄气时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 持续时间 : {value2} ~ {value3}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 诱导力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [最大蓄气时]
    # 减速持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 攻击速度减少率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 移动速度减少率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 冰冻几率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 冰冻持续时间 : {value9}秒
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [范围信息]
    # 冰霜雪人大小 : {value10} ~ {value11}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    data11 = get_data(f'{prefix}/{uuid}', 11)

# 暗影夜猫
# mage_female/witch/d085127b0edd719782bd618d5688f4a1
# 3909d0b188e9c95311399f776e331da5/d085127b0edd719782bd618d5688f4a1
class Skill14(ActiveSkill):
    """
        向敌人发射暗属性的暗影夜猫， 使其前扑一段距离后再返回并给予敌人最多2次伤害。\n
        发射暗影夜猫后进行Y轴移动时， 暗影夜猫会跟随。\n
        长按技能键蓄气后发动时， 增加暗影夜猫体积和射程。\n
        在决斗场中， 蓄气时间越长， 攻击力越高。
    """
    name = "暗影夜猫"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cd = 1.2
    mp = [20, 210]
    uuid = "d085127b0edd719782bd618d5688f4a1"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 最大蓄气时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 射程 : {value2} ~ {value3}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 暗影夜猫大小 : {value4} ~ {value5}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    data5 = get_data(f'{prefix}/{uuid}', 5)


# 驱散魔法
# mage_female/witch/9bff7f2559e003766fee2853dca00631
# 3909d0b188e9c95311399f776e331da5/9bff7f2559e003766fee2853dca00631
class Skill19(ActiveSkill):
    """
        驱散范围内敌人的增益效果， 减少敌人的施放速度， 并使其进入减速状态。\n
        驱散敌人的增益效果时， 提升自身的力量和智力， 每驱散1个， 可以额外提升。
    """
    name = "驱散魔法"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 1 #TODO
    rangeLv = 3
    cds = [0, 20, 19.5, 19.1, 18.6, 18.1, 17.6, 17.2, 16.7, 16.2, 15.7, 15.3, 14.8, 14.3, 13.8, 13.4, 12.9, 12.4, 11.9, 11.5, 11]
    mp = [30, 126]
    uuid = "9bff7f2559e003766fee2853dca00631"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 减益效果数量上限 : {value0}个
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 增加力量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 增加智力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 增加力量、 智力的持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 减速几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 敌人攻击速度减少率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 敌人移动速度减少 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 敌人施放速度减少 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 减少敌人攻击速度、 移动速度、 施放速度的持续时间 : {value8}秒
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [范围信息]
    # 减益效果范围 : {value9}px
    data9 = get_data(f'{prefix}/{uuid}', 9)

    def getSkillCD(self, mode=None):
        self.cd = self.cds[self.lv]
        return super().getSkillCD(mode)

# 远古魔法书
# mage_female/witch/01384bbfc346775d1267fa0bc4ca605f
# 3909d0b188e9c95311399f776e331da5/01384bbfc346775d1267fa0bc4ca605f
class Skill20(ActiveSkill):
    """
        借用远古知识增加魔道学者的基本攻击力和技能攻击力。
    """
    name = "远古魔法书"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 8 #TODO
    rangeLv = 3
    cd = 5
    uuid = "01384bbfc346775d1267fa0bc4ca605f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 空中施放 : 杰克爆弹
# mage_female/witch/dc1ffbe7bfcc6dc2be737951960da9ad
# 3909d0b188e9c95311399f776e331da5/dc1ffbe7bfcc6dc2be737951960da9ad
class Skill21(PassiveSkill):
    """
        可在空中使用[杰克爆弹]。\n
        在跳跃时向敌人发出[杰克爆弹]攻击， 爆弹会以斜向下轨迹飞行且施放者会因后坐力略微向后上浮。\n
        空中使用时无法进行蓄气。
    """
    name = "空中施放 : 杰克爆弹"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 5 #TODO
    rangeLv = 1
    uuid = "dc1ffbe7bfcc6dc2be737951960da9ad"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 挑衅人偶 : 舒露露
# mage_female/witch/4b2c90ec226fd40e967875aa5eabefb2
# 3909d0b188e9c95311399f776e331da5/4b2c90ec226fd40e967875aa5eabefb2
class Skill22(ActiveSkill):
    """
        向前方抛出[挑衅人偶 : 舒露露]。\n
        舒露露会吸引周围的敌人攻击自己。\n
        舒露露经过一定时间或受一定伤害后会自动消失。\n
        舒露露无法吸引领主怪物、 精英怪物及深渊怪物。\n
        在决斗场， 学习[亲和法米利尔]后， 减少冷却时间。
    """
    name = "挑衅人偶 : 舒露露"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 9 #TODO
    rangeLv = 2
    cd = 16
    mp = [18, 196]
    uuid = "4b2c90ec226fd40e967875aa5eabefb2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 舒露露持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [范围信息]
    # 吸附敌人的范围 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [改良舒露露]大成功时爆炸范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 亲和法米利尔
# mage_female/witch/4f2e001e9a19eb7bae50ad1840dfb329
# 3909d0b188e9c95311399f776e331da5/4f2e001e9a19eb7bae50ad1840dfb329
class Skill23(PassiveSkill):
    """
        变得与法米利尔 (暗影夜猫、 冰霜雪人、 光电鳗、 杰克爆弹)非常亲近， 增加法米利尔系列技能的属性能力值和基本攻击力。
    """
    name = "亲和法米利尔"
    learnLv = 15
    masterLv = 5
    maxLv = 15
    position = 4 #TODO
    rangeLv = 3
    uuid = "4f2e001e9a19eb7bae50ad1840dfb329"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 法米利尔技能失败率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 法米利尔技能成功率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 法米利尔技能大成功率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [暗影斗篷]命中率增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [反重力装置]施放时间减少 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [魔法星弹]扩大率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [冰霜钻孔车]施放时间减少 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [暴炎加热炉]施放时间减少 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [电鳗碰撞机]施放时间减少 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [改良魔法星弹]探索范围增加率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)

    associate = [{"data":data0}]

# 扫把掌握
# mage_female/witch/5152480fdde81362575a488d4cec4af9
# 3909d0b188e9c95311399f776e331da5/5152480fdde81362575a488d4cec4af9
class Skill24(PassiveSkill):
    """
        学习后， 可以装备扫把。\n
        装备扫把时， 增加施放速度和命中率， 装备扫把武器的状态下， 可以在空中进行各种动作。\n
        在空中施放部分技能时， 可以增加空中冲刺可使用次数。\n
        空中起飞 : (冲刺中)C\n
        空中攻击及连击 : (空中)X\n
        空中冲刺 : (空中)→→\n
        空中缓慢降落 : (空中)持续按住C\n
        在已学习的技能窗口中， 可以右键点击设置开启/关闭， 关闭状态下， 空中起飞、 空中攻击、 空中冲刺及空中缓慢降落功能均不适用。\n
    [可增加空中冲刺使用次数的技能]\n
    [改良魔法星弹]、 [挑衅人偶 : 舒露露]、 [魔道酸雨云]、 [熔岩药瓶]
    """
    name = "扫把掌握"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "5152480fdde81362575a488d4cec4af9"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 空中连击次数上限 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 装备扫把武器时， 施放速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 装备扫把武器时， 命中率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 改良舒露露
# mage_female/witch/5892d1fa4462e561ac8f8d2c74892b0a
# 3909d0b188e9c95311399f776e331da5/5892d1fa4462e561ac8f8d2c74892b0a
class Skill25(PassiveSkill):
    """
        [杰克爆弹系列技能]\n
        召唤改良后的舒露露， 舒露露出现后会向前移动， 舒露露消失时会引起爆炸， 造成火属性伤害。 若再次按技能键， 则舒露露直接爆炸。\n
        失败时， 减少爆炸范围和伤害； 大成功时， 增加爆炸范围和伤害。\n
        舒露露吸引的怪物种类随技能等级的不同而不同。\n
        可以在空中施放该技能， 但在决斗场中无法在空中施放。
    """
    name = "改良舒露露"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 9 #TODO
    rangeLv = 2
    uuid = "5892d1fa4462e561ac8f8d2c74892b0a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 失败时攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 成功时攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 大成功、 超大成功时攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 失败率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 成功率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 大成功率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    powerSuccess = 1.0
    powerFail = 1.0

    mode = ['失败', '成功', '大成功']

    def setMode(self, mode):
        if mode == '失败':
            self.hit0 = 1
            self.hit1 = self.hit2 = 0
            self.skillRation *= self.powerFail
        elif mode == '成功':
            self.hit1 = 1
            self.hit0 = self.hit2 = 0
            self.skillRation *= self.powerSuccess
        elif mode == '大成功':
            self.hit2 = 1
            self.hit0 = self.hit1 = 0
            self.skillRation *= self.powerSuccess

# 改良魔法星弹
# mage_female/witch/7cf17936a039b418660424125dc968d7
# 3909d0b188e9c95311399f776e331da5/7cf17936a039b418660424125dc968d7
class Skill26(ActiveSkill):
    """
        [光电鳗系列技能]\n
        发射一个光属性的改良魔法星弹来攻击敌人， 对范围内敌人造成一次光属性伤害。 有一定几率出现失败、 成功、 大成功， 并依此适用不同攻击力和效果。\n
        大成功时， 发射成功攻击力的魔法星弹， 并有感电效果， 攻击所有敌人后对命中敌人造成1次追加的连锁光属性魔法伤害。\n
        [改良魔法星弹]不适用棒棒糖的成功、 大成功几率增加效果。\n
        可以在空中施放该技能。(决斗场不适用)
    """
    name = "改良魔法星弹"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 5.4
    mp = [35, 350]
    uuid = "7cf17936a039b418660424125dc968d7"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 失败时攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 成功时攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 大成功时攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 感电几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 感电时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 感电攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # 失败率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 成功率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 大成功率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [范围信息]
    # 攻击后移动距离 : {value9}px
    data9 = get_data(f'{prefix}/{uuid}', 9)

    powerSuccess = 1.0
    powerFail = 1.0

    def setMode(self, mode):
        self.skillRation *= self.powerSuccess


# 魔法秀
# mage_female/witch/9dda3f4a849dba1a288dd65e116860f2
# 3909d0b188e9c95311399f776e331da5/9dda3f4a849dba1a288dd65e116860f2
class Skill27(ActiveSkill):
    """
        向周围敌人狂乱发射魔法， 效果持续一定时间。\n
        施放魔法时， 可以增加施放速度并减少技能冷却时间和蓄气时间上限。\n
        觉醒技能、 无施放时间的技能、 物理技能、 增益技能不适用冷却时间减少效果。
    """
    name = "魔法秀"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    cd = 40
    mp = [60, 360]
    uuid = "9dda3f4a849dba1a288dd65e116860f2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 冷却时间减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 施放速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 蓄气时间上限减少率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    associate = [{"type":"*cdRatio","data":data1,"skills":['改良魔法星弹', '改良舒露露', '熔岩药瓶', '魔道酸雨云', '旋转扫把', '电鳗碰撞机', '暴炎加热炉', '冰霜钻孔车', '反重力装置', '光电兔', '雪人刨冰', '糖果大作战 : 捣蛋杰克']}]

# 魔幻粉末
# mage_female/witch/7e904ea3d2a9faa054604e55120a9268
# 3909d0b188e9c95311399f776e331da5/7e904ea3d2a9faa054604e55120a9268
class Skill28(ActiveSkill):
    """
        施放时， 按方向键可以给扫把洒上魔法药粉， 基本攻击、 前冲攻击、 跳跃攻击、 [天击]、 [龙牙]的攻击力适用独立攻击力， 并增加攻击范围。\n
    寒冰魔法药粉 (←) : 攻击时附加冰冻效果。\n
    猛毒魔法药粉 (→) : 攻击时附加中毒效果。\n
        在决斗场中， 增加洒上魔法药粉后攻击的攻击力， 寒冰魔法药粉无冰冻效果。
    """
    name = "魔幻粉末"
    learnLv = 20
    masterLv = 1
    maxLv = 11
    position = 7 #TODO
    rangeLv = 3
    cd = 5
    mp = [35, 259]
    uuid = "7e904ea3d2a9faa054604e55120a9268"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 敌人僵直时间增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 冰冻几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 冰冻持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 中毒几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 中毒持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 中毒攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)

# 暗影斗篷
# mage_female/witch/2391a27457b5a8c6fa4b4670a91bdd11
# 3909d0b188e9c95311399f776e331da5/2391a27457b5a8c6fa4b4670a91bdd11
class Skill29(ActiveSkill):
    """
        [暗影夜猫系列技能]\n
        把前方敌人用暗影斗篷缠绕并缩紧， 这时会给予该敌人暗属性伤害的同时使其进入失明状态。\n
        可以抓取霸体和防御状态的敌人， 但对无法抓取的敌人不适用抓取和控制效果。
    """
    name = "暗影斗篷"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 1 #TODO
    rangeLv = 2
    cd = 7
    mp = [35, 350]
    uuid = "2391a27457b5a8c6fa4b4670a91bdd11"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 失明几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 失明持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 减少视野 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 减少命中率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 攻击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 变异苍蝇拍
# mage_female/witch/1812a1ece67bb37b6b44b54766450064
# 3909d0b188e9c95311399f776e331da5/1812a1ece67bb37b6b44b54766450064
class Skill31(ActiveSkill):
    """
        [暗影夜猫系列]\n
        使用超级苍蝇拍强力拍打前方的敌人， 给予敌人暗属性伤害并有一定几率使其进入诅咒状态。\n
        给失明状态的敌人增加攻击力。\n
        利用苍蝇拍的变异型魔力性质， 攻击时用敌人身体的一部分作为媒介， 有一定几率召唤出变异怪物。\n
        失败时， 召唤敌军怪物； 成功时， 可召唤友军怪物； 大成功时， 可召唤出强大的友军怪物。 
    """
    name = "变异苍蝇拍"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 1 #TODO
    rangeLv = 2
    cd = 6.4
    mp = [30, 105]
    uuid = "1812a1ece67bb37b6b44b54766450064"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 诅咒几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 诅咒持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 召唤几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 存在时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 失败率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 成功率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 大成功率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 对失明状态敌人的攻击力增加率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [范围信息]
    # 苍蝇拍大小比率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)

# 幸运棒棒糖
# mage_female/witch/2ba299855fc22192cba4f73db75e9d0e
# 3909d0b188e9c95311399f776e331da5/2ba299855fc22192cba4f73db75e9d0e
class Skill32(PassiveSkill):
    """
        发动有成功/失败/大成功几率的技能时， 凭借[幸运棒棒糖]的力量， 增加技能的成功率和大成功率。\n
        同时， 增加基本攻击力和转职技能攻击力。\n
        在决斗场中， 不会增加基本攻击和技能攻击力。\n
        [吃点甜甜， 烦恼尽散哦]
    """
    name = "幸运棒棒糖"
    learnLv = 25
    masterLv = 5
    maxLv = 15
    position = 0 #TODO
    rangeLv = 5
    uuid = "2ba299855fc22192cba4f73db75e9d0e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 成功率增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 大成功率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 基本攻击力、 技能攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [{"data":data2}]

# 魔道酸雨云
# mage_female/witch/b89c9ab317bc0a443f6497b7cca2f6a8
# 3909d0b188e9c95311399f776e331da5/b89c9ab317bc0a443f6497b7cca2f6a8
class Skill33(ActiveSkill):
    """
        [冰霜雪人系列]\n
        在空中生成会降落酸雨的乌云， 酸雨会给予敌人冰属性伤害， 效果持续一定时间。\n
        在空中也可以施放技能， 失败时和大成功时， 会出现不同的效果。\n
        失败时， 生成较弱伤害的乌云。\n
        大成功时， 额外造成光属性的闪电攻击。\n
        决斗场中不适用[魔法秀]的冷却时间减少效果， 而且无法在空中施放该技能。 
    """
    name = "魔道酸雨云"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 3
    cd = 20
    mp = [200, 1960]
    uuid = "b89c9ab317bc0a443f6497b7cca2f6a8"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 大成功时闪电攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 大成功时多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 超大成功时多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 失败时酸雨攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 成功时酸雨攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 大成功、 超大成功时酸雨攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 酸雨多段攻击次数 : {value7}次
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 失败率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 成功率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 大成功率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # [范围信息]
    # 乌云大小比率 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)

    powerSuccess = 1.0
    powerFail = 1.0

    mode = ['失败','成功','大成功']

    def setMode(self, mode):
        if mode == '失败':
            self.hit4 = 36
            self.hit1 = self.hit5 = self.hit6 = 0
            self.skillRation *= self.powerFail
            ...
        elif mode == '成功':
            self.hit5 = 36
            self.hit1 = self.hit4 = self.hit6 = 0
            self.skillRation *= self.powerSuccess
            ...
        elif mode == '大成功':
            # 测试为6 描述为5
            self.hit1 = 6
            self.hit6 = 36
            self.hit4 = self.hit5 = 0
            self.skillRation *= self.powerSuccess
            ...

# 熔岩药瓶
# mage_female/witch/7f80b887a09e88e2c4728c898bd73654
# 3909d0b188e9c95311399f776e331da5/7f80b887a09e88e2c4728c898bd73654
class Skill34(ActiveSkill):
    """
        [杰克爆弹系列]\n
        在前方生成熔岩地带给予敌人火属性伤害， 降低敌人跳跃力， 并使敌人进入减速状态， 效果持续一定时间。\n
        失败时， 发生较弱伤害的火属性爆炸， 但不生成熔岩地带\n
        大成功时， 生成较大范围的熔岩地带， 并有一定几率使敌人进入灼伤状态。\n
        在空中也可以施放技能。\n
        [魔法秀]的冷却时间减少效果、 空中施放技能功能不适用于决斗场。
    """
    name = "熔岩药瓶"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 3
    cd = 20
    mp = [200, 1960]
    uuid = "7f80b887a09e88e2c4728c898bd73654"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 熔岩地带攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 超大成功时火球攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 超大成功时火球多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 失败时爆炸攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 灼伤几率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 灼伤持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 灼伤攻击力 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 减速几率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 移动速度减少率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 减速持续时间 : {value10}秒
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 减速发生间隔 : {value11}秒
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 减速跳跃力减少率 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 熔岩地带多段攻击次数 : {value13}次
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # 失败率 : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # 成功率 : {value15}%
    data15 = get_data(f'{prefix}/{uuid}', 15)
    # 大成功率 : {value16}%
    data16 = get_data(f'{prefix}/{uuid}', 16)
    # [范围信息]
    # 大成功时熔岩地带大小 : {value17}px
    data17 = get_data(f'{prefix}/{uuid}', 17)
    # 成功时熔岩地带大小比率 : {value18}%
    data18 = get_data(f'{prefix}/{uuid}', 18)
    # 失败时爆炸大小比率 : {value19}%
    data19 = get_data(f'{prefix}/{uuid}', 19)

    mode = ['失败','成功','大成功']

    powerSuccess = 1.0
    powerFail = 1.0

    def setMode(self, mode):
        if mode == '失败':
            self.hit4 = 1
            self.hit1 = self.hit2 = 0
            self.skillRation *= self.powerFail
            ...
        elif mode == '大成功':
            self.hit1 = 6
            self.hit2 = 11
            self.hit4 = 0
            self.skillRation *= self.powerSuccess
            ...

# 苍蝇拍 : 魔法禁锢
# mage_female/witch/b42cab9c815150aee1ef44daec1fe4c5
# 3909d0b188e9c95311399f776e331da5/b42cab9c815150aee1ef44daec1fe4c5
class Skill35(PassiveSkill):
    """
        使用[变异苍蝇拍]和[超级苍蝇拍]击中敌人后， 不会召唤出怪物。\n
        可以在已学习的技能窗口上用鼠标右键设置开启/关闭。 开启状态下， 不会发动召唤效果。
    """
    name = "苍蝇拍 : 魔法禁锢"
    learnLv = 30
    masterLv = 1
    maxLv = 1
    position = 1 #TODO
    rangeLv = 1
    uuid = "b42cab9c815150aee1ef44daec1fe4c5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 苦涩棒棒糖
# mage_female/witch/d53301bb328baf12a3ae482cc6a565dd
# 3909d0b188e9c95311399f776e331da5/d53301bb328baf12a3ae482cc6a565dd
class Skill36(PassiveSkill):
    """
        吃起来非常苦的棒棒糖。 可以将[幸运棒棒糖]转换成[苦涩棒棒糖]。\n
        长按技能键， 可以发动特定技能的失败效果， 并且增加失败技能的攻击力。\n
    - [可发动失败效果的技能] -\n
    [熔岩药瓶]、 [暴炎加热炉]、 [冰霜钻孔车]\n
        [失败有时候也有意外效果？ 如果利用这一点的话……！？ 啊呀~好苦！]
    """
    name = "苦涩棒棒糖"
    learnLv = 35
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 3
    uuid = "d53301bb328baf12a3ae482cc6a565dd"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 发动失败蓄气时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [熔岩药瓶]失败攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [暴炎加热炉]失败攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [冰霜钻孔车]失败攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    associate = [
        {"data":data1,"type":"+powerFail","skills":["熔岩药瓶"]},
        {"data":data2,"type":"+powerFail","skills":["暴炎加热炉"]},
        {"data":data3,"type":"+powerFail","skills":["冰霜钻孔车"]},
    ]

# 旋转扫把
# mage_female/witch/2c9d9a36c8401bddff6cdb80fab8dc24
# 3909d0b188e9c95311399f776e331da5/2c9d9a36c8401bddff6cdb80fab8dc24
class Skill37(ActiveSkill):
    """
        [光电鳗系列]\n
        旋转扫把， 对周围敌人造成光属性多段伤害。 最后由于晕眩而跌倒， 产生冲击波。\n
        被击中的敌人有一定几率进入感电异常状态。\n
        旋转时按跳跃键可以强制中断。\n
        倒地前输入部分技能的技能键时， 倒地后可立即发动。\n
        [反重力装置]只能在掌握[魔道学助手]后才能施放。\n
        在空中施放时， 在骑着扫把的状态下旋转扫把， 对敌人造成光属性多段伤害。\n
        落地时产生冲击波， 自身有一定几率进入混乱状态。 混乱状态下， 会恢复生命值和魔法值。\n
        立即发动技能 : [魔道机械系列技能]、 [魔道酸雨云]、 [熔岩药瓶]、 [改良舒露露]、 [反重力装置]、 [改良魔法星弹]、 [杰克爆弹]\n
        决斗场中只有在空中才能施放， 倒地时无法施放其他技能。
    """
    name = "旋转扫把"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 12
    mp = [100, 840]
    uuid = "2c9d9a36c8401bddff6cdb80fab8dc24"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 地上旋转多段攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 地上旋转多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 地上旋转最后一击攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 空中旋转攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 空中旋转多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 空中和地上冲击波攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 混乱状态下生命值恢复 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 混乱状态下魔法值恢复 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 混乱几率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 感电几率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 感电持续时间 : {value10}秒
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 感电攻击力 : {value11}
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # [范围信息]
    # 攻击范围比率 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)

    mode = ["地面","空中"]

    def setMode(self, mode):
        if mode == "地面":
            self.hit0 = 8
            self.hit2 = 1
            self.hit3 = self.hit5 = 0
        elif mode == "空中":
            self.hit3 = 2
            self.hit5 = 1
            self.hit0 = self.hit2 = 0

    def vp_1(self):
        """
        [旋转扫把]\n
        向前方扔出巨型扫把\n
        - 无法在空中施放\n
        - 删除地上最后一击、 地上冲击波攻击\n
        - 总攻击力相同
        """
        self.setMode("地面")
        ...

    def vp_2(self):
        """
        [旋转扫把]\n
        抓住冰霜雪人的手旋转移动\n
        - 增加冰属性攻击\n
        - 使命中的敌人进入冰冻状态3秒\n
        - X、 Y轴移动速度增加\n
        - 施放技能过程中所受伤害 -70%\n
        空中施放时增加转向功能\n
        未学习[魔道学助手]技能或技能关闭时， 无法发动效果
        """
        ...

# 电鳗碰撞机
# mage_female/witch/c5a2956d8ed3af1746ed2f76ca971a09
# 3909d0b188e9c95311399f776e331da5/c5a2956d8ed3af1746ed2f76ca971a09
class Skill38(ActiveSkill):
    """
        [魔道机械/光电鳗系列技能]\n
        在地面上设置电鳗碰撞机产生强烈的电流， 电流会给予一定范围内的敌人光属性伤害的同时使敌人进入强制控制状态。 连续按<X>键会使发电速度增加。\n
        即使发电速度变快， 过程时间、 攻击次数也不会发生变化。\n
        若电鳗碰撞机受到一定伤害， 则会损坏。 若魔法师搭乘在电鳗碰撞机上， 则所受伤害减少。\n
        失败时， 无法发电并只出现一股电流； 大成功时， 增加攻击力和发电次数， 同时还会使敌人进入感电状态。\n
        学习[引爆试验]技能时， 输入跳跃键可以中断技能。
    """
    name = "电鳗碰撞机"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [360, 3024]
    uuid = "c5a2956d8ed3af1746ed2f76ca971a09"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 生命值 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 失败时攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 失败时多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 成功时攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 成功时多段攻击次数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 大成功时攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 大成功时多段攻击次数 : {value7}次
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 超大成功时攻击力 : {value8}
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 超大成功时多段攻击次数 : {value9}次
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 最终爆炸攻击力 : {value10}
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 大成功时感电几率 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 大成功时感电时间 : {value12}秒
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 大成功时感电攻击力 : {value13}
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # 失败率 : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # 成功率 : {value15}%
    data15 = get_data(f'{prefix}/{uuid}', 15)
    # 大成功率 : {value16}%
    data16 = get_data(f'{prefix}/{uuid}', 16)
    # 所受伤害减少率 : {value17}%
    data17 = get_data(f'{prefix}/{uuid}', 17)
    # [范围信息]
    # 魔法阵大小比率 : {value18}%
    data18 = get_data(f'{prefix}/{uuid}', 18)

    mode = ["设置型","乘骑型"]

    powerSuccess = 1.0
    powerFail = 1.0

    def setMode(self, mode):
        if mode == "设置型":
            self.hit6 = self.hit13 = 14
            self.hit10 = 1
            self.skillRation *= self.powerSuccess
        elif mode == "乘骑型":
            self.hit6 = self.hit13 = 22
            self.hit10 = 1
            self.skillRation *= self.powerSuccess

    def vp_1(self):
        """
        [电鳗碰撞机]\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 12.5秒\n
        - 单次攻击力 -50%\n
        每次攻击时使敌人向电鳗碰撞机方向移动\n
        攻击范围 +60%
        """
        self.cd = 12.5
        self.skillRation *= 1 - 0.5
        ...

    def vp_2(self):
        """
        [电鳗碰撞机]\n
        变更为大型游乐设施， 以光电鳗的奔跑作为动力引擎运作\n
        - 电线附在范围敌人身上后， 使其浮空并旋转\n
        - 如果光电鳗已经通过其他技能登场， 则由其他何蒙库鲁兹在动力引擎奔跑\n
        - 如果所有何蒙库鲁兹都已经登场， 则由魔道学者亲自在动力引擎奔跑\n
        施放技能时进入无敌状态\n
        学习后， 固定以超大成功形态发动\n
        未学习[魔道学助手]技能或技能关闭时， 无法发动效果\n
        - 适用[魔道学助手]开启时的攻击力\n
        基本冷却时间变更为50秒\n
        - 总攻击力 +100%
        """
        self.cd = 50
        self.skillRation *= 1 + 1
        self.setMode("设置型")  # 变更为设置型技能
        ...

# 反重力装置
# mage_female/witch/e0daa922b19cdc35de879e938361464e
# 3909d0b188e9c95311399f776e331da5/e0daa922b19cdc35de879e938361464e
class Skill39(ActiveSkill):
    """
        [魔道机械/暗影夜猫系列技能]\n
        在地面上设置一个反向重力的魔道机械， 使反重力范围的敌人浮空并给予暗属性伤害。\n
        失败时， 敌人不会浮空并给予较小的伤害； 大成功时， 增加攻击力， 并且敌人落地时还会生成冲击波攻击周围没有浮空的敌人。 
    """
    name = "反重力装置"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 8 #TODO
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [160, 1344]
    uuid = "e0daa922b19cdc35de879e938361464e"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 失败时攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 成功时攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 大成功、 超大成功时攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 失败率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 成功率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 大成功率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 魔道机械魔法阵大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    mode = ["失败", "成功", "大成功"]

    powerSuccess = 1.0
    powerFail = 1.0

    def setMode(self, mode):
        if mode == "失败":
            self.hit0 = 1
            self.hit1 = self.hit2 = 0
            self.skillRation *= self.powerFail
        elif mode == "成功":
            self.hit1 = 1
            self.hit0 = self.hit2 = 0
            self.skillRation *= self.powerSuccess
        elif mode == "大成功":
            self.hit2 = 1
            self.hit0 = self.hit1 = 0
            self.skillRation *= self.powerSuccess

    def vp_1(self):
        """
        [反重力装置]\n
        变更为可填充3次的技能\n
        - 每次填充冷却时间 : 6.6秒\n
        - 每次攻击力 -67%\n
        增加使敌人浮空的速度及降落速度\n
        施放时， 增加可空中冲刺的次数\n
        未学习[魔道学助手]技能或技能关闭时， 无法发动效果
        """
        self.cd = 6.6
        self.skillRation *= 1 - 0.67
        ...

    def vp_2(self):
        """
        [反重力装置]\n
        在空中生成魔法阵， 向下坠落并将敌人压制， 使敌人进入强制控制状态3秒\n
        - 未命中攻击的敌人进入技能范围时， 将受到攻击并被压制\n
        学习后， 固定以超大成功形态发动\n
        - 攻击范围 +50%
        """
        ...

# 暴炎加热炉
# mage_female/witch/e0a072e8cef2d77893aad5f68aeed56a
# 3909d0b188e9c95311399f776e331da5/e0a072e8cef2d77893aad5f68aeed56a
class Skill40(ActiveSkill):
    """
        [魔道机械/杰克爆弹系列技能]\n
        在地面上设置暴炎加热炉， 加热炉里会喷出火焰石块生成火属性爆炸。 经过一段时间或受到一定伤害， 加热炉都会发生爆炸。 可按方向键设置攻击方向。\n
        失败时， 喷出熔岩对周围造成伤害； 大成功时， 增加爆炸伤害和范围。\n
        在决斗场中， 施放[引爆试验]技能中断时魔道学者不会倒地。
    """
    name = "暴炎加热炉"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [180, 1512]
    uuid = "e0a072e8cef2d77893aad5f68aeed56a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 加热炉生命值 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 所受伤害减少率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 失败率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 成功率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 大成功率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 失败时熔岩多段攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 失败时熔岩多段攻击次数 : {value7}次
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 成功时火焰石块攻击力 : {value8}
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 成功时火焰石块多段攻击次数 : {value9}次
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 成功时加热炉爆炸攻击力 : {value10}
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 大成功时火焰石块攻击力 : {value11}
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 大成功时火焰石块多段攻击次数 : {value12}次
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 大成功时加热炉爆炸攻击力 : {value13}
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # 喷发的火焰石块对单个目标造成伤害次数上限 : {value14}
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # 超大成功时火焰石块攻击力 : {value15}
    data15 = get_data(f'{prefix}/{uuid}', 15)
    # 超大成功时火焰石块多段攻击次数 : {value16}次
    data16 = get_data(f'{prefix}/{uuid}', 16)
    # 超大成功时加热炉爆炸攻击力 : {value17}
    data17 = get_data(f'{prefix}/{uuid}', 17)
    # [范围信息]
    # 大成功时火焰石块及加热炉爆炸大小比率 : {value18}%
    data18 = get_data(f'{prefix}/{uuid}', 18)
    # 成功时火焰石块及加热炉爆炸大小比率 : {value19}%
    data19 = get_data(f'{prefix}/{uuid}', 19)
    # 失败时火柱大小比率 : {value20}%
    data20 = get_data(f'{prefix}/{uuid}', 20)

    mode = ["失败", "成功", "大成功"]

    powerSuccess = 1.0
    powerFail = 1.0

    def setMode(self, mode):
        if mode == "失败":
            self.hit6 = 13
            self.hit8 = self.hit15 = self.hit17 = 0
            self.skillRation *= self.powerFail
        elif mode == "成功":
            self.hit8 = 28
            self.hit6 = self.hit15 = self.hit17 = 0
            self.skillRation *= self.powerSuccess
        elif mode == "大成功":
            self.hit15 = 48
            self.hit17 = 1
            self.hit6 = self.hit8 = 0
            self.skillRation *= self.powerSuccess

    def vp_1(self):
        """
        [暴炎加热炉]\n
        召唤加热炉后， 在起身前输入1个部分技能时， 起身的同时施放该技能\n
        - 学习后， 固定以[苦涩棒棒糖]失败形态发动\n
        - 减少施放时间、 技能施放后僵直\n
        - 可输入的技能 : [改良魔法星弹]、 [改良舒露露]、 [魔道酸雨云]、 [熔岩药瓶]、 [电鳗碰撞机]、 [反重力装置]、 [光电兔]\n
        未学习[苦涩棒棒糖]技能时， 无法触发附加属性
        """
        self.setMode("失败")
        ...

    def vp_2(self):
        """
        [暴炎加热炉]\n
        冰霜雪人帮助杰克爆弹安装加热炉\n
        - 失败时， 无法触发[苦涩棒棒糖]效果\n
        - 石块爆炸范围 +20%\n
        学习后， 固定以大成功形态发动\n
        未学习[魔道学助手]技能或技能关闭时， 无法发动效果
        """
        self.setMode("大成功")
        ...

# 引爆试验
# mage_female/witch/ce572b597666f4472b1577a02fd5e1c3
# 3909d0b188e9c95311399f776e331da5/ce572b597666f4472b1577a02fd5e1c3
class Skill41(ActiveSkill):
    """
        施放[引爆试验]时， 立即引爆施放中的魔道机械系列部分技能， 并强制中断该技能。 技能施放过程中按跳跃键可以发动[引爆试验]。\n
    - [设置型技能] -\n
    [电鳗碰撞机]、 [暴炎加热炉] 、 [冰霜钻孔车]、 [光电兔]、 [雪人刨冰]、 [乌洛波洛斯之环]\n
        在决斗场中， 只有施放[暴炎加热炉]时可以发动[引爆试验]。
    """
    name = "引爆试验"
    learnLv = 40
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    mp = [200, 200]
    uuid = "ce572b597666f4472b1577a02fd5e1c3"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 冰霜钻孔车
# mage_female/witch/0fbb8de70002ad34f046c94c2cb3e863
# 3909d0b188e9c95311399f776e331da5/0fbb8de70002ad34f046c94c2cb3e863
class Skill42(ActiveSkill):
    """
        [魔道机械 / 冰霜雪人系列] 技能\n
        在空中组装冰霜钻孔车后， 落地生成冲击波给予周围敌人伤害。\n
        魔道学者乘坐钻孔车通过方向键控制钻孔车移动， 并给予敌人冰属性伤害。\n
        连续按攻击键或技能键， 可以吸附敌人。 按Z键可以转换方向。\n
        若冰霜钻孔车受到一定伤害， 则会损坏并结束技能。 若魔法师搭乘在冰霜钻孔车上， 受到的伤害减少。\n
        失败时， 冰霜钻孔车落地造成多段伤害后爆炸； 大成功时， 会生成大冰块钻孔机来装备钻孔车， 造成更大的伤害。
    """
    name = "冰霜钻孔车"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [360, 3024]
    uuid = "0fbb8de70002ad34f046c94c2cb3e863"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501
    #TODO REMARK 韩服接口 魔道数据错位

    # 冰霜钻孔车生命值 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 失败时多段攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 失败时多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 失败时爆炸攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 成功时钻孔车落地攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 成功时钻孔车攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 成功时钻孔车多段攻击次数 : {value7}次
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 大成功、 超大成功时钻孔车落地攻击力 : {value8}
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 大成功、 超大成功时钻孔车攻击力 : {value9}
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 大成功、 超大成功时钻孔车多段攻击次数 : {value10}次
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 最后爆炸攻击力 : {value11}
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 最后爆炸多段攻击次数 : {value12}次
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 失败率 : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # 成功率 : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # 大成功率 : {value15}%
    data15 = get_data(f'{prefix}/{uuid}', 15)
    # 所受伤害减少率 : {value16}%
    data16 = get_data(f'{prefix}/{uuid}', 16)
    # [范围信息]
    # 成功时[冰霜钻孔车]大小比率 : {value17}%
    data17 = get_data(f'{prefix}/{uuid}', 17)
    # 成功时最终爆炸范围比率 : {value18}%
    data18 = get_data(f'{prefix}/{uuid}', 18)
    # 失败时攻击范围比率 : {value19}%
    data19 = get_data(f'{prefix}/{uuid}', 19)

    mode = ["失败","大成功"]

    powerSuccess = 1.0
    powerFail = 1.0

    def setMode(self, mode):
        if mode == "失败":
            self.hit2 = 9
            self.hit4 = 1
            self.hit8 = self.hit9 = self.hit11 = 0
            self.skillRation *= self.powerFail
        elif mode == "大成功":
            self.hit8 = 1
            self.hit9 = 47
            self.hit11 = 3
            self.hit2 = self.hit4 = 0
            self.skillRation *= self.powerSuccess

    def vp_1(self):
        """
        [冰霜钻孔车]\n
        学习后， 变更[苦涩棒棒糖]失败形态； 输入技能键时， 立即施放失败形态\n
        - 乘坐冰霜钻孔车向最强敌人突进后爆炸\n
        - 学习后， 固定以失败形态发动\n
        - 突进时， 沿移动路径抓取敌人\n
        - 突进过程中进入无敌状态\n
        学习后， 无法发动[引爆试验]以及[旋转扫把]摔倒后立即发动技能的功能\n
        未学习[苦涩棒棒糖]时， 无法施放[冰霜钻孔车]\n
        删除多段攻击\n
        - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [冰霜钻孔车]\n
        可以在乘坐冰霜钻孔车状态下施放部分技能\n
        - 乘坐时， 固定以超大成功形态发动\n
        - 可施放技能 : [改良魔法星弹]、 [改良舒露露]、 [熔岩药瓶]、 [魔道酸雨云]、 [电鳗碰撞机] (进化方向2除外)、 [反重力装置]\n
        - 以最大连击次数标准施放\n
        - 乘坐时， 可以按空格键进行跳跃\n
        - 乘坐移动速度 +30%\n
        - 乘坐时攻击范围 +40%\n
        乘坐持续时间 +4.5秒\n
        [苦涩棒棒糖]失败时， 生成吸附敌人的旋风\n
        - 失败时攻击范围 +40%\n
        - 失败时， 被爆炸命中的敌人进入冰冻状态3秒\n
        - 失败时， 施放速度 +30%\n
        - 失败时， 多段攻击命中后到爆炸的时间减少
        """
        ...

# 成功预感
# mage_female/witch/5806440d21e7546d50007a5ba11f8024
# 3909d0b188e9c95311399f776e331da5/5806440d21e7546d50007a5ba11f8024
class Skill43(PassiveSkill):
    """
        学习后， 增加魔法暴击率和魔法暴击伤害。\n
        魔道学者使用转职技能时， 有一定几率在一定时间内增加下一个技能的成功率和大成功率。
    """
    name = "成功预感"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "5806440d21e7546d50007a5ba11f8024"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 成功预感发动几率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 成功率增加量 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 大成功率增加量 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 成功预感持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 魔法暴击伤害增加量 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 魔法暴击率增加量 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    associate = [{"data":data4}]

# 技艺融合
# mage_female/witch/3fb8395ae3b81bd608e0c4223a8eb534
# 3909d0b188e9c95311399f776e331da5/3fb8395ae3b81bd608e0c4223a8eb534
class Skill44(ActiveSkill):
    """
        [魔道机械系列]\n
        利用法米利尔的力量产生的机械装置， 将敌人吸附过来， 可以束缚敌人并使敌人受到巨大伤害。\n
        电鳗罗刹可以束缚敌人并使其受到光属性伤害； 杰克追击者可以使敌人受到火属性爆炸伤害； 冰霜雪人可以使敌人受到冰属性伤害； 最后利用暗影猫之拳破坏设置好的机械装置， 使敌人受到暗属性伤害并向后击飞。\n
        杰克工厂和雪人风暴生成之后， 若连按技能键或攻击键， 则更快速地生产杰克追击者和冰霜雪人。
    """
    name = "技艺融合"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [1000, 8400]
    uuid = "3fb8395ae3b81bd608e0c4223a8eb534"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 法米利尔团体多段攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 21
    # 法米利尔团体多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 电鳗罗刹束缚几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 电鳗罗刹束缚持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 暗影猫之拳攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1

# 超级苍蝇拍
# mage_female/witch/ac21c02567f04a92b54dd85c091d1e5a
# 3909d0b188e9c95311399f776e331da5/ac21c02567f04a92b54dd85c091d1e5a
class Skill45(ActiveSkill):
    """
        [暗影夜猫系列技能]\n
        使用超级苍蝇拍强力拍打前方的敌人， 并给予敌人暗属性的伤害。 攻击时， 利用苍蝇拍的变异型魔力性质， 用敌人身体的一部分作为媒介， 有一定几率召唤出变异怪物。\n
    失败时 : 可召唤敌军怪物； 成功时 : 可召唤友军怪物； 大成功时 : 可召唤出强大的友军怪物。 
    """
    name = "超级苍蝇拍"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 1 #TODO
    rangeLv = 2
    cube = 2
    cd = 30
    mp = [400, 1120]
    uuid = "ac21c02567f04a92b54dd85c091d1e5a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 召唤几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 存在时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 失败率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 成功率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 大成功率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 苍蝇拍大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def effect(self, old, new):
        if self.vp == 1:
            self.associate = [{"data": [0]+[-17.6]*self.maxLv,"skills":["变异苍蝇拍"]}]
        return super().effect(old, new)

    def vp_1(self):
        """
        [超级苍蝇拍]\n
        使冲击波向周围扩散\n
        - [超级苍蝇拍]大小 -15%\n
        - 施放速度 +30%\n
        施放[超级苍蝇拍]时初始化[变异苍蝇拍]技能冷却时间\n
        - [变异苍蝇拍]攻击力 -17.6%\n
        - [变异苍蝇拍]攻击范围 +40%\n
        - 增加[变异苍蝇拍]地面施放时的跳跃高度
        """
        ...

    def vp_2(self):
        """
        [超级苍蝇拍]\n
        - 100%几率对每个命中的敌人随机召唤2个何蒙库鲁兹\n
        - 删除何蒙库鲁兹持续时间\n
        - 变更为最多可召唤4只\n
        - 删除杰克爆弹的迷你杰克爆弹攻击\n
        - 杰克爆弹何蒙库鲁兹的总攻击力相同\n
        - 优先召唤未被召唤过的何蒙库鲁兹\n
        - 何蒙库鲁兹攻击速度 +10%\n
        - 何蒙库鲁兹攻击范围 +30%\n
        何蒙库鲁兹的部分攻击附带异常状态\n
        - 杰克爆弹 : 灼伤及减速异常状态\n
        - 暗影夜猫 : 中毒及束缚异常状态\n
        - 光电鳗 : 感电及眩晕异常状态\n
        - 冰霜雪人 : 出血及冰冻异常状态\n
        学习后， 固定以超大成功形态发动\n
        [苍蝇拍 : 魔法禁锢]开启状态下， 召唤功能无效\n
        未学习[魔道学助手]技能或技能关闭时， 无法发动效果\n
        在地下城中开启[苍蝇拍 : 魔法禁锢]或关闭[魔道学助手]时， 已召唤的何蒙库鲁兹会立即消失
        """
        ...

# 光电兔
# mage_female/witch/8b08f9504167a9c0f3a1d29d71b7943e
# 3909d0b188e9c95311399f776e331da5/8b08f9504167a9c0f3a1d29d71b7943e
class Skill46(ActiveSkill):
    """
        [魔道机械/光电鳗系列技能]\n
        操作可怕的兔子机械进行超高压的光属性电击伤害。\n
        有一定几率出现失败、 成功、 大成功， 并依此出现不同效果。\n
        成功情况越高， 攻击范围和攻击力越大。\n
        对命中的敌人有一定几率赋予感电异常状态， 并且在操作兔子机械时所受伤害减少。
    """
    name = "光电兔"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [800, 1680]
    uuid = "8b08f9504167a9c0f3a1d29d71b7943e"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 失败率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 成功率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 大成功率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 失败多段攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 成功多段攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 大成功多段攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 4
    # 多段攻击次数 : {value6}次
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 兔子机械爆炸失败攻击力 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 兔子机械爆炸成功攻击力 : {value8}
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 兔子机械爆炸大成功攻击力 : {value9}
    data9 = get_data(f'{prefix}/{uuid}', 9)
    hit9 = 1
    # 感电几率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 感电攻击力 : {value11}
    data11 = get_data(f'{prefix}/{uuid}', 11)
    hit11 = 4
    # 感电持续时间 : {value12}秒
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 所受伤害减少率 : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # [范围信息]
    # 攻击范围比率 : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)

    powerSuccess = 1.0
    powerFail = 1.0

    def setMode(self, mode):
        self.skillRation *= self.powerSuccess

    def vp_1(self):
        """
        [光电兔]\n
        光电兔充能后引发爆炸\n
        - 光电兔逐渐变大， 魔法阵逐渐变小\n
        - 魔法阵变小时， 魔法阵内的敌人会进入僵直状态并被吸附过来\n
        光电兔完全充能后， 再次按技能键时会引发爆炸\n
        - 最多可以持续15秒\n
        - 施放其他技能过程中可以引发爆炸， 持续时间结束时自动爆炸\n
        删除多段攻击\n
        - 总攻击力相同\n
        固定以超大成功形态发动\n
         魔法阵大小 +30%\n
        光电兔爆炸大小 +50%\n
        学习后， 无法发动[引爆试验]
        """
        ...

    def vp_2(self):
        """
        [光电兔]\n
        光电鳗何蒙库鲁兹出现并拉动操作杆\n
        - 光电兔会喷出蓝色闪电\n
        - 可以在空中施放\n
        学习后， 固定以超大成功形态发动\n
        未学习[魔道学助手]技能或技能关闭时， 无法发动效果
        """
        ...

# 雪人刨冰
# mage_female/witch/b8f4966608e4ebb3cc80ba4eac3649bb
# 3909d0b188e9c95311399f776e331da5/b8f4966608e4ebb3cc80ba4eac3649bb
class Skill47(ActiveSkill):
    """
        [魔道机械 / 冰霜雪人系列] 技能\n
       组装冰霜雪人外形的刨冰机， 冻住一定范围内的敌人使其僵直， 然后将敌人聚到一处， 将其制成冰爽的刨冰。\n
        刨冰刀对聚拢的敌人造成巨大伤害， 并且向四周射出碎冰块攻击敌人， 一定时间后发生爆炸。\n
        施放后连续按<X>键， 可以加快攻击速度。
    """
    name = "雪人刨冰"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [360, 3024]
    uuid = "b8f4966608e4ebb3cc80ba4eac3649bb"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 刨冰刀刃多段攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 21
    # 刨冰刀刃多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 碎冰块攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 11
    # 碎冰块多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 最终爆炸攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # [范围信息]
    # 攻击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [雪人刨冰]\n
        放置刨冰机时， 发动高速模式\n
        - 刨冰机放置速度 +50%\n
        - 刨冰机旋转速度 +100%\n
        搭乘刨冰机时， 立即以最大速度旋转\n
        刨冰机旋转时， 持续将吸附敌人至中心
        """
        ...

    def vp_2(self):
        """
        [雪人刨冰]\n
        改造雪人刨冰机， 可以用于制作女巫汤\n
        - 可将冰霜雪人、 杰克爆弹、 光电鳗系列部分技能投入锅中\n
        - 选择技能时， 不单独执行该技能， 合并攻击力\n
        - 冰霜雪人系列技能 : [魔道酸雨云]、 [冰霜钻孔车]\n
        - 杰克爆弹系列技能 : [熔岩药瓶]、 [暴炎加热炉]\n
        - 光电鳗系列技能 : [电鳗碰撞机]、 [光电兔]\n
        - 光电鳗技能的感电几率和感电伤害与所选技能一致\n
        - 合算时， 适用所选技能的进程中最高的攻击力\n
        (若所选技能处于技能定制状态， 则适用该进程中最高的攻击)\n
        学习后， 无法发动[引爆试验]\n
        删除刨冰刀刃、 碎冰块和最终爆炸攻击\n
        - 增加搅拌、 终结攻击\n
        - 总攻击力相同\n
        攻击范围 +15%
        """
        ...

# 贤者之石
# mage_female/witch/8e358ecf99ac9df31a6132aeafe378a9
# 3909d0b188e9c95311399f776e331da5/8e358ecf99ac9df31a6132aeafe378a9
class Skill48(PassiveSkill):
    """
        运用魔道学中的圣器——贤者之石作为媒介， 获得比以往更高境界的成果。\n
        使用[引爆试验]时， 自身不会摔倒； 使用[旋转扫把]时， 不会进入混乱状态。\n
         进入地下城后， [魔法秀]技能变更为全程适用； 另外， 以数值最高的属性强化为标准， 使其他属性强化发生一定量变化。\n
        施放时具有超大成功的可能性， 且部分技能超大成功时新增效果。\n
    - [超大成功时新增效果的技能] -\n
    [熔岩药瓶]、 [魔道酸雨云]、 [电鳗碰撞机]、 [暴炎加热炉]、 [反重力装置]
    """
    name = "贤者之石"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 1 #TODO
    rangeLv = 3
    uuid = "8e358ecf99ac9df31a6132aeafe378a9"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # [超大成功附加效果]
    # <超大成功时新增效果>
    # 成功、 大成功、 超大成功攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # <熔岩药瓶>
    # 生成适用单独攻击力的火球
    # <魔道酸雨云>
    # 闪电生成间隔减少 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # <暴炎加热炉>
    # 火球生成间隔减少 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 火球数量增加 : {value3}个
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # <电鳗碰撞机>
    # 多段攻击间隔减少 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 僵直时间增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # <反重力装置>
    # 魔道机械魔法阵范围增加 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [持续效果]
    # 属性强化变化比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [冰霜钻孔车]攻击力增加率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

    associate = [
        {"data":data0,"type":"+powerSuccess","skills":['改良舒露露','改良魔法星弹','魔道酸雨云', '电鳗碰撞机', '反重力装置', '熔岩药瓶', '暴炎加热炉']},
        {"data":data8,"skills":['冰霜钻孔车']}
    ]

class Skill49(PassiveSkill):
    """
        魔道学者经过长时间的研究， 结合魔道学和法米利尔的能量制作了人造生命体——何蒙库鲁兹并将其当做自己的助手， 大大增强特定技能的效果。
        何蒙库鲁兹的技能等级随[贤者之石]技能等级增加而增加。
    """
    # 接口缺少该技能数据
    name = "魔道学助手"
    learnLv = 75
    masterLv = 1
    maxLv = 1
    position = 2
    rangeLv = 3
    uuid = "84fd944f5aef4283b100c73152d9c4fa"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    data0 = [0] + [17 + 2*i for i in range(1, maxLv + 1)]
    data1 = [0] + [38 + 2*i for i in range(1, maxLv + 1)]

    associate = [
        {"data":data0,"skills":['变异苍蝇拍', '超级苍蝇拍', '改良舒露露', '改良魔法星弹', '暗影斗篷', '技艺融合','超级棒棒糖', '光电兔', '雪人刨冰', '乌洛波洛斯之环', '糖果大作战精怪乐园', '糖果大作战捣蛋杰克']},
        {"data":data1,"type":"+powerFail","skills":['熔岩药瓶', '暴炎加热炉', '冰霜钻孔车']}
    ]

    @property
    def lv(self):
        """技能等级"""
        return self.char.GetSkillByName("贤者之石").lv

    @lv.setter
    def lv(self, value):
        ...

# 超级棒棒糖
# mage_female/witch/9bc30e0f6e22b0333762d04acae7d252
# 3909d0b188e9c95311399f776e331da5/9bc30e0f6e22b0333762d04acae7d252
class Skill50(ActiveSkill):
    """
        使用巨大的棒棒糖拍打前方敌人， 击中敌人后会召唤糖果人偶。\n
        召唤出的糖果会搜寻敌人并引发爆炸。\n
        召唤出的糖果人偶根据颜色具有不同的特效。\n
        黑色糖果人偶 : 攻击敌人的同时， 有一定几率使敌人进入失明状态。\n
        白色糖果人偶 : 攻击敌人的同时， 有一定几率使敌人进入感电状态。\n
    拍打领主或者稀有怪物时， 可以召唤出更强大的暗属性特殊糖果人偶。\n
        可以在空中施放该技能。\n
        领主/稀有糖果人偶的糖果人偶栏可持有数量， 与白色糖果人偶和黑色糖果人偶不同。
    """
    name = "超级棒棒糖"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 2 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "9bc30e0f6e22b0333762d04acae7d252"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 拍打攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 击中一个敌人召唤的糖果人偶数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 糖果人偶爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 领主/稀有糖果人偶攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 失明几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 失明持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 失明视野减少率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 失明减少命中率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 感电几率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 感电持续时间 : {value9}秒
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 感电攻击力 : {value10}
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 糖果人偶召唤数上限 : {value11}个
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 领主/稀有糖果人偶的糖果人偶栏可持有数量 : {value12}个
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # [范围信息]
    # 棒棒糖大小比率 : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13)

    def vp_1(self):
        """
        [超级棒棒糖]\n
        不生成糖果人偶\n
        地面施放时， 不再跳跃， 向前方拍下巨大的棒棒糖\n
        - 巨大糖果直接命中敌人时， 可以强制中断并施放转职技能\n
        - 未命中时冷却时间变更为5秒\n
        删除糖果人偶攻击\n
        - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [超级棒棒糖]\n
        命中时， 有一定几率生成魔道学者藏起来的糖果\n
        靠近糖果时快速回收， 融化后食用时获得增益效果\n
        至少生成1个糖果， 根据概率最多可生成3个\n
        - 效果持续时间 : 20秒\n
        - 红色糖果 : 进入霸体状态， 所受伤害 -10%\n
        - 蓝色糖果 : 攻击、 移动、 施放速度 +20%\n
        - 绿色糖果 : 每秒恢复2%的生命值和魔法值
        """
        ...

# 乌洛波洛斯之环
# mage_female/witch/0f638da961acf7958ac6070b7aaed013
# 3909d0b188e9c95311399f776e331da5/0f638da961acf7958ac6070b7aaed013
class Skill51(ActiveSkill):
    """
    [魔道机械系列]\n
        运用魔道学中象征着无限循环的乌洛波洛斯之环攻击敌人。\n
        魔道学者与何蒙库鲁兹一起驾驶装置， 同时释放出与自身属性相同的元素闪电。\n
        若施放中连续按攻击键， 则履带旋转速度增加， 持续时间减少， 此时兴奋的何蒙库鲁兹会大喊万岁。\n
        持续时间结束或中断技能时， 乌洛波洛斯之环会爆炸并攻击周围的敌人。
    """
    name = "乌洛波洛斯之环"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 8000]
    uuid = "0f638da961acf7958ac6070b7aaed013"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间上限 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 履带多段攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 20
    # 履带多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 元素闪电攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 20
    # 元素闪电多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 最后爆炸攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1

# 粉红糖果
# mage_female/witch/f1111c21369d2b835b186dd1d58be88d
# 3909d0b188e9c95311399f776e331da5/f1111c21369d2b835b186dd1d58be88d
class Skill52(PassiveSkill):
    """
        粉红糖果， 魔道学的精髓， 是用贤者之石加工而成的世界上最珍贵最危险的糖果。\n
        增加基本攻击及转职技能攻击力， 部分法米利尔进化成各种形态的魔道学助手， 发挥比以前更特殊的能力。\n
    [暗影斗篷]\n
        进化为暗影夜猫魔道学助手。 暗影夜猫魔道学助手使用暗影斗篷后， 会观察周围， 如果发现还有敌人没有被拉进斗篷里的话， 会伸展猫臂， 将范围内的敌人拉进斗篷里。\n
    [魔道酸雨云]\n
        进化为拥有自我意识的冰霜云魔道学助手。 冰霜云会追击周围最强大敌人， 用冰雹和冰块对其进行攻击。 命中的敌人有一定的几率进入冰冻状态。\n
        冰雹和冰块的攻击力和大成功时的酸雨和闪电攻击力相同。
    """
    name = "粉红糖果"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 1 #TODO
    rangeLv = 3
    uuid = "f1111c21369d2b835b186dd1d58be88d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 冰霜云冰冻几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 冰霜云冰冻持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    associate = [{"data": data0}]

# 糖果大作战 : 捣蛋杰克
# mage_female/witch/fa7f1a3dc90600456cbe010e5714bef3
# 3909d0b188e9c95311399f776e331da5/fa7f1a3dc90600456cbe010e5714bef3
class Skill53(ActiveSkill):
    """
        [杰克爆弹系列技能]\n
        用最大最甜的南瓜和最优质的粉红糖果创造的魔道学助手。\n
        捣蛋杰克会追随自己的创造者魔道学者的脚步， 向前方的敌人喷射地狱般的高温岩浆。\n
        再次按技能键时， 捣蛋杰克会转换方向， 向相反的方向喷射岩浆。
    """
    name = "糖果大作战 : 捣蛋杰克"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [773, 6000]
    uuid = "fa7f1a3dc90600456cbe010e5714bef3"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 岩浆攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 25
    # 岩浆多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 糖果大作战 : 精怪乐园
# mage_female/witch/5fe93d62fcf6d0b1bb6b910b2dd24a0b
# 3909d0b188e9c95311399f776e331da5/5fe93d62fcf6d0b1bb6b910b2dd24a0b
class Skill54(ActiveSkill):
    """
        [魔道机械系列]\n
        魔道学者结合所有研究成果， 创造出终极魔道机械过山车“精怪号”， 并搭乘过山车。 魔道学助手们也按照各自特性搭乘过山车或制作过山车轨道等， 各自执行自己的任务。\n
        搭载魔道学者和魔道学助手的精怪号会喷射出熔岩球， 横穿整个画面后， 高高冲到空中， 直接脱离轨道后掉落到地面， 华丽地爆炸。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "糖果大作战 : 精怪乐园"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "5fe93d62fcf6d0b1bb6b910b2dd24a0b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 过山车驶过攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 过山车驶过多段攻击次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 过山车返回攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 4
    # 过山车返回多段攻击次数 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 坠落攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # 终结爆炸攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 4
    # 终结爆炸多段攻击次数 : {value6}次
    data6 = get_data(f'{prefix}/{uuid}', 6)



class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'witch'
        self.nameCN = '知源·魔道学者'
        self.role = 'mage_female'
        self.角色 = '魔法师(女)'
        self.职业 = '魔道学者'
        self.jobId = '3909d0b188e9c95311399f776e331da5'
        self.jobGrowId = 'c9b492038ee3ca8d27d7004cf58d59f3'

        self.武器选项 = ['扫把','魔杖', '法杖', '矛', '棍棒'] # TODO
        self.输出类型选项 = ["魔法固伤"] # TODO
        self.输出类型 = '魔法固伤' # TODO
        self.防具精通属性 = ['智力'] # TODO
        self.防具类型 = '皮甲'
        self.buff = 1.992

        super().__init__(equVersion, __name__)
