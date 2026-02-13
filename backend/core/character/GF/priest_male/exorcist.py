#f6a4ad30555b99b499c07835f87ce522
from core.basic.formula import 武器冷却惩罚
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "priest_male/exorcist/cn/skillDetail"

class ActiveSkill(ActiveSkill):
    def getWeaponCDRatio(self):
        weapon = self.char.charEquipInfo['武器'].equInfo
        if weapon is None or '传世武器' in weapon.categorize:
            return 1
        elif weapon.itemDetailType in ['念珠','战斧']:
            return 1.0
        else:
            return 武器冷却惩罚(weapon.itemDetailType, self.char.输出类型)

# 空斩打
# priest_male/exorcist/3c5604bdbb0240b8f130f59ab40509c3
# f6a4ad30555b99b499c07835f87ce522/3c5604bdbb0240b8f130f59ab40509c3
class Skill0(ActiveSkill):
    """
        用巨兵向敌人发出攻击并使其浮空， 发动时有霸体判定。 \n
        在[意念驱动]已施放状态下， 将无法使用此技能。\n
        转职为光明骑士后， 技能类型变为独立攻击力。\n
        转职为驱魔师后， 可以蓄气攻击。
    """
    name = "空斩打"
    learnLv = 1
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    cd = 2
    uuid = "3c5604bdbb0240b8f130f59ab40509c3"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 浮空力比率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1


# 基础精通
# priest_male/exorcist/5a56514f35cf0270ae8d6c65f8fefd78
# f6a4ad30555b99b499c07835f87ce522/5a56514f35cf0270ae8d6c65f8fefd78
class Skill3(PassiveSkill):
    """
        增加基本攻击、 前冲攻击、 跳跃攻击、 [空斩打]的攻击力。\n
        在决斗场中， 增益/减益技能、 被动技能的技能攻击力增加效果对[基础精通]无影响。
    """
    name = "基础精通"
    learnLv = 1
    masterLv = 115
    maxLv = 200
    position = 0 #TODO
    rangeLv = 1
    uuid = "5a56514f35cf0270ae8d6c65f8fefd78"
    icon = "$common/$uuid"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力变化率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 前冲攻击力变化率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 跳跃攻击力变化率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [{"type":"*skillDamage","data":[i-100 if i>0 else 0 for i in data0],"skills":["空斩打","疾风打"]}]


# 法阵 : 万悟
# priest_male/exorcist/ebff277c02cc8b54c32635cd0d25f6f3
# f6a4ad30555b99b499c07835f87ce522/ebff277c02cc8b54c32635cd0d25f6f3
class Skill6(PassiveSkill):
    """
        追求万物感悟的驱魔师的气魄。 时而以武艺， 时而以智慧将自己的气息和谐地结合到一起。\n
        力量和智力、 物理暴击率和魔法暴击率中会按照一定比率相互补正。
    """
    name = "法阵 : 万悟"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "ebff277c02cc8b54c32635cd0d25f6f3"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 力量和智力补正比率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理和魔法暴击率补正比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 落凤锤
# priest_male/exorcist/45442bbbe33540b4deeec29437dae70c
# f6a4ad30555b99b499c07835f87ce522/45442bbbe33540b4deeec29437dae70c
class Skill16(ActiveSkill):
    """
        跳跃后把巨兵砸向地面引发冲击波并使周围敌人受到一定伤害。\n
        跳跃时可以移动， 但蓝拳使者在[意念驱动]已施放状态下， 无法使用此技能。\n
        转职成为驱魔师时， 增加20%的攻击力， 增加冲击波范围、 跳跃高度和跳跃速度。\n
        而且， 下劈后可以强制中断动作并施放部分驱魔师巨兵系技能。\n
    - [可施放技能] -\n
    [疾风打]\n
    [星落打]\n
    [狂乱锤击]\n
    [疾空旋风破]\n
    [无双击]\n
    [逆鳞震]\n
    [逆龙七杀]
    """
    name = "落凤锤"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 6
    mp = [28, 308]
    uuid = "45442bbbe33540b4deeec29437dae70c"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 巨兵打击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波范围 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 冲击波攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 转职成为驱魔师时， 冲击波范围增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    skillDamage = 1.2

# 潜龙
# priest_male/exorcist/b163d099c8cc27fdb6fd3639c2ee6df9
# f6a4ad30555b99b499c07835f87ce522/b163d099c8cc27fdb6fd3639c2ee6df9
class Skill17(PassiveSkill):
    """
        驱魔师凭借坚韧的胆魄， 通过施放技能获得霸体状态时， 所受伤害减少。\n
        即使在持续蓄气期间， 该效果也适用， 并且在受到伤害时不会被击退。
    """
    name = "潜龙"
    learnLv = 15
    masterLv = 1
    maxLv = 11
    position = 0 #TODO
    rangeLv = 5
    uuid = "b163d099c8cc27fdb6fd3639c2ee6df9"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 所受伤害减少率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

# 驱魔震慑
# priest_male/exorcist/51a08fd0c90f0a5276cd552047fac93d
# f6a4ad30555b99b499c07835f87ce522/51a08fd0c90f0a5276cd552047fac93d
class Skill18(PassiveSkill):
    """
        基本、 前冲、 跳跃攻击变更为被驱魔师之力特化的固有动作。 基本攻击的最后动作可通过蓄气攻击使用。\n
        增加驱魔师的移动速度， 并且向不死族、 恶魔、 精灵系列的怪物发出基本攻击时， 可以增加5%的攻击力。
    """
    name = "驱魔震慑"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "51a08fd0c90f0a5276cd552047fac93d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 移动速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

# 疾风打
# priest_male/exorcist/8572675ec6a1f50b6eff6a867376c2de
# f6a4ad30555b99b499c07835f87ce522/8572675ec6a1f50b6eff6a867376c2de
class Skill19(ActiveSkill):
    """
        像野兽一般向前方突进， 利用肩膀将敌人撞开。\n
        被命中的敌人有一定几率进入眩晕状态。\n
        该技能攻击力受[基础精通]影响。   
    """
    name = "疾风打"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 2
    cd = 4.5
    mp = [190, 190]
    uuid = "8572675ec6a1f50b6eff6a867376c2de"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 撞击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 撞击冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 眩晕几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 眩晕持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 封魔莲华
# priest_male/exorcist/128b9ddef2262f40723deae4407bdb42
# f6a4ad30555b99b499c07835f87ce522/128b9ddef2262f40723deae4407bdb42
class Skill20(ActiveSkill):
    """
        驱魔师惩恶扬善的力量之源。\n
        给武器赋予火属性和光属性； 并增加自身的基本攻击力、 技能攻击力和命中率， 以及直接攻击时被命中敌人的僵直时间。\n
        在决斗场中， 不适用命中率增加效果。
    """
    name = "封魔莲华"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    cd = 5
    uuid = "128b9ddef2262f40723deae4407bdb42"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 命中率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 僵直时间增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    associate = [{"data":data0}]

# 巨兵精通
# priest_male/exorcist/0b8db1e10b3abbd24d38564e708675d5
# f6a4ad30555b99b499c07835f87ce522/0b8db1e10b3abbd24d38564e708675d5
class Skill21(PassiveSkill):
    """
        驱魔师挥舞巨兵并发挥出内在力量。\n
        增加攻击力。 装备巨兵时， 增加命中率。\n
        装备战斧和念珠时， 技能魔法值、 冷却时间增减不受武器类型的影响。\n
        在决斗场中， 技能魔法值、 冷却时间增减受武器类型的影响。
    """
    name = "巨兵精通"
    learnLv = 20
    masterLv = 20
    maxLv = 30
    position = 0 #TODO
    rangeLv = 3
    uuid = "0b8db1e10b3abbd24d38564e708675d5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 命中率增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理、 魔法攻击力增加比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [{"data":data1,"type":"$*PAtkP"}]

# 升天阵
# priest_male/exorcist/b89c9ab317bc0a443f6497b7cca2f6a8
# f6a4ad30555b99b499c07835f87ce522/b89c9ab317bc0a443f6497b7cca2f6a8
class Skill22(ActiveSkill):
    """
        在前方布下升天阵， 使阵内的敌人受到伤害的同时使其浮空。\n
        转职成为驱魔师时， 才可以强制中断基本攻击动作， 并立即施放该技能； 增加20%的攻击力。\n
       [升天阵]可以把浮空的敌人聚集到阵的中心。
    """
    name = "升天阵"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 5
    mp = [28, 308]
    uuid = "b89c9ab317bc0a443f6497b7cca2f6a8"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 浮空力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 攻击范围 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 转职成为驱魔师时， 攻击范围 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    skillDamage = 1.2


# 星落打
# priest_male/exorcist/01384bbfc346775d1267fa0bc4ca605f
# f6a4ad30555b99b499c07835f87ce522/01384bbfc346775d1267fa0bc4ca605f
class Skill24(ActiveSkill):
    """
        用巨兵轻轻挑起前方的敌人后， 大幅度挥动甩飞敌人。 (挥动攻击会一同攻击范围内的其他敌人)\n
        按住技能键时吸附周围敌人， 可以根据按键持续时间调整击飞高度。\n
        挥动前按方向键可以改变被甩飞敌人的飞行轨迹。\n
    方向键(无操作) : 会飞向前方下端\n
    方向键(前方) : 快速飞向前方\n
    方向键(上方) : 快速飞向前方上端
    """
    name = "星落打"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 12
    mp = [60, 756]
    uuid = "01384bbfc346775d1267fa0bc4ca605f"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 挥击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 漩涡吸附敌人范围 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 式神 : 热炎朱雀
# priest_male/exorcist/e0a072e8cef2d77893aad5f68aeed56a
# f6a4ad30555b99b499c07835f87ce522/e0a072e8cef2d77893aad5f68aeed56a
class Skill25(ActiveSkill):
    """
        召唤式神朱雀。 被召唤的朱雀会向前方突进， 造成多段伤害后升天再一次造成打击。
    """
    name = "式神 : 热炎朱雀"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 8
    mp = [40, 462]
    uuid = "e0a072e8cef2d77893aad5f68aeed56a"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 突进攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 突进多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 升天攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 式神 : 地之玄武
# priest_male/exorcist/92360eab6e1f378902018eca681ac629
# f6a4ad30555b99b499c07835f87ce522/92360eab6e1f378902018eca681ac629
class Skill26(ActiveSkill):
    """
        召唤式神玄武。\n
        被召唤的玄武在驱魔师的前方伸手展开岩石翻腾攻击的领域。\n
        之后玄武举起手指， 对领域内的敌人进行强制控制。
    """
    name = "式神 : 地之玄武"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 8
    mp = [65, 686]
    uuid = "92360eab6e1f378902018eca681ac629"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 岩石攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 10
    # 岩石多段攻击间隔 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 岩石多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 领域范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 驱魔之书
# priest_male/exorcist/150aa05b9ee8b9c7c04a25f3e425900c
# f6a4ad30555b99b499c07835f87ce522/150aa05b9ee8b9c7c04a25f3e425900c
class Skill27(PassiveSkill):
    """
        记载了驱魔师知识的书， 可以增加技能的攻击力。 除[四座千泰门]、 [真龙焚天]、 [雷鸣怒海· 火啸山崩]的其他技能的冷却时间减少。
    """
    name = "驱魔之书"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    uuid = "150aa05b9ee8b9c7c04a25f3e425900c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 冷却时间减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"data":data0},{"data":data1,"type":"*cdReduce","exceptSkills":["四座千泰门", "真龙焚天", "雷鸣怒海·火啸山崩"]}]

# 式神 : 空之白虎
# priest_male/exorcist/0ed3148658fe37b3336ccb718dc0fdb0
# f6a4ad30555b99b499c07835f87ce522/0ed3148658fe37b3336ccb718dc0fdb0
class Skill28(ActiveSkill):
    """
        召唤式神白虎。\n
        被召唤的白虎在驱魔师前方伸手召唤空之法珠。\n
        召唤出的空之法珠将展开领域， 向进入领域内部的敌人的位置召唤雷电。\n
        领域内落下雷电的数量固定， 会依次落在领域内的敌人身上； 只有单一目标时， 会朝着此目标落下所有雷电。 
    """
    name = "式神 : 空之白虎"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cube = 1
    cd = 16.5
    mp = [65, 686]
    uuid = "0ed3148658fe37b3336ccb718dc0fdb0"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 雷电攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 8
    # 雷电多段攻击间隔 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 雷电多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 领域范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [式神 : 空之白虎]\n
        落雷会攻击法珠， 法珠被击中后产生波动， 攻击范围内的所有敌人\n
        - 共攻击5次， 最后生成更强的落雷\n
        - 总攻击力相同\n
        攻击范围 +25%
        """
        ...

    def vp_2(self):
        """
        [式神 : 空之白虎]\n
        进入地下城时， 白虎跟随驱魔师\n
        按技能键时白虎追踪前方范围\n
        - 对范围内最强敌人降下落雷 (次数及间隔与原来相同)\n
        - 通过共鸣发动时， 则落向被巨兵攻击的敌人\n
        - 落雷冷却时间 : 16.5秒\n
        - 落雷准备就绪时， 白虎会恢复原本的姿态进入待命状态
        """
        ...

# 狂乱锤击
# priest_male/exorcist/c27418ae613c647527200a7ca17d97fd
# f6a4ad30555b99b499c07835f87ce522/c27418ae613c647527200a7ca17d97fd
class Skill29(ActiveSkill):
    """
        用巨兵向前方敌人进行多次锤击。\n
        蓄积力量给予的最后一击可以敌人进入眩晕状态。\n
        连续按技能键或蓄气施放时， 可以向敌人发出更快的锤击。\n
        若按左右方向键， 则可以改变攻击方向。 若在最后一击发动前按跳跃键， 则会中断锤击。\n
        [封魔莲华]状态下， 锤击可以聚集敌人。\n
        决斗场中， 输入跳跃键无法中断攻击； [封魔莲华]状态下也无法聚集敌人。
    """
    name = "狂乱锤击"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cube = 1
    cd = 14
    mp = [180, 1512]
    uuid = "c27418ae613c647527200a7ca17d97fd"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 锤击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 锤击攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 眩晕几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 眩晕持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 攻击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [狂乱锤击]\n
        每次锤击生成冲击波\n
        - 锤击攻击次数变为6次\n
        - 吸附敌人的力量 +50%\n
        - 删除最后一击\n
        - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [狂乱锤击]\n
        锤击和最后一击动作变更为向周围大范围挥动\n
        - 锤击次数变更为2次\n
        - 删除最后一击附加眩晕状态的效果\n
        - 总攻击力相同\n
        连按或蓄气时， 不会增加速度\n
        锤击过程中按技能键(Z)时， 立即发动最后一击
        """
        ...

# 疾空旋风破
# priest_male/exorcist/eb71e1d82d92c7e1d40500a0dcd77aa6
# f6a4ad30555b99b499c07835f87ce522/eb71e1d82d92c7e1d40500a0dcd77aa6
class Skill30(ActiveSkill):
    """
        携带巨兵以连续的大回旋攻击周围敌人。\n
        若连续按攻击键， 则可以增加回旋速度。\n
    若按方向键， 则可以在回旋中移动； 若按跳跃键， 则可以立即中断回旋动作。\n
    在决斗场中无法中断技能。
    """
    name = "疾空旋风破"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [200, 1680]
    uuid = "eb71e1d82d92c7e1d40500a0dcd77aa6"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 回旋次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 回旋攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 7
    # 最后击飞攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [疾空旋风破]\n
        旋转时形成旋风， 将周围的敌人聚拢到中心\n
        - 旋转次数变更为4次\n
        - 总攻击力相同\n
        蓄气时， 固定以最大速度旋转
        """
        ...

    def vp_2(self):
        """
        [疾空旋风破]\n
        挥舞的战斧借助朱雀之力， 更强烈地燃烧并旋转攻击敌人\n
        施放过程中与“式神 : 热炎朱雀”产生共鸣时， 朱雀冷却时间及攻击力变为2.5倍\n
        施放过程中， [潜龙]所受伤害减少率效果 +100%
        """
        ...

    def effect(self, old, new):
        if self.vp == 2:
            self.associate = [
                {"type":"*skillRation","data":[0] + [150]*self.maxLv,"skills":["式神 : 热炎朱雀"]},
                {"type":"*cdReduce","data":[0] + [-150]*self.maxLv,"skills":["式神 : 热炎朱雀"]},
            ]
        return super().effect(old, new)

# 无双击
# priest_male/exorcist/d53301bb328baf12a3ae482cc6a565dd
# f6a4ad30555b99b499c07835f87ce522/d53301bb328baf12a3ae482cc6a565dd
class Skill31(ActiveSkill):
    """
        大力挥动巨兵， 使周围的敌人聚集并向敌人发出强烈的捶击。\n
        对无法抓取的敌人不适用控制效果。
    """
    name = "无双击"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [350, 2940]
    uuid = "d53301bb328baf12a3ae482cc6a565dd"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 挥动打击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 捶击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 捶击范围扩大率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [无双击]\n
        将武器变为苍龙巨兵， 以水的力量挥舞攻击更大范围\n
        水的流动有助于身体的循环， 从而强化自身的气息\n
        - 20秒内[式神契结 : 真龙]速度增加量 +150%
        """
        ...

    def vp_2(self):
        """
        [无双击]\n
        施放技能时进入无敌状态\n
        - 无法蓄气施放\n
        在突进或者[疾风打]施放过程中施放时， 向前方突进并施放
        """
        ...

# 斗志散发
# priest_male/exorcist/7e904ea3d2a9faa054604e55120a9268
# f6a4ad30555b99b499c07835f87ce522/7e904ea3d2a9faa054604e55120a9268
class Skill32(PassiveSkill):
    """
    사신의 인정을 받은 용투사는 평범한 사람들도 느낄 수 있는 투기가 발산되고 있다.\n
    增加基本攻击力和技能攻击力。
    """
    name = "斗志散发"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 3
    uuid = "7e904ea3d2a9faa054604e55120a9268"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]

# 四座千泰门
# priest_male/exorcist/5892d1fa4462e561ac8f8d2c74892b0a
# f6a4ad30555b99b499c07835f87ce522/5892d1fa4462e561ac8f8d2c74892b0a
class Skill33(ActiveSkill):
    """
        召唤四神寺的镇寺门。 驱魔师借用式神之力打开大门， 无数的神鸟夺门而出后， 一只巨大的神鸟掠过并造成伤害。
    """
    name = "四座千泰门"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [900, 7559]
    uuid = "5892d1fa4462e561ac8f8d2c74892b0a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 神鸟群多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 20
    # 神鸟群多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 巨大神鸟攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

# 式神 : 幻海青龙
# priest_male/exorcist/0e409ac3e1c1f3976b3ef2bfe4c13069
# f6a4ad30555b99b499c07835f87ce522/0e409ac3e1c1f3976b3ef2bfe4c13069
class Skill34(ActiveSkill):
    """
        召唤式神青龙。\n
        被召唤的青龙向驱魔师的前方进行冲锋， 挥舞巨兵造成3次攻击后跳起， 发动终结攻击后消失。\n
        在青龙已被召唤的状态下再次召唤时， 青龙立即发动终结攻击， 并协同驱魔师发动攻击。 (此时未进行的攻击的攻击力将合算至终结攻击)
    """
    name = "式神 : 幻海青龙"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [200, 1680]
    uuid = "0e409ac3e1c1f3976b3ef2bfe4c13069"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 巨兵第1次攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 巨兵第2次攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 巨兵第3次攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 巨兵终结攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [式神 : 幻海青龙]\n
        青龙向前突进并立即发动最后一击\n
        - 攻击更大范围并突进\n
        - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [式神 : 幻海青龙]\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 16.5秒\n
        - 单次攻击力 -45%\n
        [式神之悟]共鸣效果不消耗使用次数
        """
        self.cd = 16.5
        self.skillDamage *= 1 - 0.45
        ...

# 逆鳞震
# priest_male/exorcist/c5a2956d8ed3af1746ed2f76ca971a09
# f6a4ad30555b99b499c07835f87ce522/c5a2956d8ed3af1746ed2f76ca971a09
class Skill35(ActiveSkill):
    """
        向后挥动巨兵， 然后跳起砸向地面， 使地面产生巨大裂缝， 地裂范围内的敌人受到巨大伤害。\n
        可以蓄气施放， 最大蓄气时增加跳跃高度和攻击范围。
    """
    name = "逆鳞震"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [800, 1680]
    uuid = "c5a2956d8ed3af1746ed2f76ca971a09"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 下砸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最大蓄气时范围增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [逆鳞震]\n
        下砸时借助玄武之力， 更加猛烈地猛击地面， 并强制控制敌人1秒\n
        施放时， 若[式神 : 地之玄武]处于可施放状态， 则消耗玄武的冷却时间； 变更效果如下\n
        - 玄武召唤出巨大石拳， 猛烈砸向地面， 并强制控制敌人2秒\n
        - 玄武地面冲击攻击力与原玄武的总攻击力相同\n
        - 无法蓄气施放
        """
        ...

    def vp_2(self):
        """
        [逆鳞震]\n
        若在跳跃时按方向键， 则会向该方向跳跃并施放技能\n
        攻击范围 +25%\n
        蓄气施放时， 攻击范围增加率变更为25%
        """
        ...

# 式神契结 : 真龙
# priest_male/exorcist/1f4b87944dc5551b91bf6cd25d84b48e
# f6a4ad30555b99b499c07835f87ce522/1f4b87944dc5551b91bf6cd25d84b48e
class Skill36(PassiveSkill):
    """
        被真龙附体后， 真龙星君变得更加心平气和， 拥有了让自己和友军受益的能力。\n
        技能攻击力增加， 在同一空间包括自己在内的所有队员的所有速度增加。\n
        此外， 因为法力得到强化， [升天阵]和[式神 : 空之白虎]的攻击范围增加。
    """
    name = "式神契结 : 真龙"
    learnLv = 75
    masterLv = 1
    maxLv = 11
    position = 0 #TODO
    rangeLv = 50
    uuid = "1f4b87944dc5551b91bf6cd25d84b48e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [升天阵]范围增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [式神 ： 空之白虎]范围增加量 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 驱魔师和队友所有速度增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    associate = [{"data":data0}]

# 式神之力
# priest_male/exorcist/328867949b763ce73e243da84fd59157
# f6a4ad30555b99b499c07835f87ce522/328867949b763ce73e243da84fd59157
class Skill37(PassiveSkill):
    """
        达到神之境界的真龙星君能够平静地掌控内心的斗志， 从而增加物理/魔法攻击力和暴击率。
    """
    name = "式神之力"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 3
    uuid = "328867949b763ce73e243da84fd59157"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 物理/魔法攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [{"data":data0}]

# 逆龙七杀
# priest_male/exorcist/5197b141332a65a89d452adf227c2f30
# f6a4ad30555b99b499c07835f87ce522/5197b141332a65a89d452adf227c2f30
class Skill38(ActiveSkill):
    """
        通过第1击压制敌人后， 挥动6次巨兵对敌人造成伤害。\n
        被第1击命中的敌人将进入超级控制状态。\n
        施放技能时无法强制中断， 若第1击未击中敌人， 则不会发动后续攻击。\n
        施展第1击攻击时， 若按攻击键或技能键， 则可以进行更快的攻击。
    """
    name = "逆龙七杀"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 5
    cd = 50
    mp = [800, 6000]
    uuid = "5197b141332a65a89d452adf227c2f30"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 第3击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 第4击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 第5击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # 第6击攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # 第7击攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 1
    # [范围信息]
    # 攻击范围扩大率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    def vp_1(self):
        """
        [逆龙七杀]\n
        将全身的力量注入武器后， 攻击周围所有敌人\n
        攻击范围 +20%
        """
        ...

    def vp_2(self):
        """
        [逆龙七杀]\n
        技能形态变更为三次强力挥斩\n
        - 每次攻击之间自由行动时间 : 10秒\n
        - 每次攻击若命中失败则等待下一击发动\n
        可强制中断巨兵系列技能的施放后僵直并立即施放\n
        - 挥斩命中后， 也可以强制中断施放后僵直并立即施放巨兵系列技能\n
        连击时不再增加攻击速度
        """
        ...

# 升龙·开阵
# priest_male/exorcist/7dd85dccf7ae1f65609c36d66e2e1c95
# f6a4ad30555b99b499c07835f87ce522/7dd85dccf7ae1f65609c36d66e2e1c95
class Skill39(ActiveSkill):
    """
        在前方展开真龙升天的具现化领域。\n
        真龙从展开的领域中心升天， 对领域内的敌人造成多段攻击伤害。\n
        随后， 升天的真龙落地， 造成巨大伤害。
    """
    name = "升龙·开阵"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 5
    cd = 50
    mp = [800, 6000]
    uuid = "7dd85dccf7ae1f65609c36d66e2e1c95"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 真龙升天攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 20
    # 真龙升天多段攻击间隔 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 真龙升天多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 真龙下落攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 领域范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [升龙·开阵]\n
        法阵启动时， 立即为领域内的敌人贴上符咒\n
        - 附着的符咒在造成4次伤害后爆炸\n
        - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [升龙·开阵]\n
        四位式神同时释放力量， 在前方引发灾变\n
        - 灾变中吸附周围敌人\n
        - 灾变结束后真龙降临进行最后一击\n
        - 总攻击力相同\n
        变更为可以共鸣的技能
        """
        ...

# 真龙焚天
# priest_male/exorcist/75747c67e14eec6088ce67f63ea41628
# f6a4ad30555b99b499c07835f87ce522/75747c67e14eec6088ce67f63ea41628
class Skill40(ActiveSkill):
    """
        借助真龙之力歼灭敌人。\n
        接受了从天而降的真龙气息， 利用以真龙化作的巨斧武器， 对敌人进行大范围的挥舞攻击并造成伤害。
    """
    name = "真龙焚天"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 8000]
    uuid = "75747c67e14eec6088ce67f63ea41628"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 真龙巨斧攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1

# 式神之悟
# priest_male/exorcist/863295a0fc634cf5fcc01e82a735fd6b
# f6a4ad30555b99b499c07835f87ce522/863295a0fc634cf5fcc01e82a735fd6b
class Skill41(PassiveSkill):
    """
        领悟了五式神的真正力量， 通过与它们极致的共鸣， 到达神将的境界。\n
        增加基本攻击力和转职技能攻击力， 变更部分技能。\n
    [共鸣]\n
        在施放巨兵系列技能过程中， 可以施放式神技能。 最多可填充2次， 并且不受冷却时间减少效果的影响。\n
    -    巨兵系列 : [空斩打]、 [落凤锤]、 [疾风打]、 [星落打]、 [狂乱锤击]、 [疾空旋风破]、 [无双击]、 [逆鳞击]、 [逆龙七绝]、 [式神灭却·合]\n
    [式神 : 地之玄武]\n
        减少多段攻击间隔。
    """
    name = "式神之悟"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 3
    uuid = "863295a0fc634cf5fcc01e82a735fd6b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 共鸣填充冷却时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [{"data":data0}]

# 式神灭却·合
# priest_male/exorcist/3153ca0e6752a6283412c59c5ec8e002
# f6a4ad30555b99b499c07835f87ce522/3153ca0e6752a6283412c59c5ec8e002
class Skill42(ActiveSkill):
    """
        借助四位式神的力量立即将巨兵插入地面， 震碎地表使敌人浮空。 然后， 再次向前方挑击， 使掀起的地表与地面发生碰撞， 飞散碎裂的岩石。
    """
    name = "式神灭却·合"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [960, 7200]
    uuid = "3153ca0e6752a6283412c59c5ec8e002"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 插入巨兵攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 挑击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 挑击冲击波攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 飞散岩石攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 4
    # 岩石多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 雷鸣怒海·火啸山崩
# priest_male/exorcist/02ac8e048f7bbcfa616e74ac68988872
# f6a4ad30555b99b499c07835f87ce522/02ac8e048f7bbcfa616e74ac68988872
class Skill43(ActiveSkill):
    """
        使呼唤五式神的真正力量， 然后化为斧头和念珠的形态。\n
        先释放式神原本的力量， 引发雷电和海啸， 吞没敌人后浮上海面。\n
        然后， 冥想的同时将所有剩余力量汇聚于斧头上， 发动惊天动地的终结一击。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "雷鸣怒海·火啸山崩"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4027, 12888]
    uuid = "02ac8e048f7bbcfa616e74ac68988872"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 雷电多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 雷电多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 上涌的水柱攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 最后下劈攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 地面爆炸多段攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 10
    # 地面爆炸多段攻击次数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'exorcist'
        self.nameCN = '神启·驱魔师'
        self.role = 'priest_male'
        self.角色 = '圣职者(男)'
        self.职业 = '驱魔师'
        self.jobId = 'f6a4ad30555b99b499c07835f87ce522'
        self.jobGrowId = '6d459bc74ba73ee4fe5cdc4655400193'

        self.武器选项 = ['光杖','念珠','图腾','镰刀','战斧']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '板甲'
        self.buff = 1.83

        super().__init__(equVersion, __name__)
