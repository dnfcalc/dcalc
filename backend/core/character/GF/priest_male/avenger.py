#f6a4ad30555b99b499c07835f87ce522
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "priest_male/avenger/cn/skillDetail"


# 恶魔之手
# priest_male/avenger/ca75c965f20a150f99f54155a37400df
# f6a4ad30555b99b499c07835f87ce522/ca75c965f20a150f99f54155a37400df
class Skill10(ActiveSkill):
    """
        召唤出恶魔之手， 使敌人受到伤害。\n
        恶魔之手的伸手和握住各有攻击判定， 握住时有一定几率使敌人进入束缚状态。\n
        可以强制中断基本攻击动作， 并立即施放该技能。\n
        若在[魔化 : 末日守卫者]状态下施放该技能， 则增加攻击力和冷却时间。
    """
    name = "恶魔之手"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 6
    mp = [28, 308]
    uuid = "ca75c965f20a150f99f54155a37400df"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 伸手时攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 握住时攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 束缚几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 束缚持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # - [魔化 ： 末日守卫者]状态下施放时-
    # 攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 冷却时间增加率 : {value5}% 
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 手大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    associate = [{"data":data4,"skills":[name]},{"data":data5,"skills":[name],"type":"*cd"}]


# 化魔
# priest_male/avenger/2f5d03c7848effbc0a23f4df45d9ca46
# f6a4ad30555b99b499c07835f87ce522/2f5d03c7848effbc0a23f4df45d9ca46
class Skill13(ActiveSkill):
    """
        在效果持续期间， 将自身一定量的生命值转换成魔法值， 若当前生命值少于施放技能所需的生命值， 则无法使用此技能。\n
    - [转职为惩戒者后] -\n
        施放其他技能时， 可以施放[化魔]； 施放一次后， 每隔一段时间自动施放。\n
        使用单独的生命值消耗量和魔法值恢复量， 并且发动[恶魔诅咒]技能。\n
        当前生命值少于施放技能所需的生命值时， 仍然会消耗剩余生命值发动技能； 生命值为1时， 将不消耗生命值直接发动。\n
        每次施放时， 增加魔化状态的持续时间、 减少冷却时间， 并且恢复一定量的恶魔能量。\n
        在决斗场中， 施放其他技能过程中无法使用该技能。
    """
    name = "化魔"
    learnLv = 15
    masterLv = 1
    maxLv = 11
    position = 0 #TODO
    rangeLv = 5
    cd = 8
    uuid = "2f5d03c7848effbc0a23f4df45d9ca46"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 生命值消耗 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法值恢复 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # - [转职为惩戒者后] -
    # 恶魔能量恢复 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 魔化状态持续时间增加 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 魔化状态冷却时间减少 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 生命值消耗 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 魔法值恢复 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [化魔]发动间隔 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7)



# 恶魔之力
# priest_male/avenger/dac8d8207618150c162e4c6f9e168527
# f6a4ad30555b99b499c07835f87ce522/dac8d8207618150c162e4c6f9e168527
class Skill15(PassiveSkill):
    """
    惩戒者特有技能； 可以使基本攻击产生变化， 在进行基本攻击或技能攻击时， 可以积攒恶魔能量。 施放技能后， 可以按Z、 X、 C键， 消耗恶魔能量并用恶魔残影给予敌人暗属性魔法伤害。 部分技能施放过程中， 无法追加施放[恶魔之力]， 且魔化状态下无法发动。\n
        并且[落凤锤]、 [升天阵]、 [恶魔屏障]、 [审判]、 [邪魔再临]、 [极恶洪流]、 [末日福音 : 毁灭之翼]技能不会恢复恶魔能量， 部分技能消耗恶魔能量， 可以造成更强大的伤害。 [审判]技能在恶魔能量不足时无法施放。\n
    [可以使用恶魔之力]\n
    [恶魔之手]、 [裂地锤]、 [回旋飞镰]、 [魔镰之舞]、 [黑暗之刺]、 [厄运之轮]、 [黑暗之触]、 [恶魔之拳]、 [黑暗权能]、 [审判] (半魔化)、 前冲攻击 (半魔化)\n
    [消耗恶魔能量]\n
    [黑暗权能]、 [不朽战吼]、 [毁灭强击]、 [永堕 : 混沌弑神]、 [极恶洪流]、 [审判](恶魔能量不足时无法施放)\n
        在决斗场中， 决斗开始时恶魔能量初始值为0。
    """
    name = "恶魔之力"
    learnLv = 15
    masterLv = 20
    maxLv = 30
    position = 0 #TODO
    rangeLv = 3
    uuid = "dac8d8207618150c162e4c6f9e168527"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # TODO 暂时不做 目前复仇都是魔化流
    # 恶魔能量上限 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 使用Z键攻击时， 恶魔能量消耗 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 使用X键攻击时， 恶魔能量消耗 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 使用C键攻击时， 恶魔能量消耗 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 使用Z键时的攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 使用X键时的攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 使用C键时的攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

# 魔镰之舞
# priest_male/avenger/8e358ecf99ac9df31a6132aeafe378a9
# f6a4ad30555b99b499c07835f87ce522/8e358ecf99ac9df31a6132aeafe378a9
class Skill16(ActiveSkill):
    """
        将恶魔的气息注入到镰刀之中， 并快速挥动镰刀给予敌人多段暗属性伤害； 每次攻击可恢复一定量的生命值。 若连续按技能键， 则可以加快镰刀挥动速度。\n
        若在[魔化 : 末日守卫者]状态下施放该技能， 则增加攻击力和冷却时间。
    """
    name = "魔镰之舞"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 5
    mp = [30, 336]
    uuid = "8e358ecf99ac9df31a6132aeafe378a9"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 挥舞镰刀攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 6
    # 多段攻击次数 : 6次
    # 每次攻击的生命值恢复 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # - [魔化 ： 末日守卫者]状态下施放[魔镰之舞]时 -
    # 攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 冷却时间增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    associate = [{"data":data2,"skills":[name]},{"data":data3,"skills":[name],"type":"*cd"}]

# 半魔化
# priest_male/avenger/5c00ce6d7dbbb5e9a0f6e1071d486832
# f6a4ad30555b99b499c07835f87ce522/5c00ce6d7dbbb5e9a0f6e1071d486832
class Skill17(ActiveSkill):
    """
        解放部分恶魔之力， 在人形或半魔化状态时， 增加部分技能的攻击力。 施放[半魔化]后， 会进入半人半魔的状态， 增加攻击速度和移动速度， 并施放更为强力的恶魔残影。\n
        在半魔化状态下， 施放[厄运之轮]、 [末日浩劫]途中可以变身为[魔化 : 末日守卫者]， 并对敌人造成伤害。\n
    메타몰포시스 상태에서 데빌 스트라이커 사용 시 악마 게이지가 소모되지 않는다.\n
        [增加攻击力的技能]\n
    [恶魔之手]、 [魔镰之舞]、 [裂地锤]、 [回旋飞镰]、 [黑暗之刺]、 [厄运之轮]、 [黑暗之触]、 [恶魔之拳]、 [黑暗权能]、 [地狱之门]、 [末日浩劫]、 [不朽战吼]、 [毁灭强击]、 [永堕 : 混沌弑神]、 [极恶洪流]、 [末日福音 : 毁灭之翼]
    """
    name = "半魔化"
    learnLv = 15
    masterLv = 1
    maxLv = 11
    position = 0 #TODO
    rangeLv = 15
    cd = 5
    mp = [394, 5061]
    uuid = "5c00ce6d7dbbb5e9a0f6e1071d486832"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # TODO 暂时不做 目前复仇都是魔化流
    # 在人形或半魔化状态时， 技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # <Z>键恶魔残影攻击力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # <X>键恶魔残影攻击力比率 : {value2}% * 4
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # <C>键恶魔残影攻击力比率 : {value3}% * 2
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 攻击速度增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 移动速度增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 发动[半魔化]时需要的恶魔能量 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 恶魔能量衰减周期 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 每个衰减周期恶魔能量减少 : {value8}
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 在半魔化状态下， 施放[末日浩劫]途中变身为魔化状态时的冲击波范围增加率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)

# 镰刀精通
# priest_male/avenger/8b08f9504167a9c0f3a1d29d71b7943e
# f6a4ad30555b99b499c07835f87ce522/8b08f9504167a9c0f3a1d29d71b7943e
class Skill19(PassiveSkill):
    """
    마법 공격력, 크리티컬 확률이 증가한다. 낫 착용 시 공격 속도, 암속성 저항이 증가하고 명속성 저항이 감소한다.
    """
    name = "镰刀精通"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    uuid = "8b08f9504167a9c0f3a1d29d71b7943e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 魔法攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法暴击率增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [装备镰刀时]
    # 攻击速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 暗属性抗性增加量 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 光属性抗性减少量 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    associate = [{"data":data0,"type":"$*PAtkM"}]

# 裂地锤
# priest_male/avenger/0c3a468aee1f7ce06bf91eb3319518c1
# f6a4ad30555b99b499c07835f87ce522/0c3a468aee1f7ce06bf91eb3319518c1
class Skill20(ActiveSkill):
    """
        将恶魔的气息聚集到拳头后， 用力锤击地面击起乱石。 乱石柱从地面出来后， 对周围敌人造成暗属性伤害。\n
        若在[魔化 : 末日守卫者]状态下施放该技能， 石柱变为黑暗石柱， 并增加乱石的数量和冷却时间。\n
        黑暗石柱会追加爆炸， 对敌人造成伤害。
    """
    name = "裂地锤"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 5
    mp = [30, 336]
    uuid = "0c3a468aee1f7ce06bf91eb3319518c1"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # [裂地锤]生成数量 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [魔化 ： 末日守卫者]状态下施放[裂地锤]时
    # 石柱变为黑暗石柱
    # 升起的乱石数量 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 冷却时间增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    associate = [{"data":data3,"skills":[name],"type":"*cd"}]


# 回旋飞镰
# priest_male/avenger/0113c8b1306ca76d208f83f2d093dd62
# f6a4ad30555b99b499c07835f87ce522/0113c8b1306ca76d208f83f2d093dd62
class Skill22(ActiveSkill):
    """
        向前方投掷回旋的恶魔镰刀， 使敌人受到暗属性伤害。 若再按一次技能键或待一定时间后可收回镰刀， 同时给予敌人多段暗属性伤害。\n
        若在[魔化 : 末日守卫者]状态下施放该技能， 则增加攻击力和冷却时间。
    """
    name = "回旋飞镰"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 10
    mp = [45, 462]
    uuid = "0113c8b1306ca76d208f83f2d093dd62"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2
    # 攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 多段攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 5
    # 多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # - [魔化 ： 末日守卫者]状态下施放时 -
    # 投掷镰刀攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 投掷镰刀多段攻击次数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 收回镰刀多段攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 收回镰刀多段攻击次数 : {value7}次
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 攻击力增加率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 冷却时间增加率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [范围信息]
    # [魔化 ： 末日守卫者]状态下， 攻击范围比率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    associate = [{"data":data8,"skills":[name]},{"data":data9,"skills":[name],"type":"*cd"}]

# 堕落之魂
# priest_male/avenger/527cdc3ecca985e18ef819d456532b26
# f6a4ad30555b99b499c07835f87ce522/527cdc3ecca985e18ef819d456532b26
class Skill23(ActiveSkill):
    """
        消耗自身的恶魔能量， 在一段时间内增加惩戒者的基本攻击力和技能攻击力， 恶魔能量不足时无法施放。\n
        [堕落之魂]的技能等级会随着[恶魔之力]的技能等级增加而增加。
    """
    name = "堕落之魂"
    learnLv = 25
    masterLv = 20
    maxLv = 30
    position = 0 #TODO
    rangeLv = 3
    cd = 5
    uuid = "527cdc3ecca985e18ef819d456532b26"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 惩戒者基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 恶魔能量消耗 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 黑暗之刺
# priest_male/avenger/ab6fc3303df03b58911967dfca2b5d07
# f6a4ad30555b99b499c07835f87ce522/ab6fc3303df03b58911967dfca2b5d07
class Skill24(ActiveSkill):
    """
        将身体内的恶魔气息释放出来， 形成黑暗之刺， 可以给敌人造成暗属性伤害， 并使其进入僵直状态。\n
        若在[魔化 : 末日守卫者]状态下施放该技能， 则会追加打击效果， 并增加冷却时间。\n
        被击状态下也能施放技能， 被击状态下施放技能时， 攻击力会增加。
    """
    name = "黑暗之刺"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 10
    mp = [60, 686]
    uuid = "ab6fc3303df03b58911967dfca2b5d07"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 被敌人攻击时施放， 技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [魔化 ： 末日守卫者]状态下施放[黑暗之刺]时
    # 黑暗之刺巨大化
    # 追加打击效果
    # 追加打击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 冷却时间增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    associate = [{"data":data3,"skills":[name],"type":"*cd"}]

# 恶魔诅咒
# priest_male/avenger/002cbdd9bfd0f0b970451ae8d48d029e
# f6a4ad30555b99b499c07835f87ce522/002cbdd9bfd0f0b970451ae8d48d029e
class Skill25(PassiveSkill):
    """
        学习后， 增加惩戒者基本攻击和转职技能攻击力。 ([魔化 : 末日守卫者]基本攻击、 [恶魔之爪]除外)\n
        使用除[魔化 : 末日守卫者]技能之外的惩戒者转职技能时， 发动[恶魔诅咒]效果， 并增加移动速度。
    """
    name = "恶魔诅咒"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    uuid = "002cbdd9bfd0f0b970451ae8d48d029e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 移动速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [恶魔诅咒]发动几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [恶魔诅咒]持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)

    associate = [{"data":data0,"exceptSkills":["魔化 : 末日守卫者"]}]

# 厄运之轮
# priest_male/avenger/ac21c02567f04a92b54dd85c091d1e5a
# f6a4ad30555b99b499c07835f87ce522/ac21c02567f04a92b54dd85c091d1e5a
class Skill26(ActiveSkill):
    """
        利用恶魔的力量将自身变为巨大的齿轮， 向前高速旋转并攻击敌人， 使其受到多段暗属性伤害。 按方向键可以改变齿轮的攻击方向， 并且如果在开始时按住向后方向键， 则可以缓慢移动。\n
        可以在跳跃状态下施放。\n
        若在[魔化 : 末日守卫者]状态下施放该技能， 会进化为死亡打击， 并增加攻击力和冷却时间。\n
        死亡打击会瞬间斩过敌人， 并造成伤害。
    """
    name = "厄运之轮"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 16
    mp = [180, 1512]
    uuid = "ac21c02567f04a92b54dd85c091d1e5a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 齿轮多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 6
    # 移动距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # - [魔化 ： 末日守卫者]状态下施放[厄运之轮]时 -
    # 进化为死亡打击
    # 攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 冷却时间增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 移动距离 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 多段攻击次数 : {value6}次
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 攻击范围比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [魔化 ： 末日守卫者]状态下攻击范围比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

    associate = [{"data":data3,"skills":[name]},{"data":data4,"skills":[name],"type":"*cd"}]

    def vp_1(self):
        """
        [厄运之轮]\n
        [魔化 : 末日守卫者]状态下， 在原地交叉双臂并向前方挥出， 对敌人进行攻击\n
        - 将命中的敌人拉向Y轴\n
        删除多段攻击\n
        - 总攻击力相同\n
        [人形、 半魔化]状态下施放时， 不适用该属性
        """
        ...

    def vp_2(self):
        """
        [厄运之轮]\n
        [魔化 : 末日守卫者]状态下施放时， 变更为快速斩击更大范围的敌人并移动的技能\n
        - 攻击范围 +30%\n
        [人形、 半魔化]状态下施放时， 不适用该属性
        """
        ...

# 恶魔之拳
# priest_male/avenger/c91a62dc0a18360acf5031ac0ebf09f5
# f6a4ad30555b99b499c07835f87ce522/c91a62dc0a18360acf5031ac0ebf09f5
class Skill27(ActiveSkill):
    """
        从自己的影子中抽取恶魔的气息缠绕在手臂上， 然后向前方扩散。\n
        对敌人进行多段攻击并短暂强控敌人， 然后爆炸， 对周围敌人造成伤害。\n
        在决斗场中， 只有攻击之前的动作为霸体状态， 爆炸范围内的敌人会被拉到惩戒者的位置。
    """
    name = "恶魔之拳"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [300, 2604]
    uuid = "c91a62dc0a18360acf5031ac0ebf09f5"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 多段攻击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 多段攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [魔化 : 末日守卫者状态下施放时]
    # 多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 多段攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 10
    # 爆炸攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # [范围信息]
    # 爆炸大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [恶魔之拳]\n
        消耗100恶魔能量， 对命中的敌人中最强的1名敌人附加3秒的恶意\n
        恶意结束后， 复仇者回收恶意并获得增益效果\n
        恶意没有单独的伤害， 被恶意附身的敌人死亡时， 立即回收恶意\n
        - 对被附上恶意的敌人附加减速状态\n
        - 回收恶意时恢复20%的生命值\n
        - 10秒内攻击速度和移动速度 +10%\n
        恶魔能量恢复量 +50%
        """
        ...

    def vp_2(self):
        """
        [恶魔之拳]\n
        可以强制中断转职技能命中后僵直并施放[恶魔之拳] (觉醒技能除外)\n
        可以强制中断[恶魔之拳]命中后僵直并施放转职技能 (觉醒技能除外)
        """
        ...

# 黑暗之触
# priest_male/avenger/5f4c55fe2ebdf0623bd76d4fda872ddc
# f6a4ad30555b99b499c07835f87ce522/5f4c55fe2ebdf0623bd76d4fda872ddc
class Skill28(ActiveSkill):
    """
        从自己的影子伸出恶魔之臂抓住敌人并聚集在前方， 撕扯攻击敌人后， 恶魔之臂回到影子里。\n
        成功命中敌人时恢复恶魔能量， 命中的敌人会被强制控制。\n
        [魔化 : 末日守卫者]状态下施放时， 增加判定大小和攻击力。
    """
    name = "黑暗之触"
    learnLv = 40
    masterLv = 50
    maxLv = 60
    position = 0 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [300, 2604]
    uuid = "5f4c55fe2ebdf0623bd76d4fda872ddc"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 刺击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 刺击攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 撕扯攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 撕扯攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 爆炸攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 恶魔能量恢复 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [魔化 : 末日守卫者状态下施放时]
    # 刺击攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 3
    # 撕扯攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    hit7 = 3
    # 爆炸攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    hit8 = 1
    # [范围信息]
    # 攻击范围比率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)

    def vp_1(self):
        """
        [黑暗之触]\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 12.5秒\n
        - 每次攻击力 -50%\n
        可以在部分技能施放过程中无施放动作发动\n
        - 可发动的技能 : [回旋飞镰]、 [黑暗之刺]、 [恶魔之拳]、 [黑暗权能]、 [不朽战吼]、 [毁灭强击]、 [极恶洪流]\n
        - [毁灭强击]、 [黑暗权能]进化方向1 (魔化) 可以在特定时间点以后可以施放
        """
        self.cd = 12.5
        self.skillRation = 1 - 0.5
        ...

    def vp_2(self):
        """
        [黑暗之触]\n
        在[魔化 : 末日守卫者]状态下施放时， 额外召唤恶魔之手\n
        - 基本冷却时间变更为50秒\n
        - 总攻击力 +100%\n
        - [人形、 半魔化]状态下施放时， 不适用该属性\n
        攻击范围 +30%\n
        - 不论当前状态均适用
        """
        self.cd = 50
        self.skillRation = 1 + 1
        ...

# 黑暗权能
# priest_male/avenger/78b86e64fbb74c1db1b71c50a5ac21cd
# f6a4ad30555b99b499c07835f87ce522/78b86e64fbb74c1db1b71c50a5ac21cd
class Skill29(ActiveSkill):
    """
        惩戒者猛击地面， 产生黑暗冲击波打击敌人， 然后横向砍击。 横向砍击路径上生成的恶魔气息与黑暗冲击波结合后产生爆炸。\n
        被黑暗冲击波击中的敌人进入强制控制状态， 直到爆炸时解除。\n
        拥有一定量的恶魔能量时， 消耗恶魔能量造成更强大的爆炸伤害。\n
        若在[魔化 : 末日守卫者]状态下施放该技能， 会用缠绕着恶魔气息的手臂对敌人进行抓挠攻击。
    """
    name = "黑暗权能"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [350, 2940]
    uuid = "78b86e64fbb74c1db1b71c50a5ac21cd"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 黑暗冲击波攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 砍击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 消耗恶魔能量时， 爆炸攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 恶魔能量消耗 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [魔化 ： 末日守卫者]状态下施放[黑暗权能]时
    # 黑暗冲击波攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # 抓挠攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 1
    # 爆炸攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    hit7 = 1
    # [范围信息]
    # 范围比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

    def vp_1(self):
        """
        [黑暗权能]\n
        [魔化 : 末日守卫者]状态下施放时， 蹬地跳跃后追踪并攻击最强敌人\n
        - 施放技能过程中所受伤害 -80%\n
        - 寻敌范围 : 角色前方800px\n
        [人形、 半魔化]状态下施放时， 不适用该属性
        """
        ...

    def vp_2(self):
        """
        [黑暗权能]\n
        [魔化 : 末日守卫者]状态下施放时， 聚集恶魔气息后， 向下重击地面， 在周围引发更大范围的冲击波\n
        - 聚集恶魔气息时吸附周围的敌人\n
        删除抓挠和爆炸攻击\n
        - 总攻击力相同\n
        [魔化 : 末日守卫者]状态下施放时， 消耗恶魔能量爆炸攻击力增加删除\n
        - 消耗恶魔能量时， 增加黑暗冲击波攻击力\n
        [人形、 半魔化]状态下施放时， 不适用该属性
        """
        ...

# 恶魔唤醒
# priest_male/avenger/31823197cc0b04d4c5dcf8f928d9220c
# f6a4ad30555b99b499c07835f87ce522/31823197cc0b04d4c5dcf8f928d9220c
class Skill30(PassiveSkill):
    """
        增加恶魔能量、 魔化状态下的基本攻击力、 [恶魔之爪]和[审判]的攻击力。\n
        在噩梦的作用下， 增加技能攻击力。
    """
    name = "恶魔唤醒"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 3
    uuid = "31823197cc0b04d4c5dcf8f928d9220c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 恶魔能量额外获得 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔化状态下基本攻击攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [审判]攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 技能攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    associate = [
        {"data":data1,"skills":["魔化 : 末日守卫者"]},
        {"data":data2,"skills":["审判"]},
        {"data":data3,"exceptSkills":["审判","魔化 : 末日守卫者"]},
        ]

# 魔化 : 末日守卫者
# priest_male/avenger/5cac3411ccef1af333953e0ded5e942d
# f6a4ad30555b99b499c07835f87ce522/5cac3411ccef1af333953e0ded5e942d
class Skill31(ActiveSkill):
    """
        化为恶魔形态进行战斗。\n
        魔化后恢复恶魔能量， 并在魔化时全程适用霸体状态， 同时增加防御力、 攻击速度、 移动速度、 命中率和魔法暴击伤害， 同时增加控制型异常状态抗性。\n
    [魔化状态下可使用的新技能]\n
    [恶魔之爪]、 [审判]、 [恶魔屏障]、 \n
    [恶魔之爪] : Z\n
        [恶魔之爪]可以强制中断基本攻击动作后立即施放， 也可在蓄气后使用。\n
        在空中基本攻击时， 会撕开地面的敌人。\n
        [他的内心里还留有披上神圣的礼官服时的纯粹、 正直、 慈爱与怜悯。]
    """
    name = "魔化 : 末日守卫者"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [1500, 12600]
    uuid = "5cac3411ccef1af333953e0ded5e942d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 魔化持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 生命值增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 物理/魔法防御力增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 攻击速度增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 魔法暴击伤害增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 移动速度增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 控制型异常状态抗性增加 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 命中率增加 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 第1击攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 第2击攻击力 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 第3击攻击力 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 第4击攻击力 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 前冲攻击力 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 空中撕裂攻击攻击力 : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # [半魔化]或魔化状态下， 冲击波攻击力 : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # 在[半魔化]增益状态下施放[厄运之轮]时， 魔化攻击攻击力 : {value15}%
    data15 = get_data(f'{prefix}/{uuid}', 15)
    # 在[半魔化]增益状态下施放[厄运之轮]时， 魔化攻击攻击力 : {value16}%
    data16 = get_data(f'{prefix}/{uuid}', 16)
    # [恶魔之爪]
    # 攻击力 : {value17}~{value18}%
    data17 = get_data(f'{prefix}/{uuid}', 17)
    data18 = get_data(f'{prefix}/{uuid}', 18)
    # [恶魔屏障]
    # 所受伤害减少率 : {value19}%
    data19 = get_data(f'{prefix}/{uuid}', 19)
    # [学习半魔化后]
    # 攻击速度增加 : 5%
    # 移动速度增加 : 10%

    mode = ["x","z","z蓄力"]

    associate = [{"data":data4,"type":"$*PAtkM"}]

    def setMode(self, mode):
        if mode == "x":
            self.hit8 = 2
            self.hit9 = 2
            self.hit10 = 2
            self.hit11 = 2
            ...
        elif mode == "z":
            self.hit17 = 1
            ...
        elif mode == "z蓄力":
            self.hit18 = 1
            ...

    def getSkillCD(self, mode=None):
        if mode == "x":
            return 1.0
        elif mode == "z":
            return 2.0
        elif mode == "z蓄力":
            return 2.0

# 审判
# priest_male/avenger/85f7c810ad503790e8626439fe936d56
# f6a4ad30555b99b499c07835f87ce522/85f7c810ad503790e8626439fe936d56
class Skill32(ActiveSkill):
    """
        将右臂变为恶魔本体的模样对敌人行刑。\n
        按向前键施放技能时， 伸出巨大的手臂抓取敌人并砸向地面， 然后拖动一定距离后抛出。 对于无法抓取的敌人， 则直接握住并粉碎敌人。\n
        只有在半魔化及魔化状态下才能聚集恶魔之力施放[审判]。 若在[魔化 : 末日守卫者]状态下施放该技能， 则可以增加攻击力。
    """
    name = "审判"
    learnLv = 50
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    cd = 145
    uuid = "85f7c810ad503790e8626439fe936d56"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 恶魔能量消耗 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [审判]向上攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [审判]最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # -  [用 → 方向键追加操作时]  -
    # 砸向地面的攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 땅에 찍을 때 충격파 공격력 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 拖动敌人时多段攻击的攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 拖动多段攻击次数 : {value6}次
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 扔出前向下击打的攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 扔出敌人的攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 握住并粉碎无法抓取的敌人的攻击力 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 魔化状态下[审判]攻击力增加率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)

    associate = [{"data": [0] + [10]*60,"skills":[name]}]

    def skillInfo(self, mode = None):
        pre = self.char.GetSkillByName("魔化 : 末日守卫者")
        for data in [self.data1, self.data2, self.data3, self.data4, self.data5, self.data6, self.data7, self.data8, self.data9]:
            data[:] = [0] + [data[1] * (1+(lv-1)*16/69) for lv in range(1,pre.maxLv+1)]
        return super().skillInfo(mode)

# 恶魔屏障
# priest_male/avenger/dd32a9825ec1af42a91f2223be6658e5
# f6a4ad30555b99b499c07835f87ce522/dd32a9825ec1af42a91f2223be6658e5
class Skill33(ActiveSkill):
    """
        生成一道屏障， 减轻自身受到的伤害。\n
        只能在魔化状态下使用。\n
        [神的惩罚者从不畏惧痛苦……和死亡！]
    """
    name = "恶魔屏障"
    learnLv = 50
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    cd = 5
    uuid = "dd32a9825ec1af42a91f2223be6658e5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 邪魔再临
# priest_male/avenger/573723c8c0614f5b1218ca9ff992115b
# f6a4ad30555b99b499c07835f87ce522/573723c8c0614f5b1218ca9ff992115b
class Skill34(PassiveSkill):
    """
        在危机时刻， 凭借对恶的憎恶和毁灭的决心战胜消亡。\n
        魔化状态下生命值降为0时， 变回人类形态。\n
        变回人类形态时恢复生命值/魔法值。\n
        该效果具有单独的冷却时间， 在冷却时间内生命值降为0则不会发动技能。
    """
    name = "邪魔再临"
    learnLv = 50
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "573723c8c0614f5b1218ca9ff992115b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 邪魔再临冷却时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 生命值/魔法值恢复 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 地狱之门
# priest_male/avenger/902a016f6978f13740f237e4740a5646
# f6a4ad30555b99b499c07835f87ce522/902a016f6978f13740f237e4740a5646
class Skill35(ActiveSkill):
    """
        利用恶魔的力量打开地狱之门， 从中释放出大量的恶魔气息攻击敌人。 在[魔化 : 末日守卫者]状态下， 技能攻击力会大幅提升。
    """
    name = "地狱之门"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [600, 1680]
    uuid = "902a016f6978f13740f237e4740a5646"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 黑暗气息攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 8
    # 多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # - [魔化 : 末日守卫者状态下] -
    # 攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 发射距离比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    associate = [{"data":data2,"skills":[name]}]

    def vp_1(self):
        """
        [地狱之门]\n
        消耗150恶魔能量， 施放技能后可以移动\n
        - 恶魔能量不足150时， 不发动该效果\n
        发射距离 +30%
        """
        ...

    def vp_2(self):
        """
        [地狱之门]\n
        命中时获得增益效果\n
        - 攻击、 移动速度 +10%， 效果持续10秒\n
        - 施放时进入无敌状态
        """
        ...

# 末日浩劫
# priest_male/avenger/370586038cf40378f20d338d507a780c
# f6a4ad30555b99b499c07835f87ce522/370586038cf40378f20d338d507a780c
class Skill36(ActiveSkill):
    """
        高高跃起， 并在下方形成魔法阵吸附敌人。 经过一段时间或追加操作时， 惩戒者会在高空正对魔法阵中心直冲而下， 产生冲击波， 可对敌人造成大量伤害。\n
        在[魔化 : 末日守卫者]状态下， 惩戒者会造成更大的灾难。
    """
    name = "末日浩劫"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [1200, 2520]
    uuid = "370586038cf40378f20d338d507a780c"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 冲击波攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # -  [魔化 ： 末日守卫者]状态下  -
    # 攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 吸附范围 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 冲击波范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    associate = [{"data":data1,"skills":[name]}]

    def vp_1(self):
        """
        [末日浩劫]\n
        在[魔化 : 末日守卫者]状态下施放， 会在前方引发强烈的爆炸\n
        - 总攻击力相同\n
        - 被击中的敌人进入诅咒状态， 效果持续3秒\n
        [人形、 半魔化]状态下施放时， 不适用该属性
        """
        ...

    def vp_2(self):
        """
        [末日浩劫]\n
        吸附敌人的范围 +50%\n
        - 大幅增加吸附敌人的速度\n
        - 大幅增加跳跃移动速度\n
        冲击波攻击范围 +40%
        """
        ...

# 不朽战吼
# priest_male/avenger/ce7cd04a44e32212e80f120f4421996e
# f6a4ad30555b99b499c07835f87ce522/ce7cd04a44e32212e80f120f4421996e
class Skill37(ActiveSkill):
    """
        发出恶魔的战吼对附近敌人造成大量伤害， 并使周围的敌人进入诅咒和失魂状态。 攻击敌人可以恢复恶魔能量。\n
        在魔化状态下使用时， 技能会变为多段攻击， 对敌人造成更大的伤害。\n
        拥有一定量的恶魔能量时， 消耗恶魔能量来换取施放额外的[不朽战吼]。 在半魔化状态下使用时， 可以减少追加恶魔能量的消耗量。 \n
        [啊， 没有归宿的可怜的野兽……]
    """
    name = "不朽战吼"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "ce7cd04a44e32212e80f120f4421996e"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 战吼攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 战吼多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 失魂状态持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 诅咒几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 诅咒持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # - [多段攻击命中时， 恶魔能量恢复量] -
    # 一般怪物和精英怪物 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 领主怪物 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # - [魔化 : 末日守卫者状态下] -
    # 战吼攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    hit7 = 5
    # 战吼多段攻击次数 : {value8}次
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # - [额外战吼] -
    # 额外战吼次数上限 : {value9}次
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 每1次额外战吼攻击力 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    hit10 = 2
    # 每1次额外战吼恶魔能量消耗值 : {value11}
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # [半魔化状态下]
    # 恶魔能量消耗量减少率 : 100%
    # [范围信息]
    # 大小比率 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)

    def vp_1(self):
        """
        [不朽战吼]\n
        在[魔化 : 末日守卫者]状态下施放时， 消耗恶魔能量， 发动1次怒吼\n
        - 恶魔能量的消耗量以技能最大消耗值为基准\n
        - 恶魔能量的消耗基准总攻击力相同\n
        - 消耗100点恶魔能量、 恶魔能量低于100时， 不发动属性效果\n
        - 在[人形、 半魔化]状态下施放时， 不适用属性\n
        施放[不朽战吼]过程中， 无法变身为[魔化 : 末日守卫者]\n
        攻击范围 +25%\n
        命中时， 无视怪物等级， 恢复60点恶魔能量
        """
        ...

    def vp_2(self):
        """
        [不朽战吼]\n
        [魔化 : 末日守卫者]状态下命中时， 每次攻击减少1秒[邪魔再临]的技能冷却时间\n
        - [人形、 半魔化]状态下施放时， 不适用该属性\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 20秒\n
        - 每次攻击力 -50%\n
        - 恶魔能量恢复量 -50%\n
        - 恶魔能量消耗量 -50%\n
        攻击范围 +30%
        """
        self.cd = 20
        self.skillRation *= 1 - 0.5
        ...

# 原罪之力
# priest_male/avenger/f45301a5590cccefbe0becf2f8d029f5
# f6a4ad30555b99b499c07835f87ce522/f45301a5590cccefbe0becf2f8d029f5
class Skill38(PassiveSkill):
    """
        恶魔的力量进一步得到进化。增加[恶魔之力]的攻击力， 并且大幅增加基本攻击和[恶魔之力]之外的所有技能攻击力。而且， 施放[毁灭强击]、 [不朽战吼]、 [永堕 : 混沌弑神]、 [极恶洪流]、 [末日福音 : 毁灭之翼]过程中可以立即魔化。
    """
    name = "原罪之力"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 3
    uuid = "f45301a5590cccefbe0becf2f8d029f5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # [恶魔之力]攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击和除[恶魔之力]外所有技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [
        {"data":data1,"exceptSkills":["恶魔之力"]},
        {"data":data0,"skills":["恶魔之力"]}
        ]

# 毁灭强击
# priest_male/avenger/b1732acfaf117f8e9ff130f47d3ed0e7
# f6a4ad30555b99b499c07835f87ce522/b1732acfaf117f8e9ff130f47d3ed0e7
class Skill39(ActiveSkill):
    """
        使用恶魔之角突进并聚拢敌人， 然后再发动强力的黑暗冲击波对范围内的敌人造成暗属性伤害。\n
        被黑暗冲击波命中的敌人会因被暗炎附身而受到持续性伤害。 拥有恶魔能量时， 消耗恶魔能量可增加暗炎的击打次数。\n
        对无法抓取的敌人不适用控制效果。\n
        在魔化状态下， 可以增加技能攻击力； 在变形状态下， 可以减少恶魔能量消耗量。\n
        [你以为世人会歌颂你们的功绩吗？ 他们只会在被救赎后， 用轻蔑的眼神指责你们， 用苛责的方式打压你们， 让你们终生悔过和赎罪。  --致不朽战士]
    """
    name = "毁灭强击"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "b1732acfaf117f8e9ff130f47d3ed0e7"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 强击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 黑暗冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 暗炎攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 10
    # 暗炎攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [追加效果]
    # 连续按技能键时， 恶魔能量最大消耗量 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 最大消耗时暗炎攻击次数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [魔化 : 末日守卫者状态下]
    # 攻击力增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [半魔化状态下]
    # 恶魔能量消耗量减少 : 100%
    # [范围信息]
    # 爆炸大小比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    associate = [{"data":data6,"skills":[name]}]

    def vp_1(self):
        """
        [毁灭强击]\n
        向最强敌人突进后撕裂对方\n
        - 追踪距离 : 角色前方900px\n
        删除强击、 黑暗冲击波攻击力\n
        - 追加撕裂攻击力\n
        - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [毁灭强击]\n
        施放时在大范围内产生多个黑暗冲击波\n
        删除强击攻击\n
        - 总攻击力相同
        """
        ...

# 永堕 : 混沌弑神
# priest_male/avenger/4126d0a7ccd5bdf87a0ab698f857dcd1
# f6a4ad30555b99b499c07835f87ce522/4126d0a7ccd5bdf87a0ab698f857dcd1
class Skill40(ActiveSkill):
    """
        释放恶魔之力攻击前方所有敌人。 施展强力的连锁攻击， 每次攻击敌人时可恢复恶魔能量。\n
        施放后连续按<X>键， 可以增加攻击速度。 按<C>键， 可以直接进行终结一击。 \n
        若技能结束之前按<X>键或<Z>键， 则可以通过消耗额外的恶魔能量， 进行更强力的终结一击。 半魔化状态下减少恶魔能量消耗量。
    """
    name = "永堕 : 混沌弑神"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "4126d0a7ccd5bdf87a0ab698f857dcd1"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 恶魔之力释放时的爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 连锁撕裂的攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 12
    # 连锁撕裂攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 每次撕裂时获得的恶魔能量 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 向上撕裂的攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # 向下撕裂的攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 2
    # 向下撕裂攻击次数 : {value6}次
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # - [X、 Z键追加操作] -
    # 最大蓄力时向下撕裂攻击力增加率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 向下撕裂恶魔能量消耗值上限 : {value8}
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # - [魔化 : 末日守卫者状态下] -
    # 攻击力增加率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # - [半魔化状态下] -
    # 恶魔能量消耗量减少 : 100%

    associate = [{"data":data9,"skills":[name]},{"data":data7,"skills":[name],"type":"+power5"}]

# 光之影
# priest_male/avenger/ca2536eb56df0e812c88c59cabd38be0
# f6a4ad30555b99b499c07835f87ce522/ca2536eb56df0e812c88c59cabd38be0
class Skill41(PassiveSkill):
    """
        将恶魔的力量释放到极限， 可以使用更强大的恶魔之力， 绝不屈服于无止尽的恶魔低语， 凭借真挚信念获得驱使光的力量。 增加基本攻击力和转职技能攻击力， 变更部分[魔化 : 末日守卫者]状态下使用的技能。\n
        [回旋飞镰] : [魔化 : 末日守卫者]状态下施放时， 在攻击范围内以攻击次数上限对敌人进行攻击。 镰刀投掷攻击力和回旋飞镰的攻击力相同， 镰刀回收攻击力和回旋飞镰的多段攻击力相同。\n
        [裂地锤] : [魔化 : 末日守卫者]状态下施放时， 在前方生成多个黑暗石柱， 并使其爆炸。 黑暗石柱生成和爆炸攻击变更为范围攻击判定。 黑暗石柱生成和爆炸攻击力随裂地锤攻击力增加而增加。\n
        [啊……这是您对我的试练吗]
    """
    name = "光之影"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 3
    uuid = "ca2536eb56df0e812c88c59cabd38be0"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [裂地锤]黑暗石柱生成攻击 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [裂地锤]黑暗石柱爆炸攻击数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 黑暗石柱生成和爆炸攻击力 : [裂地锤]的攻击力的{value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [回旋飞镰]镰刀投掷最大攻击数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [回旋飞镰]镰刀回收最大攻击数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)

    associate = [{"data":data0}]

# 极恶洪流
# priest_male/avenger/7f9ffcd296361f1367b8b74e773d5e99
# f6a4ad30555b99b499c07835f87ce522/7f9ffcd296361f1367b8b74e773d5e99
class Skill42(ActiveSkill):
    """
        释放恶魔的力量， 在头上生成暗黑球， 从球体中发射光线横扫前方的敌人。 拥有一定量的恶魔能量时， 消耗一定量的恶魔能量， 可以凝聚内心的光之力， 发射更强大的光线。\n
        [魔化 : 末日守卫者]状态下使用时， 造成额外伤害。 [半魔化]状态下使用时， 减少恶魔能量消耗量。
    """
    name = "极恶洪流"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [800, 6000]
    uuid = "7f9ffcd296361f1367b8b74e773d5e99"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 光线攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 光线攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 光线最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [附加效果]
    # 恶魔能量消耗 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 消耗恶魔能量时攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [魔化 ： 末日守卫者]状态下施放时
    # 攻击力增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [半魔化]状态下施放时
    # 恶魔能量消耗量减少 : 100%
    associate = [{"data":data5,"skills":[name]},{"data":data4,"skills":[name]}]

# 末日福音 : 毁灭之翼
# priest_male/avenger/c1dd8b776fb1dd24c6373c678ef1dd2e
# f6a4ad30555b99b499c07835f87ce522/c1dd8b776fb1dd24c6373c678ef1dd2e
class Skill43(ActiveSkill):
    """
        将恶魔的力量释放到精神的极限， 进入真·恶魔化的状态， 但低语愈加明显。 变身结束后， 撕裂自己的翅膀， 投向地图中的最强大的敌人。 投掷的翅膀穿刺敌人并使其悬空， 惩戒者突袭后拔出刺入的翅膀。 拔出翅膀时， 在冲击的余波下出现黑暗空间， 惩戒者将自己的全部力量集中于翅膀上， 形成巨大的光之镰刀， 毁灭敌人和黑暗空间。\n
        [魔化 : 末日守卫者]状态下使用时， 造成额外伤害。\n
        施放技能的过程中无法使用[恶魔屏障]。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。 
    """
    name = "末日福音 : 毁灭之翼"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "c1dd8b776fb1dd24c6373c678ef1dd2e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 翅膀穿刺攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 突袭攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 翅膀拔出攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 终结镰刀斩击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [魔化 ： 末日守卫者状态下]施放时
    # 攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    associate = [{"data":data4,"skills":[name]}]


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'avenger'
        self.nameCN = '神启·复仇者'
        self.role = 'priest_male'
        self.角色 = '圣职者(男)'
        self.职业 = '复仇者'
        self.jobId = 'f6a4ad30555b99b499c07835f87ce522'
        self.jobGrowId = 'c9b492038ee3ca8d27d7004cf58d59f3'

        self.武器选项 = ['光杖','念珠','图腾','镰刀','战斧']
        self.输出类型选项 = ['魔法百分比']
        self.输出类型 = '魔法百分比'
        self.防具精通属性 = ['智力']
        self.防具类型 = '重甲'
        self.buff = 1.972

        super().__init__(equVersion, __name__)
