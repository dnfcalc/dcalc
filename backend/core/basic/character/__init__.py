"""
core.basic.character 包
- jade.py         : Jade（辟邪玉）数据类
- base.py         : CharacterBase — 属性声明、__init__、基础状态设置、技能操作
- calc_equip.py   : CalcEquipMixin — 套装/装备/时装/基础强化/辟邪玉/杂项计算 + calc 主入口
- calc_carry.py   : CalcCarryMixin — 输出角色伤害系数与技能伤害计算
- calc_buffer.py  : CalcBufferMixin — 辅助角色 Buff 技能计算
- info.py         : CharacterInfoMixin — 前端展示信息查询
"""

import importlib

from .jade import Jade
from .calc_equip import CalcEquipMixin
from .calc_carry import CalcCarryMixin
from .calc_buffer import CalcBufferMixin
from .info import CharacterInfoMixin


class Character(CalcEquipMixin, CalcCarryMixin, CalcBufferMixin, CharacterInfoMixin):
    """
    角色类，通过多重继承组合各模块能力。

    MRO（方法解析顺序）:
      Character → CalcEquipMixin → CalcCarryMixin → CalcBufferMixin
               → CharacterInfoMixin → CharacterBase → CharacterProperty
    """


def createCharacter(alter: str, equVersion: str = '0') -> 'Character':
    character: Character = None
    module_name = 'core.character.' + alter
    if equVersion is None or equVersion == '':
        equVersion = '0'
    try:
        character = importlib.import_module(module_name).classChange(equVersion)
    except Exception as ex:
        print(ex)
        print('create character ' + module_name + ' error.')
    return character


__all__ = ['Character', 'Jade', 'createCharacter']
