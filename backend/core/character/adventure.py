import base64
from copy import deepcopy

adv = [
    {
        'id': 0,
        'name': 'swordman_male',
        'title': '鬼剑士(男)',
        'children': [
            {'id': 0, 'name': 'weapon_master', 'title': '极诣·剑魂', 'open': True, 'class': 'GF.swordman_male.weapon_master'},
            {'id': 1, 'name': 'soul_bender', 'title': '极诣·鬼泣', 'open': True, 'class': 'GF.swordman_male.soul_bender'},
            {'id': 2, 'name': 'berserker', 'title': '极诣·狂战士', 'open': True, 'class': 'GF.swordman_male.berserker'},
            {'id': 3, 'name': 'asura', 'title': '极诣·阿修罗', 'open': True, 'class': 'GF.swordman_male.asura'},
            {'id': 4, 'name': 'ghostblade', 'title': '极诣·剑影', 'open': True, 'class': 'GF.swordman_male.ghostblade'},
        ],
    },
    {
        'id': 1,
        'name': 'swordman_female',
        'title': '鬼剑士(女)',
        'children': [
            {'id': 0, 'name': 'sword_master', 'title': '极诣·驭剑士', 'open': True, 'class': 'GF.swordman_female.sword_master'},
            {'id': 1, 'name': 'dark_templar', 'title': '极诣·暗殿骑士', 'open': True, 'class': 'GF.swordman_female.dark_templar'},
            {'id': 2, 'name': 'demon_slayer', 'title': '极诣·契魔者', 'open': True, 'class': 'GF.swordman_female.demon_slayer'},
            {'id': 3, 'name': 'vegabond', 'title': '极诣·流浪武士', 'open': True, 'class': 'GF.swordman_female.vegabond'},
            {'id': 4, 'name': 'spectre', 'title': '极诣·刃影', 'open': True, 'class': 'GF.swordman_female.spectre'},
        ],
    },
    {
        'id': 2,
        'name': 'fighter_male',
        'title': '格斗家(男)',
        'children': [
            {'id': 0, 'name': 'nenmaster_male', 'title': '归元·气功师', 'open': False},
            {'id': 1, 'name': 'striker_male', 'title': '归元·散打', 'open': False},
            {'id': 2, 'name': 'brawler_male', 'title': '归元·街霸', 'open': False},
            {'id': 3, 'name': 'grappler_male', 'title': '归元·柔道家', 'open': False},
            {'name': 'empty', 'title': '', 'comment': '首页'},
        ],
    },
    {
        'id': 3,
        'name': 'fighter_female',
        'title': '格斗家(女)',
        'children': [
            {'id': 0, 'name': 'nenmaster_female', 'title': '归元·气功师', 'open': True, 'class': 'GF.fighter_female.nenmaster_female'},
            {'id': 1, 'name': 'striker_female', 'title': '归元·散打', 'open': False},
            {'id': 2, 'name': 'brawler_female', 'title': '归元·街霸', 'open': False},
            {'id': 3, 'name': 'grappler_female', 'title': '归元·柔道家', 'open': False},
            {'name': 'sponsor', 'url': 'https://bbs.colg.cn', 'title': '', 'open': True},
        ],
    },
    {
        'id': 4,
        'name': 'gunner_male',
        'title': '神枪手(男)',
        'children': [
            {'id': 0, 'name': 'ranger_male', 'title': '重霄·漫游枪手', 'open': False},
            {'id': 1, 'name': 'launcher_male', 'title': '重霄·枪炮师', 'open': False},
            {'id': 2, 'name': 'mechanic_male', 'title': '重霄·机械师', 'open': False},
            {'id': 3, 'name': 'spitfire_male', 'title': '重霄·弹药专家', 'open': False},
            {'id': 4, 'name': 'assault', 'title': '重霄·合金战士', 'open': False},
        ],
    },
    {
        'id': 5,
        'name': 'gunner_female',
        'title': '神枪手(女)',
        'children': [
            {'id': 0, 'name': 'ranger_female', 'title': '重霄·漫游枪手', 'open': False},
            {'id': 1, 'name': 'launcher_female', 'title': '重霄·枪炮师', 'open': False},
            {'id': 2, 'name': 'mechanic_female', 'title': '重霄·机械师', 'open': False},
            {'id': 3, 'name': 'spitfire_female', 'title': '重霄·弹药专家', 'open': True, 'class': 'GF.gunner_female.spitfire_female'},
            {'name': 'empty', 'title': '', 'comment': ''},
        ],
    },
    {
        'id': 6,
        'name': 'mage_male',
        'title': '魔法师(男)',
        'children': [
            {'id': 0, 'name': 'elemental_bomber', 'title': '知源·元素爆破师', 'open': False},
            {'id': 1, 'name': 'glacial_master', 'title': '知源·冰结师', 'open': True, 'class': 'GF.mage_male.glacial_master'},
            {'id': 2, 'name': 'blood_mage', 'title': '知源·血法师', 'open': False},
            {'id': 3, 'name': 'swift_master', 'title': '知源·逐风者', 'open': False},
            {'id': 4, 'name': 'dimension_walker', 'title': '知源·次元行者', 'open': False},
        ],
    },
    {
        'id': 7,
        'name': 'mage_female',
        'title': '魔法师(女)',
        'children': [
            {'id': 0, 'name': 'elementalist', 'title': '知源·元素师', 'open': False},
            {'id': 1, 'name': 'summoner', 'title': '知源·召唤师', 'open': False},
            {'id': 2, 'name': 'battle_mage', 'title': '知源·战斗法师', 'open': False},
            {'id': 3, 'name': 'witch', 'title': '知源·魔道学者', 'open': False},
            {
                'id': 4,
                'name': 'enchantress',
                'title': '知源·小魔女',
                'open': False,
                'options': [{'id': 0, 'name': 'default', 'title': '奶', 'class': 'enchantress'}, {'id': 1, 'name': 'default', 'title': '输出', 'class': 'enchantress_carry'}],
            },
        ],
    },
    {
        'id': 8,
        'name': 'priest_male',
        'title': '圣职者(男)',
        'children': [
            {
                'id': 0,
                'name': 'crusader_male',
                'title': '神启·圣骑士',
                'open': False,
                'options': [{'id': 0, 'name': 'default', 'title': '奶', 'class': 'crusader_male'}, {'id': 1, 'name': 'default', 'title': '审判', 'class': 'crusader_male_carry'}],
            },
            {'id': 1, 'name': 'infighter', 'title': '神启·蓝拳圣使', 'open': False},
            {'id': 2, 'name': 'exorcist', 'title': '神启·驱魔师', 'open': False},
            {'id': 3, 'name': 'avenger', 'title': '神启·复仇者', 'open': False},
            {'id': 4, 'name': 'empty', 'title': ''},
        ],
    },
    {
        'id': 9,
        'name': 'priest_female',
        'title': '圣职者(女)',
        'children': [
            {
                'id': 0,
                'name': 'crusader_female',
                'title': '神启·圣骑士',
                'open': True,
                'class': 'GF.priest_female.crusader_female'
                # 'options': [{'id': 0, 'name': 'default', 'title': '奶', 'class': 'GF.priest_female.crusader_female', "open": True}, {'id': 1, 'name': 'default', 'title': '输出', 'class': 'crusader_female_carry'}],
            },
            {'id': 1, 'name': 'inquistor', 'title': '神启·异端审判者', 'open': False},
            {'id': 2, 'name': 'sorceress', 'title': '神启·巫女', 'open': False},
            {'id': 3, 'name': 'mistress', 'title': '神启·诱魔者', 'open': False},
            {'id': 4, 'name': 'empty', 'title': ''},
        ],
    },
    {
        'id': 10,
        'name': 'thief',
        'title': '暗夜使者',
        'children': [
            {'id': 0, 'name': 'rogue', 'title': '隐夜·刺客', 'open': False},
            {'id': 1, 'name': 'necro', 'title': '隐夜·死灵术士', 'open': False},
            {'id': 2, 'name': 'kunoichi', 'title': '隐夜·忍者', 'open': False},
            {'id': 3, 'name': 'shadow_dancer', 'title': '隐夜·影舞者', 'open': False},
            {'id': 4, 'name': 'empty', 'title': ''},
        ],
    },
    {
        'id': 11,
        'name': 'knight',
        'title': '守护者',
        'children': [
            {'id': 0, 'name': 'elven_knight', 'title': '皓曦·精灵骑士', 'open': False},
            {'id': 1, 'name': 'chaos', 'title': '皓曦·混沌魔灵', 'open': False},
            {'id': 2, 'name': 'paladin', 'title': '皓曦·帕拉丁', 'open': False},
            {'id': 3, 'name': 'dragon_knight', 'title': '皓曦·龙骑士', 'open': False},
            {'id': 4, 'name': 'empty', 'title': ''},
        ],
    },
    {
        'id': 12,
        'name': 'demonic_lancer',
        'title': '魔枪士',
        'children': [
            {'id': 0, 'name': 'vanguard', 'title': '千魂·征战者', 'open': False},
            {'id': 1, 'name': 'skirmisher', 'title': '千魂·决战者', 'open': False},
            {'id': 2, 'name': 'dragoon', 'title': '千魂·狩猎者', 'open': False},
            {'id': 3, 'name': 'impaler', 'title': '千魂·暗枪士', 'open': False},
            {'id': 4, 'name': 'empty', 'title': ''},
        ],
    },
    {
        'id': 13,
        'name': 'gunblader',
        'title': '枪剑士',
        'children': [
            {'id': 0, 'name': 'hitman', 'title': '苍暮·暗刃', 'open': False},
            {'id': 1, 'name': 'agent', 'title': '苍暮·特工', 'open': False},
            {'id': 2, 'name': 'trouble_shooter', 'title': '苍暮·战线佣兵', 'open': False},
            {'id': 3, 'name': 'specialist', 'title': '苍暮·源能专家', 'open': False},
            {'id': 4, 'name': 'empty', 'title': ''},
        ],
    },
    {
        'id': 14,
        'name': 'archer',
        'title': '弓箭手',
        'children': [
            {'id': 0, 'name': 'muse', 'title': '聆风·缪斯', 'open': False},
            {'id': 1, 'name': 'traveler', 'title': '聆风·旅人', 'open': False},
            {'id': 2, 'name': 'hunter', 'title': '聆风·猎人', 'open': False},
            {'id': 3, 'name': 'vigilante', 'title': '聆风·妖护使', 'open': False},
            {'id': 4, 'name': 'empty', 'title': ''},
        ],
    },
    {
        'id': 15,
        'name': 'extra',
        'title': '外传',
        'children': [
            {'id': 0, 'name': 'creator', 'title': '知源·缔造者', 'open': False},
            {'id': 1, 'name': 'dark_knight', 'title': '极诣·黑暗武士', 'open': False},
            {'id': 2, 'name': 'empty', 'title': ''},
            {'id': 3, 'name': 'empty', 'title': ''},
            {'id': 4, 'name': 'empty', 'title': ''},
        ],
    },
]


def get_adv_list():
    temp = deepcopy(adv)
    for parent in temp:
        parent_id = f'{parent["id"]:02}'
        for child in parent['children']:
            child_id = f'{child.get("id", 0):02}'
            if 'options' in child:
                for idx, option in enumerate(child['options']):
                    option['value'] = base64.b64encode(f'{parent_id}{child_id}{idx:02}'.encode()).decode()
                    option.pop('class', None)
            else:
                child['value'] = base64.b64encode(f'{parent_id}{child_id}00'.encode()).decode()
                child.pop('class', None)
    return temp


def get_adv_info(value):
    value = base64.b64decode(value).decode()
    parent_id, child_id, option_id = map(int, (value[:2], value[2:4], value[4:6]))
    parent = next((p for p in adv if p['id'] == parent_id), None)
    if not parent:
        return None
    child = next((c for c in parent['children'] if c.get('id', 0) == child_id), None)
    if not child:
        return None
    if 'options' in child:
        return next((o for o in child['options'] if o.get('id', 0) == option_id), None)
    else:
        return child if option_id == 0 else None
