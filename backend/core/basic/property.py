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

    AtkP = '物理攻击', '/ui/UI_ProfileIcon_006.png', lambda x: round(x, 0)
    """物理攻击力"""

    AtkM = '魔法攻击', '/ui/UI_ProfileIcon_007.png', lambda x: round(x, 0)
    """魔法攻击力"""

    AtkI = '独立攻击', '/ui/UI_ProfileIcon_008.png', lambda x: round(x, 0)
    """独立攻击力"""

    ElementDB = '攻击属性', '/ui/UI_ProfileIcon_009.png', lambda x: f'火({int(x['火'])})/冰({int(x['冰'])})/光({int(x['光'])})/暗({int(x['暗'])})'
    """攻击属性"""

    SkillAttack = '技能伤害', '/ui/UI_ProfileIcon_047.png', lambda x: f'{format(x * 100 - 100, ".1f")}%'
    """技能攻击力"""

    SpeedA = '攻击速度', '/ui/UI_ProfileIcon_012.png', lambda x: f'{format(x * 100, ".2f")}%'
    """攻击速度"""

    SpeedM = '移动速度', '/ui/UI_ProfileIcon_014.png', lambda x: f'{format(x * 100, ".2f")}%'
    """移动速度"""

    SpeedR = '施放速度', '/ui/UI_ProfileIcon_013.png', lambda x: f'{format(x * 100, ".2f")}%'
    """施放速度"""

    Attack = '攻击强化', '/ui/UI_ProfileIcon_015.png', lambda x: f'{format(x, ".1f")}%'
    """攻击强化"""

    AttackP = '攻击强化%', '/ui/UI_ProfileIcon_015.png', lambda x: f'{format(x * 100 - 100, ".1f")}%'
    """攻击强化%"""

    EquEffectRatio = '特效伤害', '/ui/UI_ProfileIcon_016.png', lambda x: f'{format(x * 100 - 100, ".1f")}%'

    # HitP : float
    # """命中率"""

    # Hit : float
    # """命中"""
