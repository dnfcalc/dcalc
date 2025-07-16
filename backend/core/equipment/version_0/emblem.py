from core.abstract.character import CharacterProperty
from .register import register

emblem_func_list = {}

@register
def emblem_1(char: CharacterProperty):
    # DCALC_REMOVE: emblem_1
    # 力智+20 暴击+1.9%
    # rarity: 玲珑
    char.SetStatus(力智=20)
    pass


@register
def emblem_2(char: CharacterProperty):
    # DCALC_REMOVE: emblem_2
    # 力智+15 暴击+1.5%
    # rarity: 玲珑
    char.SetStatus(力智=15)
    pass


@register
def emblem_3(char: CharacterProperty):
    # DCALC_REMOVE: emblem_3
    # 力智+10 暴击+1.1%
    # rarity: 玲珑
    char.SetStatus(力智=10)
    pass


@register
def emblem_4(char: CharacterProperty):
    # DCALC_REMOVE: emblem_4
    # 力智+35
    # rarity: 玲珑
    char.SetStatus(力智=35)
    pass


@register
def emblem_5(char: CharacterProperty):
    # DCALC_REMOVE: emblem_5
    # 体精+35
    # rarity: 玲珑
    char.SetStatus(体精=35)
    pass


@register
def emblem_6(char: CharacterProperty):
    # DCALC_REMOVE: emblem_6
    # 体精+25
    # rarity: 玲珑
    char.SetStatus(体精=25)
    pass


@register
def emblem_7(char: CharacterProperty):
    # DCALC_REMOVE: emblem_7
    # 体精+17
    # rarity: 玲珑
    char.SetStatus(体精=17)
    pass


@register
def emblem_8(char: CharacterProperty):
    # DCALC_REMOVE: emblem_8
    # 力智+30
    # rarity: 玲珑
    char.SetStatus(力智=30)
    pass


@register
def emblem_9(char: CharacterProperty):
    # DCALC_REMOVE: emblem_9
    # 攻速+2%
    # rarity: 玲珑
    char.SetStatus(攻速=0.02)
    pass


@register
def emblem_10(char: CharacterProperty):
    # DCALC_REMOVE: emblem_10
    # 体精+30
    # rarity: 玲珑
    char.SetStatus(体精=30)
    pass


@register
def emblem_11(char: CharacterProperty):
    # DCALC_REMOVE: emblem_11
    # 三攻+20
    # rarity: 玲珑
    char.SetStatus(三攻=20)
    pass


@register
def emblem_12(char: CharacterProperty):
    # DCALC_REMOVE: emblem_12
    # 力智+30
    # rarity: 玲珑
    char.SetStatus(力智=30)
    pass


@register
def emblem_13(char: CharacterProperty):
    # DCALC_REMOVE: emblem_13
    # 体精+30
    # rarity: 玲珑
    char.SetStatus(体精=30)
    pass


@register
def emblem_14(char: CharacterProperty):
    # DCALC_REMOVE: emblem_14
    # 力智+25
    # rarity: 灿烂
    char.SetStatus(力智=25)
    pass


@register
def emblem_15(char: CharacterProperty):
    # DCALC_REMOVE: emblem_15
    # 力智+15
    # rarity: 灿烂
    char.SetStatus(力智=15)
    pass


@register
def emblem_16(char: CharacterProperty):
    # DCALC_REMOVE: emblem_16
    # 攻速+1.5%
    # rarity: 灿烂
    char.SetStatus(攻速=0.015)
    pass


@register
def emblem_17(char: CharacterProperty):
    # DCALC_REMOVE: emblem_17
    # 体精+15
    # rarity: 灿烂
    char.SetStatus(体精=15)
    pass


@register
def emblem_18(char: CharacterProperty):
    # DCALC_REMOVE: emblem_18
    # 三攻+15
    # rarity: 灿烂
    char.SetStatus(三攻=15)
    pass


@register
def emblem_19(char: CharacterProperty):
    # DCALC_REMOVE: emblem_19
    # 体精+15
    # rarity: 灿烂
    char.SetStatus(体精=15)
    pass


@register
def emblem_20(char: CharacterProperty):
    # DCALC_REMOVE: emblem_20
    # 力智+17
    # rarity: 华丽
    char.SetStatus(力智=17)
    pass


@register
def emblem_21(char: CharacterProperty):
    # DCALC_REMOVE: emblem_21
    # 力智+10
    # rarity: 华丽
    char.SetStatus(力智=10)
    pass


@register
def emblem_22(char: CharacterProperty):
    # DCALC_REMOVE: emblem_22
    # 攻速+1.1%
    # rarity: 华丽
    char.SetStatus(攻速=0.011)
    pass


@register
def emblem_23(char: CharacterProperty):
    # DCALC_REMOVE: emblem_23
    # 体精+10
    # rarity: 华丽
    char.SetStatus(体精=10)
    pass


@register
def emblem_24(char: CharacterProperty):
    # DCALC_REMOVE: emblem_24
    # 三攻+10
    # rarity: 华丽
    char.SetStatus(三攻=10)
    pass


@register
def emblem_25(char: CharacterProperty):
    # DCALC_REMOVE: emblem_25
    # 体精+10
    # rarity: 华丽
    char.SetStatus(体精=10)
    pass

for i in range(0, 3000):
    try:
        if str(i) not in emblem_func_list.keys():
            emblem_func_list[str(i)] = eval(f'emblem_{i}')
    except Exception:
        pass
