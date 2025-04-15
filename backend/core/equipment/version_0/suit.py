from core.abstract.character import CharacterProperty
from core.basic.equipment import EquEffect
from .register import register

# region 潜影暗袭


@register
def suit_1(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_2(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_3(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_4(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_5(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_6(char: CharacterProperty):
    """
      逆转与影子的因果关系，实现超乎寻常的动作。
    [潜影藏锋][装备主动技能]
    - 强制中断角色动作（觉醒技能除外）
    - 冷却时间5秒
    """
    pass


@register
def suit_7(char: CharacterProperty):
    """
      逆转与影子的因果关系，实现超乎寻常的动作。
    [潜影藏锋][装备主动技能]
    - 强制中断角色动作（觉醒技能除外）
    - 冷却时间5秒
    """
    pass


@register
def suit_8(char: CharacterProperty):
    """
      逆转与影子的因果关系，实现超乎寻常的动作。
    [潜影藏锋][装备主动技能]
    - 强制中断角色动作（觉醒技能除外）
    - 冷却时间5秒
    """
    pass


@register
def suit_9(char: CharacterProperty):
    """
      逆转与影子的因果关系，实现超乎寻常的动作。
    [潜影藏锋][装备主动技能]
    - 强制中断角色动作（觉醒技能除外）
    - 冷却时间5秒
    """
    pass


@register
def suit_10(char: CharacterProperty):
    """
      逆转与影子的因果关系，实现超乎寻常的动作。
    [潜影藏锋][装备主动技能]
    - 强制中断角色动作（觉醒技能除外）
    - 冷却时间5秒
    """
    pass


@register
def suit_11(char: CharacterProperty):
    """
      逆转与影子的因果关系，实现超乎寻常的动作。
    施放技能时，获得[影子]层数。（最多叠加10次）
    [潜影灭迹][装备主动技能]存在[影子]层数时，施放装备技能时发动以下效果。
    - 消耗3个[影子]层数
    - 强制中断角色动作（觉醒技能除外）
    - 所有速度 +5%，效果持续5秒（最多叠加3次）
    """
    char.SetStatus(SpeedA=0.05 * 3, SpeedM=0.05 * 3, SpeedR=0.05 * 3)
    pass


@register
def suit_12(char: CharacterProperty):
    """
      逆转与影子的因果关系，实现超乎寻常的动作。
    施放技能时，获得[影子]层数。（最多叠加10次）
    [潜影灭迹][装备主动技能]存在[影子]层数时，施放装备技能时发动以下效果。
    - 消耗3个[影子]层数
    - 强制中断角色动作（觉醒技能除外）
    - 所有速度 +5%，效果持续5秒（最多叠加3次）
    """
    suit_11(char)
    pass


@register
def suit_13(char: CharacterProperty):
    """
      逆转与影子的因果关系，实现超乎寻常的动作。
    施放技能时，获得[影子]层数。（最多叠加10次）
    [潜影灭迹][装备主动技能]存在[影子]层数时，施放装备技能时发动以下效果。
    - 消耗3个[影子]层数
    - 强制中断角色动作（觉醒技能除外）
    - 所有速度 +5%，效果持续5秒（最多叠加3次）
    """
    suit_11(char)
    pass


@register
def suit_14(char: CharacterProperty):
    """
      逆转与影子的因果关系，实现超乎寻常的动作。
    施放技能时，获得[影子]层数。（最多叠加10次）
    [潜影灭迹][装备主动技能]存在[影子]层数时，施放装备技能时发动以下效果。
    - 消耗3个[影子]层数
    - 强制中断角色动作（觉醒技能除外）
    - 所有速度 +5%，效果持续5秒（最多叠加3次）
    """
    suit_11(char)
    pass


@register
def suit_15(char: CharacterProperty):
    """
      逆转与影子的因果关系，实现超乎寻常的动作。
    施放技能时，获得[影子]层数。（最多叠加10次）
    [潜影灭迹][装备主动技能]存在[影子]层数时，施放装备技能时发动以下效果。
    - 消耗3个[影子]层数
    - 强制中断角色动作（觉醒技能除外）
    - 所有速度 +5%，效果持续5秒（最多叠加3次）
    """
    suit_11(char)
    pass


@register
def suit_16(char: CharacterProperty):
    """
      逆转与影子的因果关系，实现超乎寻常的动作。
    施放技能时，获得[影子]层数。（最多叠加10次）
    [潜影灭迹][装备主动技能]
    存在[影子]层数时，施放装备技能时发动以下效果。
    - 消耗2个[影子]层数
    - 强制中断角色动作（觉醒技能除外）
    - 所有速度 +5%，效果持续5秒（最多叠加3次）
    [追击替罪羊][装备主动技能]
    - 消耗7个[影子]层数
    - 强制中断角色动作（觉醒技能除外）
    - 瞬移到最强大的敌人背后
    - 追击范围:600px
    - 冷却时间：8秒
    """
    suit_11(char)
    pass


@register
def suit_17(char: CharacterProperty):
    """
      逆转与影子的因果关系，实现超乎寻常的动作。
    施放技能时，获得[影子]层数。（最多叠加10次）
    [潜影灭迹][装备主动技能]
    存在[影子]层数时，施放装备技能时发动以下效果。
    - 消耗2个[影子]层数
    - 强制中断角色动作（觉醒技能除外）
    - 所有速度 +5%，效果持续5秒（最多叠加3次）
    [追击替罪羊][装备主动技能]
    - 消耗7个[影子]层数
    - 强制中断角色动作（觉醒技能除外）
    - 瞬移到最强大的敌人背后
    - 追击范围:600px
    - 冷却时间：8秒
    """
    suit_11(char)
    pass


@register
def suit_18(char: CharacterProperty):
    """
      逆转与影子的因果关系，实现超乎寻常的动作。
    施放技能时，获得[影子]层数。（最多叠加10次）
    [潜影灭迹][装备主动技能]
    存在[影子]层数时，施放装备技能时发动以下效果。
    - 消耗2个[影子]层数
    - 强制中断角色动作（觉醒技能除外）
    - 所有速度 +5%，效果持续5秒（最多叠加3次）
    [追击替罪羊][装备主动技能]
    - 消耗7个[影子]层数
    - 强制中断角色动作（觉醒技能除外）
    - 瞬移到最强大的敌人背后
    - 追击范围:600px
    - 冷却时间：8秒
    """
    suit_11(char)
    pass


@register
def suit_19(char: CharacterProperty):
    """
      逆转与影子的因果关系，实现超乎寻常的动作。
    施放技能时，获得[影子]层数。（最多叠加10次）
    [潜影灭迹][装备主动技能]
    存在[影子]层数时，施放装备技能时发动以下效果。
    - 消耗2个[影子]层数
    - 强制中断角色动作（觉醒技能除外）
    - 所有速度 +5%，效果持续5秒（最多叠加3次）
    [追击替罪羊][装备主动技能]
    - 消耗7个[影子]层数
    - 强制中断角色动作（觉醒技能除外）
    - 瞬移到最强大的敌人背后
    - 追击范围:600px
    - 冷却时间：8秒
    """
    suit_11(char)
    pass


@register
def suit_20(char: CharacterProperty):
    """
      逆转与影子的因果关系，实现超乎寻常的动作。
    施放技能时，获得[影子]层数。（最多叠加10次）
    [潜影灭迹][装备主动技能]
    存在[影子]层数时，施放装备技能时发动以下效果。
    - 消耗2个[影子]层数
    - 强制中断角色动作（觉醒技能除外）
    - 所有速度 +5%，效果持续5秒（最多叠加3次）
    [追击替罪羊][装备主动技能]
    - 消耗7个[影子]层数
    - 强制中断角色动作（觉醒技能除外）
    - 瞬移到最强大的敌人背后
    - 追击范围:600px
    - 冷却时间：8秒
    """
    suit_11(char)
    pass


@register
def suit_21(char: CharacterProperty):
    """
      逆转与影子的因果关系，实现超乎寻常的动作。
    施放技能时，获得[影子]层数。（最多叠加10次）
    [潜影灭迹][装备主动技能]存在[影子]层数时，施放装备技能时发动以下效果。
    - 消耗1个[影子]层数
    - 强制中断角色动作（觉醒技能除外）
    - 所有速度 +5%，效果持续5秒（最多叠加3次）
    [追击替罪羊][装备主动技能]
    - 消耗5个[影子]层数
    - 强制中断角色动作（觉醒技能除外）
    一瞬移到最强大的敌人背后
    - 追击范围:800px
    - 冷却时间：8秒
    """
    suit_11(char)
    pass


# endregion
# region 精灵国度


@register
def suit_22(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_23(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_24(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_25(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_26(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_27(char: CharacterProperty):
    """
      召唤精灵一起战斗。
    [火灵安珀]
    每2秒施放一次火花：伤害量19,200%
    每3秒恢复1%的生命值
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    - 攻击中止/继续攻击
    - 冷却时间1秒
    """
    char.equ_effect.append(EquEffect(name='火灵安珀', icon='/equipment/skill/29.png', cd=2, data=19200))
    pass


@register
def suit_28(char: CharacterProperty):
    """
      召唤精灵一起战斗。
    [火灵安珀]
    每2秒施放一次火花：伤害量19,200%
    每3秒恢复1%的生命值
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    - 攻击中止/继续攻击
    - 冷却时间1秒
    """
    suit_27(char)
    pass


@register
def suit_29(char: CharacterProperty):
    """
      召唤精灵一起战斗。
    [火灵安珀]
    每2秒施放一次火花：伤害量19,200%
    每3秒恢复1%的生命值
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    - 攻击中止/继续攻击
    - 冷却时间1秒
    """
    suit_27(char)
    pass


@register
def suit_30(char: CharacterProperty):
    """
      召唤精灵一起战斗。
    [火灵安珀]
    每2秒施放一次火花：伤害量19,200%
    每3秒恢复1%的生命值
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    - 攻击中止/继续攻击
    - 冷却时间1秒
    """
    suit_27(char)
    pass


@register
def suit_31(char: CharacterProperty):
    """
      召唤精灵一起战斗。
    [火灵安珀]
    每2秒施放一次火花：伤害量19,200%
    每3秒恢复1%的生命值
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    - 攻击中止/继续攻击
    - 冷却时间1秒
    """
    suit_27(char)
    pass


@register
def suit_32(char: CharacterProperty):
    """
      召唤精灵一起战斗。
    [火灵安珀]
    每2秒施放一次火花：伤害量19,200%
    每3秒恢复1%的生命值
    [水灵阿库娅]
    每3秒施放一次水弹：伤害量24,000%
    每3秒恢复1%的魔法值
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    一攻击中止/继续攻击
    - 冷却时间1秒
    [元素释放][装备主动技能]对精灵下达协同攻击指令。
    - 消耗150精灵之魂
    - 攻击时，精灵之魂 +10（冷却时间1秒）
    - 被击时，精灵之魂- 5（冷却时间1秒）
    - 元素释放伤害量:80,400%
    """
    char.equ_effect.append(EquEffect(name='火灵安珀', icon='/equipment/skill/29.png', cd=2, data=19200))
    char.equ_effect.append(EquEffect(name='水灵阿库娅', icon='/equipment/skill/29.png', cd=3, data=24000))
    char.equ_effect.append(EquEffect(name='元素释放', icon='/equipment/skill/29.png', cd=15, data=80400))
    pass


@register
def suit_33(char: CharacterProperty):
    """
      召唤精灵一起战斗。
    [火灵安珀]
    每2秒施放一次火花：伤害量19,200%
    每3秒恢复1%的生命值
    [水灵阿库娅]
    每3秒施放一次水弹：伤害量24,000%
    每3秒恢复1%的魔法值
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    一攻击中止/继续攻击
    - 冷却时间1秒
    [元素释放][装备主动技能]对精灵下达协同攻击指令。
    - 消耗150精灵之魂
    - 攻击时，精灵之魂 +10（冷却时间1秒）
    - 被击时，精灵之魂- 5（冷却时间1秒）
    - 元素释放伤害量:80,401%
    """
    suit_32(char)
    pass


@register
def suit_34(char: CharacterProperty):
    """
      召唤精灵一起战斗。
    [火灵安珀]
    每2秒施放一次火花：伤害量19,200%
    每3秒恢复1%的生命值
    [水灵阿库娅]
    每3秒施放一次水弹：伤害量24,000%
    每3秒恢复1%的魔法值
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    一攻击中止/继续攻击
    - 冷却时间1秒
    [元素释放][装备主动技能]对精灵下达协同攻击指令。
    - 消耗150精灵之魂
    - 攻击时，精灵之魂 +10（冷却时间1秒）
    - 被击时，精灵之魂- 5（冷却时间1秒）
    - 元素释放伤害量:80,402%
    """
    suit_32(char)
    pass


@register
def suit_35(char: CharacterProperty):
    """
      召唤精灵一起战斗。
    [火灵安珀]
    每2秒施放一次火花：伤害量19,200%
    每3秒恢复1%的生命值
    [水灵阿库娅]
    每3秒施放一次水弹：伤害量24,000%
    每3秒恢复1%的魔法值
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    一攻击中止/继续攻击
    - 冷却时间1秒
    [元素释放][装备主动技能]对精灵下达协同攻击指令。
    - 消耗150精灵之魂
    - 攻击时，精灵之魂 +10（冷却时间1秒）
    - 被击时，精灵之魂- 5（冷却时间1秒）
    - 元素释放伤害量:80,403%
    """
    suit_32(char)
    pass


@register
def suit_36(char: CharacterProperty):
    """
      召唤精灵一起战斗。
    [火灵安珀]
    每2秒施放一次火花：伤害量19,200%
    每3秒恢复1%的生命值
    [水灵阿库娅]
    每3秒施放一次水弹：伤害量24,000%
    每3秒恢复1%的魔法值
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    一攻击中止/继续攻击
    - 冷却时间1秒
    [元素释放][装备主动技能]对精灵下达协同攻击指令。
    - 消耗150精灵之魂
    - 攻击时，精灵之魂 +10（冷却时间1秒）
    - 被击时，精灵之魂- 5（冷却时间1秒）
    - 元素释放伤害量:80,404%
    """
    suit_32(char)
    pass


@register
def suit_37(char: CharacterProperty):
    """
      召唤精灵一起战斗。
    [火灵安珀]
    每2秒施放一次火花：伤害量19,200%
    每3秒恢复1%的生命值
    [水灵阿库娅]
    每3秒施放一次水弹：伤害量24,000%
    每3秒恢复1%的魔法值
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    一攻击中止/继续攻击
    - 冷却时间1秒
    [风灵希尔珂]
    每2秒施放一次刀风：伤害量19,200%
    移动速度 +15%
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    - 攻击中止/继续攻击
    - 冷却时间1秒
    [元素释放][装备主动技能]对精灵下达协同攻击指令。
    - 消耗150精灵之魂
    一攻击时，精灵之魂 +10（冷却时间1秒）
    一被击时，精灵之魂- 5（冷却时间1秒）
    - 元素释放伤害量:118,200%
    """
    char.equ_effect.append(EquEffect(name='火灵安珀', icon='/equipment/skill/29.png', cd=2, data=19200))
    char.equ_effect.append(EquEffect(name='水灵阿库娅', icon='/equipment/skill/29.png', cd=3, data=24000))
    char.equ_effect.append(EquEffect(name='风灵希尔珂', icon='/equipment/skill/29.png', cd=2, data=19200))
    char.SetStatus(SpeedM=0.15)
    char.equ_effect.append(EquEffect(name='元素释放', icon='/equipment/skill/29.png', cd=15, data=118200))
    pass


@register
def suit_38(char: CharacterProperty):
    """
      召唤精灵一起战斗。
    [火灵安珀]
    每2秒施放一次火花：伤害量19,200%
    每3秒恢复1%的生命值
    [水灵阿库娅]
    每3秒施放一次水弹：伤害量24,000%
    每3秒恢复1%的魔法值
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    一攻击中止/继续攻击
    - 冷却时间1秒
    [风灵希尔珂]
    每2秒施放一次刀风：伤害量19,200%
    移动速度 +15%
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    - 攻击中止/继续攻击
    - 冷却时间1秒
    [元素释放][装备主动技能]对精灵下达协同攻击指令。
    - 消耗150精灵之魂
    一攻击时，精灵之魂 +10（冷却时间1秒）
    一被击时，精灵之魂- 5（冷却时间1秒）
    - 元素释放伤害量:118,200%
    """
    suit_37(char)
    pass


@register
def suit_39(char: CharacterProperty):
    """
      召唤精灵一起战斗。
    [火灵安珀]
    每2秒施放一次火花：伤害量19,200%
    每3秒恢复1%的生命值
    [水灵阿库娅]
    每3秒施放一次水弹：伤害量24,000%
    每3秒恢复1%的魔法值
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    一攻击中止/继续攻击
    - 冷却时间1秒
    [风灵希尔珂]
    每2秒施放一次刀风：伤害量19,200%
    移动速度 +15%
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    - 攻击中止/继续攻击
    - 冷却时间1秒
    [元素释放][装备主动技能]对精灵下达协同攻击指令。
    - 消耗150精灵之魂
    一攻击时，精灵之魂 +10（冷却时间1秒）
    一被击时，精灵之魂- 5（冷却时间1秒）
    - 元素释放伤害量:118,200%
    """
    suit_37(char)
    pass


@register
def suit_40(char: CharacterProperty):
    """
      召唤精灵一起战斗。
    [火灵安珀]
    每2秒施放一次火花：伤害量19,200%
    每3秒恢复1%的生命值
    [水灵阿库娅]
    每3秒施放一次水弹：伤害量24,000%
    每3秒恢复1%的魔法值
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    一攻击中止/继续攻击
    - 冷却时间1秒
    [风灵希尔珂]
    每2秒施放一次刀风：伤害量19,200%
    移动速度 +15%
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    - 攻击中止/继续攻击
    - 冷却时间1秒
    [元素释放][装备主动技能]对精灵下达协同攻击指令。
    - 消耗150精灵之魂
    一攻击时，精灵之魂 +10（冷却时间1秒）
    一被击时，精灵之魂- 5（冷却时间1秒）
    - 元素释放伤害量:118,200%
    """
    suit_37(char)
    pass


@register
def suit_41(char: CharacterProperty):
    """
      召唤精灵一起战斗。
    [火灵安珀]
    每2秒施放一次火花：伤害量19,200%
    每3秒恢复1%的生命值
    [水灵阿库娅]
    每3秒施放一次水弹：伤害量24,000%
    每3秒恢复1%的魔法值
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    一攻击中止/继续攻击
    - 冷却时间1秒
    [风灵希尔珂]
    每2秒施放一次刀风：伤害量19,200%
    移动速度 +15%
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    - 攻击中止/继续攻击
    - 冷却时间1秒
    [元素释放][装备主动技能]对精灵下达协同攻击指令。
    - 消耗150精灵之魂
    一攻击时，精灵之魂 +10（冷却时间1秒）
    一被击时，精灵之魂- 5（冷却时间1秒）
    - 元素释放伤害量:118,200%
    """
    suit_37(char)
    pass


@register
def suit_42(char: CharacterProperty):
    """
      召唤精灵一起战斗。
    [火灵安珀]
    每2秒施放一次火花：伤害量19,200%
    每3秒恢复1%的生命值
    [水灵阿库娅]
    每3秒施放一次水弹：伤害量24,000%
    每3秒恢复1%的魔法值
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    一攻击中止/继续攻击
    - 冷却时间1秒
    [风灵希尔珂]
    每2秒施放一次刀风：伤害量19,200%
    移动速度 +15%
    [精灵女王提泰妮娅]每5秒发动毁灭弹或毁灭斩击。
    - 伤害量47,520%
    [停止攻击开关][装备主动技能]控制精灵们的攻击。
    - 攻击中止/继续攻击
    - 冷却时间1秒
    [元素释放][装备主动技能]对精灵下达协同攻击指令。
    - 消耗150精灵之魂
    一攻击时，精灵之魂 +10（冷却时间1秒）
    一被击时，精灵之魂- 5（冷却时间1秒）
    - 元素释放伤害量:118,200%
    """
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
    """
    -
    """
    pass


@register
def suit_44(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_45(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_46(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_47(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_48(char: CharacterProperty):
    """
      根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。

    - 数值总和每达到 +11时， 技能范围增加2% (最多叠加7次)
    - 防具 : 数值每达到 +5， 所受物理/魔法伤害 - 1%% (最多叠加7次)
    - 首饰 : 数值每达到 +3， 技能伤害  +1% (最多叠加7次)
    - 特殊装备 : 数值每达到 +3， 所有速度  +2% (最多叠加7次)
    """
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
    """
      根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。

    - 数值总和每达到 +11时， 技能范围增加2% (最多叠加7次)
    - 防具 : 数值每达到 +5， 所受物理/魔法伤害 - 1%% (最多叠加7次)
    - 首饰 : 数值每达到 +3， 技能伤害  +1% (最多叠加7次)
    - 特殊装备 : 数值每达到 +3， 所有速度  +2% (最多叠加7次)
    """
    suit_48(char)
    pass


@register
def suit_50(char: CharacterProperty):
    """
      根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。

    - 数值总和每达到 +11时， 技能范围增加2% (最多叠加7次)
    - 防具 : 数值每达到 +5， 所受物理/魔法伤害 - 1%% (最多叠加7次)
    - 首饰 : 数值每达到 +3， 技能伤害  +1% (最多叠加7次)
    - 特殊装备 : 数值每达到 +3， 所有速度  +2% (最多叠加7次)
    """
    suit_48(char)
    pass


@register
def suit_51(char: CharacterProperty):
    """
      根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。

    - 数值总和每达到 +11时， 技能范围增加2% (最多叠加7次)
    - 防具 : 数值每达到 +5， 所受物理/魔法伤害 - 1%% (最多叠加7次)
    - 首饰 : 数值每达到 +3， 技能伤害  +1% (最多叠加7次)
    - 特殊装备 : 数值每达到 +3， 所有速度  +2% (最多叠加7次)
    """
    suit_48(char)
    pass


@register
def suit_52(char: CharacterProperty):
    """
      根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。

    - 数值总和每达到 +11时， 技能范围增加2% (最多叠加7次)
    - 防具 : 数值每达到 +5， 所受物理/魔法伤害 - 1%% (最多叠加7次)
    - 首饰 : 数值每达到 +3， 技能伤害  +1% (最多叠加7次)
    - 特殊装备 : 数值每达到 +3， 所有速度  +2% (最多叠加7次)
    """
    suit_48(char)
    pass


@register
def suit_53(char: CharacterProperty):
    """
      根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。

    - 数值总和每达到 +11时， 技能范围增加2% (最多叠加12次)
    - 防具 : 数值每达到 +5， 所受物理/魔法伤害 - 1%% (最多叠加12次)
    - 首饰 : 数值每达到 +3， 技能伤害  +1% (最多叠加12次)
    - 特殊装备 : 数值每达到 +3， 所有速度  +2% (最多叠加12次)

    [辅助职业专属属性]

    装备的强化/增幅数值平均每增加1时， 适用以下效果。 (最多叠加12次)
    - 技能冷却时间 - 2%
    """

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
    """
      根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。

    - 数值总和每达到 +11时， 技能范围增加2% (最多叠加12次)
    - 防具 : 数值每达到 +5， 所受物理/魔法伤害 - 1%% (最多叠加12次)
    - 首饰 : 数值每达到 +3， 技能伤害  +1% (最多叠加12次)
    - 特殊装备 : 数值每达到 +3， 所有速度  +2% (最多叠加12次)



    [辅助职业专属属性]

    装备的强化/增幅数值平均每增加1时， 适用以下效果。 (最多叠加12次)
    - 技能冷却时间 - 2%
    """

    suit_53(char)
    pass


@register
def suit_55(char: CharacterProperty):
    """
      根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。

    - 数值总和每达到 +11时， 技能范围增加2% (最多叠加12次)
    - 防具 : 数值每达到 +5， 所受物理/魔法伤害 - 1%% (最多叠加12次)
    - 首饰 : 数值每达到 +3， 技能伤害  +1% (最多叠加12次)
    - 特殊装备 : 数值每达到 +3， 所有速度  +2% (最多叠加12次)



    [辅助职业专属属性]

    装备的强化/增幅数值平均每增加1时， 适用以下效果。 (最多叠加12次)
    - 技能冷却时间 - 2%
    """
    suit_53(char)
    pass


@register
def suit_56(char: CharacterProperty):
    """
      根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。

    - 数值总和每达到 +11时， 技能范围增加2% (最多叠加12次)
    - 防具 : 数值每达到 +5， 所受物理/魔法伤害 - 1%% (最多叠加12次)
    - 首饰 : 数值每达到 +3， 技能伤害  +1% (最多叠加12次)
    - 特殊装备 : 数值每达到 +3， 所有速度  +2% (最多叠加12次)



    [辅助职业专属属性]

    装备的强化/增幅数值平均每增加1时， 适用以下效果。 (最多叠加12次)
    - 技能冷却时间 - 2%
    """
    suit_53(char)
    pass


@register
def suit_57(char: CharacterProperty):
    """
      根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。

    - 数值总和每达到 +11时， 技能范围增加2% (最多叠加12次)
    - 防具 : 数值每达到 +5， 所受物理/魔法伤害 - 1%% (最多叠加12次)
    - 首饰 : 数值每达到 +3， 技能伤害  +1% (最多叠加12次)
    - 特殊装备 : 数值每达到 +3， 所有速度  +2% (最多叠加12次)



    [辅助职业专属属性]

    装备的强化/增幅数值平均每增加1时， 适用以下效果。 (最多叠加12次)
    - 技能冷却时间 - 2%
    """
    suit_53(char)
    pass


@register
def suit_58(char: CharacterProperty):
    """
      根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。
    - 超过110时，每11点，增加2%技能伤害（最多叠加2次）
    - 数值总和每达到 +11时， 技能范围增加2% (最多叠加12次)
    - 防具 : 数值每达到 +5， 所受物理/魔法伤害 - 1%% (最多叠加12次)
    - 首饰 : 数值每达到 +3， 技能伤害  +1% (最多叠加12次)
    - 特殊装备 : 数值每达到 +3， 所有速度  +2% (最多叠加12次)

    [淘银热]

    根据防具/首饰/特殊装备的强化/增幅数值总和，投掷银币攻击（冷却时间10秒）

    ?* 银币伤害量信息
    - 低于88 : 9,600%%
    - 88 ~ 109 : 10,440%
    - 110 ~ 131 : 12,000%
    - 132以上 : 14,400%

    [辅助职业专属属性]

    装备的强化/增幅数值总和每增加11时， 适用以下效果。 (最多叠加12次)
    - 技能冷却时间 - 2%
    - 110以上时， 数值每达到 +11， 增益量  +750 (最多叠加2次)
    """
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
    """
      根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。
    - 超过110时，每11点，增加2%技能伤害（最多叠加2次）
    - 数值总和每达到 +11时， 技能范围增加2% (最多叠加12次)
    - 防具 : 数值每达到 +5， 所受物理/魔法伤害 - 1%% (最多叠加12次)
    - 首饰 : 数值每达到 +3， 技能伤害  +1% (最多叠加12次)
    - 特殊装备 : 数值每达到 +3， 所有速度  +2% (最多叠加12次)

    [淘银热]

    根据防具/首饰/特殊装备的强化/增幅数值总和，投掷银币攻击（冷却时间10秒）

    ?* 银币伤害量信息
    - 低于88 : 9,600%%
    - 88 ~ 109 : 10,440%
    - 110 ~ 131 : 12,000%
    - 132以上 : 14,400%

    [辅助职业专属属性]

    装备的强化/增幅数值总和每增加11时， 适用以下效果。 (最多叠加12次)
    - 技能冷却时间 - 2%
    - 110以上时， 数值每达到 +11， 增益量  +750 (最多叠加2次)
    """
    suit_58(char)
    pass


@register
def suit_60(char: CharacterProperty):
    """
      根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。
    - 超过110时，每11点，增加2%技能伤害（最多叠加2次）
    - 数值总和每达到 +11时， 技能范围增加2% (最多叠加12次)
    - 防具 : 数值每达到 +5， 所受物理/魔法伤害 - 1%% (最多叠加12次)
    - 首饰 : 数值每达到 +3， 技能伤害  +1% (最多叠加12次)
    - 特殊装备 : 数值每达到 +3， 所有速度  +2% (最多叠加12次)

    [淘银热]

    根据防具/首饰/特殊装备的强化/增幅数值总和，投掷银币攻击（冷却时间10秒）

    ?* 银币伤害量信息
    - 低于88 : 9,600%%
    - 88 ~ 109 : 10,440%
    - 110 ~ 131 : 12,000%
    - 132以上 : 14,400%

    [辅助职业专属属性]

    装备的强化/增幅数值总和每增加11时， 适用以下效果。 (最多叠加12次)
    - 技能冷却时间 - 2%
    - 110以上时， 数值每达到 +11， 增益量  +750 (最多叠加2次)
    """
    suit_58(char)
    pass


@register
def suit_61(char: CharacterProperty):
    """
      根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。
    - 超过110时，每11点，增加2%技能伤害（最多叠加2次）
    - 数值总和每达到 +11时， 技能范围增加2% (最多叠加12次)
    - 防具 : 数值每达到 +5， 所受物理/魔法伤害 - 1%% (最多叠加12次)
    - 首饰 : 数值每达到 +3， 技能伤害  +1% (最多叠加12次)
    - 特殊装备 : 数值每达到 +3， 所有速度  +2% (最多叠加12次)

    [淘银热]

    根据防具/首饰/特殊装备的强化/增幅数值总和，投掷银币攻击（冷却时间10秒）

    ?* 银币伤害量信息
    - 低于88 : 9,600%%
    - 88 ~ 109 : 10,440%
    - 110 ~ 131 : 12,000%
    - 132以上 : 14,400%

    [辅助职业专属属性]

    装备的强化/增幅数值总和每增加11时， 适用以下效果。 (最多叠加12次)
    - 技能冷却时间 - 2%
    - 110以上时， 数值每达到 +11， 增益量  +750 (最多叠加2次)
    """
    suit_58(char)
    pass


@register
def suit_62(char: CharacterProperty):
    """
      根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。
    - 超过110时，每11点，增加2%技能伤害（最多叠加2次）
    - 数值总和每达到 +11时， 技能范围增加2% (最多叠加12次)
    - 防具 : 数值每达到 +5， 所受物理/魔法伤害 - 1%% (最多叠加12次)
    - 首饰 : 数值每达到 +3， 技能伤害  +1% (最多叠加12次)
    - 特殊装备 : 数值每达到 +3， 所有速度  +2% (最多叠加12次)

    [淘银热]

    根据防具/首饰/特殊装备的强化/增幅数值总和，投掷银币攻击（冷却时间10秒）

    ?* 银币伤害量信息
    - 低于88 : 9,600%%
    - 88 ~ 109 : 10,440%
    - 110 ~ 131 : 12,000%
    - 132以上 : 14,400%

    [辅助职业专属属性]

    装备的强化/增幅数值总和每增加11时， 适用以下效果。 (最多叠加12次)
    - 技能冷却时间 - 2%
    - 110以上时， 数值每达到 +11， 增益量  +750 (最多叠加2次)
    """
    suit_58(char)
    pass


@register
def suit_63(char: CharacterProperty):
    """
      根据防具/首饰/特殊装备的强化/增幅数值总和， 适用以下效果。
    - 超过110时，每11点，增加2%技能伤害（最多叠加2次）
    - 数值总和每达到 +11时， 技能范围增加2% (最多叠加12次)
    - 防具 : 数值每达到 +5， 所受物理/魔法伤害 - 1%% (最多叠加12次)
    - 首饰 : 数值每达到 +3， 技能伤害  +1% (最多叠加12次)
    - 特殊装备 : 数值每达到 +3， 所有速度  +2% (最多叠加12次)

    [淘金热]

    根据防具/首饰/特殊装备的强化/增幅数值总和，投掷金币攻击（冷却时间10秒）

    ?* 金币伤害量 : 每次攻击3,000%%
    - 低于88 : 9,600%%
    - 88 ~ 109 : 10,440%
    - 110 ~ 131 : 12,000%
    - 132以上 : 14,400%

    [辅助职业专属属性]

    装备的强化/增幅数值总和每增加11时， 适用以下效果。 (最多叠加12次)
    - 技能冷却时间 - 2%
    - 121以上时， 数值每达到 +11， 增益量  +1500 (最多叠加2次)
    """
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
    """
    -
    """
    pass


@register
def suit_65(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_66(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_67(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_68(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_69(char: CharacterProperty):
    """
      [虬龙之火]
    无色小晶块消耗量减少1个。
    所有速度  +10%
    """
    char.SetStatus(SpeedA=0.1, SpeedM=0.1, SpeedR=0.1)
    pass


@register
def suit_70(char: CharacterProperty):
    """
      [虬龙之火]
    无色小晶块消耗量减少1个。
    所有速度  +10%
    """
    suit_69(char)
    pass


@register
def suit_71(char: CharacterProperty):
    """
      [虬龙之火]
    无色小晶块消耗量减少1个。
    所有速度  +10%
    """
    suit_69(char)
    pass


@register
def suit_72(char: CharacterProperty):
    """
      [虬龙之火]
    无色小晶块消耗量减少1个。
    所有速度  +10%
    """
    suit_69(char)
    pass


@register
def suit_73(char: CharacterProperty):
    """
      [虬龙之火]
    无色小晶块消耗量减少1个。
    所有速度  +10%
    """
    suit_69(char)
    pass


@register
def suit_74(char: CharacterProperty):
    """
      [蛟龙之火]
    无色小晶块消耗量减少2个。
    所有速度  +10%

    [龙之胜战]
    攻击时， 青龙升天。 (冷却时间10秒)
    * 青龙升天伤害量 : 14,400%
    """
    char.SetStatus(SpeedA=0.1, SpeedM=0.1, SpeedR=0.1)
    char.equ_effect.append(EquEffect(name='龙之胜战', icon='/equipment/suit/1.png', cd=10, data=14400))
    pass


@register
def suit_75(char: CharacterProperty):
    """
      [蛟龙之火]
    无色小晶块消耗量减少2个。
    所有速度  +10%

    [龙之胜战]
    攻击时， 青龙升天。 (冷却时间10秒)
    * 青龙升天伤害量 : 14,400%
    """
    suit_74(char)
    pass


@register
def suit_76(char: CharacterProperty):
    """
      [蛟龙之火]
    无色小晶块消耗量减少2个。
    所有速度  +10%

    [龙之胜战]
    攻击时， 青龙升天。 (冷却时间10秒)
    * 青龙升天伤害量 : 14,400%
    """
    suit_74(char)
    pass


@register
def suit_77(char: CharacterProperty):
    """
      [蛟龙之火]
    无色小晶块消耗量减少2个。
    所有速度  +10%

    [龙之胜战]
    攻击时， 青龙升天。 (冷却时间10秒)
    * 青龙升天伤害量 : 14,400%
    """
    suit_74(char)
    pass


@register
def suit_78(char: CharacterProperty):
    """
      [蛟龙之火]
    无色小晶块消耗量减少2个。
    所有速度  +10%

    [龙之胜战]
    攻击时， 青龙升天。 (冷却时间10秒)
    * 青龙升天伤害量 : 14,400%
    """
    suit_74(char)
    pass


@register
def suit_79(char: CharacterProperty):
    """
      通过释放龙之力来增强自己。
    [烛龙之火]
    无色小晶块消耗量减少3个。
    一。不会减少到少于1个
    所有速度  +10%
    [烛龙腾霄]
    攻击时，烛龙腾霄。（冷却时间10秒）
    *烛龙腾霄伤害量:14,400%
    [荧惑如意珠][装备主动技能]
    将[烛龙之火]变更为[烛龙的如意珠
    ]，效果持续30秒。
    - 删除无色小晶块消耗量减少效果
    - 所有速度增加效果变更为30%
    - 技能伤害 +3%
    - 无色小晶块技能的消耗量固定30个
    一施放消耗无色小晶块的技能时，发动白龙强袭（冷却时间3秒）
    * 白龙强袭伤害量:6,000%
    - 冷却时间60秒
    """
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
    """
      通过释放龙之力来增强自己。
    [烛龙之火]
    无色小晶块消耗量减少3个。
    一。不会减少到少于1个
    所有速度  +10%
    [烛龙腾霄]
    攻击时，烛龙腾霄。（冷却时间10秒）
    *烛龙腾霄伤害量:14,400%
    [荧惑如意珠][装备主动技能]
    将[烛龙之火]变更为[烛龙的如意珠
    ]，效果持续30秒。
    - 删除无色小晶块消耗量减少效果
    - 所有速度增加效果变更为30%
    - 技能伤害 +3%
    - 无色小晶块技能的消耗量固定30个
    一施放消耗无色小晶块的技能时，发动白龙强袭（冷却时间3秒）
    * 白龙强袭伤害量:6,000%
    - 冷却时间60秒
    """
    suit_79(char)
    pass


@register
def suit_81(char: CharacterProperty):
    """
      通过释放龙之力来增强自己。
    [烛龙之火]
    无色小晶块消耗量减少3个。
    一。不会减少到少于1个
    所有速度  +10%
    [烛龙腾霄]
    攻击时，烛龙腾霄。（冷却时间10秒）
    *烛龙腾霄伤害量:14,400%
    [荧惑如意珠][装备主动技能]
    将[烛龙之火]变更为[烛龙的如意珠
    ]，效果持续30秒。
    - 删除无色小晶块消耗量减少效果
    - 所有速度增加效果变更为30%
    - 技能伤害 +3%
    - 无色小晶块技能的消耗量固定30个
    一施放消耗无色小晶块的技能时，发动白龙强袭（冷却时间3秒）
    * 白龙强袭伤害量:6,000%
    - 冷却时间60秒
    """
    suit_79(char)
    pass


@register
def suit_82(char: CharacterProperty):
    """
      通过释放龙之力来增强自己。
    [烛龙之火]
    无色小晶块消耗量减少3个。
    一。不会减少到少于1个
    所有速度  +10%
    [烛龙腾霄]
    攻击时，烛龙腾霄。（冷却时间10秒）
    *烛龙腾霄伤害量:14,400%
    [荧惑如意珠][装备主动技能]
    将[烛龙之火]变更为[烛龙的如意珠
    ]，效果持续30秒。
    - 删除无色小晶块消耗量减少效果
    - 所有速度增加效果变更为30%
    - 技能伤害 +3%
    - 无色小晶块技能的消耗量固定30个
    一施放消耗无色小晶块的技能时，发动白龙强袭（冷却时间3秒）
    * 白龙强袭伤害量:6,000%
    - 冷却时间60秒
    """
    suit_79(char)
    pass


@register
def suit_83(char: CharacterProperty):
    """
      通过释放龙之力来增强自己。
    [烛龙之火]
    无色小晶块消耗量减少3个。
    一。不会减少到少于1个
    所有速度  +10%
    [烛龙腾霄]
    攻击时，烛龙腾霄。（冷却时间10秒）
    *烛龙腾霄伤害量:14,400%
    [荧惑如意珠][装备主动技能]
    将[烛龙之火]变更为[烛龙的如意珠
    ]，效果持续30秒。
    - 删除无色小晶块消耗量减少效果
    - 所有速度增加效果变更为30%
    - 技能伤害 +3%
    - 无色小晶块技能的消耗量固定30个
    一施放消耗无色小晶块的技能时，发动白龙强袭（冷却时间3秒）
    * 白龙强袭伤害量:6,000%
    - 冷却时间60秒
    """
    suit_79(char)
    pass


@register
def suit_84(char: CharacterProperty):
    """
      [应龙之火]
    无色小晶块消耗量减少5个。
    所有速度  +10%

    [应龙腾霄]
    攻击时，应龙腾霄。（冷却时间10秒）* 应龙腾霄伤害量:14,400%
    [荧惑如意珠][装备主动技能]将[应龙之火]变更为[应龙的如意珠]
    一删除无色小晶块消耗量减少效果
    - 所有速度增加效果变更为30%
    - 技能伤害 +3%
    - 无色小晶块技能的消耗量固定15个
    一施放消耗无色小晶块的技能时，白龙强袭（冷却时间3秒）
    * 白龙强袭伤害量:6,000%
    - 再次使用，解除效果
    [应龙之怒]
    [应龙的如意珠]效果生效状态下攻击时，黑龙横扫敌人。（冷却时间4秒）
    *横扫伤害量:7,200%
    """
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
    """
    -
    """
    pass


@register
def suit_86(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_87(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_88(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_89(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_90(char: CharacterProperty):
    """
      进入地下城时， 净化状态自动生效

    [净化]
    - 技能冷却时间 - 30.0%
    - 每秒恢复0.5%生命值/魔法值
    """
    char.SetSkillCD(cd=0.3)
    pass


@register
def suit_91(char: CharacterProperty):
    """
      进入地下城时， 净化状态自动生效

    [净化]
    - 技能冷却时间 - 30.0%
    - 每秒恢复0.5%生命值/魔法值
    """
    suit_90(char)
    pass


@register
def suit_92(char: CharacterProperty):
    """
      进入地下城时， 净化状态自动生效

    [净化]
    - 技能冷却时间 - 30.0%
    - 每秒恢复0.5%生命值/魔法值
    """
    suit_90(char)
    pass


@register
def suit_93(char: CharacterProperty):
    """
      进入地下城时， 净化状态自动生效

    [净化]
    - 技能冷却时间 - 30.0%
    - 每秒恢复0.5%生命值/魔法值
    """
    suit_90(char)
    pass


@register
def suit_94(char: CharacterProperty):
    """
      进入地下城时， 净化状态自动生效

    [净化]
    - 技能冷却时间 - 30.0%
    - 每秒恢复0.5%生命值/魔法值
    """
    suit_90(char)
    pass


@register
def suit_95(char: CharacterProperty):
    """
      [暗黑净化][装备主动技能]根据使用者的意愿调整净化与堕落状态。
    - 进入地下城时，净化状态自动生效
    - 冷却时间：300秒
    [净化]
    - 技能伤害  +17.5%
    - 技能冷却时间- 30%（觉醒技能除外）
    - 每秒恢复0.5%的生命值和魔法值
    [堕落]
    - 技能冷却时间- 55%（觉醒技能除外）
    - 进入霸体状态
    """
    if char.equ_options.get('2', 0) == 0:
        char.SetStatus(SkillAttack=0.175)
        char.SetSkillCD(cd=0.3)
    else:
        char.SetSkillCD(cd=0.55)
    pass


@register
def suit_96(char: CharacterProperty):
    """
      [暗黑净化][装备主动技能]根据使用者的意愿调整净化与堕落状态。
    - 进入地下城时，净化状态自动生效
    - 冷却时间：300秒
    [净化]
    - 技能伤害  +17.5%
    - 技能冷却时间- 30%（觉醒技能除外）
    - 每秒恢复0.5%的生命值和魔法值
    [堕落]
    - 技能冷却时间- 55%（觉醒技能除外）
    - 进入霸体状态
    """
    suit_95(char)
    pass


@register
def suit_97(char: CharacterProperty):
    """
      [暗黑净化][装备主动技能]根据使用者的意愿调整净化与堕落状态。
    - 进入地下城时，净化状态自动生效
    - 冷却时间：300秒
    [净化]
    - 技能伤害  +17.5%
    - 技能冷却时间- 30%（觉醒技能除外）
    - 每秒恢复0.5%的生命值和魔法值
    [堕落]
    - 技能冷却时间- 55%（觉醒技能除外）
    - 进入霸体状态
    """
    suit_95(char)
    pass


@register
def suit_98(char: CharacterProperty):
    """
      [暗黑净化][装备主动技能]根据使用者的意愿调整净化与堕落状态。
    - 进入地下城时，净化状态自动生效
    - 冷却时间：300秒
    [净化]
    - 技能伤害  +17.5%
    - 技能冷却时间- 30%（觉醒技能除外）
    - 每秒恢复0.5%的生命值和魔法值
    [堕落]
    - 技能冷却时间- 55%（觉醒技能除外）
    - 进入霸体状态
    """
    suit_95(char)
    pass


@register
def suit_99(char: CharacterProperty):
    """
      [暗黑净化][装备主动技能]根据使用者的意愿调整净化与堕落状态。
    - 进入地下城时，净化状态自动生效
    - 冷却时间：300秒
    [净化]
    - 技能伤害  +17.5%
    - 技能冷却时间- 30%（觉醒技能除外）
    - 每秒恢复0.5%的生命值和魔法值
    [堕落]
    - 技能冷却时间- 55%（觉醒技能除外）
    - 进入霸体状态
    """
    suit_95(char)
    pass


@register
def suit_100(char: CharacterProperty):
    """
      [暗黑净化][装备主动技能]
    根据使用者的意愿调整净化与堕落状态。
    - 进入地下城时，净化状态自动生效
    - 冷却时间：300秒
    [净化]
    - 技能伤害 +17.5%
    - 技能冷却时间- 30%（觉醒技能除外）
    - 每秒恢复0.5%的生命值和魔法值
    - 每10秒生成最大生命值10%的保护罩
    [堕落]
    - 技能冷却时间- 55%（觉醒技能除外）
    - 进入霸体状态
    - 跳跃时可以再跳跃一次
    """
    suit_95(char)
    pass


@register
def suit_101(char: CharacterProperty):
    """
      [暗黑净化][装备主动技能]
    根据使用者的意愿调整净化与堕落状态。
    - 进入地下城时，净化状态自动生效
    - 冷却时间：300秒
    [净化]
    - 技能伤害 +17.5%
    - 技能冷却时间- 30%（觉醒技能除外）
    - 每秒恢复0.5%的生命值和魔法值
    - 每10秒生成最大生命值10%的保护罩
    [堕落]
    - 技能冷却时间- 55%（觉醒技能除外）
    - 进入霸体状态
    - 跳跃时可以再跳跃一次
    """
    suit_95(char)
    pass


@register
def suit_102(char: CharacterProperty):
    """
      [暗黑净化][装备主动技能]
    根据使用者的意愿调整净化与堕落状态。
    - 进入地下城时，净化状态自动生效
    - 冷却时间：300秒
    [净化]
    - 技能伤害 +17.5%
    - 技能冷却时间- 30%（觉醒技能除外）
    - 每秒恢复0.5%的生命值和魔法值
    - 每10秒生成最大生命值10%的保护罩
    [堕落]
    - 技能冷却时间- 55%（觉醒技能除外）
    - 进入霸体状态
    - 跳跃时可以再跳跃一次
    """
    suit_95(char)
    pass


@register
def suit_103(char: CharacterProperty):
    """
      [暗黑净化][装备主动技能]
    根据使用者的意愿调整净化与堕落状态。
    - 进入地下城时，净化状态自动生效
    - 冷却时间：300秒
    [净化]
    - 技能伤害 +17.5%
    - 技能冷却时间- 30%（觉醒技能除外）
    - 每秒恢复0.5%的生命值和魔法值
    - 每10秒生成最大生命值10%的保护罩
    [堕落]
    - 技能冷却时间- 55%（觉醒技能除外）
    - 进入霸体状态
    - 跳跃时可以再跳跃一次
    """
    suit_95(char)
    pass


@register
def suit_104(char: CharacterProperty):
    """
      [暗黑净化][装备主动技能]
    根据使用者的意愿调整净化与堕落状态。
    - 进入地下城时，净化状态自动生效
    - 冷却时间：300秒
    [净化]
    - 技能伤害 +17.5%
    - 技能冷却时间- 30%（觉醒技能除外）
    - 每秒恢复0.5%的生命值和魔法值
    - 每10秒生成最大生命值10%的保护罩
    [堕落]
    - 技能冷却时间- 55%（觉醒技能除外）
    - 进入霸体状态
    - 跳跃时可以再跳跃一次
    """
    suit_95(char)
    pass


@register
def suit_105(char: CharacterProperty):
    """
      净化与堕落达到协调后， 进入均衡状态。

    [均衡]
    - 每秒恢复0.5%生命值/魔法值
    - 赋予生命值最大值10%的保护罩
    - 进入霸体状态
    - 跳跃时可以再跳跃一次

    [暗黑净化] [装备发动属性]
    选择使用净化和堕落的力量。
    进入地下城时， 净化状态自动生效
    - 冷却时间300秒

    [净化]
    - 技能伤害  +17.5%
    - 技能冷却时间 - 30.0%?

    [堕落]
    - 技能冷却时间 - 55.0%
    """
    suit_95(char)
    pass


# endregion
# region 天命者的气运


@register
def suit_106(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_107(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_108(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_109(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_110(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_111(char: CharacterProperty):
    """
      神秘的蝴蝶为角色带来好运。 有一定几率初始化技能冷却时间， 提供更多施放技能的机会。

    [第一次幸运]
    技能伤害  +3%

    [天命所归]
    攻击时， 有3%的几率发动[神的祝福]。 (发动冷却1秒)
    剩余冷却时间33秒以下的技能中， 初始化剩余时间最长的1个技能 (觉醒技能除外)
    """
    char.SetStatus(SkillAttack=0.03)
    pass


@register
def suit_112(char: CharacterProperty):
    """
      神秘的蝴蝶为角色带来好运。 有一定几率初始化技能冷却时间， 提供更多施放技能的机会。

    [第一次幸运]
    技能伤害  +3%

    [天命所归]
    攻击时， 有3%的几率发动[神的祝福]。 (发动冷却1秒)
    剩余冷却时间33秒以下的技能中， 初始化剩余时间最长的1个技能 (觉醒技能除外)
    """
    suit_111(char)
    pass


@register
def suit_113(char: CharacterProperty):
    """
      神秘的蝴蝶为角色带来好运。 有一定几率初始化技能冷却时间， 提供更多施放技能的机会。

    [第一次幸运]
    技能伤害  +3%

    [天命所归]
    攻击时， 有3%的几率发动[神的祝福]。 (发动冷却1秒)
    剩余冷却时间33秒以下的技能中， 初始化剩余时间最长的1个技能 (觉醒技能除外)
    """
    suit_111(char)
    pass


@register
def suit_114(char: CharacterProperty):
    """
      神秘的蝴蝶为角色带来好运。 有一定几率初始化技能冷却时间， 提供更多施放技能的机会。

    [第一次幸运]
    技能伤害  +3%

    [天命所归]
    攻击时， 有3%的几率发动[神的祝福]。 (发动冷却1秒)
    剩余冷却时间33秒以下的技能中， 初始化剩余时间最长的1个技能 (觉醒技能除外)
    """
    suit_111(char)
    pass


@register
def suit_115(char: CharacterProperty):
    """
      神秘的蝴蝶为角色带来好运。 有一定几率初始化技能冷却时间， 提供更多施放技能的机会。

    [第一次幸运]
    技能伤害  +3%

    [天命所归]
    攻击时， 有3%的几率发动[神的祝福]。 (发动冷却1秒)
    剩余冷却时间33秒以下的技能中， 初始化剩余时间最长的1个技能 (觉醒技能除外)
    """
    suit_111(char)
    pass


@register
def suit_116(char: CharacterProperty):
    """
      [第一次幸运]
    技能伤害  +3%

    [第二次幸运]
    攻击时， 有3%的几率所有属性增加33 (持续时间33秒， 发动冷却1秒)

    [天命所归]
    - 攻击时，有3%的几率发动[天命所归]。（发动机会冷却时间1秒）- 剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外）
    - 剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外）
    - 立即发动[第二次幸运]
    """
    char.SetStatus(SkillAttack=0.03)
    char.AddElementDB('火',33,1)
    char.AddElementDB('冰',33,1)
    char.AddElementDB('光',33,1)
    char.AddElementDB('暗',33,1)
    pass


@register
def suit_117(char: CharacterProperty):
    """
      [第一次幸运]
    技能伤害  +3%

    [第二次幸运]
    攻击时， 有3%的几率所有属性增加33 (持续时间33秒， 发动冷却1秒)

    [天命所归]
    - 攻击时，有3%的几率发动[天命所归]。（发动机会冷却时间1秒）- 剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外）
    - 剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外）
    - 立即发动[第二次幸运]
    """
    suit_116(char)
    pass


@register
def suit_118(char: CharacterProperty):
    """
      [第一次幸运]
    技能伤害  +3%

    [第二次幸运]
    攻击时， 有3%的几率所有属性增加33 (持续时间33秒， 发动冷却1秒)

    [天命所归]
    - 攻击时，有3%的几率发动[天命所归]。（发动机会冷却时间1秒）- 剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外）
    - 剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外）
    - 立即发动[第二次幸运]
    """
    suit_116(char)
    pass


@register
def suit_119(char: CharacterProperty):
    """
      [第一次幸运]
    技能伤害  +3%

    [第二次幸运]
    攻击时， 有3%的几率所有属性增加33 (持续时间33秒， 发动冷却1秒)

    [天命所归]
    - 攻击时，有3%的几率发动[天命所归]。（发动机会冷却时间1秒）- 剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外）
    - 剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外）
    - 立即发动[第二次幸运]
    """
    suit_116(char)
    pass


@register
def suit_120(char: CharacterProperty):
    """
      [第一次幸运]
    技能伤害  +3%

    [第二次幸运]
    攻击时， 有3%的几率所有属性增加33 (持续时间33秒， 发动冷却1秒)

    [天命所归]
    - 攻击时，有3%的几率发动[天命所归]。（发动机会冷却时间1秒）- 剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外）
    - 剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外）
    - 立即发动[第二次幸运]
    """
    suit_116(char)
    pass


@register
def suit_121(char: CharacterProperty):
    """
      [第一次幸运]
    - 技能伤害  +3%
    [第二次幸运]
    - 攻击时，有3%的几率使所有属性强化 +33（持续时间33秒；发动机会冷却时间1秒）
    [天命所归]
    - 攻击时，有3%的几率发动[天命所归]。（发动机会冷却时间1秒）
    - 剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外）
    - 初始化所有剩余冷却时间33秒以下的技能（觉醒技能除外；冷却时间33秒）
    - 立即发动[第二次幸运]
    [幸运之翼][装备主动技能]
    - [第二次幸运]、[天命所归]发动
    几率提高3倍，效果持续33秒
    - 冷却时间：99秒
    - 立即发动[第二次幸运]
    """
    suit_116(char)
    pass


@register
def suit_122(char: CharacterProperty):
    """
      [第一次幸运]
    - 技能伤害  +3%
    [第二次幸运]
    - 攻击时，有3%的几率使所有属性强化 +33（持续时间33秒；发动机会冷却时间1秒）
    [天命所归]
    - 攻击时，有3%的几率发动[天命所归]。（发动机会冷却时间1秒）
    - 剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外）
    - 初始化所有剩余冷却时间33秒以下的技能（觉醒技能除外；冷却时间33秒）
    - 立即发动[第二次幸运]
    [幸运之翼][装备主动技能]
    - [第二次幸运]、[天命所归]发动
    几率提高3倍，效果持续33秒
    - 冷却时间：100秒
    - 立即发动[第二次幸运]
    """
    suit_116(char)
    pass


@register
def suit_123(char: CharacterProperty):
    """
      [第一次幸运]
    - 技能伤害  +3%
    [第二次幸运]
    - 攻击时，有3%的几率使所有属性强化 +33（持续时间33秒；发动机会冷却时间1秒）
    [天命所归]
    - 攻击时，有3%的几率发动[天命所归]。（发动机会冷却时间1秒）
    - 剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外）
    - 初始化所有剩余冷却时间33秒以下的技能（觉醒技能除外；冷却时间33秒）
    - 立即发动[第二次幸运]
    [幸运之翼][装备主动技能]
    - [第二次幸运]、[天命所归]发动
    几率提高3倍，效果持续33秒
    - 冷却时间：101秒
    - 立即发动[第二次幸运]
    """
    suit_116(char)
    pass


@register
def suit_124(char: CharacterProperty):
    """
      [第一次幸运]
    - 技能伤害  +3%
    [第二次幸运]
    - 攻击时，有3%的几率使所有属性强化 +33（持续时间33秒；发动机会冷却时间1秒）
    [天命所归]
    - 攻击时，有3%的几率发动[天命所归]。（发动机会冷却时间1秒）
    - 剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外）
    - 初始化所有剩余冷却时间33秒以下的技能（觉醒技能除外；冷却时间33秒）
    - 立即发动[第二次幸运]
    [幸运之翼][装备主动技能]
    - [第二次幸运]、[天命所归]发动
    几率提高3倍，效果持续33秒
    - 冷却时间：102秒
    - 立即发动[第二次幸运]
    """
    suit_116(char)
    pass


@register
def suit_125(char: CharacterProperty):
    """
      [第一次幸运]
    - 技能伤害  +3%
    [第二次幸运]
    - 攻击时，有3%的几率使所有属性强化 +33（持续时间33秒；发动机会冷却时间1秒）
    [天命所归]
    - 攻击时，有3%的几率发动[天命所归]。（发动机会冷却时间1秒）
    - 剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外）
    - 初始化所有剩余冷却时间33秒以下的技能（觉醒技能除外；冷却时间33秒）
    - 立即发动[第二次幸运]
    [幸运之翼][装备主动技能]
    - [第二次幸运]、[天命所归]发动
    几率提高3倍，效果持续33秒
    - 冷却时间：103秒
    - 立即发动[第二次幸运]
    """
    suit_116(char)
    pass


@register
def suit_126(char: CharacterProperty):
    """
      [第一次幸运]
    技能伤害  +3%

    [第二次幸运]
    攻击时， 有3%的几率所有属性增加33 (持续时间33秒， 发动冷却1秒)

    [第二次幸运]
    - 攻击时，有3%的几率使所有属性强化 +33（持续时间33秒；发动机会冷却时间1秒）
    [天命所归]
    - 攻击时，有3%的几率发动[天命所归]：（发动机会冷却时间1秒）
    - 剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外）
    - 剩余冷却时间33秒以下的技能中，随机初始化1个技能（觉醒技能除外）
    - 初始化所有剩余冷却时间33秒以下的技能（觉醒技能除外；冷却时间33秒）
    - 立即发动[第二次幸运]
    [幸运之翼][装备主动技能]
    - [第二次幸运]、[天命所归]发动
    几率提高3倍，效果持续33秒
    - 冷却时间：99秒
    - 立即发动[第二次幸运]
    """
    suit_116(char)
    pass


# endregion
# region 究极能量


@register
def suit_127(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_128(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_129(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_130(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_131(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_132(char: CharacterProperty):
    """
      [限制器解除]
    - 解除觉醒技能链接 (辅助职业除外)
    - 100级技能攻击力  +30%
    - 85级技能攻击力  +30%
    - 85级技能冷却时间 - 30% (辅助职业除外)
    - 50级技能冷却时间 - 30% (辅助职业除外)
    """
    if not char.buffer:
        char.SetSkillCD(50,50,0.3,[])
        char.SetSkillCD(85,85,0.3,[])
    char.SetSkillRation(100,100,0.3)
    char.SetSkillRation(85,85,0.3)
    pass


@register
def suit_133(char: CharacterProperty):
    """
      [限制器解除]
    - 解除觉醒技能链接 (辅助职业除外)
    - 100级技能攻击力  +30%
    - 85级技能攻击力  +30%
    - 85级技能冷却时间 - 30% (辅助职业除外)
    - 50级技能冷却时间 - 30% (辅助职业除外)
    """
    suit_132(char)
    pass


@register
def suit_134(char: CharacterProperty):
    """
      [限制器解除]
    - 解除觉醒技能链接 (辅助职业除外)
    - 100级技能攻击力  +30%
    - 85级技能攻击力  +30%
    - 85级技能冷却时间 - 30% (辅助职业除外)
    - 50级技能冷却时间 - 30% (辅助职业除外)
    """
    suit_132(char)
    pass


@register
def suit_135(char: CharacterProperty):
    """
      [限制器解除]
    - 解除觉醒技能链接 (辅助职业除外)
    - 100级技能攻击力  +30%
    - 85级技能攻击力  +30%
    - 85级技能冷却时间 - 30% (辅助职业除外)
    - 50级技能冷却时间 - 30% (辅助职业除外)
    """
    suit_132(char)
    pass


@register
def suit_136(char: CharacterProperty):
    """
      [限制器解除]
    - 解除觉醒技能链接 (辅助职业除外)
    - 100级技能攻击力  +30%
    - 85级技能攻击力  +30%
    - 85级技能冷却时间 - 30% (辅助职业除外)
    - 50级技能冷却时间 - 30% (辅助职业除外)
    """
    suit_132(char)
    pass


@register
def suit_137(char: CharacterProperty):
    """
      [限制器解除]
    - 解除觉醒技能链接 (辅助职业除外)
    - 100级技能攻击力  +40%
    - 85级技能攻击力  +40%
    - 100级技能冷却时间 - 50% (辅助职业除外)
    - 85级技能冷却时间 - 30% (辅助职业除外)
    - 50级技能冷却时间 - 50% (辅助职业除外)
    """
    if not char.buffer:
        char.SetSkillCD(50,50,0.5,[])
        char.SetSkillCD(85,85,0.3,[])
        char.SetSkillCD(100,100,0.5,[])
    char.SetSkillRation(100,100,0.4)
    char.SetSkillRation(85,85,0.4)
    pass


@register
def suit_138(char: CharacterProperty):
    """
      [限制器解除]
    - 解除觉醒技能链接 (辅助职业除外)
    - 100级技能攻击力  +40%
    - 85级技能攻击力  +40%
    - 100级技能冷却时间 - 50% (辅助职业除外)
    - 85级技能冷却时间 - 30% (辅助职业除外)
    - 50级技能冷却时间 - 50% (辅助职业除外)
    """
    suit_137(char)
    pass


@register
def suit_139(char: CharacterProperty):
    """
      [限制器解除]
    - 解除觉醒技能链接 (辅助职业除外)
    - 100级技能攻击力  +40%
    - 85级技能攻击力  +40%
    - 100级技能冷却时间 - 50% (辅助职业除外)
    - 85级技能冷却时间 - 30% (辅助职业除外)
    - 50级技能冷却时间 - 50% (辅助职业除外)
    """
    suit_137(char)
    pass


@register
def suit_140(char: CharacterProperty):
    """
      [限制器解除]
    - 解除觉醒技能链接 (辅助职业除外)
    - 100级技能攻击力  +40%
    - 85级技能攻击力  +40%
    - 100级技能冷却时间 - 50% (辅助职业除外)
    - 85级技能冷却时间 - 30% (辅助职业除外)
    - 50级技能冷却时间 - 50% (辅助职业除外)
    """
    suit_137(char)
    pass


@register
def suit_141(char: CharacterProperty):
    """
      [限制器解除]
    - 解除觉醒技能链接 (辅助职业除外)
    - 100级技能攻击力  +40%
    - 85级技能攻击力  +40%
    - 100级技能冷却时间 - 50% (辅助职业除外)
    - 85级技能冷却时间 - 30% (辅助职业除外)
    - 50级技能冷却时间 - 50% (辅助职业除外)
    """
    suit_137(char)
    pass


@register
def suit_142(char: CharacterProperty):
    """
      [限制器解除]
    - 解除觉醒技能链接 (辅助职业除外)
    - 100级技能攻击力  +60%
    - 85级技能攻击力  +50%
    - 50级技能攻击力  +10%
    - 100级技能冷却时间 - 50% (辅助职业除外)
    - 85级技能冷却时间 - 30% (辅助职业除外)
    - 50级技能冷却时间 - 50% (辅助职业除外)

    [抵达极限的能量]
    施放三觉技能时进入能量蓄气状态 (最大15)
    - 每秒 +1
    - 每消耗1个无色小晶块 +1

    最大填充时释放能量造成大量伤害
    * 能量释放伤害 : 240,000%
    """
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
    """
      [限制器解除]
    - 解除觉醒技能链接 (辅助职业除外)
    - 100级技能攻击力  +60%
    - 85级技能攻击力  +50%
    - 50级技能攻击力  +10%
    - 100级技能冷却时间 - 50% (辅助职业除外)
    - 85级技能冷却时间 - 30% (辅助职业除外)
    - 50级技能冷却时间 - 50% (辅助职业除外)

    [抵达极限的能量]
    施放三觉技能时进入能量蓄气状态 (最大15)
    - 每秒 +1
    - 每消耗1个无色小晶块 +1

    最大填充时释放能量造成大量伤害
    * 能量释放伤害 : 240,000%
    """
    suit_142(char)
    pass


@register
def suit_144(char: CharacterProperty):
    """
      [限制器解除]
    - 解除觉醒技能链接 (辅助职业除外)
    - 100级技能攻击力  +60%
    - 85级技能攻击力  +50%
    - 50级技能攻击力  +10%
    - 100级技能冷却时间 - 50% (辅助职业除外)
    - 85级技能冷却时间 - 30% (辅助职业除外)
    - 50级技能冷却时间 - 50% (辅助职业除外)

    [抵达极限的能量]
    施放三觉技能时进入能量蓄气状态 (最大15)
    - 每秒 +1
    - 每消耗1个无色小晶块 +1

    最大填充时释放能量造成大量伤害
    * 能量释放伤害 : 240,000%
    """
    suit_142(char)
    pass


@register
def suit_145(char: CharacterProperty):
    """
      [限制器解除]
    - 解除觉醒技能链接 (辅助职业除外)
    - 100级技能攻击力  +60%
    - 85级技能攻击力  +50%
    - 50级技能攻击力  +10%
    - 100级技能冷却时间 - 50% (辅助职业除外)
    - 85级技能冷却时间 - 30% (辅助职业除外)
    - 50级技能冷却时间 - 50% (辅助职业除外)

    [抵达极限的能量]
    施放三觉技能时进入能量蓄气状态 (最大15)
    - 每秒 +1
    - 每消耗1个无色小晶块 +1

    最大填充时释放能量造成大量伤害
    * 能量释放伤害 : 240,000%
    """
    suit_142(char)
    pass


@register
def suit_146(char: CharacterProperty):
    """
      [限制器解除]
    - 解除觉醒技能链接 (辅助职业除外)
    - 100级技能攻击力  +60%
    - 85级技能攻击力  +50%
    - 50级技能攻击力  +10%
    - 100级技能冷却时间 - 50% (辅助职业除外)
    - 85级技能冷却时间 - 30% (辅助职业除外)
    - 50级技能冷却时间 - 50% (辅助职业除外)

    [抵达极限的能量]
    施放三觉技能时进入能量蓄气状态 (最大15)
    - 每秒 +1
    - 每消耗1个无色小晶块 +1

    最大填充时释放能量造成大量伤害
    * 能量释放伤害 : 240,000%
    """
    suit_142(char)
    pass


@register
def suit_147(char: CharacterProperty):
    """
      [限制器解除]

    - 解除觉醒技能链接 (辅助职业除外)
    - 100级技能攻击力  +76%
    - 85级技能攻击力  +60%
    - 50级技能攻击力  +15%
    - 100级技能冷却时间 - 50% (辅助职业除外)
    - 85级技能冷却时间 - 30% (辅助职业除外)
    - 50级技能冷却时间 - 50% (辅助职业除外)

    [超越界限的能量]
    施放三觉技能时进入能量蓄气状态 (最大15)
    - 每秒 +1
    - 每消耗1个无色小晶块 +1


    最大填充时释放能量造成大量伤害
    * 能量释放伤害 : 360,000%
    """
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
    """
    -
    """
    pass


@register
def suit_149(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_150(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_151(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_152(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_153(char: CharacterProperty):
    """
      [无可违背的自然 - 干预]
    攻击时引发自然爆炸攻击敌人。 (冷却时间5秒)
    - 自然燃烧伤害8,640%
    """
    pass


@register
def suit_154(char: CharacterProperty):
    """
      [无可违背的自然 - 干预]
    攻击时引发自然爆炸攻击敌人。 (冷却时间5秒)
    - 自然燃烧伤害8,640%
    """
    char.equ_effect.append(EquEffect(name='自燃爆炸', icon='/equipment/suit/6.png', cd=5, data=8640))
    pass


@register
def suit_155(char: CharacterProperty):
    """
      [无可违背的自然 - 干预]
    攻击时引发自然爆炸攻击敌人。 (冷却时间5秒)
    - 自然燃烧伤害8,640%
    """
    suit_154(char)
    pass


@register
def suit_156(char: CharacterProperty):
    """
      [无可违背的自然 - 干预]
    攻击时引发自然爆炸攻击敌人。 (冷却时间5秒)
    - 自然燃烧伤害8,640%
    """
    suit_154(char)
    pass


@register
def suit_157(char: CharacterProperty):
    """
      [无可违背的自然 - 干预]
    攻击时引发自然爆炸攻击敌人。 (冷却时间5秒)
    - 自然燃烧伤害8,640%
    """
    suit_154(char)
    pass


@register
def suit_158(char: CharacterProperty):
    """
      [无可违背的自然 - 震怒]
    攻击时产生小型旋风， 攻击小范围的敌人， 并吸附敌人。 (冷却时间5秒)
    - 小型旋风伤害25920%
    """
    char.equ_effect.append(EquEffect(name='小型旋风', icon='/equipment/suit/6.png', cd=5, data=25920))
    pass


@register
def suit_159(char: CharacterProperty):
    """
      [无可违背的自然 - 震怒]
    攻击时产生小型旋风， 攻击小范围的敌人， 并吸附敌人。 (冷却时间5秒)
    - 小型旋风伤害25920%
    """
    suit_158(char)
    pass


@register
def suit_160(char: CharacterProperty):
    """
      [无可违背的自然 - 震怒]
    攻击时产生小型旋风， 攻击小范围的敌人， 并吸附敌人。 (冷却时间5秒)
    - 小型旋风伤害25920%
    """
    suit_158(char)
    pass


@register
def suit_161(char: CharacterProperty):
    """
      [无可违背的自然 - 震怒]
    攻击时产生小型旋风， 攻击小范围的敌人， 并吸附敌人。 (冷却时间5秒)
    - 小型旋风伤害25920%
    """
    suit_158(char)
    pass


@register
def suit_162(char: CharacterProperty):
    """
      [无可违背的自然 - 震怒]
    攻击时产生小型旋风， 攻击小范围的敌人， 并吸附敌人。 (冷却时间5秒)
    - 小型旋风伤害25920%
    """
    suit_158(char)
    pass


@register
def suit_163(char: CharacterProperty):
    """
      [无可违背的自然 - 制裁]
    攻击时引发落雷， 攻击大范围敌人。 (冷却时间5秒)
    - 落雷伤害43,200%
    """
    char.equ_effect.append(EquEffect(name='落雷', icon='/equipment/suit/6.png', cd=5, data=43200))
    pass


@register
def suit_164(char: CharacterProperty):
    """
      [无可违背的自然 - 制裁]
    攻击时引发落雷， 攻击大范围敌人。 (冷却时间5秒)
    - 落雷伤害43,200%
    """
    suit_163(char)
    pass


@register
def suit_165(char: CharacterProperty):
    """
      [无可违背的自然 - 制裁]
    攻击时引发落雷， 攻击大范围敌人。 (冷却时间5秒)
    - 落雷伤害43,200%
    """
    suit_163(char)
    pass


@register
def suit_166(char: CharacterProperty):
    """
      [无可违背的自然 - 制裁]
    攻击时引发落雷， 攻击大范围敌人。 (冷却时间5秒)
    - 落雷伤害43,200%
    """
    suit_163(char)
    pass


@register
def suit_167(char: CharacterProperty):
    """
      [无可违背的自然 - 制裁]
    攻击时引发落雷， 攻击大范围敌人。 (冷却时间5秒)
    - 落雷伤害43,200%
    """
    suit_163(char)
    pass


@register
def suit_168(char: CharacterProperty):
    """
      利用无可违背的自然之力，对敌人造成巨大伤害。
    [无可违背的自然- 灾变]攻击时引发暴风雪，攻击地图上的所有敌人。（冷却时间5秒）- 暴风雪伤害量 60,480%
    [狂澜怒涛][装备主动技能]发动狂澜怒涛，攻击地图上的所有敌人。
    - 狂澜怒涛伤害量104,400%
    - 冷却时间：60秒
    """
    char.equ_effect.append(EquEffect(name='狂澜怒涛', icon='/equipment/skill/54.png', cd=60, data=104400))
    char.equ_effect.append(EquEffect(name='暴风雪', icon='/equipment/suit/6.png', cd=5, data=60480))
    pass


# endregion
# region 诸神黄昏之女武神


@register
def suit_169(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_170(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_171(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_172(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_173(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_174(char: CharacterProperty):
    """
      借用女武神的一部分神秘力量。

    [突破] [装备发动属性]
    与女武神融合， 向前方突进。
    - 正面突破伤害 : 6,360%
    - 冷却时间8秒
    """
    char.equ_effect.append(EquEffect(name='突破', icon='/equipment/skill/0.png', cd=8, data=6360))
    pass


@register
def suit_175(char: CharacterProperty):
    """
      借用女武神的一部分神秘力量。

    [突破] [装备发动属性]
    与女武神融合， 向前方突进。
    - 正面突破伤害 : 6,360%
    - 冷却时间9秒
    """
    suit_174(char)
    pass


@register
def suit_176(char: CharacterProperty):
    """
      借用女武神的一部分神秘力量。

    [突破] [装备发动属性]
    与女武神融合， 向前方突进。
    - 正面突破伤害 : 6,360%
    - 冷却时间10秒
    """
    suit_174(char)
    pass


@register
def suit_177(char: CharacterProperty):
    """
      借用女武神的一部分神秘力量。

    [突破] [装备发动属性]
    与女武神融合， 向前方突进。
    - 正面突破伤害 : 6,360%
    - 冷却时间11秒
    """
    suit_174(char)
    pass


@register
def suit_178(char: CharacterProperty):
    """
      借用女武神的一部分神秘力量。

    [突破] [装备发动属性]
    与女武神融合， 向前方突进。
    - 正面突破伤害 : 6,360%
    - 冷却时间12秒
    """
    suit_174(char)
    pass


@register
def suit_179(char: CharacterProperty):
    """
      借用女武神的一部分神秘力量。

    [突破] [装备发动属性]
    与女武神融合， 向前方突进。
    - 正面突破伤害 : 6,360%
    - 冷却时间8秒

    [审判][装备发动属性]
    与女武神融合， 移动到敌人后方进行攻击。
    - 审判伤害 : 9,300%
    - 冷却时间15秒
    """
    char.equ_effect.append(EquEffect(name='突破', icon='/equipment/skill/0.png', cd=8, data=6360))
    char.equ_effect.append(EquEffect(name='审判', icon='/equipment/skill/1.png', cd=15, data=9300))
    pass


@register
def suit_180(char: CharacterProperty):
    """
      借用女武神的一部分神秘力量。

    [突破] [装备发动属性]
    与女武神融合， 向前方突进。
    - 正面突破伤害 : 6,360%
    - 冷却时间8秒

    [审判][装备发动属性]
    与女武神融合， 移动到敌人后方进行攻击。
    - 审判伤害 : 9,300%
    - 冷却时间16秒
    """
    suit_179(char)
    pass


@register
def suit_181(char: CharacterProperty):
    """
      借用女武神的一部分神秘力量。

    [突破] [装备发动属性]
    与女武神融合， 向前方突进。
    - 正面突破伤害 : 6,360%
    - 冷却时间8秒

    [审判][装备发动属性]
    与女武神融合， 移动到敌人后方进行攻击。
    - 审判伤害 : 9,300%
    - 冷却时间17秒
    """
    suit_179(char)
    pass


@register
def suit_182(char: CharacterProperty):
    """
      借用女武神的一部分神秘力量。

    [突破] [装备发动属性]
    与女武神融合， 向前方突进。
    - 正面突破伤害 : 6,360%
    - 冷却时间8秒

    [审判][装备发动属性]
    与女武神融合， 移动到敌人后方进行攻击。
    - 审判伤害 : 9,300%
    - 冷却时间18秒
    """
    suit_179(char)
    pass


@register
def suit_183(char: CharacterProperty):
    """
      借用女武神的一部分神秘力量。

    [突破] [装备发动属性]
    与女武神融合， 向前方突进。
    - 正面突破伤害 : 6,360%
    - 冷却时间8秒

    [审判][装备发动属性]
    与女武神融合， 移动到敌人后方进行攻击。
    - 审判伤害 : 9,300%
    - 冷却时间19秒
    """
    suit_179(char)
    pass


@register
def suit_184(char: CharacterProperty):
    """
      借用女武神的一部分神秘力量。

    [突破] [装备发动属性]

    与女武神融合， 向前方突进。
    - 正面突破伤害 : 6,360%
    - 冷却时间8秒

    [审判][装备发动属性]
    与女武神融合， 移动到敌人后方进行攻击。
    - 审判伤害 : 9,300%
    - 冷却时间15秒

    每施放8次无色小晶块技能时， 发动[天罚] 。 (冷却时间20秒)

    [天罚]
    召唤女武神， 对四周敌人施以天罚。
    - 天罚伤害 : 136800%
    """
    char.equ_effect.append(EquEffect(name='突破', icon='/equipment/skill/0.png', cd=8, data=6360))
    char.equ_effect.append(EquEffect(name='审判', icon='/equipment/skill/1.png', cd=15, data=9300))
    char.equ_effect.append(EquEffect(name='天罚', icon='/equipment/suit/7.png', cd=20, data=136800))
    pass


@register
def suit_185(char: CharacterProperty):
    """
      借用女武神的一部分神秘力量。

    [突破] [装备发动属性]

    与女武神融合， 向前方突进。
    - 正面突破伤害 : 6,360%
    - 冷却时间8秒

    [审判][装备发动属性]
    与女武神融合， 移动到敌人后方进行攻击。
    - 审判伤害 : 9,300%
    - 冷却时间15秒

    每施放8次无色小晶块技能时， 发动[天罚] 。 (冷却时间20秒)

    [天罚]
    召唤女武神， 对四周敌人施以天罚。
    - 天罚伤害 : 136800%
    """
    suit_184(char)
    pass


@register
def suit_186(char: CharacterProperty):
    """
      借用女武神的一部分神秘力量。

    [突破] [装备发动属性]

    与女武神融合， 向前方突进。
    - 正面突破伤害 : 6,360%
    - 冷却时间8秒

    [审判][装备发动属性]
    与女武神融合， 移动到敌人后方进行攻击。
    - 审判伤害 : 9,300%
    - 冷却时间15秒

    每施放8次无色小晶块技能时， 发动[天罚] 。 (冷却时间20秒)

    [天罚]
    召唤女武神， 对四周敌人施以天罚。
    - 天罚伤害 : 136800%
    """
    suit_184(char)
    pass

@register
def suit_187(char: CharacterProperty):
    """
      借用女武神的一部分神秘力量。

    [突破] [装备发动属性]

    与女武神融合， 向前方突进。
    - 正面突破伤害 : 6,360%
    - 冷却时间8秒

    [审判][装备发动属性]
    与女武神融合， 移动到敌人后方进行攻击。
    - 审判伤害 : 9,300%
    - 冷却时间15秒

    每施放8次无色小晶块技能时， 发动[天罚] 。 (冷却时间20秒)

    [天罚]
    召唤女武神， 对四周敌人施以天罚。
    - 天罚伤害 : 136800%
    """
    suit_184(char)
    pass


@register
def suit_188(char: CharacterProperty):
    """
      借用女武神的一部分神秘力量。

    [突破] [装备发动属性]

    与女武神融合， 向前方突进。
    - 正面突破伤害 : 6,360%
    - 冷却时间8秒

    [审判][装备发动属性]
    与女武神融合， 移动到敌人后方进行攻击。
    - 审判伤害 : 9,300%
    - 冷却时间15秒

    每施放8次无色小晶块技能时， 发动[天罚] 。 (冷却时间20秒)

    [天罚]
    召唤女武神， 对四周敌人施以天罚。
    - 天罚伤害 : 136800%
    """
    suit_184(char)
    pass


@register
def suit_189(char: CharacterProperty):
    """
      借用女武神的一部分神秘力量。

    [突破] [装备发动属性]
    与女武神融合， 向前方突进。
    - 正面突破伤害 : 6,360%
    - 冷却时间8秒

    [审判][装备发动属性]
    与女武神融合， 移动到敌人后方进行攻击。
    - 审判伤害 : 9,300%
    - 冷却时间15秒

    [降临][装备发动属性]
    发挥女武神真正的力量， 降临世间。
    - 降临伤害 : 329,400%
    - 冷却时间140秒

    每施放8次无色小晶块技能时， 发动[天罚] 。 (冷却时间20秒)

    [天罚]
    召唤女武神， 对四周敌人施以天罚。
    - 天罚伤害 : 136800%
    """
    char.equ_effect.append(EquEffect(name='突破', icon='/equipment/skill/0.png', cd=8, data=6360))
    char.equ_effect.append(EquEffect(name='审判', icon='/equipment/skill/1.png', cd=15, data=9300))
    char.equ_effect.append(EquEffect(name='降临', icon='/equipment/skill/3.png', cd=140, data=329400))
    char.equ_effect.append(EquEffect(name='天罚', icon='/equipment/suit/7.png', cd=20, data=136800))
    pass


# endregion
# region 青丘灵珠


@register
def suit_190(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_191(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_192(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_193(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_194(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_195(char: CharacterProperty):
    """
      借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活
    - 攻击时，灵珠能量 +5（冷却时间1秒）
    - 灵珠最多可填充1个
    一青丘灵珠增益效果生效时，无法充能灵珠
    - 进入地下城时，灵珠能量填充100
    [青丘灵珠][装备主动技能]
    - 发动时，消耗能量充满的所有灵珠，激活增益效果
    - 每消耗1个灵珠，技能伤害 +10%
    - 增益效果持续时间30秒
    - 冷却时间30秒
    """
    char.SetStatus(SkillAttack=0.1)
    pass


@register
def suit_196(char: CharacterProperty):
    """
      借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活
    - 攻击时，灵珠能量 +5（冷却时间1秒）
    - 灵珠最多可填充1个
    一青丘灵珠增益效果生效时，无法充能灵珠
    - 进入地下城时，灵珠能量填充100
    [青丘灵珠][装备主动技能]
    - 发动时，消耗能量充满的所有灵珠，激活增益效果
    - 每消耗1个灵珠，技能伤害 +10%
    - 增益效果持续时间30秒
    - 冷却时间30秒
    """
    suit_195(char)
    pass


@register
def suit_197(char: CharacterProperty):
    """
      借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活
    - 攻击时，灵珠能量 +5（冷却时间1秒）
    - 灵珠最多可填充1个
    一青丘灵珠增益效果生效时，无法充能灵珠
    - 进入地下城时，灵珠能量填充100
    [青丘灵珠][装备主动技能]
    - 发动时，消耗能量充满的所有灵珠，激活增益效果
    - 每消耗1个灵珠，技能伤害 +10%
    - 增益效果持续时间30秒
    - 冷却时间30秒
    """
    suit_195(char)
    pass


@register
def suit_198(char: CharacterProperty):
    """
      借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活
    - 攻击时，灵珠能量 +5（冷却时间1秒）
    - 灵珠最多可填充1个
    一青丘灵珠增益效果生效时，无法充能灵珠
    - 进入地下城时，灵珠能量填充100
    [青丘灵珠][装备主动技能]
    - 发动时，消耗能量充满的所有灵珠，激活增益效果
    - 每消耗1个灵珠，技能伤害 +10%
    - 增益效果持续时间30秒
    - 冷却时间30秒
    """
    suit_195(char)
    pass


@register
def suit_199(char: CharacterProperty):
    """
      借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活
    - 攻击时，灵珠能量 +5（冷却时间1秒）
    - 灵珠最多可填充1个
    一青丘灵珠增益效果生效时，无法充能灵珠
    - 进入地下城时，灵珠能量填充100
    [青丘灵珠][装备主动技能]
    - 发动时，消耗能量充满的所有灵珠，激活增益效果
    - 每消耗1个灵珠，技能伤害 +10%
    - 增益效果持续时间30秒
    - 冷却时间30秒
    """
    suit_195(char)
    pass


@register
def suit_200(char: CharacterProperty):
    """
      借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活
    - 攻击时，灵珠能量 +9（冷却时间1秒）
    - 每秒灵珠能量 +1
    - 灵珠最多可填充2个
    - 青丘灵珠增益效果生效时，无法充能灵珠
    - 进入地下城时，灵珠能量填充200
    [青丘灵珠][装备主动技能]
    - 发动时，消耗能量充满的所有灵珠，激活增益效果
    - 每消耗1个灵珠，技能伤害 +10%
    - 增益效果持续时间30秒
    - 冷却时间30秒
    """
    char.SetStatus(SkillAttack=0.2)
    pass


@register
def suit_201(char: CharacterProperty):
    """
      借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活
    - 攻击时，灵珠能量 +9（冷却时间1秒）
    - 每秒灵珠能量 +1
    - 灵珠最多可填充2个
    - 青丘灵珠增益效果生效时，无法充能灵珠
    - 进入地下城时，灵珠能量填充200
    [青丘灵珠][装备主动技能]
    - 发动时，消耗能量充满的所有灵珠，激活增益效果
    - 每消耗1个灵珠，技能伤害 +10%
    - 增益效果持续时间30秒
    - 冷却时间30秒
    """
    suit_200(char)
    pass


@register
def suit_202(char: CharacterProperty):
    """
      借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活
    - 攻击时，灵珠能量 +9（冷却时间1秒）
    - 每秒灵珠能量 +1
    - 灵珠最多可填充2个
    - 青丘灵珠增益效果生效时，无法充能灵珠
    - 进入地下城时，灵珠能量填充200
    [青丘灵珠][装备主动技能]
    - 发动时，消耗能量充满的所有灵珠，激活增益效果
    - 每消耗1个灵珠，技能伤害 +10%
    - 增益效果持续时间30秒
    - 冷却时间30秒
    """
    suit_200(char)
    pass


@register
def suit_203(char: CharacterProperty):
    """
      借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活
    - 攻击时，灵珠能量 +9（冷却时间1秒）
    - 每秒灵珠能量 +1
    - 灵珠最多可填充2个
    - 青丘灵珠增益效果生效时，无法充能灵珠
    - 进入地下城时，灵珠能量填充200
    [青丘灵珠][装备主动技能]
    - 发动时，消耗能量充满的所有灵珠，激活增益效果
    - 每消耗1个灵珠，技能伤害 +10%
    - 增益效果持续时间30秒
    - 冷却时间30秒
    """
    suit_200(char)
    pass


@register
def suit_204(char: CharacterProperty):
    """
      借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活
    - 攻击时，灵珠能量 +9（冷却时间1秒）
    - 每秒灵珠能量 +1
    - 灵珠最多可填充2个
    - 青丘灵珠增益效果生效时，无法充能灵珠
    - 进入地下城时，灵珠能量填充200
    [青丘灵珠][装备主动技能]
    - 发动时，消耗能量充满的所有灵珠，激活增益效果
    - 每消耗1个灵珠，技能伤害 +10%
    - 增益效果持续时间30秒
    - 冷却时间30秒
    """
    suit_200(char)
    pass


@register
def suit_205(char: CharacterProperty):
    """
      借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活
    一攻击时，灵珠能量  +9（冷却时间1秒）
    - 每秒灵珠能量  +2
    - 灵珠最多可填充3个
    一青丘灵珠增益效果生效时，也可以充能灵珠
    - 进入地下城时，灵珠能量填充200
    [青丘灵珠][装备主动技能]
    - 发动时，消耗能量充满的所有灵珠，激活增益效果
    - 每消耗1个灵珠，技能伤害 +10%
    - 增益效果持续时间30秒
    - 冷却时间30秒
    [青丘灵珠开关][装备主动技能]- 灵珠全部填满时，自动使用青丘灵珠增益效果（冷却时间1秒）
    - 再次使用时，关闭自动使用功能
    """
    char.SetStatus(SkillAttack=0.3)
    pass


@register
def suit_206(char: CharacterProperty):
    """
      借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活
    一攻击时，灵珠能量  +9（冷却时间1秒）
    - 每秒灵珠能量  +2
    - 灵珠最多可填充3个
    一青丘灵珠增益效果生效时，也可以充能灵珠
    - 进入地下城时，灵珠能量填充200
    [青丘灵珠][装备主动技能]
    - 发动时，消耗能量充满的所有灵珠，激活增益效果
    - 每消耗1个灵珠，技能伤害 +10%
    - 增益效果持续时间30秒
    - 冷却时间30秒
    [青丘灵珠开关][装备主动技能]- 灵珠全部填满时，自动使用青丘灵珠增益效果（冷却时间1秒）
    - 再次使用时，关闭自动使用功能
    """
    suit_205(char)
    pass


@register
def suit_207(char: CharacterProperty):
    """
      借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活
    一攻击时，灵珠能量  +9（冷却时间1秒）
    - 每秒灵珠能量  +2
    - 灵珠最多可填充3个
    一青丘灵珠增益效果生效时，也可以充能灵珠
    - 进入地下城时，灵珠能量填充200
    [青丘灵珠][装备主动技能]
    - 发动时，消耗能量充满的所有灵珠，激活增益效果
    - 每消耗1个灵珠，技能伤害 +10%
    - 增益效果持续时间30秒
    - 冷却时间30秒
    [青丘灵珠开关][装备主动技能]- 灵珠全部填满时，自动使用青丘灵珠增益效果（冷却时间1秒）
    - 再次使用时，关闭自动使用功能
    """
    suit_205(char)
    pass


@register
def suit_208(char: CharacterProperty):
    """
      借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活
    一攻击时，灵珠能量  +9（冷却时间1秒）
    - 每秒灵珠能量  +2
    - 灵珠最多可填充3个
    一青丘灵珠增益效果生效时，也可以充能灵珠
    - 进入地下城时，灵珠能量填充200
    [青丘灵珠][装备主动技能]
    - 发动时，消耗能量充满的所有灵珠，激活增益效果
    - 每消耗1个灵珠，技能伤害 +10%
    - 增益效果持续时间30秒
    - 冷却时间30秒
    [青丘灵珠开关][装备主动技能]- 灵珠全部填满时，自动使用青丘灵珠增益效果（冷却时间1秒）
    - 再次使用时，关闭自动使用功能
    """
    suit_205(char)
    pass


@register
def suit_209(char: CharacterProperty):
    """
      借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活
    一攻击时，灵珠能量  +9（冷却时间1秒）
    - 每秒灵珠能量  +2
    - 灵珠最多可填充3个
    一青丘灵珠增益效果生效时，也可以充能灵珠
    - 进入地下城时，灵珠能量填充200
    [青丘灵珠][装备主动技能]
    - 发动时，消耗能量充满的所有灵珠，激活增益效果
    - 每消耗1个灵珠，技能伤害 +10%
    - 增益效果持续时间30秒
    - 冷却时间30秒
    [青丘灵珠开关][装备主动技能]- 灵珠全部填满时，自动使用青丘灵珠增益效果（冷却时间1秒）
    - 再次使用时，关闭自动使用功能
    """
    suit_205(char)
    pass


@register
def suit_210(char: CharacterProperty):
    """
      借用青丘狐的灵珠之力，瞬间变强。[青丘灵珠]激活
    - 攻击时，灵珠能量 +14（冷却时间1秒）
    - 每秒灵珠能量 +3
    - 灵珠最多可填充4个
    一青丘灵珠增益效果生效时，也可以充能灵珠
    - 进入地下城时，灵珠能量填充400
    [青丘灵珠][装备主动技能]
    - 发动时，消耗能量充满的所有灵珠，激活增益效果
    - 每消耗1个灵珠，技能伤害 +10%
    - 增益效果持续时间30秒
    - 冷却时间30秒
    [青丘灵珠开关][装备主动技能]- 灵珠全部填满时，自动使用青丘灵珠增益效果（冷却时间1秒）
    - 再次使用时，关闭自动使用功能
    """
    char.SetStatus(SkillAttack=0.4)
    pass


# endregion
# region 群猎美学


@register
def suit_211(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_212(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_213(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_214(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_215(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_216(char: CharacterProperty):
    """
      与同伴在一起时， 会变得更强。

    [组队时生效]
    [群猎之力]
    给队员赋予光环， 获得以下效果。 (最多叠加1次)
    - 所有速度  +10%

    [酣畅狩猎][装备主动技能]
    发出吼叫震慑敌人。
    一 伤害量:3,825%
    一使被命中的敌人进入崩裂状态，持续30秒
    一冷却时间30秒
    （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）
    （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）
    [单人挑战时适用]
    - 技能伤害 +10.6%
    - 适用[群猎之力]效果
    - 不适用[酣畅狩猎]效果
    """
    if char.equ_options.get('3',0) == 0:
        char.SetStatus(SkillAttack=0.106)
    else:
        char.SetStatus(SkillAttack=0.08,SpeedA=0.1,SpeedM=0.1,SpeedR=0.1)
        char.equ_effect.append(EquEffect(name='酣畅狩猎', icon='/equipment/skill/15.png', cd=30, data=3825))
    pass


@register
def suit_217(char: CharacterProperty):
    """
      与同伴在一起时， 会变得更强。

    [组队时生效]
    [群猎之力]
    给队员赋予光环， 获得以下效果。 (最多叠加1次)
    - 所有速度  +10%

    [酣畅狩猎][装备主动技能]
    发出吼叫震慑敌人。
    一 伤害量:3,825%
    一使被命中的敌人进入崩裂状态，持续30秒
    一冷却时间30秒
    （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）
    （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）
    [单人挑战时适用]
    - 技能伤害 +10.6%
    - 适用[群猎之力]效果
    - 不适用[酣畅狩猎]效果
    """
    suit_216(char)
    pass


@register
def suit_218(char: CharacterProperty):
    """
      与同伴在一起时， 会变得更强。

    [组队时生效]
    [群猎之力]
    给队员赋予光环， 获得以下效果。 (最多叠加1次)
    - 所有速度  +10%

    [酣畅狩猎][装备主动技能]
    发出吼叫震慑敌人。
    一 伤害量:3,825%
    一使被命中的敌人进入崩裂状态，持续30秒
    一冷却时间30秒
    （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）
    （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）
    [单人挑战时适用]
    - 技能伤害 +10.6%
    - 适用[群猎之力]效果
    - 不适用[酣畅狩猎]效果
    """
    suit_216(char)
    pass


@register
def suit_219(char: CharacterProperty):
    """
      与同伴在一起时， 会变得更强。

    [组队时生效]
    [群猎之力]
    给队员赋予光环， 获得以下效果。 (最多叠加1次)
    - 所有速度  +10%

    [酣畅狩猎][装备主动技能]
    发出吼叫震慑敌人。
    一 伤害量:3,825%
    一使被命中的敌人进入崩裂状态，持续30秒
    一冷却时间30秒
    （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）
    （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）
    [单人挑战时适用]
    - 技能伤害 +10.6%
    - 适用[群猎之力]效果
    - 不适用[酣畅狩猎]效果
    """
    suit_216(char)
    pass


@register
def suit_220(char: CharacterProperty):
    """
      与同伴在一起时， 会变得更强。

    [组队时生效]
    [群猎之力]
    给队员赋予光环， 获得以下效果。 (最多叠加1次)
    - 所有速度  +10%

    [酣畅狩猎][装备主动技能]
    发出吼叫震慑敌人。
    一 伤害量:3,825%
    一使被命中的敌人进入崩裂状态，持续30秒
    一冷却时间30秒
    （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）
    （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）
    [单人挑战时适用]
    - 技能伤害 +10.6%
    - 适用[群猎之力]效果
    - 不适用[酣畅狩猎]效果
    """
    suit_216(char)
    pass


@register
def suit_221(char: CharacterProperty):
    """
      与同伴在一起时， 会变得更强。
    [组队时生效]
    [群猎之力]
    给队员赋予光环，获得以下效果。（最多叠加1次）
    一 所有速度±15%
    - 每10秒恢复10，000点的生命值和魔法值，持续10秒
    [酣畅狩猎][装备主动技能]
    发出吼叫震慑敌人。
    - 伤害量:5,738%
    一使被命中的敌人进入崩裂状态，持续45秒
    一冷却时间30秒
    （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）
    （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）
    [单人挑战时适用]
    - 技能伤害 +17.8%
    - 适用[群猎之力]效果
    - 不适用[酣畅狩猎]效果
    """
    if char.equ_options.get('3',0) == 0:
        char.SetStatus(SkillAttack=0.178)
    else:
        char.SetStatus(SkillAttack=0.08,SpeedA=0.15,SpeedM=0.15,SpeedR=0.15)
        char.equ_effect.append(EquEffect(name='酣畅狩猎', icon='/equipment/skill/15.png', cd=30, data=5738))
    pass


@register
def suit_222(char: CharacterProperty):
    """
      与同伴在一起时， 会变得更强。
    [组队时生效]
    [群猎之力]
    给队员赋予光环，获得以下效果。（最多叠加1次）
    一 所有速度±15%
    - 每10秒恢复10，000点的生命值和魔法值，持续10秒
    [酣畅狩猎][装备主动技能]
    发出吼叫震慑敌人。
    - 伤害量:5,738%
    一使被命中的敌人进入崩裂状态，持续45秒
    一冷却时间30秒
    （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）
    （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）
    [单人挑战时适用]
    - 技能伤害 +17.8%
    - 适用[群猎之力]效果
    - 不适用[酣畅狩猎]效果
    """
    suit_221(char)
    pass


@register
def suit_223(char: CharacterProperty):
    """
      与同伴在一起时， 会变得更强。
    [组队时生效]
    [群猎之力]
    给队员赋予光环，获得以下效果。（最多叠加1次）
    一 所有速度±15%
    - 每10秒恢复10，000点的生命值和魔法值，持续10秒
    [酣畅狩猎][装备主动技能]
    发出吼叫震慑敌人。
    - 伤害量:5,738%
    一使被命中的敌人进入崩裂状态，持续45秒
    一冷却时间30秒
    （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）
    （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）
    [单人挑战时适用]
    - 技能伤害 +17.8%
    - 适用[群猎之力]效果
    - 不适用[酣畅狩猎]效果
    """
    suit_221(char)
    pass


@register
def suit_224(char: CharacterProperty):
    """
      与同伴在一起时， 会变得更强。
    [组队时生效]
    [群猎之力]
    给队员赋予光环，获得以下效果。（最多叠加1次）
    一 所有速度±15%
    - 每10秒恢复10，000点的生命值和魔法值，持续10秒
    [酣畅狩猎][装备主动技能]
    发出吼叫震慑敌人。
    - 伤害量:5,738%
    一使被命中的敌人进入崩裂状态，持续45秒
    一冷却时间30秒
    （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）
    （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）
    [单人挑战时适用]
    - 技能伤害 +17.8%
    - 适用[群猎之力]效果
    - 不适用[酣畅狩猎]效果
    """
    suit_221(char)
    pass


@register
def suit_225(char: CharacterProperty):
    """
      与同伴在一起时， 会变得更强。
    [组队时生效]
    [群猎之力]
    给队员赋予光环，获得以下效果。（最多叠加1次）
    一 所有速度±15%
    - 每10秒恢复10，000点的生命值和魔法值，持续10秒
    [酣畅狩猎][装备主动技能]
    发出吼叫震慑敌人。
    - 伤害量:5,738%
    一使被命中的敌人进入崩裂状态，持续45秒
    一冷却时间30秒
    （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）
    （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）
    [单人挑战时适用]
    - 技能伤害 +17.8%
    - 适用[群猎之力]效果
    - 不适用[酣畅狩猎]效果
    """
    suit_221(char)
    pass


@register
def suit_226(char: CharacterProperty):
    """
      与同伴在一起时， 会变得更强。

    [组队挑战时适用]
    [群猎之力]
    给队员赋予光环，获得以下效果。（最多叠加1次）
    - 所有速度  +20%
    - 所受物理/魔法伤害- 10%
    - 每10秒恢复10，000点的生命值和魔法值，持续10秒
    [酣畅狩猎][装备主动技能]
    发出吼叫震慑敌人。
    - 伤害量:6,750%
    一。使被命中的敌人进入崩裂状态，持续60秒
    一冷却时间30秒
    （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）
    （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）
    [单人挑战时适用]
    - 技能伤害 +17.8%
    - 适用[群猎之力]效果
    - 不适用[酣畅狩猎]效果
    """
    if char.equ_options.get('3',0) == 0:
        char.SetStatus(SkillAttack=0.178)
    else:
        char.SetStatus(SkillAttack=0.08,SpeedA=0.2,SpeedM=0.0,SpeedR=0.0)
        char.equ_effect.append(EquEffect(name='酣畅狩猎', icon='/equipment/skill/15.png', cd=30, data=6750))
    pass


@register
def suit_227(char: CharacterProperty):
    """
      与同伴在一起时， 会变得更强。

    [组队挑战时适用]
    [群猎之力]
    给队员赋予光环，获得以下效果。（最多叠加1次）
    - 所有速度  +20%
    - 所受物理/魔法伤害- 10%
    - 每10秒恢复10，000点的生命值和魔法值，持续10秒
    [酣畅狩猎][装备主动技能]
    发出吼叫震慑敌人。
    - 伤害量:6,750%
    一。使被命中的敌人进入崩裂状态，持续60秒
    一冷却时间30秒
    （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）
    （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）
    [单人挑战时适用]
    - 技能伤害 +17.8%
    - 适用[群猎之力]效果
    - 不适用[酣畅狩猎]效果
    """
    suit_226(char)
    pass


@register
def suit_228(char: CharacterProperty):
    """
      与同伴在一起时， 会变得更强。

    [组队挑战时适用]
    [群猎之力]
    给队员赋予光环，获得以下效果。（最多叠加1次）
    - 所有速度  +20%
    - 所受物理/魔法伤害- 10%
    - 每10秒恢复10，000点的生命值和魔法值，持续10秒
    [酣畅狩猎][装备主动技能]
    发出吼叫震慑敌人。
    - 伤害量:6,750%
    一。使被命中的敌人进入崩裂状态，持续60秒
    一冷却时间30秒
    （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）
    （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）
    [单人挑战时适用]
    - 技能伤害 +17.8%
    - 适用[群猎之力]效果
    - 不适用[酣畅狩猎]效果
    """
    suit_226(char)
    pass


@register
def suit_229(char: CharacterProperty):
    """
      与同伴在一起时， 会变得更强。

    [组队挑战时适用]
    [群猎之力]
    给队员赋予光环，获得以下效果。（最多叠加1次）
    - 所有速度  +20%
    - 所受物理/魔法伤害- 10%
    - 每10秒恢复10，000点的生命值和魔法值，持续10秒
    [酣畅狩猎][装备主动技能]
    发出吼叫震慑敌人。
    - 伤害量:6,750%
    一。使被命中的敌人进入崩裂状态，持续60秒
    一冷却时间30秒
    （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）
    （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）
    [单人挑战时适用]
    - 技能伤害 +17.8%
    - 适用[群猎之力]效果
    - 不适用[酣畅狩猎]效果
    """
    suit_226(char)
    pass


@register
def suit_230(char: CharacterProperty):
    """
      与同伴在一起时， 会变得更强。

    [组队挑战时适用]
    [群猎之力]
    给队员赋予光环，获得以下效果。（最多叠加1次）
    - 所有速度  +20%
    - 所受物理/魔法伤害- 10%
    - 每10秒恢复10，000点的生命值和魔法值，持续10秒
    [酣畅狩猎][装备主动技能]
    发出吼叫震慑敌人。
    - 伤害量:6,750%
    一。使被命中的敌人进入崩裂状态，持续60秒
    一冷却时间30秒
    （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）
    （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）
    [单人挑战时适用]
    - 技能伤害 +17.8%
    - 适用[群猎之力]效果
    - 不适用[酣畅狩猎]效果
    """
    suit_226(char)
    pass


@register
def suit_231(char: CharacterProperty):
    """
      与同伴在一起时， 会变得更强。

    [组队挑战时适用]
    [群猎之力]
    给队员赋予光环，获得以下效果。（最多叠加1次）
    - 所有速度  +30%
    - 所受物理/魔法伤害- 15%
    - 每10秒恢复10，000点的生命值和魔法值，持续10秒
    [酣畅狩猎][装备主动技能]
    发出吼叫震慑敌人。
    - 伤害量 :9,563%
    一。使被命中的敌人进入最大叠加的崩裂状态，持续60秒
    一 冷却时间30秒
    （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）
    （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）
    [单人挑战时适用]
    - 技能伤害 +21.6%
    - 适用[群猎之力]效果
    """
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
    """
    -
    """
    pass


@register
def suit_233(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_234(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_235(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_236(char: CharacterProperty):
    """
    -
    """
    pass


@register
def suit_237(char: CharacterProperty):
    """
      操控魔攻核攻击敌人。
    [魔攻核]
    进入地下城时，召唤普通模式魔攻核。
    [命令：转换][装备主动技能]转换魔攻核的攻击模式。
    一普通模式/追击模式
    - 冷却时间：5秒
    [魔攻核：普通模式]
    每秒发射魔力波动。
    - 魔力波动伤害量:19.200%
    - 魔力波动范围:150px
    [魔攻核：追击模式]
    追击最强的敌人，每秒发射魔力波动。
    - 魔力波动伤害量:13.714%
    - 魔力波动范围:150px
    """
    if char.equ_options.get('4',0) == 0:
        char.equ_effect.append(EquEffect(name='普通模式', icon='/equipment/skill/57.png', cd=1, data=19200))
    else:
        char.equ_effect.append(EquEffect(name='追击模式', icon='/equipment/skill/57.png', cd=1, data=13714))
    pass


@register
def suit_238(char: CharacterProperty):
    """
      操控魔攻核攻击敌人。
    [魔攻核]
    进入地下城时，召唤普通模式魔攻核。
    [命令：转换][装备主动技能]转换魔攻核的攻击模式。
    一普通模式/追击模式
    - 冷却时间：5秒
    [魔攻核：普通模式]
    每秒发射魔力波动。
    - 魔力波动伤害量:19.200%
    - 魔力波动范围:150px
    [魔攻核：追击模式]
    追击最强的敌人，每秒发射魔力波动。
    - 魔力波动伤害量:13.714%
    - 魔力波动范围:150px
    """
    suit_237(char)
    pass


@register
def suit_239(char: CharacterProperty):
    """
      操控魔攻核攻击敌人。
    [魔攻核]
    进入地下城时，召唤普通模式魔攻核。
    [命令：转换][装备主动技能]转换魔攻核的攻击模式。
    一普通模式/追击模式
    - 冷却时间：5秒
    [魔攻核：普通模式]
    每秒发射魔力波动。
    - 魔力波动伤害量:19.200%
    - 魔力波动范围:150px
    [魔攻核：追击模式]
    追击最强的敌人，每秒发射魔力波动。
    - 魔力波动伤害量:13.714%
    - 魔力波动范围:150px
    """
    suit_237(char)
    pass


@register
def suit_240(char: CharacterProperty):
    """
      操控魔攻核攻击敌人。
    [魔攻核]
    进入地下城时，召唤普通模式魔攻核。
    [命令：转换][装备主动技能]转换魔攻核的攻击模式。
    一普通模式/追击模式
    - 冷却时间：5秒
    [魔攻核：普通模式]
    每秒发射魔力波动。
    - 魔力波动伤害量:19.200%
    - 魔力波动范围:150px
    [魔攻核：追击模式]
    追击最强的敌人，每秒发射魔力波动。
    - 魔力波动伤害量:13.714%
    - 魔力波动范围:150px
    """
    suit_237(char)
    pass


@register
def suit_241(char: CharacterProperty):
    """
      操控魔攻核攻击敌人。
    [魔攻核]
    进入地下城时，召唤普通模式魔攻核。
    [命令：转换][装备主动技能]转换魔攻核的攻击模式。
    一普通模式/追击模式
    - 冷却时间：5秒
    [魔攻核：普通模式]
    每秒发射魔力波动。
    - 魔力波动伤害量:19.200%
    - 魔力波动范围:150px
    [魔攻核：追击模式]
    追击最强的敌人，每秒发射魔力波动。
    - 魔力波动伤害量:13.714%
    - 魔力波动范围:150px
    """
    suit_237(char)
    pass


@register
def suit_242(char: CharacterProperty):
    """
      操控魔攻核攻击敌人。
    [魔攻核]
    进入地下城时，召唤普通模式魔攻核。
    [命令：转换][装备主动技能]转换魔攻核的攻击模式。
    - 普通模式/追击模式
    - 冷却时间：5秒
    [魔攻核：普通模式]
    每秒发射魔力波动。
    - 魔力波动伤害量:31,680%
    - 魔力波动范围:150px
    - 移动速度  +25%
    - 进入霸体状态
    [魔攻核：追击模式]
    追击最强的敌人，每秒发射魔力波动。
    - 魔力波动伤害量:20,571%
    - 魔力波动范围:150px
    """
    if char.equ_options.get('4',0) == 0:
        char.equ_effect.append(EquEffect(name='普通模式', icon='/equipment/skill/57.png', cd=1, data=31680))
        char.SetStatus(SpeedM=0.25)
    else:
        char.equ_effect.append(EquEffect(name='追击模式', icon='/equipment/skill/57.png', cd=1, data=20571))
    pass


@register
def suit_243(char: CharacterProperty):
    """
      操控魔攻核攻击敌人。
    [魔攻核]
    进入地下城时，召唤普通模式魔攻核。
    [命令：转换][装备主动技能]转换魔攻核的攻击模式。
    - 普通模式/追击模式
    - 冷却时间：5秒
    [魔攻核：普通模式]
    每秒发射魔力波动。
    - 魔力波动伤害量:31,680%
    - 魔力波动范围:150px
    - 移动速度  +25%
    - 进入霸体状态
    [魔攻核：追击模式]
    追击最强的敌人，每秒发射魔力波动。
    - 魔力波动伤害量:20,571%
    - 魔力波动范围:150px
    """
    suit_242(char)
    pass


@register
def suit_244(char: CharacterProperty):
    """
      操控魔攻核攻击敌人。
    [魔攻核]
    进入地下城时，召唤普通模式魔攻核。
    [命令：转换][装备主动技能]转换魔攻核的攻击模式。
    - 普通模式/追击模式
    - 冷却时间：5秒
    [魔攻核：普通模式]
    每秒发射魔力波动。
    - 魔力波动伤害量:31,680%
    - 魔力波动范围:150px
    - 移动速度  +25%
    - 进入霸体状态
    [魔攻核：追击模式]
    追击最强的敌人，每秒发射魔力波动。
    - 魔力波动伤害量:20,571%
    - 魔力波动范围:150px
    """
    suit_242(char)
    pass


@register
def suit_245(char: CharacterProperty):
    """
      操控魔攻核攻击敌人。
    [魔攻核]
    进入地下城时，召唤普通模式魔攻核。
    [命令：转换][装备主动技能]转换魔攻核的攻击模式。
    - 普通模式/追击模式
    - 冷却时间：5秒
    [魔攻核：普通模式]
    每秒发射魔力波动。
    - 魔力波动伤害量:31,680%
    - 魔力波动范围:150px
    - 移动速度  +25%
    - 进入霸体状态
    [魔攻核：追击模式]
    追击最强的敌人，每秒发射魔力波动。
    - 魔力波动伤害量:20,571%
    - 魔力波动范围:150px
    """
    suit_242(char)
    pass


@register
def suit_246(char: CharacterProperty):
    """
      操控魔攻核攻击敌人。
    [魔攻核]
    进入地下城时，召唤普通模式魔攻核。
    [命令：转换][装备主动技能]转换魔攻核的攻击模式。
    - 普通模式/追击模式
    - 冷却时间：5秒
    [魔攻核：普通模式]
    每秒发射魔力波动。
    - 魔力波动伤害量:31,680%
    - 魔力波动范围:150px
    - 移动速度  +25%
    - 进入霸体状态
    [魔攻核：追击模式]
    追击最强的敌人，每秒发射魔力波动。
    - 魔力波动伤害量:20,571%
    - 魔力波动范围:150px
    """
    suit_242(char)
    pass


@register
def suit_247(char: CharacterProperty):
    """
      操控魔攻核攻击敌人。
    [魔攻核]
    进入地下城时，召唤普通模式魔攻核。
    [命令：转换][装备主动技能]转换魔攻核的攻击模式。
    - 普通模式/追击模式
    - 冷却时间：5秒
    [魔攻核：普通模式]
    每秒发射魔力波动。
    - 魔力波动伤害量:47,520%
    - 魔力波动范围:200px
    - 移动速度  +25%
    一 进入霸体状态
    [魔攻核：追击模式]
    追击最强的敌人，每秒发射魔力波动。
    - 魔力波动伤害量:30,857%
    - 魔力波动范围:200px
    """
    if char.equ_options.get('4',0) == 0:
        char.equ_effect.append(EquEffect(name='普通模式', icon='/equipment/skill/57.png', cd=1, data=47520))
        char.SetStatus(SpeedM=0.25)
    else:
        char.equ_effect.append(EquEffect(name='追击模式', icon='/equipment/skill/57.png', cd=1, data=30857))
    pass


@register
def suit_248(char: CharacterProperty):
    """
      操控魔攻核攻击敌人。
    [魔攻核]
    进入地下城时，召唤普通模式魔攻核。
    [命令：转换][装备主动技能]转换魔攻核的攻击模式。
    - 普通模式/追击模式
    - 冷却时间：5秒
    [魔攻核：普通模式]
    每秒发射魔力波动。
    - 魔力波动伤害量:47,520%
    - 魔力波动范围:200px
    - 移动速度  +25%
    一 进入霸体状态
    [魔攻核：追击模式]
    追击最强的敌人，每秒发射魔力波动。
    - 魔力波动伤害量:30,857%
    - 魔力波动范围:200px
    """
    suit_247(char)
    pass


@register
def suit_249(char: CharacterProperty):
    """
      操控魔攻核攻击敌人。
    [魔攻核]
    进入地下城时，召唤普通模式魔攻核。
    [命令：转换][装备主动技能]转换魔攻核的攻击模式。
    - 普通模式/追击模式
    - 冷却时间：5秒
    [魔攻核：普通模式]
    每秒发射魔力波动。
    - 魔力波动伤害量:47,520%
    - 魔力波动范围:200px
    - 移动速度  +25%
    一 进入霸体状态
    [魔攻核：追击模式]
    追击最强的敌人，每秒发射魔力波动。
    - 魔力波动伤害量:30,857%
    - 魔力波动范围:200px
    """
    suit_247(char)
    pass


@register
def suit_250(char: CharacterProperty):
    """
      操控魔攻核攻击敌人。
    [魔攻核]
    进入地下城时，召唤普通模式魔攻核。
    [命令：转换][装备主动技能]转换魔攻核的攻击模式。
    - 普通模式/追击模式
    - 冷却时间：5秒
    [魔攻核：普通模式]
    每秒发射魔力波动。
    - 魔力波动伤害量:47,520%
    - 魔力波动范围:200px
    - 移动速度  +25%
    一 进入霸体状态
    [魔攻核：追击模式]
    追击最强的敌人，每秒发射魔力波动。
    - 魔力波动伤害量:30,857%
    - 魔力波动范围:200px
    """
    suit_247(char)
    pass


@register
def suit_251(char: CharacterProperty):
    """
      操控魔攻核攻击敌人。
    [魔攻核]
    进入地下城时，召唤普通模式魔攻核。
    [命令：转换][装备主动技能]转换魔攻核的攻击模式。
    - 普通模式/追击模式
    - 冷却时间：5秒
    [魔攻核：普通模式]
    每秒发射魔力波动。
    - 魔力波动伤害量:47,520%
    - 魔力波动范围:200px
    - 移动速度  +25%
    一 进入霸体状态
    [魔攻核：追击模式]
    追击最强的敌人，每秒发射魔力波动。
    - 魔力波动伤害量:30,857%
    - 魔力波动范围:200px
    """
    suit_247(char)
    pass


@register
def suit_252(char: CharacterProperty):
    """
      操控魔攻核攻击敌人。
    [魔攻核]
    进入地下城时，召唤普通模式魔攻核。
    [命令：转换][装备主动技能]转换魔攻核的攻击模式。
    - 普通模式/追击模式
    - 冷却时间：5秒
    [魔攻核：普通模式]
    每秒发射魔力波动。
    - 魔力波动伤害量:60,720%
    - 魔力波动范围:300px
    - 移动速度  +25%
    - 进入霸体状态
    - 所受物理/魔法伤害 - 10%
    [魔攻核：追击模式]
    追击最强的敌人，每秒发射魔力波动。
    - 魔力波动伤害量 :39,428%
    - 魔力波动范围:200px
    """
    if char.equ_options.get('4',0) == 0:
        char.equ_effect.append(EquEffect(name='普通模式', icon='/equipment/skill/57.png', cd=1, data=60720))
        char.SetStatus(SpeedM=0.25)
    else:
        char.equ_effect.append(EquEffect(name='追击模式', icon='/equipment/skill/57.png', cd=1, data=39428))
    pass


# endregion
