from functools import cache
import importlib
from typing import Any, Literal, Mapping, Union
from uuid import uuid1

from core.basic.property import CharacterInfo
from core.basic.skill import Skill

from core.basic.equipment import get_equipment, EquEffect, Equ

# from core.basic.equipment import equipments
# from core.basic.skill import Skill, ActiveSkill, PassiveSkill
from .formula import 增幅计算, 强化技攻, 武器强化计算, 精通计算, 获取基础属性, 耳环计算, 左右计算, 锻造计算
from .roleinfo import CharacterEquipInfo, get_key_by_value
# from .property import 精通计算, 角色基础, CharacterInfo


class Jade:
    ElementIncrease: float
    """属性增幅"""
    AttackP: float
    """攻击强化%"""
    SkillAttack: float
    """技能攻击力%"""

    def __init__(self) -> None:
        self.ElementIncrease = 0.0
        self.AttackP = 0.0
        self.SkillAttack = 0.0


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

    jade_effect: 'Jade'
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

    skills: list['Skill'] = []
    # """技能列表"""
    skills_dict: dict[str, 'Skill'] = {}
    # """技能名字对应技能"""
    equVersion: str = '0'
    """装备版本"""
    charEquipInfo: dict[str, 'CharacterEquipInfo']
    """装备打造信息"""
    equ_effect: list['EquEffect'] = []
    """装备效果列表"""
    equ_options: dict[str, int] = {}
    """装备选项列表"""
    EquEffectRatio = 1
    """装备效果倍率"""
    max_point = 0
    """套装效果点数"""

    # region 角色属性
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

    输出类型: str = '物理百分比'

    # endregion

    def __init__(self, equVersion) -> None:
        self.equVersion = equVersion
        # self.equs = get_equ(self.equVersion)
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
            self.ElementDB[elem] += kwargs.get(f'{elem}强', 0) + kwargs.get('ElementDB', {}).get(elem, 0) + kwargs.get('全属强', 0)
            self.ElementR[elem] += kwargs.get(f'{elem}抗', 0) + kwargs.get('ElementR', {}).get(elem, 0) + kwargs.get('全属抗', 0)
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
        self.EquEffectRatio *= 1 + kwargs.get('EquEffectRatio', 0.0)
        pass

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
        pass

    def AddSkillLv(self, min: int, max: int, lv: int, type=-1) -> None:
        """
        增加技能等级
        type: -1 全部, 0 被动, 1 主动
        """
        for skill in self.skills:
            if min <= skill.learnLv <= max:
                type = 'all' if type == -1 else ('active' if type == 1 else 'passive')
                if type == 'all' or skill.type == type:
                    skill.lv += 1

    def SetSkillCD(self, min=1, max=100, cd=0, exclude=[50, 85, 100]) -> None:
        """
        设置技能CD
        type: -1 全部, 0 被动, 1 主动
        """
        for skill in self.skills:
            if min <= skill.learnLv <= max and skill.damage and skill.learnLv not in exclude:
                skill.cdReduce *= 1 - cd

    def SetSkillCDRecover(self, min=1, max=100, cd=0, exclude=[50, 85, 100]) -> None:
        """设置技能CD恢复"""
        for skill in self.skills:
            if min <= skill.learnLv <= max and skill.damage and skill.learnLv not in exclude:
                skill.cdRecover += cd

    def SetSkillRation(self, min=1, max=100, ratio=0, type=0) -> None:
        """设置技能倍率 0 修改技能面板 1 不修改技能面板"""
        for skill in self.skills:
            if min <= skill.learnLv <= max and skill.damage:
                if type == 0:
                    skill.skillRation *= 1 + ratio
                else:
                    skill.skillDamage *= 1 + ratio

    def GetSkillByName(self, name) -> Skill:
        """通过技能名获取技能"""
        return self.skills_dict.get(name, None)

    def GetSkillByID(self, id: str) -> Skill:
        skill = list(filter(lambda x: str(x.id) == id, self.skills))
        """通过技能ID获取技能"""
        return skill[0] if len(skill) > 0 else None

    def GetSkillNames(self, type: Literal['active', 'passive', 'all'] = 'all', damage: Literal[True, False, 'all'] = 'all') -> list[str]:
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

    def getInfo(self):
        """返回到前端信息"""
        info = {}
        info['role'] = self.role
        info['alter'] = self.name
        info['equVersion'] = self.equVersion
        info['name'] = self.nameCN
        info['weapons'] = self.武器选项
        skillInfo = []
        skill_clothes = []
        platinum = []
        for skill in self.skills:
            # 白金
            if 15 <= skill.learnLv <= 70 and skill.learnLv not in [48, 50]:
                platinum.append(skill.name)
            # 时装
            if skill.learnLv <= 95:
                skill_clothes.append(skill.name)
            skillInfo.append(
                {
                    'id': skill.id,
                    'name': skill.name,
                    'icon': skill.icon,
                    'type': skill.type,
                    # 'SPCost': skill.SPCost,
                    'learnLv': skill.learnLv,
                    'masterLv': skill.masterLv,
                    'maxLearnLv': skill.calculate_lv(),
                    'maxLv': skill.maxLv,
                    # 'TPCost': 0 if not skill.hasTP else skill.TPCost,
                    # "masterTPLv":0 if not skill.hasTP else  skill.masterTPLv,
                    # 'maxTPLv': 0 if not skill.hasTP else skill.TPLearnMax,
                    'position': skill.position,
                }
            )
        info['skills'] = skillInfo
        equInfos = get_equipment(self.equVersion)
        equs = []
        suits = []
        stones = []
        for i in equInfos.equs:
            if i.itemType == '武器' and i.itemDetailType not in self.武器选项:
                continue
            equs.append(i.__dict__)
        for i in equInfos.suits:
            suits.append(i.__dict__)
        for i in equInfos.stones:
            stones.append(i.__dict__)
        info['equips'] = equs
        info['suits'] = suits
        info['stones'] = stones
        info['enchants'] = equInfos.enchants
        info['emblems'] = equInfos.emblems
        info['avatar'] = equInfos.funs.get_dress_list(skill_clothes)
        info['jades'] = equInfos.jades
        info['sundry'] = equInfos.funs.sundryList
        for skill in platinum:
            info['emblems'].append(
                {
                    'id': skill,
                    'fame': 232,
                    'position': ['辅助装备', '魔法石'],
                    'detail': skill + ' Lv+1' + ' 四维 + 8',
                    'categorize': ['技能'],
                    'rarity': '白金',
                }
            )
        return info

    def getBasicInos(self):
        res = []
        attrs = []
        if self.输出类型.includes('物理'):
            attrs = ['STR', 'PSTR', 'AtkP', 'PAtkP', 'CriticalPP', 'CriticalP']
        if self.输出类型.includes('魔法'):
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

    def calc_suits(self):
        """套装效果统计"""
        suitInfo = {}
        equs = get_equipment(self.equVersion)
        # 设置装备和获取对应的套装属性
        for item in filter(lambda x: x.equInfo is not None, self.charEquipInfo.values()):
            partEqu = item.equInfo
            partFusion = item.fusionInfo
            # 套装属性设置
            if partEqu is not None:
                for suit in partEqu.suit:
                    if suitInfo.get(suit, None) is None:
                        suitInfo[suit] = {
                            'point': 0,
                            'count': 0,
                        }
                    if partEqu.Point == 0:
                        suitInfo[suit]['count'] += 1
                    else:
                        suitInfo[suit]['point'] += partEqu.Point
            if partFusion is not None:
                for suit in partFusion.suit:
                    if suitInfo.get(suit, None) is None:
                        suitInfo[suit] = {
                            'point': 0,
                            'count': 0,
                        }
                    if partFusion.Point == 0:
                        suitInfo[suit]['count'] += 1
                    else:
                        suitInfo[suit]['point'] += partFusion.Point
        # 取得点数最高的套装
        max_point_suit = max((suit for suit in suitInfo if suitInfo[suit]['point'] > 0), key=lambda suit: suitInfo[suit]['point'], default=None)
        # 处理没有点数的老套装
        zero_point_suits = [suit for suit in suitInfo if suitInfo[suit]['point'] == 0]
        suits = zero_point_suits + ([max_point_suit] if max_point_suit is not None else [])
        suits_effect = []
        suitList = []
        res = []
        for suit in suits:
            if suitInfo[suit]['point'] == 0:
                suitList += equs.get_suit_info(suit, 0, suitInfo[suit]['count'])
                # suits_effect += [i.id for i in equs.get_suit_info(suit, 0, suitInfo[suit]['count'])]
            else:
                suitList += equs.get_suit_info(suit, suitInfo[suit]['point'], 0)
                # suits_effect += [i.id for i in equs.get_suit_info(suit, suitInfo[suit]['point'], 0)]
            if len(suitList) == 0:
                continue
            temp = suitList[-1]
            res.append(
                {
                    'id': temp.id,
                    'name': temp.name,
                    'rarity': temp.rarity,
                    'point': suitInfo[suit]['point'],
                    'count': suitInfo[suit]['count'],
                    'level': temp.level,
                    'imageUrl': temp.imageUrl,
                    'value': temp.value,
                }
            )
        suits_effect = [i.id for i in suitList]
        for i in suits_effect:
            func = equs.funs.suit_func_list.get(str(i), None)
            suit = next((x for x in equs.suits if str(x.id) == str(i)), None)
            if func is not None:
                func(self)
            if suit is not None:
                filtered_dict = {k: v for k, v in suit.__dict__.items() if k[0].isupper()}
                self.SetStatus(**filtered_dict)
        self.max_point = max([i['point'] for i in res], default=0)
        return res

    def calc_equs(self):
        """计算装备基础效果、附魔、贴膜"""
        effects = get_equipment(self.equVersion).funs
        for detail in [(item.equInfo, item.fusionInfo, item.enchant, item.emblem_0, item.emblem_1) for item in filter(lambda x: x.equInfo is not None, self.charEquipInfo.values())]:
            equ = detail[0]
            fusion = detail[1]
            enchat = detail[2]
            if equ is None:
                continue
            fun = effects.equ_func_list.get(str(equ.id), None)
            if fun is None:
                continue
            # 获取装备基础属性 并给角色设置（大写开头属性为角色属性）
            filtered_dict = {k: v for k, v in equ.__dict__.items() if k[0].isupper()}
            self.SetStatus(**filtered_dict)
            # 获取装备额外属性
            fun(self)
            # 附魔
            fun = effects.enchant_func_list.get(str(enchat), None)
            if fun is not None:
                fun(self)
            # 徽章效果
            emblem_0 = detail[3]
            emblem_1 = detail[4]
            if str(emblem_1).isdigit():
                fun = effects.emblem_func_list.get(str(emblem_0), None)
                if fun is not None:
                    fun(self)
            else:
                # 白金徽章处理
                skill = self.GetSkillByName(emblem_0)
                if skill is not None:
                    skill.lv += 1
                    self.SetStatus(四维=8)
            fun = effects.emblem_func_list.get(str(emblem_1), None)
            if fun is not None:
                fun(self)
            # 贴膜
            if fusion is None:
                continue
            fun = effects.stone_func_list.get(str(fusion.id), None)
            # 获取装备基础属性 并给角色设置（大写开头属性为角色属性）
            filtered_dict = {k: v for k, v in fusion.__dict__.items() if k[0].isupper()}
            self.SetStatus(**filtered_dict)
            # 获取装备额外属性
            if fun is not None:
                fun(self)

    def calc_avatar(self, avatar: dict):
        """计算时装效果"""
        equ = get_equipment(self.equVersion)
        dress = {key: value for key, value in avatar.items() if key in ['头发', '帽子', '脸部', '胸部', '上衣', '腰带', '下装', '鞋']}
        equ.funs.calc_dress_effect(dress, self)
        avatarElse = {key: value for key, value in avatar.items() if key not in ['头发', '帽子', '脸部', '胸部', '上衣', '腰带', '下装', '鞋']}
        for key in avatarElse:
            value = avatarElse[key].get('enchant', None)
            emblem_0 = avatarElse[key].get('emblem_0', None)
            emblem_1 = avatarElse[key].get('emblem_1', None)
            if value is not None:
                fun = equ.funs.enchant_func_list.get(str(value), None)
                if fun is not None:
                    fun(self)
            for i in [emblem_0, emblem_1]:
                if i is None:
                    continue
                fun = equ.funs.emblem_func_list.get(str(i), None)
                if fun is not None:
                    fun(self)
        pass

    def calc_basic(self):
        """计算基础属性:防具精通、增幅、强化等"""
        # 防具精通跟随装备品级
        for part in ['上衣', '头肩', '下装', '腰带', '鞋']:
            cur = self.charEquipInfo[part]
            if cur.equInfo is None:
                continue
            equ = cur.equInfo
            reinforce = self.charEquipInfo[part].reinforce
            if equ is None:
                continue
            value = 精通计算(115, equ.rarity, reinforce, equ.itemDetailType, self.防具类型)
            for key in self.防具精通属性:
                key = get_key_by_value(key)
                setattr(self, key, getattr(self, key) + value)
        # 115增幅强化品级固定史诗
        for part in self.charEquipInfo.keys():
            cur = self.charEquipInfo[part]
            if cur.equInfo is None:
                continue
            # 增幅
            if cur.reinforceType == 1:
                # 增幅四维
                value = 增幅计算(115, '史诗', cur.reinforce)
                self.SetStatus(STR=value, INT=value, Spirit=value, Vitality=value)
            # 增幅技攻计算
            value = 强化技攻(cur.reinforce, cur.reinforceType, part)
            self.SetStatus(SkillAttack=value)
            # 武器强化、武器锻造、特殊装备强化额外效果计算
            if part == '武器':
                # 锻造独立计算
                value = 锻造计算(115, '史诗', cur.refine)
                self.SetStatus(AtkI=value)
                # 传世武器强化系数取所有武器的最高的1.12
                if cur.equInfo.categorize == '传世武器':
                    value = 武器强化计算(115, '史诗', cur.reinforce, cur.equInfo.itemDetailType, '物理', 1.12)
                    self.SetStatus(AtkP=value, AtkM=value)
                else:
                    # 强化计算
                    value = 武器强化计算(115, '史诗', cur.reinforce, cur.equInfo.itemDetailType, '物理')
                    self.SetStatus(AtkP=value)
                    value = 武器强化计算(115, '史诗', cur.reinforce, cur.equInfo.itemDetailType, '魔法')
                    self.SetStatus(AtkM=value)
                pass
            if part == '耳环':
                value = 耳环计算(115, '史诗', cur.reinforce)
                self.SetStatus(AtkM=value, AtkP=value, AtkI=value)
                pass
            if part in ['辅助装备', '魔法石']:
                value = 左右计算(115, '史诗', cur.reinforce)
                self.SetStatus(STR=value, INT=value, Spirit=value, Vitality=value)
                pass
        pass

    def calc_jade(self, jades):
        """计算辟邪玉效果"""
        funs = get_equipment(self.equVersion).funs
        for key in jades:
            jade = jades[key]
            fun = funs.jade_func_list.get(str(jade.get('id',0)), None)
            if fun is not None:
                fun(self,jade.get('value', 0))
        pass

    def calc_sundry(self, sundry: dict):
        """计算杂项效果"""
        funs = get_equipment(self.equVersion).funs
        funs.sundry_func_list.get("0")(self,
            sundry.get("medal_rarity", 0),
            sundry.get("medal_reinforce", 0),
            [sundry.get("medal_0", 0), sundry.get("medal_1", 0), sundry.get("medal_2", 0), sundry.get("medal_3", 0)],
        )
        funs.sundry_func_list.get("6")(self,
            sundry.get("adventure", 1)
        )
        funs.sundry_func_list.get("7")(self,
            sundry.get("marriage_house", 0),
            sundry.get("marriage_ring", 0)
        )
        funs.sundry_func_list.get("9")(self,
            sundry.get("contract", 0)
        )
        funs.sundry_func_list.get("10")(self,
            sundry.get("collection_type", 0),
            sundry.get("collection_num_0", 0),
            sundry.get("collection_num_1", 0),
        )
        funs.sundry_func_list.get("13")(self,
            sundry.get("costume_card", 0)
        )
        pass

    def calc(self, setInfo: dict[str, dict]):
        self.calc_init(setInfo)
        # self.SetDetail(setInfo)
        # 角色基础属性
        self.SetBaseStatus()
        # 辟邪玉计算
        self.calc_jade(setInfo.get('jades', []))
        # 时装计算
        self.calc_avatar(setInfo.get('avatar', {}))
        # 精通、增幅、强化计算
        self.calc_basic()
        # 杂项信息
        self.calc_sundry(setInfo.get('sundry', {}))
        # 计算套装基础效果
        suit = self.calc_suits()
        # 部位效果计算
        self.calc_equs()

        # print(suit)
        # effects = get_equipment(self.equVersion).funs
        # for effect in equ_effect:
        #     func = effects.equ_func_list.get(str(effect), None)
        #     if func is not None:
        #         func(self)
        # for effect in suits_effect:
        #     func = effects.suit_func_list.get(str(effect), None)
        #     if func is not None:
        #         func(self)
        # 徽章计算
        # 附魔计算

        # 技能计算
        skillInfos = []
        for i in self.skills:
            if i.damage and i.lv > 0:
                for mode in i.mode:
                    temp = i.skillInfo(mode)
                    skillInfos.append(
                        {
                            'name': i.name,
                            'icon': i.icon,
                            'lv': i.lv,
                            'data': temp[0],
                            'ratio': temp[1],
                            'cd': temp[2],
                            'mode': mode,
                        }
                    )
        ratios = self.calc_damage_ration()
        ratio_char_skill = ratios[0] * ratios[1] * ratios[2] * ratios[3] * ratios[4] * ratios[5] * ratios[6] * ratios[7] * ratios[8] * ratios[9] / 1000
        ratuio_equ_skill = ratios[0] * ratios[1] * ratios[3] * ratios[4] * ratios[6] * ratios[7] * ratios[8] * ratios[9] / 1000
        for i in skillInfos:
            i['damage'] = ratio_char_skill * i['data'] * i['ratio'] / 100
        for i in self.equ_effect:
            skillInfos.append(
                {
                    'name': i.name,
                    'icon': i.icon,
                    'lv': 0,
                    'data': i.data,
                    'ratio': 10.0,
                    'cd': i.cd,
                    'damage': ratuio_equ_skill * i.data * 10 * self.EquEffectRatio / 100,
                    'mode':''
                }
            )
        attrs = []
        if self.输出类型 == '物理百分比':
            attrs.extend(['STR', 'AtkP'])
        if self.输出类型 == '魔法百分比':
            attrs.extend(['INT', 'AtkM'])
        if self.输出类型 == '物理固伤':
            attrs.extend(['STR', 'AtkI'])
        if self.输出类型 == '魔法固伤':
            attrs.extend(['INT', 'AtkI'])
        info = []
        attrs.extend(['Attack', 'AttackP', 'SkillAttack','EquEffectRatio', 'ElementDB'])
        for attr in attrs:
            temp = getattr(CharacterInfo, attr)
            if attr.startswith('Atk'):
                info.append({'name': temp.name, 'value': temp.value(getattr(self, attr) * getattr(self, f'P{attr}'))})
                pass
            else:
                value = getattr(self, attr)
                if attr == 'SkillAttack':
                    value *= (self.jade_effect.SkillAttack + 1)
                if attr == 'AttackP':
                    value += self.jade_effect.AttackP
                info.append(
                    {
                        'name': temp.name,
                        'value': temp.value(value),
                    }
                )
                pass
        return {
            'uuid': uuid1().hex,
            'skills': skillInfos,
            'info': info,
            'suits': suit,
        }
        # 技能影响角色的属性，如属强、抗性等

    def calc_damage_ration(self):
        """计算属性系数"""
        # 计算最终属性
        # 力/智 攻击力 攻击力%(特效不吃这部分)
        attrs = []
        if self.输出类型 == '物理百分比':
            attrs.extend(['STR', 'AtkP', 'PAtkP'])
        if self.输出类型 == '魔法百分比':
            attrs.extend(['INT', 'AtkM', 'PAtkM'])
        if self.输出类型 == '物理固伤':
            attrs.extend(['STR', 'AtkI', 'PAtkI'])
        if self.输出类型 == '魔法固伤':
            attrs.extend(['INT', 'AtkI', 'PAtkI'])
        # 力智系数
        ratio_0: float = getattr(self, attrs[0]) / 250 + 1
        # 物理/魔法/独立攻击力
        ratio_1: float = getattr(self, attrs[1])
        # 技能 物理/魔法/独立攻击力%
        ratio_2: float = getattr(self, attrs[2])
        # 属强系数
        ratio_3 = max(self.ElementDB.values()) * 0.0045 + 1.05
        # 暴击系数
        ratio_4 = 1.5
        # BUFF系数
        ratio_5 = self.buff
        # 技攻系数
        ratio_6 = self.SkillAttack * (self.jade_effect.SkillAttack + 1)
        # 攻击强化
        ratio_7 = 1 + self.Attack / 100 * (self.AttackP + self.jade_effect.AttackP)
        # 防御系数,暂定145沙袋防御
        monster_defense = 75117226590
        ratio_8 = 1 - monster_defense / (monster_defense + 200 * 100)
        # 杂项 斗神、宠物技能、队友增幅等(技能的属性增幅归属到这部分，因为会加成到特效部分，修复后修改为技能攻击力计算)
        ratio_9 = 1.0 * self.ElementIncrease
        return (ratio_0, ratio_1, ratio_2, ratio_3, ratio_4, ratio_5, ratio_6, ratio_7, ratio_8, ratio_9)

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
