from core.basic.property import CharacterProperty
from core.equipment.property import 成长词条计算
import core.equipment.entry_0.params as pa


def entry_1873(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '@[五感之幻景]@', '融合装备的强化/增幅从10开始每增加1，技能伤害+1%（最多叠加2次）', '攻击速度+5%', '施放速度+7.5%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        x = char.获取强化等级(['项链'])
        if x > 10:
            char.技能攻击力加成(x=0.01 * min(2, x-10))
        pass
    if mode == 1:
        pass

def entry_3000(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.攻击速度增加(params[lv][0]/100)
        char.施放速度增加(params[lv][1]/100)
        pass
    if mode == 1:
        pass


def entry_1874(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '所有属性强化 +35', '', '@[怨恨之寒气]@', '生成冰龙，对敌人造成伤害，并使其进入冰冻状态', '- 冰龙伤害600%', '攻击时给予敌人5秒冰冻状态（冷却时间2秒）']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        char.所有属性强化加成(35)
        pass
    if mode == 1:
        pass

def entry_3002(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        if '冰冻' not in pa.get_state_type():
            pa.state_type.append('冰冻')
            char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],params[lv][0])
        pass
    if mode == 1:
        pass


def entry_1875(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['@[时光倒流者]@', '施放技能时有10%几率使该技能冷却时间初始化（觉醒技能除外）', '- 可连续初始化相同技能']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1876(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4% ', '', '50,85,100级技能攻击力 +11%', '50,85,100级技能冷却恢复速度 +15%（辅助职业不适用）']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        for i in [50,85,100]:
            char.技能倍率加成(i,i,0.11)
            if not (char.类型 == "辅助" or char.bufferCarry):
                char.技能恢复加成(i,i,0.15)
        pass
    if mode == 1:
        pass

def entry_1877(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10% ', '', '@[镜甲]@', '被击中时适用以下效果', '- 在3秒内恢复所受伤害的30%（冷却时间3秒）', '- 对敌人造成反击伤害', '  * 反击伤害15000%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1878(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11.5% ']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1879(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11% ', '', '@[灵魂吸收]@', '每15秒吸收灵魂', '- 魔法值恢复15%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_1880(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间 -7% ', '所有属性强化 +7', '', '@[红兔的礼物]@', '施放技能时有7.77%几率使该技能攻击力+77%']
    if mode == 0:
        char.技能冷却缩减(1,100,0.07,excName=char.觉醒技能)
        char.所有属性强化加成(7)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_1881(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '@[五感之幻景]@', '融合装备的强化/增幅从10开始每增加1，技能伤害+1%（最多叠加2次）', '移动速度+5%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        x = char.获取强化等级(['戒指'])
        if x > 10:
            char.技能攻击力加成(x=0.01 * min(2, x-10))
        pass
    if mode == 1:
        pass

def entry_3016(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.移动速度增加(params[lv][0]/100)
        pass
    if mode == 1:
        pass

def entry_1882(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '所有属性强化 +35', '', '@[愤怒之寒气]@', '生成冰龙，对敌人造成伤害，并使其进入冰冻状态', '- 冰龙伤害600%', '攻击时给予敌人5秒冰冻状态（冷却时间2秒）']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        char.所有属性强化加成(35)
        pass
    if mode == 1:
        pass

def entry_3018(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        if '冰冻' not in pa.get_state_type():
            pa.state_type.append('冰冻')
            char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],params[lv][0])
        pass
    if mode == 1:
        pass

def entry_1883(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10% ', '', '@[流淌的回忆]@', '施放技能时有1%的几率初始化1个技能冷却时间（辅助职业不适用）']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_1884(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4% ', '', '50,85,100级技能攻击力 +11%', '50,85,100级技能冷却恢复速度+15%（辅助职业不适用）']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        for i in [50,85,100]:
            char.技能倍率加成(i,i,0.11)
            if not (char.类型 == "辅助" or char.bufferCarry):
                char.技能恢复加成(i,i,0.15)
        pass
    if mode == 1:
        pass


def entry_1885(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['@[聚焦在我身上！]@', '- 技能伤害 +5%', '- 技能冷却时间 -10%（觉醒技能除外）', '- 获得霸体护甲', '- 生成聚光灯']
    if mode == 0:
        char.技能攻击力加成(params[lv][1]/100)
        char.辅助属性加成(buff量=params[lv][0])
        char.技能冷却缩减(1,100,0.1,excName=char.觉醒技能)
        pass
    if mode == 1:
        pass

def entry_1886(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['@[铲除异端]@', '将敌人定义为异端', '攻击异端时，技能伤害+11.5%']
    if mode == 0:
        char.技能攻击力加成(params[lv][1]/100)
        char.辅助属性加成(buff量=params[lv][0])
        pass
    if mode == 1:
        pass

def entry_3026(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        pass
    if mode == 1:
        pass

def entry_3027(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        pass
    if mode == 1:
        pass

def entry_1887(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8% ', '', '@[团结的灵魂]@', '聊天输入“团结”时，消耗1个金色小晶块，应用“团结的灵魂”(冷却30秒)', '- 无敌2秒，期间无法行动']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_1888(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9% ', '', '500px内队友所受物理/魔法伤害减少量+15%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1889(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9% ', ' ', ' 技能魔法值消耗量+100%', '每秒恢复2%的魔法值']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        char.MP消耗量加成(1)
        pass
    if mode == 1:
        pass

def entry_1890(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4% ', ' ', '50,85,100级技能攻击力 +8%', '50,85,100级技能冷却时间恢复速度+15%(辅助职业除外)']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        for i in [50,85,100]:
            char.技能倍率加成(i,i,0.08)
            if not (char.类型 == "辅助" or char.bufferCarry):
                char.技能恢复加成(i,i,0.15)
        pass
    if mode == 1:
        pass

def entry_1891(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9% ', ' ', '技能范围 +23%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_3036(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+params[lv][0]/100)
        char.multiply_eq_params('skill_range_multi',1+params[lv][0]/100)
        pass
    if mode == 1:
        pass

def entry_1892(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9% ', ' ', '技能魔法值消耗量-30%', '攻击时有5%的概率触发，30秒内适用“召唤:记录的神兽”(冷却时间30秒)', '- 造成总攻击强化数值600%的伤害']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_3039(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.MP消耗量加成(-params[lv][0]/100)
        pass
    if mode == 1:
        pass

def entry_1893(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9% ', ' ', '移动速度+15%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_3040(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.移动速度增加(params[lv][0]/100)
        pass
    if mode == 1:
        pass


def entry_1894(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7% ', ' ', '敌人剩余HP少于50%时, 技能伤害+4%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_3042(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.移动速度增加(params[lv][0]/100)
        pass
    if mode == 1:
        pass

def entry_1895(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5% ', ' ', '攻击时触发地爆。(冷却时间2秒)', ' -造成相当于总攻击力增加数值1200%的伤害']
    if mode == 0:
        char.攻击强化加成(1200.0)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_3045(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.移动速度增加(params[lv][0]/100)
        pass
    if mode == 1:
        pass


def entry_1896(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4% ', ' ', '50,85,100级技能攻击力+8%', '50,85,100级技能冷却时间恢复速度+15%(辅助职业除外)']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        for i in [50,85,100]:
            char.技能倍率加成(i,i,0.08)
            if not (char.类型 == "辅助" or char.bufferCarry):
                char.技能恢复加成(i,i,0.15)
        pass
    if mode == 1:
        pass


def entry_1897(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9% ', ' ', '生命值、魔法值上限+2000']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_3048(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.所有速度增加(params[lv][0]/100)
        pass
    if mode == 1:
        pass


def entry_1898(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间-15%(不包含觉醒)', '施放技能时有8%的概率给自己施加等级10的[圣光守护]']
    if mode == 0:
        char.技能冷却缩减(1,100,0.15,excName=char.觉醒技能)
        char.技能攻击力加成(params[lv][0]/100)
        char.攻击强化加成(500.0)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1899(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '', '移动速度 +10%', '每分钟回复920.4生命值']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_3052(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.移动速度增加(params[lv][0]/100)
        pass
    if mode == 1:
        pass


def entry_1900(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '', '攻击时向敌人施放冰锥。(冷却时间3秒，造成相当于总攻击强化数值1800%的伤害)', '攻击时，使敌人进入5秒的冰冻状态(冷却时间2秒)']
    if mode == 0:
        char.攻击强化加成(1200.0)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_3055(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        if '冰冻' not in pa.get_state_type():
            pa.state_type.append('冰冻')
            char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],params[lv][0])
        pass
    if mode == 1:
        pass


def entry_1901(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间 -18%(觉醒技能除外)', '所有属性抗性 +5']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        char.技能冷却缩减(1,100,0.18,excName=char.觉醒技能)

        pass
    if mode == 1:
        pass

def entry_3056(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.所有属性抗性加成(params[lv][0])
    if mode == 1:
        pass

def entry_1902(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '', '50,85,100级技能攻击力 +8%', '50,85,100级技能冷却时间恢复速度 +15%(辅助职业除外)']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        for i in [50,85,100]:
            char.技能倍率加成(i,i,0.08)
            if not (char.类型 == "辅助" or char.bufferCarry):
                char.技能恢复加成(i,i,0.15)
        pass
    if mode == 1:
        pass


def entry_1903(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '', '所有速度+5% ', '所受物理/魔法伤害减少值 +25%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1904(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '', '所有属性抗性+25']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        char.所有属性抗性加成(25)
        pass
    if mode == 1:
        pass

def entry_3062(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.所有属性抗性加成(params[lv][0])
    if mode == 1:
        pass

def entry_3063(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.移动速度增加(params[lv][0]/100)
    if mode == 1:
        pass

def entry_1905(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '技能范围 +7%', '生命值最大值 +5% ']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_3064(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+params[lv][0]/100)
        char.multiply_eq_params('skill_range_multi',1+params[lv][0]/100)
    if mode == 1:
        pass

def entry_1906(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '物理/魔法暴击率 +5%', ' 回避率+20%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1907(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '@[千钧一发]@', '技能命中时，有1%概率增加技能攻击力1000%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1908(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['85级技能攻击力增加30%', '85级技能冷却恢复速度增加100%（BUFF增益技能除外）']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        char.技能倍率加成(85,85,0.3)
        char.技能恢复加成(85,85,1)
        pass
    if mode == 1:
        pass

def entry_3071(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.移动速度增加(params[lv][0]/100)
    if mode == 1:
        pass

def entry_1909(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '@[契约爆发 - 灼烧/感电]@', '施加灼烧/感电状态时，一次性结算与该状态相同的异常状态伤害', '- 通过转换属性施加状态时不适用']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        char.set_eq_params('灼伤-结算', 1.0)
        char.set_eq_params('感电-结算', 1.0)
        pass
    if mode == 1:
        pass

def entry_3073(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.移动速度增加(params[lv][0]/100)
    if mode == 1:
        pass

def entry_1910(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '', '攻击时施加必中一击。（冷却时间2秒）', '- 伤害量为总攻击强化的1200%', '攻击时赋予5秒的束缚状态（冷却时间2秒）']
    if mode == 0:
        char.攻击强化加成( 1200.0)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_3075(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        if '束缚' not in pa.get_state_type():
            pa.state_type.append('束缚')
    if mode == 1:
        pass

def entry_1911(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '5秒内生成生命值最大值10%的保护罩（冷却时间5秒）']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_3076(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.set_eq_params('protect',char.get_eq_params('protect') + params[lv][0]/100)
    if mode == 1:
        pass

def entry_1912(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '攻击时， 赋予火、冰、光、暗攻击属性（冷却时间5秒）']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_3079(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.移动速度增加(params[lv][0]/100)
    if mode == 1:
        pass

def entry_1913(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '', '死亡时1秒内发动永生咒术（冷却时间120秒）', '- 立即恢复1%生命值', '- 其他HP恢复效果及伤害无效', '生命值最大值 +1000', '魔法值最大值 +1000']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1914(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '恢复魔法值消耗量的20%的生命值']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1915(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '@[契约爆发 - 出血/中毒]@', '施加出血/中毒状态时，一次性结算与该状态相同的异常状态伤害', '- 通过转换属性施加状态时不适用']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        char.set_eq_params('出血-结算', 1.0)
        char.set_eq_params('中毒-结算', 1.0)
        pass
    if mode == 1:
        pass

def entry_3085(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.移动速度增加(params[lv][0]/100)
    if mode == 1:
        pass

def entry_1916(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '', '攻击时施加元素爆炸。（冷却时间2秒）', '- 伤害量为总攻击强化的600%', '攻击时赋予5秒的眩晕状态（冷却时间2秒）']
    if mode == 0:
        char.攻击强化加成(1200.0)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_3087(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        if '眩晕' not in pa.get_state_type():
            pa.state_type.append('眩晕')
    if mode == 1:
        pass

def entry_1917(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '移动速度+20%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_3088(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.移动速度增加(params[lv][0]/100)
    if mode == 1:
        pass

def entry_1918(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '魔法/物理暴击率 +5%', '魔法/物理所受伤害减少量 +20%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1919(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '赋予霸体效果', '所有速度 +8%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_3092(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.移动速度增加(params[lv][0]/100)
    if mode == 1:
        pass


def entry_3093(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        for i in ['出血', '灼伤', '中毒', '感电']:
            if i not in pa.get_state_type():
                pa.state_type.append(i)
            char.异常时间[i][3] = min(char.异常时间[i][3],params[lv][0])
    if mode == 1:
        pass

def entry_1920(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '技能范围 +7%', ' 物理/魔法防御力 +10000']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_3094(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+params[lv][0]/100)
        char.multiply_eq_params('skill_range_multi',1+params[lv][0]/100)
    if mode == 1:
        pass

def entry_1921(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '命中率 +10%', '所有异常状态抗性 +5%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_3096(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        char.所有异常抗性加成(params[lv][0]/100)
    if mode == 1:
        pass

def entry_1922(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '', '攻击时施加时空斩。(冷却时间2秒)', ' - 伤害为总攻击强化的1800%', '攻击时赋予5秒的冰冻状态（冷却时间2秒）']
    if mode == 0:
        char.攻击强化加成(1200)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass

def entry_3099(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return []
    if mode == 0:
        if '冰冻' not in pa.get_state_type():
            pa.state_type.append('冰冻')
            char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],params[lv][0])
        pass
    if mode == 1:
        pass


def entry_1923(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +1%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1924(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1925(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1926(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%']
    if mode == 0:
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1927(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +350.0%']
    if mode == 0:
        char.攻击强化加成(350)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1928(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +700.0%']
    if mode == 0:
        char.攻击强化加成(700)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1929(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +1050.0%']
    if mode == 0:
        char.攻击强化加成(1050)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1930(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +1400.0%']
    if mode == 0:
        char.攻击强化加成(1400)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1931(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +6']
    if mode == 0:
        char.所有属性强化加成(6)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1932(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +10']
    if mode == 0:
        char.所有属性强化加成(10)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1933(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +14']
    if mode == 0:
        char.所有属性强化加成(14)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1934(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +18']
    if mode == 0:
        char.所有属性强化加成(18)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1935(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性强化 +8']
    if mode == 0:
        char.所有属性强化加成(火属性强化=8)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1936(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性强化 +12']
    if mode == 0:
        char.所有属性强化加成(火属性强化=12)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1937(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性强化 +16']
    if mode == 0:
        char.所有属性强化加成(火属性强化=16)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1938(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性强化 +20']
    if mode == 0:
        char.所有属性强化加成(火属性强化=20)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1939(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冰属性强化 +8']
    if mode == 0:
        char.所有属性强化加成(冰属性强化=8)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1940(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冰属性强化 +12']
    if mode == 0:
        char.所有属性强化加成(冰属性强化=12)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1941(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冰属性强化 +16']
    if mode == 0:
        char.所有属性强化加成(冰属性强化=16)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1942(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冰属性强化 +20']
    if mode == 0:
        char.所有属性强化加成(冰属性强化=20)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1943(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['光属性强化 +8']
    if mode == 0:
        char.所有属性强化加成(光属性强化=8)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1944(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['光属性强化 +12']
    if mode == 0:
        char.所有属性强化加成(光属性强化=12)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1945(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['光属性强化 +16']
    if mode == 0:
        char.所有属性强化加成(光属性强化=16)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1946(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['光属性强化 +20']
    if mode == 0:
        char.所有属性强化加成(光属性强化=20)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1947(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暗属性强化 +8']
    if mode == 0:
        char.所有属性强化加成(暗属性强化=8)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1948(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暗属性强化 +12']
    if mode == 0:
        char.所有属性强化加成(暗属性强化=12)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1949(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暗属性强化 +16']
    if mode == 0:
        char.所有属性强化加成(暗属性强化=16)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1950(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暗属性强化 +20']
    if mode == 0:
        char.所有属性强化加成(暗属性强化=20)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1951(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能范围 +8%']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.08)
        char.multiply_eq_params('skill_range_multi',1.08)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1952(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能范围 +12%']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.12)
        char.multiply_eq_params('skill_range_multi',1.12)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1953(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能范围 +16%']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.16)
        char.multiply_eq_params('skill_range_multi',1.16)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1954(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能范围 +20%']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.2)
        char.multiply_eq_params('skill_range_multi',1.2)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1955(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性抗性 +8']
    if mode == 0:
        char.所有属性抗性加成(8)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1956(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性抗性 +12']
    if mode == 0:
        char.所有属性抗性加成(12)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1957(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性抗性 +16']
    if mode == 0:
        char.所有属性抗性加成(16)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1958(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性抗性 +20']
    if mode == 0:
        char.所有属性抗性加成(20)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1959(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有速度 +3%']
    if mode == 0:
        char.所有速度增加(0.03)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1960(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有速度 +6%']
    if mode == 0:
        char.所有速度增加(0.06)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1961(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有速度 +9%']
    if mode == 0:
        char.所有速度增加(0.09)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1962(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有速度 +12%']
    if mode == 0:
        char.所有速度增加(0.12)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1963(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['增益量 750']
    if mode == 0:
        char.辅助属性加成(buff量=750)
        if char.bufferCarry:
            char.技能攻击力加成(0.01)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1964(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['增益量 900']
    if mode == 0:
        char.辅助属性加成(buff量=900)
        if char.bufferCarry:
            char.技能攻击力加成(0.02)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1965(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['增益量 1050']
    if mode == 0:
        char.辅助属性加成(buff量=1050)
        if char.bufferCarry:
            char.技能攻击力加成(0.03)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass


def entry_1966(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['增益量 1200']
    if mode == 0:
        char.辅助属性加成(buff量=1200)
        if char.bufferCarry:
            char.技能攻击力加成(0.04)
        char.技能攻击力加成(params[lv][0]/100)
        char.辅助属性加成(buff量=params[lv][1])
        pass
    if mode == 1:
        pass