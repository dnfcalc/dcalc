#ca0f0e0e9e1d55b5f9955b03d9dd213c
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "fighter_male/striker_male/cn/skillDetail"



# 下段踢
# fighter_male/striker_male/4655101518604f874721b3cc249aae10
# ca0f0e0e9e1d55b5f9955b03d9dd213c/4655101518604f874721b3cc249aae10
class Skill6(ActiveSkill):
    """
    向敌人发出高伤害的踢脚攻击， 可以攻击倒地的敌人， 而且能使被击中的敌人出现较长时间的僵直。\n
    攻击成功时产生冲击波， 对周围敌人造成伤害。\n
    被直接命中的敌人不受冲击波伤害。
    """
    name = "下段踢"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 2
    mp = [10, 112]
    uuid = "4655101518604f874721b3cc249aae10"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 下段踢攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 发动速度增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 冲击波大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)


# 蹲伏
# fighter_male/striker_male/9dda3f4a849dba1a288dd65e116860f2
# ca0f0e0e9e1d55b5f9955b03d9dd213c/9dda3f4a849dba1a288dd65e116860f2
class Skill9(ActiveSkill):
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
    position = 7
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
# fighter_male/striker_male/c9664191611af31142e052dfaef84530
# ca0f0e0e9e1d55b5f9955b03d9dd213c/c9664191611af31142e052dfaef84530
class Skill10(PassiveSkill):
    """
    使自身的身体强悍如钢铁， 并增加一定的物防和体力。 被击时， 有一定几率使自身进入霸体状态。
    """
    name = "钢筋铁骨"
    learnLv = 10
    masterLv = 50
    maxLv = 60
    position = 4
    rangeLv = 3
    uuid = "c9664191611af31142e052dfaef84530"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 增加物理防御力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 增加体力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 霸体发动几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 鹰踏
# fighter_male/striker_male/78bd107acd474518b606be1e4fd38239
# ca0f0e0e9e1d55b5f9955b03d9dd213c/78bd107acd474518b606be1e4fd38239
class Skill11(ActiveSkill):
    """
    在空中跳跃着踩踏敌人并给予敌人一定伤害。\n
    可以连续对敌人进行一定次数的踩踏。 技能的冷却时间从最后一次踩踏结束落地时开始计算。
    """
    name = "鹰踏"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 7
    mp = [10, 97]
    uuid = "78bd107acd474518b606be1e4fd38239"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 踩踏攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 踩踏次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后踩踏攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

# 疾风追击
# fighter_male/striker_male/dcb31a63ef58954f44ff2070c42a9a98
# ca0f0e0e9e1d55b5f9955b03d9dd213c/dcb31a63ef58954f44ff2070c42a9a98
class Skill12(ActiveSkill):
    """
    前冲攻击后， 通过快速连续的攻击给予敌人一定伤害； 前冲攻击命中敌人时， 敌人不会倒地。 前冲攻击后按攻击键或技能键， 可以进行追击， 此时会消耗自身一定量的魔法值。\n
    该技能的基本攻击只有1次， 但学习[疾风连击]后可再追加1次。
    """
    name = "疾风追击"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cd = 2
    mp = [8, 67]
    uuid = "dcb31a63ef58954f44ff2070c42a9a98"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1


# 瞬步
# fighter_male/striker_male/9dc8438e4572d39243c97da31c113acc
# ca0f0e0e9e1d55b5f9955b03d9dd213c/9dc8438e4572d39243c97da31c113acc
class Skill14(ActiveSkill):
    """
    向前方快速移动一定距离。\n
    撞到敌人时停止移动。
    """
    name = "瞬步"
    learnLv = 10
    masterLv = 1
    maxLv = 1
    position = 6
    rangeLv = 2
    cd = 5
    mp = [10, 10]
    uuid = "9dc8438e4572d39243c97da31c113acc"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 移动距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)


# 拳套掌握
# fighter_male/striker_male/1dad88963abdc96b091fcab185a8820d
# ca0f0e0e9e1d55b5f9955b03d9dd213c/1dad88963abdc96b091fcab185a8820d
class Skill19(PassiveSkill):
    """

    """
    name = "拳套掌握"
    learnLv = 15
    masterLv = 1
    maxLv = 10
    position = 1
    rangeLv = 3
    uuid = "1dad88963abdc96b091fcab185a8820d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 冷却时间减少率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [
        {"data":data0,"type":"*cdReduce", 'exceptSkills': ['双重释放', '烈焰焚步', '极武霸皇踢', '焚火逐日拳']}
    ]

# 强拳
# fighter_male/striker_male/dcd536f1674630f01fc9667bb202b851
# ca0f0e0e9e1d55b5f9955b03d9dd213c/dcd536f1674630f01fc9667bb202b851
class Skill20(ActiveSkill):
    """
    集中体内的能量， 增加命中敌人的僵直比率和自身暴击伤害， 效果持续一定时间。
    """
    name = "强拳"
    learnLv = 15
    masterLv = 20
    maxLv = 30
    position = 5
    rangeLv = 3
    cd = 5
    uuid = "dcd536f1674630f01fc9667bb202b851"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 敌人的僵直比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 暴击伤害增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 决斗场攻击速度减少 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 肘击
# fighter_male/striker_male/c77a417c43de80c4ce32c1ed405d174a
# ca0f0e0e9e1d55b5f9955b03d9dd213c/c77a417c43de80c4ce32c1ed405d174a
class Skill21(ActiveSkill):
    """
    用强劲的肘部快速攻击敌人， 并使敌人进入僵直状态。\n
    可以通过按方向键， 调整方向移动施放。
    """
    name = "肘击"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cd = 6
    mp = [30, 252]
    uuid = "c77a417c43de80c4ce32c1ed405d174a"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 肘击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 敌人僵直比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 肘击速度增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 霸体护甲
# fighter_male/striker_male/3d8f3d438405d79f8d3ed68072674d1e
# ca0f0e0e9e1d55b5f9955b03d9dd213c/3d8f3d438405d79f8d3ed68072674d1e
class Skill22(ActiveSkill):
    """
    可以使自身增加物理/魔法防御力和体力， 而且被攻击后不会倒地， 但仍会受到伤害， 效果持续一定时间。
    """
    name = "霸体护甲"
    learnLv = 20
    masterLv = 20
    maxLv = 30
    position = 4
    rangeLv = 3
    cd = 30
    mp = [40, 336]
    uuid = "3d8f3d438405d79f8d3ed68072674d1e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理、 魔法防御力增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 体力增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [决斗场]
    # 移动速度减少 : 10%

# 疾风连击
# fighter_male/striker_male/8572675ec6a1f50b6eff6a867376c2de
# ca0f0e0e9e1d55b5f9955b03d9dd213c/8572675ec6a1f50b6eff6a867376c2de
class Skill23(PassiveSkill):
    """
    施放[疾风追击]时， 可以向敌人发出第3、 4击。
    """
    name = "疾风连击"
    learnLv = 20
    masterLv = 1
    maxLv = 1
    position = 8
    rangeLv = 1
    uuid = "8572675ec6a1f50b6eff6a867376c2de"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501




# 铁山靠
# fighter_male/striker_male/3c5604bdbb0240b8f130f59ab40509c3
# ca0f0e0e9e1d55b5f9955b03d9dd213c/3c5604bdbb0240b8f130f59ab40509c3
class Skill25(ActiveSkill):
    """
    向前滑行用肩部对敌人进行猛力的攻击。\n
    按前方向键， 可以滑行得更远进行攻击。
    """
    name = "铁山靠"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 7
    mp = [50, 420]
    uuid = "3c5604bdbb0240b8f130f59ab40509c3"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 铁山靠攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 碎骨
# fighter_male/striker_male/717f1e2104fe4b796f800352fa143ecc
# ca0f0e0e9e1d55b5f9955b03d9dd213c/717f1e2104fe4b796f800352fa143ecc
class Skill26(ActiveSkill):
    """
    向敌人发出强威力的下段踢。\n
    有一定几率使命中的敌人进入减速状态。\n
    攻击成功时产生冲击波， 对周围敌人造成伤害。\n
    被直接击中的敌人不受冲击波伤害。
    """
    name = "碎骨"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 1
    rangeLv = 2
    cd = 7
    mp = [50, 420]
    uuid = "717f1e2104fe4b796f800352fa143ecc"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 发动速度增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 下段踢攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit0 = 1
    # 冲击波攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 减速几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 减速持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 移动速度减少率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 攻击速度减少率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 冲击波大小比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

# 强袭重击
# fighter_male/striker_male/8ec9da6f808889b63adf2680fbf1f331
# ca0f0e0e9e1d55b5f9955b03d9dd213c/8ec9da6f808889b63adf2680fbf1f331
class Skill27(PassiveSkill):
    """
    [鹰踏]变更为[强袭重击]， 使用[鹰踏]时， 使用俯冲地面的[强袭重击]击打敌人。\n
    [鹰踏]的攻击力使用增加后的伤害向下重击地面。\n
    [强袭重击]的第一次击打攻击力是[鹰踏]的第一次击打攻击力， 最后的爆炸攻击力是[鹰踏]的最后一击攻击力。\n
    在空中可以使用[柔化肌肉]强制中断。
    """
    name = "强袭重击"
    learnLv = 25
    masterLv = 1
    maxLv = 11
    position = 3
    rangeLv = 1
    uuid = "8ec9da6f808889b63adf2680fbf1f331"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # [鹰踏]攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

    associate = [
        {"type":"*skillDamage","data":data0,"skills":["鹰踏"]},
    ]

# 弱点感知
# fighter_male/striker_male/23a5e0fba03283cb1b324a847b3fe370
# ca0f0e0e9e1d55b5f9955b03d9dd213c/23a5e0fba03283cb1b324a847b3fe370
class Skill28(PassiveSkill):
    """
    感知敌人的弱点， 并增加自身的物理暴击率和物理命中率。
    """
    name = "弱点感知"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 5
    rangeLv = 3
    uuid = "23a5e0fba03283cb1b324a847b3fe370"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 暴击率增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 命中率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 旋风腿
# fighter_male/striker_male/202edb928046f4fa6dedf6337377efd5
# ca0f0e0e9e1d55b5f9955b03d9dd213c/202edb928046f4fa6dedf6337377efd5
class Skill29(ActiveSkill):
    """
    在原地快速旋转身体并用连续的扫腿攻击周围的敌人； 可以在地面或空中使用， 对命中的敌人有吸附效果。\n
    施放后不能移动， 可以按跳跃键中断技能。\n
    转职成为散打时， 才可以强制中断基本攻击动作， 并立即施放该技能。
    """
    name = "旋风腿"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cd = 8
    mp = [50, 420]
    uuid = "202edb928046f4fa6dedf6337377efd5"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 旋风腿攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 10
    # 攻击次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 柔化肌肉
# fighter_male/striker_male/5152480fdde81362575a488d4cec4af9
# ca0f0e0e9e1d55b5f9955b03d9dd213c/5152480fdde81362575a488d4cec4af9
class Skill30(PassiveSkill):
    """
    使自身的身体瞬间变得柔若无骨； 增加转职技能攻击力， 使用散打系列技能时， 可以强制中断当前的技能并立即施放散打系列的其他技能， 可以使技能与技能形成连续技。\n
    使用[柔化肌肉]强制中断并施放技能时， 如果该技能命中敌人， 则增加已激活的霸体状态持续时间。\n
    可以强制中断的技能 : [后踢]、 [前踢]、 [下段踢]、 [鹰踏]、 [强袭重击]、 [疾风连击]、 [旋风腿]、 [闪击快打]、 [肘击]、 [铁山靠]、 [碎骨]、 [炽焰旋风腿]、 [冲膝]、 [闪电之舞]、 [瞬影连环踢]、 [旋风碎心踢]、 [飞燕旋风]、 [烈火强踢]、 [烈火强拳]、 [极武霸皇踢]、 [炼狱坠星腿]\n
    可以强制中断其他散打系列技能并立即使用[焚火逐日拳]， 但无法中断[焚火逐日拳]并立即施放其他散打系列技能。\n
    在决斗场中有起始冷却时间， 起始冷却时间结束后自动激活。 技能攻击力增加率效果仅适用于柔化后使用的技能。
    """
    name = "柔化肌肉"
    learnLv = 30
    masterLv = 5
    maxLv = 15
    position = 5
    rangeLv = 5
    uuid = "5152480fdde81362575a488d4cec4af9"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 强制中断的次数 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 强制中断次数自动恢复时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 转职技能攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 霸体持续时间增加 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 霸体持续时间上限 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # - [决斗场] -
    # 起始冷却时间 : 10秒

    associate = [{"type":"*skillDamage","data":data2}]

# 闪步
# fighter_male/striker_male/0c262dac3ec41ff79e359ada9c7a7faf
# ca0f0e0e9e1d55b5f9955b03d9dd213c/0c262dac3ec41ff79e359ada9c7a7faf
class Skill31(PassiveSkill):
    """
    向前后方快速移动一定距离。\n
    使用[柔化肌肉]强制中断其他技能， 并发动此技能时， 可以无视冷却时间使用。\n
    使用[柔化肌肉]强制施放此技能时， 若按向后方向键， 则角色会面向前方， 并向后移动。\n
    学习[闪步]后， 身手变得更加灵活， [瞬步]移动过程中即使撞到敌人也不会停下。
    """
    name = "闪步"
    learnLv = 30
    masterLv = 1
    maxLv = 1
    position = 0
    rangeLv = 1
    uuid = "0c262dac3ec41ff79e359ada9c7a7faf"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 闪击快打
# fighter_male/striker_male/d204ec03a0aed2f20211fb6ccc48d46d
# ca0f0e0e9e1d55b5f9955b03d9dd213c/d204ec03a0aed2f20211fb6ccc48d46d
class Skill32(ActiveSkill):
    """
    以光一般的速度向敌人突进并发动敏捷的连续攻击。\n
    按方向键可以追踪前方一定范围内的敌人并向其突进， 并对突进过程中碰到第一个敌人发动连续攻击。\n
    使用[柔化肌肉]强制中断后施放时， 也可以转换方向。
    """
    name = "闪击快打"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cd = 12
    mp = [50, 420]
    uuid = "d204ec03a0aed2f20211fb6ccc48d46d"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 突进肘击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 中段踢攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 第2击冲击波大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 冲膝
# fighter_male/striker_male/42c82812f86ff6704ae9952a2e6093a4
# ca0f0e0e9e1d55b5f9955b03d9dd213c/42c82812f86ff6704ae9952a2e6093a4
class Skill33(ActiveSkill):
    """
    将力量聚集到膝盖， 然后向近身的敌人发出极强威力的撞击； 可以击退敌人并引发冲击波， 使前方的多个敌人受到伤害。\n
    虽然此技能破坏力极大， 但是未命中敌人时会出现极大的空隙。
    """
    name = "冲膝"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [130, 1092]
    uuid = "42c82812f86ff6704ae9952a2e6093a4"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 膝撞速度增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 踢击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 冲击波攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 冲击波大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [冲膝]\n
        若未命中目标， 技能冷却时间缩短为1秒\n
        命中时， 10秒内所受伤害 -30%\n
        通过[柔化肌肉]强制中断并施放时， 技能施放速度 +20%
        """
        ...

    def vp_2(self):
        """
        [冲膝]\n
        使被直接命中的敌人进入强制控制状态， 效果持续3秒\n
        再次攻击强制控制状态的敌人， 或强制控制时间结束时， 攻击力伤害生效， 并产生巨大冲击波， 对周围敌人造成等量伤害\n
        - 删除直接命中攻击力\n
        - 总攻击力相同\n
        - 冲击波大小 +70%\n
        - 被强制控制的敌人攻击力 -30%， 效果持续10秒
        """
        ...

# 炽焰旋风腿
# fighter_male/striker_male/852f8ad797db4dca1405cb3e77198401
# ca0f0e0e9e1d55b5f9955b03d9dd213c/852f8ad797db4dca1405cb3e77198401
class Skill34(ActiveSkill):
    """
    向上跃起并用带有火焰的旋风腿对附近敌人造成多段攻击伤害， 随后向下劈击敌人。\n
    按向前键后施放技能时， 会边前进边跳跃， 随后向下劈击敌人。\n
    技能施放过程中按跳跃键时， 技能会被取消。\n
    在决斗场中， 无法用跳跃键取消技能。
    """
    name = "炽焰旋风腿"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [170, 1428]
    uuid = "852f8ad797db4dca1405cb3e77198401"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 旋风腿攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 7
    # 旋风腿多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 下踢攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 攻击速度增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [炽焰旋风腿]\n
        多段攻击次数 +12次\n
        - 总攻击力相同\n
        攻击范围 +70%\n
        通过[柔化肌肉]强制中断并施放时， 技能施放速度 +50%
        """
        ...

    def vp_2(self):
        """
        [炽焰旋风腿]\n
        变更为向前方施展敏捷的3次回旋踢\n
        - 总攻击力相同\n
        - 无法在空中施放
        """
        ...

# 闪电之舞
# fighter_male/striker_male/28b583c75a49103a1d8aabf799c000a4
# ca0f0e0e9e1d55b5f9955b03d9dd213c/28b583c75a49103a1d8aabf799c000a4
class Skill35(ActiveSkill):
    """
    向前方敌人发出强威力的踢脚， 并利用反作用力闪电般地在一定范围内的多个敌人间移动且对这些敌人造成伤害， 最后将敌人聚到一处并给予超强威力的终结一击。 周围没有敌人或移动攻击达到一定次数后就会停止移动。 无法攻击处于透明、 无敌、 伪装状态或一定高度以上的敌人。\n
    技能施放过程中， 按方向键可以调整移动距离， 按跳跃键可以停止移动并立即发动最后一击。\n
    对无法抓取的敌人不适用控制效果。\n
    在决斗场中， 被[闪电之舞]击中的敌人会微微浮空并被束缚。
    """
    name = "闪电之舞"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [180, 1512]
    uuid = "28b583c75a49103a1d8aabf799c000a4"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 移动攻击次数上限 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 每次攻击时的攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 待确认
    hit0 = 1
    # 终结一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 打击后移动距离 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [闪电之舞]\n
        施放时， 追踪范围的敌人并移动至该敌人位置发动首次攻击\n
        删除最后一击\n
        - 总攻击力相同\n
        施放中移动速度 +50%
        """
        ...

    def vp_2(self):
        """
        [闪电之舞]\n
        以首次攻击位置为基准， 瞬间聚集大范围内的敌人后， 发动最后一击\n
        - 周围敌人聚集范围 : 1200px\n
        - 移动次数 +4次\n
        - 基本冷却时间变更为12秒\n
        总攻击力 -40%
        """
        self.cd = 12
        self.skillRation *= 1 - 0.4
        ...

# 瞬影连环踢
# fighter_male/striker_male/0b8db1e10b3abbd24d38564e708675d5
# ca0f0e0e9e1d55b5f9955b03d9dd213c/0b8db1e10b3abbd24d38564e708675d5
class Skill36(ActiveSkill):
    """
    此技能是散打系列技能的上位技能， 发动后， 可以向敌人发出强威力的飞踢， 使敌人受到巨大伤害。\n
    飞踢后落地时， 可以用[柔化肌肉]强制中断当前技能并施放其他技能。\n
    但是， 在决斗场中无法在落地时使用[柔化肌肉]强制施放其他技能。
    """
    name = "瞬影连环踢"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [400, 3360]
    uuid = "0b8db1e10b3abbd24d38564e708675d5"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 飞踢攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [瞬影连环踢]\n
        追踪前方一定范围内最强的敌人， 以肉眼不可见的速度发出飞踢\n
        攻击后， 可以使用[柔化肌肉]强制中断并施放[旋风腿]、 [炽焰旋风腿]、 [烈火强踢]、 [强袭重击]、 [炼狱坠星腿]
        """
        ...

    def vp_2(self):
        """
        [瞬影连环踢]\n
        通过持续按住技能键， 可维持准备动作\n
        准备动作的维持时间越长， 连环踢距离和命中时的冲击波范围越大\n
        - 攻击力最多增加50%\n
        - 冷却时间最多增加50%\n
        - 准备动作最大维持时间 : 3秒\n
        施放技能过程中所受伤害 -90%
        """
        self.cd = 45 * 1.5
        self.skillRation *= 1 + 0.5
        ...

# 烈焰燃烧
# fighter_male/striker_male/6e33d47e6622ce03b6defdd912140270
# ca0f0e0e9e1d55b5f9955b03d9dd213c/6e33d47e6622ce03b6defdd912140270
class Skill37(PassiveSkill):
    """
    몸 안에 내재된 힘을 집중하여 더욱 강하고 효율적으로 운용한다. 습득 시 물리 공격력이 증가하고, 화염의 각 스킬의 지속 시간이 늘어나며, 지속 시간 동안 스킬 MP 소모량이 감소한다.\n
    배운 스킬창 목록에서 화염의 각 바닥 데미지를 on/off 가능하다.
    """
    name = "烈焰燃烧"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    uuid = "6e33d47e6622ce03b6defdd912140270"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [烈焰焚步]持续时间增加 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 魔法值消耗量减少率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [{"type":"$*PAtkP","data":data0}]

# 烈焰焚步
# fighter_male/striker_male/01384bbfc346775d1267fa0bc4ca605f
# ca0f0e0e9e1d55b5f9955b03d9dd213c/01384bbfc346775d1267fa0bc4ca605f
class Skill38(ActiveSkill):
    """
    召唤地狱烈焰缠绕在双脚上； 可以减少除[烈焰焚步]、 [双重释放]、 [极武霸皇踢]、 [焚火逐日拳]以外的散打系列技能的冷却时间、 技能施放后的僵直时间， 同时还可以增加敌人的僵直时间以及技能和基本攻击的攻击力。
    """
    name = "烈焰焚步"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [500, 4480]
    uuid = "01384bbfc346775d1267fa0bc4ca605f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    bind = False

    # [烈焰焚步]持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 散打系列技能冷却时间减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 散打系列技能的僵直时间减少率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 敌人僵直时间增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 移动速度增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 技能攻击力增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 基本攻击和上击时额外变化率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 施放后爆炸攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 地面的烈焰攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [柔化肌肉]蓄气时间减少 : {value9}秒
    data9 = get_data(f'{prefix}/{uuid}', 9)

    associate = [
        {"data":data1,"type":"*cdReduce", 'exceptSkills': ['双重释放', '烈焰焚步', '极武霸皇踢', '焚火逐日拳']},
        {"type":"*skillDamage","data":data5},
    ]


# 双重释放
# fighter_male/striker_male/c39c703f72d289fcd5a8f182068140d4
# ca0f0e0e9e1d55b5f9955b03d9dd213c/c39c703f72d289fcd5a8f182068140d4
class Skill39(ActiveSkill):
    """
    瞬间引爆体内的地狱火焰， 释放更强大的力量。 [瞬影连环踢]、 [烈火强拳]、 [炼狱坠星腿]中， 在[双重释放]后最先使用的技能将额外适用[双重释放]的攻击力。\n
    可以在[烈焰焚步]状态下施放。\n
    学习后， 技能等级与[烈焰焚步]同步。
    """
    name = "双重释放"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cd = 145
    mp = [850, 7000]
    uuid = "c39c703f72d289fcd5a8f182068140d4"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    bind = True

    # 双重释放强化攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1

    @property
    def lv(self):
        """技能等级"""
        return self.char.GetSkillByName("烈焰焚步").lv

    @lv.setter
    def lv(self, value):
        ...

# 飞燕旋风
# fighter_male/striker_male/8e358ecf99ac9df31a6132aeafe378a9
# ca0f0e0e9e1d55b5f9955b03d9dd213c/8e358ecf99ac9df31a6132aeafe378a9
class Skill40(ActiveSkill):
    """
    以敏捷的回旋踢聚集敌人后， 发动强力终结攻击。\n
    施放技能时， 按前方向键可以向前方跳跃。
    """
    name = "飞燕旋风"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [450, 1260]
    uuid = "8e358ecf99ac9df31a6132aeafe378a9"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 回旋踢攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2
    # 回旋踢多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 终结攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [飞燕旋风]\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 15秒\n
        - 单次攻击力 -50%\n
        可通过输入方向键沿着对角线方向移动并施放回旋踢\n
        回旋踢移动距离 +20%\n
        回旋踢攻击范围 +20%
        """
        self.cd = 15
        self.skillRation *= 1 - 0.5
        ...

    def vp_2(self):
        """
        [飞燕旋风]\n
        施放时， 攻击敌人并进行后空翻， 随后可通过再次输入技能键施放飞踢\n
        施放时进入无敌状态\n
        - 无敌状态持续时间 : 1.5秒
        """
        ...

# 旋风碎心踢
# fighter_male/striker_male/31823197cc0b04d4c5dcf8f928d9220c
# ca0f0e0e9e1d55b5f9955b03d9dd213c/31823197cc0b04d4c5dcf8f928d9220c
class Skill41(ActiveSkill):
    """
    先高速旋转身体引发一阵旋风， 然后跃起利用离心力进行极具威力的踢腿攻击。\n
    被击中的敌人会向后飞出并倒地。
    """
    name = "旋风碎心踢"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [935, 1960]
    uuid = "31823197cc0b04d4c5dcf8f928d9220c"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 旋转多段攻击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 旋转多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 第一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 最后一击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 冲击波大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [旋风碎心踢]\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 25秒\n
        - 单次攻击力 -50%\n
        最后踢腿攻击时攻击前方大范围的敌人， 并生成聚拢命中的敌人的冲击波
        """
        self.cd = 25
        self.skillRation *= 1 - 0.5
        ...

    def vp_2(self):
        """
        [旋风碎心踢]\n
        变更为仅使用最后一击的1段攻击\n
        - 总攻击力相同\n
        攻击可抓取的敌人时， 使其猛烈旋转并浮空； 攻击不可抓取的敌人时， 使其进入强制控制状态\n
        - 强制控制持续时间 : 1秒
        """
        ...

# 烈火强踢
# fighter_male/striker_male/374f53e8989ef04a8506c8ec99d9ecdc
# ca0f0e0e9e1d55b5f9955b03d9dd213c/374f53e8989ef04a8506c8ec99d9ecdc
class Skill42(ActiveSkill):
    """
    往前突进， 并让敌人进入僵直状态。 把敌人聚集后， 使用强力的向下劈击对敌人造成大量伤害。\n
    无法聚集或上挑霸体状态的怪物。\n
    在空中可以强制中断该技能并使用[柔化肌肉]。
    """
    name = "烈火强踢"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 2
    cube = 3
    cd = 45
    mp = [450, 1260]
    uuid = "374f53e8989ef04a8506c8ec99d9ecdc"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [烈火强踢]\n
        使用[柔化肌肉]强制中断并施放技能时， 无跳跃动作立即用脚下劈\n
        普通施放时， 跳跃后下劈\n
        攻击范围 +30%
        """
        ...

    def vp_2(self):
        """
        [烈火强踢]\n
        以命中的地点为中心生成火焰领域， 为散打和敌人赋予各类增益/减益效果\n
        - 火焰领域持续时间 : 10秒\n
        [散打适用效果]\n
        - 攻击速度 +20%\n
        - 移动速度 +20%\n
        - 所受伤害 -20%\n
        [敌人适用效果]\n
        - 赋予敌人灼伤异常状态
        """
        ...

# 烈火支配
# fighter_male/striker_male/b501ae53638d33a32351904f31cb6aa3
# ca0f0e0e9e1d55b5f9955b03d9dd213c/b501ae53638d33a32351904f31cb6aa3
class Skill43(PassiveSkill):
    """
    使用灵魂的力量支配火焰。\n
    学习后， 会根据[烈火支配]的效果增加技能攻击力和基本攻击力， 增加[柔化肌肉]的强制中断次数、 减少恢复时间。
    """
    name = "烈火支配"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "b501ae53638d33a32351904f31cb6aa3"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [柔化肌肉]恢复时间减少 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [柔化肌肉]强制中断次数增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [ {"type":"*skillDamage","data":data0} ]

# 烈火强拳
# fighter_male/striker_male/e1daab884dd07fc9e70d08b83d1790eb
# ca0f0e0e9e1d55b5f9955b03d9dd213c/e1daab884dd07fc9e70d08b83d1790eb
class Skill44(ActiveSkill):
    """
    用强力的突进拳击攻击并击飞敌人。\n
    可以通过按住技能键蓄力调整突进的时机， 同时在施放准备姿态下， 可以通过输入方向键调整突进距离。\n
    输入向前方向键时， 突进距离会调整到前方。 输入向后方向键时， 突进距离会调整到原地。
    """
    name = "烈火强拳"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 4
    cd = 55
    mp = [450, 1260]
    uuid = "e1daab884dd07fc9e70d08b83d1790eb"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 突进拳击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [烈火强拳]\n
        生成伴随强烈热气的冲击波， 对更大范围进行攻击\n
        - 突进距离 +50%\n
        - 攻击范围 +20%\n
        攻击过程中， 可以使用[柔化肌肉]强制中断\n
        突进时身体周围产生风压， 吸引更大范围内的敌人
        """
        ...

    def vp_2(self):
        """
        [烈火强拳]\n
        无需准备动作， 立即向正前方发动突进拳击\n
        突进过程中若接触到敌人， 则停止突进并在该位置生成冲击波\n
        - 删除长按技能键功能\n
        - 删除施放时方向键输入功能\n
        可以在地面和空中施放技能
        """
        ...

# 极武霸皇踢
# fighter_male/striker_male/c524c4f378d1cd0ff99e4580750a4567
# ca0f0e0e9e1d55b5f9955b03d9dd213c/c524c4f378d1cd0ff99e4580750a4567
class Skill45(ActiveSkill):
    """
    以电光火石般的拳击把前方的敌人聚集到击打地点， 左右轮番攻击一次， 并且把全身的力量聚于腿的末端， 使用穿刺前方的强力飞踢对敌人造成大量伤害。
    """
    name = "极武霸皇踢"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "c524c4f378d1cd0ff99e4580750a4567"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 第一击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第二击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 最后第三击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

# 千锤百炼
# fighter_male/striker_male/ef9d26746effee9199b54541f01b8752
# ca0f0e0e9e1d55b5f9955b03d9dd213c/ef9d26746effee9199b54541f01b8752
class Skill46(PassiveSkill):
    """
    以烈火煅烧自身肉体超越极限， 增加基本攻击力和技能攻击力， 使部分技能附加额外效果。\n
    [碎骨] : 在[烈焰焚步]状态下施放时， 攻击时产生的冲击波范围变大。\n
    [铁山靠] : 在[烈焰焚步]状态下施放时， 攻击时产生向前方扩散的冲击波。\n
    [烈焰焚步] : 可以在施放其他技能的过程中双重施放， 利用双重施放强化后的技能在命中敌人之前， 双重施放功能处于未激活状态。
    """
    name = "千锤百炼"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "ef9d26746effee9199b54541f01b8752"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

    associate = [ {"type":"*skillDamage","data":data0} ]

# 炼狱坠星腿
# fighter_male/striker_male/5536486eaf9b13c9a8283447cb5e77ab
# ca0f0e0e9e1d55b5f9955b03d9dd213c/5536486eaf9b13c9a8283447cb5e77ab
class Skill47(ActiveSkill):
    """
    可以在地面和空中施放。 施放时， 可以搜寻周围的敌人当中最强大的敌人， 敏捷地跳跃到空中后， 对其发动致命的下劈攻击， 并产生冲击波对敌人造成伤害。\n
    双重释放激活的状态下， 产生更强力的冲击波， 冲击波适用双重释放攻击力。
    """
    name = "炼狱坠星腿"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [773, 6000]
    uuid = "5536486eaf9b13c9a8283447cb5e77ab"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 搜寻敌人范围 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 下劈冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

# 焚火逐日拳
# fighter_male/striker_male/e36ae35f8964d92e30e33529a65544d7
# ca0f0e0e9e1d55b5f9955b03d9dd213c/e36ae35f8964d92e30e33529a65544d7
class Skill48(ActiveSkill):
    """
    将不惜牺牲一切的觉悟蕴含在拳中， 竭尽浑身力量发动一次又一次的连击。\n
    施放时， 搜寻并瞬间移动至周围最强大的敌人身边， 然后发动连续攻击。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "焚火逐日拳"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "e36ae35f8964d92e30e33529a65544d7"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 铁山靠攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 正拳第1击 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 正拳第2击 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 正拳第3击 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 高踢攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # 终结攻击拳击攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # 终结攻击拳击冲击波攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 1


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'striker_male'
        self.nameCN = '归元·散打'
        self.role = 'fighter_male'
        self.角色 = '格斗家(男)'
        self.职业 = '散打'
        self.jobId = 'ca0f0e0e9e1d55b5f9955b03d9dd213c'
        self.jobGrowId = '618326026de1a1f1cfba5dbd0b8396e7'

        self.武器选项 = ['手套', '臂铠','爪','拳套','东方棍']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '轻甲'
        self.buff = 2.143

        super().__init__(equVersion, __name__)
