from enum import Enum
from typing import Union

from core.basic.equipment import Equ, get_equipment


class CharacterEquipInfo:
    id: str
    """装备ID"""
    reinforce: int
    """强化等级"""
    reinforceType: int
    """强化类型"""
    enchant: str
    """附魔"""
    emblem_0: str
    """徽章1"""
    emblem_1: str
    """徽章2"""
    fusion: int | None
    """贴膜ID"""
    refine: int | None
    """锻造等级"""
    weaponFusion: int | None
    """武器融合详情"""
    adaptation: int
    """调适等级"""
    equInfo: Union['Equ', None]
    """装备信息"""
    fusionInfo: Union['Equ', None]
    """贴膜信息"""
    precision:float
    """秘宝精度"""

    def __init__(self, info={}, equVerison=0, part='') -> None:
        info["fusion"] = info.get("fusion", None)
        info["precision"] = info.get("precision", 0)
        info["weaponFusion"] = info.get("weaponFusion", None)
        self.__dict__.update(info)
        equ = get_equipment(equVerison).equ_dict.get(self.id, None)
        fusion = get_equipment(equVerison).stone_dict.get(self.fusion, None)
        if equ is not None and (equ.itemType == part or equ.itemDetailType == part or (equ.itemType == '武器' and part == '副武器')):
            self.equInfo = equ.adapt(self.adaptation)
            self.adaptation = min(self.adaptation, self.equInfo.max_adaptation)
            if part == '副武器' and equ.itemType == '武器':
                self.equInfo.itemType = "副武器"
        else:
            self.equInfo = None
        if fusion is not None and (fusion.itemType == part or fusion.itemDetailType == part):
            self.fusionInfo = fusion.adapt(self.adaptation)
        else:
            self.fusionInfo = None


class CharacterWeaponInfo(CharacterEquipInfo):
    refine: int
    """锻造等级"""
    upgradeDetail: dict
    """贴膜详情"""

    def __init__(self, info={}) -> None:
        self.__dict__.update(info)


class Part(Enum):
    weaopn = '武器'
    title = '称号'
    coat = '上衣'
    neck = '护肩'
    pants = '下装'
    shoes = '鞋子'
    belt = '腰带'
    bracelet = '手镯'
    ring = '戒指'
    necklace = '项链'
    support = '辅助装备'
    magic_stone = '魔法石'
    earring = '耳环'


class CharacterAttributes(Enum):
    STR = '力量'
    INT = '智力'
    Spirit = '精神'
    Vitality = '体力'
    AtkP = '物理攻击力'
    AtkM = '魔法攻击力'
    AtkI = '独立攻击力'
    ElementA = '属性攻击'
    ElementDB = '属性强化数值'
    ElementR = '属性抗性数值'
    CriticalM = '魔法暴击'
    CriticalP = '物理暴击'
    SkillAttack = '技能攻击力'
    SpeedA = '攻击速度'
    SpeedM = '移动速度'
    SpeedR = '施放速度'
    Hit = '命中率'
    Abnormal = '敌人异常状态'
    MonsterInfo = '怪物信息'
    Buffer = '增益量'
    BufferP = '增益量%'
    Attack = '攻击强化'
    AttackP = '攻击强化%'


mapping = {value.value : key for key, value in CharacterAttributes.__members__.items()}


def get_key_by_value(value: str) -> str:
    return mapping[value]
