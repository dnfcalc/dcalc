from core.abstract.character import CharacterProperty
from .register import register

@register
def jade_0(char: CharacterProperty = {}, value=0):
    pass

@register
def jade_1(char: CharacterProperty = {}, value=0):
    char.jade_effect.SkillAttack += value/100

@register
def jade_2(char: CharacterProperty = {}, value=0):
    char.jade_effect.AttackP += value/100
    pass

@register
def jade_3(char: CharacterProperty = {}, value=0):
    char.jade_effect.ElementIncrease += value/100
    pass

@register
def jade_4(char: CharacterProperty = {}, value=0):
    if value > 0:
        char.AddSkillLv(10, 15, 1)
    pass


@register
def jade_5(char: CharacterProperty = {}, value=0):
    if value > 0:
        char.AddSkillLv(20, 25, 1)
    pass


@register
def jade_6(char: CharacterProperty = {}, value=0):
    if value > 0:
        char.AddSkillLv(30, 35, 1)
    pass

@register
def jade_7(char: CharacterProperty = {}, value=0):
    if value > 0:
        char.AddSkillLv(40, 45, 1)
    pass

@register
def jade_8(char: CharacterProperty = {}, value=0):
    if value > 0:
        char.AddSkillLv(55, 60, 1)
    pass

@register
def jade_9(char: CharacterProperty = {}, value=0):
    if value > 0:
        char.AddSkillLv(65, 70, 1)
    pass

@register
def jade_10(char: CharacterProperty = {}, value=0):
    if value > 0:
        char.AddSkillLv(75, 80, 1)
    pass

@register
def jade_11(char: CharacterProperty = {}, value=0):
    if value > 0:
        char.AddSkillLv(50, 50, 1)
    pass

@register
def jade_12(char: CharacterProperty = {}, value=0):
    if value > 0:
        char.AddSkillLv(85, 85, 1)
    pass

@register
def jade_13(char: CharacterProperty = {}, value=0):
    char.BuffSkill.STRINTPLUS += value
    char.SetStatus(BufferP=value/1000)

@register
def jade_14(char: CharacterProperty = {}, value=0):
    char.BuffSkill.STRINTRatio *= 1 + value/100
    char.SetStatus(BufferP=value/200)

@register
def jade_15(char: CharacterProperty = {}, value=0):
    char.BuffSkill.ATKPLUS += value
    char.SetStatus(BufferP=value/200)

@register
def jade_16(char: CharacterProperty = {}, value=0):
    char.BuffSkill.ATKRatio *= 1 + value/100
    char.SetStatus(BufferP=value/200)

@register
def jade_17(char: CharacterProperty = {}, value=0):
    char.AwakeSkill.STRINTPLUS += value
    char.SetStatus(BufferP=value/4000)

@register
def jade_18(char: CharacterProperty = {}, value=0):
    char.AwakeSkill.STRINTRatio *= 1 + value/100
    char.SetStatus(BufferP=value/200)
