#944b9aab492c15a8474f96947ceeb9e4
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "gunner_female/ranger_female/cn/skillDetail"

# 后撩踢
# gunner_female/ranger_female/717f1e2104fe4b796f800352fa143ecc
# 944b9aab492c15a8474f96947ceeb9e4/717f1e2104fe4b796f800352fa143ecc
class Skill0(ActiveSkill):
    """
        向敌人发出强威力的后撩踢并使其浮空。\n
        发动的瞬间存在霸体判定。\n
        转职为弹药专家或协战师后， 技能类型变为独立攻击力。
    """
    name = "后撩踢"
    learnLv = 1
    masterLv = 10
    maxLv = 20
    position = 5
    rangeLv = 3
    cd = 2
    uuid = "717f1e2104fe4b796f800352fa143ecc"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 发动速度增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 浮空力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 踢击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

# 浮空弹
# gunner_female/ranger_female/128b9ddef2262f40723deae4407bdb42
# 944b9aab492c15a8474f96947ceeb9e4/128b9ddef2262f40723deae4407bdb42
class Skill1(ActiveSkill):
    """
        向敌人发射1发子弹并使其浮空。\n
        转职为协战师后， 技能类型变为独立攻击力。
    """
    name = "浮空弹"
    learnLv = 1
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 3.6
    mp = [6, 140]
    uuid = "128b9ddef2262f40723deae4407bdb42"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 子弹攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 浮空力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 双枪极舞刃
# gunner_female/ranger_female/7cf17936a039b418660424125dc968d7
# 944b9aab492c15a8474f96947ceeb9e4/7cf17936a039b418660424125dc968d7
class Skill2(PassiveSkill):
    """
        在左轮枪枪口下方装备枪刃， 施展天界皇宫独有的枪斗术。\n
        枪刃的攻击力受基本攻击力的影响。\n
    - [双枪极舞刃的特有技能] -\n
    - [飞旋射击]\n
        向前方跳跃并攻击沿途的敌人。\n
    (地面状态下) 连续按C\n
        银光飞刃 : \n
    跳跃状态下快速向地面俯冲并斩击敌人。\n
    (跳跃状态下) Z\n
    - [枪刃冲击]\n
        前冲滑铲状态下起身斩击敌人。\n
    (前冲状态下) Z\n
    - [翻腾攻击]\n
        枪刃冲击及上旋踢状态下向上飞踢敌人。\n
    (枪刃冲击及[上旋踢]动作中) Z\n
        在决斗场中特有技能的攻击力和效果均有下调。
    """
    name = "双枪极舞刃"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 8
    rangeLv = 2
    uuid = "7cf17936a039b418660424125dc968d7"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 飞旋射击攻击力比率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 银光飞刃攻击力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 枪刃冲击攻击力比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 翻腾攻击攻击力比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 银光飞刃冷却时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 飞旋射击冷却时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 枪刃冲击冷却时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 翻腾攻击冷却时间 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7)

# 银弹
# gunner_female/ranger_female/a6c8f69107f8c4f5d1a0c7a57d000290
# 944b9aab492c15a8474f96947ceeb9e4/a6c8f69107f8c4f5d1a0c7a57d000290
class Skill9(ActiveSkill):
    """
        使一定数量子弹的属性变成光属性， 且命中敌人时附加光属性伤害。\n
        攻击不死族、 恶魔、 精灵类怪物时， 可以大幅度增加伤害值。
    """
    name = "银弹"
    learnLv = 5
    masterLv = 20
    maxLv = 30
    position = 7
    rangeLv = 2
    cd = 16
    mp = [60, 560]
    uuid = "a6c8f69107f8c4f5d1a0c7a57d000290"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 银弹装弹数 : {value0}发
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 附加攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 不死族、 恶魔、 精灵时的附加攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 上旋踢
# gunner_female/ranger_female/0969cd4054d93da07708108c0cc1c4b5
# 944b9aab492c15a8474f96947ceeb9e4/0969cd4054d93da07708108c0cc1c4b5
class Skill11(ActiveSkill):
    """
        向周围的敌人发出炫丽的上旋踢攻击。\n
        前冲攻击或者倒地后， 可以边发动上旋踢边站立。\n
        若学习了[花式枪术]， 施放时可以移动。\n
        转职为协战师后， 技能类型变为独立攻击力。
    """
    name = "上旋踢"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 4.5
    mp = [25, 210]
    uuid = "0969cd4054d93da07708108c0cc1c4b5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 发动速度增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 踢击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 2
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 钉刺射
# gunner_female/ranger_female/4655101518604f874721b3cc249aae10
# 944b9aab492c15a8474f96947ceeb9e4/4655101518604f874721b3cc249aae10
class Skill12(ActiveSkill):
    """
        用滑铲攻击前方敌人， 使其浮空， 并对该敌人进行追射。\n
        前方敌人倒下时， 会对周围的敌人造成伤害。\n
        可以抓取霸体和防御状态的敌人， 但对无法抓取的敌人不适用抓取和控制效果。\n
        转职为协战师时， 技能类型变为独立攻击力； 仅射击2次。
    """
    name = "钉刺射"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 0
    rangeLv = 2
    cd = 6
    mp = [30, 252]
    uuid = "4655101518604f874721b3cc249aae10"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 发射子弹数 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 射击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 7
    # 冲击波攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 0

# 炙烤
# gunner_female/ranger_female/8c2379737c5acc935c1731f67f607655
# 944b9aab492c15a8474f96947ceeb9e4/8c2379737c5acc935c1731f67f607655
class Skill13(ActiveSkill):
    """
        先向1名敌人发出强威力的后撩踢使其浮空， 然后再用格林机枪对其进行猛烈追射， 使敌人受到一定伤害。\n
        后撩踢的攻击力与当前已学的[后撩踢]攻击力相同。\n
        对无法抓取的敌人不适用控制效果， 只能造成后撩踢的攻击伤害。
    """
    name = "炙烤"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 8
    mp = [30, 322]
    uuid = "8c2379737c5acc935c1731f67f607655"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 12
    # 发射次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 浮空铲
# gunner_female/ranger_female/dcd536f1674630f01fc9667bb202b851
# 944b9aab492c15a8474f96947ceeb9e4/dcd536f1674630f01fc9667bb202b851
class Skill14(ActiveSkill):
    """
        使滑铲(前冲攻击)命中的敌人浮空。
    """
    name = "浮空铲"
    learnLv = 10
    masterLv = 1
    maxLv = 1
    position = 6
    rangeLv = 3
    cd = 8
    mp = [22, 22]
    uuid = "dcd536f1674630f01fc9667bb202b851"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 浮空力比率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

    damage = False


# 烟尘弹
# gunner_female/ranger_female/0dbdeaf846356f8b9380f8fbb8e97377
# 944b9aab492c15a8474f96947ceeb9e4/0dbdeaf846356f8b9380f8fbb8e97377
class Skill17(ActiveSkill):
    """
        向敌人脚下的地面快速连续射击， 溅起尘土， 对敌人造成伤害。 
    """
    name = "烟尘弹"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 1
    rangeLv = 2
    cd = 6
    mp = [30, 322]
    uuid = "0dbdeaf846356f8b9380f8fbb8e97377"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 连续射击攻击力 : {value0}% x {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 6
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 溃灭射击
# gunner_female/ranger_female/eb71e1d82d92c7e1d40500a0dcd77aa6
# 944b9aab492c15a8474f96947ceeb9e4/eb71e1d82d92c7e1d40500a0dcd77aa6
class Skill18(ActiveSkill):
    """
        向敌人发射一颗精准的强威力子弹， 有极高的暴击率和穿刺力。
    """
    name = "溃灭射击"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 6.2
    mp = [60, 560]
    uuid = "eb71e1d82d92c7e1d40500a0dcd77aa6"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 子弹攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2
    # 暴击增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 穿刺力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 子弹速度比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    associate = [{"type":"+dataplus0","data":data0,"skills":["心灵反击","溃灭回射"],"ratio":1}]# noqa: E501

# 刺踢
# gunner_female/ranger_female/c9664191611af31142e052dfaef84530
# 944b9aab492c15a8474f96947ceeb9e4/c9664191611af31142e052dfaef84530
class Skill19(ActiveSkill):
    """
        向前方敌人发出肉眼无法看清的快踢攻击。\n
        可以击退敌人并有一定几率使其进入眩晕状态。\n
        转职为协战师后， 技能类型变为独立攻击力。
    """
    name = "刺踢"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 4.4
    mp = [20, 224]
    uuid = "c9664191611af31142e052dfaef84530"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 踢击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 发动速度增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 击退时间比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 眩晕几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 眩晕持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 攻击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

# M-3喷火器
# gunner_female/ranger_female/8f73f243041c2d27739fe7696f02bf9b
# 944b9aab492c15a8474f96947ceeb9e4/8f73f243041c2d27739fe7696f02bf9b
class Skill20(ActiveSkill):
    """
        用M-3喷火器向敌人喷射火焰， 使敌人受到火属性伤害。 可以不受障碍物的影响进行攻击和多段打击。\n
        按住攻击键的期间， 会持续喷射火焰到持续时间结束， 放开攻击键时， 火焰也会停止。 喷射后有与喷射时间成比例的延迟。\n
        技能等级越高， 被攻击对象的僵直时间就越长。
    """
    name = "M-3喷火器"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 9
    rangeLv = 2
    cd = 7
    mp = [45, 392]
    uuid = "8f73f243041c2d27739fe7696f02bf9b"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 喷火持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 喷火攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 喷火攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 15
    # 敌人僵直时间增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 移动速度比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 左轮奥义
# gunner_female/ranger_female/d085127b0edd719782bd618d5688f4a1
# 944b9aab492c15a8474f96947ceeb9e4/d085127b0edd719782bd618d5688f4a1
class Skill21(PassiveSkill):
    """
        增加物理攻击力， 改装升级左轮枪的膛线、 弹仓和弹夹， 增加左轮枪的装弹数、 连射速度、 贯穿力、 暴击率、 攻击速度和移动速度， 并减少填装时间。
    """
    name = "左轮奥义"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 1
    rangeLv = 3
    uuid = "d085127b0edd719782bd618d5688f4a1"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 填装数增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 连射速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 贯穿率增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 暴击率增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 攻击速度增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 移动速度增加 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 填装速度增加 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    associate = [{"type":"$*PAtkP","data":data0}]

# 空中射击
# gunner_female/ranger_female/bb34e8854a93fd250347a1c64119f7ab
# 944b9aab492c15a8474f96947ceeb9e4/bb34e8854a93fd250347a1c64119f7ab
class Skill22(ActiveSkill):
    """
        增加跳跃攻击的空中停留时间以及跳跃射击的攻击力和射击次数上限， 效果持续一定时间。
    """
    name = "空中射击"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 8
    rangeLv = 3
    cd = 40
    mp = [40, 168]
    uuid = "bb34e8854a93fd250347a1c64119f7ab"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    damage = False
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 空中射击攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 增加发射子弹数上限 : 左轮枪{value2}发、 自动手枪{value3}发、 步枪{value4}发、 手炮{value5}发、 手弩{value6}发
    data2 = get_data(f'{prefix}/{uuid}', 2)
    data3 = get_data(f'{prefix}/{uuid}', 3)
    data4 = get_data(f'{prefix}/{uuid}', 4)
    data5 = get_data(f'{prefix}/{uuid}', 5)
    data6 = get_data(f'{prefix}/{uuid}', 6)

# G-14手雷
# gunner_female/ranger_female/de3fea2d65c597f4d55c70a02b97fc79
# 944b9aab492c15a8474f96947ceeb9e4/de3fea2d65c597f4d55c70a02b97fc79
class Skill23(ActiveSkill):
    """
        向前方投掷G-14手雷， 使一定范围内的所有敌人受到伤害。\n
        G-14手雷有最大填装数和填装冷却时间， 按上、 下方向键后施放技能时， 可以调整投掷位置。 转职成为弹药专家时， 可以强制中断基本攻击动作， 投掷G-14手雷。
    """
    name = "G-14手雷"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cd = 2
    mp = [20, 160]
    uuid = "de3fea2d65c597f4d55c70a02b97fc79"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 最大填装数 : {value0}发
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 地面投掷时的冷却时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 空中投掷时的冷却时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 爆炸范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 远程格挡
# gunner_female/ranger_female/2f5d03c7848effbc0a23f4df45d9ca46
# 944b9aab492c15a8474f96947ceeb9e4/2f5d03c7848effbc0a23f4df45d9ca46
class Skill24(ActiveSkill):
    """
        利用枪械进行格挡， 可以减少所受敌人远程攻击的伤害。 有一定几率可以抵挡全部伤害。
    """
    name = "远程格挡"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 3
    cd = [0, 5, 4.8, 4.5, 4.3, 4, 3.8, 3.5, 3.3, 3, 2.8, 2.5, 2.3, 2, 1.8, 1.5, 1.3, 1, 0.8, 0.5, 0.3]
    mp = [25, 235]
    uuid = "2f5d03c7848effbc0a23f4df45d9ca46"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    damage = False
    # 所受伤害减少率 (物理) : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 所受伤害减少率 (魔法) : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 所受伤害完全吸收几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def getSkillCD(self,mode=None):
        self.cd = self.cds[self.lv]
        return super().getSkillCD(mode)

# 花式枪术
# gunner_female/ranger_female/d429147c372b549c3dadcabcba50787f
# 944b9aab492c15a8474f96947ceeb9e4/d429147c372b549c3dadcabcba50787f
class Skill25(PassiveSkill):
    """
        掌握该技能后， 施放[上旋踢]时可以移动， 并且施放技能过程中可以强制中断后连接其他技能。\n
        技能强制中断有次数限制， 经过一定时间后次数限制会恢复。\n
        强制中断[上旋踢]后施放[刺踢]时， 不消耗限制次数。\n
        强制中断[刺踢]后施放[浮空弹]、 [溃灭射击]时， 不消耗限制次数。\n
        在决斗场中， 技能可强制中断次数为0。
    """
    name = "花式枪术"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 1
    rangeLv = 3
    uuid = "d429147c372b549c3dadcabcba50787f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 可强制中断次数上限 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 可强制中断次数恢复所需时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 基本攻击力和技能攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 攻击速度和移动速度增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 增益效果持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # X轴每秒移动距离 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # Y轴每秒移动距离 : {value6}px
    data6 = get_data(f'{prefix}/{uuid}', 6)
    associate = [{"data":data2}]



# 快速拔枪
# gunner_female/ranger_female/45442bbbe33540b4deeec29437dae70c
# 944b9aab492c15a8474f96947ceeb9e4/45442bbbe33540b4deeec29437dae70c
class Skill27(PassiveSkill):
    """
        快速拔枪攻击敌人， 发动后可以增加攻击速度和普通射击的攻击力。 转职为漫游枪手后增加精通等级。
    """
    name = "快速拔枪"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 7
    rangeLv = 3
    uuid = "45442bbbe33540b4deeec29437dae70c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    damage = False
    # 拔枪速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 普通射击的攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 心灵反击
# gunner_female/ranger_female/5dc7008b12a459325b548b0715c6b73c
# 944b9aab492c15a8474f96947ceeb9e4/5dc7008b12a459325b548b0715c6b73c
class Skill28(ActiveSkill):
    """
        被击时， 在一定时间内按技能键就会进行反击， 使敌人进入眩晕状态。 按住技能键时， 准备动作可以维持一定时间。\n
        [心灵反击]的攻击力相当于已掌握的[溃灭射击]攻击力。\n
        倒地、 被抓取、 无法行动等状态下， 将无法进行反击。\n
        可以中断[心灵反击]的施放并连接[溃灭射击]、 [枪舞]技能。\n
        在决斗场中无法眩晕敌人， 但是可以解除敌人的霸体状态， 且远距离击退敌人。 决斗场中也无法维持准备动作， 且无法中断[心灵反击]的施放。
    """
    name = "心灵反击"
    learnLv = 25
    masterLv = 1
    maxLv = 1
    position = 5
    rangeLv = 2
    cd = 4
    mp = [252, 252]
    uuid = "5dc7008b12a459325b548b0715c6b73c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 被攻击后发动时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 眩晕几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 眩晕持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [溃灭射击]攻击力变换率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 准备动作持续时间上限 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [决斗场]
    # 解除敌人霸体状态的几率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    dataplus0 = 0
    hitplus0 = 2
    powerplus0 = 1.7

# 锁链截击
# gunner_female/ranger_female/e1daab884dd07fc9e70d08b83d1790eb
# 944b9aab492c15a8474f96947ceeb9e4/e1daab884dd07fc9e70d08b83d1790eb
class Skill29(ActiveSkill):
    """
        使枪刃往垂直方向旋转， 并聚集周围的敌人。\n
    施放技能时， 若再次输入技能快捷键， 则可以将敌人推开； 若此时第二次输入技能键， 则可以将推开的敌人吸附到身边。
    """
    name = "锁链截击"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 1
    rangeLv = 3
    cd = 5
    mp = [50, 420]
    uuid = "e1daab884dd07fc9e70d08b83d1790eb"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 第1击多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 第1击多段攻击间隔 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 第2击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 第3击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 溃灭回射
# gunner_female/ranger_female/3d8f3d438405d79f8d3ed68072674d1e
# 944b9aab492c15a8474f96947ceeb9e4/3d8f3d438405d79f8d3ed68072674d1e
class Skill30(ActiveSkill):
    """
        快速向后方敌人施放[溃灭射击]。\n
     并增加该技能的伤害； 魔法值与当前的[溃灭射击]相同。
    """
    name = "溃灭回射"
    learnLv = 30
    masterLv = 1
    maxLv = 1
    position = 4
    rangeLv = 2
    cd = 12.5
    uuid = "3d8f3d438405d79f8d3ed68072674d1e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # [溃灭射击]攻击力强化比率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

    dataplus0 = 0
    hitplus0 = 2
    powerplus0 = 1.2

# 音速劫击
# gunner_female/ranger_female/27bade584bb42fef68148d3a0b72bace
# 944b9aab492c15a8474f96947ceeb9e4/27bade584bb42fef68148d3a0b72bace
class Skill31(ActiveSkill):
    """
        向斜上方跳跃用膝盖攻击敌人。\n
        [上旋踢]命中敌人时再次按攻击键， 可以发动[音速劫击]。\n
        被[音速劫击]命中的敌人， 会受到多段攻击伤害并向前飞出。
    """
    name = "音速劫击"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 4.4
    mp = [50, 420]
    uuid = "27bade584bb42fef68148d3a0b72bace"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 音速劫击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 攻击次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 死亡左轮
# gunner_female/ranger_female/bc11d28c04e01923a093d65752c55516
# 944b9aab492c15a8474f96947ceeb9e4/bc11d28c04e01923a093d65752c55516
class Skill32(ActiveSkill):
    """
        增加暴击伤害， 效果持续一定时间。 装备左轮枪系列武器时， 增加所有攻击的暴击率。
    """
    name = "死亡左轮"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 3
    cd = 5
    uuid = "bc11d28c04e01923a093d65752c55516"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    buff = True
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理暴击伤害增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 物理暴击率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 枪舞
# gunner_female/ranger_female/cfacda0647b9a0f595df2c2aad30c18d
# 944b9aab492c15a8474f96947ceeb9e4/cfacda0647b9a0f595df2c2aad30c18d
class Skill33(ActiveSkill):
    """
        向周围的敌人发出乱射， 挥舞枪刃攻击敌人。\n
        若施放后连续按攻击键或技能快捷键， 则可以更快地发射子弹； 若按跳跃键， 则可以中断该技能。
    """
    name = "枪舞"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cube = 1
    cd = 17.6
    mp = [150, 1260]
    uuid = "cfacda0647b9a0f595df2c2aad30c18d"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 射击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 20
    # 射击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 枪刃攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 9
    # 枪刃攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [枪舞]\n
        以最快速度攻击， 删除乱射\n
        - 总攻击力相同\n
        - 删除连续按键效果\n
        - 删除枪刃的击倒判定\n
        - [枪舞]攻击判定变更为体术系列\n
        - 枪刃攻击次数 +100%\n
        - 使枪刃命中的敌人移动到前方175px的位置\n
        [枪舞]攻击速度 +20%\n
        [枪舞]攻击范围 +30%
        """
        ...

    def vp_2(self):
        """
        [枪舞]\n
        施放[枪舞]时所受伤害 -70%\n
        施放[枪舞]时， 发动[远程格挡]效果\n
        - 每次成功用[枪舞]抵挡远程攻击时， 恢复1次[花式枪术]的使用次数 (最多3次)\n
        [枪舞]射击次数减少7次， 枪刃攻击次数减少3次\n
        - 总攻击力相同
        """
        ...

# 移动射击
# gunner_female/ranger_female/9cb6f9ed646fa87f9b7680a42ce83d1a
# 944b9aab492c15a8474f96947ceeb9e4/9cb6f9ed646fa87f9b7680a42ce83d1a
class Skill34(ActiveSkill):
    """
        施放后使自身进入移动射击模式。\n
        在此状态下按攻击键或技能键可以进行移动射击， 按方向键则可以移动。\n
        若按跳跃键， 则可以中断移动射击模式。 此外， 还可以用<Z>改变射击方向。\n
        在地下城中， 可以使子弹破裂， 造成大范围的伤害。\n
        在决斗场中， 移动射击时不会进入霸体状态。
    """
    name = "移动射击"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cube = 1
    cd = 24.3
    mp = [200, 1680]
    uuid = "9cb6f9ed646fa87f9b7680a42ce83d1a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 移动速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 射击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 45
    # 持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 射击发射数 : {value3}发
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 破裂子弹范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [移动射击]\n
        将子弹转化为爆破弹， 增加攻击范围\n
        - 发射次数 +50%\n
        - 总攻击力相同\n
        - 攻击范围 +30%\n
        施放过程中攻击速度 +30%、 移动速度 +50%\n
        切换地下城房间时， 保留技能效果
        """
        ...

    def vp_2(self):
        """
        [移动射击]\n
        减少发射次数， 移动射击过程中所受伤害减少\n
        - 发射次数 -40%\n
        - 总攻击力相同\n
        攻击范围 +20%\n
        移动射击施放过程中所受伤害 -50%
        """
        ...

# 多重射击
# gunner_female/ranger_female/669f1428193f61f9d92c743b72438c4d
# 944b9aab492c15a8474f96947ceeb9e4/669f1428193f61f9d92c743b72438c4d
class Skill35(ActiveSkill):
    """
        向一定范围内的敌人连续射击， 使命中的敌人受到极大伤害。\n
        每次发射可以用方向键控制发射方向， 并给该方向的多个敌人造成伤害。
    """
    name = "多重射击"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 1
    cd = 19.8
    mp = [150, 1260]
    uuid = "669f1428193f61f9d92c743b72438c4d"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 发射次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 射击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 5
    # 敌人僵直时间比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 锁定范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [多重射击]\n
        按技能键时， 自动向范围内最强敌人所在方向射击， 并对范围内所有敌人造成伤害\n
         - 删除输入方向键功能\n
        可以分多次射击\n
         - 首次射击后20秒内可以追加射击\n
        与其他技能连接施放时不会消耗[花式枪术]的使用次数\n
        射击过程中可以接住[双鹰回旋]\n
        攻击范围 +40%
        """
        ...

    def vp_2(self):
        """
        [多重射击]\n
        射击时最多可以输入两个方向键进行射击\n
        - 输入两个方向键时， 同时射击两个方向\n
        - 射击攻击次数 -2次\n
        - 总攻击力相同
        """
        ...

# 双鹰回旋
# gunner_female/ranger_female/1fadde0eece18649caddbca7bd58cc2f
# 944b9aab492c15a8474f96947ceeb9e4/1fadde0eece18649caddbca7bd58cc2f
class Skill36(ActiveSkill):
    """
        旋转并向前方敌人投掷漫游枪手专用手枪， 手枪会自动发射子弹并对周围敌人造成伤害。\n
        在一定距离内， 投掷的手枪会自动飞回， 这时漫游枪手抓取手枪成功后可以再次投掷。\n
        可抓取飞回的手枪的状态 : [站立时； 移动/前冲时； 普通攻击时； 站立状态下受到伤害时]\n
        在地下城中， 将枪刃附在手枪上， 可以将更大范围内的敌人拖到射击中心。\n
        在决斗场中抓取手枪后， 不会进入霸体状态。
    """
    name = "双鹰回旋"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cube = 2
    cd = 44.5
    mp = [360, 3024]
    uuid = "1fadde0eece18649caddbca7bd58cc2f"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 第1次鹰枪攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 14
    # 第2次鹰枪攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 18
    # 第3次鹰枪攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 32
    # [范围信息]
    # 鹰枪大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [双鹰回旋]\n
        投掷次数 -1次\n
        - 从第2次攻击开始投掷\n
        - 手枪持续时间 +30%\n
        - 多段攻击间隔 -20%\n
        - 总攻击力相同\n
        [双鹰回旋]手枪大小 +25%\n
        [双鹰回旋]吸附范围 +25%\n
        再次投掷手枪时， 可施放体术系列技能并自动投掷\n
        - 消耗1次[花式枪术]的使用次数\n
        - [后撩踢]、 [上旋踢]、 [刺踢]、 [锁链截击]、 [音速劫击]、 [回闪劫击]、 [死亡锁链]投掷时、 [锁链切割]、 [毁灭风暴]、 [盛放·绯红花园]
        """
        ...

    def vp_2(self):
        """
        [双鹰回旋]\n
        施放时， 最多投掷3次鹰枪\n
        - 向前方600px内最强敌人投掷\n
        - 范围内没有追踪目标时， 会根据方向键输入的方向进行投掷\n
        第3次鹰枪的部分功能变更\n
        - 投掷范围增加\n
        - 造成两次伤害后不会返回\n
        - 总攻击力相同\n
        鹰枪自动回收， 无需回收动作\n
        - 回收后5秒内可再次投掷\n
        再次投掷鹰枪时， 可通过施放体术系列技能进行投掷\n
        - 消耗1次[花式枪术]使用次数\n
        - [后撩踢]、 [上旋踢]、 [刺踢]、 [锁链截击]、 [音速劫击]、 [回闪劫击]、 [死亡锁链]投掷时、 [锁链切割]、 [毁灭风暴]、 [盛放·绯红花园]
        """
        ...

# 隐匿切割
# gunner_female/ranger_female/fc458e449ee00b01dbf88d09aae65462
# 944b9aab492c15a8474f96947ceeb9e4/fc458e449ee00b01dbf88d09aae65462
class Skill37(PassiveSkill):
    """
        增加基本攻击和射击技能攻击力。 使用部分体术系技能时， 施加额外的斩击使敌人进入出血状态。\n
    [增加射击攻击力的技能]\n
    - [浮空弹]、 [钉刺射]、 [烟尘弹]、 [溃灭射击]、 [溃灭回射]、 [心灵反击]、 [锁链截击] (射击)、 [音速劫击]、  [枪舞]、 [移动射击]、 [多重射击]、 [双鹰回旋]、 [压制射击]、 [死亡锁链]、 [血舞祭]、 [毁灭风暴] (射击)、 [盛放·绯红花园] (射击)\n
    [发动隐匿切割的技能]\n
    - [后撩踢]、 [浮空铲]、 [上旋踢]、 [刺踢]、 [锁链截击] (体术)、 [音速劫击] (体术)、 [绯红盛宴]、 [回闪劫击]、 [死亡锁链]、 [锁链切割]、 [毁灭风暴] (射击)、 [盛放·绯红花园] (射击)
    """
    name = "隐匿切割"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 3
    uuid = "fc458e449ee00b01dbf88d09aae65462"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和射击技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 发动[隐匿切割]时追加攻击力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 出血几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 出血持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 出血攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    associate = [{"data":data0}]

# 绯红盛宴
# gunner_female/ranger_female/374f53e8989ef04a8506c8ec99d9ecdc
# 944b9aab492c15a8474f96947ceeb9e4/374f53e8989ef04a8506c8ec99d9ecdc
class Skill38(ActiveSkill):
    """
        使用枪刃向前方发动刀刃攻击。\n
        按向前方向键， 可以增加最后一击前近距离。
    """
    name = "绯红盛宴"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [1000, 8400]
    uuid = "374f53e8989ef04a8506c8ec99d9ecdc"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 向前斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 25
    # 向前斩击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

# 回闪劫击
# gunner_female/ranger_female/7f80b887a09e88e2c4728c898bd73654
# 944b9aab492c15a8474f96947ceeb9e4/7f80b887a09e88e2c4728c898bd73654
class Skill39(ActiveSkill):
    """
        枪刃指向前方， 向斜上方跳跃攻击敌人。\n
        若跳跃过程中再次按技能快捷键， 则施放[新月斩击]攻击敌人后落地。\n
        在空中和[上旋踢]施放过程中也可以发动该技能。
    """
    name = "回闪劫击"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 2
    cd = 25
    mp = [400, 1120]
    uuid = "7f80b887a09e88e2c4728c898bd73654"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 上升攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [新月斩击]攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [回闪劫击]\n
        施放时向前方突进\n
        - 无法在空中施放\n
        - 移除新月斩击\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 12.5秒\n
        - 每次攻击力 -50%\n
        在施放鲜血之跃过程中按反方向键并施放技能时， 可以消耗花式枪术进行逆向连接施放
        """
        ...

    def vp_2(self):
        """
        [回闪劫击]\n
        固定连接新月斩击\n
        - 施放时进入无敌状态\n
        - 删除追加输入功能\n
        施放时， 10秒内攻击速度、 移动速度和回避率 +10%
        """
        ...

# 压制射击
# gunner_female/ranger_female/0fbb8de70002ad34f046c94c2cb3e863
# 944b9aab492c15a8474f96947ceeb9e4/0fbb8de70002ad34f046c94c2cb3e863
class Skill40(ActiveSkill):
    """
        向前方发射子弹。\n
    按攻击键或技能快捷键时， 可用更快的速度发射子弹。\n
        射击时，  按跳跃键可以强制中断技能。
    """
    name = "压制射击"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 3
    cd = 50
    mp = [800, 1680]
    uuid = "0fbb8de70002ad34f046c94c2cb3e863"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 前方乱射攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 20
    # 前方乱射攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后射击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [压制射击]\n
        射击时舞动枪刃发动10次追加攻击\n
        - 基本冷却时间变更为65秒\n
        - 总攻击力 +30%\n
        - 使枪刃命中的敌人移动到前方150px的位置
        """
        ...

    def vp_2(self):
        """
        [压制射击]\n
        固定以最快速度进行乱射攻击\n
        - 删除连续按键效果\n
        - 删除最后射击\n
        - 总攻击力相同
        """
        ...

# 枪刃改良
# gunner_female/ranger_female/b501ae53638d33a32351904f31cb6aa3
# 944b9aab492c15a8474f96947ceeb9e4/b501ae53638d33a32351904f31cb6aa3
class Skill41(PassiveSkill):
    """
        在枪刃上附上锯齿， 给予敌人更加致命的打击。\n
        学习该技能后， 增加出血状态的持续时间， 并增加基本攻击力和技能攻击力。
    """
    name = "枪刃改良"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 3
    uuid = "b501ae53638d33a32351904f31cb6aa3"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 出血持续时间增加 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"data":data0}]

# 死亡锁链
# gunner_female/ranger_female/8ec9da6f808889b63adf2680fbf1f331
# 944b9aab492c15a8474f96947ceeb9e4/8ec9da6f808889b63adf2680fbf1f331
class Skill42(ActiveSkill):
    """
        向前方投掷锁链枪刃， 将击中的敌人锁住。\n
        技能持续时间内， 再次按技能键， 可以快速射击锁住的敌人中最强的敌人。\n
        若持续时间内没有再次按技能键， 则不发动射击。
    """
    name = "死亡锁链"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "8ec9da6f808889b63adf2680fbf1f331"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 投掷锁链枪刃数量上限 : {value0}个
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 锁住敌人的持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 快速射击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 5
    # 快速射击多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 最终射击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # 无法锁住的敌人移动速度减少率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 投掷距离比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [死亡锁链]\n
        投掷枪刃的同时进行射击\n
        - 投掷范围内存在敌人时才能施放\n
        - 枪刃无关射击， 禁锢敌人\n
        - 枪刃禁锢敌人时间 -1秒\n
        - 枪刃固定敌人过程中， 再次按技能键时， 解除枪刃\n
        枪刃投掷数量上限 +4个\n
        投掷范围 +30%
        """
        ...

    def vp_2(self):
        """
        [死亡锁链]\n
        将枪刃拿在手中向前突进攻击\n
        - 突进施放过程中进入无敌状态\n
        - 突进命中时给敌人附着枪刃\n
        - 突进时按向前方向键可以增加突进距离\n
        - 枪刃禁锢敌人时间 +3秒\n
        突进施放过程中按相反方向键并施放技能时， 可以消耗[花式枪术]反方向连接施放\n
        可以对附着枪刃的目标发动原[死亡锁链]的射击\n
        - 射击过程中进入无敌状态
        """
        ...

# 锁链切割
# gunner_female/ranger_female/0c262dac3ec41ff79e359ada9c7a7faf
# 944b9aab492c15a8474f96947ceeb9e4/0c262dac3ec41ff79e359ada9c7a7faf
class Skill43(ActiveSkill):
    """
        向前方大范围挥舞2次枪刃， 将敌人拉过来之后再次强力挥割敌人。
    """
    name = "锁链切割"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 1
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 8000]
    uuid = "0c262dac3ec41ff79e359ada9c7a7faf"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
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
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [锁链切割]\n
        每次挥动锁链时， 生成刀刃风暴， 攻击更大范围\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 22.5秒\n
        - 单次攻击力 -50%\n
        命中时， 将敌人吸附至前方150px位置
        """
        self.cd = 22.5
        self.skillRation *= 1 - 0.5
        ...

    def vp_2(self):
        """
        [锁链切割]\n
        施放技能时， 发动锁链切割终结攻击\n
        终结攻击命中时， 在对方身上留下10秒的玫瑰印记\n
        - 玫瑰印记会随着漫游枪手的攻击成长， 达到最大阶段时爆炸\n
        - 每10次攻击会强化至下一阶段 (最多3阶段)\n
        - 爆炸时仅对附着的目标造成爆炸伤害\n
        - 总攻击力相同\n
        - 爆炸时恢复[花式枪术]使用次数最大值\n
        (每次施放仅发动1次)
        """
        ...

# 血舞祭
# gunner_female/ranger_female/3af805da8505fe6234a95b535610f064
# 944b9aab492c15a8474f96947ceeb9e4/3af805da8505fe6234a95b535610f064
class Skill44(ActiveSkill):
    """
        向周围投掷多把枪刃向前突进， 同时将大范围的敌人聚集到一起给予毁灭性的强力射击。
    """
    name = "血舞祭"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 8000]
    uuid = "3af805da8505fe6234a95b535610f064"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 射击攻击力 : {value0}% 
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1

# 锁链意志
# gunner_female/ranger_female/6166762c62f234c5f50c2d2ebc5e48d0
# 944b9aab492c15a8474f96947ceeb9e4/6166762c62f234c5f50c2d2ebc5e48d0
class Skill45(PassiveSkill):
    """
        进一步强化体术和射击术， 增加基本攻击力和除[音速劫击]以外的转职技能攻击力， 并增加[花式枪术]可强制中断次数上限。\n
        更有效率地运用射击与体术相结合的连接攻击， [锁链截击]和[音速劫击]获得附加效果。\n
    [锁链截击]\n
        删除第1击多段攻击； 施放时， 第2击和第3击攻击后， 向前方射击。\n
        射击攻击力以[锁链截击]第1击多段攻击力的一定比率适用。\n
    [音速劫击]\n
        突进攻击时不跳到空中， 突进攻击后回头射击。\n
        射击攻击力以[音速劫击]物理攻击力的一定比率适用。
    """
    name = "锁链意志"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "6166762c62f234c5f50c2d2ebc5e48d0"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和转职技能攻击力增加率 ([音速劫击]除外) : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [锁链截击]
    # 射击攻击力 : [锁链截击]第1击多段攻击力的{value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [音速劫击]
    # 射击攻击力 : [音速劫击]攻击力的{value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [花式枪术]
    # 可强制中断次数上限增加量 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    associate = [{"data":data0}]

# 毁灭风暴
# gunner_female/ranger_female/d59c9840f65381bde8487757f1753c71
# 944b9aab492c15a8474f96947ceeb9e4/d59c9840f65381bde8487757f1753c71
class Skill46(ActiveSkill):
    """
        连接枪刃斩击和射击， 对周围敌人造成强力伤害。\n
        使用枪刃大范围快速斩击4次后， 第5次斩击的同时， 发动强力终结射击。 终结射击时， 枪刃和锁链散成碎片， 对周围额外造成伤害。\n
        施放过程中， 连按攻击键或技能快捷键， 可以加快斩击速度。\n
        斩击过程中， 按跳跃键可以中断攻击。
    """
    name = "毁灭风暴"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [960, 9600]
    uuid = "d59c9840f65381bde8487757f1753c71"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 第1次斩击攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 第2次斩击攻击力 : {value2}% X {value3}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 3
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 第3次斩击攻击力 : {value4}% X {value5}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 3
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 第4次斩击攻击力 : {value6}% X {value7}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 3
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 第5次斩击攻击力 : {value8}% X {value9}
    data8 = get_data(f'{prefix}/{uuid}', 8)
    hit8 = 3
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 终结射击攻击力 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    hit10 = 1
    # 枪刃和锁链碎片攻击力 : {value11}% X {value12}
    data11 = get_data(f'{prefix}/{uuid}', 11)
    hit11 = 5
    data12 = get_data(f'{prefix}/{uuid}', 12)

# 盛放·绯红花园
# gunner_female/ranger_female/bbc15561bec24f9c1e79e23d715b1dd2
# 944b9aab492c15a8474f96947ceeb9e4/bbc15561bec24f9c1e79e23d715b1dd2
class Skill47(ActiveSkill):
    """
        施放时， 向四面八方投掷枪刃， 用锁链编织成绯红花园， 歼灭所有敌人。\n
        绯红花园完成后， 发动体术和射击连接攻击， 在强大的攻击下， 固定的锁链开始断裂。\n
        连接攻击过程中， 枪刃结合点变得不稳定， 此时切断所有锁链， 使用枪刃发动终结斩击。\n
        施放[盛放·绯红花园]过程中， 无法使用[花式枪术]强制中断。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "盛放·绯红花园"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 9667]
    uuid = "bbc15561bec24f9c1e79e23d715b1dd2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 锁链编织攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 枪刃乱舞攻击力 : {value2}% X {value3}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 6
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 射击攻击力 : {value4}% X {value5}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 7
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 枪刃发射攻击力 : {value6}% X {value7}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 6
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 枪刃旋转攻击力 : {value8}% X {value9}
    data8 = get_data(f'{prefix}/{uuid}', 8)
    hit8 = 13
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 终结斩击攻击力 : {value10}% X {value11}
    data10 = get_data(f'{prefix}/{uuid}', 10)
    hit10 = 3
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 锁链碎片攻击力 : {value12}% X {value13}
    data12 = get_data(f'{prefix}/{uuid}', 12)
    hit12 = 6
    data13 = get_data(f'{prefix}/{uuid}', 13)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'ranger_female'
        self.nameCN = '重霄·漫游枪手'
        self.role = 'gunner_female'
        self.角色 = '神枪手(女)'
        self.职业 = '漫游枪手'
        self.jobId = '944b9aab492c15a8474f96947ceeb9e4'
        self.jobGrowId = '37495b941da3b1661bc900e68ef3b2c6'

        self.武器选项 = ['手弩', '步枪','左轮枪','自动手枪','手炮']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '皮甲'
        self.buff = 2.335

        super().__init__(equVersion, __name__)
