from core.basic.property import CharacterProperty
from core.equipment.property import 成长词条计算
import core.equipment.entry_0.params as pa

# 固定装备：胜负之役短剑 - 狂战士 ， 胜负之役太刀 - 狂战士 ， 胜负之役钝器 - 狂战士 ， 胜负之役巨剑 - 狂战士
def entry_539(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放[饥渴]技能时，消耗10%的生命值，获得3层血气。 (最多叠加10次)', '- [饥渴]删除蓄气功能。', '- 施放其他技能期间可施放[饥渴]。', '- 进入地下城时，获得1层血气。', '', '施放[爆发之刃]、[暴怒狂斩]时，消耗1层血气，强化。', '- 攻击力 +30%', '- 技能范围 +15%', '', '施放[爆发之刃]、[暴怒狂斩]时，恢复5%的生命值。']
    if mode == 0:
        char.技能攻击力加成(0.1)
        char.单技能加成('血气之刃', 1.35)
        char.单技能加成('暴怒狂斩', 1.35)
        char.单技能加成('浴血之怒',1.15)
        char.单技能加成('致命血陨',1.15)
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役短剑 - 剑魂 ， 胜负之役太刀 - 剑魂 ， 胜负之役钝器 - 剑魂 ， 胜负之役巨剑 - 剑魂 ， 胜负之役光剑 - 剑魂
def entry_543(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '磨炼招式，强化[万剑归宗]技能。', '- 持续时间 +20秒', '- 施放35级以上技能时，持续时间 +5秒 (不会超过持续时间上限)', '- 穿云刺发射个数 +1', '- 减少穿云刺发射回收时间', '', '解除穿戴时，[万剑归宗]持续时间结束。', '', '[极 · 神剑术 (破空斩)]斩击次数固定为1次。', '- 爆炸攻击力 +50%', '- 装备太刀、光剑时，爆炸攻击力 +10%', '', '[极 · 神剑术 (瞬斩)]删除剑气攻击。', '- 最后一击攻击力 +20%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)
        skill = char.get_skill_by_name('极神剑术破空斩')
        # 武器倍率已计入
        skill.多段倍率 = {'短剑': 1, '光剑': 1, '巨剑': 1 * 1.08, '钝器': 1, '太刀': 1}
        skill.爆炸倍率 = {'短剑': 1 * 1.5, '光剑': 1* 1.6, '巨剑': 1.08* 1.5, '钝器': 1* 1.5, '太刀': 1 *1.6}
        skill = char.get_skill_by_name('极神剑术瞬斩')
        skill.power1 = 0
        skill.power2 = 1.2
        pass


# 固定装备：胜负之役短剑 - 鬼泣 ， 胜负之役太刀 - 鬼泣 ， 胜负之役钝器 - 鬼泣 ， 胜负之役巨剑 - 鬼泣
def entry_547(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['通过冥界之力，[冥炎之卡洛]生成冥界火焰。', '火焰叠加层数上限 +2', '', '以下技能生成冥界火焰。', '使用特定技能攻击附着冥界火焰的对象时，火焰爆发。', '- 爆发攻击力： [冥炎之卡洛]火焰攻击力的300%', '- 每1个冥界火焰，爆发攻击力增加10%。', '', '<冥界火焰生成技能>', '- [冥炎之卡洛]', '- [冰霜之萨亚]', '- [瘟疫之罗刹]', '- [死亡墓碑]', '- [死亡墓碑]', '- [死亡墓碑]', '', '<冥界火焰爆发技能>', '- [鬼斩]', '- [月光斩]', '- [鬼斩：狂怒]', '- [鬼影闪]', '- [鬼斩：炼狱]', '- [冥炎剑]', '- [幽魂降临：式]', '- [鬼神剑·黄泉摆渡]']
    if mode == 0:
        char.get_skill_by_name('冥炎之卡洛').CP武器 = True
        char.get_skill_by_name('冥炎之卡洛').power2 = 3 * pa.cp_soul_bender * (1+0.1*pa.cp_soul_bender)
        char.技能攻击力加成(0.06)
        char.单技能加成('冥炎剑',1.2)
        for skill in ['冰霜之萨亚','瘟疫之罗刹','幽魂之布雷德']:
            char.单技能加成(skill,1.15)
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役短剑 - 阿修罗 ， 胜负之役太刀 - 阿修罗 ， 胜负之役钝器 - 阿修罗 ， 胜负之役巨剑 - 阿修罗
def entry_551(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[爆炎·波动剑]快速爆炸。', '- 爆炸位置变更', '- 爆炸间隔减少30%', '- 爆炸间隔距离减少90%', '- 爆炸大小增加45%', '- 第3击爆炸大小增加70%', '', '获得雷神之力，施放以下技能期间，可以无施放动作发动[邪光波动阵]。', '- [爆炎 · 波动剑]', '- [不动明王阵]', '- [天雷 · 波动剑]', '', '[无尽波动]波动范围 +20%', '', '[邪光波动阵]波动范围比率 +25%']
    if mode == 0:
        char.技能攻击力加成(0.1)
        char.单技能加成('天雷·降魔杵',2,1.7)
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役短剑 - 剑影 ， 胜负之役太刀 - 剑影 ， 胜负之役钝器 - 剑影 ， 胜负之役巨剑 - 剑影
def entry_555(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['剑术，共鸣系列技能命中时，鬼步冷却时间初始化。', '- 通过鬼步施放剑术系列技能时不初始化。', '', '[鬼步]攻击力 +20%', '', '[鬼步]Y轴攻击范围 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        char.get_skill_by_name("鬼步").倍率 *= 1.2
        char.单技能加成('魂破斩',1.1)
        char.单技能加成('冥灵断魂斩',1.1)
        char.单技能加成('裂魂乱舞',1.1)
        pass


# 固定装备：胜负之役短剑 - 驭剑士 ， 胜负之役太刀 - 驭剑士 ， 胜负之役钝器 - 驭剑士 ， 胜负之役巨剑 - 驭剑士
def entry_559(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['使用究极魔剑雷沃汀，施放[恶即斩]。', '- [恶即斩]始终以最大蓄气发动', '- [恶即斩]攻击力 +40%', '- [恶即斩]冷却时间 -30%', '- 命中时，增加10%的技能伤害，效果持续20秒', '', '通过雷沃汀施放的[恶即斩]，对敌人造成20秒伤痕。', '- [破军旋舞斩]或[瞬影三绝斩]攻击伤痕状态的敌人时，[恶即斩]技能的剩余冷却时间减少10%。 (各技能每使用1次时仅适用1次)']
    if mode == 0:
        pass
    if mode == 1:
        恶即斩 = char.get_skill_by_name("恶即斩")
        恶即斩.CP武器 = True
        恶即斩.倍率 *= 1.4
        恶即斩.CDR *= 0.7
        char.技能攻击力加成(0.1)
        恶即斩.CD *= 0.9 * 0.9
        pass


# 固定装备：胜负之役短剑 - 契魔者 ， 胜负之役太刀 - 契魔者 ， 胜负之役钝器 - 契魔者 ， 胜负之役巨剑 - 契魔者
def entry_563(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['变更为最多填充3次的技能', '- 从地面召唤的剑 +3个', '- 转职技能攻击时，[蛇腹剑：破]填充1次。 ([蛇腹剑：破]除外)', '- 不自动蓄气。', '', '可强制中断除觉醒技能外的转职技能的施放后僵直并立即发动[蛇腹剑：破]。 (觉醒技能除外)', '', '可强制中断[蛇腹剑：破]的施放后僵直并使用转职技能。']
    if mode == 0:
        char.get_skill_by_name("蛇腹剑：破").hit0 = 0
        char.get_skill_by_name("蛇腹剑：破").hit1 = 6
        char.get_skill_by_name("群魔乱舞").hit0 += 3
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役短剑 - 流浪武士 ， 胜负之役太刀 - 流浪武士 ， 胜负之役钝器 - 流浪武士 ， 胜负之役巨剑 - 流浪武士 ， 胜负之役光剑 - 流浪武士
def entry_567(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放[啸空十字刃]时，追击前方最强敌人后，同时施放水平、垂直斩击。', '', '可强制中断转职技能并施放[啸空十字刃]、[落英惊鸿掌]。', '', '以下技能冷却时间 -20%', '- [一花渡江]', '- [啸空十字刃]', '- [樱花劫]', '- [落英惊鸿掌]']
    if mode == 0:
        char.技能攻击力加成(0.07)
        char.单技能加成('一花渡江', CD=0.8)
        char.单技能加成('啸空十字斩', CD=0.8)
        char.单技能加成('樱花劫', CD=0.8)
        char.单技能加成('落英惊鸿掌', CD=0.8)
        char.单技能加成('莲花剑舞',1.12)
        char.单技能加成('樱花劫',1.12)
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役短剑 - 暗殿骑士 ， 胜负之役太刀 - 暗殿骑士 ， 胜负之役钝器 - 暗殿骑士 ， 胜负之役巨剑 - 暗殿骑士
def entry_571(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '[汲魂之力]灵魂吸收个数上限 +30个', '', '以下技能的额外灵魂吸收数量 +5个', '- [释魂狂怒]', '- [暗影盛宴]', '- [暗影绽放：死亡荆棘]', '', '[释魂飞弹]每发射1个能量消耗的灵魂个数 +2个', '- 追踪攻击最大距离 +20%', '', '[释魂飞弹]每消耗2个灵魂，以下技能的剩余冷却时间减少1%。 (不适用[薄暮]效果)', '- [暗影盛宴]', '- [罚罪之光]', '- [天罚之剑]', '- [暗影绽放：死亡荆棘]', '', '[薄暮]消耗灵魂时附加效果增加率 +50%', '', '[灵魂消耗附加效果适用技能]', '- [神罚 · 灭世裁决]', '- [罚罪之光]', '- [天罚之剑]']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)
        for i in ['天罚死光','神罚·灭世裁决','天罚之剑']:
            skill = char.get_skill_by_name(i)
            # 10->15% 15->20%
            skill.灵魂消耗倍率 += 0.05
        char.get_skill_by_name('释魂飞弹').power0 += 2
        pass


# 固定装备：胜负之役短剑 - 刃影 ， 胜负之役太刀 - 刃影 ， 胜负之役钝器 - 刃影 ， 胜负之役巨剑 - 刃影
def entry_575(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[收刀术]成功连接时，连接的技能与收刀术技能的剩余冷却时间减少15%。', '- 用觉醒技能连接收刀术时，剩余冷却时间不减少。', '', '[鬼缚钉]斩击攻击删除，可强制中断[鬼缚钉]的施放后僵直并连接转职技能。', '- 斩击攻击力合算至踢击攻击力。', '', '可强制中断转职技能并施放[鬼缚钉]。', '- [回旋十字刃]、觉醒技能除外。']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.07)
        char.get_skill_by_name('秘术·曜夜斩').CD *= 0.8 * 0.8
        char.get_skill_by_name('秘术·心斩').CD *= 0.8 * 0.8
        char.get_skill_by_name('秘术·曜夜斩').倍率 *= 1.15
        char.get_skill_by_name('悬丝风暴').倍率 *= 1.15
        pass


# 固定装备：胜负之役手套 - 散打(男) ， 胜负之役臂铠 - 散打(男) ， 胜负之役爪 - 散打(男) ， 胜负之役拳套 - 散打(男) ， 胜负之役东方棍 - 散打(男)
def entry_579(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[双重释放]效果变更为持续15秒的猛烈之焰，技能伤害 +45% (觉醒技能除外)', '- [双重释放]强化攻击力效果不适用', '- 35级以上技能攻击力 +10%', '', '用火焰之力强化[柔化肌肉]。', '- 强制中断攻击时，[双重释放]剩余冷却时间 -3%', '- 强制中断时，转职技能攻击力增加率 +2%，效果持续30秒', '- 强制中断次数 +2次']
    if mode == 0:
        pass
    if mode == 1:
        if pa.cp_striker_male == 1:
            双重释放 = char.get_skill_by_name('双重释放')
            双重释放.hit0 = 0
            双重释放.是否有伤害 = 0
            双重释放.额外倍率 = 1.45
            双重释放.额外倍率1 = 1.1
        char.get_skill_by_name('柔化肌肉').额外加成 = 0.02
        pass


# 固定装备：胜负之役手套 - 气功师(男) ， 胜负之役臂铠 - 气功师(男) ， 胜负之役爪 - 气功师(男) ， 胜负之役东方棍 - 气功师(男)
def entry_583(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[念兽：猛虎震地]的念兽，咆哮后引发爆炸。', '- 咆哮攻击多段攻击次数：4', '- 咆哮攻击力：[念兽：猛虎震地]多段攻击力的100%。', '- 爆炸攻击力：[念兽：猛虎震地]爆炸攻击力的100%', '- 将念兽咆哮命中的敌人吸附。', '- 技能范围 +20%', '', '[禅语·形灭]的念气环绕后爆炸。', '- 施放速度 +20%', '- 球体及爆炸范围 +10%']
    if mode == 0:
        char.技能攻击力加成(0.12)
        char.单技能加成('念兽：猛虎震地',1.2)
        char.单技能加成('禅语·形灭',1.2)
        char.单技能加成('奔雷螺旋击',1.1)
        char.单技能加成('月辉念气破',1.1)
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役手套 - 柔道家(男) ， 胜负之役臂铠 - 柔道家(男) ， 胜负之役爪 - 柔道家(男) ， 胜负之役东方棍 - 柔道家(男)
def entry_587(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[地狱风火轮]下踢时，引发地震，变更为2次蓄气技能。', '- 地震攻击力：下踢攻击力的50%', '- 蓄气冷却时间：12秒 ', '可强制中断[地狱风火轮]的施放后僵直并连接转职技能。', '', '以下技能抓取失败时，该技能冷却时间减少至5秒。 (冷却时间10秒)', '- [无情摔击]', '- [霹雳旋踢]', '- [浮空凌云踢] (地面上使用)', '- [地狱风火轮]', '- [死亡旋律] (地面上使用)', '- 武莲华', '- [黑震旋风]']
    if mode == 0:
        char.技能攻击力加成(0.1)
        char.get_skill_by_name("地狱风火轮").CD = 12
        char.get_skill_by_name("地狱风火轮").power1 = 1.5
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役手套 - 街霸(男) ， 胜负之役臂铠 - 街霸(男) ， 胜负之役爪 - 街霸(男) ， 胜负之役东方棍 - 街霸(男)
def entry_591(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放[狂·霸王拳]时，变更为用火焰瓶炸弹下劈。', '- [狂·霸王拳]终结冲击波删除', '- 对周围敌人造成与抓取敌人相同的伤害。', '- 抓取失败时，同样适用。', '', '[狂 · 霸王拳]添加异常状态效果。', '- 攻击范围：每个异常状态 +10%', '- 冷却时间减少：每个异常状态 +10%']
    if mode == 0:
        char.技能攻击力加成(0.1)
        char.get_skill_by_name('狂·霸王拳').CD缩减 = 1 - 0.1*3
        for i in ['出血', '灼伤', '中毒', '感电']:
            if i not in pa.get_state_type():
                pa.state_type.append(i)
            char.异常时间[i][3] = min(char.异常时间[i][3],3)
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役手套 - 散打(女) ， 胜负之役臂铠 - 散打(女) ， 胜负之役爪 - 散打(女) ， 胜负之役拳套 - 散打(女) ， 胜负之役东方棍 - 散打(女)
def entry_595(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '[闪电之舞]一对一攻击时，在攻击对象左右移动攻击。', '- 攻击力 -15%', '- 攻击速度 +30%', '- 删除角色僵直效果', '- 移动范围 +5%', '- 攻击时，使敌人进入感电状态 (冷却时间15秒)', '', '[闪电之舞]攻击时，生成冲击波。', '- 直接击中的对象不受冲击波攻击', '- 一对一攻击时，不生成冲击波']
    if mode == 0:
        if '感电' not in pa.get_state_type():
            pa.state_type.append('感电')
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)
        闪电之舞 = char.get_skill_by_name("闪电之舞")
        if '闪电之舞' in char.护石栏:
            闪电之舞.hit0 = 17
        else:
            闪电之舞.hit0 = 13
        闪电之舞.倍率 *= 0.85
        pass


# 固定装备：胜负之役手套 - 气功师(女) ， 胜负之役臂铠 - 气功师(女) ， 胜负之役爪 - 气功师(女) ， 胜负之役东方棍 - 气功师(女)
def entry_599(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[蓄念炮]蓄气时间和冷却时间删除。', '', '[念气波]冷却时间增加，但同时增加攻击力和大小。', '- 攻击力 +120%', '- 大小 +20%', '- 冷却时间 +4秒', '- 转职为气功师后，不适用冷却时间减少功能', '', '[念气波]施放时，发动以下效果。', '- [聚能念气炮]剩余冷却时间 -5%', '- 有10%的几率，[念气波]攻击力 +500%', '', '[念兽螺旋波]强化为黄龙形态发射。', '- 攻击力 +20%', '', '[聚能念气炮]强化。', '- 攻击力 +15%', '- 大小 +30%']
    if mode == 0:
        念气波 = char.get_skill_by_name("念气波")
        念气波.CP武器 = True
        念气波.倍率 *= 2.2
        念气波.倍率 *= 1.5
        char.get_skill_by_name("念兽螺旋波").倍率 *= 1.2
        char.get_skill_by_name("聚能念气炮").倍率 *= 1.15
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役手套 - 柔道家(女) ， 胜负之役臂铠 - 柔道家(女) ， 胜负之役爪 - 柔道家(女) ， 胜负之役东方棍 - 柔道家(女)
def entry_603(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['转职技能命中时，获得技术得分。 (最多20分)', '- 1~30级：1分', '- 35~45级：2分', '- 60~80级：2分', '- 50、85、95级：5分', '- 100级：10分', '- 无情抓取连接/空中使用技能时，附加1分', '', '根据技术得分施放效果。', '- 超过11分：50、85、100级技能命中时，所有技能剩余冷却时间减少30%。 (觉醒技能除外 / 消耗所有技术得分)', '- 超过6分：抓取技能攻击失败时，该技能冷却时间减少至3秒。 (消耗3分技术得分)', '- 超过1分：[无情抓取]技能连接时，[无情抓取]恢复时间减少3秒。']
    if mode == 0:
        char.技能攻击力加成(0.16)
        char.单技能加成('裂石破天',1.15)
        char.单技能加成('死亡摇篮',1.15)
        char.单技能加成('末日摇篮',1.15)
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役手套 - 街霸(女) ， 胜负之役臂铠 - 街霸(女) ， 胜负之役爪 - 街霸(女) ， 胜负之役东方棍 - 街霸(女)
def entry_607(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['特定技能攻击时，发动即爆之血，爆发自身出血/中毒/灼伤/感电伤害。', '[发动即爆之血的技能]', '- [擒月炎]摆拳攻击', '-[猛毒擒月炎]摆拳攻击', '- [伏虎霸王拳]终结冲击波攻击', '', '以下技能，每1个异常状态的附加攻击力增加率 +5%', '- [擒月炎]', '- [猛毒擒月炎]', '- [狂霸王拳]']
    if mode == 0:
        for i in ['出血', '灼伤', '中毒', '感电']:
            if i not in pa.get_state_type():
                pa.state_type.append(i)
            char.异常时间[i][3] = min(char.异常时间[i][3],3)
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)
        擒月炎 = char.get_skill_by_name('擒月炎')
        擒月炎.power0 += 0.05*3
        擒月炎.power1 += 0.05*3
        擒月炎.涂毒power0 += 0.05*3
        擒月炎.涂毒power1 += 0.05*3
        猛毒擒月炎 = char.get_skill_by_name('猛毒擒月炎')
        猛毒擒月炎.power0 += 0.05*3
        猛毒擒月炎.power1 += 0.05*3
        猛毒擒月炎.中毒power0 += 0.05*3
        猛毒擒月炎.涂毒power0 += 0.05*3
        猛毒擒月炎.涂毒power1 += 0.05*3
        char.get_skill_by_name('狂·霸王拳').异常倍率 += 0.05*3
        char.单技能加成('连环毒爆弹',1.15)
        char.单技能加成('毒龙轰天雷',1.15)
        char.单技能加成('钻心毒爆',1.15)
        pass
        pass


# 固定装备：胜负之役左轮枪 - 枪炮师(男) ， 胜负之役自动手枪 - 枪炮师(男) ， 胜负之役步枪 - 枪炮师(男) ， 胜负之役手炮 - 枪炮师(男) ， 胜负之役手弩 - 枪炮师(男)
def entry_611(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[激光炮]变更为最多填充3次的技能。', '- 攻击力 +20%', '- 大小 +40%', '- 填充冷却时间：7秒', '- [蓄电激光炮]蓄电时间 -50%', '- 命中时，使敌人进入电磁场10秒。', '', '强化[FM-92刺弹炮]', '- 攻击力 +15%', '- 爆炸范围 +25%', '- 存在电磁场的敌人时，向敌人发射追击的破甲弹。']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        skill = char.get_skill_by_name("激光炮")
        skill.基础施放次数 = 4
        skill.CD = 7
        skill.倍率 *= 1.5
        char.get_skill_by_name("FM92刺弹炮").倍率 *= 1.15
        char.get_skill_by_name("卫星射线").倍率 *= 1.15
        char.单技能加成('毁灭射线',1.15,0.8)
        pass


# 固定装备：胜负之役左轮枪 - 机械师(男) ， 胜负之役自动手枪 - 机械师(男) ， 胜负之役步枪 - 机械师(男) ， 胜负之役手炮 - 机械师(男) ， 胜负之役手弩 - 机械师(男)
def entry_615(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[机械引爆]引爆机器人时，生成R-步行者。', '- R-步行者攻击力：RX-78追击者攻击力的50%', '- 适用[机械引爆]的爆炸伤害变化率效果。', '- 最多生成10个。', '', '[R-步行者生成技能]', '- RX-78追击者', '- EZ-8爆破者', '- RX-60陷阱追击者', '- [空战机械：风暴]', '- [空投支援]', '- [拦截机工厂]', '- EZ-10反击者', '- TX-45 特攻队', '', '[RX-78追击者]攻击力 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("RX78追击者").CP倍率 = 0.5
        char.get_skill_by_name("RX78追击者").追加 = 2
        char.get_skill_by_name("Ez8自爆者").追加 = 1
        char.get_skill_by_name("RX60陷阱追击者").追加 = 1
        if "空战机械：风暴" not in char.护石栏:
            char.get_skill_by_name("空战机械：风暴").追加 = 1
        char.get_skill_by_name("空投支援").追加 = 10
        if char.get_skill_by_name("光反应能量模块").等级 > 0:
            char.get_skill_by_name("拦截机工厂").追加 = 1
        else:
            char.get_skill_by_name("拦截机工厂").追加 = 8
        char.get_skill_by_name("EZ10反击者").追加 = 4
        char.get_skill_by_name("TX-45特攻队").追加 = 5
        char.get_skill_by_name("RX78追击者").倍率 *= 1.05

        char.技能攻击力加成(0.07)
        char.单技能加成('HS1全息机械猎手',1.1,0.8)
        char.单技能加成('拦截机工厂',1.1)
        char.单技能加成('空投支援',1.1)
        pass


# 固定装备：胜负之役左轮枪 - 漫游枪手(男) ， 胜负之役自动手枪 - 漫游枪手(男) ， 胜负之役步枪 - 漫游枪手(男) ， 胜负之役手炮 - 漫游枪手(男) ， 胜负之役手弩 - 漫游枪手(男)
def entry_619(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['强化[双鹰回旋]。', '- 成功抓取第三把鹰枪时，投掷第二把鹰枪后，使用技能的剩余冷却时间减少20%。', '- 鹰枪大小 +10%', '- 施放[双鹰回旋]时，增加30%的攻击速度，效果持续4秒。', '', '[花式枪术]可强制中断次数上限 +1', '', '穿戴时，生成光谱。']
    if mode == 0:
        char.技能攻击力加成(0.12)
        char.单技能加成('双鹰回旋',1.2,0.7)
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役左轮枪 - 弹药专家(男) ， 胜负之役自动手枪 - 弹药专家(男) ， 胜负之役步枪 - 弹药专家(男) ， 胜负之役手炮 - 弹药专家(男) ， 胜负之役手弩 - 弹药专家(男)
def entry_623(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +15%', '', '[聚合弹]变更为轰炸最强的敌人。', '- 施放其他技能时，可以无施放动作发动', '', '[重火力支援]炮弹生成个数 +100%', '[重火力支援]炮弹攻击力 -30%', '', '适用[超负荷装填]期间，施放10次基本攻击或施放35级以上无色小晶块技能时，填充强化弹药。 (最多3个)', '- 进入地下城时，装填1个弹药', '', '施放[聚合弹]、[凝固汽油弹]、[重火力支援]时，消耗强化弹药，强化技能。', '[聚合弹]', '- 攻击力 +80%', '[凝固汽油弹]', '- 攻击力 +20%', '[重火力支援]', '- 炮弹下落间隔 -50%', '- 爆炸范围 +30%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.15)
        聚合弹 = char.get_skill_by_name("聚合弹")
        聚合弹.倍率 *= 1.8
        聚合弹.CP武器 = True
        char.get_skill_by_name("凝固汽油弹").倍率 *= 1.2
        char.get_skill_by_name("重火力支援").倍率 *= 2 * 0.7
        pass


# 固定装备：胜负之役左轮枪 - 枪炮师(女) ， 胜负之役自动手枪 - 枪炮师(女) ， 胜负之役步枪 - 枪炮师(女) ， 胜负之役手炮 - 枪炮师(女) ， 胜负之役手弩 - 枪炮师(女)
def entry_627(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放[聚焦喷火器]时，压缩火焰后发射，变更为最多填充3次的技能。', '- 攻击力：总攻击力的50%', '- 填充冷却时间：4秒', '', '施放[M-3喷火器]时，压缩火焰后发射。', '', '[UHT-03爆炎喷火器]移动速度增加率 +10%']
    if mode == 0:
        char.技能攻击力加成(0.1)
        skill = char.get_skill_by_name('聚焦喷火器')
        skill.CD = 4
        skill.基础施放次数 = 3
        skill.倍率 *= 0.8
        char.单技能加成('FSC7',1.2)
        char.单技能加成('UHT-03爆炎喷火器',1.2)
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役左轮枪 - 机械师(女) ， 胜负之役自动手枪 - 机械师(女) ， 胜负之役步枪 - 机械师(女) ， 胜负之役手炮 - 机械师(女) ， 胜负之役手弩 - 机械师(女)
def entry_631(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '[G-超级猎鹰]攻击力 +15%', '[G-超级猎鹰]冷却时间 -20%', '', '[G-0战争领主]攻击力 +20%', '', '[G-X星尘天穹]攻击力 +20%', '', '[G-1科罗纳]状态下，改装为旋雷者或捕食者时，生成全息G-1科罗纳，效果持续8秒。', '- 攻击力：[G-1科罗纳]攻击力的50%', '- 施放[G-磁力弹]时，由全息G-1科罗纳代替施放', '', '[改装：G-2旋雷者]强化。', '- 数量 +2个', '- 填充冷却时间 -0.5秒', '', '[改装：G-3捕食者]发射强化激光。', '- 攻击力 +5%', '- 缠住敌人的捕食者个数上限 +2个', '- 数量 +1个']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)
        char.get_skill_by_name("G3捕食者").倍率 *= 1.05*1.5
        char.get_skill_by_name("G2旋雷者").倍率 *= 1.5
        char.get_skill_by_name("GSP猎鹰").CDR *= 0.8
        char.get_skill_by_name("GSP猎鹰").倍率 *= 1.15
        char.get_skill_by_name("G0战争领主").倍率 *= 1.2
        char.get_skill_by_name("G-X星尘天穹").倍率 *= 1.2
        pass


# 固定装备：胜负之役左轮枪 - 漫游枪手(女) ， 胜负之役自动手枪 - 漫游枪手(女) ， 胜负之役步枪 - 漫游枪手(女) ， 胜负之役手炮 - 漫游枪手(女) ， 胜负之役手弩 - 漫游枪手(女)
def entry_635(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[移动射击]子弹爆裂，造成更大范围的伤害。', '- 攻击力 +30%', '- 发射次数 +50%', '- 冷却时间 -20%', '- 攻击范围 +10%', '', '施放[移动射击]时，适用以下效果。', '- 施放技能时，立即适用冷却时间。', '- 攻击速度 +30%', '- 移动速度 +30%', '- 切换地下城房间时，保留技能效果。']
    if mode == 0:
        char.技能攻击力加成(0.1)
        char.单技能加成('移动射击', 1.5*1.7)
        char.单技能加成('移动射击', 1, 0.75)
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役左轮枪 - 弹药专家(女) ， 胜负之役自动手枪 - 弹药专家(女) ， 胜负之役步枪 - 弹药专家(女) ， 胜负之役手炮 - 弹药专家(女) ， 胜负之役手弩 - 弹药专家(女)
def entry_639(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[G-14手雷]、[G-35L感电手雷]、[G-18C冰冻手雷]技能强化。', '- 最大装填数 +2', '- 跳跃状态下施放时，不消耗单兵推进器。', '', '', '消耗手雷，强化[光子霰雷发射器]。', '- 每消耗1个手雷，攻击力增加2%。 (最多30%)', '- [空袭战略]期间，将发射最大强化数值的[光子霰雷发射器]。']
    if mode == 0:
        char.技能攻击力加成(0.08)
        char.所有速度增加(0.1,'武器')
        char.get_skill_by_name("G35感电手雷").基础施放次数 += 2
        char.get_skill_by_name("G18冰冻手雷").基础施放次数 += 2
        char.单技能加成('光子霰雷发射器', 1.3)
        char.单技能加成('凝固汽油弹',1.25)
        char.单技能加成('超真空弹：切利',1.25)
        char.单技能加成('空袭战略',CD=0.85)
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役矛 - 冰结师 ， 胜负之役棍棒 - 冰结师 ， 胜负之役魔杖 - 冰结师 ， 胜负之役法杖 - 冰结师
def entry_643(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[冰之技艺]冰霜矛追击被冰霜武器命中的所有敌人并且贯穿。', '- 冰霜矛攻击力反应率额外增加20%。', '- 冰霜矛爆炸功能删除。', '- 冰霜矛有10%的几率使敌人进入冰冻状态2秒。', '', '[冰舞乱击]追击前方最强敌人，同时攻击周围敌人。', '- 追击范围：500px']
    if mode == 0:
        char.技能攻击力加成(0.1)
        char.get_skill_by_name("冰之技艺").额外冰枪攻击力 += 2
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役矛 - 元素爆破师 ， 胜负之役棍棒 - 元素爆破师 ， 胜负之役魔杖 - 元素爆破师 ， 胜负之役法杖 - 元素爆破师
def entry_647(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放[元素炮]时，发射的元素炮变更为向前方爆炸的深渊炮。', '- 攻击力 +50%', '- 冷却时间 +5秒', '- 施放其他技能期间也可以施放', '', '施放[元素炮]时，仅消耗1个元素之力。', '- 每消耗1个元素之力，[元素炮]攻击力增加量 +50%', '', '施放35级以上技能时，消耗1个元素之力，技能伤害 +18%，效果持续10秒。', '', '施放[元素炮]时，技能冷却时间恢复速度 +30%，效果持续20秒。 (觉醒技能除外)', '', '施放[聚能魔炮]、[聚魔轰击]技能时，[元素炮]技能的冷却时间初始化。']
    if mode == 0:
        pass
    if mode == 1:
        元素炮 = char.get_skill_by_name("元素炮")
        元素炮.倍率 *= 1.5
        元素炮.CD += 5
        char.get_skill_by_name("元素之力").额外倍率 += 0.5
        char.get_skill_by_name("元素之力").层数 = 1
        char.技能恢复加成(1, 100, 0.3, excName=char.觉醒技能)
        char.技能攻击力加成(0.18)
        pass


# 固定装备：胜负之役矛 - 逐风者 ， 胜负之役棍棒 - 逐风者 ， 胜负之役魔杖 - 逐风者 ， 胜负之役法杖 - 逐风者
def entry_651(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[狂风冲刺]变更为最多填充3次的技能。', '', '施放[狂风冲刺]时，生成[游离之风]，并增加10%的技能伤害，效果持续20秒。', '-  [狂风冲刺]的游离之风攻击力：[游离之风]攻击力的50%。', '', '[游离之风]大小 +10%']
    if mode == 0:
        char.get_skill_by_name("游离之风").CP倍率 = 0.5
        char.技能攻击力加成(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役矛 - 血法师 ， 胜负之役棍棒 - 血法师 ， 胜负之役魔杖 - 血法师 ， 胜负之役法杖 - 血法师
def entry_655(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['使用部分技能攻击时，获得猩红之眼。', '- [隐行之噬]：获得5个', '- 吸收系技能：获得1个', '- 进入地下城时获得1个', '', '拥有猩红之眼时，技能伤害 +15%', '施放[猩红狩猎]、 [绯红之狱]时，消耗1个猩红之眼，分别强化为[致命狩猎]、[血腥地狱]。', '', '[致命狩猎]', '- [猩红狩猎]攻击力 +50%', '- [猩红狩猎]冷却时间 -30%', '- 变更为单次攻击', '- 攻击500px范围内所有敌人', '', '[血腥地狱]', '- [绯红之狱]攻击力 +50%', '- [绯红之狱]冷却时间 -30%', '- 施放后可以移动', '', '[隐行之噬]冷却时间 -10%，施放速度 +30%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("狱血之噬").CDR *= 0.9
        char.技能攻击力加成(0.15)
        char.get_skill_by_name("血腥狩猎").倍率 *= 1.5
        char.get_skill_by_name("血腥狩猎").CDR *= 0.7
        char.get_skill_by_name("血腥炼狱").倍率 *= 1.5
        char.get_skill_by_name("血腥炼狱").CDR *= 0.7
        pass


# 固定装备：胜负之役矛 - 次元行者 ， 胜负之役棍棒 - 次元行者 ， 胜负之役魔杖 - 次元行者 ， 胜负之役法杖 - 次元行者 ， 胜负之役扫把 - 次元行者
def entry_659(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +15%', '', '[次元：粒子风暴]技能强化。', '- 攻击力 +35%', '- 爆炸速度 +50%', '- 技能范围 +25%', '- 适用[次元边界]效果时，向前方生成多个次元爆炸', '', '奈雅丽施放技能时，生成分身代替施放技能。 (觉醒技能除外)', '', '以下技能攻击力增加25%，冷却时间减少10%。', '- [乖离：魅魔之舞]', '- [乖离：异界蜂群]', '- [乖离：禁锢]', '- [乖离：沉沦]', '- [乖离：边缘之兽]']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.15)
        char.get_skill_by_name("次元：粒子风暴").倍率 *= 1.35
        for skill in ["乖离：魅魔之舞","乖离：异界蜂群","乖离：禁锢","乖离：沉沦","乖离：边缘之兽"]:
            char.get_skill_by_name(skill).CDR *= 0.9
            char.get_skill_by_name(skill).倍率 *= 1.25
        pass


# 固定装备：胜负之役矛 - 魔道学者 ， 胜负之役棍棒 - 魔道学者 ， 胜负之役魔杖 - 魔道学者 ， 胜负之役法杖 - 魔道学者 ， 胜负之役扫把 - 魔道学者
def entry_663(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[超级棒棒糖]生成更多的糖果人偶。', '- 糖果人偶生成个数上限 +5', '- 每命中1名敌人，使人偶生成数增加2个。', '- 每生成一个糖果人偶，[超级棒棒糖]的剩余冷却时间减少3%。', '- 糖果人偶攻击力 -20%', '', '吸收未爆炸的糖果人偶，下一次施放[超级棒棒糖]时生成。 (最多15个)', '- 每一个糖果人偶只能吸收一次。', '- 额外生成的糖果人偶不包含在糖果生成数量上限中。']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        超级棒棒糖 = char.get_skill_by_name('超级棒棒糖')
        超级棒棒糖.CD *= 1 - (0.09 * 3)
        超级棒棒糖.hit1 = pa.cp_witch_1
        超级棒棒糖.hit2 = pa.cp_witch_2 + 3
        超级棒棒糖.power1 = 0.8
        超级棒棒糖.power2 = 0.8
        pass


# 固定装备：胜负之役矛 - 战斗法师 ， 胜负之役棍棒 - 战斗法师 ， 胜负之役魔杖 - 战斗法师 ， 胜负之役法杖 - 战斗法师
def entry_667(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['增加炫纹攻击力和发射数量。', '- 一次发射的炫纹数量 +2', '- 攻击力 -45%', '- 连击50次以上时，自动发动炫纹发射。', '- 炫纹生成数量上限 +1', '- 炫纹大小比率 +20%', '- 技能魔法值消耗量 -70%', '', '一次性生成的炫纹数量 +1']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name('炫纹发射').倍率 *= 0.65
        char.get_skill_by_name('炫纹发射').hit0 += 2
        char.技能攻击力加成(0.17)
        char.单技能加成('炫纹强压',1.15)
        char.单技能加成('超级炫纹',1.15)
        char.单技能加成('炫纹簇',1.15)
        pass


# 固定装备：胜负之役矛 - 元素师 ， 胜负之役棍棒 - 元素师 ， 胜负之役魔杖 - 元素师 ， 胜负之役法杖 - 元素师
def entry_671(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['把一个高级元素技能或部分特级元素技能储存在符文中并释放。', '- 输入[装备属性指令]后，施放技能时，储存在符文中60秒。', '- 再次输入[装备属性指令]时，发动储存的技能。 (冷却时间0.1秒)', '- 释放技能攻击力：原技能攻击力的15%', '- 储存技能冷却时间：原技能的15%', '- 储存的技能为最大蓄气状态', '', '[魔法记忆]施放速度提升率 +15%', '', '<可以存储的技能>', '- 天雷', '- 极冰盛宴', '- 湮灭黑洞', '- 杰克降临', '- 元素之幕', '- 元素震荡', '- 圣灵水晶']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.11)
        char.cp_power = 0.15
        char.cp_cd = 0.15
        char.单技能加成('圣灵水晶',1.15)
        char.单技能加成('元素之门',1.15)
        pass


# 固定装备：胜负之役矛 - 召唤师 ， 胜负之役棍棒 - 召唤师 ， 胜负之役魔杖 - 召唤师 ， 胜负之役法杖 - 召唤师
def entry_675(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['上级精灵与精灵王伊伽贝拉的[蚀月附灵]追加操作模式攻击力增加20%。', '', '强化[蚀月附灵]。', '- 技能追加操作模式删除施放动作。', '- 亡魂默克尔：施放黑雾，可强制控制敌人。', '- 极光格雷林：施放落雷，可吸附敌人。', '- 冰影阿奎利斯：发射七重冰导弹。', '- 火焰赫瑞克：火焰爆剑术生成旋涡，可吸附敌人。', '- 伊伽贝拉：发射超高密度镭射光变更为多个激光轰炸地面']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)
        char.get_skill_by_name("精灵召唤：亡魂默克尔").power_f0 = 1.25
        char.get_skill_by_name("精灵召唤：冰影阿奎利斯").power_f0 = 1.25
        char.get_skill_by_name("精灵召唤：极光格雷林").power_f0 = 1.25
        skill = char.get_skill_by_name("精灵召唤：火焰赫瑞克")
        skill.power_f0 = 1.25
        skill.power_f1 = 1.25
        skill.power_f2 = 1.25
        skill.power_f3 = 1.25
        char.get_skill_by_name("精灵召唤：伊伽贝拉").power_f0 = 1.25
        char.单技能加成('狂化黑月',1.15)
        char.单技能加成('传说召唤：月蚀之影',1.1)
        char.单技能加成('至高精灵王',1.1)
        pass


# 固定装备：胜负之役矛 - 小魔女 ， 胜负之役棍棒 - 小魔女 ， 胜负之役魔杖 - 小魔女 ， 胜负之役法杖 - 小魔女 ， 胜负之役扫把 - 小魔女
def entry_679(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[禁术吟咏]效果 +8%', '- 解除穿戴时，效果消失', '- 在增益效果强化装备栏穿戴时不适用该效果', '', '[细心缝补]技能范围 +20%', '', '删除[哇咔咔！]施放动作。', '[哇咔咔！]吸附范围 +10%', '', '[咆哮吧！疯疯熊]诅咒吐息向命中的敌人赋予诅咒之息，并发生爆炸。', '- 爆炸伤害：[咆哮吧！ 疯疯熊]诅咒吐息总攻击力的50%。', '', '[冥月绽放]的独立攻击力增加量额外增加20%', '', '解除穿戴时，辅助职业50级技能增益效果 -50%']
    if mode == 0:
        if char.bufferCarry:
            char.get_skill_by_name('冥月绽放').额外倍率 = 0.2
            char.get_skill_by_name('咆哮吧！疯疯熊').power0 *= 1.5
        buff = char.get_skill_by_name('BUFF')
        buff.倍率 *= 1.08
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役十字架 - 圣骑士(男) ， 胜负之役念珠 - 圣骑士(男) ， 胜负之役图腾 - 圣骑士(男) ， 胜负之役镰刀 - 圣骑士(男) ， 胜负之役战斧 - 圣骑士(男)
def entry_683(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[荣誉祝福]效果 +8%', '- 解除穿戴时，效果消失', '- 在增益效果强化装备栏穿戴时不适用该效果', '', '[缓慢愈合]技能范围 +20%', '', '施放[正义审判]时，召唤光晕，对范围内的10名敌人进行追击并发射正义之矛后爆炸。', '- 正义之矛攻击力：光之刃攻击力的1600%', '- 正义之矛爆炸攻击力：魔法阵持续时间达上限时终结攻击力的100%', '- 可以在施放其他技能时使用该技能。', '', '[圣光突袭]技能攻击力 +20%', '- 前冲距离 -70%', '', '[圣光沁盾]生命值 +400%', '- 技能不移动。', '', '单人挑战时，独立攻击力 +20%', '', '解除穿戴时，辅助职业50级技能增益效果 -50%']
    if mode == 0:
        if char.类型 == '辅助':
            buff = char.get_skill_by_name("BUFF")
            buff.倍率 *= 1.08
        char.get_skill_by_name("圣光突袭").倍率 *= 1.2
        char.单技能加成('圣光沁盾',1.2)
        char.单技能加成('神圣之光',1.1)
        char.单技能加成('圣佑结界',1.1)
        char.get_skill_by_name("正义审判").hit0 = 1
        char.get_skill_by_name("正义审判").power0 = 16
        char.技能攻击力加成(0.16)
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役十字架 - 驱魔师 ， 胜负之役念珠 - 驱魔师 ， 胜负之役图腾 - 驱魔师 ， 胜负之役镰刀 - 驱魔师 ， 胜负之役战斧 - 驱魔师
def entry_687(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '前冲施放[无双击]时，向前方突进施放。', '[式神：白虎]魔法珠大小比率 +50%', '', '[落雷符]技能攻击力 +20%', '[落雷符]范围 +20%', '', '[无双击]攻击力 +60%', '[无双击]范围 +20%', '[脉轮：圣光]适用期间，[无双击]技能攻击力 +20%', '', '[狂乱锤击]技能效果强化。', '- 删除[狂乱锤击]最后一击，最后一击攻击力合算至狂乱锤击攻击力。', '- [狂乱锤击]次数 +100%', '- 技能攻击力 +20%', '- 冷却时间 -20%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)
        char.get_skill_by_name("式神：空之白虎").倍率 *= 1.2
        skill = char.get_skill_by_name("无双击")
        skill.倍率 *=1.6
        狂乱锤击 = char.get_skill_by_name("狂乱锤击")
        狂乱锤击.hit0 = 8
        狂乱锤击.hit1 = 1
        狂乱锤击.hit2 = 1
        狂乱锤击.倍率 *= 1.2
        狂乱锤击.CDR *= 0.8
        pass


# 固定装备：胜负之役十字架 - 蓝拳圣使 ， 胜负之役念珠 - 蓝拳圣使 ， 胜负之役图腾 - 蓝拳圣使 ， 胜负之役镰刀 - 蓝拳圣使 ， 胜负之役战斧 - 蓝拳圣使
def entry_691(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[正义执行：雷米迪奥斯的圣座]关联技能为[泯灭神击]时，[制裁：怒火疾风]变更为最多填充3次的技能。', '- 连击攻击力增加100%', '- 连击次数减少9次', '- 删除终结攻击和爆炸', '- 追踪敌人进行攻击', '- 填充冷却时间：40秒', '- 追击范围：780px', '- 魔法值消耗量 -30%', '- 无色小晶块消耗量 -5个', '- 使用[刺拳猛击]技能时，[制裁：怒火疾风]技能的剩余冷却时间 -12%', '- 可强制中断[制裁：怒火疾风]并施放转职技能。', '- 强制中断转职技能并施放[制裁：怒火疾风]时，不消耗[干涸之泉]能量。']
    if mode == 0:
        for skill in char.技能队列:
            if skill["名称"] == "制裁：怒火疾风":
                skill["无色消耗"] -= 5
        pass
    if mode == 1:
        char.技能攻击力加成(0.08)
        觉醒 = char.get_skill_by_name("制裁：怒火疾风")
        觉醒.CD = 35
        觉醒.无色消耗 = 5
        觉醒.power0 = 2.5
        觉醒.hit0 = 10
        觉醒.hit1 = 0
        觉醒.hit2 = 0
        觉醒.MP = [int(i*0.7) for i in 觉醒.MP]
        char.单技能加成('正义铁拳',1.25)
        pass


# 固定装备：胜负之役十字架 - 复仇者 ， 胜负之役念珠 - 复仇者 ， 胜负之役图腾 - 复仇者 ， 胜负之役镰刀 - 复仇者 ， 胜负之役战斧 - 复仇者
def entry_695(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[魔化：末日守卫者]状态下，恶魔能量条超过30时，消耗恶魔能量的技能攻击时，额外消耗40点发动恶魔之爪。 (觉醒技能除外)', '- [恶魔之力]的攻击力的2000%', '', '[魔化：末日守卫者]基本攻击与技能的恶魔能量恢复量 +10%', '[化魔]恶魔能量恢复量 +10%', '', '[魔化：末日守卫者]攻击速度增加量 +20%，移动速度增加量 +10%']
    if mode == 0:
        char.技能攻击力加成(0.08)
        char.get_skill_by_name('恶魔之力').CP倍率 += 26
        pass
    if mode == 1:
        # char.get_skill_by_name('恶魔之力').CP倍率 += 5
        pass


# 固定装备：胜负之役十字架 - 圣骑士(女) ， 胜负之役念珠 - 圣骑士(女) ， 胜负之役图腾 - 圣骑士(女) ， 胜负之役镰刀 - 圣骑士(女) ， 胜负之役战斧 - 圣骑士(女)
def entry_699(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[勇气祝福]效果 +8%', '- 解除穿戴时，效果消失', '- 在增益效果强化装备栏穿戴时不适用该效果', '', '[治愈祈祷]治愈范围 +20%', '', '[圣洁之光]贯穿敌人，先前移动300px后爆发。', '- 攻击力 +100%', '- 技能范围 +10%', '', '[圣洁之光]技能命中敌人时，[神光十字]和[忏悔重击]剩余冷却时间减少2%。', '', '[圣光灌注]的独立攻击力增加量 +20%', '', '解除穿戴时，辅助职业50级技能增益效果 -50%']
    if mode == 0:
        if char.类型 == '辅助':
            buff = char.get_skill_by_name("BUFF")
            buff.倍率 *= 1.08
        if char.bufferCarry:
            char.get_skill_by_name('圣光灌注').额外倍率 += 0.2
            char.get_skill_by_name('圣洁之光').倍率 *= 2
        pass
    if mode == 1:
        pass


# 固定装备：胜负之役十字架 - 诱魔者 ， 胜负之役念珠 - 诱魔者 ， 胜负之役图腾 - 诱魔者 ， 胜负之役镰刀 - 诱魔者 ， 胜负之役战斧 - 诱魔者
def entry_703(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[原罪释放·净化]变身状态下，[诱魔之手]命中时，变身持续时间 +12秒', '- 不能超过最大变身持续时间', '', '施放[暴食之噬]时，以自身为中心吸附敌人并在周围爆发。', '- 攻击力 +30%', '- 罪业层数超过3个时，消耗3个罪业层数，分身代替施放。', '', '罪业层数超过3个时，施放[罪业加身]技能，会消耗3个罪业层数并减少15%物理/魔法所受伤害，持续10秒。', '', '[原罪释放·净化]状态下，控制[罪业加身]时间 +1秒', '', '[诱魔之手]罪业层数增加量 +2']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name('暴食之噬').倍率 *= 1.6
        char.技能攻击力加成(0.1)
        char.单技能加成('灵魂烙印：原罪冲击',1.1)
        char.单技能加成('肋骨重塑：原罪战矛',1.1)
        char.单技能加成('至高之刑',1.1)
        pass


# 固定装备：胜负之役十字架 - 异端审判者 ， 胜负之役念珠 - 异端审判者 ， 胜负之役图腾 - 异端审判者 ， 胜负之役镰刀 - 异端审判者 ， 胜负之役战斧 - 异端审判者
def entry_707(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[神焰洗礼]、[净化之焰]技能冷却时间 -20%', '', '施放[净化之焰]时，对500px范围内所有敌人产生爆炸。', '', '[火焰精华]变更为最多填充5次的技能。', '- 冷却时间：8秒', '- 发动焚烧时，填充时间 -1秒']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.18)
        char.get_skill_by_name('火焰精华').CD = 8
        char.get_skill_by_name('火焰精华').CD固定缩减 = 1
        char.get_skill_by_name('神焰洗礼').CDR *= 0.8
        char.get_skill_by_name('净化之焰').CDR *= 0.8
        char.get_skill_by_name('神焰').CDR *= 0.7
        char.单技能加成('逆罪灭绝',1.1)
        char.单技能加成('裁决轮回斩',1.1)
        char.单技能加成('车轮刑',1.1)
        pass


# 固定装备：胜负之役十字架 - 巫女 ， 胜负之役念珠 - 巫女 ， 胜负之役图腾 - 巫女 ， 胜负之役镰刀 - 巫女 ， 胜负之役战斧 - 巫女
def entry_711(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[念珠连射]、[木槵子经]攻击1次时，获得1个神力念珠。 (最多获得25个)', '', '施放以下技能时，消耗神力念珠进行强化。', '- 不动珠箔阵：念珠旋转次数 +1 (消耗8个)', '- 百八念珠：念珠连射个数 +10 (消耗10个)', '- 退魔阴阳符：弹跳次数 +3 (消耗10个)', '- 天坠阴阳玉：念珠坠落个数 +1 (消耗15个)', '', '每施放1次[念珠连射]、[木槵子经]， [百八念珠]、[不动珠箔阵]的技能冷却时间恢复速度增加1%。', '- 施放[百八念珠]、[不动珠箔阵]时，效果初始化。']
    if mode == 0:
        char.技能攻击力加成(0.08)
        pass
    if mode == 1:
        char.get_skill_by_name('不动珠箔阵').hit0 += 8
        char.单技能加成("木槵子经",CD=0.5)
        百八念珠 = char.get_skill_by_name('百八念珠')
        百八念珠.power0 *= 30/20
        百八念珠.power1 *= 20/10
        char.get_skill_by_name('退魔阴阳符').hit1 += 3
        char.get_skill_by_name('天坠阴阳玉').倍率 *= 2
        pass


# 固定装备：胜负之役匕首 - 死灵术士 ， 胜负之役双剑 - 死灵术士 ， 胜负之役手杖 - 死灵术士
def entry_715(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[降临：莱迪娅]变更为最多填充3次的技能。', '', '直接引发爆炸。', '- 攻击力：[降临：莱迪娅]总攻击力的60%', '- 填充冷却时间：15秒', '- 向敌人生成恐怖之烙印，增加10%的技能伤害，效果持续20秒', '- 删除追加操作功能', '', '对带有恐怖之烙印的敌人使用以下技能攻击时，该技能的攻击力增加10%。', '- [巴拉克的野心]', '- [巴拉克的愤怒]', '- [复苏者之缚]', '- [怨噬之沼]', '- [暗黑蛛丝引]', '- [暴君湮灭斩]', '- [亡者之茧]']
    if mode == 0:
        pass
    if mode == 1:
        莱迪娅 = char.get_skill_by_name("降临：僵尸莱迪娅")
        莱迪娅.基础施放次数 = 3
        莱迪娅.倍率 *= 0.6
        莱迪娅.CD = 15
        char.get_skill_by_name("降临：僵尸莱迪娅").CP武器 = True
        char.技能攻击力加成(0.1)
        for skill in ['巴拉克的野心','巴拉克的愤怒','死灵之缚','怨噬之沼','暗黑蛛丝引','暴君极刑斩','亡者之茧']:
            char.get_skill_by_name(skill).倍率 *= 1.1
        pass


# 固定装备：胜负之役匕首 - 刺客 ， 胜负之役双剑 - 刺客 ， 胜负之役手杖 - 刺客
def entry_719(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放[剑刃风暴]时，技能伤害 +10%，效果持续15秒。', '', '[剑刃风暴]变更为最多填充3次的技能。', '- 每次攻击获得连击点数 +900%', '- 可获得连击点数上限 +100%', '- 移动速度 +30%', '- 吸附力 +30%', '', '施放[剑刃风暴]期间施放[终结之击]时，适用以下效果。', '- 合计[剑刃风暴]剩余伤害进行攻击', '- 向最强敌人发射剩余匕首', '', '[死亡风暴]发射的匕首可贯穿敌人，发射的匕首个数 -10个']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)
        char.get_skill_by_name('死亡风暴').CP武器 = True
        pass


# 固定装备：胜负之役匕首 - 忍者 ， 胜负之役双剑 - 忍者 ， 胜负之役手杖 - 忍者 ， 胜负之役苦无 - 忍者
def entry_723(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[忍法：残影术]每消耗1个残影，记录的[忍法：六道轮回]残影攻击力比率增加3%。 (最多叠加6次)', '', '施放[忍法：六道轮回]时，以下技能攻击力增加20%，效果持续20秒。 (冷却时间10秒)', '- [火遁·炎舞天璇]', '- [火遁·风魔手里剑]', '- [八岐大蛇]', '- [天照]', '- [勾玉之火：镰鼬]', '', '[勾玉之火：镰鼬]最后一击命中时，合并计算的灼伤伤害 +10%']
    if mode == 0:
        char.get_skill_by_name('勾玉之火·镰鼬').结算加成 = 1.15
        pass
    if mode == 1:
        char.get_skill_by_name("忍法：残影术").额外倍率 += 6*0.03
        char.get_skill_by_name('火遁·炎舞天璇').倍率 *= 1.25
        char.get_skill_by_name('火遁·风魔手里剑').倍率 *= 1.25
        char.get_skill_by_name('八岐大蛇').倍率 *= 1.25
        char.get_skill_by_name('天照').倍率 *= 1.25
        char.get_skill_by_name('勾玉之火·镰鼬').倍率 *= 1.25
        pass


# 固定装备：胜负之役匕首 - 影舞者 ， 胜负之役双剑 - 影舞者 ， 胜负之役手杖 - 影舞者
def entry_727(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['背击时，获得暗影之痕。', '- 获得2个暗影之痕。 (最多50个)', '- 正面攻击时，减少3个暗影之痕。', '', '[摧心]背后抽取时，消耗所有暗影之痕，强化攻击力。', '- 每消耗一个暗影之痕，攻击力 +1% (最多50%)', '', '施放[摧心]时，进入隐身状态15秒，技能冷却时间恢复速度 +12%。 (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name('剜心').倍率 *= 1.5
        char.技能恢复加成(1, 100, 0.2, excName=char.觉醒技能)
        pass


# 固定装备：胜负之役短剑 - 混沌魔灵 ， 胜负之役太刀 - 混沌魔灵 ， 胜负之役钝器 - 混沌魔灵 ， 胜负之役巨剑 - 混沌魔灵
def entry_731(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[魔能榨取]的基本/技能攻击力增加量 +15%', '', '施放[碎灵之击]时，魔灵爆炸变更为亚丁的化身召唤魔灵战士幻影并引发爆炸。', '- 攻击力 +30%', '- 冷却时间 -10%', '- 技能范围 +20%', '- 施放[碎灵之击]技能期间，可以施放[午夜嘉年华]', '- 没有魔灵时，立即召唤所有魔灵']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("碎灵屠戮").倍率 *= 1.3
        char.get_skill_by_name("碎灵屠戮").CDR *= 0.9
        char.get_skill_by_name("魔能榨取").CP武器 = True
        pass


# 固定装备：胜负之役短剑 - 帕拉丁 ， 胜负之役太刀 - 帕拉丁 ， 胜负之役钝器 - 帕拉丁 ， 胜负之役巨剑 - 帕拉丁
def entry_735(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['消耗[天使光翼]，施放[惩罚之锤]技能时，发动额外效果。', '- 每消耗1个[天使光翼]，攻击力增加4%。', '- 每消耗1个[天使光翼]，技能范围增加3%。', '- 使敌人进入眩晕状态。', '', '消耗[天使光翼]，施放[神光冲击]技能时，发动额外效果。', '- 强制控制2秒吸附的敌人。', '- 聚怪效果范围适用为6阶段', '- 聚怪效果范围 +20%', '- [天使光翼]最多消耗2个。', '', '[神光冲击]强化', '- 技能范围 +20% ', '- 击中成功时，[天使光翼]获得数量 +2', '- 对进入挑衅状态的敌人，保持防御状态时，[天使光翼]获得时间减少50%。']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.08)
        char.get_skill_by_name("神罚之锤").倍率 *= 1 + 0.06*8
        char.单技能加成('神光冲击',1.3)
        char.单技能加成('神光回旋斩',1.15)
        char.单技能加成('神光耀世',1.15)
        pass


# 固定装备：胜负之役短剑 - 龙骑士 ， 胜负之役太刀 - 龙骑士 ， 胜负之役钝器 - 龙骑士 ， 胜负之役巨剑 - 龙骑士
def entry_739(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[龙刃无双]变更为最多填充2次的技能。', '- 攻击力 -40%', '- 填充冷却时间：10秒', '', '施放[龙刃无双]时，增加5%的技能攻击力，效果持续10秒。 (最多叠加1次，觉醒技能除外)', '', '施放[龙刃无双]期间，施放阿斯特拉技能时，剩余冷却时间 -10%。', '- 每次施放[龙刃无双]，冷却时间减少效果仅适用1次。', '', '以下技能冷却时间减少10秒。', '- [火焰吐息]', '- [龙语召唤：阿斯特拉]', '- [龙之撕咬]', '- [魔龙之息]', '- [魔龙天翔]']
    if mode == 0:
        char.技能攻击力加成(0.1)
        龙刃无双 = char.get_skill_by_name("龙刃无双")
        # 龙刃无双.倍率 *= 0.6
        龙刃无双.CD = 10
        pass
    if mode == 1:
        char.get_skill_by_name("龙刃无双").CD *= 0.9
        char.get_skill_by_name("火焰吐息").CDR *= 0.85
        char.get_skill_by_name("龙语召唤：阿斯特拉").CDR *= 0.85
        char.get_skill_by_name("龙之撕咬").CDR *= 0.85
        char.get_skill_by_name("魔龙之息").CDR *= 0.85
        char.get_skill_by_name("魔龙天翔").CDR *= 0.85
        pass


# 固定装备：胜负之役短剑 - 精灵骑士 ， 胜负之役太刀 - 精灵骑士 ， 胜负之役钝器 - 精灵骑士 ， 胜负之役巨剑 - 精灵骑士
def entry_743(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[剑盾猛攻]连击6阶段的状态下，施放[剑盾强袭]时，进入8秒高燃时刻。', '- [剑盾猛攻]攻击力 +500%', '- 连锁的所有区域变更为成功区域。', '- 1~30级技能冷却时间 -70%', '- 1~30级技能攻击力 -50% ([剑盾猛攻]技能除外)', '', '施放[剑盾猛攻]技能时，1~30级技能的剩余冷却时间减少10%。']
    if mode == 0:
        pass
    if mode == 1:
        char.单技能加成('剑盾猛攻',6)
        char.单技能加成('剑盾强袭',CD=0.9)
        for i in char.技能栏:
            if i.所在等级 >= 1 and i.所在等级 <= 30:
                if i.是否有伤害 == 1 and i.名称 != '剑盾猛攻':
                    i.CDR *= (1 - 0.7)
                    i.倍率 *= 0.5
        pass


# 固定装备：胜负之役长枪 - 暗枪士 ， 胜负之役战戟 - 暗枪士 ， 胜负之役光枪 - 暗枪士 ， 胜负之役暗矛 - 暗枪士
def entry_747(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['每存在1个暗蚀状态的敌人，每1秒累积10%的黑雷气息', '- 不存在暗蚀状态的敌人时，每1秒减少5%的黑雷气息。', '', '攻击领主怪物时，获得1%的黑雷气息。', '', '黑雷气息达到100%时，发动黑雷强化效果，效果持续15秒。', '- 同时坠落黑雷枪', '- 额外坠落黑雷魔枪', '- 黑雷魔枪攻击力：[坠蚀之雨]多段攻击力的1000%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)
        char.攻击速度增加(0.15,part)
        char.get_skill_by_name('坠蚀之雨').hit0 += 16
        char.单技能加成('冥夜裂空',1.1)
        char.单技能加成('冥蚀脉冲',1.1)
        char.单技能加成('虚空碎灭',1.1)
        pass


# 固定装备：胜负之役长枪 - 狩猎者 ， 胜负之役战戟 - 狩猎者 ， 胜负之役光枪 - 狩猎者 ， 胜负之役暗矛 - 狩猎者
def entry_751(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[猎杀枪]技能攻击时，向敌人生成猎物标志，赋予猎物1阶段效果。', '每累计20个猎物标志，提升标志阶段。 (最高3阶段)', '施放以下技能时，消耗猎物阶段并提升该技能攻击力。', '- [无尽毁灭]', '- [天龙破]', '-  [无尽毁灭]', '', '[猎物阶段攻击力增加量]', '- 1阶段：10%', '- 2阶段：20%', '- 3阶段：30%', '', '[猎物标志累计量]', '- [猎杀枪]：每次打击3个', '- [猎杀枪：掠食]：每次打击10个', '- [猎杀枪：穿心]：每次打击4个', '', '[猎杀枪]魔法枪再次生成时间 -30%', '[猎杀枪]魔法枪再次发射冷却时间 -30%']
    if mode == 0:
        char.攻击速度增加(0.2,part)
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)
        char.get_skill_by_name('光焰枪').倍率 *= 1.45
        char.get_skill_by_name('天龙破').倍率 *= 1.45
        char.get_skill_by_name('无尽杀戮').倍率 *= 1.45
        char.get_skill_by_name('猎杀枪').CDR *= 0.7
        char.单技能加成('瞬光猎杀枪',1.15)
        char.单技能加成('凌空之狩',1.15)
        pass


# 固定装备：胜负之役长枪 - 征战者 ， 胜负之役战戟 - 征战者 ， 胜负之役光枪 - 征战者 ， 胜负之役暗矛 - 征战者
def entry_755(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['达到[战戟猛攻]极限时，强化[战戟猛攻]。', '- 强制中断[战戟猛攻]并施放技能时，该技能减少20%的冷却时间。 (觉醒技能除外)', '- 能量叠加次数 +1', '- 命中时能量恢复减少时间 +0.3秒', '- 攻击速度增益增加量 +10%']
    if mode == 0:
        char.技能攻击力加成(0.12)
        char.单技能加成('破灭轮回刺',1.15)
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.2, excName=char.觉醒技能)
        pass


# 固定装备：胜负之役长枪 - 决战者 ， 胜负之役战戟 - 决战者 ， 胜负之役光枪 - 决战者 ， 胜负之役暗矛 - 决战者
def entry_759(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['以下技能命中时，获得强化[夺命雷霆枪]的极·受创能量。 (最多30个)', '- 双龙流云灭：每次攻击10个', '- 无双突刺：每次攻击5个', '- 无畏波动枪：每次攻击4个', '- 双重刺击：每次攻击2个', '- 刺击：每次攻击1个', '', '每拥有一个极·受创能量，强化[夺命雷霆枪]。', '- 技能冷却时间恢复速度：+1%', '- 攻击速度：+1%', '', '[夺命雷霆枪]攻击时，消耗所有极·受创能量，每个极·受创能量可增加枪尖受创效果攻击次数。', '', '[夺命雷霆枪]攻击速度 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)
        char.攻击速度增加(0.1,part)
        夺命雷霆枪 = char.get_skill_by_name("夺命雷霆枪")
        夺命雷霆枪.恢复 += 0.3
        夺命雷霆枪.hit2 += 30
        char.单技能加成('无双突刺',1.1)
        char.单技能加成('流光无影闪',1.1)
        char.单技能加成('双龙流云灭',1.1)


# 固定装备：胜负之役长刀 - 特工 ， 胜负之役小太刀 - 特工 ， 胜负之役重剑 - 特工 ， 胜负之役源力剑 - 特工
def entry_763(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['部分技能攻击追踪目标敌人时，使敌人进入枪伤 / 斩伤状态，效果持续15秒。 (最多叠加3次)', '- 赋予枪伤的技能：[精准射击]、[锁定射击]', '- 赋予斩伤的技能：[双弦斩]、[月影秘步]', '', '对携带枪伤 / 斩伤状态的敌人，施放以下技能时，效果解除并增加技能攻击力。', '- [月相轮舞]：每1层枪伤，技能攻击力 +8%', '- [毁灭狂欢]：每1层斩伤，技能攻击力 +8%', '- [月光镇魂曲] ：每1层枪伤 / 斩伤，技能攻击力 +8%', '', '以下技能冷却时间 -15%', '- [双弦斩]', '- [精准射击]', '- [月影秘步]', '- [锁定射击]', '', '[月相轮舞]大小 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("精准射击").CDR *= 0.85
        char.get_skill_by_name("锁定射击").CDR *= 0.85
        char.get_skill_by_name("双弦斩").CDR *= 0.85
        char.get_skill_by_name("月影秘步").CDR *= 0.85
        char.get_skill_by_name("月相轮舞").倍率 *= 1.24
        char.get_skill_by_name("毁灭狂欢").倍率 *= 1.24
        char.get_skill_by_name("月光镇魂曲").倍率 *= 1.48
        char.技能攻击力加成(0.1)
        pass


# 固定装备：胜负之役长刀 - 战线佣兵 ， 胜负之役小太刀 - 战线佣兵 ， 胜负之役重剑 - 战线佣兵 ， 胜负之役源力剑 - 战线佣兵
def entry_767(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放[爆裂斩]时，转职技能攻击力增加20%，效果持续3秒。 (觉醒技能除外)', '- 可强制中断[爆裂斩]并施放转职技能。', '- 可强制中断转职技能并施放[爆裂斩]。', '- [爆裂斩]技能的额外攻击输入时间增加至3秒', '- [爆裂斩]技能结束后适用冷却时间。', '- [爆裂斩]技能冷却时间 -35%', '- [爆裂斩]爆炸范围 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能倍率加成(1, 100, 0.24, excName=char.觉醒技能)
        char.get_skill_by_name("爆裂斩").CDR *= 0.65
        pass


# 固定装备：胜负之役长刀 - 源能专家 ， 胜负之役小太刀 - 源能专家 ， 胜负之役重剑 - 源能专家 ， 胜负之役源力剑 - 源能专家
def entry_771(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['使用[源能提炼]能量时，额外消耗1个能量，使技能冷却时间减少20%，效果持续5秒。 (觉醒技能除外)', '', '可通过[源能提炼]，强化[聚能光幕]', '- 强化时， 最大蓄气攻击力 +40%', '- 强化时，以蓄气60%的状态发动多段攻击次数。', '', '[源能提炼]基本累积数 +2']
    if mode == 0:
        pass
    if mode == 1:
        char.get_skill_by_name("CEAB-2超能爆发").倍率 *= 1.5
        char.技能冷却缩减(1, 100, 0.2, excName=char.觉醒技能)
        char.单技能加成('绝望圆舞',1.15)
        char.单技能加成('临界源能弹',1.15)
        pass


# 固定装备：胜负之役长刀 - 暗刃 ， 胜负之役小太刀 - 暗刃 ， 胜负之役重剑 - 暗刃 ， 胜负之役源力剑 - 暗刃
def entry_775(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['可强制中断转职技能的施放后僵直并立即发动[轮盘连射]。', '强制中断转职技能并施放[轮盘连射]时，发动以下效果。', '- 强制中断技能的冷却时间 -20%', '- [轮盘连射]冷却时间 -50%', '-\xa08秒内攻击速度 +7% (最多叠加3次)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.07)
        char.攻击速度增加(0.25,part)
        char.单技能加成('轮盘连射',CD=0.5)
        char.单技能加成('致命焰火',1.1)
        pass


# 固定装备：胜负之役短剑 - 黑暗武士 ， 胜负之役太刀 - 黑暗武士 ， 胜负之役钝器 - 黑暗武士 ， 胜负之役巨剑 - 黑暗武士 ， 胜负之役光剑 - 黑暗武士
def entry_779(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[时间停滞]最大连击能量增加1阶段。', '- 连击能量6阶段攻击力：220%', '', '通过干涉时间，强化[时间主宰]效果。', '- 施放其他连击技能栏技能时，获得连击能量。', '- 施放扩展技能栏技能时，也不会结束现有连招技能。', '- [时间主宰]效果持续时间 +2秒']
    if mode == 0:
        char.技能攻击力加成(0.1)
        char.get_skill_by_name("时间停滞").连击倍率 = [1.0,1.3,1.5,1.8,2.0,2.4]
        char.单技能加成('邪影升龙斩',1.05)
    if mode == 1:
        pass


# 固定装备：胜负之役矛 - 缔造者 ， 胜负之役棍棒 - 缔造者 ， 胜负之役魔杖 - 缔造者 ， 胜负之役法杖 - 缔造者 ， 胜负之役扫把 - 缔造者
def entry_783(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放[末日虫洞]时，召唤[终末之钟]展开隔离时间区域。', '隔离时间区域在5秒后，或者追加技能键时，领域崩坏并发生爆炸。', '对[终末之钟]使用烈炎、寒冰、风暴系列技能攻击2次时，增加爆炸攻击力。', '- 爆发伤害： [末日虫洞]攻击力的100%', '- 每2次攻击增加5%的爆炸攻击力。 (最多增加50%)', '', '[风暴漩涡]强化', '- 吸附范围 +30%', '- [风暴漩涡]能量消耗量 -35%', '', '穿戴时[风暴漩涡]能量从0开始恢复。']
    if mode == 0:
        char.技能攻击力加成(0.08)
        char.单技能加成('末日虫洞', 1.1)
        pass
    if mode == 1:
        char.单技能加成('末日虫洞', 1.5)
        char.get_skill_by_name('风暴漩涡').最小值 *= 0.65
        pass


# 固定装备：胜负之役左轮枪 - 合金战士 ， 胜负之役自动手枪 - 合金战士 ， 胜负之役步枪 - 合金战士 ， 胜负之役手炮 - 合金战士 ， 胜负之役手弩 - 合金战士
def entry_787(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['使用超频技能强制中断转职技能时，获得1个电能。 (最多获得1个)', '', '施放技能时，消耗1个电能，使35级以上技能 ([AT-SO步行者]除外) 增加20%的攻击力，效果持续20秒。', '', '以下技能增加20%的攻击力。', '- [炎神攻城炮]', '- [超频：电流闪踢]']
    if mode == 0:
        pass
    if mode == 1:
        char.技能倍率加成(35,100,0.2,excName=["AT-SO步行者"])
        char.单技能加成('超频：电流闪踢', 1.2)
        char.单技能加成('炎神攻城炮', 1.2)
        pass


# 固定装备：吞噬本源短剑 ， 吞噬本源太刀 ， 吞噬本源钝器 ， 吞噬本源巨剑 ， 吞噬本源光剑 ， 吞噬本源手套 ， 吞噬本源臂铠 ， 吞噬本源爪 ， 吞噬本源拳套 ， 吞噬本源东方棍 ， 吞噬本源左轮枪 ， 吞噬本源自动手枪 ， 吞噬本源步枪 ， 吞噬本源手炮 ， 吞噬本源手弩 ， 吞噬本源矛 ， 吞噬本源棍棒 ， 吞噬本源魔杖 ， 吞噬本源法杖 ， 吞噬本源扫把 ， 吞噬本源十字架 ， 吞噬本源念珠 ， 吞噬本源图腾 ， 吞噬本源镰刀 ， 吞噬本源战斧 ， 吞噬本源匕首 ， 吞噬本源双剑 ， 吞噬本源手杖 ， 吞噬本源苦无 ， 吞噬本源长枪 ， 吞噬本源战戟 ， 吞噬本源光枪 ， 吞噬本源暗矛 ， 吞噬本源长刀 ， 吞噬本源小太刀 ， 吞噬本源重剑 ， 吞噬本源源力剑 ， 吞噬本源神弦弓 ， 吞噬本源玄机弓 ， 吞噬本源强攻弩 ， 吞噬本源妖影弓
def entry_791(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '所有技能等级 +1 (觉醒技能除外)']
    if mode == 0:
        char.技能攻击力加成(0.1)
        char.技能等级加成('所有', 1, 100, 1, excName=char.觉醒技能)
    if mode == 1:
        pass


# 固定装备：寂灭之信光枪 ， 寂灭之信战戟 ， 寂灭之信暗矛 ， 寂灭之信长枪 ， 寂灭之信拳套 ， 寂灭之信爪 ， 寂灭之信臂铠 ， 寂灭之信手套 ， 寂灭之信东方棍 ， 寂灭之信源力剑 ， 寂灭之信长刀 ， 寂灭之信重剑 ， 寂灭之信小太刀 ， 寂灭之信自动手枪 ， 寂灭之信手弩 ， 寂灭之信手炮 ， 寂灭之信步枪 ， 寂灭之信左轮枪 ， 寂灭之信扫把 ， 寂灭之信棍棒 ， 寂灭之信魔杖 ， 寂灭之信矛 ， 寂灭之信法杖 ， 寂灭之信战斧 ， 寂灭之信十字架 ， 寂灭之信念珠 ， 寂灭之信镰刀 ， 寂灭之信图腾 ， 寂灭之信光剑 ， 寂灭之信钝器 ， 寂灭之信太刀 ， 寂灭之信巨剑 ， 寂灭之信短剑 ， 寂灭之信苦无 ， 寂灭之信匕首 ， 寂灭之信双剑 ， 寂灭之信手杖 ， 寂灭之信神弦弓 ， 寂灭之信玄机弓 ， 寂灭之信强攻弩 ， 寂灭之信妖影弓
def entry_1300(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '攻击时，使敌人进入出血/中毒/灼伤/感电状态10秒。 (冷却时间3秒)', '', '每3秒恢复1%的生命值/魔法值。', '', '所有异常状态抗性 +20%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.1)
        for i in ['出血', '灼伤', '中毒', '感电']:
            if i not in pa.get_state_type():
                pa.state_type.append(i)
            char.异常时间[i][3] = min(char.异常时间[i][3],3)
        char.所有异常抗性加成(0.2,mode=0)
        pass
    if mode == 1:
        pass


# 固定装备：怒战之意光枪 ， 怒战之意战戟 ， 怒战之意暗矛 ， 怒战之意长枪 ， 怒战之意拳套 ， 怒战之意爪 ， 怒战之意臂铠 ， 怒战之意手套 ， 怒战之意东方棍 ， 怒战之意源力剑 ， 怒战之意长刀 ， 怒战之意重剑 ， 怒战之意小太刀 ， 怒战之意自动手枪 ， 怒战之意手弩 ， 怒战之意手炮 ， 怒战之意步枪 ， 怒战之意左轮枪 ， 怒战之意扫把 ， 怒战之意棍棒 ， 怒战之意魔杖 ， 怒战之意矛 ， 怒战之意法杖 ， 怒战之意战斧 ， 怒战之意十字架 ， 怒战之意念珠 ， 怒战之意镰刀 ， 怒战之意图腾 ， 怒战之意光剑 ， 怒战之意钝器 ， 怒战之意太刀 ， 怒战之意巨剑 ， 怒战之意短剑 ， 怒战之意苦无 ， 怒战之意匕首 ， 怒战之意双剑 ， 怒战之意手杖 ， 怒战之意神弦弓 ， 怒战之意玄机弓 ， 怒战之意强攻弩 ， 怒战之意妖影弓
def entry_1304(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +30', '装备的物体伤害 +20%', '技能范围 +24%', '', '技能范围的属性数值的总和高于48%时，技能伤害 +8%', '', '攻击速度 +20%', '移动速度 +20%', '施放速度 +30%', '生命值最大值 +5%', '魔法值最大值 +5%']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.08*3)
        char.multiply_eq_params('skill_range_multi',1.24)
        char.所有速度增加(part=part, x=0.2)
        char.施放速度增加(0.1)
        char.所有属性强化加成(30)
        pass
    if mode == 1:
        if char.get_eq_params('skill_range') >= 0.48:
            char.技能攻击力加成(0.08)
        else:
            return '技能范围不足 48%'
        pass


# 固定装备：冰封之御光枪 ， 冰封之御战戟 ， 冰封之御暗矛 ， 冰封之御长枪 ， 冰封之御拳套 ， 冰封之御爪 ， 冰封之御臂铠 ， 冰封之御手套 ， 冰封之御东方棍 ， 冰封之御源力剑 ， 冰封之御长刀 ， 冰封之御重剑 ， 冰封之御小太刀 ， 冰封之御自动手枪 ， 冰封之御手弩 ， 冰封之御手炮 ， 冰封之御步枪 ， 冰封之御左轮枪 ， 冰封之御扫把 ， 冰封之御棍棒 ， 冰封之御魔杖 ， 冰封之御矛 ， 冰封之御法杖 ， 冰封之御战斧 ， 冰封之御十字架 ， 冰封之御念珠 ， 冰封之御镰刀 ， 冰封之御图腾 ， 冰封之御光剑 ， 冰封之御钝器 ， 冰封之御太刀 ， 冰封之御巨剑 ， 冰封之御短剑 ， 冰封之御苦无 ， 冰封之御匕首 ， 冰封之御双剑 ， 冰封之御手杖 ， 冰封之御神弦弓 ， 冰封之御玄机弓 ， 冰封之御强攻弩 ， 冰封之御妖影弓
def entry_1308(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间恢复速度 +40% (觉醒技能除外)', '冰属性攻击', '', '@[酷寒一击]@', '[冰冻打击]属性变更为技能伤害 +5%。', '', '攻击敌人时，将冰冻添加为敌人的弱点异常状态。', '', '攻击时，使敌人进入冰冻状态5秒。 (冷却时间3秒)', '', '冰属性抗性 +15', '冰冻抗性 +40%', '', '解除穿戴时，发动魔力点燃减益效果。', '- 每1秒减少10%/5000的魔法值。', '- 重新穿戴冰封之御武器时，魔力点燃效果消失。']
    if mode == 0:
        char.set_eq_params('ice_attack_rate', 1/3)
        if '冰冻' not in pa.get_state_type():
            pa.state_type.append('冰冻')
            char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],3)
        char.冰属性抗性加成(15)
        char.异常抗性加成('冰冻', 0.4)
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.4, excName=char.觉醒技能)
        pass


# 固定装备：胜负之役神弦弓 - 缪斯
def entry_1483(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[多彩感性]单人挑战时，独立攻击力 +20%', '', '[音波冲击]技能范围 +20%', '[音波冲击]技能结束时，追加生成音波', '- 追加音波在2秒内生成5次', '- 追加音波攻击力：每1次为第三次音波攻击力的30%', '施放[缪斯之声]时追加生成聚光灯，继而强化技能。', '- [缪斯之声]技能范围 +15%', '- [缪斯之声]技能伤害 +20%', '- [缪斯之声]攻击时，[音波冲击]的冷却时间初始化。', '穿戴时，向队员赋予[可爱节拍]效果增加8%的效果。', '- 解除穿戴时，可爱节拍效果消失。', '- 在增益强化装备栏穿戴时不适用该效果。', '', '[夜与梦]技能范围 +20%', '', '以下技能生命值恢复量减少50%。', '[夜与梦]', '[甜蜜柔歌]', '解除穿戴时，辅助职业50级技能增益效果 -50%', '- 重新穿戴时，恢复增益效果。', '- 使用复活币等情况下复活后，增益效果减少属性依然持续。']
    if mode == 0:
        if char.类型 == '辅助':
            buff = char.get_skill_by_name("BUFF")
            buff.倍率 *= 1.08
        pass
    if mode == 1:
        pass




# 固定装备：胜负之役玄机弓 - 旅人
def entry_1487(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[神雾兵仗·流星]冷却时间 -15%', '', '[神雾兵仗·北极星]光环最大持续时间增加7秒，可探索次数增加5次。', '[神雾兵仗·北极星]终结攻击发动后技能不结束。 (技能时间内最多发动1次终结攻击)', '-  终结攻击发动后再次按技能键时，可以结束技能。', '[装载：猛击]的弓术技能攻击力增加率 +5%', '[装载：闪攻]的弓术技能冷却时间减少率 +5%', '[营火]生命值恢复范围 +20%', '[营火]炖菜生命值恢复量 +50%']
    if mode == 0:
        char.技能攻击力加成(0.06)
        char.单技能加成('神雾兵仗·流星',1.15,0.85)
        char.单技能加成('神雾兵仗·妖旋风',1.15,0.85)
        char.单技能加成('神雾兵仗·北极星',1.1)
        char.get_skill_by_name("神雾兵仗·北极星").hit0 += 5*4
        char.get_skill_by_name("装载：猛击").猛倍率 = 1.15
        char.get_skill_by_name("装载：闪攻").闪CDR = 0.85
        pass
    if mode == 1:
        pass

# 固定装备：胜负之役强攻弩 - 猎人
def entry_1854(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[神雾兵仗·流星]冷却时间 -15%', '', '[神雾兵仗·北极星]光环最大持续时间增加7秒，可探索次数增加5次。', '[神雾兵仗·北极星]终结攻击发动后技能不结束。 (技能时间内最多发动1次终结攻击)', '-  终结攻击发动后再次按技能键时，可以结束技能。', '[装载：猛击]的弓术技能攻击力增加率 +5%', '[装载：闪攻]的弓术技能冷却时间减少率 +5%', '[营火]生命值恢复范围 +20%', '[营火]炖菜生命值恢复量 +50%']
    if mode == 0:
        char.单技能加成('重型穿甲箭',1.3)
        char.技能攻击力加成(0.05)
        char.单技能加成('三弓床弩',1.12)
        char.单技能加成('终结穿刺',1.12)
        pass
    if mode == 1:
        pass

# 固定装备：胜负之役妖影弓 - 妖护使
def entry_1858(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[神雾兵仗·流星]冷却时间 -15%', '', '[神雾兵仗·北极星]光环最大持续时间增加7秒，可探索次数增加5次。', '[神雾兵仗·北极星]终结攻击发动后技能不结束。 (技能时间内最多发动1次终结攻击)', '-  终结攻击发动后再次按技能键时，可以结束技能。', '[装载：猛击]的弓术技能攻击力增加率 +5%', '[装载：闪攻]的弓术技能冷却时间减少率 +5%', '[营火]生命值恢复范围 +20%', '[营火]炖菜生命值恢复量 +50%']
    if mode == 0:
        char.get_skill_by_name("妖兽化").CP倍率 = 1
        char.技能攻击力加成(0.16)
        char.单技能加成('凶兽噬咬',1.15)
        char.单技能加成('盛怒狂潮',1.15)
        char.单技能加成('神妖之爪',1.15)
        pass
    if mode == 1:
        pass


# 固定装备：先驱者的匕首 ， 先驱者的双剑 ， 先驱者的手杖 ， 先驱者的短剑 ， 先驱者的太刀 ， 先驱者的钝器 ， 先驱者的巨剑 ， 先驱者的光剑 ， 先驱者的手套 ， 先驱者的臂铠 ， 先驱者的爪 ， 先驱者的拳套 ， 先驱者的东方棍 ， 先驱者的左轮枪 ， 先驱者的自动手枪 ， 先驱者的步枪 ， 先驱者的手炮 ， 先驱者的手弩 ， 先驱者的矛 ， 先驱者的棍棒 ， 先驱者的魔杖 ， 先驱者的法杖 ， 先驱者的扫把 ， 先驱者的十字架 ， 先驱者的念珠 ， 先驱者的图腾 ， 先驱者的镰刀 ， 先驱者的战斧 ， 先驱者的苦无 ， 先驱者的长枪 ， 先驱者的战戟 ， 先驱者的光枪 ， 先驱者的暗矛 ， 先驱者的长刀 ， 先驱者的小太刀 ， 先驱者的重剑 ， 先驱者的源力剑 ， 先驱者的神弦弓 ， 先驱者的玄机弓 ， 先驱者的强攻弩 ， 先驱者的妖影弓
def entry_1726(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['1~100级技能等级 +2', '', '50、85、100级主动技能攻击力 +30%', '50、85、100级主动技能冷却时间 -20%', ' (辅助职业不适用该效果)', '', '解除穿戴时，发动魔力点燃效果，每1秒减少10%和5000的魔法值。', '- 重新穿戴先驱者武器时，魔力点燃效果消失。', '- 使用复活币等情况下复活后，魔力点燃效果依然持续。']
    if mode == 0:
        pass
    if mode == 1:
        char.技能等级加成('所有', 1, 100, 2)
        char.技能倍率加成(50, 50, 0.3)
        char.技能倍率加成(85, 85, 0.3)
        char.技能倍率加成(100, 100, 0.3)
        if char.类型 != "辅助":
            char.技能冷却缩减(50, 50, 0.2)
            char.技能冷却缩减(85, 85, 0.2)
            char.技能冷却缩减(100, 100, 0.2)
        pass

def entry_2000(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间恢复速度 +30% (觉醒技能除外)', '@[酷寒一击]@', '[冰冻打击]属性变更为技能伤害 +5%。', '冰冻抗性 +40%']
    if mode == 0:
        char.set_eq_params('ice_attack_rate', 1/3)
        char.异常抗性加成('冰冻', 0.4)
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.3, excName=char.觉醒技能)
        pass

def entry_2002(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['1~100级技能等级 +2', '', '50、85、100级主动技能攻击力 +30%', '50、85、100级主动技能冷却时间 -20%', ' (辅助职业不适用该效果)', '', '解除穿戴时，发动魔力点燃效果，每1秒减少10%和5000的魔法值。', '- 重新穿戴先驱者武器时，魔力点燃效果消失。', '- 使用复活币等情况下复活后，魔力点燃效果依然持续。']
    if mode == 0:
        pass
    if mode == 1:
        char.技能等级加成('所有', 1, 100, 2)
        char.技能倍率加成(50, 50, 0.3)
        char.技能倍率加成(85, 85, 0.3)
        char.技能倍率加成(100, 100, 0.3)
        if char.类型 != "辅助":
            char.技能冷却缩减(50, 50, 0.2)
            char.技能冷却缩减(85, 85, 0.2)
            char.技能冷却缩减(100, 100, 0.2)
        pass