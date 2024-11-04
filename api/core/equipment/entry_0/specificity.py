from core.basic.property import CharacterProperty
from functools import reduce
import core.equipment.entry_0.params as pa
# 规律系 - [魔弹射手]
def entry_20000(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "攻击时，发射魔弹，对附近的敌人造成伤害。(冷却时间0.5秒)<br/>- 魔弹伤害量：{0}%<br/>魔弹发射个数：{1}个"
    lv_params = [[98, 1], [196, 1], [294, 1], [588, 1], [979, 1], [1126, 1], [1350, 1]]
    cost = [30, 30, 30, 30, 30, 60, 60]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 规律系 - [魔力增幅]
def entry_20001(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "魔弹伤害量 +{0}%"
    lv_params = [[10], [15], [20], [25], [30], [35], [40]]
    cost = [30, 30, 30, 30, 30, 60, 60]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 规律系 - [预备弹夹]
def entry_20002(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "魔弹发射个数 +{0}个"
    lv_params = [[2]]
    cost = [80]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 规律系 - [乱射]
def entry_20003(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "第6次发射魔弹时，魔弹个数增加至{0}倍{1}"
    lv_params = [[3, ''], [3, '<br/>第66次发射魔弹时，触发魔弹暴走。<br/>- 魔弹暴走的伤害量应用魔弹射手的数值']]
    cost = [100, 100]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 规律系 - [魔剑舞者]
def entry_20004(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "攻击时，生成[魔剑风暴]，对附近的敌人造成伤害。 (冷却时间5秒)。<br/>- [魔剑风暴]伤害量：{0}%<br/>- [魔剑风暴]持续时间：{1}秒"
    lv_params = [[306, 1.5], [459, 1.5], [612, 1.5], [688, 2], [917, 2.5], [1070, 3], [1310, 3.5], [1441, 3.5], [1572, 3.5], [1868, 3.5]]
    cost = [10, 10, 10, 20, 20, 20, 20, 30, 30, 60]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 规律系 - [荆棘护甲]
def entry_20005(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "[魔剑风暴]范围 +{0}%"
    lv_params = [[10], [20], [30], [40], [50]]
    cost = [20, 20, 20, 20, 20]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 规律系 - [剑刃账幕]
def entry_20006(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "[魔剑风暴]伤害量 +{0}%"
    lv_params = [[5], [10], [15], [20], [25], [30], [35]]
    cost = [20, 20, 20, 30, 30, 50, 50]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 规律系 - [剑痕]
def entry_20007(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "[魔剑风暴]多段攻击间隔 -{0}%"
    lv_params = [[10], [20], [30], [40], [50], [55], [65]]
    cost = [30, 30, 30, 30, 30, 60, 60]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 规律系 - [魔工学炮手]
def entry_20008(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "生成1个追踪敌人进行攻击的魔力炮。 (再次生成所需冷却时间30秒)<br/>- 魔力炮伤害量：{0}%<br/>- 魔力炮持续时间：10秒"
    lv_params = [[486], [973], [1459], [2919], [4864], [5837], [7094]]
    cost = [20, 20, 20, 20, 20, 40, 40]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 规律系 - [核融合]
def entry_20009(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "魔力炮伤害量 +{0}%"
    lv_params = [[5], [7], [10], [15], [20]]
    cost = [30, 30, 30, 50, 50]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 规律系 - [空气力学]
def entry_20010(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "魔力炮多段攻击间隔 -{0}%"
    lv_params = [[7], [10], [12], [15], [20]]
    cost = [30, 30, 30, 30, 30]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 规律系 - [魔力猎食]
def entry_20011(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "每次攻击魔力炮时，持续时间 +{0}秒。 (冷却时间{1}秒){2}"
    lv_params = [[3, 5, ''], [4, 4, ''], [5, 3, ''], [5, 3, '<br/>魔力炮攻击时，释放魔力波动。 (冷却时间7秒)<br/>- 魔力波动伤害量：魔力炮伤害量的100%'], [5, 3, '<br/>魔力炮攻击时，释放魔力波动。 (冷却时间7秒)<br/>- 魔力波动伤害量：魔力炮伤害量的300%']]
    cost = [40, 50, 50, 80, 80]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 规律系 - [强力一击]
def entry_20016(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "技能伤害 +{0}%"
    lv_params = [[10], [16], [22], [28], [35]]
    cost = [96, 96, 96, 96, 96]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
            char.技能攻击力加成(lv_params[lv-1][0]/100)
            if char.实际名称 == 'crusader_male':
                char.get_skill_by_name('生命源泉').CDR *= 0.5
        pass
    if mode == 1:
        pass

# 规律系 - [冥想]
def entry_20017(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "技能冷却时间 -{0}%"
    lv_params = [[10], [20]]
    cost = [96, 96]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
            char.技能冷却缩减(1, 100, lv_params[lv-1][0]/100, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass

# 猛攻系 - [速攻：连击]
def entry_20100(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "施放技能时，进入[连击]状态5秒。<br/>[连击]：所有速度 +{0}%"
    lv_params = [[2], [3], [4], [4.5], [5]]
    cost = [40, 40, 45, 35, 35]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        if lv > 0:
            char.所有速度增加(lv_params[lv-1][0]/100, '特性')
        pass
    if mode == 1:
        pass

# 猛攻系 - [速攻：奔涌击]
def entry_20101(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "[连击]状态下，施放技能时，进入[奔涌击]状态5秒。<br/>[奔涌击]：所有速度 +{0}%"
    lv_params = [[2], [3], [4], [4.5], [5]]
    cost = [45, 45, 50, 40, 40]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        if lv > 0:
            char.所有速度增加(lv_params[lv-1][0]/100, '特性')
        pass
    if mode == 1:
        pass

# 猛攻系 - [速攻：闪影击]
def entry_20102(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "[奔涌击]状态下，施放技能时，进入[闪影击]状态5秒。<br/>[闪影击]:所有速度 +{0}%"
    lv_params = [[4], [5], [6], [6.5], [7]]
    cost = [50, 50, 55, 45, 45]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        if lv > 0:
            char.所有速度增加(lv_params[lv-1][0]/100, '特性')
        pass
    if mode == 1:
        pass

# 猛攻系 - [破竹之势]
def entry_20103(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "[闪影击]状态下，施放技能时{0}，技能伤害 +{1}%，效果持续10秒。"
    lv_params = [['，解除所有[速攻]效果', 3], ['，解除所有[速攻]效果', 4], ['', 5]]
    cost = [60, 50, 50]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        if lv > 0:
            char.技能攻击力加成(lv_params[lv-1][1]/100)
        pass
    if mode == 1:
        pass

# 猛攻系 - [强袭：破击]
def entry_20104(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "施放技能时，进入[破击]状态5秒。<br/>[破击]：物理/魔法所受伤害 -{0}%"
    lv_params = [[1], [2], [3], [3.5], [4]]
    cost = [40, 40, 45, 45, 45]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 猛攻系 - [强袭：强腕击]
def entry_20105(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "[破击]状态下，施放技能时，进入[强腕击]状态5秒。<br/>[强腕击]：物理/魔法所受伤害 -{0}%"
    lv_params = [[1], [2], [3], [3.5], [4]]
    cost = [45, 45, 50, 40, 40]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 猛攻系 - [强袭：泰山击]
def entry_20106(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "[强腕击]状态下，施放技能时，进入[泰山击]状态5秒。<br/>[泰山击]：物理/魔法所受伤害 -{0}%"
    lv_params = [[1], [2], [3], [3.5], [4]]
    cost = [50, 50, 55, 45, 45]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 猛攻系 - [英雄豪杰]
def entry_20107(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "[泰山击]状态下，施放技能时{0}，技能伤害 +{1}%，并进入霸体状态，效果持续10秒。"
    lv_params = [['，解除所有[强袭]效果', 3], ['，解除所有[强袭]效果', 4], ['', 5]]
    cost = [60, 50, 50]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        if lv > 0:
            char.技能攻击力加成(lv_params[lv-1][1]/100)
        pass
    if mode == 1:
        pass

# 猛攻系 - [强力一击]
def entry_20108(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "技能伤害 +{0}%"
    lv_params = [[10], [16], [22], [28], [35]]
    cost = [96, 96, 96, 96, 96]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
            char.技能攻击力加成(lv_params[lv-1][0]/100)
            if char.实际名称 == 'crusader_male':
                char.get_skill_by_name('生命源泉').CDR *= 0.5
        pass
    if mode == 1:
        pass

# 猛攻系 - [冥想]
def entry_20109(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "技能冷却时间 -{0}%"
    lv_params = [[10], [20]]
    cost = [96, 96]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
            char.技能冷却缩减(1, 100, lv_params[lv-1][0]/100, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass

# 保护系 - [保护罩填充]
def entry_20200(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "施放技能时，赋予生命值最大值3%的保护罩。 (冷却时间3秒；最多叠加{0}次)"
    lv_params = [[1], [2], [3], [4], [5]]
    cost = [30, 30, 30, 30, 30]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        if lv > 0:
            char.set_eq_params('protect', char.get_eq_params(
                'protect') + 0.03 * lv_params[lv-1][0])
        pass
    if mode == 1:
        pass

# 保护系 - [护盾爆裂 - 爆炸]
def entry_20201(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "保护罩解除时，引发爆炸，攻击周围敌人。<br/>- 爆炸伤害量：{0}%"
    lv_params = [[152], [304], [456], [912], [1521]]
    cost = [15, 15, 15, 15, 15]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 保护系 - [火盾]
def entry_20202(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "生成火焰，对触碰到保护罩的敌人造成伤害。 (冷却时间0.3秒)<br/>- 火焰伤害量：{0}%"
    lv_params = [[101], [203], [304], [608], [1014], [1217], [1521]]
    cost = [25, 25, 25, 25, 25, 40, 40]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 保护系 - [背水一战]
def entry_20203(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "解除觉醒技能关联。<br/>50级技能冷却时间 -50%<br/>50级技能攻击力 +{0}%<br/>50级增益技能效果 -70% (仅限辅助职业)"
    lv_params = [[0], [10], [15], [25], [30]]
    cost = [100, 60, 60, 70, 70]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        if lv > 0:
            char.技能冷却缩减(50, 50, 0.5)
            char.技能倍率加成(50,50,lv_params[lv-1][0]/100)
            if char.类型 == '辅助':
                char.辅助属性加成(觉醒百分比力智Total=-0.7)
        pass
    if mode == 1:
        pass

# 保护系 - [保护罩续充]
def entry_20204(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "装备的填充型保护罩的填充冷却时间 -1秒"
    lv_params = [[]]
    cost = [30]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 保护系 - [护盾爆裂 - 恢复]
def entry_20205(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "保护罩解除时，周围300px范围内的队员恢复{0}%的生命值和魔法值。"
    lv_params = [[1], [1.5], [2], [2.5], [3]]
    cost = [15, 15, 15, 15, 15]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 保护系 - [水盾]
def entry_20206(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "保护罩周围{0}px内队友的生命值/魔法值恢复{1}%。 (冷却时间3秒)<br/><br/>技能伤害 +{2}%"
    lv_params = [[100, 0.2, 0], [150, 0.3, 0], [200, 0.5, 0], [250, 0.7, 0], [300, 1, 0], [300, 1, 0.5], [300, 1, 1]]
    cost = [25, 25, 25, 25, 25, 40, 40]
    if mode == 0:
        if lv > 0:
            char.技能攻击力加成(lv_params[lv-1][2]/100)
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 保护系 - [披靡庇护]
def entry_20207(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "100级技能攻击力 +{0}%<br/>施放100级技能后，进入无敌状态一段时间。"
    lv_params = [[15], [17], [20], [22], [25]]
    cost = [100, 60, 60, 70, 70]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        if lv > 0:
            char.技能倍率加成(100, 100, lv_params[lv-1][0]/100)
        pass
    if mode == 1:
        pass

# 保护系 - [强力一击]
def entry_20208(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "技能伤害 +{0}%"
    lv_params = [[10], [16], [22], [28], [35]]
    cost = [96, 96, 96, 96, 96]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
            char.技能攻击力加成(lv_params[lv-1][0]/100)
            if char.实际名称 == 'crusader_male':
                char.get_skill_by_name('生命源泉').CDR *= 0.5
        pass
    if mode == 1:
        pass

# 保护系 - [冥想]
def entry_20209(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "技能冷却时间 -{0}%"
    lv_params = [[10], [20]]
    cost = [96, 96]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
            char.技能冷却缩减(1, 100, lv_params[lv-1][0]/100, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass

# 具现系 - [灵药炼制]
def entry_20300(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "每{0}秒炼制一~四等灵药<br/>- 腕力灵药：技能伤害 +1/2/4/5%，效果持续20秒。<br/>- 铁壁灵药：物理/魔法所受伤害 -4/7/10/15%，效果持续20秒。<br/>- 神速灵药：所有速度 +5/10/15/20%，效果持续20秒。"
    lv_params = [[30], [28], [26], [23], [20], [18], [15]]
    cost = [20, 20, 20, 20, 20, 50, 50]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 具现系 - [力量精通]
def entry_20301(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "拾取灵药时，技能伤害 +{0}%，效果持续{1}秒。"
    lv_params = [[1, 5], [1, 10], [1, 13], [1, 16], [1, 20], [1.5, 25], [2, 25]]
    cost = [20, 20, 20, 20, 20, 40, 40]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 具现系 - [强化 - 力量精通]
def entry_20302(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "拾取灵药时，所有速度 +5%，效果持续{0}秒。"
    lv_params = [[5], [10], [13], [16], [20], [22], [25]]
    cost = [30, 30, 30, 30, 30, 50, 50]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 具现系 - [传说再现 - 破坏]
def entry_20303(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "高度成熟的炼制术有时会产生意想不到的效果。<br/>- 有{0}%的几率生成武具，而非灵药。<br/>{1}"
    lv_params = [[1, ''], [2, ''], [3, ''], [5, ''], [10, ''], [10, '<br/>增强武具的效果。'], [10, '<br/>增强武具的效果。']]
    cost = [30, 30, 30, 20, 20, 30, 30]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 具现系 - [高效炼制]
def entry_20304(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "炼制时，有{0}%的几率，额外炼成1个灵药。"
    lv_params = [[10], [12], [24], [26], [28], [30], [32], [34], [37], [40]]
    cost = [20, 20, 20, 20, 20, 40, 40, 50, 50, 60]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 具现系 - [精巧收尾]
def entry_20305(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "炼制时不会生成四等灵药。"
    lv_params = [[]]
    cost = [80]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 具现系 - [完美炼制]
def entry_20306(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "炼制时不会生成三等灵药。"
    lv_params = [[]]
    cost = [100]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 具现系 - [一级炼制术士]
def entry_20307(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "炼制时不会生成二等灵药。"
    lv_params = [[]]
    cost = [100]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 具现系 - [治愈精通]
def entry_20308(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "拾取灵药时，恢复{0}%的生命值和魔法值。"
    lv_params = [[2], [3], [4], [5], [7], [8], [10]]
    cost = [20, 20, 20, 20, 20, 40, 40]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 具现系 - [强化 - 治愈精通]
def entry_20309(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "拾取灵药时，进入霸体状态{0}秒，进入无敌状态{1}秒。"
    lv_params = [[5, 0], [10, 0], [13, 0], [16, 0], [20, 0], [20, 0.2], [20, 0.5]]
    cost = [30, 30, 30, 30, 30, 50, 50]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 具现系 - [传说再现 - 守护]
def entry_20310(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "高度成熟的炼制术有时会重现传说。<br/>- 有{0}%的几率生成武具，而非灵药。<br/>{1}"
    lv_params = [[1, ''], [2, ''], [3, ''], [5, ''], [10, ''], [10, '<br/>增强武具的效果。'], [10, '<br/>增强武具的效果。']]
    cost = [30, 30, 30, 20, 20, 30, 30]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
        pass
    if mode == 1:
        pass

# 具现系 - [强力一击]
def entry_20311(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "技能伤害 +{0}%"
    lv_params = [[10], [16], [22], [28], [35]]
    cost = [96, 96, 96, 96, 96]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
            char.技能攻击力加成(lv_params[lv-1][0]/100)
            if char.实际名称 == 'crusader_male':
                char.get_skill_by_name('生命源泉').CDR *= 0.5
        pass
    if mode == 1:
        pass

# 具现系 - [冥想]
def entry_20312(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return "技能冷却时间 -{0}%"
    lv_params = [[10], [20]]
    cost = [96, 96]
    if mode == 0:
        if lv > 0:
            char.辅助属性加成(buff量=7.2*reduce(lambda x, y: x+y, cost[:lv]))
            char.技能冷却缩减(1, 100, lv_params[lv-1][0]/100, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass