from core.abstract.character import CharacterProperty

emblem_func_list = {}


def emblem_1(char: CharacterProperty):
    """
    力智+20 暴击+1.9%
    """
    char.SetStatus(力智=20)
    pass


def emblem_2(char: CharacterProperty):
    """
    力智+15 暴击+1.5%
    """
    char.SetStatus(力智=15)
    pass


def emblem_3(char: CharacterProperty):
    """
    力智+10 暴击+1.1%
    """
    char.SetStatus(力智=10)
    pass


def emblem_4(char: CharacterProperty):
    """
    力智+35
    """
    char.SetStatus(力智=35)
    pass


def emblem_5(char: CharacterProperty):
    """
    体精+35
    """
    char.SetStatus(体精=35)
    pass


def emblem_6(char: CharacterProperty):
    """
    体精+25
    """
    char.SetStatus(体精=25)
    pass


def emblem_7(char: CharacterProperty):
    """
    体精+17
    """
    char.SetStatus(体精=17)
    pass


def emblem_8(char: CharacterProperty):
    """
    力智+30
    """
    char.SetStatus(力智=30)
    pass


def emblem_9(char: CharacterProperty):
    """
    攻速+2%
    """
    char.SetStatus(攻速=0.02)
    pass


def emblem_10(char: CharacterProperty):
    """
    体精+30
    """
    char.SetStatus(体精=30)
    pass


def emblem_11(char: CharacterProperty):
    """
    三攻+20
    """
    char.SetStatus(三攻=20)
    pass


def emblem_12(char: CharacterProperty):
    """
    力智+30
    """
    char.SetStatus(力智=30)
    pass


def emblem_13(char: CharacterProperty):
    """
    体精+30
    """
    char.SetStatus(体精=30)
    pass


def emblem_14(char: CharacterProperty):
    """
    力智+25
    """
    char.SetStatus(力智=25)
    pass


def emblem_15(char: CharacterProperty):
    """
    力智+15
    """
    char.SetStatus(力智=15)
    pass


def emblem_16(char: CharacterProperty):
    """
    攻速+1.5%
    """
    char.SetStatus(攻速=0.015)
    pass


def emblem_17(char: CharacterProperty):
    """
    体精+15
    """
    char.SetStatus(体精=15)
    pass


def emblem_18(char: CharacterProperty):
    """
    三攻+15
    """
    char.SetStatus(三攻=15)
    pass


def emblem_19(char: CharacterProperty):
    """
    体精+15
    """
    char.SetStatus(体精=15)
    pass


def emblem_20(char: CharacterProperty):
    """
    力智+17
    """
    char.SetStatus(力智=17)
    pass


def emblem_21(char: CharacterProperty):
    """
    力智+10
    """
    char.SetStatus(力智=10)
    pass


def emblem_22(char: CharacterProperty):
    """
    攻速+1.1%
    """
    char.SetStatus(攻速=0.011)
    pass


def emblem_23(char: CharacterProperty):
    """
    体精+10
    """
    char.SetStatus(体精=10)
    pass


def emblem_24(char: CharacterProperty):
    """
    三攻+10
    """
    char.SetStatus(三攻=10)
    pass


def emblem_25(char: CharacterProperty):
    """
    体精+10
    """
    char.SetStatus(体精=10)
    pass

for i in range(0, 3000):
    try:
        if str(i) not in emblem_func_list.keys():
            emblem_func_list[str(i)] = eval(f'emblem_{i}')
    except Exception:
        pass
