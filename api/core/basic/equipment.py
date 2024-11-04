from copy import deepcopy
import importlib
import json
import os
import sys
from decimal import Decimal
from pyclbr import Function
from typing import Dict, List
from routers.database.db import Session,get_engine,EquData,EntryData,SuitData

try:
    os.chdir(os.path.dirname(sys.argv[0]))
except Exception:
    pass


def parse_to_number_list(info: str):
    return [] if info == "" or info  is None else [int(i) for i in info.split(",")]


def get_eq_info_data(version):
    # equ_info = {}
    # fileName = "./dataFiles/equ-data-{}.json".format(version)
    # try:
    #     with open(fileName, encoding='utf-8') as fp:
    #         equ_info = json.load(fp)
    # except Exception:
    #     with open("./dataFiles/equ-data-3.json", encoding='utf-8') as fp:
    #         equ_info = json.load(fp)
    equ_info = {}
    engine = get_engine(version)
    with Session(bind=engine) as session:
        for equ in session.query(EquData).all():
            equ.可选属性 = parse_to_number_list(equ.可选属性)
            equ.固有属性 = parse_to_number_list(equ.固有属性)
            equ.成长属性 = parse_to_number_list(equ.成长属性)
            equ.特性 = parse_to_number_list(equ.特性)
            equ.suits = parse_to_number_list(equ.suits)
            equ_info[str(equ.id)] = equ.__dict__
            for i in list(filter(lambda x: x.startswith("_"), equ.__dict__.keys())):
                del equ_info[str(equ.id)][i]
    engine.dispose()
    cus = []
    for key in equ_info.keys():
        if (('融合石' not in equ_info[key]["类型"]))and (len(equ_info[key]["可选属性"]) > 0):
            cus.append(key)
    for key in cus:
        equ_info[str(100000+int(key))] = deepcopy(equ_info[key])
        equ_info[str(100000+int(key))]["名称"] += " - 对照"
        # equ_info[str(10000+int(key))]["order"] += 100000
    return equ_info


def get_suit_info_data(version):
    suit_info = []
    engine = get_engine(version)
    with Session(bind=engine) as session:
        for suit in session.query(SuitData).all():
            temp = suit.__dict__
            for i in list(filter(lambda x: x.startswith("_"), suit.__dict__.keys())):
                del temp[i]
            if temp['compatibility']  is None:
                temp['compatibility'] = []
            else:
                temp['compatibility'] = parse_to_number_list(
                    temp['compatibility'])
            suit_info.append(temp)
            pass
    engine.dispose()
    return suit_info


def get_entry_info_data(version):
    # entry_info = {}
    # fileName = "./dataFiles/entry-data-{}.json".format(version)
    # try:
    #     with open(fileName, encoding='utf-8') as fp:
    #         entry_info = json.load(fp)
    # except Exception:
    #     with open("./dataFiles/entry-data-0.json", encoding='utf-8') as fp:
    #         entry_info = json.load(fp)
    entry_info = {}
    engine = get_engine(version)
    with Session(bind=engine) as session:
        for entry in session.query(EntryData).all():
            entry_info[str(entry.id)] = entry.__dict__
            entry_info[str(entry.id)]["props"] = entry.props.split("<br/>")
            entry_info[str(entry.id)]["additional"] = json.loads(entry.additional) if entry.additional != "" and entry.additional is not None else []
            for i in list(filter(lambda x: x.startswith("_"), entry.__dict__.keys())):
                del entry_info[str(entry.id)][i]
            pass
    engine.dispose()
    # if int(version) == 0:
    for item in entry_info:
        props = entry_info[item]['props']
        if len(entry_info[item]['additional']) > 0:
            entry_info[item]["template"] = ("<br/>").join(entry_info[item]["props"])
            entry_info[item]["params"] = entry_info[item]['additional']
            props = ("<br/>").join(entry_info[item]["props"])
            for index,param in enumerate(entry_info[item]['additional'][0]):
                props = props.replace("{"+str(index)+"}",str(param))
            entry_info[item]["props"] = props.split("<br/>")
        else:
            import re
            res = re.findall(r'攻击强化[\s]\+\d+.?\d+%',
                            ("<br/>").join(props).replace(",", ""))

            if len(res) > 0:
                params = []
                template = ("<br/>").join(props).replace(",", "")
                for index in range(0, len(res)):
                    temp = res[index].replace("攻击强化+", "攻击强化 +")
                    params.append(float(re.findall(r'\d+\.?\d*', temp)[0]))
                    template = template.replace(temp, '攻击强化 {'+str(index)+'}')
                entry_info[item]["template"] = template
                entry_info[item]["params"] = params
                entry_info[item]["filter"] = entry_info[item].get("filter", None)

        del entry_info[item]['additional']
    return entry_info


class equipment:
    名称 = ''
    等级 = ''
    品质 = ''
    部位 = ''
    类型 = ''
    力量 = 0
    智力 = 0
    体力 = 0
    精神 = 0
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0
    固有属性 = []
    成长属性 = []
    可选属性 = []
    物理暴击率 = 0
    魔法暴击率 = 0
    神 = False
    id = 0
    suits = ''

    def __init__(self, info={}):
        # 读取json获取装备属性
        self.__dict__.update(info)

        # 计算防具转甲基础
        if self.类型 in ['布甲', '皮甲', '轻甲', '重甲', '板甲']:
            设置防具基础(self)
        if self.部位 == "武器":
            设置武器基础(self)
        if self.类型 in ['首饰', '特殊装备']:
            设置其他基础(self)
    # def __iter__(self):
    #     yield from [getattr(self, i, 0) for i in ('物理攻击力', '魔法攻击力', '独立攻击力', '三攻', '力量', '智力', '力智', '体力', '精神', '体精', '四维', '物理暴击率', '魔法暴击率', '暴击率', '攻击速度', '施放速度', '移动速度', '三速')]


防具基础 = {
    "105-史诗-上衣": (141, 141, 141, 141, 1597, 0),
    "105-史诗-头肩": (132, 132, 132, 132, 1065, 0),
    "105-史诗-下装": (141, 141, 141, 141, 1331, 0),
    "105-史诗-鞋":   (124, 124, 124, 124, 799, 0),
    "105-史诗-腰带": (124, 124, 124, 124, 532, 0),
    "105-神话-上衣": (142, 142, 142, 142, 1637, 0),
    "105-传说-上衣": (140, 140, 140, 140, 1558, 0),
    "105-传说-头肩": (132, 132, 132, 132, 1038, 0),
    "105-传说-下装": (140, 140, 140, 140, 1298, 0),
    "105-传说-鞋":   (124, 124, 124, 124, 779, 0),
    "105-传说-腰带": (124, 124, 124, 124, 519, 0),
    "110-史诗-上衣": (142, 142, 142, 142, 1663, 0),
    "110-史诗-头肩": (134, 134, 134, 134, 1109, 0),
    "110-史诗-下装": (142, 142, 142, 142, 1386, 0),
    "110-史诗-鞋": (125, 125, 125, 125, 832, 0),
    "110-史诗-腰带": (125, 125, 125, 125, 554, 0),
}


武器基础 = {
    "110-史诗-短剑": (0, 88, 0, 0, 1277, 1547, 864),
    "110-史诗-太刀": (88, 133, 0, 0, 1277, 1411, 864),
    "110-史诗-钝器": (133, 0, 0, 0, 1478, 1277, 864),
    "110-史诗-巨剑": (88, 0, 0, 0, 1614, 1210, 864),
    "110-史诗-光剑": (88, 0, 0, 0, 1251, 1210, 864),
    "110-史诗-手套": (0, 88, 0, 0, 1277, 1547, 864),
    "110-史诗-臂铠": (133, 0, 0, 0, 1614, 1210, 864),
    "110-史诗-爪": (88, 44, 0, 0, 1344, 1344, 864),
    "110-史诗-拳套": (88, 0, 0, 0, 1411, 1277, 864),
    "110-史诗-东方棍": (88, 133, 0, 0, 1277, 1344, 864),
    "110-史诗-左轮枪": (88, 0, 0, 0, 1362, 1145, 864),
    "110-史诗-自动手枪": (0, 88, 0, 0, 955, 1400, 864),
    "110-史诗-步枪": (88, 133, 0, 0, 1463, 1273, 864),
    "110-史诗-手炮": (133, 0, 0, 0, 1591, 955, 864),
    "110-史诗-手弩": (88, 88, 0, 0, 1145, 1273, 864),
    "110-史诗-矛": (133, 0, 0, 0, 1614, 1143, 864),
    "110-史诗-棍棒": (120, 120, 0, 0, 1452, 1210, 864),
    "110-史诗-魔杖": (0, 133, 0, 0, 1210, 1478, 864),
    "110-史诗-法杖": (0, 88, 0, 0, 1277, 1614, 864),
    "110-史诗-扫把": (0, 88, 0, 0, 1344, 1478, 864),
    "110-史诗-十字架": (0, 88, 106, 106, 1344, 1277, 864),
    "110-史诗-念珠": (0, 133, 0, 0, 1210, 1547, 864),
    "110-史诗-图腾": (133, 0, 0, 0, 1411, 1210, 864),
    "110-史诗-镰刀": (88, 88, 0, 0, 1277, 1344, 864),
    "110-史诗-战斧": (88, 0, 0, 0, 1614, 1143, 864),
    "110-史诗-匕首": (133, 0, 0, 0, 1283, 1210, 864),
    "110-史诗-双剑": (88, 0, 0, 0, 1474, 1076, 864),
    "110-史诗-手杖": (0, 88, 0, 0, 1196, 1547, 864),
    "110-史诗-苦无": (0, 133, 0, 0, 1133, 1478, 864),
    "110-史诗-长枪": (133, 0, 0, 0, 1411, 1210, 864),
    "110-史诗-战戟": (88, 0, 0, 0, 1614, 1143, 864),
    "110-史诗-光枪": (88, 88, 0, 0, 1277, 1547, 864),
    "110-史诗-暗矛": (88, 133, 0, 0, 1277, 1411, 864),
    "110-史诗-长刀": (88, 88, 0, 0, 1452, 1210, 864),
    "110-史诗-小太刀": (88, 44, 0, 0, 1344, 1344, 864),
    "110-史诗-重剑": (88, 0, 0, 0, 1614, 1210, 864),
    "110-史诗-源力剑": (0, 88, 0, 0, 1277, 1547, 864),
    "110-史诗-神弦弓": (0, 0, 0, 106, 1344, 1277, 864),
    "110-史诗-玄机弓": (88, 88, 0, 0, 1452, 1210, 864),
    "105-史诗-短剑": (0, 85, 0, 0, 1222, 1480, 818),
    "105-史诗-太刀": (85, 128, 0, 0, 1222, 1351, 818),
    "105-史诗-钝器": (128, 0, 0, 0, 1416, 1222, 818),
    "105-史诗-巨剑": (85, 0, 0, 0, 1544, 1158, 818),
    "105-史诗-光剑": (85, 0, 0, 0, 1197, 1158, 818),
    "105-史诗-手套": (0, 85, 0, 0, 1222, 1480, 818),
    "105-史诗-臂铠": (128, 0, 0, 0, 1544, 1158, 818),
    "105-史诗-爪": (85, 43, 0, 0, 1287, 1287, 818),
    "105-史诗-拳套": (85, 0, 0, 0, 1351, 1222, 818),
    "105-史诗-东方棍": (85, 128, 0, 0, 1222, 1287, 818),
    "105-史诗-左轮枪": (85, 0, 0, 0, 1300, 1093, 818),
    "105-史诗-自动手枪": (0, 85, 0, 0, 911, 1337, 818),
    "105-史诗-步枪": (85, 128, 0, 0, 1397, 1214, 818),
    "105-史诗-手炮": (128, 0, 0, 0, 1518, 911, 818),
    "105-史诗-手弩": (85, 85, 0, 0, 1093, 1214, 818),
    "105-史诗-矛": (128, 0, 0, 0, 1544, 1093, 818),
    "105-史诗-棍棒": (114, 114, 0, 0, 1389, 1158, 818),
    "105-史诗-魔杖": (0, 128, 0, 0, 1158, 1416, 818),
    "105-史诗-法杖": (0, 85, 0, 0, 1222, 1544, 818),
    "105-史诗-扫把": (0, 85, 0, 0, 1287, 1416, 818),
    "105-史诗-十字架": (0, 85, 101, 101, 1287, 1222, 818),
    "105-史诗-念珠": (0, 128, 0, 0, 1158, 1480, 818),
    "105-史诗-图腾": (128, 0, 0, 0, 1351, 1158, 818),
    "105-史诗-镰刀": (85, 85, 0, 0, 1222, 1287, 818),
    "105-史诗-战斧": (85, 0, 0, 0, 1544, 1093, 818),
    "105-史诗-匕首": (128, 0, 0, 0, 1224, 1158, 818),
    "105-史诗-双剑": (85, 0, 0, 0, 1408, 1030, 818),
    "105-史诗-手杖": (0, 85, 0, 0, 1141, 1480, 818),
    "105-史诗-苦无": (0, 128, 0, 0, 1081, 1416, 818),
    "105-史诗-长枪": (128, 0, 0, 0, 1351, 1158, 818),
    "105-史诗-战戟": (85, 0, 0, 0, 1544, 1093, 818),
    "105-史诗-光枪": (85, 85, 0, 0, 1222, 1480, 818),
    "105-史诗-暗矛": (85, 128, 0, 0, 1222, 1351, 818),
    "105-史诗-长刀": (85, 85, 0, 0, 1389, 1158, 818),
    "105-史诗-小太刀": (85, 43, 0, 0, 1287, 1287, 818),
    "105-史诗-重剑": (85, 0, 0, 0, 1544, 1158, 818),
    "105-史诗-源力剑": (0, 85, 0, 0, 1222, 1480, 818),
    "105-史诗-神弦弓": (0, 85, 0, 101, 1287, 1222, 818),
    "105-史诗-玄机弓": (85, 85, 0, 0, 1389, 1158, 818),
    # "105-史诗-神弦弓": (0, 0, 0, 101, 1287, 1222, 818),
    # "105-史诗-玄机弓": (0, 0, 0, 101, 1287, 1222, 818),
    "105-传说-短剑": (0, 81, 0, 0, 1167, 1412, 766),
    "105-传说-太刀": (81, 0, 0, 0, 1167, 1289, 766),
    "105-传说-钝器": (122, 0, 0, 0, 1351, 1167, 766),
    "105-传说-巨剑": (81, 122, 0, 0, 1474, 1106, 766),
    "105-传说-光剑": (81, 0, 0, 0, 1142, 1106, 766),
    "105-传说-手套": (0, 81, 0, 0, 1167, 1412, 766),
    "105-传说-臂铠": (122, 0, 0, 0, 1474, 1106, 766),
    "105-传说-爪": (81, 41, 0, 0, 1229, 1229, 766),
    "105-传说-拳套": (81, 0, 0, 0, 1289, 1167, 766),
    "105-传说-东方棍": (81, 122, 0, 0, 1167, 1229, 766),
    "105-传说-左轮枪": (81, 0, 0, 0, 1239, 1042, 766),
    "105-传说-自动手枪": (0, 81, 0, 0, 868, 1274, 766),
    "105-传说-步枪": (81, 122, 0, 0, 1331, 1157, 766),
    "105-传说-手炮": (122, 0, 0, 0, 1448, 868, 766),
    "105-传说-手弩": (81, 81, 0, 0, 1042, 1157, 766),
    "105-传说-矛": (110, 110, 0, 0, 1327, 1106, 766),
    "105-传说-棍棒": (122, 0, 0, 0, 1474, 1044, 766),
    "105-传说-魔杖": (0, 122, 0, 0, 1106, 1351, 766),
    "105-传说-法杖": (0, 81, 0, 0, 1167, 1474, 766),
    "105-传说-扫把": (0, 81, 0, 0, 1229, 1351, 766),
    "105-传说-十字架": (0, 81, 99, 99, 1229, 1167, 766),
    "105-传说-念珠": (0, 122, 0, 0, 1106, 1412, 766),
    "105-传说-图腾": (122, 0, 0, 0, 1289, 1106, 766),
    "105-传说-镰刀": (81, 81, 0, 0, 1167, 1229, 766),
    "105-传说-战斧": (81, 0, 0, 0, 1474, 1044, 766),
    "105-传说-匕首": (122, 0, 0, 0, 1167, 1106, 766),
    "105-传说-双剑": (81, 0, 0, 0, 1343, 982, 766),
    "105-传说-手杖": (0, 81, 0, 0, 1087, 1412, 766),
    "105-传说-苦无": (0, 122, 0, 0, 1030, 1351, 766),
    "105-传说-长枪": (122, 0, 0, 0, 1289, 1106, 766),
    "105-传说-战戟": (81, 0, 0, 0, 1474, 1044, 766),
    "105-传说-光枪": (81, 81, 0, 0, 1167, 1412, 766),
    "105-传说-暗矛": (81, 122, 0, 0, 1167, 1289, 766),
    "105-传说-长刀": (81, 81, 0, 0, 1327, 1106, 766),
    "105-传说-小太刀": (81, 41, 0, 0, 1229, 1229, 766),
    "105-传说-重剑": (81, 0, 0, 0, 1474, 1106, 766),
    "105-传说-源力剑": (0, 81, 0, 0, 1167, 1412, 766),
    "105-传说-玄机弓": (0, 81, 0, 0, 1327, 1106, 766),
    "110-史诗-强攻弩": (88, 0, 0, 0, 1614, 1210, 864),
    "105-史诗-强攻弩": (85, 0, 0, 0, 1544, 1158, 818),
    "105-传说-强攻弩": (81, 0, 0, 0, 1474, 1106, 766),
    "110-史诗-妖影弓": (88, 88, 0, 0, 1277, 1344, 864),
    "105-史诗-妖影弓": (85, 85, 0, 0, 1222, 1287, 818),
    "105-传说-妖影弓": (81, 81, 0, 0, 1167, 1229, 766)
}

其他基础 = {
    "110-史诗-项链": (100, 151, 100, 227, 0, 11159),
    "110-史诗-戒指": (176, 176, 100, 100, 0, 4470),
    "110-史诗-手镯": (151, 100, 227, 100, 0, 6706),
    "110-史诗-辅助装备": (150, 150, 150, 150, 0, 0),
    "110-史诗-魔法石": (175, 175, 175, 175, 0, 0),
    "110-史诗-耳环": (175, 175, 175, 175, 0, 0),
    "105-史诗-项链": (100, 150, 100, 222, 0, 10736),
    "105-史诗-戒指": (173, 173, 100, 100, 0, 4294),
    "105-史诗-手镯": (150, 100, 222, 100, 0, 6600),
    "105-史诗-辅助装备": (149, 149, 149, 149, 0, 0),
    "105-史诗-魔法石": (172, 172, 172, 172, 0, 0),
    "105-史诗-耳环": (172, 172, 172, 172, 0, 0)
}


def 设置其他基础(装备):

    b = 其他基础.get('{}-{}-{}'.format(110 if 装备.神 else 装备.等级, 装备.品质, 装备.部位),
                 (0, 0, 0, 0, 0))

    attr = ['力量', '智力', '体力', '精神']
    for i in range(len(attr)):
        if (b[i] != 0):
            setattr(装备, attr[i], round((b[i]) * Decimal(1.0)))
    pass


def 设置武器基础(装备):
    # 装备.力量 = {}
    # 装备.智力 = {}
    # 装备.体力 = {}
    # 装备.精神 = {}
    # 装备.物理攻击力 = {}
    # 装备.魔法攻击力 = {}
    # 装备.独立攻击力 = {}

    b = 武器基础.get('{}-{}-{}'.format(110 if 装备.神 else 装备.等级, 装备.品质, 装备.类型),
                 (0, 0, 0, 0, 0, 0, 0, 0))

    attr = ['力量', '智力', '体力', '精神', '物理攻击力', '魔法攻击力', '独立攻击力']
    for i in range(len(attr)):
        if (b[i] != 0):
            setattr(装备, attr[i], round((b[i]) * Decimal(1.0)))


def 设置防具基础(装备):
    b = 防具基础.get('{}-{}-{}'.format(110 if 装备.神 else 装备.等级,
                 装备.品质, 装备.部位), (0, 0, 0, 0))
    attr = ['力量', '智力', '体力', '精神']
    for j in range(len(attr)):
        setattr(装备, attr[j], round((b[j]) * Decimal(1.0)))


# 词条计算优先级，默认为100，特殊需求手动设置优先级
priority = {
    # 蓝拳CP-无色消耗
    691: 0,
    # 锁血上限
    1248: 0, 1438: 0, 868: 0.5, 935: 0,
    1620: 0,
    # 无色结算顺序
    20067: 2,
    20069: 2,
    1147: 1,
    878: 998,
    1102: 999,
    1119: 1000,
    1120: 1000,
    1573: 1000,
    1589: 1000,
    1598: 1000,
    1609: 1000,
    1611: 1000,
    1614: 1000,
    1670: 1000,
    1692: 1000,
    # MP结算顺序
    1183: 998,
    1736: 998,
    988: 999,
    316: 998,
    1588: 998,
    1662: 998,
    20029: 998,
    20030: 998,
    20022: 998,
    # 属强结算
    1275: 1999, 1034: 1999, 1035: 1999, 1036: 1999, 1037: 1999,  975: 3000, 976: 1999.5, 1252: 3001, 1250: 3002, 1251: 3002, 1430: 3002, 1458: 3002, 235: 3000, 1689: 3000, 20045: 3000,
    # 异常赋予结算顺序
    190: 1, 799: 1, 810: 1, 916: 1, 900: 1, 968: 1, 977: 1, 1228: 1, 1192: 1, 1184: 1, 1333: 1, 1334: 1, 1335: 1, 1337: 1, 1338: 1, 1315: 1, 1300: 1, 1310: 1, 598: 1, 873: 1, 995: 1, 996: 1, 952: 1, 940: 1, 942: 1, 943: 1, 793: 1, 794: 1, 795: 1, 796: 1, 797: 1, 1123: 1, 1071: 1, 1072: 1, 1073: 1, 1074: 1, 59: 1, 60: 1, 61: 1, 62: 1, 63: 1, 64: 1, 65: 1, 66: 1, 67: 1, 68: 1, 69: 1, 70: 1, 71: 1, 177: 1, 178: 1, 179: 1, 180: 1, 1213: 2, 1207: 2, 1011: 1, 919: 2, 920: 1, 1219: 1, 924: 1, 1053: 1, 892: 1, 1197: 1, 842: 1, 839: 1, 1210: 3, 1276: 101, 1294: 1, 1340: 3, 1341: 1, 1342: 2, 1356: 1, 1357: 1, 1358: 1, 1343: 3, 966: 3, 1363: 1, 1364: 1, 1365: 1, 1366: 1, 1221: 2, 992: 3,
    1273: 1002, 1269: 4002, 1431: 4002, 1432: 4002, 1459: 4002, 1460: 4002, 1246: 4003, 198: 3000, 199: 3000, 203: 1, 204: 3000, 205: 3000, 1605: 4003, 1706: 3000, 1618: 4003, 1751: 3000, 1306: 3000, 20003: 4003,
    # 睡眠结算顺序
    934: 1, 1272: 1, 1271: 2004, 835: 2000, 305: 2000, 1746: 2000, 1591: 2000, 1592: 2000,
    # CD耳环
    991: 1000,
    # 属性抗性
    1297: 1999, 1316: 2000, 1317: 2000, 1239: 2000, 1253: 2000, 1148: 2000, 1387: 2000, 1256: 2000, 1257: 2000, 1012: 2000, 1013: 1999, 1014: 1999, 1015: 1999, 1016: 1999, 1002: 2000, 1028: 2000, 1029: 2000, 1030: 2000, 1031: 2000, 182: 3500, 342: 2000, 344: 3500, 350: 3500, 356: 3500, 301: 2000, 302: 2000, 303: 2000, 304: 2000, 352: 2000, 353: 2000, 354: 2000, 355: 2000, 1699: 2000, 1688: 2000,
    851: 2000, 846: 2000, 844: 2000, 849: 2000, 1022: 2000, 1385: 2000, 1386: 2000,
    # 睡眠
    1132: 2000, 265: 2000, 351: 2000, 20011: 20000,
    1566: 0, 1558: 3002, 1491: 1, 1492: 1, 1493: 1, 1494: 1, 1559: 4002, 1560: 4002, 1515: 2000, 1513: 2000, 1514: 2000,
     1637: 2001,
    # TP
    1451: 2000,
    1574: 2001, 1680: 2001
}


class equipment_list():
    def __init__(self, version: str) -> None:
        self.version = version
        self.info = get_eq_info_data(version)
        self.entry_info = get_entry_info_data(version)
        self.suit_info = get_suit_info_data(version)
        self.parts = set()
        self.load_equ()
        self.info_sj = deepcopy(self.info)
        self.load_equ_sj()

    def load_equ(self) -> None:
        self.equ_list = {}
        self.equ_id = {}
        self.equ_tuple = ()
        self.equ_id_tuple = ()
        for k in self.info.keys():
            temp = equipment(self.info[k])
            i = int(k)
            self.equ_list[i] = temp
            self.equ_id[temp.名称] = i
            self.equ_tuple += (temp, )
            self.equ_id_tuple += (i, )
            self.parts.add(temp.部位)

    def load_equ_sj(self) -> None:
        self.equ_list_sj = {}
        self.equ_id_sj = {}
        self.equ_tuple_sj = ()
        self.equ_id_tuple_sj = ()
        for k in self.info_sj.keys():
            # 特殊处理，游戏中取的110装备基础，增幅等按照105装备等级计算
            # if self.info_sj[k]["等级"] == 105 and self.info_sj[k]["品质"] == "史诗":
            #     self.info_sj[k]["等级"] = 110
            if self.info_sj[k]["品质"] == "史诗":
                self.info_sj[k]["神"] = True
            info = self.info_sj[k]
            temp = equipment(info)
            attr = ['力量', '智力', '体力', '精神', '物理攻击力', '魔法攻击力', '独立攻击力']
            for i in attr:
                self.info_sj[k][i] = getattr(temp, i)
            i = int(k)
            self.equ_list_sj[i] = temp
            self.equ_id_sj[temp.名称] = i
            self.equ_tuple_sj += (temp, )
            self.equ_id_tuple_sj += (i, )
            self.parts.add(temp.部位)

    def get_json(self, i):
        temp = self.info[str(i)]
        return {
            "id": int(i),
            "name": temp["名称"],
            "icon": temp["icon"],
            "part": temp["部位"],
            'type': temp['类型'],
            "stable": temp["固有属性"],
            "alternative": temp["可选属性"] if "可选属性" in temp else [],
            "order":  temp["order"] if "order" in temp else 0,
            "features": temp["特性"] if "特性" in temp else [],
            "rarity": temp["品质"]
        }

    def get_equ_by_id(self, id, sj=False) -> equipment:
        if sj:
            return self.equ_list_sj.get(int(id), equipment())
        else:
            return self.equ_list.get(int(id), equipment())

    def get_equ_by_name(self, name, sj=False) -> equipment:
        return self.get_equ_by_id(self.equ_id.get(name, 0), sj)

    def get_id_by_name(self, name) -> int:
        return self.equ_id.get(name, 0)

    def get_equ_list(self) -> List[equipment]:
        return self.equ_tuple

    def get_equ_id_list(self) -> List[int]:
        return self.equ_id_tuple

    def get_entry_atk_by_id(self, id) -> int:
        return self.entry_info.get(str(id), {}).get('attack', 0)

    def get_entry_buff_by_id(self, id) -> int:
        return self.entry_info.get(str(id), {}).get('buff', 0)

    def get_entry_params_by_id(self, id) -> int:
        return self.entry_info.get(str(id), {}).get('params', [])

    def get_entry_template_by_id(self, id) -> int:
        return self.entry_info.get(str(id), {}).get('template', None)

    def get_damagelist_by_idlist(self, idlist, customize: Dict[str, List[int]] = {}, fusion_list=[], merge: Dict[str, List[int]] = {}) -> List[tuple]:
        damagelist = []  # (部位, 序号, 基础伤害,类型,index)
        # 1 有成长 -1 无成长
        # 序号说明
        # 0~9 成长属性
        # 10~19 固定属性
        # 20~29 贴膜属性
        # 30~39 词条融合
        for id in idlist:
            i = self.get_equ_by_id(id)
            temp = []
            if len(i.可选属性) > 0:
                temp = customize.get(str(id), [])
            num = 0
            for k in i.成长属性 + temp:
                damagelist.append((
                    i.部位,
                    num,
                    self.get_entry_atk_by_id(k),
                    self.get_entry_buff_by_id(k),
                    self.get_entry_params_by_id(k),
                    1,
                    k
                )),
                num += 1
                pass
            if i.部位 == "武器":
                num = 30
                for j in merge:
                    damagelist.append((
                        '武器',
                        num,
                        self.get_entry_atk_by_id(j),
                        self.get_entry_buff_by_id(j),
                        self.get_entry_params_by_id(j),
                        -1,
                        j
                    ))
                    num += 1
        for id in fusion_list:
            i = self.get_equ_by_id(id)
            temp = []
            if len(i.可选属性) > 0:
                temp = list(filter(lambda x:x>0,customize.get(str(id), [])))
            num = 20
            for k in i.固有属性 + temp:
                damagelist.append((
                    i.部位,
                    num,
                    self.get_entry_atk_by_id(k),
                    self.get_entry_buff_by_id(k),
                    self.get_entry_params_by_id(k),
                    -1,
                    k
                ))
                num += 1
        return damagelist

    def get_fusion_by_idlist(self, idlist) -> List[tuple]:
        damagelist = []  # (部位, 序号, 基础伤害)
        for id in idlist:
            i = self.get_equ_by_id(id)
            num = 0
            for k in i.固有属性:
                damagelist.append((
                    i.部位,
                    num,
                    self.get_entry_atk_by_id(k),
                    self.get_entry_buff_by_id(k)))
                num += 1
                pass
        return damagelist

    def set_func_chose(self, choseinfo) -> None:
        try:
            entry = importlib.import_module(
                "core.equipment.entry_{}".format(self.version))
        except Exception:
            entry = importlib.import_module("core.equipment.entry_0")
        variable_set = entry.variable_set
        for i in choseinfo.keys():
            id = int(i)
            if id >= 20000 and id in variable_set.keys():  # 额外选项，参数设置
                try:
                    variable_set[id](choseinfo[i])
                except Exception:
                    pass
            # else:
            #    id 错误

    def get_func_by_id(self, id) -> Function:
        try:
            entry = importlib.import_module(
                "core.equipment.entry_{}".format(self.version))
        except Exception:
            entry = importlib.import_module("core.equipment.entry_0")
        entry_func_list = entry.entry_func_list
        func_list = entry_func_list.get(int(id), entry_func_list[0])
        return func_list

    def get_func_list_by_idlist(self, char) -> List[Function]:
        temp = []
        for id in char.装备栏:
            i = self.get_equ_by_id(id)
            cus = []
            if len(i.可选属性) > 0:
                cus = char.自定义词条.get(str(id), [])
            index = 0
            for k in i.成长属性 + cus:
                temp.append((k, i.部位, index, 1,id,0))  # 词条id 部位 部位序号(用于获取成长词条等级)
                index += 1
            index = 30
            mer = char.武器融合.get(str(id), [])
            for k in mer:
                temp.append((k, i.部位, index, -1,id,0))
                index += 1
            index = 10
            for k in i.固有属性:
                temp.append((k, i.部位, index, -1,id,0))  # 词条id 部位 部位序号(非成长词条无序号)
                index += 1
        for id in char.融合列表:
            i = self.get_equ_by_id(id)
            index = 20
            cus = []
            if len(i.可选属性) > 0:
                cus = list(filter(lambda x:x>0,char.自定义词条.get(str(id), [])))
            for index2,k in enumerate(i.固有属性 + cus):
                temp.append((k, i.部位, index, -3,id,index2))  # 词条id 部位 部位序号(非成长词条无序号)
                index += 1
        for id in char.特性列表:
            # 类型 -2 特性
            if id  is not None and int(id) >= 20000:
                temp.append((int(id), '', -1, -2,id,0))
        for id in char.suits:
            if id  is not None and int(id) > 30000:
                temp.append((id, '', -1, -1,id,0))
            pass
        # 词条优先级排序
        temp.sort(key=(lambda x: priority.get(x[0], 100)))
        funclist = []
        for k, part, index, type,id,positon in temp:
            funclist.append((
                self.get_func_by_id(int(k)),
                part,
                index,
                k,
                type,
                id,
                positon
                ))
        return funclist

    def get_chose_set_info(self) -> List[tuple]:
        try:
            entry = importlib.import_module(
                "core.equipment.entry_{}".format(self.version))
        except Exception:
            entry = importlib.import_module("core.equipment.entry_0")
        entry_chose = entry.entry_chose
        info = []
        entry_chose.sort()
        # for i in entry_func_list.keys():
        #     temp = entry_func_list[i]
        # if len(temp) > 1:
        #     ctext = []
        #     for k in temp:
        #         ctext.append(k(text=True))
        #     info.append((i, ctext))
        return info + entry_chose

    def get_chose_set(self, mode=0, alter="") -> List[Dict]:
        try:
            entry = importlib.import_module(
                "core.equipment.entry_{}".format(self.version))
        except Exception:
            entry = importlib.import_module("core.equipment.entry_0")
        multi_select = entry.multi_select
        if mode == 1:
            setinfo = {}
            defaule_set = {
                "20000": [75],
                "20042": [0],
                "20074": [0],
                "20113": [16],
                "20165": [1],
                "20183": [1],
                "20189": [0],
                "20194": [0],
                "20216": [0],
                "20253": [0],
                "20351": [0, 2, 3, 6, 8],
                "20813": [0],
                "20814": [0],
                "20840": [22],
                "21050": [0],
                "21127": [0],
                "21261": [0],
                "31283": [0, 2],
                "31286": [3],
                "31287": [3],
                "31288": [3],
                "31289": [4],
                "31292": [30],
                "31334": [5],
                "20037": [5],
                "31465": [0],
                "20990": [6],
                "20948": [0],
                "31666": [10],
                "30223": [0]
            }
            for i in self.get_chose_set_info():
                if i[2] == "" or i[2] in alter:
                    setinfo[i[0]] = defaule_set.get(str(i[0]), [0])
        else:
            setinfo = []
            for i in self.get_chose_set_info():
                if i[2] == "" or i[2] in alter:
                    setinfo.append({
                        "id": i[0],
                        "selectList": i[1],
                        "multi-select": multi_select.get(i[0], True)
                    })
        return setinfo

    def get_asrahan(self):
        try:
            entry = importlib.import_module(
                "core.equipment.entry_{}".format(self.version))
        except Exception:
            entry = importlib.import_module("core.equipment.entry_0")
        return entry.asrahan_effect

    def get_funs_info(self, type, char):
        try:
            entry = importlib.import_module(
                "core.equipment.entry_{}".format(self.version))
        except Exception:
            entry = importlib.import_module("core.equipment.entry_0")
        return entry.get_info(type, char)


def get_global_data(name="", version="0", defa=None):
    try:
        entry = importlib.import_module(
            "core.equipment.entry_{}.params".format(version))
    except Exception:
        entry = importlib.import_module("core.equipment.entry_0.params")
    if hasattr(entry, name):
        attr = getattr(entry, name)
        return attr() if attr.__class__.__name__ == "function" else attr
    else:
        return defa

    # def set_equ_customize(self, customize):
    #     for key in customize.keys():
    #         self.get_equ_by_id(key).成长属性 = customize[key]
    #         print(self.get_equ_by_id(key).成长属性,customize[key])


global equ0
equ0 = equipment_list("0")
# equ1 = equipment_list("1")

# global equ1
# equ1 = equipment_list("1")


def get_equ(version="0"):
    if version  is None or version == "":
        version = "0"
    try:
        temp = eval("equ{}".format(version))
    except Exception:
        temp = equ0
    return temp


def reload_equ():
    global equ0
    equ0 = equipment_list("0")
