from enum import Enum
from pydantic import BaseModel, Field
from typing import Generic, TypeVar
from pydantic.generics import GenericModel
from api.core.Response import Return as Response


class RealTimeGold(BaseModel):
    updataTime: str = Field(..., description='更新时间')
    """更新时间"""
    region: str = Field(..., description='跨区')
    """跨区"""
    goldPrice: float = Field(..., description='金价')
    """金价"""

class DayGold(BaseModel):
    date: str = Field(..., description='日期')
    """日期"""
    avg: float = Field(..., description='峰值')
    """峰值"""
    zero: float = Field(..., description='12时值')
    """12时值"""

class HistoryGold(BaseModel):
    region: str = Field(..., description='跨区')
    """跨区"""
    data: list[DayGold] = Field(..., description='历史数据')
    echartsData : dict = Field(..., description='echarts数据')
    """echarts数据"""