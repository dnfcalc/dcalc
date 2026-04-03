from collections.abc import Mapping
from typing import Any, Literal

from core.abstract.character import CharacterProperty
from core.basic.skill import Skill
from core.basic.equipment import EquEffect
from ..formula import 获取基础属性, 获取唤醒属性
from ..roleinfo import CharacterEquipInfo, get_key_by_value, CharacterOathInfo
from .jade import Jade


class CharacterBase(CharacterProperty):
    # region 额外类属性（CharacterProperty 中未声明的）

    BindAwake: int
    """绑定觉醒等级"""
    skills: list['Skill'] = []
    skills_dict: dict[str, 'Skill'] = {}
    equVersion: str = '0'
    """装备版本"""
    charEquipInfo: dict[str, 'CharacterEquipInfo']
    """装备打造信息"""
    charOathInfo: list['CharacterOathInfo']
    """誓约打造信息"""
    equ_effect: list['EquEffect'] = []
    """装备效果列表"""
    equ_options: dict[str, int] = {}
    """装备选项列表"""
    EquEffectRatio = 1.0
    """装备效果倍率"""
    max_point = 0
    """套装效果点数"""
    buffer: bool = False

    # region 职业属性
    实际名称: str = ''
    名称: str = ''
    角色: str = ''
    角色类型: str = ''
    职业: str = ''
    武器选项: list[str] = []
    副武器选项: list[str] = []
    输出类型选项: list[str] = []
    防具精通属性: list[str] = []
    输出类型: str = '物理百分比'
    # endregion

    # endregion

    # region 跨 Mixin 方法前向声明（供静态类型检查使用，由对应 Mixin 实现）

    def load_skills(self) -> None:
        """加载技能（由 CalcEquipMixin 实现）"""

    def calc_carry_skills(self, DSB: bool, BUFF: bool) -> list:
        """计算输出技能（由 CalcCarryMixin 实现）"""
        return []

    def get_carry_info(self) -> list:
        """获取输出信息（由 CalcCarryMixin 实现）"""
        return []

    def calc_buffer_skills(self) -> list:
        """计算辅助技能（由 CalcBufferMixin 实现）"""
        return []

    def get_buffer_info(self) -> list:
        """获取辅助信息（由 CalcBufferMixin 实现）"""
        return []

    # endregion

    def __init__(self, equVersion, moduleName) -> None:
        self.equVersion = equVersion
        self.moduleName = moduleName
        # 工会四维
        self.STR = 0 + 120
        self.INT = 0 + 120
        self.Spirit = 0 + 120
        self.Vitality = 0 + 120
        # 唤醒的情况下的基础数据
        self.AtkP = 0 + 65
        self.AtkM = 0 + 65
        self.AtkI = 1116 + 65
        self.PAtkP = 1.0
        self.PAtkM = 1.0
        self.PAtkI = 1.0
        self.ElementA = {
            '火': False,
            '冰': False,
            '光': False,
            '暗': False,
        }
        self.ElementDB = {
            '火': 13,
            '冰': 13,
            '光': 13,
            '暗': 13,
        }
        self.ElementR = {
            '火': 0,
            '冰': 0,
            '光': 0,
            '暗': 0,
        }
        self.Abnormal = {
            '出血': False,
            '灼伤': False,
            '感电': False,
            '中毒': False,
        }
        self.CriticalM = 0
        self.CriticalP = 0
        self.SkillAttack = 1
        self.SpeedA = 0
        self.SpeedM = 0
        self.SpeedR = 0
        self.HitP = 0
        self.Hit = 0
        self.MonsterInfo = {
            'DefenseP': 0,
            'DefenseM': 0,
            '火抗': 0,
            '冰抗': 0,
            '光抗': 0,
            '暗抗': 0,
        }
        self.Buffer = 0
        self.BufferP = 1.0
        self.Attack = 0
        self.AttackP = 1.0
        self.ElementIncrease = 1.0
        self.equs = {}
        self.jade_effect = Jade()
        self.equ_effect = []
        self.equ_options = {}
        self.max_point = 0
        self.skills = []
        self.skills_dict = {}
        self.load_skills()

    # region 角色属性设置

    def SetBaseStatus(self) -> None:
        """设角色基础属性"""
        temp = 获取基础属性(self.角色, self.职业)
        唤醒 = 获取唤醒属性()
        for index, i in enumerate([get_key_by_value(i) for i in ['力量', '体力', '智力', '精神']]):
            setattr(self, i, getattr(self, i) + temp[index] + 唤醒)

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
        全属抗=0,
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
        **kwargs: Mapping[
            Literal[
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
                '火强',
                '冰强',
                '光强',
                '暗强',
                '火属性抗性',
                '冰属性抗性',
                '光属性抗性',
                '暗属性抗性',
                '火属性攻击',
                '冰属性攻击',
                '光属性攻击',
                '暗属性攻击',
            ],
            Any,
        ],
    ) -> None:
        """设置角色属性"""
        self.STR += 力量 + kwargs.get('STR', 0) + 四维 + 力智
        self.INT += 智力 + kwargs.get('INT', 0) + 四维 + 力智
        self.Spirit += 精神 + kwargs.get('Spirit', 0) + 四维 + 体精
        self.Vitality += 体力 + kwargs.get('Vitality', 0) + 四维 + 体精
        self.AtkP += 物攻 + kwargs.get('AtkP', 0) + 三攻
        self.AtkM += 魔攻 + kwargs.get('AtkM', 0) + 三攻
        self.AtkI += 独立 + kwargs.get('AtkI', 0) + 三攻
        self.PAtkP *= kwargs.get('PAtkP', 1.0)
        self.PAtkM *= kwargs.get('PAtkM', 1.0)
        self.PAtkI *= kwargs.get('PAtkI', 1.0)
        for elem in ['火', '冰', '光', '暗']:
            self.ElementA[elem] = kwargs.get(f'{elem}属性攻击', False) or kwargs.get('ElementA', {}).get(elem, False) or self.ElementA[elem]
            self.ElementDB[elem] += kwargs.get(f'{elem}强', 0) + kwargs.get('ElementDB', {}).get(elem, 0) + 全属强
            self.ElementR[elem] += kwargs.get(f'{elem}抗', 0) + kwargs.get('ElementR', {}).get(elem, 0) + 全属抗
        self.CriticalM += kwargs.get('CriticalM', 0) + 魔暴
        self.CriticalP += kwargs.get('CriticalP', 0) + 物暴
        self.SkillAttack *= (1 + 技攻) * (1 + kwargs.get('SkillAttack', 0))
        self.SpeedA += 攻击速度 + kwargs.get('SpeedA', 0) + 三速
        self.SpeedM += 移动速度 + kwargs.get('SpeedM', 0) + 三速
        self.SpeedR += 施放速度 + kwargs.get('SpeedR', 0) + 三速
        self.HitP += 命中率 + kwargs.get('HitP', 0)
        self.Hit += 命中 + kwargs.get('Hit', 0)
        self.Attack += 攻击强化 + kwargs.get('Attack', 0)
        self.AttackP += 攻击强化P + kwargs.get('AttackP', 0.0)
        self.Buffer += 增益量 + kwargs.get('Buffer', 0)
        self.BufferP += 增益量P + kwargs.get('BufferP', 0)
        self.EquEffectRatio += kwargs.get('EquEffectRatio', 0.0)

    def AddElementDB(self, element: str, value: float, type: int = 0) -> None:
        """
        增加属性强化
        type: 0 站街 1 进图
        """
        if element not in self.ElementDB:
            raise ValueError(f'Invalid element: {element}')
        if type == 0:
            value = value * (1 + self.jade_effect.ElementIncrease)
        if type == 1:
            value = int(value * (1 + self.jade_effect.ElementIncrease))
        self.ElementDB[element] += value

    def AddSkillLv(self, min: int, max: int, lv: int, type=-1, exceptSkills: list[str] = []) -> None:
        """
        增加技能等级
        type: -1 全部, 0 被动, 1 主动
        """
        skillType = 'all' if type == -1 else ('active' if type == 1 else 'passive')
        for skill in self.skills:
            if min <= skill.learnLv <= max:
                if (skillType == 'all' or skill.type == skillType) and skill.lv > 0 and skill.name not in exceptSkills:
                    skill.lv += lv

    def SetSkillCD(self, min=1, max=100, cd=0, exclude=[50, 85, 100]) -> None:
        """设置技能CD"""
        for skill in self.skills:
            if min <= skill.learnLv <= max and (skill.type == 'active' or skill.damage) and skill.learnLv not in exclude:
                skill.cdReduce *= 1 - cd

    def SetSkillCDRecover(self, min=1, max=100, cd=0, exclude=[50, 85, 100]) -> None:
        """设置技能CD恢复"""
        for skill in self.skills:
            if min <= skill.learnLv <= max and (skill.type == 'active' or skill.damage) and skill.learnLv not in exclude:
                skill.cdRecover += cd

    def SetSkillRation(self, min=1, max=100, ratio=1, type=-1) -> None:
        """设置技能倍率
        0 修改技能面板 1 不修改技能面板
        type: -1 全部, 0 被动, 1 主动
        """
        for skill in self.skills:
            if min <= skill.learnLv <= max and skill.damage and skill.type == 'active':
                if type == 0:
                    skill.skillRation *= 1 + ratio
                else:
                    skill.skillDamage *= 1 + ratio

    # endregion

    # region 技能查询

    def GetSkillByName(self, name) -> 'Skill':
        """通过技能名获取技能"""
        return self.skills_dict.get(name, None)

    def GetSkillByID(self, id: str) -> 'Skill':
        """通过技能ID获取技能"""
        skill = list(filter(lambda x: str(x.id) == id, self.skills))
        return skill[0] if len(skill) > 0 else None

    def GetSkillByUUID(self, uuid: str) -> 'Skill':
        """通过技能UUID获取技能"""
        skill = list(filter(lambda x: str(x.uuid) == uuid, self.skills))
        return skill[0] if len(skill) > 0 else None

    def GetSkillNames(self, type: Literal['active', 'passive', 'all'] = 'all', damage: Literal[True, False, 'all'] = 'all') -> list[str]:
        """获取技能名字"""
        return [skill.name for skill in self.skills if (type == 'all' or skill.type == type) and (damage == 'all' or skill.damage == damage)]

    def GetWeaponType(self) -> tuple[str, str]:
        """获取武器类型"""
        weapon = self.charEquipInfo['武器'].equInfo
        if weapon is None:
            return None, None
        else:
            return weapon.itemDetailType, weapon.categorize

    # endregion
