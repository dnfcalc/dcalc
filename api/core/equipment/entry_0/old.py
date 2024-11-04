from core.basic.property import CharacterProperty
from core.equipment.property import 成长词条计算
import core.equipment.entry_0.params as pa
def entry_14001(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +26', '技能攻击力 +29%', '攻击时,附加10%的伤害', '力量、智力 +10%', '物理、魔法、独立攻击力 +11%']
    if mode == 0:
        char.所有属性强化加成(26)
        char.技能攻击力加成(part=part, x=0.29)
        char.附加伤害加成(0.10)
        char.百分比力智加成(0.1)
        char.百分比三攻加成(0.11)
    if mode == 1:
        pass

def entry_14002(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能攻击力 +29%', '所有职业Lv1~45所有技能Lv +1', '技能MP消耗量 -20%', '攻击时，额外增加11%的伤害增加量', '所有职业Lv1~45所有技能Lv +1', "力量、智力 +12%"]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.29)
        char.技能等级加成('所有', 1, 45, 1)
        char.伤害增加加成(0.11)
        char.百分比力智加成(0.12)
    if mode == 1:
        char.技能等级加成('所有', 1, 45, 1)
        char.MP消耗量加成(-0.2)
        pass

def entry_14003(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能攻击力 +31%', '物理、魔法、独立攻击力 +3%', '最终伤害 +10%', '攻击时，额外增加8%的伤害增加量', '所有属性强化 +24', '所有职业Lv1~45所有技能冷却时间 -10%', ]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.31)
        char.百分比三攻加成(0.03)
        char.最终伤害加成(0.1)
        char.伤害增加加成(0.08)
        char.所有属性强化加成(24)
    if mode == 1:
        char.技能冷却缩减(1, 45, 0.1)
        pass

def entry_14004(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暗属性抗性 +10', '技能攻击力 +19%', '每5点暗属性抗性，增加1%的最终伤害(最多增加5%)', '所有职业Lv5~100所有技能Lv +1', '物理、魔法、独立攻击力 +7%', '物理、魔法、独立攻击力 +80']
    if mode == 0:
        char.暗属性抗性加成(10)
        char.技能攻击力加成(part=part, x=0.19)
        char.百分比三攻加成(0.07)
        char.基础属性加成(三攻=80)
        char.最终伤害加成(0.05)
        char.技能等级加成('所有', 5, 100, 1)
    if mode == 1:
        pass

def entry_14005(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +18', '技能攻击力 +30%', '物理、魔法、独立攻击力 +4%', '力量、智力 +10%', '暴击时，额外增加8%的伤害增加量', '物理、魔法、独立攻击力 +170']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.30)
        char.所有属性强化加成(18)
        char.百分比力智加成(0.1)
        char.暴击伤害加成(0.08)
        char.基础属性加成(三攻=170)
    if mode == 1:
        char.百分比三攻加成(0.04)
        pass

def entry_14006(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +28', '技能攻击力 +29%', '暴击时，额外增加7%的伤害增加量', '攻击时，额外增加5%的伤害增加量', '攻击时，附加6%的伤害', "最终伤害 +5%"]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.29)
        char.所有属性强化加成(28)
        char.附加伤害加成(0.06)
        char.暴击伤害加成(0.07)
        char.伤害增加加成(0.05)
        char.最终伤害加成(0.05)
    if mode == 1:
        pass

def entry_14007(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +26', '技能攻击力 +30%', '攻击时，额外增加4%的伤害增加量', '物理、魔法、独立攻击力 +3%''暴击时，额外增加10%的伤害增加量', "力量、智力 +8%"]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.30)
        char.所有属性强化加成(26)
        char.暴击伤害加成(0.10)
        char.百分比三攻加成(0.03)
        char.伤害增加加成(0.04)
        char.百分比力智加成(0.08)
    if mode == 1:
        pass

def entry_14008(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能攻击力 +27%', '物理、魔法、独立攻击力 +7%''所有属性强化 +40', '攻击时，额外增加10%的伤害增加量', "攻击时，附加10%的伤害"]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.27)
        char.所有属性强化加成(40)
        char.百分比三攻加成(0.07)
        char.伤害增加加成(0.10)
        char.附加伤害加成(0.10)
    if mode == 1:
        pass

def entry_14009(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +29', '技能攻击力 +30%', '技能快捷栏中每存在一个空栏，攻击时额外增加1%的伤害增加量(最多增加6%)', '物理、魔法、独立攻击力 +8%', '力量、智力 +8%', '暴击时，额外增加15%的伤害增加量']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.30)
        char.所有属性强化加成(29)
        char.伤害增加加成(
            min(0.06, len(list(filter(lambda i: i == "", char.hotkey)))*0.01))
        char.百分比三攻加成(0.08)
        char.百分比力智加成(0.08)
        char.暴击伤害加成(0.15)
    if mode == 1:
        pass

def entry_14010(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +22', '技能攻击力 +34%', "攻击速度 +15%", "最终伤害 +10%", '暴击时，额外增加8%的伤害增加量', '攻击时，额外增加4%的伤害增加量', '力量、智力 +3%', ]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.34)
        char.所有属性强化加成(22)
        char.伤害增加加成(0.04)
        char.暴击伤害加成(0.08)
        char.百分比力智加成(0.03)
    if mode == 1:
        char.攻击速度增加(part=part, x=0.15)
        pass

def entry_14011(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +23', '所有职业Lv45 全部技能 Lv +2''技能攻击力 +25%', "技能攻击力 +4%", "最终伤害 +4%", '攻击时，额外增加9%的伤害增加量', '暴击时，额外增加7%的伤害增加量', ]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.25)
        char.技能攻击力加成(part=part, x=0.04)
        char.所有属性强化加成(23)
        char.最终伤害加成(0.04)
        char.伤害增加加成(0.09)
        char.暴击伤害加成(0.07)
        if char.职业 == '缔造者':
            char.技能等级加成('所有', 50, 50, 2)
        else:
            char.技能等级加成('所有', 45, 45, 2)
    if mode == 1:
        pass

def entry_14012(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +6%', '移动速度 +6%', '施放速度 +9%', "技能攻击力 +35%", "所有职业Lv1~48所有技能Lv+1", '物理、魔法、独立攻击力 +70', '最终伤害 +5%', "力量、智力 +160"]
    if mode == 0:
        char.攻击速度增加(part=part, x=0.06)
        char.移动速度增加(0.06)
        char.施放速度增加(0.09)
        char.技能攻击力加成(part=part, x=0.35)
        char.技能等级加成('所有', 1, 48, 1)
        char.基础属性加成(三攻=70)
        char.最终伤害加成(0.05)
        char.基础属性加成(力智=100)
    if mode == 1:
        pass

def entry_14013(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +20', "技能攻击力 +34%", "攻击时发生持续伤害3秒,伤害量为对敌人造成伤害的5%", '暴击时，额外增加7%的伤害增加量', '攻击时，附加4%的伤害', "攻击时，额外增加9%的伤害增加量"]
    if mode == 0:
        char.所有属性强化加成(20)
        char.技能攻击力加成(part=part, x=0.34)
        char.持续伤害加成(0.05)
        char.暴击伤害加成(0.07)
        char.附加伤害加成(0.04)
        char.伤害增加加成(0.09)
    if mode == 1:
        pass

def entry_14014(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +22', "技能攻击力 +24%", "所有职业Lv1~80所有技能冷却时间 -13%（Lv50技能除外）", '攻击时，附加9%的伤害', "力量、智力 +4%", "最终伤害 +4%", "物理、魔法、独立攻击力 +7%"]
    if mode == 0:
        char.所有属性强化加成(22)
        char.技能攻击力加成(part=part, x=0.24)
        char.技能冷却缩减(1, 80, 0.13, [50])
        char.附加伤害加成(0.09)
        char.百分比力智加成(0.04)
        char.最终伤害加成(0.04)
        char.百分比三攻加成(0.07)
    if mode == 1:
        pass

def entry_14015(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +29', '技能攻击力 +30%', '暴击时，额外增加10%的伤害增加', "物理、魔法独立攻击力 +10%", '攻击时，附加10%的伤害', ]
    if mode == 0:
        char.所有属性强化加成(29)
        char.技能攻击力加成(part=part, x=0.30)
        char.技能冷却缩减(1, 80, 0.13, [50])
        char.附加伤害加成(0.10)
        char.暴击伤害加成(0.10)
        char.百分比三攻加成(0.10)
    if mode == 1:
        pass

def entry_14016(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +31', '技能攻击力 +23%', '攻击时附加5%的伤害', '最终伤害 +4% ', "物理、魔法、独立攻击力 +13%", '力量、智力 +4%', '技能攻击力 +5% ']
    if mode == 0:
        char.所有属性强化加成(31)
        char.技能攻击力加成(part=part, x=0.23)
        char.附加伤害加成(0.5)
        char.最终伤害加成(0.04)
        char.百分比三攻加成(0.13)
        char.百分比力智加成(0.04)
        char.技能攻击力加成(part=part, x=0.05)
    if mode == 1:
        pass

def entry_14017(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +14', '技能攻击力 +25%', '所有职业Lv45技能攻击力-30%', "所有职业Lv45技能冷却时间恢复速度 +100%", '所有职业Lv1~45所有技能Lv +1', "攻击时，附加5%的伤害", '力量、智力+8%', '最终伤害+6%']
    if mode == 0:
        char.所有属性强化加成(14)
        char.技能攻击力加成(part=part, x=0.25)
        if char.职业 == '缔造者':
            char.技能倍率加成(50, 50, -0.3)
            char.技能恢复加成(50, 50, 1)
        else:
            char.技能倍率加成(45, 45, -0.3)
            char.技能恢复加成(45, 45, 1)
        char.技能等级加成('所有', 1, 45, 1)
        char.附加伤害加成(0.05)
        char.百分比力智加成(0.08)
        char.最终伤害加成(0.06)
    if mode == 1:
        pass

def entry_14018(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +23', '技能攻击力 +33%', '攻击时，额外增加5%的伤害增加量', '暴击时，额外增加7%的伤害增加量', "最终伤害 +6%", '攻击时，附加5%的伤害'
                ]
    if mode == 0:
        char.所有属性强化加成(23)
        char.技能攻击力加成(part=part, x=0.33)
        char.伤害增加加成(0.05)
        char.暴击伤害加成(0.07)
        char.最终伤害加成(0.06)
        char.附加伤害加成(0.05)
    if mode == 1:
        char.所有属性强化加成(24, mode=1)
        pass

def entry_14019(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +6', '技能攻击力 +30%', '所有属性强化 +24''力量、智力 +12%', '攻击时，额外增加9%的伤害增加量', "最终伤害 +9%"]
    if mode == 0:
        char.所有属性强化加成(6)
        char.技能攻击力加成(part=part, x=0.3)
        char.百分比力智加成(0.24)
        char.伤害增加加成(0.09)
        char.最终伤害加成(0.09)
    if mode == 1:
        char.所有属性强化加成(24, mode=1)
        pass

def entry_14020(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +25', '技能攻击力 +25%', '物理、魔法、独立攻击力 +3%''技能攻击力 +6%', '暴击时，额外增加9%的伤害增加', "力量、智力 +6%"]
    if mode == 0:
        char.所有属性强化加成(25)
        char.技能攻击力加成(part=part, x=0.25)
        char.百分比力智加成(0.6)
        char.暴击伤害加成(0.09)
        char.百分比力智加成(0.06)
    if mode == 1:
        pass

def entry_14021(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化+16', '技能攻击力+16%', '强化、增幅数值每增加1,额外增加1%的技能攻击力最多适用至+13) ''Lv15~30所有技能冷却时间恢复速度+30%', '所有职业Lv1~48所有技能Lv +1', "物理、魔法、独立攻击力+110", "暴击时，额外增加10%的伤害增加量", "攻击时，额外增加11%的伤害增加量"]
    if mode == 0:
        char.所有属性强化加成(16)
        char.技能攻击力加成(part=part, x=0.16)
        char.技能攻击力加成(part=part, x=min(char.获取强化等级([part]), 13)*0.01)
        char.技能恢复加成(15, 30, 0.3)
        char.基础属性加成(三攻=110)
        char.暴击伤害加成(0.1)
        char.伤害增加加成(0.11)
        pass
    if mode == 1:
        pass

def entry_14022(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["所有属性强化+32", "攻击时，附加7%的伤害", "技能攻击力+30%", "暴击时，额外增加4%的伤害增加量", "力量、智力+10%", "攻击时，额外增加3%的伤害增加量", "物理、魔法独立攻击力 +8%"]
    if mode == 0:
        char.所有属性强化加成(32)
        char.附加伤害加成(0.07)
        char.技能攻击力加成(part=part, x=0.3)
        char.暴击伤害加成(0.04)
        char.百分比力智加成(0.1)
        char.伤害增加加成(0.03)
        char.百分比三攻加成(0.08)
        pass
    if mode == 1:
        pass

def entry_14023(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化+35', '攻击时，附加8%的伤害', '技能攻击力+27%', '力量、智力+160', '最终伤害+12%', '物理、魔法、独立攻击力+12%']
    if mode == 0:
        char.所有属性强化加成(35)
        char.附加伤害加成(0.08)
        char.技能攻击力加成(part=part, x=0.27)
        char.基础属性加成(力智=160)
        char.最终伤害加成(0.12)
        char.百分比三攻加成(0.12)
        pass
    if mode == 1:
        pass

def entry_14024(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化+5', '技能攻击力 +30%', '所有属性强化+36(81暗抗)', '力量、智力+240', '攻击时，附加7%的伤害', '物理、魔法、独立攻击力+12%']
    if mode == 0:
        char.所有属性强化加成(5)
        char.所有属性强化加成(36)
        char.技能攻击力加成(part=part, x=0.3)
        char.基础属性加成(力智=240)
        char.附加伤害加成(0.07)
        char.百分比三攻加成(0.12)
        pass
    if mode == 1:
        pass

def entry_14025(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化+5', '力量、智力+8%', '技能攻击力+30%', '技能冷却时间-15%（觉醒技能除外）', '力量、智力+4%', '所有属性强化+20', '物理、魔法、独立攻击力+100', '最终伤害+8%']
    if mode == 0:
        char.所有属性强化加成(5)
        char.百分比力智加成(0.08)
        char.技能攻击力加成(part=part, x=0.3)
        char.技能冷却缩减(1, 100, 0.15, excName=char.觉醒技能)
        char.百分比力智加成(0.04)
        char.所有属性强化加成(20)
        char.基础属性加成(三攻=100)
        char.最终伤害加成(0.08)
        pass
    if mode == 1:
        pass

def entry_14026(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化+31', '最终伤害+5%', '技能攻击力+25%', '技能攻击力+3%', '攻击时，附加4%的伤害', '力量、智力+7%', '物理、魔法、独立攻击力+12%']
    if mode == 0:
        char.所有属性强化加成(31)
        char.技能攻击力加成(part=part, x=0.03)
        char.附加伤害加成(0.04)
        char.百分比力智加成(0.07)
        char.百分比三攻加成(0.12)
        pass
    if mode == 1:
        char.最终伤害加成(0.05)
        char.技能攻击力加成(part=part, x=0.25)
        pass

def entry_14027(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化+2', '力量、智力+11%', '技能攻击力+29%', '攻击时，额外增加10%的伤害增加量', '所有属性强化+32', '暴击时，额外增加12%的伤害增加量']
    if mode == 0:
        char.所有属性强化加成(2)
        char.百分比力智加成(0.11)
        char.伤害增加加成(0.10)
        char.所有属性强化加成(32)
        char.暴击伤害加成(0.12)
        pass
    if mode == 1:
        char.技能攻击力加成(part=part, x=0.29)
        pass

def entry_14028(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化+25', '最终伤害+5%', '技能攻击力+30%', '攻击时，附加4%的伤害', '物理、魔法、独立攻击力+9%', '技能攻击力+4%', '最终伤害+7%']
    if mode == 0:
        char.移动速度增加(0.15)
        char.所有属性强化加成(25)
        char.最终伤害加成(0.05)
        char.技能攻击力加成(part=part, x=0.3)
        char.附加伤害加成(0.04)
        char.百分比三攻加成(0.09)
        char.技能攻击力加成(part=part, x=0.04)
        char.最终伤害加成(0.07)
        pass
    if mode == 1:
        pass

def entry_14029(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能攻击力+27%', '所有属性强化+12', '所有属性强化+40', '最终伤害+8%', '力量、智力+5%', '攻击时，额外增加4%的伤害增加量']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.27)
        char.所有属性强化加成(40)
        char.最终伤害加成(0.08)
        char.百分比力智加成(0.05)
        char.伤害增加加成(0.04)
        pass
    if mode == 1:
        char.所有属性强化加成(12, mode=1)
        char.攻击速度增加(part=part, x=0.15)
        char.移动速度增加(0.15)
        char.施放速度增加(37.5)
        pass

def entry_14030(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化+39', '攻击时，额外增加5%的伤害增加量', '技能攻击力+25%', '物理、魔法、独立攻击力+6%', '技能攻击力+4%', '攻击时，附加8%的伤害', '力量、智力+5%']
    if mode == 0:
        char.所有属性强化加成(39)
        char.伤害增加加成(0.05)
        char.技能攻击力加成(part=part, x=0.25)
        char.技能攻击力加成(part=part, x=0.04)
        char.附加伤害加成(0.08)
        char.百分比力智加成(0.05)
        pass
    if mode == 1:
        pass

def entry_14031(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，附加5%的伤害', '技能攻击力+30%', '所有属性强化+30', '攻击时，额外增加12%的伤害增加量', '力量、智力+220', '攻击时，附加12%的伤害']
    if mode == 0:
        char.附加伤害加成(0.05)
        char.技能攻击力加成(part=part, x=0.3)
        char.所有属性强化加成(30)
        char.伤害增加加成(0.12)
        char.基础属性加成(力智=220)
        char.附加伤害加成(0.12)
        pass
    if mode == 1:
        pass

def entry_14032(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能攻击力+30%', '最终伤害+6%(18暗抗)', '最终伤害+12%', '所有属性强化+40', '攻击时，附加9%的伤害']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.3)
        char.最终伤害加成(0.6)
        char.最终伤害加成(0.12)
        char.所有属性强化加成(0.4)
        char.附加伤害加成(0.09)
        pass
    if mode == 1:
        pass

def entry_14033(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能攻击力+19%', '最终伤害+10%', '所有职业Lv50所有技能Lv+1', '所有职业Lv85所有技能Lv+1', '所有职业Lv100所有技能Lv+1', '力量、智力+300', '暴击时，额外增加11%的伤害增加量', '所有职业Lv60~100所有技能Lv+1']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.19)
        char.最终伤害加成(0.1)
        char.基础属性加成(力智=300)
        char.暴击伤害加成(0.11)
        pass
    if mode == 1:
        char.技能等级加成('所有', 50, 50, 1)
        char.技能等级加成('所有', 85, 85, 1)
        char.技能等级加成('所有', 100, 100, 1)
        pass

def entry_14034(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化+10', '技能攻击力+27%', '物理、魔法、独立攻击力+120', '所有职业Lv1~45所有技能+1', '力量、智力+4%', '攻击时，附加7%的伤害', '最终伤害+10%(期望)']
    if mode == 0:
        char.所有属性强化加成(10)
        char.技能攻击力加成(part=part, x=0.27)
        char.基础属性加成(三攻=120)
        char.技能等级加成('所有', 1, 45, 1)
        char.百分比力智加成(0.04)
        char.附加伤害加成(0.07)
        pass
    if mode == 1:
        char.最终伤害加成(0.1)
        pass

def entry_14035(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化+23', '技能攻击力+27%', '攻击时，附加5.3%的伤害(期望)', '所有属性强化+16', '攻击时发生持续伤害3秒，伤害量为对敌人造成伤害的10%', '暴击时，额外增加8%的伤害增加量', '力量、智力+140']
    if mode == 0:
        char.所有属性强化加成(23)
        char.技能攻击力加成(part=part, x=0.27)
        char.附加伤害加成(0.053)
        char.所有属性强化加成(16)
        char.持续伤害加成(0.1)
        char.暴击伤害加成(0.08)
        char.基础属性加成(力智=140)
        pass
    if mode == 1:
        pass

def entry_14036(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有职业Lv1~85所有技能Lv+1（特性技能除外）', '所有职业Lv100所有技能Lv+1（特性技能除外）', '所有属性强化+20*改造等级', '所有属性强化+12', '5阶段', '- 技能攻击力+1%(x20)', '6阶段', '- 技能攻击力+3%', '7阶段', '- 所有属性强化+12']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.技能等级加成('所有', 1, 85, 1)
        char.技能等级加成('所有', 100, 100, 1)
        char.所有属性强化加成(20*改造lv)
        char.所有属性强化加成(12)
        if 改造lv >= 5:
            for i in range(0, 20):
                char.技能攻击力加成(part=part, x=0.01)
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
        if 改造lv >= 7:
            char.所有属性强化加成(12)
        pass
    if mode == 1:
        pass

def entry_14037(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暴击时，额外增加2%*改造等级的伤害增加量', '所有属性强化+8*改造等级', '暴击时，额外增加3%的伤害增加量', '1阶段', '-暴击时，额外增加28%的伤害增加量', '4阶段', '-技能攻击力+10%', '6阶段', '-技能攻击力+3%', '7阶段', '-暴击时，额外增加3%的伤害增加量']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.暴击伤害加成(0.02*改造lv)
        char.所有属性强化加成(8*改造lv)
        char.暴击伤害加成(0.03)
        if 改造lv >= 1:
            char.暴击伤害加成(0.28)
        if 改造lv >= 4:
            char.技能攻击力加成(part=part, x=0.1)
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
        if 改造lv >= 7:
            char.暴击伤害加成(0.03)
        pass
    if mode == 1:
        pass

def entry_14038(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["攻击时，额外增加3%*改造等级的伤害增加量", '所有属性强化+4*改造等级', "攻击时，额外增加3%的伤害增加量", '1阶段', '-力量、智力+18%', '4阶段', "-攻击时,附加1.75%的属性伤害(期望)", "-技能攻击力+8.65%(期望)", "6阶段", "-技能攻击力+3%", "7阶段", "-攻击时，额外增加3%的伤害增加量"]
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.伤害增加加成(0.03*改造lv)
        char.伤害增加加成(0.03)
        char.所有属性强化加成(4*改造lv)
        if 改造lv >= 1:
            char.百分比力智加成(0.18)
        if 改造lv >= 4:
            char.属性附加加成(0.0175)
            char.技能攻击力加成(part=part, x=0.0865)
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
        if 改造lv >= 7:
            char.暴击伤害加成(0.03)
        pass
    if mode == 1:
        pass

def entry_14039(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['力量、智力+30*改造等级', '所有属性强化+8*改造等级', '攻击时，附加3%的伤害', '1阶段', '-攻击时，附加35%的伤害', '5阶段', '-攻击时，附加10%的伤害', '-技能攻击力+7%', '6阶段', '-技能攻击力+3%', '7阶段', '-攻击时，附加3%的伤害']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.基础属性加成(力智=30*改造lv)
        char.所有属性强化加成(8*改造lv)
        char.附加伤害加成(0.03)
        if 改造lv >= 1:
            char.附加伤害加成(0.35)
        if 改造lv >= 5:
            char.附加伤害加成(0.1)
            char.技能攻击力加成(part=part, x=0.07)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.附加伤害加成(0.03)
            pass
        pass
    if mode == 1:
        pass

def entry_14040(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理、魔法、独立攻击力+40*改造等级', '所有属性强化+8*改造等级', '攻击时，额外增加3%的伤害增加量', '1阶段', '-攻击时，增加35%的伤害', '5阶段', '-所有属性强化+40', '6阶段', '-技能攻击力+3%', '7阶段', '-攻击时，额外增加3%的伤害增加量']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.基础属性加成(三攻=40*改造lv)
        char.所有属性强化加成(8*改造lv)
        char.伤害增加加成(0.03)
        if 改造lv >= 1:
            char.附加伤害加成(0.35)
            pass
        if 改造lv >= 4:
            char.所有属性强化加成(40)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.伤害增加加成(0.03)
            pass
        pass
    if mode == 1:
        pass

def entry_14041(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化+16*改造等级', '所有属性强化+12', '1阶段', '-所有职业Lv1~85所有技能Lv+2（特性技能除外）', '-所有职业Lv100所有技能Lv+2（特性技能除外）', '4阶段', '-力量、智力+8%', '6阶段', '-技能攻击力+3%', '7阶段', '-所有属性强化+12']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.所有属性强化加成(16*改造lv)
        char.所有属性强化加成(12)
        if 改造lv >= 1:
            char.技能等级加成('所有', 1, 85, 2)
            char.技能等级加成('所有', 100, 100, 2)
            pass
        if 改造lv >= 4:
            char.百分比力智加成(0.08)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.所有属性强化加成(12)
            pass
        pass
    if mode == 1:
        pass

def entry_14042(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暴击时，额外增加2%*改造等级的伤害增加量', '所有属性强化+8*改造等级', '暴击时，额外增加3%的伤害增加量', '1阶段', '-物理、魔法、独立攻击力+18%', '4阶段', '-攻击时，额外增加8%的伤害增加量', '-技能攻击力+7%', '5阶段', '-装备[青面修罗的面具]、[噙毒手套]中一种以上时，攻击时，附加7%的伤害', '6阶段', '-技能攻击力+3%', '7阶段', '-暴击时，额外增加3%的伤害增加量']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.所有属性强化加成(8*改造lv)
        char.暴击伤害加成(0.03)
        if 改造lv >= 1:
            char.百分比三攻加成(0.18)
            pass
        if 改造lv >= 4:
            char.伤害增加加成(0.08)
            char.技能攻击力加成(part=part, x=0.07)
            pass
        if 改造lv >= 5:
            if 40 in char.装备栏 or 36 in char.装备栏:
                char.附加伤害加成(0.07)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.暴击伤害加成(0.03)
            pass
        pass
    if mode == 1:
        pass

def entry_14043(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，额外增加2%*改造等级的伤害增加', '所有属性强化+8*改造等级', '攻击时，额外增加3%的伤害增加量', '1阶段', '-所有职业Lv50、85、100所有技能Lv+2', '-攻击时，附加4%的属性伤害', '5阶段', '-攻击时，额外增加5%的伤害增加量', '-技能攻击力+6%', '6阶段', '-技能攻击力+3%', '7阶段', '-攻击时，额外增加3%的伤害增加量']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.所有属性强化加成(8*改造lv)
        char.伤害增加加成(0.03)
        if 改造lv >= 1:
            char.技能等级加成('所有', 50, 50, 2)
            char.技能等级加成('所有', 85, 85, 2)
            char.技能等级加成('所有', 100, 100, 2)
            char.属性附加加成(0.04)
            pass
        if 改造lv >= 5:
            char.伤害增加加成(0.05)
            char.技能攻击力加成(part=part, x=0.06)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.伤害增加加成(0.03)
            pass
        pass
    if mode == 1:
        pass

def entry_14044(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能攻击力+4*改造等级', '攻击时，附加3%的伤害', '1阶段', '-攻击时，额外增加7%的伤害增加量', '-Lv50主动技能攻击力+30%', '-Lv85主动技能攻击力+25%', '-Lv100主动技能攻击力+16%', '5阶段', '-技能攻击力+12%', '6阶段', '-技能攻击力+3%', '7阶段', '-攻击时，附加3%的伤害']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.技能攻击力加成(part=part, x=0.04*改造lv)
        char.附加伤害加成(0.03)
        if 改造lv >= 1:
            char.伤害增加加成(0.07)
            char.技能倍率加成(50, 50, 0.3, type="active")
            char.技能倍率加成(85, 85, 0.25, type="active")
            char.技能倍率加成(100, 100, 0.16, type="active")
            pass
        if 改造lv >= 5:
            char.技能攻击力加成(part=part, x=0.12)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.附加伤害加成(0.03)
            pass
        pass
    if mode == 1:
        pass

def entry_14045(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暴击时，额外增加2%*改造等级的伤害增加量', '所有属性强化+8*改造等级', '暴击时，额外增加3%的伤害增加量', '1阶段', '-暴击时，额外增加5%的伤害增加量', '-所有属性强化+30', '-所有职业Lv50~85所有技能Lv+1（特性技能除外）', '-所有职业Lv100技能Lv+1（特性技能除外）', '5阶段', '-暴击时，额外增加10%的伤害增加量', '-技能攻击力+2%', '6阶段', '-技能攻击力+3%', '7阶段', '-暴击时，额外增加3%的伤害增加量']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.暴击伤害加成(0.02*改造lv)
        char.所有属性强化加成(8*改造lv)
        char.暴击伤害加成(0.03)
        if 改造lv >= 1:
            char.暴击伤害加成(0.05)
            char.所有属性强化加成(30)
            char.技能等级加成('所有', 50, 85, 1)
            char.技能等级加成('所有', 100, 100, 1)
            pass
        if 改造lv >= 5:
            char.暴击伤害加成(0.06)
            char.技能攻击力加成(part=part, x=0.02)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.暴击伤害加成(0.03)
            pass
        pass
    if mode == 1:
        pass

def entry_14046(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['最终伤害+2%*改造等级', '所有属性强化+8*改造等级', '最终伤害+3%', '1阶段', '-技能攻击力+5%', '-所有属性强化+42', '5阶段', '-技能攻击力+9%', '6阶段', '-技能攻击力+3%', '7阶段', '-最终伤害+3%']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.最终伤害加成(0.03)
        char.最终伤害加成(0.02*改造lv)
        char.所有属性强化加成(8*改造lv)
        if 改造lv >= 1:
            char.技能攻击力加成(part=part, x=0.05)
            char.所有属性强化加成(42)
            pass
        if 改造lv >= 5:
            char.技能攻击力加成(part=part, x=0.09)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.最终伤害加成(0.03)
            pass
        pass
    if mode == 1:
        pass

def entry_14047(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理、魔法、独立攻击力+2%*改造等级', '所有属性强化+8*改造等级', '物理、魔法、独立攻击力+3%', '1阶段', '-最终伤害+10%', '-物理、魔法、独立攻击力+11%', '5阶段', '-攻击时，附加4%的伤害', '-技能攻击力+7%', '6阶段', '-技能攻击力+3%', '7阶段', '-物理、魔法、独立攻击力+3%']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.百分比三攻加成(0.02*改造lv)
        char.所有属性强化加成(8*改造lv)
        char.百分比三攻加成(0.03)
        if 改造lv >= 1:
            char.最终伤害加成(0.1)
            char.百分比三攻加成(0.11)
            pass
        if 改造lv >= 5:
            char.附加伤害加成(0.04)
            char.技能攻击力加成(part=part, x=0.07)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.百分比三攻加成(0.03)
            pass
        pass
    if mode == 1:
        pass

def entry_14048(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化+16*改造等级', '所有属性强化+12', '1阶段', '-力量、智力+5%', '-技能攻击力+13%', '4阶段', '-攻击时，附加5%的属性伤害', '6阶段', '-技能攻击力+3%', '7阶段', '-所有属性强化+12']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.所有属性强化加成(16*改造lv)
        char.所有属性强化加成(12)
        if 改造lv >= 1:
            char.百分比力智加成(0.05)
            char.技能攻击力加成(part=part, x=0.13)
            pass
        if 改造lv >= 4:
            char.属性附加加成(0.05)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.所有属性强化加成(12)
            pass
        pass
    if mode == 1:
        pass

def entry_14049(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["攻击时，额外增加2%*改造等级的伤害增加量", '所有属性强化+8*改造等级', "攻击时，额外增加3%的伤害增加量""1阶段", "-攻击时，额外增加12%的伤害增加量", "攻击时，附加10%的伤害", "4阶段", "-发生持续伤害3秒，伤害量为对敌人造成伤害的4%", "-技能攻击力 +7%", "6阶段", "-技能攻击力 +3%", "7阶段", "-攻击时，额外增加3%的伤害增加量"
                ]
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.伤害增加加成(0.02*改造lv)
        char.所有属性强化加成(8*改造lv)
        char.伤害增加加成(0.03)
        if 改造lv >= 1:
            char.伤害增加加成(0.12)
            char.附加伤害加成(0.1)
            pass
        if 改造lv >= 4:
            char.持续伤害加成(0.04)
            char.技能攻击力加成(part=part, x=0.07)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.伤害增加加成(0.03)
            pass
        pass
    if mode == 1:
        pass

def entry_14050(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能攻击力+4*改造等级', '攻击时，附加3%的伤害', '1阶段', '-所有属性强化+40', '-攻击时，额外增加10%的伤害增加量', '4阶段', '-攻击时，附加10%的伤害', '6阶段', '-技能攻击力+3%', '7阶段', '-攻击时，附加3%的伤害']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.技能攻击力加成(part=part, x=0.04*改造lv)
        char.附加伤害加成(0.03)
        if 改造lv >= 1:
            char.所有属性强化加成(40)
            char.伤害增加加成(0.1)
            pass
        if 改造lv >= 4:
            char.附加伤害加成(0.1)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.附加伤害加成(0.03)
            pass
        pass
    if mode == 1:
        pass

def entry_14051(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理、魔法、独立攻击力+3%*改造等级', '所有属性强化+4*改造等级', '物理、魔法、独立攻击力+3%', '1阶段', '-物理、魔法、独立攻击力+14%', '-最终伤害+8%', '4阶段', '-技能攻击力+10%', '6阶段', '-技能攻击力+3%', '7阶段', '-物理、魔法、独立攻击力+3%']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.百分比三攻加成(0.03*改造lv)
        char.所有属性强化加成(4*改造lv)
        char.百分比三攻加成(0.03)
        if 改造lv >= 1:
            char.百分比三攻加成(0.14)
            char.最终伤害加成(0.08)
            pass
        if 改造lv >= 4:
            char.技能攻击力加成(part=part, x=0.1)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.百分比三攻加成(0.03)
            pass
        pass
    if mode == 1:
        pass

def entry_14052(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能攻击力+4*改造等级', '攻击时，附加3%的伤害', '1阶段', '-暴击时，额外增加18%的伤害增加量', '4阶段', '-攻击时，附加4%的伤害', '6阶段', '-技能攻击力+3%', '7阶段', '-攻击时，附加3%的伤害']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.技能攻击力加成(part=part, x=0.04*改造lv)
        char.附加伤害加成(0.03)
        if 改造lv >= 1:
            char.暴击伤害加成(0.18)
            pass
        if 改造lv >= 4:
            char.附加伤害加成(0.04)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.附加伤害加成(0.03)
            pass
        pass
    if mode == 1:
        pass

def entry_14053(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暴击时，额外增加3%*改造等级的伤害增加量', '所有属性强化+4*改造等级', '暴击时，额外增加3%的伤害增加量', '1阶段', '-力量、智力+15%', '-所有属性强化+10', '4阶段', '-技能攻击力+14%', '6阶段', '-技能攻击力+3%', '7阶段', '-暴击时，额外增加3%的伤害增加量']
    if mode == 0:
        改造lv = char.获取改造等级([part])
        char.暴击伤害加成(0.03*改造lv)
        char.所有属性强化加成(4*改造lv)
        char.暴击伤害加成(0.03)
        if 改造lv >= 1:
            char.百分比力智加成(0.15)
            char.所有属性强化加成(10)
            pass
        if 改造lv >= 4:
            char.技能攻击力加成(part=part, x=0.14)
            pass
        if 改造lv >= 6:
            char.技能攻击力加成(part=part, x=0.03)
            pass
        if 改造lv >= 7:
            char.暴击伤害加成(0.03)
            pass

