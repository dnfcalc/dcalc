from core.basic.property import CharacterProperty
from core.equipment.property import 成长词条计算
import core.equipment.entry_0.params as pa
def entry_12001(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +4%', '移动速度 +4%', '施放速度 +4%', '所有属性强化 +25', '物理、魔法、独立攻击力 +5%', '暴击时，额外增加5%的伤害增加量', '最终伤害 +5%', '力量、智力 +5%', '攻击时，附加5%的伤害', '攻击强化增幅 +25%', '攻击时，有3%的几率增加35点力量、智力、体力、精神，效果持续20秒(冷却时间30秒)', '施放技能时，有5%的几率增加5%的物理、魔法暴击率，效果持续20秒(冷却时间30秒)']
    if mode == 0:
        char.所有属性强化加成(25)
        char.百分比三攻加成(0.05)
        char.暴击伤害加成(0.05)
        char.最终伤害加成(0.05)
        char.百分比力智加成(0.05)
        char.附加伤害加成(0.05)
        char.百分比攻击强化加成(0.25)
        char.所有速度增加(part=part, x=0.04)
    if mode == 1:
        # char.基础属性加成(力智=35)
        char.暴击率增加(0.05)
        pass

def entry_12002(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +4%', '移动速度 +4%', '施放速度 +4%', '所有属性强化 +22', '物理、魔法、独立攻击力 +12%', '攻击时，附加10%的伤害', '攻击强化增幅 +22%', '攻击时，有3%的几率增加35点力量、智力、体力、精神，效果持续20秒(冷却时间30秒)', '施放技能时，有5%的几率增加5%的物理、魔法暴击率，效果持续20秒(冷却时间30秒)']
    if mode == 0:
        char.所有属性强化加成(22)
        char.百分比三攻加成(0.12)
        char.附加伤害加成(0.10)
        char.百分比攻击强化加成(0.22)
        char.所有速度增加(part=part, x=0.04)
    if mode == 1:
        # char.基础属性加成(力智=35)
        char.暴击率增加(0.05)
        pass

def entry_12003(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +3%', '移动速度 +3%', '施放速度 +3%', '火属性强化 +15', '攻击强化增幅 +17%', '攻击时，有3%的几率获得所有属性强化+10并增加3%的攻击、移动和施放速度，效果持续30秒(冷却时间40秒)']
    if mode == 0:
        char.火属性强化加成(15)
        char.所有速度增加(part=part, x=0.03)
        char.百分比攻击强化加成(0.17)
    if mode == 1:
        char.所有速度增加(part=part, x=0.03)
        char.所有属性强化加成(10, mode=1)
        pass

def entry_12004(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +3%', '移动速度 +3%', '施放速度 +3%', '冰属性强化 +15', '攻击强化增幅 +17%', '攻击时，有3%的几率获得所有属性强化+10并增加3%的攻击、移动和施放速度，效果持续30秒(冷却时间40秒)']
    if mode == 0:
        char.冰属性强化加成(15)
        char.所有速度增加(part=part, x=0.03)
        char.百分比攻击强化加成(0.17)
    if mode == 1:
        char.所有速度增加(part=part, x=0.03)
        char.所有属性强化加成(10, mode=1)
        pass

def entry_12005(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +3%', '移动速度 +3%', '施放速度 +3%', '光属性强化 +15', '攻击强化增幅 +17%', '攻击时，有3%的几率获得所有属性强化+10并增加3%的攻击、移动和施放速度，效果持续30秒(冷却时间40秒)']
    if mode == 0:
        char.光属性强化加成(15)
        char.所有速度增加(part=part, x=0.03)
        char.百分比攻击强化加成(0.17)
    if mode == 1:
        char.所有速度增加(part=part, x=0.03)
        char.所有属性强化加成(10, mode=1)
        pass

def entry_12006(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +3%', '移动速度 +3%', '施放速度 +3%', '暗属性强化 +15', '攻击强化增幅 +17%', '攻击时，有3%的几率获得所有属性强化+10并增加3%的攻击、移动和施放速度，效果持续30秒(冷却时间40秒)']
    if mode == 0:
        char.暗属性强化加成(15)
        char.所有速度增加(part=part, x=0.03)
        char.百分比攻击强化加成(0.17)
    if mode == 1:
        char.所有速度增加(part=part, x=0.03)
        char.所有属性强化加成(10, mode=1)
        pass

def entry_12007(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +3%', '移动速度 +3%', '施放速度 +3%', '所有属性强化 +20', '攻击时，额外增加6%的伤害增加量', '暴击时，额外增加6%的伤害增加量', '力量、智力 +6%', '攻击强化增幅 +18%', '攻击时，有3%的几率增加35点力量、智力、体力、精神，效果持续20秒(冷却时间30秒)', '施放技能时，有5%的几率增加5%的物理、魔法暴击率，效果持续20秒(冷却时间30秒)']
    if mode == 0:
        char.所有属性强化加成(20)
        char.伤害增加加成(0.06)
        char.暴击伤害加成(0.06)
        char.百分比力智加成(0.06)
        char.百分比攻击强化加成(0.18)
        char.所有速度增加(part=part, x=0.03)
    if mode == 1:
        # char.基础属性加成(力智=35)
        char.暴击率增加(0.05)

def entry_12008(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +3%', '移动速度 +3%', '施放速度 +3%', '命中率 +2%', '回避率 +2%', '所有属性强化 +20', '攻击强化增幅 +20%', 'Lv95被动技能等级 +1', '攻击时，有3%的几率增加35点力量、智力、体力、精神，效果持续20秒(冷却时间30秒)', '施放技能时，有5%的几率增加5%的物理、魔法暴击率，效果持续20秒(冷却时间30秒)']
    if mode == 0:
        char.所有属性强化加成(20)
        char.百分比攻击强化加成(0.2)
        char.所有速度增加(part=part, x=0.03)
        char.技能等级加成('被动', 95, 95, 1)
    if mode == 1:
        # char.基础属性加成(力智=35)
        char.暴击率增加(0.05)

def entry_12009(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +3%', '移动速度 +3%', '施放速度 +3%', '命中率 +2%', '回避率 +2%', '所有属性强化 +20', '攻击强化增幅 +20%', 'Lv95被动技能等级 +1', '攻击时，有3%的几率增加35点力量、智力、体力、精神，效果持续20秒(冷却时间30秒)', '施放技能时，有5%的几率增加5%的物理、魔法暴击率，效果持续20秒(冷却时间30秒)']
    if mode == 0:
        char.所有属性强化加成(20)
        char.百分比攻击强化加成(0.2)
        char.所有速度增加(part=part, x=0.03)
        char.技能等级加成('被动', 95, 95, 1)
    if mode == 1:
        # char.基础属性加成(力智=35)
        char.暴击率增加(0.05)

def entry_12010(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +4%', '移动速度 +4%', '施放速度 +4%', '命中率 +3%', '回避率 +3%', '所有属性强化 +25', '攻击强化增幅 +28%', 'Lv95被动技能等级 +1', '攻击时，有3%的几率增加35点力量、智力、体力、精神，效果持续20秒(冷却时间30秒)', '施放技能时，有5%的几率增加5%的物理、魔法暴击率，效果持续20秒(冷却时间30秒)']
    if mode == 0:
        char.所有属性强化加成(25)
        char.百分比攻击强化加成(0.28)
        char.所有速度增加(part=part, x=0.04)
        char.技能等级加成('被动', 95, 95, 1)
    if mode == 1:
        # char.基础属性加成(力智=35)
        char.暴击率增加(0.05)

def entry_12011(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +3%', '移动速度 +3%', '施放速度 +3%', '命中率 +2%', '回避率 +2%', '所有属性强化 +20', '攻击强化增幅 +22%', 'Lv95被动技能等级 +1', '攻击时，有3%的几率增加35点力量、智力、体力、精神，效果持续20秒(冷却时间30秒)', '施放技能时，有5%的几率增加5%的物理、魔法暴击率，效果持续20秒(冷却时间30秒)']
    if mode == 0:
        char.所有属性强化加成(20)
        char.百分比攻击强化加成(0.22)
        char.所有速度增加(part=part, x=0.03)
        char.技能等级加成('被动', 95, 95, 1)
    if mode == 1:
        # char.基础属性加成(力智=35)
        char.暴击率增加(0.05)

def entry_12012(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +4%', '移动速度 +4%', '施放速度 +4%', '命中率 +3%', '回避率 +3%', '所有属性强化 +30', '攻击强化增幅 +30%', 'Lv95被动技能等级 +1', '攻击时，有3%的几率增加35点力量、智力、体力、精神，效果持续20秒(冷却时间30秒)', '施放技能时，有5%的几率增加5%的物理、魔法暴击率，效果持续20秒(冷却时间30秒)']
    if mode == 0:
        char.所有属性强化加成(30)
        char.百分比攻击强化加成(0.30)
        char.所有速度增加(part=part, x=0.04)
        char.技能等级加成('被动', 95, 95, 1)
    if mode == 1:
        # char.基础属性加成(力智=35)
        char.暴击率增加(0.05)

def entry_13001(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["Lv1~35 全部 技能 Lv +1"]
    if mode == 0:
        char.技能等级加成('所有', 1, 35, 1)
    if mode == 1:
        pass

def entry_13002(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["Lv15~35 全部 技能 Lv +1", "所有属性强化 +15", "攻击、施放、移动速度 +3%"]
    if mode == 0:
        char.技能等级加成('所有', 15, 35, 1)
        char.所有属性强化加成(15)
    if mode == 1:
        pass

