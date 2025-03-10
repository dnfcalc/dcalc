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
    emblems: list[str]
    """徽章"""
    fusion: int | None
    """贴膜ID"""
    refine: int | None
    """锻造等级"""
    fusionDetail: dict | None
    """贴膜详情"""
    adaptation: int
    """调适等级"""
    equInfo: Union['Equ', None]
    """装备信息"""
    fusionInfo: Union['Equ', None]
    """贴膜信息"""

    def __init__(self, info={}, equVerison=0, part='') -> None:
        self.__dict__.update(info)
        equ = get_equipment(equVerison).equ_dict.get(self.id, None)
        if equ is not None and (equ.itemType == part or equ.itemDetailType == part):
            self.equInfo = equ.adapt(self.adaptation)
        else:
            self.equInfo = None


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


mapping = {value: key for key, value in CharacterAttributes.__members__.items()}


def get_key_by_value(value: str) -> str:
    return mapping[value]
