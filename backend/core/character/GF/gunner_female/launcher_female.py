#944b9aab492c15a8474f96947ceeb9e4
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "gunner_female/launcher_female/cn/skillDetail"


# M-137格林机枪
# gunner_female/launcher_female/01c3a2fb793d293a25ed8dc7a0d70c1a
# 944b9aab492c15a8474f96947ceeb9e4/01c3a2fb793d293a25ed8dc7a0d70c1a
class Skill6(ActiveSkill):
    """
        使用M-137格林机枪攻击敌人。 若连按攻击键可以延长发射时间， 但按跳跃键或达到发射时间上限， 则会停止发射。\n
        若发射中按住向上方向键， 则可以向上发射。
    """
    name = "M-137格林机枪"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 5
    mp = [10, 180]
    uuid = "01c3a2fb793d293a25ed8dc7a0d70c1a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 取出机枪所用时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 发射攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 30
    # 每秒发射次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 发射次数上限 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 穿刺几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)


# 重火器拔击
# gunner_female/launcher_female/1dad88963abdc96b091fcab185a8820d
# 944b9aab492c15a8474f96947ceeb9e4/1dad88963abdc96b091fcab185a8820d
class Skill9(ActiveSkill):
    """
        使重火器的拔出动作出现攻击判定， 命中敌人后可以将敌人击退。
    """
    name = "重火器拔击"
    learnLv = 5
    masterLv = 1
    maxLv = 11
    position = 3
    rangeLv = 3
    uuid = "1dad88963abdc96b091fcab185a8820d"
    type = "passive"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 敌人僵直时间增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)


# 炙烤
# gunner_female/launcher_female/8c2379737c5acc935c1731f67f607655
# 944b9aab492c15a8474f96947ceeb9e4/8c2379737c5acc935c1731f67f607655
class Skill12(ActiveSkill):
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
# gunner_female/launcher_female/dcd536f1674630f01fc9667bb202b851
# 944b9aab492c15a8474f96947ceeb9e4/dcd536f1674630f01fc9667bb202b851
class Skill13(ActiveSkill):
    """
        使滑铲(前冲攻击)命中的敌人浮空。
    """
    name = "浮空铲"
    learnLv = 10
    masterLv = 1
    maxLv = 1
    position = 8
    rangeLv = 3
    cd = 8
    mp = [22, 22]
    uuid = "dcd536f1674630f01fc9667bb202b851"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 浮空力比率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)


# M-3喷火器
# gunner_female/launcher_female/8f73f243041c2d27739fe7696f02bf9b
# 944b9aab492c15a8474f96947ceeb9e4/8f73f243041c2d27739fe7696f02bf9b
class Skill18(ActiveSkill):
    """
        用M-3喷火器向敌人喷射火焰， 使敌人受到火属性伤害。 可以不受障碍物的影响进行攻击和多段打击。\n
        按住攻击键的期间， 会持续喷射火焰到持续时间结束， 放开攻击键时， 火焰也会停止。 喷射后有与喷射时间成比例的延迟。\n
        技能等级越高， 被攻击对象的僵直时间就越长。
    """
    name = "M-3喷火器"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 3
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
    hit2 = 8
    # 敌人僵直时间增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 移动速度比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 重火器精通
# gunner_female/launcher_female/ade01c1d6afc8a05055225045e89fe49
# 944b9aab492c15a8474f96947ceeb9e4/ade01c1d6afc8a05055225045e89fe49
class Skill19(PassiveSkill):
    """
        减少所有重火器技能的魔法值消耗， 增加手炮系列武器的拔出速度和攻击力， 增加重火器技能的攻击力。\n
        并减少除[远古粒子炮]、 [火力全开]、 [制胜 · 最终兵器]外的其他技能的冷却时间。
    """
    name = "重火器精通"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 1
    rangeLv = 3
    uuid = "ade01c1d6afc8a05055225045e89fe49"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 重火器技能魔法值减少比率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 手炮拔出速度增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 重火器技能攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 技能冷却时间减少率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    associate = [
        {"type":"$*PAtkP","data":data2},
        {"data":data3},
        {"type":"*cdReduce","data":data4,"exceptSkills":['远古粒子炮', '火力全开', '制胜·最终兵器']},
    ]


# 重火器奥义
# gunner_female/launcher_female/e49e57b2e8fbeceb0a2c56a0c63fe6c5
# 944b9aab492c15a8474f96947ceeb9e4/e49e57b2e8fbeceb0a2c56a0c63fe6c5
class Skill21(PassiveSkill):
    """
        领悟重火器奥义， 使除了1、 2、 3次觉醒技能之外的所有重火器技能各增加1级。
    """
    name = "重火器奥义"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 0
    rangeLv = 1
    uuid = "e49e57b2e8fbeceb0a2c56a0c63fe6c5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    def effect(self, old, new):
        skills = []
        for i in self.char.skills:
            if i.type == "active" and i.learnLv not in [50,85,100] and i.damage and i.lv > 0:
                skills.append(i.name)
        self.associate = [{"type":"+lv","data":[0] + [1]*self.maxLv,"ratio":1,"skills":skills}]
        super().effect(old, new)

# G-14手雷
# gunner_female/launcher_female/de3fea2d65c597f4d55c70a02b97fc79
# 944b9aab492c15a8474f96947ceeb9e4/de3fea2d65c597f4d55c70a02b97fc79
class Skill22(ActiveSkill):
    """
        向前方投掷G-14手雷， 使一定范围内的所有敌人受到伤害。\n
        G-14手雷有最大填装数和填装冷却时间， 按上、 下方向键后施放技能时， 可以调整投掷位置。 转职成为弹药专家时， 可以强制中断基本攻击动作， 投掷G-14手雷。
    """
    name = "G-14手雷"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 10
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

# 反坦克炮
# gunner_female/launcher_female/0ed3148658fe37b3336ccb718dc0fdb0
# 944b9aab492c15a8474f96947ceeb9e4/0ed3148658fe37b3336ccb718dc0fdb0
class Skill23(ActiveSkill):
    """
        向前方敌人发射一颗可以爆炸的炮弹。
    """
    name = "反坦克炮"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 6
    mp = [40, 391]
    uuid = "0ed3148658fe37b3336ccb718dc0fdb0"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 3
    # 拔出武器需要的时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 爆炸次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 爆炸大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 加农炮
# gunner_female/launcher_female/8510294202d0e042dd29a2422fc6770d
# 944b9aab492c15a8474f96947ceeb9e4/8510294202d0e042dd29a2422fc6770d
class Skill24(ActiveSkill):
    """
        施放后向敌人发射强威力的能量球并给予敌人无属性物理伤害， 且飞行一定距离后会爆炸。\n
        发射时有霸体判定， 且可以按上下方向键控制发射方向。\n
        若达最大蓄气后未及时发射， 则经过一定时间后将自动发射能量球。\n
    - [学习重武装改造后变更效果] -\n
        增加能量球飞行距离， 且命中敌人时立即爆炸。 同时， 冲撞伤害与爆炸伤害合并。
    """
    name = "加农炮"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 5
    mp = [30, 280]
    uuid = "8510294202d0e042dd29a2422fc6770d"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2
    # 最大蓄气后自动发射时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 射程 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 缓冲时爆炸范围扩大率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)


# 快速拔枪
# gunner_female/launcher_female/45442bbbe33540b4deeec29437dae70c
# 944b9aab492c15a8474f96947ceeb9e4/45442bbbe33540b4deeec29437dae70c
class Skill26(PassiveSkill):
    """
        快速拔枪攻击敌人， 发动后可以增加攻击速度和普通射击的攻击力。 转职为漫游枪手后增加精通等级。
    """
    name = "快速拔枪"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 0
    rangeLv = 3
    uuid = "45442bbbe33540b4deeec29437dae70c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 拔枪速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 普通射击的攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 激光炮
# gunner_female/launcher_female/23a5e0fba03283cb1b324a847b3fe370
# 944b9aab492c15a8474f96947ceeb9e4/23a5e0fba03283cb1b324a847b3fe370
class Skill27(ActiveSkill):
    """
        向敌人发射激光， 使敌人受到光属性伤害； 激光的攻击范围比较狭小， 但是射程极远。
    """
    name = "激光炮"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cd = 7
    mp = [61, 512]
    uuid = "23a5e0fba03283cb1b324a847b3fe370"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 射程 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 蓄电激光炮
# gunner_female/launcher_female/01384bbfc346775d1267fa0bc4ca605f
# 944b9aab492c15a8474f96947ceeb9e4/01384bbfc346775d1267fa0bc4ca605f
class Skill28(PassiveSkill):
    """
        使用[激光炮]时， 按住攻击键进行充电后可向敌人发射更强威力的激光。\n
        激光的攻击力随充电时间增加， 达到最大充电值时， 可以增加攻击范围和射程， 但会有很大的后坐力。
    """
    name = "蓄电激光炮"
    learnLv = 25
    masterLv = 1
    maxLv = 11
    position = 8
    rangeLv = 2
    uuid = "01384bbfc346775d1267fa0bc4ca605f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 充电时间上限 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"data":data1,"skills":["激光炮"]}]

# 脉冲雷达-63
# gunner_female/launcher_female/9376d04c476cd41d60ed1974ca69ab95
# 944b9aab492c15a8474f96947ceeb9e4/9376d04c476cd41d60ed1974ca69ab95
class Skill29(PassiveSkill):
    """
        装备重火器雷达部件， 增加物理暴击率和物理攻击力。
    """
    name = "脉冲雷达-63"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 1
    rangeLv = 3
    uuid = "9376d04c476cd41d60ed1974ca69ab95"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 物理暴击率增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"data":data1,"type":"$*PAtkP"}]

# 聚焦喷火器
# gunner_female/launcher_female/04883563896fe1adac7505c6146b5f59
# 944b9aab492c15a8474f96947ceeb9e4/04883563896fe1adac7505c6146b5f59
class Skill30(ActiveSkill):
    """
        用聚焦喷火器向前方敌人喷射火焰， 使敌人受到火属性伤害。\n
        喷射中可以移动。
    """
    name = "聚焦喷火器"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 12
    mp = [130, 980]
    uuid = "04883563896fe1adac7505c6146b5f59"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 29
    # 攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 移动速度比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 潜能爆发
# gunner_female/launcher_female/1721e94897e9961d5c98130a13392f17
# 944b9aab492c15a8474f96947ceeb9e4/1721e94897e9961d5c98130a13392f17
class Skill31(ActiveSkill):
    """
        增加基本攻击力以及所有重火器技能的命中率和攻击力， 并使远距离的敌人无法判定枪炮师的位置， 效果持续一定时间。
    """
    name = "潜能爆发"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 5
    rangeLv = 3
    cd = 5
    uuid = "1721e94897e9961d5c98130a13392f17"
    hasVP = False
    hasUP = False
    buff = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 重火器命中率增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 基本攻击和重火器攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# FM-31榴弹发射器
# gunner_female/launcher_female/762c4e6d030eaf0abbfe1fec2b298574
# 944b9aab492c15a8474f96947ceeb9e4/762c4e6d030eaf0abbfe1fec2b298574
class Skill32(ActiveSkill):
    """
        使用榴弹发射器快速发射榴弹。\n
        榴弹命中敌人时， 会引起爆炸并使周围敌人受到伤害。
    """
    name = "FM-31榴弹发射器"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 15
    mp = [50, 630]
    uuid = "762c4e6d030eaf0abbfe1fec2b298574"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 发射榴弹数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 榴弹攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 8
    # [范围信息]
    # 攻击范围扩大率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [FM-31榴弹发射器]\n
        变更为每次发射1发榴弹\n
         - 长按技能键可以连续发射\n
        可持有的榴弹数量 +1个\n
         - 每次填充冷却时间 : 3秒\n
         - 总攻击力相同\n
        除部分技能外， 可以在重火器发射僵直过程中立即发射榴弹\n
         - 榴弹发射后僵直减少\n
        [除外目标技能]\n
         - [M-137格林机枪]、 [M-3喷火器]、 [聚焦喷火器]、 [远古粒子炮]、 [火力全开]、 [制胜·最终兵器]
        """
        ...

    def vp_2(self):
        """
        [FM-31榴弹发射器]\n
        在发射榴弹时， 可以向上、 下方向发射\n
         - 爆炸范围 +30%\n
         - 发射间隔 -20%
        """
        ...

# FM-92榴弹
# gunner_female/launcher_female/38612d8f2561edc2eb68d5057a837bfa
# 944b9aab492c15a8474f96947ceeb9e4/38612d8f2561edc2eb68d5057a837bfa
class Skill33(ActiveSkill):
    """
        向空中发射榴弹， 榴弹在空中分离后会形成多个爆弹掉落地面并爆炸， 可以使爆炸范围内的敌人受到火属性物理伤害。\n
        若经过一定时间或松开技能键， 则榴弹会自动分离成小爆弹。\n
    [学习重武装改造后变更效果]\n
        在地面施放重火器系列技能时可以同时使用该技能。 减少40%的攻击力和冷却时间， 变更为最多可施放2次再进行冷却的技能。
    """
    name = "FM-92榴弹"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [164, 1376]
    uuid = "38612d8f2561edc2eb68d5057a837bfa"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆弹攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 8
    # 爆弹攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最短飞行时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最长飞行时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 爆炸大小扩大率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [FM-92榴弹]\n
        删除学习[重武装改造]后变更效果\n
         - 删除填充功能\n
         - 使用其他重火器技能过程中无法发射\n
        直接从正面发射榴弹\n
         - 删除长按技能键操作\n
         - 榴弹接触敌人或飞行一定距离后立即爆炸， 攻击更大范围
        """
        ...

    def vp_2(self):
        """
        [FM-92榴弹]\n
        无法直接施放\n
        使用重火器技能攻击敌人时， 自动发射攻击周围敌人\n
         - 自动发射冷却时间 : 0.5秒\n
        填充数量上限增加\n
         - 填充数量上限 +4个\n
         - 每次填充冷却时间 : 4秒\n
         - 总攻击力相同
        """
        ...

# 光热反应
# gunner_female/launcher_female/33ad4930f4724a7d025c3046c6f6074b
# 944b9aab492c15a8474f96947ceeb9e4/33ad4930f4724a7d025c3046c6f6074b
class Skill34(PassiveSkill):
    """
        将光、 火属性值中较低的属性值补正为较高的属性值。
    """
    name = "光热反应"
    learnLv = 35
    masterLv = 1
    maxLv = 1
    position = 4
    rangeLv = 3
    uuid = "33ad4930f4724a7d025c3046c6f6074b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

# 量子爆弹
# gunner_female/launcher_female/e4c354a89c337310aeb7041d5e742828
# 944b9aab492c15a8474f96947ceeb9e4/e4c354a89c337310aeb7041d5e742828
class Skill35(ActiveSkill):
    """
        向敌人投放光属性量子爆弹， 使周围敌人受到光属性伤害并有一定几率使敌人进入感电状态， 可以通过方向键控制投放位置。
    """
    name = "量子爆弹"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 9
    rangeLv = 2
    cube = 1
    cd = 18
    mp = [164, 1376]
    uuid = "e4c354a89c337310aeb7041d5e742828"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 导弹攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 感电几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 感电持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 感电攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # [范围信息]
    # 爆炸领域 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [量子爆弹]\n
        变更为地毯式轰炸\n
         - 无法指定投放位置\n
         - 删除导弹碰撞攻击力\n
         - 导弹大小 -50%\n
         - 可以在其他重火器施放过程中请求轰炸\n
        爆炸次数 +7次\n
         - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [量子爆弹]\n
        炸弹落地时不会立即爆炸， 而是在地面停留60秒\n
         - 删除导弹的碰撞攻击力\n
         - 总攻击力相同\n
        部署的导弹在等待时间结束或达成触发条件时爆炸， 攻击更大范围的敌人\n
         - 延迟爆炸时范围增加\n
         - 触发爆炸时范围额外增加\n
        [触发功能]说明\n
         - 用特定技能攻击待机状态的炸弹可使其进入过热状态\n
         - 再次输入该技能时， 过所有过热状态的炸弹将同时引爆\n
         - 未再次输入时， 导弹将恢复等待状态\n
        [触发技能]\n
         - [M-3喷火器]、 [聚焦喷火器]、[等离子放射器]、 [UHT-03爆炎喷火器]
        """
        ...

# X-2太阳神光炮
# gunner_female/launcher_female/28fc502b0b8b4e57709f34a1e9369692
# 944b9aab492c15a8474f96947ceeb9e4/28fc502b0b8b4e57709f34a1e9369692
class Skill36(ActiveSkill):
    """
        展开恒星生成器[X-2太阳神光炮]。\n
        在前方凝聚能量， 生成爆炸的恒星后发射。\n
        射出的恒星吸附路径上的敌人， 使范围内的敌人进入灼伤状态， 并爆炸造成伤害。\n
        在决斗场中， 射出的恒星碰到墙壁时会爆炸， 且恒星的爆炸范围与射击距离无关。\n
    [学习重武装改造后]\n
        技能施放中可以追加施放[激光炮]技能， [激光炮]的攻击力相当于最大充电时的攻击力。
    """
    name = "X-2太阳神光炮"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [350, 2940]
    uuid = "28fc502b0b8b4e57709f34a1e9369692"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 灼伤攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 激光攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 激光攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 攻击范围扩大比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [X-2太阳神光炮]\n
        使用强化部件， 实现性能迭代\n
         - 增加火器操作速度\n
        将灼伤伤害包含在爆炸伤害中\n
         - 总攻击力相同\n
        [激光炮]连接强化\n
         - 可以强制中断[激光炮]并施放该技能\n
         - 有效射程额外增加\n
        施放该技能时， 立即初始化[激光炮]的冷却时间\n
         - [激光炮]攻击力 -12.5%
        """
        ...

    def vp_2(self):
        """
        [X-2太阳神光炮]\n
        变更为瞄准地面发射\n
         - 无法使用激光炮形态\n
        发射前按住技能键可以增加爆炸范围\n
         - 最多增加30%\n
         - 最大蓄气所需时间 : 1秒\n
         - 最大蓄气持续时间 : 5秒\n
        发射的恒星会钻入地面并爆炸， 形成火焰地带\n
         - 删除灼伤伤害\n
        火焰地带会持续对敌人造成伤害并附加减速\n
         - 火焰地带持续时间 : 5秒\n
         - 总攻击力相同\n
         - 减速持续时间 : 2秒\n
         - 减速效果 : 50%
        """
        ...

    def effect(self, old, new):
        if self.vp == 1:
            self.associate = [{"type":"*skillRation","data":[0] + [-12.5]*self.maxLv,"skills":["激光炮"]}]
        return super().effect(old, new)

# 超温重火器
# gunner_female/launcher_female/5892d1fa4462e561ac8f8d2c74892b0a
# 944b9aab492c15a8474f96947ceeb9e4/5892d1fa4462e561ac8f8d2c74892b0a
class Skill37(PassiveSkill):
    """
        增加基本攻击和重火器技能的攻击力。
    """
    name = "超温重火器"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    uuid = "5892d1fa4462e561ac8f8d2c74892b0a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击和重火器攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]

# 远古粒子炮
# gunner_female/launcher_female/2ba299855fc22192cba4f73db75e9d0e
# 944b9aab492c15a8474f96947ceeb9e4/2ba299855fc22192cba4f73db75e9d0e
class Skill38(ActiveSkill):
    """
        向前方敌人发射远古粒子炮， 可以使敌人受到巨大的物理伤害。\n
        若快速连续按技能键则会达到最大蓄电， 并可以发射更强的激光。\n
        可以对龙族敌人造成更大的伤害。
    """
    name = "远古粒子炮"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 8
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [1000, 8400]
    uuid = "2ba299855fc22192cba4f73db75e9d0e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 主炮基本攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 0
    # 主炮最大蓄电时攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 10
    # 主炮持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 主炮攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 对龙族伤害比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 等离子放射器
# gunner_female/launcher_female/2a0a39184de92acf1c1375e00b77404c
# 944b9aab492c15a8474f96947ceeb9e4/2a0a39184de92acf1c1375e00b77404c
class Skill39(ActiveSkill):
    """
        用等离子放射器发射电流， 对敌人造成伤害并强制控制敌人。\n
        发射过程中， 可以用方向键移动。
    """
    name = "等离子放射器"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [400, 1120]
    uuid = "2a0a39184de92acf1c1375e00b77404c"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 放射攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 37
    # 多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 移动速度比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 强制控制持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [等离子放射器]\n
        提升放射装置输出功率， 一次性全部放射\n
         - 删除长按技能键操作\n
         - 增加放射后僵直\n
         - 发射位置残留电场\n
        施放技能时， 放射装置强化15秒\n
         - 施放以下技能时， 会瞬间喷射全部高压压缩火焰\n
         - 总攻击力相同\n
        目标技能\n
         - [M-3喷火器]、 [聚焦喷火器]
        """
        ...

    def vp_2(self):
        """
        [等离子放射器]\n
        用特殊变压装置使功能加强\n
         - 向周围大范围放射等离子体\n
         - 放射过程中， 过充电流保护枪炮师免受伤害
        """
        ...

# FM-92特殊榴弹
# gunner_female/launcher_female/9dc8438e4572d39243c97da31c113acc
# 944b9aab492c15a8474f96947ceeb9e4/9dc8438e4572d39243c97da31c113acc
class Skill40(ActiveSkill):
    """
        向空中发射榴弹。 一段时间后， 榴弹快速发射出画面外， 然后返回掉落到目标敌人处， 造成爆炸伤害。\n
        按住技能键， 可以调整双重点火时机。
    """
    name = "FM-92特殊榴弹"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [800, 1680]
    uuid = "9dc8438e4572d39243c97da31c113acc"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 最短飞行时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最长飞行时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 爆炸范围扩大率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [FM-92特殊榴弹]\n
        基本冷却时间变更为75秒\n
        总攻击力 +50%\n
        强化导弹性能， 对广域发动强力攻击\n
         - 删除长按技能键操作\n
         - 诱导范围扩大\n
         - 爆炸范围 +30%
        """
        self.cd = 75
        self.skillRation *= 1 + 0.5
        ...

    def vp_2(self):
        """
        [FM-92特殊榴弹]\n
        基本冷却时间变更为25秒\n
        总攻击力 -50%\n
        优化导弹规格以减负\n
         - 可以在使用其他重火器过程中， 同时操作使用\n
         - 单独使用时减少操作僵直
        """
        self.cd = 25
        self.skillRation *= 1 - 0.5
        ...

# 重武装改造
# gunner_female/launcher_female/9bc30e0f6e22b0333762d04acae7d252
# 944b9aab492c15a8474f96947ceeb9e4/9bc30e0f6e22b0333762d04acae7d252
class Skill41(PassiveSkill):
    """
        为了弥补女性力量上的劣势而发明的强化重武装。\n
        学习后， 增加基本攻击力和技能攻击力， 减少部分技能的后坐力和发射后僵直时间， 并改良[加农炮]、 [FM-92榴弹]、 [X-2太阳神光炮]的性能， 变更部分重火器的外形和发射时特效。 \n
    - [减少后坐力的技能] -\n
    [反坦克炮]、 [激光炮]、 [蓄电激光炮]、 [FM-31榴弹发射器]\n
    - [减少发射后僵直时间的技能] -\n
    [M-137格林机枪]、 [炙烤]、 [M-3喷火器]、 [聚焦喷火器]、 [FM-31榴弹发射器]、 [FM-92榴弹]、 [远古粒子炮]和[FM-92特殊榴弹]。\n
    - [变更重火器外形或特效的技能] -\n
    [激光炮]、 [M-3喷火器]、 [聚焦喷火器]、 [等离子放射器]、 [M-137格林机枪]\n
    - [加农炮性能改良] -\n
        增加能量球飞行距离， 且命中敌人时立即爆炸。 同时， 冲撞伤害与爆炸伤害合并。\n
    - [FM-92榴弹]性能改良 - \n
        减少40%的攻击力和冷却时间，  变更为最多可施放2次再进行冷却的技能。\n
        在地面施放重火器系列技能时可以同时使用该技能。\n
    - [X-2太阳神光炮性能改良] -\n
        施放时可以同时使用[激光炮]。
    """
    name = "重武装改造"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 1
    rangeLv = 3
    uuid = "9bc30e0f6e22b0333762d04acae7d252"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 后坐力减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 发射后僵直时间减少率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    associate = [{"data":data0}]

# 集束炸弹
# gunner_female/launcher_female/68062215e75d92575958873ac8ede31a
# 944b9aab492c15a8474f96947ceeb9e4/68062215e75d92575958873ac8ede31a
class Skill42(ActiveSkill):
    """
        发射具有子母弹功能的炸弹。 炸弹命中敌人时发生爆炸， 炸弹中的小型炸弹向四方扩散， 引起连锁爆炸。
    """
    name = "集束炸弹"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [777, 6021]
    uuid = "68062215e75d92575958873ac8ede31a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 炸弹攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 10
    # 爆炸多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 爆炸范围扩大率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [集束炸弹]\n
        变更为可填充2次的技能\n
         - 每次填充冷却时间 : 20秒\n
         - 每次攻击力 -50%\n
        使用轻量化炸弹\n
         - 减少发射反冲\n
        发射后3秒内移动速度 +30%\n
         - 效果持续时间内施放特定技能时， 持续时间延长至该技能结束\n
        [目标技能目录]\n
         - [M-3喷火器]、 [聚焦喷火器]、 [等离子放射器]、 [UHT-03爆炎喷火器]
        """
        self.cd = 20
        self.skillRation *= 1 - 0.5
        ...

    def vp_2(self):
        """
        [集束炸弹]\n
        使用装载了更多火药的强化子弹\n
         - 子弹速度 +30%\n
         - 攻击范围更广\n
        未命中时迅速重新装填\n
         - 未命中时冷却时间缩短为5秒
        """
        ...

# PT-15原始型压缩炮
# gunner_female/launcher_female/95103ae7c54eaedea3bbcf726520db6c
# 944b9aab492c15a8474f96947ceeb9e4/95103ae7c54eaedea3bbcf726520db6c
class Skill43(ActiveSkill):
    """
        压缩空气后向前发射， 压缩后的空气炮会吸附沿途敌人， 并引发爆炸。\n
        可以使用上下方向键指定空气炮发射的方向。\n
    [不使用方向键]\n
        默认以角色面向的方向发射空气炮， 炮弹飞出一段距离后发生爆炸。\n
    [按下方向键]\n
        向地面发射炮弹并引爆， 同时聚集周围的敌人\n
    [按上或向后方向键]\n
        向前后发射。\n
    (最多射击1次)
    """
    name = "PT-15原始型压缩炮"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [580, 4500]
    uuid = "95103ae7c54eaedea3bbcf726520db6c"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 左右方向射击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 前方射击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 地面射击爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 前方发射范围扩大率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [PT-15原始型压缩炮]\n
        在地面放置PT-15后发射\n
         - 喷出高压缩空气， 攻击周围大范围敌人\n
        火器操作过程中， 进入无敌状态
        """
        ...

    def vp_2(self):
        """
        [PT-15原始型压缩炮]\n
        使用强化压缩模组， 实现性能迭代\n
         - 攻击范围更广\n
         - 始终发动前方强化射击版本\n
        释放空气击退敌人\n
         - 整齐排列范围内敌人的位置\n
        可以强制中断发射后僵直， 并施放其他重火器技能
        """
        ...

# 火力全开
# gunner_female/launcher_female/0f638da961acf7958ac6070b7aaed013
# 944b9aab492c15a8474f96947ceeb9e4/0f638da961acf7958ac6070b7aaed013
class Skill44(ActiveSkill):
    """
        召唤并装备强袭装甲后， 摧毁前方的一切敌人。\n
        召唤强袭装甲时， 会产生冲击波， 将周围敌人向前推开。
    """
    name = "火力全开"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 8000]
    uuid = "0f638da961acf7958ac6070b7aaed013"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 激光炮和格林机枪攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 50
    # 激光炮和格林机枪多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 多重炮击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 20
    # 多重炮击多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 火箭炮爆炸攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1

# 潘多拉1号
# gunner_female/launcher_female/de20372767d014d62dc7361ac686834e
# 944b9aab492c15a8474f96947ceeb9e4/de20372767d014d62dc7361ac686834e
class Skill45(PassiveSkill):
    """
        凝结天界战争技术的决战兵器， 设计为陆战型， 具备高度机动性和强大火力。\n
        学习后， 增加基本攻击力和转职技能攻击力， 变更部分技能效果。\n
    [反坦克炮]\n
        将主炮末端与潘多拉1号对接， 更替为攻击范围更广的集束弹。\n
    [M-3喷火器]、 [聚焦喷火器]、 [等离子放射器]、 [UHT-03爆炎喷火器]\n
        开启潘多拉1号的机动装置， 施放过程中移动速度比率以相同数值适用。\n
        施放[M-3喷火器]和[聚焦喷火器]时， 获得霸体护甲。
    """
    name = "潘多拉1号"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "de20372767d014d62dc7361ac686834e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [M-3喷火器]、 [聚焦喷火器]、 [等离子放射器]、 [UHT-03爆炎喷火器]移动速度比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"data":data0}]

# UHT-03爆炎喷火器
# gunner_female/launcher_female/3a691a432c58abebc08211df45c4f4bd
# 944b9aab492c15a8474f96947ceeb9e4/3a691a432c58abebc08211df45c4f4bd
class Skill46(ActiveSkill):
    """
        运用潘多拉1号开启爆炎喷火器模式。\n
        施放过程中， 使用[M-3喷火器]或[聚焦喷火器]， 可以强化喷出的火焰。\n
        使用[M-3喷火器]或[聚焦喷火器]强化技能时， 该技能攻击力在[UHT-03爆炎喷火器]攻击力之上叠加。\n
        喷火器发射过程中， 可以用方向键移动。
    """
    name = "UHT-03爆炎喷火器"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [773, 6000]
    uuid = "3a691a432c58abebc08211df45c4f4bd"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 喷火攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit1 = 25
    # 喷火攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 移动速度比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 制胜·最终兵器
# gunner_female/launcher_female/25c0018b82c644f6e20d728f1478e671
# 944b9aab492c15a8474f96947ceeb9e4/25c0018b82c644f6e20d728f1478e671
class Skill47(ActiveSkill):
    """
        解除潘多拉1号终极接入权限， 展开决战形态， 执行最终作战。\n
        展开决战形态后立即发射导弹扰乱敌人， 然后搜索自由开火区域， 并对该区域进行机动打击。\n
        占领自由开火区域后， 双手的机关枪转换成激光炮， 发射敌人无法躲避的激光。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "制胜·最终兵器"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 12889]
    uuid = "25c0018b82c644f6e20d728f1478e671"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 展开决战形态时导弹攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 展开决战形态时导弹攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 战场轰炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 5
    # 战场轰炸攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 机动打击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 10
    # 机动打击攻击次数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 双手激光炮攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 25
    # 双手激光炮攻击次数 : {value7}次
    data7 = get_data(f'{prefix}/{uuid}', 7)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'launcher_female'
        self.nameCN = '重霄·枪炮师'
        self.role = 'gunner_female'
        self.角色 = '神枪手(女)'
        self.职业 = '枪炮师'
        self.jobId = '944b9aab492c15a8474f96947ceeb9e4'
        self.jobGrowId = '618326026de1a1f1cfba5dbd0b8396e7'

        self.武器选项 = ['手弩', '步枪','左轮枪','自动手枪','手炮']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '重甲'
        self.buff = 2.023

        super().__init__(equVersion, __name__)
