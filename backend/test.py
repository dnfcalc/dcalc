from core.character.GF.gunner_female.spitfire_female import classChange


if __name__ == '__main__':
    # print(equs.equ_dict["100161036"].adapt(2).adapt(0).Point)
    char = classChange(0)
    print(char.getInfo())
    char.calc_init(
        {
            'equips': {
                '武器': {
                    'id': '85',
                    'reinforce': 1,
                    'reinforceType': 1,
                    'enchant': '1',
                    'emblems': ['1'],
                    'upgrade': 1,
                    'refine': 1,
                    'upgradeDetail': {'1': 1},
                    'adaptation': 1,
                },
                '上衣': {
                    'id': '855',
                    'reinforce': 1,
                    'reinforceType': 1,
                    'enchant': '1',
                    'emblems': ['1'],
                    'upgrade': 1,
                    'refine': 1,
                    'upgradeDetail': {'1': 1},
                    'adaptation': 0,
                },
            },
            'skills': {'1': {'lv': 20}, '5': {'lv': 10}},
        }
    )
    手雷精通 = char.GetSkillByName('手雷精通')
    G14手雷 = char.GetSkillByName('G-14手雷')
    print(手雷精通.lv, G14手雷.lv)
    print(char.GetSkillByName('G-14手雷').skillInfo())
    print(char.charEquipInfo['武器'].equInfo.name)
#     # 当前适用的套装搜索
#     suitId = 16201
#     point = 2345

#     suits = equs.get_suit_info(suitId, point,0)

#     print(suits[0].__dict__)

# class A:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#         self.skills:list[B] = []

#     def __str__(self):
#         return f"{self.a} {self.b}"

#     def __repr__(self):
#         return f"{self.a} {self.b}"

# class B:

#     _lv = 0

#     def __init__(self,char):
#         self.char = char
#         self.lv = 1

#     @property
#     def lv(self):
#         return self._lv

#     @lv.setter
#     def lv(self, value):
#         if self._lv != value:
#             self.effect(self._lv,value)
#             self._lv = value

#     def effect(self,old,new):
#         self.char.a += new - old

# a = A()
# b = B(a)
# a.skills.append(b)
# b.lv += 1
# print(a.a)
