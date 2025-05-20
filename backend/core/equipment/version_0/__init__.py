from .avatar import get_dress_list,calc_dress_effect
from . import equ
from . import stone
from . import jade
from . import emblem
from . import enchant
from . import sundry
from . import suit

from .register import execture

options = [
    {'id': 1, 'name': '龙战八荒', 'options': ['BUFF OFF', 'BUFF ON', '期望']},
    {'id': 2, 'name': '混沌净化', 'options': ['净化', '堕落']},
    {'id': 3, 'name': '群猎美学', 'options': ['单刷', '组队']},
    {'id': 4, 'name': '魔攻核', 'options': ['普通', '追击']},
    {'id': 5,'name':'传世手杖','options':['BUFF ON', 'BUFF OFF', '期望']}
]

sundryList = {
    'medal_rarity': {'id': 0, 'options': [{'name': f'品质:{i}', 'value': idx} for idx, i in enumerate(['普通', '高级', '稀有', '神器', '传说', '史诗'])]},
    'medal_reinforce': {'id': 1, 'options': [{'name': f'强化 +{i}', 'value': i} for i in range(0, 13)]},
    'medal_gem_0': {'id': 2, 'options': [{'name': f'{i}', 'value': idx} for idx, i in enumerate(['普通', '高级', '稀有', '神器', '传说'])]},
    'medal_gem_1': {'id': 3, 'options': [{'name': f'{i}', 'value': idx} for idx, i in enumerate(['普通', '高级', '稀有', '神器', '传说'])]},
    'medal_gem_2': {'id': 4, 'options': [{'name': f'{i}', 'value': idx} for idx, i in enumerate(['普通', '高级', '稀有', '神器', '传说'])]},
    'medal_gem_3': {'id': 5, 'options': [{'name': f'{i}', 'value': idx} for idx, i in enumerate(['普通', '高级', '稀有', '神器', '传说'])]},
    'adventure': {'id': 6, 'options': [{'name': f'Lv:{i}', 'value': i} for i in range(1, 41)]},
    'marriage_house': {'id': 7, 'options': [{'name': f'{i}', 'value': idx} for idx, i in enumerate(['无', '全属强(1)', '全属强(3)', '全属强(5)|三攻(5)', '全属强(8)|三攻(10|20)'])]},
    'marriage_ring': {'id': 8, 'options': [{'name': f'{i}', 'value': idx} for idx, i in enumerate(['无', '体精(8)', '体精(10)|力智(15)'])]},
    'contract': {'id': 9, 'options': [{'name': f'{i}', 'value': idx} for idx, i in enumerate(['无', '无色契约 三攻(40)'])]},
    'collection_type': {'id': 10, 'options': [{'name': f'{i}', 'value': idx} for idx, i in enumerate(['无', '春节套', '夏日套'])]},
    'collection_num_0': {'id': 11, 'options': [{'name': f'稀有{i}个', 'value': i} for i in range(0, 6)]},
    'collection_num_1': {'id': 12, 'options': [{'name': f'神器{i}个', 'value': i} for i in range(0, 6)]},
    'costume_card': {'id': 13, 'options': [{'name': f'{i}', 'value': idx} for idx, i in enumerate(['无', '四维(3)|三速(1%)'])]},
}

__all__= [get_dress_list, calc_dress_effect, options , execture, sundryList, equ, stone, jade, emblem, enchant, sundry, suit]

