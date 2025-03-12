# 944b9aab492c15a8474f96947ceeb9e4
from core.basic.skill import PassiveSkill, ActiveSkill, characterLv
from core.basic.character import Character


class Skill0(ActiveSkill):
    # 기본기 숙련
    # https://api.neople.co.kr/df/skills/944b9aab492c15a8474f96947ceeb9e4/5a56514f35cf0270ae8d6c65f8fefd78?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
    name = '基础精通'
    icon = '$common/$name'
    learnLv = 1
    masterLv = characterLv
    maxLv = 200
    position = 0
    rangeLv = 1
    damage = False
    type = 'passive'


    data0 = [0, 150, 158.7, 167.3, 176, 184.5, 193.2, 201.8, 210.5, 219.2, 227.7, 236.4, 245, 253.7, 262.2, 270.9, 284.3, 297.6, 311, 324.3, 337.7, 350.9, 364.2, 377.6, 390.9, 404.3, 417.6, 431, 444.3, 457.7, 471, 484.2, 497.6, 510.9, 524.3, 537.6, 551, 564.3, 577.7, 591, 604.4, 617.7, 630.9, 644.3, 657.6, 671, 684.3, 697.7, 711, 724.4, 737.7, 751.1, 764.3, 777.6, 791, 804.3, 817.7, 831, 844.4, 857.7, 871.1, 884.4, 897.8, 911, 924.3, 937.7, 951, 964.4, 977.7, 991.1, 1004.4, 1017.8, 1031.1, 1044.5, 1057.7, 1071, 1084.4, 1097.7, 1111.1, 1124.4, 1137.8, 1151.1, 1164.5, 1177.8, 1191, 1204.4, 1217.7, 1231.1, 1244.4, 1257.8, 1271.1, 1284.5, 1297.8, 1311.2, 1324.5, 1337.7, 1351.1, 1364.4, 1377.8, 1391.1, 1404.5, 1417.8, 1431.2, 1444.5, 1457.9, 1471.2, 1484.6, 1497.9, 1511.3, 1524.6, 1538, 1551.3, 1564.7, 1578, 1591.4, 1604.7, 1618.1, 1631.4, 1644.8, 1658.1, 1671.5, 1684.8, 1698.2, 1711.5, 1724.9, 1738.2, 1751.6, 1764.9, 1778.3, 1791.6, 1805, 1818.3, 1831.7, 1845, 1858.4, 1871.7, 1885.1, 1898.4, 1911.8, 1925.1, 1938.5, 1951.8, 1965.2, 1978.5, 1991.9, 2005.2, 2018.6, 2031.9, 2045.3, 2058.6, 2072, 2085.3, 2098.7, 2112, 2125.4, 2138.7, 2152.1, 2165.4, 2178.8, 2192.1, 2205.5, 2218.8, 2232.2, 2245.5, 2258.9, 2272.2, 2285.6, 2298.9, 2312.3, 2325.6, 2339, 2352.3, 2365.7, 2379, 2392.4, 2405.7, 2419.1, 2432.4, 2445.8, 2459.1, 2472.5, 2485.8, 2499.2, 2512.5, 2525.9, 2539.2, 2552.6, 2565.9, 2579.3, 2592.6, 2606, 2619.3, 2632.7, 2646, 2659.4, 2672.7, 2686.1, 2699.4, 2712.8, 2726.1, 2739.5]# noqa: E501

# G-14手雷 G-14 파열류탄
# https://api.neople.co.kr/df/skills/944b9aab492c15a8474f96947ceeb9e4/de3fea2d65c597f4d55c70a02b97fc79?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill1(ActiveSkill):
    name = "G-14手雷"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 2
    mp = [20, 160]

    data0 = [0, 751, 830, 904, 981, 1057, 1132, 1210, 1287, 1362, 1438, 1516, 1591, 1668, 1746, 1819, 1897, 1972, 2049, 2127, 2202, 2278, 2355, 2429, 2508, 2584, 2659, 2735, 2814, 2888, 2965, 3041, 3116, 3194, 3271, 3346, 3422, 3500, 3575, 3652, 3732, 3806, 3883, 3961, 4034, 4112, 4189, 4264, 4342, 4418, 4493, 4570, 4648, 4723, 4799, 4876, 4950, 5029, 5105, 5180, 5256, 5335, 5409, 5486, 5562, 5637, 5715, 5792, 5867, 5943, 6021]# noqa: E501

class Skill2(PassiveSkill):
    # 니트로 모터
    # https://api.neople.co.kr/df/skills/944b9aab492c15a8474f96947ceeb9e4/4224f9b0b8c7c903e9a1e0f9d9f6d04d?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
    name = '单兵推进器'
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 8
    rangeLv = 1

    data0 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
    data1 = [0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

    associate = [
        {'data': data0, 'skills': ['交叉射击', '聚合弹', '凝固汽油弹', '超真空弹：切利']},
        {'data': data1, 'skills': ['爆裂弹']}
    ]


class Skill3(PassiveSkill):
    # 병기 숙련
    # https://api.neople.co.kr/df/skills/944b9aab492c15a8474f96947ceeb9e4/bae12a6dc7d22a5cf149673e88ddda28?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
    name = '兵器研究'
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 0
    rangeLv = 3

    data0 = [0, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]  # noqa: E501
    associate = [{'data': data0, 'type': '$*PAtkI'}]

    # def precondition(self):
    #     weapon = self.char.charEquipInfo['武器'].equInfo
    #     if weapon is not None and (weapon.itemDetailType == '手弩' or weapon.itemDetailType == '步枪' or weapon.categorize == '传世武器'):
    #         return True
    #     return False

class Skill4(PassiveSkill):
    # 강화탄
    # https://api.neople.co.kr/df/skills/944b9aab492c15a8474f96947ceeb9e4/3829c15bf5f520c13998a3479ba0ce7b?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
    name = '弹药改良'
    learnLv = 20
    masterLv = 10  # todo
    maxLv = 20
    position = 1  # todo
    rangeLv = 3

    data0 = [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]  # noqa: E501
    data1 = [0, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]  # noqa: E501


class Skill5(PassiveSkill):
    # 유탄 마스터리
    # https://api.neople.co.kr/df/skills/944b9aab492c15a8474f96947ceeb9e4/0113c8b1306ca76d208f83f2d093dd62?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
    name = '手雷精通'
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 7
    rangeLv = 3

    data0 = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]  # noqa: E501

    associate = [{'type': '*skillRation', 'data': data0, 'skills': ['G-14手雷']}]

class Skill6(ActiveSkill):
    # M18 클레이모어
    # https://api.neople.co.kr/df/skills/944b9aab492c15a8474f96947ceeb9e4/2ff50c35efcf0f287c4c418c8454da48?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
    name = "M18阔剑地雷"
    learnLv = 20
    masterLv = 60 #todo
    maxLv = 70
    position = 8 #todo
    rangeLv = 2
    cd = 6
    mp = [70, 588]

    data0 = [0, 2094, 2307, 2519, 2732, 2944, 3157, 3368, 3580, 3793, 4009, 4221, 4434, 4646, 4859, 5071, 5284, 5496, 5709, 5921, 6132, 6344, 6557, 6769, 6982, 7198, 7410, 7623, 7835, 8048, 8260, 8473, 8685, 8896, 9109, 9321, 9534, 9746, 9959, 10171, 10384, 10600, 10812, 11025, 11237, 11450, 11660, 11873, 12085, 12298, 12510, 12723, 12935, 13148, 13360, 13573, 13789, 14001, 14212, 14425, 14637, 14850, 15062, 15275, 15487, 15700, 15912, 16125, 16337, 16550, 16762]# noqa: E501

class classChange(Character):
    def __init__(self, equVersion=''):

        super().__init__(equVersion)
        self.name = 'spitfire_female'
        self.nameShow = '重霄·弹药专家'
        self.role = 'gunner_female'

        # 用来筛CP武器的
        # self.转职 = '弹药专家(女)'
        self.武器选项 = ['手弩', '步枪','左轮枪','自动手枪','手炮']
        self.输出类型选项 = ['魔法固伤', '物理固伤']
        self.防具精通属性 = ['智力', '力量']
        self.类型 = '魔法固伤'
        self.武器类型 = '手弩'
        self.防具类型 = '皮甲'
        self.buff = 1.84

        self.load_skills()

    def load_skills(self):
        """加载技能"""
        skills = []
        skills_dict = {}
        i = 0
        while i >= 0:
            try:
                tem = eval('Skill' + str(i) + '(char=self)')
                skills_dict[tem.name] = tem
                skills.append(tem)
                i += 1
            except Exception as e:
                print(e)
                i = -1
        self.skills = skills
        self.skills_dict = skills_dict

    def set_skill_info(self, info, rune_except=[], clothes_pants=[]):
        super().set_skill_info(info, rune_except=['爆裂弹'], clothes_pants=['远古记忆'])
