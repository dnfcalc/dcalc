from abc import ABC, abstractmethod
from typing import Any, Literal, Mapping

class CharacterProperty(ABC):
    """
    抽象类，用于定义Character的接口和属性
    """

    # region 角色属性
    STR: float
    """力量"""

    INT: float
    """智力"""

    Spirit: float
    """精神"""

    Vitality: float
    """体力"""

    AtkP: float
    """物理攻击力"""

    PAtkP: float
    """物理攻击力%"""

    AtkM: float
    """魔法攻击力"""

    PAtkM: float
    """魔法攻击力%"""

    AtkI: float
    """独立攻击力"""

    PAtkI: float
    """独立攻击力%"""

    ElementA: dict[str, float]
    """属性攻击"""

    ElementIncrease: float
    """属性增幅"""

    ElementDB: dict[str, float]
    """属性强化数值"""

    ElementR: dict[str, float]
    """属性抗性数值"""

    CriticalM: float
    """魔法暴击"""

    CriticalP: float
    """物理暴击"""

    SkillAttack: float
    """技能攻击力"""

    SpeedA: float
    """攻击速度"""

    SpeedM: float
    """移动速度"""

    SpeedR: float
    """施放速度"""

    Hit: float
    """命中率"""

    Abnormal: dict[str, bool]
    """敌人异常状态"""

    MonsterInfo: dict[str, float]
    """怪物信息"""

    jade_effect: Any
    """辟邪玉加成"""

    Buffer: float
    """增益量"""

    BufferP: float
    """增益量%"""

    Attack: float
    """攻击强化"""

    AttackP: float
    """攻击强化%"""

    # endregion

    # region 职业属性
    实际名称: str
    名称: str
    角色: str
    角色类型: str
    职业: str
    武器选项: list[str]
    副武器选项: list[str]
    输出类型选项: list[str]
    防具精通属性: list[str]
    输出类型: str
    # endregion

    @abstractmethod
    def SetBaseStatus(self) -> None:
        """设角色基础属性"""
        pass

    @abstractmethod
    def SetStatus(
        self,
        力量=0,
        智力=0,
        力智=0,
        体力=0,
        精神=0,
        体精=0,
        四维=0,
        物攻=0,
        魔攻=0,
        独立=0,
        三攻=0,
        技攻=0,
        全属强=0,
        火强=0,
        冰强=0,
        光强=0,
        暗强=0,
        全属抗=0,
        火属性抗性=0,
        冰属性抗性=0,
        光属性抗性=0,
        暗属性抗性=0,
        火属性攻击=False,
        冰属性攻击=False,
        光属性攻击=False,
        暗属性攻击=False,
        移动速度=0,
        攻击速度=0,
        施放速度=0,
        三速=0,
        命中=0,
        命中率=0,
        物暴=0,
        魔暴=0,
        攻击强化=0,
        攻击强化P=0,
        增益量=0,
        增益量P=0,
        **kwargs: Mapping[Literal[
                'STR',
                'INT',
                'AtkP',
                'AtkM',
                'AtkI',
                'PAtkP',
                'PAtkM',
                'PAtkI',
                'PATKIPDamage',
                'PDamageC',
                'PSTR',
                'PINT',
                'PDamageB',
                'ElementA',
                'ElementDB',
                'ElementR',
                'CriticalMP',
                'CriticalM',
                'CriticalPP',
                'CriticalP',
                'EquipmentSkillAttack',
                'SkillAttack',
                'SpeedA',
                'SpeedM',
                'SpeedR',
                'HitP',
                'Hit',
                'Attack',
                'AttackP',
                'Buffer',
                'BufferP',
                'Spirit',
                'Vitality',
                'EquEffectRatio',
            ], Any],
    ) -> None:
        """设置角色属性"""
        pass

    @abstractmethod
    def AddElementDB(self, element: str, value: float, type: int = 0) -> None:
        """增加属性强化"""
        pass

    @abstractmethod
    def AddSkillLv(self, min: int, max: int, lv: int, type=-1,exceptSkills:list[str]=[]) -> None:
        """增加技能等级"""
        pass

    @abstractmethod
    def SetSkillCD(self, min=1, max=100, cd=0, exclude=[50, 85, 100]) -> None:
        """设置技能CD"""
        pass

    @abstractmethod
    def SetSkillCDRecover(self, min=1, max=100, cd=0, exclude=[50, 85, 100]) -> None:
        """设置技能CD恢复"""
        pass

    @abstractmethod
    def SetSkillRation(self, min=1, max=100, ratio=0, type=0) -> None:
        """设置技能倍率"""
        pass

    @abstractmethod
    def GetSkillByName(self, name) -> Any:
        """通过技能名获取技能"""
        pass

    @abstractmethod
    def GetSkillByID(self, id: str) -> Any:
        """通过技能ID获取技能"""
        pass

    @abstractmethod
    def GetSkillNames(self, type: Literal['active', 'passive', 'all'] = 'all', damage: Literal[True, False, 'all'] = 'all') -> list[str]:
        """获取技能名字"""
        pass

    @abstractmethod
    def calc(self, setInfo: dict[str, dict]) -> dict:
        """计算角色属性"""
        pass
