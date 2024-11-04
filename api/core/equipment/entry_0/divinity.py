from core.basic.property import CharacterProperty
from core.equipment.property import 成长词条计算
import core.equipment.entry_0.params as pa

# 自定义装备：领域之主 - 上衣 ， 海湾侠踪衬衫
def entry_1572(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +192.7%', '攻击时，敌人韧性条 -1 (冷却时间1秒)']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(params[0])
        pass


# 自定义装备：领域之主 - 上衣 ， 海湾侠踪衬衫
def entry_1573(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['不消耗无色小晶块的技能攻击力 +10%', '物理/魔法防御力 +5000']
    if mode == 0:
        char.add_eq_params('defense',5000)
        pass
    if mode == 1:
        char.无色技能加成(0,0.1)
        pass


# 自定义装备：领域之主 - 上衣 ， 海湾侠踪衬衫
def entry_1574(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间 -10% (觉醒技能除外)', '- 需要穿戴[超界次元]或拥有"所有特性技能等级 +1"属性']
    if mode == 0:
        pass
    if mode == 1:
        if char.get_eq_params('tp') > 0 or char.check_equ_by_name('超界次元'):
            char.技能冷却缩减(1, 100, 0.1, excName=char.觉醒技能)
        else:
            return '未获得特性技能等级增加效果'
        pass


# 自定义装备：领域之主 - 上衣 ， 海湾侠踪衬衫
def entry_1575(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +444.6%', '物理/魔法防御力 +5000']
    if mode == 0:
        char.add_eq_params('defense',5000)
        pass
    if mode == 1:
        char.攻击强化加成(params[0])
        pass


# 自定义装备：领域之主 - 上衣 ， 海湾侠踪衬衫
def entry_1576(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +296.4%']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(params[0])
        pass


# 自定义装备：领域之主 - 上衣 ， 海湾侠踪衬衫
def entry_1577(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +15', '所有速度 +10%']
    if mode == 0:
        char.所有属性强化加成(15)
        char.所有速度增加(part=part, x=0.1)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 下装 ， 海湾侠踪长裤
def entry_1578(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['自身当前每适用1种异常状态，技能伤害 +2% (最多叠加4次)']
    if mode == 0:
        pass
    if mode == 1:
        num = len(list(filter(lambda i: i not in ['石化', '睡眠', '眩晕', '冰冻', ''], pa.own_type)) + ((['石化'] if '石化' in pa.own_type and 1537 in char.装备栏 else [] + ['睡眠'] if '睡眠' in pa.own_type and (1684 in char.装备栏 or 295 in char.装备栏) else []) if char.check_fun_by_id(1625) else []))
        for i in range(0, min(num, 4)):
            char.技能攻击力加成(part=part, x=0.02)
        if num < 4:
            return '自身异常状态缺少{}种'.format(4 - num)
        pass


# 自定义装备：领域之主 - 下装 ， 海湾侠踪长裤
def entry_1579(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放技能消耗15个以上无色小晶块时，技能伤害 +6%，效果持续30秒。', '所有速度 +10%']
    if mode == 0:
        char.所有速度增加(0.1, part)
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        pass


# 自定义装备：领域之主 - 下装 ， 海湾侠踪长裤
def entry_1580(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(params[0])
        pass


# 自定义装备：领域之主 - 下装 ， 海湾侠踪长裤
def entry_1581(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤伤害 +20%', '灼伤抗性 +5%']
    if mode == 0:
        char.异常增伤('灼伤', 0.2)
        char.异常抗性加成('灼伤',0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 下装 ， 海湾侠踪长裤
def entry_1582(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['50、85、100级技能攻击力 +8%']
    if mode == 0:
        char.技能倍率加成(50, 50, 0.08)
        char.技能倍率加成(85, 85, 0.08)
        char.技能倍率加成(100, 100, 0.08)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 下装 ， 海湾侠踪长裤
def entry_1583(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%', '所有异常状态抗性 +10%']
    if mode == 0:
        char.所有异常抗性加成(0.1)
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 头肩 ， 海湾侠踪护肩
def entry_1584(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.06)
        pass


# 自定义装备：领域之主 - 头肩 ， 海湾侠踪护肩
def entry_1585(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['出血伤害 +15%']
    if mode == 0:
        char.异常增伤('出血', 0.15)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 头肩 ， 海湾侠踪护肩
def entry_1586(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '技能冷却时间 -6% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.06, excName=char.觉醒技能)
        char.技能攻击力加成(0.02)
        pass


# 自定义装备：领域之主 - 头肩 ， 海湾侠踪护肩
def entry_1587(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '技能冷却时间 -4% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.04, excName=char.觉醒技能)
        char.技能攻击力加成(0.03)
        pass


# 自定义装备：领域之主 - 头肩 ， 海湾侠踪护肩
def entry_1588(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间 -16% (觉醒技能除外)', '- 需要穿戴[天才技术大师的加厚长靴]']
    if mode == 0:
        pass
    if mode == 1:
        if char.check_equ_by_name('天才技术大师的加厚长靴'):
            char.技能冷却缩减(1, 100, 0.16, excName=char.觉醒技能)
        else:
            return '未穿戴[天才技术大师的加厚长靴]'
        pass


# 自定义装备：领域之主 - 头肩 ， 海湾侠踪护肩
def entry_1589(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['消耗15个以上无色小晶块的技能攻击力 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.无色技能加成(15,0.1)
        pass


# 自定义装备：领域之主 - 腰带 ， 海湾侠踪腰带
def entry_1590(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '物理/魔法防御力 +4000']
    if mode == 0:
        char.技能攻击力加成(0.06)
        char.add_eq_params('defense',4000)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 腰带 ， 海湾侠踪腰带
def entry_1591(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '- 需要穿戴[永恒的心愿]', '睡眠抗性 -20%']
    if mode == 0:
        char.异常抗性加成('睡眠', -0.2)
        if char.check_equ_by_name('永恒的心愿'):
            char.技能攻击力加成(0.07)
        else:
            return '未穿戴[永恒的心愿]'
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 腰带 ， 海湾侠踪腰带
def entry_1592(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +444.6%', '- 需要穿戴[永恒的心愿]']
    if mode == 0:
        if char.check_equ_by_name('永恒的心愿'):
            char.攻击强化加成(params[0])
        else:
            return '未穿戴[永恒的心愿]'
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 腰带 ， 海湾侠踪腰带
def entry_1593(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['被攻击时，生成生命值最大值10%的保护罩，效果持续10秒。 (冷却时间10秒)']
    if mode == 0:
        char.set_eq_params('protect',char.get_eq_params('protect')+0.1)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 腰带 ， 海湾侠踪腰带
def entry_1594(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能范围 +15%']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.15)
        char.multiply_eq_params('skill_range_multi',1.15)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 腰带 ， 海湾侠踪腰带
def entry_1595(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间恢复速度 +15% (觉醒技除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.15, excName=char.觉醒技能)
        pass


# 自定义装备：领域之主 - 鞋 ， 海湾侠踪短靴
def entry_1596(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['感电伤害 +20%', '移动速度 +5%']
    if mode == 0:
        char.异常增伤('感电', 0.2)
        char.移动速度增加(0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 鞋 ， 海湾侠踪短靴
def entry_1597(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤-冰冻联接造成的灼伤伤害 +15%']
    if mode == 0:
        char.异常结算加成['灼伤破冰'] += 0.15
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 鞋 ， 海湾侠踪短靴
def entry_1598(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['不消耗无色小晶块的技能攻击力 +10%', '移动速度 +5%']
    if mode == 0:
        char.移动速度增加(0.05)
        pass
    if mode == 1:
        char.无色技能加成(0,0.1)
        pass


# 自定义装备：领域之主 - 鞋 ， 海湾侠踪短靴
def entry_1599(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤伤害 +20%', '@[酷寒一击]@', '将[冰冻打击]属性变更为技能伤害 +5%']
    if mode == 0:
        char.异常增伤('灼伤', 0.2)
        char.set_eq_params('ice_attack_rate', 1/3)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 鞋 ， 海湾侠踪短靴
def entry_1600(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%', '移动速度 +15%']
    if mode == 0:
        char.攻击强化加成(params[0])
        char.移动速度增加(0.15)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 鞋 ， 海湾侠踪短靴
def entry_1601(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间恢复速度 +15% (觉醒技除外)']
    if mode == 0:
        char.技能恢复加成(1, 100, 0.15, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 项链 ， 海湾侠踪项链
def entry_1602(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['@[傀儡一击]@', '将[石化打击]属性变更为技能伤害 +5%']
    if mode == 0:
        char.set_eq_params('stone_attack_rate', 1/3)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 项链 ， 海湾侠踪项链
def entry_1603(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '技能范围 +10%']
    if mode == 0:
        char.技能攻击力加成(0.04)
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.1)
        char.multiply_eq_params('skill_range_multi',1.1)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 项链 ， 海湾侠踪项链
def entry_1604(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤伤害 +15%', '灼伤抗性 +10%']
    if mode == 0:
        char.异常增伤('灼伤', 0.15)
        char.异常抗性加成('灼伤',0.1)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 项链 ， 海湾侠踪项链
def entry_1605(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +177.8%']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 项链 ， 海湾侠踪项链
def entry_1606(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +251.9%', '清除自身赋予敌人石化状态的物理/魔法所受伤害减少效果。']
    if mode == 0:
        char.攻击强化加成(params[0])
        char.移动速度增加(0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 项链 ， 海湾侠踪项链
def entry_1607(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '进入索利达斯 (高级)地下城时，技能伤害 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        if '[团结]' in pa.dungeons_type:
            char.技能攻击力加成(0.1)
        pass


# 自定义装备：领域之主 - 手镯 ， 海湾侠踪手镯
def entry_1608(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)
        pass


# 自定义装备：领域之主 - 手镯 ， 海湾侠踪手镯
def entry_1609(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['不消耗无色小晶块的1~35级技能攻击力 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.无色技能加成(0,0.1,1,35)
        pass


# 自定义装备：领域之主 - 手镯 ， 海湾侠踪手镯
def entry_1610(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +251.9%']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(params[0])
        pass


# 自定义装备：领域之主 - 手镯 ， 海湾侠踪手镯
def entry_1611(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间 -10% (觉醒技能除外)']
    if mode == 0:
        char.技能冷却缩减(1, 100, 0.1, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 手镯 ， 海湾侠踪手镯
def entry_1612(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.04)
        pass


# 自定义装备：领域之主 - 手镯 ， 海湾侠踪手镯
def entry_1613(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +251.9%', '物理/魔法伤害减少量 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(params[0])
        pass


# 自定义装备：领域之主 - 戒指 ， 海湾侠踪戒指
def entry_1614(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['消耗无色小晶块的技能技能伤害 +8%']
    if mode == 0:
        pass
    if mode == 1:
        char.无色技能加成(1,0.08)
        pass


# 自定义装备：领域之主 - 戒指 ， 海湾侠踪戒指
def entry_1615(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放50、85、100级技能时，有8%的几率增加88%的该技能攻击力']
    if mode == 0:
        pass
    if mode == 1:
        # char.技能倍率加成(50, 50, 0.88*0.08)
        # char.技能倍率加成(85, 85, 0.88*0.08)
        # char.技能倍率加成(100, 100, 0.88*0.08)
        pass


# 自定义装备：领域之主 - 戒指 ， 海湾侠踪戒指
def entry_1616(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '- 需要穿戴[告别过去的前进]']
    if mode == 0:
        if char.check_equ_by_name('告别过去的前进'):
            char.技能攻击力加成(0.04)
        else:
            return '未穿戴[告别过去的前进]'
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 戒指 ， 海湾侠踪戒指
def entry_1617(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['回避率 +4%', '辅助职业技能冷却时间恢复速度 +30% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        if char.类型 == "辅助":
            char.技能恢复加成(1,100,0.3, excName=char.觉醒技能)
        if char.bufferCarry:
            char.技能恢复加成(1,100,0.3, excName=char.觉醒技能)
        pass


# 自定义装备：领域之主 - 戒指 ， 海湾侠踪戒指
def entry_1618(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +25', '攻击时，恢复500点生命值。 (冷却时间1秒)']
    if mode == 0:
        char.所有属性强化加成(25)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 戒指 ， 海湾侠踪戒指
def entry_1619(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +25', '攻击时，恢复500点魔法值。 (冷却时间1秒)']
    if mode == 0:
        char.所有属性强化加成(25)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 辅助装备 ， 海湾侠踪保护器
def entry_1620(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '命中率 +8%']
    if mode == 0:
        char.技能攻击力加成(0.03)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 辅助装备 ， 海湾侠踪保护器
def entry_1621(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间恢复速度 +15% (觉醒技能除外)', '- 需穿戴[铭刻之誓约]']
    if mode == 0:
        if char.check_equ_by_name('铭刻之誓约'):
            char.技能恢复加成(1, 100, 0.15, excName=char.觉醒技能)
        else:
            return '未穿戴[铭刻之誓约]'
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 辅助装备 ， 海湾侠踪保护器
def entry_1622(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +251.9%', '命中率 +4%']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(params[0])
        pass


# 自定义装备：领域之主 - 辅助装备 ， 海湾侠踪保护器
def entry_1623(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +251.9%', '回避率 +4%']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(params[0])
        pass


# 自定义装备：领域之主 - 辅助装备 ， 海湾侠踪保护器
def entry_1624(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['中毒伤害 +12%']
    if mode == 0:
        char.异常增伤('中毒', 0.12)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 辅助装备 ， 海湾侠踪保护器
def entry_1625(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '回避率 +8%']
    if mode == 0:
        char.技能攻击力加成(0.03)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 魔法石 ， 海湾侠踪宝石
def entry_1626(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['装备发动的物体伤害 +10%']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 魔法石 ， 海湾侠踪宝石
def entry_1627(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['控制型异常状态、强控的韧性条减少量 +100%']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 魔法石 ， 海湾侠踪宝石
def entry_1628(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '被破招时，物理/魔法所受伤害 -5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        pass


# 自定义装备：领域之主 - 魔法石 ， 海湾侠踪宝石
def entry_1629(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['出血伤害 +15%', '移动速度 +5%']
    if mode == 0:
        char.异常增伤('出血', 0.15)
        char.移动速度增加(0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 魔法石 ， 海湾侠踪宝石
def entry_1630(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '被背击时，物理/魔法所受伤害 -5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        pass


# 自定义装备：领域之主 - 魔法石 ， 海湾侠踪宝石
def entry_1631(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '正面被攻击时，物理/魔法所受伤害 -5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        pass


# 自定义装备：领域之主 - 耳环 ， 海湾侠踪耳环
def entry_1632(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['用指令施放技能时，进入霸体状态30秒。']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 耳环 ， 海湾侠踪耳环
def entry_1633(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '- 需要穿戴[永恒的心愿]']
    if mode == 0:
        if char.check_equ_by_name('永恒的心愿'):
            char.技能攻击力加成(0.06)
        else:
            return '未穿戴[永恒的心愿]'
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 耳环 ， 海湾侠踪耳环
def entry_1634(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['按照装备、消耗品、生命值恢复技能提供的生命值恢复量的50%，恢复保护罩。', '- 持续恢复的技能除外。']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 耳环 ， 海湾侠踪耳环
def entry_1635(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +251.9%', '进入霸体护甲状态']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(params[0])
        pass


# 自定义装备：领域之主 - 耳环 ， 海湾侠踪耳环
def entry_1636(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '魔法值最大值 +300']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        pass


# 自定义装备：领域之主 - 耳环 ， 海湾侠踪耳环
def entry_1637(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '- 需要穿戴[超界次元]或拥有"所有特性技能等级 +1"属性', '75~100级技能攻击力 +6%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能倍率加成(75, 100, 0.06)
        if char.get_eq_params("tp") or char.check_equ_by_name('超界次元'):
            char.技能攻击力加成(0.06)
        else:
            return '未获得特性点等级增加效果'
        pass


# 固定装备：雾之意志追随者上衣
def entry_1638(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '韧性条减少量 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)
        pass


# 固定装备：雾之意志追随者下装
def entry_1640(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '强控的韧性条减少量 +200%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.08)
        pass


# 固定装备：虚蚀之神兽斗篷
def entry_1642(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%', '', '物理/魔法所受伤害 -10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.11)
        char.add_eq_params('hurted_ratio',0.1)
        pass


# 固定装备：雾之探索者腰带
def entry_1644(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +13%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.13)
        pass


# 固定装备：雾之意志追随者鞋
def entry_1646(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +13%', '韧性条减少量 +100%', '', '@[弱点攻略]@', '攻击韧性条低于90%的敌人时，赋予敌人的所有控制型异常状态均视为敌人的弱点。']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.13)
        pass


# 固定装备：雾之探索者项链
def entry_1648(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '攻击速度 +10%', '施放速度 +10%', '移动速度 +10%', '回避率 +20%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.09)
        char.所有速度增加(0.10)
        pass


# 固定装备：邪恶力量侵蚀手镯
def entry_1650(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +16%', '', '攻击领主/稀有怪物时，韧性条 -1% (辅助职业不适用)', '- 仅限于攻击韧性条高于90%以上的敌人时，适用该效果。']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.16)
        pass


# 固定装备：雾之探索者戒指
def entry_1652(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '技能冷却时间恢复速度增加30% (觉醒技能除外)', '', '移动速度 +15%']
    if mode == 0:
        char.技能恢复加成(1, 100, 0.3, excName=char.觉醒技能)
        char.技能攻击力加成(0.02)
        char.移动速度增加(0.15)
        pass
    if mode == 1:
        pass


# 固定装备：悲蚀之神兽面纱
def entry_1654(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%']
    if mode == 0:
        char.技能攻击力加成(0.09)
        pass
    if mode == 1:
        pass


# 固定装备：被侵蚀的高原之精髓
def entry_1656(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '攻击速度 +5%', '施放速度 +5%', '移动速度 +5%', '所有属性抗性 +10', '回避率 +8%']
    if mode == 0:
        char.技能攻击力加成(0.08)
        char.所有速度增加(0.05)
        char.所有属性抗性加成(10)
        pass
    if mode == 1:
        pass


# 固定装备：被侵蚀的神兽之泪
def entry_1658(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%', '', '攻击速度 +5%', '施放速度 +5%', '移动速度 +5%', '所有异常状态抗性 +10%']
    if mode == 0:
        char.技能攻击力加成(0.12)
        char.所有异常抗性加成(0.1)
        char.所有速度增加(0.05)
        pass
    if mode == 1:
        pass


# 固定装备：守望溪谷的注视
def entry_1660(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '攻击速度 +10%', '施放速度 +10%', '移动速度 +10%']
    if mode == 0:
        char.技能攻击力加成(0.08)
        char.所有速度增加(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：守望溪谷的行动
def entry_1662(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '物理/魔法所受伤害 -10%']
    if mode == 0:
        char.add_eq_params('hurted_ratio',0.1)
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)
        pass


# 固定装备：守护晴烟的意志
def entry_1664(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +9%', '灼伤伤害 +10%', '', '灼伤持续时间 -20%']
    if mode == 0:
        char.异常增伤('灼伤', 0.1)
        char.异常时间['灼伤'][2] -= 0.2
        pass
    if mode == 1:
        char.技能攻击力加成(0.09)
        pass


# 固定装备：承诺誓约的腰带
def entry_1666(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '@[爆发契约 - 强化]@', '施加出血/中毒/灼伤/感电状态时，增加10%的相同异常状态伤害后一次性结算。', '- 通过转换属性施加状态时不适用', '', '物理/魔法所受伤害 -15%']
    if mode == 0:
        for i in ['感电','中毒','出血','灼伤']:
            char.异常结算加成[i] += 0.1
            char.set_eq_params(f'{i}-结算', 1.0)
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)
        char.add_eq_params('hurted_ratio',0.15)
        pass


# 固定装备：信守誓约的步伐
def entry_1668(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '@[酷寒一击]@', '将[冰冻打击]属性变更为技能伤害 +5%。', '', '删除装备[永眠前的准备]的@[灼伤冰冻]@冷却时间。', '', '灼伤持续时间 +4秒', '', '攻击普通怪物时，使所有敌人进入冰冻状态。 (冷却时间1秒)']
    if mode == 0:
        char.异常时间['灼伤'][1] += 4
        if '冰冻' not in pa.state_type:
            pa.state_type.append('冰冻')
            char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],1)
        char.技能攻击力加成(0.1)
        char.set_eq_params('ice_attack_rate', 1/3)
        pass
    if mode == 1:
        pass


# 固定装备：记录者的项链
def entry_1670(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%', '- 需穿戴[自由之缚手镯]装备。', '', '穿戴[死亡蚕食胸甲]时，狂暴状态持续时间上限 +5秒']
    if mode == 0:
        if char.check_equ_by_name('自由之缚手镯'):
            char.技能攻击力加成(0.11)
        else:
            return '未穿戴[自由之缚手镯]'
        pass
    if mode == 1:
        pass


# 固定装备：传令使的祝福
def entry_1672(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +18%', '', '物理/魔法防御力 +36000']
    if mode == 0:
        char.add_eq_params('defense',36000)
        pass
    if mode == 1:
        char.技能攻击力加成(0.18)
        pass


# 固定装备：守望者之证
def entry_1674(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '@[人偶剧]@', 'D011-Risa跟随角色。', '- 需穿戴[混乱核心胸甲]']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)
        pass


# 固定装备：守护晴烟之力
def entry_1676(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +251.9%', '所有属性强化 +15', '', '攻击时，发动1次迷雾雷。 (冷却时间1秒)', '- 有10%几率施放强化迷雾雷。', '- 迷雾雷和强化迷雾雷，分别造成总攻击强化数值1000%，1480%的伤害', '', '攻击速度 +10%', '施放速度 +10%', '移动速度 +10%']
    if mode == 0:
        char.所有速度增加(0.1)
        char.所有属性强化加成(15)
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 固定装备：记录者的宝石
def entry_1678(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%', '', '使用恢复型消耗品时，[填充型保护罩]开始自动填充。', '装备保护罩最大值 +20%']
    if mode == 0:
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.05*4)
        pass
    if mode == 1:
        char.技能攻击力加成(0.12)
        pass


# 固定装备：守望溪谷的标志
def entry_1680(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +14%', '1~70级技能范围 +15%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.14)
        pass


# 固定装备：想象力充沛的工程师衬衫
def entry_1682(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '', '施放技能期间，增加300%的移动速度。', '', '所有队员进入霸体状态。']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.08)
        pass


# 固定装备：想象力充沛的工程师长裤
def entry_1684(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)
        pass


# 固定装备：化虚为实之想象
def entry_1686(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%', '', '所有异常状态抗性 +30%']
    if mode == 0:
        char.所有异常抗性加成(0.3)
        pass
    if mode == 1:
        char.技能攻击力加成(0.11)
        pass


# 固定装备：想象力充沛的工程师工作腰带
def entry_1688(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +12%', '', '所有属性抗性 +15']
    if mode == 0:
        char.技能攻击力加成(0.12)
        char.所有属性抗性加成(15)
        pass
    if mode == 1:
        pass


# 固定装备：想象力充沛的工程师防护鞋
def entry_1690(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +19%', '', '物理/魔法所受伤害 -20%']
    if mode == 0:
        char.add_eq_params('hurted_ratio',0.2)
        pass
    if mode == 1:
        char.技能攻击力加成(0.19)
        pass


# 固定装备：机械工程学核心项链
def entry_1692(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '技能的魔法值恢复量 +200%']
    if mode == 0:
        char.技能攻击力加成(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：封存时空的手镯
def entry_1694(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +18%', '', '获得生命值最大值15%的@[填充型保护罩]@。']
    if mode == 0:
        char.技能攻击力加成(0.18)
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.15)
        pass
    if mode == 1:
        pass


# 固定装备：俯瞰夜色的工程师之眼
def entry_1696(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['50、85、100级技能攻击力 +20%', '50、85、100级技能冷却时间恢复速度 +40% (辅助职业除外)']
    if mode == 0:
        char.技能倍率加成(50,50,0.2)
        char.技能倍率加成(85,85,0.2)
        char.技能倍率加成(100,100,0.2)
        if char.类型 != '辅助':
            char.技能恢复加成(50, 50, 0.4)
            char.技能恢复加成(85, 85, 0.4)
            char.技能恢复加成(100, 100, 0.4)
        pass
    if mode == 1:
        pass


# 固定装备：查理的面具
def entry_1698(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 -35% (觉醒技能除外)', '技能冷却时间 -50% (觉醒技能除外)']
    if mode == 0:
        char.技能倍率加成(1, 100, -0.35, excName=char.觉醒技能)
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.5, excName=char.觉醒技能)
        pass


# 固定装备：机械工程学的精髓
def entry_1700(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +13%', '火/冰/光/暗攻击属性']
    if mode == 0:
        char.技能攻击力加成(0.13)
        pass
    if mode == 1:
        pass


# 固定装备：时间工程学的时刻
def entry_1702(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +14%', '', '物理/魔法所受伤害 -15%']
    if mode == 0:
        char.技能攻击力加成(0.14)
        char.add_eq_params('hurted_ratio',0.15)
        pass
    if mode == 1:
        pass


# 固定装备：勇敢骑士甲胄
def entry_1704(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '技能冷却时间恢复速度 +20% (觉醒技能除外)', '', '攻击速度 +10%', '施放速度 +10%', '移动速度 +10%']
    if mode == 0:
        char.技能攻击力加成(0.04)
        char.技能恢复加成(1, 100, 0.2, excName=char.觉醒技能)
        char.攻击速度增加(part=part, x=0.1)
        char.施放速度增加(0.1)
        char.移动速度增加(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：坚定骑士护腿
def entry_1706(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.1)
        pass


# 固定装备：坚忍骑士肩甲
def entry_1708(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '技能范围 +16%']
    if mode == 0:
        char.技能攻击力加成(0.1)
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.16)
        char.multiply_eq_params('skill_range_multi',1.16)
        pass
    if mode == 1:
        pass


# 固定装备：忠诚骑士腰带
def entry_1710(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +11%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.11)
        pass


# 固定装备：幻想骑士战靴
def entry_1712(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +22%', '- 需穿戴[魔力抑制手镯]装备。', '', '攻击时，恢复2500点魔法值。 (冷却时间1秒)']
    if mode == 0:
        if char.check_equ_by_name('魔力抑制手镯'):
            char.技能攻击力加成(0.22)
        else:
            return '未穿戴[魔力抑制手镯]'
    if mode == 1:
        pass


# 固定装备：对敌之慎重
def entry_1714(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '技能范围 +16%']
    if mode == 0:
        char.技能攻击力加成(0.1)
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.16)
        char.multiply_eq_params('skill_range_multi',1.16)
        pass
    if mode == 1:
        pass


# 固定装备：铭刻之誓约
def entry_1716(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +16.5%', '所有属性强化 +30']
    if mode == 0:
        char.技能攻击力加成(0.165)
        char.所有属性强化加成(30)
        pass
    if mode == 1:
        pass


# 固定装备：压倒性之勇猛
def entry_1718(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +10%', '', '@[审判时间]@', '输入↑↓ + [装备属性指令]时，审判领主怪物并累积伤害，效果持续10秒。 (冷却时间20秒)', '- 审判结束时，一次性结算累积的伤害', '- 再次按指令键时，解除审判', '- [审判时间]持续期间，所有速度 +75%']
    if mode == 0:
        pass
    if mode == 1:
        char.所有速度增加(x=0.75/2,part=part)
        char.技能攻击力加成(0.1)
        pass


# 固定装备：挺进之气势
def entry_1720(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间恢复速度 +15%', '技能范围 +16%']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.16)
        char.multiply_eq_params('skill_range_multi',1.16)
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.15, excName=char.觉醒技能)
        pass


# 固定装备：守护之坚忍
def entry_1722(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +13%']
    if mode == 0:
        char.技能攻击力加成(0.13)
        pass
    if mode == 1:
        pass


# 固定装备：永不放弃的勇气
def entry_1724(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +13%', '', '物理/魔法所受伤害 -10%']
    if mode == 0:
        char.add_eq_params('hurted_ratio',0.1)
        pass
    if mode == 1:
        char.技能攻击力加成(0.13)
        pass

