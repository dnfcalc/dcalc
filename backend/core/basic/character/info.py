from core.basic.equipment import get_equipment
from core.basic.property import CharacterInfo
from .base import CharacterBase


class CharacterInfoMixin(CharacterBase):
    """角色信息查询相关方法（用于前端展示）"""

    def getInfo(self):
        """返回到前端信息"""
        info = {}
        info['role'] = self.role
        info['alter'] = self.name
        info['equVersion'] = self.equVersion
        info['name'] = self.nameCN
        info['weapons'] = self.武器选项
        info['subweapons'] = self.副武器选项
        info['buffer'] = self.buffer
        if self.buffer:
            info['properties'] = self.防具精通属性
        info['properties'] = self.输出类型选项
        skillInfo = []
        skill_clothes = []
        platinum = []
        for skill in self.skills:
            if 15 <= skill.learnLv <= 70 and skill.learnLv not in [48, 50]:
                platinum.append(skill.name)
            if skill.learnLv <= 95:
                skill_clothes.append(skill.name)
            skillInfo.append(
                {
                    'id': skill.id,
                    'name': skill.name,
                    'icon': skill.icon,
                    'type': skill.type,
                    'learnLv': skill.learnLv,
                    'masterLv': skill.masterLv,
                    'maxLearnLv': skill.calculate_lv(),
                    'maxLv': skill.maxLv,
                    'position': skill.position,
                    'line': skill.line,
                    'bind': skill.bind,
                    'hasVP': skill.hasVP,
                    'hasUP': skill.hasUP,
                    'upType': skill.upType,
                    'uuid': skill.uuid,
                    'vps': [{'name': i['name'], 'desc': i['desc']} for i in skill.vps],
                }
            )
        info['skills'] = skillInfo
        equInfos = get_equipment(self.equVersion)
        equs = []
        suits = []
        oaths = []
        oaths_skills = {}
        # stones = []
        for i in equInfos.equs:
            if i.itemType == '武器' and i.itemDetailType not in self.武器选项:
                continue
            equs.append(i.__dict__)
        for i in equInfos.suits:
            suits.append(i.__dict__)
        for i in equInfos.oaths:
            oaths.append(i.__dict__)
        for i in equInfos.oath_suits:
            if i.suitId not in oaths_skills:
                oaths_skills[i.suitId] = {'suitInfo': [], 'skills': []}
            oaths_skills[i.suitId]['suitInfo'].append(
                {
                    'name': i.name,
                    'rarity': i.rarity,
                    'SkillAttack': i.SkillAttack,
                    'Buffer': i.Buffer,
                    'Attack': i.Attack,
                }
            )
            if len(oaths_skills[i.suitId]['skills']) == 0:
                for skill in i.skills:
                    oaths_skills[i.suitId]['skills'].append(
                        {
                            'skillId': skill.skillId,
                            'name': skill.name,
                            'icon': skill.imageUrl,
                        }
                    )
        # for i in equInfos.stones:
        #     stones.append(i.__dict__)
        info['oaths'] = oaths
        info['equips'] = equs
        info['suits'] = suits
        info['oaths_skills'] = oaths_skills
        # info['stones'] = stones
        key = '辅助' if self.buffer else '输出'
        info['enchants'] = list(filter(lambda x: key in x['categorize'], equInfos.enchants))
        info['emblems'] = [i for i in equInfos.emblems]
        info['avatar'] = equInfos.funs.get_dress_list(skill_clothes)
        info['jades'] = equInfos.jades
        info['options'] = equInfos.funs.options
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
