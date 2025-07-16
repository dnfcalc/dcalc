from core.abstract.character import CharacterProperty
from .register import register

# region 头肩


@register
def enchant_1(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1
    # 三攻(10)|四维(40)|技攻(3%)|暴击率(5%)
    char.SetStatus(三攻=10, 四维=40, 技攻=0.03)
    pass


@register
def enchant_2(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2
    # 三攻(20)|四维(75)|Lv1~50主动+1
    char.SetStatus(三攻=20, 四维=75)
    char.AddSkillLv(1, 50, 1, 1)
    pass


@register
def enchant_3(char: CharacterProperty):
    # DCALC_REMOVE: enchant_3
    # 三攻(20)|四维(75)|技攻(5%)
    char.SetStatus(三攻=20, 四维=75, 技攻=0.05)
    pass


@register
def enchant_4(char: CharacterProperty):
    # DCALC_REMOVE: enchant_4
    # Lv30增益技能等级 +1|lv50主动技能等级+1
    if char.buffer:
        char.AddSkillLv(30, 30, 1, 1)
        char.AddSkillLv(50, 50, 1, 1)
    pass


# endregion
# region 上衣


@register
def enchant_100(char: CharacterProperty):
    # DCALC_REMOVE: enchant_100
    # 三攻(110)|力智(80)
    char.SetStatus(三攻=110, 力智=80)
    pass


@register
def enchant_101(char: CharacterProperty):
    # DCALC_REMOVE: enchant_101
    # 四维(100)|奶系Lv15被动+3
    char.SetStatus(四维=100)
    if char.buffer:
        char.AddSkillLv(15, 15, 3, 0)
    pass


@register
def enchant_102(char: CharacterProperty):
    # DCALC_REMOVE: enchant_102
    # 四维(120)|奶系Lv15被动+3
    char.SetStatus(四维=120)
    if char.buffer:
        char.AddSkillLv(15, 15, 3, 0)
    pass


@register
def enchant_103(char: CharacterProperty):
    # DCALC_REMOVE: enchant_103
    # 三攻(110)|力智(90)|技攻(1%)
    char.SetStatus(三攻=110, 力智=90, 技攻=0.01)
    pass


@register
def enchant_104(char: CharacterProperty):
    # DCALC_REMOVE: enchant_104
    # 四维(125)|奶系Lv15被动+4
    char.SetStatus(四维=125)
    if char.buffer:
        char.AddSkillLv(15, 15, 4, 0)
    pass


@register
def enchant_105(char: CharacterProperty):
    # DCALC_REMOVE: enchant_105
    # 三攻(110)|力智(90)|技攻(2%)
    char.SetStatus(三攻=110, 力智=90, 技攻=0.02)
    pass


# endregion
# region 头肩


@register
def enchant_106(char: CharacterProperty):
    # DCALC_REMOVE: enchant_106
    # 四维(120)|奶系Lv15被动+3
    char.SetStatus(四维=120)
    if char.buffer:
        char.AddSkillLv(15, 15, 3, 0)
    pass


# endregion
# region 武器


@register
def enchant_107(char: CharacterProperty):
    # DCALC_REMOVE: enchant_107
    # 独立(90)|力智(60)
    char.SetStatus(独立=90, 力智=60)
    pass


@register
def enchant_108(char: CharacterProperty):
    # DCALC_REMOVE: enchant_108
    # 魔攻(90)|力智(60)
    char.SetStatus(魔攻=90, 力智=60)
    pass


@register
def enchant_109(char: CharacterProperty):
    # DCALC_REMOVE: enchant_109
    # 物攻(90)|力智(60)
    char.SetStatus(物攻=90, 力智=60)
    pass


@register
def enchant_110(char: CharacterProperty):
    # DCALC_REMOVE: enchant_110
    # 智力(100)
    char.SetStatus(智力=100)
    pass


@register
def enchant_111(char: CharacterProperty):
    # DCALC_REMOVE: enchant_111
    # 力量(100)
    char.SetStatus(力量=100)
    pass


@register
def enchant_112(char: CharacterProperty):
    # DCALC_REMOVE: enchant_112
    # 体力(100)
    char.SetStatus(体力=100)
    pass


@register
def enchant_113(char: CharacterProperty):
    # DCALC_REMOVE: enchant_113
    # 精神(100)
    char.SetStatus(精神=100)
    pass


# endregion
# region 下装


@register
def enchant_200(char: CharacterProperty):
    # DCALC_REMOVE: enchant_200
    # 三攻(110)|力智(80)
    char.SetStatus(三攻=110, 力智=80)
    pass


@register
def enchant_201(char: CharacterProperty):
    # DCALC_REMOVE: enchant_201
    # 四维(125)|奶系Lv15被动+4
    char.SetStatus(四维=125)
    if char.buffer:
        char.AddSkillLv(15, 15, 4, 0)
    pass


@register
def enchant_202(char: CharacterProperty):
    # DCALC_REMOVE: enchant_202
    # 三攻(110)|力智(90)|技攻(2%)
    char.SetStatus(三攻=110, 力智=90, 技攻=0.02)
    pass

@register
def enchant_203(char: CharacterProperty):
    # DCALC_REMOVE: enchant_203
    # 三攻(90)|力智(60)
    char.SetStatus(三攻=90, 力智=60)
    pass

@register
def enchant_204(char: CharacterProperty):
    # DCALC_REMOVE: enchant_204
    # 四维(100)
    char.SetStatus(四维=100)
    pass


# endregion
# region 腰带


@register
def enchant_300(char: CharacterProperty):
    # DCALC_REMOVE: enchant_300
    # 三攻(30)|技攻(1%)
    char.SetStatus(三攻=30, 技攻=0.01)
    pass


@register
def enchant_301(char: CharacterProperty):
    # DCALC_REMOVE: enchant_301
    # 三攻(10)|四维(40)|技攻(2%)
    char.SetStatus(三攻=10, 四维=40, 技攻=0.02)
    pass


@register
def enchant_302(char: CharacterProperty):
    # DCALC_REMOVE: enchant_302
    # 四维(45)|Lv1~50主动+1
    char.SetStatus(四维=45)
    char.AddSkillLv(1, 50, 1, 1)
    pass


@register
def enchant_303(char: CharacterProperty):
    # DCALC_REMOVE: enchant_303
    # 三攻(36)|技攻(5%)|暴击率(3%)
    char.SetStatus(三攻=36, 技攻=0.05)
    pass

@register
def enchant_304(char: CharacterProperty):
    # DCALC_REMOVE: enchant_304
    # 四维(50)|三攻(15)|技攻(3%)|暴击率(3%)
    char.SetStatus(四维=50, 三攻=15, 技攻=0.03)
    pass

@register
def enchant_305(char: CharacterProperty):
    # DCALC_REMOVE: enchant_305
    # 四维(120)|奶系Lv15被动+3|暴击率(7%)
    char.SetStatus(四维=120)
    if char.buffer:
        char.AddSkillLv(15, 15, 3, 0)
    pass

@register
def enchant_306(char: CharacterProperty):
    # DCALC_REMOVE: enchant_306
    # 三攻(10)|四维(40)|技攻(1%)
    char.SetStatus(三攻=10, 四维=40, 技攻=0.01)
    pass

@register
def enchant_307(char: CharacterProperty):
    # DCALC_REMOVE: enchant_307
    # 四维(100)|奶系Lv15被动+1
    char.SetStatus(四维=100)
    if char.buffer:
        char.AddSkillLv(15, 15, 1, 0)
    pass

@register
def enchant_308(char: CharacterProperty):
    # DCALC_REMOVE: enchant_308
    # 三攻(36)|技攻(3%)
    char.SetStatus(三攻=36, 技攻=0.03)
    pass
# endregion
# region 武器


@register
def enchant_500(char: CharacterProperty):
    # DCALC_REMOVE: enchant_500
    # 火强(15)
    char.AddElementDB('火', 15)
    pass


@register
def enchant_501(char: CharacterProperty):
    # DCALC_REMOVE: enchant_501
    # 冰强(15)
    char.AddElementDB('冰', 15)
    pass


@register
def enchant_502(char: CharacterProperty):
    # DCALC_REMOVE: enchant_502
    # 光强(15)
    char.AddElementDB('光', 15)
    pass


@register
def enchant_503(char: CharacterProperty):
    # DCALC_REMOVE: enchant_503
    # 暗强(15)
    char.AddElementDB('暗', 15)
    pass


@register
def enchant_504(char: CharacterProperty):
    # DCALC_REMOVE: enchant_504
    # 火强(15)|光强(15)
    char.AddElementDB('火', 15)
    char.AddElementDB('光', 15)
    pass


@register
def enchant_505(char: CharacterProperty):
    # DCALC_REMOVE: enchant_505
    # 冰强(15)|暗强(15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('暗', 15)
    pass


@register
def enchant_506(char: CharacterProperty):
    # DCALC_REMOVE: enchant_506
    # 火强(15)|冰强(15)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    pass


@register
def enchant_507(char: CharacterProperty):
    # DCALC_REMOVE: enchant_507
    # 全属强(13)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    pass


@register
def enchant_508(char: CharacterProperty):
    # DCALC_REMOVE: enchant_508
    # 物攻(30)|独立(30)|全属强(15)|攻速(5%)
    char.SetStatus(物攻=30, 独立=30, 攻速=0.05)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    pass


@register
def enchant_509(char: CharacterProperty):
    # DCALC_REMOVE: enchant_509
    # 魔攻(30)|独立(30)|全属强(15)|施放(6%)
    char.SetStatus(魔攻=30, 独立=30, 施放=0.06)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    pass


@register
def enchant_510(char: CharacterProperty):
    # DCALC_REMOVE: enchant_510
    # 三攻(30)|全属强(15)
    char.SetStatus(三攻=30)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    pass


@register
def enchant_511(char: CharacterProperty):
    # DCALC_REMOVE: enchant_511
    # 四维(110)|施放(7%)
    char.SetStatus(四维=110, 施放速度=0.07)
    pass


@register
def enchant_512(char: CharacterProperty):
    # DCALC_REMOVE: enchant_512
    # 三攻(50)|全属强(16)|属性攻击
    char.SetStatus(三攻=50)
    char.AddElementDB('火', 16)
    char.AddElementDB('冰', 16)
    char.AddElementDB('光', 16)
    char.AddElementDB('暗', 16)
    pass


# endregion
# region 项链


@register
def enchant_600(char: CharacterProperty):
    # DCALC_REMOVE: enchant_600
    # 全属强(30)
    char.AddElementDB('火', 30)
    char.AddElementDB('冰', 30)
    char.AddElementDB('光', 30)
    char.AddElementDB('暗', 30)
    pass


@register
def enchant_601(char: CharacterProperty):
    # DCALC_REMOVE: enchant_601
    # 全属强(28)
    char.AddElementDB('火', 28)
    char.AddElementDB('冰', 28)
    char.AddElementDB('光', 28)
    char.AddElementDB('暗', 28)
    pass


@register
def enchant_602(char: CharacterProperty):
    # DCALC_REMOVE: enchant_602
    # 四维(70)
    char.SetStatus(四维=70)
    pass


@register
def enchant_603(char: CharacterProperty):
    # DCALC_REMOVE: enchant_603
    # 全属强(33)
    char.AddElementDB('火', 33)
    char.AddElementDB('冰', 33)
    char.AddElementDB('光', 33)
    char.AddElementDB('暗', 33)
    pass


@register
def enchant_604(char: CharacterProperty):
    # DCALC_REMOVE: enchant_604
    # 火强(35)|光强(35)
    char.AddElementDB('火', 35)
    char.AddElementDB('光', 35)
    pass


@register
def enchant_605(char: CharacterProperty):
    # DCALC_REMOVE: enchant_605
    # 冰强(35)|暗强(35)
    char.AddElementDB('冰', 35)
    char.AddElementDB('暗', 35)
    pass


@register
def enchant_606(char: CharacterProperty):
    # DCALC_REMOVE: enchant_606
    # 四维(90)
    char.SetStatus(四维=90)
    pass


@register
def enchant_607(char: CharacterProperty):
    # DCALC_REMOVE: enchant_607
    # 四维(100)|奶系Lv15被动+1
    char.SetStatus(四维=100)
    if char.buffer:
        char.AddSkillLv(15, 15, 1, 0)
    pass


@register
def enchant_608(char: CharacterProperty):
    # DCALC_REMOVE: enchant_608
    # 全属强(35)|技攻(1%)
    char.AddElementDB('火', 35)
    char.AddElementDB('冰', 35)
    char.AddElementDB('光', 35)
    char.AddElementDB('暗', 35)
    char.SetStatus(技攻=0.01)
    pass

@register
def enchant_609(char: CharacterProperty):
    # DCALC_REMOVE: enchant_609
    # 全属强(35)|技攻(2%)
    char.AddElementDB('火', 35)
    char.AddElementDB('冰', 35)
    char.AddElementDB('光', 35)
    char.AddElementDB('暗', 35)
    char.SetStatus(技攻=0.02)
    pass

@register
def enchant_610(char: CharacterProperty):
    # DCALC_REMOVE: enchant_610
    # 四维(120)|奶系Lv15被动+1
    char.SetStatus(四维=120)
    if char.buffer:
        char.AddSkillLv(15, 15, 1, 0)
    pass

# endregion
# region 辅助装备


@register
def enchant_900(char: CharacterProperty):
    # DCALC_REMOVE: enchant_900
    # 三攻(110)
    char.SetStatus(三攻=110)
    pass


@register
def enchant_901(char: CharacterProperty):
    # DCALC_REMOVE: enchant_901
    # 四维(100)
    char.SetStatus(四维=100)
    pass


@register
def enchant_902(char: CharacterProperty):
    # DCALC_REMOVE: enchant_902
    # 攻强(3%)|全属强(11)|暴击率(3%)
    char.SetStatus(攻击强化P=0.03)
    char.AddElementDB('火', 11)
    char.AddElementDB('冰', 11)
    char.AddElementDB('光', 11)
    char.AddElementDB('暗', 11)
    pass


@register
def enchant_903(char: CharacterProperty):
    # DCALC_REMOVE: enchant_903
    # 四维(100)|奶系Lv15被动+3
    char.SetStatus(四维=100)
    if char.buffer:
        char.AddSkillLv(15, 15, 3, 0)
    pass


@register
def enchant_904(char: CharacterProperty):
    # DCALC_REMOVE: enchant_904
    # 技攻(5%)|全属强(15)|暴击率(5%)
    char.SetStatus(技攻=0.05)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    pass


@register
def enchant_905(char: CharacterProperty):
    # DCALC_REMOVE: enchant_905
    # 技攻(7%)|全属强(15)|暴击率(5%)
    char.SetStatus(技攻=0.07)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    pass

@register
def enchant_906(char: CharacterProperty):
    # DCALC_REMOVE: enchant_906
    # 攻击强化(1%)|全属强(8)|暴击率(3%)
    char.SetStatus(攻击强化P=0.01)
    char.AddElementDB('火', 8)
    char.AddElementDB('冰', 8)
    char.AddElementDB('光', 8)
    char.AddElementDB('暗', 8)
    pass

@register
def enchant_907(char: CharacterProperty):
    # DCALC_REMOVE: enchant_907
    # 攻击强化(3%)|全属强(12)|暴击率(3%)
    char.SetStatus(攻击强化P=0.03)
    char.AddElementDB('火', 12)
    char.AddElementDB('冰', 12)
    char.AddElementDB('光', 12)
    char.AddElementDB('暗', 12)
    pass

# endregion
# region 魔法石


@register
def enchant_1000(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1000
    # 全属强(30)
    char.AddElementDB('火', 30)
    char.AddElementDB('冰', 30)
    char.AddElementDB('光', 30)
    char.AddElementDB('暗', 30)
    pass


@register
def enchant_1001(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1001
    # 全属强(35)
    char.AddElementDB('火', 35)
    char.AddElementDB('冰', 35)
    char.AddElementDB('光', 35)
    char.AddElementDB('暗', 35)
    pass


@register
def enchant_1002(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1002
    # 四维(100)|奶系Lv15被动+3
    char.SetStatus(四维=100)
    if char.buffer:
        char.AddSkillLv(15, 15, 3, 0)
    pass


@register
def enchant_1003(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1003
    # 全属强(40)
    char.AddElementDB('火', 40)
    char.AddElementDB('冰', 40)
    char.AddElementDB('光', 40)
    char.AddElementDB('暗', 40)
    pass


@register
def enchant_1004(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1004
    # 四维(120)|奶系Lv15被动+3
    char.SetStatus(四维=120)
    if char.buffer:
        char.AddSkillLv(15, 15, 3, 0)
    pass


# endregion
# region 耳环


@register
def enchant_1100(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1100
    # 四维(50)|全属强(11)
    char.SetStatus(四维=50)
    char.AddElementDB('火', 11)
    char.AddElementDB('冰', 11)
    char.AddElementDB('光', 11)
    char.AddElementDB('暗', 11)
    pass


@register
def enchant_1101(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1101
    # 四维(175)
    char.SetStatus(四维=175)
    pass


@register
def enchant_1102(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1102
    # 四维(70)|全属强(15)
    char.SetStatus(四维=70)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    pass


@register
def enchant_1103(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1103
    # 四维(200)
    char.SetStatus(四维=200)
    pass

@register
def enchant_1104(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1104
    # 四维(100)|全属强(25)
    char.AddElementDB('火', 40)
    char.AddElementDB('冰', 40)
    char.AddElementDB('光', 40)
    char.AddElementDB('暗', 40)
    pass

@register
def enchant_1105(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1105
    # 四维(250)
    char.SetStatus(四维=250)
    pass

# endregion
# region 称号


@register
def enchant_1200(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1200
    # 三攻(40)|全属强(15)|Lv1~50主动+1
    char.SetStatus(三攻=40)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.AddSkillLv(1, 50, 1, 1)
    pass


@register
def enchant_1201(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1201
    # 三攻(40)|全属强(15)|技攻(3%)
    char.SetStatus(三攻=40, 技攻=0.03)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    pass


@register
def enchant_1202(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1202
    # Lv40主动+2|三攻(40)|全属强(15)|技攻(3%)
    char.SetStatus(三攻=40, 技攻=0.03)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.AddSkillLv(40, 40, 2, 1,["念兽 : 龙虎啸", "风雷啸", "圣灵符文", "神圣之光"])
    pass


@register
def enchant_1203(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1203
    # Lv45主动+2|三攻(40)|全属强(15)|技攻(3%)
    char.SetStatus(三攻=40, 技攻=0.03)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.AddSkillLv(45, 45, 2, 1,["念兽 : 龙虎啸", "风雷啸", "圣灵符文", "神圣之光"])
    pass


@register
def enchant_1204(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1204
    # Lv60主动+2|三攻(40)|全属强(15)|技攻(3%)
    char.SetStatus(三攻=40, 技攻=0.03)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.AddSkillLv(60, 60, 2, 1,["念兽 : 龙虎啸", "风雷啸", "圣灵符文", "神圣之光"])
    pass


@register
def enchant_1205(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1205
    # Lv70主动+2|三攻(40)|全属强(15)|技攻(3%)
    char.SetStatus(三攻=40, 技攻=0.03)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.AddSkillLv(70, 70, 2, 1,["念兽 : 龙虎啸", "风雷啸", "圣灵符文", "神圣之光"])
    pass


@register
def enchant_1206(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1206
    # Lv75主动+2|三攻(40)|全属强(15)|技攻(3%)
    char.SetStatus(三攻=40, 技攻=0.03)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.AddSkillLv(75, 75, 2, 1,["念兽 : 龙虎啸", "风雷啸", "圣灵符文", "神圣之光"])
    pass


@register
def enchant_1207(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1207
    # Lv80主动+2|三攻(40)|全属强(15)|技攻(3%)
    char.SetStatus(三攻=40, 技攻=0.03)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.AddSkillLv(80, 80, 2, 1,["念兽 : 龙虎啸", "风雷啸", "圣灵符文", "神圣之光"])
    pass


@register
def enchant_1208(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1208
    # Lv30增益技能等级 +1
    if char.buffer:
        char.AddSkillLv(30, 30, 1, 1)
    pass


@register
def enchant_1209(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1209
    # Lv30增益技能等级 +2
    if char.buffer:
        char.AddSkillLv(30, 30, 2, 1)
    pass


@register
def enchant_1210(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1210
    # Lv50主动技能等级 +1
    if char.buffer:
        char.AddSkillLv(50, 50, 1, 1)
    pass


@register
def enchant_1211(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1211
    # Lv50主动技能等级 +2
    if char.buffer:
        char.AddSkillLv(50, 50, 2, 1)
    pass


# endregion
# region 宠物


@register
def enchant_1300(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1300
    # 火强(25)
    char.AddElementDB('火', 25)
    pass


@register
def enchant_1301(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1301
    # 冰强(25)
    char.AddElementDB('冰', 25)
    pass


@register
def enchant_1302(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1302
    # 光强(25)
    char.AddElementDB('光', 25)
    pass


@register
def enchant_1303(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1303
    # 暗强(25)
    char.AddElementDB('暗', 25)
    pass


@register
def enchant_1304(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1304
    # 全属强(23)
    char.AddElementDB('火', 23)
    char.AddElementDB('冰', 23)
    char.AddElementDB('光', 23)
    char.AddElementDB('暗', 23)
    pass


@register
def enchant_1305(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1305
    # 力量(50)
    char.SetStatus(力量=50)
    pass


@register
def enchant_1306(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1306
    # 智力(50)
    char.SetStatus(智力=50)
    pass


@register
def enchant_1307(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1307
    # 精神(50)
    char.SetStatus(精神=50)
    pass


@register
def enchant_1308(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1308
    # 体力(50)
    char.SetStatus(体力=50)
    pass


@register
def enchant_1309(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1309
    # 物攻(60)
    char.SetStatus(物攻=60)
    pass


@register
def enchant_1310(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1310
    # 魔攻(60)
    char.SetStatus(魔攻=60)
    pass


@register
def enchant_1311(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1311
    # 独立(60)
    char.SetStatus(独立=60)
    pass


@register
def enchant_1312(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1312
    # 火强(16)
    char.AddElementDB('火', 16)
    pass


@register
def enchant_1313(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1313
    # 冰强(16)
    char.AddElementDB('冰', 16)
    pass


@register
def enchant_1314(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1314
    # 光强(16)
    char.AddElementDB('光', 16)
    pass


@register
def enchant_1315(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1315
    # 暗强(16)
    char.AddElementDB('暗', 16)
    pass


@register
def enchant_1316(char: CharacterProperty):
    # DCALC_REMOVE: enchant_1316
    # 全属强(14)
    char.AddElementDB('火', 14)
    char.AddElementDB('冰', 14)
    char.AddElementDB('光', 14)
    char.AddElementDB('暗', 14)
    pass


# endregion
# region 光环


@register
def enchant_2000(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2000
    # Lv1~95+1|攻击强化(12%)|增益量(7%)
    char.SetStatus(攻击强化P=0.12,增益量P=0.07)
    char.AddSkillLv(1, 95, 1)
    pass


@register
def enchant_2001(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2001
    # Lv1~95+1|攻击强化(7%)|增益量(5%)
    char.SetStatus(攻击强化P=0.07,增益量P=0.05)
    char.AddSkillLv(1, 95, 1)
    pass


@register
def enchant_2002(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2002
    # Lv1~35+1|攻击强化(5%)|增益量(3%)
    char.SetStatus(攻击强化P=0.05,增益量P=0.03)
    char.AddSkillLv(1, 35, 1)
    pass


# endregion
# region 武器装扮


@register
def enchant_2100(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2100
    # Lv40主动+1|四维(55)
    char.AddSkillLv(40, 40, 1, 1,["念兽 : 龙虎啸", "风雷啸", "圣灵符文", "神圣之光"])
    char.SetStatus(四维=55)
    pass


@register
def enchant_2101(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2101
    # Lv45主动+1|四维(55)
    char.AddSkillLv(45, 45, 1, 1,["念兽 : 龙虎啸", "风雷啸", "圣灵符文", "神圣之光"])
    char.SetStatus(四维=55)
    pass


@register
def enchant_2102(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2102
    # Lv60主动+1|四维(55)
    char.AddSkillLv(60, 60, 1, 1,["念兽 : 龙虎啸", "风雷啸", "圣灵符文", "神圣之光"])
    char.SetStatus(四维=55)
    pass


@register
def enchant_2103(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2103
    # Lv70主动+1|四维(55)
    char.AddSkillLv(70, 70, 1, 1,["念兽 : 龙虎啸", "风雷啸", "圣灵符文", "神圣之光"])
    char.SetStatus(四维=55)
    pass


@register
def enchant_2104(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2104
    # Lv75主动+1|四维(55)
    char.AddSkillLv(75, 75, 1, 1,["念兽 : 龙虎啸", "风雷啸", "圣灵符文", "神圣之光"])
    char.SetStatus(四维=55)
    pass


@register
def enchant_2105(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2105
    # Lv80主动+1|四维(55)
    char.AddSkillLv(80, 80, 1, 1,["念兽 : 龙虎啸", "风雷啸", "圣灵符文", "神圣之光"])
    char.SetStatus(四维=55)
    pass


# endregion
# region 皮肤


@register
def enchant_2200(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2200
    # Lv40主动+1|全属强(12)|四维(55)
    char.AddSkillLv(40, 40, 1, 1, exceptSkills=["念兽 : 龙虎啸", "风雷啸", "圣灵符文", "神圣之光"])
    char.SetStatus(四维=55)
    char.AddElementDB('火', 12)
    char.AddElementDB('冰', 12)
    char.AddElementDB('光', 12)
    char.AddElementDB('暗', 12)
    pass


@register
def enchant_2201(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2201
    # Lv45主动+1|全属强(12)|四维(55)
    char.AddSkillLv(45, 45, 1, 1, exceptSkills=["念兽 : 龙虎啸", "风雷啸", "圣灵符文", "神圣之光"])
    char.SetStatus(四维=55)
    char.AddElementDB('火', 12)
    char.AddElementDB('冰', 12)
    char.AddElementDB('光', 12)
    char.AddElementDB('暗', 12)
    pass


@register
def enchant_2202(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2202
    # Lv60主动+1|全属强(12)|四维(55)
    char.AddSkillLv(60, 60, 1, 1, exceptSkills=["念兽 : 龙虎啸", "风雷啸", "圣灵符文", "神圣之光"])
    char.SetStatus(四维=55)
    char.AddElementDB('火', 12)
    char.AddElementDB('冰', 12)
    char.AddElementDB('光', 12)
    char.AddElementDB('暗', 12)
    pass


@register
def enchant_2203(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2203
    # Lv70主动+1|全属强(12)|四维(55)
    char.AddSkillLv(70, 70, 1, 1, exceptSkills=["念兽 : 龙虎啸", "风雷啸", "圣灵符文", "神圣之光"])
    char.SetStatus(四维=55)
    char.AddElementDB('火', 12)
    char.AddElementDB('冰', 12)
    char.AddElementDB('光', 12)
    char.AddElementDB('暗', 12)
    pass


@register
def enchant_2204(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2204
    # Lv75主动+1|全属强(12)|四维(55)
    char.AddSkillLv(75, 75, 1, 1, exceptSkills=["念兽 : 龙虎啸", "风雷啸", "圣灵符文", "神圣之光"])
    char.SetStatus(四维=55)
    char.AddElementDB('火', 12)
    char.AddElementDB('冰', 12)
    char.AddElementDB('光', 12)
    char.AddElementDB('暗', 12)
    pass


@register
def enchant_2205(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2205
    # Lv80主动+1|全属强(12)|四维(55)
    char.AddSkillLv(80, 80, 1, 1 , exceptSkills=["念兽 : 龙虎啸", "风雷啸", "圣灵符文", "神圣之光"])
    char.SetStatus(四维=55)
    char.AddElementDB('火', 12)
    char.AddElementDB('冰', 12)
    char.AddElementDB('光', 12)
    char.AddElementDB('暗', 12)
    pass


@register
def enchant_2206(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2206
    # 全属强(6)
    char.AddElementDB('火', 6)
    char.AddElementDB('冰', 6)
    char.AddElementDB('光', 6)
    char.AddElementDB('暗', 6)
    pass


# endregion
# region 宠物装备-红


@register
def enchant_2500(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2500
    # 攻击强化(10%)
    char.SetStatus(攻击强化P=0.1)
    pass


@register
def enchant_2501(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2501
    # 攻击强化(8%)
    char.SetStatus(攻击强化P=0.08)
    pass


@register
def enchant_2502(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2502
    # 攻击强化(4%)|全属强(6)
    char.SetStatus(攻击强化P=0.04)
    char.AddElementDB('火', 6)
    char.AddElementDB('冰', 6)
    char.AddElementDB('光', 6)
    char.AddElementDB('暗', 6)
    pass


@register
def enchant_2503(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2503
    # 攻击强化(4%)|全属强(4)|光强(4)
    char.SetStatus(攻击强化P=0.04)
    char.AddElementDB('火', 4)
    char.AddElementDB('冰', 4)
    char.AddElementDB('光', 8)
    char.AddElementDB('暗', 4)
    pass


@register
def enchant_2504(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2504
    # 攻击强化(4%)|全属强(4)|火强(4)
    char.SetStatus(攻击强化P=0.04)
    char.AddElementDB('火', 8)
    char.AddElementDB('冰', 4)
    char.AddElementDB('光', 4)
    char.AddElementDB('暗', 4)
    pass


@register
def enchant_2505(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2505
    # 攻击强化(4%)|全属强(4)|冰强(4)
    char.SetStatus(攻击强化P=0.04)
    char.AddElementDB('火', 6)
    char.AddElementDB('冰', 6)
    char.AddElementDB('光', 6)
    char.AddElementDB('暗', 6)
    pass


@register
def enchant_2506(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2506
    # 攻击强化(4%)|全属强(4)|暗强(4)
    char.SetStatus(攻击强化P=0.04)
    char.AddElementDB('火', 4)
    char.AddElementDB('冰', 4)
    char.AddElementDB('光', 8)
    char.AddElementDB('暗', 4)
    pass


@register
def enchant_2507(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2507
    # 四维(33)
    char.SetStatus(四维=33)
    pass


@register
def enchant_2508(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2508
    # 四维(25)
    char.SetStatus(四维=25)
    pass


@register
def enchant_2509(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2509
    # 四维(50)
    char.SetStatus(四维=50)
    pass


# endregion
# region 宠物装备-绿


@register
def enchant_2600(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2600
    # 三攻(40)|全属强(30)
    char.SetStatus(三攻=40)
    char.AddElementDB('火', 30)
    char.AddElementDB('冰', 30)
    char.AddElementDB('光', 30)
    char.AddElementDB('暗', 30)
    pass


@register
def enchant_2601(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2601
    # 三攻(40)|全属强(20)
    char.SetStatus(三攻=40)
    char.AddElementDB('火', 20)
    char.AddElementDB('冰', 20)
    char.AddElementDB('光', 20)
    char.AddElementDB('暗', 20)
    pass


@register
def enchant_2602(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2602
    # 四维(50)|全属强(20)
    char.SetStatus(四维=50)
    char.AddElementDB('火', 20)
    char.AddElementDB('冰', 20)
    char.AddElementDB('光', 20)
    char.AddElementDB('暗', 20)
    pass


@register
def enchant_2603(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2603
    # 四维(30)|全属强(20)
    char.SetStatus(四维=30)
    char.AddElementDB('火', 20)
    char.AddElementDB('冰', 20)
    char.AddElementDB('光', 20)
    char.AddElementDB('暗', 20)
    pass


@register
def enchant_2604(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2604
    # 四维(30)
    char.SetStatus(四维=30)
    pass


@register
def enchant_2605(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2605
    # 四维(16)
    char.SetStatus(四维=16)
    pass


# endregion
# region 宠物装备-蓝


@register
def enchant_2606(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2606
    # 技攻(2%)|三速(5%)
    char.SetStatus(技攻=0.02, 三速=0.05)
    pass


@register
def enchant_2607(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2607
    # 三攻(30)|三速(4%)
    char.SetStatus(三攻=30, 三速=0.04)
    pass


@register
def enchant_2608(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2608
    # 三攻(30)
    char.SetStatus(三攻=30)
    pass


@register
def enchant_2609(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2609
    # 三攻(25)|三速(2%)|属性攻击|暴击(5%)
    char.SetStatus(三攻=25, 三速=0.02)
    pass


@register
def enchant_2610(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2610
    # 四维(50)|三速(4%)
    char.SetStatus(四维=50, 三速=0.04)
    pass


@register
def enchant_2611(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2611
    # 四维(25)|三速(2%)
    char.SetStatus(四维=25, 三速=0.02)
    pass


@register
def enchant_2612(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2612
    # 四维(20)|三速(2%)
    char.SetStatus(四维=20, 三速=0.02)
    pass


# endregion
# region 快捷栏装备


@register
def enchant_2700(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2700
    # 三攻(30)|攻击强化(10%)
    char.SetStatus(三攻=30, 攻击强化P=0.1)
    pass


@register
def enchant_2701(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2701
    # 三攻(30)|攻击强化(8%)
    char.SetStatus(三攻=30, 攻击强化P=0.08)
    pass


@register
def enchant_2702(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2702
    # 四维(8)|攻击强化(8%)
    char.SetStatus(四维=8, 攻击强化P=0.08)
    pass


@register
def enchant_2703(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2703
    # 四维(5)|攻击强化(8%)|攻速(8%)
    char.SetStatus(四维=5, 攻击强化P=0.08, 攻速=0.08)
    pass


@register
def enchant_2704(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2704
    # 三攻(30)|三速(5%)
    char.SetStatus(三攻=30, 三速=0.05)
    pass


@register
def enchant_2705(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2705
    # 三攻(30)|三速(5%)|增益量(1%)
    char.SetStatus(三攻=30, 三速=0.05, 增益量P=0.01)
    pass


@register
def enchant_2706(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2706
    # 四维(50)
    char.SetStatus(四维=50)
    pass


@register
def enchant_2707(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2707
    # 四维(50)|三速(5%)
    char.SetStatus(四维=50, 三速=0.05)
    pass


@register
def enchant_2708(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2708
    # 四维(50)|三速(5%)|增益量(1%)
    char.SetStatus(四维=50, 三速=0.05, 增益量P=0.01)
    pass


@register
def enchant_2709(char: CharacterProperty):
    # DCALC_REMOVE: enchant_2709
    # 三攻(50)|四维(100)|增益量(3%)|攻击强化(15%)|三速(5%)
    char.SetStatus(三攻=50, 四维=100, 三速=0.05, 攻击强化P=0.15, 增益量P=0.03)
    pass



# endregion
