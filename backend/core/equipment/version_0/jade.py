from core.abstract.character import CharacterProperty

jade_func_list = {}


def jade_0(char: CharacterProperty = {}, value=0):
    pass

def jade_1(char: CharacterProperty = {}, value=0):
    char.jade_effect.SkillAttack += value/100

def jade_2(char: CharacterProperty = {}, value=0):
    char.jade_effect.AttackP += value/100
    pass

def jade_3(char: CharacterProperty = {}, value=0):
    char.jade_effect.ElementIncrease += value/100
    pass

def jade_4(char: CharacterProperty = {}, value=0):
    if value > 0:
        char.AddSkillLv(10, 15, 1)
    pass


def jade_5(char: CharacterProperty = {}, value=0):
    if value > 0:
        char.AddSkillLv(20, 25, 1)
    pass


def jade_6(char: CharacterProperty = {}, value=0):
    if value > 0:
        char.AddSkillLv(30, 35, 1)
    pass

def jade_7(char: CharacterProperty = {}, value=0):
    if value > 0:
        char.AddSkillLv(40, 45, 1)
    pass

def jade_8(char: CharacterProperty = {}, value=0):
    if value > 0:
        char.AddSkillLv(55, 60, 1)
    pass

def jade_9(char: CharacterProperty = {}, value=0):
    if value > 0:
        char.AddSkillLv(65, 70, 1)
    pass

def jade_10(char: CharacterProperty = {}, value=0):
    if value > 0:
        char.AddSkillLv(75, 80, 1)
    pass

def jade_11(char: CharacterProperty = {}, value=0):
    if value > 0:
        char.AddSkillLv(50, 50, 1)
    pass

def jade_12(char: CharacterProperty = {}, value=0):
    if value > 0:
        char.AddSkillLv(85, 85, 1)
    pass

def jade_13(char: CharacterProperty = {}, value=0):
    char.BuffSkill.STRINTPLUS += value
    char.SetStatus(BufferP=value/1000)

def jade_14(char: CharacterProperty = {}, value=0):
    char.BuffSkill.STRINTRatio *= 1 + value/100
    char.SetStatus(BufferP=value/200)

def jade_15(char: CharacterProperty = {}, value=0):
    char.BuffSkill.ATKPLUS += value
    char.SetStatus(Buffer=value/1000)

def jade_16(char: CharacterProperty = {}, value=0):
    char.BuffSkill.ATKRatio *= 1 + value/100
    char.SetStatus(BufferP=value/200)

def jade_17(char: CharacterProperty = {}, value=0):
    char.AwakeSkill.STRINTPLUS += value
    char.SetStatus(BufferP=value/4000)

def jade_18(char: CharacterProperty = {}, value=0):
    char.AwakeSkill.STRINTRatio *= 1 + value/100
    char.SetStatus(BufferP=value/200)
# # 辟邪玉效果id范围 26001~26999
# for i in range(26001, 26206):
#     try:
#         if i not in jade_func_list.keys():
#             jade_func_list[i] = eval('jade_{}'.format(i))
#     except Exception:
#         pass


# def jade_26201(char=CharacterProperty, text=False, value=0):
#     if text:
#         return "(76, -25, 25, '', 1, 'Lv30 Buff技能力智增加',1)"
#     char.辅助属性加成(buff固定力智=value, 百分比buff量=value / 1000)


# def jade_26202(char=CharacterProperty, text=False, value=0):
#     if text:
#         return "(76, -5, 5, '%', 0.1, 'Lv30 Buff技能力智增加%',1)"
#     char.辅助属性加成(buff百分比力智=value / 100, 百分比buff量=value / 200)


# def jade_26203(char=CharacterProperty, text=False, value=0):
#     if text:
#         return "(76, -5, 5, '', 1, 'Lv30 Buff技能三攻增加',1)"
#     char.辅助属性加成(buff固定三攻=value, 百分比buff量=value / 200)


# def jade_26204(char=CharacterProperty, text=False, value=0):
#     if text:
#         return "(76, -5, 5, '%', 0.1, 'Lv30 Buff技能三攻增加%',1)"
#     char.辅助属性加成(buff百分比三攻=value / 100, 百分比buff量=value / 200)


# def jade_26205(char=CharacterProperty, text=False, value=0):
#     if text:
#         return "(76, -100, 100, '', 1, 'Lv50 主动技能力智增加',1)"
#     char.辅助属性加成(觉醒固定力智=value, 百分比buff量=value / 4000)


# def jade_26206(char=CharacterProperty, text=False, value=0):
#     if text:
#         return "(76, -5, 5, '%', 0.1, 'Lv50 主动技能力智增加%',1)"
#     char.辅助属性加成(觉醒百分比力智=value/100, 百分比buff量=value / 200)


# def jade_26207(char={}, text=False, value=0):
#     if text:
#         return "(55, -5, 5, '%', 0.1, '攻击、移动、施放速度',1)"
#     char.攻击速度增加(value/100)


for i in range(0,20):
    try:
        if str(i) not in jade_func_list.keys():
            jade_func_list[str(i)] = eval(f'jade_{i}')
    except Exception:
        pass

# def get_jadefunc_by_id(id):
#     return jade_func_list.get(int(id), jade_26000)


# def get_jade_setinfo():
#     infolist = []
#     for i in jade_func_list.keys():
#         data = {}
#         data['id'] = i
#         info = eval(jade_func_list[i](text=True))
#         num = 0
#         for k in index:
#             data[k] = info[num]
#             num += 1
#         infolist.append(data)
#     infolist = sorted(infolist, key=lambda x: x["order"])
#     return infolist