from core.basic.equipment import EquEffect
from core.abstract.character import CharacterProperty
from .register import register
# region 武器


@register
def equ_1(char: CharacterProperty):
    # DCALC_REMOVE: equ_1 - 百里挑一短剑
    # 魔法百分比技能
    # 魔法值 +15%
    # 施放速度 +2%
    # 魔法暴击率 +2%
    # rarity: 稀有
    pass


@register
def equ_2(char: CharacterProperty):
    # DCALC_REMOVE: equ_2 - 独一无二短剑
    # 魔法百分比技能
    # 魔法值 +15%
    # 施放速度 +2%
    # 魔法暴击率 +2%
    # rarity: 神器
    pass


@register
def equ_3(char: CharacterProperty):
    # DCALC_REMOVE: equ_3 - 传说承继 - 短剑
    # 魔法百分比技能
    # 魔法值 +15%
    # 施放速度 +2%
    # 魔法暴击率 +2%
    # rarity: 传说
    pass


@register
def equ_4(char: CharacterProperty):
    # DCALC_REMOVE: equ_4 - 英雄叙事诗 - 短剑
    # 魔法百分比技能
    # 魔法值 +15%
    # 施放速度 +2%
    # 魔法暴击率 +2%
    # rarity: 史诗
    pass


@register
def equ_5(char: CharacterProperty):
    # DCALC_REMOVE: equ_5 - 太初之星 - 短剑
    # 魔法百分比技能
    # 魔法值 +15%
    # 施放速度 +2%
    # 魔法暴击率 +2%
    # rarity: 太初
    pass


@register
def equ_6(char: CharacterProperty):
    # DCALC_REMOVE: equ_6 - 无影剑 - 摘叶飞花
    # 光属性攻击
    # [达到摘叶飞花境界的无影之剑]
    # 攻击时，无影之剑辉追踪敌人并贯穿进行攻击。
    # - 无影之剑射出数量：1个
    # - 追踪的敌人数量上限：2名
    # - 无影之剑总伤害量：32400%
    # - 冷却时间15秒
    # rarity: 传说
    char.equ_effect.append(EquEffect(name='无影之剑', icon='/equipment/icon/weapon/swordman/sswd/00227.png', cd=15, data=32400))
    pass


@register
def equ_7(char: CharacterProperty):
    # DCALC_REMOVE: equ_7 - 无影剑 - 问道顶峰
    # 光属性攻击
    # [达到顶峰境界的无影之剑]
    # 攻击时，无影之剑辉追踪敌人并贯穿进行攻击。
    # - 无影之剑射出数量：3个
    # - 追踪的敌人数量上限：4名
    # - 无影之剑总伤害量：48600%
    # - 冷却时间15秒
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='无影之剑', icon='/equipment/icon/weapon/swordman/sswd/00228.png', cd=15, data=48600))
    pass


@register
def equ_8(char: CharacterProperty):
    # DCALC_REMOVE: equ_8 - 无影剑 - 缘生劫灭
    # 光属性攻击
    # [达到缘生劫灭境界的无影之剑]
    # 攻击时，无影之剑辉追踪敌人并贯穿进行攻击。
    # - 无影之剑射出数量：4个
    # - 追踪的敌人数量上限：6名
    # - 无影之剑总伤害量：64800%
    # - 冷却时间10秒
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='无影之剑', icon='/equipment/icon/weapon/swordman/sswd/00229.png', cd=10, data=64800))
    pass


@register
def equ_9(char: CharacterProperty):
    # DCALC_REMOVE: equ_9 - 百里挑一太刀
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 +5% 冷却时间 -5%
    # 攻击速度 +8%
    # 施放速度 +5%
    # 物理暴击率 +2%
    # rarity: 稀有
    pass


@register
def equ_10(char: CharacterProperty):
    # DCALC_REMOVE: equ_10 - 独一无二太刀
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 +5% 冷却时间 -5%
    # 攻击速度 +8%
    # 施放速度 +5%
    # 物理暴击率 +2%
    # rarity: 神器
    pass


@register
def equ_11(char: CharacterProperty):
    # DCALC_REMOVE: equ_11 - 传说承继 - 太刀
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 +5% 冷却时间 -5%
    # 攻击速度 +8%
    # 施放速度 +5%
    # 物理暴击率 +2%
    # rarity: 传说
    pass


@register
def equ_12(char: CharacterProperty):
    # DCALC_REMOVE: equ_12 - 英雄叙事诗 - 太刀
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 +5% 冷却时间 -5%
    # 攻击速度 +8%
    # 施放速度 +5%
    # 物理暴击率 +2%
    # rarity: 史诗
    pass


@register
def equ_13(char: CharacterProperty):
    # DCALC_REMOVE: equ_13 - 太初之星 - 太刀
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 +5% 冷却时间 -5%
    # 攻击速度 +8%
    # 施放速度 +5%
    # 物理暴击率 +2%
    # rarity: 太初
    pass


@register
def equ_14(char: CharacterProperty):
    # DCALC_REMOVE: equ_14 - 凡作 - 金印刀
    # [寒光掠影][装备主动技能]
    # 同样的技能，凡作只能发出平凡的一击。
    # - 寒光掠影伤害量：113400%
    # - 冷却时间40秒
    # rarity: 传说
    char.equ_effect.append(EquEffect(name='寒光掠影', icon='/equipment/skill/4.png', cd=40, data=113400))
    pass


@register
def equ_15(char: CharacterProperty):
    # DCALC_REMOVE: equ_15 - 名作 - 金印锐刀
    # [寒光掠影][装备主动技能]
    # 蕴含锐利剑意的一击，难掩名作之风采。
    # - 寒光掠影伤害量：226800%
    # - 冷却时间40秒
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='寒光掠影', icon='/equipment/skill/4.png', cd=40, data=226800))
    pass


@register
def equ_16(char: CharacterProperty):
    # DCALC_REMOVE: equ_16 - 杰作 - 金印绝刀
    # [寒光掠影][装备主动技能]
    # 剑意三千境，一招足以制胜。
    # - 寒光掠影伤害量：340200%
    # - 冷却时间40秒
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='寒光掠影', icon='/equipment/skill/4.png', cd=40, data=340200))
    pass


@register
def equ_17(char: CharacterProperty):
    # DCALC_REMOVE: equ_17 - 百里挑一钝器
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5%
    # 命中率 +1%
    # rarity: 稀有
    pass


@register
def equ_18(char: CharacterProperty):
    # DCALC_REMOVE: equ_18 - 独一无二钝器
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5%
    # 命中率 +1%
    # rarity: 神器
    pass


@register
def equ_19(char: CharacterProperty):
    # DCALC_REMOVE: equ_19 - 传说承继 - 钝器
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5%
    # 命中率 +1%
    # rarity: 传说
    pass


@register
def equ_20(char: CharacterProperty):
    # DCALC_REMOVE: equ_20 - 英雄叙事诗 - 钝器
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5%
    # 命中率 +1%
    # rarity: 史诗
    pass


@register
def equ_21(char: CharacterProperty):
    # DCALC_REMOVE: equ_21 - 太初之星 - 钝器
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5%
    # 命中率 +1%
    # rarity: 太初
    pass


@register
def equ_22(char: CharacterProperty):
    # DCALC_REMOVE: equ_22 - 梁月的钝剑 : 形
    # 技能冷却时间20%减少（觉醒技能除外）
    # 所有速度 +10%
    # rarity: 传说
    char.SetSkillCD(1, 100, 0.2, [50, 85, 100])
    char.SetStatus(SpeedM=0.1, SpeedA=0.1, SpeedR=0.1)
    pass


@register
def equ_23(char: CharacterProperty):
    # DCALC_REMOVE: equ_23 - 梁月的钝剑 : 意
    # 技能冷却时间20%减少（觉醒技能除外）
    # 所有速度 +12.5%
    # [合一]
    # 基本攻击时， 生成可移动攻击的分身。（冷却时间7秒）
    # 使用技能时， 生成可移动攻击的分身。（冷却时间15秒）
    # 分身攻击命中时，技能冷却时间恢复速度 +3%，效果持续3秒。（觉醒技能除外；最多叠加1次）
    # rarity: 史诗
    char.SetSkillCD(1, 100, 0.2, [50, 85, 100])
    char.SetStatus(SpeedM=0.125, SpeedA=0.125, SpeedR=0.125)
    char.SetSkillCDRecover(1, 100, 0.03, [50, 85, 100])
    pass


@register
def equ_24(char: CharacterProperty):
    # DCALC_REMOVE: equ_24 - 梁月的钝剑 : 神
    # 技能冷却时间20%减少（觉醒技能除外）
    # 所有速度 +15%
    # [合一]
    # 基本攻击时， 生成可移动攻击的分身。（冷却时间3秒）
    # 使用技能时， 生成可移动攻击的分身。（冷却时间7秒）
    # 分身攻击命中时，技能冷却时间恢复速度 +3%，效果持续3秒。（觉醒技能除外；最多叠加1次）
    # rarity: 太初
    char.SetSkillCD(1, 100, 0.2, [50, 85, 100])
    char.SetStatus(SpeedM=0.15, SpeedA=0.15, SpeedR=0.15)
    char.SetSkillCDRecover(1, 100, 0.03, [50, 85, 100])
    pass


@register
def equ_25(char: CharacterProperty):
    # DCALC_REMOVE: equ_25 - 百里挑一巨剑
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # rarity: 稀有
    pass


@register
def equ_26(char: CharacterProperty):
    # DCALC_REMOVE: equ_26 - 独一无二巨剑
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # rarity: 神器
    pass


@register
def equ_27(char: CharacterProperty):
    # DCALC_REMOVE: equ_27 - 传说承继 - 巨剑
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # rarity: 传说
    pass


@register
def equ_28(char: CharacterProperty):
    # DCALC_REMOVE: equ_28 - 英雄叙事诗 - 巨剑
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # rarity: 史诗
    pass


@register
def equ_29(char: CharacterProperty):
    # DCALC_REMOVE: equ_29 - 太初之星 - 巨剑
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # rarity: 太初
    pass


@register
def equ_30(char: CharacterProperty):
    # DCALC_REMOVE: equ_30 - 第1型 - 攻式·行云剑
    # 命中率 +10%
    # [凌云武神之魂]
    # 穿戴时，凌云武神之魂保护自身。
    # - 所受物理/魔法伤害 -20%
    # [坚固防御][装备主动技能]
    # 凌云武神阻挡穿戴者15秒内所受的全部伤害。
    # - 获得最大生命值15%数值的保护罩
    # - 冷却时间：60秒
    # rarity: 传说
    pass


@register
def equ_31(char: CharacterProperty):
    # DCALC_REMOVE: equ_31 - 第2型 - 守式·停云剑
    # 命中率 +15%
    # [凌云武神之魂]
    # 穿戴时，凌云武神之魂保护自身。
    # - 所受物理/魔法伤害 -25%
    # 鬼剑士（男）
    # [格挡]技能等级 +3
    # 鬼剑士（女）
    # [招架]技能等级 +3
    # 守护者
    # [自动防御]技能等级 +3
    # [坚固防御][装备主动技能]
    # 凌云武神阻挡穿戴者20秒内所受的全部伤害。
    # - 获得最大生命值20%数值的保护罩
    # - 冷却时间：60秒
    # rarity: 史诗
    pass


@register
def equ_32(char: CharacterProperty):
    # DCALC_REMOVE: equ_32 - 特型 - 武神凌云剑
    # 命中率 +20%
    # [凌云武神之魂]
    # 穿戴时，凌云武神之魂保护自身。
    # - 所受物理/魔法伤害 -30%
    # 鬼剑士（男）
    # [格挡]技能等级 +5
    # 鬼剑士（女）
    # [招架]技能等级 +5
    # 守护者
    # [自动防御]技能等级 +5
    # [坚固防御][装备主动技能]
    # 凌云武神阻挡穿戴者30秒内所受的全部伤害。
    # - 获得最大生命值30%数值的保护罩
    # - 冷却时间：60秒
    # rarity: 太初
    pass


@register
def equ_33(char: CharacterProperty):
    # DCALC_REMOVE: equ_33 - 百里挑一光剑
    # 需要[光剑掌握]技能
    # 物理百分比技能
    # 魔法值 -10% 冷却时间 -10%
    # 攻击速度 +10%
    # rarity: 稀有
    pass


@register
def equ_34(char: CharacterProperty):
    # DCALC_REMOVE: equ_34 - 独一无二光剑
    # 需要[光剑掌握]技能
    # 物理百分比技能
    # 魔法值 -10% 冷却时间 -10%
    # 攻击速度 +10%
    # rarity: 神器
    pass


@register
def equ_35(char: CharacterProperty):
    # DCALC_REMOVE: equ_35 - 传说承继 - 光剑
    # 需要[光剑掌握]技能
    # 物理百分比技能
    # 魔法值 -10% 冷却时间 -10%
    # 攻击速度 +10%
    # rarity: 传说
    pass


@register
def equ_36(char: CharacterProperty):
    # DCALC_REMOVE: equ_36 - 英雄叙事诗 - 光剑
    # 需要[光剑掌握]技能
    # 物理百分比技能
    # 魔法值 -10% 冷却时间 -10%
    # 攻击速度 +10%
    # rarity: 史诗
    pass


@register
def equ_37(char: CharacterProperty):
    # DCALC_REMOVE: equ_37 - 太初之星 - 光剑
    # 需要[光剑掌握]技能
    # 物理百分比技能
    # 魔法值 -10% 冷却时间 -10%
    # 攻击速度 +10%
    # rarity: 太初
    pass


@register
def equ_38(char: CharacterProperty):
    # DCALC_REMOVE: equ_38 - 敌龙剑巴鲁姆克
    # 需要[光剑掌握]技能
    # [灭龙者]
    # 技能快捷栏中存在6个及以上空栏，发动[黑龙之力]效果。
    # - 所有速度 +10%
    # rarity: 传说
    char.SetStatus(SpeedM=0.1, SpeedA=0.1, SpeedR=0.1)
    pass


@register
def equ_39(char: CharacterProperty):
    # DCALC_REMOVE: equ_39 - 降龙剑巴鲁姆克
    # 需要[光剑掌握]技能
    # [灭龙者]
    # 技能快捷栏中存在4个及以上空栏，发动[黑龙之力]效果。
    # - 所受物理/魔法伤害 -5%
    # - 所有速度 +15%
    # rarity: 史诗
    char.SetStatus(SpeedM=0.15, SpeedA=0.15, SpeedR=0.15)
    pass


@register
def equ_40(char: CharacterProperty):
    # DCALC_REMOVE: equ_40 - 灭龙剑巴鲁姆克
    # 需要[光剑掌握]技能
    # [灭龙者]
    # 技能快捷栏中存在3个及以上空栏，发动[黑龙之力]效果。
    # - 进入霸体状态
    # - 所受物理/魔法伤害 -10%
    # - 所有速度 +20%
    # rarity: 太初
    char.SetStatus(SpeedM=0.2, SpeedA=0.2, SpeedR=0.2)
    pass


@register
def equ_41(char: CharacterProperty):
    # DCALC_REMOVE: equ_41 - 百里挑一手套
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 +15%
    # 攻击速度 +10%
    # 施放速度 +2%
    # rarity: 稀有
    pass


@register
def equ_42(char: CharacterProperty):
    # DCALC_REMOVE: equ_42 - 独一无二手套
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 +15%
    # 攻击速度 +10%
    # 施放速度 +2%
    # rarity: 神器
    pass


@register
def equ_43(char: CharacterProperty):
    # DCALC_REMOVE: equ_43 - 传说承继 - 手套
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 +15%
    # 攻击速度 +10%
    # 施放速度 +2%
    # rarity: 传说
    pass


@register
def equ_44(char: CharacterProperty):
    # DCALC_REMOVE: equ_44 - 英雄叙事诗 - 手套
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 +15%
    # 攻击速度 +10%
    # 施放速度 +2%
    # rarity: 史诗
    pass


@register
def equ_45(char: CharacterProperty):
    # DCALC_REMOVE: equ_45 - 太初之星 - 手套
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 +15%
    # 攻击速度 +10%
    # 施放速度 +2%
    # rarity: 太初
    pass


@register
def equ_46(char: CharacterProperty):
    # DCALC_REMOVE: equ_46 - 念气之星点
    # 技能冷却时间20%减少（觉醒技能除外）
    # 光属性攻击
    # 魔法防御力 +7000
    # 光属性抗性 +20
    # rarity: 传说
    char.SetSkillCD(cd=0.2)
    pass


@register
def equ_47(char: CharacterProperty):
    # DCALC_REMOVE: equ_47 - 念气之星群
    # 技能冷却时间20%减少（觉醒技能除外）
    # 光属性攻击
    # 魔法防御力 +7000
    # 光属性抗性 +20
    # 施放[念兽：龙虎啸]时，变更技能特效。
    # rarity: 史诗
    char.SetSkillCD(cd=0.2)
    pass


@register
def equ_48(char: CharacterProperty):
    # DCALC_REMOVE: equ_48 - 念气之星河
    # 技能冷却时间20%减少（觉醒技能除外）
    # 光属性攻击
    # 魔法防御力 +7000
    # 光属性抗性 +20
    # 施放[念兽：龙虎啸]时，变更技能特效。
    # 召唤念气星体。
    # rarity: 太初
    char.SetSkillCD(cd=0.2)
    pass


@register
def equ_49(char: CharacterProperty):
    # DCALC_REMOVE: equ_49 - 百里挑一臂铠
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # 命中率 +1%
    # rarity: 稀有
    pass


@register
def equ_50(char: CharacterProperty):
    # DCALC_REMOVE: equ_50 - 独一无二臂铠
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # 命中率 +1%
    # rarity: 神器
    pass


@register
def equ_51(char: CharacterProperty):
    # DCALC_REMOVE: equ_51 - 传说承继 - 臂铠
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # 命中率 +1%
    # rarity: 传说
    pass


@register
def equ_52(char: CharacterProperty):
    # DCALC_REMOVE: equ_52 - 英雄叙事诗 - 臂铠
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # 命中率 +1%
    # rarity: 史诗
    pass


@register
def equ_53(char: CharacterProperty):
    # DCALC_REMOVE: equ_53 - 太初之星 - 臂铠
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # 命中率 +1%
    # rarity: 太初
    pass


@register
def equ_54(char: CharacterProperty):
    # DCALC_REMOVE: equ_54 - 未完成的行星臂铠
    # 进入地下城时，生命值上限锁定为80%
    # 所受物理/魔法伤害 -25%
    # 生命值不足80%的情况下攻击时，恢复2%的生命值。（冷却时间30秒）
    # rarity: 传说
    pass


@register
def equ_55(char: CharacterProperty):
    # DCALC_REMOVE: equ_55 - 未完成的恒星臂铠
    # 进入地下城时，生命值上限锁定为80%
    # 所受物理/魔法伤害 -30%
    # 攻击敌人时，使敌人发生绯红爆炸。（冷却时间10秒）
    # [绯红爆炸]
    # - 对爆炸范围内的敌人造成72000%伤害
    # - 爆炸发生时，如果生命值不足80%，则恢复20%的生命值。（冷却时间30秒）
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='绯红爆炸', icon='/equipment/icon/weapon/fighter/gauntlet/00246.png', cd=10, data=72000))
    pass


@register
def equ_56(char: CharacterProperty):
    # DCALC_REMOVE: equ_56 - 未完成的宇宙臂铠
    # 进入地下城时，生命值上限锁定为80%
    # 所受物理/魔法伤害 -35%
    # 攻击敌人时，使敌人发生绯红爆炸。（冷却时间10秒）
    # [绯红爆炸]
    # - 对爆炸范围内的敌人造成72000%伤害
    # - 绯红爆炸范围 +50%
    # - 爆炸发生时，如果生命值不足80%，则恢复40%的生命值。（冷却时间30秒）
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='绯红爆炸', icon='/equipment/icon/weapon/fighter/gauntlet/00247.png', cd=10, data=72000))
    pass


@register
def equ_57(char: CharacterProperty):
    # DCALC_REMOVE: equ_57 - 百里挑一爪
    # 物理暴击率 +3%
    # rarity: 稀有
    pass


@register
def equ_58(char: CharacterProperty):
    # DCALC_REMOVE: equ_58 - 独一无二爪
    # 物理暴击率 +3%
    # rarity: 神器
    pass


@register
def equ_59(char: CharacterProperty):
    # DCALC_REMOVE: equ_59 - 传说承继 - 爪
    # 物理暴击率 +3%
    # rarity: 传说
    pass


@register
def equ_60(char: CharacterProperty):
    # DCALC_REMOVE: equ_60 - 英雄叙事诗 - 爪
    # 物理暴击率 +3%
    # rarity: 史诗
    pass


@register
def equ_61(char: CharacterProperty):
    # DCALC_REMOVE: equ_61 - 太初之星 - 爪
    # 物理暴击率 +3%
    # rarity: 太初
    pass


@register
def equ_62(char: CharacterProperty):
    # DCALC_REMOVE: equ_62 - 魔女的悲伤
    # 暗属性攻击
    # 所有速度 +10%
    # 暗属性抗性 +20
    # [悲伤魔珠][装备主动技能]
    # 生成蕴含沉痛悲伤的魔珠。
    # - 悲伤魔珠伤害量：15300%
    # - 冷却时间：30秒
    # rarity: 传说
    char.SetStatus(SpeedM=0.1, SpeedA=0.1, SpeedR=0.1)
    char.equ_effect.append(EquEffect(name='悲伤魔珠', icon='/equipment/skill/38.png', cd=30, data=15300))
    pass


@register
def equ_63(char: CharacterProperty):
    # DCALC_REMOVE: equ_63 - 魔女的恨意
    # 穿戴时，发动悲伤残影，并适用以下增益效果
    # 暗属性攻击
    # 所有速度 +20%
    # 暗属性抗性 +20
    # [悲伤魔珠][装备主动技能]
    # 生成蕴含沉痛悲伤的魔珠。
    # - 悲伤魔珠伤害量：15300%
    # - 冷却时间：15秒
    # rarity: 史诗
    char.SetStatus(SpeedM=0.2, SpeedA=0.2, SpeedR=0.2)
    char.equ_effect.append(EquEffect(name='悲伤魔珠', icon='/equipment/skill/38.png', cd=15, data=15300))
    pass


@register
def equ_64(char: CharacterProperty):
    # DCALC_REMOVE: equ_64 - 魔女的堕落
    # 穿戴时，发动悲伤残影，并适用以下增益效果
    # 暗属性攻击
    # 所有速度 +25%
    # 暗属性抗性 +20
    # [悲伤魔珠][装备主动技能]
    # 生成蕴含沉痛悲伤的魔珠。
    # - 悲伤魔珠伤害量：15300%
    # - 冷却时间：10秒
    # [彻骨之恨]
    # 身体被彻骨之恨包裹，减少所受伤害。
    # - 所受物理/魔法伤害 -10%
    # rarity: 太初
    char.SetStatus(SpeedM=0.25, SpeedA=0.25, SpeedR=0.25)
    char.equ_effect.append(EquEffect(name='悲伤魔珠', icon='/equipment/skill/38.png', cd=10, data=15300))
    pass


@register
def equ_65(char: CharacterProperty):
    # DCALC_REMOVE: equ_65 - 百里挑一拳套
    # 需要[拳套掌握]技能
    # 物理百分比技能
    # 魔法值 +5% 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 -5%
    # 攻击速度 +10%
    # rarity: 稀有
    pass


@register
def equ_66(char: CharacterProperty):
    # DCALC_REMOVE: equ_66 - 独一无二拳套
    # 需要[拳套掌握]技能
    # 物理百分比技能
    # 魔法值 +5% 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 -5%
    # 攻击速度 +10%
    # rarity: 神器
    pass


@register
def equ_67(char: CharacterProperty):
    # DCALC_REMOVE: equ_67 - 传说承继 - 拳套
    # 需要[拳套掌握]技能
    # 物理百分比技能
    # 魔法值 +5% 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 -5%
    # 攻击速度 +10%
    # rarity: 传说
    pass


@register
def equ_68(char: CharacterProperty):
    # DCALC_REMOVE: equ_68 - 英雄叙事诗 - 拳套
    # 需要[拳套掌握]技能
    # 物理百分比技能
    # 魔法值 +5% 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 -5%
    # 攻击速度 +10%
    # rarity: 史诗
    pass


@register
def equ_69(char: CharacterProperty):
    # DCALC_REMOVE: equ_69 - 太初之星 - 拳套
    # 需要[拳套掌握]技能
    # 物理百分比技能
    # 魔法值 +5% 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 -5%
    # 攻击速度 +10%
    # rarity: 太初
    pass


@register
def equ_70(char: CharacterProperty):
    # DCALC_REMOVE: equ_70 - 贝兹公爵的强力之拳
    # 需要[拳套掌握]技能
    # 技能范围 +20%
    # rarity: 传说
    pass


@register
def equ_71(char: CharacterProperty):
    # DCALC_REMOVE: equ_71 - 贝兹伯爵的英勇之拳
    # 需要[拳套掌握]技能
    # 技能范围 +25%
    # 攻击敌人时，对该敌人产生冲击波。（冷却时间0.2秒）
    # - 冲击波伤害量：2400%
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='冲击波', icon='/equipment/icon/weapon/fighter/bglove/00208.png', cd=0.2, data=2400))
    pass


@register
def equ_72(char: CharacterProperty):
    # DCALC_REMOVE: equ_72 - 贝兹女王的辉煌之拳
    # 需要[拳套掌握]技能
    # 技能范围 +30%
    # 攻击敌人时，对该敌人产生冲击波。（冷却时间0.2秒）
    # - 冲击波伤害量：2400%
    # - 冲击波范围 +50%
    # - 冲击波施放4次后，下次冲击波变为强化冲击波。
    # - 强化冲击波伤害量：4800%
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='冲击波', icon='/equipment/icon/weapon/fighter/bglove/00209.png', cd=0.2, data=2400))
    char.equ_effect.append(EquEffect(name='强化冲击波', icon='/equipment/icon/weapon/fighter/bglove/00209', cd=1, data=4800))
    pass


@register
def equ_73(char: CharacterProperty):
    # DCALC_REMOVE: equ_73 - 百里挑一东方棍
    # 物理百分比技能
    # 魔法值 -5%
    # 攻击速度 +5%
    # 回避率 +3%
    # 命中率 +2%
    # rarity: 稀有
    pass


@register
def equ_74(char: CharacterProperty):
    # DCALC_REMOVE: equ_74 - 独一无二东方棍
    # 物理百分比技能
    # 魔法值 -5%
    # 攻击速度 +5%
    # 回避率 +3%
    # 命中率 +2%
    # rarity: 神器
    pass


@register
def equ_75(char: CharacterProperty):
    # DCALC_REMOVE: equ_75 - 传说承继 - 东方棍
    # 物理百分比技能
    # 魔法值 -5%
    # 攻击速度 +5%
    # 回避率 +3%
    # 命中率 +2%
    # rarity: 传说
    pass


@register
def equ_76(char: CharacterProperty):
    # DCALC_REMOVE: equ_76 - 英雄叙事诗 - 东方棍
    # 物理百分比技能
    # 魔法值 -5%
    # 攻击速度 +5%
    # 回避率 +3%
    # 命中率 +2%
    # rarity: 史诗
    pass


@register
def equ_77(char: CharacterProperty):
    # DCALC_REMOVE: equ_77 - 太初之星 - 东方棍
    # 物理百分比技能
    # 魔法值 -5%
    # 攻击速度 +5%
    # 回避率 +3%
    # 命中率 +2%
    # rarity: 太初
    pass


@register
def equ_78(char: CharacterProperty):
    # DCALC_REMOVE: equ_78 - 魔力供给器
    # 所有速度 +10%
    # [魔力吸纳]
    # 吸收大气中的魔力，每10秒恢复3%魔法值。
    # rarity: 传说
    pass


@register
def equ_79(char: CharacterProperty):
    # DCALC_REMOVE: equ_79 - 魔力激活器
    # 所有速度 +10%
    # [魔力吸纳]
    # 吸收大气中的魔力，每10秒恢复3%魔法值。
    # [魔力觉察][装备主动技能]
    # 魔法值在50%以上时发动，进入魔力觉察状态。
    # - 所有速度 +10%
    # - 所受物理/魔法伤害 -10%
    # - 每秒魔法值 -1%
    # - 魔法值消耗量 +300%
    # - 魔法值为0或再次按键时，解除[魔力觉察]状态
    # rarity: 史诗
    char.SetStatus(SpeedA=0.2, SpeedM=0.2, SpeedR=0.2)
    pass


@register
def equ_80(char: CharacterProperty):
    # DCALC_REMOVE: equ_80 - 魔力先觉者
    # 所有速度 +10%
    # [魔力吸纳]
    # 吸收大气中的魔力，每10秒恢复3%魔法值。
    # [魔力觉察][装备主动技能]
    # 魔法值在30%以上时发动，进入魔力觉察状态。
    # - 所有速度 +20%
    # - 所受物理/魔法伤害 -20%
    # - 每秒魔法值 -1%
    # - 魔法值消耗量 +200%
    # - 魔法值为0或再次按键时，解除[魔力觉察]状态
    # rarity: 太初
    char.SetStatus(SpeedA=0.3, SpeedM=0.3, SpeedR=0.3)
    pass


@register
def equ_81(char: CharacterProperty):
    # DCALC_REMOVE: equ_81 - 百里挑一左轮枪
    # 物理百分比技能
    # 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 物理暴击率 +2%
    # rarity: 稀有
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(cd=0.2)
    pass


@register
def equ_82(char: CharacterProperty):
    # DCALC_REMOVE: equ_82 - 独一无二左轮枪
    # 物理百分比技能
    # 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 物理暴击率 +2%
    # rarity: 神器
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(cd=0.2)
    pass


@register
def equ_83(char: CharacterProperty):
    # DCALC_REMOVE: equ_83 - 传说承继 - 左轮枪
    # 物理百分比技能
    # 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 物理暴击率 +2%
    # rarity: 传说
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(cd=0.2)
    pass


@register
def equ_84(char: CharacterProperty):
    # DCALC_REMOVE: equ_84 - 英雄叙事诗 - 左轮枪
    # 物理百分比技能
    # 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 物理暴击率 +2%
    # rarity: 史诗
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(cd=0.2)
    pass


@register
def equ_85(char: CharacterProperty):
    # DCALC_REMOVE: equ_85 - 太初之星 - 左轮枪
    # 物理百分比技能
    # 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 物理暴击率 +2%
    # rarity: 太初
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(cd=0.2)
    pass


@register
def equ_86(char: CharacterProperty):
    # DCALC_REMOVE: equ_86 - 漫游枪手的道路
    # [道路独行者]
    # 技能快捷栏中存在6个及以上空栏时，发动[漫游枪手的资格]效果。
    # - 所有速度 +10%
    # - 发动权威光谱效果
    # rarity: 传说
    char.SetStatus(SpeedA=0.1, SpeedM=0.1, SpeedR=0.1)
    pass


@register
def equ_87(char: CharacterProperty):
    # DCALC_REMOVE: equ_87 - 漫游枪手的宿命
    # [子弹的宿命]
    # 技能快捷栏中存在4个及以上空栏时，发动[漫游枪手的资格]效果。
    # - 所受物理/魔法伤害 -5%
    # - 所有速度 +15%
    # - 发动权威光谱效果
    # rarity: 史诗
    char.SetStatus(SpeedA=0.15, SpeedM=0.15, SpeedR=0.15)
    pass


@register
def equ_88(char: CharacterProperty):
    # DCALC_REMOVE: equ_88 - 漫游枪手的威权
    # [帝王的眼界]
    # 技能快捷栏中存在3个及以上空栏时，发动[漫游枪手的资格]效果。
    # - 进入霸体状态
    # - 所受物理/魔法伤害 -10%
    # - 所有速度 +20%
    # - 发动权威光谱效果
    # rarity: 太初
    char.SetStatus(SpeedA=0.2, SpeedM=0.2, SpeedR=0.2)
    pass


@register
def equ_89(char: CharacterProperty):
    # DCALC_REMOVE: equ_89 - 百里挑一手弩
    # 物理百分比技能
    # 魔法值 -10% 冷却时间 -10%
    # 攻击速度 +2%
    # 物理暴击率 +3%
    # 命中率 +1%
    # rarity: 稀有
    pass


@register
def equ_90(char: CharacterProperty):
    # DCALC_REMOVE: equ_90 - 独一无二手弩
    # 物理百分比技能
    # 魔法值 -10% 冷却时间 -10%
    # 攻击速度 +2%
    # 物理暴击率 +3%
    # 命中率 +1%
    # rarity: 神器
    pass


@register
def equ_91(char: CharacterProperty):
    # DCALC_REMOVE: equ_91 - 传说承继 - 手弩
    # 物理百分比技能
    # 魔法值 -10% 冷却时间 -10%
    # 攻击速度 +2%
    # 物理暴击率 +3%
    # 命中率 +1%
    # rarity: 传说
    pass


@register
def equ_92(char: CharacterProperty):
    # DCALC_REMOVE: equ_92 - 英雄叙事诗 - 手弩
    # 物理百分比技能
    # 魔法值 -10% 冷却时间 -10%
    # 攻击速度 +2%
    # 物理暴击率 +3%
    # 命中率 +1%
    # rarity: 史诗
    pass


@register
def equ_93(char: CharacterProperty):
    # DCALC_REMOVE: equ_93 - 太初之星 - 手弩
    # 物理百分比技能
    # 魔法值 -10% 冷却时间 -10%
    # 攻击速度 +2%
    # 物理暴击率 +3%
    # 命中率 +1%
    # rarity: 太初
    pass


@register
def equ_94(char: CharacterProperty):
    # DCALC_REMOVE: equ_94 - 冰封的火焰之躯
    # 攻击时放置冰弩，持续30秒。（冷却时间30秒）
    # - 每次攻击伤害量：7200%
    # - 冰弩攻击敌人时，使敌人进入冰冻状态，效果持续5秒。
    # [模式切换][装备主动技能]
    # 切换所有弩箭的模式。
    # - 射击模式：攻击敌人
    # - 静止模式：中止攻击
    # - 冷却时间1秒
    # rarity: 传说
    char.equ_effect.append(EquEffect(name='冰封的火焰之躯', icon='/equipment/skill/26.png', cd=1, data=7200))
    pass


@register
def equ_95(char: CharacterProperty):
    # DCALC_REMOVE: equ_95 - 燃烧的霜冻之躯
    # 攻击时放置冰弩，持续30秒。（冷却时间30秒）
    # - 每次攻击伤害量：7200%
    # - 冰弩攻击敌人时，使敌人进入冰冻状态，效果持续5秒。
    # 攻击时放置火弩，持续30秒。（冷却时间30秒）
    # - 每次攻击伤害量：7200%
    # [模式切换][装备主动技能]
    # 切换所有弩箭的模式。
    # - 射击模式：攻击敌人
    # - 静止模式：中止攻击
    # - 冷却时间1秒
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='冰弩', icon='/equipment/skill/26.png', cd=1, data=7200))
    char.equ_effect.append(EquEffect(name='火弩', icon='/equipment/skill/26.png', cd=1, data=7200))
    pass


@register
def equ_96(char: CharacterProperty):
    # DCALC_REMOVE: equ_96 - 冰火的淬炼之躯
    # 攻击时放置冰弩，持续30秒。（冷却时间30秒）
    # - 每次攻击伤害量：7200%
    # - 冰弩攻击敌人时，使敌人进入冰冻状态，效果持续5秒。
    # 攻击时放置火弩，持续30秒。（冷却时间30秒）
    # - 每次攻击伤害量：7200%
    # 攻击时，对敌人降下箭雨。（冷却时间20秒）
    # - 箭雨伤害量：45600%
    # [模式切换][装备主动技能]
    # 切换所有弩箭的模式。
    # - 射击模式：攻击敌人
    # - 静止模式：中止攻击
    # - 冷却时间1秒
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='冰弩', icon='/equipment/skill/26.png', cd=1, data=7200))
    char.equ_effect.append(EquEffect(name='火弩', icon='/equipment/skill/26.png', cd=1, data=7200))
    char.equ_effect.append(EquEffect(name='箭雨', icon='/equipment/skill/26.png', cd=20, data=45600))
    pass


@register
def equ_97(char: CharacterProperty):
    # DCALC_REMOVE: equ_97 - 百里挑一步枪
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5%
    # rarity: 稀有
    pass


@register
def equ_98(char: CharacterProperty):
    # DCALC_REMOVE: equ_98 - 独一无二步枪
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5%
    # rarity: 神器
    pass


@register
def equ_99(char: CharacterProperty):
    # DCALC_REMOVE: equ_99 - 传说承继 - 步枪
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5%
    # rarity: 传说
    pass


@register
def equ_100(char: CharacterProperty):
    # DCALC_REMOVE: equ_100 - 英雄叙事诗 - 步枪
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5%
    # rarity: 史诗
    pass


@register
def equ_101(char: CharacterProperty):
    # DCALC_REMOVE: equ_101 - 太初之星 - 步枪
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5%
    # rarity: 太初
    pass


@register
def equ_102(char: CharacterProperty):
    # DCALC_REMOVE: equ_102 - 归来之火花狙击者
    # 火属性攻击
    # 45级技能攻击力 +15%
    # [火花]
    # 进入地下城时，使自身燃烧。
    # - 消耗无色小晶块的技能攻击力 +25%
    # rarity: 传说
    for skill in char.skills:
        if skill.learnLv == 45 and skill.damage:
            skill.skillRation *= 1.15
        if skill.damage and skill.cube > 0:
            skill.skillDamage *= 1.25
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(cd=0.2)
    pass


@register
def equ_103(char: CharacterProperty):
    # DCALC_REMOVE: equ_103 - 归来之烈焰狙击者
    # 火属性攻击
    # 45级技能攻击力 +15%
    # [火花]
    # 进入地下城时，使自身燃烧。
    # - 消耗无色小晶块的技能攻击力 +25%
    # - 不消耗无色小晶块的技能攻击力 +10%
    # rarity: 史诗
    for skill in char.skills:
        if skill.learnLv == 45 and skill.damage:
            skill.skillRation *= 1.15
        if skill.damage and skill.cube > 0:
            skill.skillDamage *= 1.25
        if skill.damage and skill.cube == 0:
            skill.skillDamage *= 1.10
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(cd=0.2)
    pass


@register
def equ_104(char: CharacterProperty):
    # DCALC_REMOVE: equ_104 - 归来之黑玫瑰狙击者
    # 火属性攻击
    # 45级技能攻击力 +15%
    # [火花]
    # 进入地下城时，使自身燃烧。
    # - 消耗无色小晶块的技能攻击力 +30%
    # - 不消耗无色小晶块的技能攻击力 +25%
    # - 攻击时，燃烧敌人并造成伤害（冷却时间0.2秒）
    # *燃烧伤害量：480%
    # rarity: 太初
    for skill in char.skills:
        if skill.learnLv == 45 and skill.damage:
            skill.skillRation *= 1.15
        if skill.damage and skill.cube > 0:
            skill.skillDamage *= 1.30
        if skill.damage and skill.cube == 0:
            skill.skillDamage *= 1.25
    char.equ_effect.append(EquEffect(name='燃烧', icon='/equipment/icon/weapon/gunner/musket/00234.png', cd=0.2, data=480))
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(cd=0.2)
    pass


@register
def equ_105(char: CharacterProperty):
    # DCALC_REMOVE: equ_105 - 百里挑一自动手枪
    # 物理百分比技能
    # 魔法值 -30% 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 +10%
    # rarity: 稀有
    pass


@register
def equ_106(char: CharacterProperty):
    # DCALC_REMOVE: equ_106 - 独一无二自动手枪
    # 物理百分比技能
    # 魔法值 -30% 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 +10%
    # rarity: 神器
    pass


@register
def equ_107(char: CharacterProperty):
    # DCALC_REMOVE: equ_107 - 传说承继 - 自动手枪
    # 物理百分比技能
    # 魔法值 -30% 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 +10%
    # rarity: 传说
    pass


@register
def equ_108(char: CharacterProperty):
    # DCALC_REMOVE: equ_108 - 英雄叙事诗 - 自动手枪
    # 物理百分比技能
    # 魔法值 -30% 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 +10%
    # rarity: 史诗
    pass


@register
def equ_109(char: CharacterProperty):
    # DCALC_REMOVE: equ_109 - 太初之星 - 自动手枪
    # 物理百分比技能
    # 魔法值 -30% 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 +10%
    # rarity: 太初
    pass


@register
def equ_110(char: CharacterProperty):
    # DCALC_REMOVE: equ_110 - 创新式自动手枪
    # [斗志机器人]
    # 进入地下城时，斗志机器人跟随角色并提供增益。
    # - 技能冷却时间 -20%（觉醒技能除外）
    # rarity: 传说
    char.SetSkillCD(1, 100, 0.2)
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetStatus(SkillAttack=0.123)
    pass


@register
def equ_111(char: CharacterProperty):
    # DCALC_REMOVE: equ_111 - 变革式自动手枪
    # [斗志机器人]
    # 进入地下城时，斗志机器人跟随角色并提供增益。
    # - 技能冷却时间 -20%（觉醒技能除外）
    # [自动爆炸]
    # 每10秒自动对敌人引发爆炸。
    # - 自动爆炸总伤害量：47647%
    # [自动爆炸开关][装备主动技能]
    # 关闭自动爆炸，再次使用时开启。（冷却10秒）
    # rarity: 史诗
    char.SetSkillCD(1, 100, 0.2)
    char.equ_effect.append(EquEffect(name='自动爆炸', icon='/equipment/skill/33.png', cd=10, data=47647))
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetStatus(SkillAttack=0.123)
    pass


@register
def equ_112(char: CharacterProperty):
    # DCALC_REMOVE: equ_112 - 进化式自动手枪
    # [斗志机器人]
    # 进入地下城时，斗志机器人跟随角色并提供增益。
    # - 技能冷却时间 -20%（觉醒技能除外）
    # [自动爆炸]
    # 每10秒自动对敌人引发爆炸。
    # - 自动爆炸总伤害量：95294%
    # [自动爆炸开关][装备主动技能]
    # 关闭自动爆炸，再次使用时开启。（冷却10秒）
    # rarity: 太初
    char.SetSkillCD(1, 100, 0.2)
    char.equ_effect.append(EquEffect(name='自动爆炸', icon='/equipment/skill/33.png', cd=10, data=95294))
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetStatus(SkillAttack=0.123)
    pass


@register
def equ_113(char: CharacterProperty):
    # DCALC_REMOVE: equ_113 - 百里挑一手炮
    # 物理百分比技能
    # 魔法值 +25% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -25%
    # rarity: 稀有
    pass


@register
def equ_114(char: CharacterProperty):
    # DCALC_REMOVE: equ_114 - 独一无二手炮
    # 物理百分比技能
    # 魔法值 +25% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -25%
    # rarity: 神器
    pass


@register
def equ_115(char: CharacterProperty):
    # DCALC_REMOVE: equ_115 - 传说承继 - 手炮
    # 物理百分比技能
    # 魔法值 +25% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -25%
    # rarity: 传说
    pass


@register
def equ_116(char: CharacterProperty):
    # DCALC_REMOVE: equ_116 - 英雄叙事诗 - 手炮
    # 物理百分比技能
    # 魔法值 +25% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -25%
    # rarity: 史诗
    pass


@register
def equ_117(char: CharacterProperty):
    # DCALC_REMOVE: equ_117 - 太初之星 - 手炮
    # 物理百分比技能
    # 魔法值 +25% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -25%
    # rarity: 太初
    pass


@register
def equ_118(char: CharacterProperty):
    # DCALC_REMOVE: equ_118 - 少年乌尔班的创意
    # 技能范围 +20%
    # [发射巨炮][装备主动技能]
    # - 巨炮伤害量：113400%
    # - 冷却时间：40秒
    # rarity: 传说
    char.equ_effect.append(EquEffect(name='发射巨炮', icon='/equipment/skill/41.png', cd=40, data=113400))
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(cd=0.2)
    pass


@register
def equ_119(char: CharacterProperty):
    # DCALC_REMOVE: equ_119 - 乌尔班巨炮雏形
    # 技能范围 +25%
    # [发射巨炮][装备主动技能]
    # 发射高效改良巨炮。
    # - 巨炮伤害量：226800%
    # - 冷却时间：40秒
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='发射巨炮', icon='/equipment/skill/41.png', cd=40, data=226800))
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(cd=0.2)
    pass


@register
def equ_120(char: CharacterProperty):
    # DCALC_REMOVE: equ_120 - 乌尔班毕生杰作
    # 技能范围 +30%
    # [发射巨炮][装备主动技能]
    # 发射乌尔班的杰作巨炮。
    # - 巨炮伤害量：340200%
    # - 冷却时间：40秒
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='发射巨炮', icon='/equipment/skill/41.png', cd=40, data=340200))
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(cd=0.2)
    pass


@register
def equ_121(char: CharacterProperty):
    # DCALC_REMOVE: equ_121 - 百里挑一法杖
    # 魔法百分比技能
    # 魔法值 +10% 冷却时间 +5%
    # 攻击速度 -10%
    # rarity: 稀有
    pass


@register
def equ_122(char: CharacterProperty):
    # DCALC_REMOVE: equ_122 - 独一无二法杖
    # 魔法百分比技能
    # 魔法值 +10% 冷却时间 +5%
    # 攻击速度 -10%
    # rarity: 神器
    pass


@register
def equ_123(char: CharacterProperty):
    # DCALC_REMOVE: equ_123 - 传说承继 - 法杖
    # 魔法百分比技能
    # 魔法值 +10% 冷却时间 +5%
    # 攻击速度 -10%
    # rarity: 传说
    pass


@register
def equ_124(char: CharacterProperty):
    # DCALC_REMOVE: equ_124 - 英雄叙事诗 - 法杖
    # 魔法百分比技能
    # 魔法值 +10% 冷却时间 +5%
    # 攻击速度 -10%
    # rarity: 史诗
    pass


@register
def equ_125(char: CharacterProperty):
    # DCALC_REMOVE: equ_125 - 太初之星 - 法杖
    # 魔法百分比技能
    # 魔法值 +10% 冷却时间 +5%
    # 攻击速度 -10%
    # rarity: 太初
    pass


@register
def equ_126(char: CharacterProperty):
    # DCALC_REMOVE: equ_126 - 尘封的知识
    # 每存在1个冷却中的技能，技能冷却时间恢复速度 +6%（最多叠加5次，觉醒技能除外）
    # - 最大叠加时，技能范围 +10%
    # rarity: 传说
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetStatus(SkillAttack=0.123)
    char.SetSkillCDRecover(cd=0.06 * 5)
    pass


@register
def equ_127(char: CharacterProperty):
    # DCALC_REMOVE: equ_127 - 禁忌的知识
    # 每存在1个冷却中的技能，技能冷却时间恢复速度 +6%（最多叠加5次，觉醒技能除外）
    # - 最大叠加时，技能范围 +12%
    # rarity: 史诗
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetStatus(SkillAttack=0.123)
    char.SetSkillCDRecover(cd=0.06 * 5)
    pass


@register
def equ_128(char: CharacterProperty):
    # DCALC_REMOVE: equ_128 - 解禁的知识
    # 每存在1个冷却中的技能，技能冷却时间恢复速度 +6%（最多叠加5次，觉醒技能除外）
    # - 最大叠加时，技能范围 +15%
    # rarity: 太初
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetStatus(SkillAttack=0.123)
    char.SetSkillCDRecover(cd=0.06 * 5)
    pass


@register
def equ_129(char: CharacterProperty):
    # DCALC_REMOVE: equ_129 - 百里挑一法杖
    # 魔法百分比技能
    # 魔法值 +10% 冷却时间 +5%
    # 攻击速度 -10%
    # rarity: 稀有
    pass


@register
def equ_130(char: CharacterProperty):
    # DCALC_REMOVE: equ_130 - 独一无二法杖
    # 魔法百分比技能
    # 魔法值 +10% 冷却时间 +5%
    # 攻击速度 -10%
    # rarity: 神器
    pass


@register
def equ_131(char: CharacterProperty):
    # DCALC_REMOVE: equ_131 - 传说承继 - 法杖
    # 魔法百分比技能
    # 魔法值 +10% 冷却时间 +5%
    # 攻击速度 -10%
    # rarity: 传说
    pass


@register
def equ_132(char: CharacterProperty):
    # DCALC_REMOVE: equ_132 - 英雄叙事诗 - 法杖
    # 魔法百分比技能
    # 魔法值 +10% 冷却时间 +5%
    # 攻击速度 -10%
    # rarity: 史诗
    pass


@register
def equ_133(char: CharacterProperty):
    # DCALC_REMOVE: equ_133 - 太初之星 - 魔杖
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 攻击速度 +10%
    # 施放速度 +5%
    # rarity: 太初
    pass


@register
def equ_134(char: CharacterProperty):
    # DCALC_REMOVE: equ_134 - 牧羊人的第一道谎言
    # [羊群]
    # 施放技能时， 生成3只羊。
    # - 最多4只
    # 攻击时，消耗1只羊，施放羊袭。（冷却时间0.5秒）
    # - 羊袭伤害量：3600%
    # 被击时，消耗1只羊， 生成最大生命值10%数值的保护罩，效果持续2秒。（冷却时间2秒）
    # rarity: 传说
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    char.equ_effect.append(EquEffect(name='羊袭', icon='/equipment/icon/weapon/mage/rod/00282.png', cd=0.5, data=3600))
    pass


@register
def equ_135(char: CharacterProperty):
    # DCALC_REMOVE: equ_135 - 牧羊人的第二道谎言
    # [羊群]
    # 施放技能时， 生成5只羊。
    # - 每1只羊可使所受物理/魔法伤害 -2%
    # - 最多6只
    # 攻击时，消耗1只羊，施放羊袭。（冷却时间0.5秒）
    # - 羊袭伤害量：6000%
    # 被击时，消耗1只羊， 生成最大生命值15%数值的保护罩，效果持续2秒。（冷却时间2秒）
    # rarity: 史诗
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    char.equ_effect.append(EquEffect(name='羊袭', icon='/equipment/icon/weapon/mage/rod/00283.png', cd=0.5, data=6000))
    pass


@register
def equ_136(char: CharacterProperty):
    # DCALC_REMOVE: equ_136 - 牧羊人最后的谎言
    # [羊群]
    # 施放技能时， 生成6只羊。
    # - 每1只羊可使所受物理/魔法伤害 -2%
    # - 最多9只
    # 攻击时，消耗1只羊，施放绵羊云。（冷却时间2秒）
    # - 羊袭伤害量：33600%
    # 被击时，消耗1只羊， 生成最大生命值20%数值的保护罩，效果持续2秒。（冷却时间2秒）
    # rarity: 太初
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    char.equ_effect.append(EquEffect(name='绵羊云', icon='/equipment/icon/weapon/mage/rod/00284.png', cd=2, data=33600))
    pass


@register
def equ_137(char: CharacterProperty):
    # DCALC_REMOVE: equ_137 - 百里挑一棍棒
    # 物理百分比技能
    # 冷却时间 -5%
    # 攻击速度 +5%
    # 命中率 +1%
    # rarity: 稀有
    pass


@register
def equ_138(char: CharacterProperty):
    # DCALC_REMOVE: equ_138 - 独一无二棍棒
    # 物理百分比技能
    # 冷却时间 -5%
    # 攻击速度 +5%
    # 命中率 +1%
    # rarity: 神器
    pass


@register
def equ_139(char: CharacterProperty):
    # DCALC_REMOVE: equ_139 - 传说承继 - 棍棒
    # 物理百分比技能
    # 冷却时间 -5%
    # 攻击速度 +5%
    # 命中率 +1%
    # rarity: 传说
    pass


@register
def equ_140(char: CharacterProperty):
    # DCALC_REMOVE: equ_140 - 英雄叙事诗 - 棍棒
    # 物理百分比技能
    # 冷却时间 -5%
    # 攻击速度 +5%
    # 命中率 +1%
    # rarity: 史诗
    pass


@register
def equ_141(char: CharacterProperty):
    # DCALC_REMOVE: equ_141 - 太初之星 - 棍棒
    # 物理百分比技能
    # 冷却时间 -5%
    # 攻击速度 +5%
    # 命中率 +1%
    # rarity: 太初
    pass


@register
def equ_142(char: CharacterProperty):
    # DCALC_REMOVE: equ_142 - 时来运转 : 莫强求
    # 进入地下城时，获得1个幸运硬币。
    # 每20秒获得1个幸运硬币。（最多叠加10次）
    # [投掷硬币][装备主动技能]
    # - 消耗1个幸运硬币，按照指定的几率发动以下两种效果中的一种，效果持续30秒。（冷却时间3秒）
    # - 快乐（50%）
    # *所有速度 +30%
    # *生命值/魔法值恢复10%
    # - 悲伤（50%）
    # *所有速度 +10%
    # （快乐、悲伤的所有速度效果仅适用于最高值）
    # rarity: 传说
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    char.SetStatus(SpeedA=0.3, SpeedM=0.3, SpeedR=0.3)


@register
def equ_143(char: CharacterProperty):
    # DCALC_REMOVE: equ_143 - 卡匹迪恩 : 莫追悔
    # 进入地下城时，获得1个幸运硬币。
    # 每20秒获得1个幸运硬币。（最多叠加10次）
    # [投掷硬币][装备主动技能]
    # - 消耗1个幸运硬币，按照指定的几率发动以下两种效果中的一种，效果持续30秒。（冷却时间3秒）
    # - 快乐（70%）
    # *所有速度 +30%
    # *生命值/魔法值恢复10%
    # - 悲伤（30%）
    # *所有速度 +10%
    # （快乐、悲伤的所有速度效果仅适用于最高值）
    # rarity: 史诗
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    char.SetStatus(SpeedA=0.3, SpeedM=0.3, SpeedR=0.3)
    pass


@register
def equ_144(char: CharacterProperty):
    # DCALC_REMOVE: equ_144 - 哈库纳玛塔塔 : 莫烦忧
    # 进入地下城时，获得1个幸运硬币。
    # 每10秒获得1个硬币。（最多叠加10次）
    # [投掷硬币][装备主动技能]
    # - 消耗1个硬币，按照指定的几率发动以下两种效果中的一种，效果持续30秒。（冷却时间3秒）
    # - 心情好到炸裂（70%）
    # *所有速度 +30%
    # 生命值/魔法值恢复20%
    # *效果发动时，生产攻击附近敌人的闪电
    # -闪电伤害量：14400%
    # - 快乐（30%）
    # *所有速度 +30%
    # *生命值/魔法值恢复10%
    # （快乐、悲伤的所有速度效果仅适用于最高值）
    # rarity: 太初
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    char.SetStatus(SpeedA=0.3, SpeedM=0.3, SpeedR=0.3)
    char.equ_effect.append(EquEffect(name='闪电', icon='/equipment/skill/35.png', cd=3, data=14400))
    pass


@register
def equ_145(char: CharacterProperty):
    # DCALC_REMOVE: equ_145 - 百里挑一矛
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 攻击速度 -5%
    # 物理暴击率 +2%
    # 命中率 +1%
    # rarity: 稀有
    pass


@register
def equ_146(char: CharacterProperty):
    # DCALC_REMOVE: equ_146 - 独一无二矛
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 攻击速度 -5%
    # 物理暴击率 +2%
    # 命中率 +1%
    # rarity: 神器
    pass


@register
def equ_147(char: CharacterProperty):
    # DCALC_REMOVE: equ_147 - 传说承继 - 矛
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 攻击速度 -5%
    # 物理暴击率 +2%
    # 命中率 +1%
    # rarity: 传说
    pass


@register
def equ_148(char: CharacterProperty):
    # DCALC_REMOVE: equ_148 - 英雄叙事诗 - 矛
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 攻击速度 -5%
    # 物理暴击率 +2%
    # 命中率 +1%
    # rarity: 史诗
    pass


@register
def equ_149(char: CharacterProperty):
    # DCALC_REMOVE: equ_149 - 太初之星 - 矛
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 攻击速度 -5%
    # 物理暴击率 +2%
    # 命中率 +1%
    # rarity: 太初
    pass


@register
def equ_150(char: CharacterProperty):
    # DCALC_REMOVE: equ_150 - 终结者
    # [绝对零度][装备主动技能]
    # 挥舞冰霜之矛进行攻击。
    # - 绝对零度伤害量：113400%
    # - 冷却时间40秒
    # rarity: 传说
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    char.equ_effect.append(EquEffect(name='绝对零度', icon='/equipment/skill/31.png', cd=40, data=113400))
    pass


@register
def equ_151(char: CharacterProperty):
    # DCALC_REMOVE: equ_151 - 凛冬终结者
    # [绝对零度][装备主动技能]
    # 挥舞寒意刺骨的冰冻之矛进行攻击。
    # - 绝对零度伤害量：226800%
    # - 冷却时间40秒
    # rarity: 史诗
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    char.equ_effect.append(EquEffect(name='绝对零度', icon='/equipment/skill/31.png', cd=40, data=226800))
    pass


@register
def equ_152(char: CharacterProperty):
    # DCALC_REMOVE: equ_152 - 绝对零度终结者
    # [绝对零度][装备主动技能]
    # 挥洒冰封万物的凛冽寒气歼灭攻击。
    # - 绝对零度伤害量：340200%
    # - 冷却时间40秒
    # rarity: 太初
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    char.equ_effect.append(EquEffect(name='绝对零度', icon='/equipment/skill/31.png', cd=40, data=340200))
    pass


@register
def equ_153(char: CharacterProperty):
    # DCALC_REMOVE: equ_153 - 百里挑一扫把
    # 需要[扫把掌握]技能
    # 攻击速度 +6%
    # 移动速度 +3%
    # rarity: 稀有
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
    pass


@register
def equ_154(char: CharacterProperty):
    # DCALC_REMOVE: equ_154 - 独一无二扫把
    # 需要[扫把掌握]技能
    # 攻击速度 +6%
    # 移动速度 +3%
    # rarity: 神器
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_155(char: CharacterProperty):
    # DCALC_REMOVE: equ_155 - 传说承继 - 扫把
    # 需要[扫把掌握]技能
    # 攻击速度 +6%
    # 移动速度 +3%
    # rarity: 传说
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_156(char: CharacterProperty):
    # DCALC_REMOVE: equ_156 - 英雄叙事诗 - 扫把
    # 需要[扫把掌握]技能
    # 攻击速度 +6%
    # 移动速度 +3%
    # rarity: 史诗
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_157(char: CharacterProperty):
    # DCALC_REMOVE: equ_157 - 太初之星 - 扫把
    # 需要[扫把掌握]技能
    # 攻击速度 +6%
    # 移动速度 +3%
    # rarity: 太初
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_158(char: CharacterProperty):
    # DCALC_REMOVE: equ_158 - 暗黑祈祷
    # 需要[扫把掌握]技能
    # 暗属性攻击
    # 进入地下城时，生成暗黑花园，发动以下效果。
    # - 每秒魔法值减少0.5%
    # - 攻击时魔法值恢复0.8%（冷却时间1秒）
    # 技能范围 +20%
    # rarity: 传说
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_159(char: CharacterProperty):
    # DCALC_REMOVE: equ_159 - 暗黑祈愿
    # 需要[扫把掌握]技能
    # 暗属性攻击
    # 进入地下城时，生成暗黑花园，发动以下效果。
    # - 每秒魔法值减少1%
    # - 攻击时魔法值恢复1.5%（冷却时间1秒）
    # 技能范围 +25%
    # rarity: 史诗
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_160(char: CharacterProperty):
    # DCALC_REMOVE: equ_160 - 暗黑诅咒
    # 需要[扫把掌握]技能
    # 暗属性攻击
    # 进入地下城时，生成暗黑花园，发动以下效果。
    # - 每秒魔法值减少1%
    # - 攻击时魔法值恢复2%（冷却时间1秒）
    # 技能范围 +30%
    # rarity: 太初
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_161(char: CharacterProperty):
    # DCALC_REMOVE: equ_161 - 百里挑一光杖
    # 魔法百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 施放速度 +2%
    # rarity: 稀有
    pass
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4


@register
def equ_162(char: CharacterProperty):
    # DCALC_REMOVE: equ_162 - 独一无二光杖
    # 魔法百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 施放速度 +2%
    # rarity: 神器
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_163(char: CharacterProperty):
    # DCALC_REMOVE: equ_163 - 传说承继 - 光杖
    # 魔法百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 施放速度 +2%
    # rarity: 传说
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_164(char: CharacterProperty):
    # DCALC_REMOVE: equ_164 - 英雄叙事诗 - 光杖
    # 魔法百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 施放速度 +2%
    # rarity: 史诗
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_165(char: CharacterProperty):
    # DCALC_REMOVE: equ_165 - 太初之星 - 光杖
    # 魔法百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 施放速度 +2%
    # rarity: 太初
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_166(char: CharacterProperty):
    # DCALC_REMOVE: equ_166 - 荣耀之神木光杖
    # 获得最大生命值10%数值的[填充型保护罩]。
    # [神之惩罚][装备主动技能]
    # - 在前方生成1道落雷
    # - 落雷伤害量：30600%
    # - 冷却时间：30秒
    # rarity: 传说
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_167(char: CharacterProperty):
    # DCALC_REMOVE: equ_167 - 救赎之神木光杖
    # 获得最大生命值15%数值的[填充型保护罩]。
    # [神之惩罚][装备主动技能]
    # - 在前方生成2道落雷
    # - 落雷伤害量：30600%
    # - 冷却时间：30秒
    # rarity: 史诗
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_168(char: CharacterProperty):
    # DCALC_REMOVE: equ_168 - 永恒之神木光杖
    # 获得最大生命值20%数值的[填充型保护罩]。
    # [神之惩罚][装备主动技能]
    # - 在前方生成3道落雷
    # - 落雷伤害量：30600%
    # - 冷却时间：30秒
    # rarity: 太初
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_169(char: CharacterProperty):
    # DCALC_REMOVE: equ_169 - 百里挑一镰刀
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 冷却时间 -5%
    # 攻击速度 +8%
    # 物理暴击率 +2%
    # 魔法暴击率 +2%
    # rarity: 稀有
    pass


@register
def equ_170(char: CharacterProperty):
    # DCALC_REMOVE: equ_170 - 独一无二镰刀
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 冷却时间 -5%
    # 攻击速度 +8%
    # 物理暴击率 +2%
    # 魔法暴击率 +2%
    # rarity: 神器
    pass


@register
def equ_171(char: CharacterProperty):
    # DCALC_REMOVE: equ_171 - 传说承继 - 镰刀
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 冷却时间 -5%
    # 攻击速度 +8%
    # 物理暴击率 +2%
    # 魔法暴击率 +2%
    # rarity: 传说
    pass


@register
def equ_172(char: CharacterProperty):
    # DCALC_REMOVE: equ_172 - 英雄叙事诗 - 镰刀
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 冷却时间 -5%
    # 攻击速度 +8%
    # 物理暴击率 +2%
    # 魔法暴击率 +2%
    # rarity: 史诗
    pass


@register
def equ_173(char: CharacterProperty):
    # DCALC_REMOVE: equ_173 - 太初之星 - 镰刀
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 冷却时间 -5%
    # 攻击速度 +8%
    # 物理暴击率 +2%
    # 魔法暴击率 +2%
    # rarity: 太初
    pass


@register
def equ_174(char: CharacterProperty):
    # DCALC_REMOVE: equ_174 - 灵魂追踪者
    # [灵魂进献]
    # 进献灵魂，获得以下效果。
    # - 魔法值限制为50%
    # - 施放技能时，通过额外消耗技能所需魔法值的200%，增加该技能10%的技能攻击力
    # *如果剩余魔法值不足以额外消耗，则不会发动
    # - 攻击时，恢复1%的魔法值（冷却时间1秒）
    # rarity: 传说
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_175(char: CharacterProperty):
    # DCALC_REMOVE: equ_175 - 灵魂狩猎者
    # [灵魂交易]
    # 交易灵魂，获得以下效果。
    # - 魔法值限制为50%
    # - 施放技能时，通过额外消耗技能所需魔法值的300%，增加该技能13%的技能攻击力
    # *如果剩余魔法值不足以额外消耗，则不会发动
    # - 攻击时，使敌人发生灵魂爆炸，恢复10%的魔法值（冷却时间6秒）
    # rarity: 史诗
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_176(char: CharacterProperty):
    # DCALC_REMOVE: equ_176 - 灵魂掠夺者
    # [灵魂支配]
    # 支配灵魂，获得以下效果。
    # - 施放技能时，通过额外消耗技能所需魔法值的400%，增加该技能15%的技能攻击力
    # *如果剩余魔法值不足以额外消耗，则不会发动
    # - 每6秒吸收敌人的灵魂，恢复15%的魔法值
    # rarity: 太初
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_177(char: CharacterProperty):
    # DCALC_REMOVE: equ_177 - 百里挑一念珠
    # 物理百分比技能
    # 魔法值 -10% 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 +15%
    # 攻击速度 -5%
    # 施放速度 +5%
    # 魔法暴击率 +2%
    # rarity: 稀有
    pass


@register
def equ_178(char: CharacterProperty):
    # DCALC_REMOVE: equ_178 - 独一无二念珠
    # 物理百分比技能
    # 魔法值 -10% 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 +15%
    # 攻击速度 -5%
    # 施放速度 +5%
    # 魔法暴击率 +2%
    # rarity: 神器
    pass


@register
def equ_179(char: CharacterProperty):
    # DCALC_REMOVE: equ_179 - 传说承继 - 念珠
    # 物理百分比技能
    # 魔法值 -10% 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 +15%
    # 攻击速度 -5%
    # 施放速度 +5%
    # 魔法暴击率 +2%
    # rarity: 传说
    pass


@register
def equ_180(char: CharacterProperty):
    # DCALC_REMOVE: equ_180 - 英雄叙事诗 - 念珠
    # 物理百分比技能
    # 魔法值 -10% 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 +15%
    # 攻击速度 -5%
    # 施放速度 +5%
    # 魔法暴击率 +2%
    # rarity: 史诗
    pass


@register
def equ_181(char: CharacterProperty):
    # DCALC_REMOVE: equ_181 - 太初之星 - 念珠
    # 物理百分比技能
    # 魔法值 -10% 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 +15%
    # 攻击速度 -5%
    # 施放速度 +5%
    # 魔法暴击率 +2%
    # rarity: 太初
    pass


@register
def equ_182(char: CharacterProperty):
    # DCALC_REMOVE: equ_182 - 彗星念珠
    # 施放技能后，有15%的几率掉落流星。
    # - 流星伤害量：15000%
    # - 冷却时间：10秒
    # 所有速度 +15%
    # rarity: 传说
    char.equ_effect.append(EquEffect(name='流星念珠', icon='/equipment/icon/weapon/priest/rosary/00196.png', cd=10, data=15000))
    char.SetStatus(SpeedM=0.15, SpeedA=0.15, SpeedR=0.15)
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_183(char: CharacterProperty):
    # DCALC_REMOVE: equ_183 - 飞星念珠
    # 施放技能后，有25%的几率掉落流星。
    # - 流星伤害量：15000%
    # - 冷却时间：5秒
    # 所有速度 +20%
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='流星念珠', icon='/equipment/icon/weapon/priest/rosary/00197.png', cd=5, data=15000))
    char.SetStatus(SpeedM=0.15, SpeedA=0.15, SpeedR=0.15)
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_184(char: CharacterProperty):
    # DCALC_REMOVE: equ_184 - 流星念珠
    # 施放技能后，掉落蕴含宇宙力量的流星，效果持续5秒。
    # - 流星伤害量：135000%
    # - 冷却时间：20秒
    # 所有速度 +30%
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='流星念珠', icon='/equipment/icon/weapon/priest/rosary/00198.png', cd=20, data=340200))
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_185(char: CharacterProperty):
    # DCALC_REMOVE: equ_185 - 百里挑一战斧
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -15% 冷却时间 -10%
    # 攻击速度 -8%
    # 命中率 +2%
    # rarity: 稀有
    pass


@register
def equ_186(char: CharacterProperty):
    # DCALC_REMOVE: equ_186 - 独一无二战斧
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -15% 冷却时间 -10%
    # 攻击速度 -8%
    # 命中率 +2%
    # rarity: 神器
    pass


@register
def equ_187(char: CharacterProperty):
    # DCALC_REMOVE: equ_187 - 传说承继 - 战斧
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -15% 冷却时间 -10%
    # 攻击速度 -8%
    # 命中率 +2%
    # rarity: 传说
    pass


@register
def equ_188(char: CharacterProperty):
    # DCALC_REMOVE: equ_188 - 英雄叙事诗 - 战斧
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -15% 冷却时间 -10%
    # 攻击速度 -8%
    # 命中率 +2%
    # rarity: 史诗
    pass


@register
def equ_189(char: CharacterProperty):
    # DCALC_REMOVE: equ_189 - 太初之星 - 战斧
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -15% 冷却时间 -10%
    # 攻击速度 -8%
    # 命中率 +2%
    # rarity: 太初
    pass


@register
def equ_190(char: CharacterProperty):
    # DCALC_REMOVE: equ_190 - 大地破坏者
    # 技能范围 +20%
    # [行星破坏][装备主动技能]
    # 给战斧赋予摧毁大地的破坏之力并掷出。
    # - 行星破坏伤害量：113400%
    # - 冷却时间：40秒
    # rarity: 传说
    char.equ_effect.append(EquEffect(name='行星破坏', icon='/equipment/skill/40.png', cd=40, data=340200))
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_191(char: CharacterProperty):
    # DCALC_REMOVE: equ_191 - 行星粉碎者
    # 技能范围 +25%
    # [行星破坏][装备主动技能]
    # 给战斧赋予粉碎行星的破坏之力并掷出。
    # - 行星破坏伤害量：226800%
    # - 冷却时间：40秒
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='行星破坏', icon='/equipment/skill/40.png', cd=40, data=340200))
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_192(char: CharacterProperty):
    # DCALC_REMOVE: equ_192 - 灭亡之根源
    # 技能范围 +30%
    # [行星破坏][装备主动技能]
    # 掷出拥有灭亡的根源之力的战斧。
    # - 行星破坏伤害量：340200%
    # - 冷却时间：40秒
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='行星破坏', icon='/equipment/skill/40.png', cd=40, data=340200))
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetSkillCD(1, 100, 0.2)
    pass


@register
def equ_193(char: CharacterProperty):
    # DCALC_REMOVE: equ_193 - 百里挑一图腾
    # 物理百分比技能
    # 魔法值 +5%
    # 魔法百分比技能
    # 魔法值 -10% 冷却时间 -5%
    # 命中率 +1%
    # rarity: 稀有
    pass


@register
def equ_194(char: CharacterProperty):
    # DCALC_REMOVE: equ_194 - 独一无二图腾
    # 物理百分比技能
    # 魔法值 +5%
    # 魔法百分比技能
    # 魔法值 -10% 冷却时间 -5%
    # 命中率 +1%
    # rarity: 神器
    pass


@register
def equ_195(char: CharacterProperty):
    # DCALC_REMOVE: equ_195 - 传说承继 - 图腾
    # 物理百分比技能
    # 魔法值 +5%
    # 魔法百分比技能
    # 魔法值 -10% 冷却时间 -5%
    # 命中率 +1%
    # rarity: 传说
    pass


@register
def equ_196(char: CharacterProperty):
    # DCALC_REMOVE: equ_196 - 英雄叙事诗 - 图腾
    # 物理百分比技能
    # 魔法值 +5%
    # 魔法百分比技能
    # 魔法值 -10% 冷却时间 -5%
    # 命中率 +1%
    # rarity: 史诗
    pass


@register
def equ_197(char: CharacterProperty):
    # DCALC_REMOVE: equ_197 - 太初之星 - 图腾
    # 物理百分比技能
    # 魔法值 +5%
    # 魔法百分比技能
    # 魔法值 -10% 冷却时间 -5%
    # 命中率 +1%
    # rarity: 太初
    pass


@register
def equ_198(char: CharacterProperty):
    # DCALC_REMOVE: equ_198 - 天道之亲和
    # 技能冷却时间20%减少（觉醒技能除外）
    # [威严怒击]
    # 攻击时，向前方施放怒击。（冷却时间1秒）
    # - 怒击伤害量：6000%
    # rarity: 传说
    char.SetSkillCD(1, 100, 0.2)
    char.equ_effect.append(EquEffect(name='威严怒击', icon='/equipment/icon/weapon/priest/totem/00280.png', cd=1, data=6000))
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetStatus(SkillAttack=0.123)
    pass


@register
def equ_199(char: CharacterProperty):
    # DCALC_REMOVE: equ_199 - 天道之慈悲
    # 技能冷却时间20%减少（觉醒技能除外）
    # [威严怒击]
    # 攻击时，向前方施放怒击。（冷却时间1秒）
    # - 怒击伤害量：6000%
    # [威严猛击]
    # 施放技能时，向前方施放猛烈的连击。（冷却时间5秒）
    # - 猛烈连击伤害量：32400%
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='威严怒击', icon='/equipment/icon/weapon/priest/totem/00281.png', cd=1, data=6000))
    char.equ_effect.append(EquEffect(name='威严猛击', icon='/equipment/icon/weapon/priest/totem/00281.png', cd=5, data=32400))
    char.SetSkillCD(1, 100, 0.2)
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetStatus(SkillAttack=0.123)
    pass


@register
def equ_200(char: CharacterProperty):
    # DCALC_REMOVE: equ_200 - 天道之威严
    # 技能冷却时间20%减少（觉醒技能除外）
    # [威严怒击]
    # 攻击时，向前方施放怒击。（冷却时间1秒）
    # - 怒击伤害量：6000%
    # [威严猛击]
    # 施放技能时，向前方施放猛烈的连击。（冷却时间5秒）
    # - 猛烈连击伤害量：32400%
    # [威严痛击]
    # 施放无色小晶块技能时，发动威严痛击。（冷却时间10秒）
    # - 威严痛击伤害量：90000%
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='威严怒击', icon='/equipment/icon/weapon/priest/totem/00282.png', cd=1, data=6000))
    char.equ_effect.append(EquEffect(name='威严猛击', icon='/equipment/icon/weapon/priest/totem/00282.png', cd=5, data=32400))
    char.equ_effect.append(EquEffect(name='威严痛击', icon='/equipment/icon/weapon/priest/totem/00282.png', cd=5, data=90000))
    char.SetSkillCD(1, 100, 0.2)
    if char.buffer:
        char.AddSkillLv(1, 100, 2)
        char.BuffSkill.lv += 3
        char.AwakeSkill.lv += 4
        char.SetStatus(SkillAttack=0.123)
    pass


@register
def equ_201(char: CharacterProperty):
    # DCALC_REMOVE: equ_201 - 百里挑一匕首
    # 物理百分比技能
    # 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 -10% 冷却时间 -5%
    # 攻击速度 +10%
    # 物理暴击率 +10%
    # rarity: 稀有
    pass


@register
def equ_202(char: CharacterProperty):
    # DCALC_REMOVE: equ_202 - 独一无二匕首
    # 物理百分比技能
    # 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 -10% 冷却时间 -5%
    # 攻击速度 +10%
    # 物理暴击率 +10%
    # rarity: 神器
    pass


@register
def equ_203(char: CharacterProperty):
    # DCALC_REMOVE: equ_203 - 传说承继 - 匕首
    # 物理百分比技能
    # 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 -10% 冷却时间 -5%
    # 攻击速度 +10%
    # 物理暴击率 +10%
    # rarity: 传说
    pass


@register
def equ_204(char: CharacterProperty):
    # DCALC_REMOVE: equ_204 - 英雄叙事诗 - 匕首
    # 物理百分比技能
    # 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 -10% 冷却时间 -5%
    # 攻击速度 +10%
    # 物理暴击率 +10%
    # rarity: 史诗
    pass


@register
def equ_205(char: CharacterProperty):
    # DCALC_REMOVE: equ_205 - 太初之星 - 匕首
    # 物理百分比技能
    # 冷却时间 -10%
    # 魔法百分比技能
    # 魔法值 -10% 冷却时间 -5%
    # 攻击速度 +10%
    # 物理暴击率 +10%
    # rarity: 太初
    pass


@register
def equ_206(char: CharacterProperty):
    # DCALC_REMOVE: equ_206 - 女帝的华丽银妆刀
    # [女帝的威严]
    # 技能快捷栏中存在6个及以上空栏时，发动[女帝的威严]效果。
    # - 所有速度 +10%
    # rarity: 传说
    char.SetStatus(SpeedM=0.1, SpeedA=0.1, SpeedR=0.1)
    pass


@register
def equ_207(char: CharacterProperty):
    # DCALC_REMOVE: equ_207 - 女帝的灿烂银妆刀
    # [女帝的威严]
    # 技能快捷栏中存在4个及以上空栏时，发动[女帝的威严]效果。
    # - 所受物理/魔法伤害 -5%
    # - 所有速度 +15%
    # rarity: 史诗
    char.SetStatus(SpeedM=0.15, SpeedA=0.15, SpeedR=0.15)
    pass


@register
def equ_208(char: CharacterProperty):
    # DCALC_REMOVE: equ_208 - 女帝的玲珑银妆刀
    # [女帝的威严]
    # 技能快捷栏中存在3个及以上空栏时，发动[女帝的威严]效果。
    # - 进入霸体状态
    # - 所受物理/魔法伤害 -10%
    # - 所有速度 +20%
    # rarity: 太初
    char.SetStatus(SpeedM=0.2, SpeedA=0.2, SpeedR=0.2)
    pass


@register
def equ_209(char: CharacterProperty):
    # DCALC_REMOVE: equ_209 - 百里挑一双剑
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -20% 冷却时间 -10%
    # 攻击速度 -8%
    # 物理暴击率 +5%
    # rarity: 稀有
    pass


@register
def equ_210(char: CharacterProperty):
    # DCALC_REMOVE: equ_210 - 独一无二双剑
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -20% 冷却时间 -10%
    # 攻击速度 -8%
    # 物理暴击率 +5%
    # rarity: 神器
    pass


@register
def equ_211(char: CharacterProperty):
    # DCALC_REMOVE: equ_211 - 传说承继 - 双剑
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -20% 冷却时间 -10%
    # 攻击速度 -8%
    # 物理暴击率 +5%
    # rarity: 传说
    pass


@register
def equ_212(char: CharacterProperty):
    # DCALC_REMOVE: equ_212 - 英雄叙事诗 - 双剑
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -20% 冷却时间 -10%
    # 攻击速度 -8%
    # 物理暴击率 +5%
    # rarity: 史诗
    pass


@register
def equ_213(char: CharacterProperty):
    # DCALC_REMOVE: equ_213 - 太初之星 - 双剑
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -20% 冷却时间 -10%
    # 攻击速度 -8%
    # 物理暴击率 +5%
    # rarity: 太初
    pass


@register
def equ_214(char: CharacterProperty):
    # DCALC_REMOVE: equ_214 - 摇曳之地狱火
    # [永劫地狱火]
    # 施放技能后1.5秒内再次施放技能时，对最强敌人施放[永劫地狱火]。（冷却时间1秒）
    # - 地狱火伤害量：9360%
    # 每存在1个冷却中的技能，技能冷却时间恢复速度 +6%（觉醒技能除外；最多叠加5次）
    # - 叠加达上限时，技能范围 +10%
    # rarity: 传说
    char.SetSkillCDRecover(1, 100, 0.3)
    char.equ_effect.append(EquEffect(name='永劫地狱火', icon='/equipment/icon/weapon/thief/twinswd/00246.png', cd=1, data=9360))
    pass


@register
def equ_215(char: CharacterProperty):
    # DCALC_REMOVE: equ_215 - 闪耀之地狱火
    # [永劫地狱火]
    # 释放技能时，对最强的敌人释放[永劫地狱火]。（冷却时间1秒）
    # - 地狱火伤害量：10400%
    # 释放地狱火后，下一次地狱火的伤害量和大小 +4%（最多叠加5次）
    # - 10秒内未释放地狱火时，地狱火层数 -1
    # 每存在1个冷却中的技能，技能冷却时间恢复速度 +6%（觉醒技能除外；最多叠加5次）
    # - 叠加达上限时，技能范围 +12%
    # rarity: 史诗
    char.SetSkillCDRecover(1, 100, 0.3)
    char.equ_effect.append(EquEffect(name='永劫地狱火', icon='/equipment/icon/weapon/thief/twinswd/00247.png', cd=1, data=10400 * 1.2))
    pass


@register
def equ_216(char: CharacterProperty):
    # DCALC_REMOVE: equ_216 - 璀璨之地狱火
    # [永劫地狱火]
    # 释放技能时，对最强的敌人释放[永劫地狱火]。（冷却时间1秒）
    # - 地狱火伤害量：12480%
    # [覆灭地狱火]
    # 第5次释放地狱火时，对最强敌人释放烈炎狱火。
    # - 烈炎狱火伤害量：15600%
    # 每存在1个冷却中的技能，技能冷却时间恢复速度 +6%（觉醒技能除外；最多叠加5次）
    # - 叠加达上限时，技能范围 +15%
    # rarity: 太初
    char.SetSkillCDRecover(1, 100, 0.3)
    char.equ_effect.append(EquEffect(name='永劫地狱火', icon='/equipment/icon/weapon/thief/twinswd/00248.png', cd=1, data=12480))
    char.equ_effect.append(EquEffect(name='覆灭地狱火', icon='/equipment/icon/weapon/thief/twinswd/00248.png', cd=5, data=15600))
    pass


@register
def equ_217(char: CharacterProperty):
    # DCALC_REMOVE: equ_217 - 百里挑一手杖
    # 物理百分比技能
    # 魔法值 -5%
    # 魔法百分比技能
    # 魔法值 +15% 冷却时间 +5%
    # 攻击速速度 -10%
    # 魔法暴击率 +5%
    # rarity: 稀有
    pass


@register
def equ_218(char: CharacterProperty):
    # DCALC_REMOVE: equ_218 - 独一无二手杖
    # 物理百分比技能
    # 魔法值 -5%
    # 魔法百分比技能
    # 魔法值 +15% 冷却时间 +5%
    # 攻击速速度 -10%
    # 魔法暴击率 +5%
    # rarity: 神器
    pass


@register
def equ_219(char: CharacterProperty):
    # DCALC_REMOVE: equ_219 - 传说承继 - 手杖
    # 物理百分比技能
    # 魔法值 -5%
    # 魔法百分比技能
    # 魔法值 +15% 冷却时间 +5%
    # 攻击速速度 -10%
    # 魔法暴击率 +5%
    # rarity: 传说
    pass


@register
def equ_220(char: CharacterProperty):
    # DCALC_REMOVE: equ_220 - 英雄叙事诗 - 手杖
    # 物理百分比技能
    # 魔法值 -5%
    # 魔法百分比技能
    # 魔法值 +15% 冷却时间 +5%
    # 攻击速速度 -10%
    # 魔法暴击率 +5%
    # rarity: 史诗
    pass


@register
def equ_221(char: CharacterProperty):
    # DCALC_REMOVE: equ_221 - 太初之星 - 手杖
    # 物理百分比技能
    # 魔法值 -5%
    # 魔法百分比技能
    # 魔法值 +15% 冷却时间 +5%
    # 攻击速速度 -10%
    # 魔法暴击率 +5%
    # rarity: 太初
    pass


@register
def equ_222(char: CharacterProperty):
    # DCALC_REMOVE: equ_222 - 畏惧之主宰
    # 攻击时，被恐惧压制的敌人受到伤害。（冷却时间0.2秒）
    # *[恐惧]攻击力：1920%
    # rarity: 传说
    char.equ_effect.append(EquEffect(name='恐惧', icon='/equipment/icon/weapon/thief/wand/00269.png', cd=0.2, data=1920))
    pass


@register
def equ_223(char: CharacterProperty):
    # DCALC_REMOVE: equ_223 - 恐惧之主宰
    # 攻击时，被恐惧压制的敌人受到伤害。（冷却时间0.2秒）
    # *[恐惧]攻击力：1920%
    # [残暴的恐惧][装备主动技能]
    # 给最强大的敌人烙下恐惧之烙印。
    # - 技能伤害 +5%，效果持续10秒
    # - 冷却时间20秒
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='恐惧', icon='/equipment/icon/weapon/thief/wand/00270.png', cd=0.2, data=1920))
    if char.equ_options.get('5', 0) == 0:
        char.SetStatus(SkillAttack=0.05)
    elif char.equ_options.get('5', 0) == 2:
        char.SetStatus(SkillAttack=0.05 / 2)
    pass


@register
def equ_224(char: CharacterProperty):
    # DCALC_REMOVE: equ_224 - 恐怖之主宰
    # 攻击时，被恐惧压制的敌人受到伤害。（冷却时间0.2秒）
    # *[恐惧]攻击力：1920%
    # [无尽的恐惧][装备主动技能]
    # 给最强大的敌人施放降灵术。
    # - 技能伤害 +10%，效果持续10秒
    # - 持续时间结束时，落下冥河之钥
    # *冥河之钥伤害量：22800%
    # - 冷却时间20秒
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='恐惧', icon='/equipment/icon/weapon/thief/wand/00271.png', cd=0.2, data=1920))
    char.equ_effect.append(EquEffect(name='冥河之钥', icon='/equipment/skill/55.png', cd=20, data=22800))
    if char.equ_options.get('5', 0) == 0:
        char.SetStatus(SkillAttack=0.1)
    elif char.equ_options.get('5', 0) == 2:
        char.SetStatus(SkillAttack=0.1 / 2)
    pass


@register
def equ_225(char: CharacterProperty):
    # DCALC_REMOVE: equ_225 - 百里挑一苦无
    # 需要[苦无掌握]技能
    # 魔法百分比技能
    # 魔法值 +10%
    # 攻击速度 -5%
    # 施放速度 +5%
    # rarity: 稀有
    pass


@register
def equ_226(char: CharacterProperty):
    # DCALC_REMOVE: equ_226 - 独一无二苦无
    # 需要[苦无掌握]技能
    # 魔法百分比技能
    # 魔法值 +10%
    # 攻击速度 -5%
    # 施放速度 +5%
    # rarity: 神器
    pass


@register
def equ_227(char: CharacterProperty):
    # DCALC_REMOVE: equ_227 - 传说承继 - 苦无
    # 需要[苦无掌握]技能
    # 魔法百分比技能
    # 魔法值 +10%
    # 攻击速度 -5%
    # 施放速度 +5%
    # rarity: 传说
    pass


@register
def equ_228(char: CharacterProperty):
    # DCALC_REMOVE: equ_228 - 英雄叙事诗 - 苦无
    # 需要[苦无掌握]技能
    # 魔法百分比技能
    # 魔法值 +10%
    # 攻击速度 -5%
    # 施放速度 +5%
    # rarity: 史诗
    pass


@register
def equ_229(char: CharacterProperty):
    # DCALC_REMOVE: equ_229 - 太初之星 - 苦无
    # 需要[苦无掌握]技能
    # 魔法百分比技能
    # 魔法值 +10%
    # 攻击速度 -5%
    # 施放速度 +5%
    # rarity: 太初
    pass


@register
def equ_230(char: CharacterProperty):
    # DCALC_REMOVE: equ_230 - 恶道之因果轮回
    # 需要[苦无掌握]技能
    # [恶道]
    # 施放技能时，发动恶道之果，效果持续20秒。
    # - 技能范围 +15%
    # - 所有速度 +5%
    # rarity: 传说
    char.SetStatus(SpeedM=0.05, SpeedA=0.05, SpeedR=0.05)
    pass


@register
def equ_231(char: CharacterProperty):
    # DCALC_REMOVE: equ_231 - 善道之因果轮回
    # 需要[苦无掌握]技能
    # [善道]
    # 施放技能时，发动善道之果，效果持续20秒。
    # - 技能范围 +20%
    # - 所有速度 +5%
    # rarity: 史诗
    char.SetStatus(SpeedM=0.05, SpeedA=0.05, SpeedR=0.05)
    pass


@register
def equ_232(char: CharacterProperty):
    # DCALC_REMOVE: equ_232 - 六道之因果轮回
    # 需要[苦无掌握]技能
    # [六道]
    # 施放技能时，发动六道之果，效果持续20秒。
    # - 技能范围 +20%
    # - 所有速度 +10%
    # - 所受物理/魔法伤害 -5%
    # rarity: 太初
    char.SetStatus(SpeedM=0.1, SpeedA=0.1, SpeedR=0.1)
    pass


@register
def equ_233(char: CharacterProperty):
    # DCALC_REMOVE: equ_233 - 百里挑一长枪
    # 物理百分比技能
    # 魔法值 +10%
    # 攻击速度 +15%
    # 物理暴击率 +2%
    # rarity: 稀有
    pass


@register
def equ_234(char: CharacterProperty):
    # DCALC_REMOVE: equ_234 - 独一无二长枪
    # 物理百分比技能
    # 魔法值 +10%
    # 攻击速度 +15%
    # 物理暴击率 +2%
    # rarity: 神器
    pass


@register
def equ_235(char: CharacterProperty):
    # DCALC_REMOVE: equ_235 - 传说承继 - 长枪
    # 物理百分比技能
    # 魔法值 +10%
    # 攻击速度 +15%
    # 物理暴击率 +2%
    # rarity: 传说
    pass


@register
def equ_236(char: CharacterProperty):
    # DCALC_REMOVE: equ_236 - 英雄叙事诗 - 长枪
    # 物理百分比技能
    # 魔法值 +10%
    # 攻击速度 +15%
    # 物理暴击率 +2%
    # rarity: 史诗
    pass


@register
def equ_237(char: CharacterProperty):
    # DCALC_REMOVE: equ_237 - 太初之星 - 长枪
    # 物理百分比技能
    # 魔法值 +10%
    # 攻击速度 +15%
    # 物理暴击率 +2%
    # rarity: 太初
    pass


@register
def equ_238(char: CharacterProperty):
    # DCALC_REMOVE: equ_238 - 战场支配者
    # 15级技能冷却时间 -20%
    # 生成冲锋旗帜，发动以下效果。
    # - 所受物理/魔法伤害 -20%
    # rarity: 传说
    char.SetSkillCD(15,15,0.2)
    pass


@register
def equ_239(char: CharacterProperty):
    # DCALC_REMOVE: equ_239 - 战场至尊
    # 15级技能冷却时间 -30%
    # 生成冲锋旗帜，发动以下效果。
    # - 所受物理/魔法伤害 -25%
    # rarity: 史诗
    char.SetSkillCD(15, 15, 0.3)
    pass


@register
def equ_240(char: CharacterProperty):
    # DCALC_REMOVE: equ_240 - 战场斗神
    # 15级技能冷却时间 -40%
    # 生成冲锋旗帜，发动以下效果。
    # - 所受物理/魔法伤害 -30%
    # rarity: 太初
    char.SetSkillCD(15, 15, 0.4)
    pass


@register
def equ_241(char: CharacterProperty):
    # DCALC_REMOVE: equ_241 - 百里挑一战戟
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10% 冷却时间 -10%
    # 攻击速度 -8%
    # 命中率 +1%
    # rarity: 稀有
    pass


@register
def equ_242(char: CharacterProperty):
    # DCALC_REMOVE: equ_242 - 独一无二战戟
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10% 冷却时间 -10%
    # 攻击速度 -8%
    # 命中率 +1%
    # rarity: 神器
    pass


@register
def equ_243(char: CharacterProperty):
    # DCALC_REMOVE: equ_243 - 传说承继 - 战戟
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10% 冷却时间 -10%
    # 攻击速度 -8%
    # 命中率 +1%
    # rarity: 传说
    pass


@register
def equ_244(char: CharacterProperty):
    # DCALC_REMOVE: equ_244 - 英雄叙事诗 - 战戟
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10% 冷却时间 -10%
    # 攻击速度 -8%
    # 命中率 +1%
    # rarity: 史诗
    pass


@register
def equ_245(char: CharacterProperty):
    # DCALC_REMOVE: equ_245 - 太初之星 - 战戟
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10% 冷却时间 -10%
    # 攻击速度 -8%
    # 命中率 +1%
    # rarity: 太初
    pass


@register
def equ_246(char: CharacterProperty):
    # DCALC_REMOVE: equ_246 - 墨龙偃月刀
    # [墨龙偃月斩][装备主动技能]
    # 强力斩击前方的敌人，击倒对方。
    # - 伤害量：113400%
    # - 冷却时间：40秒
    # rarity: 传说
    char.equ_effect.append(EquEffect(name='墨龙偃月斩', icon='/equipment/skill/61.png', cd=40, data=113400))
    pass


@register
def equ_247(char: CharacterProperty):
    # DCALC_REMOVE: equ_247 - 精 · 墨龙偃月刀
    # [墨龙偃月斩][装备主动技能]
    # 强力斩击前方的敌人，击倒对方。
    # - 伤害量：226800%
    # - 冷却时间：40秒
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='墨龙偃月斩', icon='/equipment/skill/61.png', cd=40, data=226800))
    pass


@register
def equ_248(char: CharacterProperty):
    # DCALC_REMOVE: equ_248 - 真 · 墨龙偃月刀
    # [墨龙偃月斩][装备主动技能]
    # 强力斩击前方的敌人，击倒对方。
    # - 伤害量：340200%
    # - 冷却时间：40秒
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='墨龙偃月斩', icon='/equipment/skill/61.png', cd=40, data=340200))
    pass


@register
def equ_249(char: CharacterProperty):
    # DCALC_REMOVE: equ_249 - 百里挑一光枪
    # 魔法百分比技能
    # 魔法值 +15%
    # 施放速度 +2%
    # 魔法暴击率 +2%
    # rarity: 稀有
    pass


@register
def equ_250(char: CharacterProperty):
    # DCALC_REMOVE: equ_250 - 独一无二光枪
    # 魔法百分比技能
    # 魔法值 +15%
    # 施放速度 +2%
    # 魔法暴击率 +2%
    # rarity: 神器
    pass


@register
def equ_251(char: CharacterProperty):
    # DCALC_REMOVE: equ_251 - 传说承继 - 光枪
    # 魔法百分比技能
    # 魔法值 +15%
    # 施放速度 +2%
    # 魔法暴击率 +2%
    # rarity: 传说
    pass


@register
def equ_252(char: CharacterProperty):
    # DCALC_REMOVE: equ_252 - 英雄叙事诗 - 光枪
    # 魔法百分比技能
    # 魔法值 +15%
    # 施放速度 +2%
    # 魔法暴击率 +2%
    # rarity: 史诗
    pass


@register
def equ_253(char: CharacterProperty):
    # DCALC_REMOVE: equ_253 - 太初之星 - 光枪
    # 魔法百分比技能
    # 魔法值 +15%
    # 施放速度 +2%
    # 魔法暴击率 +2%
    # rarity: 太初
    pass


@register
def equ_254(char: CharacterProperty):
    # DCALC_REMOVE: equ_254 - 将星 : 流陨星光
    # 技能冷却时间20%减少（觉醒技能除外）
    # 所有速度 +10%
    # [星光盛宴]
    # 生成星之气息。（冷却时间30秒）
    # 生成星之气息后施放[后跳]技能时，消耗星之气息在随机位置进行流星攻击。
    # - 流星伤害量：38250%
    # - 使敌人进入眩晕状态
    # rarity: 传说
    char.SetSkillCD(1, 100, 0.2)
    char.SetStatus(SpeedM=0.1, SpeedA=0.1, SpeedR=0.1)
    char.equ_effect.append(EquEffect(name='星光盛宴', icon='/equipment/icon/weapon/demoniclancer/beamspear/00177.png', cd=30, data=38250))
    pass


@register
def equ_255(char: CharacterProperty):
    # DCALC_REMOVE: equ_255 - 将星 : 流陨星雨
    # 技能冷却时间20%减少（觉醒技能除外）
    # 所有速度 +12.5%
    # [星光盛宴]
    # 生成星之气息。（冷却时间30秒）
    # 生成星之气息后施放[后跳]技能时，消耗星之气息在随机位置进行流星攻击。
    # - 流星伤害量：38250%
    # - 使敌人进入眩晕状态
    # - [强化 -后跳]冷却时间 -10%
    # rarity: 史诗
    char.SetSkillCD(1, 100, 0.2)
    char.SetStatus(SpeedM=0.125, SpeedA=0.125, SpeedR=0.125)
    char.equ_effect.append(EquEffect(name='星光盛宴', icon='/equipment/icon/weapon/demoniclancer/beamspear/00178.png', cd=30, data=38250))
    pass


@register
def equ_256(char: CharacterProperty):
    # DCALC_REMOVE: equ_256 - 将星 : 流陨星河
    # 技能冷却时间20%减少（觉醒技能除外）
    # 所有速度 +15%
    # [星光盛宴]
    # 生成星之气息。（冷却时间30秒）
    # 生成星之气息后施放[后跳]技能时，消耗星之气息在随机位置进行流星攻击。
    # - 流星伤害量：38250%
    # - 使敌人进入眩晕状态
    # - [强化 -后跳]冷却时间 -20%
    # rarity: 太初
    char.SetSkillCD(1, 100, 0.2)
    char.SetStatus(SpeedM=0.15, SpeedA=0.15, SpeedR=0.15)
    char.equ_effect.append(EquEffect(name='星光盛宴', icon='/equipment/icon/weapon/demoniclancer/beamspear/00179.png', cd=30, data=38250))
    # char.equ_effect.append(EquEffect
    pass


@register
def equ_257(char: CharacterProperty):
    # DCALC_REMOVE: equ_257 - 百里挑一暗矛
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 +5% 冷却时间 -5%
    # 攻击速度 +8%
    # 施放速度 +5%
    # 魔法暴击率 +2%
    # rarity: 稀有
    pass


@register
def equ_258(char: CharacterProperty):
    # DCALC_REMOVE: equ_258 - 独一无二暗矛
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 +5% 冷却时间 -5%
    # 攻击速度 +8%
    # 施放速度 +5%
    # 魔法暴击率 +2%
    # rarity: 神器
    pass


@register
def equ_259(char: CharacterProperty):
    # DCALC_REMOVE: equ_259 - 传说承继 - 暗矛
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 +5% 冷却时间 -5%
    # 攻击速度 +8%
    # 施放速度 +5%
    # 魔法暴击率 +2%
    # rarity: 传说
    pass


@register
def equ_260(char: CharacterProperty):
    # DCALC_REMOVE: equ_260 - 英雄叙事诗 - 暗矛
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 +5% 冷却时间 -5%
    # 攻击速度 +8%
    # 施放速度 +5%
    # 魔法暴击率 +2%
    # rarity: 史诗
    pass


@register
def equ_261(char: CharacterProperty):
    # DCALC_REMOVE: equ_261 - 太初之星 - 暗矛
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 魔法值 +5% 冷却时间 -5%
    # 攻击速度 +8%
    # 施放速度 +5%
    # 魔法暴击率 +2%
    # rarity: 太初
    pass


@register
def equ_262(char: CharacterProperty):
    # DCALC_REMOVE: equ_262 - 无影暗寂灭
    # 所有速度 +5%
    # [深邃黑暗]
    # 对周围的所有敌人赋予深邃黑暗。
    # 存在深邃黑暗状态的怪物时，所有速度 +5%，效果持续10秒。（最多叠加4次）
    # rarity: 传说
    char.SetStatus(SpeedM=0.05, SpeedA=0.05, SpeedR=0.05)
    char.SetStatus(SpeedM=0.05*4, SpeedA=0.05*4, SpeedR=0.05*4)
    pass


@register
def equ_263(char: CharacterProperty):
    # DCALC_REMOVE: equ_263 - 无影暗诛灭
    # 所有速度 +15%
    # [深邃黑暗]
    # 对周围的所有敌人赋予深邃黑暗。
    # 存在深邃黑暗状态的怪物时，所有速度 +5%，效果持续10秒。（最多叠加4次）
    # [吞噬一切之暗]
    # 生产暗灭之矛气息。（冷却时间20秒）
    # 跳跃状态下攻击时，对已命中的怪物追加暗灭之矛攻击。
    # - 暗灭之矛伤害量：22800%
    # rarity: 史诗
    char.SetStatus(SpeedM=0.15, SpeedA=0.15, SpeedR=0.15)
    char.SetStatus(SpeedM=0.05*4, SpeedA=0.05*4, SpeedR=0.05*4)
    char.equ_effect.append(EquEffect(name='暗灭之矛', icon='/equipment/icon/weapon/demoniclancer/javelin/00167.png', cd=20, data=22800))
    pass


@register
def equ_264(char: CharacterProperty):
    # DCALC_REMOVE: equ_264 - 无影暗断灭
    # 所有速度 +15%
    # [深邃黑暗]
    # 对周围的所有敌人赋予深邃黑暗。
    # 存在深邃黑暗状态的怪物时，所有速度 +5%，效果持续10秒。（最多叠加4次）
    # [吞噬一切之暗]
    # 生产暗灭之矛气息。（冷却时间20秒）
    # 跳跃状态下攻击时，对已命中的怪物追加暗灭之矛攻击。
    # - 暗灭之矛伤害量：22800%
    # 暗灭之矛出现后，6个暗灭之矛追加攻击。
    # - 暗灭之矛伤害量：1000%
    # rarity: 太初
    char.SetStatus(SpeedM=0.15, SpeedA=0.15, SpeedR=0.15)
    char.SetStatus(SpeedM=0.05*4, SpeedA=0.05*4, SpeedR=0.05*4)
    char.equ_effect.append(EquEffect(name='暗灭之矛', icon='/equipment/icon/weapon/demoniclancer/javelin/00184.png', cd=20, data=22800+1000*6))
    pass


@register
def equ_265(char: CharacterProperty):
    # DCALC_REMOVE: equ_265 - 百里挑一小太刀
    # 物理百分比技能
    # 冷却时间 -5%
    # 攻击速度 +10%
    # 物理暴击率 +3%
    # rarity: 稀有
    pass


@register
def equ_266(char: CharacterProperty):
    # DCALC_REMOVE: equ_266 - 独一无二小太刀
    # 物理百分比技能
    # 冷却时间 -5%
    # 攻击速度 +10%
    # 物理暴击率 +3%
    # rarity: 神器
    pass


@register
def equ_267(char: CharacterProperty):
    # DCALC_REMOVE: equ_267 - 传说承继 - 小太刀
    # 物理百分比技能
    # 冷却时间 -5%
    # 攻击速度 +10%
    # 物理暴击率 +3%
    # rarity: 传说
    pass


@register
def equ_268(char: CharacterProperty):
    # DCALC_REMOVE: equ_268 - 英雄叙事诗 - 小太刀
    # 物理百分比技能
    # 冷却时间 -5%
    # 攻击速度 +10%
    # 物理暴击率 +3%
    # rarity: 史诗
    pass


@register
def equ_269(char: CharacterProperty):
    # DCALC_REMOVE: equ_269 - 太初之星 - 小太刀
    # 物理百分比技能
    # 冷却时间 -5%
    # 攻击速度 +10%
    # 物理暴击率 +3%
    # rarity: 太初
    pass


@register
def equ_270(char: CharacterProperty):
    # DCALC_REMOVE: equ_270 - 纳斯卡 : 灵魂低语
    # [魂器][装备主动技能]
    # - 施放时召唤魂器，召唤的魂器在2秒后激活
    # - 再次施放时，破坏已激活的魂器后瞬移到该位置
    # - 冷却时间：2秒
    # 所受物理/魔法伤害 -20%
    # rarity: 传说
    pass


@register
def equ_271(char: CharacterProperty):
    # DCALC_REMOVE: equ_271 - 纳斯卡 : 灵魂悲鸣
    # [魂器][装备主动技能]
    # - 施放时召唤魂器，召唤的魂器在2秒后激活
    # - 再次施放时，破坏已激活的魂器后瞬移到该位置
    # - 冷却时间：2秒
    # 所受物理/魔法伤害 -25%
    # rarity: 史诗
    pass


@register
def equ_272(char: CharacterProperty):
    # DCALC_REMOVE: equ_272 - 纳斯卡 : 灵魂审判
    # [魂器][装备主动技能]
    # - 施放时，召唤已激活的魂器
    # - 再次施放时，破坏已激活的魂器后瞬移到该位置
    # 所受物理/魔法伤害 -30%
    # rarity: 太初
    pass


@register
def equ_273(char: CharacterProperty):
    # DCALC_REMOVE: equ_273 - 百里挑一长刀
    # 物理百分比技能
    # 魔法值 +10%
    # 攻击速度 +5%
    # 命中率 +1%
    # rarity: 稀有
    pass


@register
def equ_274(char: CharacterProperty):
    # DCALC_REMOVE: equ_274 - 独一无二长刀
    # 物理百分比技能
    # 魔法值 +10%
    # 攻击速度 +5%
    # 命中率 +1%
    # rarity: 神器
    pass


@register
def equ_275(char: CharacterProperty):
    # DCALC_REMOVE: equ_275 - 传说承继 - 长刀
    # 物理百分比技能
    # 魔法值 +10%
    # 攻击速度 +5%
    # 命中率 +1%
    # rarity: 传说
    pass


@register
def equ_276(char: CharacterProperty):
    # DCALC_REMOVE: equ_276 - 英雄叙事诗 - 长刀
    # 物理百分比技能
    # 魔法值 +10%
    # 攻击速度 +5%
    # 命中率 +1%
    # rarity: 史诗
    pass


@register
def equ_277(char: CharacterProperty):
    # DCALC_REMOVE: equ_277 - 太初之星 - 长刀
    # 物理百分比技能
    # 魔法值 +10%
    # 攻击速度 +5%
    # 命中率 +1%
    # rarity: 太初
    pass


@register
def equ_278(char: CharacterProperty):
    # DCALC_REMOVE: equ_278 - 新月夜天刀
    # [满月]
    # 使用消耗无色小晶块的技能时，召唤攻击敌人的月影。
    # - 月影攻击力：82050%
    # - 冷却时间：20秒
    # 所有速度 +15%
    # rarity: 传说
    char.equ_effect.append(EquEffect(name='满月', icon='/equipment/icon/weapon/gunblader/lblade/00194.png', cd=20, data=82050))
    char.SetStatus(SpeedM=0.15, SpeedA=0.15, SpeedR=0.15)
    pass


@register
def equ_279(char: CharacterProperty):
    # DCALC_REMOVE: equ_279 - 弦月夜天刀
    # [满月]
    # 使用消耗无色小晶块的技能时，召唤攻击敌人的月影。
    # - 月影攻击力：164100%
    # - 冷却时间：20秒
    # 所有速度 +20%
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='满月', icon='/equipment/icon/weapon/gunblader/lblade/00195.png', cd=20, data=164100))
    char.SetStatus(SpeedM=0.2, SpeedA=0.2, SpeedR=0.2)
    pass


@register
def equ_280(char: CharacterProperty):
    # DCALC_REMOVE: equ_280 - 满月 : 辉光夜天刀
    # [满月]
    # 使用消耗无色小晶块的技能时，召唤攻击敌人的月影。
    # - 月影攻击力：218800%
    # - 冷却时间：20秒
    # 施放[电光飞掠]和[集结·暮光之翼]时，增加夜空中的星星闪烁效果。
    # 所有速度 +30%
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='满月', icon='/equipment/icon/weapon/gunblader/lblade/00196.png', cd=20, data=218800))
    char.SetStatus(SpeedM=0.3, SpeedA=0.3, SpeedR=0.3)
    pass


@register
def equ_281(char: CharacterProperty):
    # DCALC_REMOVE: equ_281 - 百里挑一重剑
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # rarity: 稀有
    pass


@register
def equ_282(char: CharacterProperty):
    # DCALC_REMOVE: equ_282 - 独一无二重剑
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # rarity: 神器
    pass


@register
def equ_283(char: CharacterProperty):
    # DCALC_REMOVE: equ_283 - 传说承继 - 重剑
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # rarity: 传说
    pass


@register
def equ_284(char: CharacterProperty):
    # DCALC_REMOVE: equ_284 - 英雄叙事诗 - 重剑
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # rarity: 史诗
    pass


@register
def equ_285(char: CharacterProperty):
    # DCALC_REMOVE: equ_285 - 太初之星 - 重剑
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # rarity: 太初
    pass


@register
def equ_286(char: CharacterProperty):
    # DCALC_REMOVE: equ_286 - 爆裂之锯
    # 技能冷却时间20%减少（觉醒技能除外）
    # [躁狂]
    # 进入地下城时，[躁狂]层数 +10
    # - 最多叠加10层
    # 每秒[躁狂]层数 +1
    # [戮影之舞][装备主动技能]
    # 消耗6层[躁狂]，攻击前方敌人。
    # - 戮影之舞伤害量：12600%
    # rarity: 传说
    char.SetSkillCD(cd=0.2)
    char.equ_effect.append(EquEffect(name='戮影之舞', icon='/equipment/skill/43.png', cd=6, data=12600))
    pass


@register
def equ_287(char: CharacterProperty):
    # DCALC_REMOVE: equ_287 - 凶残之锯
    # 技能冷却时间20%减少（觉醒技能除外）
    # [躁狂]
    # 进入地下城时，[躁狂]层数 +10
    # - 最多叠加10层
    # 每秒[躁狂]层数 +1
    # 释放技能时，[躁狂]层数 +1（冷却时间5秒）
    # [戮影之舞][装备主动技能]
    # 消耗5层[躁狂]，攻击前方敌人。
    # - 戮影之舞伤害量：12600%
    # rarity: 史诗
    char.SetSkillCD(cd=0.2)
    char.equ_effect.append(EquEffect(name='戮影之舞', icon='/equipment/skill/43.png', cd=4.17, data=12600))
    pass


@register
def equ_288(char: CharacterProperty):
    # DCALC_REMOVE: equ_288 - 惊魂之锯
    # 技能冷却时间20%减少（觉醒技能除外）
    # [躁狂]
    # 进入地下城时，[躁狂]层数 +12
    # - 最多叠加12层
    # 每秒[躁狂]层数 +1
    # 释放技能时，[躁狂]层数 +2（冷却时间5秒）
    # [戮影之舞][装备主动技能]
    # 消耗4层[躁狂]，攻击前方敌人。
    # - 戮影之舞伤害量：12600%
    # rarity: 太初
    char.SetSkillCD(cd=0.2)
    char.equ_effect.append(EquEffect(name='戮影之舞', icon='/equipment/skill/43.png', cd=2.85, data=12600))
    pass


@register
def equ_289(char: CharacterProperty):
    # DCALC_REMOVE: equ_289 - 百里挑一源力剑
    # 魔法百分比技能
    # 魔法值 +15%
    # 魔法暴击率 +2%
    # rarity: 稀有
    pass


@register
def equ_290(char: CharacterProperty):
    # DCALC_REMOVE: equ_290 - 独一无二源力剑
    # 魔法百分比技能
    # 魔法值 +15%
    # 魔法暴击率 +2%
    # rarity: 神器
    pass


@register
def equ_291(char: CharacterProperty):
    # DCALC_REMOVE: equ_291 - 传说承继 - 源力剑
    # 魔法百分比技能
    # 魔法值 +15%
    # 魔法暴击率 +2%
    # rarity: 传说
    pass


@register
def equ_292(char: CharacterProperty):
    # DCALC_REMOVE: equ_292 - 英雄叙事诗 - 源力剑
    # 魔法百分比技能
    # 魔法值 +15%
    # 魔法暴击率 +2%
    # rarity: 史诗
    pass


@register
def equ_293(char: CharacterProperty):
    # DCALC_REMOVE: equ_293 - 太初之星 - 源力剑
    # 魔法百分比技能
    # 魔法值 +15%
    # 魔法暴击率 +2%
    # rarity: 太初
    pass


@register
def equ_294(char: CharacterProperty):
    # DCALC_REMOVE: equ_294 - 超频之心
    # [超频源力]
    # 攻击时，给敌人附着核心源动力。
    # - 各目标适用冷却时间40秒
    # 根据对附着核心源动力的敌人造成的攻击次数，追加攻击。
    # - 每攻击5次，发动能量冲击
    # 能量冲击伤害量2835%
    # - 攻击100次后，解除核心源动力
    # rarity: 传说
    char.equ_effect.append(EquEffect(name='超频源力[5次]', icon='/equipment/icon/weapon/gunblader/coreswd/00163.png', cd=40, data=2835))
    pass


@register
def equ_295(char: CharacterProperty):
    # DCALC_REMOVE: equ_295 - 超频之核
    # [超频源力]
    # 攻击时，给敌人附着核心源动力。
    # - 各目标适用冷却时间40秒
    # 根据对附着核心源动力的敌人造成的攻击次数，追加攻击。
    # - 每攻击5次：发动能量冲击
    # 能量冲击伤害量2835%
    # - 每攻击20次：发动能量爆发
    # 能量爆发伤害量：22680%
    # - 攻击100次后，解除核心源动力
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='超频源力[5次]', icon='/equipment/icon/weapon/gunblader/coreswd/00164.png', cd=40, data=2835))
    char.equ_effect.append(EquEffect(name='超频源力[20次]', icon='/equipment/icon/weapon/gunblader/coreswd/00164.png', cd=40, data=22680))
    pass


@register
def equ_296(char: CharacterProperty):
    # DCALC_REMOVE: equ_296 - 核心源力
    # [超频源力]
    # 攻击时，给敌人附着核心源动力。
    # - 各目标适用冷却时间40秒
    # 根据对附着核心源动力的敌人造成的攻击次数，追加攻击。
    # - 每攻击5次：发动能量冲击
    # 能量冲击伤害量2835%
    # - 每攻击20次：发动能量爆发
    # 能量爆发伤害量：22680%
    # - 每攻击100次：发动核心爆发
    # 核心爆发伤害量：170100%
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='超频源力[5次]', icon='/equipment/icon/weapon/gunblader/coreswd/00165.png', cd=40, data=2835))
    char.equ_effect.append(EquEffect(name='超频源力[20次]', icon='/equipment/icon/weapon/gunblader/coreswd/00165.png', cd=40, data=22680))
    char.equ_effect.append(EquEffect(name='超频源力[100次]', icon='/equipment/icon/weapon/gunblader/coreswd/00165.png', cd=40, data=170100))
    pass


@register
def equ_297(char: CharacterProperty):
    # DCALC_REMOVE: equ_297 - 百里挑一玄机弓
    # 物理百分比技能
    # 魔法值 +10%
    # 攻击速度 +8%
    # rarity: 稀有
    pass


@register
def equ_298(char: CharacterProperty):
    # DCALC_REMOVE: equ_298 - 独一无二玄机弓
    # 物理百分比技能
    # 魔法值 +10%
    # 攻击速度 +8%
    # rarity: 神器
    pass


@register
def equ_299(char: CharacterProperty):
    # DCALC_REMOVE: equ_299 - 传说承继 - 玄机弓
    # 物理百分比技能
    # 魔法值 +10%
    # 攻击速度 +8%
    # rarity: 传说
    pass


@register
def equ_300(char: CharacterProperty):
    # DCALC_REMOVE: equ_300 - 英雄叙事诗 - 玄机弓
    # 物理百分比技能
    # 魔法值 +10%
    # 攻击速度 +8%
    # rarity: 史诗
    pass


@register
def equ_301(char: CharacterProperty):
    # DCALC_REMOVE: equ_301 - 太初之星 - 玄机弓
    # 物理百分比技能
    # 魔法值 +10%
    # 攻击速度 +8%
    # rarity: 太初
    pass


@register
def equ_302(char: CharacterProperty):
    # DCALC_REMOVE: equ_302 - 迷雾旅行者
    # [引路者][装备主动技能]
    # 进入地下城时，[迷雾行者]自动生效。
    # 使用时，[迷雾之路]生效。
    # - 冷却时间300秒
    # [迷雾行者]
    # - 技能伤害 +12.3%
    # [迷雾之路]
    # - 技能冷却时间 -20%
    # rarity: 传说
    pass


@register
def equ_303(char: CharacterProperty):
    # DCALC_REMOVE: equ_303 - 迷雾探险者
    # [引路者][装备主动技能]
    # 进入地下城时，[迷雾行者]自动生效。
    # 使用时，[迷雾之路]生效。
    # - 冷却时间300秒
    # [迷雾行者]
    # - 技能伤害 +12.3%
    # [迷雾之路]
    # - 技能冷却时间 -20%
    # rarity: 史诗
    pass


@register
def equ_304(char: CharacterProperty):
    # DCALC_REMOVE: equ_304 - 迷雾拓荒者
    # [引路者][装备主动技能]
    # 进入地下城时，[迷雾行者]自动生效。
    # 使用时，[迷雾之路]生效。
    # - 冷却时间300秒
    # [迷雾行者]
    # - 技能伤害 +12.3%
    # [迷雾之路]
    # - 技能冷却时间 -20%
    # rarity: 太初
    pass


@register
def equ_305(char: CharacterProperty):
    # DCALC_REMOVE: equ_305 - 百里挑一神弦弓
    # 需要[悦耳音律]技能
    # 攻击速度 +5%
    # 施放速度 +2%
    # rarity: 稀有
    pass


@register
def equ_306(char: CharacterProperty):
    # DCALC_REMOVE: equ_306 - 独一无二神弦弓
    # 需要[悦耳音律]技能
    # 攻击速度 +5%
    # 施放速度 +2%
    # rarity: 神器
    pass


@register
def equ_307(char: CharacterProperty):
    # DCALC_REMOVE: equ_307 - 传说承继 - 神弦弓
    # 需要[悦耳音律]技能
    # 攻击速度 +5%
    # 施放速度 +2%
    # rarity: 传说
    pass


@register
def equ_308(char: CharacterProperty):
    # DCALC_REMOVE: equ_308 - 英雄叙事诗 - 神弦弓
    # 需要[悦耳音律]技能
    # 攻击速度 +5%
    # 施放速度 +2%
    # rarity: 史诗
    pass


@register
def equ_309(char: CharacterProperty):
    # DCALC_REMOVE: equ_309 - 太初之星 - 神弦弓
    # 需要[悦耳音律]技能
    # 攻击速度 +5%
    # 施放速度 +2%
    # rarity: 太初
    pass


@register
def equ_310(char: CharacterProperty):
    # DCALC_REMOVE: equ_310 - 私语独奏
    # 需要[悦耳音律]技能
    # [琴瑟谐和][装备主动技能]
    # 进入地下城时，[活力旋律]自动生效。
    # 使用时，[华彩乐章]生效。
    # - 冷却时间300秒
    # [活力旋律]
    # - 技能冷却时间 -20%
    # [华彩乐章]
    # - 技能伤害 +12.3%
    # rarity: 传说
    pass


@register
def equ_311(char: CharacterProperty):
    # DCALC_REMOVE: equ_311 - 私语双重奏
    # 需要[悦耳音律]技能
    # [琴瑟谐和][装备主动技能]
    # 进入地下城时，[活力旋律]自动生效。
    # 使用时，[华彩乐章]生效。
    # - 冷却时间300秒
    # [活力旋律]
    # - 技能冷却时间 -20%
    # [华彩乐章]
    # - 技能伤害 +12.3%
    # rarity: 史诗
    pass


@register
def equ_312(char: CharacterProperty):
    # DCALC_REMOVE: equ_312 - 私语音乐会
    # 需要[悦耳音律]技能
    # [琴瑟谐和][装备主动技能]
    # 进入地下城时，[活力旋律]自动生效。
    # 使用时，[华彩乐章]生效。
    # - 冷却时间300秒
    # [活力旋律]
    # - 技能冷却时间 -20%
    # [华彩乐章]
    # - 技能伤害 +12.3%
    # rarity: 太初
    pass


@register
def equ_313(char: CharacterProperty):
    # DCALC_REMOVE: equ_313 - 百里挑一强攻弩
    # 需要[强弓弩掌握]技能
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # rarity: 稀有
    pass


@register
def equ_314(char: CharacterProperty):
    # DCALC_REMOVE: equ_314 - 独一无二强攻弩
    # 需要[强弓弩掌握]技能
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # rarity: 神器
    pass


@register
def equ_315(char: CharacterProperty):
    # DCALC_REMOVE: equ_315 - 传说承继 - 强攻弩
    # 需要[强弓弩掌握]技能
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # rarity: 传说
    pass


@register
def equ_316(char: CharacterProperty):
    # DCALC_REMOVE: equ_316 - 英雄叙事诗 - 强攻弩
    # 需要[强弓弩掌握]技能
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # rarity: 史诗
    pass


@register
def equ_317(char: CharacterProperty):
    # DCALC_REMOVE: equ_317 - 太初之星 - 强攻弩
    # 需要[强弓弩掌握]技能
    # 物理百分比技能
    # 魔法值 +20% 冷却时间 +5%
    # 魔法百分比技能
    # 魔法值 -10%
    # 攻击速度 -8%
    # rarity: 太初
    pass


@register
def equ_318(char: CharacterProperty):
    # DCALC_REMOVE: equ_318 - 伙伴帕伊卡
    # 需要[强弓弩掌握]技能
    # [战略调整][装备主动技能]
    # 进入地下城时，[帕伊卡助攻]自动生效。
    # 使用时，[帕伊卡巡逻]生效。
    # - 冷却时间300秒
    # [帕伊卡助攻]
    # - 技能伤害 +12.3%
    # [帕伊卡巡逻]
    # - 技能冷却时间 -20%
    # rarity: 传说
    pass


@register
def equ_319(char: CharacterProperty):
    # DCALC_REMOVE: equ_319 - 挚友帕伊卡
    # 需要[强弓弩掌握]技能
    # [战略调整][装备主动技能]
    # 进入地下城时，[帕伊卡助攻]自动生效。
    # 使用时，[帕伊卡巡逻]生效。
    # - 冷却时间300秒
    # [帕伊卡助攻]
    # - 技能伤害 +12.3%
    # [帕伊卡巡逻]
    # - 技能冷却时间 -20%
    # rarity: 史诗
    pass


@register
def equ_320(char: CharacterProperty):
    # DCALC_REMOVE: equ_320 - 亲眷帕伊卡
    # [战略调整][装备主动技能]
    # 进入地下城时，[帕伊卡助攻]自动生效。
    # 使用时，[帕伊卡巡逻]生效。
    # - 冷却时间300秒
    # [帕伊卡助攻]
    # - 技能伤害 +12.3%
    # [帕伊卡巡逻]
    # - 技能冷却时间 -20%
    # rarity: 太初
    pass


@register
def equ_321(char: CharacterProperty):
    # DCALC_REMOVE: equ_321 - 百里挑一妖影弓
    # 需要[超越两界]技能
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 冷却时间 -5%
    # 攻击速度 +8%
    # 物理暴击率 +2%
    # 魔法暴击率 +2%
    # rarity: 稀有
    pass


@register
def equ_322(char: CharacterProperty):
    # DCALC_REMOVE: equ_322 - 独一无二妖影弓
    # 需要[超越两界]技能
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 冷却时间 -5%
    # 攻击速度 +8%
    # 物理暴击率 +2%
    # 魔法暴击率 +2%
    # rarity: 神器
    pass


@register
def equ_323(char: CharacterProperty):
    # DCALC_REMOVE: equ_323 - 传说承继 - 妖影弓
    # 需要[超越两界]技能
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 冷却时间 -5%
    # 攻击速度 +8%
    # 物理暴击率 +2%
    # 魔法暴击率 +2%
    # rarity: 传说
    pass


@register
def equ_324(char: CharacterProperty):
    # DCALC_REMOVE: equ_324 - 英雄叙事诗 - 妖影弓
    # 需要[超越两界]技能
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 冷却时间 -5%
    # 攻击速度 +8%
    # 物理暴击率 +2%
    # 魔法暴击率 +2%
    # rarity: 史诗
    pass


@register
def equ_325(char: CharacterProperty):
    # DCALC_REMOVE: equ_325 - 太初之星 - 妖影弓
    # 需要[超越两界]技能
    # 物理百分比技能
    # 魔法值 -5% 冷却时间 -5%
    # 魔法百分比技能
    # 冷却时间 -5%
    # 攻击速度 +8%
    # 物理暴击率 +2%
    # 魔法暴击率 +2%
    # rarity: 太初
    pass


@register
def equ_326(char: CharacterProperty):
    # DCALC_REMOVE: equ_326 - 妖语子夜
    # 需要[超越两界]技能
    # [全神贯注][装备主动技能]
    # 进入地下城时，[弱点捕捉]自动生效。
    # 使用时，[危险感知]生效。
    # - 冷却时间 -300秒
    # [弱点捕捉]
    # - 技能伤害 +12.3%
    # [危险感知]
    # - 技能冷却时间 -20%
    # rarity: 传说
    pass


@register
def equ_327(char: CharacterProperty):
    # DCALC_REMOVE: equ_327 - 妖语黎明
    # 需要[超越两界]技能
    # [全神贯注][装备主动技能]
    # 进入地下城时，[弱点捕捉]自动生效。
    # 使用时，[危险感知]生效。
    # - 冷却时间 -300秒
    # [弱点捕捉]
    # - 技能伤害 +12.3%
    # [危险感知]
    # - 技能冷却时间 -20%
    # rarity: 史诗
    pass


@register
def equ_328(char: CharacterProperty):
    # DCALC_REMOVE: equ_328 - 妖语黄昏
    # [全神贯注][装备主动技能]
    # 进入地下城时，[弱点捕捉]自动生效。
    # 使用时，[危险感知]生效。
    # - 冷却时间 -300秒
    # [弱点捕捉]
    # - 技能伤害 +12.3%
    # [危险感知]
    # - 技能冷却时间 -20%
    # rarity: 太初
    pass


# endregion
# region 稀有装备 套装


@register
def equ_329(char: CharacterProperty):
    # DCALC_REMOVE: equ_329 - 起始之忍上衣
    # -
    # rarity: 稀有
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_330(char: CharacterProperty):
    # DCALC_REMOVE: equ_330 - 起始之忍下装
    # -
    # rarity: 稀有
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_331(char: CharacterProperty):
    # DCALC_REMOVE: equ_331 - 起始之志长袍
    # 攻击速度 +35%
    # 施放速度 +35%
    # rarity: 稀有
    char.SetStatus(SpeedA=0.35, SpeedR=0.35)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_332(char: CharacterProperty):
    # DCALC_REMOVE: equ_332 - 起始之典腰带
    # 物品栏负重上限 +3kg
    # rarity: 稀有
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_333(char: CharacterProperty):
    # DCALC_REMOVE: equ_333 - 起始之源鞋子
    # 移动速度 +39%
    # rarity: 稀有
    char.SetStatus(SpeedM=0.39)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_334(char: CharacterProperty):
    # DCALC_REMOVE: equ_334 - 起始之勉项链
    # 所有属性强化 +40
    # rarity: 稀有
    char.AddElementDB('光', 40)
    char.AddElementDB('火', 40)
    char.AddElementDB('冰', 40)
    char.AddElementDB('暗', 40)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_335(char: CharacterProperty):
    # DCALC_REMOVE: equ_335 - 起始之鸣手镯
    # 所有属性强化 +50
    # rarity: 稀有
    char.AddElementDB('光', 50)
    char.AddElementDB('火', 50)
    char.AddElementDB('冰', 50)
    char.AddElementDB('暗', 50)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_336(char: CharacterProperty):
    # DCALC_REMOVE: equ_336 - 起始之瞬戒指
    # 所有属性强化 +40
    # rarity: 稀有
    char.AddElementDB('光', 40)
    char.AddElementDB('火', 40)
    char.AddElementDB('冰', 40)
    char.AddElementDB('暗', 40)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_337(char: CharacterProperty):
    # DCALC_REMOVE: equ_337 - 起始之备辅助装备
    # 物理暴击率 +20%
    # 魔法暴击率 +20%
    # rarity: 稀有
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_338(char: CharacterProperty):
    # DCALC_REMOVE: equ_338 - 起始之恒魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 稀有
    char.SetSkillCD(1, 100, 0.15)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 2
    pass


@register
def equ_339(char: CharacterProperty):
    # DCALC_REMOVE: equ_339 - 起始之声耳环
    # -
    # rarity: 稀有
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
        char.SetStatus(STR=200, INT=200, Spirit=200, Vitality=200)
    pass


# endregion
# region 通宝装备


@register
def equ_340(char: CharacterProperty):
    # DCALC_REMOVE: equ_340 - 通宝 - 铁面的爆笑胸甲
    # 所受物理/魔法伤害 -10%
    # rarity: 神器
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_341(char: CharacterProperty):
    # DCALC_REMOVE: equ_341 - 通宝 - 铁面的谑笑胸甲
    # 所受物理/魔法伤害 -15%
    # rarity: 传说
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_342(char: CharacterProperty):
    # DCALC_REMOVE: equ_342 - 通宝 - 铁面的哭泣胸甲
    # 所受物理/魔法伤害 -20%
    # rarity: 史诗
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_343(char: CharacterProperty):
    # DCALC_REMOVE: equ_343 - 通宝 - 清海的坚硬腿甲
    # 维持前冲状态1秒后，进入无敌状态0.3秒
    # rarity: 神器
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_344(char: CharacterProperty):
    # DCALC_REMOVE: equ_344 - 通宝 - 清海的坚韧腿甲
    # 维持前冲状态1秒后，进入无敌状态0.5秒
    # rarity: 传说
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_345(char: CharacterProperty):
    # DCALC_REMOVE: equ_345 - 通宝 - 清海的坚不可摧腿甲
    # 维持前冲状态1秒后，进入无敌状态1秒
    # rarity: 史诗
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_346(char: CharacterProperty):
    # DCALC_REMOVE: equ_346 - 通宝 - 萌生的不安气息头肩
    # 攻击时，生成雾珠，聚集100px范围内敌人。（冷却10秒）
    # rarity: 神器
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_347(char: CharacterProperty):
    # DCALC_REMOVE: equ_347 - 通宝 - 滋生的不祥气息头肩
    # 攻击时，生成雾珠，聚集200px范围内敌人。（冷却10秒）
    # rarity: 传说
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_348(char: CharacterProperty):
    # DCALC_REMOVE: equ_348 - 通宝 - 蔓生之妖气头肩
    # 攻击时，生成雾珠，聚集400px范围内敌人。（冷却10秒）
    # rarity: 史诗
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_349(char: CharacterProperty):
    # DCALC_REMOVE: equ_349 - 通宝 - 灭妖者的意志腰带
    # 物品栏负重上限 +3kg
    # [强化 -后跳]技能冷冷却时间 -3秒
    # rarity: 神器
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_350(char: CharacterProperty):
    # DCALC_REMOVE: equ_350 - 通宝 - 灭妖者的迷失腰带
    # 物品栏负重上限 +3kg
    # [强化 -后跳]技能冷冷却时间 -5秒
    # rarity: 传说
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_351(char: CharacterProperty):
    # DCALC_REMOVE: equ_351 - 通宝 - 灭妖者的愤怒腰带
    # 物品栏负重上限 +3kg
    # [强化 -后跳]技能冷冷却时间 -10秒
    # rarity: 史诗
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_352(char: CharacterProperty):
    # DCALC_REMOVE: equ_352 - 通宝 - 慈爱的猎月者鞋子
    # 移动速度 +24%
    # 所有速度 +20%
    # rarity: 神器
    char.SetStatus(SpeedM=0.24)
    char.SetStatus(SpeedM=0.2)
    char.SetStatus(SpeedA=0.2)
    char.SetStatus(SpeedR=0.2)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_353(char: CharacterProperty):
    # DCALC_REMOVE: equ_353 - 通宝 - 决绝的猎月者鞋子
    # 移动速度 +29%
    # 所有速度 +30%
    # rarity: 传说
    char.SetStatus(SpeedM=0.29)
    char.SetStatus(SpeedM=0.3)
    char.SetStatus(SpeedA=0.3)
    char.SetStatus(SpeedR=0.3)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_354(char: CharacterProperty):
    # DCALC_REMOVE: equ_354 - 通宝 - 悲痛的猎月者鞋子
    # 移动速度 +29%
    # 所有速度 +50%
    # rarity: 史诗
    char.SetStatus(SpeedM=0.29)
    char.SetStatus(SpeedM=0.5)
    char.SetStatus(SpeedA=0.5)
    char.SetStatus(SpeedR=0.5)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_355(char: CharacterProperty):
    # DCALC_REMOVE: equ_355 - 通宝 - 无瑕冥语的记忆项链
    # 所有属性强化 +40
    # 获得生命值最大值10%的[填充型保护罩]
    # - 按照装备、消耗品、恢复技能提供的生命值恢复量的10%，恢复保护罩
    # - 持续恢复的技能除外
    # rarity: 神器
    char.AddElementDB('光', 40)
    char.AddElementDB('火', 40)
    char.AddElementDB('冰', 40)
    char.AddElementDB('暗', 40)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_356(char: CharacterProperty):
    # DCALC_REMOVE: equ_356 - 通宝 - 无瑕冥语的希望项链
    # 所有属性强化 +40
    # 获得生命值最大值20%的[填充型保护罩]
    # - 按照装备、消耗品、恢复技能提供的生命值恢复量的30%，恢复保护罩
    # - 持续恢复的技能除外
    # rarity: 传说
    char.AddElementDB('光', 40)
    char.AddElementDB('火', 40)
    char.AddElementDB('冰', 40)
    char.AddElementDB('暗', 40)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_357(char: CharacterProperty):
    # DCALC_REMOVE: equ_357 - 通宝 - 无瑕冥语的多情项链
    # 所有属性强化 +40
    # 获得生命值最大值30%的[填充型保护罩]
    # - 按照装备、消耗品、恢复技能提供的生命值恢复量的50%，恢复保护罩
    # - 持续恢复的技能除外
    # rarity: 史诗
    char.AddElementDB('光', 40)
    char.AddElementDB('火', 40)
    char.AddElementDB('冰', 40)
    char.AddElementDB('暗', 40)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_358(char: CharacterProperty):
    # DCALC_REMOVE: equ_358 - 通宝 - 亵渎者的取向手镯
    # 所有属性强化 +50
    # 特效伤害 +3%
    # rarity: 神器
    char.AddElementDB('光', 50)
    char.AddElementDB('火', 50)
    char.AddElementDB('冰', 50)
    char.AddElementDB('暗', 50)
    char.SetStatus(EquEffectRatio=0.03)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_359(char: CharacterProperty):
    # DCALC_REMOVE: equ_359 - 通宝 - 亵渎者的计划手镯
    # 所有属性强化 +50
    # 特效伤害 +6%
    # rarity: 传说
    char.AddElementDB('光', 50)
    char.AddElementDB('火', 50)
    char.AddElementDB('冰', 50)
    char.AddElementDB('暗', 50)
    char.SetStatus(EquEffectRatio=0.06)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_360(char: CharacterProperty):
    # DCALC_REMOVE: equ_360 - 通宝 - 亵渎者的愚弄手镯
    # 所有属性强化 +50
    # 特效伤害 +10%
    # rarity: 史诗
    char.AddElementDB('光', 50)
    char.AddElementDB('火', 50)
    char.AddElementDB('冰', 50)
    char.AddElementDB('暗', 50)
    char.SetStatus(EquEffectRatio=0.1)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_361(char: CharacterProperty):
    # DCALC_REMOVE: equ_361 - 通宝 - 亵渎者的诱惑戒指
    # 所有属性强化 +40
    # [受身蹲伏]的蹲伏姿势时，无敌时间上限 +0.3秒
    # rarity: 神器
    char.AddElementDB('光', 40)
    char.AddElementDB('火', 40)
    char.AddElementDB('冰', 40)
    char.AddElementDB('暗', 40)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_362(char: CharacterProperty):
    # DCALC_REMOVE: equ_362 - 通宝 - 亵渎者的魅惑戒指
    # 所有属性强化 +40
    # [受身蹲伏]的蹲伏姿势时，无敌时间上限 +0.5秒
    # rarity: 传说
    char.AddElementDB('光', 40)
    char.AddElementDB('火', 40)
    char.AddElementDB('冰', 40)
    char.AddElementDB('暗', 40)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_363(char: CharacterProperty):
    # DCALC_REMOVE: equ_363 - 通宝 - 亵渎者的蛊惑戒指
    # 所有属性强化 +40
    # [受身蹲伏]的蹲伏姿势时，无敌时间上限 +1秒
    # rarity: 史诗
    char.AddElementDB('光', 40)
    char.AddElementDB('火', 40)
    char.AddElementDB('冰', 40)
    char.AddElementDB('暗', 40)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_364(char: CharacterProperty):
    # DCALC_REMOVE: equ_364 - 通宝 - 浑浊的甲板长迷雾装置
    # 物理暴击率 +20%
    # 魔法暴击率 +20%
    # rarity: 神器
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_365(char: CharacterProperty):
    # DCALC_REMOVE: equ_365 - 通宝 - 侵蚀的甲板长迷雾装置
    # 物理暴击率 +25%
    # 魔法暴击率 +25%
    # rarity: 传说
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_366(char: CharacterProperty):
    # DCALC_REMOVE: equ_366 - 通宝 - 蚕食的甲板长迷雾装置
    # 物理暴击率 +30%
    # 魔法暴击率 +30%
    # rarity: 史诗
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_367(char: CharacterProperty):
    # DCALC_REMOVE: equ_367 - 通宝 - 唤醒自我的咆哮
    # 技能冷却时间25%减少（觉醒技能除外）
    # rarity: 神器
    char.SetSkillCD(1, 100, 0.25)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 2
    pass


@register
def equ_368(char: CharacterProperty):
    # DCALC_REMOVE: equ_368 - 通宝 - 淹没自我的咆哮
    # 技能冷却时间25%减少（觉醒技能除外）
    # rarity: 传说
    char.SetSkillCD(1, 100, 0.25)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 2
    pass


@register
def equ_369(char: CharacterProperty):
    # DCALC_REMOVE: equ_369 - 通宝 - 混淆自我的咆哮
    # 技能冷却时间25%减少（觉醒技能除外）
    # rarity: 史诗
    char.SetSkillCD(1, 100, 0.25)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 2
    pass


@register
def equ_370(char: CharacterProperty):
    # DCALC_REMOVE: equ_370 - 通宝 - 终音弥漫之礼
    # 技能范围 +10%
    # rarity: 神器
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
        char.SetStatus(STR=200, INT=200, Spirit=200, Vitality=200)
    pass


@register
def equ_371(char: CharacterProperty):
    # DCALC_REMOVE: equ_371 - 通宝 - 恸哭弥漫之礼
    # 技能范围 +20%
    # rarity: 传说
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
        char.SetStatus(STR=200, INT=200, Spirit=200, Vitality=200)
    pass


@register
def equ_372(char: CharacterProperty):
    # DCALC_REMOVE: equ_372 - 通宝 - 肃寂弥漫之礼
    # 技能范围 +30%
    # rarity: 史诗
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
        char.SetStatus(STR=200, INT=200, Spirit=200, Vitality=200)
    pass


# endregion
# region 潜影暗袭 套装


@register
def equ_373(char: CharacterProperty):
    # DCALC_REMOVE: equ_373 - 浅淡的潜影暗袭上衣
    # -
    # rarity: 神器
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_374(char: CharacterProperty):
    # DCALC_REMOVE: equ_374 - 灰暗的潜影暗袭上衣
    # 生命值最大值 +5%
    # 魔法值最大值 +5%
    # rarity: 传说
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_375(char: CharacterProperty):
    # DCALC_REMOVE: equ_375 - 浓郁的潜影暗袭上衣
    # 生命值最大值 +15%
    # 魔法值最大值 +15%
    # rarity: 史诗
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_376(char: CharacterProperty):
    # DCALC_REMOVE: equ_376 - 浅淡的潜影融化下装
    # -
    # rarity: 神器
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_377(char: CharacterProperty):
    # DCALC_REMOVE: equ_377 - 灰暗的潜影融化下装
    # 所受物理/魔法伤害 -5%
    # rarity: 传说
    equ_376(char)
    pass


@register
def equ_378(char: CharacterProperty):
    # DCALC_REMOVE: equ_378 - 浓郁的潜影融化下装
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 史诗
    char.SetStatus(SpeedA=0.4, SpeedR=0.4)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_379(char: CharacterProperty):
    # DCALC_REMOVE: equ_379 - 浅淡的潜影抹除之容貌
    # 攻击速度 +35%
    # 施放速度 +35%
    # rarity: 神器
    char.SetStatus(SpeedA=0.35, SpeedR=0.35)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_380(char: CharacterProperty):
    # DCALC_REMOVE: equ_380 - 灰暗的潜影抹除之容貌
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 传说
    char.SetStatus(SpeedA=0.4, SpeedR=0.4)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_381(char: CharacterProperty):
    # DCALC_REMOVE: equ_381 - 浓郁的潜影抹除之容貌
    # 所受物理/魔法伤害 -10%
    # rarity: 史诗
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_382(char: CharacterProperty):
    # DCALC_REMOVE: equ_382 - 浅淡的潜影缔造之腰带
    # 物品栏负重上限 +3kg
    # rarity: 神器
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_383(char: CharacterProperty):
    # DCALC_REMOVE: equ_383 - 灰暗的潜影缔造之腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +20.5%
    # rarity: 传说
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_384(char: CharacterProperty):
    # DCALC_REMOVE: equ_384 - 浓郁的潜影缔造之腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +30.5%
    # rarity: 史诗
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_385(char: CharacterProperty):
    # DCALC_REMOVE: equ_385 - 浅淡的潜影之步伐
    # 移动速度 +39%
    # rarity: 神器
    char.SetStatus(SpeedM=0.39)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_386(char: CharacterProperty):
    # DCALC_REMOVE: equ_386 - 灰暗的潜影之步伐
    # 移动速度 +44%
    # rarity: 传说
    char.SetStatus(SpeedM=0.44)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_387(char: CharacterProperty):
    # DCALC_REMOVE: equ_387 - 浓郁的潜影之步伐
    # 移动速度 +44%
    # rarity: 史诗
    char.SetStatus(SpeedM=0.44)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_388(char: CharacterProperty):
    # DCALC_REMOVE: equ_388 - 浅淡的潜影项链 - 绯
    # 所有属性强化 +40
    # rarity: 神器
    char.AddElementDB('光', 40)
    char.AddElementDB('火', 40)
    char.AddElementDB('冰', 40)
    char.AddElementDB('暗', 40)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_389(char: CharacterProperty):
    # DCALC_REMOVE: equ_389 - 灰暗的潜影项链 - 绯
    # 所有属性强化 +40
    # rarity: 传说
    equ_388(char)
    pass


@register
def equ_390(char: CharacterProperty):
    # DCALC_REMOVE: equ_390 - 浓郁的潜影项链 - 绯
    # 所有属性强化 +40
    # rarity: 史诗
    equ_388(char)
    pass


@register
def equ_391(char: CharacterProperty):
    # DCALC_REMOVE: equ_391 - 深邃的潜影项链 - 绯
    # 所有属性强化 +40
    # rarity: 太初
    equ_388(char)
    pass


@register
def equ_392(char: CharacterProperty):
    # DCALC_REMOVE: equ_392 - 黑牙 : 浓郁的潜影项链 - 绯
    # 所有属性强化 +40
    # rarity: 史诗
    equ_388(char)
    pass


@register
def equ_393(char: CharacterProperty):
    # DCALC_REMOVE: equ_393 - 黑牙 : 深邃的潜影项链 - 绯
    # 所有属性强化 +40
    # rarity: 太初
    equ_388(char)
    pass


@register
def equ_394(char: CharacterProperty):
    # DCALC_REMOVE: equ_394 - 浅淡的潜影手镯 - 火
    # 所有属性强化 +50
    # rarity: 神器
    char.AddElementDB('光', 50)
    char.AddElementDB('火', 50)
    char.AddElementDB('冰', 50)
    char.AddElementDB('暗', 50)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_395(char: CharacterProperty):
    # DCALC_REMOVE: equ_395 - 灰暗的潜影手镯 - 火
    # 所有属性强化 +50
    # rarity: 传说
    equ_394(char)
    pass


@register
def equ_396(char: CharacterProperty):
    # DCALC_REMOVE: equ_396 - 浓郁的潜影手镯 - 火
    # 所有属性强化 +50
    # rarity: 史诗
    equ_394(char)
    pass


@register
def equ_397(char: CharacterProperty):
    # DCALC_REMOVE: equ_397 - 深邃的潜影手镯 - 火
    # 所有属性强化 +50
    # rarity: 太初
    equ_394(char)
    pass


@register
def equ_398(char: CharacterProperty):
    # DCALC_REMOVE: equ_398 - 黑牙 : 浓郁的潜影手镯 - 火
    # 所有属性强化 +50
    # rarity: 史诗
    equ_394(char)
    pass


@register
def equ_399(char: CharacterProperty):
    # DCALC_REMOVE: equ_399 - 黑牙 : 深邃的潜影手镯 - 火
    # 所有属性强化 +50
    # rarity: 太初
    equ_394(char)
    pass


@register
def equ_400(char: CharacterProperty):
    # DCALC_REMOVE: equ_400 - 浅淡的潜影戒指 - 毒
    # 所有属性强化 +40
    # rarity: 神器
    char.AddElementDB('光', 40)
    char.AddElementDB('火', 40)
    char.AddElementDB('冰', 40)
    char.AddElementDB('暗', 40)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_401(char: CharacterProperty):
    # DCALC_REMOVE: equ_401 - 灰暗的潜影戒指 - 毒
    # 所有属性强化 +40
    # rarity: 传说
    equ_400(char)
    pass


@register
def equ_402(char: CharacterProperty):
    # DCALC_REMOVE: equ_402 - 浓郁的潜影戒指 - 毒
    # 所有属性强化 +40
    # rarity: 史诗
    equ_400(char)
    pass


@register
def equ_403(char: CharacterProperty):
    # DCALC_REMOVE: equ_403 - 深邃的潜影戒指 - 毒
    # 所有属性强化 +40
    # rarity: 太初
    equ_400(char)
    pass


@register
def equ_404(char: CharacterProperty):
    # DCALC_REMOVE: equ_404 - 黑牙 : 浓郁的潜影戒指 - 毒
    # 所有属性强化 +40
    # rarity: 史诗
    equ_400(char)
    pass


@register
def equ_405(char: CharacterProperty):
    # DCALC_REMOVE: equ_405 - 黑牙 : 深邃的潜影戒指 - 毒
    # 所有属性强化 +40
    # rarity: 太初
    equ_400(char)
    pass


@register
def equ_406(char: CharacterProperty):
    # DCALC_REMOVE: equ_406 - 浅淡的潜影辅助装备 - 锋
    # 物理暴击率 +20%
    # 魔法暴击率 +20%
    # rarity: 神器
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_407(char: CharacterProperty):
    # DCALC_REMOVE: equ_407 - 灰暗的潜影辅助装备 - 锋
    # 物理暴击率 +25%
    # 魔法暴击率 +25%
    # rarity: 传说
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_408(char: CharacterProperty):
    # DCALC_REMOVE: equ_408 - 浓郁的潜影辅助装备 - 锋
    # 物理暴击率 +30%
    # 魔法暴击率 +30%
    # rarity: 史诗
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


@register
def equ_409(char: CharacterProperty):
    # DCALC_REMOVE: equ_409 - 浅淡的潜影魔法石 - 爆
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 神器
    char.SetSkillCD(1, 100, 0.15)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 2
    pass


@register
def equ_410(char: CharacterProperty):
    # DCALC_REMOVE: equ_410 - 灰暗的潜影魔法石 - 爆
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 传说
    char.SetSkillCD(1, 100, 0.15)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 2
    pass


@register
def equ_411(char: CharacterProperty):
    # DCALC_REMOVE: equ_411 - 浓郁的潜影魔法石 - 爆
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 史诗
    char.SetSkillCD(1, 100, 0.15)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 2
    pass


@register
def equ_412(char: CharacterProperty):
    # DCALC_REMOVE: equ_412 - 浅淡的潜影耳环 - 电
    # -
    # rarity: 神器
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
        char.SetStatus(STR=200, INT=200, Spirit=200, Vitality=200)
    pass


@register
def equ_413(char: CharacterProperty):
    # DCALC_REMOVE: equ_413 - 灰暗的潜影耳环 - 电
    # -
    # rarity: 传说
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
        char.SetStatus(STR=200, INT=200, Spirit=200, Vitality=200)
    pass


@register
def equ_414(char: CharacterProperty):
    # DCALC_REMOVE: equ_414 - 浓郁的潜影耳环 - 电
    # -
    # rarity: 史诗
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
        char.SetStatus(STR=200, INT=200, Spirit=200, Vitality=200)
    pass


# endregion
# region 精灵国度 套装


@register
def equ_415(char: CharacterProperty):
    # DCALC_REMOVE: equ_415 - 初阶精灵上衣
    # -
    # rarity: 神器
    equ_373(char)
    pass


@register
def equ_416(char: CharacterProperty):
    # DCALC_REMOVE: equ_416 - 高阶精灵上衣
    # 生命值最大值 +5%
    # 魔法值最大值 +5%
    # rarity: 传说
    equ_374(char)
    pass


@register
def equ_417(char: CharacterProperty):
    # DCALC_REMOVE: equ_417 - 贵族精灵上衣
    # 生命值最大值 +15%
    # 魔法值最大值 +15%
    # rarity: 史诗
    equ_375(char)
    pass


@register
def equ_418(char: CharacterProperty):
    # DCALC_REMOVE: equ_418 - 低阶精灵下装
    # -
    # rarity: 神器
    equ_376(char)
    pass


@register
def equ_419(char: CharacterProperty):
    # DCALC_REMOVE: equ_419 - 高阶精灵下装
    # 所受物理/魔法伤害 -5%
    # rarity: 传说
    equ_377(char)
    pass


@register
def equ_420(char: CharacterProperty):
    # DCALC_REMOVE: equ_420 - 贵族精灵下装
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 史诗
    equ_378(char)
    pass


@register
def equ_421(char: CharacterProperty):
    # DCALC_REMOVE: equ_421 - 低阶精灵头肩
    # 攻击速度 +35%
    # 施放速度 +35%
    # rarity: 神器
    equ_379(char)
    pass


@register
def equ_422(char: CharacterProperty):
    # DCALC_REMOVE: equ_422 - 高阶精灵头肩
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 传说
    equ_380(char)
    pass


@register
def equ_423(char: CharacterProperty):
    # DCALC_REMOVE: equ_423 - 贵族精灵头肩
    # 所受物理/魔法伤害 -10%
    # rarity: 史诗
    equ_381(char)
    pass


@register
def equ_424(char: CharacterProperty):
    # DCALC_REMOVE: equ_424 - 低阶精灵腰带
    # 物品栏负重上限 +3kg
    # rarity: 神器
    equ_382(char)
    pass


@register
def equ_425(char: CharacterProperty):
    # DCALC_REMOVE: equ_425 - 高阶精灵腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +20.5%
    # rarity: 传说
    equ_383(char)
    pass


@register
def equ_426(char: CharacterProperty):
    # DCALC_REMOVE: equ_426 - 贵族精灵腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +30.5%
    # rarity: 史诗
    equ_384(char)
    pass


@register
def equ_427(char: CharacterProperty):
    # DCALC_REMOVE: equ_427 - 低阶精灵鞋子
    # 移动速度 +39%
    # rarity: 神器
    equ_385(char)
    pass


@register
def equ_428(char: CharacterProperty):
    # DCALC_REMOVE: equ_428 - 高阶精灵鞋子
    # 移动速度 +44%
    # rarity: 传说
    equ_386(char)
    pass


@register
def equ_429(char: CharacterProperty):
    # DCALC_REMOVE: equ_429 - 贵族精灵鞋子
    # 移动速度 +44%
    # rarity: 史诗
    equ_387(char)
    pass


@register
def equ_430(char: CharacterProperty):
    # DCALC_REMOVE: equ_430 - 低阶精灵项链
    # 所有属性强化 +40
    # rarity: 神器
    equ_388(char)
    pass


@register
def equ_431(char: CharacterProperty):
    # DCALC_REMOVE: equ_431 - 高阶精灵项链
    # 所有属性强化 +40
    # rarity: 传说
    equ_389(char)
    pass


@register
def equ_432(char: CharacterProperty):
    # DCALC_REMOVE: equ_432 - 贵族精灵项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_390(char)
    pass


@register
def equ_433(char: CharacterProperty):
    # DCALC_REMOVE: equ_433 - 皇室精灵项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_391(char)
    pass


@register
def equ_434(char: CharacterProperty):
    # DCALC_REMOVE: equ_434 - 黑牙 : 贵族精灵项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_392(char)
    pass


@register
def equ_435(char: CharacterProperty):
    # DCALC_REMOVE: equ_435 - 黑牙 : 皇室精灵项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_393(char)
    pass


@register
def equ_436(char: CharacterProperty):
    # DCALC_REMOVE: equ_436 - 低阶精灵手镯
    # 所有属性强化 +50
    # rarity: 神器
    equ_394(char)
    pass


@register
def equ_437(char: CharacterProperty):
    # DCALC_REMOVE: equ_437 - 高阶精灵手镯
    # 所有属性强化 +50
    # rarity: 传说
    equ_395(char)
    pass


@register
def equ_438(char: CharacterProperty):
    # DCALC_REMOVE: equ_438 - 贵族精灵手镯
    # 所有属性强化 +50
    # rarity: 史诗
    equ_396(char)
    pass


@register
def equ_439(char: CharacterProperty):
    # DCALC_REMOVE: equ_439 - 皇室精灵手镯
    # 所有属性强化 +50
    # rarity: 太初
    equ_397(char)
    pass


@register
def equ_440(char: CharacterProperty):
    # DCALC_REMOVE: equ_440 - 黑牙 : 贵族精灵手镯
    # 所有属性强化 +50
    # rarity: 史诗
    equ_398(char)
    pass


@register
def equ_441(char: CharacterProperty):
    # DCALC_REMOVE: equ_441 - 黑牙 : 皇室精灵手镯
    # 所有属性强化 +50
    # rarity: 太初
    equ_399(char)
    pass


@register
def equ_442(char: CharacterProperty):
    # DCALC_REMOVE: equ_442 - 低阶精灵戒指
    # 所有属性强化 +40
    # rarity: 神器
    equ_400(char)
    pass


@register
def equ_443(char: CharacterProperty):
    # DCALC_REMOVE: equ_443 - 高阶精灵戒指
    # 所有属性强化 +40
    # rarity: 传说
    equ_401(char)
    pass


@register
def equ_444(char: CharacterProperty):
    # DCALC_REMOVE: equ_444 - 贵族精灵戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_402(char)
    pass


@register
def equ_445(char: CharacterProperty):
    # DCALC_REMOVE: equ_445 - 皇室精灵戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_403(char)
    pass


@register
def equ_446(char: CharacterProperty):
    # DCALC_REMOVE: equ_446 - 黑牙 : 贵族精灵戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_404(char)
    pass


@register
def equ_447(char: CharacterProperty):
    # DCALC_REMOVE: equ_447 - 黑牙 : 皇室精灵戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_405(char)
    pass


@register
def equ_448(char: CharacterProperty):
    # DCALC_REMOVE: equ_448 - 低阶精灵辅助装备
    # 物理暴击率 +20%
    # 魔法暴击率 +20%
    # rarity: 神器
    equ_406(char)
    pass


@register
def equ_449(char: CharacterProperty):
    # DCALC_REMOVE: equ_449 - 高阶精灵辅助装备
    # 物理暴击率 +25%
    # 魔法暴击率 +25%
    # rarity: 传说
    equ_407(char)
    pass


@register
def equ_450(char: CharacterProperty):
    # DCALC_REMOVE: equ_450 - 贵族精灵辅助装备
    # 物理暴击率 +30%
    # 魔法暴击率 +30%
    # rarity: 史诗
    equ_408(char)
    pass


@register
def equ_451(char: CharacterProperty):
    # DCALC_REMOVE: equ_451 - 低阶精灵魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 神器
    equ_409(char)
    pass


@register
def equ_452(char: CharacterProperty):
    # DCALC_REMOVE: equ_452 - 高阶精灵魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 传说
    equ_410(char)
    pass


@register
def equ_453(char: CharacterProperty):
    # DCALC_REMOVE: equ_453 - 贵族精灵魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 史诗
    equ_411(char)
    pass


@register
def equ_454(char: CharacterProperty):
    # DCALC_REMOVE: equ_454 - 低阶精灵耳环
    # -
    # rarity: 神器
    equ_412(char)
    pass


@register
def equ_455(char: CharacterProperty):
    # DCALC_REMOVE: equ_455 - 高阶精灵耳环
    # -
    # rarity: 传说
    equ_413(char)
    pass


@register
def equ_456(char: CharacterProperty):
    # DCALC_REMOVE: equ_456 - 贵族精灵耳环
    # -
    # rarity: 史诗
    equ_414(char)
    pass


# endregion
# region 理想之黄金乡 套装


@register
def equ_457(char: CharacterProperty):
    # DCALC_REMOVE: equ_457 - 闪耀的黄金乡胸甲
    # -
    # rarity: 神器
    equ_373(char)
    pass


@register
def equ_458(char: CharacterProperty):
    # DCALC_REMOVE: equ_458 - 华丽的黄金乡胸甲
    # 生命值最大值 +5%
    # 魔法值最大值 +5%
    # rarity: 传说
    equ_374(char)
    pass


@register
def equ_459(char: CharacterProperty):
    # DCALC_REMOVE: equ_459 - 灿烂的黄金乡胸甲
    # 生命值最大值 +15%
    # 魔法值最大值 +15%
    # rarity: 史诗
    equ_375(char)
    pass


@register
def equ_460(char: CharacterProperty):
    # DCALC_REMOVE: equ_460 - 闪耀的黄金乡腿甲
    # -
    # rarity: 神器
    equ_376(char)
    pass


@register
def equ_461(char: CharacterProperty):
    # DCALC_REMOVE: equ_461 - 华丽的黄金乡腿甲
    # 所受物理/魔法伤害 -5%
    # rarity: 传说
    equ_377(char)
    pass


@register
def equ_462(char: CharacterProperty):
    # DCALC_REMOVE: equ_462 - 灿烂的黄金乡腿甲
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 史诗
    equ_378(char)
    pass


@register
def equ_463(char: CharacterProperty):
    # DCALC_REMOVE: equ_463 - 闪耀的黄金乡肩甲
    # 攻击速度 +35%
    # 施放速度 +35%
    # rarity: 神器
    equ_379(char)
    pass


@register
def equ_464(char: CharacterProperty):
    # DCALC_REMOVE: equ_464 - 华丽的黄金乡肩甲
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 传说
    equ_380(char)
    pass


@register
def equ_465(char: CharacterProperty):
    # DCALC_REMOVE: equ_465 - 灿烂的黄金乡肩甲
    # 所受物理/魔法伤害 -10%
    # rarity: 史诗
    equ_381(char)
    pass


@register
def equ_466(char: CharacterProperty):
    # DCALC_REMOVE: equ_466 - 闪耀的黄金乡腰带
    # 物品栏负重上限 +3kg
    # rarity: 神器
    equ_382(char)
    pass


@register
def equ_467(char: CharacterProperty):
    # DCALC_REMOVE: equ_467 - 华丽的黄金乡腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +20.5%
    # rarity: 传说
    equ_383(char)
    pass


@register
def equ_468(char: CharacterProperty):
    # DCALC_REMOVE: equ_468 - 灿烂的黄金乡腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +30.5%
    # rarity: 史诗
    equ_384(char)
    pass


@register
def equ_469(char: CharacterProperty):
    # DCALC_REMOVE: equ_469 - 闪耀的黄金乡靴子
    # 移动速度 +39%
    # rarity: 神器
    equ_385(char)
    pass


@register
def equ_470(char: CharacterProperty):
    # DCALC_REMOVE: equ_470 - 华丽的黄金乡靴子
    # 移动速度 +44%
    # rarity: 传说
    equ_386(char)
    pass


@register
def equ_471(char: CharacterProperty):
    # DCALC_REMOVE: equ_471 - 灿烂的黄金乡靴子
    # 移动速度 +44%
    # rarity: 史诗
    equ_387(char)
    pass


@register
def equ_472(char: CharacterProperty):
    # DCALC_REMOVE: equ_472 - 闪耀的黄金乡祝福 - 项链
    # 所有属性强化 +40
    # rarity: 神器
    equ_388(char)
    pass


@register
def equ_473(char: CharacterProperty):
    # DCALC_REMOVE: equ_473 - 华丽的黄金乡祝福 - 项链
    # 所有属性强化 +40
    # rarity: 传说
    equ_389(char)
    pass


@register
def equ_474(char: CharacterProperty):
    # DCALC_REMOVE: equ_474 - 灿烂的黄金乡祝福 - 项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_390(char)
    pass


@register
def equ_475(char: CharacterProperty):
    # DCALC_REMOVE: equ_475 - 玲珑的黄金乡祝福 - 项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_391(char)
    pass


@register
def equ_476(char: CharacterProperty):
    # DCALC_REMOVE: equ_476 - 黑牙 : 灿烂的黄金乡祝福 - 项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_392(char)
    pass


@register
def equ_477(char: CharacterProperty):
    # DCALC_REMOVE: equ_477 - 黑牙 : 玲珑的黄金乡祝福 - 项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_393(char)
    pass


@register
def equ_478(char: CharacterProperty):
    # DCALC_REMOVE: equ_478 - 闪耀的黄金乡荣耀 - 手镯
    # 所有属性强化 +50
    # rarity: 神器
    equ_394(char)
    pass


@register
def equ_479(char: CharacterProperty):
    # DCALC_REMOVE: equ_479 - 华丽的黄金乡荣耀 - 手镯
    # 所有属性强化 +50
    # rarity: 传说
    equ_395(char)
    pass


@register
def equ_480(char: CharacterProperty):
    # DCALC_REMOVE: equ_480 - 灿烂的黄金乡荣耀 - 手镯
    # 所有属性强化 +50
    # rarity: 史诗
    equ_396(char)
    pass


@register
def equ_481(char: CharacterProperty):
    # DCALC_REMOVE: equ_481 - 玲珑的黄金乡荣耀 - 手镯
    # 所有属性强化 +50
    # rarity: 太初
    equ_397(char)
    pass


@register
def equ_482(char: CharacterProperty):
    # DCALC_REMOVE: equ_482 - 黑牙 : 灿烂的黄金乡荣耀 - 手镯
    # 所有属性强化 +50
    # rarity: 史诗
    equ_398(char)
    pass


@register
def equ_483(char: CharacterProperty):
    # DCALC_REMOVE: equ_483 - 黑牙 : 玲珑的黄金乡荣耀 - 手镯
    # 所有属性强化 +50
    # rarity: 太初
    equ_399(char)
    pass


@register
def equ_484(char: CharacterProperty):
    # DCALC_REMOVE: equ_484 - 闪耀的黄金乡之梦 - 戒指
    # 所有属性强化 +40
    # rarity: 神器
    equ_400(char)
    pass


@register
def equ_485(char: CharacterProperty):
    # DCALC_REMOVE: equ_485 - 华丽的黄金乡之梦 - 戒指
    # 所有属性强化 +40
    # rarity: 传说
    equ_401(char)
    pass


@register
def equ_486(char: CharacterProperty):
    # DCALC_REMOVE: equ_486 - 灿烂的黄金乡之梦 - 戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_402(char)
    pass


@register
def equ_487(char: CharacterProperty):
    # DCALC_REMOVE: equ_487 - 玲珑的黄金乡之梦 - 戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_403(char)
    pass


@register
def equ_488(char: CharacterProperty):
    # DCALC_REMOVE: equ_488 - 黑牙 : 灿烂的黄金乡之梦 - 戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_404(char)
    pass


@register
def equ_489(char: CharacterProperty):
    # DCALC_REMOVE: equ_489 - 黑牙 : 玲珑的黄金乡之梦 - 戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_405(char)
    pass


@register
def equ_490(char: CharacterProperty):
    # DCALC_REMOVE: equ_490 - 闪耀的黄金乡执念 - 辅助装备
    # 物理暴击率 +20%
    # 魔法暴击率 +20%
    # rarity: 神器
    equ_406(char)
    pass


@register
def equ_491(char: CharacterProperty):
    # DCALC_REMOVE: equ_491 - 华丽的黄金乡执念 - 辅助装备
    # 物理暴击率 +25%
    # 魔法暴击率 +25%
    # rarity: 传说
    equ_407(char)
    pass


@register
def equ_492(char: CharacterProperty):
    # DCALC_REMOVE: equ_492 - 灿烂的黄金乡执念 - 辅助装备
    # 物理暴击率 +30%
    # 魔法暴击率 +30%
    # rarity: 史诗
    equ_408(char)
    pass


@register
def equ_493(char: CharacterProperty):
    # DCALC_REMOVE: equ_493 - 闪耀的黄金乡诅咒 - 魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 神器
    equ_409(char)
    pass


@register
def equ_494(char: CharacterProperty):
    # DCALC_REMOVE: equ_494 - 华丽的黄金乡诅咒 - 魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 传说
    equ_410(char)
    pass


@register
def equ_495(char: CharacterProperty):
    # DCALC_REMOVE: equ_495 - 灿烂的黄金乡诅咒 - 魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 史诗
    equ_411(char)
    pass


@register
def equ_496(char: CharacterProperty):
    # DCALC_REMOVE: equ_496 - 闪耀的黄金乡异面 - 耳环
    # -
    # rarity: 神器
    equ_412(char)
    pass


@register
def equ_497(char: CharacterProperty):
    # DCALC_REMOVE: equ_497 - 华丽的黄金乡异面 - 耳环
    # -
    # rarity: 传说
    equ_413(char)
    pass


@register
def equ_498(char: CharacterProperty):
    # DCALC_REMOVE: equ_498 - 灿烂的黄金乡异面 - 耳环
    # -
    # rarity: 史诗
    equ_414(char)
    pass


# endregion
# region 龙战八荒 套装


@register
def equ_499(char: CharacterProperty):
    # DCALC_REMOVE: equ_499 - 虬龙的喷火甲胄
    # -
    # rarity: 神器
    equ_373(char)
    pass


@register
def equ_500(char: CharacterProperty):
    # DCALC_REMOVE: equ_500 - 蛟龙的喷火甲胄
    # 生命值最大值 +5%
    # 魔法值最大值 +5%
    # rarity: 传说
    equ_374(char)
    pass


@register
def equ_501(char: CharacterProperty):
    # DCALC_REMOVE: equ_501 - 烛龙的喷火甲胄
    # 生命值最大值 +15%
    # 魔法值最大值 +15%
    # rarity: 史诗
    equ_375(char)
    pass


@register
def equ_502(char: CharacterProperty):
    # DCALC_REMOVE: equ_502 - 虬龙的惊雷绑腿
    # -
    # rarity: 神器
    equ_376(char)
    pass


@register
def equ_503(char: CharacterProperty):
    # DCALC_REMOVE: equ_503 - 蛟龙的惊雷绑腿
    # 所受物理/魔法伤害 -5%
    # rarity: 传说
    equ_377(char)
    pass


@register
def equ_504(char: CharacterProperty):
    # DCALC_REMOVE: equ_504 - 烛龙的惊雷绑腿
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 史诗
    equ_378(char)
    pass


@register
def equ_505(char: CharacterProperty):
    # DCALC_REMOVE: equ_505 - 虬龙的逐风肩甲
    # 攻击速度 +35%
    # 施放速度 +35%
    # rarity: 神器
    equ_379(char)
    pass


@register
def equ_506(char: CharacterProperty):
    # DCALC_REMOVE: equ_506 - 蛟龙的逐风肩甲
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 传说
    equ_380(char)
    pass


@register
def equ_507(char: CharacterProperty):
    # DCALC_REMOVE: equ_507 - 烛龙的逐风肩甲
    # 所受物理/魔法伤害 -10%
    # rarity: 史诗
    equ_381(char)
    pass


@register
def equ_508(char: CharacterProperty):
    # DCALC_REMOVE: equ_508 - 虬龙的辟地腰带
    # 物品栏负重上限 +3kg
    # rarity: 神器
    equ_382(char)
    pass


@register
def equ_509(char: CharacterProperty):
    # DCALC_REMOVE: equ_509 - 蛟龙的辟地腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +20.5%
    # rarity: 传说
    equ_383(char)
    pass


@register
def equ_510(char: CharacterProperty):
    # DCALC_REMOVE: equ_510 - 烛龙的辟地腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +30.5%
    # rarity: 史诗
    equ_384(char)
    pass


@register
def equ_511(char: CharacterProperty):
    # DCALC_REMOVE: equ_511 - 虬龙的开天利爪
    # 移动速度 +39%
    # rarity: 神器
    equ_385(char)
    pass


@register
def equ_512(char: CharacterProperty):
    # DCALC_REMOVE: equ_512 - 蛟龙的开天利爪
    # 移动速度 +44%
    # rarity: 传说
    equ_386(char)
    pass


@register
def equ_513(char: CharacterProperty):
    # DCALC_REMOVE: equ_513 - 烛龙的开天利爪
    # 移动速度 +44%
    # rarity: 史诗
    equ_387(char)
    pass


@register
def equ_514(char: CharacterProperty):
    # DCALC_REMOVE: equ_514 - 虬龙的威慑咆哮
    # 所有属性强化 +40
    # rarity: 神器
    equ_388(char)
    pass


@register
def equ_515(char: CharacterProperty):
    # DCALC_REMOVE: equ_515 - 蛟龙的威慑咆哮
    # 所有属性强化 +40
    # rarity: 传说
    equ_389(char)
    pass


@register
def equ_516(char: CharacterProperty):
    # DCALC_REMOVE: equ_516 - 烛龙的威慑咆哮
    # 所有属性强化 +40
    # rarity: 史诗
    equ_390(char)
    pass


@register
def equ_517(char: CharacterProperty):
    # DCALC_REMOVE: equ_517 - 应龙的威慑咆哮
    # 所有属性强化 +40
    # rarity: 太初
    equ_391(char)
    pass


@register
def equ_518(char: CharacterProperty):
    # DCALC_REMOVE: equ_518 - 黑牙 : 烛龙的威慑咆哮
    # 所有属性强化 +40
    # rarity: 史诗
    equ_392(char)
    pass


@register
def equ_519(char: CharacterProperty):
    # DCALC_REMOVE: equ_519 - 黑牙 : 应龙的威慑咆哮
    # 所有属性强化 +40
    # rarity: 太初
    equ_393(char)
    pass


@register
def equ_520(char: CharacterProperty):
    # DCALC_REMOVE: equ_520 - 虬龙的染痕凶牙
    # 所有属性强化 +50
    # rarity: 神器
    equ_394(char)
    pass


@register
def equ_521(char: CharacterProperty):
    # DCALC_REMOVE: equ_521 - 蛟龙的染痕凶牙
    # 所有属性强化 +50
    # rarity: 传说
    equ_395(char)
    pass


@register
def equ_522(char: CharacterProperty):
    # DCALC_REMOVE: equ_522 - 烛龙的染痕凶牙
    # 所有属性强化 +50
    # rarity: 史诗
    equ_396(char)
    pass


@register
def equ_523(char: CharacterProperty):
    # DCALC_REMOVE: equ_523 - 应龙的染痕凶牙
    # 所有属性强化 +50
    # rarity: 太初
    equ_397(char)
    pass


@register
def equ_524(char: CharacterProperty):
    # DCALC_REMOVE: equ_524 - 黑牙 : 烛龙的染痕凶牙
    # 所有属性强化 +50
    # rarity: 史诗
    equ_398(char)
    pass


@register
def equ_525(char: CharacterProperty):
    # DCALC_REMOVE: equ_525 - 黑牙 : 应龙的染痕凶牙
    # 所有属性强化 +50
    # rarity: 太初
    equ_399(char)
    pass


@register
def equ_526(char: CharacterProperty):
    # DCALC_REMOVE: equ_526 - 虬龙的避祸锐鳞
    # 所有属性强化 +40
    # rarity: 神器
    equ_400(char)
    pass


@register
def equ_527(char: CharacterProperty):
    # DCALC_REMOVE: equ_527 - 蛟龙的避祸锐鳞
    # 所有属性强化 +40
    # rarity: 传说
    equ_401(char)
    pass


@register
def equ_528(char: CharacterProperty):
    # DCALC_REMOVE: equ_528 - 烛龙的避祸锐鳞
    # 所有属性强化 +40
    # rarity: 史诗
    equ_402(char)
    pass


@register
def equ_529(char: CharacterProperty):
    # DCALC_REMOVE: equ_529 - 应龙的避祸锐鳞
    # 所有属性强化 +40
    # rarity: 太初
    equ_403(char)
    pass


@register
def equ_530(char: CharacterProperty):
    # DCALC_REMOVE: equ_530 - 黑牙 : 烛龙的避祸锐鳞
    # 所有属性强化 +40
    # rarity: 史诗
    equ_404(char)
    pass


@register
def equ_531(char: CharacterProperty):
    # DCALC_REMOVE: equ_531 - 黑牙 : 应龙的避祸锐鳞
    # 所有属性强化 +40
    # rarity: 太初
    equ_405(char)
    pass


@register
def equ_532(char: CharacterProperty):
    # DCALC_REMOVE: equ_532 - 虬龙的隐秘逆鳞
    # 物理暴击率 +20%
    # 魔法暴击率 +20%
    # rarity: 神器
    equ_406(char)
    pass


@register
def equ_533(char: CharacterProperty):
    # DCALC_REMOVE: equ_533 - 蛟龙的隐秘逆鳞
    # 物理暴击率 +25%
    # 魔法暴击率 +25%
    # rarity: 传说
    equ_407(char)
    pass


@register
def equ_534(char: CharacterProperty):
    # DCALC_REMOVE: equ_534 - 烛龙的隐秘逆鳞
    # 物理暴击率 +30%
    # 魔法暴击率 +30%
    # rarity: 史诗
    equ_408(char)
    pass


@register
def equ_535(char: CharacterProperty):
    # DCALC_REMOVE: equ_535 - 虬龙的玲珑如意珠
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 神器
    equ_409(char)
    pass


@register
def equ_536(char: CharacterProperty):
    # DCALC_REMOVE: equ_536 - 蛟龙的玲珑如意珠
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 传说
    equ_410(char)
    pass


@register
def equ_537(char: CharacterProperty):
    # DCALC_REMOVE: equ_537 - 烛龙的玲珑如意珠
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 史诗
    equ_411(char)
    pass


@register
def equ_538(char: CharacterProperty):
    # DCALC_REMOVE: equ_538 - 虬龙的耸立威角
    # -
    # rarity: 神器
    equ_412(char)
    pass


@register
def equ_539(char: CharacterProperty):
    # DCALC_REMOVE: equ_539 - 蛟龙的耸立威角
    # -
    # rarity: 传说
    equ_413(char)
    pass


@register
def equ_540(char: CharacterProperty):
    # DCALC_REMOVE: equ_540 - 烛龙的耸立威角
    # -
    # rarity: 史诗
    equ_414(char)
    pass


# endregion
# region 混沌净化 套装


@register
def equ_541(char: CharacterProperty):
    # DCALC_REMOVE: equ_541 - 纯洁净化上衣
    # -
    # rarity: 神器
    equ_373(char)
    pass


@register
def equ_542(char: CharacterProperty):
    # DCALC_REMOVE: equ_542 - 无瑕净化上衣
    # 生命值最大值 +5%
    # 魔法值最大值 +5%
    # rarity: 传说
    equ_374(char)
    pass


@register
def equ_543(char: CharacterProperty):
    # DCALC_REMOVE: equ_543 - 澄澈净化上衣
    # 生命值最大值 +15%
    # 魔法值最大值 +15%
    # rarity: 史诗
    equ_375(char)
    pass


@register
def equ_544(char: CharacterProperty):
    # DCALC_REMOVE: equ_544 - 纯洁净化下装
    # -
    # rarity: 神器
    equ_376(char)
    pass


@register
def equ_545(char: CharacterProperty):
    # DCALC_REMOVE: equ_545 - 无瑕净化下装
    # 所受物理/魔法伤害 -5%
    # rarity: 传说
    equ_377(char)
    pass


@register
def equ_546(char: CharacterProperty):
    # DCALC_REMOVE: equ_546 - 澄澈净化下装
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 史诗
    equ_378(char)
    pass


@register
def equ_547(char: CharacterProperty):
    # DCALC_REMOVE: equ_547 - 纯洁净化头肩
    # 攻击速度 +35%
    # 施放速度 +35%
    # rarity: 神器
    equ_379(char)
    pass


@register
def equ_548(char: CharacterProperty):
    # DCALC_REMOVE: equ_548 - 无瑕净化头肩
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 传说
    equ_380(char)
    pass


@register
def equ_549(char: CharacterProperty):
    # DCALC_REMOVE: equ_549 - 澄澈净化护肩
    # 所受物理/魔法伤害 -10%
    # rarity: 史诗
    equ_381(char)
    pass


@register
def equ_550(char: CharacterProperty):
    # DCALC_REMOVE: equ_550 - 纯洁净化腰带
    # 物品栏负重上限 +3kg
    # rarity: 神器
    equ_382(char)
    pass


@register
def equ_551(char: CharacterProperty):
    # DCALC_REMOVE: equ_551 - 无瑕净化腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +20.5%
    # rarity: 传说
    equ_383(char)
    pass


@register
def equ_552(char: CharacterProperty):
    # DCALC_REMOVE: equ_552 - 澄澈净化腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +30.5%
    # rarity: 史诗
    equ_384(char)
    pass


@register
def equ_553(char: CharacterProperty):
    # DCALC_REMOVE: equ_553 - 纯洁净化鞋子
    # 移动速度 +39%
    # rarity: 神器
    equ_385(char)
    pass


@register
def equ_554(char: CharacterProperty):
    # DCALC_REMOVE: equ_554 - 无瑕净化鞋子
    # 移动速度 +44%
    # rarity: 传说
    equ_386(char)
    pass


@register
def equ_555(char: CharacterProperty):
    # DCALC_REMOVE: equ_555 - 澄澈净化鞋子
    # 移动速度 +44%
    # rarity: 史诗
    equ_387(char)
    pass


@register
def equ_556(char: CharacterProperty):
    # DCALC_REMOVE: equ_556 - 淡黑净化项链
    # 所有属性强化 +40
    # rarity: 神器
    equ_388(char)
    pass


@register
def equ_557(char: CharacterProperty):
    # DCALC_REMOVE: equ_557 - 深黑净化项链
    # 所有属性强化 +40
    # rarity: 传说
    equ_389(char)
    pass


@register
def equ_558(char: CharacterProperty):
    # DCALC_REMOVE: equ_558 - 暗黑净化项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_390(char)
    pass


@register
def equ_559(char: CharacterProperty):
    # DCALC_REMOVE: equ_559 - 混沌净化项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_391(char)
    pass


@register
def equ_560(char: CharacterProperty):
    # DCALC_REMOVE: equ_560 - 黑牙 : 暗黑净化项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_392(char)
    pass


@register
def equ_561(char: CharacterProperty):
    # DCALC_REMOVE: equ_561 - 黑牙 : 混沌净化项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_393(char)
    pass


@register
def equ_562(char: CharacterProperty):
    # DCALC_REMOVE: equ_562 - 淡黑净化手镯
    # 所有属性强化 +50
    # rarity: 神器
    equ_394(char)
    pass


@register
def equ_563(char: CharacterProperty):
    # DCALC_REMOVE: equ_563 - 深黑净化手镯
    # 所有属性强化 +50
    # rarity: 传说
    equ_395(char)
    pass


@register
def equ_564(char: CharacterProperty):
    # DCALC_REMOVE: equ_564 - 暗黑净化手镯
    # 所有属性强化 +50
    # rarity: 史诗
    equ_396(char)
    pass


@register
def equ_565(char: CharacterProperty):
    # DCALC_REMOVE: equ_565 - 混沌净化手镯
    # 所有属性强化 +50
    # rarity: 太初
    equ_397(char)
    pass


@register
def equ_566(char: CharacterProperty):
    # DCALC_REMOVE: equ_566 - 黑牙 : 暗黑净化手镯
    # 所有属性强化 +50
    # rarity: 史诗
    equ_398(char)
    pass


@register
def equ_567(char: CharacterProperty):
    # DCALC_REMOVE: equ_567 - 黑牙 : 混沌净化手镯
    # 所有属性强化 +50
    # rarity: 太初
    equ_399(char)
    pass


@register
def equ_568(char: CharacterProperty):
    # DCALC_REMOVE: equ_568 - 淡黑净化戒指
    # 所有属性强化 +40
    # rarity: 神器
    equ_400(char)
    pass


@register
def equ_569(char: CharacterProperty):
    # DCALC_REMOVE: equ_569 - 深黑净化戒指
    # 所有属性强化 +40
    # rarity: 传说
    equ_401(char)
    pass


@register
def equ_570(char: CharacterProperty):
    # DCALC_REMOVE: equ_570 - 暗黑净化戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_402(char)
    pass


@register
def equ_571(char: CharacterProperty):
    # DCALC_REMOVE: equ_571 - 混沌净化戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_403(char)
    pass


@register
def equ_572(char: CharacterProperty):
    # DCALC_REMOVE: equ_572 - 黑牙 : 暗黑净化戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_404(char)
    pass


@register
def equ_573(char: CharacterProperty):
    # DCALC_REMOVE: equ_573 - 黑牙 : 混沌净化戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_405(char)
    pass


@register
def equ_574(char: CharacterProperty):
    # DCALC_REMOVE: equ_574 - 淡黑净化辅助装备
    # 物理暴击率 +20%
    # 魔法暴击率 +20%
    # rarity: 神器
    equ_406(char)
    pass


@register
def equ_575(char: CharacterProperty):
    # DCALC_REMOVE: equ_575 - 深黑净化辅助装备
    # 物理暴击率 +25%
    # 魔法暴击率 +25%
    # rarity: 传说
    equ_407(char)
    pass


@register
def equ_576(char: CharacterProperty):
    # DCALC_REMOVE: equ_576 - 暗黑净化辅助装备
    # 物理暴击率 +30%
    # 魔法暴击率 +30%
    # rarity: 史诗
    equ_408(char)
    pass


@register
def equ_577(char: CharacterProperty):
    # DCALC_REMOVE: equ_577 - 淡黑净化魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 神器
    equ_409(char)
    pass


@register
def equ_578(char: CharacterProperty):
    # DCALC_REMOVE: equ_578 - 深黑净化魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 传说
    equ_410(char)
    pass


@register
def equ_579(char: CharacterProperty):
    # DCALC_REMOVE: equ_579 - 暗黑净化魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 史诗
    equ_411(char)
    pass


@register
def equ_580(char: CharacterProperty):
    # DCALC_REMOVE: equ_580 - 淡黑净化耳环
    # -
    # rarity: 神器
    equ_412(char)
    pass


@register
def equ_581(char: CharacterProperty):
    # DCALC_REMOVE: equ_581 - 深黑净化耳环
    # -
    # rarity: 传说
    equ_413(char)
    pass


@register
def equ_582(char: CharacterProperty):
    # DCALC_REMOVE: equ_582 - 暗黑净化耳环
    # -
    # rarity: 史诗
    equ_414(char)
    pass


# endregion
# region 天命者的气运 套装


@register
def equ_583(char: CharacterProperty):
    # DCALC_REMOVE: equ_583 - 强固之天命气运夹克
    # -
    # rarity: 神器
    equ_373(char)
    pass


@register
def equ_584(char: CharacterProperty):
    # DCALC_REMOVE: equ_584 - 坚固之天命气运夹克
    # 生命值最大值 +5%
    # 魔法值最大值 +5%
    # rarity: 传说
    equ_374(char)
    pass


@register
def equ_585(char: CharacterProperty):
    # DCALC_REMOVE: equ_585 - 坚实之天命气运夹克
    # 生命值最大值 +15%
    # 魔法值最大值 +15%
    # rarity: 史诗
    equ_375(char)
    pass


@register
def equ_586(char: CharacterProperty):
    # DCALC_REMOVE: equ_586 - 强固之天命气运裤子
    # -
    # rarity: 神器
    equ_376(char)
    pass


@register
def equ_587(char: CharacterProperty):
    # DCALC_REMOVE: equ_587 - 坚固之天命气运裤子
    # 所受物理/魔法伤害 -5%
    # rarity: 传说
    equ_377(char)
    pass


@register
def equ_588(char: CharacterProperty):
    # DCALC_REMOVE: equ_588 - 坚实之天命气运裤子
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 史诗
    equ_378(char)
    pass


@register
def equ_589(char: CharacterProperty):
    # DCALC_REMOVE: equ_589 - 强固之天命气运肩章
    # 攻击速度 +35%
    # 施放速度 +35%
    # rarity: 神器
    equ_379(char)
    pass


@register
def equ_590(char: CharacterProperty):
    # DCALC_REMOVE: equ_590 - 坚固之天命气运肩章
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 传说
    equ_380(char)
    pass


@register
def equ_591(char: CharacterProperty):
    # DCALC_REMOVE: equ_591 - 坚实之天命气运肩章
    # 所受物理/魔法伤害 -10%
    # rarity: 史诗
    equ_381(char)
    pass


@register
def equ_592(char: CharacterProperty):
    # DCALC_REMOVE: equ_592 - 强固之天命气运腰带
    # 物品栏负重上限 +3kg
    # rarity: 神器
    equ_382(char)
    pass


@register
def equ_593(char: CharacterProperty):
    # DCALC_REMOVE: equ_593 - 坚固之天命气运腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +20.5%
    # rarity: 传说
    equ_383(char)
    pass


@register
def equ_594(char: CharacterProperty):
    # DCALC_REMOVE: equ_594 - 坚实之天命气运腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +30.5%
    # rarity: 史诗
    equ_384(char)
    pass


@register
def equ_595(char: CharacterProperty):
    # DCALC_REMOVE: equ_595 - 强固之天命气运靴子
    # 移动速度 +39%
    # rarity: 神器
    equ_385(char)
    pass


@register
def equ_596(char: CharacterProperty):
    # DCALC_REMOVE: equ_596 - 坚固之天命气运靴子
    # 移动速度 +44%
    # rarity: 传说
    equ_386(char)
    pass


@register
def equ_597(char: CharacterProperty):
    # DCALC_REMOVE: equ_597 - 坚实之天命气运靴子
    # 移动速度 +44%
    # rarity: 史诗
    equ_387(char)
    pass


@register
def equ_598(char: CharacterProperty):
    # DCALC_REMOVE: equ_598 - 强固之鸿运当头项链
    # 所有属性强化 +40
    # rarity: 神器
    equ_388(char)
    pass


@register
def equ_599(char: CharacterProperty):
    # DCALC_REMOVE: equ_599 - 坚固之鸿运当头项链
    # 所有属性强化 +40
    # rarity: 传说
    equ_389(char)
    pass


@register
def equ_600(char: CharacterProperty):
    # DCALC_REMOVE: equ_600 - 坚实之鸿运当头项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_390(char)
    pass


@register
def equ_601(char: CharacterProperty):
    # DCALC_REMOVE: equ_601 - 坚韧之鸿运当头项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_391(char)
    pass


@register
def equ_602(char: CharacterProperty):
    # DCALC_REMOVE: equ_602 - 黑牙 : 坚实之鸿运当头项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_392(char)
    pass


@register
def equ_603(char: CharacterProperty):
    # DCALC_REMOVE: equ_603 - 黑牙 : 坚韧之鸿运当头项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_393(char)
    pass


@register
def equ_604(char: CharacterProperty):
    # DCALC_REMOVE: equ_604 - 强固之鸿运当头手镯
    # 所有属性强化 +50
    # rarity: 神器
    equ_394(char)
    pass


@register
def equ_605(char: CharacterProperty):
    # DCALC_REMOVE: equ_605 - 坚固之鸿运当头手镯
    # 所有属性强化 +50
    # rarity: 传说
    equ_395(char)
    pass


@register
def equ_606(char: CharacterProperty):
    # DCALC_REMOVE: equ_606 - 坚实之鸿运当头手镯
    # 所有属性强化 +50
    # rarity: 史诗
    equ_396(char)
    pass


@register
def equ_607(char: CharacterProperty):
    # DCALC_REMOVE: equ_607 - 坚韧之鸿运当头手镯
    # 所有属性强化 +50
    # rarity: 太初
    equ_397(char)
    pass


@register
def equ_608(char: CharacterProperty):
    # DCALC_REMOVE: equ_608 - 黑牙 : 坚实之鸿运当头手镯
    # 所有属性强化 +50
    # rarity: 史诗
    equ_398(char)
    pass


@register
def equ_609(char: CharacterProperty):
    # DCALC_REMOVE: equ_609 - 黑牙 : 坚韧之鸿运当头手镯
    # 所有属性强化 +50
    # rarity: 太初
    equ_399(char)
    pass


@register
def equ_610(char: CharacterProperty):
    # DCALC_REMOVE: equ_610 - 强固之鸿运当头戒指
    # 所有属性强化 +40
    # rarity: 神器
    equ_400(char)
    pass


@register
def equ_611(char: CharacterProperty):
    # DCALC_REMOVE: equ_611 - 坚固之鸿运当头戒指
    # 所有属性强化 +40
    # rarity: 传说
    equ_401(char)
    pass


@register
def equ_612(char: CharacterProperty):
    # DCALC_REMOVE: equ_612 - 坚实之鸿运当头戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_402(char)
    pass


@register
def equ_613(char: CharacterProperty):
    # DCALC_REMOVE: equ_613 - 坚韧之鸿运当头戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_403(char)
    pass


@register
def equ_614(char: CharacterProperty):
    # DCALC_REMOVE: equ_614 - 黑牙 : 坚实之鸿运当头戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_404(char)
    pass


@register
def equ_615(char: CharacterProperty):
    # DCALC_REMOVE: equ_615 - 黑牙 : 坚韧之鸿运当头戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_405(char)
    pass


@register
def equ_616(char: CharacterProperty):
    # DCALC_REMOVE: equ_616 - 强固之吉人天相面具
    # 物理暴击率 +20%
    # 魔法暴击率 +20%
    # rarity: 神器
    equ_406(char)
    pass


@register
def equ_617(char: CharacterProperty):
    # DCALC_REMOVE: equ_617 - 坚固之吉人天相面具
    # 物理暴击率 +25%
    # 魔法暴击率 +25%
    # rarity: 传说
    equ_407(char)
    pass


@register
def equ_618(char: CharacterProperty):
    # DCALC_REMOVE: equ_618 - 坚实之吉人天相面具
    # 物理暴击率 +30%
    # 魔法暴击率 +30%
    # rarity: 史诗
    equ_408(char)
    pass


@register
def equ_619(char: CharacterProperty):
    # DCALC_REMOVE: equ_619 - 强固之吉人天相宝石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 神器
    equ_409(char)
    pass


@register
def equ_620(char: CharacterProperty):
    # DCALC_REMOVE: equ_620 - 坚固之吉人天相宝石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 传说
    equ_410(char)
    pass


@register
def equ_621(char: CharacterProperty):
    # DCALC_REMOVE: equ_621 - 坚实之吉人天相宝石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 史诗
    equ_411(char)
    pass


@register
def equ_622(char: CharacterProperty):
    # DCALC_REMOVE: equ_622 - 强固之吉人天相耳环
    # -
    # rarity: 神器
    equ_412(char)
    pass


@register
def equ_623(char: CharacterProperty):
    # DCALC_REMOVE: equ_623 - 坚固之吉人天相耳环
    # -
    # rarity: 传说
    equ_413(char)
    pass


@register
def equ_624(char: CharacterProperty):
    # DCALC_REMOVE: equ_624 - 坚实之吉人天相耳环
    # -
    # rarity: 史诗
    equ_414(char)
    pass


# endregion
# region 究极能量 套装


@register
def equ_625(char: CharacterProperty):
    # DCALC_REMOVE: equ_625 - 释能 - 打破极限之力
    # -
    # rarity: 神器
    equ_373(char)
    pass


@register
def equ_626(char: CharacterProperty):
    # DCALC_REMOVE: equ_626 - 节能 - 打破极限之力
    # 生命值最大值 +5%
    # 魔法值最大值 +5%
    # rarity: 传说
    equ_374(char)
    pass


@register
def equ_627(char: CharacterProperty):
    # DCALC_REMOVE: equ_627 - 充能 - 打破极限之力
    # 生命值最大值 +15%
    # 魔法值最大值 +15%
    # rarity: 史诗
    equ_375(char)
    pass


@register
def equ_628(char: CharacterProperty):
    # DCALC_REMOVE: equ_628 - 释能 - 击倒极限之腿
    # -
    # rarity: 神器
    equ_376(char)
    pass


@register
def equ_629(char: CharacterProperty):
    # DCALC_REMOVE: equ_629 - 节能 - 击倒极限之腿
    # 所受物理/魔法伤害 -5%
    # rarity: 传说
    equ_377(char)
    pass


@register
def equ_630(char: CharacterProperty):
    # DCALC_REMOVE: equ_630 - 充能 - 击倒极限之腿
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 史诗
    equ_378(char)
    pass


@register
def equ_631(char: CharacterProperty):
    # DCALC_REMOVE: equ_631 - 释能 - 粉碎极限之肩
    # 攻击速度 +35%
    # 施放速度 +35%
    # rarity: 神器
    equ_379(char)
    pass


@register
def equ_632(char: CharacterProperty):
    # DCALC_REMOVE: equ_632 - 节能 - 粉碎极限之肩
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 传说
    equ_380(char)
    pass


@register
def equ_633(char: CharacterProperty):
    # DCALC_REMOVE: equ_633 - 充能 - 粉碎极限之肩
    # 所受物理/魔法伤害 -10%
    # rarity: 史诗
    equ_381(char)
    pass


@register
def equ_634(char: CharacterProperty):
    # DCALC_REMOVE: equ_634 - 释能 - 摧毁极限之腰
    # 物品栏负重上限 +3kg
    # rarity: 神器
    equ_382(char)
    pass


@register
def equ_635(char: CharacterProperty):
    # DCALC_REMOVE: equ_635 - 节能 - 摧毁极限之腰
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +20.5%
    # rarity: 传说
    equ_383(char)
    pass


@register
def equ_636(char: CharacterProperty):
    # DCALC_REMOVE: equ_636 - 充能 - 摧毁极限之腰
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +30.5%
    # rarity: 史诗
    equ_384(char)
    pass


@register
def equ_637(char: CharacterProperty):
    # DCALC_REMOVE: equ_637 - 释能 - 碾压极限之足
    # 移动速度 +39%
    # rarity: 神器
    equ_385(char)
    pass


@register
def equ_638(char: CharacterProperty):
    # DCALC_REMOVE: equ_638 - 节能 - 碾压极限之足
    # 移动速度 +44%
    # rarity: 传说
    equ_386(char)
    pass


@register
def equ_639(char: CharacterProperty):
    # DCALC_REMOVE: equ_639 - 充能 - 碾压极限之足
    # 移动速度 +44%
    # rarity: 史诗
    equ_387(char)
    pass


@register
def equ_640(char: CharacterProperty):
    # DCALC_REMOVE: equ_640 - 释能 - 开启极限之钥项链
    # 所有属性强化 +40
    # rarity: 神器
    equ_388(char)
    pass


@register
def equ_641(char: CharacterProperty):
    # DCALC_REMOVE: equ_641 - 节能 - 开启极限之钥项链
    # 所有属性强化 +40
    # rarity: 传说
    equ_389(char)
    pass


@register
def equ_642(char: CharacterProperty):
    # DCALC_REMOVE: equ_642 - 充能 - 开启极限之钥项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_390(char)
    pass


@register
def equ_643(char: CharacterProperty):
    # DCALC_REMOVE: equ_643 - 过载 - 开启极限之钥项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_391(char)
    pass


@register
def equ_644(char: CharacterProperty):
    # DCALC_REMOVE: equ_644 - 黑牙 : 充能 - 开启极限之钥项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_392(char)
    pass


@register
def equ_645(char: CharacterProperty):
    # DCALC_REMOVE: equ_645 - 黑牙 : 过载 - 开启极限之钥项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_393(char)
    pass


@register
def equ_646(char: CharacterProperty):
    # DCALC_REMOVE: equ_646 - 释能 - 导引极限之航手镯
    # 所有属性强化 +50
    # rarity: 神器
    equ_394(char)
    pass


@register
def equ_647(char: CharacterProperty):
    # DCALC_REMOVE: equ_647 - 节能 - 导引极限之航手镯
    # 所有属性强化 +50
    # rarity: 传说
    equ_395(char)
    pass


@register
def equ_648(char: CharacterProperty):
    # DCALC_REMOVE: equ_648 - 充能 - 导引极限之航手镯
    # 所有属性强化 +50
    # rarity: 史诗
    equ_396(char)
    pass


@register
def equ_649(char: CharacterProperty):
    # DCALC_REMOVE: equ_649 - 过载 - 导引极限之航手镯
    # 所有属性强化 +50
    # rarity: 太初
    equ_397(char)
    pass


@register
def equ_650(char: CharacterProperty):
    # DCALC_REMOVE: equ_650 - 黑牙 : 充能 - 导引极限之航手镯
    # 所有属性强化 +50
    # rarity: 史诗
    equ_398(char)
    pass


@register
def equ_651(char: CharacterProperty):
    # DCALC_REMOVE: equ_651 - 黑牙 : 过载 - 导引极限之航手镯
    # 所有属性强化 +50
    # rarity: 太初
    equ_399(char)
    pass


@register
def equ_652(char: CharacterProperty):
    # DCALC_REMOVE: equ_652 - 释能 - 突破极限之隙戒指
    # 所有属性强化 +40
    # rarity: 神器
    equ_400(char)
    pass


@register
def equ_653(char: CharacterProperty):
    # DCALC_REMOVE: equ_653 - 节能 - 突破极限之隙戒指
    # 所有属性强化 +40
    # rarity: 传说
    equ_401(char)
    pass


@register
def equ_654(char: CharacterProperty):
    # DCALC_REMOVE: equ_654 - 充能 - 突破极限之隙戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_402(char)
    pass


@register
def equ_655(char: CharacterProperty):
    # DCALC_REMOVE: equ_655 - 过载 - 突破极限之隙戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_403(char)
    pass


@register
def equ_656(char: CharacterProperty):
    # DCALC_REMOVE: equ_656 - 黑牙 : 充能 - 突破极限之隙戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_404(char)
    pass


@register
def equ_657(char: CharacterProperty):
    # DCALC_REMOVE: equ_657 - 黑牙 : 过载 - 突破极限之隙戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_405(char)
    pass


@register
def equ_658(char: CharacterProperty):
    # DCALC_REMOVE: equ_658 - 释能 - 跨越极限之境辅助装备
    # 物理暴击率 +20%
    # 魔法暴击率 +20%
    # rarity: 神器
    equ_406(char)
    pass


@register
def equ_659(char: CharacterProperty):
    # DCALC_REMOVE: equ_659 - 节能 - 跨越极限之境辅助装备
    # 物理暴击率 +25%
    # 魔法暴击率 +25%
    # rarity: 传说
    equ_407(char)
    pass


@register
def equ_660(char: CharacterProperty):
    # DCALC_REMOVE: equ_660 - 充能 - 跨越极限之境辅助装备
    # 物理暴击率 +30%
    # 魔法暴击率 +30%
    # rarity: 史诗
    equ_408(char)
    pass


@register
def equ_661(char: CharacterProperty):
    # DCALC_REMOVE: equ_661 - 释能 - 超越极限之证魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 神器
    equ_409(char)
    pass


@register
def equ_662(char: CharacterProperty):
    # DCALC_REMOVE: equ_662 - 节能 - 超越极限之证魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 传说
    equ_410(char)
    pass


@register
def equ_663(char: CharacterProperty):
    # DCALC_REMOVE: equ_663 - 充能 - 超越极限之证魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 史诗
    equ_411(char)
    pass


@register
def equ_664(char: CharacterProperty):
    # DCALC_REMOVE: equ_664 - 释能 - 动摇极限之讯耳环
    # -
    # rarity: 神器
    equ_412(char)
    pass


@register
def equ_665(char: CharacterProperty):
    # DCALC_REMOVE: equ_665 - 节能 - 动摇极限之讯耳环
    # -
    # rarity: 传说
    equ_413(char)
    pass


@register
def equ_666(char: CharacterProperty):
    # DCALC_REMOVE: equ_666 - 充能 - 动摇极限之讯耳环
    # -
    # rarity: 史诗
    equ_414(char)
    pass


# endregion
# region 造化自然 套装


@register
def equ_667(char: CharacterProperty):
    # DCALC_REMOVE: equ_667 - 自然的干预上衣
    # -
    # rarity: 神器
    equ_373(char)
    pass


@register
def equ_668(char: CharacterProperty):
    # DCALC_REMOVE: equ_668 - 自然的震怒上衣
    # 生命值最大值 +5%
    # 魔法值最大值 +5%
    # rarity: 传说
    equ_374(char)
    pass


@register
def equ_669(char: CharacterProperty):
    # DCALC_REMOVE: equ_669 - 自然的制裁上衣
    # 生命值最大值 +15%
    # 魔法值最大值 +15%
    # rarity: 史诗
    equ_375(char)
    pass


@register
def equ_670(char: CharacterProperty):
    # DCALC_REMOVE: equ_670 - 自然的干预下装
    # -
    # rarity: 神器
    equ_376(char)
    pass


@register
def equ_671(char: CharacterProperty):
    # DCALC_REMOVE: equ_671 - 自然的震怒下装
    # 所受物理/魔法伤害 -5%
    # rarity: 传说
    equ_377(char)
    pass


@register
def equ_672(char: CharacterProperty):
    # DCALC_REMOVE: equ_672 - 自然的制裁下装
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 史诗
    equ_378(char)
    pass


@register
def equ_673(char: CharacterProperty):
    # DCALC_REMOVE: equ_673 - 自然的干预头肩
    # 攻击速度 +35%
    # 施放速度 +35%
    # rarity: 神器
    equ_379(char)
    pass


@register
def equ_674(char: CharacterProperty):
    # DCALC_REMOVE: equ_674 - 自然的震怒头肩
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 传说
    equ_380(char)
    pass


@register
def equ_675(char: CharacterProperty):
    # DCALC_REMOVE: equ_675 - 自然的制裁头肩
    # 所受物理/魔法伤害 -10%
    # rarity: 史诗
    equ_381(char)
    pass


@register
def equ_676(char: CharacterProperty):
    # DCALC_REMOVE: equ_676 - 自然的干预腰带
    # 物品栏负重上限 +3kg
    # rarity: 神器
    equ_382(char)
    pass


@register
def equ_677(char: CharacterProperty):
    # DCALC_REMOVE: equ_677 - 自然的震怒腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +20.5%
    # rarity: 传说
    equ_383(char)
    pass


@register
def equ_678(char: CharacterProperty):
    # DCALC_REMOVE: equ_678 - 自然的制裁腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +30.5%
    # rarity: 史诗
    equ_384(char)
    pass


@register
def equ_679(char: CharacterProperty):
    # DCALC_REMOVE: equ_679 - 自然的干预鞋子
    # 移动速度 +39%
    # rarity: 神器
    equ_385(char)
    pass


@register
def equ_680(char: CharacterProperty):
    # DCALC_REMOVE: equ_680 - 自然的震怒鞋子
    # 移动速度 +44%
    # rarity: 传说
    equ_386(char)
    pass


@register
def equ_681(char: CharacterProperty):
    # DCALC_REMOVE: equ_681 - 自然的制裁鞋子
    # 移动速度 +44%
    # rarity: 史诗
    equ_387(char)
    pass


@register
def equ_682(char: CharacterProperty):
    # DCALC_REMOVE: equ_682 - 自然的干预项链
    # 所有属性强化 +40
    # rarity: 神器
    equ_388(char)
    pass


@register
def equ_683(char: CharacterProperty):
    # DCALC_REMOVE: equ_683 - 自然的震怒项链
    # 所有属性强化 +40
    # rarity: 传说
    equ_389(char)
    pass


@register
def equ_684(char: CharacterProperty):
    # DCALC_REMOVE: equ_684 - 自然的制裁项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_390(char)
    pass


@register
def equ_685(char: CharacterProperty):
    # DCALC_REMOVE: equ_685 - 自然的灾变项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_391(char)
    pass


@register
def equ_686(char: CharacterProperty):
    # DCALC_REMOVE: equ_686 - 黑牙 : 自然的制裁项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_392(char)
    pass


@register
def equ_687(char: CharacterProperty):
    # DCALC_REMOVE: equ_687 - 黑牙 : 自然的灾变项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_393(char)
    pass


@register
def equ_688(char: CharacterProperty):
    # DCALC_REMOVE: equ_688 - 自然的干预手镯
    # 所有属性强化 +50
    # rarity: 神器
    equ_394(char)
    pass


@register
def equ_689(char: CharacterProperty):
    # DCALC_REMOVE: equ_689 - 自然的震怒手镯
    # 所有属性强化 +50
    # rarity: 传说
    equ_395(char)
    pass


@register
def equ_690(char: CharacterProperty):
    # DCALC_REMOVE: equ_690 - 自然的制裁手镯
    # 所有属性强化 +50
    # rarity: 史诗
    equ_396(char)
    pass


@register
def equ_691(char: CharacterProperty):
    # DCALC_REMOVE: equ_691 - 自然的灾变手镯
    # 所有属性强化 +50
    # rarity: 太初
    equ_397(char)
    pass


@register
def equ_692(char: CharacterProperty):
    # DCALC_REMOVE: equ_692 - 黑牙 : 自然的制裁手镯
    # 所有属性强化 +50
    # rarity: 史诗
    equ_398(char)
    pass


@register
def equ_693(char: CharacterProperty):
    # DCALC_REMOVE: equ_693 - 黑牙 : 自然的灾变手镯
    # 所有属性强化 +50
    # rarity: 太初
    equ_399(char)
    pass


@register
def equ_694(char: CharacterProperty):
    # DCALC_REMOVE: equ_694 - 自然的干预戒指
    # 所有属性强化 +40
    # rarity: 神器
    equ_400(char)
    pass


@register
def equ_695(char: CharacterProperty):
    # DCALC_REMOVE: equ_695 - 自然的震怒戒指
    # 所有属性强化 +40
    # rarity: 传说
    equ_401(char)
    pass


@register
def equ_696(char: CharacterProperty):
    # DCALC_REMOVE: equ_696 - 自然的制裁戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_402(char)
    pass


@register
def equ_697(char: CharacterProperty):
    # DCALC_REMOVE: equ_697 - 自然的灾变戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_403(char)
    pass


@register
def equ_698(char: CharacterProperty):
    # DCALC_REMOVE: equ_698 - 黑牙 : 自然的制裁戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_404(char)
    pass


@register
def equ_699(char: CharacterProperty):
    # DCALC_REMOVE: equ_699 - 黑牙 : 自然的灾变戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_405(char)
    pass


@register
def equ_700(char: CharacterProperty):
    # DCALC_REMOVE: equ_700 - 自然的干预辅助装备
    # 物理暴击率 +20%
    # 魔法暴击率 +20%
    # rarity: 神器
    equ_406(char)
    pass


@register
def equ_701(char: CharacterProperty):
    # DCALC_REMOVE: equ_701 - 自然的愤怒辅助装备
    # 物理暴击率 +25%
    # 魔法暴击率 +25%
    # rarity: 传说
    equ_407(char)
    pass


@register
def equ_702(char: CharacterProperty):
    # DCALC_REMOVE: equ_702 - 自然的制裁辅助装备
    # 物理暴击率 +30%
    # 魔法暴击率 +30%
    # rarity: 史诗
    equ_408(char)
    pass


@register
def equ_703(char: CharacterProperty):
    # DCALC_REMOVE: equ_703 - 自然的干预魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 神器
    equ_409(char)
    pass


@register
def equ_704(char: CharacterProperty):
    # DCALC_REMOVE: equ_704 - 自然的震怒魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 传说
    equ_410(char)
    pass


@register
def equ_705(char: CharacterProperty):
    # DCALC_REMOVE: equ_705 - 自然的制裁魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 史诗
    equ_411(char)
    pass


@register
def equ_706(char: CharacterProperty):
    # DCALC_REMOVE: equ_706 - 自然的干预耳环
    # -
    # rarity: 神器
    equ_412(char)
    pass


@register
def equ_707(char: CharacterProperty):
    # DCALC_REMOVE: equ_707 - 自然的震怒耳环
    # -
    # rarity: 传说
    equ_413(char)
    pass


@register
def equ_708(char: CharacterProperty):
    # DCALC_REMOVE: equ_708 - 自然的制裁耳环
    # -
    # rarity: 史诗
    equ_414(char)
    pass


# endregion
# region 诸神黄昏之女武神 套装


@register
def equ_709(char: CharacterProperty):
    # DCALC_REMOVE: equ_709 - 先锋之女武神铠甲
    # -
    # rarity: 神器
    equ_373(char)
    pass


@register
def equ_710(char: CharacterProperty):
    # DCALC_REMOVE: equ_710 - 逆袭之女武神铠甲
    # 生命值最大值 +5%
    # 魔法值最大值 +5%
    # rarity: 传说
    equ_374(char)
    pass


@register
def equ_711(char: CharacterProperty):
    # DCALC_REMOVE: equ_711 - 不灭之女武神铠甲
    # 生命值最大值 +15%
    # 魔法值最大值 +15%
    # rarity: 史诗
    equ_375(char)
    pass


@register
def equ_712(char: CharacterProperty):
    # DCALC_REMOVE: equ_712 - 先锋之女武神长裙
    # -
    # rarity: 神器
    equ_376(char)
    pass


@register
def equ_713(char: CharacterProperty):
    # DCALC_REMOVE: equ_713 - 逆袭之女武神长裙
    # 所受物理/魔法伤害 -5%
    # rarity: 传说
    equ_377(char)
    pass


@register
def equ_714(char: CharacterProperty):
    # DCALC_REMOVE: equ_714 - 不灭之女武神长裙
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 史诗
    equ_378(char)
    pass


@register
def equ_715(char: CharacterProperty):
    # DCALC_REMOVE: equ_715 - 先锋之女武神肩甲
    # 攻击速度 +35%
    # 施放速度 +35%
    # rarity: 神器
    equ_379(char)
    pass


@register
def equ_716(char: CharacterProperty):
    # DCALC_REMOVE: equ_716 - 逆袭之女武神肩甲
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 传说
    equ_380(char)
    pass


@register
def equ_717(char: CharacterProperty):
    # DCALC_REMOVE: equ_717 - 不灭之女武神肩甲
    # 所受物理/魔法伤害 -10%
    # rarity: 史诗
    equ_381(char)
    pass


@register
def equ_718(char: CharacterProperty):
    # DCALC_REMOVE: equ_718 - 先锋之女武神腰甲
    # 物品栏负重上限 +3kg
    # rarity: 神器
    equ_382(char)
    pass


@register
def equ_719(char: CharacterProperty):
    # DCALC_REMOVE: equ_719 - 逆袭之女武神腰甲
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +20.5%
    # rarity: 传说
    equ_383(char)
    pass


@register
def equ_720(char: CharacterProperty):
    # DCALC_REMOVE: equ_720 - 不灭之女武神腰甲
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +30.5%
    # rarity: 史诗
    equ_384(char)
    pass


@register
def equ_721(char: CharacterProperty):
    # DCALC_REMOVE: equ_721 - 先锋之女武神战靴
    # 移动速度 +39%
    # rarity: 神器
    equ_385(char)
    pass


@register
def equ_722(char: CharacterProperty):
    # DCALC_REMOVE: equ_722 - 逆袭之女武神战靴
    # 移动速度 +44%
    # rarity: 传说
    equ_386(char)
    pass


@register
def equ_723(char: CharacterProperty):
    # DCALC_REMOVE: equ_723 - 不灭之女武神战靴
    # 移动速度 +44%
    # rarity: 史诗
    equ_387(char)
    pass


@register
def equ_724(char: CharacterProperty):
    # DCALC_REMOVE: equ_724 - 先锋之女武神苍穹项链
    # 所有属性强化 +40
    # rarity: 神器
    equ_388(char)
    pass


@register
def equ_725(char: CharacterProperty):
    # DCALC_REMOVE: equ_725 - 逆袭之女武神苍穹项链
    # 所有属性强化 +40
    # rarity: 传说
    equ_389(char)
    pass


@register
def equ_726(char: CharacterProperty):
    # DCALC_REMOVE: equ_726 - 不灭之女武神苍穹项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_390(char)
    pass


@register
def equ_727(char: CharacterProperty):
    # DCALC_REMOVE: equ_727 - 英灵殿之女武神苍穹项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_391(char)
    pass


@register
def equ_728(char: CharacterProperty):
    # DCALC_REMOVE: equ_728 - 黑牙 : 不灭之女武神苍穹项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_392(char)
    pass


@register
def equ_729(char: CharacterProperty):
    # DCALC_REMOVE: equ_729 - 黑牙 : 英灵殿之女武神苍穹项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_393(char)
    pass


@register
def equ_730(char: CharacterProperty):
    # DCALC_REMOVE: equ_730 - 先锋之女武神守护手镯
    # 所有属性强化 +50
    # rarity: 神器
    equ_394(char)
    pass


@register
def equ_731(char: CharacterProperty):
    # DCALC_REMOVE: equ_731 - 逆袭之女武神守护手镯
    # 所有属性强化 +50
    # rarity: 传说
    equ_395(char)
    pass


@register
def equ_732(char: CharacterProperty):
    # DCALC_REMOVE: equ_732 - 不灭之女武神守护手镯
    # 所有属性强化 +50
    # rarity: 史诗
    equ_396(char)
    pass


@register
def equ_733(char: CharacterProperty):
    # DCALC_REMOVE: equ_733 - 英灵殿之女武神守护手镯
    # 所有属性强化 +50
    # rarity: 太初
    equ_397(char)
    pass


@register
def equ_734(char: CharacterProperty):
    # DCALC_REMOVE: equ_734 - 黑牙 : 不灭之女武神守护手镯
    # 所有属性强化 +50
    # rarity: 史诗
    equ_398(char)
    pass


@register
def equ_735(char: CharacterProperty):
    # DCALC_REMOVE: equ_735 - 黑牙 : 英灵殿之女武神守护手镯
    # 所有属性强化 +50
    # rarity: 太初
    equ_399(char)
    pass


@register
def equ_736(char: CharacterProperty):
    # DCALC_REMOVE: equ_736 - 先锋之女武神祝福戒指
    # 所有属性强化 +40
    # rarity: 神器
    equ_400(char)
    pass


@register
def equ_737(char: CharacterProperty):
    # DCALC_REMOVE: equ_737 - 逆袭之女武神祝福戒指
    # 所有属性强化 +40
    # rarity: 传说
    equ_401(char)
    pass


@register
def equ_738(char: CharacterProperty):
    # DCALC_REMOVE: equ_738 - 不灭之女武神祝福戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_402(char)
    pass


@register
def equ_739(char: CharacterProperty):
    # DCALC_REMOVE: equ_739 - 英灵殿之女武神祝福戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_403(char)
    pass


@register
def equ_740(char: CharacterProperty):
    # DCALC_REMOVE: equ_740 - 黑牙 : 不灭之女武神祝福戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_404(char)
    pass


@register
def equ_741(char: CharacterProperty):
    # DCALC_REMOVE: equ_741 - 黑牙 : 英灵殿之女武神祝福戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_405(char)
    pass


@register
def equ_742(char: CharacterProperty):
    # DCALC_REMOVE: equ_742 - 先锋之女武神战斗头盔
    # 物理暴击率 +20%
    # 魔法暴击率 +20%
    # rarity: 神器
    equ_406(char)
    pass


@register
def equ_743(char: CharacterProperty):
    # DCALC_REMOVE: equ_743 - 逆袭之女武神战斗头盔
    # 物理暴击率 +25%
    # 魔法暴击率 +25%
    # rarity: 传说
    equ_407(char)
    pass


@register
def equ_744(char: CharacterProperty):
    # DCALC_REMOVE: equ_744 - 不灭之女武神战斗头盔
    # 物理暴击率 +30%
    # 魔法暴击率 +30%
    # rarity: 史诗
    equ_408(char)
    pass


@register
def equ_745(char: CharacterProperty):
    # DCALC_REMOVE: equ_745 - 先锋之女武神苍穹宝玉
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 神器
    equ_409(char)
    pass


@register
def equ_746(char: CharacterProperty):
    # DCALC_REMOVE: equ_746 - 逆袭之女武神苍穹宝玉
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 传说
    equ_410(char)
    pass


@register
def equ_747(char: CharacterProperty):
    # DCALC_REMOVE: equ_747 - 不灭之女武神苍穹宝玉
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 史诗
    equ_411(char)
    pass


@register
def equ_748(char: CharacterProperty):
    # DCALC_REMOVE: equ_748 - 先锋之女武神耳环
    # -
    # rarity: 神器
    equ_412(char)
    pass


@register
def equ_749(char: CharacterProperty):
    # DCALC_REMOVE: equ_749 - 逆袭之女武神耳环
    # -
    # rarity: 传说
    equ_413(char)
    pass


@register
def equ_750(char: CharacterProperty):
    # DCALC_REMOVE: equ_750 - 不灭之女武神耳环
    # -
    # rarity: 史诗
    equ_414(char)
    pass


# endregion
# region 青丘灵珠 套装


@register
def equ_751(char: CharacterProperty):
    # DCALC_REMOVE: equ_751 - 见习狐仙的丝绸斗篷
    # -
    # rarity: 神器
    equ_373(char)
    pass


@register
def equ_752(char: CharacterProperty):
    # DCALC_REMOVE: equ_752 - 低阶狐仙的丝绸斗篷
    # 生命值最大值 +5%
    # 魔法值最大值 +5%
    # rarity: 传说
    equ_374(char)
    pass


@register
def equ_753(char: CharacterProperty):
    # DCALC_REMOVE: equ_753 - 高阶狐仙的丝绸斗篷
    # 生命值最大值 +15%
    # 魔法值最大值 +15%
    # rarity: 史诗
    equ_375(char)
    pass


@register
def equ_754(char: CharacterProperty):
    # DCALC_REMOVE: equ_754 - 见习狐仙的暗影下装
    # -
    # rarity: 神器
    equ_376(char)
    pass


@register
def equ_755(char: CharacterProperty):
    # DCALC_REMOVE: equ_755 - 低阶狐仙的暗影下装
    # 所受物理/魔法伤害 -5%
    # rarity: 传说
    equ_377(char)
    pass


@register
def equ_756(char: CharacterProperty):
    # DCALC_REMOVE: equ_756 - 高阶狐仙的暗影下装
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 史诗
    equ_378(char)
    pass


@register
def equ_757(char: CharacterProperty):
    # DCALC_REMOVE: equ_757 - 见习狐仙的护佑头肩
    # 攻击速度 +35%
    # 施放速度 +35%
    # rarity: 神器
    equ_379(char)
    pass


@register
def equ_758(char: CharacterProperty):
    # DCALC_REMOVE: equ_758 - 低阶狐仙的护佑头肩
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 传说
    equ_380(char)
    pass


@register
def equ_759(char: CharacterProperty):
    # DCALC_REMOVE: equ_759 - 高阶狐仙的护佑头肩
    # 所受物理/魔法伤害 -10%
    # rarity: 史诗
    equ_381(char)
    pass


@register
def equ_760(char: CharacterProperty):
    # DCALC_REMOVE: equ_760 - 见习狐仙的秘藏腰带
    # 物品栏负重上限 +3kg
    # rarity: 神器
    equ_382(char)
    pass


@register
def equ_761(char: CharacterProperty):
    # DCALC_REMOVE: equ_761 - 低阶狐仙的秘藏腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +20.5%
    # rarity: 传说
    equ_383(char)
    pass


@register
def equ_762(char: CharacterProperty):
    # DCALC_REMOVE: equ_762 - 高阶狐仙的秘藏腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +30.5%
    # rarity: 史诗
    equ_384(char)
    pass


@register
def equ_763(char: CharacterProperty):
    # DCALC_REMOVE: equ_763 - 见习狐仙的银色鞋子
    # 移动速度 +39%
    # rarity: 神器
    equ_385(char)
    pass


@register
def equ_764(char: CharacterProperty):
    # DCALC_REMOVE: equ_764 - 低阶狐仙的银色鞋子
    # 移动速度 +44%
    # rarity: 传说
    equ_386(char)
    pass


@register
def equ_765(char: CharacterProperty):
    # DCALC_REMOVE: equ_765 - 高阶狐仙的银色鞋子
    # 移动速度 +44%
    # rarity: 史诗
    equ_387(char)
    pass


@register
def equ_766(char: CharacterProperty):
    # DCALC_REMOVE: equ_766 - 见习狐仙的灵魂项链
    # 所有属性强化 +40
    # rarity: 神器
    equ_388(char)
    pass


@register
def equ_767(char: CharacterProperty):
    # DCALC_REMOVE: equ_767 - 低阶狐仙的灵魂项链
    # 所有属性强化 +40
    # rarity: 传说
    equ_389(char)
    pass


@register
def equ_768(char: CharacterProperty):
    # DCALC_REMOVE: equ_768 - 高阶狐仙的灵魂项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_390(char)
    pass


@register
def equ_769(char: CharacterProperty):
    # DCALC_REMOVE: equ_769 - 青丘天狐的灵魂项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_391(char)
    pass


@register
def equ_770(char: CharacterProperty):
    # DCALC_REMOVE: equ_770 - 黑牙 : 高阶狐仙的灵魂项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_392(char)
    pass


@register
def equ_771(char: CharacterProperty):
    # DCALC_REMOVE: equ_771 - 黑牙 : 青丘天狐的灵魂项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_393(char)
    pass


@register
def equ_772(char: CharacterProperty):
    # DCALC_REMOVE: equ_772 - 见习狐仙的智慧手镯
    # 所有属性强化 +50
    # rarity: 神器
    equ_394(char)
    pass


@register
def equ_773(char: CharacterProperty):
    # DCALC_REMOVE: equ_773 - 低阶狐仙的智慧手镯
    # 所有属性强化 +50
    # rarity: 传说
    equ_395(char)
    pass


@register
def equ_774(char: CharacterProperty):
    # DCALC_REMOVE: equ_774 - 高阶狐仙的智慧手镯
    # 所有属性强化 +50
    # rarity: 史诗
    equ_396(char)
    pass


@register
def equ_775(char: CharacterProperty):
    # DCALC_REMOVE: equ_775 - 青丘天狐的智慧手镯
    # 所有属性强化 +50
    # rarity: 太初
    equ_397(char)
    pass


@register
def equ_776(char: CharacterProperty):
    # DCALC_REMOVE: equ_776 - 黑牙 : 高阶狐仙的智慧手镯
    # 所有属性强化 +50
    # rarity: 史诗
    equ_398(char)
    pass


@register
def equ_777(char: CharacterProperty):
    # DCALC_REMOVE: equ_777 - 黑牙 : 青丘天狐的智慧手镯
    # 所有属性强化 +50
    # rarity: 太初
    equ_399(char)
    pass


@register
def equ_778(char: CharacterProperty):
    # DCALC_REMOVE: equ_778 - 见习狐仙的魅惑戒指
    # 所有属性强化 +40
    # rarity: 神器
    equ_400(char)
    pass


@register
def equ_779(char: CharacterProperty):
    # DCALC_REMOVE: equ_779 - 低阶狐仙的魅惑戒指
    # 所有属性强化 +40
    # rarity: 传说
    equ_401(char)
    pass


@register
def equ_780(char: CharacterProperty):
    # DCALC_REMOVE: equ_780 - 高阶狐仙的魅惑戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_402(char)
    pass


@register
def equ_781(char: CharacterProperty):
    # DCALC_REMOVE: equ_781 - 青丘天狐的魅惑戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_403(char)
    pass


@register
def equ_782(char: CharacterProperty):
    # DCALC_REMOVE: equ_782 - 黑牙 : 高阶狐仙的魅惑戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_404(char)
    pass


@register
def equ_783(char: CharacterProperty):
    # DCALC_REMOVE: equ_783 - 黑牙 : 青丘天狐的魅惑戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_405(char)
    pass


@register
def equ_784(char: CharacterProperty):
    # DCALC_REMOVE: equ_784 - 见习狐仙的符咒辅助装备
    # 物理暴击率 +20%
    # 魔法暴击率 +20%
    # rarity: 神器
    equ_406(char)
    pass


@register
def equ_785(char: CharacterProperty):
    # DCALC_REMOVE: equ_785 - 低阶狐仙的符咒辅助装备
    # 物理暴击率 +25%
    # 魔法暴击率 +25%
    # rarity: 传说
    equ_407(char)
    pass


@register
def equ_786(char: CharacterProperty):
    # DCALC_REMOVE: equ_786 - 高阶狐仙的符咒辅助装备
    # 物理暴击率 +30%
    # 魔法暴击率 +30%
    # rarity: 史诗
    equ_408(char)
    pass


@register
def equ_787(char: CharacterProperty):
    # DCALC_REMOVE: equ_787 - 见习狐仙的灵韵魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 神器
    equ_409(char)
    pass


@register
def equ_788(char: CharacterProperty):
    # DCALC_REMOVE: equ_788 - 低阶狐仙的灵韵魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 传说
    equ_410(char)
    pass


@register
def equ_789(char: CharacterProperty):
    # DCALC_REMOVE: equ_789 - 高阶狐仙的灵韵魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 史诗
    equ_411(char)
    pass


@register
def equ_790(char: CharacterProperty):
    # DCALC_REMOVE: equ_790 - 见习狐仙的低语耳环
    # -
    # rarity: 神器
    equ_412(char)
    pass


@register
def equ_791(char: CharacterProperty):
    # DCALC_REMOVE: equ_791 - 低阶狐仙的低语耳环
    # -
    # rarity: 传说
    equ_413(char)
    pass


@register
def equ_792(char: CharacterProperty):
    # DCALC_REMOVE: equ_792 - 高阶狐仙的低语耳环
    # -
    # rarity: 史诗
    equ_414(char)
    pass


# endregion
# region 群猎美学 套装


@register
def equ_793(char: CharacterProperty):
    # DCALC_REMOVE: equ_793 - 群猎之林上衣
    # -
    # rarity: 神器
    equ_373(char)
    pass


@register
def equ_794(char: CharacterProperty):
    # DCALC_REMOVE: equ_794 - 群猎之光上衣
    # 生命值最大值 +5%
    # 魔法值最大值 +5%
    # rarity: 传说
    equ_374(char)
    pass


@register
def equ_795(char: CharacterProperty):
    # DCALC_REMOVE: equ_795 - 群猎之星上衣
    # 生命值最大值 +15%
    # 魔法值最大值 +15%
    # rarity: 史诗
    equ_375(char)
    pass


@register
def equ_796(char: CharacterProperty):
    # DCALC_REMOVE: equ_796 - 群猎之林下装
    # -
    # rarity: 神器
    equ_376(char)
    pass


@register
def equ_797(char: CharacterProperty):
    # DCALC_REMOVE: equ_797 - 群猎之光下装
    # 所受物理/魔法伤害 -5%
    # rarity: 传说
    equ_377(char)
    pass


@register
def equ_798(char: CharacterProperty):
    # DCALC_REMOVE: equ_798 - 群猎之星下装
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 史诗
    equ_378(char)
    pass


@register
def equ_799(char: CharacterProperty):
    # DCALC_REMOVE: equ_799 - 群猎之林头盔
    # 攻击速度 +35%
    # 施放速度 +35%
    # rarity: 神器
    equ_379(char)
    pass


@register
def equ_800(char: CharacterProperty):
    # DCALC_REMOVE: equ_800 - 群猎之光头盔
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 传说
    equ_380(char)
    pass


@register
def equ_801(char: CharacterProperty):
    # DCALC_REMOVE: equ_801 - 群猎之星头盔
    # 所受物理/魔法伤害 -10%
    # rarity: 史诗
    equ_381(char)
    pass


@register
def equ_802(char: CharacterProperty):
    # DCALC_REMOVE: equ_802 - 群猎之林腰带
    # 物品栏负重上限 +3kg
    # rarity: 神器
    equ_382(char)
    pass


@register
def equ_803(char: CharacterProperty):
    # DCALC_REMOVE: equ_803 - 群猎之光腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +20.5%
    # rarity: 传说
    equ_383(char)
    pass


@register
def equ_804(char: CharacterProperty):
    # DCALC_REMOVE: equ_804 - 群猎之星腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +30.5%
    # rarity: 史诗
    equ_384(char)
    pass


@register
def equ_805(char: CharacterProperty):
    # DCALC_REMOVE: equ_805 - 群猎之林鞋子
    # 移动速度 +39%
    # rarity: 神器
    equ_385(char)
    pass


@register
def equ_806(char: CharacterProperty):
    # DCALC_REMOVE: equ_806 - 群猎之光鞋子
    # 移动速度 +44%
    # rarity: 传说
    equ_386(char)
    pass


@register
def equ_807(char: CharacterProperty):
    # DCALC_REMOVE: equ_807 - 群猎之星鞋子
    # 移动速度 +44%
    # rarity: 史诗
    equ_387(char)
    pass


@register
def equ_808(char: CharacterProperty):
    # DCALC_REMOVE: equ_808 - 群猎之林项链
    # 所有属性强化 +40
    # rarity: 神器
    equ_388(char)
    pass


@register
def equ_809(char: CharacterProperty):
    # DCALC_REMOVE: equ_809 - 群猎之光项链
    # 所有属性强化 +40
    # rarity: 传说
    equ_389(char)
    pass


@register
def equ_810(char: CharacterProperty):
    # DCALC_REMOVE: equ_810 - 群猎之星项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_390(char)
    pass


@register
def equ_811(char: CharacterProperty):
    # DCALC_REMOVE: equ_811 - 群猎之神项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_391(char)
    pass


@register
def equ_812(char: CharacterProperty):
    # DCALC_REMOVE: equ_812 - 黑牙 : 群猎之星项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_392(char)
    pass


@register
def equ_813(char: CharacterProperty):
    # DCALC_REMOVE: equ_813 - 黑牙 : 群猎之神项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_393(char)
    pass


@register
def equ_814(char: CharacterProperty):
    # DCALC_REMOVE: equ_814 - 群猎之林护腕
    # 所有属性强化 +50
    # rarity: 神器
    equ_394(char)
    pass


@register
def equ_815(char: CharacterProperty):
    # DCALC_REMOVE: equ_815 - 群猎之光护腕
    # 所有属性强化 +50
    # rarity: 传说
    equ_395(char)
    pass


@register
def equ_816(char: CharacterProperty):
    # DCALC_REMOVE: equ_816 - 群猎之星护腕
    # 所有属性强化 +50
    # rarity: 史诗
    equ_396(char)
    pass


@register
def equ_817(char: CharacterProperty):
    # DCALC_REMOVE: equ_817 - 群猎之神护腕
    # 所有属性强化 +50
    # rarity: 太初
    equ_397(char)
    pass


@register
def equ_818(char: CharacterProperty):
    # DCALC_REMOVE: equ_818 - 黑牙 : 群猎之星护腕
    # 所有属性强化 +50
    # rarity: 史诗
    equ_398(char)
    pass


@register
def equ_819(char: CharacterProperty):
    # DCALC_REMOVE: equ_819 - 黑牙 : 群猎之神护腕
    # 所有属性强化 +50
    # rarity: 太初
    equ_399(char)
    pass


@register
def equ_820(char: CharacterProperty):
    # DCALC_REMOVE: equ_820 - 群猎之林戒指
    # 所有属性强化 +40
    # rarity: 神器
    equ_400(char)
    pass


@register
def equ_821(char: CharacterProperty):
    # DCALC_REMOVE: equ_821 - 群猎之光戒指
    # 所有属性强化 +40
    # rarity: 传说
    equ_401(char)
    pass


@register
def equ_822(char: CharacterProperty):
    # DCALC_REMOVE: equ_822 - 群猎之星戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_402(char)
    pass


@register
def equ_823(char: CharacterProperty):
    # DCALC_REMOVE: equ_823 - 群猎之神戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_403(char)
    pass


@register
def equ_824(char: CharacterProperty):
    # DCALC_REMOVE: equ_824 - 黑牙 : 群猎之星戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_404(char)
    pass


@register
def equ_825(char: CharacterProperty):
    # DCALC_REMOVE: equ_825 - 黑牙 : 群猎之神戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_405(char)
    pass


@register
def equ_826(char: CharacterProperty):
    # DCALC_REMOVE: equ_826 - 群猎之林手斧
    # 物理暴击率 +20%
    # 魔法暴击率 +20%
    # rarity: 神器
    equ_406(char)
    pass


@register
def equ_827(char: CharacterProperty):
    # DCALC_REMOVE: equ_827 - 群猎之光手斧
    # 物理暴击率 +25%
    # 魔法暴击率 +25%
    # rarity: 传说
    equ_407(char)
    pass


@register
def equ_828(char: CharacterProperty):
    # DCALC_REMOVE: equ_828 - 群猎之星手斧
    # 物理暴击率 +30%
    # 魔法暴击率 +30%
    # rarity: 史诗
    equ_408(char)
    pass


@register
def equ_829(char: CharacterProperty):
    # DCALC_REMOVE: equ_829 - 群猎之林魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 神器
    equ_409(char)
    pass


@register
def equ_830(char: CharacterProperty):
    # DCALC_REMOVE: equ_830 - 群猎之光魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 传说
    equ_410(char)
    pass


@register
def equ_831(char: CharacterProperty):
    # DCALC_REMOVE: equ_831 - 群猎之星魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 史诗
    equ_411(char)
    pass


@register
def equ_832(char: CharacterProperty):
    # DCALC_REMOVE: equ_832 - 群猎之林耳环
    # -
    # rarity: 神器
    equ_412(char)
    pass


@register
def equ_833(char: CharacterProperty):
    # DCALC_REMOVE: equ_833 - 群猎之光耳环
    # -
    # rarity: 传说
    equ_413(char)
    pass


@register
def equ_834(char: CharacterProperty):
    # DCALC_REMOVE: equ_834 - 群猎之星耳环
    # -
    # rarity: 史诗
    equ_414(char)
    pass


# endregion
# region 冥思者的魔力领域 套装


@register
def equ_835(char: CharacterProperty):
    # DCALC_REMOVE: equ_835 - 魔力领域 - 入静上衣
    # -
    # rarity: 神器
    equ_373(char)
    pass


@register
def equ_836(char: CharacterProperty):
    # DCALC_REMOVE: equ_836 - 魔力领域 - 入真上衣
    # 生命值最大值 +5%
    # 魔法值最大值 +5%
    # rarity: 传说
    equ_374(char)
    pass


@register
def equ_837(char: CharacterProperty):
    # DCALC_REMOVE: equ_837 - 魔力领域 - 入定上衣
    # 生命值最大值 +15%
    # 魔法值最大值 +15%
    # rarity: 史诗
    equ_375(char)
    pass


@register
def equ_838(char: CharacterProperty):
    # DCALC_REMOVE: equ_838 - 魔力领域 - 入静下装
    # -
    # rarity: 神器
    equ_376(char)
    pass


@register
def equ_839(char: CharacterProperty):
    # DCALC_REMOVE: equ_839 - 魔力领域 - 入真下装
    # 所受物理/魔法伤害 -5%
    # rarity: 传说
    equ_377(char)
    pass


@register
def equ_840(char: CharacterProperty):
    # DCALC_REMOVE: equ_840 - 魔力领域 - 入定下装
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 史诗
    equ_378(char)
    pass


@register
def equ_841(char: CharacterProperty):
    # DCALC_REMOVE: equ_841 - 魔力领域 - 入静头肩
    # 攻击速度 +35%
    # 施放速度 +35%
    # rarity: 神器
    equ_379(char)
    pass


@register
def equ_842(char: CharacterProperty):
    # DCALC_REMOVE: equ_842 - 魔力领域 - 入真头肩
    # 攻击速度 +40%
    # 施放速度 +40%
    # rarity: 传说
    equ_380(char)
    pass


@register
def equ_843(char: CharacterProperty):
    # DCALC_REMOVE: equ_843 - 魔力领域 - 入定头肩
    # 所受物理/魔法伤害 -10%
    # rarity: 史诗
    equ_381(char)
    pass


@register
def equ_844(char: CharacterProperty):
    # DCALC_REMOVE: equ_844 - 魔力领域 - 入静腰带
    # 物品栏负重上限 +3kg
    # rarity: 神器
    equ_382(char)
    pass


@register
def equ_845(char: CharacterProperty):
    # DCALC_REMOVE: equ_845 - 魔力领域 - 入真腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +20.5%
    # rarity: 传说
    equ_383(char)
    pass


@register
def equ_846(char: CharacterProperty):
    # DCALC_REMOVE: equ_846 - 魔力领域 - 入定腰带
    # 物品栏负重上限 +3kg
    # 所有异常状态抗性 +30.5%
    # rarity: 史诗
    equ_384(char)
    pass


@register
def equ_847(char: CharacterProperty):
    # DCALC_REMOVE: equ_847 - 魔力领域 - 入静鞋子
    # 移动速度 +39%
    # rarity: 神器
    equ_385(char)
    pass


@register
def equ_848(char: CharacterProperty):
    # DCALC_REMOVE: equ_848 - 魔力领域 - 入真鞋子
    # 移动速度 +44%
    # rarity: 传说
    equ_386(char)
    pass


@register
def equ_849(char: CharacterProperty):
    # DCALC_REMOVE: equ_849 - 魔力领域 - 入定鞋子
    # 移动速度 +44%
    # rarity: 史诗
    equ_387(char)
    pass


@register
def equ_850(char: CharacterProperty):
    # DCALC_REMOVE: equ_850 - 魔力领域 - 入静项链
    # 所有属性强化 +40
    # rarity: 神器
    equ_388(char)
    pass


@register
def equ_851(char: CharacterProperty):
    # DCALC_REMOVE: equ_851 - 魔力领域 - 入真项链
    # 所有属性强化 +40
    # rarity: 传说
    equ_389(char)
    pass


@register
def equ_852(char: CharacterProperty):
    # DCALC_REMOVE: equ_852 - 魔力领域 - 入定项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_390(char)
    pass


@register
def equ_853(char: CharacterProperty):
    # DCALC_REMOVE: equ_853 - 魔力领域 - 入神项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_391(char)
    pass


@register
def equ_854(char: CharacterProperty):
    # DCALC_REMOVE: equ_854 - 黑牙 : 魔力领域 - 入定项链
    # 所有属性强化 +40
    # rarity: 史诗
    equ_392(char)
    pass


@register
def equ_855(char: CharacterProperty):
    # DCALC_REMOVE: equ_855 - 黑牙 : 魔力领域 - 入神项链
    # 所有属性强化 +40
    # rarity: 太初
    equ_393(char)
    pass


@register
def equ_856(char: CharacterProperty):
    # DCALC_REMOVE: equ_856 - 魔力领域 - 入静手镯
    # 所有属性强化 +50
    # rarity: 神器
    equ_394(char)
    pass


@register
def equ_857(char: CharacterProperty):
    # DCALC_REMOVE: equ_857 - 魔力领域 - 入真手镯
    # 所有属性强化 +50
    # rarity: 传说
    equ_395(char)
    pass


@register
def equ_858(char: CharacterProperty):
    # DCALC_REMOVE: equ_858 - 魔力领域 - 入定手镯
    # 所有属性强化 +50
    # rarity: 史诗
    equ_396(char)
    pass


@register
def equ_859(char: CharacterProperty):
    # DCALC_REMOVE: equ_859 - 魔力领域 - 入神手镯
    # 所有属性强化 +50
    # rarity: 太初
    equ_397(char)
    pass


@register
def equ_860(char: CharacterProperty):
    # DCALC_REMOVE: equ_860 - 黑牙 : 魔力领域 - 入定手镯
    # 所有属性强化 +50
    # rarity: 史诗
    equ_398(char)
    pass


@register
def equ_861(char: CharacterProperty):
    # DCALC_REMOVE: equ_861 - 黑牙 : 魔力领域 - 入神手镯
    # 所有属性强化 +50
    # rarity: 太初
    equ_399(char)
    pass


@register
def equ_862(char: CharacterProperty):
    # DCALC_REMOVE: equ_862 - 魔力领域 - 入静戒指
    # 所有属性强化 +40
    # rarity: 神器
    equ_400(char)
    pass


@register
def equ_863(char: CharacterProperty):
    # DCALC_REMOVE: equ_863 - 魔力领域 - 入真戒指
    # 所有属性强化 +40
    # rarity: 传说
    equ_401(char)
    pass


@register
def equ_864(char: CharacterProperty):
    # DCALC_REMOVE: equ_864 - 魔力领域 - 入定戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_402(char)
    pass


@register
def equ_865(char: CharacterProperty):
    # DCALC_REMOVE: equ_865 - 魔力领域 - 入神戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_403(char)
    pass


@register
def equ_866(char: CharacterProperty):
    # DCALC_REMOVE: equ_866 - 黑牙 : 魔力领域 - 入定戒指
    # 所有属性强化 +40
    # rarity: 史诗
    equ_404(char)
    pass


@register
def equ_867(char: CharacterProperty):
    # DCALC_REMOVE: equ_867 - 黑牙 : 魔力领域 - 入神戒指
    # 所有属性强化 +40
    # rarity: 太初
    equ_405(char)
    pass


@register
def equ_868(char: CharacterProperty):
    # DCALC_REMOVE: equ_868 - 魔力领域 - 入静辅助装备
    # 物理暴击率 +20%
    # 魔法暴击率 +20%
    # rarity: 神器
    equ_406(char)
    pass


@register
def equ_869(char: CharacterProperty):
    # DCALC_REMOVE: equ_869 - 魔力领域 - 入真辅助装备
    # 物理暴击率 +25%
    # 魔法暴击率 +25%
    # rarity: 传说
    equ_407(char)
    pass


@register
def equ_870(char: CharacterProperty):
    # DCALC_REMOVE: equ_870 - 魔力领域 - 入定辅助装备
    # 物理暴击率 +30%
    # 魔法暴击率 +30%
    # rarity: 史诗
    equ_408(char)
    pass


@register
def equ_871(char: CharacterProperty):
    # DCALC_REMOVE: equ_871 - 魔力领域 - 入静魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 神器
    equ_409(char)
    pass


@register
def equ_872(char: CharacterProperty):
    # DCALC_REMOVE: equ_872 - 魔力领域 - 入真魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 传说
    equ_410(char)
    pass


@register
def equ_873(char: CharacterProperty):
    # DCALC_REMOVE: equ_873 - 魔力领域 - 入定魔法石
    # 技能冷却时间15%减少（觉醒技能除外）
    # rarity: 史诗
    equ_411(char)
    pass


@register
def equ_874(char: CharacterProperty):
    # DCALC_REMOVE: equ_874 - 魔力领域 - 入静耳环
    # -
    # rarity: 神器
    equ_412(char)
    pass


@register
def equ_875(char: CharacterProperty):
    # DCALC_REMOVE: equ_875 - 魔力领域 - 入真耳环
    # -
    # rarity: 传说
    equ_413(char)
    pass


@register
def equ_876(char: CharacterProperty):
    # DCALC_REMOVE: equ_876 - 魔力领域 - 入定耳环
    # -
    # rarity: 史诗
    equ_414(char)
    pass


@register
def equ_877(char: CharacterProperty): ...
    # DCALC_REMOVE: equ_877 - 百里挑一嵌合弓
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5%
    # rarity: 稀有
@register
def equ_878(char: CharacterProperty): ...
    # DCALC_REMOVE: equ_878 - 独一无二嵌合弓
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5%
    # rarity: 神器
@register
def equ_879(char: CharacterProperty): ...
    # DCALC_REMOVE: equ_879 - 传说承继 - 嵌合弓
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5%
    # rarity: 传说
@register
def equ_880(char: CharacterProperty): ...
    # DCALC_REMOVE: equ_880 - 英雄叙事诗 - 嵌合弓
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5%
    # rarity: 史诗
@register
def equ_881(char: CharacterProperty): ...
    # DCALC_REMOVE: equ_881 - 太初之星 - 嵌合弓
    # 物理百分比技能
    # 魔法值 +10%
    # 魔法百分比技能
    # 魔法值 -5%
    # rarity: 太初
@register
def equ_882(char: CharacterProperty):
    # DCALC_REMOVE: equ_882 - 黯辉之翼·伊卡洛斯
    # [轨道飞行实验开启][装备主动技能]
    # 选择使用[本能飞跃]和[非理性着陆]
    # 进入地下城时，[本能飞跃]自动生效。
    # - 冷却时间 300秒
    # [本能飞跃]
    # - 技能伤害 +12.3%
    # [非理性着陆]
    # - 技能冷却时间 -20%
    # rarity: 传说
    if char.equ_options.get('6', 0) == 0:
        char.SetStatus(SkillAttack=0.123)
    elif char.equ_options.get('6', 0) == 1:
        char.SetSkillCD(cd=0.2)
    ...


@register
def equ_883(char: CharacterProperty):
    # DCALC_REMOVE: equ_883 - 流彩之翼·伊卡洛斯
    # [轨道飞行实验开启][装备主动技能]
    # 选择使用[本能飞跃]和[非理性着陆]
    # 进入地下城时，[本能飞跃]自动生效。
    # - 冷却时间 300秒
    # [本能飞跃]
    # - 技能伤害 +12.3%
    # [非理性着陆]
    # - 技能冷却时间 -20%
    # rarity: 史诗
    if char.equ_options.get('6', 0) == 0:
        char.SetStatus(SkillAttack=0.123)
    elif char.equ_options.get('6', 0) == 1:
        char.SetSkillCD(cd=0.2)
    ...


@register
def equ_884(char: CharacterProperty):
    # DCALC_REMOVE: equ_884 - 光铸之翼·伊卡洛斯
    # [轨道飞行实验开启][装备主动技能]
    # 选择使用[本能飞跃]和[非理性着陆]
    # 进入地下城时，[本能飞跃]自动生效。
    # - 冷却时间 300秒
    # [本能飞跃]
    # - 技能伤害 +12.3%
    # [非理性着陆]
    # - 技能冷却时间 -20%
    # rarity: 太初
    if char.equ_options.get('6', 0) == 0:
        char.SetStatus(SkillAttack=0.123)
    elif char.equ_options.get('6', 0) == 1:
        char.SetSkillCD(cd=0.2)
    ...


# endregion
# region 秘宝装备
@register
def equ_2000(char: CharacterProperty):
    # DCALC_REMOVE: equ_2000 - 馥郁袭人的香氛
    # <维纳斯的恩宠>
    # 穿戴的最高套装积分达到2100点以上时，才能发挥能力。
    # 套装积分达到2550以上时，会发动更强的效果。
    # 技能伤害 +53.9%
    # 增益量12530
    # 精度
    # 精度100%时，技能伤害 +13.1%，增益量4650
    # 技能冷却时间15%减少（觉醒技能除外）
    # [地震波]
    # 精度达到25%时，[地震波]属性生效。
    # 攻击时，生成地震冲击波，攻击周围所有敌人。（冷却时间30秒）
    # - 伤害量：45900%
    # - 精度每提升25%，伤害量增加45900%，范围增加50%（最大75%）
    # [膜拜]
    # 精度达到100%时，在城镇中使用普通聊天输入“膜拜”时，出现特效。（冷却时间600秒）
    # rarity: 太初
    if 2100 <= char.max_point < 2550:
        char.SetStatus(SkillAttack=0.378, Buffer=12180)
        pass
    if char.max_point >= 2550:
        char.SetStatus(SkillAttack=0.539, Buffer=12530)
        pass
    point = char.charEquipInfo['魔法石'].precision
    skillAttack = 0.1 * point - (point // 25) * 0.1 + (0.5 if point >= 25 else 0) + (0.6 if point >= 50 else 0) + (0.6 if point >= 75 else 0) + (1.8 if point >= 100 else 0)
    buffer = 30 * point - (point // 25) * 30 + (390 if point >= 25 else 0) + (420 if point >= 50 else 0) + (420 if point >= 75 else 0) + (540 if point >= 100 else 0)
    char.SetStatus(SkillAttack=skillAttack / 100, Buffer=buffer)
    char.SetSkillCD(cd=0.15)
    effect = (point // 25) * 0.5
    if effect > 0:
        char.equ_effect.append(EquEffect(name='地震波', icon='/equipment/icon/special/magicstone/00417.png', cd=30, data=45900 * effect))
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 2
    pass


@register
def equ_2001(char: CharacterProperty):
    # DCALC_REMOVE: equ_2001 - 玲珑的秘宝气候晶体
    # <纳波尔的记忆>
    # 穿戴的最高套装积分达到2100点以上时，才能发挥能力。
    # 套装积分达到2550以上时，会发动更强的效果。
    # 技能伤害+54.6%
    # 增益量12530
    # 精度
    # 精度100%时，技能伤害+10%，增益量4650
    # 技能冷却时间-4%（觉醒技能除外）
    # 精度每提升25%，技能冷却时间-4%（最多叠加4次；觉醒技能除外）
    # [不稳定性]
    # 展现神之权能，以1~11秒的时间间隔，每次有1%的几率初始化所有技能冷却时间
    # *仅当2个以上技能处于冷却时间时适用
    # *组队挑战时，辅助角色的觉醒技能不会被初始化
    # [气候重构]
    # 精度达到100%时，在城镇中使用普通聊天输入“气候重构”时，出现特效。（冷却时间600秒）
    # rarity: 太初
    if 2100 <= char.max_point < 2550:
        char.SetStatus(SkillAttack=0.384, Buffer=11220)
        pass
    if char.max_point >= 2550:
        char.SetStatus(SkillAttack=0.494 + 0.052, Buffer=12180 + 350)
        pass
    point = char.charEquipInfo['耳环'].precision
    skillAttack = 0.1 * point - (point // 25) * 0.1 + (0.5 if point >= 25 else 0) + (0.6 if point >= 50 else 0) + (0.6 if point >= 75 else 0) + (1.8 if point >= 100 else 0)
    buffer = 30 * point - (point // 25) * 30 + (390 if point >= 25 else 0) + (420 if point >= 50 else 0) + (420 if point >= 75 else 0) + (540 if point >= 100 else 0)
    char.SetStatus(SkillAttack=skillAttack / 100, Buffer=buffer)
    char.SetSkillCD(cd=0.04)
    cd = (point // 25) * 0.04
    if cd > 0:
        char.SetSkillCD(cd=cd)
    if char.buffer:
        char.BuffSkill.lv += 1
        char.AwakeSkill.lv += 1
    pass


# endregion
# region 春节


@register
def equ_3000(char: CharacterProperty):
    # DCALC_REMOVE: equ_3000 - 穿越星空的祈愿
    # 所有属性强化 +22
    # 攻击强化增幅 +22%
    # 暴击率 +15%
    # 所有速度 +4%
    # rarity: 传说
    char.AddElementDB('火', 22)
    char.AddElementDB('冰', 22)
    char.AddElementDB('光', 22)
    char.AddElementDB('暗', 22)
    char.SetStatus(AttackP=0.22, SpeedM=0.04, SpeedA=0.04, SpeedR=0.04)
    pass


@register
def equ_3001(char: CharacterProperty):
    # DCALC_REMOVE: equ_3001 - 永恒追猎
    # 所有属性强化 +15
    # 攻击强化增幅 +15%
    # 暴击率 +12%
    # 所有速度 +3%
    # rarity: 稀有
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.SetStatus(AttackP=0.15, SpeedM=0.03, SpeedA=0.03, SpeedR=0.03)
    pass


@register
def equ_3002(char: CharacterProperty):
    # DCALC_REMOVE: equ_3002 - 时空超越者
    # 所有属性强化 +25
    # 攻击强化增幅 +25%
    # 暴击率 +15%
    # 所有速度 +4%
    # rarity: 传说
    char.AddElementDB('火', 25)
    char.AddElementDB('冰', 25)
    char.AddElementDB('光', 25)
    char.AddElementDB('暗', 25)
    char.SetStatus(AttackP=0.25, SpeedM=0.04, SpeedA=0.04, SpeedR=0.04)
    pass


@register
def equ_3003(char: CharacterProperty):
    # DCALC_REMOVE: equ_3003 - 时空旅人
    # 所有属性强化 +20
    # 攻击强化增幅 +18%
    # 暴击率 +12%
    # 所有速度 +3%
    # rarity: 稀有
    char.AddElementDB('火', 20)
    char.AddElementDB('冰', 20)
    char.AddElementDB('光', 20)
    char.AddElementDB('暗', 20)
    char.SetStatus(AttackP=0.18, SpeedM=0.03, SpeedA=0.03, SpeedR=0.03)
    pass


@register
def equ_3004(char: CharacterProperty):
    # DCALC_REMOVE: equ_3004 - 破茧·三次觉醒
    # 三觉被动Lv +1
    # 所有属性强化 +25
    # 攻击强化增幅 +28%
    # 暴击率 +15%
    # 所有速度 +4%
    # rarity: 传说
    char.AddElementDB('火', 25)
    char.AddElementDB('冰', 25)
    char.AddElementDB('光', 25)
    char.AddElementDB('暗', 25)
    char.SetStatus(AttackP=0.28, SpeedM=0.04, SpeedA=0.04, SpeedR=0.04)
    char.AddSkillLv(95, 95, 1, 0)
    pass


@register
def equ_3005(char: CharacterProperty):
    # DCALC_REMOVE: equ_3005 - 悟·一次觉醒
    # 三觉被动Lv +1
    # 所有属性强化 +20
    # 攻击强化增幅 +20%
    # 暴击率 +12%
    # 所有速度 +3%
    # rarity: 稀有
    char.AddElementDB('火', 20)
    char.AddElementDB('冰', 20)
    char.AddElementDB('光', 20)
    char.AddElementDB('暗', 20)
    char.SetStatus(AttackP=0.2, SpeedM=0.03, SpeedA=0.03, SpeedR=0.03)
    char.AddSkillLv(95, 95, 1, 0)
    pass


@register
def equ_3006(char: CharacterProperty):
    # DCALC_REMOVE: equ_3006 - 千年之守望
    # 三觉被动Lv +1
    # 所有属性强化 +30
    # 攻击强化增幅 +30%
    # 暴击率 +15%
    # 所有速度 +4%
    # rarity: 传说
    char.AddElementDB('火', 30)
    char.AddElementDB('冰', 30)
    char.AddElementDB('光', 30)
    char.AddElementDB('暗', 30)
    char.SetStatus(AttackP=0.3, SpeedM=0.04, SpeedA=0.04, SpeedR=0.04)
    char.AddSkillLv(95, 95, 1, 0)
    pass


@register
def equ_3007(char: CharacterProperty):
    # DCALC_REMOVE: equ_3007 - 白云监视者
    # 三觉被动Lv +1
    # 所有属性强化 +20
    # 攻击强化增幅 +22%
    # 暴击率 +12%
    # 所有速度 +3%
    # rarity: 稀有
    char.AddElementDB('火', 20)
    char.AddElementDB('冰', 20)
    char.AddElementDB('光', 20)
    char.AddElementDB('暗', 20)
    char.SetStatus(AttackP=0.22, SpeedM=0.03, SpeedA=0.03, SpeedR=0.03)
    char.AddSkillLv(95, 95, 1, 0)
    pass


@register
def equ_3008(char: CharacterProperty):
    # DCALC_REMOVE: equ_3008 - 万壑松风之凌云志
    # 三觉被动Lv +1
    # 所有属性强化 +30
    # 攻击强化增幅 +33%
    # 暴击率 +15%
    # 所有速度 +4%
    # rarity: 传说
    char.AddElementDB('火', 30)
    char.AddElementDB('冰', 30)
    char.AddElementDB('光', 30)
    char.AddElementDB('暗', 30)
    char.SetStatus(AttackP=0.33, SpeedM=0.04, SpeedA=0.04, SpeedR=0.04)
    char.AddSkillLv(95, 95, 1, 0)
    pass


@register
def equ_3009(char: CharacterProperty):
    # DCALC_REMOVE: equ_3009 - 踏雪寻梅之冷香
    # 三觉被动Lv +1
    # 所有属性强化 +20
    # 攻击强化增幅 +25%
    # 暴击率 +12%
    # 所有速度 +3%
    # rarity: 稀有
    char.AddElementDB('火', 20)
    char.AddElementDB('冰', 20)
    char.AddElementDB('光', 20)
    char.AddElementDB('暗', 20)
    char.SetStatus(AttackP=0.25, SpeedM=0.03, SpeedA=0.03, SpeedR=0.03)
    char.AddSkillLv(95, 95, 1, 0)
    pass


# endregion
# region 耕耘


@register
def equ_3010(char: CharacterProperty):
    # DCALC_REMOVE: equ_3010 - 骑士之誓[光]
    # Lv15~35所有技能 +1
    # 所有速度 +3%
    # rarity: 稀有
    char.AddSkillLv(15, 35, 1)
    char.SetStatus(SpeedM=0.03, SpeedA=0.03, SpeedR=0.03)
    pass


@register
def equ_3011(char: CharacterProperty):
    # DCALC_REMOVE: equ_3011 - 精灵的思乡夜曲
    # Lv15~35所有技能 +1
    # 所有速度 +3%
    # rarity: 稀有
    char.AddSkillLv(15, 35, 1)
    char.SetStatus(SpeedM=0.03, SpeedA=0.03, SpeedR=0.03)
    pass


@register
def equ_3012(char: CharacterProperty):
    # DCALC_REMOVE: equ_3012 - 永恒挚爱
    # Lv15~35所有技能 +1
    # 所有属性强化 +15
    # 所有速度 +3%
    # rarity: 稀有
    char.AddSkillLv(15, 35, 1)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.SetStatus(SpeedM=0.03, SpeedA=0.03, SpeedR=0.03)
    pass


@register
def equ_3013(char: CharacterProperty):
    # DCALC_REMOVE: equ_3013 - 地下城与勇士 X SNK联动：拳皇
    # Lv15~35所有技能 +1
    # 所有属性强化 +15
    # 攻击强化 +20%
    # 所有速度 +3%
    # rarity: 稀有
    char.AddSkillLv(15, 35, 1)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.SetStatus(SpeedM=0.03, SpeedA=0.03, SpeedR=0.03, AttackP=0.2)
    pass


@register
def equ_3015(char: CharacterProperty):
    # DCALC_REMOVE: equ_3015 - 夙世今生的缘分
    # Lv15~35所有技能 +1
    # 所有属性强化 +15
    # 攻击强化 +20%
    # 所有速度 +3%
    # rarity: 稀有
    char.AddSkillLv(15, 35, 1)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.SetStatus(SpeedM=0.03, SpeedA=0.03, SpeedR=0.03, AttackP=0.2)
    pass


@register
def equ_3016(char: CharacterProperty):
    # DCALC_REMOVE: equ_3016 - 铁碎牙
    # 三觉被动Lv +1
    # 所有属性强化 +20
    # 攻击强化增幅 +22%
    # 暴击率 +12%
    # 所有速度 +3%
    # rarity: 稀有
    char.AddSkillLv(95, 95, 1, 0)
    char.AddElementDB('火', 20)
    char.AddElementDB('冰', 20)
    char.AddElementDB('光', 20)
    char.AddElementDB('暗', 20)
    char.SetStatus(SpeedM=0.03, SpeedA=0.03, SpeedR=0.03, AttackP=0.22)
    pass


# endregion
# region 白嫖


@register
def equ_3014(char: CharacterProperty):
    # DCALC_REMOVE: equ_3014 - 海岸椰影
    # 暴击率 +3%
    # 所有速度 +3%
    # rarity: 稀有
    char.SetStatus(SpeedM=0.03, SpeedA=0.03, SpeedR=0.03)
    pass


# endregion
# region 春节


@register
def equ_4000(char: CharacterProperty):
    # DCALC_REMOVE: equ_4000 - 火神的化身 蕾切尔
    # Lv1~80所有技能 +1
    # 所有属性强化 +25
    # 攻击强化增幅 +32%
    # 暴击率 +10%
    # 所有速度 +5%
    # 技能冷却时间 -5%
    # rarity: 稀有
    char.AddSkillLv(1, 80, 1)
    char.AddElementDB('火', 25)
    char.AddElementDB('冰', 25)
    char.AddElementDB('光', 25)
    char.AddElementDB('暗', 25)
    char.SetStatus(AttackP=0.32, SpeedM=0.05, SpeedA=0.05, SpeedR=0.05)
    char.SetSkillCD(1, 100, 0.05, [])
    pass


@register
def equ_4001(char: CharacterProperty):
    # DCALC_REMOVE: equ_4001 - 骑士 蕾切尔
    # Lv1~80所有技能 +1
    # 所有属性强化 +25
    # 攻击强化增幅 +22%
    # 暴击率 +10%
    # 所有速度 +5%
    # 技能冷却时间 -5%
    # rarity: 稀有
    char.AddSkillLv(1, 80, 1)
    char.AddElementDB('火', 25)
    char.AddElementDB('冰', 25)
    char.AddElementDB('光', 25)
    char.AddElementDB('暗', 25)
    char.SetStatus(AttackP=0.22, SpeedM=0.05, SpeedA=0.05, SpeedR=0.05)
    char.SetSkillCD(1, 100, 0.05, [])
    pass


@register
def equ_4002(char: CharacterProperty):
    # DCALC_REMOVE: equ_4002 - 超越时空 厄俄斯
    # Lv1~95所有技能 +1
    # 所有属性强化 +25
    # 攻击强化增幅 +35%
    # 暴击率 +10%
    # 所有速度 +5%
    # 技能冷却时间 -5%
    # rarity: 稀有
    char.AddSkillLv(1, 95, 1)
    char.AddElementDB('火', 25)
    char.AddElementDB('冰', 25)
    char.AddElementDB('光', 25)
    char.AddElementDB('暗', 25)
    char.SetStatus(AttackP=0.35, SpeedM=0.05, SpeedA=0.05, SpeedR=0.05)
    char.SetSkillCD(1, 100, 0.05, [])
    pass


@register
def equ_4003(char: CharacterProperty):
    # DCALC_REMOVE: equ_4003 - 次元探险家 厄俄斯
    # Lv1~95所有技能 +1
    # 所有属性强化 +25
    # 攻击强化增幅 +22%
    # 暴击率 +10%
    # 所有速度 +5%
    # 技能冷却时间 -5%
    # rarity: 稀有
    char.AddSkillLv(1, 95, 1)
    char.AddElementDB('火', 25)
    char.AddElementDB('冰', 25)
    char.AddElementDB('光', 25)
    char.AddElementDB('暗', 25)
    char.SetStatus(AttackP=0.22, SpeedM=0.05, SpeedA=0.05, SpeedR=0.05)
    char.SetSkillCD(1, 100, 0.05, [])
    pass


@register
def equ_4004(char: CharacterProperty):
    # DCALC_REMOVE: equ_4004 - 太初之赛丽亚
    # Lv1~95所有技能 +1
    # 所有属性强化 +25
    # 攻击强化增幅 +40%
    # 暴击率 +10%
    # 所有速度 +5%
    # 技能冷却时间 -5%
    # rarity: 稀有
    char.AddSkillLv(1, 95, 1)
    char.AddElementDB('火', 25)
    char.AddElementDB('冰', 25)
    char.AddElementDB('光', 25)
    char.AddElementDB('暗', 25)
    char.SetStatus(AttackP=0.40, SpeedM=0.05, SpeedA=0.05, SpeedR=0.05)
    char.SetSkillCD(1, 100, 0.05, [])
    pass


@register
def equ_4005(char: CharacterProperty):
    # DCALC_REMOVE: equ_4005 - 神剑梁月
    # Lv1~95所有技能 +1
    # 所有属性强化 +25
    # 攻击强化增幅 +25%
    # 暴击率 +10%
    # 所有速度 +5%
    # 技能冷却时间 -5%
    # rarity: 稀有
    char.AddSkillLv(1, 95, 1)
    char.AddElementDB('火', 25)
    char.AddElementDB('冰', 25)
    char.AddElementDB('光', 25)
    char.AddElementDB('暗', 25)
    char.SetStatus(AttackP=0.25, SpeedM=0.05, SpeedA=0.05, SpeedR=0.05)
    char.SetSkillCD(1, 100, 0.05, [])
    pass


@register
def equ_4006(char: CharacterProperty):
    # DCALC_REMOVE: equ_4006 - 迷你地界镇护者舒茉
    # Lv1~95所有技能 +1
    # 所有属性强化 +25
    # 攻击强化增幅 +45%
    # 暴击率 +10%
    # 所有速度 +5%
    # 技能冷却时间 -5%
    # rarity: 稀有
    char.AddSkillLv(1, 95, 1)
    char.AddElementDB('火', 25)
    char.AddElementDB('冰', 25)
    char.AddElementDB('光', 25)
    char.AddElementDB('暗', 25)
    char.SetStatus(AttackP=0.45, SpeedM=0.05, SpeedA=0.05, SpeedR=0.05)
    char.SetSkillCD(1, 100, 0.05, [])
    pass


@register
def equ_4007(char: CharacterProperty):
    # DCALC_REMOVE: equ_4007 - 迷你溪谷守望者鲁加鲁
    # Lv1~95所有技能 +1
    # 所有属性强化 +25
    # 攻击强化增幅 +30%
    # 暴击率 +10%
    # 所有速度 +5%
    # 技能冷却时间 -5%
    # rarity: 稀有
    char.AddSkillLv(1, 95, 1)
    char.AddElementDB('火', 25)
    char.AddElementDB('冰', 25)
    char.AddElementDB('光', 25)
    char.AddElementDB('暗', 25)
    char.SetStatus(AttackP=0.30, SpeedM=0.05, SpeedA=0.05, SpeedR=0.05)
    char.SetSkillCD(1, 100, 0.05, [])
    pass


@register
def equ_4008(char: CharacterProperty):
    # DCALC_REMOVE: equ_4008 - 菩提龙女
    # Lv1~95所有技能 +1
    # 所有属性强化 +25
    # 攻击强化增幅 +50%
    # 暴击率 +10%
    # 所有速度 +5%
    # 技能冷却时间 -5%
    # rarity: 稀有
    char.AddSkillLv(1, 95, 1)
    char.AddElementDB('火', 25)
    char.AddElementDB('冰', 25)
    char.AddElementDB('光', 25)
    char.AddElementDB('暗', 25)
    char.SetStatus(AttackP=0.50, SpeedM=0.05, SpeedA=0.05, SpeedR=0.05)
    char.SetSkillCD(1, 100, 0.05, [])
    pass


@register
def equ_4009(char: CharacterProperty):
    # DCALC_REMOVE: equ_4009 - 妙笔麒麟
    # Lv1~95所有技能 +1
    # 所有属性强化 +25
    # 攻击强化增幅 +35%
    # 暴击率 +10%
    # 所有速度 +5%
    # 技能冷却时间 -5%
    # rarity: 稀有
    char.AddSkillLv(1, 95, 1)
    char.AddElementDB('火', 25)
    char.AddElementDB('冰', 25)
    char.AddElementDB('光', 25)
    char.AddElementDB('暗', 25)
    char.SetStatus(AttackP=0.35, SpeedM=0.05, SpeedA=0.05, SpeedR=0.05)
    char.SetSkillCD(1, 100, 0.05, [])
    pass


# endregion
# region 耕耘


@register
def equ_4010(char: CharacterProperty):
    # DCALC_REMOVE: equ_4010 - 九霄守卫者雅娜
    # Lv1~50所有技能 +1
    # 攻击强化增幅 +14%
    # 增益量增幅 +3%
    # 暴击率 +3%
    # 所有速度 +5%
    # rarity: 稀有
    char.AddSkillLv(1, 50, 1)
    char.SetStatus(AttackP=0.14, SpeedM=0.05, SpeedA=0.05, SpeedR=0.05, BufferP=0.03)
    pass


@register
def equ_4011(char: CharacterProperty):
    # DCALC_REMOVE: equ_4011 - 日光守卫者克利
    # Lv1~50所有技能 +1
    # 攻击强化增幅 +10%
    # 增益量增幅 +1.5%
    # 暴击率 +3%
    # 所有速度 +4%
    # rarity: 稀有
    char.AddSkillLv(1, 50, 1)
    char.SetStatus(AttackP=0.10, SpeedM=0.04, SpeedA=0.04, SpeedR=0.04, BufferP=0.015)
    pass


@register
def equ_4012(char: CharacterProperty):
    # DCALC_REMOVE: equ_4012 - 卓越的精灵礼官
    # Lv1~50所有技能 +1
    # 攻击强化增幅 +14%
    # 增益量增幅 +3%
    # 暴击率 +3%
    # 所有速度 +5%
    # rarity: 稀有
    char.AddSkillLv(1, 50, 1)
    char.SetStatus(AttackP=0.14, SpeedM=0.05, SpeedA=0.05, SpeedR=0.05, BufferP=0.03)
    pass


@register
def equ_4013(char: CharacterProperty):
    # DCALC_REMOVE: equ_4013 - 精灵礼官
    # Lv1~50所有技能 +1
    # 攻击强化增幅 +10%
    # 增益量增幅 +1.5%
    # 暴击率 +3%
    # 所有速度 +4%
    # rarity: 稀有
    char.AddSkillLv(1, 50, 1)
    char.SetStatus(AttackP=0.10, SpeedM=0.04, SpeedA=0.04, SpeedR=0.04, BufferP=0.015)
    pass


@register
def equ_4014(char: CharacterProperty):
    # DCALC_REMOVE: equ_4014 - 迷你婚纱礼服赛丽亚
    # Lv1~75所有技能 +1
    # 所有属性强化 +25
    # 攻击强化增幅 +25%
    # 增益量增幅 +5%
    # 暴击率 +10%
    # 所有速度 +5%
    # rarity: 稀有
    char.AddSkillLv(1, 75, 1)
    char.AddElementDB('火', 25)
    char.AddElementDB('冰', 25)
    char.AddElementDB('光', 25)
    char.AddElementDB('暗', 25)
    char.SetStatus(AttackP=0.25, SpeedM=0.05, SpeedA=0.05, SpeedR=0.05, BufferP=0.05)
    pass


@register
def equ_4015(char: CharacterProperty):
    # DCALC_REMOVE: equ_4015 - 迷你礼服赛丽亚
    # Lv1~50所有技能 +1
    # 所有属性强化 +15
    # 攻击强化增幅 +25%
    # 增益量增幅 +2%
    # 暴击率 +5%
    # 所有速度 +4%
    # rarity: 稀有
    char.AddSkillLv(1, 50, 1)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.SetStatus(AttackP=0.25, SpeedM=0.04, SpeedA=0.04, SpeedR=0.04, BufferP=0.02)
    pass


@register
def equ_4016(char: CharacterProperty):
    # DCALC_REMOVE: equ_4016 - 迷你不知火舞
    # Lv1~75所有技能 +1
    # 所有属性强化 +25
    # 攻击强化增幅 +25%
    # 增益量增幅 +5%
    # 暴击率 +10%
    # 所有速度 +5%
    # rarity: 稀有
    char.AddSkillLv(1, 75, 1)
    char.AddElementDB('火', 25)
    char.AddElementDB('冰', 25)
    char.AddElementDB('光', 25)
    char.AddElementDB('暗', 25)
    char.SetStatus(AttackP=0.25, SpeedM=0.05, SpeedA=0.05, SpeedR=0.05, BufferP=0.05)
    pass


@register
def equ_4017(char: CharacterProperty):
    # DCALC_REMOVE: equ_4017 - 迷你麻宫雅典娜
    # Lv1~50所有技能 +1
    # 所有属性强化 +15
    # 攻击强化增幅 +25%
    # 增益量增幅 +2%
    # 暴击率 +5%
    # 所有速度 +4%
    # rarity: 稀有
    char.AddSkillLv(1, 50, 1)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.SetStatus(AttackP=0.25, SpeedM=0.04, SpeedA=0.04, SpeedR=0.04, BufferP=0.02)
    pass


@register
def equ_4018(char: CharacterProperty):
    # DCALC_REMOVE: equ_4018 - 迷你云母
    # Lv1~75所有技能 +1
    # 所有属性强化 +25
    # 攻击强化增幅 +35%
    # 增益量增幅 +8%
    # 暴击率 +10%
    # 所有速度 +5%
    # rarity: 稀有
    char.AddSkillLv(1, 75, 1)
    char.AddElementDB('火', 25)
    char.AddElementDB('冰', 25)
    char.AddElementDB('光', 25)
    char.AddElementDB('暗', 25)
    char.SetStatus(AttackP=0.35, SpeedM=0.05, SpeedA=0.05, SpeedR=0.05, BufferP=0.08)
    pass


@register
def equ_4019(char: CharacterProperty):
    # DCALC_REMOVE: equ_4019 - 迷你铃
    # Lv1~50所有技能 +1
    # 所有属性强化 +15
    # 攻击强化增幅 +35%
    # 增益量增幅 +3%
    # 暴击率 +5%
    # 所有速度 +4%
    # rarity: 稀有
    char.AddSkillLv(1, 50, 1)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.SetStatus(AttackP=0.35, SpeedM=0.04, SpeedA=0.04, SpeedR=0.04, BufferP=0.03)


# endregion
