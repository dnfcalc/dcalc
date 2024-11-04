from core.basic.property import CharacterProperty

jade_func_list = {}

# 名望 最小值 最大值 单位 分段 属性
index = ("maxFame", "min", "max", "unit", "pre", "props", "order")


def jade_26000(char: CharacterProperty = {}, text=False, value=0):
    if text:
        return "(0, 1, 1, '', 0, '无',-1)"


def jade_26001(char={}, text=False, value=0):
    if text:
        return "(56, 1, 1, '', 0, '其它',2)"


def jade_26002(char={}, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, '[附加伤害增加]增幅',1)"
    char.附加伤害增加增幅 += value/100
    char.百分比攻击强化加成(value/100)


def jade_26003(char={}, text=False, value=0):
    if text:
        return "(76, -6, 6, '%', 0.1, '技能伤害增加',0)"
    char.技能攻击力加成(value/100)


def jade_26004(char={}, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, '[暴击伤害增加]增幅',1)"
    char.暴击伤害增加增幅 += value/100
    char.百分比攻击强化加成(value/100)


def jade_26005(char={}, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, '[伤害增加]增幅',1)"
    char.伤害增加增幅 += value/100
    char.百分比攻击强化加成(value/100)


def jade_26006(char={}, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, '[最终伤害增加]增幅',1)"
    char.最终伤害增加增幅 += value/100
    char.百分比攻击强化加成(value/100)


def jade_26007(char={}, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, '[物理/魔法/独立攻击力增加]增幅',1)"
    char.物理魔法攻击力增加增幅 += value/100
    char.百分比攻击强化加成(value/100)


def jade_26008(char={}, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, '[力量智力增加]增幅',1)"
    char.力量智力增加增幅 += value/100
    char.百分比攻击强化加成(value/100)


def jade_26009(char={}, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, '[装备属性强化增加]增幅',1)"
    char.所有属性强化增幅 += value/100


def jade_26010(char={}, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, '[属性附加伤害增加]增幅',1)"
    char.属性附加伤害增加增幅 += value/100
    char.百分比攻击强化加成(value/100)


def jade_26011(char={}, text=False, value=0):
    if text:
        return "(68, 1, 1, 'Lv+1', 0, 'Lv10~15技能Lv增加',1)"
    char.技能等级加成('所有', 10, 15, int(value))


def jade_26012(char={}, text=False, value=0):
    if text:
        return "(68, 1, 1, 'Lv+1', 0, 'Lv20~25技能Lv增加',1)"
    char.技能等级加成('所有', 20, 25, int(value))


def jade_26013(char={}, text=False, value=0):
    if text:
        return "(68, 1, 1, 'Lv+1', 0, 'Lv30~35技能Lv增加',1)"
    char.技能等级加成('所有', 30, 35, int(value))


def jade_26014(char={}, text=False, value=0):
    if text:
        return "(68, 1, 1, 'Lv+1', 0, 'Lv40~45技能Lv增加',1)"
    char.技能等级加成('所有', 40, 45, int(value))


def jade_26015(char={}, text=False, value=0):
    if text:
        return "(68, 1, 1, 'Lv+1', 0, 'Lv55~60技能Lv增加',1)"
    char.技能等级加成('所有', 55, 60, int(value))


def jade_26016(char={}, text=False, value=0):
    if text:
        return "(68, 1, 1, 'Lv+1', 0, 'Lv65~70技能Lv增加',1)"
    char.技能等级加成('所有', 65, 70, int(value))


def jade_26017(char={}, text=False, value=0):
    if text:
        return "(68, 1, 1, 'Lv+1', 0, 'Lv75~80技能Lv增加',1)"
    char.技能等级加成('所有', 75, 80, int(value))


def jade_26018(char={}, text=False, value=0):
    if text:
        return "(68, 1, 1, 'Lv+1', 0, '一次觉醒技能Lv增加',1)"
    char.技能等级加成('主动', 50, 50, int(value))


def jade_26019(char={}, text=False, value=0):
    if text:
        return "(68, 1, 1, 'Lv+1', 0, '二次觉醒技能Lv增加',1)"
    char.技能等级加成('主动', 85, 85, int(value))


# 辟邪玉效果id范围 26001~26999
for i in range(26001, 26206):
    try:
        if i not in jade_func_list.keys():
            jade_func_list[i] = eval('jade_{}'.format(i))
    except Exception:
        pass


def jade_26201(char=CharacterProperty, text=False, value=0):
    if text:
        return "(76, -25, 25, '', 1, 'Lv30 Buff技能力智增加',1)"
    char.辅助属性加成(buff固定力智=value, 百分比buff量=value / 1000)


def jade_26202(char=CharacterProperty, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, 'Lv30 Buff技能力智增加%',1)"
    char.辅助属性加成(buff百分比力智=value / 100, 百分比buff量=value / 200)


def jade_26203(char=CharacterProperty, text=False, value=0):
    if text:
        return "(76, -5, 5, '', 1, 'Lv30 Buff技能三攻增加',1)"
    char.辅助属性加成(buff固定三攻=value, 百分比buff量=value / 200)


def jade_26204(char=CharacterProperty, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, 'Lv30 Buff技能三攻增加%',1)"
    char.辅助属性加成(buff百分比三攻=value / 100, 百分比buff量=value / 200)


def jade_26205(char=CharacterProperty, text=False, value=0):
    if text:
        return "(76, -100, 100, '', 1, 'Lv50 主动技能力智增加',1)"
    char.辅助属性加成(觉醒固定力智=value, 百分比buff量=value / 4000)


def jade_26206(char=CharacterProperty, text=False, value=0):
    if text:
        return "(76, -5, 5, '%', 0.1, 'Lv50 主动技能力智增加%',1)"
    char.辅助属性加成(觉醒百分比力智=value/100, 百分比buff量=value / 200)


def jade_26207(char={}, text=False, value=0):
    if text:
        return "(55, -5, 5, '%', 0.1, '攻击、移动、施放速度',1)"
    char.攻击速度增加(value/100)


for i in range(26201, 26210):
    try:
        if i not in jade_func_list.keys():
            jade_func_list[i] = eval('jade_{}'.format(i))
        sorted(jade_func_list, key=lambda x: eval(x(text=True))[6])
    except Exception:
        pass


def get_jadefunc_by_id(id):
    return jade_func_list.get(int(id), jade_26000)


def get_jade_setinfo():
    infolist = []
    for i in jade_func_list.keys():
        data = {}
        data['id'] = i
        info = eval(jade_func_list[i](text=True))
        num = 0
        for k in index:
            data[k] = info[num]
            num += 1
        infolist.append(data)
    infolist = sorted(infolist, key=lambda x: x["order"])
    return infolist
