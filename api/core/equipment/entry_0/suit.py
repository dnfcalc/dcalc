from core.basic.property import CharacterProperty
from core.equipment.property import 成长词条计算
import core.equipment.entry_0.params as pa

def entry_30001(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%']
    if mode == 0:
        char.技能攻击力加成(0.03)
        if char.bufferCarry or char.类型 == "辅助":
            char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.2)
            char.multiply_eq_params('skill_range_multi',1.2)
    if mode == 1:
        pass

def entry_30002(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['移动速度 +15%']
    if mode == 0:
        char.移动速度增加(0.15)
        if char.bufferCarry or char.类型 == "辅助":
            char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.1)
            char.multiply_eq_params('skill_range_multi',1.1)
    if mode == 1:
        pass

def entry_30003(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +150.0%','物理/魔法防御力 +4,000','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.攻击强化加成(150)
        char.add_eq_params('defense',7000)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30004(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间恢复速度 +5% (觉醒技能除外)','魔法值最大值 +630','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.技能恢复加成(1, 100, 0.05, excName=char.觉醒技能)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30005(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能范围 +5%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.05)
        char.multiply_eq_params('skill_range_multi',1.05)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30006(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.技能攻击力加成(0.02)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30007(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +200.0%','物理/魔法所受伤害 -10%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.攻击强化加成(200)
        char.add_eq_params('hurted_ratio',0.1)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30008(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%','所有速度 +5%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.技能攻击力加成(0.02)
        char.所有速度增加(0.05)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30009(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有速度 +5%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.所有速度增加(0.05)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30010(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.技能攻击力加成(0.02)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30011(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +150.0%','技能范围 +5%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.攻击强化加成(150)
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.05)
        char.multiply_eq_params('skill_range_multi',1.05)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30012(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['中毒抗性 +5%','技能伤害 +6%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.异常抗性加成('中毒',0.05)
        char.技能攻击力加成(0.06)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30013(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有速度 +5%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.所有速度增加(0.05)
        char.技能攻击力加成(0.02)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30014(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.技能攻击力加成(0.075)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30015(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +150.0%','技能范围 +5%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.攻击强化加成(150)
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.05)
        char.multiply_eq_params('skill_range_multi',1.05)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30016(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['感电抗性 +5%','技能伤害 +2%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.异常抗性加成('感电',0.05)
        char.技能攻击力加成(0.02)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30017(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有速度 +5%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.所有速度增加(0.05)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30018(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.技能攻击力加成(0.02)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30019(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +150.0%','队员生命值恢复量 +5%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.攻击强化加成(150)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30020(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['生命值最大值 +600','技能冷却时间 -10% (觉醒技能除外)','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.技能冷却缩减(1, 100, 0.1, excName=char.觉醒技能)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30021(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能范围 +10%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.1)
        char.multiply_eq_params('skill_range_multi',1.1)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30022(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.技能攻击力加成(0.02)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30023(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +150.0%','技能范围 +5%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.攻击强化加成(150)
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.05)
        char.multiply_eq_params('skill_range_multi',1.05)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30024(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['出血抗性 +5%','技能伤害 +2%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.异常抗性加成('出血',0.05)
        char.技能攻击力加成(0.02)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30025(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有速度 +5%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.所有速度增加(0.05)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30026(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.技能攻击力加成(0.02)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30027(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +150.0%','技能范围 +5%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.攻击强化加成(150)
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.05)
        char.multiply_eq_params('skill_range_multi',1.05)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30028(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤抗性 +5%','技能伤害 +2%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.异常抗性加成('灼伤',0.05)
        char.技能攻击力加成(0.02)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30029(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有速度 +5%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.所有速度增加(0.05)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30030(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.技能攻击力加成(0.02)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30031(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +150.0%','装备提供的保护罩最大值 +5%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.攻击强化加成(150)
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.05)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30032(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%','生命值最大值 +400','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.技能攻击力加成(0.02)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30033(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能范围 +5%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.05)
        char.multiply_eq_params('skill_range_multi',1.05)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30034(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.技能攻击力加成(0.02)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30035(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +150.0%','攻击时，恢复1750点魔法值。 (冷却时间1秒)','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.攻击强化加成(150)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30036(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%','装备的魔法值恢复量 +10%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.技能攻击力加成(0.02)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30037(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有速度 +5%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.所有速度增加(0.05)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

def entry_30038(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%','单人挑战时，技能伤害 +5%']
    if mode == 0:
        char.技能攻击力加成(0.02)
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


# 固定装备：烈火 : 缠火的理性 ， 烈火 : 缠结的意志 ， 烈火 : 汹涌的不羁 ， 烈火 : 无尽的燃烧 ， 烈火 : 最后的一步
def entry_30039(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[内面的火花]', '根据烈火装备个数(2/3/5)适用以下效果。', '- 技能范围 +10%/+15%/+25%']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.10)
        char.multiply_eq_params('skill_range_multi',1.10)
        pass
    if mode == 1:
        pass


# 固定装备：烈火 : 缠火的理性 ， 烈火 : 缠结的意志 ， 烈火 : 汹涌的不羁 ， 烈火 : 无尽的燃烧 ， 烈火 : 最后的一步
def entry_30040(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[内面的火花]', '根据烈火装备个数(2/3/5)适用以下效果。', '- 技能范围 +10%/+15%/+25%']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.15)
        char.multiply_eq_params('skill_range_multi',1.15)
        pass
    if mode == 1:
        pass

# 固定装备：烈火 : 缠火的理性 ， 烈火 : 缠结的意志 ， 烈火 : 汹涌的不羁 ， 烈火 : 无尽的燃烧 ， 烈火 : 最后的一步
def entry_30041(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[内面的火花]', '根据烈火装备个数(2/3/5)适用以下效果。', '- 技能范围 +10%/+15%/+25%']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.25)
        char.multiply_eq_params('skill_range_multi',1.25)
        pass
    if mode == 1:
        pass

# 固定装备：雪景 : 蔓延的寒气 ， 雪景 : 绵延的小雪 ， 雪景 : 严寒的感觉 ， 雪景 : 未定的命运 ， 雪景 : 未被留下的脚印
def entry_30042(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[幻视之瞳]', '根据雪景装备个数(2/3/5)适用以下效果。', '- 闪避率 +30%/45%/75%- 被击时，解除[幻视之瞳]效果。 (再次适用的冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass

# 固定装备：雪景 : 蔓延的寒气 ， 雪景 : 绵延的小雪 ， 雪景 : 严寒的感觉 ， 雪景 : 未定的命运 ， 雪景 : 未被留下的脚印
def entry_30043(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[幻视之瞳]', '根据雪景装备个数(2/3/5)适用以下效果。', '- 闪避率 +30%/45%/75%- 被击时，解除[幻视之瞳]效果。 (再次适用的冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass

# 固定装备：雪景 : 蔓延的寒气 ， 雪景 : 绵延的小雪 ， 雪景 : 严寒的感觉 ， 雪景 : 未定的命运 ， 雪景 : 未被留下的脚印
def entry_30044(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[幻视之瞳]', '根据雪景装备个数(2/3/5)适用以下效果。', '- 闪避率 +30%/45%/75%- 被击时，解除[幻视之瞳]效果。 (再次适用的冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass

# 固定装备：对流 : 席卷前的寂静 ， 对流 : 一扫而过的痕迹 ， 对流 : 千变幻流 ， 对流 : 无法制御的疾风 ， 对流 : 狂风的重量
def entry_30045(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[浓缩的对流]', '根据对流装备个数(2/3/5)适用以下效果。', '- 移动速度 +6%/9%/15%']
    if mode == 0:
        char.移动速度增加(0.06)
        pass
    if mode == 1:
        pass

# 固定装备：对流 : 席卷前的寂静 ， 对流 : 一扫而过的痕迹 ， 对流 : 千变幻流 ， 对流 : 无法制御的疾风 ， 对流 : 狂风的重量
def entry_30046(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[浓缩的对流]', '根据对流装备个数(2/3/5)适用以下效果。', '- 移动速度 +6%/9%/15%']
    if mode == 0:
        char.移动速度增加(0.09)
        pass
    if mode == 1:
        pass

# 固定装备：对流 : 席卷前的寂静 ， 对流 : 一扫而过的痕迹 ， 对流 : 千变幻流 ， 对流 : 无法制御的疾风 ， 对流 : 狂风的重量
def entry_30047(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[浓缩的对流]', '根据对流装备个数(2/3/5)适用以下效果。', '- 移动速度 +6%/9%/15%']
    if mode == 0:
        char.移动速度增加(0.15)
        pass
    if mode == 1:
        pass

# 固定装备：雷鸣 : 覆盖大地的暗云 ， 雷鸣 : 如影随形的痛苦 ， 雷鸣 : 昏昏欲睡的感觉 ， 雷鸣 : 铭刻天空的伤痕 ， 雷鸣 : 踏足乌云的脚步
def entry_30048(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[怒雷之云]', '攻击时，召唤怒雷之云攻击最多4名敌人，根据雷鸣装备个数(2/3/5)适用以下效果。', '- 怒雷之云召唤冷却时间7.5秒/5秒/3秒。', '- 造成总攻击强化1500%的伤害，敌人韧性条 -5。']
    if mode == 0:
        pass
    if mode == 1:
        pass

# 固定装备：雷鸣 : 覆盖大地的暗云 ， 雷鸣 : 如影随形的痛苦 ， 雷鸣 : 昏昏欲睡的感觉 ， 雷鸣 : 铭刻天空的伤痕 ， 雷鸣 : 踏足乌云的脚步
def entry_30049(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[怒雷之云]', '攻击时，召唤怒雷之云攻击最多4名敌人，根据雷鸣装备个数(2/3/5)适用以下效果。', '- 怒雷之云召唤冷却时间7.5秒/5秒/3秒。', '- 造成总攻击强化1500%的伤害，敌人韧性条 -5。']
    if mode == 0:
        pass
    if mode == 1:
        pass

# 固定装备：雷鸣 : 覆盖大地的暗云 ， 雷鸣 : 如影随形的痛苦 ， 雷鸣 : 昏昏欲睡的感觉 ， 雷鸣 : 铭刻天空的伤痕 ， 雷鸣 : 踏足乌云的脚步
def entry_30050(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[怒雷之云]', '攻击时，召唤怒雷之云攻击最多4名敌人，根据雷鸣装备个数(2/3/5)适用以下效果。', '- 怒雷之云召唤冷却时间7.5秒/5秒/3秒。', '- 造成总攻击强化1500%的伤害，敌人韧性条 -5。']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 固定装备：大地 : 生命回归之土 ， 大地 : 迎接死亡的时间 ， 大地 : 开花时节 ， 大地 : 生与死的交错 ， 大地 : 碎裂的脚步
def entry_30051(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[生死的境界]', '根据大地装备个数(2/3/5)适用以下效果。', '- 所有速度 +6%/9%/15%']
    if mode == 0:
        char.所有速度增加(0.06)
        pass
    if mode == 1:
        pass

# 固定装备：大地 : 生命回归之土 ， 大地 : 迎接死亡的时间 ， 大地 : 开花时节 ， 大地 : 生与死的交错 ， 大地 : 碎裂的脚步
def entry_30052(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[生死的境界]', '根据大地装备个数(2/3/5)适用以下效果。', '- 所有速度 +6%/9%/15%']
    if mode == 0:
        char.所有速度增加(0.09)
        pass
    if mode == 1:
        pass

# 固定装备：大地 : 生命回归之土 ， 大地 : 迎接死亡的时间 ， 大地 : 开花时节 ， 大地 : 生与死的交错 ， 大地 : 碎裂的脚步
def entry_30053(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['[生死的境界]', '根据大地装备个数(2/3/5)适用以下效果。', '- 所有速度 +6%/9%/15%']
    if mode == 0:
        char.所有速度增加(0.15)
        pass
    if mode == 1:
        pass

def entry_30054(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%','技能冷却时间 -15% (觉醒技能除外)','','物理/魔法暴击率 +10%','所有速度 +10%','物理/魔法所有伤害 -10%','','[辅助职业专属属性]','1~25级技能等级 +2','技能范围 +15%']
    if mode == 0:
        damage = [0.02,0.06,0.08,0.1,0.12,0.13,0.15]
        char.技能攻击力加成(damage[char.兼容数量统计(15)])
        char.技能冷却缩减(1,100,0.15, excName=char.觉醒技能)
        char.所有速度增加(0.3)
        char.add_eq_params('hurted_ratio',0.3)
        if char.类型 == "辅助" or char.bufferCarry:
            char.技能等级加成('所有',1,25,2)
            char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.15)
            char.multiply_eq_params('skill_range_multi',1.15)
            char.所有速度增加(0.2)
        pass
    if mode == 1:
        pass

def entry_30055(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间恢复速度 +30% (觉醒技能除外)','','[辅助职业专属属性]','力量 +50','智力 +50','体力 +50','精神 +50','','技能范围 +15%']
    if mode == 0:
        damage = [0,0.027,0.047,0.075,0.104,0.133]
        char.技能攻击力加成(damage[char.兼容数量统计(16)])
        char.技能恢复加成(1,100,0.3,excName=char.觉醒技能)
        if char.类型 == "辅助" or char.bufferCarry:
            char.基础属性加成(四维=50)
            char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.15)
            char.multiply_eq_params('skill_range_multi',1.15)
        pass
    if mode == 1:
        pass

def entry_30056(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +22.8%','技能冷却时间 -15% (觉醒技能除外)','','所有速度 +30%','物理/魔法所有伤害 -10%','','穿戴全套“痕”系列装备时，适用以下效果。','- 技能伤害 +1.5%','- 移动速度 +10%','','[辅助职业专属属性]','1~25级技能等级 +2','技能范围 +15%']
    if mode == 0:
        char.技能攻击力加成(0.228)
        char.技能冷却缩减(1,100,0.15, excName=char.觉醒技能)
        char.所有速度增加(0.3)
        char.add_eq_params('hurted_ratio',0.2)
        if len(list(set(char.suits) & set([30057,30059,30061]))) > 0:
            char.技能攻击力加成(0.015)
            char.移动速度增加(0.15)
        if char.类型 == "辅助" or char.bufferCarry:
            char.技能等级加成('所有',1,25,2)
            char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.15)
            char.multiply_eq_params('skill_range_multi',1.15)
        pass
    if mode == 1:
        pass

def entry_30057(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +19.3%','技能冷却时间恢复速度 +30% (觉醒技能除外)','','穿戴全套“录”系列装备时，适用以下效果。','- 技能伤害 +1.5%','- 技能范围 +10%','','[辅助职业专属属性]','力量 +50','智力 +50','体力 +50','精神 +50','','技能范围 +15%']
    if mode == 0:
        char.技能攻击力加成(0.193)
        char.技能恢复加成(1,100,0.3,excName=char.觉醒技能)
        if len(list(set(char.suits) & set([30056,30058,30060]))) > 0:
            char.技能攻击力加成(0.015)
            char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.1)
            char.multiply_eq_params('skill_range_multi',1.1)
        if char.类型 == "辅助" or char.bufferCarry:
            char.基础属性加成(四维=50)
            char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.15)
            char.multiply_eq_params('skill_range_multi',1.15)
        pass
    if mode == 1:
        pass

def entry_30058(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +13%','技能冷却时间 -35% (觉醒技能除外)','','[沙场老将的战术]','沙场老将决胜千里之外，增加所有队员的士气。','- 队员攻击速度 +10%。','- 队员物理/魔法所有伤害 -5%','','所有速度 +10%','物理/魔法所受伤害 -10%','','穿戴全套“痕”系列装备时，适用以下效果。','- 技能伤害 +1.5%','- 移动速度 +10%','','[辅助职业专属属性]','技能伤害 +5%','1~25级技能等级 +2','技能范围 +20%']
    if mode == 0:
        char.技能攻击力加成(0.13)
        char.技能冷却缩减(1,100,0.35, excName=char.觉醒技能)
        char.攻击速度增加(0.1)
        char.所有速度增加(0.10)
        char.add_eq_params('hurted_ratio',0.3)
        if len(list(set(char.suits) & set([30057,30059,30061]))) > 0:
            char.技能攻击力加成(0.015)
            char.移动速度增加(0.15)
        if char.类型 == "辅助" or char.bufferCarry:
            char.技能攻击力加成(0.05)
            char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.2)
            char.multiply_eq_params('skill_range_multi',1.2)
            char.所有速度增加(0.3)
            char.技能等级加成('所有',1,25,2)
        pass
    if mode == 1:
        pass

def entry_30059(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11.3%','技能冷却时间恢复速度 +60% (觉醒技能除外)','','[沙场老将的谋略]','沙场老将运筹帷幄之中，增加所有队员的士气。','- 队员移动速度 +10%。','- 每1秒队员生命值/魔法值恢复0.2%','','穿戴全套“录”系列装备时，适用以下效果。','- 技能伤害 +1.5%','- 技能范围 +10%','','[辅助职业专属属性]','技能伤害 +3%','力量 +50','智力 +50','体力 +50','精神 +50','技能范围 +20%','','获得相当于生命值最大值30%的[填充型保护罩]']
    if mode == 0:
        char.技能攻击力加成(0.113)
        char.技能恢复加成(1,100,0.6,excName=char.觉醒技能)
        char.移动速度增加(0.1)
        if len(list(set(char.suits) & set([30056,30058,30060]))) > 0:
            char.技能攻击力加成(0.015)
            char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.1)
            char.multiply_eq_params('skill_range_multi',1.1)
        if char.类型 == "辅助" or char.bufferCarry:
            char.技能攻击力加成(0.03)
            char.基础属性加成(四维=50)
            char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.2)
            char.multiply_eq_params('skill_range_multi',1.2)
            char.set_eq_params('protect',char.get_eq_params('protect') + 0.3)
        pass
    if mode == 1:
        pass

def entry_30060(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +22.7%','技能冷却时间 -10% (觉醒技能除外)',')','所有速度 +10%','生命值最大值 +30%','物理/魔法所受伤害 -20%','回避率 +30%','','穿戴全套“痕”系列装备时，适用以下效果。','- 技能伤害 +1.5%','- 移动速度 +10%','','[辅助职业专属属性]','技能伤害 +2%','1~25技能等级 +2']
    if mode == 0:
        char.技能攻击力加成(0.227)
        char.技能冷却缩减(1,100,0.1, excName=char.觉醒技能)
        char.所有速度增加(0.1)
        if len(list(set(char.suits) & set([30057,30059,30061]))) > 0:
            char.技能攻击力加成(0.015)
            char.移动速度增加(0.15)
        if char.类型 == "辅助" or char.bufferCarry:
            char.技能等级加成('所有',1,25,2)
            char.技能攻击力加成(0.02)
        pass
    if mode == 1:
        pass

def entry_30061(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +18.6%','技能冷却时间恢复速度 +20% (觉醒技能除外)','','攻击时，恢复3%的生命值。(冷却时间1秒)','生命值最大值 +20%','','穿戴全套“录”系列装备时，适用以下效果。','- 技能伤害 +1.5%','- 技能范围 +10%','','[辅助职业专属属性]','技能伤害 +1%','力量 +50','智力 +50','体力 +50','精神 +50']
    if mode == 0:
        char.技能攻击力加成(0.186)
        char.技能恢复加成(1,100,0.2,excName=char.觉醒技能)
        if len(list(set(char.suits) & set([30056,30058,30060]))) > 0:
            char.技能攻击力加成(0.015)
            char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.1)
            char.multiply_eq_params('skill_range_multi',1.1)
        if char.类型 == "辅助" or char.bufferCarry:
            char.基础属性加成(四维 = 50)
            char.技能攻击力加成(0.1)
        pass
    if mode == 1:
        pass
