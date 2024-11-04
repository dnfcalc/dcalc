from core.basic.property import CharacterProperty
from core.equipment.property import 成长词条计算
import core.equipment.entry_0.params as pa

def entry_1363(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '攻击时，使敌人进入出血状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '出血' not in pa.get_state_type():
            pa.state_type.append('出血')
        char.异常时间['出血'][3] = min(char.异常时间['出血'][3],3)
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        pass


def entry_1364(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '攻击时，使敌人进入感电状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '感电' not in pa.get_state_type():
            pa.state_type.append('感电')
        char.异常时间['感电'][3] = min(char.异常时间['感电'][3],3)
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        pass


def entry_1365(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '攻击时，使敌人进入中毒状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '中毒' not in pa.get_state_type():
            pa.state_type.append('中毒')
        char.异常时间['中毒'][3] = min(char.异常时间['中毒'][3],3)
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        pass


def entry_1366(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '攻击时，使敌人进入灼伤状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '灼伤' not in pa.get_state_type():
            pa.state_type.append('灼伤')
        char.异常时间['灼伤'][3] = min(char.异常时间['灼伤'][3],3)
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        pass


def entry_1367(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤伤害 +15%']
    if mode == 0:
        char.异常增伤('灼伤', 0.15)
        pass
    if mode == 1:
        pass


def entry_1368(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['出血伤害 +15%']
    if mode == 0:
        char.异常增伤('出血', 0.15)
        pass
    if mode == 1:
        pass


def entry_1369(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['感电伤害 +15%']
    if mode == 0:
        char.异常增伤('感电', 0.15)
        pass
    if mode == 1:
        pass


def entry_1370(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['中毒伤害 +15%']
    if mode == 0:
        char.异常增伤('中毒', 0.15)
        pass
    if mode == 1:
        pass


def entry_1371(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击人型敌人时，技能伤害 +8%']
    if mode == 0:
        pass
    if mode == 1:
        if '人型' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.08, show=False)
        else:
            return '缺少人型敌人'
        pass


def entry_1372(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击野兽类型敌人时，技能伤害 +8%']
    if mode == 0:
        pass
    if mode == 1:
        if '野兽' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.08, show=False)
        else:
            return '缺少野兽型敌人'
        pass


def entry_1373(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击植物类型的敌人时，技能伤害 +8%']
    if mode == 0:
        pass
    if mode == 1:
        if '植物' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.08, show=False)
        else:
            return '缺少植物型敌人'
        pass


def entry_1374(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击昆虫类型的敌人时，技能伤害 +8%']
    if mode == 0:
        pass
    if mode == 1:
        if '昆虫' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.08, show=False)
        else:
            return '缺少昆虫型敌人'
        pass


def entry_1375(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击不死族类型的敌人时，技能伤害 +8%']
    if mode == 0:
        pass
    if mode == 1:
        if '不死' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.08, show=False)
        else:
            return '缺少不死族类型敌人'
        pass


def entry_1376(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击机械类型的敌人时，技能伤害 +8%']
    if mode == 0:
        pass
    if mode == 1:
        if '机械' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.08, show=False)
        else:
            return '缺少机械类型敌人'
        pass


def entry_1377(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击恶魔类型的敌人时，技能伤害 +8%']
    if mode == 0:
        pass
    if mode == 1:
        if '恶魔' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.08, show=False)
        else:
            return '缺少恶魔类型敌人'
        pass


def entry_1378(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击精灵类型的敌人时，技能伤害 +8%']
    if mode == 0:
        pass
    if mode == 1:
        if '精灵' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.08, show=False)
        else:
            return '缺少精灵类型敌人'
        pass


def entry_1379(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击天使类型的敌人时，技能伤害 +8%']
    if mode == 0:
        pass
    if mode == 1:
        if '天使' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.08, show=False)
        else:
            return '缺少天使类型敌人'
        pass


def entry_1380(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击龙族类型的敌人时，技能伤害 +8%']
    if mode == 0:
        pass
    if mode == 1:
        if '龙族' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.08, show=False)
        else:
            return '缺少龙族型敌人'
        pass


def entry_1381(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '闪避率 +4%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        pass


def entry_1382(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '命中率 +4%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        pass


def entry_1383(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '生命值最大值 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        pass


def entry_1384(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8% (觉醒技能除外)', '技能冷却时间 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能倍率加成(1, 100, 0.08, excName=char.觉醒技能)
        char.技能冷却缩减(1, 100, -0.1)
        pass


def entry_1385(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '所有属性抗性 +10']
    if mode == 0:
        char.所有属性抗性加成(10)
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        pass


def entry_1386(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '被破招攻击时，物理/魔法所受伤害 -5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        pass


def entry_1387(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +30']
    if mode == 0:
        char.所有属性强化加成(30)
        pass
    if mode == 1:
        pass


def entry_1388(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '1~45级技能冷却时间恢复速度 +20%']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.技能恢复加成(1, 45, 0.2)
        pass
    if mode == 1:
        pass


def entry_1389(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '60~80级技能冷却时间恢复速度 +15%']
    if mode == 0:
        char.技能攻击力加成(0.02)
        char.技能恢复加成(60, 80, 0.15)
        pass
    if mode == 1:
        pass


def entry_1390(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '95级技能冷却时间恢复速度 +15%']
    if mode == 0:
        char.技能攻击力加成(0.04)
        char.技能恢复加成(95, 95, 0.15)
        pass
    if mode == 1:
        pass


def entry_1391(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '1~20级技能冷却时间 -20%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        char.技能冷却缩减(1, 20, 0.2)
        pass


def entry_1392(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '25、30级技能冷却时间 -20%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        char.技能冷却缩减(25, 30, 0.2)
        pass


def entry_1393(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '35、40级技能冷却时间 -15%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        char.技能冷却缩减(35, 40, 0.15)
        pass


def entry_1394(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '45级技能冷却时间 -15%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        char.技能冷却缩减(45, 45, 0.15)
        pass


def entry_1395(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '60级技能冷却时间 -15%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        char.技能冷却缩减(60, 60, 0.15)
        pass


def entry_1396(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '70级技能冷却时间 -15%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        char.技能冷却缩减(70, 70, 0.15)
        pass


def entry_1397(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '75级技能冷却时间 -10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        char.技能冷却缩减(75, 75, 0.1)
        pass


def entry_1398(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '80级技能冷却时间 -10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        char.技能冷却缩减(80, 80, 0.1)
        pass


def entry_1399(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '95级技能冷却时间 -10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.04)
        char.技能冷却缩减(95, 95, 0.1)
        pass


def entry_1400(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '50级技能攻击力 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        char.技能倍率加成(50, 50, 0.1)
        pass


def entry_1401(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '85级技能攻击力 +8%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        char.技能倍率加成(85, 85, 0.08)
        pass


def entry_1402(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '100级技能攻击力 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        char.技能倍率加成(100, 100, 0.05)
        pass


def entry_1403(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '被击时，获得生命值最大值10%的保护罩，效果持续15秒。 (冷却时间12秒)']
    if mode == 0:
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.1)
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        pass


def entry_1404(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '生命值低于55%时，装备的保护罩最大值 +10%']
    if mode == 0:
        char.set_eq_params('protect_max',char.get_eq_params('protect_max') + 0.1)
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        pass


def entry_1405(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '魔法值低于55%时，装备的保护罩最大值 +10%']
    if mode == 0:
        char.set_eq_params('protect_max',char.get_eq_params('protect_max') + 0.1)
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        pass


def entry_1406(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '攻击时，2秒内恢复2200点生命值。 (冷却时间2秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        pass


def entry_1407(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '攻击时，2秒内恢复1750点魔法值。 (冷却时间2秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        pass


def entry_1408(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '攻击时，3秒内恢复2200点生命值和1750点魔法值。 (冷却时间3秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        pass


def entry_1409(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '物理/魔法所受伤害 -3%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.07)
        char.add_eq_params('hurted_ratio',0.03)
        pass


def entry_1410(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '消耗品、装备、技能的生命值恢复效果 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.07)
        pass


def entry_1411(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '魔法值消耗量 +100%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.07)
        char.MP消耗量加成(1.0)
        pass


def entry_1412(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '受到攻击时，生命值恢复10%。 (冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.07)
        pass


def entry_1413(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '受到攻击时，魔法值恢复10%。 (冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.07)
        pass


def entry_1414(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '每存在1名队友，增加6%的移动速度。 (最多叠加4次)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        char.移动速度增加(0.06*pa.teammate_num)
        pass


def entry_1415(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '存在1名队友，增加6%的攻击速度和9%的施放速度。 (最多叠加4次)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        char.攻击速度增加(part=part, x=0.06*pa.teammate_num)
        char.施放速度增加(0.09*pa.teammate_num)
        pass


def entry_1416(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '物理/魔法所受伤害 -8%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        char.add_eq_params('hurted_ratio',0.08)
        pass


def entry_1417(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间 -10% (觉醒技能除外)', '物理/魔法所受伤害 -7%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.1, excName=char.觉醒技能)
        char.add_eq_params('hurted_ratio',0.07)
        pass


def entry_1418(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能范围 +10%', '技能冷却时间 -10% (觉醒技能除外)']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.1)
        char.multiply_eq_params('skill_range_multi',1.1)
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.1, excName=char.觉醒技能)
        pass


def entry_1419(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '技能范围 +12%']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.12)
        char.multiply_eq_params('skill_range_multi',1.12)
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        pass


def entry_1420(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '回避率 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        pass


def entry_1421(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '命中率 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        pass


def entry_1422(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1423(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '所有速度 +10%']
    if mode == 0:
        char.所有速度增加(part=part, x=0.1)
        char.技能攻击力加成(0.06)
        pass
    if mode == 1:
        pass


def entry_1424(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '跳跃力 +30']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        pass


def entry_1425(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '攻击速度 +16%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.16)
        char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


def entry_1426(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['40~80级技能冷却时间恢复速度 +20% (觉醒技能除外)']
    if mode == 0:
        char.技能恢复加成(40, 80, 0.2)
        pass
    if mode == 1:
        pass


def entry_1427(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '所有速度 +15%']
    if mode == 0:
        char.所有速度增加(part=part, x=0.15)
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        pass


def entry_1428(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['装备的物体伤害 +10%', '所有速度 +15%']
    if mode == 0:
        char.所有速度增加(part=part,x=0.15)
        pass
    if mode == 1:
        for i in char.特效:
            i["power"] *= 1.1
        pass


def entry_1429(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '物理/魔法暴击率 +3%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        char.暴击率增加(0.03)
        pass


def entry_1430(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +25', '所有速度 +20%']
    if mode == 0:
        char.所有属性强化加成(25)
        char.所有速度增加(part=part, x=0.2)
        pass
    if mode == 1:
        pass


def entry_1431(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '物理/魔法防御力 +5000']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.06)
        char.add_eq_params('defense',5000)
        pass
    if mode == 1:
        pass


def entry_1432(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间 -10% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.1, excName=char.觉醒技能)
        pass


def entry_1433(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '移动速度 +5%']
    if mode == 0:
        char.移动速度增加(0.05)
        char.技能攻击力加成(0.04)
        pass
    if mode == 1:
        pass


def entry_1434(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '韧性条减少量 +25%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        pass


def entry_1435(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '弱点控制型异常状态和强控的韧性条减少量 +50%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.07)
        pass


def entry_1436(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '魔法值最大值 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        pass


def entry_1437(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '生命值最大值 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        pass


def entry_1438(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '进入地下城时，锁定生命值最大值的20%。', '移动速度 +15%']
    if mode == 0:
        cur = char.get_eq_params('hp_max')
        char.set_eq_params('hp_max',(100 if cur == 0 else cur)*0.8)
        char.移动速度增加(0.15)
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        pass


def entry_1439(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '每分钟恢复348点魔法值']
    if mode == 0:
        char.技能攻击力加成(0.07)
        pass
    if mode == 1:
        pass


def entry_1440(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.04)
        pass


def entry_1441(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '技能冷却时间恢复速度 +5% (觉醒技能除外)']
    if mode == 0:
        char.技能攻击力加成(0.04)
        char.技能恢复加成(1, 100, 0.05, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


def entry_1442(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '技能冷却时间恢复速度 +10% (觉醒技能除外)']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.技能恢复加成(1, 100, 0.1, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


def entry_1491(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '攻击时，使敌人进入出血状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '出血' not in pa.get_state_type():
            pa.state_type.append('出血')
        char.异常时间['出血'][3] = min(char.异常时间['出血'][3],3)
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1492(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '攻击时，使敌人进入感电状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '感电' not in pa.get_state_type():
            pa.state_type.append('感电')
        char.异常时间['感电'][3] = min(char.异常时间['感电'][3],3)
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1493(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '攻击时，使敌人进入中毒状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '中毒' not in pa.get_state_type():
            pa.state_type.append('中毒')
        char.异常时间['中毒'][3] = min(char.异常时间['中毒'][3],3)
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1494(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '攻击时，使敌人进入灼伤状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '灼伤' not in pa.get_state_type():
            pa.state_type.append('灼伤')
        char.异常时间['灼伤'][3] = min(char.异常时间['灼伤'][3],3)
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1495(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤伤害 +10%']
    if mode == 0:
        char.异常增伤('灼伤', 0.10)
        pass
    if mode == 1:
        pass


def entry_1496(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['出血伤害 +10%']
    if mode == 0:
        char.异常增伤('出血', 0.10)
        pass
    if mode == 1:
        pass


def entry_1497(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['感电伤害 +10%']
    if mode == 0:
        char.异常增伤('感电', 0.10)
        pass
    if mode == 1:
        pass


def entry_1498(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['中毒伤害 +10%']
    if mode == 0:
        char.异常增伤('中毒', 0.10)
        pass
    if mode == 1:
        pass


def entry_1499(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击人型敌人时，技能伤害 +4%']
    if mode == 0:
        pass
    if mode == 1:
        if '人型' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.04, show=False)
        else:
            return '缺少人型敌人'
        pass


def entry_1500(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击野兽类型敌人时，技能伤害 +4%']
    if mode == 0:
        pass
    if mode == 1:
        if '野兽' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.04, show=False)
        else:
            return '缺少野兽型敌人'
        pass


def entry_1501(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击植物类型的敌人时，技能伤害 +4%']
    if mode == 0:
        pass
    if mode == 1:
        if '植物' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.04, show=False)
        else:
            return '缺少植物型敌人'
        pass


def entry_1502(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击昆虫类型的敌人时，技能伤害 +4%']
    if mode == 0:
        pass
    if mode == 1:
        if '昆虫' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.08, show=False)
        else:
            return '缺少昆虫型敌人'
        pass


def entry_1503(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击不死族类型的敌人时，技能伤害 +4%']
    if mode == 0:
        pass
    if mode == 1:
        if '不死' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.04, show=False)
        else:
            return '缺少不死族类型敌人'
        pass


def entry_1504(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击机械类型的敌人时，技能伤害 +4%']
    if mode == 0:
        pass
    if mode == 1:
        if '机械' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.04, show=False)
        else:
            return '缺少机械类型敌人'
        pass


def entry_1505(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击恶魔类型的敌人时，技能伤害 +4%']
    if mode == 0:
        pass
    if mode == 1:
        if '恶魔' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.04, show=False)
        else:
            return '缺少恶魔类型敌人'
        pass


def entry_1506(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击精灵类型的敌人时，技能伤害 +4%']
    if mode == 0:
        pass
    if mode == 1:
        if '精灵' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.04, show=False)
        else:
            return '缺少精灵类型敌人'
        pass


def entry_1507(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击天使类型的敌人时，技能伤害 +4%']
    if mode == 0:
        pass
    if mode == 1:
        if '天使' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.04, show=False)
        else:
            return '缺少天使类型敌人'
        pass


def entry_1508(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击龙族类型的敌人时，技能伤害 +4%']
    if mode == 0:
        pass
    if mode == 1:
        if '龙族' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.04, show=False)
        else:
            return '缺少龙族型敌人'
        pass


def entry_1509(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '闪避率 +4%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1510(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '命中率 +4%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1511(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '生命值最大值 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1512(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5% (觉醒技能除外)', '技能冷却时间 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能倍率加成(1, 100, 0.05, excName=char.觉醒技能)
        char.技能冷却缩减(1, 100, -0.05)
        pass


def entry_1513(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '所有属性抗性 +5']
    if mode == 0:
        char.所有属性抗性加成(5)
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1514(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '被破招攻击时，物理/魔法所受伤害 -3%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1515(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +18']
    if mode == 0:
        char.所有属性强化加成(18)
        pass
    if mode == 1:
        pass


def entry_1516(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +1%', '1~45级技能冷却时间恢复速度 +12%']
    if mode == 0:
        char.技能攻击力加成(0.01)
        char.技能恢复加成(1, 45, 0.12)
        pass
    if mode == 1:
        pass


def entry_1517(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +1%', '60~80级技能冷却时间恢复速度 +9%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.01)
        char.技能恢复加成(60, 80, 0.09)
        pass


def entry_1518(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '95级技能冷却时间恢复速度 +9%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        char.技能恢复加成(95, 95, 0.09)
        pass


def entry_1519(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '1~20级技能冷却时间 -12%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        char.技能冷却缩减(1, 20, 0.12)
        pass


def entry_1520(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '25、30级技能冷却时间 -12%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        char.技能冷却缩减(25, 30, 0.12)
        pass


def entry_1521(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '35、40级技能冷却时间 -9%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        char.技能冷却缩减(35, 40, 0.09)
        pass


def entry_1522(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '45级技能冷却时间 -9%。']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        char.技能冷却缩减(45, 45, 0.09)
        pass


def entry_1523(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '60级技能冷却时间 -9%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        char.技能冷却缩减(60, 60, 0.09)
        pass


def entry_1524(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '70级技能冷却时间 -9%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        char.技能冷却缩减(70, 70, 0.09)
        pass


def entry_1525(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '75级技能冷却时间 -6%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        char.技能冷却缩减(75, 75, 0.06)
        pass


def entry_1526(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '80级技能冷却时间 -6%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        char.技能冷却缩减(80, 80, 0.06)
        pass


def entry_1527(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '95级技能冷却时间 -6%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        char.技能冷却缩减(95, 95, 0.06)
        pass


def entry_1528(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '50级技能攻击力 +6%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        char.技能倍率加成(50, 50, 0.06)
        pass


def entry_1529(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '85级技能攻击力 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        char.技能倍率加成(85, 85, 0.05)
        pass


def entry_1530(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '100级技能攻击力 +3%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        char.技能倍率加成(100, 100, 0.03)
        pass


def entry_1531(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '被击时，获得生命值最大值5%的保护罩，效果持续15秒。 (冷却时间12秒)']
    if mode == 0:
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.05)
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1532(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '生命值低于55%时，装备的保护罩最大值 +5%']
    if mode == 0:
        char.set_eq_params('protect_max',char.get_eq_params('protect_max') + 0.05)
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1533(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '魔法值低于55%时，装备的保护罩最大值 +5%']
    if mode == 0:
        char.set_eq_params('protect_max',char.get_eq_params('protect_max') + 0.05)
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1534(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '攻击时，2秒内恢复1100点生命值。 (冷却时间2秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1535(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '攻击时，2秒内恢复875点魔法值。 (冷却时间2秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1536(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '攻击时，3秒内恢复1100点生命值和875点魔法值。 (冷却时间3秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1537(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '物理/魔法所受伤害 -2%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.04)
        char.add_eq_params('hurted_ratio',0.02)
        pass


def entry_1538(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '消耗品、装备、技能的生命值恢复效果 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.04)
        pass


def entry_1539(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '魔法值消耗量 +100%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.04)
        char.MP消耗量加成(1.0)
        pass


def entry_1540(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '受到攻击时，生命值恢复5%。 (冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.04)
        pass


def entry_1541(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '受到攻击时，魔法值恢复5%。 (冷却时间30秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.04)
        pass


def entry_1542(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '每存在1名队友，增加6%的移动速度。 (最多叠加2次)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        char.移动速度增加(0.06*min(2, pa.teammate_num))
        pass


def entry_1543(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '存在1名队友，增加6%的攻击速度和9%的施放速度。 (最多叠加2次)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        char.攻击速度增加(part=part, x=0.06*min(2, pa.teammate_num))
        char.施放速度增加(0.09*min(2, pa.teammate_num))
        pass


def entry_1544(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '物理/魔法所受伤害 -4%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        char.add_eq_params('hurted_ratio',0.04)
        pass


def entry_1545(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间 -8% (觉醒技能除外)', '物理/魔法所受伤害 -3%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.08, excName=char.觉醒技能)
        char.add_eq_params('hurted_ratio',0.03)
        pass


def entry_1546(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能范围 +5%', '技能冷却时间 -6% (觉醒技能除外)']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.05)
        char.multiply_eq_params('skill_range_multi',1.05)
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.06, excName=char.觉醒技能)
        pass


def entry_1547(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '技能范围 +6%']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.06)
        char.multiply_eq_params('skill_range_multi',1.06)
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1548(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '回避率 +3%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        pass


def entry_1549(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '命中率 +3%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        pass


def entry_1550(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['']
    if mode == 0:
        pass
    if mode == 1:
        pass


def entry_1551(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '所有速度 +5%']
    if mode == 0:
        char.所有速度增加(part=part, x=0.05)
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1552(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '跳跃力 +15']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1553(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '攻击速度 +8%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.08)
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1554(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['40~80级技能冷却时间恢复速度 +12% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(40, 80, 0.12)
        pass


def entry_1555(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '所有速度 +8%']
    if mode == 0:
        char.所有速度增加(part=part, x=0.08)
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1556(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['装备的物体伤害 +6%', '所有速度 +8%']
    if mode == 0:
        char.所有速度增加(part=part, x=0.08)
        pass
    if mode == 1:
        for i in char.特效:
            i["power"] *= 1.06
        pass


def entry_1557(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '物理/魔法暴击率 +1.5%']
    if mode == 0:
        char.暴击率增加(0.015)
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1558(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +15', '所有速度 +12%']
    if mode == 0:
        char.所有属性强化加成(15)
        char.所有速度增加(part=part, x=0.12)
        pass
    if mode == 1:
        pass


def entry_1559(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '物理/魔法防御力 +2500']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.03)
        char.add_eq_params('defense',2500)
        pass
    if mode == 1:
        pass


def entry_1560(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间 -6% (觉醒技能除外)']
    if mode == 0:
        char.技能冷却缩减(1, 100, 0.06, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


def entry_1561(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '移动速度 +3%']
    if mode == 0:
        char.移动速度增加(0.03)
        char.技能攻击力加成(0.03)
        pass
    if mode == 1:
        pass


def entry_1562(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '韧性条减少量 +15%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(x=0.03)
        pass


def entry_1563(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '弱点控制型异常状态和强控的韧性条减少量 +25%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1564(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '魔法值最大值 +3%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1565(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '生命值最大值 +3%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        pass


def entry_1566(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '进入地下城时，锁定生命值最大值的20%。', '移动速度 +8%']
    if mode == 0:
        cur = char.get_eq_params('hp_max')
        char.set_eq_params('hp_max',(100 if cur == 0 else cur)*0.8)
        char.移动速度增加(0.08)
        char.技能攻击力加成(0.03)
        pass
    if mode == 1:
        pass


def entry_1567(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '每分钟恢复174点魔法值']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.04)
        pass


def entry_1568(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        pass


def entry_1569(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '技能冷却时间恢复速度 +2% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        char.技能恢复加成(1, 100, 0.02, excName=char.觉醒技能)
        pass


def entry_1570(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +1%', '技能冷却时间恢复速度 +8% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.01)
        char.技能恢复加成(1, 100, 0.08, excName=char.觉醒技能)
        pass


def entry_1571(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，攻击强化 +762.7%，效果持续60秒。']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(params[0])

