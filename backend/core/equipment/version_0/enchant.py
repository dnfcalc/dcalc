from core.abstract.character import CharacterProperty

enchant_func_list = {}

# region 头肩


def enchant_1(char: CharacterProperty):
    """
    三攻(10)|四维(40)|技攻(3%)|暴击率(5%)
    """
    char.SetStatus(三攻=10, 四维=40, 技攻=0.03)
    pass


def enchant_2(char: CharacterProperty):
    """
    三攻(20)|四维(75)|Lv1~50主动+1
    """
    char.SetStatus(三攻=20, 四维=75)
    char.AddSkillLv(1, 50, 1, 1)
    pass


def enchant_3(char: CharacterProperty):
    """
    三攻(20)|四维(75)|技攻(5%)
    """
    char.SetStatus(三攻=20, 四维=75, 技攻=0.05)
    pass


def enchant_4(char: CharacterProperty):
    """
    Lv30增益技能等级 +1|lv50主动技能等级+1
    """
    if char.buffer:
        char.AddSkillLv(30, 1, 1, 1)
        char.AddSkillLv(50, 1, 1, 1)
    pass


# endregion
# region 上衣


def enchant_100(char: CharacterProperty):
    """
    三攻(110)|力智(80)
    """
    char.SetStatus(三攻=110, 力智=80)
    pass


def enchant_101(char: CharacterProperty):
    """
    四维(100)|奶系Lv15被动+3
    """
    char.SetStatus(四维=100)
    if char.buffer:
        char.AddSkillLv(15, 15, 3, 1)
    pass


def enchant_102(char: CharacterProperty):
    """
    四维(120)|奶系Lv15被动+3
    """
    char.SetStatus(四维=120)
    if char.buffer:
        char.AddSkillLv(15, 15, 3, 1)
    pass


def enchant_103(char: CharacterProperty):
    """
    三攻(110)|力智(90)|技攻(1%)
    """
    char.SetStatus(三攻=110, 力智=90, 技攻=0.01)
    pass


def enchant_104(char: CharacterProperty):
    """
    四维(125)|奶系Lv15被动+4
    """
    char.SetStatus(四维=125)
    if char.buffer:
        char.AddSkillLv(15, 15, 4, 1)
    pass


def enchant_105(char: CharacterProperty):
    """
    三攻(110)|力智(90)|技攻(2%)
    """
    char.SetStatus(三攻=110, 力智=90, 技攻=0.02)
    pass


# endregion
# region 头肩


def enchant_106(char: CharacterProperty):
    """
    四维(120)|奶系Lv15被动+3
    """
    char.SetStatus(四维=120)
    if char.buffer:
        char.AddSkillLv(15, 15, 3, 1)
    pass


# endregion
# region 武器


def enchant_107(char: CharacterProperty):
    """
    独立(90)|力智(60)
    """
    char.SetStatus(独立=90, 力智=60)
    pass


def enchant_108(char: CharacterProperty):
    """
    魔攻(90)|力智(60)
    """
    char.SetStatus(魔攻=90, 力智=60)
    pass


def enchant_109(char: CharacterProperty):
    """
    物攻(90)|力智(60)
    """
    char.SetStatus(物攻=90, 力智=60)
    pass


def enchant_110(char: CharacterProperty):
    """
    智力(100)
    """
    char.SetStatus(智力=100)
    pass


def enchant_111(char: CharacterProperty):
    """
    力量(100)
    """
    char.SetStatus(力量=100)
    pass


def enchant_112(char: CharacterProperty):
    """
    体力(100)
    """
    char.SetStatus(体力=100)
    pass


def enchant_113(char: CharacterProperty):
    """
    精神(100)
    """
    char.SetStatus(精神=100)
    pass


# endregion
# region 下装


def enchant_200(char: CharacterProperty):
    """
    三攻(110)|力智(80)
    """
    char.SetStatus(三攻=110, 力智=80)
    pass


def enchant_201(char: CharacterProperty):
    """
    四维(125)|奶系Lv15被动+4
    """
    char.SetStatus(四维=125)
    if char.buffer:
        char.AddSkillLv(15, 15, 4, 1)
    pass


def enchant_202(char: CharacterProperty):
    """
    三攻(110)|力智(90)|技攻(2%)
    """
    char.SetStatus(三攻=110, 力智=90, 技攻=0.02)
    pass


# endregion
# region 腰带


def enchant_300(char: CharacterProperty):
    """
    三攻(30)|技攻(1%)
    """
    char.SetStatus(三攻=30, 技攻=0.01)
    pass


def enchant_301(char: CharacterProperty):
    """
    三攻(10)|四维(40)|技攻(2%)
    """
    char.SetStatus(三攻=10, 四维=40, 技攻=0.02)
    pass


def enchant_302(char: CharacterProperty):
    """
    四维(45)|Lv1~50主动+1
    """
    char.SetStatus(四维=45)
    if char.buffer:
        char.AddSkillLv(1, 50, 1, 1)
    pass


def enchant_303(char: CharacterProperty):
    """
    三攻(36)|技能伤害(5%)|暴击率(3%)
    """
    char.SetStatus(三攻=36, 技能伤害=0.05)
    pass


# endregion
# region 武器


def enchant_500(char: CharacterProperty):
    """
    火强(15)
    """
    char.AddElementDB('火', 15)
    pass


def enchant_501(char: CharacterProperty):
    """
    冰强(15)
    """
    char.AddElementDB('冰', 15)
    pass


def enchant_502(char: CharacterProperty):
    """
    光强(15)
    """
    char.AddElementDB('光', 15)
    pass


def enchant_503(char: CharacterProperty):
    """
    暗强(15)
    """
    char.AddElementDB('暗', 15)
    pass


def enchant_504(char: CharacterProperty):
    """
    火强(15)|光强(15)
    """
    char.AddElementDB('火', 15)
    char.AddElementDB('光', 15)
    pass


def enchant_505(char: CharacterProperty):
    """
    冰强(15)|暗强(15)
    """
    char.AddElementDB('冰', 15)
    char.AddElementDB('暗', 15)
    pass


def enchant_506(char: CharacterProperty):
    """
    火强(15)|冰强(15)
    """
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    pass


def enchant_507(char: CharacterProperty):
    """
    所有属性强化(13)
    """
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    pass


def enchant_508(char: CharacterProperty):
    """
    物攻(30)|独立(30)|全属强(15)|攻速(5%)
    """
    char.SetStatus(物攻=30, 独立=30, 攻速=0.05)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    pass


def enchant_509(char: CharacterProperty):
    """
    魔攻(30)|独立(30)|全属强(15)|施放(6%)
    """
    char.SetStatus(魔攻=30, 独立=30, 施放=0.06)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    pass


def enchant_510(char: CharacterProperty):
    """
    三攻(30)|全属强(15)
    """
    char.SetStatus(三攻=30)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    pass


def enchant_511(char: CharacterProperty):
    """
    四维(110)|施放(7%)
    """
    char.SetStatus(四维=110, 施放速度=0.07)
    pass


def enchant_512(char: CharacterProperty):
    """
    三攻(50)|全属强(16)|属性攻击
    """
    char.SetStatus(三攻=50)
    char.AddElementDB('火', 16)
    char.AddElementDB('冰', 16)
    char.AddElementDB('光', 16)
    char.AddElementDB('暗', 16)
    pass


# endregion
# region 项链


def enchant_600(char: CharacterProperty):
    """
    所有属性强化(30)
    """
    char.AddElementDB('火', 30)
    char.AddElementDB('冰', 30)
    char.AddElementDB('光', 30)
    char.AddElementDB('暗', 30)
    pass


def enchant_601(char: CharacterProperty):
    """
    所有属性强化(28)
    """
    char.AddElementDB('火', 28)
    char.AddElementDB('冰', 28)
    char.AddElementDB('光', 28)
    char.AddElementDB('暗', 28)
    pass


def enchant_602(char: CharacterProperty):
    """
    四维(70)
    """
    char.SetStatus(四维=70)
    pass


def enchant_603(char: CharacterProperty):
    """
    所有属性强化(33)
    """
    char.AddElementDB('火', 33)
    char.AddElementDB('冰', 33)
    char.AddElementDB('光', 33)
    char.AddElementDB('暗', 33)
    pass


def enchant_604(char: CharacterProperty):
    """
    火强(35)|光强(35)
    """
    char.AddElementDB('火', 35)
    char.AddElementDB('光', 35)
    pass


def enchant_605(char: CharacterProperty):
    """
    冰强(35)|暗强(35)
    """
    char.AddElementDB('冰', 35)
    char.AddElementDB('暗', 35)
    pass


def enchant_606(char: CharacterProperty):
    """
    四维(90)
    """
    char.SetStatus(四维=90)
    pass


def enchant_607(char: CharacterProperty):
    """
    四维(100)|奶系Lv15被动+1
    """
    char.SetStatus(四维=100)
    if char.buffer:
        char.AddSkillLv(15, 15, 1, 1)
    pass


def enchant_608(char: CharacterProperty):
    """
    全属强(35)|技攻(1%)
    """
    char.AddElementDB('火', 35)
    char.AddElementDB('冰', 35)
    char.AddElementDB('光', 35)
    char.AddElementDB('暗', 35)
    char.SetStatus(技攻=0.01)
    pass


# endregion
# region 辅助装备


def enchant_900(char: CharacterProperty):
    """
    三攻(110)
    """
    char.SetStatus(三攻=110)
    pass


def enchant_901(char: CharacterProperty):
    """
    四维(100)
    """
    char.SetStatus(四维=100)
    pass


def enchant_902(char: CharacterProperty):
    """
    攻强(3%)|所有属性强化(11)|暴击率(3%)
    """
    char.SetStatus(攻击强化P=0.03)
    char.AddElementDB('火', 11)
    char.AddElementDB('冰', 11)
    char.AddElementDB('光', 11)
    char.AddElementDB('暗', 11)
    pass


def enchant_903(char: CharacterProperty):
    """
    四维(100)|奶系Lv15被动+3
    """
    char.SetStatus(四维=100)
    if char.buffer:
        char.AddSkillLv(15, 15, 3, 1)
    pass


def enchant_904(char: CharacterProperty):
    """
    技攻(5%)|所有属性强化(15)|暴击率(5%)
    """
    char.SetStatus(技攻=0.05)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    pass


def enchant_905(char: CharacterProperty):
    """
    技攻(7%)|所有属性强化(15)|暴击率(5%)
    """
    char.SetStatus(技攻=0.07)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    pass


# endregion
# region 魔法石


def enchant_1000(char: CharacterProperty):
    """
    所有属性强化(30)
    """
    char.AddElementDB('火', 30)
    char.AddElementDB('冰', 30)
    char.AddElementDB('光', 30)
    char.AddElementDB('暗', 30)
    pass


def enchant_1001(char: CharacterProperty):
    """
    所有属性强化(35)
    """
    char.AddElementDB('火', 35)
    char.AddElementDB('冰', 35)
    char.AddElementDB('光', 35)
    char.AddElementDB('暗', 35)
    pass


def enchant_1002(char: CharacterProperty):
    """
    四维(100)|奶系Lv15被动+3
    """
    char.SetStatus(四维=100)
    if char.buffer:
        char.AddSkillLv(15, 15, 3, 1)
    pass


def enchant_1003(char: CharacterProperty):
    """
    所有属性强化(40)
    """
    char.AddElementDB('火', 40)
    char.AddElementDB('冰', 40)
    char.AddElementDB('光', 40)
    char.AddElementDB('暗', 40)
    pass


def enchant_1004(char: CharacterProperty):
    """
    四维(120)|奶系Lv15被动+3
    """
    char.SetStatus(四维=120)
    if char.buffer:
        char.AddSkillLv(15, 15, 3, 1)
    pass


# endregion
# region 耳环


def enchant_1100(char: CharacterProperty):
    """
    四维(50)|所有属性强化(11)
    """
    char.SetStatus(四维=50)
    char.AddElementDB('火', 11)
    char.AddElementDB('冰', 11)
    char.AddElementDB('光', 11)
    char.AddElementDB('暗', 11)
    pass


def enchant_1101(char: CharacterProperty):
    """
    四维(175)
    """
    char.SetStatus(四维=175)
    pass


def enchant_1102(char: CharacterProperty):
    """
    四维(70)|所有属性强化(15)
    """
    char.SetStatus(四维=70)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    pass


def enchant_1103(char: CharacterProperty):
    """
    四维(200)
    """
    char.SetStatus(四维=200)
    pass


# endregion
# region 称号


def enchant_1200(char: CharacterProperty):
    """
    三攻(40)|所有属性强化(15)|Lv1~50主动+1
    """
    char.SetStatus(三攻=40)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.AddSkillLv(1, 50, 1, 1)
    pass


def enchant_1201(char: CharacterProperty):
    """
    三攻(40)|所有属性强化(15)|技攻(3%)
    """
    char.SetStatus(三攻=40, 技攻=0.03)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    pass


def enchant_1202(char: CharacterProperty):
    """
    Lv40主动+2|三攻(40)|所有属性强化(15)|技攻(3%)
    """
    char.SetStatus(三攻=40, 技攻=0.03)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.AddSkillLv(40, 40, 2, 1)
    pass


def enchant_1203(char: CharacterProperty):
    """
    Lv45主动+2|三攻(40)|所有属性强化(15)|技攻(3%)
    """
    char.SetStatus(三攻=40, 技攻=0.03)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.AddSkillLv(45, 45, 2, 1)
    pass


def enchant_1204(char: CharacterProperty):
    """
    Lv60主动+2|三攻(40)|所有属性强化(15)|技攻(3%)
    """
    char.SetStatus(三攻=40, 技攻=0.03)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.AddSkillLv(60, 60, 2, 1)
    pass


def enchant_1205(char: CharacterProperty):
    """
    Lv70主动+2|三攻(40)|所有属性强化(15)|技攻(3%)
    """
    char.SetStatus(三攻=40, 技攻=0.03)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.AddSkillLv(70, 70, 2, 1)
    pass


def enchant_1206(char: CharacterProperty):
    """
    Lv75主动+2|三攻(40)|所有属性强化(15)|技攻(3%)
    """
    char.SetStatus(三攻=40, 技攻=0.03)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.AddSkillLv(75, 75, 2, 1)
    pass


def enchant_1207(char: CharacterProperty):
    """
    Lv80主动+2|三攻(40)|所有属性强化(15)|技攻(3%)
    """
    char.SetStatus(三攻=40, 技攻=0.03)
    char.AddElementDB('火', 15)
    char.AddElementDB('冰', 15)
    char.AddElementDB('光', 15)
    char.AddElementDB('暗', 15)
    char.AddSkillLv(80, 80, 2, 1)
    pass


def enchant_1208(char: CharacterProperty):
    """
    Lv30增益技能等级 +1
    """
    if char.buffer:
        char.AddSkillLv(30, 30, 1, 1)
    pass


def enchant_1209(char: CharacterProperty):
    """
    Lv30增益技能等级 +2
    """
    if char.buffer:
        char.AddSkillLv(30, 30, 2, 1)
    pass


def enchant_1210(char: CharacterProperty):
    """
    Lv50主动技能等级 +1
    """
    if char.buffer:
        char.AddSkillLv(50, 50, 1, 1)
    pass


def enchant_1211(char: CharacterProperty):
    """
    Lv50主动技能等级 +2
    """
    if char.buffer:
        char.AddSkillLv(50, 50, 2, 1)
    pass


# endregion
# region 宠物


def enchant_1300(char: CharacterProperty):
    """
    火强(25)
    """
    char.AddElementDB('火', 25)
    pass


def enchant_1301(char: CharacterProperty):
    """
    冰强(25)
    """
    char.AddElementDB('冰', 25)
    pass


def enchant_1302(char: CharacterProperty):
    """
    光强(25)
    """
    char.AddElementDB('光', 25)
    pass


def enchant_1303(char: CharacterProperty):
    """
    暗强(25)
    """
    char.AddElementDB('暗', 25)
    pass


def enchant_1304(char: CharacterProperty):
    """
    所有属性强化(23)
    """
    char.AddElementDB('火', 23)
    char.AddElementDB('冰', 23)
    char.AddElementDB('光', 23)
    char.AddElementDB('暗', 23)
    pass


def enchant_1305(char: CharacterProperty):
    """
    力量(50)
    """
    char.SetStatus(力量=50)
    pass


def enchant_1306(char: CharacterProperty):
    """
    智力(50)
    """
    char.SetStatus(智力=50)
    pass


def enchant_1307(char: CharacterProperty):
    """
    精神(50)
    """
    char.SetStatus(精神=50)
    pass


def enchant_1308(char: CharacterProperty):
    """
    体力(50)
    """
    char.SetStatus(体力=50)
    pass


def enchant_1309(char: CharacterProperty):
    """
    物攻(60)
    """
    char.SetStatus(物攻=60)
    pass


def enchant_1310(char: CharacterProperty):
    """
    魔攻(60)
    """
    char.SetStatus(魔攻=60)
    pass


def enchant_1311(char: CharacterProperty):
    """
    独立(60)
    """
    char.SetStatus(独立=60)
    pass


def enchant_1312(char: CharacterProperty):
    """
    火强(16)
    """
    char.AddElementDB('火', 16)
    pass


def enchant_1313(char: CharacterProperty):
    """
    冰强(16)
    """
    char.AddElementDB('冰', 16)
    pass


def enchant_1314(char: CharacterProperty):
    """
    光强(16)
    """
    char.AddElementDB('光', 16)
    pass


def enchant_1315(char: CharacterProperty):
    """
    暗强(16)
    """
    char.AddElementDB('暗', 16)
    pass


def enchant_1316(char: CharacterProperty):
    """
    所有属性强化(14)
    """
    char.AddElementDB('火', 14)
    char.AddElementDB('冰', 14)
    char.AddElementDB('光', 14)
    char.AddElementDB('暗', 14)
    pass


# endregion
# region 光环


def enchant_2000(char: CharacterProperty):
    """
    Lv1~95+1|攻击强化(12%)|增益量(7%)
    """
    char.SetStatus(攻击强化P=0.12,增益量P=0.07)
    char.AddSkillLv(1, 95, 1)
    pass


def enchant_2001(char: CharacterProperty):
    """
    Lv1~95+1|攻击强化(7%)|增益量(5%)
    """
    char.SetStatus(攻击强化P=0.07,增益量P=0.05)
    char.AddSkillLv(1, 95, 1)
    pass


def enchant_2002(char: CharacterProperty):
    """
    Lv1~35+1|攻击强化(5%)|增益量(3%)
    """
    char.SetStatus(攻击强化P=0.05,增益量P=0.03)
    char.AddSkillLv(1, 35, 1)
    pass


# endregion
# region 武器装扮


def enchant_2100(char: CharacterProperty):
    """
    Lv40主动+1|四维(55)
    """
    char.AddSkillLv(40, 40, 1, 1)
    char.SetStatus(四维=55)
    pass


def enchant_2101(char: CharacterProperty):
    """
    Lv45主动+1|四维(55)
    """
    char.AddSkillLv(45, 45, 1, 1)
    char.SetStatus(四维=55)
    pass


def enchant_2102(char: CharacterProperty):
    """
    Lv60主动+1|四维(55)
    """
    char.AddSkillLv(60, 60, 1, 1)
    char.SetStatus(四维=55)
    pass


def enchant_2103(char: CharacterProperty):
    """
    Lv70主动+1|四维(55)
    """
    char.AddSkillLv(70, 70, 1, 1)
    char.SetStatus(四维=55)
    pass


def enchant_2104(char: CharacterProperty):
    """
    Lv75主动+1|四维(55)
    """
    char.AddSkillLv(75, 75, 1, 1)
    char.SetStatus(四维=55)
    pass


def enchant_2105(char: CharacterProperty):
    """
    Lv80主动+1|四维(55)
    """
    char.AddSkillLv(80, 80, 1, 1)
    char.SetStatus(四维=55)
    pass


# endregion
# region 皮肤


def enchant_2200(char: CharacterProperty):
    """
    Lv40主动+1|所有属性强化(12)|四维(55)
    """
    char.AddSkillLv(40, 40, 1, 1)
    char.SetStatus(四维=55)
    char.AddElementDB('火', 12)
    char.AddElementDB('冰', 12)
    char.AddElementDB('光', 12)
    char.AddElementDB('暗', 12)
    pass


def enchant_2201(char: CharacterProperty):
    """
    Lv45主动+1|所有属性强化(12)|四维(55)
    """
    char.AddSkillLv(45, 45, 1, 1)
    char.SetStatus(四维=55)
    char.AddElementDB('火', 12)
    char.AddElementDB('冰', 12)
    char.AddElementDB('光', 12)
    char.AddElementDB('暗', 12)
    pass


def enchant_2202(char: CharacterProperty):
    """
    Lv60主动+1|所有属性强化(12)|四维(55)
    """
    char.AddSkillLv(60, 60, 1, 1)
    char.SetStatus(四维=55)
    char.AddElementDB('火', 12)
    char.AddElementDB('冰', 12)
    char.AddElementDB('光', 12)
    char.AddElementDB('暗', 12)
    pass


def enchant_2203(char: CharacterProperty):
    """
    Lv70主动+1|所有属性强化(12)|四维(55)
    """
    char.AddSkillLv(70, 70, 1, 1)
    char.SetStatus(四维=55)
    char.AddElementDB('火', 12)
    char.AddElementDB('冰', 12)
    char.AddElementDB('光', 12)
    char.AddElementDB('暗', 12)
    pass


def enchant_2204(char: CharacterProperty):
    """
    Lv75主动+1|所有属性强化(12)|四维(55)
    """
    char.AddSkillLv(75, 75, 1, 1)
    char.SetStatus(四维=55)
    char.AddElementDB('火', 12)
    char.AddElementDB('冰', 12)
    char.AddElementDB('光', 12)
    char.AddElementDB('暗', 12)
    pass


def enchant_2205(char: CharacterProperty):
    """
    Lv80主动+1|所有属性强化(12)|四维(55)
    """
    char.AddSkillLv(80, 80, 1, 1)
    char.SetStatus(四维=55)
    char.AddElementDB('火', 12)
    char.AddElementDB('冰', 12)
    char.AddElementDB('光', 12)
    char.AddElementDB('暗', 12)
    pass


def enchant_2206(char: CharacterProperty):
    """
    所有属性强化(6)
    """
    char.AddElementDB('火', 6)
    char.AddElementDB('冰', 6)
    char.AddElementDB('光', 6)
    char.AddElementDB('暗', 6)
    pass


# endregion
# region 宠物装备-红


def enchant_2500(char: CharacterProperty):
    """
    攻击强化(10%)
    """
    char.SetStatus(攻击强化P=0.1)
    pass


def enchant_2501(char: CharacterProperty):
    """
    攻击强化(8%)
    """
    char.SetStatus(攻击强化P=0.08)
    pass


def enchant_2502(char: CharacterProperty):
    """
    攻击强化(4%)|所有属性强化(6)
    """
    char.SetStatus(攻击强化P=0.04)
    char.AddElementDB('火', 6)
    char.AddElementDB('冰', 6)
    char.AddElementDB('光', 6)
    char.AddElementDB('暗', 6)
    pass


def enchant_2503(char: CharacterProperty):
    """
    攻击强化(4%)|所有属性强化(4)|光强(4)
    """
    char.SetStatus(攻击强化P=0.04)
    char.AddElementDB('火', 4)
    char.AddElementDB('冰', 4)
    char.AddElementDB('光', 8)
    char.AddElementDB('暗', 4)
    pass


def enchant_2504(char: CharacterProperty):
    """
    攻击强化(4%)|所有属性强化(4)|火强(4)
    """
    char.SetStatus(攻击强化P=0.04)
    char.AddElementDB('火', 8)
    char.AddElementDB('冰', 4)
    char.AddElementDB('光', 4)
    char.AddElementDB('暗', 4)
    pass


def enchant_2505(char: CharacterProperty):
    """
    攻击强化(4%)|所有属性强化(4)|冰强(4)
    """
    char.SetStatus(攻击强化P=0.04)
    char.AddElementDB('火', 6)
    char.AddElementDB('冰', 6)
    char.AddElementDB('光', 6)
    char.AddElementDB('暗', 6)
    pass


def enchant_2506(char: CharacterProperty):
    """
    攻击强化(4%)|所有属性强化(4)|暗强(4)
    """
    char.SetStatus(攻击强化P=0.04)
    char.AddElementDB('火', 4)
    char.AddElementDB('冰', 4)
    char.AddElementDB('光', 8)
    char.AddElementDB('暗', 4)
    pass


def enchant_2507(char: CharacterProperty):
    """
    四维(33)
    """
    char.SetStatus(四维=33)
    pass


def enchant_2508(char: CharacterProperty):
    """
    四维(25)
    """
    char.SetStatus(四维=25)
    pass


def enchant_2509(char: CharacterProperty):
    """
    四维(50)
    """
    char.SetStatus(四维=50)
    pass


# endregion
# region 宠物装备-绿


def enchant_2600(char: CharacterProperty):
    """
    三攻(40)|所有属性强化(30)
    """
    char.SetStatus(三攻=40)
    char.AddElementDB('火', 30)
    char.AddElementDB('冰', 30)
    char.AddElementDB('光', 30)
    char.AddElementDB('暗', 30)
    pass


def enchant_2601(char: CharacterProperty):
    """
    三攻(40)|所有属性强化(20)
    """
    char.SetStatus(三攻=40)
    char.AddElementDB('火', 20)
    char.AddElementDB('冰', 20)
    char.AddElementDB('光', 20)
    char.AddElementDB('暗', 20)
    pass


def enchant_2602(char: CharacterProperty):
    """
    四维(50)|所有属性强化(20)
    """
    char.SetStatus(四维=50)
    char.AddElementDB('火', 20)
    char.AddElementDB('冰', 20)
    char.AddElementDB('光', 20)
    char.AddElementDB('暗', 20)
    pass


def enchant_2603(char: CharacterProperty):
    """
    四维(30)|所有属性强化(20)
    """
    char.SetStatus(四维=30)
    char.AddElementDB('火', 20)
    char.AddElementDB('冰', 20)
    char.AddElementDB('光', 20)
    char.AddElementDB('暗', 20)
    pass


def enchant_2604(char: CharacterProperty):
    """
    四维(30)
    """
    char.SetStatus(四维=30)
    pass


def enchant_2605(char: CharacterProperty):
    """
    四维(16)
    """
    char.SetStatus(四维=16)
    pass


# endregion
# region 宠物装备-蓝


def enchant_2606(char: CharacterProperty):
    """
    技攻(2%)|三速(5%)
    """
    char.SetStatus(技攻=0.02, 三速=0.05)
    pass


def enchant_2607(char: CharacterProperty):
    """
    三攻(30)|三速(4%)
    """
    char.SetStatus(三攻=30, 三速=0.04)
    pass


def enchant_2608(char: CharacterProperty):
    """
    三攻(30)
    """
    char.SetStatus(三攻=30)
    pass


def enchant_2609(char: CharacterProperty):
    """
    三攻(25)|三速(2%)|属性攻击|暴击(5%)
    """
    char.SetStatus(三攻=25, 三速=0.02)
    pass


def enchant_2610(char: CharacterProperty):
    """
    四维(50)|三速(4%)
    """
    char.SetStatus(四维=50, 三速=0.04)
    pass


def enchant_2611(char: CharacterProperty):
    """
    四维(25)|三速(2%)
    """
    char.SetStatus(四维=25, 三速=0.02)
    pass


def enchant_2612(char: CharacterProperty):
    """
    四维(20)|三速(2%)
    """
    char.SetStatus(四维=20, 三速=0.02)
    pass


# endregion
# region 快捷栏装备


def enchant_2700(char: CharacterProperty):
    """
    三攻(30)|攻击强化(10%)
    """
    char.SetStatus(三攻=30, 攻击强化P=0.1)
    pass


def enchant_2701(char: CharacterProperty):
    """
    三攻(30)|攻击强化(8%)
    """
    char.SetStatus(三攻=30, 攻击强化P=0.08)
    pass


def enchant_2702(char: CharacterProperty):
    """
    四维(8)|攻击强化(8%)
    """
    char.SetStatus(四维=8, 攻击强化P=0.08)
    pass


def enchant_2703(char: CharacterProperty):
    """
    四维(5)|攻击强化(8%)|攻速(8%)
    """
    char.SetStatus(四维=5, 攻击强化P=0.08, 攻速=0.08)
    pass


def enchant_2704(char: CharacterProperty):
    """
    三攻(30)|三速(5%)
    """
    char.SetStatus(三攻=30, 三速=0.05)
    pass


def enchant_2705(char: CharacterProperty):
    """
    三攻(30)|三速(5%)|增益量(1%)
    """
    char.SetStatus(三攻=30, 三速=0.05, 增益量=0.01)
    pass


def enchant_2706(char: CharacterProperty):
    """
    四维(50)
    """
    char.SetStatus(四维=50)
    pass


def enchant_2707(char: CharacterProperty):
    """
    四维(50)|三速(5%)
    """
    char.SetStatus(四维=50, 三速=0.05)
    pass


def enchant_2708(char: CharacterProperty):
    """
    四维(50)|三速(5%)|增益量(1%)
    """
    char.SetStatus(四维=50, 三速=0.05, 增益量=0.01)
    pass


def enchant_2709(char: CharacterProperty):
    """
    三攻(50)|三速(5%)|增益量(3%)
    """
    char.SetStatus(三攻=50, 三速=0.05, 增益量=0.03)
    pass


def enchant_2710(char: CharacterProperty):
    """
    四维(100)|三速(5%)|增益量(3%)
    """
    char.SetStatus(四维=100, 三速=0.05, 增益量=0.03)
    pass


# endregion

for i in range(0, 3000):
    try:
        if str(i) not in enchant_func_list.keys():
            enchant_func_list[str(i)] = eval(f'enchant_{i}')
    except Exception:
        pass
