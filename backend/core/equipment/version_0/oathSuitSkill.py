import inspect

from core.abstract.character import CharacterProperty
from core.basic.equipment import EquEffect
from .register import register


def check_suit(char: CharacterProperty) -> bool:
    caller_frame = inspect.stack()[1]
    fun_name = caller_frame.function
    suitId = int(fun_name.split('_')[-1]) % 10000 + 16000
    print(f'检查套装 {suitId}')
    return next((x for x in char.suitInfo if x.suitId == suitId), None) is not None


# region 潜影暗袭


@register
def oath_skill_2010101(char: CharacterProperty):
    pass


@register
def oath_skill_2010102(char: CharacterProperty):
    pass


@register
def oath_skill_2010103(char: CharacterProperty):
    pass


@register
def oath_skill_2010201(char: CharacterProperty):
    pass


@register
def oath_skill_2010202(char: CharacterProperty):
    pass


@register
def oath_skill_2010203(char: CharacterProperty):
    pass


@register
def oath_skill_2010301(char: CharacterProperty):
    pass


@register
def oath_skill_2010302(char: CharacterProperty):
    pass


@register
def oath_skill_2010303(char: CharacterProperty):
    pass


@register
def oath_skill_2010401(char: CharacterProperty):
    pass


@register
def oath_skill_2010402(char: CharacterProperty):
    pass


@register
def oath_skill_2010403(char: CharacterProperty):
    pass


@register
def oath_skill_2010501(char: CharacterProperty):
    pass


@register
def oath_skill_2010502(char: CharacterProperty):
    pass


@register
def oath_skill_2010503(char: CharacterProperty):
    pass


# endregion


# region 精灵国度
@register
def oath_skill_2020101(char: CharacterProperty):
    pass


@register
def oath_skill_2020102(char: CharacterProperty):
    pass


@register
def oath_skill_2020103(char: CharacterProperty):
    pass


@register
def oath_skill_2020201(char: CharacterProperty):
    pass


@register
def oath_skill_2020202(char: CharacterProperty):
    pass


@register
def oath_skill_2020203(char: CharacterProperty):
    pass


@register
def oath_skill_2020301(char: CharacterProperty):
    pass


@register
def oath_skill_2020302(char: CharacterProperty):
    pass


@register
def oath_skill_2020303(char: CharacterProperty):
    pass


@register
def oath_skill_2020401(char: CharacterProperty):
    pass


@register
def oath_skill_2020402(char: CharacterProperty):
    pass


@register
def oath_skill_2020403(char: CharacterProperty):
    pass


@register
def oath_skill_2020501(char: CharacterProperty):
    pass


@register
def oath_skill_2020502(char: CharacterProperty):
    pass


@register
def oath_skill_2020503(char: CharacterProperty):
    pass


# endregion


# region 理想之黄金乡
@register
def oath_skill_2030101(char: CharacterProperty):
    oath_skill_2030501(char)
    pass


@register
def oath_skill_2030102(char: CharacterProperty):
    pass


@register
def oath_skill_2030103(char: CharacterProperty):
    pass


@register
def oath_skill_2030201(char: CharacterProperty):
    pass


@register
def oath_skill_2030202(char: CharacterProperty):
    pass


@register
def oath_skill_2030203(char: CharacterProperty):
    pass


@register
def oath_skill_2030301(char: CharacterProperty):
    pass


@register
def oath_skill_2030302(char: CharacterProperty):
    pass


@register
def oath_skill_2030303(char: CharacterProperty):
    pass


@register
def oath_skill_2030401(char: CharacterProperty):
    pass


@register
def oath_skill_2030402(char: CharacterProperty):
    pass


@register
def oath_skill_2030403(char: CharacterProperty):
    pass


@register
def oath_skill_2030501(char: CharacterProperty):
    # 所有速度+7%
    # 技能范围+14%
    # 所受伤害-14%

    # 根据防具/首饰/特殊装备的强化/增幅数值总和，适用以下效果。
    # - 每+11，技能伤害+0.5%（最多可叠加12次）
    # - 防具：每+5，所受伤害-0.5%（最多可叠加12次）
    # - 首饰：每+3，技能范围+1%（最多可叠加12次）
    # - 特殊装备：每+3，所有速度+1%（最多可叠加12次）

    # 穿戴[黄金乡：永恒国度]套装时，根据防具/首饰/特殊装备的强化/增幅数值总和，适用以下效果：
    # - 110以上：技能伤害+0.5%
    # - 121以上：技能伤害+1.5%
    # - 132以上：技能伤害+2.5%，赋予霸体，删除[淘金热]
    char.SetStatus(SpeedA=0.07, SpeedM=0.07, SpeedR=0.07)
    reinforce, reinforce_0, reinforce_1, reinforce_2 = char.GetReinforceSum()
    char.SetStatus(SkillAttack=0.005 * min(reinforce_1 // 3, 12))
    char.SetStatus(SpeedA=0.01 * min(reinforce_2 // 3, 12))
    char.SetStatus(SpeedM=0.01 * min(reinforce_2 // 3, 12))
    char.SetStatus(SpeedR=0.01 * min(reinforce_2 // 3, 12))
    if check_suit(char):
        print('穿戴黄金乡')
        char.SetStatus(SkillRange=0.02 * min(reinforce // 11, 12))
        # char.SetStatus(DamageReduce=0.01 * min(reinforce_0 // 5, 7))
        char.SetStatus(SkillAttack=0.01 * min(reinforce_1 // 3, 12))
        char.SetStatus(SpeedA=0.02 * min(reinforce_2 // 3, 12))
        char.SetStatus(SpeedM=0.02 * min(reinforce_2 // 3, 12))
        char.SetStatus(SpeedR=0.02 * min(reinforce_2 // 3, 12))
        if char.buffer:
            char.SetSkillCD(cd=0.02 * min(reinforce // 1, 12))
        if reinforce >= 110:
            char.SetStatus(SkillAttack=0.02 * min((reinforce - 110) // 11, 2))
            if char.buffer:
                char.SetStatus(Buffer=1500 * min((reinforce - 110) // 11, 2))
            # TODO
            #             穿戴[黄金乡：永恒国度]套装时，根据防具/首饰/特殊装备的强化/增幅数值总和，适用以下效果：
            # - 110以上：技能伤害+0.5%
            # - 121以上：技能伤害+1.5%
            # - 132以上：技能伤害+2.5%，赋予霸体，删除[淘金热]
    pass


@register
def oath_skill_2030502(char: CharacterProperty):
    char.SetStatus(SkillAttack=0.132, SpeedA=0.22, SpeedM=0.22, SpeedR=0.22)
    pass


@register
def oath_skill_2030503(char: CharacterProperty):
    reinforce, reinforce_0, reinforce_1, reinforce_2 = char.GetReinforceSum()
    if reinforce >= 121:
        char.SetStatus(SkillAttack=0.1, SpeedA=0.3, SpeedM=0.3, SpeedR=0.3)
    pass


# endregion

# region 龙战八荒


@register
def oath_skill_2040101(char: CharacterProperty):
    pass


@register
def oath_skill_2040102(char: CharacterProperty):
    pass


@register
def oath_skill_2040103(char: CharacterProperty):
    pass


@register
def oath_skill_2040201(char: CharacterProperty):
    pass


@register
def oath_skill_2040202(char: CharacterProperty):
    pass


@register
def oath_skill_2040203(char: CharacterProperty):
    pass


@register
def oath_skill_2040301(char: CharacterProperty):
    pass


@register
def oath_skill_2040302(char: CharacterProperty):
    pass


@register
def oath_skill_2040303(char: CharacterProperty):
    pass


@register
def oath_skill_2040401(char: CharacterProperty):
    pass


@register
def oath_skill_2040402(char: CharacterProperty):
    pass


@register
def oath_skill_2040403(char: CharacterProperty):
    pass


@register
def oath_skill_2040501(char: CharacterProperty):
    pass


@register
def oath_skill_2040502(char: CharacterProperty):
    pass


@register
def oath_skill_2040503(char: CharacterProperty):
    pass


# endregion

# region 暗黑净化


@register
def oath_skill_2050101(char: CharacterProperty):
    pass


@register
def oath_skill_2050102(char: CharacterProperty):
    pass


@register
def oath_skill_2050103(char: CharacterProperty):
    pass


@register
def oath_skill_2050201(char: CharacterProperty):
    pass


@register
def oath_skill_2050202(char: CharacterProperty):
    pass


@register
def oath_skill_2050203(char: CharacterProperty):
    pass


@register
def oath_skill_2050301(char: CharacterProperty):
    pass


@register
def oath_skill_2050302(char: CharacterProperty):
    pass


@register
def oath_skill_2050303(char: CharacterProperty):
    pass


@register
def oath_skill_2050401(char: CharacterProperty):
    pass


@register
def oath_skill_2050402(char: CharacterProperty):
    pass


@register
def oath_skill_2050403(char: CharacterProperty):
    pass


@register
def oath_skill_2050501(char: CharacterProperty):
    pass


@register
def oath_skill_2050502(char: CharacterProperty):
    pass


@register
def oath_skill_2050503(char: CharacterProperty):
    pass


# endregion

# region 天命者的气运


@register
def oath_skill_2060101(char: CharacterProperty):
    pass


@register
def oath_skill_2060102(char: CharacterProperty):
    pass


@register
def oath_skill_2060103(char: CharacterProperty):
    pass


@register
def oath_skill_2060201(char: CharacterProperty):
    pass


@register
def oath_skill_2060202(char: CharacterProperty):
    pass


@register
def oath_skill_2060203(char: CharacterProperty):
    pass


@register
def oath_skill_2060301(char: CharacterProperty):
    pass


@register
def oath_skill_2060302(char: CharacterProperty):
    pass


@register
def oath_skill_2060303(char: CharacterProperty):
    pass


@register
def oath_skill_2060401(char: CharacterProperty):
    pass


@register
def oath_skill_2060402(char: CharacterProperty):
    pass


@register
def oath_skill_2060403(char: CharacterProperty):
    pass


@register
def oath_skill_2060501(char: CharacterProperty):
    pass


@register
def oath_skill_2060502(char: CharacterProperty):
    pass


@register
def oath_skill_2060503(char: CharacterProperty):
    pass


# endregion

# region 究极能量


@register
def oath_skill_2070101(char: CharacterProperty):
    pass


@register
def oath_skill_2070102(char: CharacterProperty):
    pass


@register
def oath_skill_2070103(char: CharacterProperty):
    pass


@register
def oath_skill_2070201(char: CharacterProperty):
    pass


@register
def oath_skill_2070202(char: CharacterProperty):
    pass


@register
def oath_skill_2070203(char: CharacterProperty):
    pass


@register
def oath_skill_2070301(char: CharacterProperty):
    pass


@register
def oath_skill_2070302(char: CharacterProperty):
    pass


@register
def oath_skill_2070303(char: CharacterProperty):
    pass


@register
def oath_skill_2070401(char: CharacterProperty):
    pass


@register
def oath_skill_2070402(char: CharacterProperty):
    pass


@register
def oath_skill_2070403(char: CharacterProperty):
    pass


@register
def oath_skill_2070501(char: CharacterProperty):
    pass


@register
def oath_skill_2070502(char: CharacterProperty):
    pass


@register
def oath_skill_2070503(char: CharacterProperty):
    pass


# endregion

# region 造化自然


@register
def oath_skill_2080101(char: CharacterProperty):
    pass


@register
def oath_skill_2080102(char: CharacterProperty):
    pass


@register
def oath_skill_2080103(char: CharacterProperty):
    pass


@register
def oath_skill_2080201(char: CharacterProperty):
    pass


@register
def oath_skill_2080202(char: CharacterProperty):
    pass


@register
def oath_skill_2080203(char: CharacterProperty):
    pass


@register
def oath_skill_2080301(char: CharacterProperty):
    pass


@register
def oath_skill_2080302(char: CharacterProperty):
    pass


@register
def oath_skill_2080303(char: CharacterProperty):
    pass


@register
def oath_skill_2080401(char: CharacterProperty):
    pass


@register
def oath_skill_2080402(char: CharacterProperty):
    pass


@register
def oath_skill_2080403(char: CharacterProperty):
    pass


@register
def oath_skill_2080501(char: CharacterProperty):
    pass


@register
def oath_skill_2080502(char: CharacterProperty):
    pass


@register
def oath_skill_2080503(char: CharacterProperty):
    pass


# endregion

# region 诸神黄昏之女武神


@register
def oath_skill_2090101(char: CharacterProperty):
    pass


@register
def oath_skill_2090102(char: CharacterProperty):
    pass


@register
def oath_skill_2090103(char: CharacterProperty):
    pass


@register
def oath_skill_2090201(char: CharacterProperty):
    pass


@register
def oath_skill_2090202(char: CharacterProperty):
    pass


@register
def oath_skill_2090203(char: CharacterProperty):
    pass


@register
def oath_skill_2090301(char: CharacterProperty):
    pass


@register
def oath_skill_2090302(char: CharacterProperty):
    pass


@register
def oath_skill_2090303(char: CharacterProperty):
    pass


@register
def oath_skill_2090401(char: CharacterProperty):
    pass


@register
def oath_skill_2090402(char: CharacterProperty):
    pass


@register
def oath_skill_2090403(char: CharacterProperty):
    pass


@register
def oath_skill_2090501(char: CharacterProperty):
    pass


@register
def oath_skill_2090502(char: CharacterProperty):
    pass


@register
def oath_skill_2090503(char: CharacterProperty):
    pass


# endregion

# region 青丘灵珠


@register
def oath_skill_2100101(char: CharacterProperty):
    pass


@register
def oath_skill_2100102(char: CharacterProperty):
    pass


@register
def oath_skill_2100103(char: CharacterProperty):
    pass


@register
def oath_skill_2100201(char: CharacterProperty):
    pass


@register
def oath_skill_2100202(char: CharacterProperty):
    pass


@register
def oath_skill_2100203(char: CharacterProperty):
    pass


@register
def oath_skill_2100301(char: CharacterProperty):
    pass


@register
def oath_skill_2100302(char: CharacterProperty):
    pass


@register
def oath_skill_2100303(char: CharacterProperty):
    pass


@register
def oath_skill_2100401(char: CharacterProperty):
    pass


@register
def oath_skill_2100402(char: CharacterProperty):
    pass


@register
def oath_skill_2100403(char: CharacterProperty):
    pass


@register
def oath_skill_2100501(char: CharacterProperty):
    pass


@register
def oath_skill_2100502(char: CharacterProperty):
    pass


@register
def oath_skill_2100503(char: CharacterProperty):
    pass


# endregion

# region 群猎美学


@register
def oath_skill_2110101(char: CharacterProperty):
    pass


@register
def oath_skill_2110102(char: CharacterProperty):
    pass


@register
def oath_skill_2110103(char: CharacterProperty):
    pass


@register
def oath_skill_2110201(char: CharacterProperty):
    pass


@register
def oath_skill_2110202(char: CharacterProperty):
    pass


@register
def oath_skill_2110203(char: CharacterProperty):
    pass


@register
def oath_skill_2110301(char: CharacterProperty):
    pass


@register
def oath_skill_2110302(char: CharacterProperty):
    pass


@register
def oath_skill_2110303(char: CharacterProperty):
    pass


@register
def oath_skill_2110401(char: CharacterProperty):
    pass


@register
def oath_skill_2110402(char: CharacterProperty):
    pass


@register
def oath_skill_2110403(char: CharacterProperty):
    pass


@register
def oath_skill_2110501(char: CharacterProperty):
    pass


@register
def oath_skill_2110502(char: CharacterProperty):
    pass


@register
def oath_skill_2110503(char: CharacterProperty):
    pass


# endregion

# region 冥思者的魔力领域


@register
def oath_skill_2120101(char: CharacterProperty):
    pass


@register
def oath_skill_2120102(char: CharacterProperty):
    pass


@register
def oath_skill_2120103(char: CharacterProperty):
    pass


@register
def oath_skill_2120201(char: CharacterProperty):
    pass


@register
def oath_skill_2120202(char: CharacterProperty):
    pass


@register
def oath_skill_2120203(char: CharacterProperty):
    pass


@register
def oath_skill_2120301(char: CharacterProperty):
    pass


@register
def oath_skill_2120302(char: CharacterProperty):
    pass


@register
def oath_skill_2120303(char: CharacterProperty):
    pass


@register
def oath_skill_2120401(char: CharacterProperty):
    pass


@register
def oath_skill_2120402(char: CharacterProperty):
    pass


@register
def oath_skill_2120403(char: CharacterProperty):
    pass


@register
def oath_skill_2120501(char: CharacterProperty):
    pass


@register
def oath_skill_2120502(char: CharacterProperty):
    pass


@register
def oath_skill_2120503(char: CharacterProperty):
    pass


# endregion
