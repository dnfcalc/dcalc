from core.basic.property import CharacterProperty
from core.equipment.property import 成长词条计算
import core.equipment.entry_0.params as pa

# 固定装备：六方式脉冲肩甲
def entry_924(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '清除自身赋予敌人石化状态的所受伤害减少效果。', '', '攻击时，使所有敌人进入石化状态10秒。 (冷却时间15秒)']
    if mode == 0:
        if '石化' not in pa.get_state_type():
            pa.state_type.append('石化')
        char.技能攻击力加成(part=part, x=0.1)
        pass
    if mode == 1:
        pass


# 固定装备：月落星沉腰带
def entry_1228(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '攻击时，恢复30%的生命值/魔法值，效果持续10秒。 (冷却时间60秒)', '', '物理/魔法所受伤害 -10%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.1)
        char.add_eq_params('hurted_ratio',0.1)
        pass
    if mode == 1:
        pass


# 固定装备：天才技术大师的加厚长靴
def entry_1183(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +326.0%', '所有属性强化 +15', '', '按照技能魔法值消耗量属性之和的5%，增加技能伤害。 (最多25%)', '', '技能魔法值消耗量 +100%', '', '物理/魔法所受伤害 -20%']
    if mode == 0:
        char.攻击强化加成(params[0])
        char.MP消耗量加成(1.0)
        char.所有属性强化加成(15,mode=1)
        char.add_eq_params('hurted_ratio',0.2)
    if mode == 1:
        if char.MP消耗倍率() >= 1:
            char.技能攻击力加成(part=part, x=min((char.MP消耗倍率() - 1)*0.05, 0.25))
        if char.MP消耗倍率() < 6:
            return 'MP消耗量增加需提升{}%'.format(round(600-char.MP消耗倍率()*100), 0)
        pass


# 固定装备：天才技术大师的百宝腰带
def entry_997(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +666.9%', '技能伤害 +5%', '', '技能魔法值消耗量 +100%']
    if mode == 0:
        char.MP消耗量加成(1)
        char.攻击强化加成(params[0])
        char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


# 固定装备：天才技术大师的保护面罩
def entry_1025(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%', '', '每30秒，恢复30%的生命值/魔法值。']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(part=part, x=0.11)


# 固定装备：和平之翼长裤
def entry_899(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '攻击时，获得生命值最大值10%的保护罩，效果持续1.5秒。 (冷却时间0.5秒)', '', '攻击时恢复1%的魔法值。 (冷却时间1秒)']
    if mode == 0:
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.1)
        char.技能攻击力加成(0.08)
        pass
    if mode == 1:
        pass


# 固定装备：冤魂的执念上衣
def entry_1184(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +10', '感电伤害 +20%', '', '@[缩小化]@', '输入[装备属性指令]时，角色缩小，效果持续25秒。 (冷却时间60秒)', '- 移动速度 +30%', '- 回避率 +75%', '- 每秒恢复1%的生命值/魔法值', '- 无法使用技能和基本攻击', '- 再次输入[装备属性指令]可以解除效果', '', '攻击时，使所有敌人进入感电状态15秒。 (冷却时间10秒)', '', '感电抗性 +10%']
    if mode == 0:
        char.异常增伤('感电', 0.2)
        char.异常抗性加成('感电', 0.1)
        char.异常时间['感电'][3] = min(char.异常时间['感电'][3],10)
        if '感电' not in pa.get_state_type():
            pa.state_type.append('感电')
        char.所有属性强化加成(10)
        pass
    if mode == 1:
        pass


# 固定装备：混沌之幕护腿
def entry_1042(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)


# 固定装备：灵巧的支配者护肩
def entry_1106(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +13%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(part=part, x=0.13)


# 固定装备：死亡蚕食胸甲
def entry_814(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +296.4%', '技能伤害 +5%', '', '@[最后的狂暴]@', '死亡判定时，推迟死亡，进入狂暴状态，效果持续5秒。', '- 施放技能时每消耗1个无色小晶块，增加0.3秒狂暴时间。', '- 狂暴状态结束时，角色死亡。', '', '攻击速度 +15%', '施放速度 +22.5%']
    if mode == 0:
        char.攻击强化加成(params[0])
        char.攻击速度增加(part=part, x=0.15)
        char.施放速度增加(0.225)
        char.技能攻击力加成(part=part, x=0.05)
        pass
    if mode == 1:
        pass


# 固定装备：恐惧缠绕腰带
def entry_1147(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['1~30级技能攻击力 +12%', '', '无色小晶块技能攻击力增加', '- 1个~9个：2%', '- 10个~15个：15%', '- 16个以上：20%', '', '不消耗无色的技能无色小晶块消耗量 +2']
    if mode == 0:
        char.技能倍率加成(1, 30, 0.12)
        # 伏虎霸王拳特殊处理
        skill = char.get_skill_by_name('狂·霸王拳')
        if skill.所在等级 == 40:
            skill.额外倍率 /= 1.12
        for skill in char.技能队列:
            if skill["无色消耗"] == 0 and skill['名称'] != '基础精通' and skill['名称'] != '幻影爆碎' and skill['名称'] != '鬼连斩：极':
                skill["无色消耗"] = 2
    if mode == 1:
        for skill in char.技能队列:
            无色消耗 = skill["无色消耗"]
            if skill['名称'] == '炫纹发射':
                无色消耗 = min(无色消耗, 3)
            if skill['名称'] == '神罚之锤' and char.实际名称 == 'crusader_male_carry':
                无色消耗 = 0
            if 无色消耗 >= 16:
                skill["倍率"] *= 1.2
            elif 无色消耗 >= 10:
                skill["倍率"] *= 1.15
            elif 无色消耗 >= 1:
                skill["倍率"] *= 1.02
        pass


# 固定装备：电弧爆源手镯
def entry_900(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +16%', '攻击时，恢复3000点生命值。 (冷却时间1秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.16)
        pass


# 固定装备：熔丝项链
def entry_1232(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '攻击时，敌人的韧性条 -10 (冷却时间3秒；辅助角色不适用)', '', '攻击破韧状态的敌人时，发动以下效果。', '- 根据破韧次数，韧性条减少量 +20% (最多叠加5次)', '- 敌人最后被赋予的控制型异常状态适用为该敌人的弱点。']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(part=part, x=0.08)
        pass


# 固定装备：金翼戒指
def entry_904(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '物理/魔法所受伤害 -20%']
    if mode == 0:
        char.add_eq_params('hurted_ratio',0.2)
        char.技能攻击力加成(part=part, x=0.05)
        pass
    if mode == 1:
        pass



# 固定装备：全能主宰者之戒
def entry_1079(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '移动速度 +20%']
    if mode == 0:
        char.移动速度增加(0.2)
        char.技能攻击力加成(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：遥感之心项链
def entry_933(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '攻击时，恢复0.1%的魔法值。 (冷却时间0.1秒)', '消灭敌人时，恢复10%的魔法值。', '', '技能魔法值消耗量 +50%']
    if mode == 0:
        char.技能攻击力加成(0.08)
        char.MP消耗量加成(0.5)
        pass
    if mode == 1:
        pass


# 固定装备：魔力抑制手镯
def entry_868(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +385.3%', '技能伤害 +15%', '', '@[禁忌的魔法契约]@', '缔结禁忌的魔法契约，失去生命值，将魔法与生命连接。', '- 施放技能或者被攻击时，不消耗生命值而消耗魔法值', '- 按照生命值恢复量的25%恢复魔法值', '- 锁定生命值最大值的99%', '', '魔法值最大值 +4196']
    if mode == 0:
        cur = char.get_eq_params('hp_max')
        char.set_eq_params('hp_max',(100 if cur == 0 else cur)*0.01)
        char.攻击强化加成(params[0])
        char.技能攻击力加成(part=part, x=0.15)
        pass
    if mode == 1:
        pass


# 固定装备：黯星项链
def entry_1078(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['生命值低于50%，技能伤害 +11%', '', '攻击速度 +20%', '施放速度 +20%', '移动速度 +20%']
    if mode == 0:
        char.所有速度增加(0.2)
        pass
    if mode == 1:
        if pa.get_hp_rate_num(char) <= 50:
            char.技能攻击力加成(part=part, x=0.11)
        if pa.get_hp_rate_num(char) > 50:
            return '生命值高于50%'
        pass


# 固定装备：无尽的痛苦之戒
def entry_935(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%', '', '装备的生命值恢复效果 +30%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        pass
    if mode == 1:
        pass


# 固定装备：自由之缚手镯
def entry_878(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +518.7%', '技能伤害 +10%', '所有属性强化 +15', '', '技能的无色小晶块消耗量增加8倍。 (最多16个)']
    if mode == 0:
        char.技能攻击力加成(0.1)
        for index in range(0, len(char.技能队列)):
            skill = char.技能队列[index]
            if skill["无色消耗"] > 0:
                skill["无色消耗"] = min(16, skill["无色消耗"] * 8)
        char.所有属性强化加成(15)
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 固定装备：原核之芯耳环
def entry_923(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%', '', '@[美杜莎的眼睛]@', '- 石化状态期间，累积敌人所受的伤害。石化结束时，一次性结算累积的伤害。', '', '击败敌人时，恢复5%的生命值。']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        pass
    if mode == 1:
        pass


# 固定装备：德卡制导装置
def entry_890(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '技能冷却时间恢复速度 +20% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.04)
        char.技能恢复加成(1, 100, 0.2, excName=char.觉醒技能)
        pass


# 固定装备：迷你电池包
def entry_1105(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%', '', '技能魔法值消耗量 +100%']
    if mode == 0:
        char.MP消耗量加成(1)
        char.技能攻击力加成(part=part, x=0.11)
        pass
    if mode == 1:
        pass


# 固定装备：黄昏殿堂
def entry_1218(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +444.6%', '技能伤害 +5%', '', '攻击领主怪物时，恢复1%的生命值。 (冷却时间0.5秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(params[0])
        char.技能攻击力加成(part=part, x=0.05)
        pass


# 固定装备：生命的喘息
def entry_1077(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '物理/魔法暴击率 +20%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(part=part, x=0.1)
        pass


# 固定装备：堕落的灵魂
def entry_1174(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['对消耗无色小晶块的技能，发动以下效果。', '- 技能攻击力 +10%', '- 技能冷却时间 -10% (觉醒技能除外)', '- 无色小晶块消耗量 +2', '', '技能魔法值消耗量 -10%']
    if mode == 0:
        char.MP消耗量加成(-0.1)
        pass
    if mode == 1:
        for skill in char.技能队列:
            if skill["无色消耗"] > 0:
                skill["无色消耗"] += 2
                skill["倍率"] *= 1.10
                if skill['名称'] not in char.觉醒技能:
                    skill["CDR"] *= 0.9
        pass


# 固定装备：高科技战术强化靴
def entry_1138(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%', '', '无色小晶块技能的指令使用效果 +400% (觉醒技能除外)', '', '攻击速度 +10%', '施放速度 +10%', '移动速度 +10%', '物理/魔法所受伤害 -12%']
    if mode == 0:
        char.技能攻击力加成(0.11)
        char.所有速度增加(0.1, part=part)
        char.add_eq_params('hurted_ratio',0.12)
        pass
    if mode == 1:
        for skill in char.技能栏:
            if skill.是否有伤害 == 1 and skill.无色消耗 > 0 and skill.手搓 and skill.名称 not in char.觉醒技能:
                skill.手搓收益 += 4
        pass


# 固定装备：千丝萦绕腰带
def entry_877(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['不消耗无色小晶块的技能攻击力 +20%', '', '物理/魔法所受伤害 -15%', '技能消耗魔法值 -30%']
    if mode == 0:
        char.add_eq_params('hurted_ratio',0.15)
        char.MP消耗量加成(-0.3)
        pass
    if mode == 1:
        char.无色技能加成(0,0.2)


# 固定装备：暗影之迹短靴
def entry_1081(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['15~30级技能攻击力 +18%', '[基础精通]技能伤害 +52%', '', '攻击速度 +20%', '施放速度 +30%']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(part=part, x=0.20)
        char.施放速度增加(0.30)
        char.基础精通加成(0.52)
        char.技能倍率加成(15, 30, 0.18, type="active")
        pass


# 固定装备：黑猫头盔
def entry_1059(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['1~30级技能攻击力 +10%', '[基础精通]技能伤害 +20%', '', '普通攻击、跳跃、前冲攻击时，有10%的几率，增加300%的攻击力。']
    if mode == 0:
        char.基础精通加成(0.2)
        char.技能倍率加成(1, 30, 0.1)
    if mode == 1:
        pass


# 固定装备：梵塔黑色长裤
def entry_1062(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +15%', '技能冷却时间 +15%', '[基础精通]攻击力 +53%', '', '攻击速度 +15%', '施放速度 +15%']
    if mode == 0:
        pass
    if mode == 1:
        char.基础精通加成(0.53)
        char.攻击速度增加(part=part, x=0.15)
        char.施放速度增加(0.15)
        char.技能冷却缩减(1, 100, - 0.15)
        char.技能攻击力加成(0.15)
        pass


# 固定装备：子夜的圣域
def entry_1110(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '技能冷却时间恢复速度 +12% (觉醒技能除外)', '- 需穿戴[自由之缚手镯]装备。', '', '攻击速度 +10%', '施放速度 +15%']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击速度增加(part=part, x=0.10)
        char.施放速度增加(0.15)
        if char.check_equ_by_name('自由之缚手镯'):
            char.技能攻击力加成(part=part, x=0.1)
            char.技能恢复加成(1, 100, 0.12, excName=char.觉醒技能)
        else:
            return '未穿戴[自由之缚手镯]'


# 固定装备：静谧之像
def entry_1056(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['15~35级技能攻击力 +25%', '15~35级技能冷却时间恢复速度 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能倍率加成(15, 35, 0.25)
        char.技能恢复加成(15, 35, 0.1)
        pass


# 固定装备：无色冰晶耳环
def entry_999(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '不消耗无色小晶块的技能冷却时间 -30%', '', '消耗无色小晶块的技能冷却时间 +15% (觉醒技能除外)']
    if mode == 0:
        char.技能攻击力加成(0.1)
        for skill in char.技能队列:
            if skill["无色消耗"] == 0:
                skill["CDR"] *= 0.7
            if skill["无色消耗"] > 0 and char.get_skill_by_name(skill['名称']).所在等级 not in [50, 85, 100]:
                skill["CDR"] *= 1.15
    if mode == 1:
        pass


# 固定装备：全息通话器
def entry_1060(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['1~30级主动技能攻击力 +12%', '', '物理/魔法伤害所受伤害 -15%']
    if mode == 0:
        char.技能倍率加成(1, 30, 0.12, type='active')
        char.add_eq_params('hurted_ratio',0.15)
        pass
    if mode == 1:
        pass


# 固定装备：千里之音手镯
def entry_983(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[基础精通]技能伤害 +44%', '15~30级技能攻击力 +21%']
    if mode == 0:
        char.基础精通加成(0.44)
        char.技能倍率加成(15, 30, 0.21, type="active")
    if mode == 1:
        pass


# 固定装备：玉化亡灵肩甲
def entry_1169(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%', '', '@[背后袭击]@', '- 向最强敌人生成标志。', '- 施放[后跳]时，移动至敌人的后方。 (冷却时间10秒)', '', '所有异常状态抗性 +10%']
    if mode == 0:
        char.所有异常抗性加成(0.1)
        char.技能攻击力加成(part=part, x=0.11)
        pass
    if mode == 1:
        pass


# 固定装备：生命本源背包
def entry_971(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '', '物理/魔法暴击率 +5%', '光属性抗性 +50']
    if mode == 0:
        char.光属性抗性加成(50)
    if mode == 1:
        char.技能攻击力加成(0.07)
        char.暴击率增加(0.05)
        pass

# 固定装备：幻影之触控制面板
def entry_833(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%','','物理/魔法暴击率 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.暴击率增加(0.02 * 5)
        char.技能攻击力加成(0.08)
        pass


# 固定装备：缥缈的知识
def entry_837(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '', '物理/魔法暴击率 +5%', '暗属性抗性 +50']
    if mode == 0:
        char.暗属性抗性加成(50)
    if mode == 1:
        char.技能攻击力加成(0.07)
        char.暴击率增加(0.05)


# 固定装备：黎明圣杯
def entry_1137(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['使用指令施放技能时，根据输入的方向键数量，增加技能伤害。 (觉醒技能除外)', '- 1个方向键：技能伤害 +7%', '- 2个方向键：技能伤害 +9%', '- 3个方向键：技能伤害 +11%', '- 4个方向键：技能伤害 +15%', '', '攻击速度 +15%', '施放速度 +15%', '移动速度 +15%']
    if mode == 0:
        char.所有速度增加(part=part, x=0.05*3)
        pass
    if mode == 1:
        for i in char.技能栏:
            if i.手搓 == True and i.名称 not in char.觉醒技能 and not (i.名称 == '神罚之锤' and char.实际名称 == 'crusader_male_carry'):
                if i.是否有伤害 == 1:
                    倍率 = 1.0
                    if i.手搓指令数 == 1:
                        倍率 = 1.07
                    if i.手搓指令数 == 2:
                        倍率 = 1.09
                    if i.手搓指令数 == 3:
                        倍率 = 1.11
                    if i.手搓指令数 == 4:
                        倍率 = 1.15
                    i.倍率 *= 倍率
                if i.名称 == '鬼连斩':
                    char.get_skill_by_name("鬼连斩：极").额外加成 /= 倍率


# 固定装备：挖掘之王部件
def entry_889(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['辅助职业技能伤害 +3%', '技能冷却时间 -10% (觉醒技能除外)', '所有属性强化 +10', '', '@[灵魂武器]@', '普通攻击、跳跃攻击、前冲攻击时，召唤可使用剑击的灵魂武器。', '- 施放技能时，可剑击次数 +5', '- 可剑击次数为50时，消耗所有次数发动强力剑击。', '- 剑击与强力剑击分别造成总攻击强化数值60%、2400%的伤害。', '', '攻击速度 +25%', '施放速度 +40%']
    if mode == 0:
        char.特效.append({"power": 24, "hit": 1})
        char.所有属性强化加成(10)
        char.攻击速度增加(part=part, x=0.05 * 5)
        char.施放速度增加(0.08 * 5)
        char.技能冷却缩减(1, 100, 0.1, excName=char.觉醒技能)
        if char.bufferCarry:
            char.技能攻击力加成(0.03)
        pass
    if mode == 1:
        pass


# 固定装备：死亡之冠
def entry_903(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '', '物理/魔法所受伤害 -10%']
    if mode == 0:
        char.add_eq_params('hurted_ratio',0.1)
        char.技能攻击力加成(0.09)
        pass
    if mode == 1:
        pass


# 固定装备：不祥的暗纹石板
def entry_1154(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '进入霸体状态。', '', '跳跃期间可以再次跳跃。']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.08)
        pass
    if mode == 1:
        pass


# 固定装备：心之潜影
def entry_978(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '', '物理/魔法暴击率 +5%', '火属性抗性 +50']
    if mode == 0:
        char.火属性抗性加成(50)
        char.技能攻击力加成(0.07)
        char.暴击率增加(0.05)
    if mode == 1:
        pass


# 固定装备：正义骑士面具
def entry_1158(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间 -12%。 (觉醒技能除外)', '', '跳跃状态下，按住[跳跃键]0.5秒，可进入飞行状态，持续5秒。 (冷却时间30秒)', '- 连续按方向键，可在空中前冲。 (最多2次)', '', '进入霸体状态。', '', '物理/魔法所受伤害 -15%']
    if mode == 0:
        char.技能冷却缩减(1, 100, 0.12, excName=char.觉醒技能)
        char.add_eq_params('hurted_ratio',0.15)
        pass
    if mode == 1:
        pass


# 固定装备：虚影幻息眼镜
def entry_996(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '', '@[火焰步伐]@', '脚步携带火焰气息，移动时生成火焰地带，效果持续3秒。', '- 敌人接触火焰地带时，进入灼伤状态15秒。 (冷却时间10秒)', '- 造成总攻击强化数值4%的伤害。', '', '攻击灼伤状态的敌人时，发生火焰爆炸。 (冷却时间0.5秒)', '造成总攻击强化数值28%的伤害。']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.04)
        char.异常时间['灼伤'][3] = min(char.异常时间['灼伤'][3],10)
        if "灼伤" not in pa.get_state_type():
            pa.state_type.append('灼伤')
        pass
    if mode == 1:
        pass


# 固定装备：梦之呼唤
def entry_994(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间恢复速度 +50% (觉醒技能除外)', '- 需要穿戴装备[永恒的心愿]。', '', '睡眠抗性 -10%']
    if mode == 0:
        char.异常抗性加成('睡眠', -0.1)
        if char.check_equ_by_name('永恒的心愿'):
            char.技能恢复加成(1, 100, 0.5)
        else:
            return '未穿戴[永恒的心愿]'
        pass
    if mode == 1:
        pass


# 固定装备：命运的魔法箱
def entry_1826(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['@[白色魔法师]@', '该装备的附魔效果 +100%', '- 不包含：技能等级增加效果，冒险家名望增加效果', '', '生命值最大值 +200', '魔法值最大值 +315']
    if mode == 0:
        char.部位附魔[part](char, rate=1,calcLv=False,part=part)
    if mode == 1:
        pass

# 固定装备：猎龙者之证 - 龙骨角笛
def entry_887(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +30', '职业60级主动技能等级 +10', '- 不包含：[独家演奏]']
    if mode == 0:
        char.所有属性强化加成(30)
        pass
    if mode == 1:
        for i in char.技能栏:
            if i.所在等级 == 60 and i.是否主动 == 1 and i.名称 != '独家演奏':
                i.等级加成(10)
        pass


# 固定装备：摇曳的生命之水
def entry_995(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '', '@[寒冰步伐]@', '脚步携带寒冰气息，移动时生成冰河地带，效果持续3秒。', '- 敌人接触冰河地带时，进入冰冻状态5秒。 (冷却时间8秒)', '', '攻击冰冻状态的敌人时，发生寒冰爆炸。 (冷却时间0.5秒)', '- 造成总攻击强化数值40%的伤害']
    if mode == 0:
        char.技能攻击力加成(0.09)
        if "冰冻" not in pa.get_state_type():
            pa.state_type.append('冰冻')
        char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],8)
        pass
    if mode == 1:
        if '冰冻' in pa.get_state_type():
            char.特效.append({"power": 0.4, "hit": 1})
        pass


# 固定装备：空战型 : 战术螺旋桨无人机
def entry_963(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '', '@[无人机助攻]@', '攻击时召唤战斗无人机、被攻击时召唤急救无人机，投放补给箱。 (冷却时间30秒)', '- 战斗：60秒内所有速度 +15%', '- 急救：恢复30%的生命值/魔法值']
    if mode == 0:
        char.所有速度增加(0.15,part)
        char.技能攻击力加成(0.09)
        pass
    if mode == 1:
        pass


# 固定装备：自然灵息露珠
def entry_867(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '@[属性亲和 - 暗]@', '暗属性抗性越高，物理/魔法所受伤害越少。', '- 为敌人的攻击赋予暗属性', '', '被攻击时，恢复5%的生命值，效果持续5秒。 (冷却时间7秒)', '', '暗属性抗性 +25', '', '辅助职业技能伤害 +10%']
    if mode == 0:
        char.暗属性抗性加成(25)
        if char.bufferCarry:
            char.技能攻击力加成(0.1)
        char.技能攻击力加成(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：未知的黄金石碑
def entry_951(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%', '', '@[幽灵爆炸]@', '攻击时，召唤幽灵，追踪敌人并爆炸。 (冷却时间0.5秒)', '- 有30%的几率召唤2只', '- 造成总攻击强化数值200%的伤害', '', '所有异常状态抗性 +16%']
    if mode == 0:
        char.技能攻击力加成(0.12)
        char.所有异常抗性加成(0.16)
        pass
    if mode == 1:
        char.特效.append({"power": 2, "hit": 1})
        pass


# 固定装备：灵动的慧眼
def entry_949(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +13%', '', '@[电池炸弹]@', '随身携带一个电池，攻击时会过热产生爆炸。', '- 攻击5次时，电池过热', '- 过热的电池3秒后爆炸', '- 造成总攻击强化数值2000%的伤害', '', '物理/魔法暴击率 +7%', '攻击速度 +20%', '施放速度 +20%', '移动速度 +20%']
    if mode == 0:
        char.所有速度增加(0.2,part)
        char.技能攻击力加成(0.13)
        char.暴击率增加(0.7)
        pass
    if mode == 1:
        char.特效.append({"power": 20, "hit": 1})
        pass


# 固定装备：陆战型 : 战术车轮无人机
def entry_805(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +13%', '', '攻击速度 +10%', '施放速度 +10%', '移动速度 +10%']
    if mode == 0:
        char.所有速度增加(part=part, x=0.1)
        char.技能攻击力加成(part=part, x=0.13)
        pass
    if mode == 1:
        pass


# 固定装备：猎龙者之证 - 龙心加工石
def entry_888(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '职业70级主动技能等级 +10', '- 不包含：[永恒的占有]、[圣洁之翼]']
    if mode == 0:
        char.技能攻击力加成(0.1)
        pass
    if mode == 1:
        for i in char.技能栏:
            if i.所在等级 == 70 and i.是否主动 == 1 and i.名称 not in ['永恒的占有','圣洁之翼']:
                i.等级加成(10)
        pass


# 固定装备：诅咒之心
def entry_1101(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +15%', '', '@[坚不可摧的心]@', '被击时，技能不会强制中断。 (冷却时间10秒)', '- 强制控制除外']
    if mode == 0:
        char.技能攻击力加成(0.15)
        pass
    if mode == 1:
        pass


# 固定装备：多德卡全息图
def entry_1127(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '技能冷却时间恢复速度 +20% (觉醒技能除外)']
    if mode == 0:
        char.技能恢复加成(1, 100, 0.2, excName=char.觉醒技能)
        char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


# 固定装备：生机盎然的绿宝石
def entry_865(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '@[属性亲和 - 光]@', '光属性抗性越高，物理/魔法所受伤害越少。', '- 为敌人的攻击赋予光属性', '', '被攻击时，恢复5%的生命值，效果持续5秒。 (冷却时间7秒)', '', '光属性抗性 +25', '辅助职业技能伤害 +10%']
    if mode == 0:
        char.技能攻击力加成(0.1)
        char.光属性抗性加成(25)
        if char.bufferCarry:
            char.技能攻击力加成(0.1)
    if mode == 1:
        pass


# 固定装备：未知文明 - 星石
def entry_864(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '@[属性亲和 - 冰]@', '冰属性抗性越高，物理/魔法所受伤害越少。', '- 为敌人的攻击赋予冰属性', '', '被攻击时，恢复5%的生命值，效果持续5秒。 (冷却时间7秒)', '', '冰属性抗性 +25', '辅助职业技能伤害 +10%']
    if mode == 0:
        char.技能攻击力加成(0.1)
        char.冰属性抗性加成(25)
        if char.bufferCarry:
            char.技能攻击力加成(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：奔涌之息宝石
def entry_1215(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间恢复速度 +50% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.5, excName=char.觉醒技能)
        pass


# 固定装备：不败奖牌
def entry_866(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '@[属性亲和 - 火]@', '火属性抗性越高，物理/魔法所受伤害越少。', '- 为敌人的攻击赋予火属性', '', '被攻击时，恢复5%的生命值，效果持续5秒。 (冷却时间7秒)', '', '火属性抗性 +25', '辅助职业技能伤害 +10%']
    if mode == 0:
        char.技能攻击力加成(0.1)
        char.火属性抗性加成(25)
        if char.bufferCarry:
            char.技能攻击力加成(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：吞噬黑暗的心脏
def entry_938(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['被攻击时，恢复10%的魔法值。 (冷却时间30秒)', '', '攻击速度 +30%', '施放速度 +40%', '移动速度 +30%', '物理/魔法所受伤害 -10%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.30)
        char.施放速度增加(0.40)
        char.移动速度增加(0.30)
        char.add_eq_params('hurted_ratio',0.1)
        pass
    if mode == 1:
        pass


# 固定装备：虚伪之石
def entry_31(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '@[白色魔法师]@', '该装备的附魔效果 +100%', '- 不包含：技能等级增加效果，冒险家名望增加效果', '', '生命值最大值 +200', '魔法值最大值 +315']
    if mode == 0:
        char.技能攻击力加成(0.08)
        char.部位附魔[part](char, rate=1,calcLv=False,part=part)
    if mode == 1:
        pass


# 固定装备：炙热之情宝石
def entry_1229(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '物理/魔法所受伤害 -10%', '睡眠抗性 -20%']
    if mode == 0:
        char.异常抗性加成('睡眠', -0.2)
        char.技能攻击力加成(0.1)
        char.add_eq_params('hurted_ratio',0.1)
        pass
    if mode == 1:
        pass


# 固定装备：逆流之魂灵珠
def entry_910(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['@[金牌收藏家]@', '携带及拥有的宠物数量为20个以上时，根据角色发动光谱效果。', '- 技能伤害 +12%', '- 技能冷却时间 -8% (觉醒技能除外)', '', '攻击速度 +15%', '施放速度 +15%', '移动速度 +15%']
    if mode == 0:
        char.所有速度增加(part=part, x=0.15)
        char.技能冷却缩减(1, 100, 0.08, excName=char.觉醒技能)
        char.技能攻击力加成(part=part, x=0.12)
        pass
    if mode == 1:
        pass


# 固定装备：和平捍卫者
def entry_1206(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%', '', '攻击速度 +20%', '施放速度 +30%', '移动速度 +20%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.2)
        char.移动速度增加(0.2)
        char.施放速度增加(0.3)
        pass
    if mode == 1:
        char.技能攻击力加成(0.12)
        pass


# 固定装备：未知文明 - 双子石
def entry_1035(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冰属性强化 +50', '', '物理/魔法暴击率 +15%']
    if mode == 0:
        char.冰属性强化加成(50)
        pass
    if mode == 1:
        char.暴击率增加(0.15)
        pass


# 固定装备：吞噬风暴耳环
def entry_1171(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +13%', '', '消耗品的魔法值恢复效果 +50%', '技能魔法值消耗量 -20%', '', '魔法值最大值 +4196']
    if mode == 0:
        char.MP消耗量加成(-0.2)
        pass
    if mode == 1:
        char.技能攻击力加成(part=part, x=0.13)
        pass


# 固定装备：无尽的生机耳环
def entry_1036(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['光属性强化 +50', '', '物理/魔法暴击率 +15%']
    if mode == 0:
        char.光属性强化加成(50)
        pass
    if mode == 1:
        char.暴击率增加(0.15)
        pass


# 固定装备：脉冲之源耳环
def entry_988(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +17%', '- 需穿戴[天才技术大师的加厚长靴]装备。']
    if mode == 0:
        if char.check_equ_by_name('天才技术大师的加厚长靴'):
            char.技能攻击力加成(0.17)
        else:
            return '未穿戴[天才技术大师的加厚长靴]'
    if mode == 1:
        pass


# 固定装备：万物引力耳环
def entry_1066(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +14%', '', '前冲攻击时，疾跑至前方。 (冷却时间5秒)', '', '移动速度 +20%']
    if mode == 0:
        char.移动速度增加(0.2)
        pass
    if mode == 1:
        char.技能攻击力加成(part=part, x=0.14)
        pass


# 固定装备：猎龙者之证 - 龙鳞耳环
def entry_1128(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +30', '职业75级主动技能的等级 +10', '- 不包含：[圣灵符文]、[神圣之光]、[风雷啸]', '', '物理/魔法暴击率 +5%<']
    if mode == 0:
        char.所有属性强化加成(30)
        for i in char.技能栏:
            if i.名称 == '时空禁制' or (i.所在等级 == 75 and i.是否主动 == 1 and i.名称 not in ['圣灵符文', '神圣之光', '风雷啸']):
                i.等级加成(10)
        pass
    if mode == 1:
        pass


# 固定装备：诅咒的枷锁
def entry_806(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '自身处于出血状态时，技能冷却时间恢复速度 +30% (觉醒技能除外)', '', '生命值恢复效果 +50%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.02)
        pass
    if mode == 1:
        if '出血' in pa.own_type:
            char.技能恢复加成(1, 100, 0.3, excName=char.觉醒技能)
        pass


# 固定装备：战争之主耳环
def entry_1037(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性强化 +50', '', '物理/魔法暴击率 +15%']
    if mode == 0:
        char.火属性强化加成(50)
        pass
    if mode == 1:
        char.暴击率增加(0.15)
        pass


# 固定装备：隐匿之叹息耳环
def entry_991(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +15%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.15)
        pass


# 固定装备：爆炸型 : 小型战术信号弹
def entry_932(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '攻击速度 +30%', '施放速度 +30%', '移动速度 +45%']
    if mode == 0:
        char.攻击速度增加(0.3,part)
        char.施放速度增加(0.3)
        char.技能攻击力加成(0.1)
        char.移动速度增加(0.45)
        pass
    if mode == 1:
        pass


# 固定装备：晨曦的新芽耳环
def entry_1034(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暗属性强化 +50', '', '物理/魔法暴击率 +15%']
    if mode == 0:
        char.暗属性强化加成(50)
        pass
    if mode == 1:
        char.暴击率增加(0.15)
        pass


# 固定装备：时间之念耳环
def entry_32(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['@[白色魔法师]@', '该装备的附魔效果 +100%', '- 不包含：技能等级增加效果，冒险家名望增加效果', '', '物理/魔法所受伤害 -10%', '攻击时，恢复1500点魔法值 (冷却时间1秒)']
    if mode == 0:
        char.部位附魔[part](char, rate=1,calcLv=False,part=part)
    if mode == 1:
        pass


# 固定装备：灵犀之音耳环
def entry_873(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%', '', '@[冰冻魔法]@', '在聊天中输入“冰”/“叮”使角色进入/解除冰冻状态。', '- 冰冻状态期间，物理/魔法所受伤害 -30%', '- 进入冰冻状态时，恢复20%的生命值']
    if mode == 0:
        if '冰冻' in pa.own_type:
            char.add_eq_params('hurted_ratio',0.3)
        pass
    if mode == 1:
        char.技能攻击力加成(0.12)
        pass


# 固定装备：徘徊之魄耳环
def entry_897(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '技能冷却时间恢复速度 +20% (觉醒技能除外)', '', '待机、行走时，移动速度 +200%/Y轴移动速度 +50%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.2, excName=char.觉醒技能)
        char.技能攻击力加成(0.1)
        pass


# 固定装备：苍空飞羽耳环
def entry_915(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '', '@[殷红碎裂]@攻击领主、稀有、精英怪物时，剩余的生命值 -1%', '- 该效果在攻击10、50、250、1250、6250次时发动', '- 辅助职业除外', '', '攻击速度 +15%', '施放速度 +22.5%', '移动速度 +15%', '出血抗性 +20%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.15)
        char.移动速度增加(0.15)
        char.施放速度增加(0.225)
        char.异常抗性加成('出血', 0.2)
        char.技能攻击力加成(0.06)
        pass
    if mode == 1:
        pass


# 固定装备：未知文明 - 人面石
def entry_875(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '', '物理/魔法暴击率 +5%', '冰属性抗性 +50']
    if mode == 0:
        char.冰属性抗性加成(50)
    if mode == 1:
        char.技能攻击力加成(0.07)
        char.暴击率增加(0.05)
        pass


# 固定装备：古老的探险家大衣
def entry_798(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +10', '出血伤害 +20%', '', '输入[装备属性指令]时，将地图上掉落的道具移动至角色脚下。 (冷却时间30秒)', '', '攻击时，使所有敌人进入出血状态15秒。 (冷却时间10秒)', '', '出血抗性 +10%']
    if mode == 0:
        char.所有属性强化加成(10)
        char.异常时间['出血'][3] = min(char.异常时间['出血'][3],10)
        if '出血' not in pa.get_state_type():
            pa.state_type.append('出血')
        char.异常增伤('出血', 0.2)
        char.异常抗性加成('出血', 0.1)
        pass
    if mode == 1:
        pass


# 固定装备：轰天裂地石甲
def entry_801(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +10', '中毒伤害 +20%', '', '@[召唤]@', '输入[装备属性指令]时，可以将1名队员移动到自身所在位置。 (冷却时间10秒)', '- 被召唤的队员20秒内移动速度 +20%', '- 队员处于无敌或霸体状态时无法选择', '', '攻击时，使所有敌人进入中毒状态15秒。 (冷却时间10秒)', '', '中毒抗性 +10%']
    if mode == 0:
        char.所有属性强化加成(10)
        if '中毒' not in pa.get_state_type():
            pa.state_type.append('中毒')
        char.异常时间['中毒'][3] = min(char.异常时间['中毒'][3],10)
        char.异常抗性加成('中毒', 0.1)
        char.异常增伤('中毒', 0.2)
        pass
    if mode == 1:
        pass


# 固定装备：极魂之驱上衣
def entry_1065(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '@[巨大化]@', '输入[装备属性指令]时，角色变大，效果持续25秒。 (冷却时间60秒)', '- 进入无法攻击状态，前冲/跳跃时发动冲击波', '- 物理/魔法所受伤害 -20%', '-  再次输入[装备属性指令]时解除角色变大效果', '- 前冲/跳跃冲击波分别造成总攻击强化数值288%/1440%的伤害', '', '物理/魔法防御力 +10000']
    if mode == 0:
        char.add_eq_params('defense',10000)
        char.技能攻击力加成(0.08)
        pass
    if mode == 1:
        pass


# 固定装备：钢筋铁骨披肩
def entry_1038(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '技能范围 +10%', '', '获得掉落的道具时，增加30%的移动速度，效果持续30秒。']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.1)
        char.multiply_eq_params('skill_range_multi',1.1)
        char.技能攻击力加成(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：自由之翼护肩
def entry_809(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '', '攻击速度 +30%', '施放速度 +30%', '移动速度 +30%', '物理/魔法所受伤害 -15%', '火属性抗性 +10']
    if mode == 0:
        char.所有速度增加(part=part, x=0.3)
        char.火属性抗性加成(10)
        char.add_eq_params('hurted_ratio',0.15)
        char.技能攻击力加成(part=part, x=0.05)
        pass
    if mode == 1:
        pass


# 固定装备：猎龙者
def entry_1083(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%', '所有属性抗性 +15']
    if mode == 0:
        char.技能攻击力加成(0.11)
        char.所有属性抗性加成(15)
        pass
    if mode == 1:
        pass


# 固定装备：不倦旅程护腿
def entry_1175(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '技能范围 +27%', '', '移动速度 +10%']
    if mode == 0:
        char.移动速度增加(0.10)
        char.技能攻击力加成(0.07)
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.27)
        char.multiply_eq_params('skill_range_multi',1.27)
        pass
    if mode == 1:
        pass


# 固定装备：隐匿的自然生命
def entry_968(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +10', '', '@[自然之怒]@', '攻击时，发动4种效果中的1种。 (冷却时间0.5秒)', '- 火属性：灼热火焰', '- 冰属性：寒冰利锥', '- 光属性：闪电重击', '- 暗属性：黑暗爆炸', '- 造成总攻击强化数值300%的伤害', '', '攻击时，使所有敌人进入灼伤状态15秒。 (冷却时间10秒)']
    if mode == 0:
        char.所有属性强化加成(10)
        if '灼伤' not in pa.get_state_type():
            pa.state_type.append('灼伤')
        char.异常时间['灼伤'][3] = min(char.异常时间['灼伤'][3],10)
        char.特效.append({"power": 0.3, "hit": 1})
        pass
    if mode == 1:
        pass


# 固定装备：神谕之信念
def entry_1014(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冰属性强化 +50']
    if mode == 0:
        char.冰属性强化加成(50)
        pass
    if mode == 1:
        pass


# 固定装备：星灭光离腰带
def entry_1012(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '技能冷却时间恢复速度 +15% (觉醒技能除外)', '', '攻击速度 +45%', '施放速度 +45%', '移动速度 +45%']
    if mode == 0:
        char.所有速度增加(part=part, x=0.45)
        char.技能恢复加成(1, 100, 0.15, excName=char.觉醒技能)
        char.技能攻击力加成(part=part, x=0.07)
        pass
    if mode == 1:
        pass


# 固定装备：亘古的悬空石腰带
def entry_1123(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间恢复速度 +25% (觉醒技能除外)', '所有属性强化 +10', '', '使自身进入无法解除的中毒状态。', '', '攻击时，使敌人进入中毒状态10秒。 (冷却时间5秒)']
    if mode == 0:
        if '中毒' not in pa.own_type:
            pa.own_type.append('中毒')
        if '中毒' not in pa.get_state_type():
            pa.state_type.append('中毒')
        char.所有属性强化加成(10)
        char.技能恢复加成(1, 100, 0.25, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 固定装备：循环的自然之法
def entry_947(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '', '@[黑暗攻击]@', '攻击时，根据暗属性强化数值发动暗属性元素攻击。 (冷却时间1.5秒)', '- 100~149：暗黑爆炸', '- 150~249：暗黑球', '- 250以上：黑洞', '- 分别造成总攻击强化数值720%/920%/1480%的伤害。', '- 黑洞使敌人进入失明状态10秒。 (冷却时间30秒)', '攻击速度 +10%', '施放速度 +15%', '暗属性抗性 +20']
    if mode == 0:
        char.暗属性抗性加成(20)
        char.攻击速度增加(part=part, x=0.1)
        char.施放速度增加(0.15)
        pass
    if mode == 1:
        char.技能攻击力加成(part=part, x=0.02)
        char.特效.append({"power": 14.8, "hit": 1})
        pass


# 固定装备：暴走之躯战靴
def entry_930(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +17%', '', '物理/魔法防御力 +16000']
    if mode == 0:
        char.add_eq_params('defense',16000)
        pass
    if mode == 1:
        char.技能攻击力加成(part=part, x=0.17)
        pass


# 固定装备：黑暗吞噬短靴
def entry_1220(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '技能冷却时间恢复速度 +15% (觉醒技能除外)', '中毒伤害 +10%', '','攻击速度 +15%', '施放速度 +15%', '移动速度 +15%']
    if mode == 0:
        char.异常增伤('中毒', 0.10)
        char.移动速度增加(0.15)
        char.攻击速度增加(part=part, x=0.15)
        char.施放速度增加(0.15)
        char.技能攻击力加成(part=part, x=0.05)
        char.技能恢复加成(1, 100, 0.15, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 固定装备：天才技术大师的研究服上衣
def entry_939(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '技能冷却时间恢复速度 +20% (觉醒技能除外)', '', '攻击时，使500px内引发爆炸。 (冷却时间10秒)', '- 爆炸造成总攻击强化数值1300%的伤害。']
    if mode == 0:
        char.技能攻击力加成(0.04)
        char.特效.append({"power": 13, "hit": 1})
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.2, excName=char.觉醒技能)
        pass


# 固定装备：澎湃之心上衣
def entry_815(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '@[不灭之术]@', '生命终结判定时，发动[不灭之术]，效果持续5秒。 (冷却时间300秒)', '- 恢复10%的生命值', '- 其他生命值恢复效果及伤害变为无效', '- [不灭之术]结束时，锁定生命值最大值的30%', '', '物理/魔法暴击率 +5%']
    if mode == 0:
        char.技能攻击力加成(0.08)
        char.暴击率增加(0.05)
        pass
    if mode == 1:
        pass


# 固定装备：深渊之源上衣
def entry_799(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '火/冰/光/暗攻击属性', '', '物理/魔法暴击率 +10%']
    if mode == 0:
        char.技能攻击力加成(0.09)
        char.暴击率增加(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：御力装甲上衣
def entry_839(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +10', '灼伤伤害 +20%', '', '攻击时，使所有敌人进入灼伤状态15秒。 (冷却时间10秒)', '', '灼伤抗性 +10%']
    if mode == 0:
        if '灼伤' not in pa.get_state_type():
            pa.state_type.append('灼伤')
        char.异常时间['灼伤'][3] = min(char.异常时间['灼伤'][3],10)
        char.所有属性强化加成(10)
        char.异常增伤('灼伤', 0.20)
        char.异常抗性加成('灼伤', 0.10)
    if mode == 1:
        pass


# 固定装备：霜云暗影长裤
def entry_1015(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['光属性强化 +50']
    if mode == 0:
        char.光属性强化加成(50)
        pass
    if mode == 1:
        pass


# 固定装备：苍龙闪影护腿
def entry_1086(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '所有属性抗性 +15']
    if mode == 0:
        char.技能攻击力加成(0.08)
        char.所有属性抗性加成(15)
        pass
    if mode == 1:
        pass


# 固定装备：耀武之威护肩
def entry_892(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['出血伤害 +15%', '', '攻击时，使所有敌人进入出血状态10秒。 (冷却时间5秒)', '', '出血抗性 +10%']
    if mode == 0:
        if '出血' not in pa.get_state_type():
            pa.state_type.append('出血')
        char.异常时间['出血'][3] = min(char.异常时间['出血'][3],5)
        char.异常增伤('出血', 0.15)
        char.异常抗性加成('出血', 0.1)
        pass
    if mode == 1:
        pass


# 固定装备：绽放的自然生命
def entry_944(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '', '@[冰冻攻击]@', '攻击时，根据冰属性强化数值发动冰属性元素攻击。 (冷却时间1.5秒)', '- 100~149：冰冻针刺', '- 150~249：冰冻吐息', '- 250以上：暴雪', '- 分别造成总攻击强化数值720%/920%/1480%的伤害。', '- 暴雪使命中敌人进入冰冻状态10秒。 (冷却时间30秒)', '', '攻击速度 +10%', '施放速度 +15%', '冰属性抗性 +20']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.02)
        char.冰属性抗性加成(20)
        char.攻击速度增加(part=part, x=0.1)
        char.施放速度增加(0.15)
        pass
    if mode == 1:
        char.特效.append({"power": 14.8, "hit": 1})
        pass


# 固定装备：隐匿之光护肩
def entry_883(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '出血伤害 +20%', '使自身进入无法解除的出血状态。', '', '物理/魔法暴击率 +10%', '攻击速度 +5%', '施放速度 +7.5%']
    if mode == 0:
        if '出血' not in pa.own_type:
            pa.own_type.append('出血')
        char.异常增伤('出血', 0.2)
        char.技能攻击力加成(0.02)
        pass
    if mode == 1:
        char.暴击率增加(0.1)
        char.攻击速度增加(part=part, x=0.05)
        char.施放速度增加(0.075)
        pass


# 固定装备：御雷腰带
def entry_940(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '火属性强化 +20', '冰属性强化 +20', '暗属性强化 +20', '', '攻击时，使敌人进入感电状态15秒。 (冷却时间10秒)']
    if mode == 0:
        char.火属性强化加成(20)
        char.冰属性强化加成(20)
        char.暗属性强化加成(20)
        char.技能攻击力加成(0.1)
        if '感电' not in pa.get_state_type():
            pa.state_type.append('感电')
        char.异常时间['感电'][3] = min(char.异常时间['感电'][3],10)
        pass
    if mode == 1:
        pass


# 固定装备：高科技战术腰带
def entry_870(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%', '获得生命值最大值10%的@[填充型保护罩]@。', '', '物理/魔法所受伤害 -30%']
    if mode == 0:
        char.技能攻击力加成(0.12)
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.1)
        char.add_eq_params('hurted_ratio',0.3)
        pass
    if mode == 1:
        pass


# 固定装备：流星飞电战靴
def entry_919(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +17%', '', '攻击时，闪电落下，使敌人进入感电状态15秒。 (冷却时间10秒)', '- 造成总攻击强化数值84%的伤害。', '', '使自身进入无法解除的感电状态。', '', '攻击速度 +20%', '施放速度 +30%', '移动速度 +20%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.2)
        char.施放速度增加(0.3)
        char.移动速度增加(0.2)
        char.技能攻击力加成(part=part, x=0.17)
        if '感电' not in pa.get_state_type():
            pa.state_type.append('感电')
        if '感电' not in pa.own_type:
            pa.own_type.append('感电')
        char.异常时间['感电'][3] = min(char.异常时间['感电'][3],10)
        pass
    if mode == 1:
        char.特效.append({"power": 0.84, "hit": 1})
        pass


# 固定装备：无畏的勇气短靴
def entry_1223(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +326.0%', '技能伤害 +9%', '1~25级技能等级 +2', '', '辅助职业技能伤害 +5%']
    if mode == 0:
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
        char.技能等级加成('所有', 1, 25, 2)
        char.攻击强化加成(params[0])
        char.技能攻击力加成(0.09)
        pass
    if mode == 1:
        pass


# 固定装备：大地的馈赠上衣
def entry_946(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '', '@[火力攻击]@', '攻击时，根据火属性强化数值，发动火属性元素攻击。 (冷却时间1.5秒)', '- 火属性强化为100~149：发动火焰爆炸', '- 火属性强化为150~249：发动地炎', '- 火属性强化为250以上：发动陨石', '- 分别造成总攻击强化数值的 720%/920%/1480%的伤害', '- 陨石攻击使敌人进入灼伤状态15秒 (冷却时间10秒)', '', '攻击速度 +10%', '施放速度 +15%', '火属性抗性 +20']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.02)
        char.火属性抗性加成(20)
        char.攻击速度增加(part=part, x=0.1)
        char.施放速度增加(0.15)
        pass
    if mode == 1:
        char.特效.append({"power": 14.8, "hit": 1})
        pass


# 固定装备：白金流光夹克 ， 白虹贯日长裤 ， 白玉无邪腰带
def entry_1361(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '@[白色魔法师]@', '该装备的附魔效果 +100%', '- 不包含：技能等级增加效果、冒险家名望增加效果', '', '生命值最大值 +200', '魔法值最大值 +315']
    if mode == 0:
        char.技能攻击力加成(0.08)
        char.部位附魔[part](char, rate=1,calcLv=False,part=part)
    if mode == 1:
        pass


# 固定装备：屠龙者
def entry_975(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '火/冰/光/暗攻击属性', '', '所有属性抗性 +25']
    if mode == 0:
        char.技能攻击力加成(0.09)
        char.所有属性抗性加成(25)
        pass
    if mode == 1:
        pass


# 固定装备：守护之王者铠甲
def entry_800(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '@[埃癸斯之盾]@', '输入[装备属性指令]时，召唤埃癸斯之盾，效果持续5秒。 (冷却时间45秒)', '- 埃癸斯之盾生命值相当于自身生命值最大值的30%。', '- 防御敌人的远程攻击并限制敌人移动', '', '攻击时，恢复2%的生命值。 (冷却时间1秒)', '物理/魔法防御力 +20%']
    if mode == 0:
        char.技能攻击力加成(0.08)
        char.add_eq_params('defense_ratio',0.2)
        pass
    if mode == 1:
        pass


# 固定装备：舞台的华丽
def entry_1098(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '施放[后跳]期间，移动速度 +200%', '', '物理/魔法所受伤害 -10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.08)
        char.add_eq_params('hurted_ratio',0.1)
        pass


# 固定装备：沧海之覆护腿
def entry_842(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['中毒伤害 +15%', '', '攻击时，使所有敌人进入中毒状态15秒。 (冷却时间10秒)', '', '中毒抗性 +10%']
    if mode == 0:
        if '中毒' not in pa.get_state_type():
            pa.state_type.append('中毒')
        char.异常时间['中毒'][3] = min(char.异常时间['中毒'][3],10)
        char.异常抗性加成('中毒', 0.10)
        char.异常增伤('中毒', 0.15)
    if mode == 1:
        pass


# 固定装备：永不破碎的信念
def entry_1013(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暗属性强化 +50']
    if mode == 0:
        char.暗属性强化加成(50)
        pass
    if mode == 1:
        pass


# 固定装备：高科技战术护腿
def entry_1179(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '@[格挡守卫]@', '使用防御技能阻挡敌人攻击时，控制敌人2秒。', '- 防御技能：[格挡]、[招架]、[格挡反击]、[武器格挡]、[盾牌格挡]、[圣盾]、[远程格挡]', '- 施放技能后0.5秒内防御敌人的攻击时发动']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(part=part, x=0.08)
        pass


# 固定装备：荒漠之界长裤
def entry_964(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性强化 +40', '', '攻击时，生成1个火种，持续5秒。 (冷却时间0.1秒)', '- 火种每生成5个时，引发爆炸。', '- 火种造成总攻击强化数值96%的伤害。', '', '火属性抗性 +25']
    if mode == 0:
        char.火属性强化加成(40)
        char.火属性抗性加成(25)
        pass
    if mode == 1:
        char.特效.append({"power": 0.96, "hit": 1})
        pass


# 固定装备：望穿尽头的视线
def entry_911(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%', '', '物理/魔法暴击率 +5%']
    if mode == 0:
        char.技能攻击力加成(0.11)
        pass
    if mode == 1:
        pass


# 固定装备：冰玉之蚀肩甲
def entry_1188(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '中毒伤害 +20%', '', '使自身进入无法解除的中毒状态。', '', '物理/魔法暴击率 +10%', '攻击速度 +5%', '施放速度 +7.5%']
    if mode == 0:
        char.异常增伤('中毒', 0.20)
        char.技能攻击力加成(0.02)
        if '中毒' not in pa.own_type:
            pa.own_type.append('中毒')
        char.暴击率增加(0.1)
        char.攻击速度增加(part=part, x=0.05)
        char.施放速度增加(0.075)
        pass
    if mode == 1:
        pass


# 固定装备：白色的信念斗篷
def entry_1824(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '', '@[白色魔法师]@', '该装备的附魔效果 +100%', '- 不包含：技能等级增加效果，冒险家名望增加效果', '', '生命值最大值 +200', '魔法值最大值 +315']
    if mode == 0:
        char.技能攻击力加成(0.06)
        char.部位附魔[part](char, rate=1,calcLv=False,part=part)
    if mode == 1:
        pass


# 固定装备：远古之法则护肩
def entry_1080(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间恢复速度 +30% (觉醒技能除外)', '', '辅助职业技能伤害 +10%', '辅助职业技能冷却时间恢复速度 +20% (觉醒技能除外)']
    if mode == 0:
        if char.bufferCarry:
            char.技能攻击力加成(0.1)
            char.技能恢复加成(1, 100, 0.2,excName=char.觉醒技能)
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.3, excName=char.觉醒技能)
        pass


# 固定装备：华丽的清音护肩
def entry_835(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冷却时间恢复速度 +50% (觉醒技能除外)', '- 需要穿戴装备[永恒的心愿]。', '', '[受身蹲伏] 冷却时间 -50%', '持续[受身蹲伏]时，每秒恢复1%生命值。 (最多4秒)', '', '攻击速度 +10%', '施放速度 +10%', '移动速度 +10%', '睡眠抗性 -10%']
    if mode == 0:
        char.所有速度增加(part=part, x=0.1)
        char.异常抗性加成('睡眠', -0.1)
        pass
    if mode == 1:
        if char.check_equ_by_name('永恒的心愿'):
            char.技能恢复加成(1, 100, 0.5, excName=char.觉醒技能)
        else:
            return '未穿戴[永恒的心愿]'


# 固定装备：纯粹的自然秩序
def entry_945(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '', '@[闪电攻击]@', '攻击时，根据光属性强化数值发动光属性元素攻击。 (冷却时间1.5秒)', '- 100~149：闪光爆炸', '- 150~249：雷光链', '- 250以上：雷暴', '- 分别造成总攻击强化数值 720%/920%/1480%的伤害。', '- 雷暴攻击使敌人进入感电状态15秒。 (冷却时间10秒)', '攻击速度 +10%', '施放速度 +15%', '光属性抗性 +20']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.02)
        char.光属性抗性加成(20)
        char.攻击速度增加(part=part, x=0.10)
        char.施放速度增加(0.15)
        pass
    if mode == 1:
        char.特效.append({"power": 14.8, "hit": 1})
        pass


# 固定装备：骄傲的意志腰带
def entry_1053(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '感电伤害 +15%', '', '攻击时，使所有敌人进入感电状态15秒。 (冷却时间10秒)', '', '感电抗性 +10%']
    if mode == 0:
        if '感电' not in pa.get_state_type():
            pa.state_type.append("感电")
        char.异常时间['感电'][3] = min(char.异常时间['感电'][3],10)
        char.技能攻击力加成(0.07)
        char.异常抗性加成('感电', 0.10)
        char.异常增伤('感电', 0.15)
        pass
    if mode == 1:
        pass


# 固定装备：信念之喘息腰带
def entry_1197(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%', '', '攻击时，使所有敌人进入出血状态15秒。 (冷却时间10秒)', '', '使自身进入无法解除的出血状态。']
    if mode == 0:
        if '出血' not in pa.own_type:
            pa.own_type.append("出血")
        if '出血' not in pa.get_state_type():
            pa.state_type.append('出血')
        char.异常时间['出血'][3] = min(char.异常时间['出血'][3],5)
        char.技能攻击力加成(0.12)
        pass
    if mode == 1:
        pass


# 固定装备：静谧的星光腰带
def entry_1067(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +13%', '', '物理/魔法所受伤害 -15%']
    if mode == 0:
        pass
    if mode == 1:
        char.add_eq_params('hurted_ratio',0.15)
        char.技能攻击力加成(part=part, x=0.13)
        pass


# 固定装备：应尽之责腰带
def entry_1017(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +14%', '所有属性强化 +20']
    if mode == 0:
        char.技能攻击力加成(0.14)
        char.所有属性强化加成(20)
        pass
    if mode == 1:
        pass


# 固定装备：流星追月短靴
def entry_813(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%', '技能冷却时间 -15% (觉醒技能除外)', '', '魔法值最大值 +4196', '辅助职业技能伤害 +10%']
    if mode == 0:
        char.技能攻击力加成(0.11)
        char.技能冷却缩减(1, 100, 0.15, excName=char.觉醒技能)
        if char.bufferCarry:
            char.技能攻击力加成(0.1)
    if mode == 1:
        pass


# 固定装备：龙之开拓者短靴
def entry_1084(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +17%', '', '所有属性抗性 +15']
    if mode == 0:
        char.技能攻击力加成(0.17)
        char.所有属性抗性加成(15)
        pass
    if mode == 1:
        pass


# 固定装备：摇曳的残影短靴
def entry_1011(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +326.0%', '技能伤害 +9%', '技能冷却时间 -15% (觉醒技能除外)', '', '使自身进入无法解除的感电状态。', '', '所有属性抗性 +15']
    if mode == 0:
        if '感电' not in pa.own_type:
            pa.own_type.append('感电')
        char.攻击强化加成(params[0])
        char.技能攻击力加成(0.09)
        char.所有属性抗性加成(15)
        char.技能冷却缩减(1, 100, 0.15, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 固定装备：大地的践踏短靴
def entry_1005(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +17%', '', '每10秒赋予生命值最大值10%的保护罩。', '', '跳跃落地时，引发冲击波。', '- 产生冲击波时，使敌人进入眩晕状态3秒。 (冷却时间20秒)', '- 造成总攻击强化数值2200%的伤害。']
    if mode == 0:
        if '眩晕' not in pa.get_state_type():
            pa.state_type.append('眩晕')
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.1)
        pass
    if mode == 1:
        char.特效.append({"power": 22, "hit": 1})
        char.技能攻击力加成(part=part, x=0.17)
        pass


# 固定装备：祈愿之息短靴
def entry_1134(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +296.4%', '技能伤害 +17%', '', '@[暗影行者]@', '强化[受身蹲伏]', '- [受身蹲伏]无敌时间上限 +1秒', '- 可以隐藏在暗影中移动，效果持续2秒', '', '睡眠抗性 -20%']
    if mode == 0:
        char.攻击强化加成(params[0])
        char.异常抗性加成('睡眠', -0.2)
        char.技能攻击力加成(part=part, x=0.17)
        pass
    if mode == 1:
        pass


# 固定装备：暗影流光战袍
def entry_802(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '技能冷却时间恢复速度 +20% (觉醒技能除外)', '', '@[密语傀儡]@', '输入@[装备属性指令]@时，召唤密语傀儡。 (冷却时间10秒)', '- 使范围内的敌人进入诅咒状态30秒']
    if mode == 0:
        if '诅咒' not in pa.get_state_type():
            pa.state_type.append('诅咒')
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.2, excName=char.觉醒技能)
        char.技能攻击力加成(0.02)
        pass


# 固定装备：高科技战术指挥上衣
def entry_894(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '', '@[瞬移]@', '输入[装备属性指令]时，可以使用瞬移。 (冷却时间20秒)', '- 可按方向键调整方向。', '- 瞬移后，增加30%的移动速度，效果持续30秒。']
    if mode == 0:
        char.移动速度增加(0.3)
        char.技能攻击力加成(0.09)
        pass
    if mode == 1:
        pass


# 固定装备：暴风骑士
def entry_1104(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '技能冷却时间恢复速度 +10% (觉醒技能除外)', '', '按照魔法值消耗量的10%，恢复相应的生命值。', '', '物理/魔法防御力 +9000']
    if mode == 0:
        char.技能恢复加成(1, 100, 0.1, excName=char.觉醒技能)
        char.技能攻击力加成(0.03)
        char.add_eq_params('defense',9000)
        pass
    if mode == 1:
        pass


# 固定装备：沙漠星芒披肩
def entry_1199(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤伤害 +20%', '技能伤害 +2%', '给自己造成无法驱散的灼伤状态。', '', '', '物理/魔法暴击率 +10%', '攻击速度 +5%', '施放速度 +7.5%']
    if mode == 0:
        char.异常增伤('灼伤', 0.20)
        char.技能攻击力加成(0.02)
        if '灼伤' not in pa.own_type:
            pa.own_type.append('灼伤')
        char.暴击率增加(0.1)
        char.攻击速度增加(part=part, x=0.05)
        char.施放速度增加(0.075)
        pass
    if mode == 1:
        pass


# 固定装备：玉化亡灵腰甲
def entry_1001(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%', '', '聊天输入包含“哇”的文字时，召唤可搭乘的P0-原型机，持续时间40秒。 (冷却时间40秒)', '', '每秒恢复1000点生命值和魔法值。']
    if mode == 0:
        char.技能攻击力加成(0.12)
        pass
    if mode == 1:
        pass


# 固定装备：大地之翼腰带
def entry_950(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +13%', '', '@[光之领域]@', '攻击时，生成光之领域。 (冷却时间1秒)', '- 领域内物理/魔法所受伤害 -10%', '- 移动到领域之外时，光之领域消失', '', '生命值最大值 +10%', '所有异常状态抗性 +10%']
    if mode == 0:
        char.技能攻击力加成(0.13)
        char.所有异常抗性加成(0.1)
        pass
    if mode == 1:
        char.add_eq_params('hurted_ratio',0.1)
        pass


# 固定装备：蒸汽朋克音速鞋
def entry_1130(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +13%', '技能冷却时间恢复速度 +10% (觉醒技能除外)']
    if mode == 0:
        char.技能攻击力加成(0.13)
        char.技能恢复加成(1, 100, 0.1, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 固定装备：白色秘境皮鞋
def entry_1825(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['能伤害 +11%', '', '@[白色魔法师]@', '该装备的附魔效果 +100%', '- 不包含：技能等级增加效果，冒险家名望增加效果', '', '生命值最大值 +200', '魔法值最大值 +315']
    if mode == 0:
        char.技能攻击力加成(0.11)
        char.部位附魔[part](char, rate=1,calcLv=False,part=part)
    if mode == 1:
        pass


# 固定装备：百折不挠的梦想
def entry_817(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '@[梦之复苏]@', '使自身的生命终结成为一场梦，入睡。 (冷却时间300秒)', '- 睡眠状态中恢复10%的生命值', '- 睡眠状态中被攻击时，恢复15%的生命值。 (冷却时间1秒)', '- 睡眠状态中，即使被攻击，也不会解除睡眠。']
    if mode == 0:
        char.技能攻击力加成(0.08)
        pass
    if mode == 1:
        pass


# 固定装备：高贵的神意上衣
def entry_803(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '@[次元空间]@', '输入@[装备属性指令]@时，召唤次元空间，效果持续2秒。 (最多2次)', '- 进入次元空间后无敌。', '- 次元空间消失时，所有速度 +30%，效果持续10秒。', '', '生命值最大值 +30%', '所有异常状态抗性 +15%', '辅助职业技能伤害 +10%']
    if mode == 0:
        char.施放速度增加(0.3)
        char.攻击速度增加(part=part, x=0.3)
        char.移动速度增加(0.3)
        char.所有异常抗性加成(0.15)
        char.技能攻击力加成(0.08)
        if char.bufferCarry:
            char.技能攻击力加成(0.1)
    if mode == 1:
        pass


# 固定装备：玉化亡灵胸甲
def entry_1160(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '@[支配苍穹]@', '跳跃状态下，输入[装备属性指令]时，支配苍穹并召唤旋风，效果持续10秒。 (冷却时间20秒）', '- 吸附周围敌人', '- 进入霸体状态', '- 旋风造成总攻击强化数值2880%的伤害', '- 再次输入[装备属性指令]时落回地面', '', '攻击速度 +10%', '施放速度 +15%']
    if mode == 0:
        char.技能攻击力加成(0.08)
        char.攻击速度增加(0.1,part)
        char.施放速度增加(0.15)
        pass
    if mode == 1:
        char.特效.append({"power": 14.4, "hit": 1})
        pass


# 固定装备：双面星云皮大衣
def entry_816(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '', '@[英雄气魄]@', '生命终结判定时，推迟生命终结直到耗尽所有魔法值。 (冷却时间300秒)', '- 被击时，不消耗生命值但会消耗魔法值', '- 每秒减少2%的魔法值', '- 所有生命值恢复效果无效', '', '攻击速度 +5%', '施放速度 +7.5%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.05)
        char.施放速度增加(0.075)
        char.技能攻击力加成(part=part, x=0.09)
    if mode == 1:
        pass


# 固定装备：玉化亡灵腿甲
def entry_914(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['@[焦点巨星]@', '装扮栏中装扮个数超过120个时，获得聚光灯效果。', '- 技能伤害 +6%', '- 技能冷却时间 -8% (觉醒技能除外)', '- 进入霸体状态']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        char.技能冷却缩减(1, 100, 0.08, excName=char.觉醒技能)
        pass


# 固定装备：终极掌控者护腿
def entry_1195(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间 -15% (觉醒技能除外)', '', '使所有敌人进入诅咒状态5秒。 (冷却时间20秒)', '', '辅助职业技能伤害 +3%']
    if mode == 0:
        if '诅咒' not in pa.get_state_type():
            pa.state_type.append('诅咒')
        char.技能冷却缩减(1, 100, 0.15, excName=char.觉醒技能)
        if char.bufferCarry:
            char.技能攻击力加成(0.03)
        pass
    if mode == 1:
        pass


# 固定装备：侵蚀的意志护腿
def entry_1016(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性强化 +50']
    if mode == 0:
        char.火属性强化加成(50)
        pass
    if mode == 1:
        pass


# 固定装备：天才技术大师的百宝裤
def entry_896(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '站立、行走时进入伪装状态，回避率 +45% (冷却时间5秒)', '- 前冲、被击时解除效果']
    if mode == 0:
        char.技能攻击力加成(0.08)
        pass
    if mode == 1:
        pass


# 固定装备：电磁搜索者肩甲
def entry_909(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '感电伤害 +20%', '', '使自身进入无法解除的感电状态。', '', '物理/魔法暴击率 +10%', '攻击速度 +5%', '施放速度 +7.5%']
    if mode == 0:
        char.异常增伤('感电', 0.2)
        char.技能攻击力加成(0.02)
        if '感电' not in pa.own_type:
            pa.own_type.append('感电')
        char.暴击率增加(0.1)
        char.攻击速度增加(part=part, x=0.05)
        char.施放速度增加(0.075)
        pass
    if mode == 1:
        pass


# 固定装备：高科技御敌肩甲
def entry_853(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '使自身进入无法解除的感电状态。', '', '被击中后3秒内反击时，恢复之前所受伤害的70% （冷却时间3秒）']
    if mode == 0:
        char.技能攻击力加成(0.1)
        if '感电' not in pa.own_type:
            pa.own_type.append('感电')
        pass
    if mode == 1:
        pass


# 固定装备：龙食腐者
def entry_1085(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +14%', '', '所有属性抗性 +15']
    if mode == 0:
        char.技能攻击力加成(0.14)
        char.所有属性抗性加成(15)
        pass
    if mode == 1:
        pass


# 固定装备：动力之渊腰带
def entry_1049(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '技能冷却时间恢复速度 +15% (觉醒技能除外)', '', '攻击时，恢复2000点生命值/魔法值。 (冷却时间1秒)']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.08)
        char.技能恢复加成(1, 100, 0.15, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 固定装备：音律的夙愿
def entry_934(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '技能冷却时间 -10% (觉醒技能除外)', '', '睡眠抗性 -10%']
    if mode == 0:
        char.异常抗性加成('睡眠', -0.1)
        char.技能攻击力加成(part=part, x=0.09)
        char.技能冷却缩减(1, 100, 0.1, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 固定装备：焰纹加固靴
def entry_1196(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +16%', '冰属性强化、光属性强化、暗属性强化 +20', '', '攻击时，使敌人进入灼伤状态15秒。 (冷却时间10秒)']
    if mode == 0:
        if '灼伤' not in pa.get_state_type():
            pa.state_type.append('灼伤')
        char.异常时间['灼伤'][3] = min(char.异常时间['灼伤'][3],10)
        char.技能攻击力加成(0.16)
        char.冰属性强化加成(20)
        char.光属性强化加成(20)
        char.暗属性强化加成(20)
        pass
    if mode == 1:
        pass


# 固定装备：天翼之守护短靴
def entry_1000(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +17%', '', '在空中被攻击时，通过[拍卖行键]可恢复滞空姿势。 (冷却时间10秒)', '', '物理/魔法防御力 +20%']
    if mode == 0:
        char.add_eq_params('defense_ratio',0.2)
        char.技能攻击力加成(part=part, x=0.17)
        pass
    if mode == 1:
        pass


# 固定装备：玉化亡灵长靴
def entry_1100(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +340.9%', '技能伤害增加17%', '', '攻击速度 +24%', '施放速度 +24%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.08*3)
        char.施放速度增加(0.08*3)
        char.攻击强化加成(params[0])
        char.技能攻击力加成(part=part, x=0.17)
        pass
    if mode == 1:
        pass


# 固定装备：万念俱灰短靴
def entry_902(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +400.1%', '技能伤害 +17%', '', '装备提供的保护罩效果数值上限 +20%']
    if mode == 0:
        char.set_eq_params('protect_max',char.get_eq_params('protect_max') + 0.2)
        char.技能攻击力加成(part=part, x=0.17)
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 固定装备：骑士的救赎
def entry_1151(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +15%', '', '跳跃状态下，按[拍卖行键]可立即降落。', '', '移动速度 +20%', '跳跃力 +100']
    if mode == 0:
        char.技能攻击力加成(0.15)
        char.移动速度增加(0.2)
        pass
    if mode == 1:
        pass


# 固定装备：无人机战术手镯
def entry_937(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%', '所有属性强化 +20', '技能冷却时间 -12% (觉醒技能除外)']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        char.所有属性强化加成(20)
        char.技能冷却缩减(1, 100, 0.12, excName=char.觉醒技能)
    if mode == 1:
        pass


# 固定装备：生命之力皮护腕
def entry_1074(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '感电伤害转换 +50%', '感电伤害 +10%', '', '将所受物理/魔法伤害的50%转换为感电伤害。']
    if mode == 0:
        if '感电' not in pa.get_state_type():
            pa.state_type.append("感电")
        char.伤害类型转化('直伤', '感电', 0.5)
        char.异常增伤('感电', 0.1)
        char.技能攻击力加成(part=part, x=0.02)
        pass
    if mode == 1:
        pass


# 固定装备：和谐之音手镯
def entry_869(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +15%', '所有属性强化 +25', '', '技能、装备的生命值恢复效果 +20%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.15)
        char.所有属性强化加成(25, mode=1)
        pass
    if mode == 1:
        pass


# 固定装备：第二个黑桃 - 权威
def entry_1359(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%', '', '@[白色魔法师]@', '该装备的附魔效果 +100%', '- 不包含：技能等级增加效果，冒险家名望增加效果', '', '生命值最大值 +200', '魔法值最大值 +315']
    if mode == 0:
        char.技能攻击力加成(0.12)
        char.部位附魔[part](char, rate=1,calcLv=False,part=part)
    if mode == 1:
        pass

# 固定装备：重奏者
def entry_1033(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12.5%', '技能冷却时间恢复速度 +30% (觉醒技能除外)', '', '技能魔法值消耗量 +300%', '', '物理/魔法暴击率 +10%']
    if mode == 0:
        char.MP消耗量加成(3.0)
        char.暴击率增加(0.1)
        char.技能恢复加成(1, 100, 0.3, excName=char.觉醒技能)
        char.技能攻击力加成(0.125)
        pass
    if mode == 1:
        pass


# 固定装备：绿野的纯真手镯
def entry_921(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +15%', '', '攻击时，发动EMP冲击。 (冷却时间1.5秒)', '- 造成总攻击强化数值800%的伤害。', '', '攻击感电状态的敌人时，使敌人进入眩晕状态5秒。 (冷却时间8秒)']
    if mode == 0:
        if '感电' in pa.get_state_type() and '眩晕' not in pa.get_state_type():
            pa.state_type.append('眩晕')
        char.技能攻击力加成(0.15)
        pass
    if mode == 1:
        pass


# 固定装备：黑灵缠绕手镯
def entry_1073(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '出血伤害转换 +50%', '出血伤害 +10%', '', '将所受物理/魔法伤害的50%转换为出血伤害。']
    if mode == 0:
        if '出血' not in pa.get_state_type():
            pa.state_type.append("出血")
        char.伤害类型转化('直伤', '出血', 0.5)
        char.异常增伤('出血', 0.1)
        char.技能攻击力加成(part=part, x=0.02)
        pass
    if mode == 1:
        pass


# 固定装备：灿若繁星手镯
def entry_992(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +16%', '所有属性强化 +20', '', '使自身进入无法解除的出血/中毒/灼伤/感电状态。', '', '物理/魔法所受伤害 -20%']
    if mode == 0:
        pa.own_type = list(set(['出血', '中毒', '感电', '灼伤']) | set(pa.own_type))
        char.技能攻击力加成(part=part, x=0.16)
        char.所有属性强化加成(20)
        char.add_eq_params('hurted_ratio',0.2)
        pass
    if mode == 1:
        pass


# 固定装备：守护龙的庇护 - 慈悲
def entry_886(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +30', '35级主动技能等级 +10', '- 不包含：[饥渴]、[暗影蓄能]、[挑衅]、[幻影化身]、[忍法：残影术]、[旅人的直觉]']
    if mode == 0:
        char.所有属性强化加成(30)
        pass
    if mode == 1:
        for i in char.技能栏:
            if i.所在等级 == 35 and i.是否主动 == 1 and i.名称 not in ['饥渴','暗影蓄能','挑衅','幻影化身','忍法：残影术']:
                i.等级加成(10)
        pass


# 固定装备：流星飞电手镯
def entry_1072(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '灼伤伤害转换 +50%', '灼伤伤害 +10%', '', '将所受物理/魔法伤害的50%转换为灼伤伤害。']
    if mode == 0:
        if '灼伤' not in pa.get_state_type():
            pa.state_type.append("灼伤")
        char.伤害类型转化('直伤', '灼伤', 0.5)
        char.异常增伤('灼伤', 0.1)
        char.技能攻击力加成(part=part, x=0.02)
        pass
    if mode == 1:
        pass


# 固定装备：石巨人之核手镯
def entry_1071(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '中毒伤害转换 +50%', '中毒伤害 +10%', '', '将所受物理/魔法伤害的50%转换为中毒伤害。']
    if mode == 0:
        if '中毒' not in pa.get_state_type():
            pa.state_type.append("中毒")
        char.伤害类型转化('直伤', '中毒', 0.5)
        char.异常增伤('中毒', 0.1)
        char.技能攻击力加成(part=part, x=0.02)
        pass
    if mode == 1:
        pass


# 固定装备：迟钝的感知手镯
def entry_943(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +14%', '所有属性强化 +30', '', '使自身进入无法解除的灼伤状态。']
    if mode == 0:
        if '灼伤' not in pa.own_type:
            pa.own_type.append('灼伤')
        char.技能攻击力加成(0.14)
        char.所有属性强化加成(30)
        pass
    if mode == 1:
        pass


# 固定装备：电离掌控手镯
def entry_863(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +15%', '', '@[紧急脱离]@', '被攻击时，按跳跃键可紧急脱离。 (冷却时间10秒)', '- 按方向键可以调整方向', '- 恢复10%的生命值', '', '物理/魔法暴击率 +10%', '回避率 +10%']
    if mode == 0:
        char.回避率增加(0.1)
        char.技能攻击力加成(0.15)
        char.暴击率增加(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：收获之手
def entry_1164(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '技能冷却时间恢复速度 +25% (觉醒技能除外)']
    if mode == 0:
        char.技能恢复加成(1, 100, 0.25, excName=char.觉醒技能)
        char.技能攻击力加成(part=part, x=0.08)
        pass
    if mode == 1:
        pass


# 固定装备：残忍之心项链
def entry_929(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '攻击时，发动火属性爆炸。 (冷却时间5秒)', '- 总攻击强化数值480%的伤害', '- 对自身造成1点伤害。']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.1)
        pass
    if mode == 1:
        char.特效.append({"power": 4.8, "hit": 1})
        pass


# 固定装备：无尽的愤怒项链
def entry_912(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '', '达成200次连击时，领主/稀有怪物的剩余生命值 -1% (冷却时间30秒/辅助职业不适用)', '- 最多减少5%']
    if mode == 0:
        char.技能攻击力加成(0.09)
        pass
    if mode == 1:
        pass


# 固定装备：石巨人之心项链
def entry_927(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '攻击时，发动冰属性爆炸。 (冷却时间5秒)', '- 总攻击强化数值480%的伤害', '- 对自身造成1点伤害。']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.1)
        pass
    if mode == 1:
        char.特效.append({"power": 4.8, "hit": 1})
        pass


# 固定装备：脉冲触发器
def entry_1181(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '攻击速度 +50%']
    if mode == 0:
        char.技能攻击力加成(0.1)
        char.攻击速度增加(part=part, x=0.5)
        pass
    if mode == 1:
        pass


# 固定装备：守护龙的庇护 - 勇气
def entry_884(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +30', '40级主动技能等级 +10', '- 不包含：[念兽：龙虎啸]、[爱之急救]、[生命源泉]、[复苏之光]、[忍法：六道轮回]']
    if mode == 0:
        char.所有属性强化加成(30)
        pass
    if mode == 1:
        for i in char.技能栏:
            if i.所在等级 == 40 and i.是否主动 == 1 and i.名称 not in ['念兽：龙虎啸', '爱之急救', '生命源泉', '复苏之光', '忍法：六道轮回']:
                i.等级加成(10)
        pass


# 固定装备：浮光跃金项链
def entry_810(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +370.5%', '技能伤害 +8%', '', '使自身进入无法解除的灼伤状态。', '', '攻击时，使敌人进入灼伤状态5秒。 (冷却时间1秒)', '', '移动速度 +20%']
    if mode == 0:
        if '灼伤' not in pa.get_state_type():
            pa.state_type.append('灼伤')
        if '灼伤' not in pa.own_type:
            pa.own_type.append('灼伤')
        char.移动速度增加(0.2)
        char.攻击强化加成(params[0])
        char.技能攻击力加成(part=part, x=0.08)
        pass
    if mode == 1:
        pass


# 固定装备：五感之灵项链
def entry_1150(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '[跃翔]技能等级 +5', '', '跳跃攻击时，立即落地并生成冲击波。 (冷却时间5秒)', '- 造成总攻击强化数值3840%的伤害。', '', '进入霸体状态。']
    if mode == 0:
        char.技能攻击力加成(0.1)
        pass
    if mode == 1:
        char.特效.append({"power": 38.4, "hit": 1})
        pass


# 固定装备：高科技闪影项链
def entry_1122(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['使用指令施放技能时，根据指令的添加状态获得以下效果。', '- 添加到快捷栏：技能伤害+10%', '- 未添加到快捷栏：技能冷却时间 -15% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        for i in char.技能栏:
            if i.手搓 == True and i.名称 in char.hotkey:
                if i.是否有伤害 == 1:
                    i.倍率 *= (1 + 0.1 * char.技能伤害增加增幅)
                if i.名称 == '鬼连斩':
                    char.get_skill_by_name(
                        "鬼连斩：极").额外加成 /= (1 + 0.1 * char.技能伤害增加增幅)
            if i.名称 not in char.觉醒技能 and i.手搓 == True and i.名称 not in char.hotkey:
                if i.是否有伤害 == 1:
                    i.CDR *= (1 - 0.15)


# 固定装备：战士的荣耀项链
def entry_970(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间恢复速度 +20% (觉醒技能除外)', '装备的物体伤害 +10%', '', '攻击时，发生火属性爆炸。', '- 造成总攻击强化数值600%的伤害。']
    if mode == 0:
        char.技能恢复加成(1, 100, 0.2, excName=char.觉醒技能)
        pass
    if mode == 1:
        char.特效.append({"power": 0.15, "hit": 1})
        pass


# 固定装备：领域之心项链
def entry_841(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['@[万用黄金]@', '所持金币和金库内金币总和达到4亿时，技能伤害 +9%', '', '物理/魔法暴击率 +10%', '攻击速度 +15%', '施放速度 +15%', '移动速度 +15%']
    if mode == 0:
        char.所有速度增加(0.15)
        char.物理暴击率增加(0.1)
        char.技能攻击力加成(part=part, x=0.09)
        pass
    if mode == 1:
        pass


# 固定装备：风化的恶意
def entry_926(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '攻击时，发动暗属性爆炸。 (冷却时间5秒)', '- 总攻击强化数值480%的伤害', '- 对自身造成1点伤害。']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.1)
        pass
    if mode == 1:
        char.特效.append({"power": 4.8, "hit": 1})
        pass


# 固定装备：生命的脉动
def entry_928(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '攻击时，发动光属性爆炸。 (冷却时间5秒)', '- 总攻击强化数值480%的伤害', '- 对自身造成1点伤害。']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.10)
        pass
    if mode == 1:
        char.特效.append({"power": 4.8, "hit": 1})
        pass


# 固定装备：第一个黑桃 - 贵族
def entry_1827(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '@[白色魔法师]@', '该装备的附魔效果 +100%', '- 不包含：技能等级增加效果，冒险家名望增加效果', '', '生命值最大值 +200', '魔法值最大值 +315']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.部位附魔[part](char, rate=1,calcLv=False,part=part)
    if mode == 1:
        pass


# 固定装备：蓝色自然的种子
def entry_1225(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性强化 +20', '光属性强化 +20', '暗属性强化 +20', '', '灼伤-冰冻联接造成的灼伤伤害 +35%', '', '灼伤持续时间 +4秒', '', '攻击时，使所有敌人进入冰冻状态5秒。 (冷却时间5秒)']
    if mode == 0:
        char.火属性强化加成(20)
        char.光属性强化加成(20)
        char.暗属性强化加成(20)
        if '冰冻' not in pa.state_type:
            pa.state_type.append('冰冻')
        char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],5)
        char.异常结算加成['灼伤破冰'] += 0.35
        char.异常时间['灼伤'][1] += 4
        pass
    if mode == 1:
        pass


# 固定装备：骑士的赎罪
def entry_913(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '前冲期间，回避率 +20%', '', '攻击速度 +20%', '施放速度 +30%', '移动速度 +20%', '物理/魔法所受伤害 -10%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.1)
        char.攻击速度增加(part=part, x=0.2)
        char.移动速度增加(0.2)
        char.施放速度增加(0.3)
        char.add_eq_params('hurted_ratio',0.1)
        pass
    if mode == 1:
        pass


# 固定装备：温柔的旋律
def entry_1227(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '所有属性强化 +20', '', '所有异常状态抗性 +20%', '睡眠抗性 -30%']
    if mode == 0:
        char.所有异常抗性加成(0.2)
        char.异常抗性加成('睡眠', -0.3)
        char.所有属性强化加成(20)
        char.技能攻击力加成(part=part, x=0.1)
        pass
    if mode == 1:
        pass


# 固定装备：绽放的神秘之花
def entry_794(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '所有属性强化 +10', '', '攻击时，使敌人进入失明状态5秒。 (冷却时间8秒)']
    if mode == 0:
        if '失明' not in pa.get_state_type():
            pa.state_type.append('失明')
        char.技能攻击力加成(part=part, x=0.07)
        char.所有属性强化加成(10)
        pass
    if mode == 1:
        pass


# 固定装备：磁场探测者戒指
def entry_980(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '', '@[人力探索]@', '其他队员穿戴[磁场探测者戒指]时，技能伤害 +4%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.09)
        pass
    if mode == 1:
        pass


# 固定装备：电流星散指环
def entry_796(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '所有属性强化 +10', '', '攻击时，使敌人进入眩晕状态5秒。 (冷却时间8秒)']
    if mode == 0:
        if '眩晕' not in pa.get_state_type():
            pa.state_type.append('眩晕')
        char.技能攻击力加成(part=part, x=0.07)
        char.所有属性强化加成(10)
        pass
    if mode == 1:
        pass


# 固定装备：闪耀的音律
def entry_1173(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '', '装备的魔法值恢复效果 +30%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(part=part, x=0.06)


# 固定装备：血色结晶戒指
def entry_1204(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%', '出血伤害 +15%']
    if mode == 0:
        char.攻击强化加成(params[0])
        char.异常增伤('出血', 0.15)
        pass
    if mode == 1:
        pass


# 固定装备：闪耀的生命之戒
def entry_793(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '所有属性强化 +10', '', '攻击时，使敌人进入感电状态15秒。 (冷却时间10秒)']
    if mode == 0:
        if '感电' not in pa.get_state_type():
            pa.state_type.append('感电')
        char.异常时间['感电'][3] = min(char.异常时间['感电'][3],10)
        char.技能攻击力加成(part=part, x=0.02)
        char.所有属性强化加成(10)
        pass
    if mode == 1:
        pass


# 固定装备：骑士的骄傲
def entry_797(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '所有属性强化 +10', '', '攻击时，使敌人进入冰冻状态5秒。 (冷却时间8秒)']
    if mode == 0:
        if '冰冻' not in pa.get_state_type():
            pa.state_type.append('冰冻')
            char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],8)
        char.技能攻击力加成(part=part, x=0.07)
        char.所有属性强化加成(10)
        pass
    if mode == 1:
        pass


# 固定装备：石巨人之枢戒指
def entry_898(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '物理/魔法防御力 +12000']
    if mode == 0:
        char.add_eq_params('defense',12000)
        char.技能攻击力加成(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：血红生命之戒
def entry_795(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '所有属性强化 +10', '', '攻击时，使敌人进入灼伤状态15秒。 (冷却时间10秒)']
    if mode == 0:
        if '灼伤' not in pa.get_state_type():
            pa.state_type.append('灼伤')
        char.技能攻击力加成(0.02)
        char.所有属性强化加成(10)
        pass
    if mode == 1:
        pass


# 固定装备：隐没的邪念戒指
def entry_819(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '', '每秒恢复2%的生命值/魔法值', '', '生命值低于20%，被攻击时消耗所有魔法值，恢复成生命值。 (冷却时间60秒)']
    if mode == 0:
        char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


# 固定装备：第三个黑桃 - 死亡
def entry_1828(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '', '@[白色魔法师]@', '该装备的附魔效果 +100%', '- 不包含：技能等级增加效果，冒险家名望增加效果', '', '生命值最大值 +200', '魔法值最大值 +315']
    if mode == 0:
        char.技能攻击力加成(0.02)
        char.部位附魔[part](char, rate=1,calcLv=False,part=part)
    if mode == 1:
        pass


# 固定装备：守护龙的庇护 - 祝福
def entry_885(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +30', '45级主动技能等级 +10', '- 不包含：[圣愈之风]、[新生颂歌]、[甜蜜柔歌]']
    if mode == 0:
        char.所有属性强化加成(30)
        pass
    if mode == 1:
        for i in char.技能栏:
            if i.所在等级 == 45 and i.是否主动 == 1 and i.名称 not in ['圣愈之风', '新生颂歌', '甜蜜柔歌']:
                i.等级加成(10)
        pass


# 固定装备：永不停歇的命运
def entry_1224(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '', '@[万年雪]@', '赋予不融化于火的冰冻状态。', '- 该冰冻状态无法用灼伤状态解除', '- 攻击时，使所有敌人进入冰冻状态10秒。 (冷却时间5秒)']
    if mode == 0:
        if '冰冻' not in pa.get_state_type():
            pa.state_type.append('冰冻')
            char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],15)
        char.技能攻击力加成(part=part, x=0.07)
        pass
    if mode == 1:
        pass


# 固定装备：瞬息千里戒指
def entry_1219(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '技能冷却时间恢复速度 +10% (觉醒技能除外)', '', '使自身进入无法解除的出血状态。', '', '物理/魔法所受伤害 -10%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.05)
        char.add_eq_params('hurted_ratio',0.1)
        if '出血' not in pa.own_type:
            pa.own_type.append("出血")
        char.技能恢复加成(1, 100, 0.1, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 固定装备：雷达战网戒指
def entry_990(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间恢复速度 +30% (觉醒技能除外)', '', '@[战略性初始化]@', '施放技能时，有10%的几率使1个技能的冷却时间初始化。 (冷却时间20秒)', '- 冷却时间剩余20秒以内的技能', '- 觉醒技能除外']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.3, excName=char.觉醒技能)
        pass


# 固定装备：双音交映戒指
def entry_948(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间恢复速度 +30%', '', '@[阴阳调和]@', '攻击时，生成可获得阴阳调和的球体，效果持续15秒。 (冷却时间1秒)', '- 黑球：攻击速度 +24%，施放速度 +36%', '- 白球：赋予生命值最大值10%的保护罩', '', '移动速度+20%', '辅助职业技能伤害 +5%']
    if mode == 0:
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.1)
        char.攻击速度增加(part=part, x=0.24)
        char.施放速度增加(0.36)
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.3, excName=char.觉醒技能)
        char.移动速度增加(0.2)


# 固定装备：超小型GPS
def entry_1258(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%', '韧性条减少量 +45%', '', '物理/魔法所受伤害 -15%']
    if mode == 0:
        char.add_eq_params('hurted_ratio',0.15)
        char.技能攻击力加成(part=part, x=0.12)
        pass
    if mode == 1:
        pass


# 固定装备：完成型动力控制装置
def entry_1256(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +14%', '', '所有属性抗性 +10']
    if mode == 0:
        char.技能攻击力加成(0.14)
        char.所有属性抗性加成(10)
        pass
    if mode == 1:
        pass


# 固定装备：光学工程眼镜
def entry_1254(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%', '', '物理/魔法暴击率 +5%', '移动速度 +5%', '攻击速度 +5%', '施放速度 +7.5%']
    if mode == 0:
        char.技能攻击力加成(0.12)
        char.暴击率增加(0.05)
        char.移动速度增加(0.05)
        char.攻击速度增加(part=part, x=0.05)
        char.施放速度增加(0.075)
        pass
    if mode == 1:
        pass


# 固定装备：动力导航包
def entry_1248(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +385.3%', '技能伤害 +9%', '技能冷却时间 -15% (觉醒技能除外)', '', '获得生命值最大值65%的@[填充型保护罩]@。', '', '锁定生命值最大值的65%。', '', '物理/魔法防御力 +14000']
    if mode == 0:
        cur = char.get_eq_params('hp_max')
        char.set_eq_params('hp_max',(100 if cur == 0 else cur)*0.35)
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.65)
        char.技能冷却缩减(1, 100, 0.15, excName=char.觉醒技能)
        char.技能攻击力加成(part=part, x=0.09)
        char.add_eq_params('defense',14000)
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 固定装备：原子核项链
def entry_1250(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间恢复速度 +25% (觉醒技能除外)', '', '攻击速度 +15%', '施放速度 +15%', '移动速度 +15%']
    if mode == 0:
        char.技能恢复加成(1, 100, 0.25, excName=char.觉醒技能)
        char.所有速度增加(0.15,part)
        pass
    if mode == 1:
        pass


# 固定装备：能量搜索环
def entry_1252(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%']
    if mode == 0:
        char.技能攻击力加成(0.12)
        pass
    if mode == 1:
        pass


# 固定装备：增援号令腰带
def entry_1244(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '技能冷却时间恢复速度 +20% (觉醒技能除外)', '技能范围 +20%']
    if mode == 0:
        char.技能攻击力加成(0.06)
        char.技能恢复加成(1, 100, 0.2, excName=char.觉醒技能)
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.2)
        char.multiply_eq_params('skill_range_multi',1 + 0.2)
    if mode == 1:
        pass


# 固定装备：混乱核心胸甲
def entry_1238(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +10', '出血/中毒/灼伤/感电伤害 +15%', '', '@[D011-Risa]@', '施放技能时，召唤D011-Risa，效果持续20秒。 (最多5个)', '- 对D011-Risa适用最强敌人身上的所有异常状态', '', '所有异常状态抗性 +10%', '辅助职业技能伤害 +5%']
    if mode == 0:
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
        char.所有异常抗性加成(0.1)
        char.所有属性强化加成(10)
        char.异常增伤('中毒', 0.15)
        char.异常增伤('灼伤', 0.15)
        char.异常增伤('感电', 0.15)
        char.异常增伤('出血', 0.15)
        pass
    if mode == 1:
        pass


# 固定装备：金属齿轮护肩
def entry_1242(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '技能冷却时间恢复速度 +25% (觉醒技能除外)']
    if mode == 0:
        char.技能恢复加成(1, 100, 0.25, excName=char.觉醒技能)
        char.技能攻击力加成(0.03)
    if mode == 1:
        pass


# 固定装备：机械装甲下装
def entry_1240(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['穿戴装备的强化、增幅数值之和每6点，发动以下效果。 (最多叠加24次)', '- 技能伤害 +0.4%', '- 适用：武器、防具、首饰、特殊装备', '- 不包含：勋章、副武器', '', '该装备的强化、增幅数值每1点，所有速度 +2% (最多叠加12次)']
    if mode == 0:
        x = char.获取强化等级([part])
        char.所有速度增加(part=part, x=0.02 * min(12, x))
        if x < 12:
            return '该装备增幅/强化需再提升{}点'.format(12-x)
        pass
    if mode == 1:
        x = char.获取强化等级()
        char.技能攻击力加成(part=part, x=0.004 * min(24, int(x / 6)))
        if x < 144:
            return '全身装备增幅/强化需再提升{}点'.format(144-x)
        pass


# 固定装备：赛博音速长靴
def entry_1246(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +20%', '- 装备提供的攻击速度增加属性高于140%时，额外增加10%。', '- 包含：防具、首饰、特殊装备、装扮、徽章、守护珠、宠物、称号、辟邪玉、纹章、宠物装备、名称装饰卡', '', '技能魔法值消耗量 -50%']
    if mode == 0:
        char.MP消耗量加成(-0.5)
        pass
    if mode == 1:
        if char.攻击速度() >= 1.4:
            char.技能攻击力加成(part=part, x=0.3)
        else:
            char.技能攻击力加成(part=part, x=0.2)
        if char.攻击速度() < 1.4:
            return '攻击速度需再提升{}%'.format(round(100*(1.4-char.攻击速度()), 0))


# 固定装备：冷静的谋略家上衣
def entry_1261(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '技能冷却时间恢复速度 +30% (觉醒技能除外)']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.技能恢复加成(1, 100, 0.3, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 固定装备：指引胜利的正义
def entry_1263(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '弱点控制型异常状态的韧性条减少量 +200%']
    if mode == 0:
        char.技能攻击力加成(0.08)
        pass
    if mode == 1:
        pass


# 固定装备：欢笑中的祈盼
def entry_1265(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%', '', '@[掷骰子]@', '每30秒投掷骰子，每1点骰子点数，移动速度 +2%', '- 攻击时，骰子点数 +1', '', '物理/魔法防御力 +10000']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.11)
        char.移动速度增加(0.12)
        char.add_eq_params('defense',10000)
        pass
    if mode == 1:
        pass


# 固定装备：永眠前的准备
def entry_1267(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤伤害 +15%', '', '@[灼伤冰冻]@', '对敌人施加冰冻状态时，一次性结算灼伤与冰冻伤害。 (冷却时间3秒)', '- 累积对敌人造成的灼伤伤害一次性结算', '- 立即对冰冻状态的敌人赋予灼伤状态', '', '灼伤持续时间 +50%', '灼伤持续时间 +2秒', '', '物理/魔法所受伤害 -15%']
    if mode == 0:
        if '冰冻' in pa.state_type:
            pa.state_type.append('灼伤')
        char.异常时间['灼伤'][1] += 2
        char.add_eq_params('hurted_ratio',0.15)
        char.异常增伤('灼伤', 0.15)
        char.异常时间['灼伤'][2] += 0.5
        pass
    if mode == 1:
        pass


# 固定装备：所愿之行动
def entry_1269(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +16%', '', '出血/中毒/灼伤/感电持续时间 -20%', '', '物理/魔法所受伤害 -10%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.16)
        char.add_eq_params('hurted_ratio',0.1)
        for i in ['中毒','感电','灼伤','出血']:
            char.异常时间[i][2] -= 0.2
        pass
    if mode == 1:
        pass


# 固定装备：永恒的心愿
def entry_1271(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['@[失眠]@', '为了完成长久以来的愿望导致失眠，技能伤害 +28.5%。', '- 当装备提供的睡眠抗性数值的总和为-70%以下时，适用技能伤害增加属性。', '', '睡眠抗性 -10%']
    if mode == 0:
        char.异常抗性加成('睡眠', -0.1)
        pass
    if mode == 1:
        抗性 = char.异常抗性获取('睡眠', mode=0)
        if 抗性 <= -0.7:
            char.技能攻击力加成(part=part, x=0.285)
        else:
            return '睡眠抗性需减少{}%'.format(round(抗性*100+70, 0))
        pass


# 固定装备：正气傲然的理念
def entry_1273(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +355.7%', '', '装备发动的物体伤害 +30%', '', '攻击时，燃烧所有敌人。 (冷却时间5秒)', '- 造成总攻击强化数值140%的伤害。']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        char.特效.append({"power": 1.4, "hit": 1})
        pass


# 固定装备：炽热的渴望之证
def entry_1275(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%']
    if mode == 0:
        char.技能攻击力加成(0.12)
        pass
    if mode == 1:
        pass


# 固定装备：鲁莽而合理的作战
def entry_1277(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '', '物理/魔法所受伤害 -10%']
    if mode == 0:
        char.技能攻击力加成(0.09)
        char.add_eq_params('hurted_ratio',0.1)
        pass
    if mode == 1:
        pass


# 固定装备：胜利约定之时
def entry_1279(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +13%', '', '进入霸体状态。']
    if mode == 0:
        char.技能攻击力加成(0.13)
        pass
    if mode == 1:
        pass


# 固定装备：终结永恒时光的夙愿
def entry_1281(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +14%', '', '@[毒爆弹]@', '使用遇火爆炸的毒药，每3秒向敌人施加1次灼伤。', '- 进入灼伤状态时，中毒伤害爆发。', '- 使敌人进入灼伤状态10秒。 (冷却时间3秒)']
    if mode == 0:
        char.技能攻击力加成(0.14)
        pass
    if mode == 1:
        pass


# 固定装备：铭记长夜的黎明
def entry_1312(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '', '获得生命值最大值10%的@[填充型保护罩]@。']
    if mode == 0:
        char.技能攻击力加成(0.09)
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.1)
        pass
    if mode == 1:
        pass


# 固定装备：战胜噩梦的捷报
def entry_1318(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '进入霸体状态。']
    if mode == 0:
        char.技能攻击力加成(0.08)
        pass
    if mode == 1:
        pass


# 固定装备：庇护伤痛的威严
def entry_1316(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%']
    if mode == 0:
        char.技能攻击力加成(0.11)
        pass
    if mode == 1:
        pass


# 固定装备：愈合伤痕的誓言
def entry_1320(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%', '所有属性强化 +6', '', '攻击速度 +6%', '施放速度 +6%', '移动速度 +6%']
    if mode == 0:
        char.技能攻击力加成(0.12)
        char.所有属性强化加成(6)
        char.所有速度增加(part=part, x=0.06)
        pass
    if mode == 1:
        pass


# 固定装备：告别过去的前进
def entry_1314(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +370.5%', '技能伤害 +16%', '', '@[小巨人的步伐]@', '成为小巨人，在石化状态下仍然可以前进。', '- 石化免疫', '- 进入霸体状态', '', '攻击时，使所有敌人进入石化状态10秒。 (冷却时间30秒)']
    if mode == 0:
        char.技能攻击力加成(0.16)
        char.攻击强化加成(params[0])
        if '石化' not in pa.get_state_type():
            pa.state_type.append('石化')
        pass
    if mode == 1:
        pass


# 固定装备：爆龙王的支配 - 武力
def entry_1324(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +15%', '所有属性强化 +30', '', '每3秒恢复1%的生命值/魔法值。']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.15)
        char.所有属性强化加成(30)
        pass
    if mode == 1:
        pass


# 固定装备：爆龙王的支配 - 恐怖
def entry_1322(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '', '获得生命值最大值15%的@[填充型保护罩]@。', '@[填充型保护罩]@的恢复冷却时间 -1秒', '装备提供的保护罩效果最大值 +8%', '', '攻击速度 +20%', '施放速度 +30%', '移动速度 +20%']
    if mode == 0:
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.15)
        char.set_eq_params('protect_max',char.get_eq_params('protect_max') + 0.08)
        char.所有速度增加(0.2)
        char.施放速度增加(0.1)
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        pass


# 固定装备：爆龙王的支配 - 压制
def entry_1326(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.11)
        pass
    if mode == 1:
        pass


# 固定装备：生息之壶觞
def entry_1328(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '', '30%的物理/魔法伤害转化为持续10秒的伤害']
    if mode == 0:
        char.技能攻击力加成(0.07)
        pass
    if mode == 1:
        pass


# 固定装备：终结之龙玉
def entry_1330(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +13%', '', '物理/魔法所受伤害 -12%']
    if mode == 0:
        char.add_eq_params('hurted_ratio',0.12)
        char.技能攻击力加成(part=part, x=0.13)
        pass
    if mode == 1:
        pass


# 固定装备：含泪之宝石
def entry_1332(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +17%', '', '自身获得1种无法解除的异常状态，持续时间20秒。 (冷却时间4秒)', '- 出血/中毒/感电/灼伤中的1种异常状态']
    if mode == 0:
        char.技能攻击力加成(0.17)
        pa.own_type = list(set(['出血', '中毒', '感电', '灼伤']) | set(pa.own_type))
        pass
    if mode == 1:
        pass


# 固定装备：临界崩坏之隙
def entry_1443(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '@[次元移动]@', '输入[装备属性指令]时，开启异次元裂缝，效果持续40秒。 (最多2个；冷却时间20秒)', '- 在异次元裂缝跳跃时，移动到另一个异次元裂缝。 (冷却时间3秒)', '- 移动后，30秒内物理/魔法所受伤害 -30%', '', '物理/魔法所受伤害 -12%']
    if mode == 0:
        char.技能攻击力加成(0.08)
        char.add_eq_params('hurted_ratio',0.12)
        char.add_eq_params('hurted_ratio',0.3)
        pass
    if mode == 1:
        pass


# 固定装备：穿云破雾之光
def entry_1445(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '将50%的物理/魔法伤害转化为持续性伤害，持续时间30秒。', '', '进入霸体状态。']
    if mode == 0:
        char.技能攻击力加成(0.08)
        pass
    if mode == 1:
        pass


# 固定装备：触手可及之记忆
def entry_1447(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '', '技能冷却时间恢复速度 +10% (觉醒技能除外)', '', '进入霸体状态。', '', '移动速度 +5%']
    if mode == 0:
        char.技能攻击力加成(0.07)
        char.技能恢复加成(1, 100, 0.1, excName=char.觉醒技能)
        char.移动速度增加(0.05)
        pass
    if mode == 1:
        pass


# 固定装备：铭刻记忆之星尘
def entry_1449(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +16%']
    if mode == 0:
        char.技能攻击力加成(0.16)
        pass
    if mode == 1:
        pass


# 固定装备：超界次元
def entry_1451(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +13%', '所有属性强化 +10', '', '技能范围的属性数值总和高于23%时，所有特性技能等级 +1', '', '物理/魔法暴击率 +5%']
    if mode == 0:
        char.暴击率增加(0.05)
        char.技能攻击力加成(0.13)
        char.所有属性强化加成(10)
        pass
    if mode == 1:
        if char.get_eq_params('skill_range') >= 0.23:
            char.set_eq_params("tp",1)
            for skill in char.技能栏:
                if hasattr(skill,"TP等级")  and skill.TP等级 > 0:
                    skill.TP等级加成(1)
        else:
            return '技能范围增加不足23%'
        pass


# 固定装备：如流岁月
def entry_1453(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +19%', '', '施放技能时，获得生命值最大值15%的保护罩，效果持续2秒。 (冷却时间0.5秒)']
    if mode == 0:
        char.技能攻击力加成(0.19)
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.15)
        pass
    if mode == 1:
        pass


# 固定装备：命运的领航标
def entry_1455(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '', '攻击速度 +10%', '施放速度 +10%', '移动速度 +10%']
    if mode == 0:
        char.技能攻击力加成(0.09)
        char.所有速度增加(part=part, x=0.1)
        pass
    if mode == 1:
        pass


# 固定装备：世界的中心轴
def entry_1457(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%']
    if mode == 0:
        char.技能攻击力加成(0.11)
        pass
    if mode == 1:
        pass


# 固定装备：知海沉舟
def entry_1459(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '', '攻击速度 +35%', '施放速度 +35%', '移动速度 +35%']
    if mode == 0:
        char.所有速度增加(0.35,part)
        char.技能攻击力加成(0.07)
        pass
    if mode == 1:
        pass


# 固定装备：忘却之记载
def entry_1461(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +14%']
    if mode == 0:
        char.技能攻击力加成(0.14)
        pass
    if mode == 1:
        pass


# 固定装备：遥远之刻痕
def entry_1463(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['50、85、100级技能攻击力 + 20%', '', '攻击速度 +30%', '施放速度 +30%', '移动速度 +30%', '', '@[冥界的刻印]@', '施放技能时，有7.77%的几率增加100%的技能攻击力，使敌人通往冥界。']
    if mode == 0:
        char.所有速度增加(0.3,part)
        pass
    if mode == 1:
        char.技能倍率加成(50, 50, 0.2)
        char.技能倍率加成(85, 85, 0.2)
        char.技能倍率加成(100, 100, 0.2)
        # 暂未实现
        pass


# 固定装备：指挥官的丝绸上衣 ， 未知肌纤维上衣 ， 总司令官的制服上衣 ， 巡礼者的旧风衣
def entry_1862(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%']
    if mode == 0:
        char.技能攻击力加成(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：战略家的量身战裤 ， 未知金属绑腿 ， 总司令官的制服裤子 ， 巡礼者的工装裤
def entry_1863(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%']
    if mode == 0:
        char.技能攻击力加成(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：联盟指挥者披风 ， 未知宝石肩甲 ， 总司令官的义务 ， 巡礼者的护肩带
def entry_1864(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%', '所有属性强化 +18', '', '物理/魔法暴击率 +5%']
    if mode == 0:
        char.技能攻击力加成(0.11)
        char.所有属性强化加成(18)
        pass
    if mode == 1:
        pass


# 固定装备：誓约之黄金护腰 ， 未知机甲腰带 ， 总司令官的指挥 ， 巡礼者的木腰带
def entry_1865(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +14%', '所有属性强化 +20']
    if mode == 0:
        char.技能攻击力加成(0.14)
        char.所有属性强化加成(20)
        pass
    if mode == 1:
        pass


# 固定装备：决意之战靴 ， 未知关节鞋 ， 总司令官的决断 ， 巡礼者的沙漠靴
def entry_1867(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +17%', '攻击强化 +400.1%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.17)
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 固定装备：无限的灵感 ， 未知鳞片手镯 ， 总司令官的制敌法 ， 巡礼者的重担
def entry_1866(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +15%', '所有属性强化 +30', '', '物理/魔法暴击率 +5%', '所有速度 +10%']
    if mode == 0:
        char.技能攻击力加成(0.15)
        char.所有属性强化加成(30)
        char.所有速度增加(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：锻造核心之项链 ， 未知之瞳项链 ， 总司令官的壮烈一步 ， 巡礼者的困局
def entry_1868(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '所有属性强化 +20']
    if mode == 0:
        char.技能攻击力加成(0.09)
        char.所有属性强化加成(20)
        pass
    if mode == 1:
        pass


# 固定装备：协调之理 ， 未知之骨戒指 ， 总司令官的初心 ， 巡礼者的试炼
def entry_1869(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%', '', '物理/魔法暴击率 +5%']
    if mode == 0:
        char.技能攻击力加成(0.11)
        pass
    if mode == 1:
        pass


# 固定装备：无悔之思 ， 未知之能战矛 ， 总司令官的布阵图 ， 巡礼者的预言之视线
def entry_1870(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%']
    if mode == 0:
        char.技能攻击力加成(0.12)
        pass
    if mode == 1:
        pass


# 固定装备：无瑕之心 ， 未知之灵信号 ， 总司令官的指向罗盘 ， 巡礼者的前路之光亮
def entry_1871(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +15%']
    if mode == 0:
        char.技能攻击力加成(0.15)
        pass
    if mode == 1:
        pass


# 固定装备：铭忆之石 ， 未知之力战镰 ， 总司令官的战友遗物 ， 巡礼者的前进之意志
def entry_1872(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +15%', '', '[辅助职业专属属性]', '力量 +125', '智力 +125', '体力 +125', '体力 +125']
    if mode == 0:
        char.技能攻击力加成(0.15)
        if char.类型 == "辅助" or char.bufferCarry:
            char.基础属性加成(四维=125)
        pass
    if mode == 1:
        pass

# 固定装备：指挥官的丝绸上衣 ， 未知肌纤维上衣 ， 总司令官的制服上衣 ， 巡礼者的旧风衣
def entry_2862(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%']
    if mode == 0:
        char.技能攻击力加成(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：战略家的量身战裤 ， 未知金属绑腿 ， 总司令官的制服裤子 ， 巡礼者的工装裤
def entry_2863(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%']
    if mode == 0:
        char.技能攻击力加成(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：联盟指挥者披风 ， 未知宝石肩甲 ， 总司令官的义务 ， 巡礼者的护肩带
def entry_2864(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%', '所有属性强化 +18', '', '物理/魔法暴击率 +5%']
    if mode == 0:
        char.技能攻击力加成(0.11)
        char.所有属性强化加成(18)
        pass
    if mode == 1:
        pass


# 固定装备：誓约之黄金护腰 ， 未知机甲腰带 ， 总司令官的指挥 ， 巡礼者的木腰带
def entry_2865(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +14%', '所有属性强化 +20']
    if mode == 0:
        char.技能攻击力加成(0.14)
        char.所有属性强化加成(20)
        pass
    if mode == 1:
        pass


# 固定装备：决意之战靴 ， 未知关节鞋 ， 总司令官的决断 ， 巡礼者的沙漠靴
def entry_2867(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +17%', '攻击强化 +400.1%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.17)
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 固定装备：无限的灵感 ， 未知鳞片手镯 ， 总司令官的制敌法 ， 巡礼者的重担
def entry_2866(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +15%', '所有属性强化 +30', '', '物理/魔法暴击率 +5%', '所有速度 +10%']
    if mode == 0:
        char.技能攻击力加成(0.15)
        char.所有属性强化加成(30)
        char.所有速度增加(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：锻造核心之项链 ， 未知之瞳项链 ， 总司令官的壮烈一步 ， 巡礼者的困局
def entry_2868(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '所有属性强化 +20']
    if mode == 0:
        char.技能攻击力加成(0.09)
        char.所有属性强化加成(20)
        pass
    if mode == 1:
        pass


# 固定装备：协调之理 ， 未知之骨戒指 ， 总司令官的初心 ， 巡礼者的试炼
def entry_2869(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%', '', '物理/魔法暴击率 +5%']
    if mode == 0:
        char.技能攻击力加成(0.11)
        pass
    if mode == 1:
        pass


# 固定装备：无悔之思 ， 未知之能战矛 ， 总司令官的布阵图 ， 巡礼者的预言之视线
def entry_2870(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%']
    if mode == 0:
        char.技能攻击力加成(0.12)
        pass
    if mode == 1:
        pass


# 固定装备：无瑕之心 ， 未知之灵信号 ， 总司令官的指向罗盘 ， 巡礼者的前路之光亮
def entry_2871(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +15%']
    if mode == 0:
        char.技能攻击力加成(0.15)
        pass
    if mode == 1:
        pass


# 固定装备：铭忆之石 ， 未知之力战镰 ， 总司令官的战友遗物 ， 巡礼者的前进之意志
def entry_2872(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +15%', '', '[辅助职业专属属性]', '力量 +125', '智力 +125', '体力 +125', '体力 +125']
    if mode == 0:
        char.技能攻击力加成(0.15)
        if char.类型 == "辅助" or char.bufferCarry:
            char.基础属性加成(四维=125)
        pass
    if mode == 1:
        pass
