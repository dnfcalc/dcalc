from copy import deepcopy
import re
from typing import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from core.basic.character import Character

characterLv = 120 + 5


class Skill:
    name: str = ''
    """技能名称"""
    _lv: int = 0
    id: int = 0
    """技能ID"""
    icon: str = '$char/$name'
    """技能图标，默认当前职业下该技能名称对应的图标，支持以下模板字符串
    $common 通用图标路径
    $char   当前职业图标路径
    $name   技能名称
    $id     技能ID
    """
    type: Literal['active', 'passive'] = 'active'
    """技能类型 active主动 passive被动"""
    learnLv: int = 0
    """学习等级"""
    masterLv: int = 0
    """精通等级"""
    maxLv: int = 0
    """最大等级"""
    position: int = 0
    """技能树位置"""
    rangeLv: int = 1
    """学习间隔"""
    cube: int = 0
    """无色消耗"""
    skillRation: int = 1
    """技能面板倍率 [改变技能面板]"""
    skillDamage: int = 1
    """技能技攻 [不改变技能面板]"""
    char: 'Character' = None
    """技能所属角色"""
    damage: bool = False
    """是否是伤害技能"""
    cd: float = 0
    """技能冷却时间"""
    cdReduce: float = 1
    """技能冷却缩减"""
    cdRecover: float = 1
    """技能冷却恢复"""
    associate: list = []
    """关联技能
    type: 关联类型 *乘算 +加算 $角色属性 默认'*skillRation'
    e.g.
    *skillRation 乘算技能面板倍率
    *cdReduce 乘算技能冷却缩减
    $*PATK 乘算角色物理攻击
    ~直接走type对应的函数名称 传参为old,new,data,skills
    skills: 关联技能 默认 '*'
    """

    def __init__(self, char):
        self.char = char
        self.id = self._extract_id()
        self.icon = self._generate_icon()
        # self.lv = self._calculate_lv()
        pass

    def _extract_id(self):
        className = self.__class__.__name__
        return int(re.search(r'\d+', className).group()) if re.search(r'\d+', className) else 0

    def _generate_icon(self):
        icon = self.icon or '$char/$name'
        icon = icon.replace('$char', f'/characters/{self.char.name}/skill')
        icon = icon.replace('$common', '/characters/common')
        icon = icon.replace('$name', f'{self.name}')
        icon = icon.replace('$id', f'{self.id}')
        return f'{icon}.png'

    def calculate_lv(self):
        return min(int((characterLv - self.learnLv) / self.rangeLv + 1), self.masterLv) if self._lv == 0 else self._lv

    @property
    def lv(self):
        """技能等级"""
        return self._lv

    @lv.setter
    def lv(self, value):
        value = min(self.maxLv, value)
        if self._lv != value:
            self.effect(self._lv, value)
            self._lv = value

    def effect(self, old: int, new: int):
        for assoc in self.associate:
            type = assoc.get('type', '*skillRation')
            skills = assoc.get('skills', 'all')
            data = assoc.get('data', [0] * self.maxLv)
            if type[0] not in ['*', '+', '$']:
                if self.precondition():
                    getattr(self, type)(old, new, data, skills)
                continue
            if self.precondition():
                self._apply_association(type, old, new, data, skills)

    def precondition(self):
        """effect的前置条件"""
        return True

    def _apply_association(self, type, old, new, data, skills):
        if type.startswith('$*'):
            value = (1 + data[new] / 100) / (1 + data[old] / 100)
            eval(f'self.char.SetStatus({type[2:]}={value})')
        elif type.startswith('$+'):
            value = data[new] / 100 - data[old] / 100
            eval(f'self.char.SetStatus({type[2:]}={value})')
        else:
            if skills == '*':
                skills = self.char.GetSkillNames('all', True)
            for name in skills:
                skill = self.char.GetSkillByName(name)
                if skill is not None:
                    self._update_skill_attribute(skill,type, old, new, data)

    def _update_skill_attribute(self,skill, type, old, new, data):
        if type.startswith('*'):
            setattr(skill, type[1:], getattr(skill, type[1:]) * (1 + data[new] / 100) / (1 + data[old] / 100))
        elif type.startswith('+'):
            setattr(skill, type[1:], getattr(skill, type[1:]) + data[new] / 100 - data[old] / 100)



class ActiveSkill(Skill):
    type: str = 'active'
    """技能类型 active主动 passive被动"""
    damage: bool = True
    """是否是伤害技能"""

    def __init__(self, char):
        super().__init__(char)

    def skillInfo(self, mode: str | None = None):
        basic = self
        if mode is not None:
            basic = deepcopy(self)
            basic.setMode(mode)
        else:
            basic = self
        date = basic.getSkillDate(self.lv)
        cd = basic.getSkillCD()
        return date * self.skillRation , self.skillDamage ,cd

    def setMode(self, mode: str):
        pass

    def getSkillDate(self,lv:int=0):
        res = 0
        for i in range(0,10):
            data = getattr(self, f'data{i}', [])
            if len(data) == 0:
                break
            if lv < len(data):
                hit = getattr(self, f'hit{i}', 1)
                power = getattr(self, f'power{i}', 1)
                res += hit * power * data[lv]
        return res

    def getSkillCD(self):
        return self.cd * self.cdReduce / self.cdRecover

class PassiveSkill(Skill):
    type: str = 'passive'
    """技能类型 active主动 passive被动"""
    damage: bool = False
    """是否是伤害技能"""
