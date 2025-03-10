import enum


class CharacterInfo(enum.Enum):
    def __init__(self, name, icon, func) -> None:
        self._name = name
        self._icon = icon
        self._func = func

    @property
    def name(self):
        return self._name

    @property
    def icon(self):
        return self._icon

    def value(self, value):
        return self._func(value)

    STR = '力量', '/ui/UI_ProfileIcon_002.png', lambda x: round(x, 0)
    """力量"""

    INT = '智力', '/ui/UI_ProfileIcon_003.png', lambda x: round(x, 0)
    """智力"""

    AtkP = '物理攻击力', '/ui/UI_ProfileIcon_006.png', lambda x: round(x, 0)
    """物理攻击力"""

    AtkM = '魔法攻击力', '/ui/UI_ProfileIcon_007.png', lambda x: round(x, 0)
    """魔法攻击力"""

    AtkI = '独立攻击力', '/ui/UI_ProfileIcon_008.png', lambda x: round(x, 0)
    """独立攻击力"""

    ElementA: dict[str, float]
    # """属性攻击"""

    ElementDB0 = '火属性强化', '/ui/UI_ProfileIcon_022.png', lambda x: round(x, 0)

    ElementR0 = '火属性抗性', '/ui/UI_ProfileIcon_023.png', lambda x: round(x, 0)

    ElementDB1 = '冰属性强化', '/ui/UI_ProfileIcon_024.png', lambda x: round(x, 0)

    ElementR1 = '冰属性抗性', '/ui/UI_ProfileIcon_025.png', lambda x: round(x, 0)

    ElementDB2 = '光属性强化', '/ui/UI_ProfileIcon_026.png', lambda x: round(x, 0)

    ElementR2 = '光属性抗性', '/ui/UI_ProfileIcon_027.png', lambda x: round(x, 0)

    ElementDB3 = '暗属性强化', '/ui/UI_ProfileIcon_028.png', lambda x: round(x, 0)

    ElementR3 = '暗属性抗性', '/ui/UI_ProfileIcon_029.png', lambda x: round(x, 0)

    CriticalP = '物理暴击', '/ui/UI_ProfileIcon_011.png', lambda x: f'{format(x * 100, ".2f")}%'
    """物理暴击"""

    CriticalM = '魔法暴击', '/ui/UI_ProfileIcon_010.png', lambda x: f'{format(x * 100, ".2f")}%'
    """魔法暴击"""

    EquipmentSkillAttack = '技能攻击力增加', '/ui/UI_ProfileIcon_047.png', lambda x: f'{format(x * 100 - 100, ".2f")}%'
    """技能攻击力"""

    SpeedA = '攻击速度', '/ui/UI_ProfileIcon_012.png', lambda x: f'{format(x * 100, ".2f")}%'
    """攻击速度"""

    SpeedM = '移动速度', '/ui/UI_ProfileIcon_014.png', lambda x: f'{format(x * 100, ".2f")}%'
    """移动速度"""

    SpeedR = '施放速度', '/ui/UI_ProfileIcon_013.png', lambda x: f'{format(x * 100, ".2f")}%'
    """施放速度"""

    # HitP : float
    # """命中率"""

    # Hit : float
    # """命中"""
