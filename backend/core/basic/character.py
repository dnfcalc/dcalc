from functools import cache
import importlib
from typing import Literal

from core.basic.property import CharacterInfo
from core.basic.skill import Skill

from core.basic.equipment import get_equipment
# from core.basic.equipment import equipments
# from core.basic.skill import Skill, ActiveSkill, PassiveSkill
from .formula import 获取基础属性
from .roleinfo import CharacterEquipInfo, get_key_by_value
# from .property import 精通计算, 角色基础, CharacterInfo


class Character:
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

    Buffer: float
    """增益量"""

    BufferP: float
    """增益量%"""

    Attack: float
    """攻击强化"""

    AttackP: float
    """攻击强化%"""

    # endregion

    skills: list["Skill"] = []
    # """技能列表"""
    skills_dict: dict[str, "Skill"] = {}
    # """技能名字对应技能"""
    equVersion: str = '0'
    """装备版本"""
    charEquipInfo: dict[str, "CharacterEquipInfo"]
    """装备打造信息"""

    # region 角色属性
    输出类型: str = '物理'

    buffer: bool = False
    # endregion

    # region 职业属性
    实际名称: str = ''
    名称: str = ''
    角色: str = ''
    角色类型: str = ''
    职业: str = ''
    武器选项: list[str] = []
    输出类型选项: list[str] = []
    防具精通属性: list[str] = []
    类型 = ''

    输出类型: str = '物理'

    # endregion

    def __init__(self, equVersion) -> None:
        self.equVersion = equVersion
        # self.equs = get_equ(self.equVersion)
        self.STR = 0
        self.INT = 0
        self.AtkP = 0
        self.AtkM = 0
        self.AtkI = 0
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
            '火': 0,
            '冰': 0,
            '光': 0,
            '暗': 0,
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
        pass

    # region 角色属性设置
    def SetBaseStatus(self) -> None:
        """设角色基础属性"""
        # 角色四维
        temp = 获取基础属性(self.角色, self.职业)
        for index, i in enumerate([get_key_by_value(i) for i in ['力量', '体力', '智力', '精神']]):
            setattr(self, i, temp[index])
        # 角色属性抗性
        pass
        # 角色异常抗性
        pass

    def SetStatus(
        self,
        力量=0,
        智力=0,
        物攻=0,
        魔攻=0,
        独立=0,
        技攻=0,
        全属强=0,
        火强=0,
        冰强=0,
        光强=0,
        暗强=0,
        全属抗=0,
        火抗=0,
        冰抗=0,
        光抗=0,
        暗抗=0,
        火属性攻击=False,
        冰属性攻击=False,
        光属性攻击=False,
        暗属性攻击=False,
        移速=0,
        攻速=0,
        施放=0,
        命中=0,
        命中率=0,
        物暴=0,
        魔暴=0,
        攻击强化=0,
        攻击强化P=0,
        增益量=0,
        增益量P=0,
        **kwargs,
    ) -> None:
        """设置角色属性"""
        allowed_kwargs = {
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
        }
        for key in kwargs:
            if key not in allowed_kwargs:
                raise ValueError(f'Invalid keyword argument: {key}')
        self.STR += 力量 + kwargs.get('STR', 0)
        self.INT += 智力 + kwargs.get('INT', 0)
        self.AtkP += 物攻 + kwargs.get('AtkP', 0)
        self.AtkM += 魔攻 + kwargs.get('AtkM', 0)
        self.AtkI += 独立 + kwargs.get('AtkI', 0)
        self.PAtkP *= kwargs.get('PAtkP', 0)
        self.PAtkM *= kwargs.get('PAtkM', 0)
        self.PAtkI *= kwargs.get('PAtkI', 0)
        for elem in ['火', '冰', '光', '暗']:
            self.ElementA[elem] = kwargs.get(f'{elem}属性攻击', False) or kwargs.get('ElementA', {}).get(elem, False) or self.ElementA[elem]
            self.ElementDB[elem] += kwargs.get(f'{elem}强', 0) + kwargs.get('ElementDB', {}).get(elem, 0) + kwargs.get('全属强', 0)
            self.ElementR[elem] += kwargs.get(f'{elem}抗', 0) + kwargs.get('ElementR', {}).get(elem, 0) + kwargs.get('全属抗', 0)
        self.CriticalM += kwargs.get('CriticalM', 0) + 魔暴
        self.CriticalP += kwargs.get('CriticalP', 0) + 物暴
        self.SkillAttack += (1 + 技攻) * (1 + kwargs.get('SkillAttack', 0))
        self.SpeedA += 攻速 + kwargs.get('SpeedA', 0)
        self.SpeedM += 移速 + kwargs.get('SpeedM', 0)
        self.SpeedR += 施放 + kwargs.get('SpeedR', 0)
        self.HitP += 命中率 + kwargs.get('HitP', 0)
        self.Hit += 命中 + kwargs.get('Hit', 0)
        self.Attack += 攻击强化 + kwargs.get('Attack', 0)
        self.AttackP += 攻击强化P + kwargs.get('AttackP', 0)
        self.Buffer += 增益量 + kwargs.get('Buffer', 0)
        self.BufferP += 增益量P + kwargs.get('BufferP', 0)
        pass

    def AddSkillLv(self, min, max, lv, type=-1) -> None:
        """
        增加技能等级
        type: -1 全部, 0 被动, 1 主动
        """
        for skill in self.skills:
            if min <= skill.requiredLv <= max:
                if type == -1 or skill.type == type:
                    skill.AddLv(lv, self)

    def SetSkillCD(self, min=1, max=99, cd=0) -> None:
        """
        设置技能CD
        type: -1 全部, 0 被动, 1 主动
        """
        for skill in self.skills:
            if min <= skill.requiredLv <= max and skill.damage:
                skill.CDR *= 1 - cd

    def GetSkillByName(self, name) -> Skill:
        """通过技能名获取技能"""
        return self.skills_dict.get(name,None)

    def GetSkillByID(self,id:str) -> Skill:
        skill = list(filter(lambda x:str(x.id) == id,self.skills))
        """通过技能ID获取技能"""
        return skill[0] if len(skill) > 0 else None

    @cache
    def GetSkillNames(self, type: Literal['active', 'passive', 'all'] = 'all' , damage:Literal[True,False,'all'] = 'all') -> list[str]:
        """获取技能名字"""
        return [skill.name for skill in self.skills if (type == 'all' or skill.type == type) and (damage == 'all' or skill.damage == damage)]

    # endregion

    # region 计算相关
    def SetDetail(self, info: dict[str, dict]) -> None:
        self.charEquipInfo = {}
        """打造信息导入"""
        for key in info['equips']:
            # 导入部位打造信息、装备信息、贴膜信息
            self.charEquipInfo[key] = CharacterEquipInfo(info['equips'][key], self.equVersion, key)

    # def calc(self):
    #     """计算角色属性"""
    #     func = []
    #     for i in self.charEquipInfo:
    #         # 计算装备
    #         temp = self.equs.get_func_by_id(self.charEquipInfo[i].id)
    #         func.append(temp)
    #         temp(self)
    #     pass

    def getInfo(self):
        """返回到前端信息"""
        info = {}
        info['alter'] = self.实际名称
        info['equVersion'] = self.equVersion
        info['name'] = self.名称
        info['weaopns'] = self.武器选项
        skillInfo = []
        for skill in self.skills:
            skillInfo.append(
                {
                    'name': skill.name,
                    'icon': skill.icon,
                    'type': skill.type,
                    # 'SPCost': skill.SPCost,
                    "learnLv": skill.learnLv,
                    "masterLv": skill.masterLv,
                    "maxLv": skill.maxLv,
                    # 'TPCost': 0 if not skill.hasTP else skill.TPCost,
                    # "masterTPLv":0 if not skill.hasTP else  skill.masterTPLv,
                    # 'maxTPLv': 0 if not skill.hasTP else skill.TPLearnMax,
                    'positon':skill.position
                }
            )
        info['skills'] = skillInfo
        equs = []
        suits = []
        for i in get_equipment(self.equVersion).equs:
            equs.append(i.__dict__)
        for i in get_equipment(self.equVersion).suits:
            suits.append(i.__dict__)
        info['equips'] = equs
        info['suits'] = suits
        enchats = []
        emblems = []
        # 装备过滤
        # for i in self.equs.info:
        #     if (i.typeSon1Id == '武器' and i.typeSon2Id not in self.武器选项) or (i.name.startswith('精 · ') and self.异界 not in i.name):
        #         pass
        #     else:
        #         equs.append(
        #             {
        #                 'id': i.id,
        #                 'name': i.name,
        #                 'icon': i.icon,
        #                 'typeSon1Id': i.typeSon1Id,
        #                 'typeSon2Id': i.typeSon2Id,
        #                 'typeSon3Id': i.typeSon3Id,
        #                 'rarity': i.rarity,
        #                 'lv': i.lv,
        #                 'suit': i.suit,
        #             }
        #         )
        # 附魔、徽章
        # for i in self.equs.prop:
        #     if i.typeSon1Id == '附魔':
        #         enchats.append(
        #             {
        #                 'id': i.id,
        #                 'name': i.name,
        #                 'icon': i.icon,
        #                 'typeSon1Id': i.typeSon1Id,
        #                 'typeSon2Id': i.typeSon2Id,
        #                 'typeSon3Id': i.typeSon3Id,
        #                 'rarity': i.rarity,
        #                 'lv': i.lv,
        #                 'desc': i.desc,
        #             }
        #         )
        #     if i.typeSon1Id == '徽章':
        #         emblems.append(
        #             {
        #                 'id': i.id,
        #                 'name': i.name,
        #                 'icon': i.icon,
        #                 'typeSon1Id': i.typeSon1Id,
        #                 'typeSon2Id': i.typeSon2Id,
        #                 'typeSon3Id': i.typeSon3Id,
        #                 'rarity': i.rarity,
        #                 'lv': i.lv,
        #                 'desc': i.desc,
        #             }
        #         )
        # info['enchats'] = enchats
        # info['emblems'] = emblems
        # info['seal'] = [i.__dict__ for i in self.equs.seal]
        return info

    def getBasicInos(self):
        res = []
        attrs = []
        if self.输出类型 == '物理':
            attrs = ['STR', 'PSTR', 'AtkP', 'PAtkP', 'CriticalPP', 'CriticalP']
        if self.输出类型 == '魔法':
            attrs = ['INT', 'PINT', 'AtkM', 'PAtkM', 'CriticalMP', 'CriticalM']
        for attr in attrs + ['PDamage', 'PDamageC', 'PDamageB', 'SpeedA', 'SpeedM', 'SpeedR']:
            temp = getattr(CharacterInfo, attr)
            res.append(
                {
                    'name': temp.name,
                    'value': temp.value(getattr(self, attr)),
                    'icon': temp.icon,
                }
            )
        keys = ['火', '冰', '光', '暗']
        for index in range(0, 4):
            temp = getattr(CharacterInfo, f'ElementDB{index}')
            res.append(
                {
                    'name': temp.name,
                    'value': temp.value(getattr(self, 'ElementDB')[keys[index]]),
                    'icon': temp.icon,
                }
            )
            temp = getattr(CharacterInfo, f'ElementR{index}')
            res.append(
                {
                    'name': temp.name,
                    'value': temp.value(getattr(self, 'ElementR')[keys[index]]),
                    'icon': temp.icon,
                }
            )
        return res

    def calc_init(self, setInfo: dict[str, dict]):
        # 打造信息导入
        self.SetDetail(setInfo)
        # 技能等级设置
        self.SetSkills(setInfo.get('skills', {}))
        pass

    def SetSkills(self, skills: dict[str, dict]):
        """设置技能等级"""
        for key in skills:
            skill = self.GetSkillByID(key)
            if skill is not None:
                skill.lv = skills[key].get('lv', 0)
        pass

    def load_skills(self):
        pass

    def calc(self, setInfo: dict[str, dict]):
        funcs = []
        suits = []
        self.calc_init(setInfo)
        # self.SetDetail(setInfo)
        # 角色基础属性
        self.SetBaseStatus()
        return
        # 技能影响角色的属性，如属强、抗性等
        for skill in self.skills:
            skill.effect(self)
        for i in self.charEquipInfo:
            # region 装备效果
            fun = self.equs.get_func_by_id(f'equ_{self.charEquipInfo[i].id}')
            equ = self.equs.get_equ_by_id(self.charEquipInfo[i].id)
            if equ is None:
                continue
            self.SetStatus(**equ.__dict__)
            funcs.append(fun + (equ,))
            # 护甲精通计算
            if equ.typeSon2Id == self.防具类型:
                self.SetStatus(**精通计算(equ.lv, equ.rarity, equ.typeSon1Id, equ.typeSon2Id, self.输出类型, self.buffer))
            # 套装效果
            suits += (equ.suit or '').split(',')
            # endregion
            # region 附魔效果
            fun = self.equs.get_func_by_id(f'prop_{self.charEquipInfo[i].enchant}')
            funcs.append(fun + (equ,))
            # endregion
            # region 徽章效果
            for emblem in self.charEquipInfo[i].emblems:
                fun = self.equs.get_func_by_id(f'prop_{emblem}')
                funcs.append(fun + (equ,))
            # endregion
            # region 魔法封印效果
            for seal in self.charEquipInfo[i].seals:
                fun = self.equs.get_func_by_id(f'seal_{seal}')
                funcs.append(fun + (equ,))
            # endregion
        # region 套装效果
        matchSuit = []
        for i in list(set(filter(lambda x: x != '' and x is not None, suits))):
            # 获取当前的套装的数量
            nums = len(list(filter(lambda x: x == i, suits)))
            # 获取当前的套装信息
            suisInfos = list(filter(lambda x: x.suitID == i, self.equs.suit))
            if len(suisInfos) > 0:
                matchSuit += [i.id for i in list(filter(lambda x: x.needNum <= nums, suisInfos))]
                # 兼容于判断
                if suisInfos[0].compatibility is not None and suisInfos[0].compatibility != '':
                    for compatibility in suisInfos[0].compatibility.split(','):
                        # 兼容于的装备数量
                        numsComp = len(list(filter(lambda x: x == compatibility, suits)))
                        # 大于兼容于小于兼容于加上当前套装数量
                        if numsComp > 0:
                            matchSuit += [
                                i.id
                                for i in list(
                                    filter(
                                        lambda x: x.suitID == compatibility and numsComp < x.needNum <= nums + numsComp,
                                        self.equs.suit,
                                    )
                                )
                            ]
        for i in matchSuit:
            fun = self.equs.get_func_by_id(f'suit_{i}')
            funcs.append(fun + (None,))
        # endregion
        funcs.sort(key=lambda x: x[2])
        for func in funcs:
            # 站街
            func[1](self, func[3], 0)
            # 进图
            func[1](self, func[3], 1)
        return {
            'basicInfo': self.getBasicInos(),
            'skillInfo': [],
        }

    # endregion


def createCharacter(alter: str, equVersion: str = '0'):
    character: Character = None
    module_name = 'core.character.' + alter
    if equVersion is None or equVersion == '':
        equVersion = '0'
    try:
        character = importlib.import_module(module_name).classChange(equVersion)
    except Exception as ex:
        print(ex)
        print('create character ' + module_name + ' error.')
        pass
    return character
