# sundry_list = ['medal_rarity', 'medal_rarity', 'medal_reinforce', 'medal_gem_0', 'medal_gem_1', 'medal_gem_2', 'medal_gem_3', 'adventure', 'marriage_house', 'marriage_ring', 'contract', 'collection_type', 'collection_num_0', 'collection_num_1', 'costume_card']

from core.abstract.character import CharacterProperty
from .register import register

@register
def sundry_0(char: CharacterProperty, *args):
    '''勋章'''
    # 勋章基础 四维 48 三攻 30
    char.SetStatus(四维=48, 三攻=30)
    # 勋章品质
    # 攻击强化 BUFF量 名望
    medal_quality = [(1035, 125, 235), (2045, 249, 315), (3799, 461, 415), (5960, 724, 509), (8532, 1035, 606), (11688, 1418, 708)]
    quality = medal_quality[args[0]]
    char.SetStatus(攻击强化=quality[0]*0.1, 增益量=quality[1])
    # 勋章强化
    medal_lv = [(0, 0, 0), (390, 47, 24), (779, 95, 47), (1169, 142, 71), (1558, 189, 94), (1948, 236, 118), (2337, 284, 142), (2727, 331, 165), (3117, 378, 189), (3506, 425, 212), (3896, 473, 236), (4285, 520, 259), (4675, 567, 283)]
    lv = medal_lv[args[1]]
    char.SetStatus(攻击强化=lv[0]*0.1, 增益量=lv[1])
    # 宝石 基础 三速 3% 所有属强 7
    char.SetStatus(三速=0.03, 全属强=7)
    medal_gems_quality = [(224, 27, 46), (403, 49, 58), (701, 85, 72),(1140, 138, 88), (1753, 212, 106)]
    for i in args[2]:
        gems_quality = medal_gems_quality[i]
        char.SetStatus(攻击强化=gems_quality[0]*0.1, 增益量=gems_quality[1])

@register
def sundry_6(char: CharacterProperty, *args):
    '''冒险团'''
    lv = args[0] - 1
    values = [100,110,125,140,150,160,170,180,190,200,210,220,220,220,220,230,230,240,240,250,250,250,250,250,260,260,260,260,260,270,270,270,270,270,280,280,280,280,280,290]
    char.SetStatus(四维=values[lv])

@register
def sundry_7(char: CharacterProperty, *args):
    '''
    婚房婚戒
    婚戒属强不享受辟邪玉加成
    '''
    # 婚戒
    if args[0] == 1:
        char.SetStatus(全属强=1)
    elif args[0] == 2:
        char.SetStatus(全属强=3)
    elif args[0] == 3:
        char.SetStatus(全属强=5, 三攻=5)
    elif args[0] == 4:
        char.SetStatus(全属强=8, 物攻=10, 魔攻=10, 独立=20)
    # 婚房
    if args[1] == 1:
        char.SetStatus(体精=8)
    elif args[1] == 2:
        char.SetStatus(体精=10, 力智=15)

@register
def sundry_9(char: CharacterProperty, *args):
    '''契约'''
    if args[0] == 1:
        char.SetStatus(三攻=40)

@register
def sundry_10(char: CharacterProperty, *args):
    '''收集箱'''
    per_0 = 0
    per_1 = 0
    per_2 = 0
    if args[0] == 1:
      per_0 = 15
      per_1 = 15
      per_2 = 3
    elif args[0] == 2:
      per_0 = 10
      per_1 = 10
      per_2 = 2
    xy = 0
    sq = 0
    try:
        xy = args[1]
    except Exception:
        pass
    try:
        sq = args[2]
    except Exception:
        pass
    char.SetStatus(四维=sq*per_0, 三攻=xy*per_1)
    char.AddElementDB('火',sq*per_2)
    char.AddElementDB('冰',sq*per_2)
    char.AddElementDB('光',sq*per_2)
    char.AddElementDB('暗',sq*per_2)

@register
def sundry_13(char: CharacterProperty, *args):
    if args[0] == 1:
        char.SetStatus(三速=0.01,四维=3)
