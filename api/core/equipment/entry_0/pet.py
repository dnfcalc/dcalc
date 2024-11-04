from core.basic.property import CharacterProperty
from core.equipment.property import 成长词条计算
import core.equipment.entry_0.params as pa
def entry_10101(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        # (宠物)
        return ["增益量 +3%", "所有职业Lv1~50 全部技能+1", "Lv30 Buff技能力量、智力增加量 +3%", "Lv30 Buff技能物理、魔法、独立攻击力 +3%"]
    if mode == 0:
        char.技能等级加成('所有', 1, 50, 1)
        char.辅助属性加成(buff百分比力智=0.03, buff百分比三攻=0.03, 百分比buff量=0.03)

def entry_10102(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        # (宠物)
        return ["所有属性强化 +15", "攻击、施放、移动速度 +4%", "MP最大值 +5%", "攻击强化增幅 +12%", "增益量 +2%", "所有职业Lv1~50 全部技能+1", ]
    if mode == 0:
        char.技能等级加成('所有', 1, 50, 1)
        char.辅助属性加成(百分比buff量=0.02)
        char.所有速度增加(part=part, x=0.04)
        char.所有属性强化加成(15)
        char.百分比攻击强化加成(0.12)

def entry_10103(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        # (宠物)
        return ["所有属性强化 +25", "攻击、施放、移动速度 +5%", "MP最大值 +5%", "攻击强化增幅 +15%", "增益量 +5%", "所有职业Lv1~75 全部技能+1", ]
    if mode == 0:
        char.技能等级加成('所有', 1, 75, 1)
        char.辅助属性加成(百分比buff量=0.05)
        char.所有速度增加(part=part, x=0.05)
        char.所有属性强化加成(25)
        char.百分比攻击强化加成(0.15)

def entry_11001(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +5%', '移动速度 +5%', '施放速度 +5%', '所有属性强化 +25', '所有职业Lv1~95 全部技能+1', '物理、魔法、独立攻击力 +20%', '攻击时,附加15%伤害', '所有技能冷却时间 -5%(加算)', '攻击强化增幅 +35%']
    if mode == 0:
        char.所有属性强化加成(25)
        char.附加伤害加成(0.15)
        char.百分比三攻加成(0.2)
        char.百分比攻击强化加成(0.35)
        char.加算冷却缩减(0.05)
        char.技能等级加成('所有', 1, 95, 1)
        char.所有速度增加(part=part, x=0.05)
    if mode == 1:
        pass

def entry_11002(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +5%', '移动速度 +5%', '施放速度 +5%', '所有属性强化 +25', '所有职业Lv1~95 全部技能+1', '物理、魔法、独立攻击力 +15%', '攻击时,附加20%伤害', '所有技能冷却时间 -5%(加算)', '攻击强化增幅 +35%']
    if mode == 0:
        char.所有属性强化加成(25)
        char.附加伤害加成(0.20)
        char.百分比三攻加成(0.15)
        char.百分比攻击强化加成(0.35)
        char.加算冷却缩减(0.05)
        char.技能等级加成('所有', 1, 95, 1)
        char.所有速度增加(part=part, x=0.05)
    if mode == 1:
        pass

def entry_11003(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +5%', '移动速度 +5%', '施放速度 +5%', '所有属性强化 +25', '所有职业Lv1~95 全部技能+1', '物理、魔法、独立攻击力 +12%', '攻击时,附加10%伤害', '所有技能冷却时间 -5%(加算)', '攻击强化增幅 +22%']
    if mode == 0:
        char.所有属性强化加成(25)
        char.附加伤害加成(0.10)
        char.百分比三攻加成(0.12)
        char.百分比攻击强化加成(0.22)
        char.加算冷却缩减(0.05)
        char.技能等级加成('所有', 1, 95, 1)
        char.所有速度增加(part=part, x=0.05)
    if mode == 1:
        pass

def entry_11004(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +5%', '移动速度 +5%', '施放速度 +5%', '所有属性强化 +25', '所有职业Lv1~95 全部技能+1', '物理、魔法、独立攻击力 +10%', '攻击时,附加12%伤害', '所有技能冷却时间 -5%(加算)', '攻击强化增幅 +22%']
    if mode == 0:
        char.所有属性强化加成(25)
        char.附加伤害加成(0.12)
        char.百分比三攻加成(0.10)
        char.百分比攻击强化加成(0.22)
        char.加算冷却缩减(0.05)
        char.技能等级加成('所有', 1, 95, 1)
        char.所有速度增加(part=part, x=0.05)
    if mode == 1:
        pass

def entry_11005(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +5%', '移动速度 +5%', '施放速度 +5%', '所有属性强化 +25', '所有职业Lv1~80 全部技能+1', '暴击时,额外增加20%的伤害增加量', '力量、智力 +12%', '所有技能冷却时间 -5%(加算)', '攻击强化增幅 +32%']
    if mode == 0:
        char.所有属性强化加成(25)
        char.暴击伤害加成(0.20)
        char.百分比力智加成(0.12)
        char.百分比攻击强化加成(0.32)
        char.加算冷却缩减(0.05)
        char.技能等级加成('所有', 1, 80, 1)
        char.所有速度增加(part=part, x=0.05)
    if mode == 1:
        pass

def entry_11006(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +5%', '移动速度 +5%', '施放速度 +5%', '所有属性强化 +25', '所有职业Lv1~80 全部技能+1', '物理、魔法、独立攻击力 +12%', '攻击时,附加10%伤害', '所有技能冷却时间 -5%(加算)', '攻击强化增幅 +22%']
    if mode == 0:
        char.所有属性强化加成(25)
        char.百分比三攻加成(0.12)
        char.附加伤害加成(0.10)
        char.百分比攻击强化加成(0.22)
        char.加算冷却缩减(0.05)
        char.技能等级加成('所有', 1, 80, 1)
        char.所有速度增加(part=part, x=0.05)
    if mode == 1:
        pass

def entry_11007(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +5%', '移动速度 +5%', '施放速度 +5%', '所有属性强化 +25', '所有职业Lv1~95 全部技能+1', '所有技能冷却时间 -5%(加算)', '攻击强化增幅 +25%']
    if mode == 0:
        char.所有属性强化加成(25)
        char.百分比攻击强化加成(0.25)
        char.加算冷却缩减(0.05)
        char.技能等级加成('所有', 1, 95, 1)
        char.所有速度增加(part=part, x=0.05)
    if mode == 1:
        pass

def entry_11009(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +5%', '移动速度 +5%', '施放速度 +5%', '所有属性强化 +25', '所有职业Lv1~95 全部技能+1', '所有技能冷却时间 -5%(加算)', '攻击强化增幅 +40%']
    if mode == 0:
        char.所有属性强化加成(25)
        char.百分比攻击强化加成(0.40)
        char.加算冷却缩减(0.05)
        char.技能等级加成('所有', 1, 95, 1)
        char.所有速度增加(part=part, x=0.05)
    if mode == 1:
        pass

def entry_11010(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +5%', '移动速度 +5%', '施放速度 +5%', '所有属性强化 +25', '所有职业Lv1~95 全部技能+1', '所有技能冷却时间 -5%(加算)', '攻击强化增幅 +30%']
    if mode == 0:
        char.所有属性强化加成(25)
        char.百分比攻击强化加成(0.30)
        char.加算冷却缩减(0.05)
        char.技能等级加成('所有', 1, 95, 1)
        char.所有速度增加(part=part, x=0.05)
    if mode == 1:
        pass

def entry_11011(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +5%', '移动速度 +5%', '施放速度 +5%', '所有属性强化 +25', '所有职业Lv1~95 全部技能+1', '所有技能冷却时间 -5%(加算)', '攻击强化增幅 +45%']
    if mode == 0:
        char.所有属性强化加成(25)
        char.百分比攻击强化加成(0.45)
        char.加算冷却缩减(0.05)
        char.技能等级加成('所有', 1, 95, 1)
        char.所有速度增加(part=part, x=0.05)
    if mode == 1:
        pass

