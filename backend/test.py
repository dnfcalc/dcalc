from core.basic.character import createCharacter

char = createCharacter('GF.gunner_female.spitfire_female')

char.calc_init(
    {
        'oaths': {'0': {'id': '2030201', 'adaptation': 3}, '1': {'id': '2030201', 'adaptation': 3}, '2': {'id': '2030201', 'adaptation': 3}, '3': {'id': '2030201', 'adaptation': 3}, '4': {'id': '2030201', 'adaptation': 3}, '11': {'id': '2030200', 'adaptation': 0}},
        'oathSkill': 1,
        'equips': {
            '武器': {'id': '88', 'reinforce': 14, 'reinforceType': 1, 'enchant': 512, 'emblem_0': 0, 'emblem_1': 0, 'fusion': 0, 'refine': 8, 'adaptation': 3, 'precision': 100},
            '称号': {'id': '3017', 'reinforce': 0, 'reinforceType': 0, 'enchant': 1201, 'emblem_0': 0, 'emblem_1': 0, 'fusion': 0, 'refine': 0, 'adaptation': 3, 'precision': 100},
            '上衣': {'id': '999', 'reinforce': 13, 'reinforceType': 1, 'enchant': 105, 'emblem_0': 1, 'emblem_1': 1, 'fusion': '26', 'refine': 0, 'adaptation': 3, 'precision': 100},
            '头肩': {'id': '1001', 'reinforce': 14, 'reinforceType': 1, 'enchant': 5, 'emblem_0': 0, 'emblem_1': 0, 'fusion': '28', 'refine': 0, 'adaptation': 3, 'precision': 100},
            '下装': {'id': '1000', 'reinforce': 14, 'reinforceType': 1, 'enchant': 202, 'emblem_0': 1, 'emblem_1': 1, 'fusion': '27', 'refine': 0, 'adaptation': 3, 'precision': 100},
            '鞋': {'id': '1003', 'reinforce': 14, 'reinforceType': 1, 'enchant': 309, 'emblem_0': 11, 'emblem_1': 11, 'fusion': '30', 'refine': 0, 'adaptation': 3, 'precision': 100},
            '腰带': {'id': '1002', 'reinforce': 14, 'reinforceType': 1, 'enchant': 309, 'emblem_0': 4, 'emblem_1': 4, 'fusion': '29', 'refine': 0, 'adaptation': 3, 'precision': 100},
            '项链': {'id': '477', 'reinforce': 13, 'reinforceType': 1, 'enchant': 609, 'emblem_0': 0, 'emblem_1': 0, 'fusion': '180', 'refine': 0, 'adaptation': 3, 'precision': 100},
            '手镯': {'id': '483', 'reinforce': 14, 'reinforceType': 1, 'enchant': 609, 'emblem_0': 11, 'emblem_1': 11, 'fusion': '302', 'refine': 0, 'adaptation': 3, 'precision': 100},
            '戒指': {'id': '489', 'reinforce': 14, 'reinforceType': 1, 'enchant': 609, 'emblem_0': 4, 'emblem_1': 4, 'fusion': '304', 'refine': 0, 'adaptation': 3, 'precision': 100},
            '辅助装备': {'id': '492', 'reinforce': 14, 'reinforceType': 1, 'enchant': 905, 'emblem_0': '兵器研究', 'emblem_1': 0, 'fusion': '182', 'refine': 3, 'adaptation': 3, 'precision': 100},
            '魔法石': {'id': '495', 'reinforce': 14, 'reinforceType': 1, 'enchant': 1003, 'emblem_0': '兵器研究', 'emblem_1': 0, 'fusion': '184', 'refine': 3, 'adaptation': 3, 'precision': 100},
            '耳环': {'id': '498', 'reinforce': 14, 'reinforceType': 1, 'enchant': 1104, 'emblem_0': 0, 'emblem_1': 0, 'fusion': '186', 'refine': 0, 'adaptation': 3, 'precision': 100},
            '宠物': {'id': '4022', 'reinforce': 0, 'reinforceType': 0, 'enchant': 1304, 'emblem_0': 0, 'emblem_1': 0, 'fusion': 0, 'refine': 0, 'adaptation': 3, 'precision': 100},
        },
    }
)

char.calc_suits()

# for oath in char.charOathInfo:
#     print(oath.id, oath.adaptation, oath.oathInfo.position, oath.oathInfo.max_adaptation, oath.oathInfo.Point)
