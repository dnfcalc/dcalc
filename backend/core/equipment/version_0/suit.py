from core.abstract.character import CharacterProperty
from core.basic.equipment import EquEffect
from .register import register

# region 潜影暗袭


@register
def suit_1(char: CharacterProperty):
    # DCALC_REMOVE: suit_1 - 潜影之初心
    # level: 1
    # value: -
    # rarity: 稀有
    pass


@register
def suit_2(char: CharacterProperty):
    # DCALC_REMOVE: suit_2 - 潜影之初心
    # level: 2
    # value: -
    # rarity: 稀有
    pass


@register
def suit_3(char: CharacterProperty):
    # DCALC_REMOVE: suit_3 - 潜影之初心
    # level: 3
    # value: -
    # rarity: 稀有
    pass


@register
def suit_4(char: CharacterProperty):
    # DCALC_REMOVE: suit_4 - 潜影之初心
    # level: 4
    # value: -
    # rarity: 稀有
    pass


@register
def suit_5(char: CharacterProperty):
    # DCALC_REMOVE: suit_5 - 潜影之初心
    # level: 5
    # value: -
    # rarity: 稀有
    pass


@register
def suit_6(char: CharacterProperty):
    # DCALC_REMOVE: suit_6 - 潜影之藏锋
    # level: 1
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。 [潜影藏锋][装备主动技能] - 强制中断角色动作（觉醒技能除外） - 冷却时间5秒
    # rarity: 神器
    pass


@register
def suit_7(char: CharacterProperty):
    # DCALC_REMOVE: suit_7 - 潜影之藏锋
    # level: 2
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。 [潜影藏锋][装备主动技能] - 强制中断角色动作（觉醒技能除外） - 冷却时间5秒
    # rarity: 神器
    pass


@register
def suit_8(char: CharacterProperty):
    # DCALC_REMOVE: suit_8 - 潜影之藏锋
    # level: 3
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。 [潜影藏锋][装备主动技能] - 强制中断角色动作（觉醒技能除外） - 冷却时间5秒
    # rarity: 神器
    pass


@register
def suit_9(char: CharacterProperty):
    # DCALC_REMOVE: suit_9 - 潜影之藏锋
    # level: 4
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。 [潜影藏锋][装备主动技能] - 强制中断角色动作（觉醒技能除外） - 冷却时间5秒
    # rarity: 神器
    pass


@register
def suit_10(char: CharacterProperty):
    # DCALC_REMOVE: suit_10 - 潜影之藏锋
    # level: 5
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。 [潜影藏锋][装备主动技能] - 强制中断角色动作（觉醒技能除外） - 冷却时间5秒
    # rarity: 神器
    pass


@register
def suit_11(char: CharacterProperty):
    # DCALC_REMOVE: suit_11 - 潜影之伏击
    # level: 1
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。 施放技能时，获得[影子]层数。（最多叠加10次） [潜影灭迹][装备主动技能]存在[影子]层数时，施放装备技能时发动以下效果。 - 消耗3个[影子]层数 - 强制中断角色动作（觉醒技能除外） - 所有速度 +5%，效果持续5秒（最多叠加3次）
    # rarity: 传说
    char.SetStatus(SpeedA=0.05 * 3, SpeedM=0.05 * 3, SpeedR=0.05 * 3)
    pass


@register
def suit_12(char: CharacterProperty):
    # DCALC_REMOVE: suit_12 - 潜影之伏击
    # level: 2
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。 施放技能时，获得[影子]层数。（最多叠加10次） [潜影灭迹][装备主动技能]存在[影子]层数时，施放装备技能时发动以下效果。 - 消耗3个[影子]层数 - 强制中断角色动作（觉醒技能除外） - 所有速度 +5%，效果持续5秒（最多叠加3次）
    # rarity: 传说
    suit_11(char)
    pass


@register
def suit_13(char: CharacterProperty):
    # DCALC_REMOVE: suit_13 - 潜影之伏击
    # level: 3
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。 施放技能时，获得[影子]层数。（最多叠加10次） [潜影灭迹][装备主动技能]存在[影子]层数时，施放装备技能时发动以下效果。 - 消耗3个[影子]层数 - 强制中断角色动作（觉醒技能除外） - 所有速度 +5%，效果持续5秒（最多叠加3次）
    # rarity: 传说
    suit_11(char)
    pass


@register
def suit_14(char: CharacterProperty):
    # DCALC_REMOVE: suit_14 - 潜影之伏击
    # level: 4
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。 施放技能时，获得[影子]层数。（最多叠加10次） [潜影灭迹][装备主动技能]存在[影子]层数时，施放装备技能时发动以下效果。 - 消耗3个[影子]层数 - 强制中断角色动作（觉醒技能除外） - 所有速度 +5%，效果持续5秒（最多叠加3次）
    # rarity: 传说
    suit_11(char)
    pass


@register
def suit_15(char: CharacterProperty):
    # DCALC_REMOVE: suit_15 - 潜影之伏击
    # level: 5
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。 施放技能时，获得[影子]层数。（最多叠加10次） [潜影灭迹][装备主动技能]存在[影子]层数时，施放装备技能时发动以下效果。 - 消耗3个[影子]层数 - 强制中断角色动作（觉醒技能除外） - 所有速度 +5%，效果持续5秒（最多叠加3次）
    # rarity: 传说
    suit_11(char)
    pass


@register
def suit_16(char: CharacterProperty):
    # DCALC_REMOVE: suit_16 - 潜影之灭迹
    # level: 1
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。 施放技能时，获得[影子]层数。（最多叠加10次） [潜影灭迹][装备主动技能] 存在[影子]层数时，施放装备技能时发动以下效果。 - 消耗2个[影子]层数 - 强制中断角色动作（觉醒技能除外） - 所有速度 +5%，效果持续5秒（最多叠加3次） [追击替罪羊][装备主动技能] - 消耗7个[影子]层数 - 强制中断角色动作（觉醒技能除外） - 瞬移到最强大的敌人背后 - 追击范围:600px - 冷却时间：8秒
    # rarity: 史诗
    suit_11(char)
    pass


@register
def suit_17(char: CharacterProperty):
    # DCALC_REMOVE: suit_17 - 潜影之灭迹
    # level: 2
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。 施放技能时，获得[影子]层数。（最多叠加10次） [潜影灭迹][装备主动技能] 存在[影子]层数时，施放装备技能时发动以下效果。 - 消耗2个[影子]层数 - 强制中断角色动作（觉醒技能除外） - 所有速度 +5%，效果持续5秒（最多叠加3次） [追击替罪羊][装备主动技能] - 消耗7个[影子]层数 - 强制中断角色动作（觉醒技能除外） - 瞬移到最强大的敌人背后 - 追击范围:600px - 冷却时间：8秒
    # rarity: 史诗
    suit_11(char)
    pass


@register
def suit_18(char: CharacterProperty):
    # DCALC_REMOVE: suit_18 - 潜影之灭迹
    # level: 3
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。 施放技能时，获得[影子]层数。（最多叠加10次） [潜影灭迹][装备主动技能] 存在[影子]层数时，施放装备技能时发动以下效果。 - 消耗2个[影子]层数 - 强制中断角色动作（觉醒技能除外） - 所有速度 +5%，效果持续5秒（最多叠加3次） [追击替罪羊][装备主动技能] - 消耗7个[影子]层数 - 强制中断角色动作（觉醒技能除外） - 瞬移到最强大的敌人背后 - 追击范围:600px - 冷却时间：8秒
    # rarity: 史诗
    suit_11(char)
    pass


@register
def suit_19(char: CharacterProperty):
    # DCALC_REMOVE: suit_19 - 潜影之灭迹
    # level: 4
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。 施放技能时，获得[影子]层数。（最多叠加10次） [潜影灭迹][装备主动技能] 存在[影子]层数时，施放装备技能时发动以下效果。 - 消耗2个[影子]层数 - 强制中断角色动作（觉醒技能除外） - 所有速度 +5%，效果持续5秒（最多叠加3次） [追击替罪羊][装备主动技能] - 消耗7个[影子]层数 - 强制中断角色动作（觉醒技能除外） - 瞬移到最强大的敌人背后 - 追击范围:600px - 冷却时间：8秒
    # rarity: 史诗
    suit_11(char)
    pass


@register
def suit_20(char: CharacterProperty):
    # DCALC_REMOVE: suit_20 - 潜影之灭迹
    # level: 5
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。 施放技能时，获得[影子]层数。（最多叠加10次） [潜影灭迹][装备主动技能] 存在[影子]层数时，施放装备技能时发动以下效果。 - 消耗2个[影子]层数 - 强制中断角色动作（觉醒技能除外） - 所有速度 +5%，效果持续5秒（最多叠加3次） [追击替罪羊][装备主动技能] - 消耗7个[影子]层数 - 强制中断角色动作（觉醒技能除外） - 瞬移到最强大的敌人背后 - 追击范围:600px - 冷却时间：8秒
    # rarity: 史诗
    suit_11(char)
    pass


@register
def suit_21(char: CharacterProperty):
    # DCALC_REMOVE: suit_21 - 潜影之幽冥代理
    # level: 1
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。 施放技能时，获得[影子]层数。（最多叠加10次） [潜影灭迹][装备主动技能]存在[影子]层数时，施放装备技能时发动以下效果。 - 消耗1个[影子]层数 - 强制中断角色动作（觉醒技能除外） - 所有速度 +5%，效果持续5秒（最多叠加3次） [追击替罪羊][装备主动技能] - 消耗5个[影子]层数 - 强制中断角色动作（觉醒技能除外） 一瞬移到最强大的敌人背后 - 追击范围:800px - 冷却时间：8秒
    # rarity: 太初
    suit_11(char)
    pass


# endregion
# region 精灵国度


@register
def suit_22(char: CharacterProperty):
    # DCALC_REMOVE: suit_22 - 精灵元气
    # level: 1
    # value: -
    # rarity: 稀有
    pass


@register
def suit_23(char: CharacterProperty):
    # DCALC_REMOVE: suit_23 - 精灵元气
    # level: 2
    # value: -
    # rarity: 稀有
    pass


@register
def suit_24(char: CharacterProperty):
    # DCALC_REMOVE: suit_24 - 精灵元气
    # level: 3
    # value: -
    # rarity: 稀有
    pass


@register
def suit_25(char: CharacterProperty):
    # DCALC_REMOVE: suit_25 - 精灵元气
    # level: 4
    # value: -
    # rarity: 稀有
    pass


@register
def suit_26(char: CharacterProperty):
    # DCALC_REMOVE: suit_26 - 精灵元气
    # level: 5
    # value: -
    # rarity: 稀有
    pass


@register
def suit_27(char: CharacterProperty):
    # DCALC_REMOVE: suit_27 - 初阶精灵
    # level: 1
    # value: 召唤精灵一起战斗。 [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值 [停止攻击开关][装备主动技能]控制精灵们的攻击。 - 攻击中止/继续攻击 - 冷却时间1秒
    # rarity: 神器
    char.equ_effect.append(EquEffect(name='火灵安珀', icon='/equipment/skill/29.png', cd=2, data=19200))
    pass


@register
def suit_28(char: CharacterProperty):
    # DCALC_REMOVE: suit_28 - 初阶精灵
    # level: 2
    # value: 召唤精灵一起战斗。 [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值 [停止攻击开关][装备主动技能]控制精灵们的攻击。 - 攻击中止/继续攻击 - 冷却时间1秒
    # rarity: 神器
    suit_27(char)
    pass


@register
def suit_29(char: CharacterProperty):
    # DCALC_REMOVE: suit_29 - 初阶精灵
    # level: 3
    # value: 召唤精灵一起战斗。 [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值 [停止攻击开关][装备主动技能]控制精灵们的攻击。 - 攻击中止/继续攻击 - 冷却时间1秒
    # rarity: 神器
    suit_27(char)
    pass


@register
def suit_30(char: CharacterProperty):
    # DCALC_REMOVE: suit_30 - 初阶精灵
    # level: 4
    # value: 召唤精灵一起战斗。 [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值 [停止攻击开关][装备主动技能]控制精灵们的攻击。 - 攻击中止/继续攻击 - 冷却时间1秒
    # rarity: 神器
    suit_27(char)
    pass


@register
def suit_31(char: CharacterProperty):
    # DCALC_REMOVE: suit_31 - 初阶精灵
    # level: 5
    # value: 召唤精灵一起战斗。 [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值 [停止攻击开关][装备主动技能]控制精灵们的攻击。 - 攻击中止/继续攻击 - 冷却时间1秒
    # rarity: 神器
    suit_27(char)
    pass


@register
def suit_32(char: CharacterProperty):
    # DCALC_REMOVE: suit_32 - 高阶精灵
    # level: 1
    # value: 召唤精灵一起战斗。 [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值 [水灵阿库娅] 每3秒施放一次水弹：伤害量24,000% 每3秒恢复1%的魔法值 [停止攻击开关][装备主动技能]控制精灵们的攻击。 一攻击中止/继续攻击 - 冷却时间1秒 [元素释放][装备主动技能]对精灵下达协同攻击指令。 - 消耗150精灵之魂 - 攻击时，精灵之魂 +10（冷却时间1秒） - 被击时，精灵之魂- 5（冷却时间1秒） - 元素释放伤害量:80,400%
    # rarity: 传说
    char.equ_effect.append(EquEffect(name='火灵安珀', icon='/equipment/skill/29.png', cd=2, data=19200))
    char.equ_effect.append(EquEffect(name='水灵阿库娅', icon='/equipment/skill/29.png', cd=3, data=24000))
    char.equ_effect.append(EquEffect(name='元素释放', icon='/equipment/skill/29.png', cd=15, data=80400))
    pass


@register
def suit_33(char: CharacterProperty):
    # DCALC_REMOVE: suit_33 - 高阶精灵
    # level: 2
    # value: 召唤精灵一起战斗。 [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值 [水灵阿库娅] 每3秒施放一次水弹：伤害量24,000% 每3秒恢复1%的魔法值 [停止攻击开关][装备主动技能]控制精灵们的攻击。 一攻击中止/继续攻击 - 冷却时间1秒 [元素释放][装备主动技能]对精灵下达协同攻击指令。 - 消耗150精灵之魂 - 攻击时，精灵之魂 +10（冷却时间1秒） - 被击时，精灵之魂- 5（冷却时间1秒） - 元素释放伤害量:80,400%
    # rarity: 传说
    suit_32(char)
    pass


@register
def suit_34(char: CharacterProperty):
    # DCALC_REMOVE: suit_34 - 高阶精灵
    # level: 3
    # value: 召唤精灵一起战斗。 [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值 [水灵阿库娅] 每3秒施放一次水弹：伤害量24,000% 每3秒恢复1%的魔法值 [停止攻击开关][装备主动技能]控制精灵们的攻击。 一攻击中止/继续攻击 - 冷却时间1秒 [元素释放][装备主动技能]对精灵下达协同攻击指令。 - 消耗150精灵之魂 - 攻击时，精灵之魂 +10（冷却时间1秒） - 被击时，精灵之魂- 5（冷却时间1秒） - 元素释放伤害量:80,400%
    # rarity: 传说
    suit_32(char)
    pass


@register
def suit_35(char: CharacterProperty):
    # DCALC_REMOVE: suit_35 - 高阶精灵
    # level: 4
    # value: 召唤精灵一起战斗。 [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值 [水灵阿库娅] 每3秒施放一次水弹：伤害量24,000% 每3秒恢复1%的魔法值 [停止攻击开关][装备主动技能]控制精灵们的攻击。 一攻击中止/继续攻击 - 冷却时间1秒 [元素释放][装备主动技能]对精灵下达协同攻击指令。 - 消耗150精灵之魂 - 攻击时，精灵之魂 +10（冷却时间1秒） - 被击时，精灵之魂- 5（冷却时间1秒） - 元素释放伤害量:80,400%
    # rarity: 传说
    suit_32(char)
    pass


@register
def suit_36(char: CharacterProperty):
    # DCALC_REMOVE: suit_36 - 高阶精灵
    # level: 5
    # value: 召唤精灵一起战斗。 [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值 [水灵阿库娅] 每3秒施放一次水弹：伤害量24,000% 每3秒恢复1%的魔法值 [停止攻击开关][装备主动技能]控制精灵们的攻击。 一攻击中止/继续攻击 - 冷却时间1秒 [元素释放][装备主动技能]对精灵下达协同攻击指令。 - 消耗150精灵之魂 - 攻击时，精灵之魂 +10（冷却时间1秒） - 被击时，精灵之魂- 5（冷却时间1秒） - 元素释放伤害量:80,400%
    # rarity: 传说
    suit_32(char)
    pass


@register
def suit_37(char: CharacterProperty):
    # DCALC_REMOVE: suit_37 - 贵族精灵
    # level: 1
    # value: 召唤精灵一起战斗。 [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值 [水灵阿库娅] 每3秒施放一次水弹：伤害量24,000% 每3秒恢复1%的魔法值 [停止攻击开关][装备主动技能]控制精灵们的攻击。 一攻击中止/继续攻击 - 冷却时间1秒 [风灵希尔珂] 每2秒施放一次刀风：伤害量19,200% 移动速度 +15% [停止攻击开关][装备主动技能]控制精灵们的攻击。 - 攻击中止/继续攻击 - 冷却时间1秒 [元素释放][装备主动技能]对精灵下达协同攻击指令。 - 消耗150精灵之魂 一攻击时，精灵之魂 +10（冷却时间1秒） 一被击时，精灵之魂- 5（冷却时间1秒） - 元素释放伤害量:118,200%
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='火灵安珀', icon='/equipment/skill/29.png', cd=2, data=19200))
    char.equ_effect.append(EquEffect(name='水灵阿库娅', icon='/equipment/skill/29.png', cd=3, data=24000))
    char.equ_effect.append(EquEffect(name='风灵希尔珂', icon='/equipment/skill/29.png', cd=2, data=19200))
    char.SetStatus(SpeedM=0.15)
    char.equ_effect.append(EquEffect(name='元素释放', icon='/equipment/skill/29.png', cd=15, data=118200))
    pass


@register
def suit_38(char: CharacterProperty):
    # DCALC_REMOVE: suit_38 - 贵族精灵
    # level: 2
    # value: 召唤精灵一起战斗。 [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值 [水灵阿库娅] 每3秒施放一次水弹：伤害量24,000% 每3秒恢复1%的魔法值 [停止攻击开关][装备主动技能]控制精灵们的攻击。 一攻击中止/继续攻击 - 冷却时间1秒 [风灵希尔珂] 每2秒施放一次刀风：伤害量19,200% 移动速度 +15% [停止攻击开关][装备主动技能]控制精灵们的攻击。 - 攻击中止/继续攻击 - 冷却时间1秒 [元素释放][装备主动技能]对精灵下达协同攻击指令。 - 消耗150精灵之魂 一攻击时，精灵之魂 +10（冷却时间1秒） 一被击时，精灵之魂- 5（冷却时间1秒） - 元素释放伤害量:118,200%
    # rarity: 史诗
    suit_37(char)
    pass


@register
def suit_39(char: CharacterProperty):
    # DCALC_REMOVE: suit_39 - 贵族精灵
    # level: 3
    # value: 召唤精灵一起战斗。 [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值 [水灵阿库娅] 每3秒施放一次水弹：伤害量24,000% 每3秒恢复1%的魔法值 [停止攻击开关][装备主动技能]控制精灵们的攻击。 一攻击中止/继续攻击 - 冷却时间1秒 [风灵希尔珂] 每2秒施放一次刀风：伤害量19,200% 移动速度 +15% [停止攻击开关][装备主动技能]控制精灵们的攻击。 - 攻击中止/继续攻击 - 冷却时间1秒 [元素释放][装备主动技能]对精灵下达协同攻击指令。 - 消耗150精灵之魂 一攻击时，精灵之魂 +10（冷却时间1秒） 一被击时，精灵之魂- 5（冷却时间1秒） - 元素释放伤害量:118,200%
    # rarity: 史诗
    suit_37(char)
    pass


@register
def suit_40(char: CharacterProperty):
    # DCALC_REMOVE: suit_40 - 贵族精灵
    # level: 4
    # value: 召唤精灵一起战斗。 [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值 [水灵阿库娅] 每3秒施放一次水弹：伤害量24,000% 每3秒恢复1%的魔法值 [停止攻击开关][装备主动技能]控制精灵们的攻击。 - 攻击中止/继续攻击 - 冷却时间1秒 [风灵希尔珂] 每2秒施放一次刀风：伤害量19,200% 移动速度 +15% [停止攻击开关][装备主动技能]控制精灵们的攻击。 - 攻击中止/继续攻击 - 冷却时间1秒 [元素释放][装备主动技能]对精灵下达协同攻击指令。 - 消耗150精灵之魂 - 攻击时，精灵之魂 +10（冷却时间1秒） - 被击时，精灵之魂 -5（冷却时间1秒） - 元素释放伤害量:118,200%
    # rarity: 史诗
    suit_37(char)
    pass


@register
def suit_41(char: CharacterProperty):
    # DCALC_REMOVE: suit_41 - 贵族精灵
    # level: 5
    # value: 召唤精灵一起战斗。 [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值 [水灵阿库娅] 每3秒施放一次水弹：伤害量24,000% 每3秒恢复1%的魔法值 [停止攻击开关][装备主动技能]控制精灵们的攻击。 一攻击中止/继续攻击 - 冷却时间1秒 [风灵希尔珂] 每2秒施放一次刀风：伤害量19,200% 移动速度 +15% [停止攻击开关][装备主动技能]控制精灵们的攻击。 - 攻击中止/继续攻击 - 冷却时间1秒 [元素释放][装备主动技能]对精灵下达协同攻击指令。 - 消耗150精灵之魂 - 攻击时，精灵之魂 +10（冷却时间1秒） - 被击时，精灵之魂 -5（冷却时间1秒） - 元素释放伤害量:118,200%
    # rarity: 史诗
    suit_37(char)
    pass


@register
def suit_42(char: CharacterProperty):
    # DCALC_REMOVE: suit_42 - 皇室精灵
    # level: 1
    # value: 召唤精灵一起战斗。 [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值 [水灵阿库娅] 每3秒施放一次水弹：伤害量24,000% 每3秒恢复1%的魔法值 [停止攻击开关][装备主动技能]控制精灵们的攻击。 一攻击中止/继续攻击 - 冷却时间1秒 [风灵希尔珂] 每2秒施放一次刀风：伤害量19,200% 移动速度 +15% [精灵女王提泰妮娅]每5秒发动毁灭弹或毁灭斩击。 - 伤害量47,520% [停止攻击开关][装备主动技能]控制精灵们的攻击。 - 攻击中止/继续攻击 - 冷却时间1秒 [元素释放][装备主动技能]对精灵下达协同攻击指令。 - 消耗150精灵之魂 一攻击时，精灵之魂 +10（冷却时间1秒） 一被击时，精灵之魂- 5（冷却时间1秒） - 元素释放伤害量:118,200%
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='火灵安珀', icon='/equipment/skill/29.png', cd=2, data=19200))
    char.equ_effect.append(EquEffect(name='水灵阿库娅', icon='/equipment/skill/29.png', cd=3, data=24000))
    char.equ_effect.append(EquEffect(name='风灵希尔珂', icon='/equipment/skill/29.png', cd=2, data=19200))
    char.SetStatus(SpeedM=0.15)
    char.equ_effect.append(EquEffect(name='元素释放', icon='/equipment/skill/29.png', cd=10, data=181920))
    char.equ_effect.append(EquEffect(name='精灵女王提泰妮娅', icon='/equipment/skill/29.png', cd=5, data=47520))
    pass


# endregion
# region 理想之黄金乡


@register
def suit_43(char: CharacterProperty):
    # DCALC_REMOVE: suit_43 - 黄金乡 : 雏形
    # level: 1
    # value: -
    # rarity: 稀有
    pass


@register
def suit_44(char: CharacterProperty):
    # DCALC_REMOVE: suit_44 - 黄金乡 : 雏形
    # level: 2
    # value: -
    # rarity: 稀有
    pass


@register
def suit_45(char: CharacterProperty):
    # DCALC_REMOVE: suit_45 - 黄金乡 : 雏形
    # level: 3
    # value: -
    # rarity: 稀有
    pass


@register
def suit_46(char: CharacterProperty):
    # DCALC_REMOVE: suit_46 - 黄金乡 : 雏形
    # level: 4
    # value: -
    # rarity: 稀有
    pass


@register
def suit_47(char: CharacterProperty):
    # DCALC_REMOVE: suit_47 - 黄金乡 : 雏形
    # level: 5
    # value: -
    # rarity: 稀有
    pass


@register
def suit_48(char: CharacterProperty):
    # DCALC_REMOVE: suit_48 - 黄金乡 : 构想
    # level: 1
    # value: 根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。  - 数值总和每达到+11时，技能范围+2% (最多叠加7次) - 防具:数值每达到+5，所受物理/魔法伤害-1% (最多叠加7次) - 首饰:数值每达到+3，技能伤害+1% (最多叠加7次) - 特殊装备:数值每达到+3，所有速度+2% (最多叠加7次)    [辅助职业专属属性]  根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。 -数值总和每达到+11时，技能冷却时间-2%（最多叠加7次）
    # rarity: 神器
    reinforce_0 = 0
    """防具"""
    reinforce_1 = 0
    """首饰"""
    reinforce_2 = 0
    """特殊装备"""
    reinforce_3 = 0
    """武器"""
    for part in char.charEquipInfo.keys():
        if char.charEquipInfo[part] is None:
            continue
        num = char.charEquipInfo[part].reinforce
        if part == '武器':
            reinforce_3 += num
        if part in ['上衣', '头肩', '下装', '腰带', '鞋']:
            reinforce_0 += num
        if part in ['手镯', '项链', '戒指']:
            reinforce_1 += num
        if part in ['耳环', '辅助装备', '魔法石']:
            reinforce_2 += num
    reinforce = reinforce_0 + reinforce_1 + reinforce_2 + reinforce_3
    char.SetStatus(SkillRange=0.02 * min(reinforce // 11, 7))
    # char.SetStatus(DamageReduce=0.01 * min(reinforce_0 // 5, 7))
    char.SetStatus(SkillAttack=0.01 * min(reinforce_1 // 3, 7))
    char.SetStatus(SpeedA=0.02 * min(reinforce_2 // 3, 7))
    char.SetStatus(SpeedM=0.02 * min(reinforce_2 // 3, 7))
    char.SetStatus(SpeedR=0.02 * min(reinforce_2 // 3, 7))
    pass


@register
def suit_49(char: CharacterProperty):
    # DCALC_REMOVE: suit_49 - 黄金乡 : 构想
    # level: 2
    # value: 根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。  - 数值总和每达到+11时，技能范围+2% (最多叠加7次) - 防具:数值每达到+5，所受物理/魔法伤害-1% (最多叠加7次) - 首饰:数值每达到+3，技能伤害+1% (最多叠加7次) - 特殊装备:数值每达到+3，所有速度+2% (最多叠加7次)    [辅助职业专属属性]  根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。 -数值总和每达到+11时，技能冷却时间-2%（最多叠加7次）
    # rarity: 神器
    suit_48(char)
    pass


@register
def suit_50(char: CharacterProperty):
    # DCALC_REMOVE: suit_50 - 黄金乡 : 构想
    # level: 3
    # value: 根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。  - 数值总和每达到+11时，技能范围+2% (最多叠加7次) - 防具:数值每达到+5，所受物理/魔法伤害-1% (最多叠加7次) - 首饰:数值每达到+3，技能伤害+1% (最多叠加7次) - 特殊装备:数值每达到+3，所有速度+2% (最多叠加7次)    [辅助职业专属属性]  根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。 -数值总和每达到+11时，技能冷却时间-2%（最多叠加7次）
    # rarity: 神器
    suit_48(char)
    pass


@register
def suit_51(char: CharacterProperty):
    # DCALC_REMOVE: suit_51 - 黄金乡 : 构想
    # level: 4
    # value: 根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。  - 数值总和每达到+11时，技能范围+2% (最多叠加7次) - 防具:数值每达到+5，所受物理/魔法伤害-1% (最多叠加7次) - 首饰:数值每达到+3，技能伤害+1% (最多叠加7次) - 特殊装备:数值每达到+3，所有速度+2% (最多叠加7次)    [辅助职业专属属性]  根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。 -数值总和每达到+11时，技能冷却时间-2%（最多叠加7次）
    # rarity: 神器
    suit_48(char)
    pass


@register
def suit_52(char: CharacterProperty):
    # DCALC_REMOVE: suit_52 - 黄金乡 : 构想
    # level: 5
    # value: 根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。  - 数值总和每达到+11时，技能范围+2% (最多叠加7次) - 防具:数值每达到+5，所受物理/魔法伤害-1% (最多叠加7次) - 首饰:数值每达到+3，技能伤害+1% (最多叠加7次) - 特殊装备:数值每达到+3，所有速度+2% (最多叠加7次)    [辅助职业专属属性]  根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。 -数值总和每达到+11时，技能冷却时间-2%（最多叠加7次）
    # rarity: 神器
    suit_48(char)
    pass


@register
def suit_53(char: CharacterProperty):
    # DCALC_REMOVE: suit_53 - 黄金乡 : 梦想成真
    # level: 1
    # value: 根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。  - 数值总和每达到+11时，技能范围+2% (最多叠加7次) - 防具:数值每达到+5，所受物理/魔法伤害-1% (最多叠加7次) - 首饰:数值每达到+3，技能伤害+1% (最多叠加7次) - 特殊装备:数值每达到+3，所有速度+2% (最多叠加7次)    [辅助职业专属属性]  根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。 -数值总和每达到+11时，技能冷却时间-2%（最多叠加12次）
    # rarity: 传说

    reinforce_0 = 0
    """防具"""
    reinforce_1 = 0
    """首饰"""
    reinforce_2 = 0
    """特殊装备"""
    reinforce_3 = 0
    """武器"""
    for part in char.charEquipInfo.keys():
        if char.charEquipInfo[part] is None:
            continue
        num = char.charEquipInfo[part].reinforce
        if part == '武器':
            reinforce_3 += num
        if part in ['上衣', '头肩', '下装', '腰带', '鞋']:
            reinforce_0 += num
        if part in ['手镯', '项链', '戒指']:
            reinforce_1 += num
        if part in ['耳环', '辅助装备', '魔法石']:
            reinforce_2 += num
    reinforce = reinforce_0 + reinforce_1 + reinforce_2 + reinforce_3
    char.SetStatus(SkillRange=0.02 * min(reinforce // 11, 12))
    # char.SetStatus(DamageReduce=0.01 * min(reinforce_0 // 5, 7))
    char.SetStatus(SkillAttack=0.01 * min(reinforce_1 // 3, 12))
    char.SetStatus(SpeedA=0.02 * min(reinforce_2 // 3, 12))
    char.SetStatus(SpeedM=0.02 * min(reinforce_2 // 3, 12))
    char.SetStatus(SpeedR=0.02 * min(reinforce_2 // 3, 12))

    if char.buffer:
        char.SetSkillCD(cd=0.02 * min(reinforce // 1, 12))
    pass


@register
def suit_54(char: CharacterProperty):
    # DCALC_REMOVE: suit_54 - 黄金乡 : 梦想成真
    # level: 2
    # value: 根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。  - 数值总和每达到+11时，技能范围+2% (最多叠加12次) - 防具:数值每达到+5，所受物理/魔法伤害-1% (最多叠加12次) - 首饰:数值每达到+3，技能伤害+1% (最多叠加12次) - 特殊装备:数值每达到+3，所有速度+2% (最多叠加12次)    [辅助职业专属属性]  根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。 -数值总和每达到+11时，技能冷却时间-2%（最多叠加12次）
    # rarity: 传说

    suit_53(char)
    pass


@register
def suit_55(char: CharacterProperty):
    # DCALC_REMOVE: suit_55 - 黄金乡 : 梦想成真
    # level: 3
    # value: 根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。  - 数值总和每达到+11时，技能范围+2% (最多叠加12次) - 防具:数值每达到+5，所受物理/魔法伤害-1% (最多叠加12次) - 首饰:数值每达到+3，技能伤害+1% (最多叠加12次) - 特殊装备:数值每达到+3，所有速度+2% (最多叠加12次)    [辅助职业专属属性]  根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。 -数值总和每达到+11时，技能冷却时间-2%（最多叠加12次）
    # rarity: 传说
    suit_53(char)
    pass


@register
def suit_56(char: CharacterProperty):
    # DCALC_REMOVE: suit_56 - 黄金乡 : 梦想成真
    # level: 4
    # value: 根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。  - 数值总和每达到+11时，技能范围+2% (最多叠加12次) - 防具:数值每达到+5，所受物理/魔法伤害-1% (最多叠加12次) - 首饰:数值每达到+3，技能伤害+1% (最多叠加12次) - 特殊装备:数值每达到+3，所有速度+2% (最多叠加12次)    [辅助职业专属属性]  根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。 -数值总和每达到+11时，技能冷却时间-2%（最多叠加12次）
    # rarity: 传说
    suit_53(char)
    pass


@register
def suit_57(char: CharacterProperty):
    # DCALC_REMOVE: suit_57 - 黄金乡 : 梦想成真
    # level: 5
    # value: 根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。  - 数值总和每达到+11时，技能范围+2% (最多叠加12次) - 防具:数值每达到+5，所受物理/魔法伤害-1% (最多叠加12次) - 首饰:数值每达到+3，技能伤害+1% (最多叠加12次) - 特殊装备:数值每达到+3，所有速度+2% (最多叠加12次)    [辅助职业专属属性]  根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。 -数值总和每达到+11时，技能冷却时间-2%（最多叠加12次）
    # rarity: 传说
    suit_53(char)
    pass


@register
def suit_58(char: CharacterProperty):
    # DCALC_REMOVE: suit_58 - 黄金乡 : 璀璨理想
    # level: 1
    # value: 根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。 - 超过110时，每11点，技能伤害+2%（最多叠加2次） - 数值总和每达到+11时， 技能范围+2% (最多叠加12次) - 防具:数值每达到+5， 所受物理/魔法伤害-1% (最多叠加12次) - 首饰:数值每达到+3， 技能伤害+1% (最多叠加12次) - 特殊装备:数值每达到+3，所有速度+2% (最多叠加12次)  [淘银热]  根据防具/首饰/特殊装备的强化/增幅数值总和，降落相应数量的银币进行攻击（冷却时间10秒）  * 银币伤害量信息 - 低于88:9,600% - 88~109:10,440% - 110~131:12,000% - 132以上:14,400%  [辅助职业专属属性]  根据防具/首饰/特殊装备的强化/增幅数值总和，适用以下效果。 -数值综合每到达+11时，技能冷却时间-2% (最多叠加12次) - 110以上时，增益量+750(最多叠加2次)
    # rarity: 史诗
    reinforce_0 = 0
    """防具"""
    reinforce_1 = 0
    """首饰"""
    reinforce_2 = 0
    """特殊装备"""
    reinforce_3 = 0
    """武器"""
    for part in char.charEquipInfo.keys():
        if char.charEquipInfo is None:
            continue
        num = char.charEquipInfo[part].reinforce
        if part == '武器':
            reinforce_3 += num
        if part in ['上衣', '头肩', '下装', '腰带', '鞋']:
            reinforce_0 += num
        if part in ['手镯', '项链', '戒指']:
            reinforce_1 += num
        if part in ['耳环', '辅助装备', '魔法石']:
            reinforce_2 += num
    reinforce = reinforce_0 + reinforce_1 + reinforce_2 + reinforce_3
    char.SetStatus(SkillRange=0.02 * min(reinforce // 11, 12))
    # char.SetStatus(DamageReduce=0.01 * min(reinforce_0 // 5, 7))
    char.SetStatus(SkillAttack=0.01 * min(reinforce_1 // 3, 12))
    char.SetStatus(SpeedA=0.02 * min(reinforce_2 // 3, 12))
    char.SetStatus(SpeedM=0.02 * min(reinforce_2 // 3, 12))
    char.SetStatus(SpeedR=0.02 * min(reinforce_2 // 3, 12))

    if char.buffer:
        char.SetSkillCD(cd=0.02 * min(reinforce // 1, 12))

    if reinforce >= 110:
        char.SetStatus(SkillAttack=0.02 * min((reinforce - 110) // 11, 2))

        if char.buffer:
            char.SetStatus(Buffer=750 * min((reinforce - 110) // 11, 2))

    if reinforce < 88:
        char.equ_effect.append(EquEffect(name='淘银热', icon='/equipment/suit/0.png', cd=10, data=9600))
    elif reinforce < 110:
        char.equ_effect.append(EquEffect(name='淘银热', icon='/equipment/suit/0.png', cd=10, data=10440))
    elif reinforce < 132:
        char.equ_effect.append(EquEffect(name='淘银热', icon='/equipment/suit/0.png', cd=10, data=12000))
    else:
        char.equ_effect.append(EquEffect(name='淘银热', icon='/equipment/suit/0.png', cd=10, data=14400))
    pass


@register
def suit_59(char: CharacterProperty):
    # DCALC_REMOVE: suit_59 - 黄金乡 : 璀璨理想
    # level: 2
    # value: 根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。 - 超过110时，每11点，技能伤害+2%（最多叠加2次） - 数值总和每达到+11时， 技能范围+2% (最多叠加12次) - 防具:数值每达到+5， 所受物理/魔法伤害-1% (最多叠加12次) - 首饰:数值每达到+3， 技能伤害+1% (最多叠加12次) - 特殊装备:数值每达到+3，所有速度+2% (最多叠加12次)  [淘银热]  根据防具/首饰/特殊装备的强化/增幅数值总和，降落相应数量的银币进行攻击（冷却时间10秒）  * 银币伤害量信息 - 低于88:9,600% - 88~109:10,440% - 110~131:12,000% - 132以上:14,400%  [辅助职业专属属性]  根据防具/首饰/特殊装备的强化/增幅数值总和，适用以下效果。 -数值综合每到达+11时，技能冷却时间-2% (最多叠加12次) - 110以上时，增益量+750(最多叠加2次)
    # rarity: 史诗
    suit_58(char)
    pass


@register
def suit_60(char: CharacterProperty):
    # DCALC_REMOVE: suit_60 - 黄金乡 : 璀璨理想
    # level: 3
    # value: 根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。 - 超过110时，每11点，技能伤害+2%（最多叠加2次） - 数值总和每达到+11时， 技能范围+2% (最多叠加12次) - 防具:数值每达到+5， 所受物理/魔法伤害-1% (最多叠加12次) - 首饰:数值每达到+3， 技能伤害+1% (最多叠加12次) - 特殊装备:数值每达到+3，所有速度+2% (最多叠加12次)  [淘银热]  根据防具/首饰/特殊装备的强化/增幅数值总和，降落相应数量的银币进行攻击（冷却时间10秒）  * 银币伤害量信息 - 低于88:9,600% - 88~109:10,440% - 110~131:12,000% - 132以上:14,400%  [辅助职业专属属性]  根据防具/首饰/特殊装备的强化/增幅数值总和，适用以下效果。 -数值综合每到达+11时，技能冷却时间-2% (最多叠加12次) - 110以上时，增益量+750(最多叠加2次)
    # rarity: 史诗
    suit_58(char)
    pass


@register
def suit_61(char: CharacterProperty):
    # DCALC_REMOVE: suit_61 - 黄金乡 : 璀璨理想
    # level: 4
    # value: 根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。 - 超过110时，每11点，增加2%技能伤害（最多叠加2次） - 数值总和每达到 +11时， 技能范围增加2% (最多叠加12次) - 防具 : 数值每达到 +5， 所受物理/魔法伤害 - 1% (最多叠加12次) - 首饰 : 数值每达到 +3， 技能伤害  +1% (最多叠加12次) - 特殊装备 : 数值每达到 +3， 所有速度  +2% (最多叠加12次)  [淘银热]  根据防具/首饰/特殊装备的强化/增幅数值总和，降落相应数量的银币进行攻击（冷却时间10秒）  * 银币伤害量信息 - 低于88 : 9,600%% - 88 ~ 109 : 10,440% - 110 ~ 131 : 12,000% - 132以上 : 14,400%  [辅助职业专属属性]  根据防具/首饰/特殊装备的强化/增幅数值总和，适用以下效果。 -数值综合每到达+11时，技能冷却时间-2% (最多叠加12次) - 110以上时，增益量+750(最多叠加2次)
    # rarity: 史诗
    suit_58(char)
    pass


@register
def suit_62(char: CharacterProperty):
    # DCALC_REMOVE: suit_62 - 黄金乡 : 璀璨理想
    # level: 5
    # value: 根据防具/首饰/特殊装备的强化/增幅数值总和，适用以下效果。 - 超过110时，每11点，技能伤害+2%（最多叠加2次） - 数值总和每达到+11时，技能范围+2% (最多叠加12次) - 防具:数值每达到+5，所受物理/魔法伤害-1% (最多叠加12次) - 首饰:数值每达到+3，技能伤害+1% (最多叠加12次) - 特殊装备:数值每达到+3，所有速度+2% (最多叠加12次)  [淘银热]  根据防具/首饰/特殊装备的强化/增幅数值总和，降落相应数量的银币进行攻击（冷却时间10秒）  * 银币伤害量信息 - 低于88:9,600% - 88~109:10,440% - 110~131:12,000% - 132以上:14,400%  [辅助职业专属属性]  根据防具/首饰/特殊装备的强化/增幅数值总和，适用以下效果。 -数值综合每到达+11时，技能冷却时间-2% (最多叠加12次) - 110以上时，增益量+750(最多叠加2次)
    # rarity: 史诗
    suit_58(char)
    pass


@register
def suit_63(char: CharacterProperty):
    # DCALC_REMOVE: suit_63 - 黄金乡 : 永恒国度
    # level: 1
    # value: 根据防具/首饰/特殊装备的强化/增幅数值总和，适用以下效果。 - 超过110时，每11点，技能伤害+2%（最多叠加2次） - 数值总和每达到+11时，技能范围+2% (最多叠加12次) - 防具:数值每达到+5，所受物理/魔法伤-1% (最多叠加12次) - 首饰:数值每达到+3，技能伤害+1% (最多叠加12次) - 特殊装备:数值每达到+3，所有速度+2%(最多叠加12次)  [淘银热]  根据防具/首饰/特殊装备的强化/增幅数值总和，降落相应数量的银币进行攻击（冷却时间10秒）  * 银币伤害量信息 - 低于88:9,600% - 88~109:10,440% - 110~131:12,000% - 132以上:14,400%  [辅助职业专属属性]  根据防具/首饰/特殊装备的强化/增幅数值总和，适用以下效果。 -数值综合每到达+11时，技能冷却时间-2% (最多叠加12次) - 110以上时，数值每达到 +11，增益量+1500 (最多叠加2次)
    # rarity: 太初
    reinforce_0 = 0
    """防具"""
    reinforce_1 = 0
    """首饰"""
    reinforce_2 = 0
    """特殊装备"""
    reinforce_3 = 0
    """武器"""
    for part in char.charEquipInfo.keys():
        if char.charEquipInfo[part] is None:
            continue
        num = char.charEquipInfo[part].reinforce
        if part == '武器':
            reinforce_3 += num
        if part in ['上衣', '头肩', '下装', '腰带', '鞋']:
            reinforce_0 += num
        if part in ['手镯', '项链', '戒指']:
            reinforce_1 += num
        if part in ['耳环', '辅助装备', '魔法石']:
            reinforce_2 += num
    reinforce = reinforce_0 + reinforce_1 + reinforce_2 + reinforce_3
    char.SetStatus(SkillRange=0.02 * min(reinforce // 11, 12))
    # char.SetStatus(DamageReduce=0.01 * min(reinforce_0 // 5, 7))
    char.SetStatus(SkillAttack=0.01 * min(reinforce_1 // 3, 12))
    char.SetStatus(SpeedA=0.02 * min(reinforce_2 // 3, 12))
    char.SetStatus(SpeedM=0.02 * min(reinforce_2 // 3, 12))
    char.SetStatus(SpeedR=0.02 * min(reinforce_2 // 3, 12))

    if char.buffer:
        char.SetSkillCD(cd=0.02 * min(reinforce // 1, 12))

    if reinforce >= 110:
        char.SetStatus(SkillAttack=0.02 * min((reinforce - 110) // 11, 2))

        if char.buffer:
            char.SetStatus(Buffer=1500 * min((reinforce - 110) // 11, 2))

    if reinforce < 88:
        char.equ_effect.append(EquEffect(name='淘银热', icon='/equipment/suit/0.png', cd=10, data=9600))
    elif reinforce < 110:
        char.equ_effect.append(EquEffect(name='淘银热', icon='/equipment/suit/0.png', cd=10, data=10440))
    elif reinforce < 132:
        char.equ_effect.append(EquEffect(name='淘银热', icon='/equipment/suit/0.png', cd=10, data=12000))
    else:
        char.equ_effect.append(EquEffect(name='淘银热', icon='/equipment/suit/0.png', cd=10, data=14400))
    pass


# endregion
# region 龙战八荒


@register
def suit_64(char: CharacterProperty):
    # DCALC_REMOVE: suit_64 - 蒙昧未觉之螭龙
    # level: 1
    # value: -
    # rarity: 稀有
    pass


@register
def suit_65(char: CharacterProperty):
    # DCALC_REMOVE: suit_65 - 蒙昧未觉之螭龙
    # level: 2
    # value: -
    # rarity: 稀有
    pass


@register
def suit_66(char: CharacterProperty):
    # DCALC_REMOVE: suit_66 - 蒙昧未觉之螭龙
    # level: 3
    # value: -
    # rarity: 稀有
    pass


@register
def suit_67(char: CharacterProperty):
    # DCALC_REMOVE: suit_67 - 蒙昧未觉之螭龙
    # level: 4
    # value: -
    # rarity: 稀有
    pass


@register
def suit_68(char: CharacterProperty):
    # DCALC_REMOVE: suit_68 - 蒙昧未觉之螭龙
    # level: 5
    # value: -
    # rarity: 稀有
    pass


@register
def suit_69(char: CharacterProperty):
    # DCALC_REMOVE: suit_69 - 鸿蒙初开之虬龙
    # level: 1
    # value: [虬龙之火] 无色小晶块消耗量减少1个。 所有速度  +10%
    # rarity: 神器
    char.SetStatus(SpeedA=0.1, SpeedM=0.1, SpeedR=0.1)
    pass


@register
def suit_70(char: CharacterProperty):
    # DCALC_REMOVE: suit_70 - 鸿蒙初开之虬龙
    # level: 2
    # value: [虬龙之火] 无色小晶块消耗量减少1个。 所有速度  +10%
    # rarity: 神器
    suit_69(char)
    pass


@register
def suit_71(char: CharacterProperty):
    # DCALC_REMOVE: suit_71 - 鸿蒙初开之虬龙
    # level: 3
    # value: [虬龙之火] 无色小晶块消耗量减少1个。 所有速度  +10%
    # rarity: 神器
    suit_69(char)
    pass


@register
def suit_72(char: CharacterProperty):
    # DCALC_REMOVE: suit_72 - 鸿蒙初开之虬龙
    # level: 4
    # value: [虬龙之火] 无色小晶块消耗量减少1个。 所有速度  +10%
    # rarity: 神器
    suit_69(char)
    pass


@register
def suit_73(char: CharacterProperty):
    # DCALC_REMOVE: suit_73 - 鸿蒙初开之虬龙
    # level: 5
    # value: [虬龙之火] 无色小晶块消耗量减少1个。 所有速度  +10%
    # rarity: 神器
    suit_69(char)
    pass


@register
def suit_74(char: CharacterProperty):
    # DCALC_REMOVE: suit_74 - 鸡鸣拂晓之蛟龙
    # level: 1
    # value: [蛟龙之火] 无色小晶块消耗量减少2个。 所有速度  +10%  [蛟龙腾霄] 攻击时，蛟龙腾霄。 (冷却时间10秒) * 青龙升天伤害量 : 14,400%
    # rarity: 传说
    char.SetStatus(SpeedA=0.1, SpeedM=0.1, SpeedR=0.1)
    char.equ_effect.append(EquEffect(name='龙之胜战', icon='/equipment/suit/1.png', cd=10, data=14400))
    pass


@register
def suit_75(char: CharacterProperty):
    # DCALC_REMOVE: suit_75 - 鸡鸣拂晓之蛟龙
    # level: 2
    # value: [蛟龙之火] 无色小晶块消耗量减少2个。 所有速度  +10%  [蛟龙腾霄] 攻击时，蛟龙腾霄。 (冷却时间10秒) * 青龙升天伤害量 : 14,400%
    # rarity: 传说
    suit_74(char)
    pass


@register
def suit_76(char: CharacterProperty):
    # DCALC_REMOVE: suit_76 - 鸡鸣拂晓之蛟龙
    # level: 3
    # value: [蛟龙之火] 无色小晶块消耗量减少2个。 所有速度  +10%  [蛟龙腾霄] 攻击时，蛟龙腾霄。 (冷却时间10秒) * 青龙升天伤害量 : 14,400%
    # rarity: 传说
    suit_74(char)
    pass


@register
def suit_77(char: CharacterProperty):
    # DCALC_REMOVE: suit_77 - 鸡鸣拂晓之蛟龙
    # level: 4
    # value: [蛟龙之火] 无色小晶块消耗量减少2个。 所有速度  +10%  [蛟龙腾霄] 攻击时，蛟龙腾霄。 (冷却时间10秒) * 青龙升天伤害量 : 14,400%
    # rarity: 传说
    suit_74(char)
    pass


@register
def suit_78(char: CharacterProperty):
    # DCALC_REMOVE: suit_78 - 鸡鸣拂晓之蛟龙
    # level: 5
    # value: [蛟龙之火] 无色小晶块消耗量减少2个。 所有速度  +10%  [蛟龙腾霄] 攻击时，蛟龙腾霄。 (冷却时间10秒) * 青龙升天伤害量 : 14,400%
    # rarity: 传说
    suit_74(char)
    pass


@register
def suit_79(char: CharacterProperty):
    # DCALC_REMOVE: suit_79 - 朝露晨辉之烛龙
    # level: 1
    # value: 通过释放龙之力来增强自己。 [烛龙之火] 无色小晶块消耗量减少3个。 -不会减少到少于1个 所有速度  +10% [烛龙腾霄] 攻击时，烛龙腾霄。（冷却时间10秒） *烛龙腾霄伤害量:14,400% [荧惑如意珠][装备主动技能] 将[烛龙之火]变更为[烛龙的如意珠]，效果持续30秒。 - 删除无色小晶块消耗量减少效果 - 所有速度增加效果变更为30% - 技能伤害 +3% - 无色小晶块技能的消耗量固定30个 一施放消耗无色小晶块的技能时，发动白龙强袭（冷却时间3秒） * 白龙强袭伤害量:6,000% - 冷却时间60秒
    # rarity: 史诗
    if char.equ_options.get('1', 0) == 0:
        char.SetStatus(SpeedA=0.1, SpeedM=0.1, SpeedR=0.1)
        char.equ_effect.append(EquEffect(name='烛龙腾霄', icon='/equipment/suit/1.png', cd=10, data=14400))
    elif char.equ_options.get('1', 0) == 1:
        char.SetStatus(SpeedA=0.3, SpeedM=0.3, SpeedR=0.3)
        char.SetStatus(SkillAttack=0.03)
        char.equ_effect.append(EquEffect(name='白龙强袭', icon='/equipment/suit/1.png', cd=3, data=6000))
    elif char.equ_options.get('1', 0) == 2:
        char.SetStatus(SpeedA=0.2, SpeedM=0.2, SpeedR=0.2)
        char.SetStatus(SkillAttack=0.015)
        char.equ_effect.append(EquEffect(name='白龙强袭', icon='/equipment/suit/1.png', cd=3, data=6000))
        char.equ_effect.append(EquEffect(name='烛龙腾霄', icon='/equipment/suit/1.png', cd=10, data=14400))
    pass


@register
def suit_80(char: CharacterProperty):
    # DCALC_REMOVE: suit_80 - 朝露晨辉之烛龙
    # level: 2
    # value: 通过释放龙之力来增强自己。 [烛龙之火] 无色小晶块消耗量减少3个。 -不会减少到少于1个 所有速度  +10% [烛龙腾霄] 攻击时，烛龙腾霄。（冷却时间10秒） *烛龙腾霄伤害量:14,400% [荧惑如意珠][装备主动技能] 将[烛龙之火]变更为[烛龙的如意珠]，效果持续30秒。 - 删除无色小晶块消耗量减少效果 - 所有速度增加效果变更为30% - 技能伤害 +3% - 无色小晶块技能的消耗量固定30个 一施放消耗无色小晶块的技能时，发动白龙强袭（冷却时间3秒） * 白龙强袭伤害量:6,000% - 冷却时间60秒
    # rarity: 史诗
    suit_79(char)
    pass


@register
def suit_81(char: CharacterProperty):
    # DCALC_REMOVE: suit_81 - 朝露晨辉之烛龙
    # level: 3
    # value: 通过释放龙之力来增强自己。 [烛龙之火] 无色小晶块消耗量减少3个。 -不会减少到少于1个 所有速度  +10% [烛龙腾霄] 攻击时，烛龙腾霄。（冷却时间10秒） *烛龙腾霄伤害量:14,400% [荧惑如意珠][装备主动技能] 将[烛龙之火]变更为[烛龙的如意珠]，效果持续30秒。 - 删除无色小晶块消耗量减少效果 - 所有速度增加效果变更为30% - 技能伤害 +3% - 无色小晶块技能的消耗量固定30个 一施放消耗无色小晶块的技能时，发动白龙强袭（冷却时间3秒） * 白龙强袭伤害量:6,000% - 冷却时间60秒
    # rarity: 史诗
    suit_79(char)
    pass


@register
def suit_82(char: CharacterProperty):
    # DCALC_REMOVE: suit_82 - 朝露晨辉之烛龙
    # level: 4
    # value: 通过释放龙之力来增强自己。 [烛龙之火] 无色小晶块消耗量减少3个。 -不会减少到少于1个 所有速度  +10% [烛龙腾霄] 攻击时，烛龙腾霄。（冷却时间10秒） *烛龙腾霄伤害量:14,400% [荧惑如意珠][装备主动技能] 将[烛龙之火]变更为[烛龙的如意珠]，效果持续30秒。 - 删除无色小晶块消耗量减少效果 - 所有速度增加效果变更为30% - 技能伤害 +3% - 无色小晶块技能的消耗量固定30个 一施放消耗无色小晶块的技能时，发动白龙强袭（冷却时间3秒） * 白龙强袭伤害量:6,000% - 冷却时间60秒
    # rarity: 史诗
    suit_79(char)
    pass


@register
def suit_83(char: CharacterProperty):
    # DCALC_REMOVE: suit_83 - 朝露晨辉之烛龙
    # level: 5
    # value: 通过释放龙之力来增强自己。 [烛龙之火] 无色小晶块消耗量减少3个。 -不会减少到少于1个 所有速度  +10% [烛龙腾霄] 攻击时，烛龙腾霄。（冷却时间10秒） *烛龙腾霄伤害量:14,400% [荧惑如意珠][装备主动技能] 将[烛龙之火]变更为[烛龙的如意珠]，效果持续30秒。 - 删除无色小晶块消耗量减少效果 - 所有速度增加效果变更为30% - 技能伤害 +3% - 无色小晶块技能的消耗量固定30个 一施放消耗无色小晶块的技能时，发动白龙强袭（冷却时间3秒） * 白龙强袭伤害量:6,000% - 冷却时间60秒
    # rarity: 史诗
    suit_79(char)
    pass


@register
def suit_84(char: CharacterProperty):
    # DCALC_REMOVE: suit_84 - 明光耀世之应龙
    # level: 1
    # value: [应龙之火] 无色小晶块消耗量减少5个。 -不会减少到小于1个 所有速度  +10%  [应龙腾霄] 攻击时，应龙腾霄。（冷却时间10秒） * 应龙腾霄伤害量:14,400% [荧惑如意珠][装备主动技能] 将[应龙之火]变更为[应龙的如意珠] -删除无色小晶块消耗量减少效果 - 所有速度增加效果变更为30% - 技能伤害 +3% - 无色小晶块技能的消耗量固定15个 -施放消耗无色小晶块的技能时，白龙强袭（冷却时间3秒） * 白龙强袭伤害量:6,000% - 再次使用，解除效果 [应龙之怒] [应龙的如意珠]效果生效状态下攻击时，黑龙横扫敌人。（冷却时间4秒） *横扫伤害量:7,200%
    # rarity: 太初
    if char.equ_options.get('1', 0) == 0:
        char.SetStatus(SpeedA=0.1, SpeedM=0.1, SpeedR=0.1)
        char.equ_effect.append(EquEffect(name='烛龙腾霄', icon='/equipment/suit/1.png', cd=10, data=14400))
    elif char.equ_options.get('1', 0) == 1:
        char.SetStatus(SpeedA=0.3, SpeedM=0.3, SpeedR=0.3)
        char.SetStatus(SkillAttack=0.03)
        char.equ_effect.append(EquEffect(name='白龙强袭', icon='/equipment/suit/1.png', cd=3, data=6000))
        char.equ_effect.append(EquEffect(name='应龙之怒', icon='/equipment/suit/1.png', cd=4, data=7200))
    pass


# endregion
# region 暗黑净化


@register
def suit_85(char: CharacterProperty):
    # DCALC_REMOVE: suit_85 - 混沌净化：初始
    # level: 1
    # value: -
    # rarity: 稀有
    pass


@register
def suit_86(char: CharacterProperty):
    # DCALC_REMOVE: suit_86 - 混沌净化：初始
    # level: 2
    # value: -
    # rarity: 稀有
    pass


@register
def suit_87(char: CharacterProperty):
    # DCALC_REMOVE: suit_87 - 混沌净化：初始
    # level: 3
    # value: -
    # rarity: 稀有
    pass


@register
def suit_88(char: CharacterProperty):
    # DCALC_REMOVE: suit_88 - 混沌净化：初始
    # level: 4
    # value: -
    # rarity: 稀有
    pass


@register
def suit_89(char: CharacterProperty):
    # DCALC_REMOVE: suit_89 - 混沌净化：初始
    # level: 5
    # value: -
    # rarity: 稀有
    pass


@register
def suit_90(char: CharacterProperty):
    # DCALC_REMOVE: suit_90 - 混沌净化：挣扎
    # level: 1
    # value: 进入地下城时， 净化状态自动生效  [净化] - 技能冷却时间 - 30.0%（觉醒技能除外） - 每秒恢复0.5%生命值/魔法值
    # rarity: 神器
    char.SetSkillCD(cd=0.3)
    pass


@register
def suit_91(char: CharacterProperty):
    # DCALC_REMOVE: suit_91 - 混沌净化：挣扎
    # level: 2
    # value: 进入地下城时， 净化状态自动生效  [净化] - 技能冷却时间 - 30.0%（觉醒技能除外） - 每秒恢复0.5%生命值/魔法值
    # rarity: 神器
    suit_90(char)
    pass


@register
def suit_92(char: CharacterProperty):
    # DCALC_REMOVE: suit_92 - 混沌净化：挣扎
    # level: 3
    # value: 进入地下城时， 净化状态自动生效  [净化] - 技能冷却时间 - 30.0%（觉醒技能除外） - 每秒恢复0.5%生命值/魔法值
    # rarity: 神器
    suit_90(char)
    pass


@register
def suit_93(char: CharacterProperty):
    # DCALC_REMOVE: suit_93 - 混沌净化：挣扎
    # level: 4
    # value: 进入地下城时， 净化状态自动生效  [净化] - 技能冷却时间 - 30.0%（觉醒技能除外） - 每秒恢复0.5%生命值/魔法值
    # rarity: 神器
    suit_90(char)
    pass


@register
def suit_94(char: CharacterProperty):
    # DCALC_REMOVE: suit_94 - 混沌净化：挣扎
    # level: 5
    # value: 进入地下城时， 净化状态自动生效  [净化] - 技能冷却时间 - 30.0%（觉醒技能除外） - 每秒恢复0.5%生命值/魔法值
    # rarity: 神器
    suit_90(char)
    pass


@register
def suit_95(char: CharacterProperty):
    # DCALC_REMOVE: suit_95 - 混沌净化：失衡
    # level: 1
    # value: [暗黑净化][装备主动技能]根据使用者的意愿调整净化与堕落状态。 - 进入地下城时，净化状态自动生效 - 冷却时间：300秒 [净化] - 技能伤害  +17.5% - 技能冷却时间- 30%（觉醒技能除外） - 每秒恢复0.5%的生命值和魔法值 [堕落] - 技能冷却时间- 55%（觉醒技能除外） - 进入霸体状态
    # rarity: 传说
    if char.equ_options.get('2', 0) == 0:
        char.SetStatus(SkillAttack=0.175)
        char.SetSkillCD(cd=0.3)
    else:
        char.SetSkillCD(cd=0.55)
    pass


@register
def suit_96(char: CharacterProperty):
    # DCALC_REMOVE: suit_96 - 混沌净化：失衡
    # level: 2
    # value: [暗黑净化][装备主动技能]根据使用者的意愿调整净化与堕落状态。 - 进入地下城时，净化状态自动生效 - 冷却时间：300秒 [净化] - 技能伤害  +17.5% - 技能冷却时间- 30%（觉醒技能除外） - 每秒恢复0.5%的生命值和魔法值 [堕落] - 技能冷却时间- 55%（觉醒技能除外） - 进入霸体状态
    # rarity: 传说
    suit_95(char)
    pass


@register
def suit_97(char: CharacterProperty):
    # DCALC_REMOVE: suit_97 - 混沌净化：失衡
    # level: 3
    # value: [暗黑净化][装备主动技能]根据使用者的意愿调整净化与堕落状态。 - 进入地下城时，净化状态自动生效 - 冷却时间：300秒 [净化] - 技能伤害  +17.5% - 技能冷却时间- 30%（觉醒技能除外） - 每秒恢复0.5%的生命值和魔法值 [堕落] - 技能冷却时间- 55%（觉醒技能除外） - 进入霸体状态
    # rarity: 传说
    suit_95(char)
    pass


@register
def suit_98(char: CharacterProperty):
    # DCALC_REMOVE: suit_98 - 混沌净化：失衡
    # level: 4
    # value: [暗黑净化][装备主动技能]根据使用者的意愿调整净化与堕落状态。 - 进入地下城时，净化状态自动生效 - 冷却时间：300秒 [净化] - 技能伤害  +17.5% - 技能冷却时间- 30%（觉醒技能除外） - 每秒恢复0.5%的生命值和魔法值 [堕落] - 技能冷却时间- 55%（觉醒技能除外） - 进入霸体状态
    # rarity: 传说
    suit_95(char)
    pass


@register
def suit_99(char: CharacterProperty):
    # DCALC_REMOVE: suit_99 - 混沌净化：失衡
    # level: 5
    # value: [暗黑净化][装备主动技能]根据使用者的意愿调整净化与堕落状态。 - 进入地下城时，净化状态自动生效 - 冷却时间：300秒 [净化] - 技能伤害  +17.5% - 技能冷却时间- 30%（觉醒技能除外） - 每秒恢复0.5%的生命值和魔法值 [堕落] - 技能冷却时间- 55%（觉醒技能除外） - 进入霸体状态
    # rarity: 传说
    suit_95(char)
    pass


@register
def suit_100(char: CharacterProperty):
    # DCALC_REMOVE: suit_100 - 混沌净化：协调
    # level: 1
    # value: [暗黑净化][装备主动技能] 根据使用者的意愿调整净化与堕落状态。 - 进入地下城时，净化状态自动生效 - 冷却时间：300秒 [净化] - 技能伤害 +17.5% - 技能冷却时间- 30%（觉醒技能除外） - 每秒恢复0.5%的生命值和魔法值 - 每10秒生成最大生命值10%的保护罩 [堕落] - 技能冷却时间- 55%（觉醒技能除外） - 进入霸体状态 - 跳跃时可以再跳跃一次
    # rarity: 史诗
    suit_95(char)
    pass


@register
def suit_101(char: CharacterProperty):
    # DCALC_REMOVE: suit_101 - 混沌净化：协调
    # level: 2
    # value: [暗黑净化][装备主动技能] 根据使用者的意愿调整净化与堕落状态。 - 进入地下城时，净化状态自动生效 - 冷却时间：300秒 [净化] - 技能伤害 +17.5% - 技能冷却时间- 30%（觉醒技能除外） - 每秒恢复0.5%的生命值和魔法值 - 每10秒生成最大生命值10%的保护罩 [堕落] - 技能冷却时间- 55%（觉醒技能除外） - 进入霸体状态 - 跳跃时可以再跳跃一次
    # rarity: 史诗
    suit_95(char)
    pass


@register
def suit_102(char: CharacterProperty):
    # DCALC_REMOVE: suit_102 - 混沌净化：协调
    # level: 3
    # value: [暗黑净化][装备主动技能] 根据使用者的意愿调整净化与堕落状态。 - 进入地下城时，净化状态自动生效 - 冷却时间：300秒 [净化] - 技能伤害 +17.5% - 技能冷却时间- 30%（觉醒技能除外） - 每秒恢复0.5%的生命值和魔法值 - 每10秒生成最大生命值10%的保护罩 [堕落] - 技能冷却时间- 55%（觉醒技能除外） - 进入霸体状态 - 跳跃时可以再跳跃一次
    # rarity: 史诗
    suit_95(char)
    pass


@register
def suit_103(char: CharacterProperty):
    # DCALC_REMOVE: suit_103 - 混沌净化：协调
    # level: 4
    # value: [暗黑净化][装备主动技能] 根据使用者的意愿调整净化与堕落状态。 - 进入地下城时，净化状态自动生效 - 冷却时间：300秒 [净化] - 技能伤害 +17.5% - 技能冷却时间- 30%（觉醒技能除外） - 每秒恢复0.5%的生命值和魔法值 - 每10秒生成最大生命值10%的保护罩 [堕落] - 技能冷却时间- 55%（觉醒技能除外） - 进入霸体状态 - 跳跃时可以再跳跃一次
    # rarity: 史诗
    suit_95(char)
    pass


@register
def suit_104(char: CharacterProperty):
    # DCALC_REMOVE: suit_104 - 混沌净化：协调
    # level: 5
    # value: [暗黑净化][装备主动技能] 根据使用者的意愿调整净化与堕落状态。 - 进入地下城时，净化状态自动生效 - 冷却时间：300秒 [净化] - 技能伤害 +17.5% - 技能冷却时间- 30%（觉醒技能除外） - 每秒恢复0.5%的生命值和魔法值 - 每10秒生成最大生命值10%的保护罩 [堕落] - 技能冷却时间- 55%（觉醒技能除外） - 进入霸体状态 - 跳跃时可以再跳跃一次
    # rarity: 史诗
    suit_95(char)
    pass


@register
def suit_105(char: CharacterProperty):
    # DCALC_REMOVE: suit_105 - 混沌净化：均衡
    # level: 1
    # value: 净化与堕落达到协调后， 进入均衡状态。  [均衡] - 每秒恢复0.5%生命值/魔法值 - 每10秒生成最大生命值10%的保护罩 - 进入霸体状态 - 跳跃时可以再跳跃一次  [暗黑净化] [装备发动属性] 选择使用净化和堕落的力量。 进入地下城时， 净化状态自动生效 - 冷却时间300秒  [净化] - 技能伤害  +17.5% - 技能冷却时间 - 30.0%（觉醒技能除外）  [堕落] - 技能冷却时间 - 55.0%（觉醒技能除外）
    # rarity: 太初
    suit_95(char)
    pass


# endregion
# region 天命者的气运


@register
def suit_106(char: CharacterProperty):
    # DCALC_REMOVE: suit_106 - 天命者的微妙气运
    # level: 1
    # value: -
    # rarity: 稀有
    pass


@register
def suit_107(char: CharacterProperty):
    # DCALC_REMOVE: suit_107 - 天命者的微妙气运
    # level: 2
    # value: -
    # rarity: 稀有
    pass


@register
def suit_108(char: CharacterProperty):
    # DCALC_REMOVE: suit_108 - 天命者的微妙气运
    # level: 3
    # value: -
    # rarity: 稀有
    pass


@register
def suit_109(char: CharacterProperty):
    # DCALC_REMOVE: suit_109 - 天命者的微妙气运
    # level: 4
    # value: -
    # rarity: 稀有
    pass


@register
def suit_110(char: CharacterProperty):
    # DCALC_REMOVE: suit_110 - 天命者的微妙气运
    # level: 5
    # value: -
    # rarity: 稀有
    pass


@register
def suit_111(char: CharacterProperty):
    # DCALC_REMOVE: suit_111 - 天命者的华丽气运
    # level: 1
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] -技能伤害+3%  [天命所归] -攻击时，有1%几率发动[天命所归]。（发动机会冷却时间1秒） -剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外）
    # rarity: 神器
    char.SetStatus(SkillAttack=0.03)
    pass


@register
def suit_112(char: CharacterProperty):
    # DCALC_REMOVE: suit_112 - 天命者的华丽气运
    # level: 2
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] -技能伤害+3%  [天命所归] -攻击时，有1%几率发动[天命所归]。（发动机会冷却时间1秒） -剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外）
    # rarity: 神器
    suit_111(char)
    pass


@register
def suit_113(char: CharacterProperty):
    # DCALC_REMOVE: suit_113 - 天命者的华丽气运
    # level: 3
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] -技能伤害+3%  [天命所归] -攻击时，有1%几率发动[天命所归]。（发动机会冷却时间1秒） -剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外）
    # rarity: 神器
    suit_111(char)
    pass


@register
def suit_114(char: CharacterProperty):
    # DCALC_REMOVE: suit_114 - 天命者的华丽气运
    # level: 4
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] -技能伤害+3%  [天命所归] -攻击时，有1%几率发动[天命所归]。（发动机会冷却时间1秒） -剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外）
    # rarity: 神器
    suit_111(char)
    pass


@register
def suit_115(char: CharacterProperty):
    # DCALC_REMOVE: suit_115 - 天命者的华丽气运
    # level: 5
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] -技能伤害+3%  [天命所归] -攻击时，有1%几率发动[天命所归]。（发动机会冷却时间1秒） -剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外）
    # rarity: 神器
    suit_111(char)
    pass


@register
def suit_116(char: CharacterProperty):
    # DCALC_REMOVE: suit_116 - 天命者的华丽气运
    # level: 1
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] -技能伤害+3%  [第二次幸运] -攻击时，有3%的几率使所有属性强化+33（持续时间33秒；发动机会冷却时间1秒）  [天命所归] -攻击时，有3%几率发动[天命所归]。（发动机会冷却时间1秒） -剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外） -剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外） -立即发动[第二次幸运]
    # rarity: 传说
    char.SetStatus(SkillAttack=0.03)
    char.AddElementDB('火',33,1)
    char.AddElementDB('冰',33,1)
    char.AddElementDB('光',33,1)
    char.AddElementDB('暗',33,1)
    pass


@register
def suit_117(char: CharacterProperty):
    # DCALC_REMOVE: suit_117 - 天命者的耀眼气运
    # level: 2
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] -技能伤害+3%  [第二次幸运] -攻击时，有3%的几率使所有属性强化+33（持续时间33秒；发动机会冷却时间1秒）  [天命所归] -攻击时，有3%几率发动[天命所归]。（发动机会冷却时间1秒） -剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外） -剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外） -立即发动[第二次幸运]
    # rarity: 传说
    suit_116(char)
    pass


@register
def suit_118(char: CharacterProperty):
    # DCALC_REMOVE: suit_118 - 天命者的耀眼气运
    # level: 3
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] -技能伤害+3%  [第二次幸运] -攻击时，有3%的几率使所有属性强化+33（持续时间33秒；发动机会冷却时间1秒）  [天命所归] -攻击时，有3%几率发动[天命所归]。（发动机会冷却时间1秒） -剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外） -剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外） -立即发动[第二次幸运]
    # rarity: 传说
    suit_116(char)
    pass


@register
def suit_119(char: CharacterProperty):
    # DCALC_REMOVE: suit_119 - 天命者的耀眼气运
    # level: 4
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] -技能伤害+3%  [第二次幸运] -攻击时，有3%的几率使所有属性强化+33（持续时间33秒；发动机会冷却时间1秒）  [天命所归] -攻击时，有3%几率发动[天命所归]。（发动机会冷却时间1秒） -剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外） -剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外） -立即发动[第二次幸运]
    # rarity: 传说
    suit_116(char)
    pass


@register
def suit_120(char: CharacterProperty):
    # DCALC_REMOVE: suit_120 - 天命者的耀眼气运
    # level: 5
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] -技能伤害+3%  [第二次幸运] -攻击时，有3%的几率使所有属性强化+33（持续时间33秒；发动机会冷却时间1秒）  [天命所归] -攻击时，有3%几率发动[天命所归]。（发动机会冷却时间1秒） -剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外） -剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外） -立即发动[第二次幸运]
    # rarity: 传说
    suit_116(char)
    pass


@register
def suit_121(char: CharacterProperty):
    # DCALC_REMOVE: suit_121 - 天命者的璀璨气运
    # level: 1
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] -技能伤害+3%  [第二次幸运] -攻击时，有3%的几率使所有属性强化+33（持续时间33秒；发动机会冷却时间1秒）  [天命所归] -攻击时，有3%几率发动[天命所归]。（发动机会冷却时间1秒） -剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外） -剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外） -立即发动[第二次幸运]  [幸运之翼][装备主动技能] -[第二次幸运]、[天命所归]发动几率提高3倍，效果持续33秒 -冷却时间：99秒 -立即发动[第二次幸运]
    # rarity: 史诗
    suit_116(char)
    pass


@register
def suit_122(char: CharacterProperty):
    # DCALC_REMOVE: suit_122 - 天命者的璀璨气运
    # level: 2
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] -技能伤害+3%  [第二次幸运] -攻击时，有3%的几率使所有属性强化+33（持续时间33秒；发动机会冷却时间1秒）  [天命所归] -攻击时，有3%几率发动[天命所归]。（发动机会冷却时间1秒） -剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外） -剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外） -立即发动[第二次幸运]  [幸运之翼][装备主动技能] -[第二次幸运]、[天命所归]发动几率提高3倍，效果持续33秒 -冷却时间：99秒 -立即发动[第二次幸运]
    # rarity: 史诗
    suit_116(char)
    pass


@register
def suit_123(char: CharacterProperty):
    # DCALC_REMOVE: suit_123 - 天命者的璀璨气运
    # level: 3
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] -技能伤害+3%  [第二次幸运] -攻击时，有3%的几率使所有属性强化+33（持续时间33秒；发动机会冷却时间1秒）  [天命所归] -攻击时，有3%几率发动[天命所归]。（发动机会冷却时间1秒） -剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外） -剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外） -立即发动[第二次幸运]  [幸运之翼][装备主动技能] -[第二次幸运]、[天命所归]发动几率提高3倍，效果持续33秒 -冷却时间：99秒 -立即发动[第二次幸运]
    # rarity: 史诗
    suit_116(char)
    pass


@register
def suit_124(char: CharacterProperty):
    # DCALC_REMOVE: suit_124 - 天命者的璀璨气运
    # level: 4
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] -技能伤害+3%  [第二次幸运] -攻击时，有3%的几率使所有属性强化+33（持续时间33秒；发动机会冷却时间1秒）  [天命所归] -攻击时，有3%几率发动[天命所归]。（发动机会冷却时间1秒） -剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外） -剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外） -立即发动[第二次幸运]  [幸运之翼][装备主动技能] -[第二次幸运]、[天命所归]发动几率提高3倍，效果持续33秒 -冷却时间：99秒 -立即发动[第二次幸运]
    # rarity: 史诗
    suit_116(char)
    pass


@register
def suit_125(char: CharacterProperty):
    # DCALC_REMOVE: suit_125 - 天命者的璀璨气运
    # level: 5
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] -技能伤害+3%  [第二次幸运] -攻击时，有3%的几率使所有属性强化+33（持续时间33秒；发动机会冷却时间1秒）  [天命所归] -攻击时，有3%几率发动[天命所归]。（发动机会冷却时间1秒） -剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外） -剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外） -立即发动[第二次幸运]  [幸运之翼][装备主动技能] -[第二次幸运]、[天命所归]发动几率提高3倍，效果持续33秒 -冷却时间：99秒 -立即发动[第二次幸运]
    # rarity: 史诗
    suit_116(char)
    pass


@register
def suit_126(char: CharacterProperty):
    # DCALC_REMOVE: suit_126 - 天命者的梦幻气运
    # level: 1
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] -技能伤害+3%  [第二次幸运] -攻击时，有3%的几率使所有属性强化+33（持续时间33秒；发动机会冷却时间1秒）  [天命所归] -攻击时，有3%几率发动[天命所归]。（发动机会冷却时间1秒） -剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外） -剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外） -立即发动[第二次幸运]  [幸运之翼][装备主动技能] -[第二次幸运]、[天命所归]发动几率提高3倍，效果持续33秒 -冷却时间：99秒 -立即发动[第二次幸运]
    # rarity: 太初
    suit_116(char)
    pass


# endregion
# region 究极能量


@register
def suit_127(char: CharacterProperty):
    # DCALC_REMOVE: suit_127 - 最初的能量
    # level: 1
    # value: -
    # rarity: 稀有
    pass


@register
def suit_128(char: CharacterProperty):
    # DCALC_REMOVE: suit_128 - 最初的能量
    # level: 2
    # value: -
    # rarity: 稀有
    pass


@register
def suit_129(char: CharacterProperty):
    # DCALC_REMOVE: suit_129 - 最初的能量
    # level: 3
    # value: -
    # rarity: 稀有
    pass


@register
def suit_130(char: CharacterProperty):
    # DCALC_REMOVE: suit_130 - 最初的能量
    # level: 4
    # value: -
    # rarity: 稀有
    pass


@register
def suit_131(char: CharacterProperty):
    # DCALC_REMOVE: suit_131 - 最初的能量
    # level: 5
    # value: -
    # rarity: 稀有
    pass


@register
def suit_132(char: CharacterProperty):
    # DCALC_REMOVE: suit_132 - 涌动的能量
    # level: 1
    # value: [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力  +30% - 85级技能攻击力  +30% - 85级技能冷却时间 - 30% - 50级技能冷却时间 - 30%   *组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性
    # rarity: 神器
    if not char.buffer:
        char.SetSkillCD(50,50,0.3,[])
        char.SetSkillCD(85,85,0.3,[])
    char.SetSkillRation(100,100,0.3)
    char.SetSkillRation(85,85,0.3)
    pass


@register
def suit_133(char: CharacterProperty):
    # DCALC_REMOVE: suit_133 - 涌动的能量
    # level: 2
    # value: [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力  +30% - 85级技能攻击力  +30% - 85级技能冷却时间 - 30% - 50级技能冷却时间 - 30%   *组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性
    # rarity: 神器
    suit_132(char)
    pass


@register
def suit_134(char: CharacterProperty):
    # DCALC_REMOVE: suit_134 - 涌动的能量
    # level: 3
    # value: [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力  +30% - 85级技能攻击力  +30% - 85级技能冷却时间 - 30% - 50级技能冷却时间 - 30%   *组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性
    # rarity: 神器
    suit_132(char)
    pass


@register
def suit_135(char: CharacterProperty):
    # DCALC_REMOVE: suit_135 - 涌动的能量
    # level: 4
    # value: [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力  +30% - 85级技能攻击力  +30% - 85级技能冷却时间 - 30% - 50级技能冷却时间 - 30%   *组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性
    # rarity: 神器
    suit_132(char)
    pass


@register
def suit_136(char: CharacterProperty):
    # DCALC_REMOVE: suit_136 - 涌动的能量
    # level: 5
    # value: [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力  +30% - 85级技能攻击力  +30% - 85级技能冷却时间 - 30% - 50级技能冷却时间 - 30%   *组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性
    # rarity: 神器
    suit_132(char)
    pass


@register
def suit_137(char: CharacterProperty):
    # DCALC_REMOVE: suit_137 - 满溢的能量
    # level: 1
    # value: [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力  +40% - 85级技能攻击力  +40% - 100级技能冷却时间 -50% - 85级技能冷却时间 - 30% - 50级技能冷却时间 - 50%   *组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性
    # rarity: 传说
    if not char.buffer:
        char.SetSkillCD(50,50,0.5,[])
        char.SetSkillCD(85,85,0.3,[])
        char.SetSkillCD(100,100,0.5,[])
    char.SetSkillRation(100,100,0.4)
    char.SetSkillRation(85,85,0.4)
    pass


@register
def suit_138(char: CharacterProperty):
    # DCALC_REMOVE: suit_138 - 满溢的能量
    # level: 2
    # value: [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力  +40% - 85级技能攻击力  +40% - 100级技能冷却时间 -50% - 85级技能冷却时间 - 30% - 50级技能冷却时间 - 50%   *组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性
    # rarity: 传说
    suit_137(char)
    pass


@register
def suit_139(char: CharacterProperty):
    # DCALC_REMOVE: suit_139 - 满溢的能量
    # level: 3
    # value: [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力  +40% - 85级技能攻击力  +40% - 100级技能冷却时间 -50% - 85级技能冷却时间 - 30% - 50级技能冷却时间 - 50%   *组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性
    # rarity: 传说
    suit_137(char)
    pass


@register
def suit_140(char: CharacterProperty):
    # DCALC_REMOVE: suit_140 - 满溢的能量
    # level: 4
    # value: [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力  +40% - 85级技能攻击力  +40% - 100级技能冷却时间 -50% - 85级技能冷却时间 - 30% - 50级技能冷却时间 - 50%   *组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性
    # rarity: 传说
    suit_137(char)
    pass


@register
def suit_141(char: CharacterProperty):
    # DCALC_REMOVE: suit_141 - 满溢的能量
    # level: 5
    # value: [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力  +40% - 85级技能攻击力  +40% - 100级技能冷却时间 -50% - 85级技能冷却时间 - 30% - 50级技能冷却时间 - 50%   *组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性
    # rarity: 传说
    suit_137(char)
    pass


@register
def suit_142(char: CharacterProperty):
    # DCALC_REMOVE: suit_142 - 极限的能量
    # level: 1
    # value: [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力  +60% - 85级技能攻击力  +50% - 50级技能攻击力 +10% - 100级技能冷却时间 -50% - 85级技能冷却时间 - 30% - 50级技能冷却时间 - 50%   *组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性  [抵达极限的能量] 释放三觉技能时，进入能量填充状态，效果持续15秒。（最多填充15次） - 每秒填充 +1 - 每消耗1个无色小晶块，填充 +1（最多填充5次）  达到最大填充后，释放能量造成大量伤害。 * 能量释放伤害量：240000%
    # rarity: 史诗
    if not char.buffer:
        char.SetSkillCD(50,50,0.5,[])
        char.SetSkillCD(85,85,0.3,[])
        char.SetSkillCD(100,100,0.5,[])
    char.SetSkillRation(100,100,0.6)
    char.SetSkillRation(85,85,0.5)
    char.SetSkillRation(50,50,0.1)
    cd = 0
    for item in char.skills:
        if item.learnLv == 100:
            cd = item.getSkillCD()
    char.equ_effect.append(EquEffect(name='能量释放', icon='/equipment/suit/4.png', cd=cd, data=240000))
    pass


@register
def suit_143(char: CharacterProperty):
    # DCALC_REMOVE: suit_143 - 极限的能量
    # level: 2
    # value: [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力  +60% - 85级技能攻击力  +50% - 50级技能攻击力 +10% - 100级技能冷却时间 -50% - 85级技能冷却时间 - 30% - 50级技能冷却时间 - 50%   *组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性  [抵达极限的能量] 释放三觉技能时，进入能量填充状态，效果持续15秒。（最多填充15次） - 每秒填充 +1 - 每消耗1个无色小晶块，填充 +1（最多填充5次）  达到最大填充后，释放能量造成大量伤害。 * 能量释放伤害量：240000%
    # rarity: 史诗
    suit_142(char)
    pass


@register
def suit_144(char: CharacterProperty):
    # DCALC_REMOVE: suit_144 - 极限的能量
    # level: 3
    # value: [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力  +60% - 85级技能攻击力  +50% - 50级技能攻击力 +10% - 100级技能冷却时间 -50% - 85级技能冷却时间 - 30% - 50级技能冷却时间 - 50%   *组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性  [抵达极限的能量] 释放三觉技能时，进入能量填充状态，效果持续15秒。（最多填充15次） - 每秒填充 +1 - 每消耗1个无色小晶块，填充 +1（最多填充5次）  达到最大填充后，释放能量造成大量伤害。 * 能量释放伤害量：240000%
    # rarity: 史诗
    suit_142(char)
    pass


@register
def suit_145(char: CharacterProperty):
    # DCALC_REMOVE: suit_145 - 极限的能量
    # level: 4
    # value: [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力  +60% - 85级技能攻击力  +50% - 50级技能攻击力 +10% - 100级技能冷却时间 -50% - 85级技能冷却时间 - 30% - 50级技能冷却时间 - 50%   *组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性  [抵达极限的能量] 释放三觉技能时，进入能量填充状态，效果持续15秒。（最多填充15次） - 每秒填充 +1 - 每消耗1个无色小晶块，填充 +1（最多填充5次）  达到最大填充后，释放能量造成大量伤害。 * 能量释放伤害量：240000%
    # rarity: 史诗
    suit_142(char)
    pass


@register
def suit_146(char: CharacterProperty):
    # DCALC_REMOVE: suit_146 - 极限的能量
    # level: 5
    # value: [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力  +60% - 85级技能攻击力  +50% - 50级技能攻击力 +10% - 100级技能冷却时间 -50% - 85级技能冷却时间 - 30% - 50级技能冷却时间 - 50%   *组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性  [抵达极限的能量] 释放三觉技能时，进入能量填充状态，效果持续15秒。（最多填充15次） - 每秒填充 +1 - 每消耗1个无色小晶块，填充 +1（最多填充5次）  达到最大填充后，释放能量造成大量伤害。 * 能量释放伤害量：240000%
    # rarity: 史诗
    suit_142(char)
    pass


@register
def suit_147(char: CharacterProperty):
    # DCALC_REMOVE: suit_147 - 超越极限的能量
    # level: 1
    # value: [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力  +76% - 85级技能攻击力  +60% - 50级技能攻击力 +15% - 100级技能冷却时间 -50% - 85级技能冷却时间 - 30% - 50级技能冷却时间 - 50%   *组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性  [抵达极限的能量] 释放三觉技能时，进入能量填充状态，效果持续15秒。（最多填充15次） - 每秒填充 +1 - 每消耗1个无色小晶块，填充 +1（最多填充5次）  达到最大填充后，释放能量造成大量伤害。 * 能量释放伤害量：360000%
    # rarity: 太初
    if not char.buffer:
        char.SetSkillCD(50,50,0.5,[])
        char.SetSkillCD(85,85,0.3,[])
        char.SetSkillCD(100,100,0.5,[])
    char.SetSkillRation(100,100,0.76)
    char.SetSkillRation(85,85,0.6)
    char.SetSkillRation(50,50,0.15)
    cd = 0
    for item in char.skills:
        if item.learnLv == 100:
            cd = item.getSkillCD()
    char.equ_effect.append(EquEffect(name='能量释放', icon='/equipment/suit/4.png', cd=cd, data=360000))
    pass


# endregion
# region 造化自然


@register
def suit_148(char: CharacterProperty):
    # DCALC_REMOVE: suit_148 - 自然的造化
    # level: 1
    # value: -
    # rarity: 稀有
    pass


@register
def suit_149(char: CharacterProperty):
    # DCALC_REMOVE: suit_149 - 自然的造化
    # level: 2
    # value: -
    # rarity: 稀有
    pass


@register
def suit_150(char: CharacterProperty):
    # DCALC_REMOVE: suit_150 - 自然的造化
    # level: 3
    # value: -
    # rarity: 稀有
    pass


@register
def suit_151(char: CharacterProperty):
    # DCALC_REMOVE: suit_151 - 自然的造化
    # level: 4
    # value: -
    # rarity: 稀有
    pass


@register
def suit_152(char: CharacterProperty):
    # DCALC_REMOVE: suit_152 - 自然的造化
    # level: 5
    # value: -
    # rarity: 稀有
    pass


@register
def suit_153(char: CharacterProperty):
    # DCALC_REMOVE: suit_153 - 自然的干预
    # level: 1
    # value: [无可违背的自然 - 干预] 攻击时引发自然爆炸攻击敌人。 (冷却时间5秒) - 自然燃烧伤害8,640%
    # rarity: 神器
    pass


@register
def suit_154(char: CharacterProperty):
    # DCALC_REMOVE: suit_154 - 自然的干预
    # level: 2
    # value: [无可违背的自然 - 干预] 攻击时引发自然爆炸攻击敌人。 (冷却时间5秒) - 自然燃烧伤害8,640%
    # rarity: 神器
    char.equ_effect.append(EquEffect(name='自燃爆炸', icon='/equipment/suit/6.png', cd=5, data=8640))
    pass


@register
def suit_155(char: CharacterProperty):
    # DCALC_REMOVE: suit_155 - 自然的干预
    # level: 3
    # value: [无可违背的自然 - 干预] 攻击时引发自然爆炸攻击敌人。 (冷却时间5秒) - 自然燃烧伤害8,640%
    # rarity: 神器
    suit_154(char)
    pass


@register
def suit_156(char: CharacterProperty):
    # DCALC_REMOVE: suit_156 - 自然的干预
    # level: 4
    # value: [无可违背的自然 - 干预] 攻击时引发自然爆炸攻击敌人。 (冷却时间5秒) - 自然燃烧伤害8,640%
    # rarity: 神器
    suit_154(char)
    pass


@register
def suit_157(char: CharacterProperty):
    # DCALC_REMOVE: suit_157 - 自然的干预
    # level: 5
    # value: [无可违背的自然 - 干预] 攻击时引发自然爆炸攻击敌人。 (冷却时间5秒) - 自然燃烧伤害8,640%
    # rarity: 神器
    suit_154(char)
    pass


@register
def suit_158(char: CharacterProperty):
    # DCALC_REMOVE: suit_158 - 自然的震怒
    # level: 1
    # value: [无可违背的自然 - 震怒] 攻击时产生小型旋风， 攻击小范围的敌人， 并吸附敌人。 (冷却时间5秒) - 小型旋风伤害25920%
    # rarity: 传说
    char.equ_effect.append(EquEffect(name='小型旋风', icon='/equipment/suit/6.png', cd=5, data=25920))
    pass


@register
def suit_159(char: CharacterProperty):
    # DCALC_REMOVE: suit_159 - 自然的震怒
    # level: 2
    # value: [无可违背的自然 - 震怒] 攻击时产生小型旋风， 攻击小范围的敌人， 并吸附敌人。 (冷却时间5秒) - 小型旋风伤害25920%
    # rarity: 传说
    suit_158(char)
    pass


@register
def suit_160(char: CharacterProperty):
    # DCALC_REMOVE: suit_160 - 自然的震怒
    # level: 3
    # value: [无可违背的自然 - 震怒] 攻击时产生小型旋风， 攻击小范围的敌人， 并吸附敌人。 (冷却时间5秒) - 小型旋风伤害25920%
    # rarity: 传说
    suit_158(char)
    pass


@register
def suit_161(char: CharacterProperty):
    # DCALC_REMOVE: suit_161 - 自然的震怒
    # level: 4
    # value: [无可违背的自然 - 震怒] 攻击时产生小型旋风， 攻击小范围的敌人， 并吸附敌人。 (冷却时间5秒) - 小型旋风伤害25920%
    # rarity: 传说
    suit_158(char)
    pass


@register
def suit_162(char: CharacterProperty):
    # DCALC_REMOVE: suit_162 - 自然的震怒
    # level: 5
    # value: [无可违背的自然 - 震怒] 攻击时产生小型旋风， 攻击小范围的敌人， 并吸附敌人。 (冷却时间5秒) - 小型旋风伤害25920%
    # rarity: 传说
    suit_158(char)
    pass


@register
def suit_163(char: CharacterProperty):
    # DCALC_REMOVE: suit_163 - 自然的制裁
    # level: 1
    # value: [无可违背的自然 - 制裁] 攻击时引发落雷， 攻击大范围敌人。 (冷却时间5秒) - 落雷伤害43,200%
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='落雷', icon='/equipment/suit/6.png', cd=5, data=43200))
    pass


@register
def suit_164(char: CharacterProperty):
    # DCALC_REMOVE: suit_164 - 自然的制裁
    # level: 2
    # value: [无可违背的自然 - 制裁] 攻击时引发落雷， 攻击大范围敌人。 (冷却时间5秒) - 落雷伤害43,200%
    # rarity: 史诗
    suit_163(char)
    pass


@register
def suit_165(char: CharacterProperty):
    # DCALC_REMOVE: suit_165 - 自然的制裁
    # level: 3
    # value: [无可违背的自然 - 制裁] 攻击时引发落雷， 攻击大范围敌人。 (冷却时间5秒) - 落雷伤害43,200%
    # rarity: 史诗
    suit_163(char)
    pass


@register
def suit_166(char: CharacterProperty):
    # DCALC_REMOVE: suit_166 - 自然的制裁
    # level: 4
    # value: [无可违背的自然 - 制裁] 攻击时引发落雷， 攻击大范围敌人。 (冷却时间5秒) - 落雷伤害43,200%
    # rarity: 史诗
    suit_163(char)
    pass


@register
def suit_167(char: CharacterProperty):
    # DCALC_REMOVE: suit_167 - 自然的制裁
    # level: 5
    # value: [无可违背的自然 - 制裁] 攻击时引发落雷， 攻击大范围敌人。 (冷却时间5秒) - 落雷伤害43,200%
    # rarity: 史诗
    suit_163(char)
    pass


@register
def suit_168(char: CharacterProperty):
    # DCALC_REMOVE: suit_168 - 自然的灾变
    # level: 1
    # value: 利用无可违背的自然之力，对敌人造成巨大伤害。 [无可违背的自然- 灾变]攻击时引发暴风雪，攻击地图上的所有敌人。（冷却时间5秒） - 暴风雪伤害量 60,480% [狂澜怒涛][装备主动技能] 发动狂澜怒涛，攻击地图上的所有敌人。 - 狂澜怒涛伤害量104,400% - 冷却时间：60秒
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='狂澜怒涛', icon='/equipment/skill/54.png', cd=60, data=104400))
    char.equ_effect.append(EquEffect(name='暴风雪', icon='/equipment/suit/6.png', cd=5, data=60480))
    pass


# endregion
# region 诸神黄昏之女武神


@register
def suit_169(char: CharacterProperty):
    # DCALC_REMOVE: suit_169 - 女武神 - 英勇的战士
    # level: 1
    # value: -
    # rarity: 稀有
    pass


@register
def suit_170(char: CharacterProperty):
    # DCALC_REMOVE: suit_170 - 女武神 - 英勇的战士
    # level: 2
    # value: -
    # rarity: 稀有
    pass


@register
def suit_171(char: CharacterProperty):
    # DCALC_REMOVE: suit_171 - 女武神 - 英勇的战士
    # level: 3
    # value: -
    # rarity: 稀有
    pass


@register
def suit_172(char: CharacterProperty):
    # DCALC_REMOVE: suit_172 - 女武神 - 英勇的战士
    # level: 4
    # value: -
    # rarity: 稀有
    pass


@register
def suit_173(char: CharacterProperty):
    # DCALC_REMOVE: suit_173 - 女武神 - 英勇的战士
    # level: 5
    # value: -
    # rarity: 稀有
    pass


@register
def suit_174(char: CharacterProperty):
    # DCALC_REMOVE: suit_174 - 女武神 - 战场的先锋
    # level: 1
    # value: 借用女武神的一部分神秘力量。  [突破] [装备发动属性] 与女武神融合， 向前方突进。 - 正面突破伤害 : 6,360% - 冷却时间8秒
    # rarity: 神器
    char.equ_effect.append(EquEffect(name='突破', icon='/equipment/skill/0.png', cd=8, data=6360))
    pass


@register
def suit_175(char: CharacterProperty):
    # DCALC_REMOVE: suit_175 - 女武神 - 战场的先锋
    # level: 2
    # value: 借用女武神的一部分神秘力量。  [突破] [装备发动属性] 与女武神融合， 向前方突进。 - 正面突破伤害 : 6,360% - 冷却时间8秒
    # rarity: 神器
    suit_174(char)
    pass


@register
def suit_176(char: CharacterProperty):
    # DCALC_REMOVE: suit_176 - 女武神 - 战场的先锋
    # level: 3
    # value: 借用女武神的一部分神秘力量。  [突破] [装备发动属性] 与女武神融合， 向前方突进。 - 正面突破伤害 : 6,360% - 冷却时间8秒
    # rarity: 神器
    suit_174(char)
    pass


@register
def suit_177(char: CharacterProperty):
    # DCALC_REMOVE: suit_177 - 女武神 - 战场的先锋
    # level: 4
    # value: 借用女武神的一部分神秘力量。  [突破] [装备发动属性] 与女武神融合， 向前方突进。 - 正面突破伤害 : 6,360% - 冷却时间8秒
    # rarity: 神器
    suit_174(char)
    pass


@register
def suit_178(char: CharacterProperty):
    # DCALC_REMOVE: suit_178 - 女武神 - 战场的先锋
    # level: 5
    # value: 借用女武神的一部分神秘力量。  [突破] [装备发动属性] 与女武神融合， 向前方突进。 - 正面突破伤害 : 6,360% - 冷却时间8秒
    # rarity: 神器
    suit_174(char)
    pass


@register
def suit_179(char: CharacterProperty):
    # DCALC_REMOVE: suit_179 - 女武神 - 逆袭的战魂
    # level: 1
    # value: 借用女武神的一部分神秘力量。  [突破] [装备发动属性] 与女武神融合， 向前方突进。 - 正面突破伤害 : 6,360% - 冷却时间8秒  [审判][装备发动属性] 与女武神融合， 移动到敌人后方进行攻击。 - 审判伤害 : 9,300% - 冷却时间15秒
    # rarity: 传说
    char.equ_effect.append(EquEffect(name='突破', icon='/equipment/skill/0.png', cd=8, data=6360))
    char.equ_effect.append(EquEffect(name='审判', icon='/equipment/skill/1.png', cd=15, data=9300))
    pass


@register
def suit_180(char: CharacterProperty):
    # DCALC_REMOVE: suit_180 - 女武神 - 逆袭的战魂
    # level: 2
    # value: 借用女武神的一部分神秘力量。  [突破] [装备发动属性] 与女武神融合， 向前方突进。 - 正面突破伤害 : 6,360% - 冷却时间8秒  [审判][装备发动属性] 与女武神融合， 移动到敌人后方进行攻击。 - 审判伤害 : 9,300% - 冷却时间15秒
    # rarity: 传说
    suit_179(char)
    pass


@register
def suit_181(char: CharacterProperty):
    # DCALC_REMOVE: suit_181 - 女武神 - 逆袭的战魂
    # level: 3
    # value: 借用女武神的一部分神秘力量。  [突破] [装备发动属性] 与女武神融合， 向前方突进。 - 正面突破伤害 : 6,360% - 冷却时间8秒  [审判][装备发动属性] 与女武神融合， 移动到敌人后方进行攻击。 - 审判伤害 : 9,300% - 冷却时间15秒
    # rarity: 传说
    suit_179(char)
    pass


@register
def suit_182(char: CharacterProperty):
    # DCALC_REMOVE: suit_182 - 女武神 - 逆袭的战魂
    # level: 4
    # value: 借用女武神的一部分神秘力量。  [突破] [装备发动属性] 与女武神融合， 向前方突进。 - 正面突破伤害 : 6,360% - 冷却时间8秒  [审判][装备发动属性] 与女武神融合， 移动到敌人后方进行攻击。 - 审判伤害 : 9,300% - 冷却时间15秒
    # rarity: 传说
    suit_179(char)
    pass


@register
def suit_183(char: CharacterProperty):
    # DCALC_REMOVE: suit_183 - 女武神 - 逆袭的战魂
    # level: 5
    # value: 借用女武神的一部分神秘力量。  [突破] [装备发动属性] 与女武神融合， 向前方突进。 - 正面突破伤害 : 6,360% - 冷却时间8秒  [审判][装备发动属性] 与女武神融合， 移动到敌人后方进行攻击。 - 审判伤害 : 9,300% - 冷却时间15秒
    # rarity: 传说
    suit_179(char)
    pass


@register
def suit_184(char: CharacterProperty):
    # DCALC_REMOVE: suit_184 - 女武神 - 不灭的英雄
    # level: 1
    # value: 借用女武神的一部分神秘力量。  [突破] [装备发动属性]  与女武神融合， 向前方突进。 - 正面突破伤害 : 6,360% - 冷却时间8秒  [审判][装备发动属性] 与女武神融合， 移动到敌人后方进行攻击。 - 审判伤害 : 9,300% - 冷却时间15秒  每施放8次无色小晶块技能时， 发动[天罚] 。 (冷却时间20秒)  [天罚] 召唤女武神， 对四周敌人施以天罚。 - 天罚伤害 : 136800%
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='突破', icon='/equipment/skill/0.png', cd=8, data=6360))
    char.equ_effect.append(EquEffect(name='审判', icon='/equipment/skill/1.png', cd=15, data=9300))
    char.equ_effect.append(EquEffect(name='天罚', icon='/equipment/suit/7.png', cd=20, data=136800))
    pass


@register
def suit_185(char: CharacterProperty):
    # DCALC_REMOVE: suit_185 - 女武神 - 不灭的英雄
    # level: 2
    # value: 借用女武神的一部分神秘力量。  [突破] [装备发动属性]  与女武神融合， 向前方突进。 - 正面突破伤害 : 6,360% - 冷却时间8秒  [审判][装备发动属性] 与女武神融合， 移动到敌人后方进行攻击。 - 审判伤害 : 9,300% - 冷却时间15秒  每施放8次无色小晶块技能时， 发动[天罚] 。 (冷却时间20秒)  [天罚] 召唤女武神， 对四周敌人施以天罚。 - 天罚伤害 : 136800%
    # rarity: 史诗
    suit_184(char)
    pass


@register
def suit_186(char: CharacterProperty):
    # DCALC_REMOVE: suit_186 - 女武神 - 不灭的英雄
    # level: 3
    # value: 借用女武神的一部分神秘力量。  [突破] [装备发动属性]  与女武神融合， 向前方突进。 - 正面突破伤害 : 6,360% - 冷却时间8秒  [审判][装备发动属性] 与女武神融合， 移动到敌人后方进行攻击。 - 审判伤害 : 9,300% - 冷却时间15秒  每施放8次无色小晶块技能时， 发动[天罚] 。 (冷却时间20秒)  [天罚] 召唤女武神， 对四周敌人施以天罚。 - 天罚伤害 : 136800%
    # rarity: 史诗
    suit_184(char)
    pass

@register
def suit_187(char: CharacterProperty):
    # DCALC_REMOVE: suit_187 - 女武神 - 不灭的英雄
    # level: 4
    # value: 借用女武神的一部分神秘力量。  [突破] [装备发动属性]  与女武神融合， 向前方突进。 - 正面突破伤害 : 6,360% - 冷却时间8秒  [审判][装备发动属性] 与女武神融合， 移动到敌人后方进行攻击。 - 审判伤害 : 9,300% - 冷却时间15秒  每施放8次无色小晶块技能时， 发动[天罚] 。 (冷却时间20秒)  [天罚] 召唤女武神， 对四周敌人施以天罚。 - 天罚伤害 : 136800%
    # rarity: 史诗
    suit_184(char)
    pass


@register
def suit_188(char: CharacterProperty):
    # DCALC_REMOVE: suit_188 - 女武神 - 不灭的英雄
    # level: 5
    # value: 借用女武神的一部分神秘力量。  [突破] [装备发动属性]  与女武神融合， 向前方突进。 - 正面突破伤害 : 6,360% - 冷却时间8秒  [审判][装备发动属性] 与女武神融合， 移动到敌人后方进行攻击。 - 审判伤害 : 9,300% - 冷却时间15秒  每施放8次无色小晶块技能时， 发动[天罚] 。 (冷却时间20秒)  [天罚] 召唤女武神， 对四周敌人施以天罚。 - 天罚伤害 : 136800%
    # rarity: 史诗
    suit_184(char)
    pass


@register
def suit_189(char: CharacterProperty):
    # DCALC_REMOVE: suit_189 - 女武神 - 英灵的引导者
    # level: 1
    # value: 借用女武神的一部分神秘力量。  [突破] [装备发动属性] 与女武神融合， 向前方突进。 - 正面突破伤害 : 6,360% - 冷却时间8秒  [审判][装备发动属性] 与女武神融合， 移动到敌人后方进行攻击。 - 审判伤害 : 9,300% - 冷却时间15秒  [降临][装备发动属性] 发挥女武神真正的力量， 降临世间。 - 降临伤害 : 329,400% - 冷却时间140秒  每施放8次无色小晶块技能时， 发动[天罚] 。 (冷却时间20秒)  [天罚] 召唤女武神， 对四周敌人施以天罚。 - 天罚伤害 : 136800%
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='突破', icon='/equipment/skill/0.png', cd=8, data=6360))
    char.equ_effect.append(EquEffect(name='审判', icon='/equipment/skill/1.png', cd=15, data=9300))
    char.equ_effect.append(EquEffect(name='降临', icon='/equipment/skill/3.png', cd=140, data=329400))
    char.equ_effect.append(EquEffect(name='天罚', icon='/equipment/suit/7.png', cd=20, data=136800))
    pass


# endregion
# region 青丘灵珠


@register
def suit_190(char: CharacterProperty):
    # DCALC_REMOVE: suit_190 - 黯淡的青丘灵珠
    # level: 1
    # value: -
    # rarity: 稀有
    pass


@register
def suit_191(char: CharacterProperty):
    # DCALC_REMOVE: suit_191 - 黯淡的青丘灵珠
    # level: 2
    # value: -
    # rarity: 稀有
    pass


@register
def suit_192(char: CharacterProperty):
    # DCALC_REMOVE: suit_192 - 黯淡的青丘灵珠
    # level: 3
    # value: -
    # rarity: 稀有
    pass


@register
def suit_193(char: CharacterProperty):
    # DCALC_REMOVE: suit_193 - 黯淡的青丘灵珠
    # level: 4
    # value: -
    # rarity: 稀有
    pass


@register
def suit_194(char: CharacterProperty):
    # DCALC_REMOVE: suit_194 - 黯淡的青丘灵珠
    # level: 5
    # value: -
    # rarity: 稀有
    pass


@register
def suit_195(char: CharacterProperty):
    # DCALC_REMOVE: suit_195 - 微光的青丘灵珠
    # level: 1
    # value: 借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活 - 攻击时，灵珠能量 +5（冷却时间1秒） - 灵珠最多可填充1个 - 青丘灵珠增益效果生效时，无法充能灵珠 - 进入地下城时，灵珠能量填充100 [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒
    # rarity: 神器
    char.SetStatus(SkillAttack=0.1)
    pass


@register
def suit_196(char: CharacterProperty):
    # DCALC_REMOVE: suit_196 - 微光的青丘灵珠
    # level: 2
    # value: 借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活 - 攻击时，灵珠能量 +5（冷却时间1秒） - 灵珠最多可填充1个 - 青丘灵珠增益效果生效时，无法充能灵珠 - 进入地下城时，灵珠能量填充100 [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒
    # rarity: 神器
    suit_195(char)
    pass


@register
def suit_197(char: CharacterProperty):
    # DCALC_REMOVE: suit_197 - 微光的青丘灵珠
    # level: 3
    # value: 借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活 - 攻击时，灵珠能量 +5（冷却时间1秒） - 灵珠最多可填充1个 - 青丘灵珠增益效果生效时，无法充能灵珠 - 进入地下城时，灵珠能量填充100 [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒
    # rarity: 神器
    suit_195(char)
    pass


@register
def suit_198(char: CharacterProperty):
    # DCALC_REMOVE: suit_198 - 微光的青丘灵珠
    # level: 4
    # value: 借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活 - 攻击时，灵珠能量 +5（冷却时间1秒） - 灵珠最多可填充1个 - 青丘灵珠增益效果生效时，无法充能灵珠 - 进入地下城时，灵珠能量填充100 [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒
    # rarity: 神器
    suit_195(char)
    pass


@register
def suit_199(char: CharacterProperty):
    # DCALC_REMOVE: suit_199 - 微光的青丘灵珠
    # level: 5
    # value: 借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活 - 攻击时，灵珠能量 +5（冷却时间1秒） - 灵珠最多可填充1个 - 青丘灵珠增益效果生效时，无法充能灵珠 - 进入地下城时，灵珠能量填充100 [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒
    # rarity: 神器
    suit_195(char)
    pass


@register
def suit_200(char: CharacterProperty):
    # DCALC_REMOVE: suit_200 - 清澈的青丘灵珠
    # level: 1
    # value: 借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活 - 攻击时，灵珠能量 +9（冷却时间1秒） - 每秒灵珠能量 +1 - 灵珠最多可填充2个 - 青丘灵珠增益效果生效时，无法充能灵珠 - 进入地下城时，灵珠能量填充200 [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒
    # rarity: 传说
    char.SetStatus(SkillAttack=0.2)
    pass


@register
def suit_201(char: CharacterProperty):
    # DCALC_REMOVE: suit_201 - 清澈的青丘灵珠
    # level: 2
    # value: 借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活 - 攻击时，灵珠能量 +9（冷却时间1秒） - 每秒灵珠能量 +1 - 灵珠最多可填充2个 - 青丘灵珠增益效果生效时，无法充能灵珠 - 进入地下城时，灵珠能量填充200 [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒
    # rarity: 传说
    suit_200(char)
    pass


@register
def suit_202(char: CharacterProperty):
    # DCALC_REMOVE: suit_202 - 清澈的青丘灵珠
    # level: 3
    # value: 借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活 - 攻击时，灵珠能量 +9（冷却时间1秒） - 每秒灵珠能量 +1 - 灵珠最多可填充2个 - 青丘灵珠增益效果生效时，无法充能灵珠 - 进入地下城时，灵珠能量填充200 [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒
    # rarity: 传说
    suit_200(char)
    pass


@register
def suit_203(char: CharacterProperty):
    # DCALC_REMOVE: suit_203 - 清澈的青丘灵珠
    # level: 4
    # value: 借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活 - 攻击时，灵珠能量 +9（冷却时间1秒） - 每秒灵珠能量 +1 - 灵珠最多可填充2个 - 青丘灵珠增益效果生效时，无法充能灵珠 - 进入地下城时，灵珠能量填充200 [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒
    # rarity: 传说
    suit_200(char)
    pass


@register
def suit_204(char: CharacterProperty):
    # DCALC_REMOVE: suit_204 - 清澈的青丘灵珠
    # level: 5
    # value: 借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活 - 攻击时，灵珠能量 +9（冷却时间1秒） - 每秒灵珠能量 +1 - 灵珠最多可填充2个 - 青丘灵珠增益效果生效时，无法充能灵珠 - 进入地下城时，灵珠能量填充200 [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒
    # rarity: 传说
    suit_200(char)
    pass


@register
def suit_205(char: CharacterProperty):
    # DCALC_REMOVE: suit_205 - 耀眼的青丘灵珠
    # level: 1
    # value: 借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活 一攻击时，灵珠能量  +9（冷却时间1秒） - 每秒灵珠能量  +2 - 灵珠最多可填充3个 一青丘灵珠增益效果生效时，也可以充能灵珠 - 进入地下城时，灵珠能量填充200 [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒 [青丘灵珠开关][装备主动技能] - 灵珠全部填满时，自动使用青丘灵珠增益效果（冷却时间1秒） - 再次使用时，关闭自动使用功能
    # rarity: 史诗
    char.SetStatus(SkillAttack=0.3)
    pass


@register
def suit_206(char: CharacterProperty):
    # DCALC_REMOVE: suit_206 - 耀眼的青丘灵珠
    # level: 2
    # value: 借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活 一攻击时，灵珠能量  +9（冷却时间1秒） - 每秒灵珠能量  +2 - 灵珠最多可填充3个 一青丘灵珠增益效果生效时，也可以充能灵珠 - 进入地下城时，灵珠能量填充200 [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒 [青丘灵珠开关][装备主动技能] - 灵珠全部填满时，自动使用青丘灵珠增益效果（冷却时间1秒） - 再次使用时，关闭自动使用功能
    # rarity: 史诗
    suit_205(char)
    pass


@register
def suit_207(char: CharacterProperty):
    # DCALC_REMOVE: suit_207 - 耀眼的青丘灵珠
    # level: 3
    # value: 借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活 一攻击时，灵珠能量  +9（冷却时间1秒） - 每秒灵珠能量  +2 - 灵珠最多可填充3个 一青丘灵珠增益效果生效时，也可以充能灵珠 - 进入地下城时，灵珠能量填充200 [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒 [青丘灵珠开关][装备主动技能] - 灵珠全部填满时，自动使用青丘灵珠增益效果（冷却时间1秒） - 再次使用时，关闭自动使用功能
    # rarity: 史诗
    suit_205(char)
    pass


@register
def suit_208(char: CharacterProperty):
    # DCALC_REMOVE: suit_208 - 耀眼的青丘灵珠
    # level: 4
    # value: 借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活 一攻击时，灵珠能量  +9（冷却时间1秒） - 每秒灵珠能量  +2 - 灵珠最多可填充3个 一青丘灵珠增益效果生效时，也可以充能灵珠 - 进入地下城时，灵珠能量填充200 [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒 [青丘灵珠开关][装备主动技能] - 灵珠全部填满时，自动使用青丘灵珠增益效果（冷却时间1秒） - 再次使用时，关闭自动使用功能
    # rarity: 史诗
    suit_205(char)
    pass


@register
def suit_209(char: CharacterProperty):
    # DCALC_REMOVE: suit_209 - 耀眼的青丘灵珠
    # level: 5
    # value: 借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活 一攻击时，灵珠能量  +9（冷却时间1秒） - 每秒灵珠能量  +2 - 灵珠最多可填充3个 一青丘灵珠增益效果生效时，也可以充能灵珠 - 进入地下城时，灵珠能量填充200 [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒 [青丘灵珠开关][装备主动技能] - 灵珠全部填满时，自动使用青丘灵珠增益效果（冷却时间1秒） - 再次使用时，关闭自动使用功能
    # rarity: 史诗
    suit_205(char)
    pass


@register
def suit_210(char: CharacterProperty):
    # DCALC_REMOVE: suit_210 - 梦幻的青丘灵珠
    # level: 1
    # value: 借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活 - 攻击时，灵珠能量 +14（冷却时间1秒） - 每秒灵珠能量 +3 - 灵珠最多可填充4个 一青丘灵珠增益效果生效时，也可以充能灵珠 - 进入地下城时，灵珠能量填充400 [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒 [青丘灵珠开关][装备主动技能] - 灵珠全部填满时，自动使用青丘灵珠增益效果（冷却时间1秒） - 再次使用时，关闭自动使用功能
    # rarity: 太初
    char.SetStatus(SkillAttack=0.4)
    pass


# endregion
# region 群猎美学


@register
def suit_211(char: CharacterProperty):
    # DCALC_REMOVE: suit_211 - 群猎之风
    # level: 1
    # value: -
    # rarity: 稀有
    pass


@register
def suit_212(char: CharacterProperty):
    # DCALC_REMOVE: suit_212 - 群猎之风
    # level: 2
    # value: -
    # rarity: 稀有
    pass


@register
def suit_213(char: CharacterProperty):
    # DCALC_REMOVE: suit_213 - 群猎之风
    # level: 3
    # value: -
    # rarity: 稀有
    pass


@register
def suit_214(char: CharacterProperty):
    # DCALC_REMOVE: suit_214 - 群猎之风
    # level: 4
    # value: -
    # rarity: 稀有
    pass


@register
def suit_215(char: CharacterProperty):
    # DCALC_REMOVE: suit_215 - 群猎之风
    # level: 5
    # value: -
    # rarity: 稀有
    pass


@register
def suit_216(char: CharacterProperty):
    # DCALC_REMOVE: suit_216 - 群猎之林
    # level: 1
    # value: 与同伴在一起时， 会变得更强。  [组队时生效] [群猎之力] 给队员赋予光环， 获得以下效果。 (最多叠加1次) - 所有速度  +10%  [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量:3,825% - 使被命中的敌人进入崩裂状态，持续30秒 - 冷却时间30秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%） （[群猎之力]、[酣畅狩猎]效果对辅助职业无效） [单人挑战时适用] - 技能伤害 +10.6% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 神器
    if char.equ_options.get('3',0) == 0:
        char.SetStatus(SkillAttack=0.106)
    else:
        char.SetStatus(SkillAttack=0.08,SpeedA=0.1,SpeedM=0.1,SpeedR=0.1)
        char.equ_effect.append(EquEffect(name='酣畅狩猎', icon='/equipment/skill/15.png', cd=30, data=3825))
    pass


@register
def suit_217(char: CharacterProperty):
    # DCALC_REMOVE: suit_217 - 群猎之林
    # level: 2
    # value: 与同伴在一起时， 会变得更强。  [组队时生效] [群猎之力] 给队员赋予光环， 获得以下效果。 (最多叠加1次) - 所有速度  +10%  [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量:3,825% - 使被命中的敌人进入崩裂状态，持续30秒 - 冷却时间30秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%） （[群猎之力]、[酣畅狩猎]效果对辅助职业无效） [单人挑战时适用] - 技能伤害 +10.6% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 神器
    suit_216(char)
    pass


@register
def suit_218(char: CharacterProperty):
    # DCALC_REMOVE: suit_218 - 群猎之林
    # level: 3
    # value: 与同伴在一起时， 会变得更强。  [组队时生效] [群猎之力] 给队员赋予光环， 获得以下效果。 (最多叠加1次) - 所有速度  +10%  [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量:3,825% - 使被命中的敌人进入崩裂状态，持续30秒 - 冷却时间30秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%） （[群猎之力]、[酣畅狩猎]效果对辅助职业无效） [单人挑战时适用] - 技能伤害 +10.6% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 神器
    suit_216(char)
    pass


@register
def suit_219(char: CharacterProperty):
    # DCALC_REMOVE: suit_219 - 群猎之林
    # level: 4
    # value: 与同伴在一起时， 会变得更强。  [组队时生效] [群猎之力] 给队员赋予光环， 获得以下效果。 (最多叠加1次) - 所有速度  +10%  [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量:3,825% - 使被命中的敌人进入崩裂状态，持续30秒 - 冷却时间30秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%） （[群猎之力]、[酣畅狩猎]效果对辅助职业无效） [单人挑战时适用] - 技能伤害 +10.6% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 神器
    suit_216(char)
    pass


@register
def suit_220(char: CharacterProperty):
    # DCALC_REMOVE: suit_220 - 群猎之林
    # level: 5
    # value: 与同伴在一起时， 会变得更强。  [组队时生效] [群猎之力] 给队员赋予光环， 获得以下效果。 (最多叠加1次) - 所有速度  +10%  [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量:3,825% - 使被命中的敌人进入崩裂状态，持续30秒 - 冷却时间30秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%） （[群猎之力]、[酣畅狩猎]效果对辅助职业无效） [单人挑战时适用] - 技能伤害 +10.6% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 神器
    suit_216(char)
    pass


@register
def suit_221(char: CharacterProperty):
    # DCALC_REMOVE: suit_221 - 群猎之光
    # level: 1
    # value: 与同伴在一起时， 会变得更强。 [组队时生效] [群猎之力] 给队员赋予光环，获得以下效果。（最多叠加1次） - 所有速度+15% - 每10秒恢复10000点的生命值和魔法值，持续10秒 [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量:5,738% -使被命中的敌人进入崩裂状态，持续45秒 -冷却时间30秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%） （[群猎之力]、[酣畅狩猎]效果对辅助职业无效） [单人挑战时适用] - 技能伤害 +17.8% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 传说
    if char.equ_options.get('3',0) == 0:
        char.SetStatus(SkillAttack=0.178)
    else:
        char.SetStatus(SkillAttack=0.08,SpeedA=0.15,SpeedM=0.15,SpeedR=0.15)
        char.equ_effect.append(EquEffect(name='酣畅狩猎', icon='/equipment/skill/15.png', cd=30, data=5738))
    pass


@register
def suit_222(char: CharacterProperty):
    # DCALC_REMOVE: suit_222 - 群猎之光
    # level: 2
    # value: 与同伴在一起时， 会变得更强。 [组队时生效] [群猎之力] 给队员赋予光环，获得以下效果。（最多叠加1次） - 所有速度+15% - 每10秒恢复10000点的生命值和魔法值，持续10秒 [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量:5,738% -使被命中的敌人进入崩裂状态，持续45秒 -冷却时间30秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%） （[群猎之力]、[酣畅狩猎]效果对辅助职业无效） [单人挑战时适用] - 技能伤害 +17.8% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 传说
    suit_221(char)
    pass


@register
def suit_223(char: CharacterProperty):
    # DCALC_REMOVE: suit_223 - 群猎之光
    # level: 3
    # value: 与同伴在一起时， 会变得更强。 [组队时生效] [群猎之力] 给队员赋予光环，获得以下效果。（最多叠加1次） - 所有速度+15% - 每10秒恢复10000点的生命值和魔法值，持续10秒 [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量:5,738% -使被命中的敌人进入崩裂状态，持续45秒 -冷却时间30秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%） （[群猎之力]、[酣畅狩猎]效果对辅助职业无效） [单人挑战时适用] - 技能伤害 +17.8% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 传说
    suit_221(char)
    pass


@register
def suit_224(char: CharacterProperty):
    # DCALC_REMOVE: suit_224 - 群猎之光
    # level: 4
    # value: 与同伴在一起时， 会变得更强。 [组队时生效] [群猎之力] 给队员赋予光环，获得以下效果。（最多叠加1次） - 所有速度+15% - 每10秒恢复10000点的生命值和魔法值，持续10秒 [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量:5,738% -使被命中的敌人进入崩裂状态，持续45秒 -冷却时间30秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%） （[群猎之力]、[酣畅狩猎]效果对辅助职业无效） [单人挑战时适用] - 技能伤害 +17.8% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 传说
    suit_221(char)
    pass


@register
def suit_225(char: CharacterProperty):
    # DCALC_REMOVE: suit_225 - 群猎之光
    # level: 5
    # value: 与同伴在一起时， 会变得更强。 [组队时生效] [群猎之力] 给队员赋予光环，获得以下效果。（最多叠加1次） - 所有速度+15% - 每10秒恢复10000点的生命值和魔法值，持续10秒 [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量:5,738% -使被命中的敌人进入崩裂状态，持续45秒 -冷却时间30秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%） （[群猎之力]、[酣畅狩猎]效果对辅助职业无效） [单人挑战时适用] - 技能伤害 +17.8% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 传说
    suit_221(char)
    pass


@register
def suit_226(char: CharacterProperty):
    # DCALC_REMOVE: suit_226 - 群猎之星
    # level: 1
    # value: 与同伴在一起时， 会变得更强。  [组队挑战时适用] [群猎之力] 给队员赋予光环，获得以下效果。（最多叠加1次） - 所有速度  +20% - 所受物理/魔法伤害- 10% - 每10秒恢复10000点的生命值和魔法值，持续10秒 [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量:6,750% - 使被命中的敌人进入崩裂状态，持续60秒 - 冷却时间30秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%） （[群猎之力]、[酣畅狩猎]效果对辅助职业无效） [单人挑战时适用] - 技能伤害 +17.8% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 史诗
    if char.equ_options.get('3',0) == 0:
        char.SetStatus(SkillAttack=0.178)
    else:
        char.SetStatus(SkillAttack=0.08,SpeedA=0.2,SpeedM=0.0,SpeedR=0.0)
        char.equ_effect.append(EquEffect(name='酣畅狩猎', icon='/equipment/skill/15.png', cd=30, data=6750))
    pass


@register
def suit_227(char: CharacterProperty):
    # DCALC_REMOVE: suit_227 - 群猎之星
    # level: 2
    # value: 与同伴在一起时， 会变得更强。  [组队挑战时适用] [群猎之力] 给队员赋予光环，获得以下效果。（最多叠加1次） - 所有速度  +20% - 所受物理/魔法伤害- 10% - 每10秒恢复10000点的生命值和魔法值，持续10秒 [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量:6,750% - 使被命中的敌人进入崩裂状态，持续60秒 - 冷却时间30秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%） （[群猎之力]、[酣畅狩猎]效果对辅助职业无效） [单人挑战时适用] - 技能伤害 +17.8% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 史诗
    suit_226(char)
    pass


@register
def suit_228(char: CharacterProperty):
    # DCALC_REMOVE: suit_228 - 群猎之星
    # level: 3
    # value: 与同伴在一起时， 会变得更强。  [组队挑战时适用] [群猎之力] 给队员赋予光环，获得以下效果。（最多叠加1次） - 所有速度  +20% - 所受物理/魔法伤害- 10% - 每10秒恢复10000点的生命值和魔法值，持续10秒 [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量:6,750% - 使被命中的敌人进入崩裂状态，持续60秒 - 冷却时间30秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%） （[群猎之力]、[酣畅狩猎]效果对辅助职业无效） [单人挑战时适用] - 技能伤害 +17.8% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 史诗
    suit_226(char)
    pass


@register
def suit_229(char: CharacterProperty):
    # DCALC_REMOVE: suit_229 - 群猎之星
    # level: 4
    # value: 与同伴在一起时， 会变得更强。  [组队挑战时适用] [群猎之力] 给队员赋予光环，获得以下效果。（最多叠加1次） - 所有速度  +20% - 所受物理/魔法伤害- 10% - 每10秒恢复10000点的生命值和魔法值，持续10秒 [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量:6,750% - 使被命中的敌人进入崩裂状态，持续60秒 - 冷却时间30秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%） （[群猎之力]、[酣畅狩猎]效果对辅助职业无效） [单人挑战时适用] - 技能伤害 +17.8% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 史诗
    suit_226(char)
    pass


@register
def suit_230(char: CharacterProperty):
    # DCALC_REMOVE: suit_230 - 群猎之星
    # level: 5
    # value: 与同伴在一起时， 会变得更强。  [组队挑战时适用] [群猎之力] 给队员赋予光环，获得以下效果。（最多叠加1次） - 所有速度  +20% - 所受物理/魔法伤害- 10% - 每10秒恢复10000点的生命值和魔法值，持续10秒 [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量:6,750% - 使被命中的敌人进入崩裂状态，持续60秒 - 冷却时间30秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%） （[群猎之力]、[酣畅狩猎]效果对辅助职业无效） [单人挑战时适用] - 技能伤害 +17.8% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 史诗
    suit_226(char)
    pass


@register
def suit_231(char: CharacterProperty):
    # DCALC_REMOVE: suit_231 - 群猎之神
    # level: 1
    # value: 与同伴在一起时， 会变得更强。  [组队挑战时适用] [群猎之力] 给队员赋予光环，获得以下效果。（最多叠加1次） - 所有速度  +30% - 所受物理/魔法伤害- 15% - 每10秒恢复10，000点的生命值和魔法值，持续10秒 [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量 :9,563% - 使被命中的敌人进入最大叠加的崩裂状态，持续60秒 - 冷却时间30秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%） （[群猎之力]、[酣畅狩猎]效果对辅助职业无效） [单人挑战时适用] - 技能伤害 +21.6% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 太初
    if char.equ_options.get('3',0) == 0:
        char.SetStatus(SkillAttack=0.216)
    else:
        char.SetStatus(SkillAttack=0.08,SpeedA=0.3,SpeedM=0.3,SpeedR=0.3)
        char.equ_effect.append(EquEffect(name='酣畅狩猎', icon='/equipment/skill/15.png', cd=30, data=9563))
    pass


# endregion
# region 冥思者的魔力领域


@register
def suit_232(char: CharacterProperty):
    # DCALC_REMOVE: suit_232 - 魔力领域 - 初始
    # level: 1
    # value: -
    # rarity: 稀有
    pass


@register
def suit_233(char: CharacterProperty):
    # DCALC_REMOVE: suit_233 - 魔力领域 - 初始
    # level: 2
    # value: -
    # rarity: 稀有
    pass


@register
def suit_234(char: CharacterProperty):
    # DCALC_REMOVE: suit_234 - 魔力领域 - 初始
    # level: 3
    # value: -
    # rarity: 稀有
    pass


@register
def suit_235(char: CharacterProperty):
    # DCALC_REMOVE: suit_235 - 魔力领域 - 初始
    # level: 4
    # value: -
    # rarity: 稀有
    pass


@register
def suit_236(char: CharacterProperty):
    # DCALC_REMOVE: suit_236 - 魔力领域 - 初始
    # level: 5
    # value: -
    # rarity: 稀有
    pass


@register
def suit_237(char: CharacterProperty):
    # DCALC_REMOVE: suit_237 - 魔力领域 - 入静
    # level: 1
    # value: 操控魔攻核攻击敌人。 [魔攻核] 进入地下城时，召唤普通模式魔攻核。 [命令：转换][装备主动技能] 转换魔攻核的攻击模式。 - 普通模式/追击模式 - 冷却时间：5秒 [魔攻核：普通模式] 每秒发射魔力波动。 - 魔力波动伤害量:19200% - 魔力波动范围:150px [魔攻核：追击模式] 追击最强的敌人，每秒发射魔力波动。 - 魔力波动伤害量:13714% - 魔力波动范围:150px
    # rarity: 神器
    if char.equ_options.get('4',0) == 0:
        char.equ_effect.append(EquEffect(name='普通模式', icon='/equipment/skill/57.png', cd=1, data=19200))
    else:
        char.equ_effect.append(EquEffect(name='追击模式', icon='/equipment/skill/57.png', cd=1, data=13714))
    pass


@register
def suit_238(char: CharacterProperty):
    # DCALC_REMOVE: suit_238 - 魔力领域 - 入静
    # level: 2
    # value: 操控魔攻核攻击敌人。 [魔攻核] 进入地下城时，召唤普通模式魔攻核。 [命令：转换][装备主动技能] 转换魔攻核的攻击模式。 - 普通模式/追击模式 - 冷却时间：5秒 [魔攻核：普通模式] 每秒发射魔力波动。 - 魔力波动伤害量:19200% - 魔力波动范围:150px [魔攻核：追击模式] 追击最强的敌人，每秒发射魔力波动。 - 魔力波动伤害量:13714% - 魔力波动范围:150px
    # rarity: 神器
    suit_237(char)
    pass


@register
def suit_239(char: CharacterProperty):
    # DCALC_REMOVE: suit_239 - 魔力领域 - 入静
    # level: 3
    # value: 操控魔攻核攻击敌人。 [魔攻核] 进入地下城时，召唤普通模式魔攻核。 [命令：转换][装备主动技能] 转换魔攻核的攻击模式。 - 普通模式/追击模式 - 冷却时间：5秒 [魔攻核：普通模式] 每秒发射魔力波动。 - 魔力波动伤害量:19200% - 魔力波动范围:150px [魔攻核：追击模式] 追击最强的敌人，每秒发射魔力波动。 - 魔力波动伤害量:13714% - 魔力波动范围:150px
    # rarity: 神器
    suit_237(char)
    pass


@register
def suit_240(char: CharacterProperty):
    # DCALC_REMOVE: suit_240 - 魔力领域 - 入静
    # level: 4
    # value: 操控魔攻核攻击敌人。 [魔攻核] 进入地下城时，召唤普通模式魔攻核。 [命令：转换][装备主动技能] 转换魔攻核的攻击模式。 - 普通模式/追击模式 - 冷却时间：5秒 [魔攻核：普通模式] 每秒发射魔力波动。 - 魔力波动伤害量:19200% - 魔力波动范围:150px [魔攻核：追击模式] 追击最强的敌人，每秒发射魔力波动。 - 魔力波动伤害量:13714% - 魔力波动范围:150px
    # rarity: 神器
    suit_237(char)
    pass


@register
def suit_241(char: CharacterProperty):
    # DCALC_REMOVE: suit_241 - 魔力领域 - 入静
    # level: 5
    # value: 操控魔攻核攻击敌人。 [魔攻核] 进入地下城时，召唤普通模式魔攻核。 [命令：转换][装备主动技能] 转换魔攻核的攻击模式。 - 普通模式/追击模式 - 冷却时间：5秒 [魔攻核：普通模式] 每秒发射魔力波动。 - 魔力波动伤害量:19200% - 魔力波动范围:150px [魔攻核：追击模式] 追击最强的敌人，每秒发射魔力波动。 - 魔力波动伤害量:13714% - 魔力波动范围:150px
    # rarity: 神器
    suit_237(char)
    pass


@register
def suit_242(char: CharacterProperty):
    # DCALC_REMOVE: suit_242 - 魔力领域 - 入真
    # level: 1
    # value: 操控魔攻核攻击敌人。 [魔攻核] 进入地下城时，召唤普通模式魔攻核。 [命令：转换][装备主动技能] 转换魔攻核的攻击模式。 - 普通模式/追击模式 - 冷却时间：5秒 [魔攻核：普通模式] 每秒发射魔力波动。 - 魔力波动伤害量:31680% - 魔力波动范围:150px - 移动速度  +25% - 进入霸体状态 [魔攻核：追击模式] 追击最强的敌人，每秒发射魔力波动。 - 魔力波动伤害量:20571% - 魔力波动范围:150px
    # rarity: 传说
    if char.equ_options.get('4',0) == 0:
        char.equ_effect.append(EquEffect(name='普通模式', icon='/equipment/skill/57.png', cd=1, data=31680))
        char.SetStatus(SpeedM=0.25)
    else:
        char.equ_effect.append(EquEffect(name='追击模式', icon='/equipment/skill/57.png', cd=1, data=20571))
    pass


@register
def suit_243(char: CharacterProperty):
    # DCALC_REMOVE: suit_243 - 魔力领域 - 入真
    # level: 2
    # value: 操控魔攻核攻击敌人。 [魔攻核] 进入地下城时，召唤普通模式魔攻核。 [命令：转换][装备主动技能] 转换魔攻核的攻击模式。 - 普通模式/追击模式 - 冷却时间：5秒 [魔攻核：普通模式] 每秒发射魔力波动。 - 魔力波动伤害量:31680% - 魔力波动范围:150px - 移动速度  +25% - 进入霸体状态 [魔攻核：追击模式] 追击最强的敌人，每秒发射魔力波动。 - 魔力波动伤害量:20571% - 魔力波动范围:150px
    # rarity: 传说
    suit_242(char)
    pass


@register
def suit_244(char: CharacterProperty):
    # DCALC_REMOVE: suit_244 - 魔力领域 - 入真
    # level: 3
    # value: 操控魔攻核攻击敌人。 [魔攻核] 进入地下城时，召唤普通模式魔攻核。 [命令：转换][装备主动技能] 转换魔攻核的攻击模式。 - 普通模式/追击模式 - 冷却时间：5秒 [魔攻核：普通模式] 每秒发射魔力波动。 - 魔力波动伤害量:31680% - 魔力波动范围:150px - 移动速度  +25% - 进入霸体状态 [魔攻核：追击模式] 追击最强的敌人，每秒发射魔力波动。 - 魔力波动伤害量:20571% - 魔力波动范围:150px
    # rarity: 传说
    suit_242(char)
    pass


@register
def suit_245(char: CharacterProperty):
    # DCALC_REMOVE: suit_245 - 魔力领域 - 入真
    # level: 4
    # value: 操控魔攻核攻击敌人。 [魔攻核] 进入地下城时，召唤普通模式魔攻核。 [命令：转换][装备主动技能] 转换魔攻核的攻击模式。 - 普通模式/追击模式 - 冷却时间：5秒 [魔攻核：普通模式] 每秒发射魔力波动。 - 魔力波动伤害量:31680% - 魔力波动范围:150px - 移动速度  +25% - 进入霸体状态 [魔攻核：追击模式] 追击最强的敌人，每秒发射魔力波动。 - 魔力波动伤害量:20571% - 魔力波动范围:150px
    # rarity: 传说
    suit_242(char)
    pass


@register
def suit_246(char: CharacterProperty):
    # DCALC_REMOVE: suit_246 - 魔力领域 - 入真
    # level: 5
    # value: 操控魔攻核攻击敌人。 [魔攻核] 进入地下城时，召唤普通模式魔攻核。 [命令：转换][装备主动技能] 转换魔攻核的攻击模式。 - 普通模式/追击模式 - 冷却时间：5秒 [魔攻核：普通模式] 每秒发射魔力波动。 - 魔力波动伤害量:31680% - 魔力波动范围:150px - 移动速度  +25% - 进入霸体状态 [魔攻核：追击模式] 追击最强的敌人，每秒发射魔力波动。 - 魔力波动伤害量:20571% - 魔力波动范围:150px
    # rarity: 传说
    suit_242(char)
    pass


@register
def suit_247(char: CharacterProperty):
    # DCALC_REMOVE: suit_247 - 魔力领域 - 入定
    # level: 1
    # value: 操控魔攻核攻击敌人。 [魔攻核] 进入地下城时，召唤普通模式魔攻核。 [命令：转换][装备主动技能]转换魔攻核的攻击模式。 - 普通模式/追击模式 - 冷却时间：5秒 [魔攻核：普通模式] 每秒发射魔力波动。 - 魔力波动伤害量:47520% - 魔力波动范围:200px - 移动速度  +25% - 进入霸体状态 [魔攻核：追击模式] 追击最强的敌人，每秒发射魔力波动。 - 魔力波动伤害量:30857% - 魔力波动范围:200px
    # rarity: 史诗
    if char.equ_options.get('4',0) == 0:
        char.equ_effect.append(EquEffect(name='普通模式', icon='/equipment/skill/57.png', cd=1, data=47520))
        char.SetStatus(SpeedM=0.25)
    else:
        char.equ_effect.append(EquEffect(name='追击模式', icon='/equipment/skill/57.png', cd=1, data=30857))
    pass


@register
def suit_248(char: CharacterProperty):
    # DCALC_REMOVE: suit_248 - 魔力领域 - 入定
    # level: 2
    # value: 操控魔攻核攻击敌人。 [魔攻核] 进入地下城时，召唤普通模式魔攻核。 [命令：转换][装备主动技能]转换魔攻核的攻击模式。 - 普通模式/追击模式 - 冷却时间：5秒 [魔攻核：普通模式] 每秒发射魔力波动。 - 魔力波动伤害量:47520% - 魔力波动范围:200px - 移动速度  +25% - 进入霸体状态 [魔攻核：追击模式] 追击最强的敌人，每秒发射魔力波动。 - 魔力波动伤害量:30857% - 魔力波动范围:200px
    # rarity: 史诗
    suit_247(char)
    pass


@register
def suit_249(char: CharacterProperty):
    # DCALC_REMOVE: suit_249 - 魔力领域 - 入定
    # level: 3
    # value: 操控魔攻核攻击敌人。 [魔攻核] 进入地下城时，召唤普通模式魔攻核。 [命令：转换][装备主动技能]转换魔攻核的攻击模式。 - 普通模式/追击模式 - 冷却时间：5秒 [魔攻核：普通模式] 每秒发射魔力波动。 - 魔力波动伤害量:47520% - 魔力波动范围:200px - 移动速度  +25% - 进入霸体状态 [魔攻核：追击模式] 追击最强的敌人，每秒发射魔力波动。 - 魔力波动伤害量:30857% - 魔力波动范围:200px
    # rarity: 史诗
    suit_247(char)
    pass


@register
def suit_250(char: CharacterProperty):
    # DCALC_REMOVE: suit_250 - 魔力领域 - 入定
    # level: 4
    # value: 操控魔攻核攻击敌人。 [魔攻核] 进入地下城时，召唤普通模式魔攻核。 [命令：转换][装备主动技能]转换魔攻核的攻击模式。 - 普通模式/追击模式 - 冷却时间：5秒 [魔攻核：普通模式] 每秒发射魔力波动。 - 魔力波动伤害量:47520% - 魔力波动范围:200px - 移动速度  +25% - 进入霸体状态 [魔攻核：追击模式] 追击最强的敌人，每秒发射魔力波动。 - 魔力波动伤害量:30857% - 魔力波动范围:200px
    # rarity: 史诗
    suit_247(char)
    pass


@register
def suit_251(char: CharacterProperty):
    # DCALC_REMOVE: suit_251 - 魔力领域 - 入定
    # level: 5
    # value: 操控魔攻核攻击敌人。 [魔攻核] 进入地下城时，召唤普通模式魔攻核。 [命令：转换][装备主动技能]转换魔攻核的攻击模式。 - 普通模式/追击模式 - 冷却时间：5秒 [魔攻核：普通模式] 每秒发射魔力波动。 - 魔力波动伤害量:47520% - 魔力波动范围:200px - 移动速度  +25% - 进入霸体状态 [魔攻核：追击模式] 追击最强的敌人，每秒发射魔力波动。 - 魔力波动伤害量:30857% - 魔力波动范围:200px
    # rarity: 史诗
    suit_247(char)
    pass


@register
def suit_252(char: CharacterProperty):
    # DCALC_REMOVE: suit_252 - 魔力领域 - 入神
    # level: 1
    # value: 操控魔攻核攻击敌人。 [魔攻核] 进入地下城时，召唤普通模式魔攻核。 [命令：转换][装备主动技能] 转换魔攻核的攻击模式。 - 普通模式/追击模式 - 冷却时间：5秒 [魔攻核：普通模式] 每秒发射魔力波动。 - 魔力波动伤害量:6,720% - 魔力波动范围:300px - 移动速度  +25% - 进入霸体状态 - 所受物理/魔法伤害 - 10% [魔攻核：追击模式] 追击最强的敌人，每秒发射魔力波动。 - 魔力波动伤害量 :39428% - 魔力波动范围:200px
    # rarity: 太初
    if char.equ_options.get('4',0) == 0:
        char.equ_effect.append(EquEffect(name='普通模式', icon='/equipment/skill/57.png', cd=1, data=60720))
        char.SetStatus(SpeedM=0.25)
    else:
        char.equ_effect.append(EquEffect(name='追击模式', icon='/equipment/skill/57.png', cd=1, data=39428))
    pass


# endregion
