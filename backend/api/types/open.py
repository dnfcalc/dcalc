from enum import Enum
from pydantic import BaseModel, Field
from typing import Generic, TypeVar
from pydantic.generics import GenericModel
from api.core.Response import Return as Response


class SkillInfo(BaseModel):
    skillId: str = Field(..., description='技能ID')
    """技能ID"""
    skillName: str = Field(..., description='技能名称')
    """技能名称"""
    jobId: str = Field(..., description='职业Id')
    """职业Id"""
    jobName: str = Field(..., description='职业名称')
    """职业名称"""
    jobGrowId: str = Field(..., description='转职Id')
    """转职Id"""
    jobGrowName: str = Field(..., description='转职名称')
    """转职名称"""


class SkillType(str, Enum):
    active = 'active'
    """主动技能"""
    passive = 'passive'
    """被动技能"""
    buff = 'buff'
    """增益技能"""
    debuff = 'debuff'
    """减益技能"""
    summon = 'summon'
    """召唤技能"""
    other = 'other'
    """其他类型技能"""


class IConsumeItem(BaseModel):
    itemId: str = Field(..., description='物品ID')
    """物品ID"""
    itemName: str = Field(..., description='物品名称')
    """物品名称"""
    value: int = Field(..., description='物品类型')
    """物品类型"""


class IPreSkill(BaseModel):
    level: int = Field(..., description='前置技能等级')
    """前置技能等级"""
    name: str = Field(..., description='前置技能名称')
    """前置技能名称"""
    skillId: str = Field(..., description='前置技能ID')
    """前置技能ID"""


class IAttribute(BaseModel):
    castingTime: float | None = Field(None, description='施放时间')
    """施放时间"""
    coolTime: float | None = Field(None, description='冷却时间')
    """冷却时间"""
    consumeMp: int | None = Field(None, description='魔法值')
    """魔法值"""
    detail: str | None = Field(None, description='技能描述')
    """技能描述"""
    level: int | None = Field(None, description='技能等级')
    """技能等级"""
    optionDesc: str | None = Field(None, description='技能选项描述')
    """技能选项描述"""
    optionValue: dict[str, float | str] | None = Field(None, description='技能选项值')


class ILevelInfo(BaseModel):
    optionDesc: str | None = Field(None, description='技能选项描述')
    rows: list[IAttribute] | None = Field(None, description='技能等级信息')


class IEvolution(BaseModel):
    type: int = Field(..., description='进化类型')
    """进化类型"""
    name: str = Field(..., description='进化名称')
    """进化名称"""
    desc: str = Field(..., description='进化简介')
    """进化简介"""
    descDetail: str = Field(..., description='进化详细描述')
    """进化详细描述"""


class IKeyValues(BaseModel):
    name: str = Field(..., description='名称')
    """名称"""
    value: str = Field(..., description='数值')
    """数值"""


class IEnhancement(BaseModel):
    type: int = Field(None, description='强化类型')
    """强化类型"""
    status: list[IKeyValues] = Field(None, description='强化状态')


class SkillDetail(BaseModel):
    name: str = Field(..., description='技能名称')
    """技能名称"""
    type: SkillType = Field(..., description='技能类型')
    """技能类型"""
    desc: str | None = Field(None, description='技能描述')
    """技能描述"""
    descDetail: str | None = Field(None, description='技能详细描述')
    """技能详细描述"""
    consumeItem: IConsumeItem | None = Field(None, description='消耗物品')
    """消耗物品"""
    descSpecial: list[str] | None = Field(None, description='特殊功能')
    """特殊功能"""
    maxLevel: int = Field(..., description='等级上限')
    """等级上限"""
    requiredLevel: int = Field(..., description='学习等级')
    """学习等级"""
    requiredLevelRange: int = Field(..., description='学习间隔')
    """学习间隔"""
    preRequiredSkill: list[IPreSkill] | None = Field(None, description='前置技能')
    """前置技能"""
    jobId: str = Field(..., description='职业ID')
    """职业ID"""
    jobName: str = Field(..., description='职业名称')
    """职业名称"""
    levelInfo: ILevelInfo | None = Field(None, description='技能等级信息')
    """技能等级信息"""
    attribute: IAttribute | None = Field(None, description='技能属性')
    """技能属性"""
    evolution: list[IEvolution] | None = Field(None, description='技能进化信息')
    """技能进化信息"""
    enhancement: list[IEnhancement] | None = Field(None, description='技能强化信息')
    """技能强化信息"""


SkillDetailResponse = Response[SkillDetail | None]
SkillsListResponse = Response[list[SkillInfo]]
