from core.abstract.character import CharacterProperty
from .register import register


@register
def emblem_2101(char: CharacterProperty):
    # DCALC_REMOVE: emblem_1
    # 力智 +35
    # rarity: 灿烂 (红色)
    char.SetStatus(力智=35)
    pass


@register
def emblem_2102(char: CharacterProperty):
    # DCALC_REMOVE: emblem_2
    # 体精 +35
    # rarity: 灿烂 (红色)
    char.SetStatus(体精=35)
    pass


@register
def emblem_2103(char: CharacterProperty):
    # DCALC_REMOVE: emblem_3
    # 四维 +15
    # rarity: 灿烂 (红色)
    char.SetStatus(四维=15)
    pass


@register
def emblem_2201(char: CharacterProperty):
    # DCALC_REMOVE: emblem_4
    # 力智 +25
    # rarity: 灿烂 (黄色)
    char.SetStatus(力智=25)
    pass


@register
def emblem_2202(char: CharacterProperty):
    # DCALC_REMOVE: emblem_5
    # 体精 +25
    # rarity: 灿烂 (黄色)
    char.SetStatus(体精=25)
    pass


@register
def emblem_2203(char: CharacterProperty):
    # DCALC_REMOVE: emblem_6
    # 攻速 +1.5% 四维 +10
    # rarity: 灿烂 (黄色)
    char.SetStatus(攻速=0.015, 四维=10)
    pass


@register
def emblem_2204(char: CharacterProperty):
    # DCALC_REMOVE: emblem_7
    # 施放 +2.2% 四维 +10
    # rarity: 灿烂 (黄色)
    char.SetStatus(施放=0.022, 四维=10)
    pass


@register
def emblem_2205(char: CharacterProperty):
    # DCALC_REMOVE: emblem_8
    # 四维 +10
    # rarity: 灿烂 (黄色)
    char.SetStatus(四维=10)
    pass


@register
def emblem_2301(char: CharacterProperty):
    # DCALC_REMOVE: emblem_9
    # 力智 +25
    # rarity: 灿烂 (绿色)
    char.SetStatus(力智=25)
    pass


@register
def emblem_2302(char: CharacterProperty):
    # DCALC_REMOVE: emblem_10
    # 体精 +25
    # rarity: 灿烂 (绿色)
    char.SetStatus(体精=25)
    pass


@register
def emblem_2303(char: CharacterProperty):
    # DCALC_REMOVE: emblem_11
    # 暴击 +3% 四维 +10
    # rarity: 灿烂 (绿色)
    char.SetStatus(暴击=0.030, 四维=10)
    pass


@register
def emblem_2304(char: CharacterProperty):
    # DCALC_REMOVE: emblem_12
    # 四维 +10
    # rarity: 灿烂 (绿色)
    char.SetStatus(四维=10)
    pass


@register
def emblem_2401(char: CharacterProperty):
    # DCALC_REMOVE: emblem_13
    # 三攻 +30
    # rarity: 灿烂 (蓝色)
    char.SetStatus(三攻=30)
    pass


@register
def emblem_2402(char: CharacterProperty):
    # DCALC_REMOVE: emblem_14
    # 移动 +1.5% 四维 +10
    # rarity: 灿烂 (蓝色)
    char.SetStatus(移动=0.015, 四维=10)
    pass


@register
def emblem_2403(char: CharacterProperty):
    # DCALC_REMOVE: emblem_15
    # 四维 +10
    # rarity: 灿烂 (蓝色)
    char.SetStatus(四维=10)
    pass


@register
def emblem_2501(char: CharacterProperty):
    # DCALC_REMOVE: emblem_16
    # 四维 +10
    # rarity: 灿烂 (彩色)
    char.SetStatus(四维=10)
    pass


@register
def emblem_2601(char: CharacterProperty):
    # DCALC_REMOVE: emblem_17
    # 力智 +20 暴击 +1.5%
    # rarity: 灿烂 (红绿)
    char.SetStatus(力智=20, 暴击=0.015)
    pass


@register
def emblem_2602(char: CharacterProperty):
    # DCALC_REMOVE: emblem_18
    # 力智 +20
    # rarity: 灿烂 (红绿)
    char.SetStatus(力智=20)
    pass


@register
def emblem_2701(char: CharacterProperty):
    # DCALC_REMOVE: emblem_19
    # 四维 +10
    # rarity: 灿烂 (黄蓝)
    char.SetStatus(四维=10)
    pass


@register
def emblem_3101(char: CharacterProperty):
    # DCALC_REMOVE: emblem_20
    # 力智 +50
    # rarity: 玲珑 (红色)
    char.SetStatus(力智=50)
    pass


@register
def emblem_3102(char: CharacterProperty):
    # DCALC_REMOVE: emblem_21
    # 体精 +50
    # rarity: 玲珑 (红色)
    char.SetStatus(体精=50)
    pass


@register
def emblem_3103(char: CharacterProperty):
    # DCALC_REMOVE: emblem_22
    # 四维 +20
    # rarity: 玲珑 (红色)
    char.SetStatus(四维=20)
    pass


@register
def emblem_3201(char: CharacterProperty):
    # DCALC_REMOVE: emblem_23
    # 力智 +40
    # rarity: 玲珑 (黄色)
    char.SetStatus(力智=40)
    pass


@register
def emblem_3202(char: CharacterProperty):
    # DCALC_REMOVE: emblem_24
    # 体精 +40
    # rarity: 玲珑 (黄色)
    char.SetStatus(体精=40)
    pass


@register
def emblem_3203(char: CharacterProperty):
    # DCALC_REMOVE: emblem_25
    # 攻速 +2% 四维 +15
    # rarity: 玲珑 (黄色)
    char.SetStatus(攻速=0.020, 四维=15)
    pass


@register
def emblem_3204(char: CharacterProperty):
    # DCALC_REMOVE: emblem_26
    # 施放 +3% 四维 +15
    # rarity: 玲珑 (黄色)
    char.SetStatus(施放=0.030, 四维=15)
    pass


@register
def emblem_3205(char: CharacterProperty):
    # DCALC_REMOVE: emblem_27
    # 四维 +15
    # rarity: 玲珑 (黄色)
    char.SetStatus(四维=15)
    pass


@register
def emblem_3301(char: CharacterProperty):
    # DCALC_REMOVE: emblem_28
    # 力智 +40
    # rarity: 玲珑 (绿色)
    char.SetStatus(力智=40)
    pass


@register
def emblem_3302(char: CharacterProperty):
    # DCALC_REMOVE: emblem_29
    # 体精 +40
    # rarity: 玲珑 (绿色)
    char.SetStatus(体精=40)
    pass


@register
def emblem_3303(char: CharacterProperty):
    # DCALC_REMOVE: emblem_30
    # 暴击 +4% 四维 +15
    # rarity: 玲珑 (绿色)
    char.SetStatus(暴击=0.040, 四维=15)
    pass


@register
def emblem_3304(char: CharacterProperty):
    # DCALC_REMOVE: emblem_31
    # 四维 +15
    # rarity: 玲珑 (绿色)
    char.SetStatus(四维=15)
    pass


@register
def emblem_3401(char: CharacterProperty):
    # DCALC_REMOVE: emblem_32
    # 三攻 +40
    # rarity: 玲珑 (蓝色)
    char.SetStatus(三攻=40)
    pass


@register
def emblem_3402(char: CharacterProperty):
    # DCALC_REMOVE: emblem_33
    # 移动 +2% 四维 +15
    # rarity: 玲珑 (蓝色)
    char.SetStatus(移动=0.020, 四维=15)
    pass


@register
def emblem_3403(char: CharacterProperty):
    # DCALC_REMOVE: emblem_34
    # 四维 +15
    # rarity: 玲珑 (蓝色)
    char.SetStatus(四维=15)
    pass


@register
def emblem_3501(char: CharacterProperty):
    # DCALC_REMOVE: emblem_35
    # 四维 +15
    # rarity: 玲珑 (彩色)
    char.SetStatus(四维=15)
    pass


@register
def emblem_3601(char: CharacterProperty):
    # DCALC_REMOVE: emblem_36
    # 力智 +25 暴击 +1.9%
    # rarity: 玲珑 (红绿)
    char.SetStatus(力智=25, 暴击=0.019)
    pass


@register
def emblem_3602(char: CharacterProperty):
    # DCALC_REMOVE: emblem_37
    # 力智 +25
    # rarity: 玲珑 (红绿)
    char.SetStatus(力智=25)
    pass


@register
def emblem_3701(char: CharacterProperty):
    # DCALC_REMOVE: emblem_38
    # 四维 +15
    # rarity: 玲珑 (黄蓝)
    char.SetStatus(四维=15)
    pass


@register
def emblem_4101(char: CharacterProperty):
    # DCALC_REMOVE: emblem_39
    # 力智 +70
    # rarity: 神圣 (红色)
    char.SetStatus(力智=70)
    pass


@register
def emblem_4102(char: CharacterProperty):
    # DCALC_REMOVE: emblem_40
    # 体精 +70
    # rarity: 神圣 (红色)
    char.SetStatus(体精=70)
    pass


@register
def emblem_4103(char: CharacterProperty):
    # DCALC_REMOVE: emblem_41
    # 四维 +25
    # rarity: 神圣 (红色)
    char.SetStatus(四维=25)
    pass


@register
def emblem_4201(char: CharacterProperty):
    # DCALC_REMOVE: emblem_42
    # 力智 +55
    # rarity: 神圣 (黄色)
    char.SetStatus(力智=55)
    pass


@register
def emblem_4202(char: CharacterProperty):
    # DCALC_REMOVE: emblem_43
    # 体精 +55
    # rarity: 神圣 (黄色)
    char.SetStatus(体精=55)
    pass


@register
def emblem_4203(char: CharacterProperty):
    # DCALC_REMOVE: emblem_44
    # 攻速 +2.5% 四维 +20
    # rarity: 神圣 (黄色)
    char.SetStatus(攻速=0.025, 四维=20)
    pass


@register
def emblem_4204(char: CharacterProperty):
    # DCALC_REMOVE: emblem_45
    # 施放 +4% 四维 +20
    # rarity: 神圣 (黄色)
    char.SetStatus(施放=0.040, 四维=20)
    pass


@register
def emblem_4205(char: CharacterProperty):
    # DCALC_REMOVE: emblem_46
    # 四维 +20
    # rarity: 神圣 (黄色)
    char.SetStatus(四维=20)
    pass


@register
def emblem_4301(char: CharacterProperty):
    # DCALC_REMOVE: emblem_47
    # 力智 +55
    # rarity: 神圣 (绿色)
    char.SetStatus(力智=55)
    pass


@register
def emblem_4302(char: CharacterProperty):
    # DCALC_REMOVE: emblem_48
    # 体精 +55
    # rarity: 神圣 (绿色)
    char.SetStatus(体精=55)
    pass


@register
def emblem_4303(char: CharacterProperty):
    # DCALC_REMOVE: emblem_49
    # 暴击 +3% 四维 +20
    # rarity: 神圣 (绿色)
    char.SetStatus(暴击=0.030, 四维=20)
    pass


@register
def emblem_4304(char: CharacterProperty):
    # DCALC_REMOVE: emblem_50
    # 四维 +20
    # rarity: 神圣 (绿色)
    char.SetStatus(四维=20)
    pass


@register
def emblem_4401(char: CharacterProperty):
    # DCALC_REMOVE: emblem_51
    # 三攻 +60
    # rarity: 神圣 (蓝色)
    char.SetStatus(三攻=60)
    pass


@register
def emblem_4402(char: CharacterProperty):
    # DCALC_REMOVE: emblem_52
    # 移动 +2.5% 四维 +20
    # rarity: 神圣 (蓝色)
    char.SetStatus(移动=0.025, 四维=20)
    pass


@register
def emblem_4403(char: CharacterProperty):
    # DCALC_REMOVE: emblem_53
    # 四维 +20
    # rarity: 神圣 (蓝色)
    char.SetStatus(四维=20)
    pass


@register
def emblem_4501(char: CharacterProperty):
    # DCALC_REMOVE: emblem_54
    # 四维 +20
    # rarity: 神圣 (彩色)
    char.SetStatus(四维=20)
    pass


@register
def emblem_4601(char: CharacterProperty):
    # DCALC_REMOVE: emblem_55
    # 力智 +30 暴击 +2.5%
    # rarity: 神圣 (红绿)
    char.SetStatus(力智=30, 暴击=0.025)
    pass


@register
def emblem_4602(char: CharacterProperty):
    # DCALC_REMOVE: emblem_56
    # 力智 +30
    # rarity: 神圣 (红绿)
    char.SetStatus(力智=30)
    pass


@register
def emblem_4701(char: CharacterProperty):
    # DCALC_REMOVE: emblem_57
    # 四维 +20
    # rarity: 神圣 (黄蓝)
    char.SetStatus(四维=20)
    pass


@register
def emblem_combine(char: CharacterProperty, position: str, lv: int, emblem_list: list[int | str]):
    bufferP = [0.001, 0.002, 0.004, 0.006, 0.008, 0.01, 0.013, 0.016, 0.019, 0.022, 0.025, 0.026, 0.027, 0.028, 0.029, 0.03]
    buffer = [10, 30, 60, 90, 120, 150, 180, 210, 240270, 300, 320, 340, 360, 380, 400]
    skillAttack = [0.002, 0.004, 0.008, 0.012, 0.016, 0.02, 0.023, 0.026, 0.029, 0.032, 0.035, 0.036, 0.037, 0.038, 0.039, 0.04]
    attackP = [0.005, 0.009, 0.013, 0.017, 0.021, 0.025, 0.028, 0.031, 0.034, 0.037, 0.04, 0.042, 0.044, 0.046, 0.048, 0.05]
    # 固有属性
    if position == '彩色':
        char.SetStatus(BufferP=bufferP[lv - 1], SkillAttack=skillAttack[lv - 1])
    else:
        char.SetStatus(Buffer=buffer[lv - 1], AttackP=attackP[lv - 1])
    rarity = (lv - 1) // 5
    emblems = list(filter(lambda x: int(x) > 0, emblem_list)) or []
    emblem_raritys = [int(i) // 1000 for i in emblems]
    # 稀有
    if rarity == 0:
        skillAttack = [0.001, 0.001, 0.002, 0.002]
        buffer = []
        for i in emblem_raritys:
            pass
        pass
    # 神器
    elif rarity == 1:
        pass
    # 传说
    elif rarity == 2:
        pass
    # 史诗
    elif rarity == 3:
        pass
