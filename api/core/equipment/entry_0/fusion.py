from core.basic.property import CharacterProperty
from core.equipment.property import 成长词条计算
import core.equipment.entry_0.params as pa

# 固定装备：火龙 : 爆炸的力之源
def entry_1283(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间 -4% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.04, excName=char.觉醒技能)
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.03)
            char.辅助属性加成(buff量=775)
        pass


# 固定装备：火龙 : 沸腾的龙之息
def entry_1284(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间 -4% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.04, excName=char.觉醒技能)
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.03)
            char.辅助属性加成(buff量=775)
        pass


# 固定装备：火龙 : 燃烧的火之怒
def entry_1285(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间 -4% (觉醒技能除外)', '', '[火龙之怒]', '用愤怒喷出的火焰包围自己，攻击强化 +130.2%', '- 需要装备3种火龙融合装备。']
    if mode == 0:
        pass
    if mode == 1:
        char.技能冷却缩减(1, 100, 0.04, excName=char.觉醒技能)
        if char.check_equ_by_name('火龙 : 爆炸的力之源') and char.check_equ_by_name('火龙 : 沸腾的龙之息'):
            char.攻击强化加成(params[0])
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.03)
            char.辅助属性加成(buff量=775)
        pass


# 固定装备：金龙 : 华丽的力之源
def entry_1286(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，施放垂直光体。 (冷却时间3秒)', '- 以相同几率施放1、3、5次', '- 造成总攻击力增加数值400%的伤害。']
    if mode == 0:
        pass
    if mode == 1:
        char.特效.append({"power": 4, "hit": 3})
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.03)
            char.辅助属性加成(buff量=775)
        pass


# 固定装备：金龙 : 灿烂的龙之鳞
def entry_1287(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，向敌人施放水平晶体。 (冷却时间3秒)', '- 以同等的概率施放 1、3、5 次。', '- 造成总攻击强化数值400%的伤害。']
    if mode == 0:
        pass
    if mode == 1:
        char.特效.append({"power": 4, "hit": 3})
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.03)
            char.辅助属性加成(buff量=775)
        pass


# 固定装备：金龙 : 无限的光之结界
def entry_1288(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，向敌人施放超立方体爆炸。 (冷却时间3秒)', '- 以同等的概率施放 1、3、5 次。', '- 造成总攻击强化数值400%的伤害。']
    if mode == 0:
        pass
    if mode == 1:
        char.特效.append({"power": 4, "hit": 3})
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.03)
            char.辅助属性加成(buff量=775)
        pass


# 固定装备：黑龙 : 黑暗的力之源
def entry_1289(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['每秒恢复0.5%的魔法值。']
    if mode == 0:
        pass
    if mode == 1:
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.03)
            char.辅助属性加成(buff量=775)
        pass


# 固定装备：黑龙 : 凝视的龙之瞳
def entry_1290(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，恢复1000点魔法值。 (冷却时间1秒)']
    if mode == 0:
        pass
    if mode == 1:
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.03)
            char.辅助属性加成(buff量=775)
        pass


# 固定装备：黑龙 : 无尽的暗黑枷锁
def entry_1291(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['装备的魔法值恢复效果 +10%']
    if mode == 0:
        pass
    if mode == 1:
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.03)
            char.辅助属性加成(buff量=775)
        pass


# 固定装备：真龙 : 压倒的力之源
def entry_1292(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，引发冲击波。 (冷却时间0.5秒)', '- 造成总攻击强化数值160%的伤害。']
    if mode == 0:
        pass
    if mode == 1:
        char.特效.append({"power": 1.6, "hit": 1})
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.03)
            char.辅助属性加成(buff量=775)
        pass


# 固定装备：真龙 : 残酷的龙之爪
def entry_1293(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，引发冲击波。 (冷却时间1秒)', '- 减少敌人0.5韧性条，', '- 造成总攻击强化数值240%的伤害。']
    if mode == 0:
        pass
    if mode == 1:
        char.特效.append({"power": 2.4, "hit": 1})
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.03)
            char.辅助属性加成(buff量=775)
        pass


# 固定装备：真龙 : 沉重的铁之志
def entry_1294(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，引发冲击波。 (冷却时间0.5秒)', '- 造成总攻击力120%的伤害。', '', '攻击时，使敌人进入眩晕状态，持续时间3秒。 (冷却时间8秒)', '', '攻击时减少敌人1.5韧性条。 (冷却时间8秒)']
    if mode == 0:
        if '眩晕' not in pa.get_state_type():
            pa.state_type.append('眩晕')
        pass
    if mode == 1:
        char.特效.append({"power": 1.2, "hit": 1})
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.03)
            char.辅助属性加成(buff量=775)
        pass


# 固定装备：天界联合军 : 意志不灭
def entry_1295(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['生命值最大值 +1200', '魔法值最大值 +1890']
    if mode == 0:
        pass
    if mode == 1:
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.03)
            char.辅助属性加成(buff量=775)
        pass


# 固定装备：天界联合军 : 祈福苍生
def entry_1296(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理/魔法防御力 +14000']
    if mode == 0:
        char.add_eq_params('defense',14000)
        pass
    if mode == 1:
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.03)
            char.辅助属性加成(buff量=775)
        pass


# 固定装备：天界联合军 : 希望曙光
def entry_1297(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性抗性 +20']
    if mode == 0:
        char.所有属性抗性加成(20)
        pass
    if mode == 1:
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.03)
            char.辅助属性加成(buff量=775)
        pass


# 固定装备：冰花 : 绽放花瓣
def entry_1334(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，所有敌人进入冰冻状态3秒。 (冷却时间 10秒)', '', '生命值最大值 +200', '物理/魔法防御力 +1400', '每分钟恢复生命值230.1。']
    if mode == 0:
        if '冰冻' not in pa.get_state_type():
            pa.state_type.append('冰冻')
            char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],10)
        char.add_eq_params('defense',1400)
        pass
    if mode == 1:
        pass


# 固定装备：冰花 : 残酷寒意
def entry_1335(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，所有敌人进入冰冻状态3秒。 (冷却时间 15秒)', '', '魔法值最大值 +315', '物理/魔法防御力 +1400', '每分钟恢复生命值230.1。']
    if mode == 0:
        if '冰冻' not in pa.get_state_type():
            pa.state_type.append('冰冻')
            char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],15)
        char.add_eq_params('defense',1400)
        pass
    if mode == 1:
        pass


# 固定装备：冰花 : 萦绕冰霜
def entry_1336(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，所有敌人进入冰冻状态5秒。 (冷却时间 20秒)', '', '攻击速度 +3%', '施放速度 +4.5%', '物理/魔法防御力 +1400', '每分钟恢复魔法值174。']
    if mode == 0:
        if '冰冻' not in pa.get_state_type():
            char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],20)
        char.攻击速度增加(0.03,part)
        char.施放速度增加(0.045)
        char.add_eq_params('defense',1400)
        pass
    if mode == 1:
        pass


# 固定装备：冰花 : 永恒冰雪
def entry_1337(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，所有敌人进入冰冻状态12秒。 (冷却时间 30秒)', '', '物理/魔法暴击率 +1.5%', '移动速度 +3%', '物理/魔法防御力 +1400', '每分钟恢复魔法值174。']
    if mode == 0:
        if '冰冻' not in pa.get_state_type():
            pa.state_type.append('冰冻')
            char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],30)
        char.移动速度增加(0.03)
        char.基础属性加成(暴击率=0.015)
        char.add_eq_params('defense',1400)
        pass
    if mode == 1:
        pass


# 固定装备：冰花 : 辽阔冻土
def entry_1338(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，所有敌人进入冰冻状态5秒。 (冷却时间 15秒)', '', '移动速度 +3%', '魔法值最大值 +315', '物理/魔法防御力 +1400', '每分钟恢复魔法值174。']
    if mode == 0:
        if '冰冻' not in pa.get_state_type():
            pa.state_type.append('冰冻')
            char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],15)
        char.移动速度增加(0.03)
        char.add_eq_params('defense',1400)
        pass
    if mode == 1:
        pass


# 固定装备：猎食 : 破碎伤痕
def entry_1339(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['中毒抗性 +15%']
    if mode == 0:
        char.异常抗性加成('中毒', 0.15)
        pass
    if mode == 1:
        pass


# 固定装备：猎食 : 消弭脉动
def entry_1340(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，使敌人进入束缚状态5秒。 (冷却时间10秒)', '', '攻击速度 +8%', '施放速度 +12%', '减速抗性 +10%', '诅咒抗性 +10%', '束缚抗性 +10%']
    if mode == 0:
        char.异常抗性加成('束缚', 0.1)
        char.异常抗性加成('诅咒', 0.1)
        char.异常抗性加成('减速', 0.1)
        char.攻击速度增加(0.08,part)
        char.施放速度增加(0.12)
        pass
    if mode == 1:
        if '减速' in pa.get_state_type() and '束缚' not in pa.get_state_type():
            pa.state_type.append('束缚')
        pass


# 固定装备：猎食 : 残酷袭击
def entry_1341(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，恢复16%的魔法值。 (冷却时间15秒)', '', '攻击时，使敌人进入感电/中毒状态20秒。 (冷却时间5秒)', '', '减速抗性 +10%', '诅咒抗性 +10%', '束缚抗性 +10%']
    if mode == 0:
        char.异常抗性加成('束缚', 0.1)
        char.异常抗性加成('诅咒', 0.1)
        char.异常抗性加成('减速', 0.1)
        if '感电' not in pa.get_state_type():
            pa.state_type.append('感电')
        if '中毒' not in pa.get_state_type():
            pa.state_type.append('中毒')
        char.异常时间['感电'][3] = min(char.异常时间['感电'][3],3)
        char.异常时间['中毒'][3] = min(char.异常时间['中毒'][3],3)
        pass
    if mode == 1:
        pass


# 固定装备：猎食 : 禁锢枷锁
def entry_1342(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +25', '', '攻击时，使敌人进入出血/灼伤状态20秒。 (冷却时间5秒)', '', '减速抗性 +10%', '诅咒抗性 +10%', '束缚抗性 +10%']
    if mode == 0:
        char.异常抗性加成('束缚', 0.1)
        char.异常抗性加成('诅咒', 0.1)
        char.异常抗性加成('减速', 0.1)
        if '出血' not in pa.get_state_type():
            pa.state_type.append('出血')
        if '灼伤' not in pa.get_state_type():
            pa.state_type.append('灼伤')
        char.异常时间['灼伤'][3] = min(char.异常时间['灼伤'][3],3)
        char.异常时间['出血'][3] = min(char.异常时间['出血'][3],3)
        char.所有属性强化加成(25)
        pass
    if mode == 1:
        pass


# 固定装备：猎食 : 追袭猎手
def entry_1343(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，使敌人进入减速/束缚状态5秒。 (冷却时间8秒)', '', '移动速度 +10%']
    if mode == 0:
        if '减速' not in pa.get_state_type():
            pa.state_type.append('减速')
        if '束缚' not in pa.get_state_type():
            pa.state_type.append('束缚')
        char.移动速度增加(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：灵通 : 协同生命
def entry_1344(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['30、60级技能冷却时间恢复速度 +20%', '- 缔造者[寒冰][终末狂想]系列技能适用该效果。']
    if mode == 0:
        if char.职业 == '缔造者':
            char.技能恢复加成(10,10,0.2)
            char.技能恢复加成(50,50,0.2)
        else:
            char.技能恢复加成(30,30,0.2)
            char.技能恢复加成(60,60,0.2)
        pass
    if mode == 1:
        pass


# 固定装备：灵通 : 守候温度
def entry_1345(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['35、70级技能冷却时间恢复速度 +22.5%', '- 缔造者[控制][构造]系列技能适用该效果。']
    if mode == 0:
        if char.职业 == '缔造者':
            char.技能恢复加成(20,20,0.225)
            char.技能恢复加成(60,60,0.225)
        else:
            char.技能恢复加成(35,35,0.225)
            char.技能恢复加成(70,70,0.225)
        pass
    if mode == 1:
        pass


# 固定装备：灵通 : 暖融阳光
def entry_1346(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['40、75级技能冷却时间恢复速度 +22.5%', '- 缔造者[守护][同调]系列技能适用该效果。']
    if mode == 0:
        if char.职业 == '缔造者':
            char.技能恢复加成(30,30,0.225)
            char.技能恢复加成(70,70,0.225)
        else:
            char.技能恢复加成(40,40,0.225)
            char.技能恢复加成(75,75,0.225)
        pass
    if mode == 1:
        pass


# 固定装备：灵通 : 满盈泪珠
def entry_1347(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['45、80级技能冷却时间恢复速度 +22.5%', '', '- 缔造者[风暴][虚空]系列技能适用该效果。']
    if mode == 0:
        if char.职业 == '缔造者':
            char.技能恢复加成(40,40,0.225)
            char.技能恢复加成(80,80,0.225)
        else:
            char.技能恢复加成(45,45,0.225)
            char.技能恢复加成(80,80,0.225)
        pass
        pass
    if mode == 1:
        pass


# 固定装备：灵通 : 并行大地
def entry_1348(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['95级技能冷却时间恢复速度 +20%']
    if mode == 0:
        char.技能恢复加成(95,95,0.2)
        pass
    if mode == 1:
        pass


# 固定装备：暴怒 : 吞噬终末的气息
def entry_1349(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['进入霸体状态', '', '消耗品、装备、技能的生命值恢复量 + 10%', '', '移动速度 +4%']
    if mode == 0:
        char.移动速度增加(0.04)
        pass
    if mode == 1:
        pass


# 固定装备：暴怒 : 贪恋世间的渴求
def entry_1350(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['进入霸体状态', '', '消耗品、装备、技能的魔法值恢复量 + 10%', '', '移动速度 +4%']
    if mode == 0:
        char.移动速度增加(0.04)
        pass
    if mode == 1:
        pass


# 固定装备：暴怒 : 毁灭万物的盲目
def entry_1351(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['前冲攻击时，产生冲击波。 (冷却时间1秒)', '- 造成总攻击强化数值400%的伤害。', '', '进入霸体状态。', '', '移动速度 +4%', '物理/魔法所受伤害 -4%']
    if mode == 0:
        char.特效.append({"power": 4, "hit": 1})
        char.移动速度增加(0.04)
        char.add_eq_params('hurted_ratio',0.04)
        pass
    if mode == 1:
        pass


# 固定装备：暴怒 : 无限膨胀的食欲
def entry_1352(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['进入霸体状态。', '', '移动速度 +12%']
    if mode == 0:
        char.移动速度增加(0.12)
        pass
    if mode == 1:
        pass


# 固定装备：暴怒 : 迷失方向的绝望
def entry_1353(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['进入霸体状态。', '', '移动速度 +8%', '物理/魔法所受伤害 -10%']
    if mode == 0:
        char.移动速度增加(0.08)
        char.add_eq_params('hurted_ratio',0.1)
        pass
    if mode == 1:
        pass


# 固定装备：雷光 : 汇聚天雷的龙心
def entry_1354(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，向敌人生成雷光爆炸。 (冷却时间4秒)', '- 造成总攻击强化数值2000%的伤害。', '', '攻击速度 +16%', '施放速度 +24%', '移动速度 +16%']
    if mode == 0:
        char.特效.append({"power": 20, "hit": 1})
        char.移动速度增加(0.16)
        char.攻击速度增加(0.16,part)
        char.施放速度增加(0.24)
        pass
    if mode == 1:
        pass


# 固定装备：雷光 : 呼唤落雷的龙角
def entry_1355(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，向敌人生成雷光爆炸。 (冷却时间4秒)', '- 造成总攻击强化数值2000%的伤害。', '', '生命值最大值 +1200', '魔法值最大值 +1892']
    if mode == 0:
        char.特效.append({"power": 20, "hit": 1})
        pass
    if mode == 1:
        pass


# 固定装备：雷光 : 拥抱沉雷的龙翼
def entry_1356(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，向敌人生成3个落雷。 (冷却时间3秒)', '- 造成总攻击强化数值400%的伤害。', '', '物理/魔法所受伤害 -12%']
    if mode == 0:
        char.add_eq_params('hurted_ratio',0.12)
        char.特效.append({"power": 4, "hit": 1})
        pass
    if mode == 1:
        pass


# 固定装备：雷光 : 覆载奔雷的龙鳞
def entry_1357(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，向敌人生成3个落雷。 (冷却时间3秒)', '- 造成总攻击强化数值400%的伤害。', '', '物理/魔法防御力 +14000']
    if mode == 0:
        char.add_eq_params('defense',14000)
        char.特效.append({"power": 4, "hit": 1})
        pass
    if mode == 1:
        pass


# 固定装备：雷光 : 踏足轰雷的龙爪
def entry_1358(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，向敌人生成3个落雷。 (冷却时间3秒)', '- 造成总攻击强化数值400%的伤害。', '', '物理/魔法暴击率 +10%', '回避率 +8%']
    if mode == 0:
        char.暴击率增加(0.1)
        char.回避率增加(0.08)
        pass
    if mode == 1:
        char.特效.append({"power": 1, "hit": 3})
        pass


# 固定装备：灵魂拘束 : 支配权能
def entry_1465(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%']
    if mode == 0:
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.07)
            char.辅助属性加成(buff量=775)
        else:
            char.技能攻击力加成(0.04)
        pass
    if mode == 1:
        pass


# 固定装备：罪恶支配 : 绝望之恐怖
def entry_1466(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '攻击速度 +4%', '施放速度 +6%', '每分钟恢复348点魔法值']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.04)
        char.施放速度增加(0.06)
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.06)
            char.辅助属性加成(buff量=775)
        else:
            char.技能攻击力加成(0.03)
        pass
    if mode == 1:
        pass


# 固定装备：深渊结集 : 无法定义之存在
def entry_1467(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '技能范围 +5%', '1~40级技能范围 +15%']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.05)
        char.multiply_eq_params('skill_range_multi',1.05)
        pass
    if mode == 1:
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.06)
            char.辅助属性加成(buff量=775)
        else:
            char.技能攻击力加成(0.03)
        pass


# 固定装备：卓越 : 玛尔本源
def entry_1468(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，发动生命的律动。 (冷却时间2秒)', '- 使敌人进入束缚状态5秒。', '- 造成总攻击强化数值1000%的伤害。']
    if mode == 0:
        pass
    if mode == 1:
        char.特效.append({"power": 10, "hit": 1})
        if '束缚' not in pa.get_state_type():
            pa.state_type.append('束缚')
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.03)
            char.辅助属性加成(buff量=775)
        pass


# 固定装备：光辉 : 崇高的使命
def entry_1469(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '获得生命值最大值3%的@[填充型保护罩]@。']
    if mode == 0:
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.03)
        pass
    if mode == 1:
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.06)
            char.辅助属性加成(buff量=775)
        else:
            char.技能攻击力加成(0.03)
        pass


# 固定装备：灵魂拘束 : 沉重罪魇
def entry_1470(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%']
    if mode == 0:
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.07)
            char.辅助属性加成(buff量=775)
        else:
            char.技能攻击力加成(0.04)
        pass
    if mode == 1:
        pass


# 固定装备：罪恶支配 : 哀鸣之恐怖
def entry_1471(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '移动速度 +4%', '所有属性抗性 +8']
    if mode == 0:
        char.移动速度增加(0.04)
        char.所有属性抗性加成(8)
        pass
    if mode == 1:
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.06)
            char.辅助属性加成(buff量=775)
        else:
            char.技能攻击力加成(0.03)
        pass


# 固定装备：深渊结集 : 无限坍缩
def entry_1472(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '技能范围 +5%', '45、60、70级技能范围 +15%']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.05)
        char.multiply_eq_params('skill_range_multi',1.05)
        pass
    if mode == 1:
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.06)
            char.辅助属性加成(buff量=775)
        else:
            char.技能攻击力加成(0.03)
        pass


# 固定装备：卓越 : 魔力之环
def entry_1473(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，发动大地的脉动。 (冷却时间1秒)', '- 使敌人进入眩晕状态5秒。', '- 造成总攻击强化数值500%的伤害。']
    if mode == 0:
        if '眩晕' not in pa.get_state_type():
            pa.state_type.append('眩晕')
        pass
    if mode == 1:
        char.特效.append({"power": 5, "hit": 1})
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.03)
            char.辅助属性加成(buff量=775)
        pass


# 固定装备：光辉 : 无畏的意志
def entry_1474(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '获得生命值最大值3%的@[填充型保护罩]@。']
    if mode == 0:
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.03)
        pass
    if mode == 1:
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.06)
            char.辅助属性加成(buff量=775)
        else:
            char.技能攻击力加成(0.03)
        pass


# 固定装备：灵魂拘束 : 绝对封印
def entry_1475(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%']
    if mode == 0:
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.07)
            char.辅助属性加成(buff量=775)
        else:
            char.技能攻击力加成(0.04)
        pass
    if mode == 1:
        pass


# 固定装备：罪恶支配 : 原初之恐怖
def entry_1476(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '物理/魔法防御力 +7000', '每分钟恢复230.1点生命值']
    if mode == 0:
        char.add_eq_params('defense',7000)
        pass
    if mode == 1:
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.06)
            char.辅助属性加成(buff量=775)
        else:
            char.技能攻击力加成(0.03)
        pass


# 固定装备：深渊结集 : 未定之力
def entry_1477(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '技能范围 +5%', '75、80级技能范围 +15%']
    if mode == 0:
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.05)
        char.multiply_eq_params('skill_range_multi',1.05)
        pass
    if mode == 1:
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.06)
            char.辅助属性加成(buff量=775)
        else:
            char.技能攻击力加成(0.03)
        pass


# 固定装备：卓越 : 宇宙耳环
def entry_1478(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，发动海浪的波动。 (冷却时间3秒)', '- 使敌人进入冰冻状态5秒。', '- 造成总攻击强化数值1500%的伤害。']
    if mode == 0:
        if '冰冻' not in pa.get_state_type():
            pa.state_type.append('冰冻')
            char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],3)
        pass
    if mode == 1:
        char.特效.append({"power": 15, "hit": 1})
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.03)
            char.辅助属性加成(buff量=775)
        pass


# 固定装备：光辉 : 传承的智慧
def entry_1479(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '获得生命值最大值3%的@[填充型保护罩]@。']
    if mode == 0:
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.03)
        pass
    if mode == 1:
        if char.check_fusion_upgrade(part):
            char.技能攻击力加成(0.06)
            char.辅助属性加成(buff量=775)
        else:
            char.技能攻击力加成(0.03)
        pass


# 固定装备：无信 : 扭曲的真心
def entry_1753(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '攻击时，随机向敌人施放3次“扭曲之剑”。 (冷却时间3秒)', '- 造成总攻击强化数值400%的伤害']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.03)
        char.特效.append({"power": 4, "hit": 3})
        pass


# 固定装备：无信 : 忘却的恩惠
def entry_1755(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '攻击时，随机向敌人施放3个“忘却之剑”。 (冷却时间3秒)', '- 造成总攻击强化数值400%的伤害']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.特效.append({"power": 4, "hit": 3})
        pass
    if mode == 1:
        pass


# 固定装备：无信 : 褪色的信仰
def entry_1757(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '攻击时，随机向敌人施放“褪色之咆哮”。 (冷却时间3秒)', '- 造成总攻击强化数值12000%的伤害']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.特效.append({"power": 12, "hit": 3})
        pass
    if mode == 1:
        pass


# 固定装备：监视者 : 选择的记忆
def entry_1759(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '生命值最大值 +1200', '魔法值最大值 +1890']
    if mode == 0:
        char.技能攻击力加成(0.03)
        pass
    if mode == 1:
        pass


# 固定装备：监视者 : 坚定的意向
def entry_1761(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '物理/魔法防御力 +14000']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.add_eq_params('defense',14000)
        pass
    if mode == 1:
        pass


# 固定装备：监视者 : 守护的信念
def entry_1763(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '所有属性抗性 +20']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.所有属性抗性加成(20)
        pass
    if mode == 1:
        pass


# 固定装备：孤岛 : 幸存的决心
def entry_1765(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '每秒恢复0.75%魔法值。']
    if mode == 0:
        char.技能攻击力加成(0.03)
        pass
    if mode == 1:
        pass


# 固定装备：孤岛 : 鸣动的沉默
def entry_1767(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '攻击时，恢复1500魔法值。 (冷却时间1秒)']
    if mode == 0:
        char.技能攻击力加成(0.03)
        pass
    if mode == 1:
        pass


# 固定装备：孤岛 : 连续的境界
def entry_1769(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '装备的魔法值恢复效果 +10%']
    if mode == 0:
        char.技能攻击力加成(0.03)
        pass
    if mode == 1:
        pass


# 固定装备：因果毁灭 : 滋生的灭亡
def entry_1771(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '85、100级技能攻击力 +10%']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.技能倍率加成(100,100,0.1)
        char.技能倍率加成(85,85,0.1)
        pass
    if mode == 1:
        pass


# 固定装备：因果毁灭 : 紧迫的噩梦
def entry_1773(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '50、85级技能攻击力 +10%']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.技能倍率加成(50,50,0.1)
        char.技能倍率加成(85,85,0.1)
        pass
    if mode == 1:
        pass


# 固定装备：因果毁灭 : 怀疑的种子
def entry_1775(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '50、100级技能攻击力 +10%']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.技能倍率加成(50,50,0.1)
        char.技能倍率加成(100,100,0.1)
        pass
    if mode == 1:
        pass


# 固定装备：怪异 : 紧抓的无为
def entry_1777(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '攻击时，生成冲击波。 (冷却时间0.5秒)', '- 造成总攻击强化数值200%的伤害。']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.特效.append({"power": 1.6, "hit": 1})
        pass
    if mode == 1:
        pass


# 固定装备：怪异 : 发芽的深渊
def entry_1779(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '攻击时，生成冲击波。 (冷却时间0.1秒)', '- 敌人韧性条量 -0.1', '- 造成总攻击强化数值36%的伤害。']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.特效.append({"power": 0.36, "hit": 1})
        pass
    if mode == 1:
        pass


# 固定装备：怪异 : 沉沦的永眠
def entry_1781(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '攻击时，生成冲击波。 (冷却时间8秒)', '- 敌人韧性条量 -3', '- 使敌人进入眩晕状态5秒', '- 造成总攻击强化数值1920%的伤害。']
    if mode == 0:
        char.特效.append({"power": 19.2, "hit": 1})
        char.技能攻击力加成(0.03)
        if '眩晕' not in pa.get_state_type():
            pa.state_type.append('眩晕')
        pass
    if mode == 1:
        pass


# 固定装备：斗志 : 绝对的勇气
def entry_1783(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '冷却时间 -5% (觉醒技能除外)']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.技能冷却缩减(1,100,0.05, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 固定装备：斗志 : 荣光的证明
def entry_1785(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '技能冷却时间 -5% (觉醒技能除外)']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.技能冷却缩减(1,100,0.05, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 固定装备：斗志 : 不懈的努力
def entry_1787(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '技能冷却时间 -5% (觉醒技能除外)']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.技能冷却缩减(1,100,0.05, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 固定装备：无信 : 背弃的信义
def entry_1789(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '攻击时，发动“背弃的伤痕”。 (冷却时间2秒)', '- 造成总攻击强化数值1000%的伤害', '', '攻击时，进入束缚状态5秒。 (冷却时间2秒)']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.特效.append({"power": 10, "hit": 1})
        if '束缚' not in pa.get_state_type():
            pa.state_type.append('束缚')
        pass
    if mode == 1:
        pass


# 固定装备：无信 : 恶毒的微笑
def entry_1791(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '攻击时，发动“恶毒的裂痕”。 (冷却时间1秒)', '- 造成总攻击强化数值500%的伤害', '', '攻击时，进入眩晕状态5秒。 (冷却时间2秒)']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.特效.append({"power": 5, "hit": 1})
        if '眩晕' not in pa.get_state_type():
            pa.state_type.append('眩晕')
        pass
    if mode == 1:
        pass


# 固定装备：无信 : 失信的言语
def entry_1793(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '', '攻击时，发动“言语的波动”。 (冷却时间3秒)', '- 造成总攻击强化数值1500%的伤害', '', '攻击时，进入冰冻状态5秒。 (冷却时间2秒)']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.特效.append({"power": 15, "hit": 1})
        if '冰冻' not in pa.get_state_type():
            pa.state_type.append('冰冻')
            char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],2)
        pass
    if mode == 1:
        pass


# 固定装备：监视者 : 尊重的恩惠
def entry_1795(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '技能范围 +5%', '', '1~40级技能范围 +18%']
    if mode == 0:
        char.技能攻击力加成(0.06)
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.05)
        char.multiply_eq_params('skill_range_multi',1.05)
        pass
    if mode == 1:
        pass


# 固定装备：监视者 : 自觉的责任
def entry_1797(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '技能范围 +5%', '', '45、60、70级技能范围 +18%']
    if mode == 0:
        char.技能攻击力加成(0.06)
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.05)
        char.multiply_eq_params('skill_range_multi',1.05)
        pass
    if mode == 1:
        pass


# 固定装备：监视者 : 顾虑的意志
def entry_1799(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '技能范围 +5%', '', '75、80级技能攻击范围 +18%']
    if mode == 0:
        char.技能攻击力加成(0.06)
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.05)
        char.multiply_eq_params('skill_range_multi',1.05)
        pass
    if mode == 1:
        pass


# 固定装备：孤岛 : 坚持的理由
def entry_1801(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '', '获得生命值最大值5%的@[填充型保护罩]@。']
    if mode == 0:
        char.技能攻击力加成(0.06)
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.05)
        pass
    if mode == 1:
        pass


# 固定装备：孤岛 : 掩饰的恐惧
def entry_1803(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '', '获得生命值最大值5%的@[填充型保护罩]@。']
    if mode == 0:
        char.技能攻击力加成(0.06)
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.05)
        pass
    if mode == 1:
        pass


# 固定装备：孤岛 : 深邃的黑暗
def entry_1805(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '', '获得生命值最大值5%的@[填充型保护罩]@。']
    if mode == 0:
        char.技能攻击力加成(0.06)
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.05)
        pass
    if mode == 1:
        pass


# 固定装备：因果毁灭 : 幻惑的背叛
def entry_1807(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '', '@[爆发约定 - 出血/感电]@', '施加出血/感电状态时，一次性结算与该异常状态相同的伤害。', '- 通过转换属性施加状态时不适用', '', '攻击时，使敌人进入中毒/灼伤状态10秒。 (冷却时间3秒)']
    if mode == 0:
        char.技能攻击力加成(0.06)
        char.set_eq_params('出血-结算', 1.0)
        char.set_eq_params('感电-结算', 1.0)
        for i in ['中毒','灼伤']:
            if i not in pa.get_state_type():
                pa.state_type.append(i)
            char.异常时间[i][3] = min(char.异常时间[i][3],3)
        pass
    if mode == 1:
        pass


# 固定装备：因果毁灭 : 灿烂的终末
def entry_1809(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '', '@[爆发约定 - 中毒/灼伤]@', '施加中毒/灼伤状态时，一次性结算与该异常状态相同的伤害。', '- 通过转换属性施加状态时不适用', '', '攻击时，使敌人进入出血/感电状态10秒。 (冷却时间3秒)']
    if mode == 0:
        char.技能攻击力加成(0.06)
        char.set_eq_params('中毒-结算', 1.0)
        char.set_eq_params('灼伤-结算', 1.0)

        for i in ['出血','感电']:
            if i not in pa.get_state_type():
                pa.state_type.append(i)
            char.异常时间[i][3] = min(char.异常时间[i][3],3)
        pass
    if mode == 1:
        pass


# 固定装备：因果毁灭 : 透彻的祸乱
def entry_1811(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '', '感电/中毒/出血/灼伤伤害 +4%', '', '攻击时，使敌人进入出血/中毒/灼伤/感电状态，效果持续10秒。 (冷却时间3秒)']
    if mode == 0:
        char.技能攻击力加成(0.05)
        for i in ['中毒','出血','灼伤','感电']:
            char.异常增伤(i,0.04)
            if i not in pa.get_state_type():
                pa.state_type.append(i)
            char.异常时间[i][3] = min(char.异常时间[i][3],5)
        pass
    if mode == 1:
        pass


# 固定装备：怪异 : 纠缠的追忆
def entry_1813(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%']
    if mode == 0:
        char.技能攻击力加成(0.07)
        pass
    if mode == 1:
        pass


# 固定装备：怪异 : 扩散的波纹
def entry_1815(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%']
    if mode == 0:
        char.技能攻击力加成(0.07)
        pass
    if mode == 1:
        pass


# 固定装备：怪异 : 刻骨的咆哮
def entry_1817(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%']
    if mode == 0:
        char.技能攻击力加成(0.07)
        pass
    if mode == 1:
        pass


# 固定装备：斗志 : 成长的旅程
def entry_1819(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '', '攻击速度 +4%', '施放速度 +6%', '每分钟恢复464点魔法值']
    if mode == 0:
        char.技能攻击力加成(0.06)
        char.攻击速度增加(0.04)
        char.施放速度增加(0.06)
        pass
    if mode == 1:
        pass


# 固定装备：斗志 : 光辉的斗魂
def entry_1821(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '', '移动速度 +4%', '所有属性抗性 +10']
    if mode == 0:
        char.技能攻击力加成(0.06)
        char.移动速度增加(0.04)
        char.所有属性抗性加成(10)
        pass
    if mode == 1:
        pass


# 固定装备：斗志 : 变幻的流风
def entry_1823(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '', '物理/魔法防御力 +8000', '每分钟恢复230.1点生命值']
    if mode == 0:
        char.技能攻击力加成(0.06)
        char.add_eq_params('defense',8000)
        pass
    if mode == 1:
        pass


# 固定装备：烈炎 : 沉静火光
def entry_1829(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '中毒抗性 +15%', '', '@[内心的火花]@', '觉醒内心的火花；根据穿戴的烈炎系列装备件数(2/3/5)，发动以下效果。', '- 技能范围 +10%/15%/25%']
    if mode == 0:
        char.技能攻击力加成(0.05)
        char.异常抗性加成('中毒',0.15)
        pass
    if mode == 1:
        pass


# 固定装备：烈炎 : 缠结意志
def entry_1830(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '减速抗性 +10%', '诅咒抗性 +10%', '束缚抗性 +10%', '', '@[内心的火花]@', '觉醒内心的火花；根据穿戴的烈炎系列装备件数(2/3/5)，发动以下效果。', '- 技能范围 +10%/15%/25%']
    if mode == 0:
        char.技能攻击力加成(0.05)
        for i in ['减速','诅咒','束缚']:
            char.异常抗性加成(i,0.1)
        pass
    if mode == 1:
        pass


# 固定装备：烈炎 : 炽烟弥天
def entry_1831(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '减速抗性 +10%', '诅咒抗性 +10%', '束缚抗性 +10%', '', '@[内心的火花]@', '觉醒内心的火花；根据穿戴的烈炎系列装备件数(2/3/5)，发动以下效果。', '- 技能范围 +10%/15%/25%']
    if mode == 0:
        char.技能攻击力加成(0.05)
        for i in ['减速','诅咒','束缚']:
            char.异常抗性加成(i,0.1)
        pass
    if mode == 1:
        pass


# 固定装备：烈炎 : 不息焚焰
def entry_1832(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '减速抗性 +10%', '诅咒抗性 +10%', '束缚抗性 +10%', '', '@[内心的火花]@', '觉醒内心的火花；根据穿戴的烈炎系列装备件数(2/3/5)，发动以下效果。', '- 技能范围 +10%/15%/25%']
    if mode == 0:
        char.技能攻击力加成(0.05)
        for i in ['减速','诅咒','束缚']:
            char.异常抗性加成(i,0.1)
        pass
    if mode == 1:
        pass


# 固定装备：烈炎 : 最终一步
def entry_1833(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '移动速度 +10%', '', '@[内心的火花]@', '觉醒内心的火花；根据穿戴的烈炎系列装备件数(2/3/5)，发动以下效果。', '- 技能范围 +10%/15%/25%']
    if mode == 0:
        char.技能攻击力加成(0.05)
        char.移动速度增加(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：雪境 : 刺骨之寒气
def entry_1834(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '所有速度 +10%', '', '@[幻视之瞳]@', '发动幻视之瞳；根据穿戴的雪境系列装备个数(2/3/5)，发动以下效果。', '- 闪避率 +30%/45%/75%', '- 被击时，解除@[幻视之瞳]@效果。 (再次发动所需冷却时间30秒)']
    if mode == 0:
        char.技能攻击力加成(0.05)
        char.所有速度增加(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：雪境 : 寂静之遗言
def entry_1835(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '生命值最大值 +500', '魔法值最大值 +500', '', '@[幻视之瞳]@', '发动幻视之瞳；根据穿戴的雪境系列装备个数(2/3/5)，发动以下效果。', '- 闪避率 +30%/45%/75%', '- 被击时，解除@[幻视之瞳]@效果。 (再次发动所需冷却时间30秒)']
    if mode == 0:
        char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


# 固定装备：雪境 : 冷意之伤痕
def entry_1836(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '物理/魔法防御力 +10000', '攻击时，恢复1%的生命值和魔法值。 (冷却时间3秒)', '', '@[幻视之瞳]@', '发动幻视之瞳；根据穿戴的雪境系列装备个数(2/3/5)，发动以下效果。', '- 闪避率 +30%/45%/75%', '- 被击时，解除@[幻视之瞳]@效果。 (再次发动所需冷却时间30秒)']
    if mode == 0:
        char.技能攻击力加成(0.05)
        char.add_eq_params('defense',10000)
        pass
    if mode == 1:
        pass


# 固定装备：雪境 : 未定的命运
def entry_1837(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '物理/魔法暴击率 +5%', '攻击时，使敌人进入冰冻状态5秒。 (冷却时间3秒)', '', '@[幻视之瞳]@', '发动幻视之瞳；根据穿戴的雪境系列装备个数(2/3/5)，发动以下效果。', '- 闪避率 +30%/45%/75%', '- 被击时，解除@[幻视之瞳]@效果。 (再次发动所需冷却时间30秒)']
    if mode == 0:
        char.技能攻击力加成(0.05)
        if '冰冻' not in pa.get_state_type():
            pa.state_type.append('冰冻')
            char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],3)
        pass
    if mode == 1:
        pass


# 固定装备：雪境 : 瞬息之足迹
def entry_1838(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '移动速度 +15%', '', '@[幻视之瞳]@', '发动幻视之瞳；根据穿戴的学境系列装备个数(2/3/5)，发动以下效果。', '- 闪避率 +30%/45%/75%- 被击时，解除@[幻视之瞳]@效果。 (再次发动所需冷却时间30秒)']
    if mode == 0:
        char.技能攻击力加成(0.05)
        char.移动速度增加(0.15)
        pass
    if mode == 1:
        pass


# 固定装备：流岚 : 山雨欲来
def entry_1839(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '技能冷却时间 -4% (觉醒技能除外)', '', '@[浓缩的流岚]@', '生成浓缩的流岚；根据穿戴的流岚系列备件数(2/3/5)，发动以下效果。', '- 移动速度 +6%/9%/15%']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.技能冷却缩减(1,100,0.04,excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 固定装备：流岚 : 风卷残云
def entry_1840(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '技能冷却时间 -4% (觉醒技能除外)', '', '@[浓缩的流岚]@', '生成浓缩的流岚；根据穿戴的流岚系列备件数(2/3/5)，发动以下效果。', '- 移动速度 +6%/9%/15%']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.技能冷却缩减(1,100,0.04,excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 固定装备：流岚 : 变幻莫测
def entry_1841(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '技能冷却时间 -4% (觉醒技能除外)', '', '@[浓缩的流岚]@', '生成浓缩的流岚；根据穿戴的流岚系列备件数(2/3/5)，发动以下效果。', '- 移动速度 +6%/9%/15%']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.技能冷却缩减(1,100,0.04,excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 固定装备：流岚 : 呼啸疾风
def entry_1842(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '技能冷却时间 -4% (觉醒技能除外)', '', '@[浓缩的流岚]@', '生成浓缩的流岚；根据穿戴的流岚系列备件数(2/3/5)，发动以下效果。', '- 移动速度 +6%/9%/15%']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.技能冷却缩减(1,100,0.04,excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 固定装备：流岚 : 闻风而动
def entry_1843(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '技能冷却时间 -4% (觉醒技能除外)', '', '@[浓缩的流岚]@', '生成浓缩的流岚；根据穿戴的流岚系列备件数(2/3/5)，发动以下效果。', '- 移动速度 +6%/9%/15%']
    if mode == 0:
        char.技能攻击力加成(0.03)
        char.技能冷却缩减(1,100,0.04,excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 固定装备：雷鸣 : 暗云翻涌
def entry_1844(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +15%', '施放速度 +20%', '攻击时，对一名敌人施加雷鸣强击。 (冷却时间3秒)', '- 造成总攻击强化的1500%的伤害', '', '@[怒雷之云]@', '攻击时，召唤怒雷之云，对最多4名敌人进行攻击；根据穿戴的雷鸣系列装备件数(2/3/5)，发动以下效果。', '- 怒雷之云召唤冷却时间：7.5秒/5秒/3秒。', '- 造成总攻击强化的1500%的伤害，并使韧性条 -5']
    if mode == 0:
        char.攻击速度增加(0.15)
        char.施放速度增加(0.2)
    if mode == 1:
        pass


# 固定装备：雷鸣 : 痛如影随
def entry_1845(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['生命值最大值 +1500', '魔法值最大值 +1500', '攻击时，对一名敌人施加雷鸣强击。 (冷却时间3秒)', '- 造成总攻击强化的1500%的伤害', '', '@[怒雷之云]@', '攻击时，召唤怒雷之云，对最多4名敌人进行攻击；根据穿戴的雷鸣系列装备件数(2/3/5)，发动以下效果。', '- 怒雷之云召唤冷却时间：7.5秒/5秒/3秒。', '- 造成总攻击强化的1500%的伤害，并使韧性条 -5']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 固定装备：雷鸣 : 惊惧之宴
def entry_1846(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理/魔法所受伤害 -6%', '攻击时，对一名敌人施加雷鸣强击。 (冷却时间3秒)', '- 造成总攻击强化的1500%的伤害', '', '@[怒雷之云]@', '攻击时，召唤怒雷之云，对最多4名敌人进行攻击；根据穿戴的雷鸣系列装备件数(2/3/5)，发动以下效果。', '- 怒雷之云召唤冷却时间：7.5秒/5秒/3秒。', '- 造成总攻击强化的1500%的伤害，并使韧性条 -5']
    if mode == 0:
        char.add_eq_params('hurted_ratio',0.06)
    if mode == 1:
        pass


# 固定装备：雷鸣 : 裂天残痕
def entry_1847(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理/魔法暴击率 +10%', '攻击时，对一名敌人施加雷鸣强击。 (冷却时间3秒)', '- 造成总攻击强化的1500%的伤害', '', '@[怒雷之云]@', '攻击时，召唤怒雷之云，对最多4名敌人进行攻击；根据穿戴的雷鸣系列装备件数(2/3/5)，发动以下效果。', '- 怒雷之云召唤冷却时间：7.5秒/5秒/3秒。', '- 造成总攻击强化的1500%的伤害，并使韧性条 -5']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 固定装备：雷鸣 : 黑云压城
def entry_1848(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['移动速度 +12%', '攻击时，对一名敌人施加雷鸣强击。 (冷却时间3秒)', '- 造成总攻击强化的1500%的伤害', '', '@[怒雷之云]@', '攻击时，召唤怒雷之云，对最多4名敌人进行攻击；根据穿戴的雷鸣系列装备件数(2/3/5)，发动以下效果。', '- 怒雷之云召唤冷却时间：7.5秒/5秒/3秒。', '- 造成总攻击强化的1500%的伤害，并使韧性条 -5']
    if mode == 0:
        char.移动速度增加(0.12)
    if mode == 1:
        pass


# 固定装备：大地 : 生机乐土
def entry_1849(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '所有速度 +10%', '', '@[生死边界]@', '从生死边界获得力量；根据穿戴的大地系列装备件数(2/3/5)，发动以下效果。', '- 所有速度 +6%/9%/15%']
    if mode == 0:
        char.技能攻击力加成(0.05)
        char.所有速度增加(0.1)
        pass
    if mode == 1:
        pass


# 固定装备：大地 : 寂灭降临之刻
def entry_1850(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '生命值最大值 +5%', '', '@[生死边界]@', '从生死边界获得力量；根据穿戴的大地系列装备件数(2/3/5)，发动以下效果。', '- 所有速度 +6%/9%/15%']
    if mode == 0:
        char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


# 固定装备：大地 : 开花时节
def entry_1851(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '魔法值最大值 +5%', '', '@[生死边界]@', '从生死边界获得力量；根据穿戴的大地系列装备件数(2/3/5)，发动以下效果。', '- 所有速度 +6%/9%/15%']
    if mode == 0:
        char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


# 固定装备：大地 : 生与死之际
def entry_1852(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '物理/魔法暴击率 +10%', '', '@[生死边界]@', '从生死边界获得力量；根据穿戴的大地系列装备件数(2/3/5)，发动以下效果。', '- 所有速度 +6%/9%/15%']
    if mode == 0:
        char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


# 固定装备：大地 : 破碎步履
def entry_1853(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '闪避率 +8%', '', '@[生死边界]@', '从生死边界获得力量；根据穿戴的大地系列装备件数(2/3/5)，发动以下效果。', '- 所有速度 +6%/9%/15%']
    if mode == 0:
        char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass

