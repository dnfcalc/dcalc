from copy import deepcopy
from functools import cache
import json
import re
from typing import Literal, TYPE_CHECKING
from .formula import 武器冷却惩罚
from database.connect import get_redis
from api.core.Redis import get_redis_info

if TYPE_CHECKING:
    from core.basic.character import Character

characterLv = 115 + 5


@cache
def get_data(prefix: str, key: int | str, func = lambda x: x):
    redis = next(get_redis())
    def get_skill_info():
        # This function should retrieve the skill info based on job and jobGrow
        # For now, we return a placeholder dictionary
        with open(f'./openapi/data/{prefix}.json', encoding='utf-8') as f:
            skill_data = json.load(f)
        try:
            if isinstance(key, int):
                data = [0] + list(map(lambda x: x["optionValue"].get("value" + str(key+1), 0), skill_data["levelInfo"]["rows"]))
                data = [0 if x is None or x == "-" else x for x in data]
            elif key == "vps":
                data = [ {"name":x["name"],"desc":x["desc"]} for x in skill_data.get("evolution",[])]
        except Exception as e:
            print(f"get skill {prefix}/{key} data error",e)
            data = None
        return data

    data = get_redis_info(redis, f'dcalc:skill:{prefix}:{key}', get_skill_info, without_gzip=True)
    return func(data)


class Skill:
    name: str = ''
    """技能名称"""
    _lv: int = 0
    id: int = 0
    """技能ID"""
    icon: str = '$char/$uuid'
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
    line: int = None
    """技能行"""
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
    cdCut: float = 0
    """技能冷却时间直接减少"""
    cdReduce: float = 1
    """技能冷却缩减"""
    cdRatio: float = 1
    """技能冷却倍率,直接体现在面板上,不被上限影响"""
    cdRecover: float = 1
    """技能冷却恢复"""
    associate: list = []
    """关联技能
    type: 关联类型 *乘算 +加算 =直接赋值 $角色属性 默认'*skillRation'
    e.g.
    *skillRation 乘算技能面板倍率
    *cdReduce 乘算技能冷却缩减
    $*PATK 乘算角色物理攻击
    ~直接走type对应的函数名称 传参为old,new,data,skills,exceptSkills
    skills: 关联技能 默认 '*'
    exceptSkills: 例外技能 默认[]
    """
    mode: list[str] = ['']
    currentMode: str = ''
    """技能模式"""
    buffer: bool = False
    """是否是增益技能"""
    bind: bool = None
    uuid: str = None
    hasVP: bool = None
    """是否有VP形态"""
    hasUP: bool = None
    """是否有技能强化"""
    upType: Literal['damage', 'buff', 'heal'] = 'damage'
    vps: list = []

    def __init__(self, char):
        self.char = char
        self.id = self._extract_id()
        self.icon = self._generate_icon()
        if self.line is None:
            self.line = self.learnLv
        if self.bind is None:
            self.bind = False
            if self.learnLv in [50, 85, 100]:
                self.bind = True
        if self.hasVP is None:
            if self.learnLv not in [50, 85, 100] and self.learnLv >= 35 and self.learnLv <= 80 and self.damage:
                self.hasVP = True
            else:
                self.hasVP = False
        if self.hasUP is None:
            if self.learnLv not in [50, 85, 100] and self.learnLv >= 15 and self.learnLv <= 80 and self.damage:
                self.hasUP = True
            else:
                self.hasUP = False
        # self.lv = self._calculate_lv()
        pass

    def _extract_id(self):
        className = self.__class__.__name__
        return int(re.search(r'\d+', className).group()) if re.search(r'\d+', className) else 0

    def _generate_icon(self):
        icon = self.icon or '$char/$uuid'
        icon = icon.replace('$char', f'/characters/{self.char.role}/{self.char.name}/skill')
        icon = icon.replace('$common', '/characters/common')
        icon = icon.replace('$name', f'{self.name}')
        icon = icon.replace('$uuid', f'{self.uuid}')
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
        value = int(min(self.maxLv, value))
        if self._lv != value:
            self.effect(self._lv, value)
            self._lv = value

    def effect(self, old: int, new: int):
        for assoc in self.associate:
            type = assoc.get('type', '*skillRation')
            skills = assoc.get('skills', '*')
            data = assoc.get('data', [0] * self.maxLv)
            ratio = assoc.get('ratio', 100)
            weapon = assoc.get('weapon', self.char.武器选项)
            exceptSkills = assoc.get('exceptSkills', [])
            if type[0] not in ['*', '+', '=', '$']:
                if self.precondition() and (self.char.GetWeaponType()[0] in weapon or len(weapon) == len(self.char.武器选项)):
                    getattr(self, type)(old, new, data, skills, exceptSkills, ratio, weapon)
                continue
            if self.precondition():
                self.apply_association(type, old, new, data, skills, exceptSkills, ratio, weapon)

    def precondition(self):
        """effect的前置条件"""
        return True

    def apply_association(self, type, old, new, data, skills, exceptSkills, ratio=100, weapon=[]):
        try:
            if (self.char.GetWeaponType()[0] not in weapon) and not (self.char.GetWeaponType()[0] is None and len(weapon) == len(self.char.武器选项)):
                return
            if type.startswith('$*'):
                if 'cdReduce' in type:
                    value = (1 - data[new] / ratio) / (1 - data[old] / ratio)
                else:
                    value = (1 + data[new] / ratio) / (1 + data[old] / ratio)
                eval(f'self.char.SetStatus({type[2:]}={value})')
            elif type.startswith('$+'):
                value = data[new] / ratio - data[old] / ratio
                eval(f'self.char.SetStatus({type[2:]}={value})')
            else:
                if skills == '*':
                    skills = self.char.GetSkillNames('all', True)
                for name in skills:
                    if name in exceptSkills:
                        continue
                    skill = self.char.GetSkillByName(name)
                    if skill is not None:
                        self.update_skill_attribute(skill, type, old, new, data, ratio, weapon)
        except Exception as e:
            print(f"Error applying association {type} for skill {self.name}: {e}")
            raise e

    def update_skill_attribute(self, skill, type, old, new, data, ratio=100, weapon=[]):
        if (self.char.GetWeaponType()[0] not in weapon) and not (self.char.GetWeaponType()[0] is None and len(weapon) == len(self.char.武器选项)):
            return
        if type.startswith('*'):
            if 'cdReduce' in type or type == 'cd' or 'cdRatio' in type:
                setattr(skill, type[1:], getattr(skill, type[1:]) * (1 - data[new] / ratio) / (1 - data[old] / ratio))
            else:
                setattr(skill, type[1:], getattr(skill, type[1:]) * (1 + data[new] / ratio) / (1 + data[old] / ratio))
        elif type.startswith('+'):
            if type[1:] == 'lv' and self.char.setInfo.get('skills', {}).get(str(skill.id),{}).get('lv',0) == 0:
                return
            else:
                setattr(skill, type[1:], getattr(skill, type[1:]) + data[new] / ratio - data[old] / ratio)
        elif type.startswith('='):
            setattr(skill, type[1:], data[new])

    def skillInfo(self, mode: str | None = None):
        pass


class ActiveSkill(Skill):
    type: str = 'active'
    """技能类型 active主动 passive被动"""
    damage: bool = True
    """是否是伤害技能"""
    buffer: bool = False
    """是否是buff技能"""
    vp: int = 0
    """技能VP形态"""
    up: int = 0
    """技能强化"""

    def __init__(self, char):
        super().__init__(char)
        keys = [key.replace('data', '') for key in dir(self) if key.startswith('data') and not key.startswith('plus')]
        for i in keys:
            power = getattr(self, f'power{i}', None)
            if power is None:
                setattr(self, f'power{i}', 1)
            hit = getattr(self, f'hit{i}', None)
            if hit is None:
                setattr(self, f'hit{i}', 0)

    def skillInfo(self, mode: str | None = None):
        basic = deepcopy(self)
        basic.setUP()
        if mode is not None:
            basic.currentMode = mode
            basic.setMode(mode)
        basic.setVP()
        date = basic.getSkillData(self.lv)
        cd = basic.getSkillCD(mode)
        return date * basic.skillRation, basic.skillDamage, cd

    def setMode(self, mode: str):
        pass

    def setVP(self):
        if self.vp == 1:
            self.vp_1()
        elif self.vp == 2:
            self.vp_2()

    def setUP(self):
        if not self.hasUP:
            return
        if self.up == 1:
            if self.learnLv < 35:
                self.skillRation *= 1.6
            else:
                self.skillRation *= 1.55
        elif self.up == 2:
            self.cdReduce *= 1 - 0.15
            if self.learnLv < 35:
                self.skillRation *= 1.43
            else:
                self.skillRation *= 1.38

    def getSkillData(self, lv: int = 0):
        res = 0
        keys = [key.replace('data', '') for key in dir(self) if key.startswith('data') and not key.startswith('dataplus')]
        for i in keys:
            data = getattr(self, f'data{i}', [])
            plus = getattr(self, f'plus{i}', 0)
            hit = getattr(self, f'hit{i}', 0)
            if len(data) == 0 or hit == 0:
                continue
            if lv < len(data):
                hit = getattr(self, f'hit{i}', 0)
                power = getattr(self, f'power{i}', 1)
                res += hit * power * (data[lv] + plus)
        keys = [key.replace('dataplus', '') for key in dir(self) if key.startswith('dataplus')]
        for i in keys:
            data = getattr(self, f'dataplus{i}', 0)
            hit = getattr(self, f'hitplus{i}', 1)
            power = getattr(self, f'powerplus{i}', 1)
            res += hit * power * data
        return res

    def getWeaponCDRatio(self):
        weapon = self.char.charEquipInfo['武器'].equInfo
        if weapon is None or '传世武器' in weapon.categorize:
            return 1
        else:
            return 武器冷却惩罚(weapon.itemDetailType, self.char.输出类型)

    def getQuickCDRatio(self):
        return 1.0
        cdr = 0
        if 15 <= self.learnLv <= 30:
            cdr = 0.01
        elif 35 <= self.learnLv <= 70:
            cdr = 0.02
        elif 75 <= self.learnLv <= 100:
            cdr = 0.05
        if self.learnLv in [50, 85, 100]:
            cdr = 0.05
        return 1 - cdr

    def getSkillCD(self, mode=None):
        return max(0, round(max(self.cd * 0.3, self.cd * self.cdReduce / self.cdRecover * self.getWeaponCDRatio() * self.getQuickCDRatio()) * self.cdRatio - self.cdCut, 2))

    def vp_1(self):
        pass

    def vp_2(self):
        pass


class PassiveSkill(Skill):
    type: str = 'passive'
    """技能类型 active主动 passive被动"""
    damage: bool = False
    """是否是伤害技能"""
    buffer: bool = False
    """是否是buff技能"""


class BuffSkill(Skill):
    buffer: bool = True
    """是否是增益技能"""
    damage: bool = False
    """是否是伤害技能"""
    buffType = 'normal'
    """增益类型 normal普通 buff 主BUFF awake 觉醒技能"""

    INT: list[float] = []
    """智力"""
    STR: list[float] = []
    """力量"""
    Spirit: list[float] = []
    """精神"""
    Vitality: list[float] = []
    """体力"""
    """主要属性"""

    ATK: list[float] = []
    """三攻加成"""
    ATKRatio: float = 1
    """三攻*算倍率"""
    ATKPLUS: float = 0
    """三攻加算加成"""

    STRINT: list[float] = []
    """力量智力加成"""
    STRINTRatio: float = 1
    """力量智力*算倍率"""
    STRINTPLUS: float = 0
    """力量智力加算加成"""

    CarryRatio: list[float] = []
    """对C的额外增伤倍率"""
    vp: int = 0
    """技能VP形态"""
    up: int = 0
    """技能强化"""

    def __init__(self, char):
        super().__init__(char)
        keys = [key.replace('data', '') for key in dir(self) if key.startswith('data') and not key.startswith('plus')]
        for i in keys:
            power = getattr(self, f'power{i}', None)
            if power is None:
                setattr(self, f'power{i}', 1)
            hit = getattr(self, f'hit{i}', None)
            if hit is None:
                setattr(self, f'hit{i}', 0)

    def getSkillCD(self, mode=None):
        return '-'

    def skillInfo(self, mode: str | None = None):
        """
        Returns:
            tuple: (奶自己的面板加成,[三攻,三攻倍率,三攻额外加成],[力智,力智倍率,力智额外加成],对C增伤倍率,cd)
        """
        lv = self.lv
        value = 0
        value1 = 0 if lv > len(self.ATK) else self.ATK[lv]
        value2 = 0 if lv > len(self.STRINT) else self.STRINT[lv]
        value3 = 0 if lv > len(self.CarryRatio) else self.CarryRatio[lv]
        self.setUP()
        self.setVP()
        if self.char.适用属性 == '智力':
            value = 0 if lv > len(self.INT) else self.INT[lv]
        elif self.char.适用属性 == '力量':
            value = 0 if lv > len(self.STR) else self.STR[lv]
        elif self.char.适用属性 == '体力':
            value = 0 if lv > len(self.Vitality) else self.Vitality[lv]
        elif self.char.适用属性 == '精神':
            value = 0 if lv > len(self.Spirit) else self.Spirit[lv]
        return value, [value1, self.ATKRatio, self.ATKPLUS], [value2, self.STRINTRatio, self.STRINTPLUS], value3, self.getSkillCD(mode)

    def setVP(self):
        if self.vp == 1:
            self.vp_1()
        elif self.vp == 2:
            self.vp_2()

    def setUP(self):
        if not self.hasUP:
            return
        if self.up == 1:
            ...
        elif self.up == 2:
            if self.upType == 'damage':
                self.cdReduce *= 1 - 0.15
            elif self.upType == 'heal':
                self.cdReduce *= 1 - 0.1

    def vp_1(self):
        pass

    def vp_2(self):
        pass


class PassiveBufferSkill(BuffSkill):
    type: str = 'passive'


class ActiveBufferSkill(BuffSkill):
    type: str = 'active'

    def getWeaponCDRatio(self):
        weapon = self.char.charEquipInfo['武器'].equInfo
        if weapon is None or '传世武器' in weapon.categorize:
            return 1
        else:
            return 武器冷却惩罚(weapon.itemDetailType, self.char.输出类型)

    def getQuickCDRatio(self):
        return 1.0
        cdr = 0
        if 15 <= self.learnLv <= 30:
            cdr = 0.01
        elif 35 <= self.learnLv <= 70:
            cdr = 0.02
        elif 75 <= self.learnLv <= 100:
            cdr = 0.05
        if self.learnLv in [50, 85, 100]:
            cdr = 0.05
        return 1 - cdr

    def getSkillCD(self, mode=None):
        return max(0, round(max(self.cd * 0.3, self.cd * self.cdReduce / self.cdRecover * self.getWeaponCDRatio() * self.getQuickCDRatio(), 1) - self.cdCut, 2))
