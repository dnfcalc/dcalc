#b9cb48777665de22c006fabaf9a560b3
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "archer/traveler/cn/skillDetail"

# 附件 : 迷雾装置
# archer/traveler/9dda3f4a849dba1a288dd65e116860f2
# b9cb48777665de22c006fabaf9a560b3/9dda3f4a849dba1a288dd65e116860f2
class Skill0(PassiveSkill):
    """
        利用神界技术制作而成的迷雾装置。\n
    按照自由旅行家组织“流浪协会”的需求而设计， 可以提高旅人的弓术和机动力。\n
        装备玄机弓时， 在玄机弓上方安装用于辅助射击的迷雾装置。 旅人的弓术都依托于迷雾装置的辅助， 没有迷雾装置就无法施展弓术系列技能。\n
        可以在后跳中射击， 决斗场中存在1秒的冷却时间。
    """
    name = "附件 : 迷雾装置"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 4 #TODO
    rangeLv = 3
    uuid = "9dda3f4a849dba1a288dd65e116860f2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 凌跃一击
# archer/traveler/0969cd4054d93da07708108c0cc1c4b5
# b9cb48777665de22c006fabaf9a560b3/0969cd4054d93da07708108c0cc1c4b5
class Skill1(ActiveSkill):
    """
        该技能可在地面和空中施放。\n
        向后微微跃起， 并根据武器的不同， 向地面发射不同的投射物， 使敌人浮空。\n
        攻击时， 有霸体判定； 转职为缪斯或奇美拉后， 技能类型变为独立攻击力。
    """
    name = "凌跃一击"
    learnLv = 1
    masterLv = 10
    maxLv = 20
    position = 5 #TODO
    rangeLv = 3
    cd = 2
    uuid = "0969cd4054d93da07708108c0cc1c4b5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 箭矢攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 冲击波浮空力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [转职为缪斯后]
    # 棱镜攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 冲击波攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [转职为妖护使后]
    # 妖兽上勾拳攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [转职为奇美拉后]
    # 箭矢攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 冲击波攻击力 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)

# 迷雾爆裂
# archer/traveler/717f1e2104fe4b796f800352fa143ecc
# b9cb48777665de22c006fabaf9a560b3/717f1e2104fe4b796f800352fa143ecc
class Skill2(ActiveSkill):
    """
        通过弓弦从迷雾装置吸收迷雾能量， 发射强化箭矢。\n
        箭矢命中敌人时造成伤害， 并产生冲击波对周围敌人造成伤害。
    """
    name = "迷雾爆裂"
    learnLv = 1
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 4
    mp = [11, 64]
    uuid = "717f1e2104fe4b796f800352fa143ecc"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 箭矢攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 冲击波范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 后跳
# archer/traveler/7822d6d52e10964a6755f142c666b494
# b9cb48777665de22c006fabaf9a560b3/7822d6d52e10964a6755f142c666b494
class Skill3(ActiveSkill):
    """
        使自身向后方小跳并避开敌人的攻击。
    """
    name = "后跳"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 3 #TODO
    rangeLv = 1
    mp = [1, 1]
    uuid = "7822d6d52e10964a6755f142c666b494"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 基础精通
# archer/traveler/5a56514f35cf0270ae8d6c65f8fefd78
# b9cb48777665de22c006fabaf9a560b3/5a56514f35cf0270ae8d6c65f8fefd78
class Skill4(PassiveSkill):
    """
        增加基本攻击、 前冲攻击、 跳跃攻击、 [凌跃一击]技能的攻击力。\n
        决斗场中， 增益/减益技能、 被动技能的技能攻击力增加效果对[基础精通]无影响。
    """
    name = "基础精通"
    learnLv = 1
    masterLv = 115
    maxLv = 200
    position = 1 #TODO
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

    associate = [{"type":"*skillDamage","data":[i-100 if i>0 else 0 for i in data0],"skills":["迷雾箭雨"]}]

# 受身蹲伏
# archer/traveler/ce26c6b69d02a440a81b552bec94f03b
# b9cb48777665de22c006fabaf9a560b3/ce26c6b69d02a440a81b552bec94f03b
class Skill5(ActiveSkill):
    """
        使自身在倒地状态下迅速起身并采取蹲伏姿势； 蹲伏状态下， 自身会进入无敌状态， 效果持续一定时间。
    """
    name = "受身蹲伏"
    learnLv = 1
    masterLv = 10
    maxLv = 20
    position = 2 #TODO
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

# 防具精通
# archer/traveler/892ef624d8bf3d7fc045f84825fd6104
# b9cb48777665de22c006fabaf9a560b3/892ef624d8bf3d7fc045f84825fd6104
class Skill6(PassiveSkill):
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


# 绝技袭击
# archer/traveler/eb71e1d82d92c7e1d40500a0dcd77aa6
# b9cb48777665de22c006fabaf9a560b3/eb71e1d82d92c7e1d40500a0dcd77aa6
class Skill7(ActiveSkill):
    """
        该技能可在地面或空中施放。\n
        激活鞋子上的迷雾推进装置， 敏捷地向前上方跳起， 对地面上的敌人射击进行牵制后落地。
    """
    name = "绝技袭击"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 4
    mp = [22, 132]
    uuid = "eb71e1d82d92c7e1d40500a0dcd77aa6"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 箭矢攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2
    # 迷雾箭矢攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 4

# 全力挥击
# archer/traveler/4655101518604f874721b3cc249aae10
# b9cb48777665de22c006fabaf9a560b3/4655101518604f874721b3cc249aae10
class Skill8(ActiveSkill):
    """
        用力挥舞弓， 击打周围的敌人， 并向前推出。\n
    转职为猎人时， 再次按技能键会立即发射一枚爆炸箭矢， 造成额外伤害。\n
    转职为缪斯或奇美拉时， 技能类型变为独立攻击力。
    """
    name = "全力挥击"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 1 #TODO
    rangeLv = 2
    cd = 5
    mp = [28, 165]
    uuid = "4655101518604f874721b3cc249aae10"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 击打攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [转职为猎人后]
    # 爆炸箭矢攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 转职为猎人时， 爆炸箭矢射程 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 转职为猎人时， 爆炸箭矢爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 高速机动
# archer/traveler/147d005ac868e0de52b1f255eea35d62
# b9cb48777665de22c006fabaf9a560b3/147d005ac868e0de52b1f255eea35d62
class Skill9(ActiveSkill):
    """
        该技能可以在地面和空中施放； 可以强制中断其他技能并施放该技能。\n
        地面施放时， 快速后退； 空中施放时， 快速落地。
    """
    name = "高速机动"
    learnLv = 5
    masterLv = 1
    maxLv = 1
    position = 4 #TODO
    rangeLv = 3
    cd = 6
    mp = [20, 20]
    uuid = "147d005ac868e0de52b1f255eea35d62"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 向后移动距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)

# 翻月翔击
# archer/traveler/c9664191611af31142e052dfaef84530
# b9cb48777665de22c006fabaf9a560b3/c9664191611af31142e052dfaef84530
class Skill10(ActiveSkill):
    """
        前冲并踢飞命中的敌人。\n
        踢击仅对一名敌人造成伤害， 冲击波可以对除该敌人外附近的敌人造成伤害。\n
        对无法抓取的敌人不适用控制效果。\n
        可以按方向键调整冲刺方向。\n
        转职为缪斯或奇美拉后， 技能类型变为独立攻击力。\n
        转职为旅人时， 可以强制中断踢击后的僵直并施放空中技能。\n
        转职为妖护使时， 可以在空中施放。
    """
    name = "翻月翔击"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 5
    mp = [35, 206]
    uuid = "c9664191611af31142e052dfaef84530"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 踢击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 营火
# archer/traveler/f2fb27162beb0b87a7cb9af7900e95f2
# b9cb48777665de22c006fabaf9a560b3/f2fb27162beb0b87a7cb9af7900e95f2
class Skill11(ActiveSkill):
    """
        向前扔出一个可自动安装的营火工具， 温暖的热量可以恢复范围内所有队员的生命值。\n
        在一定范围内则获得最大恢复量， 距离越远恢复量越少。\n
        在最大恢复量适用范围内时， 增加冰冻抗性， 解除冰冻状态。
    """
    name = "营火"
    learnLv = 10
    masterLv = 1
    maxLv = 11
    position = 6 #TODO
    rangeLv = 3
    cds = [0, 20, 19.5, 19, 18.5, 18, 17.5, 17, 16.5, 16, 15.5, 15]
    mp = [85, 146]
    uuid = "f2fb27162beb0b87a7cb9af7900e95f2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 营火持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 生命值恢复间隔 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 每次间隔恢复的最大生命值量 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 每次间隔恢复的最小生命值量 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 冰冻抗性增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [学习野外生存后]
    # 炖菜生命值恢复量 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 炖菜魔法值恢复量 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 生命值最大恢复范围 : {value7}px
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 生命值最小恢复范围 : {value8}px
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 在最小恢复范围外不会获得恢复。

    def getSkillCD(self, mode=None):
        self.cd = self.cds[self.lv]
        return super().getSkillCD(mode)

# 强化 - 后跳
# archer/traveler/2b340542e776818b78f3212af184bd6b
# b9cb48777665de22c006fabaf9a560b3/2b340542e776818b78f3212af184bd6b
class Skill12(PassiveSkill):
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
    position = 4 #TODO
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
# archer/traveler/1fea5a626f15230237946a11a9d11582
# b9cb48777665de22c006fabaf9a560b3/1fea5a626f15230237946a11a9d11582
class Skill13(ActiveSkill):
    """
        增加自身20%的跳跃力， 效果持续一定时间。\n
        效果持续期间内， 再次按技能键可以结束。
    """
    name = "跃翔"
    learnLv = 10
    masterLv = 1
    maxLv = 1
    position = 6 #TODO
    rangeLv = 3
    cd = 5
    mp = [13, 13]
    uuid = "1fea5a626f15230237946a11a9d11582"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)

# 迷雾箭雨
# archer/traveler/cfacda0647b9a0f595df2c2aad30c18d
# b9cb48777665de22c006fabaf9a560b3/cfacda0647b9a0f595df2c2aad30c18d
class Skill14(ActiveSkill):
    """
        将迷雾装置的迷雾能量凝聚在箭头发射。\n
        射出的箭矢被浓缩的迷雾能量穿透， 分裂成数支迷雾箭矢攻击前方敌人， 被箭射中的敌人受到多段伤害。\n
        技能受[基础精通]的影响。
    """
    name = "迷雾箭雨"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 2 #TODO
    rangeLv = 2
    cd = 4
    mp = [29, 29]
    uuid = "cfacda0647b9a0f595df2c2aad30c18d"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 每次发射的攻击次数上限 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 每次攻击的攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 9
    # [范围信息]
    # 箭矢射程 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 驱虫烈火
# archer/traveler/45442bbbe33540b4deeec29437dae70c
# b9cb48777665de22c006fabaf9a560b3/45442bbbe33540b4deeec29437dae70c
class Skill15(ActiveSkill):
    """
        旅行必需品“引火器”的功率加大， 发射火焰， 消灭周围的毒虫。\n
        火焰命中的敌人受到火属性伤害， 并进入灼伤异常状态。\n
        被火焰命中时， 位于旅人后方和两侧的敌人被吸附至前方。
    """
    name = "驱虫烈火"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 7
    mp = [68, 401]
    uuid = "45442bbbe33540b4deeec29437dae70c"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 火焰攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 灼伤攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 灼伤持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 灼伤几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 玄机弓精通
# archer/traveler/01c3a2fb793d293a25ed8dc7a0d70c1a
# b9cb48777665de22c006fabaf9a560b3/01c3a2fb793d293a25ed8dc7a0d70c1a
class Skill16(PassiveSkill):
    """
        时刻铭记修炼弓术的重要性可谓是旅人守则的基础中的基础。\n
        增加物理攻击力， 装备玄机弓时， 增加命中率。
    """
    name = "玄机弓精通"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 5 #TODO
    rangeLv = 3
    uuid = "01c3a2fb793d293a25ed8dc7a0d70c1a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 命中率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [{"type":"$*PAtkP","data":data0}]

# 暴击
# archer/traveler/fc1262c19f3d0477ee8eda47b8db8696
# b9cb48777665de22c006fabaf9a560b3/fc1262c19f3d0477ee8eda47b8db8696
class Skill17(PassiveSkill):
    """
        集中精神， 提升物理/魔法暴击率。
    """
    name = "暴击"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 5 #TODO
    rangeLv = 3
    uuid = "fc1262c19f3d0477ee8eda47b8db8696"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 物理/魔法暴击率增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

# 三重加速
# archer/traveler/8f73f243041c2d27739fe7696f02bf9b
# b9cb48777665de22c006fabaf9a560b3/8f73f243041c2d27739fe7696f02bf9b
class Skill18(ActiveSkill):
    """
        该技能可在地面或空中施放。\n
        激活鞋子上的迷雾推进装置， 向后方跳跃， 发射三支箭矢后落地。
    """
    name = "三重加速"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 6
    mp = [55, 325]
    uuid = "8f73f243041c2d27739fe7696f02bf9b"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 箭矢攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 箭矢冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 3
    # 迷雾箭矢攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 3
    # 迷雾箭矢冲击波攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 3
    # [范围信息]
    # 冲击波范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 斗志昂扬
# archer/traveler/9cb6f9ed646fa87f9b7680a42ce83d1a
# b9cb48777665de22c006fabaf9a560b3/9cb6f9ed646fa87f9b7680a42ce83d1a
class Skill19(ActiveSkill):
    """
        旅行总是充满了令人兴奋的奇遇， 清澈的阳光照耀着前方的道路， 旅人已准备好迎接每一场旅行。\n
        增加自身基本攻击力、 技能攻击力和移动速度。
    """
    name = "斗志昂扬"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 5 #TODO
    rangeLv = 3
    cd = 5
    uuid = "9cb6f9ed646fa87f9b7680a42ce83d1a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 移动速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 细雨
# archer/traveler/4224f9b0b8c7c903e9a1e0f9d9f6d04d
# b9cb48777665de22c006fabaf9a560b3/4224f9b0b8c7c903e9a1e0f9d9f6d04d
class Skill20(ActiveSkill):
    """
        以抛物线发射箭矢和迷雾箭雨。\n
    发射的箭矢冲向地面产生冲击波， 击倒敌人。
    """
    name = "细雨"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cd = 7
    mp = [72, 426]
    uuid = "4224f9b0b8c7c903e9a1e0f9d9f6d04d"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 冲击波攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 冲击波范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 急流
# archer/traveler/78bd107acd474518b606be1e4fd38239
# b9cb48777665de22c006fabaf9a560b3/78bd107acd474518b606be1e4fd38239
class Skill21(ActiveSkill):
    """
        以旋风的形态发射迷雾能量， 将被击中的敌人聚拢在一直线上， 随后连续发射震动箭。\n
        被震动箭命中的敌人会被回旋的迷雾之风控制一段时间。
    """
    name = "急流"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 8
    mp = [82, 486]
    uuid = "78bd107acd474518b606be1e4fd38239"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 旋风最大打击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 旋风攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 4
    # 震动箭攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 震动箭控制时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 箭矢射程 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 旅人的直觉
# archer/traveler/d085127b0edd719782bd618d5688f4a1
# b9cb48777665de22c006fabaf9a560b3/d085127b0edd719782bd618d5688f4a1
class Skill22(ActiveSkill):
    """
        虽然旅人看起来总是拥有好运气， 但实际上靠的是旅行者特有的敏锐直觉。\n
    旅人可以通过流浪协会流传下来的独特专注法提高自身能力。\n
        自身的回避率、 暴击率、 暴击伤害增加。
    """
    name = "旅人的直觉"
    learnLv = 35
    masterLv = 10
    maxLv = 20
    position = 5 #TODO
    rangeLv = 3
    cd = 5
    mp = [417, 981]
    uuid = "d085127b0edd719782bd618d5688f4a1"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 回避率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 暴击率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 暴击伤害增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    associate = [ {"data":data3,"type":"*skillDamage"}]

# 高原雾花
# archer/traveler/42c82812f86ff6704ae9952a2e6093a4
# b9cb48777665de22c006fabaf9a560b3/42c82812f86ff6704ae9952a2e6093a4
class Skill23(ActiveSkill):
    """
        该技能可以在地面或空中施放； 空中施放时会俯冲到地面后施放。\n
        双脚蹬地跳起， 释放鞋子上的迷雾推进装置， 向前方跳跃后反向旋转， 形成雾气漩涡， 随后借力于雾气漩涡， 射出大量特制小型速射箭矢。
    """
    name = "高原雾花"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 12
    mp = [146, 865]
    uuid = "42c82812f86ff6704ae9952a2e6093a4"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 箭矢最大攻击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 箭矢攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 8
    # 技能结束后霸体持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 打击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [高原雾花]\n
        - 基本冷却时间变更为24秒\n
        总攻击力 +100%\n
        [高原雾花]施放速度 +30%
        """
        self.cd = 24
        self.skillRation *= 2

    def vp_2(self):
        """
        [高原雾花]\n
        空中落地和施放时进入无敌状态\n
        [高原雾花]攻击范围 +20%
        """
        ...

# 装置驱动
# archer/traveler/3d8f3d438405d79f8d3ed68072674d1e
# b9cb48777665de22c006fabaf9a560b3/3d8f3d438405d79f8d3ed68072674d1e
class Skill24(ActiveSkill):
    """
        该技能可在地面或空中施放。\n
        将迷雾凝聚在迷雾装置发射口前方后分离， 向前瞄准后， 发射用引火器点燃的火焰箭。\n
        冲出发射口的火焰箭被迷雾能量助燃， 燃烧得更加旺盛， 并继续向前方飞行， 击中敌人或达到最大射程时爆炸。\n
        空中施放时火焰箭接触到地面发生爆炸。\n
        被爆炸波及的敌人受到火属性伤害。
    """
    name = "装置驱动"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [183, 1081]
    uuid = "3d8f3d438405d79f8d3ed68072674d1e"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 空中施放技能结束后霸体护甲持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 爆炸范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [装置驱动]\n
        可以取消其他技能的施放后僵直并立即发动该技能， 或取消该技能的施放后僵直， 并发动其他技能\n
        (装置驱动系列及觉醒技能除外)
        """
        ...

    def vp_2(self):
        """
        [装置驱动]\n
        在[装置驱动]爆炸位置的地面生成火焰迷雾区域\n
        - 未被[装置驱动]的爆炸命中的敌人接触到火焰迷雾区域时， 将受到[装置驱动]攻击力50%的伤害\n
        - 火焰迷雾区域持续3秒， 使接触地面的敌人进入灼伤状态\n
        [装置驱动]爆炸范围 +40%
        """
        ...

# 装载 : 猛击
# archer/traveler/2f5d03c7848effbc0a23f4df45d9ca46
# b9cb48777665de22c006fabaf9a560b3/2f5d03c7848effbc0a23f4df45d9ca46
class Skill25(ActiveSkill):
    """
        该技能可以在地面和空中施放； 可以强制中断其他技能并施放该技能， 或强制中断该技能并施放其他技能。\n
        将封存猛击迷雾的燃料罐插入迷雾装置， 增加下次施放的弓术技能 (觉醒技能和部分技能除外) 的攻击力， 该效果仅适用1次。\n
        技能不在冷却时间时， 在旅人周围生成蓝色的星轨； 施放技能时， 变为红色并持续一段时间。\n
        适用技能 : [装置驱动]、 [浓雾暴雨]、 [登跃飞锚]、 [神雾兵仗·妖旋风]、 [流雾疾风]、 [装载 : 烟花漫天]、 [装置驱动·星云]
    """
    name = "装载 : 猛击"
    learnLv = 40
    masterLv = 1
    maxLv = 1
    position = 8 #TODO
    rangeLv = 3
    cd = 15
    mp = [68, 68]
    uuid = "2f5d03c7848effbc0a23f4df45d9ca46"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 弓术技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 增益效果最大持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 空中施放技能结束后霸体护甲持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 浓雾暴雨
# archer/traveler/ade01c1d6afc8a05055225045e89fe49
# b9cb48777665de22c006fabaf9a560b3/ade01c1d6afc8a05055225045e89fe49
class Skill26(ActiveSkill):
    """
        提高迷雾装置的输出功率， 向天空发射由箭矢和迷雾箭形成的箭雨。\n
        箭雨落到地面产生大量冲击波， 造成多段伤害。
    """
    name = "浓雾暴雨"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cube = 1
    cd = 18
    mp = [254, 1502]
    uuid = "ade01c1d6afc8a05055225045e89fe49"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 冲击波最大攻击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 每次冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 6
    # [范围信息]
    # 冲击波范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [浓雾暴雨]\n
        一次性发射全部箭矢\n
        [浓雾暴雨]范围 +30%
        """
        ...

    def vp_2(self):
        """
        [浓雾暴雨]\n
        可以强制中断[浓雾暴雨]施放后僵直， 并施放[细雨]\n
        箭矢降落速度 +20%\n
        [细雨]\n
        [细雨]变更为像[浓雾暴雨]一样降落
        """
        ...

# 神雾兵仗·流星
# archer/traveler/ff171dc487807bb9aa28900ca9a46b41
# b9cb48777665de22c006fabaf9a560b3/ff171dc487807bb9aa28900ca9a46b41
class Skill27(ActiveSkill):
    """
        学习后， 在玄机弓下方安装只有隶属于自由旅行者组织“流浪协会”的优秀弓箭手才能驾驭的[神雾兵仗·流星]。\n
        可以在除[高原雾花]和觉醒技能以外的旅人弓术系列技能的瞄准和射击过程中发动， 根据施放的弓术技能形态 (贯穿型、 爆炸型、 散射型) 发动蕴含星雾力量的流星箭。\n
        每个技能只能发射1次。
    """
    name = "神雾兵仗·流星"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cube = 1
    cd = 10
    mp = [109, 643]
    uuid = "ff171dc487807bb9aa28900ca9a46b41"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 储备箭数 : {value0}个
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 贯穿型和爆炸型流星箭攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 散射型流星箭最大打击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 散射型流星箭每次打击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 0
    # [范围信息]
    # 贯穿型箭矢射程 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 爆炸型冲击波范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 散射型冲击波范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    mode = ["爆炸型/贯穿型","散射型"]

    def setMode(self, mode):
        if mode == "爆炸型/贯穿型":
            self.hit1 = 1
            self.hit3 = 0
        elif mode == "散射型":
            self.hit1 = 0
            self.hit3 = 7

    def vp_1(self):
        """
        [神雾兵仗·流星]\n
        变更为可填充6次的技能\n
        - 每次填充冷却时间 : 6.6秒\n
        - 单次攻击力 -33%\n
        使用[神雾兵仗 · 流星]时， 10秒内攻击速度 +3%\n
        (学习[自动操作模式]后， 攻击速度增加量变更为2%)\n
        - 最多可叠加5次\n
        射程及冲击波范围 +25%
        """
        self.cd = 6.6
        self.skillRation *= 0.67

    def vp_2(self):
        """
        [神雾兵仗·流星]\n
        解除神雾兵仗·流星后， 发射强大的流星箭； 可单独施放\n
        - 可以在地面和空中施放\n
        - 在空中施放时， 会在落地后施放\n
        - 变更为可以适用装载 : 猛击/闪攻\n
        - 可以强制中断旅人转职技能施放后僵直并施放 (觉醒技能除外)\n
        - [流浪之星的纹章]冷却时间减少效果， 不受是否学习[自动操作模式]的影响\n
        - 基本冷却时间变更为40秒\n
        - 适用[神雾兵仗·流星]4次攻击力\n
        - 总攻击力相同\n
        - 删除填充效果
        """
        self.setMode("爆炸型/贯穿型")
        self.cd = 40
        self.skillRation *= 4

# 野外生存
# archer/traveler/547ab2b2bd860d3e37355a9cfbc1077c
# b9cb48777665de22c006fabaf9a560b3/547ab2b2bd860d3e37355a9cfbc1077c
class Skill28(PassiveSkill):
    """
        旅行并不会总是按照计划进行， 所以旅人时刻都要发挥出色的应变能力。\n
        增加基本攻击和技能攻击力， 增加自身受到的技能和消耗品的生命值、 魔法值恢复效果。\n
        此外， 在营火附近生成一个可以恢复生命值、 魔法值的野营便当。 
    """
    name = "野外生存"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 3
    uuid = "547ab2b2bd860d3e37355a9cfbc1077c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 技能和消耗品生命值、 魔法值恢复效果增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [ {"data":data0,"type":"*skillDamage"}]	

# 旷野火炎
# archer/traveler/506e7ed77d517419a6e1c437a2cedb17
# b9cb48777665de22c006fabaf9a560b3/506e7ed77d517419a6e1c437a2cedb17
class Skill29(ActiveSkill):
    """
        点燃引火器， 以迷雾装置的迷雾能量作为燃料， 发射多支火焰箭。\n
    发射时织梦者前方的敌人会被推开一段距离， 发射的箭矢在前方坠落引发连环爆炸， 造成火属性伤害并灼烧地面。\n
    接触燃烧地面的敌人会进入灼伤状态。
    """
    name = "旷野火炎"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [1420, 6378]
    uuid = "506e7ed77d517419a6e1c437a2cedb17"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 爆炸最大攻击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 每次爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 10
    # 灼烧地面持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 灼伤几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 每秒灼伤攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 4

# 装载 : 闪攻
# archer/traveler/8c2379737c5acc935c1731f67f607655
# b9cb48777665de22c006fabaf9a560b3/8c2379737c5acc935c1731f67f607655
class Skill30(PassiveSkill):
    """
        精炼猛击迷雾， 追加可以提升反应力的闪攻力量。\n
        施放[装载 : 猛击]时， 除了增加下一个弓术技能的攻击力外还能额外减少技能冷却时间。
    """
    name = "装载 : 闪攻"
    learnLv = 60
    masterLv = 1
    maxLv = 1
    position = 8 #TODO
    rangeLv = 3
    uuid = "8c2379737c5acc935c1731f67f607655"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 弓术技能冷却时间减少率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 增益最大持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 登跃飞锚
# archer/traveler/a5fa08f5d509e6ff2ebc68856a470b5a
# b9cb48777665de22c006fabaf9a560b3/a5fa08f5d509e6ff2ebc68856a470b5a
class Skill31(ActiveSkill):
    """
        该技能可在地面或空中施放。\n
        将用于安装帐篷或攀岩时使用的多功能飞锚附加到震动箭上， 驱动迷雾能量发射。\n
        箭在落地前射出飞锚， 产生冲击波， 摩擦地面猛烈旋转。\n
        在回收飞锚时拔出岩石轰击中央地面， 对范围内的敌人造成巨额伤害。   
    """
    name = "登跃飞锚"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 2 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [292, 1313]
    uuid = "a5fa08f5d509e6ff2ebc68856a470b5a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 冲击波攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 回旋最大多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 每次回旋攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 12
    # 岩石轰击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 岩石轰击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [登跃飞锚]\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 12.5秒\n
        - 单次攻击力 -50%\n
        岩石冲击爆炸范围 +30%
        """
        self.cd = 12.5
        self.skillRation *= 0.5

    def vp_2(self):
        """
        [登跃飞锚]\n
        安装反应型飞锚， 当周围存在敌人时发生爆炸\n
        - 总攻击力相同\n
        - 锚持续时间 : 10秒\n
        - 在持续时间内重新安装时， 现有的锚不会消失
        """
        ...

# 神雾兵仗·妖旋风
# archer/traveler/5dc7008b12a459325b548b0715c6b73c
# b9cb48777665de22c006fabaf9a560b3/5dc7008b12a459325b548b0715c6b73c
class Skill32(ActiveSkill):
    """
        该技能可以在地面和空中施放； 可以强制中断其他技能并施放该技能， 或强制中断该技能并施放其他技能。\n
        将自由旅行家组织“流浪协会”秘传的影雾封存到特制的“神雾兵仗·妖旋风”燃料罐中， 安装在迷雾装置上发射， 释放的妖气引发猛烈的旋风， 连同织梦者发射的箭矢席卷一切。
    """
    name = "神雾兵仗·妖旋风"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 8 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [480, 2153]
    uuid = "5dc7008b12a459325b548b0715c6b73c"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 空中施放时向后落地位置 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 箭矢最大攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 箭矢攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 10
    # 妖气旋风最大打击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 妖气旋风攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 10
    # [范围信息]
    # 旋风范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [神雾兵仗·妖旋风]\n
        在弹药筒中装入火焰的气息， 生成更大的旋风\n
        - 旋风攻击范围 +30%\n
        - 使命中的敌人进入强制控制状态3秒\n
        - 攻击时附加灼伤效果\n
        基本冷却时间变更为40秒\n
        总攻击力 -11%
        """
        self.cd = 40
        self.skillRation *= 0.89

    def vp_2(self):
        """
        [神雾兵仗·妖旋风]\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 22.5秒\n
        - 单次攻击力 -50%\n
        施放[神雾兵仗·妖旋风]后立即连接施放[绝技袭击]时， 跳跃距离和速度增加\n
        [绝技袭击]\n
        施放[神雾兵仗·妖旋风]时， 初始化[绝技袭击]的冷却时间\n
        - [绝技袭击]攻击力 -17%
        """
        self.cd = 22.5
        self.skillRation *= 0.5

    def effect(self, old, new):
        if self.vp == 2:
            self.associate = [{"type":"*skillRation","data":[0] + [-17]*self.maxLv,"skills":["绝技袭击"]}]
        return super().effect(old, new)


# 流浪之星的纹章
# archer/traveler/8ee0099656df08a0b39225f8a21d514b
# b9cb48777665de22c006fabaf9a560b3/8ee0099656df08a0b39225f8a21d514b
class Skill33(PassiveSkill):
    """
        赐予勇于探索属于自己的星星的天境之人的纹章， 持有者有权改造各种如燃料罐等设备， 为接下来的旅途做好准备。\n
        增加基本攻击力和转职技能攻击力， 进入地下城时， 自动施放[旅人的直觉]。\n
    改造[神雾兵仗·流星]， 使其能够更频繁地使用。 (学习[自动操作模式]后， 不适用冷却时间减少效果)
    """
    name = "流浪之星的纹章"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 3
    uuid = "8ee0099656df08a0b39225f8a21d514b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [神雾兵仗·流星]冷却时间减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [ {"data":data0,"type":"*skillDamage"}]

# 流雾疾风
# archer/traveler/da6e37c1e3f0e8867f70007d89c239ff
# b9cb48777665de22c006fabaf9a560b3/da6e37c1e3f0e8867f70007d89c239ff
class Skill34(ActiveSkill):
    """
        将迷雾装置功率发动到极限， 流动的高浓度迷雾能量包覆在箭矢上， 如同疾风骤雨般连续发射。\n
        在连续发射过程中按跳跃键可以中断技能。
    """
    name = "流雾疾风"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [987, 4433]
    uuid = "da6e37c1e3f0e8867f70007d89c239ff"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 最大连续发射次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 每次射击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 20

    def vp_1(self):
        """
        [流雾疾风]\n
        连续发射次数 -50%， 集中迷雾装置的能量后， 向前方顺着箭矢的方向， 额外发射最后一击\n
        - 总攻击力相同\n
        - 在连射过程中按跳跃键时， 立即发射最后一击\n
        施放时进入无敌状态
        """
        ...

    def vp_2(self):
        """
        [流雾疾风]\n
        [流雾疾风]施放速度 +35%\n
        Y轴攻击范围 +30%\n
        [神雾兵仗·流星]\n
        [流雾疾风]施放过程中可额外发射2次[神雾兵仗·流星]
        """
        ...

# 自动操作模式
# archer/traveler/47bd4871f29defc2a0021ee9261d7a5b
# b9cb48777665de22c006fabaf9a560b3/47bd4871f29defc2a0021ee9261d7a5b
class Skill35(PassiveSkill):
    """
        将[神雾兵仗·流星]的发射装置改造为自动模式。\n
        学习后， 不适用[流浪之星的纹章]的[神雾兵仗·流星]冷却时间减少效果； [神雾兵仗·流星]自动发射。 ([绝技袭击]除外)
    """
    name = "自动操作模式"
    learnLv = 75
    masterLv = 1
    maxLv = 1
    position = 3 #TODO
    rangeLv = 3
    uuid = "47bd4871f29defc2a0021ee9261d7a5b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 装载 : 烟花漫天
# archer/traveler/9bff7f2559e003766fee2853dca00631
# b9cb48777665de22c006fabaf9a560b3/9bff7f2559e003766fee2853dca00631
class Skill36(ActiveSkill):
    """
        该技能可在前方一定范围内存在敌人时施放。\n
        可以在地面和空中施放； 可以强制中断其他技能并施放该技能， 或强制中断该技能并施放其他技能。\n
        快速跳跃锁定范围内最强的敌人后， 将以旅行中看到的烟花为灵感制作的燃料罐安装在迷雾装置上， 朝着地面发射后落地。 箭在落到地面时产生华丽的烟花爆炸， 被爆炸波及的敌人受到火属性伤害。\n
        在标准高度以下施放时会跳跃到标准高度， 过于靠近目标施放时会后退并跳起。  
    """
    name = "装载 : 烟花漫天"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 8 #TODO
    rangeLv = 2
    cube = 5
    cd = 40
    mp = [1100, 4938]
    uuid = "9bff7f2559e003766fee2853dca00631"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 索敌距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 索敌宽度 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 索敌高度 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 标准高度 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 过近判断距离 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 烟花爆炸攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # [范围信息]
    # 爆炸范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [装载 : 烟花漫天]\n
        爆炸范围强化， 即使没有敌人时也可以施放， 并且可以在地面射击\n
        - 在地面施放时不会跳跃， 而是在地面朝前方射击\n
        - 在空中施放时不会追踪敌人， 而是以固定角度射击
        """
        ...

    def vp_2(self):
        """
        [装载 : 烟花漫天]\n
        施放[装载 : 烟花漫天]后， 20秒内移动速度 +15%\n
        [装置驱动]\n
        施放[装载 : 烟花漫天]时初始化[装置驱动]的冷却时间\n
        - [装置驱动]攻击力 -26.6%\n
        - [装置驱动]爆炸时追加小型烟花漫天
        """

    def effect(self, old, new):
        if self.vp == 2:
            self.associate = [{"type":"*skillRation","data":[0] + [-26.6]*self.maxLv,"skills":["装置驱动"]}]
        return super().effect(old, new)

# 神雾兵仗·北极星
# archer/traveler/a6c8f69107f8c4f5d1a0c7a57d000290
# b9cb48777665de22c006fabaf9a560b3/a6c8f69107f8c4f5d1a0c7a57d000290
class Skill37(ActiveSkill):
    """
        该技能可以在学习[神雾兵仗·流星]后施放。\n
        作为“流浪之星”， 获得开启[神雾兵仗·流星]隐藏的北极星模式的权限。\n
        迷雾装置的迷雾能量和由北极星模式增强的星雾能量在天空中融合， 形成星空极光， 在持续时间里朝着天境之人附近最强的敌人落下流星弹。\n
        极光持续时间结束或再次输入技能快捷键时极光消失， 短暂地形成银河后， 巨型流星沿着银河坠落后爆炸， 造成最后一击。\n
        没有敌人的情况下， 巨型流星会落在天境之人前方。
    """
    name = "神雾兵仗·北极星"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2396, 10757]
    uuid = "a6c8f69107f8c4f5d1a0c7a57d000290"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 极光最大持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击探索距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 探索间隔时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最大探索数量 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 每次探索落下流星弹数量 : {value4}发
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 流星弹攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 4*5
    # 巨型流星弹最后一击攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 1

# 星辰装置
# archer/traveler/3829c15bf5f520c13998a3479ba0ce7b
# b9cb48777665de22c006fabaf9a560b3/3829c15bf5f520c13998a3479ba0ce7b
class Skill38(PassiveSkill):
    """
        只有领悟到旅行的真谛的聆风·旅人， 才能通过名为“星辰装置”的星座图的指引， 施放神秘的星光之力。\n
        增加基本攻击力和转职技能攻击力， 变更部分技能效果。\n
        [绝技袭击]\n
        进入霸体状态， 可以强制中断其他技能并施放该技能， 或强制中断该技能并施放其他技能。\n
        [驱虫烈火]\n
        在火焰中加入星光的力量， 攻击范围增加， 并对敌人造成控制效果。 
    """
    name = "星辰装置"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 3
    uuid = "3829c15bf5f520c13998a3479ba0ce7b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # [驱虫烈火]范围增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [驱虫烈火]控制时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 基本攻击力和转职技能攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [ {"data":data2,"type":"*skillDamage"}]

# 装置驱动 : 星云
# archer/traveler/03bb5314ffd41e9458d67ef924fef38f
# b9cb48777665de22c006fabaf9a560b3/03bb5314ffd41e9458d67ef924fef38f
class Skill39(ActiveSkill):
    """
        该技能可在地面或空中施放。\n
        向前方跳起时， 分离迷雾装置的头部， 头部分化出更多的零件分布在四周， 同时向中央的零件发射充满了星辰装置光芒能量的箭矢。\n
        箭矢在零件之间来回穿梭， 对敌人造成攻击并控制敌人， 同时向零件传输能量， 被传输的能量经过零件强化并产生剧烈爆炸。\n
        地面施放时， 输入前方向键可以跳得更远。
    """
    name = "装置驱动 : 星云"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [1398, 6277]
    uuid = "03bb5314ffd41e9458d67ef924fef38f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 光箭攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 技能结束后无敌持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 神雾星仗·人马座星云
# archer/traveler/bb34e8854a93fd250347a1c64119f7ab
# b9cb48777665de22c006fabaf9a560b3/bb34e8854a93fd250347a1c64119f7ab
class Skill40(ActiveSkill):
    """
        该技能可以在学习[神雾兵仗·流星]后施放； 可以在地面和空中施放。\n
        释放星辰装置的力量， 将迷雾装置和[神雾兵仗·流星]融合在一起， 组成[神雾星仗·人马座星云]。\n
        从鞋子喷射出经过星辰装置增强的星雾， 强控敌人， 然后飞上天空， 完全展开[神雾星仗·人马座星云]， 向被星雾席卷的敌人中最强的敌人发射一束星光箭， 星光箭贯穿敌人， 将灿烂的星座刻在夜空中， 并引发爆炸。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与联动技能共享冷却时间。\n
        如果联动技能处于冷却时间， 则无法使用三次觉醒技能。
    """
    name = "神雾星仗·人马座星云"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [3944, 17712]
    uuid = "bb34e8854a93fd250347a1c64119f7ab"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 星光箭攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 星座爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'traveler'
        self.nameCN = '聆风·旅人'
        self.role = 'archer'
        self.角色 = '弓箭手'
        self.职业 = '旅人'
        self.jobId = 'b9cb48777665de22c006fabaf9a560b3'
        self.jobGrowId = '618326026de1a1f1cfba5dbd0b8396e7'

        self.武器选项 = ["玄机弓"] # TODO
        self.输出类型选项 = ["物理百分比"] # TODO
        self.输出类型 = "物理百分比" # TODO
        self.防具精通属性 = ["力量"] # TODO
        self.防具类型 = "皮甲"
        self.buff = 2.00 # TODO

        super().__init__(equVersion, __name__)
