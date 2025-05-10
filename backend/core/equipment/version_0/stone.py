from core.basic.equipment import EquEffect
from core.abstract.character import CharacterProperty
from .register import register

# region 潜影暗袭 套装


@register
def stone_1(char: CharacterProperty):
    """
    暗影：潜藏之肃灭

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_2(char: CharacterProperty):
    """
    暗影：潜藏之气息

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_3(char: CharacterProperty):
    """
    暗影：潜藏之窥伺

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_4(char: CharacterProperty):
    """
    暗影：潜藏之时机

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_5(char: CharacterProperty):
    """
    暗影：潜藏之步伐

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_6(char: CharacterProperty):
    """
    暗影：凋谢的枯萎灵魂

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_7(char: CharacterProperty):
    """
    暗影：潜形匿影之气息

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_8(char: CharacterProperty):
    """
    暗影：潜形匿影之窥伺

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_9(char: CharacterProperty):
    """
    暗影：潜形匿影之时间

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_10(char: CharacterProperty):
    """
    暗影：潜形匿影之步伐

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


# endregion
# region 精灵国度 套装


@register
def stone_11(char: CharacterProperty):
    """
    灵魂：正直精灵的纯粹

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_12(char: CharacterProperty):
    """
    灵魂：奋进精灵的勇气

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_13(char: CharacterProperty):
    """
    灵魂：果决精灵的智慧

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_14(char: CharacterProperty):
    """
    灵魂：温和精灵的威仪

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_15(char: CharacterProperty):
    """
    灵魂：巡旅精灵的步履

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_16(char: CharacterProperty):
    """
    灵魂：高洁精灵王的纯粹

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_17(char: CharacterProperty):
    """
    灵魂：常胜精灵王的勇气

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_18(char: CharacterProperty):
    """
    灵魂：沉稳精灵王的智慧

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_19(char: CharacterProperty):
    """
    灵魂：慈爱精灵王的威仪

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_20(char: CharacterProperty):
    """
    灵魂：自由精灵王的步履

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


# endregion
# region 理想之黄金乡 套装


@register
def stone_21(char: CharacterProperty):
    """
    黄金：无法触及之美梦

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_22(char: CharacterProperty):
    """
    黄金：无法忘却之理想

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_23(char: CharacterProperty):
    """
    黄金：无法接受之现实

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_24(char: CharacterProperty):
    """
    黄金：无法遏制之贪欲

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_25(char: CharacterProperty):
    """
    黄金：无法避免之止境

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_26(char: CharacterProperty):
    """
    黄金：永恒循环之美梦

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_27(char: CharacterProperty):
    """
    黄金：永恒铭刻之理想

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_28(char: CharacterProperty):
    """
    黄金：永恒既定之现实

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_29(char: CharacterProperty):
    """
    黄金：永恒无尽之贪欲

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_30(char: CharacterProperty):
    """
    黄金：永恒残酷之止境

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


# endregion
# region 龙战八荒 套装


@register
def stone_31(char: CharacterProperty):
    """
    龙战：乱世之蛟

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_32(char: CharacterProperty):
    """
    龙战：四海求战

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_33(char: CharacterProperty):
    """
    龙战：连城怒火

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_34(char: CharacterProperty):
    """
    龙战：摧裂之地

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_35(char: CharacterProperty):
    """
    龙战：破空利爪

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_36(char: CharacterProperty):
    """
    龙战：乱世显威之龙

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_37(char: CharacterProperty):
    """
    龙战：逐鹿天下之战

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_38(char: CharacterProperty):
    """
    龙战：炽焰燎原之火

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_39(char: CharacterProperty):
    """
    龙战：分崩离析之地

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_40(char: CharacterProperty):
    """
    龙战：踏破凌霄之爪

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


# endregion
# region 混沌净化 套装


@register
def stone_41(char: CharacterProperty):
    """
    净化：灿烂光辉

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_42(char: CharacterProperty):
    """
    净化：柔和光辉

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_43(char: CharacterProperty):
    """
    净化：温暖光辉

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_44(char: CharacterProperty):
    """
    净化：慈爱光辉

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_45(char: CharacterProperty):
    """
    净化：美丽光辉

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_46(char: CharacterProperty):
    """
    净化：照亮黑暗的灿烂光辉

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_47(char: CharacterProperty):
    """
    净化：治愈创伤的柔和光辉

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_48(char: CharacterProperty):
    """
    净化：驱散严寒的温暖光辉

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_49(char: CharacterProperty):
    """
    净化：唤醒众生的慈爱光辉

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_50(char: CharacterProperty):
    """
    净化：泽耀万物的美丽光辉

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


# endregion
# region 天命者的气运 套装


@register
def stone_51(char: CharacterProperty):
    """
    幸运：蝴蝶轻语

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_52(char: CharacterProperty):
    """
    幸运：蝴蝶赠礼

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_53(char: CharacterProperty):
    """
    幸运：蝴蝶扑翼

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_54(char: CharacterProperty):
    """
    幸运：蝴蝶垂泪

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_55(char: CharacterProperty):
    """
    幸运：蝴蝶拂风

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_56(char: CharacterProperty):
    """
    幸运：蝴蝶知天命

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_57(char: CharacterProperty):
    """
    幸运：蝴蝶增有余

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_58(char: CharacterProperty):
    """
    幸运：蝴蝶翩然舞

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_59(char: CharacterProperty):
    """
    幸运：蝴蝶喜极泣

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_60(char: CharacterProperty):
    """
    幸运：蝴蝶涟漪风

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


# endregion
# region 究极能量 套装


@register
def stone_61(char: CharacterProperty):
    """
    突破：岌岌可危的极限

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_62(char: CharacterProperty):
    """
    突破：摇摇欲坠的极限

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_63(char: CharacterProperty):
    """
    突破：四分五裂的极限

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_64(char: CharacterProperty):
    """
    突破：支离破碎的极限

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_65(char: CharacterProperty):
    """
    突破：千疮百孔的极限

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_66(char: CharacterProperty):
    """
    突破：撕裂极限的爆发

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_67(char: CharacterProperty):
    """
    突破：超越极限的爆发

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_68(char: CharacterProperty):
    """
    突破：无视极限的爆发

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_69(char: CharacterProperty):
    """
    突破：粉碎极限的爆发

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_70(char: CharacterProperty):
    """
    突破：摧毁极限的爆发

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


# endregion
# region 造化自然 套装


@register
def stone_71(char: CharacterProperty):
    """
    自然：绿荫绝景

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_72(char: CharacterProperty):
    """
    自然：花草芬芳

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_73(char: CharacterProperty):
    """
    自然：煦暖阳光

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_74(char: CharacterProperty):
    """
    自然：丰饶大地

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_75(char: CharacterProperty):
    """
    自然：勃勃生机

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_76(char: CharacterProperty):
    """
    自然：亘古苍茫之绿荫

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_77(char: CharacterProperty):
    """
    自然：肆意流淌之芬芳

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_78(char: CharacterProperty):
    """
    自然：万物生长之阳光

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_79(char: CharacterProperty):
    """
    自然：物华天宝之丰盈

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_80(char: CharacterProperty):
    """
    自然：生如夏花之绚烂

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


# endregion
# region 诸神黄昏之女武神 套装


@register
def stone_81(char: CharacterProperty):
    """
    战场：闪耀的女武神金装

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_82(char: CharacterProperty):
    """
    战场：闪耀的女武神金链

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_83(char: CharacterProperty):
    """
    战场：闪耀的女武神金饰

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_84(char: CharacterProperty):
    """
    战场：闪耀的女武神水晶

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_85(char: CharacterProperty):
    """
    战场：闪耀的女武神足迹

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_86(char: CharacterProperty):
    """
    战场：灿烂的女武神金装

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_87(char: CharacterProperty):
    """
    战场：灿烂的女武神金链

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_88(char: CharacterProperty):
    """
    战场：灿烂的女武神金饰

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_89(char: CharacterProperty):
    """
    战场：灿烂的女武神水晶

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_90(char: CharacterProperty):
    """
    战场：灿烂的女武神足迹

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


# endregion
# region 青丘灵珠 套装


@register
def stone_91(char: CharacterProperty):
    """
    永恒：清丽的狐仙刺绣

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_92(char: CharacterProperty):
    """
    永恒：清丽的狐仙饰品

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_93(char: CharacterProperty):
    """
    永恒：清丽的狐仙珠玉

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_94(char: CharacterProperty):
    """
    永恒：清丽的狐仙鬃毛

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_95(char: CharacterProperty):
    """
    永恒：清丽的狐仙足印

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_96(char: CharacterProperty):
    """
    永恒：和谐的狐仙刺绣

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_97(char: CharacterProperty):
    """
    永恒：和谐的狐仙饰品

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_98(char: CharacterProperty):
    """
    永恒：和谐的狐仙珠玉

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_99(char: CharacterProperty):
    """
    永恒：和谐的狐仙鬃毛

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_100(char: CharacterProperty):
    """
    永恒：和谐的狐仙足印

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


# endregion
# region 群猎美学 套装


@register
def stone_101(char: CharacterProperty):
    """
    狩猎：引路人甲衣

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_102(char: CharacterProperty):
    """
    狩猎：引路人甲裤

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_103(char: CharacterProperty):
    """
    狩猎：引路人刻印

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_104(char: CharacterProperty):
    """
    狩猎：引路人腰带

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_105(char: CharacterProperty):
    """
    狩猎：引路人长靴

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_106(char: CharacterProperty):
    """
    狩猎：先知引路人甲衣

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_107(char: CharacterProperty):
    """
    狩猎：先知引路人甲裤

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_108(char: CharacterProperty):
    """
    狩猎：先知引路人刻印

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_109(char: CharacterProperty):
    """
    狩猎：先知引路人腰带

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_110(char: CharacterProperty):
    """
    狩猎：先知引路人长靴

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


# endregion
# region 冥思者的魔力领域 套装


@register
def stone_111(char: CharacterProperty):
    """
    领域：魔力炽燃的界限

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_112(char: CharacterProperty):
    """
    领域：魔力炽然的信念

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_113(char: CharacterProperty):
    """
    领域：魔力炽然的记忆

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_114(char: CharacterProperty):
    """
    领域：魔力炽然的命运

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_115(char: CharacterProperty):
    """
    领域：魔力炽然的痕迹

    技能伤害+6%
    """
    char.SetStatus(SkillAttack=0.06)
    pass


@register
def stone_116(char: CharacterProperty):
    """
    领域：暴走魔力的界限

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_117(char: CharacterProperty):
    """
    领域：暴走魔力的信念

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_118(char: CharacterProperty):
    """
    领域：暴走魔力的记忆

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_119(char: CharacterProperty):
    """
    领域：暴走魔力的命运

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


@register
def stone_120(char: CharacterProperty):
    """
    领域：暴走魔力的足迹

    技能伤害+9%
    """
    char.SetStatus(SkillAttack=0.09)
    pass


# endregion
# region 维纳斯通宝-欲望


@register
def stone_121(char: CharacterProperty):
    """
    欲望：灵魂映照之花

    技能伤害+7%
    技能冷却时间-4%（觉醒时间除外）
    所有速度+4%
    """
    char.SetStatus(SkillAttack=0.07, SpeedA=0.04, SpeedM=0.04, SpeedR=0.04)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_122(char: CharacterProperty):
    """
    欲望：灵魂高洁之姿

    技能伤害+7%
    技能冷却时间-4%（觉醒时间除外）
    所有速度+4%
    """
    char.SetStatus(SkillAttack=0.07, SpeedA=0.04, SpeedM=0.04, SpeedR=0.04)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_123(char: CharacterProperty):
    """
    欲望：灵魂相伴之顾

    技能伤害+7%
    技能冷却时间-4%（觉醒时间除外）
    所有速度+4%
    """
    char.SetStatus(SkillAttack=0.07, SpeedA=0.04, SpeedM=0.04, SpeedR=0.04)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_124(char: CharacterProperty):
    """
    欲望：灵魂流连之盼

    技能伤害+7%
    技能冷却时间-4%（觉醒时间除外）
    所有速度+4%
    """
    char.SetStatus(SkillAttack=0.07, SpeedA=0.04, SpeedM=0.04, SpeedR=0.04)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_125(char: CharacterProperty):
    """
    欲望：灵魂浸润之雅

    技能伤害+7%
    技能冷却时间-4%（觉醒时间除外）
    所有速度+4%
    """
    char.SetStatus(SkillAttack=0.07, SpeedA=0.04, SpeedM=0.04, SpeedR=0.04)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_126(char: CharacterProperty):
    """
    欲望：枯萎凋零之魂

    技能伤害+10%
    技能冷却时间-4%（觉醒时间除外）
    所有速度+8%
    """
    char.SetStatus(SkillAttack=0.10, SpeedA=0.08, SpeedM=0.08, SpeedR=0.08)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_127(char: CharacterProperty):
    """
    欲望：颓然堕尘之魄

    技能伤害+10%
    技能冷却时间-4%（觉醒时间除外）
    所有速度+8%
    """
    char.SetStatus(SkillAttack=0.10, SpeedA=0.08, SpeedM=0.08, SpeedR=0.08)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_128(char: CharacterProperty):
    """
    欲望：无法挽留之离

    技能伤害+10%
    技能冷却时间-4%（觉醒时间除外）
    所有速度+8%
    """
    char.SetStatus(SkillAttack=0.10, SpeedA=0.08, SpeedM=0.08, SpeedR=0.08)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_129(char: CharacterProperty):
    """
    欲望：失神迷离之散

    技能伤害+10%
    技能冷却时间-4%（觉醒时间除外）
    所有速度+8%
    """
    char.SetStatus(SkillAttack=0.10, SpeedA=0.08, SpeedM=0.08, SpeedR=0.08)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_130(char: CharacterProperty):
    """
    欲望：神恩永断之绝

    技能伤害+10%
    技能冷却时间-4%（觉醒时间除外）
    所有速度+8%
    """
    char.SetStatus(SkillAttack=0.10, SpeedA=0.08, SpeedM=0.08, SpeedR=0.08)
    char.SetSkillCD(1, 100, 0.04)
    pass


# endregion
# region 维纳斯通宝-背叛


@register
def stone_131(char: CharacterProperty):
    """
    背叛：隐情揭露

    技能伤害+7%
    技能冷却时间-4%（觉醒时间除外）
    技能范围+4%
    """
    char.SetStatus(SkillAttack=0.07)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_132(char: CharacterProperty):
    """
    背叛：欲望蔓延

    技能伤害+7%
    技能冷却时间-4%（觉醒时间除外）
    技能范围+4%
    """
    char.SetStatus(SkillAttack=0.07)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_133(char: CharacterProperty):
    """
    背叛：信任崩坏

    技能伤害+7%
    技能冷却时间-4%（觉醒时间除外）
    技能范围+4%
    """
    char.SetStatus(SkillAttack=0.07)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_134(char: CharacterProperty):
    """
    背叛：噩梦难逃

    技能伤害+7%
    技能冷却时间-4%（觉醒时间除外）
    技能范围+4%
    """
    char.SetStatus(SkillAttack=0.07)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_135(char: CharacterProperty):
    """
    背叛：迷途彷徨

    技能伤害+7%
    技能冷却时间-4%（觉醒时间除外）
    技能范围+4%
    """
    char.SetStatus(SkillAttack=0.07)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_136(char: CharacterProperty):
    """
    背叛：指向凡人的愤怒

    技能伤害+10%
    技能冷却时间-4%（觉醒时间除外）
    技能范围+8%
    """
    char.SetStatus(SkillAttack=0.10)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_137(char: CharacterProperty):
    """
    背叛：堕落邪神的欲望

    技能伤害+10%
    技能冷却时间-4%（觉醒时间除外）
    技能范围+8%
    """
    char.SetStatus(SkillAttack=0.10)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_138(char: CharacterProperty):
    """
    背叛：毁信导致的悲剧

    技能伤害+10%
    技能冷却时间-4%（觉醒时间除外）
    技能范围+8%
    """
    char.SetStatus(SkillAttack=0.10)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_139(char: CharacterProperty):
    """
    背叛：永世沉沦的噩梦

    技能伤害+10%
    技能冷却时间-4%（觉醒时间除外）
    技能范围+8%
    """
    char.SetStatus(SkillAttack=0.10)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_140(char: CharacterProperty):
    """
    背叛：最后一舞的缠绵

    技能伤害+10%
    技能冷却时间-4%（觉醒时间除外）
    技能范围+8%
    """
    char.SetStatus(SkillAttack=0.10)
    char.SetSkillCD(1, 100, 0.04)
    pass


# endregion
# region 维纳斯通宝-容辉


@register
def stone_141(char: CharacterProperty):
    """
    容辉：丰饶的过往

    技能伤害+7%
    技能冷却时间-4%（觉醒时间除外）
    所受物理/魔法伤害-3%
    """
    char.SetStatus(SkillAttack=0.07)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_142(char: CharacterProperty):
    """
    容辉：从容的过往

    技能伤害+7%
    技能冷却时间-4%（觉醒时间除外）
    所受物理/魔法伤害-3%
    """
    char.SetStatus(SkillAttack=0.07)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_143(char: CharacterProperty):
    """
    容辉：光明的过往

    技能伤害+7%
    技能冷却时间-4%（觉醒时间除外）
    所受物理/魔法伤害-3%
    """
    char.SetStatus(SkillAttack=0.07)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_144(char: CharacterProperty):
    """
    容辉：慈爱的过往

    技能伤害+7%
    技能冷却时间-4%（觉醒时间除外）
    所受物理/魔法伤害-3%
    """
    char.SetStatus(SkillAttack=0.07)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_145(char: CharacterProperty):
    """
    容辉：美丽的过往

    技能伤害+7%
    技能冷却时间-4%（觉醒时间除外）
    所受物理/魔法伤害-3%
    """
    char.SetStatus(SkillAttack=0.07)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_146(char: CharacterProperty):
    """
    容辉：支离破碎的丰饶

    技能伤害+10%
    技能冷却时间-4%（觉醒时间除外）
    所受物理/魔法伤害-3%
    伤害型异常状态抗性+4%
    """
    char.SetStatus(SkillAttack=0.10)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_147(char: CharacterProperty):
    """
    容辉：患得患失的偏执

    技能伤害+10%
    技能冷却时间-4%（觉醒时间除外）
    所受物理/魔法伤害-3%
    伤害型异常状态抗性+4%
    """
    char.SetStatus(SkillAttack=0.10)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_148(char: CharacterProperty):
    """
    容辉：愤怒引来的黑暗

    技能伤害+10%
    技能冷却时间-4%（觉醒时间除外）
    所受物理/魔法伤害-3%
    伤害型异常状态抗性+4%
    """
    char.SetStatus(SkillAttack=0.10)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_149(char: CharacterProperty):
    """
    容辉：心怀憎恶的诅咒

    技能伤害+10%
    技能冷却时间-4%（觉醒时间除外）
    所受物理/魔法伤害-3%
    伤害型异常状态抗性+4%
    """
    char.SetStatus(SkillAttack=0.10)
    char.SetSkillCD(1, 100, 0.04)
    pass


@register
def stone_150(char: CharacterProperty):
    """
    容辉：金玉其外的优雅

    技能伤害+10%
    技能冷却时间-4%（觉醒时间除外）
    所受物理/魔法伤害-3%
    伤害型异常状态抗性+4%
    """
    char.SetStatus(SkillAttack=0.10)
    char.SetSkillCD(1, 100, 0.04)
    pass


# endregion


# region 潜影暗袭 套装


@register
def stone_151(char: CharacterProperty):
    """
    暗影：潜藏之视线

    技能伤害+11.5%
    """
    char.SetStatus(SkillAttack=0.115)
    pass


@register
def stone_152(char: CharacterProperty):
    """
    暗影：潜形匿影之视线

    技能伤害+13.5%
    """
    char.SetStatus(SkillAttack=0.135)
    pass


@register
def stone_153(char: CharacterProperty):
    """
    暗影：潜藏之寒冷

    技能伤害+14%
    """
    char.SetStatus(SkillAttack=0.14)
    pass


@register
def stone_154(char: CharacterProperty):
    """
    暗影：潜形匿影之寒冷

    技能伤害+16%
    """
    char.SetStatus(SkillAttack=0.16)
    pass


@register
def stone_155(char: CharacterProperty):
    """
    暗影：潜藏之灼热

    技能伤害+14%
    """
    char.SetStatus(SkillAttack=0.14)
    pass


@register
def stone_156(char: CharacterProperty):
    """
    暗影：潜形匿影之灼热

    技能伤害+16%
    """
    char.SetStatus(SkillAttack=0.16)
    pass


@register
def stone_157(char: CharacterProperty):
    """
    暗影：潜藏之强风

    技能伤害+12.5%
    """
    char.SetStatus(SkillAttack=0.125)
    pass


@register
def stone_158(char: CharacterProperty):
    """
    暗影：潜藏藏影之强风

    技能伤害+14.5%
    """
    char.SetStatus(SkillAttack=0.145)
    pass


@register
def stone_159(char: CharacterProperty):
    """
    暗影：潜藏之狂音

    技能伤害+12.5%
    """
    char.SetStatus(SkillAttack=0.125)
    pass


@register
def stone_160(char: CharacterProperty):
    """
    暗影：潜藏藏影之狂音

    技能伤害+14.5%
    """
    char.SetStatus(SkillAttack=0.145)
    pass


@register
def stone_161(char: CharacterProperty):
    """
    暗影：潜藏之黑暗

    技能伤害+12.5%
    """
    char.SetStatus(SkillAttack=0.125)
    pass


@register
def stone_162(char: CharacterProperty):
    """
    暗影：潜藏藏影之黑暗

    技能伤害+14.5%
    """
    char.SetStatus(SkillAttack=0.145)
    pass


# endregion
# region 精灵国度 套装


@register
def stone_163(char: CharacterProperty):
    """
    灵魂：精灵的庇护

    技能伤害+11.5%
    """
    stone_151(char)
    pass


@register
def stone_164(char: CharacterProperty):
    """
    灵魂：精灵王的热情庇护

    技能伤害+13.5%
    """
    stone_152(char)
    pass


@register
def stone_165(char: CharacterProperty):
    """
    灵魂：精灵的誓约

    技能伤害+14%
    """
    stone_153(char)
    pass


@register
def stone_166(char: CharacterProperty):
    """
    灵魂：精灵王的自由誓约

    技能伤害+16%
    """
    stone_154(char)
    pass


@register
def stone_167(char: CharacterProperty):
    """
    灵魂：精灵的冷静

    技能伤害+14%
    """
    stone_155(char)
    pass


@register
def stone_168(char: CharacterProperty):
    """
    灵魂：精灵王的灿烂寒芒

    技能伤害+16%
    """
    stone_156(char)
    pass


@register
def stone_169(char: CharacterProperty):
    """
    灵魂：精灵的指挥

    技能伤害+12.5%
    """
    stone_157(char)
    pass


@register
def stone_170(char: CharacterProperty):
    """
    灵魂：精灵王的渊博智慧

    技能伤害+14.5%
    """
    stone_158(char)
    pass


@register
def stone_171(char: CharacterProperty):
    """
    灵魂：精灵的心曲

    技能伤害+12.5%
    """
    stone_159(char)
    pass


@register
def stone_172(char: CharacterProperty):
    """
    灵魂：精灵王的矜贵心曲

    技能伤害+14.5%
    """
    stone_160(char)
    pass


@register
def stone_173(char: CharacterProperty):
    """
    灵魂：精灵的礼物

    技能伤害+12.5%
    """
    stone_161(char)
    pass


@register
def stone_174(char: CharacterProperty):
    """
    灵魂：精灵王的纯粹礼物

    技能伤害+14.5%
    """
    stone_162(char)
    pass


# endregion
# region 理想之黄金乡 套装


@register
def stone_175(char: CharacterProperty):
    """
    黄金：无法舍离之傲慢

    技能伤害+11.5%
    """
    stone_151(char)
    pass


@register
def stone_176(char: CharacterProperty):
    """
    黄金：永恒依存之傲慢

    技能伤害+13.5%
    """
    stone_152(char)
    pass


@register
def stone_177(char: CharacterProperty):
    """
    黄金：无法触及之风暴

    技能伤害+14%
    """
    stone_153(char)
    pass


@register
def stone_178(char: CharacterProperty):
    """
    黄金：永恒难敌之风暴

    技能伤害+16%
    """
    stone_154(char)
    pass


@register
def stone_179(char: CharacterProperty):
    """
    黄金：无法竭尽之渴望

    技能伤害+14%
    """
    stone_155(char)
    pass


@register
def stone_180(char: CharacterProperty):
    """
    黄金：永恒延续之渴望

    技能伤害+16%
    """
    stone_156(char)
    pass


@register
def stone_181(char: CharacterProperty):
    """
    黄金：无法熄灭之怒火

    技能伤害+12.5%
    """
    stone_157(char)
    pass


@register
def stone_182(char: CharacterProperty):
    """
    黄金：永恒燃烧之怒火

    技能伤害+14.5%
    """
    stone_158(char)
    pass


@register
def stone_183(char: CharacterProperty):
    """
    黄金：无法逃避之消亡

    技能伤害+12.5%
    """
    stone_159(char)
    pass


@register
def stone_184(char: CharacterProperty):
    """
    黄金：永恒不甘之消亡

    技能伤害+14.5%
    """
    stone_160(char)
    pass


@register
def stone_185(char: CharacterProperty):
    """
    黄金：无法抵达之彼岸

    技能伤害+12.5%
    """
    stone_161(char)
    pass


@register
def stone_186(char: CharacterProperty):
    """
    黄金：永恒朝圣之彼岸

    技能伤害+14.5%
    """
    stone_162(char)
    pass


# endregion
# region 龙战八荒 套装


@register
def stone_187(char: CharacterProperty):
    """
    龙战：雷霆之牙

    技能伤害+11.5%
    """
    stone_151(char)
    pass


@register
def stone_188(char: CharacterProperty):
    """
    龙战：雷霆万钧之牙

    技能伤害+13.5%
    """
    stone_152(char)
    pass


@register
def stone_189(char: CharacterProperty):
    """
    龙战：不灭斗志

    技能伤害+14%
    """
    stone_153(char)
    pass


@register
def stone_190(char: CharacterProperty):
    """
    龙战：万古不移之志

    技能伤害+16%
    """
    stone_154(char)
    pass


@register
def stone_191(char: CharacterProperty):
    """
    龙战：震天咆哮

    技能伤害+14%
    """
    stone_155(char)
    pass


@register
def stone_192(char: CharacterProperty):
    """
    龙战：震天动地之吼

    技能伤害+16%
    """
    stone_156(char)
    pass


@register
def stone_193(char: CharacterProperty):
    """
    龙战：焚心逆鳞

    技能伤害+12.5%
    """
    stone_157(char)
    pass


@register
def stone_194(char: CharacterProperty):
    """
    龙战：蚀骨焚心之鳞

    技能伤害+14.5%
    """
    stone_158(char)
    pass


@register
def stone_195(char: CharacterProperty):
    """
    龙战：征途宿命

    技能伤害+12.5%
    """
    stone_159(char)
    pass


@register
def stone_196(char: CharacterProperty):
    """
    龙战：四海降伏之威

    技能伤害+14.5%
    """
    stone_160(char)
    pass


@register
def stone_197(char: CharacterProperty):
    """
    龙战：血海孤征

    技能伤害+12.5%
    """
    stone_161(char)
    pass


@register
def stone_198(char: CharacterProperty):
    """
    龙战：烽火延绵之战

    技能伤害+14.5%
    """
    stone_162(char)
    pass


# endregion
# region 混沌净化 套装


@register
def stone_199(char: CharacterProperty):
    """
    净化：寂静黑暗

    技能伤害+11.5%
    """
    stone_151(char)
    pass


@register
def stone_200(char: CharacterProperty):
    """
    净化：侵蚀永恒的寂静黑暗

    技能伤害+13.5%
    """
    stone_152(char)
    pass


@register
def stone_201(char: CharacterProperty):
    """
    净化：冷冽黑暗

    技能伤害+14%
    """
    stone_153(char)
    pass


@register
def stone_202(char: CharacterProperty):
    """
    净化：冻结冰霜的冷冽黑暗

    技能伤害+16%
    """
    stone_154(char)
    pass


@register
def stone_203(char: CharacterProperty):
    """
    净化：炽热黑暗

    技能伤害+14%
    """
    stone_155(char)
    pass


@register
def stone_204(char: CharacterProperty):
    """
    净化：燃烧伤痛的炽热黑暗

    技能伤害+16%
    """
    stone_156(char)
    pass


@register
def stone_205(char: CharacterProperty):
    """
    净化：锋利黑暗

    技能伤害+12.5%
    """
    stone_157(char)
    pass


@register
def stone_206(char: CharacterProperty):
    """
    净化：斩断生机的锋利黑暗

    技能伤害+14.5%
    """
    stone_158(char)
    pass


@register
def stone_207(char: CharacterProperty):
    """
    净化：无情黑暗

    技能伤害+12.5%
    """
    stone_159(char)
    pass


@register
def stone_208(char: CharacterProperty):
    """
    净化：抑制喜悲的无情黑暗

    技能伤害+14.5%
    """
    stone_160(char)
    pass


@register
def stone_209(char: CharacterProperty):
    """
    净化：光暗平衡

    技能伤害+12.5%
    """
    stone_161(char)
    pass


@register
def stone_210(char: CharacterProperty):
    """
    净化：达成和谐的光暗平衡

    技能伤害+14.5%
    """
    stone_162(char)
    pass


# endregion
# region 天命者的气运 套装


@register
def stone_211(char: CharacterProperty):
    """
    幸运：蝴蝶之喜

    技能伤害+11.5%
    """
    stone_151(char)
    pass


@register
def stone_212(char: CharacterProperty):
    """
    幸运：蝴蝶启未来

    技能伤害+13.5%
    """
    stone_152(char)
    pass


@register
def stone_213(char: CharacterProperty):
    """
    幸运：蝴蝶之护

    技能伤害+14%
    """
    stone_153(char)
    pass


@register
def stone_214(char: CharacterProperty):
    """
    幸运：蝴蝶咒言灵

    技能伤害+16%
    """
    stone_154(char)
    pass


@register
def stone_215(char: CharacterProperty):
    """
    幸运：蝴蝶之美

    技能伤害+14%
    """
    stone_155(char)
    pass


@register
def stone_216(char: CharacterProperty):
    """
    幸运：蝴蝶美姿仪

    技能伤害+16%
    """
    stone_156(char)
    pass


@register
def stone_217(char: CharacterProperty):
    """
    幸运：蝴蝶之笑

    技能伤害+12.5%
    """
    stone_157(char)
    pass


@register
def stone_218(char: CharacterProperty):
    """
    幸运：蝴蝶笑颜开

    技能伤害+14.5%
    """
    stone_158(char)
    pass


@register
def stone_219(char: CharacterProperty):
    """
    幸运：蝴蝶之眸

    技能伤害+12.5%
    """
    stone_159(char)
    pass


@register
def stone_220(char: CharacterProperty):
    """
    幸运：蝴蝶辟新章

    技能伤害+14.5%
    """
    stone_160(char)
    pass


@register
def stone_221(char: CharacterProperty):
    """
    幸运：蝴蝶之运

    技能伤害+12.5%
    """
    stone_161(char)
    pass


@register
def stone_222(char: CharacterProperty):
    """
    幸运：蝴蝶盈天运

    技能伤害+14.5%
    """
    stone_162(char)
    pass


# endregion
# region 究极能量 套装


@register
def stone_223(char: CharacterProperty):
    """
    突破：指引的极限

    技能伤害+11.5%
    """
    stone_151(char)
    pass


@register
def stone_224(char: CharacterProperty):
    """
    突破：指引极限的爆发

    技能伤害+13.5%
    """
    stone_152(char)
    pass


@register
def stone_225(char: CharacterProperty):
    """
    突破：变化的极限

    技能伤害+14%
    """
    stone_153(char)
    pass


@register
def stone_226(char: CharacterProperty):
    """
    突破：变化极限的爆发

    技能伤害+16%
    """
    stone_154(char)
    pass


@register
def stone_227(char: CharacterProperty):
    """
    突破：开启的极限

    技能伤害+14%
    """
    stone_155(char)
    pass


@register
def stone_228(char: CharacterProperty):
    """
    突破：开启极限的爆发

    技能伤害+16%
    """
    stone_156(char)
    pass


@register
def stone_229(char: CharacterProperty):
    """
    突破：穿梭的极限

    技能伤害+12.5%
    """
    stone_157(char)
    pass


@register
def stone_230(char: CharacterProperty):
    """
    突破：穿梭极限的爆发

    技能伤害+14.5%
    """
    stone_158(char)
    pass


@register
def stone_231(char: CharacterProperty):
    """
    突破：跨越的极限

    技能伤害+12.5%
    """
    stone_159(char)
    pass


@register
def stone_232(char: CharacterProperty):
    """
    突破：跨越极限的爆发

    技能伤害+14.5%
    """
    stone_160(char)
    pass


@register
def stone_233(char: CharacterProperty):
    """
    突破：震撼的极限

    技能伤害+12.5%
    """
    stone_161(char)
    pass


@register
def stone_234(char: CharacterProperty):
    """
    突破：震撼极限的爆发

    技能伤害+14.5%
    """
    stone_162(char)
    pass


# endregion
# region 造化自然 套装


@register
def stone_235(char: CharacterProperty):
    """
    自然：造物恩惠

    技能伤害+11.5%
    """
    stone_151(char)
    pass


@register
def stone_236(char: CharacterProperty):
    """
    自然：天工开物之恩惠

    技能伤害+13.5%
    """
    stone_152(char)
    pass


@register
def stone_237(char: CharacterProperty):
    """
    自然：风流云散

    技能伤害+14%
    """
    stone_153(char)
    pass


@register
def stone_238(char: CharacterProperty):
    """
    自然：风起云涌之流转

    技能伤害+16%
    """
    stone_154(char)
    pass


@register
def stone_239(char: CharacterProperty):
    """
    自然：硕果累累

    技能伤害+14%
    """
    stone_155(char)
    pass


@register
def stone_240(char: CharacterProperty):
    """
    自然：春华秋实之说过

    技能伤害+16%
    """
    stone_156(char)
    pass


@register
def stone_241(char: CharacterProperty):
    """
    自然：宁静致远

    技能伤害+12.5%
    """
    stone_157(char)
    pass


@register
def stone_242(char: CharacterProperty):
    """
    自然：万物和合之宁静

    技能伤害+14.5%
    """
    stone_158(char)
    pass


@register
def stone_243(char: CharacterProperty):
    """
    自然：根深叶茂

    技能伤害+12.5%
    """
    stone_159(char)
    pass


@register
def stone_244(char: CharacterProperty):
    """
    自然：根深叶茂之生机

    技能伤害+14.5%
    """
    stone_160(char)
    pass


@register
def stone_245(char: CharacterProperty):
    """
    自然：百花争艳

    技能伤害+12.5%
    """
    stone_161(char)
    pass


@register
def stone_246(char: CharacterProperty):
    """
    自然：百花齐放之美丽

    技能伤害+14.5%
    """
    stone_162(char)
    pass


# endregion
# region 诸神黄昏之女武神 套装


@register
def stone_247(char: CharacterProperty):
    """
    战场：闪耀的女武神手套

    技能伤害+11.5%
    """
    stone_151(char)
    pass


@register
def stone_248(char: CharacterProperty):
    """
    战场：灿烂的女武神手套

    技能伤害+13.5%
    """
    stone_152(char)
    pass


@register
def stone_249(char: CharacterProperty):
    """
    战场：闪耀的女武神誓言

    技能伤害+14%
    """
    stone_153(char)
    pass


@register
def stone_250(char: CharacterProperty):
    """
    战场：灿烂的女武神誓言

    技能伤害+16%
    """
    stone_154(char)
    pass


@register
def stone_251(char: CharacterProperty):
    """
    战场：闪耀的女武神手套

    技能伤害+14%
    """
    stone_155(char)
    pass


@register
def stone_252(char: CharacterProperty):
    """
    战场：灿烂的女武神奖章

    技能伤害+16%
    """
    stone_156(char)
    pass


@register
def stone_253(char: CharacterProperty):
    """
    战场：闪耀的女武神头盔

    技能伤害+12.5%
    """
    stone_157(char)
    pass


@register
def stone_254(char: CharacterProperty):
    """
    战场：灿烂的女武神头盔

    技能伤害+14.5%
    """
    stone_158(char)
    pass


@register
def stone_255(char: CharacterProperty):
    """
    战场：闪耀的女武神翅膀

    技能伤害+12.5%
    """
    stone_159(char)
    pass


@register
def stone_256(char: CharacterProperty):
    """
    战场：灿烂的女武神翅膀

    技能伤害+14.5%
    """
    stone_160(char)
    pass


@register
def stone_257(char: CharacterProperty):
    """
    战场：闪耀的女武神意志

    技能伤害+12.5%
    """
    stone_161(char)
    pass


@register
def stone_258(char: CharacterProperty):
    """
    战场：灿烂的女武神意志

    技能伤害+14.5%
    """
    stone_162(char)
    pass


# endregion
# region 青丘灵珠 套装


@register
def stone_259(char: CharacterProperty):
    """
    永恒：清丽灵狐的信念

    技能伤害+11.5%
    """
    stone_151(char)
    pass


@register
def stone_260(char: CharacterProperty):
    """
    永恒：和谐灵狐的信念

    技能伤害+13.5%
    """
    stone_152(char)
    pass


@register
def stone_261(char: CharacterProperty):
    """
    永恒：清丽灵狐的誓言

    技能伤害+14%
    """
    stone_153(char)
    pass


@register
def stone_262(char: CharacterProperty):
    """
    永恒：和谐灵狐的誓言

    技能伤害+16%
    """
    stone_154(char)
    pass


@register
def stone_263(char: CharacterProperty):
    """
    永恒：清丽灵狐的力量

    技能伤害+14%
    """
    stone_155(char)
    pass


@register
def stone_264(char: CharacterProperty):
    """
    永恒：和谐灵狐的力量

    技能伤害+16%
    """
    stone_156(char)
    pass


@register
def stone_265(char: CharacterProperty):
    """
    永恒：清丽灵狐的宝石

    技能伤害+12.5%
    """
    stone_157(char)
    pass


@register
def stone_266(char: CharacterProperty):
    """
    永恒：和谐灵狐的宝石

    技能伤害+14.5%
    """
    stone_158(char)
    pass


@register
def stone_267(char: CharacterProperty):
    """
    永恒：清丽灵狐的心灵

    技能伤害+12.5%
    """
    stone_159(char)
    pass


@register
def stone_268(char: CharacterProperty):
    """
    永恒：和谐灵狐的心灵

    技能伤害+14.5%
    """
    stone_160(char)
    pass


@register
def stone_269(char: CharacterProperty):
    """
    永恒：清丽灵狐的意志

    技能伤害+12.5%
    """
    stone_161(char)
    pass


@register
def stone_270(char: CharacterProperty):
    """
    永恒：和谐灵狐的意志

    技能伤害+14.5%
    """
    stone_162(char)
    pass


# endregion
# region 群猎美学 套装


@register
def stone_271(char: CharacterProperty):
    """
    狩猎：引路者的指引

    技能伤害+11.5%
    """
    stone_151(char)
    pass


@register
def stone_272(char: CharacterProperty):
    """
    狩猎：先知引路者的指引

    技能伤害+13.5%
    """
    stone_152(char)
    pass


@register
def stone_273(char: CharacterProperty):
    """
    狩猎：引路者的誓言

    技能伤害+14%
    """
    stone_153(char)
    pass


@register
def stone_274(char: CharacterProperty):
    """
    狩猎：先知引路者的誓言

    技能伤害+16%
    """
    stone_154(char)
    pass


@register
def stone_275(char: CharacterProperty):
    """
    狩猎：引路者的象征

    技能伤害+14%
    """
    stone_155(char)
    pass


@register
def stone_276(char: CharacterProperty):
    """
    狩猎：先知引路者的象征

    技能伤害+16%
    """
    stone_156(char)
    pass


@register
def stone_277(char: CharacterProperty):
    """
    狩猎：引路者的意志

    技能伤害+12.5%
    """
    stone_157(char)
    pass


@register
def stone_278(char: CharacterProperty):
    """
    狩猎：先知引路者的意志

    技能伤害+14.5%
    """
    stone_158(char)
    pass


@register
def stone_279(char: CharacterProperty):
    """
    狩猎：引路者的挚友

    技能伤害+12.5%
    """
    stone_159(char)
    pass


@register
def stone_280(char: CharacterProperty):
    """
    狩猎：先知引路者的挚友

    技能伤害+14.5%
    """
    stone_160(char)
    pass


@register
def stone_281(char: CharacterProperty):
    """
    狩猎：引路者的信号

    技能伤害+12.5%
    """
    stone_161(char)
    pass


@register
def stone_282(char: CharacterProperty):
    """
    狩猎：先知引路者的信号

    技能伤害+14.5%
    """
    stone_162(char)
    pass


# endregion
# region 冥思者的魔力领域 套装


@register
def stone_283(char: CharacterProperty):
    """
    领域：魔力炽燃的线路

    技能伤害+11.5%
    """
    stone_151(char)
    pass


@register
def stone_284(char: CharacterProperty):
    """
    领域：魔力暴走的线路

    技能伤害+13.5%
    """
    stone_152(char)
    pass


@register
def stone_285(char: CharacterProperty):
    """
    领域：魔力炽燃的循环

    技能伤害+14%
    """
    stone_153(char)
    pass


@register
def stone_286(char: CharacterProperty):
    """
    领域：魔力暴走的循环

    技能伤害+16%
    """
    stone_154(char)
    pass


@register
def stone_287(char: CharacterProperty):
    """
    领域：魔力炽燃的调律

    技能伤害+14%
    """
    stone_155(char)
    pass


@register
def stone_288(char: CharacterProperty):
    """
    领域：魔力暴走的调律

    技能伤害+16%
    """
    stone_156(char)
    pass


@register
def stone_289(char: CharacterProperty):
    """
    领域：魔力炽燃的激发

    技能伤害+12.5%
    """
    stone_157(char)
    pass


@register
def stone_290(char: CharacterProperty):
    """
    领域：魔力暴走的激发

    技能伤害+14.5%
    """
    stone_158(char)
    pass


@register
def stone_291(char: CharacterProperty):
    """
    领域：魔力炽燃的增援

    技能伤害+12.5%
    """
    stone_159(char)
    pass


@register
def stone_292(char: CharacterProperty):
    """
    领域：魔力暴走的增援

    技能伤害+14.5%
    """
    stone_160(char)
    pass


@register
def stone_293(char: CharacterProperty):
    """
    领域：魔力炽燃的信号

    技能伤害+12.5%
    """
    stone_161(char)
    pass


@register
def stone_294(char: CharacterProperty):
    """
    领域：魔力暴走的信号

    技能伤害+14.5%
    """
    stone_162(char)
    pass


# endregion
# region 纳波尔通宝-祝福 套装


@register
def stone_295(char: CharacterProperty):
    """
    祝福：溶溶暖阳

    技能伤害+12.5%
    技能范围+20%
    """
    char.SetStatus(SkillAttack=0.125)
    pass


@register
def stone_296(char: CharacterProperty):
    """
    祝福：灼魂烈日

    技能伤害+14.5%
    技能范围+25%
    """
    char.SetStatus(SkillAttack=0.16)
    pass


@register
def stone_297(char: CharacterProperty):
    """
    祝福：冽冽疾风

    技能伤害+15%
    所有速度+15%
    """
    char.SetStatus(SkillAttack=0.15,SpeedA=0.15,SpeedM=0.15,SpeedR=0.15)
    pass


@register
def stone_298(char: CharacterProperty):
    """
    祝福：呼啸风暴

    技能伤害+17%
    所有速度+25%
    """
    char.SetStatus(SkillAttack=0.17,SpeedA=0.25,SpeedM=0.25,SpeedR=0.25)
    pass


@register
def stone_299(char: CharacterProperty):
    """
    祝福：凉凉清波

    技能伤害+15%
    500px范围内的队员所受物理/魔法伤害-10%
    """
    char.SetStatus(SkillAttack=0.15)
    pass


@register
def stone_300(char: CharacterProperty):
    """
    祝福：冰冻寒渊

    技能伤害+17%
    800px范围内的队员所受物理/魔法伤害-15%
    """
    char.SetStatus(SkillAttack=0.17)
    pass


# endregion
# region 纳波尔通宝-贝亚娜 套装


@register
def stone_301(char: CharacterProperty):
    """
    贝亚娜：再临的新生

    技能伤害+12.5%
    技能范围+5%
    融合的装备强化/增幅从10开始每增加1时，技能伤害+1%(最多叠加2次)
    融合的装备强化/增幅从10开始每增加1时，增益量+150(最多叠加2次)
    """
    char.SetStatus(SkillAttack=0.125)
    reinforce = char.charEquipInfo['手镯'].reinforce
    if reinforce > 10:
        value = min(reinforce - 10, 2)
        char.SetStatus(SkillAttack=0.01 * value,Buff=150 * value)
    pass


@register
def stone_302(char: CharacterProperty):
    """
    贝亚娜：轮回的新生

    技能伤害+14.5%
    技能范围+5%
    融合的装备强化/增幅从10开始每增加1时，技能伤害+1%(最多叠加2次)
    融合的装备强化/增幅从10开始每增加1时，增益量+150(最多叠加2次)
    """
    char.SetStatus(SkillAttack=0.16)
    reinforce = char.charEquipInfo['手镯'].reinforce
    if reinforce > 10:
        value = min(reinforce - 10, 2)
        char.SetStatus(SkillAttack=0.01 * value,Buff=150 * value)
    pass


@register
def stone_303(char: CharacterProperty):
    """
    贝亚娜：复始的记忆

    技能伤害+15%
    所有速度+5%
    融合的装备强化/增幅从10开始每增加1时，技能伤害+1%(最多叠加2次)
    融合的装备强化/增幅从10开始每增加1时，增益量+150(最多叠加2次)
    """
    char.SetStatus(SkillAttack=0.15,SpeedA=0.05,SpeedM=0.05,SpeedR=0.05)
    reinforce = char.charEquipInfo['戒指'].reinforce
    if reinforce > 10:
        value = min(reinforce - 10, 2)
        char.SetStatus(SkillAttack=0.01 * value,Buff=150 * value)
    pass


@register
def stone_304(char: CharacterProperty):
    """
    贝亚娜：永恒的记忆

    技能伤害+17%
    所有速度+7%
    融合的装备强化/增幅从10开始每增加1时，技能伤害+1%(最多叠加2次)
    融合的装备强化/增幅从10开始每增加1时，增益量+150(最多叠加2次)
    """
    char.SetStatus(SkillAttack=0.17,SpeedA=0.07,SpeedM=0.07,SpeedR=0.07)
    reinforce = char.charEquipInfo['戒指'].reinforce
    if reinforce > 10:
        value = min(reinforce - 10, 2)
        char.SetStatus(SkillAttack=0.01 * value,Buff=150 * value)
    pass


@register
def stone_305(char: CharacterProperty):
    """
    贝亚娜：持续的挑战

    技能伤害+15%
    所受伤害-5%
    融合的装备强化/增幅从10开始每增加1时，技能伤害+1%(最多叠加2次)
    融合的装备强化/增幅从10开始每增加1时，增益量+150(最多叠加2次)
    """
    char.SetStatus(SkillAttack=0.15)
    reinforce = char.charEquipInfo['项链'].reinforce
    if reinforce > 10:
        value = min(reinforce - 10, 2)
        char.SetStatus(SkillAttack=0.01 * value,Buff=150 * value)
    pass


@register
def stone_306(char: CharacterProperty):
    """
    贝亚娜：无尽的挑战

    技能伤害+17%
    所受伤害-7%
    融合的装备强化/增幅从10开始每增加1时，技能伤害+1%(最多叠加2次)
    融合的装备强化/增幅从10开始每增加1时，增益量+150(最多叠加2次)
    """
    char.SetStatus(SkillAttack=0.17)
    reinforce = char.charEquipInfo['项链'].reinforce
    if reinforce > 10:
        value = min(reinforce - 10, 2)
        char.SetStatus(SkillAttack=0.01 * value,Buff=150 * value)
    pass


# endregion
# region 纳波尔通宝-创造 套装


@register
def stone_307(char: CharacterProperty):
    """
    创造：变革之触

    技能伤害+11%
    特效伤害+10%
    """
    char.SetStatus(SkillAttack=0.11,EquEffectRatio=0.1)
    pass


@register
def stone_308(char: CharacterProperty):
    """
    创造：重构之触

    技能伤害+12%
    特效伤害+15%
    """
    char.SetStatus(SkillAttack=0.135,EquEffectRatio=0.15)
    pass


@register
def stone_309(char: CharacterProperty):
    """
    创造：变化的空间

    技能伤害+4%
    技能冷却时间-20%(觉醒技能除外)
    """
    char.SetStatus(SkillAttack=0.04)
    char.SetSkillCD(cd=0.2)
    pass


@register
def stone_310(char: CharacterProperty):
    """
    创造：错乱的空间

    技能伤害+6%
    技能冷却时间-20%(觉醒技能除外)
    """
    char.SetStatus(SkillAttack=0.06)
    char.SetSkillCD(cd=0.2)
    pass


@register
def stone_311(char: CharacterProperty):
    """
    创造：快进的时间

    技能伤害+3.5%
    释放技能时，有10%的几率初始化已使用技能的冷却时间。（觉醒技能除外）
    -相同技能间存在10秒冷却时间
    释放冷却时间超过1秒的技能时，有1%的几率使1个技能的冷却时间初始化。（辅助职业除外）
    """
    char.SetStatus(SkillAttack=0.035)
    pass


@register
def stone_312(char: CharacterProperty):
    """
    创造：扭曲的时间

    技能伤害+5.5%
    释放技能时，有10%的几率初始化已使用技能的冷却时间。（觉醒技能除外）
    -相同技能间存在10秒冷却时间
    释放冷却时间超过1秒的技能时，有1%的几率使1个技能的冷却时间初始化。（辅助职业除外）
    """
    char.SetStatus(SkillAttack=0.055)
    pass


# endregion
# region 纳波尔通宝-无知 套装


@register
def stone_313(char: CharacterProperty):
    """
    无知：时降雷霆

    技能伤害+4.5%
    气候之力引发灾害攻击敌人。
    -灾害伤害量：453600%
    -冷却时间：40秒
    """
    char.SetStatus(SkillAttack=0.045)
    char.equ_effect.append(EquEffect(name='无知：时降雷霆', data=453600, cd=40, icon='/equipment/icon/amalgamationstone/00375.png'))
    pass


@register
def stone_314(char: CharacterProperty):
    """
    无知：灾祸无常

    技能伤害+6.5%
    气候之力引发灾害攻击敌人。
    -灾害伤害量：453600%
    -冷却时间：40秒
    """
    char.SetStatus(SkillAttack=0.08)
    char.equ_effect.append(EquEffect(name='无知：灾祸无常', data=453600, cd=40, icon='/equipment/icon/amalgamationstone/00378.png'))
    pass


@register
def stone_315(char: CharacterProperty):
    """
    无知：刹那遗忘

    技能伤害+15%
    赋予精灵的庇佑。
    -为目标提供恢复
    -每秒恢复0.5%的生命值/魔法值
    """
    char.SetStatus(SkillAttack=0.15)
    pass


@register
def stone_316(char: CharacterProperty):
    """
    无知：永恒遗忘

    技能伤害+17%
    赋予精灵的庇佑。
    -为目标提供恢复
    -每秒恢复0.5%的生命值/魔法值

    生命值数值为70%及以下时，庇佑效果强化。
    -每秒额外恢复0.5%的生命值/魔法值

    生命值数值不足30%时，庇佑消失并立即恢复。(冷却时间300秒)
    -恢复30%的生命值/魔法值
    -消失的庇佑于30秒后复原
    """
    char.SetStatus(SkillAttack=0.185)
    pass


@register
def stone_317(char: CharacterProperty):
    """
    无知：时沐甘露

    技能伤害+15%
    获得生命值最大值7%的[填充型保护罩]。
    - 按照装备、消耗品、恢复技能提供的生命值恢复量的10%，恢复保护罩。
    - 持续恢复的技能除外
    """
    char.SetStatus(SkillAttack=0.15)
    pass


@register
def stone_318(char: CharacterProperty):
    """
    无知：天性非害

    技能伤害+17%
    进入霸体状态。
    获得生命值最大值10%的[填充型保护罩]。
    - 按照装备、消耗品、恢复技能提供的生命值恢复量的10%，恢复保护罩。
    - 持续恢复的技能除外
    """
    char.SetStatus(SkillAttack=0.185)
    pass


# endregion
# region 人造神通宝


@register
def stone_319(char: CharacterProperty):
    """
    设计：初型辅助模块 --

    技能伤害+13.5%
    """
    char.SetStatus(SkillAttack=0.135)
    pass


@register
def stone_320(char: CharacterProperty):
    """
    设计：初型辅助模块 35

    技能伤害+12.5%
    35级主动技能攻击力+7%
    """
    char.SetStatus(SkillAttack=0.125)
    char.SetSkillRation(35,35,0.07)
    pass


@register
def stone_321(char: CharacterProperty):
    """
    设计：初型辅助模块 40

    技能伤害+12.5%
    40级主动技能攻击力+7%
    """
    char.SetStatus(SkillAttack=0.125)
    char.SetSkillRation(40,40,0.07)
    pass


@register
def stone_322(char: CharacterProperty):
    """
    设计：初型辅助模块 45

    技能伤害+12.5%
    45级主动技能攻击力+7%
    """
    char.SetStatus(SkillAttack=0.125)
    char.SetSkillRation(45,45,0.07)
    pass


@register
def stone_323(char: CharacterProperty):
    """
    设计：初型辅助模块 60

    技能伤害+12.5%
    60级主动技能攻击力+7%
    """
    char.SetStatus(SkillAttack=0.125)
    char.SetSkillRation(60,60,0.07)
    pass


@register
def stone_324(char: CharacterProperty):
    """
    设计：初型辅助模块 70

    技能伤害+12.5%
    70级主动技能攻击力+7%
    """
    char.SetStatus(SkillAttack=0.125)
    char.SetSkillRation(70,70,0.07)
    pass


@register
def stone_325(char: CharacterProperty):
    """
    设计：初型辅助模块 75

    技能伤害+12.5%
    75级主动技能攻击力+7%
    """
    char.SetStatus(SkillAttack=0.125)
    char.SetSkillRation(75,75,0.07)
    pass


@register
def stone_326(char: CharacterProperty):
    """
    设计：初型辅助模块 80

    技能伤害+12.5%
    80级主动技能攻击力+7%
    """
    char.SetStatus(SkillAttack=0.125)
    char.SetSkillRation(80,80,0.07)
    pass


@register
def stone_327(char: CharacterProperty):
    """
    设计：初型辅助模块 --

    技能伤害+14.5%
    技能范围+7%
    """
    char.SetStatus(SkillAttack=0.175)
    pass


@register
def stone_328(char: CharacterProperty):
    """
    设计：初型辅助模块 35

    技能伤害+14.5%
    35级主动技能攻击力 +12%
    35级技能范围 +12%
    """
    char.SetStatus(SkillAttack=0.16)
    char.SetSkillRation(35,35,0.12)
    pass


@register
def stone_329(char: CharacterProperty):
    """
    设计：初型辅助模块 40

    技能伤害+14.5%
    40级主动技能攻击力 +12%
    40级技能范围 +12%
    """
    char.SetStatus(SkillAttack=0.16)
    char.SetSkillRation(40,40,0.12)
    pass


@register
def stone_330(char: CharacterProperty):
    """
    设计：初型辅助模块 45

    技能伤害+14.5%
    45级主动技能攻击力 +12%
    45级技能范围 +12%
    """
    char.SetStatus(SkillAttack=0.16)
    char.SetSkillRation(45,45,0.12)
    pass


@register
def stone_331(char: CharacterProperty):
    """
    设计：初型辅助模块 60

    技能伤害+14.5%
    60级主动技能攻击力 +12%
    60级技能范围 +12%
    """
    char.SetStatus(SkillAttack=0.16)
    char.SetSkillRation(60,60,0.12)


@register
def stone_332(char: CharacterProperty):
    """
    设计：初型辅助模块 70

    技能伤害+14.5%
    70级主动技能攻击力 +12%
    70级技能范围 +12%
    """
    char.SetStatus(SkillAttack=0.16)
    char.SetSkillRation(70,70,0.12)
    pass


@register
def stone_333(char: CharacterProperty):
    """
    设计：初型辅助模块 75

    技能伤害+14.5%
    75级主动技能攻击力 +12%
    75级技能范围 +12%
    """
    char.SetStatus(SkillAttack=0.16)
    char.SetSkillRation(75,75,0.12)
    pass


@register
def stone_334(char: CharacterProperty):
    """
    设计：初型辅助模块 80

    技能伤害+14.5%
    80级主动技能攻击力 +12%
    80级技能范围 +12%
    """
    char.SetStatus(SkillAttack=0.16)
    char.SetSkillRation(80,80,0.12)
    pass


@register
def stone_335(char: CharacterProperty):
    """
    设计：初型附加模块 --

    技能伤害+13.5%
    """
    stone_319(char)
    pass


@register
def stone_336(char: CharacterProperty):
    """
    设计：初型附加模块 35

    技能伤害+12.5%
    35级主动技能攻击力+7%
    """
    stone_320(char)
    pass


@register
def stone_337(char: CharacterProperty):
    """
    设计：初型附加模块 40

    技能伤害+12.5%
    40级主动技能攻击力+7%
    """
    stone_321(char)
    pass


@register
def stone_338(char: CharacterProperty):
    """
    设计：初型附加模块 45

    技能伤害+12.5%
    45级主动技能攻击力+7%
    """
    stone_322(char)
    pass


@register
def stone_339(char: CharacterProperty):
    """
    设计：初型附加模块 60

    技能伤害+12.5%
    60级主动技能攻击力+7%
    """
    stone_323(char)
    pass


@register
def stone_340(char: CharacterProperty):
    """
    设计：初型附加模块 70

    技能伤害+12.5%
    70级主动技能攻击力+7%
    """
    stone_324(char)
    pass


@register
def stone_341(char: CharacterProperty):
    """
    设计：初型附加模块 75

    技能伤害+12.5%
    75级主动技能攻击力+7%
    """
    stone_325(char)
    pass


@register
def stone_342(char: CharacterProperty):
    """
    设计：初型附加模块 80

    技能伤害+12.5%
    80级主动技能攻击力+7%
    """
    stone_326(char)
    pass


@register
def stone_343(char: CharacterProperty):
    """
    设计：初型附加模块 --

    技能伤害+14.5%
    技能范围+7%
    """
    stone_327(char)
    pass


@register
def stone_344(char: CharacterProperty):
    """
    设计：初型附加模块 35

    技能伤害+14.5%
    35级主动技能攻击力 +12%
    35级技能范围 +12%
    """
    stone_328(char)
    pass


@register
def stone_345(char: CharacterProperty):
    """
    设计：初型附加模块 40

    技能伤害+14.5%
    40级主动技能攻击力 +12%
    40级技能范围 +12%
    """
    stone_329(char)
    pass


@register
def stone_346(char: CharacterProperty):
    """
    设计：初型附加模块 45

    技能伤害+14.5%
    45级主动技能攻击力 +12%
    45级技能范围 +12%
    """
    stone_330(char)
    pass


@register
def stone_347(char: CharacterProperty):
    """
    设计：初型附加模块 60

    技能伤害+14.5%
    60级主动技能攻击力 +12%
    60级技能范围 +12%
    """
    stone_331(char)
    pass


@register
def stone_348(char: CharacterProperty):
    """
    设计：初型附加模块 70

    技能伤害+14.5%
    70级主动技能攻击力 +12%
    70级技能范围 +12%
    """
    stone_332(char)
    pass


@register
def stone_349(char: CharacterProperty):
    """
    设计：初型附加模块 75

    技能伤害+14.5%
    75级主动技能攻击力 +12%
    75级技能范围 +12%
    """
    stone_333(char)
    pass


@register
def stone_350(char: CharacterProperty):
    """
    设计：初型附加模块 80

    技能伤害+14.5%
    80级主动技能攻击力 +12%
    80级技能范围 +12%
    """
    stone_334(char)
    pass


@register
def stone_351(char: CharacterProperty):
    """
    设计：初型信号模块 --

    技能伤害+13.5%
    """
    stone_319(char)
    pass


@register
def stone_352(char: CharacterProperty):
    """
    设计：初型信号模块 35

    技能伤害+12.5%
    35级主动技能攻击力+7%
    """
    stone_320(char)
    pass


@register
def stone_353(char: CharacterProperty):
    """
    设计：初型信号模块 40

    技能伤害+12.5%
    40级主动技能攻击力+7%
    """
    stone_321(char)
    pass


@register
def stone_354(char: CharacterProperty):
    """
    设计：初型信号模块 45

    技能伤害+12.5%
    45级主动技能攻击力+7%
    """
    stone_322(char)
    pass


@register
def stone_355(char: CharacterProperty):
    """
    设计：初型信号模块 60

    技能伤害+12.5%
    60级主动技能攻击力+7%
    """
    stone_323(char)
    pass


@register
def stone_356(char: CharacterProperty):
    """
    设计：初型信号模块 70

    技能伤害+12.5%
    70级主动技能攻击力+7%
    """
    stone_324(char)
    pass


@register
def stone_357(char: CharacterProperty):
    """
    设计：初型信号模块 75

    技能伤害+12.5%
    75级主动技能攻击力+7%
    """
    stone_325(char)
    pass


@register
def stone_358(char: CharacterProperty):
    """
    设计：初型信号模块 80

    技能伤害+12.5%
    80级主动技能攻击力+7%
    """
    stone_326(char)
    pass


@register
def stone_359(char: CharacterProperty):
    """
    设计：初型信号模块 --

    技能伤害+14.5%
    技能范围+7%
    """
    stone_327(char)
    pass


@register
def stone_360(char: CharacterProperty):
    """
    设计：初型信号模块 35

    技能伤害+14.5%
    35级主动技能攻击力 +12%
    35级技能范围 +12%
    """
    stone_328(char)
    pass


@register
def stone_361(char: CharacterProperty):
    """
    设计：初型信号模块 40

    技能伤害+14.5%
    40级主动技能攻击力 +12%
    40级技能范围 +12%
    """
    stone_329(char)
    pass


@register
def stone_362(char: CharacterProperty):
    """
    设计：初型信号模块 45

    技能伤害+14.5%
    45级主动技能攻击力 +12%
    45级技能范围 +12%
    """
    stone_330(char)
    pass


@register
def stone_363(char: CharacterProperty):
    """
    设计：初型信号模块 60

    技能伤害+14.5%
    60级主动技能攻击力 +12%
    60级技能范围 +12%
    """
    stone_331(char)
    pass


@register
def stone_364(char: CharacterProperty):
    """
    设计：初型信号模块 70

    技能伤害+14.5%
    70级主动技能攻击力 +12%
    70级技能范围 +12%
    """
    stone_332(char)
    pass


@register
def stone_365(char: CharacterProperty):
    """
    设计：初型信号模块 75

    技能伤害+14.5%
    75级主动技能攻击力 +12%
    75级技能范围 +12%
    """
    stone_333(char)
    pass


@register
def stone_366(char: CharacterProperty):
    """
    设计：初型信号模块 80

    技能伤害+14.5%
    80级主动技能攻击力 +12%
    80级技能范围 +12%
    """
    stone_334(char)
    pass


# endregion


# region 神界


@register
def stone_1000(char: CharacterProperty):
    """
    馥郁的欢愉

    属性1
    技能伤害+11.5%

    [恍惚之境]
    融合的装备强化/增幅从10开始每增加1时，技能伤害+1%（最多叠加2次）

    属性2
    攻击速度+5%
    释放速度+7.5%

    属性3
    攻击时，恢复1000点魔法值。（冷却时间1秒）
    """
    char.SetStatus(SkillAttack=0.115, SpeedA=0.05, SpeedM=0.075)
    value = char.charEquipInfo['项链'].reinforce
    if value >= 10:
        char.SetStatus(SkillAttack=0.01 * min(value - 10, 2))
    pass


@register
def stone_1001(char: CharacterProperty):
    """
    逆流的记忆

    属性1
    技能伤害+3.5%

    [时间逆行者]
    释放技能时，有10%的几率初始化已使用技能的冷却时间。（觉醒技能除外）
    -相同技能间存在10秒冷却时间

    属性2
    攻击时，恢复1000点魔法值。（冷却时间1秒）

    属性3
    物理/魔法防御力+2000
    """
    char.SetStatus(SkillAttack=0.035)
    pass


@register
def stone_1002(char: CharacterProperty):
    """
    爆发的噩梦

    属性1
    技能伤害+5.5%
    50、85、100级技能攻击力+11%
    50、85、100级技能冷却时间恢复速度+15%（辅助职业除外）

    属性2
    生命值最大值+200

    属性3
    魔法值最大值+300
    """
    char.SetStatus(SkillAttack=0.055)
    for skill in char.skills:
        if skill.learnLv in [50, 85, 100]:
            skill.skillRation *= 1.11
            skill.cdRecover += 0.15
    pass


@register
def stone_1003(char: CharacterProperty):
    """
    佩鲁斯帝国的荣光

    属性1
    技能伤害+13%

    属性2
    魔法值最大值+300

    属性3
    物理/魔法防御力+2000
    """
    char.SetStatus(SkillAttack=0.13)
    pass


@register
def stone_1004(char: CharacterProperty):
    """
    红兔

    属性1
    技能伤害+1.5%
    技能冷却时间-7%（觉醒技能除外）
    所有属性强化+7

    [红兔的礼物]
    释放技能时，有7.77%的几率使技能攻击力+77%

    属性2
    生命值最大值+7%

    属性3
    魔法值最大值+7%
    """
    char.SetStatus(SkillAttack=0.015)
    char.SetSkillCD(1, 100, 0.07)
    char.AddElementDB('火', 7)
    char.AddElementDB('冰', 7)
    char.AddElementDB('光', 7)
    char.AddElementDB('暗', 7)
    pass


@register
def stone_1005(char: CharacterProperty):
    """
    回忆的低语

    属性1
    技能伤害+11.5%

    [恍惚之境]
    融合的装备强化/增幅从10开始每增加1时，技能伤害+1%（最多叠加2次）

    属性2
    移动速度+5%

    属性3
    攻击时，恢复1000点生命值。（冷却时间1秒）
    """
    char.SetStatus(SkillAttack=0.115, SpeedA=0.05)
    value = char.charEquipInfo['戒指'].reinforce
    if value >= 10:
        char.SetStatus(SkillAttack=0.01 * min(value - 10, 2))
    pass


@register
def stone_1006(char: CharacterProperty):
    """
    遗忘魔石

    属性1
    技能伤害+11.5%

    [冥河中流淌的记忆]
    释放冷却时间超过1秒的技能时，有1%的几率使1个技能的冷却时间初始化。（辅助职业除外）

    属性2
    所受物理/魔法伤害-5%

    属性3
    魔法值最大值+300
    """
    char.SetStatus(SkillAttack=0.115)
    pass


@register
def stone_1007(char: CharacterProperty):
    """
    孵化的恶意之种

    属性1
    技能伤害+5.5%
    50、85、100级技能攻击力+11%
    50、85、100级技能冷却时间恢复速度+15%（辅助职业除外）

    属性2
    生命值最大值+200

    属性3
    魔法值最大值+300
    """
    char.SetStatus(SkillAttack=0.055)
    for skill in char.skills:
        if skill.learnLv in [50, 85, 100]:
            skill.skillRation *= 1.11
            skill.cdRecover += 0.15
    pass


@register
def stone_1008(char: CharacterProperty):
    """
    世界偶像戒指

    属性1
    [目光焦点]
    -技能伤害+6.5%
    -技能冷却时间-10%（觉醒技能除外）
    -进入霸体状态
    -生成聚光灯

    属性2
    所受物理/魔法伤害-5%

    属性3
    攻击时，恢复1000点魔法值。（冷却时间1秒）
    """
    char.SetStatus(SkillAttack=0.065)
    char.SetSkillCD(1, 100, 0.10)
    pass


@register
def stone_1009(char: CharacterProperty):
    """
    辨明异徒的食指

    属性1
    [铲除异徒]
    将敌人定义为异徒。
    攻击异徒时，技能伤害+13%

    属性2
    生命值最大值+200

    属性3
    物理/魔法防御力+2000
    """
    char.SetStatus(SkillAttack=0.13)
    pass


@register
def stone_1010(char: CharacterProperty):
    """
    无限可能性的探求

    属性1
    技能伤害+5.5%
    50、85、100级技能攻击力+8%
    50、85、100级技能冷却时间恢复速度+15%（辅助职业除外）

    属性2
    生命值最大值+200

    属性3
    魔法值最大值+300
    """
    char.SetStatus(SkillAttack=0.055)
    for skill in char.skills:
        if skill.learnLv in [50, 85, 100]:
            skill.skillRation *= 1.08
            skill.cdRecover += 0.15
    pass


@register
def stone_1011(char: CharacterProperty):
    """
    技能延展

    属性1
    技能伤害+10.5%

    属性2
    技能范围+23%

    属性3
    物理/魔法防御力+2000
    """
    char.SetStatus(SkillAttack=0.105)
    pass


@register
def stone_1012(char: CharacterProperty):
    """
    无限可能性的痕迹

    属性1
    技能伤害+5.5%
    50、85、100级技能攻击力+8%
    50、85、100级技能冷却时间恢复速度+15%（辅助职业除外）

    属性2
    生命值最大值+200

    属性3
    魔法值最大值+300
    """
    char.SetStatus(SkillAttack=0.055)
    for skill in char.skills:
        if skill.learnLv in [50, 85, 100]:
            skill.skillRation *= 1.08
            skill.cdRecover += 0.15
    pass


@register
def stone_1013(char: CharacterProperty):
    """
    无限可能性的流动

    属性1
    技能伤害+5.5%
    50、85、100级技能攻击力+8%
    50、85、100级技能冷却时间恢复速度+15%（辅助职业除外）

    属性2
    生命值最大值+200

    属性3
    魔法值最大值+300
    """
    char.SetStatus(SkillAttack=0.055)
    for skill in char.skills:
        if skill.learnLv in [50, 85, 100]:
            skill.skillRation *= 1.08
            skill.cdRecover += 0.15
    pass


@register
def stone_1014(char: CharacterProperty):
    """
    死神的陷阱

    属性1
    技能伤害+11.5%

    属性2
    技能范围+7%

    属性3
    生命值最大值+5%
    """
    char.SetStatus(SkillAttack=0.115)
    pass


@register
def stone_1015(char: CharacterProperty):
    """
    混沌的漩涡

    属性1
    技能伤害+1.5%
    85级技能攻击力+30%
    85级技能冷却时间恢复速度+100%（辅助职业除外）

    属性2
    所受物理/魔法伤害-5%

    属性3
    移动速度+4%
    """
    char.SetStatus(SkillAttack=0.015)
    for skill in char.skills:
        if skill.learnLv == 85:
            skill.skillRation *= 1.30
            skill.cdRecover += 1.00
    pass


@register
def stone_1016(char: CharacterProperty):
    """
    和平的往昔

    属性1
    技能伤害+11.5%


    属性2
    获得生命最最大值10%的保护罩，效果持续5秒。（冷却时间5秒）

    属性3
    攻击时，恢复300点生命值。（冷却时间1秒）
    """
    char.SetStatus(SkillAttack=0.115)
    pass


@register
def stone_1017(char: CharacterProperty):
    """
    天堂的守护

    属性1
    技能伤害+10.5%

    [不灭之术]
    生命终结判定时，发动[不灭之术]，效果持续1秒。（冷却时间120秒）
    -恢复1%生命值
    -其他生命值恢复效果及伤害变为无效

    属性2
    生命值最大值+1000

    属性3
    魔法值最大值+1000
    """
    char.SetStatus(SkillAttack=0.105)
    pass


@register
def stone_1018(char: CharacterProperty):
    """
    末日的预告

    属性1
    技能伤害+11.5%

    属性2
    移动速度+20%

    属性3
    物理/魔法防御力+2000
    """
    char.SetStatus(SkillAttack=0.115, SpeedA=0.20)
    pass


# endregion
