#41f1cdc2ff58bb5fdc287be0db2a8df3
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "swordman_male/asura/cn/skillDetail"

# 基础精通
# swordman_male/asura/5a56514f35cf0270ae8d6c65f8fefd78
# 41f1cdc2ff58bb5fdc287be0db2a8df3/5a56514f35cf0270ae8d6c65f8fefd78
class Skill0(PassiveSkill):
    """
    增加基本攻击、 前冲攻击、 跳跃攻击、 [上挑]、 [连突刺]的攻击力。\n
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
    associate = [{"type":"*skillRation","data":[i-100 if i>0 else 0 for i in data0],"skills":["波动刻印"]}]


# 鬼印珠
# swordman_male/asura/9dda3f4a849dba1a288dd65e116860f2
# 41f1cdc2ff58bb5fdc287be0db2a8df3/9dda3f4a849dba1a288dd65e116860f2
class Skill1(ActiveSkill):
    """
    把波动印转化成鬼印珠向敌人发射。\n
    鬼印珠高速持续旋转后爆炸。\n
    命中时， 因鬼印珠高速旋转， 敌人移动速度减少。\n
    波动印的数量越多， 鬼印珠的攻击力越高。\n
    被远距离攻击命中前使用[格挡]， 可以将受到的伤害减少为0， 同时生成波动印。
    """
    name = "鬼印珠"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 6
    mp = [95, 980]
    uuid = "9dda3f4a849dba1a288dd65e116860f2"

    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 鬼印珠攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hi0 = 18
    # 鬼印珠多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 鬼印珠爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 波动刻印5个时攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 波动刻印4个时攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 波动刻印3个时攻击力增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 波动刻印2个时攻击力增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 波动刻印1个时攻击力增加率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [范围信息]
    # 鬼印珠大小比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 鬼印珠爆炸比率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)

# 地裂 · 波动剑
# swordman_male/asura/3d8f3d438405d79f8d3ed68072674d1e
# 41f1cdc2ff58bb5fdc287be0db2a8df3/3d8f3d438405d79f8d3ed68072674d1e
class Skill2(ActiveSkill):
    """
    向前方敌人快速施放无属性的波动剑。\n
    转职为阿修罗后， 可中断基本攻击使用
    """
    name = "地裂 · 波动剑"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 3
    mp = [17, 168]
    uuid = "3d8f3d438405d79f8d3ed68072674d1e"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 地裂攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 地裂大小比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)


# 波动刻印
# swordman_male/asura/128b9ddef2262f40723deae4407bdb42
# 41f1cdc2ff58bb5fdc287be0db2a8df3/128b9ddef2262f40723deae4407bdb42
class Skill3(ActiveSkill):
    """
    施放后， 每隔一段时间生成一个波动刻印， 基本攻击和[上挑]时发射波动剑气。\n
    波动剑气攻击力受[基础精通]影响。\n
    增加施放速度， 基本攻击和转职系列技能攻击力增加， 并获得附加效果。\n
    [裂波斩]\n
    命中时生成1个波动刻印， 对无法抓取的敌人也能施放裂波。\n
    在决斗场中， 不会增加基本攻击力和技能攻击力。
    """
    name = "波动刻印"
    learnLv = 15
    masterLv = 20
    maxLv = 30
    position = 3
    rangeLv = 3
    cd = 5
    mp = [126, 1380]
    uuid = "128b9ddef2262f40723deae4407bdb42"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 施放速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 波动刻印生成间隔 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 波动刻印持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 波动刻印数量上限 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 波动剑气第1击攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # 波动剑气第2击攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 1
    # 波动剑气第3击攻击力 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)
    hit7 = 1

    associate = [
        {"type":"*skillRation","data":data0},
        {"type":"*skillRation","data":[0] + [20]*maxLv,"skills":["鬼印珠","不动明王阵"]},
    ]


# 绝对感知
# swordman_male/asura/d2c6df5105577fb59fb92529a36165a0
# 41f1cdc2ff58bb5fdc287be0db2a8df3/d2c6df5105577fb59fb92529a36165a0
class Skill4(PassiveSkill):
    """
    可以在眼睛失明的状态下感知敌人的杀气， 增加自身的失明抗性和背击回避率。\n
    减少被击时防具耐久度减少率。
    """
    name = "杀气感知"
    learnLv = 18
    line = 15
    masterLv = 1
    maxLv = 1
    position = 6
    rangeLv = 1
    uuid = "d2c6df5105577fb59fb92529a36165a0"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 失明抗性增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 背击回避率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 被击时防具耐久度减少率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 邪光斩
# swordman_male/asura/92360eab6e1f378902018eca681ac629
# 41f1cdc2ff58bb5fdc287be0db2a8df3/92360eab6e1f378902018eca681ac629
class Skill5(ActiveSkill):
    """
    挥剑向前方敌人发出巨大的剑气攻击。
    """
    name = "邪光斩"
    name = "邪光斩"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 10
    mp = [65, 616]
    uuid = "92360eab6e1f378902018eca681ac629"

    # 剑气攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 剑气发射距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 剑气多段攻击间隔 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 剑气大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)


# 修罗邪光斩
# swordman_male/asura/1fadde0eece18649caddbca7bd58cc2f
# 41f1cdc2ff58bb5fdc287be0db2a8df3/1fadde0eece18649caddbca7bd58cc2f
class Skill6(PassiveSkill):
    """
    蓄气达最大值时， 可以增加攻击力、 发射速度和射程， 生成1个波动印。\n
    强制中断[冰刃 · 波动剑]、 [极冰 · 裂波剑]、 [爆炎 · 波动剑]、 [极炎 · 裂波剑]技能并施放[修罗邪光斩]时， 可以施放最大蓄气状态的[修罗邪光斩]。\n
    在决斗场中， 无法强制取消技能施放后的僵直时间。
    """
    name = "修罗邪光斩"
    learnLv = 20
    masterLv = 1
    maxLv = 11
    position = 6
    rangeLv = 15
    uuid = "1fadde0eece18649caddbca7bd58cc2f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 最大蓄气时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 邪光斩攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 发射速度和射程增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 邪光剑气多段攻击间隔 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 邪光剑气多段攻击次数 : 3次

    associate = [{"type":"*skillRation","data":data1,"skills":["邪光斩"]}]


# 慧思 관조 관조
# swordman_male/asura/4e62e33aa37394ec4207a72af2968abf
# 41f1cdc2ff58bb5fdc287be0db2a8df3/4e62e33aa37394ec4207a72af2968abf
class Skill7(PassiveSkill):
    """
    高度集中精神， 通过气的流动感知敌人。\n
    增加魔法暴击率。
    """
    name = "慧思"
    learnLv = 20
    masterLv = 1
    maxLv = 10
    position = 3
    rangeLv = 3
    uuid = "4e62e33aa37394ec4207a72af2968abf"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 魔法暴击率增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

# 波动爆发
# swordman_male/asura/03bb5314ffd41e9458d67ef924fef38f
# 41f1cdc2ff58bb5fdc287be0db2a8df3/03bb5314ffd41e9458d67ef924fef38f
class Skill8(ActiveSkill):
    """
    将体内凝聚的波动之力瞬间爆发， 可以使周围的敌人朝施放者的正前方飞出。\n
    施放时， 生成2个波动刻印。\n
    可以在地面被击状态下施放。\n
    在决斗场中， 不可在地面被击状态下施放。
    """
    name = "波动爆发"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 3
    cd = 7.5
    mp = [65, 630]
    uuid = "03bb5314ffd41e9458d67ef924fef38f"

    uuid = "03bb5314ffd41e9458d67ef924fef38f"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 波动释放攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 波动释放大小比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)


# 挫折意志
# swordman_male/asura/1803b6a67047cafb9e289b4f33cc507b
# 41f1cdc2ff58bb5fdc287be0db2a8df3/1803b6a67047cafb9e289b4f33cc507b
class Skill9(PassiveSkill):
    """
    受敌人攻击或躲避攻击后， 可以暂时增加基本攻击、 技能攻击力和魔法值恢复量。\n
    若持续时间内再次受到攻击或闪避时， 则会刷新技能持续时间。\n
    施放[波动爆发]、 [无尽波动]、 [无双波]、 [邪光波动阵]、 [不动明王阵]时， 可以获得[挫折意志]效果。
    """
    name = "挫折意志"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 3
    uuid = "1803b6a67047cafb9e289b4f33cc507b"
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 每分钟魔法值恢复增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    associate = [{"type":"*skillRation","data":data1}]


# 冰刃 · 波动剑
# swordman_male/asura/ade01c1d6afc8a05055225045e89fe49
# 41f1cdc2ff58bb5fdc287be0db2a8df3/ade01c1d6afc8a05055225045e89fe49
class Skill10(ActiveSkill):
    """
    发射沿着地面移动的冰柱。\n
    使命中的敌人进入冰冻状态。\n
    施放时， 生成1个波动刻印。\n
    在决斗场中， 武器的攻击属性不影响技能的攻击属性。
    """
    name = "冰刃 · 波动剑"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 7
    mp = [27, 308]
    uuid = "ade01c1d6afc8a05055225045e89fe49"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 冰柱攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 9
    # 冰柱多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 冰柱生成数量 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [冰冻效果]
    # 冰冻几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 冰冻持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 冰柱大小比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)


# 无尽波动
# swordman_male/asura/d0cdaca82892e54097f22a1f60817048
# 41f1cdc2ff58bb5fdc287be0db2a8df3/d0cdaca82892e54097f22a1f60817048
class Skill11(ActiveSkill):
    """
    向敌人喷射强烈的波动， 使周围敌人持续受到伤害。\n
    挑衅周围的敌人， 将攻击集中到自己身上。\n
    增加周围队友的物理暴击率和魔法暴击率， 并强化自身的基本攻击力和技能攻击力。\n
    施放时发动技能， 再次施放时解除攻击功能。\n
    技能施放后会持续消耗魔法值， 若魔法值不足则自动解除技能。\n
    对人类目标只能造成部分伤害。
    """
    name = "无尽波动"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 2
    cd = 5
    mp = [268, 2935]
    uuid = "d0cdaca82892e54097f22a1f60817048"
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 波动攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 波动多段攻击间隔 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 波动领域 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 波动领域高度 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 物理暴击率增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 魔法暴击率增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 基本攻击力和技能攻击力增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 人类目标伤害比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    def getSkillCD(self,mode=None):
        return 0.5


# 爆炎 · 波动剑
# swordman_male/asura/ff171dc487807bb9aa28900ca9a46b41
# 41f1cdc2ff58bb5fdc287be0db2a8df3/ff171dc487807bb9aa28900ca9a46b41
class Skill12(ActiveSkill):
    """
    引发火焰连锁爆炸。\n
    使命中的敌人进入灼伤状态。\n
    施放时， 生成1个波动刻印。
    """
    name = "爆炎 · 波动剑"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [130, 1092]
    uuid = "ff171dc487807bb9aa28900ca9a46b41"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆炸攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 爆炸多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [灼伤效果]
    # 灼伤攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 3
    # 灼伤几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 灼伤持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 爆炸大小比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [爆炎 · 波动剑]\n
        将火焰之息注入剑中发出剑气\n
        - 总攻击力相同\n
        施放时波动刻印生成数量额外 +2个\n
        [暗天波动眼]发动时， 不适用效果
        """
        ...

    def vp_2(self):
        """
        [爆炎 · 波动剑]\n
        施放时消耗波动刻印， 获得移动速度增加增益\n
        - 增益持续时间 : 7.5秒\n
        - 每个波动刻印移动速度增加5% (最多叠加3次)\n
        删除施放时生成波动刻印的功能\n
        爆炸范围 +20%\n
        [暗天波动眼]发动时， 不适用效果
        """
        ...

# 无双波
# swordman_male/asura/1721e94897e9961d5c98130a13392f17
# 41f1cdc2ff58bb5fdc287be0db2a8df3/1721e94897e9961d5c98130a13392f17
class Skill13(ActiveSkill):
    """
    可在[无尽波动]状态下施放。\n
    施放时， 在前方生成波动裂缝吸附周围的敌人。 施放过程中再次按技能键， 可发动终结爆炸。\n
    施放时， 可以预输入追加操作。\n
    施放过程中可以强制中断并施放[不动明王阵]\n
    在决斗场中， 无法连接施放[不动明王阵]。
    """
    name = "无双波"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [140, 1176]
    uuid = "1721e94897e9961d5c98130a13392f17"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 波动爆炸攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 波动裂痕大小比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [无双波]\n
        在前方生成波动裂缝后， 角色可以行动\n
        可以强制中断波动剑技能的施放后僵直并施放\n
        - 适用技能 : [冰刃 · 波动剑]、 [爆炎 · 波动剑]\n
        波动裂缝大小 +20%
        """
        ...

    def vp_2(self):
        """
        [无双波]\n
        施放时消耗波动刻印， 获得增加回避率的增益效果\n
        - 增益持续时间 : 10秒\n
        - 每个波动刻印回避率增加5% (最多叠加3次)\n
        施放过程中所受伤害 -90%
        """
        ...



# 邪光波动阵
# swordman_male/asura/c61f5a010370101402b05b21916c2071
# 41f1cdc2ff58bb5fdc287be0db2a8df3/c61f5a010370101402b05b21916c2071
class Skill14(ActiveSkill):
    """
    用剑下劈并形成波动， 对命中的敌人造成伤害并生成圆形波动阵。\n
    可以强制中断施放后僵直并施放[无双波]。\n
    在决斗场中， 攻击失败时僵直时间会增加， 无法连接[无双波]。
    """
    name = "邪光波动阵"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [180, 1512]
    uuid = "c61f5a010370101402b05b21916c2071"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 波动攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 波动阵攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 7
    # 波动阵多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 波动阵持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 波动阵爆炸攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # [范围信息]
    # 波动范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [邪光波动阵]\n
        命中时， 波动阵立即爆炸\n
        - 总攻击力相同\n
        命中时， 生成最大数量的波动刻印\n
        可以强制中断施放后僵直并施放[波动爆发]\n
        波动范围 +25%
        """
        ...

    def vp_2(self):
        """
        [邪光波动阵]\n
        对命中的最强敌人降下落雷， 并在一定范围内生成波动阵\n
        - 未命中敌人时无法施放技能\n
        - 总攻击力相同\n
        转职技能命中时， 可以施放[邪光波动阵]\n
        - 删除施放动作
        """
        ...

# 不动明王阵
# swordman_male/asura/b3659936a9a74c4ed6f7faf07cca1f9e
# 41f1cdc2ff58bb5fdc287be0db2a8df3/b3659936a9a74c4ed6f7faf07cca1f9e
class Skill15(ActiveSkill):
    """
    拥有1个以上波动刻印时， 可消耗波动刻印发动。\n
    在前方生成波动阵， 强控敌人后， 释放不动明王之焰珠在波动阵周围旋转后爆炸。\n
    消耗波动刻印数量越多， 攻击力越高。\n
    施放中按跳跃键， 则焰珠会立即爆炸。\n
    在决斗场中， 无法使用立即爆炸功能。
    """
    name = "不动明王阵"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [400, 3360]
    uuid = "b3659936a9a74c4ed6f7faf07cca1f9e"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501
    # 焰珠旋转攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 15
    # 焰珠旋转多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 焰珠爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 5个波动印时， 攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 4个波动印时， 攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 3个波动印时， 攻击力增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 2个波动印时， 攻击力增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 1个波动印时， 攻击力增加率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [范围信息]
    # 波动阵大小比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

    def vp_1(self):
        """
        [不动明王阵]\n
        施放时进入无敌状态\n
        波动阵大小 +20%
        """
        ...

    def vp_2(self):
        """
        [不动明王阵]\n
        在前方生成波动阵后角色可以行动\n
        球体旋转时间 -20%
        """
        ...


# 心眼
# swordman_male/asura/2391a27457b5a8c6fa4b4670a91bdd11
# 41f1cdc2ff58bb5fdc287be0db2a8df3/2391a27457b5a8c6fa4b4670a91bdd11
class Skill16(PassiveSkill):
    """
    用心神洞察万物， 可以增加自身的回避率， 效果持续一定时间。\n
    随着[心眼]技能等级提升， 增加基本攻击力、 技能攻击力和命中率。\n
    进入地下城时， 自动施放[波动刻印]。
    """
    name = "心眼"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 3
    uuid = "2391a27457b5a8c6fa4b4670a91bdd11"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 增加回避率效果冷却时间  : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 回避率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 转职技能攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 基本攻击、 [裂波斩]、 [地裂 · 波动剑]技能攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 命中率增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    data0 = [0, 4.5, 6, 7.5, 9, 10.5, 12, 13.5, 15, 16.5, 18, 19.5, 21, 22.5, 24, 25.5, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95]# noqa: E501

    data1 = [0, 16, 17.5, 19, 20.5, 22, 23.5, 25, 26.5, 28, 29.5, 31, 32.5, 34, 35.5, 37, 38.5, 40.5, 42.5, 44.5, 46.5, 48.5, 50.5, 52.5, 54.5, 56.5, 58.5, 60.5, 62.5, 64.5, 66.5, 68.5, 70.5, 72.5, 74.5, 76.5, 78.5, 80.5, 82.5, 84.5, 86.5, 88.5, 90.5, 92.5, 94.5, 96.5, 98.5, 100.5, 102.5, 104.5, 106.5]# noqa: E501

    associate = [
        {"type":"*skillRation","data":data2,"exceptSkills":["地裂 · 波动剑"]},
        {"type":"*skillRation","data":data3,"skills":["地裂 · 波动剑"]},
    ]


# 暗天波动眼
# swordman_male/asura/d53301bb328baf12a3ae482cc6a565dd
# 41f1cdc2ff58bb5fdc287be0db2a8df3/d53301bb328baf12a3ae482cc6a565dd
class Skill17(ActiveSkill):
    """
    只能在[无尽波动]状态下使用。\n
    创造持续一段时间的波动领域， 强化自身， 削弱敌人。\n
    一段时间后， 领域内部出现无数眼睛， 引发爆炸后领域结束。\n
    再次按技能键， 可发动终结爆炸。\n
    降低领域内敌人的命中率， 并使敌人进入减速状态。\n
    领域维持期间， 基本攻击和部分波动剑技能会产生变化。\n
    [波动剑 · 刺轮]\n
    基本攻击第3击时， 生成向前滚动的刺轮。\n
    [波动剑 · 光翼]\n
    变更[地裂 · 波动剑]， 向敌人发出交叉的光翼攻击。\n
    [波动剑 · 天照]\n
    变更[冰刃 · 波动剑]， 地面产生尖锐的尖刺， 并生成波动刻印。\n
    [波动剑 · 闪枪]\n
    变更[爆炎 · 波动剑]， 在敌人背后生成一定数量的长枪并使其极速穿刺前方敌人， 并生成波动刻印。\n
    转职技能施放过程中， 可以发动[暗天波动眼]终结攻击。\n
    减少命中率的技能效果叠加时， 只适用数值最高的效果。
    """
    name = "暗天波动眼"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 5
    cube = 7
    cd = 140
    mp = [1500, 12600]
    uuid = "d53301bb328baf12a3ae482cc6a565dd"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


    # 增益持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 命中率减少范围 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 命中率减少 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最后一击攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [基本攻击信息]
    # 第1次基本攻击攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 第2次基本攻击攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 第3次基本攻击攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 波动剑 · 刺轮攻击力 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 波动剑 · 刺轮多段攻击次数 : {value8}次
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [波动剑技能信息]
    # 波动剑 · 光翼冷却时间 : {value9}秒
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 波动剑 · 天照冷却时间 : {value10}秒
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 波动剑 · 闪枪冷却时间 : {value11}秒
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 波动剑 · 光翼攻击力 : {value12}
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 波动剑 · 天照攻击力 : {value13}
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # 波动剑 · 天照多段攻击次数 : {value14}次
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # 波动剑 · 闪枪攻击力 : {value15}
    data15 = get_data(f'{prefix}/{uuid}', 15)
    # 波动剑 · 闪枪多段攻击次数 : {value16}次
    data16 = get_data(f'{prefix}/{uuid}', 16)
    # [减速效果]
    # 减速范围 : {value17}px
    data17 = get_data(f'{prefix}/{uuid}', 17)
    # 减速几率 : {value18}%
    data18 = get_data(f'{prefix}/{uuid}', 18)
    # 减速持续时间 : {value19}秒
    data19 = get_data(f'{prefix}/{uuid}', 19)
    # 减速攻击速度减少率 : {value20}%
    data20 = get_data(f'{prefix}/{uuid}', 20)

    mode = ['开眼','平X','光翼','天照','闪枪']

    def setMode(self, mode):
        if mode == "开眼":
            self.hit3 = 1
        else:
            self.hit3 = 0
        if mode == "平X":
            self.hit4 = self.hit5 = self.hit6 = 1
            self.hit7 = 10
        elif mode == "光翼":
            self.hit12 = 1
            self.cd = 1.2
        elif mode == "天照":
            self.hit13 = 5
            self.cd = 2
        elif mode == "闪枪":
            self.hit15 = 7
            self.cd = 4.9

    def getSkillCD(self,mode=None):
        if mode == "光翼":
            pre = self.char.GetSkillByName("地裂 · 波动剑")
            return 1.2 * pre.getSkillCD(mode) / pre.cd
        elif mode == "天照":
            pre = self.char.GetSkillByName("冰刃 · 波动剑")
            return 2 * pre.getSkillCD(mode) / pre.cd
        elif mode == "闪枪":
            pre = self.char.GetSkillByName("爆炎 · 波动剑")
            return 4.9 * pre.getSkillCD(mode) / pre.cd
        elif mode == "平X":
            return 1.0
        else:
            return super().getSkillCD(mode)

# 极冰 · 裂波剑
# swordman_male/asura/7cf17936a039b418660424125dc968d7
# 41f1cdc2ff58bb5fdc287be0db2a8df3/7cf17936a039b418660424125dc968d7
class Skill18(ActiveSkill):
    """
    发射分裂为三叉戟形状的强化冰柱掠过地面。\n
    使命中的敌人进入冰冻状态。
    """
    name = "极冰 · 裂波剑"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [400, 1120]
    uuid = "7cf17936a039b418660424125dc968d7"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    vps = [
          {
            "name": "极冰剑 : 绝对零度",
            "desc": "增加立即爆炸功能<br/>范围增加",
            "explain": "[极冰 · 裂波剑]<br/>生成冰柱后再次按技能键时直接爆炸<br/><br/>冰柱生成数量 + 3个<br/>冰柱大小 + 30%<br/>冰柱爆炸范围 + 30%"
          },
          {
            "name": "冰花盛开",
            "desc": "攻击力和冷却时间增加",
            "explain": "[极冰 · 裂波剑]<br/>将剑插入地面后， 以魔法阵为中心展开冰花后同时发生爆炸<br/>- 基本冷却时间变更为40秒<br/>- 总攻击力 100%"
          }
        ]

    # 冰柱攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 冰柱多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 冰柱生成数量 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 冰柱爆炸攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 5
    # 冰柱爆炸多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [冰冻效果]
    # 冰冻几率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 冰冻持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 冰柱大小比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 冰柱爆炸大小比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

    def vp_1(self):
        """
        [极冰 · 裂波剑]\n
        生成冰柱后再次按技能键时直接爆炸\n
        冰柱生成数量 +3个\n
        冰柱大小 +30%\n
        冰柱爆炸范围 +30%
        """
        ...

    def vp_2(self):
        """
        [极冰 · 裂波剑]\n
        将剑插入地面后， 以魔法阵为中心展开冰花后同时发生爆炸\n
        - 基本冷却时间变更为40秒\n
        - 总攻击力 +100%
        """
        self.cd = 40
        self.skillRation *= 2
        ...


# 极炎 · 裂波剑
# swordman_male/asura/b89c9ab317bc0a443f6497b7cca2f6a8
# 41f1cdc2ff58bb5fdc287be0db2a8df3/b89c9ab317bc0a443f6497b7cca2f6a8
class Skill19(ActiveSkill):
    """
    挥舞蕴含火焰气息的剑， 气息渗入地面生成火焰地带后， 引发剧烈爆炸。\n
    使命中的敌人进入灼伤状态。\n
    火焰地带内的敌人会进入减速状态。
    """
    name = "极炎 · 裂波剑"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [800, 1680]
    uuid = "b89c9ab317bc0a443f6497b7cca2f6a8"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 火焰地带持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 火焰地带多段攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 8
    # 火焰地带多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 火焰爆炸攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 4
    # 火焰爆炸多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [灼伤效果]
    # 灼伤攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 灼伤几率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 灼伤持续时间 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [减速效果]
    # 减速持续时间 : {value8}秒
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 减速移动速度减少率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 减速攻击速度减少率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # [范围信息]
    # 火焰地带大小比率 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)

    vps = [
          {
            "name": "极炎爆裂剑",
            "desc": "攻击时间减少<br/>可多次发动",
            "explain": "[极炎 · 裂波剑]<br/>删除火焰地带， 变更为立即发生火焰爆炸的技能<br/>- 总攻击力 -50%<br/><br/>变更为可填充2次的技能<br/>- 每次填充冷却时间 : 25秒"
          },
          {
            "name": "爆炎修罗道",
            "desc": "可以同时使用[爆炎 · 波动剑]<br/>范围增加",
            "explain": "[极炎 · 裂波剑]<br/>发动火焰地带中施放[爆炎 · 波动剑]时， 引发强化的火焰爆炸<br/>- 删除[爆炎 · 波动剑]施放动作， 并入攻击力<br/><br/>火焰地带大小 + 50%<br/><br/>灼伤持续时间 + 2秒<br/>减速持续时间 +4秒"
          }
        ]

    def vp_1(self):
        """
        [极炎 · 裂波剑]\n
        删除火焰地带， 立即发生火焰爆炸\n
        - 总攻击力 -50%\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 25秒
        """
        self.cd = 25
        self.skillRation *= 0.5
        ...

    def vp_2(self):
        """
        [极炎 · 裂波剑]\n
        火焰地带发动过程中施放[爆炎 · 波动剑]时， 引发强化的火焰爆炸\n
        - 删除[爆炎 · 波动剑]施放动作， 合算攻击力\n
        火焰地带大小 +50%\n
        灼伤持续时间 +2秒\n
        减速持续时间 +4秒
        """
        ...


# 雷神之息
# swordman_male/asura/949849d5791944973d60af7e2a7eefb0
# 41f1cdc2ff58bb5fdc287be0db2a8df3/949849d5791944973d60af7e2a7eefb0
class Skill20(ActiveSkill):
    """
    降下蕴含雷神气息的落雷， 每隔一段时间攻击周围的敌人。\n
    雷神的气息攻击功能只有在激活无尽波动攻击功能时适用。\n
    增加基本攻击力和技能攻击力， 部分技能附加额外效果。\n
    [极冰 · 裂波剑]\n
    冰柱攻击时， 强制控制3秒敌人。\n
    [极炎 · 裂波剑]\n
    攻击时， 强制控制3秒敌人。\n
    令特定技能变为光属性， 攻击时使敌人进入感电状态。\n
    [适用技能]\n
    [裂波斩]、 [鬼印珠]、 [地裂 · 波动剑]、 [邪光斩]、 [修罗邪光斩]、 [波动爆发]、 [冰刃 · 波动剑]、 [爆炎 · 波动剑]、 [邪光波动阵]、 [邪光波动阵]、 [极冰 · 裂波剑]、 [极炎 · 裂波剑]、 [雷神之息]
    """
    name = "雷神之息"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    type = 'passive'
    uuid = "949849d5791944973d60af7e2a7eefb0"
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    hasVP = False

    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 落雷攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 落雷冷却时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 基本攻击力和技能攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [攻击时感电效果]
    # 感电攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 感电几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 感电持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)

    associate = [{"type":"*skillRation","data":data2}]

    def getSkillCD(self,mode=None):
        return 2.5


# 天雷 · 波动剑
# swordman_male/asura/e1daab884dd07fc9e70d08b83d1790eb
# 41f1cdc2ff58bb5fdc287be0db2a8df3/e1daab884dd07fc9e70d08b83d1790eb
class Skill21(ActiveSkill):
    """
    向目标挥动波动剑， 在一定时间内对敌人生成波动珠， 持续一段时间后爆炸。\n
    最少生成3个波动珠， 并随着波动印的数量增加。\n
    如果存在2个以上的波动珠， 则波动珠之间会相互连接。\n
    再次按技能键， 可引发爆炸。\n
    施放技能时， 可以生成波动印。\n
    攻击时， 附加感电状态、
    """
    name = "天雷 · 波动剑"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "天雷·波动剑"
    uuid = "e1daab884dd07fc9e70d08b83d1790eb"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 波动珠攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 波动珠多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 波动珠爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [感电效果]
    # 感电攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 6
    # 感电几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 感电持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 波动阵大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 波动珠爆炸大小比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    def vp_1(self):
        """
        [天雷 · 波动剑]\n
        在魔法阵中生成波动珠并引发爆炸\n
        - 总攻击力相同\n
        命中时生成数量上限的波动刻印
        """
        ...

    def vp_2(self):
        """
        [天雷 · 波动剑]\n
        增加命中时控制敌人的功能； 消耗波动刻印， 增加波动珠爆炸后的控制持续时间\n
        - 每个波动刻印的控制持续时间 +0.6秒 (最多叠加5次)\n
        - 删除施放时生成波动刻印的功能\n
        可以强制中断[邪光波动阵]的施放后僵直并施放\n
        施放时初始化[邪光波动阵]的冷却时间\n
        - [邪光波动阵]攻击力 -33%\n
        波动阵大小 +20%\n
        - 波动珠爆炸大小 +20%
        """
        ...

# 天雷 · 降魔杵
# swordman_male/asura/8d996a242c5c0efd8cfe6cb4bc6defcc
# 41f1cdc2ff58bb5fdc287be0db2a8df3/8d996a242c5c0efd8cfe6cb4bc6defcc
class Skill22(ActiveSkill):
    """
    召唤出可以产生闪电的天雷云， 每隔一段时间， 天雷云还会生成闪电下落袭击敌人。\n
    降魔杵的攻击功能只能[无尽波动]攻击功能发动的状态下适用。\n
    天雷云持续时间内再次按技能键， 可将剩余的降魔杵转化为一个巨型金刚降魔杵， 砸向地面使敌人受到伤害。\n
    降魔杵的攻击可以使敌人进入感电状态。\n
    施放转职技能过程中， 可以发动[天雷 · 降魔杵]终结攻击。
    """
    name = "天雷 · 降魔杵"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "8d996a242c5c0efd8cfe6cb4bc6defcc"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 天雷云持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 降魔杵生成间隔 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 降魔杵的数量上限 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 降魔杵攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 16
    # 降魔杵多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 降魔杵的爆炸攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 降魔杵的爆炸多段攻击次数 : {value6}次
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [最后一击信息]
    # 降魔杵多段攻击次数 : {value7}次
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 巨型降魔杵攻击力 : {value8}
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 巨型降魔杵爆炸攻击力 : {value9}
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [感电效果]
    # 感电攻击力 : {value10}
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 感电几率 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 感电持续时间 : {value12}秒
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # [范围信息]
    # 降魔杵爆炸大小比率 : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13)

    mode = ['雷针','终结']

    def setMode(self, mode):
        if mode == "雷针":
            self.hit3 = self.hit10 = 6
            self.hit8 = self.hit9 = 0
        elif mode == "终结":
            self.hit3 = self.hit10 = 0
            self.hit8 = self.hit9 = 1

    def getSkillCD(self, mode=None):
        if mode == "雷针" or self.vp == 2:
            return 2
        return super().getSkillCD(mode)

    def vp_1(self):
        """
        [天雷 · 降魔杵]\n
        雷云持续时间变更为无限制\n
        - 施放时， 删除无色小晶块消耗量\n
        再次按技能键时， 在前方范围内最强敌人的位置生成雷云\n
        - 发动最后一击时， 立即适用冷却时间和无色小晶块消耗量
        """
        ...

    def vp_2(self):
        """
        [天雷 · 降魔杵]\n
        召唤红色雷云\n
        - 向范围内所有敌人发射降魔杵\n
        - 删除发动终结攻击功能\n
        - 降魔杵攻击力 +48%\n
        - 降魔杵爆炸攻击力 +48%
        """
        self.setMode('雷针')
        self.skillRation *= 1.48
        ...



# 雷神降世 : 裁决
# swordman_male/asura/087d1068ff506d090710566608a17760
# 41f1cdc2ff58bb5fdc287be0db2a8df3/087d1068ff506d090710566608a17760
class Skill23(ActiveSkill):
    """
    生成召唤阵， 强制控制周围敌人后， 雷神登场。\n
    雷神抬起手吸收周围的雷光后捶地， 雷光爆炸审判所有敌人。\n
    雷神的攻击可诱发感电， 造成光属性伤害。
    """
    name = "雷神降世 : 裁决"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [1500, 5000]
    uuid = "087d1068ff506d090710566608a17760"

    # 雷神出现时的攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 雷光爆炸攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 5
    # 雷光爆炸多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [感电效果]
    # 感电攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 25
    # 感电几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 感电持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)


# 波动视界 : 慧眼
# swordman_male/asura/854997c3bdfc3a2b498b4c4001f69e06
# 41f1cdc2ff58bb5fdc287be0db2a8df3/854997c3bdfc3a2b498b4c4001f69e06
class Skill24(PassiveSkill):
    """
    获得波动之秘技“慧眼”。\n
    增加基本攻击力和转职技能攻击力， 部分技能附加特殊效果。\n
    [修罗邪光斩]\n
    施放技能时立即以蓄气状态发动， 增加波动印生成数量。\n
    [波动爆发]\n
    可以强制中断基本攻击并立即使用[波动爆发]； 按前方向键时， 喷发波动之力， 并向前方突进。\n
    鼠标右键可开启/关闭突进功能。
    """
    name = "波动视界 : 慧眼"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "854997c3bdfc3a2b498b4c4001f69e06"

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [修罗邪光斩]施放时波动刻印额外生成数量 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"type":"*skillRation","data":data0}]


# 波动慧眼 : 无为法
# swordman_male/asura/61c8cb33dd20b4ff335e8deed70d3d9c
# 41f1cdc2ff58bb5fdc287be0db2a8df3/61c8cb33dd20b4ff335e8deed70d3d9c
class Skill25(ActiveSkill):
    """
    随着敌人无法看到的波动之纹移动， 并生成魔法阵后引发爆炸\n
    移动过程中， 按向前方向键， 可以向魔法阵的反方向移动。
    """
    name = "波动慧眼 : 无为法"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [1067, 8000]
    uuid = "61c8cb33dd20b4ff335e8deed70d3d9c"

    # 波动之纹攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 波动之纹多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 魔法阵爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1


# 波动神诀 : 万空
# swordman_male/asura/94c450d6214cafdc673f763badceeaf1
# 41f1cdc2ff58bb5fdc287be0db2a8df3/94c450d6214cafdc673f763badceeaf1
class Skill26(ActiveSkill):
    """
    阿修罗使用“慧眼”， 看到波动的流动， 掌握所有生命体的弱点。\n
    利用雷神之力凝聚成剑后下斩， 闪电沿着波纹向四方扩散后引发光属性爆炸。\n
    [三次觉醒技能]\n
    选择[暗天波动眼]使用三次觉醒技能时， [暗天波动眼]的最后天眼爆炸变更为三次觉醒技能。 三次觉醒技能在冷却中或[暗天波动眼]未激活的状态下， 无法使用三次觉醒技能。\n
    选择[雷神降世 : 裁决]使用三次觉醒技能时， 与[雷神降世 : 裁决]共享冷却时间。 [雷神降世 : 裁决]在冷却中时， 无法使用三次觉醒技能。
    """
    name = "波动神诀 : 万空"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "94c450d6214cafdc673f763badceeaf1"

    # 雷剑生成冲击波攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 闪电攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 6
    # 闪电多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 波动爆炸攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 2
    # 波动爆炸攻击次数 : 2次
    # 闪电爆炸攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1

class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'asura'
        self.nameCN = '极诣·阿修罗'
        self.role = 'swordman_male'
        self.角色 = '鬼剑士(男)'
        self.职业 = '阿修罗'
        self.jobId = '41f1cdc2ff58bb5fdc287be0db2a8df3'
        self.jobGrowId = 'c9b492038ee3ca8d27d7004cf58d59f3'

        self.武器选项 = ['太刀', '钝器', '巨剑', '短剑']
        self.输出类型选项 = ['魔法固伤']
        self.输出类型 = '魔法固伤'
        self.防具精通属性 = ['智力']
        self.防具类型 = '板甲'
        self.buff = 1.638

        super().__init__(equVersion, __name__)

