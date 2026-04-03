import sys
from uuid import uuid1

from core.basic.equipment import get_equipment
from ..formula import 增幅计算, 强化技攻, 武器强化计算, 精通计算, 耳环计算, 左右计算, 锻造计算
from ..roleinfo import CharacterEquipInfo, CharacterOathInfo, get_key_by_value
from .base import CharacterBase


class CalcEquipMixin(CharacterBase):
    """装备计算、角色初始化相关方法"""

    # region 打造信息导入

    def SetDetail(self, info: dict[str, dict]) -> None:
        """打造信息导入"""
        self.charEquipInfo = {}
        self.charOathInfo = []
        self.bindAwake = info.get('bindAwake', 50)
        for key in info['equips']:
            self.charEquipInfo[key] = CharacterEquipInfo(info['equips'][key], self.equVersion, key)
        for key in info['oaths']:
            # 导入誓约打造信息、誓约信息
            self.charOathInfo.append(CharacterOathInfo(info['oaths'][key], self.equVersion, key))

    def calc_init(self, setInfo: dict[str, dict]):
        self.equ_options = setInfo.get('options', {})
        self.setInfo = setInfo
        self.SetDetail(setInfo)
        self.SetSkills(setInfo.get('skills', {}))

    def SetSkills(self, skills: dict[str, dict]):
        """设置技能等级"""
        for key in skills:
            skill = self.GetSkillByID(key)
            if skill is not None:
                if skill.hasUP:
                    skill.up = skills[key].get('up', 0)
                if skill.hasVP:
                    skill.vp = skills[key].get('vp', 0)
                skill.lv += skills[key].get('lv', 0)

    def load_skills(self) -> None:
        """加载技能"""
        module = sys.modules[self.moduleName]
        for name in dir(module):
            memberClass = getattr(module, name)
            if isinstance(memberClass, type) and memberClass.__name__.startswith('Skill'):
                skill = memberClass(char=self)
                self.skills_dict[skill.name] = skill
                self.skills.append(skill)

    # endregion

    # region 套装 / 装备 / 时装 / 基础属性 / 辟邪玉 / 杂项

    def calc_suits(self):
        """套装效果统计"""
        suitInfo = {}
        oathSuitInfo = {}
        equs = get_equipment(self.equVersion)
        for item in filter(lambda x: x.equInfo is not None, self.charEquipInfo.values()):
            partEqu = item.equInfo
            # partFusion = item.fusionInfo
            if partEqu is not None:
                for suit in partEqu.suit:
                    if suitInfo.get(suit, None) is None:
                        suitInfo[suit] = {'point': 0, 'count': 0}
                    if partEqu.Point == 0:
                        suitInfo[suit]['count'] += 1
                    else:
                        suitInfo[suit]['point'] += partEqu.Point
        for item in self.charOathInfo:
            partOath = item.oathInfo
            if partOath is not None:
                for suit in partOath.suit:
                    if oathSuitInfo.get(suit, None) is None:
                        oathSuitInfo[suit] = {'point': 0, 'count': 0}
                    if partOath.Point == 0:
                        oathSuitInfo[suit]['count'] += 1
                    else:
                        oathSuitInfo[suit]['point'] += partOath.Point
        max_point_suit = max((suit for suit in suitInfo if suitInfo[suit]['point'] > 0), key=lambda suit: suitInfo[suit]['point'], default=None)
        max_point_oath_suit = max((suit for suit in oathSuitInfo if oathSuitInfo[suit]['point'] > 0), key=lambda suit: oathSuitInfo[suit]['point'], default=None)
        zero_point_suits = [suit for suit in suitInfo if suitInfo[suit]['point'] == 0]
        # 套装没有到太初的时候，优先把誓约套装的点数加到装备套装上，以达到更高的套装等级
        if 0 < suitInfo[max_point_suit]['point'] < 2550:
            suitInfo[max_point_suit]['point'] += min(2550 - suitInfo[max_point_suit]['point'], oathSuitInfo[max_point_oath_suit]['point'])
            oathSuitInfo[max_point_oath_suit]['point'] -= min(2550 - suitInfo[max_point_suit]['point'], oathSuitInfo[max_point_oath_suit]['point'])
            pass
        suits = zero_point_suits + ([max_point_suit] if max_point_suit is not None else [])
        suitList = []
        oathSuitList = []
        res = []
        for suit in suits:
            if suitInfo[suit]['point'] == 0:
                suitList += equs.get_suit_info(suit, 0, suitInfo[suit]['count'])
            else:
                suitList += equs.get_suit_info(suit, suitInfo[suit]['point'], 0)
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

        for suit in oathSuitInfo:
            if oathSuitInfo[suit]['point'] == 0:
                oathSuitList += equs.get_oath_suit_info(suit, 0, oathSuitInfo[suit]['count'])
            else:
                oathSuitList += equs.get_oath_suit_info(suit, oathSuitInfo[suit]['point'], 0)
            if len(oathSuitList) == 0:
                continue
            print(oathSuitList[0].__dict__)
        suits_effect = [i.id for i in suitList]
        for i in suits_effect:
            func = equs.funs.execture(f'suit_{i}')
            suit = next((x for x in equs.suits if str(x.id) == str(i)), None)
            if func is not None:
                func(self)
            if suit is not None:
                filtered_dict = {k: v for k, v in suit.__dict__.items() if k[0].isupper()}
                self.SetStatus(**filtered_dict)
        self.max_point = max([i['point'] for i in res], default=0)
        if self.max_point >= 2550:
            skillAttack = (self.max_point - 2550) // 70 * 0.01
            buffer = (self.max_point - 2550) // 70 * 100
            self.SetStatus(SkillAttack=skillAttack, Buffer=buffer)
        return res

    def calc_equs(self):
        """计算装备基础效果、附魔"""
        effects = get_equipment(self.equVersion).funs
        # for detail in [(item.equInfo, item.fusionInfo, item.enchant, item.emblem_0, item.emblem_1) for item in filter(lambda x: x.equInfo is not None, self.charEquipInfo.values())]:
        for detail in [(item.equInfo, item.enchant) for item in filter(lambda x: x.equInfo is not None, self.charEquipInfo.values())]:
            equ = detail[0]
            if equ is None or equ.itemType == '副武器':
                continue
            enchat = detail[1]
            fun = effects.execture(f'equ_{equ.id}')
            if fun is None:
                continue
            filtered_dict = {k: v for k, v in equ.__dict__.items() if k[0].isupper()}
            self.SetStatus(**filtered_dict)
            fun(self)
            fun = effects.execture(f'enchant_{enchat}')
            if fun is not None:
                fun(self)
            # emblem_0 = detail[3]
            # emblem_1 = detail[4]
            # if str(emblem_0).isdigit():
            #     fun = effects.execture(f'emblem_{emblem_0}')
            #     if fun is not None:
            #         fun(self)
            # else:
            #     skill = self.GetSkillByName(emblem_0)
            #     if skill is not None:
            #         skill.lv += 1
            #         self.SetStatus(四维=8)
            # fun = effects.execture(f'emblem_{emblem_1}')
            # if fun is not None:
            #     fun(self)
            # if fusion is None:
            #     continue
            # fun = effects.execture(f'stone_{fusion.id}')
            # filtered_dict = {k: v for k, v in fusion.__dict__.items() if k[0].isupper()}
            # self.SetStatus(**filtered_dict)
            # if fun is not None:
            #     fun(self)

    def calc_oaths(self):
        pass

    def calc_avatar(self, avatar: dict):
        """计算时装效果"""
        equ = get_equipment(self.equVersion)
        dress = {key: value for key, value in avatar.items() if key in ['头部', '帽子', '脸部', '胸部', '上衣', '腰带', '下装', '鞋']}
        equ.funs.calc_dress_effect(dress, self)
        avatarElse = {key: value for key, value in avatar.items() if key not in ['头部', '帽子', '脸部', '胸部', '上衣', '腰带', '下装', '鞋']}
        for key in avatarElse:
            value = avatarElse[key].get('enchant', None)
            emblem_0 = avatarElse[key].get('emblem_0', None)
            emblem_1 = avatarElse[key].get('emblem_1', None)
            if value is not None:
                fun = equ.funs.execture(f'enchant_{value}')
                if fun is not None:
                    fun(self)
            for i in [emblem_0, emblem_1]:
                if i is None:
                    continue
                fun = equ.funs.execture(f'emblem_{i}')
                if fun is not None:
                    fun(self)

    def calc_weapon(self, cur: 'CharacterEquipInfo'):
        """武器强化、锻造计算"""
        value = 锻造计算(115, '史诗', cur.refine)
        self.SetStatus(AtkI=value)
        if '传世武器' in cur.equInfo.categorize:
            value = 武器强化计算(115, '史诗', cur.reinforce, cur.equInfo.itemDetailType, '物理', 1.12)
            self.SetStatus(AtkP=value, AtkM=value)
        else:
            value = 武器强化计算(115, '史诗', cur.reinforce, cur.equInfo.itemDetailType, '物理')
            self.SetStatus(AtkP=value)
            value = 武器强化计算(115, '史诗', cur.reinforce, cur.equInfo.itemDetailType, '魔法')
            self.SetStatus(AtkM=value)

    def calc_basic(self):
        """计算基础属性:防具精通、增幅、强化等"""
        for part in ['上衣', '头肩', '下装', '腰带', '鞋']:
            cur = self.charEquipInfo[part]
            if cur.equInfo is None:
                continue
            equ = cur.equInfo
            reinforce = self.charEquipInfo[part].reinforce
            if equ is None:
                continue
            for key in self.防具精通属性:
                value = 精通计算(115, equ.rarity, reinforce, equ.itemDetailType, self.防具类型, self.buffer, key)
                key = get_key_by_value(key)
                setattr(self, key, getattr(self, key) + value)
        for part in self.charEquipInfo.keys():
            cur = self.charEquipInfo[part]
            if cur.equInfo is None:
                continue
            if cur.reinforceType == 1:
                value = 增幅计算(115, '史诗', cur.reinforce)
                self.SetStatus(STR=value, INT=value, Spirit=value, Vitality=value)
            value = 强化技攻(cur.reinforce, cur.reinforceType, part)
            self.SetStatus(SkillAttack=value)
            if '武器' in part:
                self.calc_weapon(cur)
            if part == '耳环':
                value = 耳环计算(115, '史诗', cur.reinforce)
                self.SetStatus(AtkM=value, AtkP=value, AtkI=value)
            if part in ['辅助装备', '魔法石']:
                value = 左右计算(115, '史诗', cur.reinforce)
                self.SetStatus(STR=value, INT=value, Spirit=value, Vitality=value)

    def calc_jade(self, jades):
        """计算辟邪玉效果"""
        funs = get_equipment(self.equVersion).funs
        for key in jades:
            jade = jades[key]
            fun = funs.execture(f'jade_{jade.get("id", 0)}')
            if fun is not None:
                fun(self, jade.get('value', 0))

    def calc_sundry(self, sundry: dict):
        """计算杂项效果"""
        funs = get_equipment(self.equVersion).funs
        funs.execture('sundry_0')(
            self,
            sundry.get('medal_rarity', 0),
            sundry.get('medal_reinforce', 0),
            [sundry.get('medal_gem_0', 0), sundry.get('medal_gem_1', 0), sundry.get('medal_gem_2', 0), sundry.get('medal_gem_3', 0)],
        )
        funs.execture('sundry_6')(self, sundry.get('adventure', 1))
        funs.execture('sundry_5')(self, sundry.get('fog', 1))
        funs.execture('sundry_7')(self, sundry.get('marriage_house', 0), sundry.get('marriage_ring', 0))
        funs.execture('sundry_9')(self, sundry.get('contract', 0))
        funs.execture('sundry_10')(
            self,
            sundry.get('collection_type', 0),
            sundry.get('collection_num_0', 0),
            sundry.get('collection_num_1', 0),
        )
        funs.execture('sundry_13')(self, sundry.get('costume_card', 0))

    # endregion

    # region 主计算入口

    def calc(self, setInfo: dict[str, dict]):
        self.calc_init(setInfo)
        self.SetBaseStatus()
        self.calc_jade(setInfo.get('jades', []))
        self.calc_avatar(setInfo.get('avatar', {}))
        self.calc_basic()
        self.calc_sundry(setInfo.get('sundry', {}))
        suit = self.calc_suits()
        self.calc_equs()
        self.calc_oaths()
        skillInfos = []
        if self.buffer:
            skillInfos = self.calc_buffer_skills()
            info = self.get_buffer_info()
        else:
            if len(self.输出类型选项) > 1:
                temp = self.输出类型选项[0]
                if '固伤' in temp:
                    if self.INT > self.STR:
                        self.输出类型 = '魔法固伤'
                    else:
                        self.输出类型 = '物理固伤'
                else:
                    if self.INT > self.STR and self.AtkM > self.AtkP:
                        self.输出类型 = '魔法百分比'
                    else:
                        self.输出类型 = '物理百分比'
            skillInfos = self.calc_carry_skills(setInfo.get('DSB', False), setInfo.get('BUFF', False))
            info = self.get_carry_info()
        return {'uuid': uuid1().hex, 'skills': skillInfos, 'info': info, 'suits': suit, 'buffer': self.buffer}

    # endregion
