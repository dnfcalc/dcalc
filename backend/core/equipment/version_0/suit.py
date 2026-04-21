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
def suit_6(char: CharacterProperty):
    # DCALC_REMOVE: suit_6 - 潜影之藏锋
    # level: 1
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。  [潜影藏锋][装备主动技能] - 强制中断角色动作（觉醒技能除外） - 冷却时间5秒
    # rarity: 神器
    pass


@register
def suit_11(char: CharacterProperty):
    # DCALC_REMOVE: suit_11 - 潜影之伏击
    # level: 1
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。  施放技能时，获得[影子]层数。（最多叠加10次）  所有速度 +15%  [潜影灭迹][装备主动技能]存在[影子]层数时，施放装备技能时发动以下效果。 - 消耗3个[影子]层数 - 强制中断角色动作（觉醒技能除外）
    # rarity: 传说
    char.SetStatus(SpeedA=0.05 * 3, SpeedM=0.05 * 3, SpeedR=0.05 * 3)
    pass


@register
def suit_16(char: CharacterProperty):
    # DCALC_REMOVE: suit_16 - 潜影之灭迹
    # level: 1
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。  施放技能时，获得[影子]层数。（最多叠加10次）  所有速度 +15%  [潜影灭迹][装备主动技能] 存在[影子]层数时，施放装备技能时发动以下效果。 - 消耗2个[影子]层数 - 强制中断角色动作（觉醒技能除外）  [追击替罪羊][装备主动技能] - 消耗7个[影子]层数 - 强制中断角色动作（觉醒技能除外） - 瞬移到最强大的敌人背后 - 追击范围：600px - 冷却时间：8秒
    # rarity: 史诗
    suit_11(char)
    pass


@register
def suit_21(char: CharacterProperty):
    # DCALC_REMOVE: suit_21 - 潜影之幽冥代理
    # level: 1
    # value: 逆转与影子的因果关系，实现超乎寻常的动作。  施放技能时，获得[影子]层数。（最多叠加10次）  所有速度 +15%  [潜影灭迹][装备主动技能] 存在[影子]层数时，施放装备技能时发动以下效果。 - 消耗1个[影子]层数 - 强制中断角色动作（觉醒技能除外）  [追击替罪羊][装备主动技能] - 消耗7个[影子]层数 - 强制中断角色动作（觉醒技能除外） - 瞬移到最强大的敌人背后 - 追击范围：800px - 冷却时间：8秒  [太初的记忆] 套装积分达到2550后， 每增加70点套装积分， 可以获得以下效果。 技能伤害 增加 1% 增益量 +100
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
def suit_27(char: CharacterProperty):
    # DCALC_REMOVE: suit_27 - 初阶精灵
    # level: 1
    # value: 召唤精灵一起战斗。  [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值  [停止攻击开关][装备主动技能] 控制精灵们的攻击。 - 攻击中止/继续攻击 - 冷却时间1秒
    # rarity: 神器
    char.equ_effect.append(EquEffect(name='火灵安珀', icon='/equipment/skill/29.png', cd=2, data=19200))
    pass


@register
def suit_32(char: CharacterProperty):
    # DCALC_REMOVE: suit_32 - 高阶精灵
    # level: 1
    # value: 召唤精灵一起战斗。  [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值  [水灵阿库娅] 每3秒施放一次水弹：伤害量24,000% 每3秒恢复1%的魔法值  [停止攻击开关][装备主动技能]控制精灵们的攻击。 - 攻击中止/继续攻击 - 冷却时间1秒  [元素释放][装备主动技能] 对精灵下达协同攻击指令。 - 消耗150精灵之魂 - 攻击时，精灵之魂 +10（冷却时间1秒） - 被击时，精灵之魂 -5（冷却时间1秒） - 元素释放伤害量：102700%
    # rarity: 传说
    char.equ_effect.append(EquEffect(name='火灵安珀', icon='/equipment/skill/29.png', cd=2, data=19200))
    char.equ_effect.append(EquEffect(name='水灵阿库娅', icon='/equipment/skill/29.png', cd=3, data=24000))
    char.equ_effect.append(EquEffect(name='元素释放', icon='/equipment/skill/29.png', cd=15, data=102700))
    pass


@register
def suit_37(char: CharacterProperty):
    # DCALC_REMOVE: suit_37 - 贵族精灵
    # level: 1
    # value: 召唤精灵一起战斗。  [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值  [水灵阿库娅] 每3秒施放一次水弹：伤害量24,000% 每3秒恢复1%的魔法值  [风灵希尔珂] 每2秒施放一次刀风：伤害量20,500% 移动速度 +15%  [停止攻击开关][装备主动技能] 控制精灵们的攻击。 - 攻击中止/继续攻击 - 冷却时间1秒  [元素释放][装备主动技能] 对精灵下达协同攻击指令。 - 消耗150精灵之魂 - 攻击时，精灵之魂 +10（冷却时间1秒） - 被击时，精灵之魂 -5（冷却时间1秒） - 元素释放伤害量：158200%
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='火灵安珀', icon='/equipment/skill/29.png', cd=2, data=19200))
    char.equ_effect.append(EquEffect(name='水灵阿库娅', icon='/equipment/skill/29.png', cd=3, data=24000))
    char.equ_effect.append(EquEffect(name='风灵希尔珂', icon='/equipment/skill/29.png', cd=2, data=20500))
    char.SetStatus(SpeedM=0.15)
    char.equ_effect.append(EquEffect(name='元素释放', icon='/equipment/skill/29.png', cd=15, data=158200))
    pass


@register
def suit_42(char: CharacterProperty):
    # DCALC_REMOVE: suit_42 - 皇室精灵
    # level: 1
    # value: 召唤精灵一起战斗。  [火灵安珀] 每2秒施放一次火花：伤害量19,200% 每3秒恢复1%的生命值  [水灵阿库娅] 每3秒施放一次水弹：伤害量24,000% 每3秒恢复1%的魔法值  [风灵希尔珂] 每2秒施放一次刀风：伤害量20500% 移动速度 +15%  [精灵女王提泰妮娅] 每5秒发动毁灭弹或毁灭斩击。 - 伤害量67500%  [停止攻击开关][装备主动技能] 控制精灵们的攻击。 - 攻击中止/继续攻击 - 冷却时间1秒  [元素释放][装备主动技能] 对精灵下达协同攻击指令。 - 消耗150精灵之魂 - 攻击时，精灵之魂 +10（冷却时间1秒） - 被击时，精灵之魂 -5（冷却时间1秒） - 元素释放伤害量：241700%  [太初的记忆] 套装积分达到2550后，每增加70点套装积分，可以获得以下效果。 - 技能伤害 增加 1% - 增益量 +100
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='火灵安珀', icon='/equipment/skill/29.png', cd=2, data=19200))
    char.equ_effect.append(EquEffect(name='水灵阿库娅', icon='/equipment/skill/29.png', cd=3, data=24000))
    char.equ_effect.append(EquEffect(name='风灵希尔珂', icon='/equipment/skill/29.png', cd=2, data=20500))
    char.SetStatus(SpeedM=0.15)
    char.equ_effect.append(EquEffect(name='元素释放', icon='/equipment/skill/29.png', cd=10, data=241700))
    char.equ_effect.append(EquEffect(name='精灵女王提泰妮娅', icon='/equipment/skill/29.png', cd=5, data=67500))
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
def suit_48(char: CharacterProperty):
    # DCALC_REMOVE: suit_48 - 黄金乡 : 构想
    # level: 1
    # value: 根据装备的强化/增幅数值，发动额外的能力。  根据防具/首饰/特殊装备的强化/增幅数值总和，适用以下效果。  - 数值总和每达到+11时，技能范围 +2% (最多叠加7次) - 防具：数值每达到+5，所受物理/魔法伤害 -1% (最多叠加7次) - 首饰：数值每达到+3，技能伤害 +1% (最多叠加7次) - 特殊装备：数值每达到+3，所有速度 +2% (最多叠加7次)
    # rarity: 神器
    reinforce, reinforce_0, reinforce_1, reinforce_2 = char.GetReinforceSum()
    char.SetStatus(SkillRange=0.02 * min(reinforce // 11, 7))
    # char.SetStatus(DamageReduce=0.01 * min(reinforce_0 // 5, 7))
    char.SetStatus(SkillAttack=0.01 * min(reinforce_1 // 3, 7))
    char.SetStatus(SpeedA=0.02 * min(reinforce_2 // 3, 7))
    char.SetStatus(SpeedM=0.02 * min(reinforce_2 // 3, 7))
    char.SetStatus(SpeedR=0.02 * min(reinforce_2 // 3, 7))
    pass


@register
def suit_53(char: CharacterProperty):
    # DCALC_REMOVE: suit_53 - 黄金乡 : 梦想成真
    # level: 1
    # value: 根据装备的强化/增幅数值，发动额外的能力。  根据防具/首饰/特殊装备的强化/增幅数值总和，适用以下效果。  - 数值总和每达到+11时，技能范围 +2% (最多叠加12次) - 防具：数值每达到+5，所受物理/魔法伤害 -1% (最多叠加12次) - 首饰：数值每达到+3，技能伤害 +1% (最多叠加12次) - 特殊装备：数值每达到+3，所有速度 +2% (最多叠加12次)
    # rarity: 传说
    reinforce, reinforce_0, reinforce_1, reinforce_2 = char.GetReinforceSum()
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
def suit_58(char: CharacterProperty):
    # DCALC_REMOVE: suit_58 - 黄金乡 : 璀璨理想
    # level: 1
    # value: 根据装备的强化/增幅数值，发动额外的能力。  根据防具/首饰/特殊装备的强化/增幅数值总和，适用以下效果。 - 超过110时，每11点，技能伤害 +2%（最多叠加2次） - 数值总和每达到+11时，技能范围 +2% (最多叠加12次) - 防具：数值每达到+5，所受物理/魔法伤害-1% (最多叠加12次) - 首饰：数值每达到+3，技能伤害 +1% (最多叠加12次) - 特殊装备：数值每达到+3，所有速度 +2% (最多叠加12次)  [淘银热] 根据防具/首饰/特殊装备的强化/增幅数值总和，降落相应数量的银币进行攻击（冷却时间10秒） * 银币伤害量信息  - 低于88：17000%  - 88~109：18700%  - 110~131：21250%  - 132以上：25500%
    # rarity: 史诗
    reinforce, reinforce_0, reinforce_1, reinforce_2 = char.GetReinforceSum()
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
        char.equ_effect.append(EquEffect(name='淘银热', icon='/equipment/suit/0.png', cd=10, data=17000))
    elif reinforce < 110:
        char.equ_effect.append(EquEffect(name='淘银热', icon='/equipment/suit/0.png', cd=10, data=18700))
    elif reinforce < 132:
        char.equ_effect.append(EquEffect(name='淘银热', icon='/equipment/suit/0.png', cd=10, data=21250))
    else:
        char.equ_effect.append(EquEffect(name='淘银热', icon='/equipment/suit/0.png', cd=10, data=25500))
    pass


@register
def suit_63(char: CharacterProperty):
    # DCALC_REMOVE: suit_63 - 黄金乡 : 永恒国度
    # level: 1
    # value: 根据装备的强化/增幅数值，发动额外的能力。  根据防具/首饰/特殊装备的强化/增幅数值总和，适用以下效果。 - 超过110时，每11点，技能伤害 +2%（最多叠加2次） - 数值总和每达到+11时，技能范围 +2% (最多叠加12次) - 防具：数值每达到+5，所受物理/魔法伤害 -1% (最多叠加12次) - 首饰：数值每达到+3，技能伤害 +1% (最多叠加12次) - 特殊装备：数值每达到+3，所有速度 +2%(最多叠加12次)  [淘银热] 根据防具/首饰/特殊装备的强化/增幅数值总和，降落相应数量的银币进行攻击（冷却时间10秒） * 银币伤害量信息  - 低于88：17000%  - 88~109：18700%  - 110~131：21250%  - 132以上：25500%  [太初的记忆] 套装积分达到2550后，每增加70点套装积分，可以获得以下效果。 - 技能伤害 增加 1% - 增益量 +100
    # rarity: 太初
    reinforce, reinforce_0, reinforce_1, reinforce_2 = char.GetReinforceSum()
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
        char.equ_effect.append(EquEffect(name='淘银热', icon='/equipment/suit/0.png', cd=10, data=17000))
    elif reinforce < 110:
        char.equ_effect.append(EquEffect(name='淘银热', icon='/equipment/suit/0.png', cd=10, data=18700))
    elif reinforce < 132:
        char.equ_effect.append(EquEffect(name='淘银热', icon='/equipment/suit/0.png', cd=10, data=21250))
    else:
        char.equ_effect.append(EquEffect(name='淘银热', icon='/equipment/suit/0.png', cd=10, data=25500))
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
def suit_69(char: CharacterProperty):
    # DCALC_REMOVE: suit_69 - 鸿蒙初开之虬龙
    # level: 1
    # value: 通过释放龙之力来增强自己。  [虬龙之火] 无色小晶块消耗量减少1个。 - 不会减少到少于1个 所有速度 +10%
    # rarity: 神器
    char.SetStatus(SpeedA=0.1, SpeedM=0.1, SpeedR=0.1)
    pass


@register
def suit_74(char: CharacterProperty):
    # DCALC_REMOVE: suit_74 - 鸡鸣拂晓之蛟龙
    # level: 1
    # value: 通过释放龙之力来增强自己。  [虬龙之火] 无色小晶块消耗量减少2个。 - 不会减少到少于1个 所有速度 +10%  [蛟龙腾霄] 攻击时，蛟龙腾霄。 (冷却时间10秒) * 蛟龙腾霄伤害量：14,400%
    # rarity: 传说
    char.SetStatus(SpeedA=0.1, SpeedM=0.1, SpeedR=0.1)
    char.equ_effect.append(EquEffect(name='龙之胜战', icon='/equipment/suit/1.png', cd=10, data=14400))
    pass


@register
def suit_79(char: CharacterProperty):
    # DCALC_REMOVE: suit_79 - 朝露晨辉之烛龙
    # level: 1
    # value: 通过释放龙之力来增强自己。  [烛龙之火] 无色小晶块消耗量减少3个。 - 不会减少到少于1个 所有速度 +10%  [烛龙腾霄] 攻击时，烛龙腾霄。（冷却时间10秒） * 烛龙腾霄伤害量：14,400%  [荧惑如意珠][装备主动技能] 将[烛龙之火]变更为[烛龙的如意珠]，效果持续30秒。 - 冷却时间60秒  [烛龙的如意珠] - 所有速度 +30% - 技能伤害 +3% - 无色小晶块技能的消耗量固定30个 - 施放消耗无色小晶块的技能时，发动白龙强袭（冷却时间3秒） * 白龙强袭伤害量：10980%
    # rarity: 史诗
    if char.equ_options.get('1', 0) == 0:
        char.SetStatus(SpeedA=0.1, SpeedM=0.1, SpeedR=0.1)
        char.equ_effect.append(EquEffect(name='烛龙腾霄', icon='/equipment/suit/1.png', cd=10, data=14400))
    elif char.equ_options.get('1', 0) == 1:
        char.SetStatus(SpeedA=0.3, SpeedM=0.3, SpeedR=0.3)
        char.SetStatus(SkillAttack=0.03)
        char.equ_effect.append(EquEffect(name='白龙强袭', icon='/equipment/suit/1.png', cd=3, data=10980))
    elif char.equ_options.get('1', 0) == 2:
        char.SetStatus(SpeedA=0.2, SpeedM=0.2, SpeedR=0.2)
        char.SetStatus(SkillAttack=0.015)
        char.equ_effect.append(EquEffect(name='白龙强袭', icon='/equipment/suit/1.png', cd=3, data=10980))
        char.equ_effect.append(EquEffect(name='烛龙腾霄', icon='/equipment/suit/1.png', cd=10, data=14400))
    pass


@register
def suit_84(char: CharacterProperty):
    # DCALC_REMOVE: suit_84 - 明光耀世之应龙
    # level: 1
    # value: 通过释放龙之力来增强自己。 [应龙之火] 无色小晶块消耗量减少5个。 不会减少到少于1个 所有速度 +10%  [应龙腾霄] 攻击时， 应龙腾霄。 (冷却时间10秒) * 应龙腾霄伤害量 : 14,400%  [荧惑如意珠] [装备主动技能] 将[应龙之火]变更为[应龙的如意珠] - 再次使用， 解除效果  [应龙的如意珠] - 所有速度 +30% - 技能伤害 增加 3% - 无色小晶块技能的消耗量固定15个 - 施放消耗无色小晶块的技能时，白龙强袭 (冷却时间3秒) * 白龙强袭伤害量 : 10,980%  [应龙之怒] [应龙的如意珠]效果生效状态下攻击时， 黑龙横扫敌人。 (冷却时间4秒) * 横扫伤害量 : 10,200%  [太初的记忆] 套装积分达到2550后，每增加70点套装积分，可以获得以下效果。 - 技能伤害 增加 1% - 增益量 +100
    # rarity: 太初
    if char.equ_options.get('1', 0) == 0:
        char.SetStatus(SpeedA=0.1, SpeedM=0.1, SpeedR=0.1)
        char.equ_effect.append(EquEffect(name='应龙腾霄', icon='/equipment/suit/1.png', cd=10, data=14400))
    elif char.equ_options.get('1', 0) == 1:
        char.SetStatus(SpeedA=0.3, SpeedM=0.3, SpeedR=0.3)
        char.SetStatus(SkillAttack=0.03)
        char.equ_effect.append(EquEffect(name='白龙强袭', icon='/equipment/suit/1.png', cd=3, data=10980))
        char.equ_effect.append(EquEffect(name='黑龙横扫', icon='/equipment/suit/1.png', cd=4, data=10200))
        char.equ_effect.append(EquEffect(name='应龙腾霄', icon='/equipment/suit/1.png', cd=10, data=14400))
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
def suit_90(char: CharacterProperty):
    # DCALC_REMOVE: suit_90 - 混沌净化：挣扎
    # level: 1
    # value: [净化] - 技能冷却时间 -30.0%（觉醒技能除外） - 特效伤害 +15% - 每秒恢复0.5%的生命值和魔法值
    # rarity: 神器
    char.SetSkillCD(cd=0.3)
    char.SetStatus(EquEffectRatio=0.15)
    pass


@register
def suit_95(char: CharacterProperty):
    # DCALC_REMOVE: suit_95 - 混沌净化：失衡
    # level: 1
    # value: [暗黑净化][装备主动技能] 根据使用者的意愿调整净化与堕落状态。 - 进入地下城时，净化状态自动生效 - 冷却时间：300秒  [净化] - 技能伤害 +17.5% - 技能冷却时间 -30%（觉醒技能除外） - 特效伤害 +15% - 每秒恢复0.5%的生命值和魔法值  [堕落] - 技能冷却时间 -55%（觉醒技能除外） - 特效伤害 +32.5% - 进入霸体状态
    # rarity: 传说
    if char.equ_options.get('2', 0) == 0:
        char.SetStatus(SkillAttack=0.175)
        char.SetSkillCD(cd=0.3)
        char.SetStatus(EquEffectRatio=0.15)
    else:
        char.SetSkillCD(cd=0.55)
        char.SetStatus(EquEffectRatio=0.325)
    pass


@register
def suit_100(char: CharacterProperty):
    # DCALC_REMOVE: suit_100 - 混沌净化：协调
    # level: 1
    # value: [暗黑净化][装备主动技能] 根据使用者的意愿调整净化与堕落状态。 - 进入地下城时，净化状态自动生效 - 冷却时间：300秒  [净化] - 技能伤害 +17.5% - 技能冷却时间 -30%（觉醒技能除外） - 特效伤害 +15% - 每秒恢复0.5%的生命值和魔法值 - 每10秒生成最大生命值10%的保护罩  [堕落] - 技能冷却时间 -55%（觉醒技能除外） - 特效伤害 +32.5% - 进入霸体状态 - 跳跃时可以再跳跃一次
    # rarity: 史诗
    suit_95(char)
    pass


@register
def suit_105(char: CharacterProperty):
    # DCALC_REMOVE: suit_105 - 混沌净化：均衡
    # level: 1
    # value: 净化与堕落达到协调后，进入均衡状态。  [均衡] - 每秒恢复0.5%的生命值和魔法值 - 每10秒生成最大生命值10%的保护罩 - 进入霸体状态 - 跳跃时可以再跳跃一次  [暗黑净化] [装备发动属性] 选择使用净化和堕落的力量。 进入地下城时，净化状态自动生效 - 冷却时间300秒  [净化] - 技能伤害 +17.5% - 技能冷却时间 -30.0%（觉醒技能除外） - 特效伤害 +15%  [堕落] - 技能冷却时间  -55.0%（觉醒技能除外） - 特效伤害 +32.5%  [太初的记忆] 套装积分达到2550后，每增加70点套装积分，可以获得以下效果。 - 技能伤害 增加 1% - 增益量 +100
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
def suit_111(char: CharacterProperty):
    # DCALC_REMOVE: suit_111 - 天命者的华丽气运
    # level: 1
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] - 技能伤害 +3% - 特效伤害 +3%  [天命所归] - 攻击时，有1%几率发动以下效果。（发动机会冷却时间1秒） - 剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外）
    # rarity: 神器
    char.SetStatus(SkillAttack=0.03)
    char.SetStatus(EquEffectRatio=0.03)
    pass


@register
def suit_116(char: CharacterProperty):
    # DCALC_REMOVE: suit_116 - 天命者的华丽气运
    # level: 1
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] - 技能伤害 +3% - 特效伤害 +4.5%  [第二次幸运] - 攻击时，有3%的几率使所有属性强化 +33（持续时间33秒；发动机会冷却时间1秒）  [天命所归] - 攻击时，有3%几率发动[天命所归]。（发动机会冷却时间1秒） - 剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外） - 剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外） - 立即发动[第二次幸运]
    # rarity: 传说
    char.SetStatus(SkillAttack=0.03)
    char.AddElementDB('火', 33, 1)
    char.AddElementDB('冰', 33, 1)
    char.AddElementDB('光', 33, 1)
    char.AddElementDB('暗', 33, 1)
    char.SetStatus(EquEffectRatio=0.045)
    pass


@register
def suit_121(char: CharacterProperty):
    # DCALC_REMOVE: suit_121 - 天命者的璀璨气运
    # level: 1
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] - 技能伤害 +3% - 特效伤害 +13.5%  [第二次幸运] - 攻击时，有3%的几率使所有属性强化 +33（持续时间33秒；发动机会冷却时间1秒）  [天命所归] - 攻击时，有3%几率发动[天命所归]。（发动机会冷却时间1秒） - 剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外） - 剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外） - 当技能冷却时间生效中的技能超过3个时，初始化剩余冷却时间超过33秒的所有技能（觉醒技能除外，冷却时间33秒） - 立即发动[第二次幸运]  [幸运之翼][装备主动技能] - [第二次幸运]、[天命所归]发动几率提高3倍，效果持续33秒 - 立即发动[第二次幸运] - [幸运之翼]结束时发动[天命所归]，33秒后可以再次使用
    # rarity: 史诗
    char.SetStatus(SkillAttack=0.03)
    char.AddElementDB('火', 33, 1)
    char.AddElementDB('冰', 33, 1)
    char.AddElementDB('光', 33, 1)
    char.AddElementDB('暗', 33, 1)
    char.SetStatus(EquEffectRatio=0.135)
    pass


@register
def suit_126(char: CharacterProperty):
    # DCALC_REMOVE: suit_126 - 天命者的梦幻气运
    # level: 1
    # value: 幸运蝴蝶以一定几率初始化技能冷却时间，从而提供更多的技能使用机会。  [第一次幸运] - 技能伤害 +3% - 特效伤害 +19%  [第二次幸运] - 攻击时，有3%的几率使所有属性强化 +33（持续时间33秒；发动机会冷却时间1秒）  [天命所归] - 攻击时，有3%几率发动[天命所归]。（发动机会冷却时间1秒） - 剩余冷却时间33秒以下的技能中，初始化剩余时间最长的1个技能（觉醒技能除外） - 剩余冷却时间33秒以下的技能中，初始化剩余时间最短的1个技能（觉醒技能除外） - 存在3个以上冷却中的技能时，初始化剩余冷却时间超过33秒的所有技能（觉醒技能除外，冷却时间33秒） - 立即发动[第二次幸运]  [幸运之翼][装备主动技能] - 立即发动[第二次幸运] - [第二次幸运]、[天命所归]发动几率提高3倍，效果持续33秒 - [幸运之翼]结束时，发动[天命所归]，可33秒后可以再次施放。  [太初的记忆] 套装积分达到2550后，每增加70点套装积分，可以获得以下效果。 - 技能伤害 增加 1% - 增益量 +100
    # rarity: 太初
    char.SetStatus(SkillAttack=0.03)
    char.AddElementDB('火', 33, 1)
    char.AddElementDB('冰', 33, 1)
    char.AddElementDB('光', 33, 1)
    char.AddElementDB('暗', 33, 1)
    char.SetStatus(EquEffectRatio=0.19)
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
def suit_132(char: CharacterProperty):
    # DCALC_REMOVE: suit_132 - 涌动的能量
    # level: 1
    # value: 觉醒技能发挥出超越极限的破坏力。  [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力 +30% - 85级技能攻击力 +30% - 85级技能冷却时间 -30% - 50级技能冷却时间 -30%  - 特效伤害 +13%  * 组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性
    # rarity: 神器
    if not char.buffer:
        char.SetSkillCD(50, 50, 0.3, [])
        char.SetSkillCD(85, 85, 0.3, [])
    char.SetSkillRation(100, 100, 0.3)
    char.SetSkillRation(85, 85, 0.3)
    char.SetStatus(EquEffectRatio=0.13)
    pass


@register
def suit_137(char: CharacterProperty):
    # DCALC_REMOVE: suit_137 - 满溢的能量
    # level: 1
    # value: 觉醒技能发挥出超越极限的破坏力。  [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力 +40% - 85级技能攻击力 +40% - 100级技能冷却时间 -50% - 85级技能冷却时间 -40%- 50级技能冷却时间  -50%  - 特效伤害 +16.5%  * 组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性  [能量护盾] 施放50、85级技能时，发动以下效果。 - 获得生命值最大值5%的保护罩（最多10%），持续30秒 - 拥有保护罩时每秒恢复1%的魔法值 - 相同技能间存在30秒冷却时间
    # rarity: 传说
    if not char.buffer:
        char.SetSkillCD(50, 50, 0.5, [])
        char.SetSkillCD(85, 85, 0.4, [])
        char.SetSkillCD(100, 100, 0.5, [])
    char.SetSkillRation(100, 100, 0.4)
    char.SetSkillRation(85, 85, 0.4)
    char.SetStatus(EquEffectRatio=0.165)
    pass


@register
def suit_142(char: CharacterProperty):
    # DCALC_REMOVE: suit_142 - 极限的能量
    # level: 1
    # value: 觉醒技能发挥出超越极限的破坏力。  [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力 +60% - 85级技能攻击力 +50%- 50级技能攻击力 +10% - 100级技能冷却时间 -60% - 85级技能冷却时间  -50%- 50级技能冷却时间 -70%  - 特效伤害 +23%  * 组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性  [抵达极限的能量] 施放[三觉技能]时，合算[抵达极限的能量]。 - 能量释放伤害量：331000% - 该伤害量为特效伤害  [能量护盾] 施放50、85级技能时，发动以下效果。 - 获得生命值最大值10%的保护罩（最多20%），持续30秒 - 拥有保护罩时每秒恢复1%的魔法值 - 相同技能间存在30秒冷却时间
    # rarity: 史诗
    if not char.buffer:
        char.SetSkillCD(50, 50, 0.7, [])
        char.SetSkillCD(85, 85, 0.5, [])
        char.SetSkillCD(100, 100, 0.6, [])
    char.SetSkillRation(100, 100, 0.6)
    char.SetSkillRation(85, 85, 0.5)
    char.SetSkillRation(50, 50, 0.1)
    char.SetStatus(EquEffectRatio=0.23)
    cd = 0
    for item in char.skills:
        if item.learnLv == 100:
            cd = item.getSkillCD()
    char.equ_effect.append(EquEffect(name='能量释放', icon='/equipment/suit/4.png', cd=cd, data=331000))
    pass


@register
def suit_147(char: CharacterProperty):
    # DCALC_REMOVE: suit_147 - 超越极限的能量
    # level: 1
    # value: 觉醒技能发挥出超越极限的破坏力。  [限制器解除] - 解除觉醒技能关联 - 100级技能攻击力 +76% - 85级技能攻击力 +60%- 50级技能攻击力 +15% - 100级技能冷却时间 -60% - 85级技能冷却时间 -60%- 50级技能冷却时间 -70%  - 特效伤害 +27.5%  * 组队时，辅助职业不适用解除觉醒技能关联、减少技能冷却时间的属性  [冲破极限] 施放[三觉技能]时，合算[冲破极限]。 - 能量释放伤害量：480000% - 该伤害量为特效伤害  [能量护盾] 施放50、85级技能时，发动以下效果。 - 获得生命值最大值15%的保护罩（最多30%），持续30秒 - 拥有保护罩时每秒恢复1%的魔法值 - 拥有保护罩时所有速度 +10% - 相同技能间存在30秒冷却时间  [太初的记忆] 套装积分达到2550后，每增加70点套装积分，可以获得以下效果。 - 技能伤害 增加 1% - 增益量 +100
    # rarity: 太初
    if not char.buffer:
        char.SetSkillCD(50, 50, 0.7, [])
        char.SetSkillCD(85, 85, 0.6, [])
        char.SetSkillCD(100, 100, 0.6, [])
    char.SetSkillRation(100, 100, 0.76)
    char.SetSkillRation(85, 85, 0.6)
    char.SetSkillRation(50, 50, 0.15)
    char.SetStatus(EquEffectRatio=0.275)
    cd = 0
    for item in char.skills:
        if item.learnLv == 100:
            cd = item.getSkillCD()
    char.equ_effect.append(EquEffect(name='能量释放', icon='/equipment/suit/4.png', cd=cd, data=480000))
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
def suit_153(char: CharacterProperty):
    # DCALC_REMOVE: suit_153 - 自然的干预
    # level: 1
    # value: 利用无可违背的自然之力，对敌人造成巨大伤害。  [无可违背的自然 - 干预] 攻击时引发自然爆炸攻击敌人。 (冷却时间5秒) - 自然燃烧伤害12750%
    # rarity: 神器
    char.equ_effect.append(EquEffect(name='自燃爆炸', icon='/equipment/suit/6.png', cd=5, data=12750))
    pass


@register
def suit_158(char: CharacterProperty):
    # DCALC_REMOVE: suit_158 - 自然的震怒
    # level: 1
    # value: 利用无可违背的自然之力，对敌人造成巨大伤害。 所有速度 +5%  [无可违背的自然 - 干预] 攻击时产生小型旋风，攻击小范围的敌人，并吸附敌人。 (冷却时间5秒) - 小型旋风伤害33300%
    # rarity: 传说
    char.equ_effect.append(EquEffect(name='小型旋风', icon='/equipment/suit/6.png', cd=5, data=33300))
    pass


@register
def suit_163(char: CharacterProperty):
    # DCALC_REMOVE: suit_163 - 自然的制裁
    # level: 1
    # value: 利用无可违背的自然之力，对敌人造成巨大伤害。 所有速度 +5% 所有技能范围 +5%  [无可违背的自然 - 干预] 攻击时引发落雷，攻击并吸附大范围敌人。 (冷却时间5秒) - 落雷伤害55500%
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='落雷', icon='/equipment/suit/6.png', cd=5, data=55500))
    char.SetStatus(SpeedM=0.05, SpeedA=0.05, SpeedR=0.05)
    pass


@register
def suit_168(char: CharacterProperty):
    # DCALC_REMOVE: suit_168 - 自然的灾变
    # level: 1
    # value: 利用无可违背的自然之力，对敌人造成巨大伤害。 所有速度 +10% 技能范围 +10%  [无可违背的自然- 灾变] 攻击时引发暴风雪，攻击地图上的所有敌人。（冷却时间5秒） - 暴风雪伤害量 77700%  [狂澜怒涛][装备主动技能] 发动狂澜怒涛，攻击地图上的所有敌人。 - 狂澜怒涛伤害量241500% - 冷却时间：60秒  [太初的记忆] 套装积分达到2550后，每增加70点套装积分，可以获得以下效果。 - 技能伤害 增加 1% - 增益量 +100
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='狂澜怒涛', icon='/equipment/skill/54.png', cd=60, data=241500))
    char.equ_effect.append(EquEffect(name='暴风雪', icon='/equipment/suit/6.png', cd=5, data=77700))
    char.SetStatus(SpeedM=0.1, SpeedA=0.1, SpeedR=0.1)
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
def suit_174(char: CharacterProperty):
    # DCALC_REMOVE: suit_174 - 女武神 - 战场的先锋
    # level: 1
    # value: 可以借用来自女武神的力量，获得全新的力量。  [破阵][装备发动属性] 与女武神融合，向前方突进。 - 正面突破伤害：10200% - 冷却时间8秒
    # rarity: 神器
    char.equ_effect.append(EquEffect(name='突破', icon='/equipment/skill/0.png', cd=8, data=10200))
    pass


@register
def suit_179(char: CharacterProperty):
    # DCALC_REMOVE: suit_179 - 女武神 - 逆袭的战魂
    # level: 1
    # value: 可以借用来自女武神的力量，获得全新的力量。  [突破][装备发动属性] 与女武神融合，向前方突进。 - 正面突破伤害：10200% - 冷却时间8秒  [审判][装备发动属性] 与女武神融合，移动到最强的敌人后方进行攻击。 - 审判伤害：19000% - 追击范围：800px - 冷却时间：15秒
    # rarity: 传说
    char.equ_effect.append(EquEffect(name='突破', icon='/equipment/skill/0.png', cd=8, data=10200))
    char.equ_effect.append(EquEffect(name='审判', icon='/equipment/skill/1.png', cd=15, data=19000))
    pass


@register
def suit_184(char: CharacterProperty):
    # DCALC_REMOVE: suit_184 - 女武神 - 不灭的英雄
    # level: 1
    # value: 可以借用来自女武神的力量，获得全新的力量。  [突破][装备发动属性] 与女武神融合，向前方突进。 - 正面突破伤害：10200% - 冷却时间8秒  [审判][装备发动属性] 与女武神融合，移动到最强的敌人后方进行攻击。 - 审判伤害：19000% - 追击范围：800px - 冷却时间：15秒  施放无色小晶块技能时，获得“女武神的意志”。（最多8个）  [天罚] 充满“女武神意志”后发动攻击，可召唤女武神，对四周敌人施以天罚。 - 天罚伤害：200400% - 冷却时间20秒
    # rarity: 史诗
    char.equ_effect.append(EquEffect(name='突破', icon='/equipment/skill/0.png', cd=8, data=10200))
    char.equ_effect.append(EquEffect(name='审判', icon='/equipment/skill/1.png', cd=15, data=19000))
    char.equ_effect.append(EquEffect(name='天罚', icon='/equipment/suit/7.png', cd=20, data=200400))
    pass


@register
def suit_189(char: CharacterProperty):
    # DCALC_REMOVE: suit_189 - 女武神 - 英灵的引导者
    # level: 1
    # value: 可以借用来自女武神的力量，获得全新的力量。  [突破][装备发动属性] 与女武神融合，向前方突进。 - 正面突破伤害：10200% - 冷却时间8秒  [审判][装备发动属性] 与女武神融合，移动到最强的敌人后方进行攻击。 - 审判伤害：19000% - 追击范围：800px - 冷却时间：15秒  [降临][装备主动技能] 发挥女武神真正的力量，降临世间。 - 降临伤害量：329400% - 冷却时间：140秒  施放无色小晶块技能时，可以获得“女武神意志”。（最多8个）  [天罚] 充满“女武神意志”后发动攻击，可召唤女武神，对四周敌人施以天罚。 - 天罚伤害：233500% - 冷却时间：20秒  [太初的记忆] 套装积分达到2550后，每增加70点套装积分，可以获得以下效果。 - 技能伤害 增加 1% - 增益量 +100
    # rarity: 太初
    char.equ_effect.append(EquEffect(name='突破', icon='/equipment/skill/0.png', cd=8, data=10200))
    char.equ_effect.append(EquEffect(name='审判', icon='/equipment/skill/1.png', cd=15, data=19000))
    char.equ_effect.append(EquEffect(name='降临', icon='/equipment/skill/3.png', cd=140, data=329400))
    char.equ_effect.append(EquEffect(name='天罚', icon='/equipment/suit/7.png', cd=20, data=233500))
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
def suit_195(char: CharacterProperty):
    # DCALC_REMOVE: suit_195 - 微光的青丘灵珠
    # level: 1
    # value: 借用青丘狐的灵珠之力，瞬间变强。 [青丘灵珠]激活 - 攻击时，灵珠能量 +5（冷却时间1秒） - 灵珠最多可填充1个 - 青丘灵珠增益效果生效时，无法充能灵珠 - 进入地下城时，灵珠能量填充100  [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒
    # rarity: 神器
    char.SetStatus(SkillAttack=0.1)
    pass


@register
def suit_200(char: CharacterProperty):
    # DCALC_REMOVE: suit_200 - 清澈的青丘灵珠
    # level: 1
    # value: 借用青丘狐的灵珠之力，瞬间变强。 [青丘灵珠]激活 - 攻击时，灵珠能量 +6（冷却时间1秒） - 每秒灵珠能量 +1 - 灵珠最多可填充2个 - 青丘灵珠增益效果生效时，可以充能灵珠 - 进入地下城时，灵珠能量填充200  [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒
    # rarity: 传说
    char.SetStatus(SkillAttack=0.2)
    pass


@register
def suit_205(char: CharacterProperty):
    # DCALC_REMOVE: suit_205 - 耀眼的青丘灵珠
    # level: 1
    # value: 借用青丘狐的灵珠之力，瞬间变强。 [青丘灵珠]激活 - 攻击时，灵珠能量 +8（冷却时间1秒） - 每秒灵珠能量 +3 - 灵珠最多可填充3个 - 青丘灵珠增益效果生效时，也可以充能灵珠 - 进入地下城时，灵珠能量填充200  [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒  [青丘灵珠开关][装备主动技能] - 灵珠全部填满时，自动使用青丘灵珠增益效果（冷却时间1秒） - 再次使用时，关闭自动使用功能
    # rarity: 史诗
    char.SetStatus(SkillAttack=0.3)
    pass


@register
def suit_210(char: CharacterProperty):
    # DCALC_REMOVE: suit_210 - 梦幻的青丘灵珠
    # level: 1
    # value: 借用青丘狐的灵珠之力，瞬间变强。 [青丘灵珠]激活 - 攻击时，灵珠能量 +11（冷却时间1秒） - 每秒灵珠能量 +6 - 灵珠最多可填充4个 - 青丘灵珠增益效果生效时，也可以充能灵珠 - 进入地下城时，灵珠能量填充400  [青丘灵珠][装备主动技能] - 发动时，消耗能量充满的所有灵珠，激活增益效果 - 每消耗1个灵珠，技能伤害 +10% - 增益效果持续时间30秒 - 冷却时间30秒  [青丘灵珠开关][装备主动技能] - 灵珠全部填满时，自动使用青丘灵珠增益效果（冷却时间1秒） - 再次使用时，关闭自动使用功能  [太初的记忆] 套装积分达到2550后，每增加70点套装积分，可以获得以下效果。 - 技能伤害 增加 1% - 增益量 +100
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
def suit_216(char: CharacterProperty):
    # DCALC_REMOVE: suit_216 - 群猎之林
    # level: 1
    # value: 与同伴在一起时，会变得更强。  [组队挑战时适用] [群猎之力] 给队员赋予光环，获得以下效果。 (最多叠加1次) - 所有速度 +10%  [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量：3,825% - 使被命中的敌人进入崩裂状态，持续30秒 - 冷却时间10秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）  （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）  [单人挑战时适用] - 技能伤害 +7.4% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 神器
    if char.equ_options.get('3', 0) == 0:
        char.SetStatus(SkillAttack=0.074)
    else:
        char.SetStatus(SkillAttack=0.08, SpeedA=0.1, SpeedM=0.1, SpeedR=0.1)
        char.equ_effect.append(EquEffect(name='酣畅狩猎', icon='/equipment/skill/15.png', cd=10, data=3825))
    pass


@register
def suit_221(char: CharacterProperty):
    # DCALC_REMOVE: suit_221 - 群猎之光
    # level: 1
    # value: 与同伴在一起时，会变得更强。  [组队挑战时适用] [群猎之力] 给队员赋予光环，获得以下效果。（最多叠加1次） - 所有速度 +15% - 每10秒恢复10000点的生命值和魔法值，持续10秒  [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量：5,738% - 使被命中的敌人进入崩裂状态，持续45秒 - 冷却时间10秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）  （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）  [单人挑战时适用] - 技能伤害 +14.4% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 传说
    if char.equ_options.get('3', 0) == 0:
        char.SetStatus(SkillAttack=0.144)
    else:
        char.SetStatus(SkillAttack=0.08, SpeedA=0.15, SpeedM=0.15, SpeedR=0.15)
        char.equ_effect.append(EquEffect(name='酣畅狩猎', icon='/equipment/skill/15.png', cd=10, data=5738))
    pass


@register
def suit_226(char: CharacterProperty):
    # DCALC_REMOVE: suit_226 - 群猎之星
    # level: 1
    # value: 与同伴在一起时，会变得更强。  [组队挑战时适用] [群猎之力] 给队员赋予光环，获得以下效果。（最多叠加1次） - 所有速度 +20% - 所受物理/魔法伤害- 10% - 每10秒恢复10000点的生命值和魔法值，持续10秒  [酣畅狩猎][装备主动技能] 发出吼叫震慑敌人。 - 伤害量：6,750% - 使被命中的敌人进入最大层数的崩裂状态，持续60秒 - 冷却时间30秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）  （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）  [单人挑战时适用] - 技能伤害 +14.4% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果
    # rarity: 史诗
    if char.equ_options.get('3', 0) == 0:
        char.SetStatus(SkillAttack=0.144)
    else:
        char.SetStatus(SkillAttack=0.08, SpeedA=0.2, SpeedM=0.0, SpeedR=0.0)
        char.equ_effect.append(EquEffect(name='酣畅狩猎', icon='/equipment/skill/15.png', cd=30, data=6750))
    pass


@register
def suit_231(char: CharacterProperty):
    # DCALC_REMOVE: suit_231 - 群猎之神
    # level: 1
    # value: 与同伴在一起时，会变得更强。  [组队挑战时适用] [群猎之力] 给队员赋予光环，获得以下效果。（最多叠加1次） - 所有速度 +30% - 所受物理/魔法伤害- 15% - 每10秒恢复10，000点的生命值和魔法值，持续10秒  [酣畅狩猎][装备主动技能] 散发出威慑敌人的气势。 - 施放时，每秒使500px范围内的敌人进入最大层数的崩裂状态，持续60秒 - 再次施放时，不再使敌人进入崩裂状态 - 冷却时间10秒 （敌人进入崩裂状态时，所受伤害根据叠加层数(1/2/3)增加(5/7/8)%）  （[群猎之力]、[酣畅狩猎]效果对辅助职业无效）  [单人挑战时适用] - 技能伤害 +18.1% - 适用[群猎之力]效果 - 不适用[酣畅狩猎]效果  [太初的记忆] 套装积分达到2550后，每增加70点套装积分，可以获得以下效果。 - 技能伤害 增加 1% - 增益量 +100
    # rarity: 太初
    if char.equ_options.get('3', 0) == 0:
        char.SetStatus(SkillAttack=0.181)
    else:
        char.SetStatus(SkillAttack=0.08, SpeedA=0.3, SpeedM=0.3, SpeedR=0.3)
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
def suit_237(char: CharacterProperty):
    # DCALC_REMOVE: suit_237 - 魔力领域 - 入静
    # level: 1
    # value: 操控魔攻核攻击敌人。  [魔攻核] 进入地下城时，召唤普通模式魔攻核。  [命令：转换][装备主动技能] 转换魔攻核的攻击模式。 - 普通模式/追击模式 - 冷却时间：5秒  [魔攻核：普通模式] 每秒发射魔力波动。 - 魔力波动伤害量：19200% - 魔力波动范围：150px  [魔攻核：追击模式] 追击最强的敌人，每秒发射魔力波动。 - 魔力波动伤害量：13714% - 魔力波动范围：150px
    # rarity: 神器
    if char.equ_options.get('4', 0) == 0:
        char.equ_effect.append(EquEffect(name='普通模式', icon='/equipment/skill/57.png', cd=1, data=19200))
    else:
        char.equ_effect.append(EquEffect(name='追击模式', icon='/equipment/skill/57.png', cd=1, data=13714))
    pass


@register
def suit_242(char: CharacterProperty):
    # DCALC_REMOVE: suit_242 - 魔力领域 - 入真
    # level: 1
    # value: 操控魔攻核攻击敌人。  [魔攻核] 进入地下城时， 召唤普通模式魔攻核。  [命令 : 转换]  [装备主动技能] 转换魔攻核的攻击模式。 - 普通模式 / 追击模式 - 删除[追踪印记] - 冷却时间 : 5秒  [魔攻核 : 普通模式] 每秒发射魔力波动。 - 魔力波动伤害量 : 35000% - 魔力波动范围 : 150px - 移动速度 +25% - 进入霸体状态  [魔攻核 : 追击模式] 追击最强的敌人， 每秒发射魔力波动。 - 魔力波动伤害量 : 21000% - 魔力波动范围 : 150px - 对追踪目标赋予[追踪印记]  [魔攻弹 : 追击模式] 攻击时， 对赋予[追踪印记]的敌人发射魔力飞弹。 - 魔力飞弹伤害量 : 7000% - 冷却时间 : 1秒
    # rarity: 传说
    if char.equ_options.get('4', 0) == 0:
        char.equ_effect.append(EquEffect(name='普通模式', icon='/equipment/skill/57.png', cd=1, data=35000))
        char.SetStatus(SpeedM=0.25)
    else:
        char.equ_effect.append(EquEffect(name='追击模式', icon='/equipment/skill/57.png', cd=1, data=21000 + 7000))
    pass


@register
def suit_247(char: CharacterProperty):
    # DCALC_REMOVE: suit_247 - 魔力领域 - 入定
    # level: 1
    # value: 操控魔攻核攻击敌人。  [魔攻核] 进入地下城时， 召唤普通模式魔攻核。  [命令 : 转换]  [装备主动技能] 转换魔攻核的攻击模式。 - 普通模式 / 追击模式 - 删除[追踪印记] - 冷却时间 : 5秒  [魔攻核 : 普通模式] 每秒发射魔力波动。 - 魔力波动伤害量 : 52500% - 魔力波动范围 : 200px - 移动速度 +25% - 进入霸体状态  [魔攻核 : 追击模式] 追击最强的敌人， 每秒发射魔力波动。 - 魔力波动伤害量 : 31000% - 魔力波动范围 : 200px - 对追踪目标赋予[追踪印记]  [魔攻弹 : 追击模式] 攻击时， 对赋予[追踪印记]的敌人发射魔力飞弹。 - 魔力飞弹伤害量 : 11000% - 冷却时间 : 1秒
    # rarity: 史诗
    if char.equ_options.get('4', 0) == 0:
        char.equ_effect.append(EquEffect(name='普通模式', icon='/equipment/skill/57.png', cd=1, data=52500))
        char.SetStatus(SpeedM=0.25)
    else:
        char.equ_effect.append(EquEffect(name='追击模式', icon='/equipment/skill/57.png', cd=1, data=31000 + 11000))
    pass


@register
def suit_252(char: CharacterProperty):
    # DCALC_REMOVE: suit_252 - 魔力领域 - 入神
    # level: 1
    # value: 操控魔攻核攻击敌人。  [魔攻核] 进入地下城时， 召唤普通模式魔攻核。  [命令 : 转换]  [装备主动技能] 转换魔攻核的攻击模式。 - 普通模式 / 追击模式 - 删除[追踪印记] - 冷却时间 : 5秒  [魔攻核 : 普通模式] 每秒发射魔力波动。 - 魔力波动伤害量 : 67000% - 魔力波动范围 : 300px - 移动速度 +25% - 进入霸体状态 - 所受物理/魔法伤害 -10%  [魔攻核 : 追击模式] 追击最强的敌人， 每秒发射魔力波动。 - 魔力波动伤害量 : 40000% - 魔力波动范围 : 200px - 对追踪目标赋予[追踪印记]  [魔攻弹 : 追击模式] 攻击时， 对赋予[追踪印记]的敌人发射魔力飞弹。 - 魔力飞弹伤害量 : 13600% - 冷却时间 : 1秒  [太初的记忆] 套装积分达到2550后，每增加70点套装积分，可以获得以下效果。 - 技能伤害 增加 1% - 增益量 +100
    # rarity: 太初
    if char.equ_options.get('4', 0) == 0:
        char.equ_effect.append(EquEffect(name='普通模式', icon='/equipment/skill/57.png', cd=1, data=67000))
        char.SetStatus(SpeedM=0.25)
    else:
        char.equ_effect.append(EquEffect(name='追击模式', icon='/equipment/skill/57.png', cd=1, data=40000 + 13600))
    pass


# endregion
