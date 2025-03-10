from database.models import Session, EquData, SuitData
from database.connect import get_db_engine as get_engine
from functools import cache


def parse_to_number_list(info: str, default: list[float] = [0]) -> list[float]:
    return default if not info else [float(i) for i in info.split(',')]


class Equ:
    id: str
    name: str
    rarity: str
    itemType: str
    itemDetailType: str
    Point: list[float] | float
    categorize: str
    imageUrl: str
    detail: str
    bufferDetail: str
    STR: list[float] | float
    INT: list[float] | float
    Vitality: list[float] | float
    Spirit: list[float] | float
    AtkP: list[float] | float
    AtkM: list[float] | float
    AtkI: list[float] | float
    SkillAttack: list[float] | float
    Attack: list[float] | float
    Buffer: list[float] | float
    max_adaptation: int

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def adapt(self, adaptation: int = 0):
        """调适

        Args:
            adaptation (int): 调适等级
        """
        temp = self.__dict__.copy()
        keys = [key for key in EquData.__dict__.keys() if key[0].isupper()]
        for attr in keys:
            value = getattr(self, attr)
            temp[attr] = value[min(adaptation, len(value) - 1)] if isinstance(value, list) else value
        return Equ(**temp)


class Suit:
    id: int
    suitId: int
    suitName: str
    rarity: str
    name: str
    point: int
    level: int
    count: int
    SkillAttack: float
    Attack: float

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class Equipments:
    def __init__(self, version='0'):
        self.version = version
        self.engine = get_engine(version)
        self.equs: list[Equ] = []
        self.equ_dict: dict[str, Equ] = {}
        self.suits: list[Suit] = []
        self.suit_dict: dict[str, Suit] = {}
        self.init_equs()
        self.init_suits()
        self.engine.dispose()

    def init_equs(self):
        """从数据库中获取所有装备信息"""
        with Session(self.engine) as session:
            db_list = session.query(EquData).all()
        keys = [key for key in EquData.__dict__.keys() if key[0].isupper()] + ['suit']
        for item in db_list:
            max_adaptation = 0
            item.id = str(item.id)
            for attr in keys:
                value = parse_to_number_list(getattr(item, attr))
                max_adaptation = max(max_adaptation, len(value) - 1)
                setattr(item, attr, value)
            equ_dict = {k: v for k, v in item.__dict__.items() if not k.startswith('_')}
            equ_dict['max_adaptation'] = max_adaptation
            equ = Equ(**equ_dict)
            self.equs.append(equ)
            self.equ_dict[equ.id] = equ

    def init_suits(self):
        """从数据库中获取所有套装信息"""
        with Session(self.engine) as session:
            db_list = session.query(SuitData).all()
        for item in db_list:
            suit = Suit(**{k: v for k, v in item.__dict__.items() if not k.startswith('_')})
            self.suits.append(suit)
            self.suit_dict.setdefault(str(suit.suitId), []).append(suit)
        pass

    def get_suit_info(self, suitId: str | int, point: int = 0, count: int = 0) -> list[Suit]:
        """根据套装点数返回对应适用的套装属性\n
        新套装只需要传入suitID和point即可，count默认为0\n
        老套装需要传入suitID和count即可，point默认为0
        """
        # 先筛选出点数小于等于point和数量小于等于count的套装
        suits: list[Suit] = [suit for suit in self.suit_dict[str(suitId)] if suit.point <= point and suit.count <= count]
        result: dict[int, Suit] = {}
        # 取每种count套装中点数最高的
        for suit in suits:
            if suit.count not in result or suit.point > result[suit.count].point:
                result[suit.count] = suit
        return list(result.values())



@cache
def get_equipment(version: str = '0') -> Equipments:
    # print('加载装备信息')
    return Equipments(version)
