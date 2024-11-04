from .weapon import *
from .title import *
from .stable import *
from .pet import *
from .params import *
from .old import *
from .merge import *
from .fusion import *
from .customize import *
from core.basic.property import CharacterProperty
from .specificity import *
from .divinity import *
from .suit import *
from .amalgamationstone import *
from .asrahan import *
entry_func_list = {}  # id : enteyfunc 词条函数(数组)列表


def entry_0(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "空词条"
    if mode == 0:
        pass
    if mode == 1:
        pass

# region 部位固有属性


def entry_28(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['该装备的成长属性等级之和每达到40，增加3%的技能攻击力', ' - 穿戴神话装备时不适用', ' - 仅适用上衣、手镯、耳环中最高的1个']
    if mode == 0:
        if not char.已穿戴神话():  # 判断是否穿戴神话装备
            x = sum(char.词条等级.get(part, [0]))
            temp = {}
            for i in ['上衣', '手镯', '耳环']:  # 计算3个部位最高值
                temp[i] = sum(char.词条等级.get(i, [0]))
            temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)
            if part == temp[0][0]:
                char.技能攻击力加成(part=part, x=0.03 * int(min(320, x) / 40))
    if mode == 1:
        pass


def entry_29(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['Lv30 buff技能Lv+1', 'Lv50 主动技能Lv+1']
    if mode == 0:
        char.buff技能等级加成(30, 1)
        char.技能等级加成('主动', 50, 50, 1)
    if mode == 1:
        pass


def entry_30(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['Lv30 buff技能Lv+3', 'Lv50 主动技能Lv+4']
    if mode == 0:
        char.buff技能等级加成(30, 3)
        char.技能等级加成('主动', 50, 50, 4)
    if mode == 1:
        pass


def entry_10001(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["成长属性240级以上时增加1%技能攻击，每40级增加1%"]
    if mode == 0:
        if char.穿戴低于105():
            return
        x = sum(char.词条等级.get(part, [0]))
        if x >= 240:
            char.技能攻击力加成(part=part, x=0.01 * int((min(320, x) - 200) / 40))
    if mode == 1:
        pass


def entry_10002(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
      # (上衣)
        if not sj:
            return ["技能伤害 +12%"]
        else:
            return ['攻击强化 +204.8%', '技能伤害 +12%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        if char.是否升级110(part):
            char.攻击强化加成(204.8)
    if mode == 1:
        pass


def entry_10003(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
      # (下装)
        if not sj:
            return ["技能伤害 +12%"]
        else:
            return ['攻击强化 +204.8%', '技能伤害 +12%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        if char.是否升级110(part):
            char.攻击强化加成(204.8)
    if mode == 1:
        pass


def entry_10004(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
      # (头肩)
        if not sj:
            return ["技能伤害 +34%"]
        else:
            return ['攻击强化 +204.8%', '技能伤害 +34%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.34)
        if char.是否升级110(part):
            char.攻击强化加成(204.8)
    if mode == 1:
        pass


def entry_10005(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
      # (腰带)
        if not sj:
            return ["技能伤害 +12%"]
        else:
            return ['攻击强化 +204.8%', '技能伤害 +12%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        if char.是否升级110(part):
            char.攻击强化加成(204.8)
    if mode == 1:
        pass


def entry_10006(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
      # (鞋)
        if not sj:
            return ["技能伤害 +29%", "移动速度 +4%"]
        else:
            return ['攻击强化 +204.8%', "技能伤害 +29%", "移动速度 +4%"]
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.29)
        char.移动速度增加(0.04)
        if char.是否升级110(part):
            char.攻击强化加成(204.8)
    if mode == 1:
        pass


def entry_10007(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
      # (手镯)
        if not sj:
            return ["技能伤害 +12%"]
        else:
            return ['攻击强化 +204.8%', '技能伤害 +12%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        if char.是否升级110(part):
            char.攻击强化加成(204.8)
    if mode == 1:
        pass


def entry_10008(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
      # (项链)
        if not sj:
            return ["技能伤害 +12%"]
        else:
            return ['攻击强化 +204.8%', '技能伤害 +12%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        if char.是否升级110(part):
            char.攻击强化加成(204.8)
    if mode == 1:
        pass


def entry_10009(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
      # (戒指)
        if not sj:
            return ["技能伤害 +12%"]
        else:
            return ['攻击强化 +204.8%', '技能伤害 +12%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        if char.是否升级110(part):
            char.攻击强化加成(204.8)
    if mode == 1:
        pass


def entry_10010(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
      # (辅助装备)
        if not sj:
            return ["技能伤害 +12%"]
        else:
            return ['攻击强化 +204.8%', '技能伤害 +12%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        if char.是否升级110(part):
            char.攻击强化加成(204.8)
    if mode == 1:
        pass


def entry_10011(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
      # (魔法石)
        if not sj:
            return ["技能伤害 +12%"]
        else:
            return ['攻击强化 +204.8%', '技能伤害 +12%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        if char.是否升级110(part):
            char.攻击强化加成(204.8)
    if mode == 1:
        pass


def entry_10012(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
      # (耳环)
        if not sj:
            return ["技能伤害 +12%"]
        else:
            return ['攻击强化 +204.8%', '技能伤害 +12%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.12)
        if char.是否升级110(part):
            char.攻击强化加成(204.8)
    if mode == 1:
        pass


def entry_10013(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        # (胜负武器)
        if not sj:
            return ["技能伤害 +50%"]
        else:
            return ['攻击强化 +204.8%', '技能伤害 +50%']
        # (胜负武器)
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.50)
        if char.是否升级110(part):
            char.攻击强化加成(204.8)
    if mode == 1:
        pass


def entry_10014(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        # (吞噬武器)
        if not sj:
            return ["技能伤害 +49%"]
        else:
            return ['攻击强化 +204.8%', '技能伤害 +49%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.49)
        if char.是否升级110(part):
            char.攻击强化加成(204.8)
    if mode == 1:
        pass


def entry_10015(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        # (吞噬武器)
        if not sj:
            return ["技能伤害 +55%"]
        else:
            return ['攻击强化 +204.8%', '技能伤害 +55%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.55)
        if char.是否升级110(part):
            char.攻击强化加成(204.8)
    if mode == 1:
        pass


def entry_10016(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        if not sj:
        # (吞噬武器)
            return ["增益量 11695"]
        else:
            return ["增益量 11887"]
    if mode == 0:
        if char.是否升级110(part):
            char.辅助属性加成(buff量=11887)
        else:
            char.辅助属性加成(buff量=11695)
    if mode == 1:
        pass


def entry_10017(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["辅助职业 30级增益技能 Lv+3", "辅助职业 50级主动技能 Lv+4", "辅助职业 技能伤害 +20%","","解除穿戴时，已施放的30级增益技能、50级主动技能、100级主动技能的效果消失。"]
    if mode == 0:
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 3)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 4)
            char.技能攻击力加成(0.2)
    if mode == 1:
        pass


def entry_10018(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
      # (上衣)
        if not sj:
            return ["增益量 1010", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
        else:
            return ["增益量 1202", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
    if mode == 0:
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 1)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 1)
            if char.是否升级110(part):
                char.辅助属性加成(buff量=1202)
            else:
                char.辅助属性加成(buff量=1010)
    if mode == 1:
        pass


def entry_10019(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        # (下装)
        if not sj:
            return ["增益量 1010", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
        else:
            return ["增益量 1202", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
    if mode == 0:
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 1)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 1)
            if char.是否升级110(part):
                char.辅助属性加成(buff量=1202)
            else:
                char.辅助属性加成(buff量=1010)
    if mode == 1:
        pass


def entry_10020(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        # (头肩)
        if not sj:
            return ["增益量 1010", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
        else:
            return ["增益量 1202", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
    if mode == 0:
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 1)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 1)
            if char.是否升级110(part):
                char.辅助属性加成(buff量=1202)
            else:
                char.辅助属性加成(buff量=1010)
    if mode == 1:
        pass


def entry_10021(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        # (腰带)
        if not sj:
            return ["增益量 1010", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
        else:
            return ["增益量 1202", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
    if mode == 0:
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 1)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 1)
            if char.是否升级110(part):
                char.辅助属性加成(buff量=1202)
            else:
                char.辅助属性加成(buff量=1010)
    if mode == 1:
        pass


def entry_10022(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        # (鞋)
        if not sj:
            return ["增益量 1010", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
        else:
            return ["增益量 1202", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
    if mode == 0:
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 1)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 1)
            if char.是否升级110(part):
                char.辅助属性加成(buff量=1202)
            else:
                char.辅助属性加成(buff量=1010)
    if mode == 1:
        pass


def entry_10023(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        # (手镯)
        if not sj:
            return ["增益量 295", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
        else:
            return ["增益量 487", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
    if mode == 0:
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 1)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 1)
            if char.是否升级110(part):
                char.辅助属性加成(buff量=487)
            else:
                char.辅助属性加成(buff量=295)
    if mode == 1:
        pass


def entry_10024(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        # (项链)
        if not sj:
            return ["增益量 295", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
        else:
            return ["增益量 487", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
    if mode == 0:
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 1)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 1)
            if char.是否升级110(part):
                char.辅助属性加成(buff量=487)
            else:
                char.辅助属性加成(buff量=295)
    if mode == 1:
        pass


def entry_10025(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        # (戒指)
        if not sj:
            return ["增益量 295", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
        else:
            return ["增益量 487", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
    if mode == 0:
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 1)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 1)
            if char.是否升级110(part):
                char.辅助属性加成(buff量=487)
            else:
                char.辅助属性加成(buff量=295)
    if mode == 1:
        pass


def entry_10026(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        # (辅助装备)
        if not sj:
            return ["增益量 1875", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
        else:
            return ["增益量 2067", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
    if mode == 0:
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 1)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 1)
            if char.是否升级110(part):
                char.辅助属性加成(buff量=2067)
            else:
                char.辅助属性加成(buff量=1875)
    if mode == 1:
        pass


def entry_10027(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        # (魔法石)
        if not sj:
            return ["增益量 1875", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+2"]
        else:
            return ["增益量 2067", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+2"]
    if mode == 0:
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 1)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 2)
            if char.是否升级110(part):
                char.辅助属性加成(buff量=2067)
            else:
                char.辅助属性加成(buff量=1875)
    if mode == 1:
        pass


def entry_10028(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        # (耳环)
        if not sj:
            return ["增益量 1010", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
        else:
            return ["增益量 1202", "辅助职业 30级增益技能 Lv+1", "辅助职业 50级主动技能 Lv+1"]
    if mode == 0:
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 1)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 1)
            if char.是否升级110(part):
                char.辅助属性加成(buff量=1202)
            else:
                char.辅助属性加成(buff量=1010)
    if mode == 1:
        pass


def entry_10029(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        # (跨越者武器)
        if not sj:
            return ["技能伤害 +35%"]
        else:
            return ['攻击强化 +204.8%', '技能伤害 +35%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.35)
        if char.是否升级110(part):
            char.攻击强化加成(204.8)
    if mode == 1:
        pass

def entry_10030(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["辅助职业 30级增益技能 Lv+3", "辅助职业 50级主动技能 Lv+4","","解除穿戴时，已施放的30级增益技能、50级主动技能、100级主动技能的效果消失。"]
    if mode == 0:
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 3)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 4)
    if mode == 1:
        pass

# endregion

# region 雾神武器固有属性

# 土

def entry_10033(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["攻击强化 +2142.4%","技能伤害 +108.0%"]
    if mode == 0:
        char.攻击强化加成(2142.4)
        char.技能攻击力加成(1.08)
        pass
    if mode == 1:
        pass

def entry_10034(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["增益量 22266","辅助职业 1~100级技能等级 +2","辅助职业 30级增益技能 Lv+3", "辅助职业 50级主动技能 Lv+4","","解除穿戴时，已施放的30级增益技能、50级主动技能、100级主动技能的效果消失。"]
    if mode == 0:
        char.辅助属性加成(buff量=22266)
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 3)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 4)
            char.技能等级加成('所有',1,100,2)
    if mode == 1:
        pass

# 木

def entry_10031(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["攻击强化 +1927.2%","技能伤害 +60.8%"]
    if mode == 0:
        char.攻击强化加成(1927.2)
        char.技能攻击力加成(0.608)
        pass
    if mode == 1:
        pass

def entry_10032(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["增益量 22266","辅助职业 技能伤害 +20%","辅助职业 30级增益技能 Lv+3", "辅助职业 50级主动技能 Lv+4","","解除穿戴时，已施放的30级增益技能、50级主动技能、100级主动技能的效果消失。"]
    if mode == 0:
        char.辅助属性加成(buff量=22266)
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 3)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 4)
            char.技能攻击力加成(0.2)
    if mode == 1:
        pass

# 水

def entry_10035(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["攻击强化 +2142.4%","技能伤害 +92.5%"]
    if mode == 0:
        char.攻击强化加成(2142.4)
        char.技能攻击力加成(0.925)
        pass
    if mode == 1:
        pass

def entry_10036(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["增益量 22194","辅助职业 技能伤害 +20%","辅助职业 30级增益技能 Lv+3", "辅助职业 50级主动技能 Lv+4","","解除穿戴时，已施放的30级增益技能、50级主动技能、100级主动技能的效果消失。"]
    if mode == 0:
        char.辅助属性加成(buff量=22194)
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 3)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 4)
            char.技能攻击力加成(0.2)
    if mode == 1:
        pass

# 火

def entry_10037(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["攻击强化 +2142.4%","技能伤害 +116.9%"]
    if mode == 0:
        char.攻击强化加成(2142.4)
        char.技能攻击力加成(1.169)
        pass
    if mode == 1:
        pass

def entry_10038(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["增益量 22780","辅助职业 技能伤害 +20%","辅助职业 30级增益技能 Lv+3", "辅助职业 50级主动技能 Lv+4","","解除穿戴时，已施放的30级增益技能、50级主动技能、100级主动技能的效果消失。"]
    if mode == 0:
        char.辅助属性加成(buff量=22780)
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 3)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 4)
            char.技能攻击力加成(0.2)
    if mode == 1:
        pass

# 金

def entry_10039(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["攻击强化 +2142.4%","技能伤害 +114.7%"]
    if mode == 0:
        char.攻击强化加成(2142.4)
        char.技能攻击力加成(1.147)
        pass
    if mode == 1:
        pass

def entry_10040(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["增益量 22780","辅助职业 技能伤害 +20%","辅助职业 30级增益技能 Lv+3", "辅助职业 50级主动技能 Lv+4","","解除穿戴时，已施放的30级增益技能、50级主动技能、100级主动技能的效果消失。"]
    if mode == 0:
        char.辅助属性加成(buff量=22780)
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 3)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 4)
            char.技能攻击力加成(0.2)
    if mode == 1:
        pass

# 失调

def entry_10041(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["攻击强化 +204.8%","技能伤害 +78.6%"]
    if mode == 0:
        char.攻击强化加成(204.8)
        char.技能攻击力加成(0.786)
        pass
    if mode == 1:
        pass

def entry_10042(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["增益量 15502","辅助职业 技能伤害 +20%","辅助职业 30级增益技能 Lv+3", "辅助职业 50级主动技能 Lv+4","","解除穿戴时，已施放的30级增益技能、50级主动技能、100级主动技能的效果消失。"]
    if mode == 0:
        char.辅助属性加成(buff量=15502)
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 3)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 4)
            char.技能攻击力加成(0.2)
    if mode == 1:
        pass


# 超越记忆

def entry_10043(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["攻击强化 +100.0%","技能伤害 +78.6%"]
    if mode == 0:
        char.攻击强化加成(100.0)
        char.技能攻击力加成(0.786)
        pass
    if mode == 1:
        pass

def entry_10044(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ["增益量 15310","辅助职业 技能伤害 +20%","辅助职业 30级增益技能 Lv+3", "辅助职业 50级主动技能 Lv+4","","解除穿戴时，已施放的30级增益技能、50级主动技能、100级主动技能的效果消失。"]
    if mode == 0:
        char.辅助属性加成(buff量=15310)
        if char.类型 == '辅助':
            char.技能等级加成('主动', 30, 30, 3)
        if char.类型 == '辅助' or char.bufferCarry:
            char.技能等级加成('主动', 50, 50, 4)
            char.技能攻击力加成(0.2)
    if mode == 1:
        pass


# endregion


# region 部位固有属性
for i in range(10001, 10045):
    try:
        entry_func_list[i] = eval('entry_{}'.format(i))
    except Exception:
        pass
# endregion 部位固有属性


def entry_538(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['30级buff技能等级 +1', '50级主动技能等级 +2']
    if mode == 0:
        char.buff技能等级加成(30, 1)
        char.技能等级加成('主动', 50, 50, 2)
    if mode == 1:
        pass


def entry_1237(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['', '该装备的成长属性等级之和达到240，增加1%的技能伤害', '- 该装备的成长属性等级之和每增加40级，额外增加1%的技能伤害', '- 穿戴100级以下装备时不适用该效果']
    if mode == 0:
        if char.穿戴低于105():
            return
        x = sum(char.词条等级.get(part, [0]))
        if x >= 240:
            char.技能攻击力加成(part=part, x=0.01 * int((x - 200) / 40))
    if mode == 1:
        pass


# 目前成长词条范围
for i in range(4000):
    try:
        entry_func_list[i] = eval('entry_{}'.format(i))
    except Exception:
        pass

for i in range(10101, 14000):
    try:
        entry_func_list[i] = eval('entry_{}'.format(i))
    except Exception:
        pass


for i in range(14001, 14999):
    try:
        entry_func_list[i] = eval('entry_{}'.format(i))
    except Exception:
        pass

# 特性词条
for i in range(20000,20400):
    try:
        entry_func_list[i] = eval('entry_{}'.format(i))
    except Exception:
        pass

# 套装
for i in range(30001,39999):
    try:
        entry_func_list[i] = eval('entry_{}'.format(i))
    except Exception:
        pass


entry_range = {
    "growth":[0,2000],
    "specificity":[20000,20400],
    "inherent":[10000,10030],
    "pet":[10101, 14000],
    "titile":[14001, 14999]
}

def get_info(type,char={}):
    if type == "asrahan":
        return asrahan_infos
    if type == "specificity":
        return get_specificity_infos(char)
# 词条效果id范围 0~18999
    infolist = []
    keys =  entry_range.get(type,[0,0])
    for i in range(keys[0],keys[1]):
        try:
            data = {}
            data['id'] = i
            info = entry_func_list[i](char=char, text=True)
            num = 0
            for k in index:
                data[k] = info[num]
                num += 1
            infolist.append(data)
        except Exception:
            break
    return infolist

def get_specificity_infos(char: CharacterProperty = {}):
    if char.类型 != "辅助":
        return specificity_infos
    import copy
    info = copy.deepcopy(specificity_infos)
    remark = {
        "crusader_male": ["- [生命源泉]技能冷却时间-50% / 所有速度增加效果 +10%",
                          "- [圣愈之风]屏障生命值比率+10%",
                          "- [神圣洗礼 : 信仰之翼]技能的神圣之力持续时间 +0.3秒",
                          "",
                          ""],
        "crusader_female": ["- [勇气颂歌]增益效果持续时间 +4秒",
                            "- [勇气圣歌]、[新生圣歌]移动速度+200% / 物理、魔法所受伤害减少量 +20%",
                            "- 施放[救赎彼岸 : 惩戒圣枪]技能后，[圣佑之阵]强化2次<br/>* [圣佑之阵]冷却时间 -70%<br/>* 穿戴[圣佑之阵]护石时，进一步强化：队员无敌效果 +1.5秒"
                            "",
                            ""],
        "enchantress": ["- [疯狂召唤]增益效果持续时间 +3秒",
                        "- [爱之急救]持续时间+20% / 物理、魔法所受伤害减少量 +20%",
                        "- [开幕！ 人偶剧场]、[终幕！ 人偶剧场]技能增益持续时间内，[人偶之森]冷却时间 -40%",
                        "",
                        ""
                        ],
        "muse": ["- [燃情狂想曲]增益效果持续时间 +3秒",
                 "- [自由律动]持续时间+1秒",
                 "- 施放[开场:唯我璀璨]技能时，可以无限制使用[崭新曲风]，效果持续23秒。",
                 "",
                 ""
                 ]
    }
    for a in info:
        for b in a.get("detail", []):
            cost = 0
            for c in b.get("lvinfo", []):
                cost += c.get("cost", 0)
                if b.get("name", "") == "[强力一击]":
                    c["remark"] = remark.get(char.实际名称, [])[:c["lv"]]
                else:
                    c["remark"] = []
                c["remark"] = [f"增益量 {cost * 7.2}"] + c["remark"]
    return info

specificity_func_list = {}

specificity_infos = [{
    "type": 0,
    "name": "规律系",
    "desc": "遵循规律可对敌人造成额外伤害，有利于战斗。",
    "detail": [
            {
                "id": 20016,
                "name": "[强力一击]",
                "desc": "技能伤害 +{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 96,
                        "needprecost": 0,
                        "params": [10]
                    },
                    {
                        "lv": 2,
                        "cost": 96,
                        "needprecost": 210,
                        "params": [16]
                    },
                    {
                        "lv": 3,
                        "cost": 96,
                        "needprecost": 430,
                        "params": [22]
                    },
                    {
                        "lv": 4,
                        "cost": 96,
                        "needprecost": 640,
                        "params": [28]
                    },
                    {
                        "lv": 5,
                        "cost": 96,
                        "needprecost": 850,
                        "params": [35]
                    }
                ],
                "master": 5,
                "masterWith": [20017],
                "masterWithMax": 5,
                "x": 3,
                "y": 0,
                "preconditions": []
            },
        {
                "id": 20017,
                "name": "[冥想]",
                "desc": "技能冷却时间 -{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 96,
                        "needprecost": 210,
                        "params": [10]
                    },
                    {
                        "lv": 2,
                        "cost": 96,
                        "needprecost": 640,
                        "params": [20]
                    }
                ],
                "master": 2,
                "masterWith": [20016],
                "masterWithMax": 5,
                "x": 3,
                "y": 1,
                "preconditions": []
            },
        {
                "id": 20000,
                "name": "[魔弹射手]",
                "desc": "攻击时，发射魔弹，对附近的敌人造成伤害。(冷却时间0.5秒)<br/>- 魔弹伤害量：{0}%<br/>魔弹发射个数：{1}个",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [98, 1]
                    },
                    {
                        "lv": 2,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [196, 1]
                    },
                    {
                        "lv": 3,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [294, 1]
                    },
                    {
                        "lv": 4,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [588, 1]
                    },
                    {
                        "lv": 5,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [979, 1]
                    },
                    {
                        "lv": 6,
                        "cost": 60,
                        "needprecost": 0,
                        "params": [1126, 1]
                    },
                    {
                        "lv": 7,
                        "cost": 60,
                        "needprecost": 0,
                        "params": [1350, 1]
                    }
                ],
                "master": 7,
                "x": 0,
                "y": 0,
                "preconditions": []
            }, {
                "id": 20001,
                "name": "[魔力增幅]",
                "desc": "魔弹伤害量 +{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [10]
                    },
                    {
                        "lv": 2,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [15]
                    },
                    {
                        "lv": 3,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [20]
                    },
                    {
                        "lv": 4,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [25]
                    },
                    {
                        "lv": 5,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [30]
                    },
                    {
                        "lv": 6,
                        "cost": 60,
                        "needprecost": 0,
                        "params": [35]
                    },
                    {
                        "lv": 7,
                        "cost": 60,
                        "needprecost": 0,
                        "params": [40]
                    }
                ],
                "master": 7,
                "x": 0,
                "y": 1,
                "preconditions": [{
                    "id": 20000,
                    "needLv": 3
                }]
            }, {
                "id": 20002,
                "name": "[预备弹夹]",
                "desc": "魔弹发射个数 +{0}个",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 80,
                        "needprecost": 0,
                        "params": [2]
                    }
                ],
                "master": 1,
                "x": 0,
                "y": 2,
                "preconditions": [{
                    "id": 20001,
                    "needLv": 3
                }]
            }, {
                "id": 20003,
                "name": "[乱射]",
                "desc": "第6次发射魔弹时，魔弹个数增加至{0}倍{1}",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 100,
                        "needprecost": 0,
                        "params": [3, ""]
                    },
                    {
                        "lv": 2,
                        "cost": 100,
                        "needprecost": 0,
                        "params": [3, "<br/>第66次发射魔弹时，触发魔弹暴走。<br/>- 魔弹暴走的伤害量应用魔弹射手的数值"]
                    }
                ],
                "master": 2,
                "x": 0,
                "y": 3,
                "preconditions": [{
                    "id": 20002,
                    "needLv": 1
                },
                    {
                    "id": 20000,
                    "needLv": 5
                }]
            },
        {
                "id": 20004,
                "name": "[魔剑舞者]",
                "desc": "攻击时，生成[魔剑风暴]，对附近的敌人造成伤害。 (冷却时间5秒)。<br/>- [魔剑风暴]伤害量：{0}%<br/>- [魔剑风暴]持续时间：{1}秒",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 10,
                        "needprecost": 0,
                        "params": [306, 1.5]
                    },
                    {
                        "lv": 2,
                        "cost": 10,
                        "needprecost": 0,
                        "params": [459, 1.5]
                    },
                    {
                        "lv": 3,
                        "cost": 10,
                        "needprecost": 0,
                        "params": [612, 1.5]
                    },
                    {
                        "lv": 4,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [688, 2]
                    },
                    {
                        "lv": 5,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [917, 2.5]
                    },
                    {
                        "lv": 6,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [1070, 3]
                    },
                    {
                        "lv": 7,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [1310, 3.5]
                    },
                    {
                        "lv": 8,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [1441, 3.5]
                    },
                    {
                        "lv": 9,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [1572, 3.5]
                    },
                    {
                        "lv": 10,
                        "cost": 60,
                        "needprecost": 0,
                        "params": [1868, 3.5]
                    }
                ],
                "master": 10,
                "x": 1,
                "y": 0,
                "preconditions": []
            }, {
                "id": 20005,
                "name": "[荆棘护甲]",
                "desc": "[魔剑风暴]范围 +{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [10]
                    },
                    {
                        "lv": 2,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [20]
                    },
                    {
                        "lv": 3,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [30]
                    },
                    {
                        "lv": 4,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [40]
                    },
                    {
                        "lv": 5,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [50]
                    }
                ],
                "master": 5,
                "x": 1,
                "y": 1,
                "preconditions": [{
                    "id": 20004,
                    "needLv": 3
                }]
            }, {
                "id": 20006,
                "name": "[剑刃账幕]",
                "desc": "[魔剑风暴]伤害量 +{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [5]
                    }, {
                        "lv": 2,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [10]
                    }, {
                        "lv": 3,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [15]
                    }, {
                        "lv": 4,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [20]
                    }, {
                        "lv": 5,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [25]
                    }, {
                        "lv": 6,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [30]
                    }, {
                        "lv": 7,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [35]
                    }
                ],
                "master": 7,
                "x": 1,
                "y": 2,
                "preconditions": [{
                    "id": 20005,
                    "needLv": 3
                }]
            }, {
                "id": 20007,
                "name": "[剑痕]",
                "desc": "[魔剑风暴]多段攻击间隔 -{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [10]
                    }, {
                        "lv": 2,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [20]
                    }, {
                        "lv": 3,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [30]
                    }, {
                        "lv": 4,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [40]
                    }, {
                        "lv": 5,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [50]
                    }, {
                        "lv": 6,
                        "cost": 60,
                        "needprecost": 0,
                        "params": [55]
                    }, {
                        "lv": 7,
                        "cost": 60,
                        "needprecost": 0,
                        "params": [65]
                    }
                ],
                "master": 7,
                "x": 1,
                "y": 3,
                "preconditions": [{
                    "id": 20006,
                    "needLv": 3
                },
                    {
                    "id": 20004,
                    "needLv": 7
                }]
            },
        {
                "id": 20008,
                "name": "[魔工学炮手]",
                "desc": "生成1个追踪敌人进行攻击的魔力炮。 (再次生成所需冷却时间30秒)<br/>- 魔力炮伤害量：{0}%<br/>- 魔力炮持续时间：10秒",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [486]
                    },
                    {
                        "lv": 2,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [973]
                    },
                    {
                        "lv": 3,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [1459]
                    },
                    {
                        "lv": 4,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [2919]
                    },
                    {
                        "lv": 5,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [4864]
                    },
                    {
                        "lv": 6,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [5837]
                    },
                    {
                        "lv": 7,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [7094]
                    }
                ],
                "master": 7,
                "x": 2,
                "y": 0,
                "preconditions": []
            }, {
                "id": 20009,
                "name": "[核融合]",
                "desc": "魔力炮伤害量 +{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [5]
                    },
                    {
                        "lv": 2,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [7]
                    },
                    {
                        "lv": 3,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [10]
                    },
                    {
                        "lv": 4,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [15]
                    },
                    {
                        "lv": 5,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [20]
                    }
                ],
                "master": 5,
                "x": 2,
                "y": 1,
                "preconditions": [{
                    "id": 20008,
                    "needLv": 3
                }]
            }, {
                "id": 20010,
                "name": "[空气力学]",
                "desc": "魔力炮多段攻击间隔 -{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [7]
                    }, {
                        "lv": 2,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [10]
                    }, {
                        "lv": 3,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [12]
                    }, {
                        "lv": 4,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [15]
                    }, {
                        "lv": 5,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [20]
                    }
                ],
                "master": 5,
                "x": 2,
                "y": 2,
                "preconditions": [{
                    "id": 20009,
                    "needLv": 3
                }]
            }, {
                "id": 20011,
                "name": "[魔力猎食]",
                "desc": "每次攻击魔力炮时，持续时间 +{0}秒。 (冷却时间{1}秒){2}",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [3, 5, ""]
                    }, {
                        "lv": 2,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [4, 4, ""]
                    }, {
                        "lv": 3,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [5, 3, ""]
                    }, {
                        "lv": 4,
                        "cost": 80,
                        "needprecost": 0,
                        "params": [5, 3, "<br/>魔力炮攻击时，释放魔力波动。 (冷却时间7秒)<br/>- 魔力波动伤害量：魔力炮伤害量的100%"]
                    }, {
                        "lv": 5,
                        "cost": 80,
                        "needprecost": 0,
                        "params": [5, 3, "<br/>魔力炮攻击时，释放魔力波动。 (冷却时间7秒)<br/>- 魔力波动伤害量：魔力炮伤害量的300%"]
                    }
                ],
                "master": 5,
                "x": 2,
                "y": 3,
                "preconditions": [{
                    "id": 20010,
                    "needLv": 3
                },
                    {
                    "id": 20008,
                    "needLv": 5
                }]
            }
    ]
},
    {
    "type": 1,
    "name": "猛攻系",
    "desc": "可以变得更加猛烈和强力，持续不断地战斗。",
    "detail": [
            {
                "id": 20108,
                "name": "[强力一击]",
                "desc": "技能伤害 +{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 96,
                        "needprecost": 0,
                        "params": [10]
                    },
                    {
                        "lv": 2,
                        "cost": 96,
                        "needprecost": 210,
                        "params": [16]
                    },
                    {
                        "lv": 3,
                        "cost": 96,
                        "needprecost": 430,
                        "params": [22]
                    },
                    {
                        "lv": 4,
                        "cost": 96,
                        "needprecost": 640,
                        "params": [28]
                    },
                    {
                        "lv": 5,
                        "cost": 96,
                        "needprecost": 850,
                        "params": [35]
                    }
                ],
                "master": 5,
                "masterWith": [20109],
                "masterWithMax": 5,
                "x": 3,
                "y": 0,
                "preconditions": []
            },
        {
                "id": 20109,
                "name": "[冥想]",
                "desc": "技能冷却时间 -{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 96,
                        "needprecost": 210,
                        "params": [10]
                    },
                    {
                        "lv": 2,
                        "cost": 96,
                        "needprecost": 640,
                        "params": [20]
                    }
                ],
                "master": 2,
                "masterWith": [20108],
                "masterWithMax": 5,
                "x": 3,
                "y": 0.75,
                "preconditions": []
            },
        {
                "id": 20100,
                "name": "[速攻：连击]",
                "desc": "施放技能时，进入[连击]状态5秒。<br/>[连击]：所有速度 +{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [2]
                    },
                    {
                        "lv": 2,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [3]
                    },
                    {
                        "lv": 3,
                        "cost": 45,
                        "needprecost": 0,
                        "params": [4]
                    },
                    {
                        "lv": 4,
                        "cost": 35,
                        "needprecost": 0,
                        "params": [4.5]
                    },
                    {
                        "lv": 5,
                        "cost": 35,
                        "needprecost": 0,
                        "params": [5]
                    }
                ],
                "master": 5,
                "x": 0,
                "y": 0,
                "preconditions": [],
                "conflict": [20104]
            }, {
                "id": 20101,
                "name": "[速攻：奔涌击]",
                "desc": "[连击]状态下，施放技能时，进入[奔涌击]状态5秒。<br/>[奔涌击]：所有速度 +{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 45,
                        "needprecost": 0,
                        "params": [2]
                    },
                    {
                        "lv": 2,
                        "cost": 45,
                        "needprecost": 0,
                        "params": [3]
                    },
                    {
                        "lv": 3,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [4]
                    },
                    {
                        "lv": 4,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [4.5]
                    },
                    {
                        "lv": 5,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [5]
                    }
                ],
                "master": 5,
                "x": 0,
                "y": 0.75,
                "preconditions": [{
                    "id": 20100,
                    "needLv": 3
                }]
            }, {
                "id": 20102,
                "name": "[速攻：闪影击]",
                "desc": "[奔涌击]状态下，施放技能时，进入[闪影击]状态5秒。<br/>[闪影击]：所有速度 +{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [4]
                    },
                    {
                        "lv": 2,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [5]
                    },
                    {
                        "lv": 3,
                        "cost": 55,
                        "needprecost": 0,
                        "params": [6]
                    },
                    {
                        "lv": 4,
                        "cost": 45,
                        "needprecost": 0,
                        "params": [6.5]
                    },
                    {
                        "lv": 5,
                        "cost": 45,
                        "needprecost": 0,
                        "params": [7]
                    }
                ],
                "master": 5,
                "x": 0,
                "y": 2.25,
                "preconditions": [{
                    "id": 20101,
                    "needLv": 3
                }]
            }, {
                "id": 20103,
                "name": "[破竹之势]",
                "desc": "[闪影击]状态下，施放技能时{0}，技能伤害 +{1}%，效果持续10秒。",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 60,
                        "needprecost": 0,
                        "params": ["，解除所有[速攻]效果", 3]
                    },
                    {
                        "lv": 2,
                        "cost": 50,
                        "needprecost": 0,
                        "params": ["，解除所有[速攻]效果", 4]
                    },
                    {
                        "lv": 3,
                        "cost": 50,
                        "needprecost": 0,
                        "params": ["", 5]
                    }
                ],
                "master": 3,
                "x": 0,
                "y": 3,
                "preconditions": [{
                    "id": 20102,
                    "needLv": 3
                }]
            },
        {
                "id": 20104,
                "name": "[强袭：破击]",
                "desc": "施放技能时，进入[破击]状态5秒。<br/>[破击]：物理/魔法所受伤害 -{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [1]
                    },
                    {
                        "lv": 2,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [2]
                    },
                    {
                        "lv": 3,
                        "cost": 45,
                        "needprecost": 0,
                        "params": [3]
                    },
                    {
                        "lv": 4,
                        "cost": 35,
                        "needprecost": 0,
                        "params": [3.5]
                    },
                    {
                        "lv": 5,
                        "cost": 35,
                        "needprecost": 0,
                        "params": [4]
                    }
                ],
                "master": 5,
                "x": 1,
                "y": 0,
                "preconditions": [],
                "conflict": [20100]
            }, {
                "id": 20105,
                "name": "[强袭：强腕击]",
                "desc": "[破击]状态下，施放技能时，进入[强腕击]状态5秒。<br/>[强腕击]：物理/魔法所受伤害 -{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 45,
                        "needprecost": 0,
                        "params": [1]
                    },
                    {
                        "lv": 2,
                        "cost": 45,
                        "needprecost": 0,
                        "params": [2]
                    },
                    {
                        "lv": 3,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [3]
                    },
                    {
                        "lv": 4,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [3.5]
                    },
                    {
                        "lv": 5,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [4]
                    }
                ],
                "master": 5,
                "x": 1,
                "y": 0.75,
                "preconditions": [{
                    "id": 20104,
                    "needLv": 3
                }]
            }, {
                "id": 20106,
                "name": "[强袭：泰山击]",
                "desc": "[强腕击]状态下，施放技能时，进入[泰山击]状态5秒。<br/>[泰山击]：物理/魔法所受伤害 -{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [1]
                    },
                    {
                        "lv": 2,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [2]
                    },
                    {
                        "lv": 3,
                        "cost": 55,
                        "needprecost": 0,
                        "params": [3]
                    },
                    {
                        "lv": 4,
                        "cost": 45,
                        "needprecost": 0,
                        "params": [3.5]
                    },
                    {
                        "lv": 5,
                        "cost": 45,
                        "needprecost": 0,
                        "params": [4]
                    }
                ],
                "master": 5,
                "x": 1,
                "y": 2.25,
                "preconditions": [{
                    "id": 20105,
                    "needLv": 3
                }]
            }, {
                "id": 20107,
                "name": "[英雄豪杰]",
                "desc": "[泰山击]状态下，施放技能时{0}，技能伤害 +{1}%，并进入霸体状态，效果持续10秒。",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 60,
                        "needprecost": 0,
                        "params": ["，解除所有[强袭]效果", 3]
                    },
                    {
                        "lv": 2,
                        "cost": 50,
                        "needprecost": 0,
                        "params": ["，解除所有[强袭]效果", 4]
                    },
                    {
                        "lv": 3,
                        "cost": 50,
                        "needprecost": 0,
                        "params": ["", 5]
                    }
                ],
                "master": 3,
                "x": 1,
                "y": 3,
                "preconditions": [{
                    "id": 20106,
                    "needLv": 3
                }]
            },
    ]
},
    {
    "type": 2,
    "name": "保护系",
    "desc": "强化和消耗保护罩，保护队友并攻击敌人。",
    "detail": [
            {
                "id": 20208,
                "name": "[强力一击]",
                "desc": "技能伤害 +{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 96,
                        "needprecost": 0,
                        "params": [10]
                    },
                    {
                        "lv": 2,
                        "cost": 96,
                        "needprecost": 210,
                        "params": [16]
                    },
                    {
                        "lv": 3,
                        "cost": 96,
                        "needprecost": 430,
                        "params": [22]
                    },
                    {
                        "lv": 4,
                        "cost": 96,
                        "needprecost": 640,
                        "params": [28]
                    },
                    {
                        "lv": 5,
                        "cost": 96,
                        "needprecost": 850,
                        "params": [35]
                    }
                ],
                "master": 5,
                "masterWith": [20209],
                "masterWithMax": 5,
                "x": 3,
                "y": 0,
                "preconditions": []
            },
        {
                "id": 20209,
                "name": "[冥想]",
                "desc": "技能冷却时间 -{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 96,
                        "needprecost": 210,
                        "params": [10]
                    },
                    {
                        "lv": 2,
                        "cost": 96,
                        "needprecost": 640,
                        "params": [20]
                    }
                ],
                "master": 2,
                "masterWith": [20208],
                "masterWithMax": 5,
                "x": 3,
                "y": 0.75,
                "preconditions": []
            },
        {
                "id": 20200,
                "name": "[保护罩填充]",
                "desc": "施放技能时，赋予生命值最大值3%的保护罩。 (冷却时间3秒；最多叠加{0}次)",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [1]
                    },
                    {
                        "lv": 2,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [2]
                    },
                    {
                        "lv": 3,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [3]
                    },
                    {
                        "lv": 4,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [4]
                    },
                    {
                        "lv": 5,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [5]
                    }
                ],
                "master": 5,
                "x": 1,
                "y": 0,
                "preconditions": []
            }, {
                "id": 20201,
                "name": "[护盾爆裂 - 爆炸]",
                "desc": "保护罩解除时，引发爆炸，攻击周围敌人。<br/>- 爆炸伤害量：{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 15,
                        "needprecost": 0,
                        "params": [152]
                    },
                    {
                        "lv": 2,
                        "cost": 15,
                        "needprecost": 0,
                        "params": [304]
                    },
                    {
                        "lv": 3,
                        "cost": 15,
                        "needprecost": 0,
                        "params": [456]
                    },
                    {
                        "lv": 4,
                        "cost": 15,
                        "needprecost": 0,
                        "params": [912]
                    },
                    {
                        "lv": 5,
                        "cost": 15,
                        "needprecost": 0,
                        "params": [1521]
                    }
                ],
                "master": 5,
                "x": 0,
                "y": 0.75,
                "preconditions": [{
                    "id": 20200,
                    "needLv": 3
                }]
            }, {
                "id": 20202,
                "name": "[火盾]",
                "desc": "生成火焰，对触碰到保护罩的敌人造成伤害。 (冷却时间0.3秒)<br/>- 火焰伤害量：{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 25,
                        "needprecost": 0,
                        "params": [101]
                    },
                    {
                        "lv": 2,
                        "cost": 25,
                        "needprecost": 0,
                        "params": [203]
                    },
                    {
                        "lv": 3,
                        "cost": 25,
                        "needprecost": 0,
                        "params": [304]
                    },
                    {
                        "lv": 4,
                        "cost": 25,
                        "needprecost": 0,
                        "params": [608]
                    },
                    {
                        "lv": 5,
                        "cost": 25,
                        "needprecost": 0,
                        "params": [1014]
                    },
                    {
                        "lv": 6,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [1217]
                    },
                    {
                        "lv": 7,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [1521]
                    }
                ],
                "master": 7,
                "x": 0,
                "y": 2.25,
                "preconditions": [{
                    "id": 20201,
                    "needLv": 3
                }],
                "conflict": [20206]
            }, {
                "id": 20203,
                "name": "[背水一战]",
                "desc": "解除觉醒技能关联。<br/>50级技能冷却时间 -50%<br/>50级技能攻击力 +{0}%<br/>50级增益技能效果 -70% (仅限辅助职业)",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 100,
                        "needprecost": 0,
                        "params": [0]
                    },
                    {
                        "lv": 2,
                        "cost": 60,
                        "needprecost": 0,
                        "params": [10]
                    },
                    {
                        "lv": 3,
                        "cost": 60,
                        "needprecost": 0,
                        "params": [15]
                    },
                    {
                        "lv": 4,
                        "cost": 70,
                        "needprecost": 0,
                        "params": [25]
                    },
                    {
                        "lv": 5,
                        "cost": 70,
                        "needprecost": 0,
                        "params": [30]
                    }
                ],
                "master": 5,
                "x": 0,
                "y": 3,
                "preconditions": [{
                    "id": 20202,
                    "needLv": 3
                },
                    {
                    "id": 20200,
                    "needLv": 5
                }]
                }, {
                "id": 20204,
                "name": "[保护罩续充]",
                "desc": "装备的填充型保护罩的填充冷却时间 -1秒",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 30,
                        "needprecost": 0,
                        "params": []
                    }
                ],
                "master": 1,
                "x": 1,
                "y": 1.5,
                "preconditions": [{
                    "id": 20200,
                    "needLv": 1
                }]
            }, {
                "id": 20205,
                "name": "[护盾爆裂 - 恢复]",
                "desc": "保护罩解除时，周围300px范围内的队员恢复{0}%的生命值和魔法值。",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 15,
                        "needprecost": 0,
                        "params": [1]
                    },
                    {
                        "lv": 2,
                        "cost": 15,
                        "needprecost": 0,
                        "params": [1.5]
                    },
                    {
                        "lv": 3,
                        "cost": 15,
                        "needprecost": 0,
                        "params": [2]
                    },
                    {
                        "lv": 4,
                        "cost": 15,
                        "needprecost": 0,
                        "params": [2.5]
                    },
                    {
                        "lv": 5,
                        "cost": 15,
                        "needprecost": 0,
                        "params": [3]
                    }
                ],
                "master": 5,
                "x": 2,
                "y": 0.75,
                "preconditions": [{
                    "id": 20200,
                    "needLv": 3
                }]
            }, {
                "id": 20206,
                "name": "[水盾]",
                "desc": "保护罩周围{0}px内队友的生命值/魔法值恢复{1}%。 (冷却时间3秒)<br/><br/>技能伤害 +{2}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 25,
                        "needprecost": 0,
                        "params": [100, 0.2, 0]
                    },
                    {
                        "lv": 2,
                        "cost": 25,
                        "needprecost": 0,
                        "params": [150, 0.3, 0]
                    },
                    {
                        "lv": 3,
                        "cost": 25,
                        "needprecost": 0,
                        "params": [200, 0.5, 0]
                    },
                    {
                        "lv": 4,
                        "cost": 25,
                        "needprecost": 0,
                        "params": [250, 0.7, 0]
                    },
                    {
                        "lv": 5,
                        "cost": 25,
                        "needprecost": 0,
                        "params": [300, 1, 0]
                    },
                    {
                        "lv": 6,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [300,1, 0.5]
                    },
                    {
                        "lv": 7,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [300,1, 1]
                    }
                ],
                "master": 7,
                "x": 2,
                "y": 2.25,
                "preconditions": [{
                    "id": 20205,
                    "needLv": 3
                }
                ],
                "conflict": [20202]
            },
        {
                "id": 20207,
                "name": "[披靡庇护]",
                "desc": "100级技能攻击力 +{0}%<br/>施放100级技能后，进入无敌状态一段时间。",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 100,
                        "needprecost": 0,
                        "params": [15]
                    },
                    {
                        "lv": 2,
                        "cost": 60,
                        "needprecost": 0,
                        "params": [17]
                    },
                    {
                        "lv": 3,
                        "cost": 60,
                        "needprecost": 0,
                        "params": [20]
                    },
                    {
                        "lv": 4,
                        "cost": 70,
                        "needprecost": 0,
                        "params": [22]
                    },
                    {
                        "lv": 5,
                        "cost": 70,
                        "needprecost": 0,
                        "params": [25]
                    }
                ],
                "master": 5,
                "x": 2,
                "y": 3,
                "preconditions": [{
                    "id": 20206,
                    "needLv": 3
                },
                    {
                    "id": 20200,
                    "needLv": 5
                }]
            }
    ]
},
    {
    "type": 3,
    "name": "具现系",
    "desc": "使用炼金术具现出各种道具，强化自身。",
    "detail": [
            {
                "id": 20311,
                "name": "[强力一击]",
                "desc": "技能伤害 +{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 96,
                        "needprecost": 0,
                        "params": [10]
                    },
                    {
                        "lv": 2,
                        "cost": 96,
                        "needprecost": 210,
                        "params": [16]
                    },
                    {
                        "lv": 3,
                        "cost": 96,
                        "needprecost": 430,
                        "params": [22]
                    },
                    {
                        "lv": 4,
                        "cost": 96,
                        "needprecost": 640,
                        "params": [28]
                    },
                    {
                        "lv": 5,
                        "cost": 96,
                        "needprecost": 850,
                        "params": [35]
                    }
                ],
                "master": 5,
                "masterWith": [20312],
                "masterWithMax": 5,
                "x": 3,
                "y": 0,
                "preconditions": []
            },
        {
                "id": 20312,
                "name": "[冥想]",
                "desc": "技能冷却时间 -{0}%",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 96,
                        "needprecost": 210,
                        "params": [10]
                    },
                    {
                        "lv": 2,
                        "cost": 96,
                        "needprecost": 640,
                        "params": [20]
                    }
                ],
                "master": 2,
                "masterWith": [20311],
                "masterWithMax": 5,
                "x": 3,
                "y": 0.75,
                "preconditions": []
            },
        {
                "id": 20300,
                "name": "[灵药炼制]",
                "desc": "每{0}秒炼制一~四等灵药<br/>- 腕力灵药：技能伤害 +1/2/4/5%，效果持续20秒。<br/>- 铁壁灵药：物理/魔法所受伤害 -4/7/10/15%，效果持续20秒。<br/>- 神速灵药：所有速度 +5/10/15/20%，效果持续20秒。",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [30]
                    },
                    {
                        "lv": 2,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [28]
                    },
                    {
                        "lv": 3,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [26]
                    },
                    {
                        "lv": 4,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [23]
                    },
                    {
                        "lv": 5,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [20]
                    },
                    {
                        "lv": 6,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [18]
                    },
                    {
                        "lv": 7,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [15]
                    }
                ],
                "master": 7,
                "x": 1,
                "y": 0,
                "preconditions": []
            }, {
                "id": 20301,
                "name": "[力量精通]",
                "desc": "拾取灵药时，技能伤害 +{0}%，效果持续{1}秒。",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [1, 5]
                    },
                    {
                        "lv": 2,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [1, 10]
                    },
                    {
                        "lv": 3,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [1, 13]
                    },
                    {
                        "lv": 4,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [1, 16]
                    },
                    {
                        "lv": 5,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [1, 20]
                    },
                    {
                        "lv": 6,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [1.5, 25]
                    },
                    {
                        "lv": 7,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [2, 25]
                    }
                ],
                "master": 7,
                "x": 0,
                "y": 0.75,
                "preconditions": [{
                    "id": 20300,
                    "needLv": 3
                }]
            }, {
                "id": 20302,
                "name": "[强化 - 力量精通]",
                "desc": "拾取灵药时，所有速度 +5%，效果持续{0}秒。",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [5]
                    },
                    {
                        "lv": 2,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [10]
                    },
                    {
                        "lv": 3,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [13]
                    },
                    {
                        "lv": 4,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [16]
                    },
                    {
                        "lv": 5,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [20]
                    },
                    {
                        "lv": 6,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [22]
                    },
                    {
                        "lv": 7,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [25]
                    }
                ],
                "master": 7,
                "x": 0,
                "y": 1.5,
                "preconditions": [{
                    "id": 20301,
                    "needLv": 3
                }]
            }, {
                "id": 20303,
                "name": "[传说再现 - 破坏]",
                "desc": "高度成熟的炼制术有时会产生意想不到的效果。<br/>- 有{0}%的几率生成武具，而非灵药。<br/>{1}",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [1, '']
                    },
                    {
                        "lv": 2,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [2, '']
                    },
                    {
                        "lv": 3,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [3, '']
                    },
                    {
                        "lv": 4,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [5, '']
                    },
                    {
                        "lv": 5,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [10, '']
                    },
                    {
                        "lv": 6,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [10, '<br/>增强武具的效果。']
                    },
                    {
                        "lv": 7,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [10, '<br/>增强武具的效果。']
                    }
                ],
                "master": 7,
                "x": 0,
                "y": 3,
                "preconditions": [{
                    "id": 20302,
                    "needLv": 3
                },
                    {
                    "id": 20300,
                    "needLv": 5
                }],
                "conflict": [20310,20304]
                }, {
                "id": 20304,
                "name": "[高效炼制]",
                "desc": "炼制时，有{0}%的几率，额外炼成1个灵药。",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [10]
                    },
                    {
                        "lv": 2,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [12]
                    },
                    {
                        "lv": 3,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [24]
                    },
                    {
                        "lv": 4,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [26]
                    },
                    {
                        "lv": 5,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [28]
                    },
                    {
                        "lv": 6,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [30]
                    },
                    {
                        "lv": 7,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [32]
                    },
                    {
                        "lv": 8,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [34]
                    },
                    {
                        "lv": 9,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [37]
                    },
                    {
                        "lv": 10,
                        "cost": 60,
                        "needprecost": 0,
                        "params": [40]
                    }
                ],
                "master": 10,
                "x": 1,
                "y": 0.75,
                "conflict": [20310,20303],
                "preconditions": [{
                    "id": 20300,
                    "needLv": 3
                }]
            }, {
                "id": 20305,
                "name": "[精巧收尾]",
                "desc": "炼制时不会生成四等灵药。",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 80,
                        "needprecost": 0,
                        "params": []
                    }
                ],
                "master": 1,
                "x": 1,
                "y": 1.5,
                "preconditions": [{
                    "id": 20304,
                    "needLv": 3
                }]
            }, {
                "id": 20306,
                "name": "[完美炼制]",
                "desc": "炼制时不会生成三等灵药。",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 100,
                        "needprecost": 0,
                        "params": []
                    }
                ],
                "master": 1,
                "x": 1,
                "y": 2.25,
                "preconditions": [{
                    "id": 20305,
                    "needLv": 1
                },
                    {
                    "id": 20300,
                    "needLv": 5
                }
                ]
            }, {
                "id": 20307,
                "name": "[一级炼制术士]",
                "desc": "炼制时不会生成二等灵药。",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 100,
                        "needprecost": 0,
                        "params": []
                    }
                ],
                "master": 1,
                "x": 1,
                "y": 3,
                "preconditions": [{
                    "id": 20306,
                    "needLv": 1
                },
                    {
                    "id": 20300,
                    "needLv": 5
                }
                ]
            }, {
                "id": 20308,
                "name": "[治愈精通]",
                "desc": "拾取灵药时，恢复{0}%的生命值和魔法值。",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [2]
                    },
                    {
                        "lv": 2,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [3]
                    },
                    {
                        "lv": 3,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [4]
                    },
                    {
                        "lv": 4,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [5]
                    },
                    {
                        "lv": 5,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [7]
                    },
                    {
                        "lv": 6,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [8]
                    },
                    {
                        "lv": 7,
                        "cost": 40,
                        "needprecost": 0,
                        "params": [10]
                    }
                ],
                "master": 7,
                "x": 2,
                "y": 0.75,
                "preconditions": [{
                    "id": 20300,
                    "needLv": 3
                }]
            }, {
                "id": 20309,
                "name": "[强化 - 治愈精通]",
                "desc": "拾取灵药时，进入霸体状态{0}秒，进入无敌状态{1}秒。",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [5, 0]
                    },
                    {
                        "lv": 2,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [10, 0]
                    },
                    {
                        "lv": 3,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [13, 0]
                    },
                    {
                        "lv": 4,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [16, 0]
                    },
                    {
                        "lv": 5,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [20, 0]
                    },
                    {
                        "lv": 6,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [20, 0.2]
                    },
                    {
                        "lv": 7,
                        "cost": 50,
                        "needprecost": 0,
                        "params": [20, 0.5]
                    }
                ],
                "master": 7,
                "x": 2,
                "y": 1.5,
                "preconditions": [{
                    "id": 20308,
                    "needLv": 3
                }]
            }, {
                "id": 20310,
                "name": "[传说再现 - 守护]",
                "desc": "高度成熟的炼制术有时会重现传说。<br/>- 有{0}%的几率生成武具，而非灵药。<br/>{1}",
                "lvinfo": [
                    {
                        "lv": 1,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [1, '']
                    },
                    {
                        "lv": 2,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [2, '']
                    },
                    {
                        "lv": 3,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [3, '']
                    },
                    {
                        "lv": 4,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [5, '']
                    },
                    {
                        "lv": 5,
                        "cost": 20,
                        "needprecost": 0,
                        "params": [10, '']
                    },
                    {
                        "lv": 6,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [10, '<br/>增强武具的效果。']
                    },
                    {
                        "lv": 7,
                        "cost": 30,
                        "needprecost": 0,
                        "params": [10, '<br/>增强武具的效果。']
                    }
                ],
                "master": 7,
                "x": 2,
                "y": 3,
                "preconditions": [{
                    "id": 20309,
                    "needLv": 3
                },
                    {
                    "id": 20300,
                    "needLv": 5
                }],
                "conflict": [20303,20304]
            },
    ]
}
]

