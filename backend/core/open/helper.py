from openapi.dnfhelper.public import get_main_user_info_by_id
from core.basic.equipment import get_equipment

job_mapping = {
    '极诣·剑魂': 'weapon_master',
    '极诣·鬼泣': 'soul_bender',
    '极诣·狂战士': 'berserker',
    '极诣·阿修罗': 'asura',
    '极诣·剑影': 'ghostblade',
    '极诣·驭剑士': 'sword_master',
    '极诣·暗殿骑士': 'dark_templar',
    '极诣·契魔者': 'demon_slayer',
    '极诣·流浪武士': 'vegabond',
    '极诣·刃影': 'spectre',
    '归元·气功师(男)': 'nenmaster_male',
    '归元·散打(男)': 'striker_male',
    '归元·街霸(男)': 'brawler_male',
    '归元·柔道家(男)': 'grappler_male',
    '归元·气功师(女)': 'nenmaster_female',
    '归元·散打(女)': 'striker_female',
    '归元·街霸(女)': 'brawler_female',
    '归元·柔道家(女)': 'grappler_female',
    '重霄·漫游枪手(男)': 'ranger_male',
    '重霄·枪炮师(男)': 'launcher_male',
    '重霄·机械师(男)': 'mechanic_male',
    '重霄·弹药专家(男)': 'spitfire_male',
    '重霄·合金战士': 'assault',
    '重霄·漫游枪手(女)': 'ranger_female',
    '重霄·枪炮师(女)': 'launcher_female',
    '重霄·机械师(女)': 'mechanic_female',
    '重霄·弹药专家(女)': 'spitfire_female',
    '重霄·协战师': 'paramedic',
    '知源·元素爆破师': 'elemental_bomber',
    '知源·冰结师': 'glacial_master',
    '知源·血法师': 'blood_mage',
    '知源·逐风者': 'swift_master',
    '知源·次元行者': 'dimension_walker',
    '知源·元素师': 'elementalist',
    '知源·召唤师': 'summoner',
    '知源·战斗法师': 'battle_mage',
    '知源·魔道学者': 'witch',
    '知源·小魔女': 'enchantress',
    '光启·光明骑士(男)': 'crusader_male',
    '光启·蓝拳圣使': 'infighter',
    '光启·驱魔师(男)': 'exorcist',
    '光启·惩戒者': 'avenger',
    '光启·光明骑士(女)': 'crusader_female',
    '光启·正义审判者': 'inquistor',
    '光启·驱魔师(女)': 'sorceress',
    '光启·除恶者': 'mistress',
    '隐夜·暗星': 'rogue',
    '隐夜·黑夜术士': 'necro',
    '隐夜·忍者': 'kunoichi',
    '隐夜·影舞者': 'shadow_dancer',
    '皓曦·精灵骑士': 'elven_knight',
    '皓曦·混沌魔灵': 'chaos',
    '皓曦·帕拉丁': 'paladin',
    '皓曦·龙骑士': 'dragon_knight',
    '千魂·征战者': 'vanguard',
    '千魂·决战者': 'skirmisher',
    '千魂·狩猎者': 'dragoon',
    '千魂·暗枪士': 'impaler',
    '苍暮·暗刃': 'hitman',
    '苍暮·特工': 'agent',
    '苍暮·战线佣兵': 'trouble_shooter',
    '苍暮·源能专家': 'specialist',
    '聆风·缪斯': 'muse',
    '聆风·旅人': 'traveler',
    '聆风·猎人': 'hunter',
    '聆风·妖护使': 'vigilante',
    '聆风·奇美拉': 'chimera',
    '知源·缔造者': 'creator',
    '极诣·黑暗武士': 'dark_knight',
}


async def get_user_info_by_id(user_id: str, alter: str):
    # 通过OCR助手获取用户信息
    helper_info = await get_main_user_info_by_id(user_id)
    if helper_info is None:
        return None
    else:
        return trans_to_dcalc_set(helper_info)
        pass


def trans_to_dcalc_set(detail):
    job = job_mapping.get(detail.get('job', ''), '')
    basic = get_equipment('0')
    basicAvatars = basic.funs.get_dress_list([])
    equs = detail.get('equs', [])
    equips = {}
    avatar = {}
    for equ in equs:
        info = {
            'id': '0',
            # 强化
            'reinforce': equ.get('enhance', {}).get('reinforce', 0),
            # 强化类型
            'reinforceType': equ.get('enhance', {}).get('reinforceType', 0),
            # 附魔
            'enchant': 0,
            # 徽章1
            'emblem_0': 0,
            # 徽章2
            'emblem_1': 0,
            # 贴膜
            'fusion': 0,
            # 锻造等级
            'refine': equ.get('enhance', {}).get('refine', 0),
            # 调试等级
            'adaptation': 3,
            # 精度
            'precision': 100,
        }
        # 装备
        dcalcEqu = next((item for item in basic.equs if item.name == equ['name']), None)
        # 贴膜
        if dcalcEqu:
            info['id'] = dcalcEqu.id
        dcalcEquFusion = next((item for item in basic.stones if item.name == equ.get('upgrade', '')), None)
        if dcalcEquFusion:
            info['fusion'] = dcalcEquFusion.id
        info['enchant'] = getEnchatIdByName(equ.get('enchant', ''), equ.get('posName', ''), basic.enchants)
        emblems = [getEmblemIdByName(i.get('detail', ''), i.get('categorize', ''), i.get('rarity', ''), basic.emblems) for i in equ.get('emblems', [])]
        info['emblem_0'] = emblems[0] if len(emblems) > 0 else 0
        info['emblem_1'] = emblems[1] if len(emblems) > 1 else 0
        equips[equ['posName']] = info
    avatars = detail.get('avatars', [])
    for item in avatars:
        info = {
            'id': '',
            'option': '',
            'enchant': '',
            'emblem_0': '',
            'emblem_1': '',
        }
        list = basicAvatars.get(item.get('posName', ''), [])
        if len(list) > 0:
            dcalcAvatar = next((i for i in list if i.get('rarity', '') == item.get('rarity', '')), None)
            if dcalcAvatar:
                info['id'] = dcalcAvatar.get('id', '0')
                info['option'] = item.get('attr', '')
                avatar[item['posName']] = info
        else:
            # TODO: 处理没有找到对应时装的情况 即光环、皮肤、武器装扮
            print(item)
    return {
        'job': job,
        'equips': equips,
        'avatars': avatar,
    }
    # 处理装备
    # 处理时装
    pass


def getEnchatIdByName(name: str, position: str, items: list):
    items = list(filter(lambda x: position in x.get('position', []), items))
    for item in items:
        if '|'.join(sorted(item.get('detail', '').split('|'))) == '|'.join(sorted(name.split('|'))):
            return item.get('id', 0)
    return 0


def getEmblemIdByName(detail: str, categorize: str, rarity: str, items: list):
    if categorize == '白金':
        return detail
    for item in items:
        if item.get('detail', '') == detail and categorize in item.get('categorize', []) and item.get('rarity', '') == rarity:
            return item.get('id', 0)
    return 0
