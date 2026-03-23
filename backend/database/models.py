# import os
# import sys
from sqlalchemy import Column, Integer, Text, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import Session,declarative_base

Base = declarative_base()
metadata = Base.metadata


class SuitData(Base):
    __tablename__ = 'suit'

    id = Column(Integer, primary_key=True)
    suitId = Column(Integer)
    suitName = Column(Text)
    rarity = Column(Text)
    name = Column(Text)
    point = Column(Integer)
    level = Column(Integer)
    count = Column(Integer)
    SkillAttack = Column(Float)
    Attack = Column(Float)
    Buffer = Column(Float)
    imageUrl = Column(Text)
    value = Column(Text)
    bufferValue = Column(Text)
    fame = Column(Integer)

class EquData(Base):
    """
    装备属性映射
    首字母大写的属性为调适可能会影响到的属性
    """

    __tablename__ = 'equ'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    rarity = Column(Text)
    itemType = Column(Text)
    itemDetailType = Column(Text)
    Point = Column(Text)
    categorize = Column(Text)
    imageUrl = Column(Text)
    detail = Column(Text)
    bufferDetail = Column(Text)
    STR = Column(Text)
    INT = Column(Text)
    Vitality = Column(Text)
    Spirit = Column(Text)
    AtkP = Column(Text)
    AtkM = Column(Text)
    AtkI = Column(Text)
    SkillAttack = Column(Text)
    Attack = Column(Text)
    Buffer = Column(Text)
    suit = Column(Text)

class StoneData(Base):
    """
    装备属性映射
    首字母大写的属性为调适可能会影响到的属性
    """

    __tablename__ = 'stone'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    rarity = Column(Text)
    itemType = Column(Text)
    itemDetailType = Column(Text)
    Point = Column(Text)
    categorize = Column(Text)
    imageUrl = Column(Text)
    detail = Column(Text)
    bufferDetail = Column(Text)
    STR = Column(Text)
    INT = Column(Text)
    Vitality = Column(Text)
    Spirit = Column(Text)
    AtkP = Column(Text)
    AtkM = Column(Text)
    AtkI = Column(Text)
    SkillAttack = Column(Text)
    Attack = Column(Text)
    Buffer = Column(Text)
    suit = Column(Text)

class EnchantData(Base):
    __tablename__ = 'enchant'

    id = Column(Integer, primary_key=True)
    detail = Column(Text)
    categorize = Column(Integer)
    itemType = Column(Text)
    fame = Column(Integer)
    rarity = Column(Text)

class EmblemData(Base):
    __tablename__ = 'emblem'

    id = Column(Integer, primary_key=True)
    detail = Column(Text)
    categorize = Column(Integer)
    itemType = Column(Text)
    fame = Column(Integer)
    rarity = Column(Text)

class JadeData(Base):
    __tablename__ = 'jade'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    min = Column(Integer)
    max = Column(Integer)
    unit = Column(Text)
    pre = Column(Float)

class OathData(Base):
    """
    誓约属性映射
    首字母大写的属性为调适可能会影响到的属性
    """
    __tablename__ = 'oath'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    rarity = Column(Text)
    position = Column(Text)
    Point = Column(Integer)
    categorize = Column(Text)
    imageUrl = Column(Text)
    detail = Column(Text)
    bufferDetail = Column(Text)
    STR = Column(Text)
    INT = Column(Text)
    Vitality = Column(Text)
    Spirit = Column(Text)
    AtkP = Column(Text)
    AtkM = Column(Text)
    AtkI = Column(Text)
    SkillAttack = Column(Text)
    Attack = Column(Text)
    Buffer = Column(Text)
    suit = Column(Text)

class PrimerData(Base):
    """
    誓约属性映射
    首字母大写的属性为调适可能会影响到的属性
    """
    __tablename__ = 'primer'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    rarity = Column(Text)
    position = Column(Text)
    Point = Column(Integer)
    categorize = Column(Text)
    imageUrl = Column(Text)
    detail = Column(Text)
    bufferDetail = Column(Text)
    STR = Column(Text)
    INT = Column(Text)
    Vitality = Column(Text)
    Spirit = Column(Text)
    AtkP = Column(Text)
    AtkM = Column(Text)
    AtkI = Column(Text)
    SkillAttack = Column(Text)
    Attack = Column(Text)
    Buffer = Column(Text)
    suit = Column(Text)

class OathSuitData(Base):
    __tablename__ = 'oathSuit'

    id = Column(Integer, primary_key=True)
    key = Column(Text)
    suitId = Column(Integer)
    suitName = Column(Text)
    rarity = Column(Text)
    name = Column(Text)
    point = Column(Integer)
    count = Column(Integer)

class OathSuitSkillData(Base):
    __tablename__ = 'oathSuitSkill'

    id = Column(Integer, primary_key=True)
    key = Column(Text)
    suitId = Column(Integer)
    skillId = Column(Integer)
    name = Column(Text)
    rarity = Column(Text)
    imageUrl = Column(Text)
    SkillAttack = Column(Float)
    Attack = Column(Float)
    Buffer = Column(Float)
    value = Column(Text)
    bufferValue = Column(Text)