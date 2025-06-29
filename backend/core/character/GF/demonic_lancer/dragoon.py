#3deb7be5f01953ac8b1ecaa1e25e0420
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "demonic_lancer/dragoon/cn/skillDetail"

# 刺击
# demonic_lancer/dragoon/9dda3f4a849dba1a288dd65e116860f2
# 3deb7be5f01953ac8b1ecaa1e25e0420/9dda3f4a849dba1a288dd65e116860f2
class Skill0(ActiveSkill):
    """
    向前方进行普通的刺击。 用枪头击打敌人时， 可以造成更多的伤害。\n
    近距离攻击和枪头攻击不会同时命中敌人， 相应的判定重叠时， 优先判定为枪头攻击。
    """
    name = "刺击"
    learnLv = 1
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 5
    mp = [6, 40]
    uuid = "9dda3f4a849dba1a288dd65e116860f2"
    hasVP = False
    hasUP = False

    # 近距离攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 枪头攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 枪头攻击判定距离 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    mode = ["枪头","近距离"]

    def setMode(self, mode):
        if mode == "枪头":
            self.hit0 = 0
            self.hit1 = 1
        elif mode == "近距离":
            self.hit0 = 1
            self.hit1 = 0

# 枪挑
# demonic_lancer/dragoon/0969cd4054d93da07708108c0cc1c4b5
# 3deb7be5f01953ac8b1ecaa1e25e0420/0969cd4054d93da07708108c0cc1c4b5
class Skill1(ActiveSkill):
    """
    从下往上挑击， 使敌人浮空。
    """
    name = "枪挑"
    learnLv = 1
    masterLv = 10
    maxLv = 20
    position = 8
    rangeLv = 3
    cd = 2
    uuid = "0969cd4054d93da07708108c0cc1c4b5"
    hasVP = False
    hasUP = False

    # 挑击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 浮空力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)


# 基础精通
# demonic_lancer/dragoon/5a56514f35cf0270ae8d6c65f8fefd78
# 3deb7be5f01953ac8b1ecaa1e25e0420/5a56514f35cf0270ae8d6c65f8fefd78
class Skill3(PassiveSkill):
    """
    增加基本攻击、 前冲攻击、 跳跃攻击、 [枪挑]的攻击力。\n
    在决斗场中， 增益/减益技能、 被动技能的技能攻击力增加效果对[基础精通]无影响。
    """
    name = "基础精通"
    learnLv = 1
    masterLv = 190
    maxLv = 200
    position = 1
    rangeLv = 1
    uuid = "5a56514f35cf0270ae8d6c65f8fefd78"
    icon = "$common/$uuid"
    hasVP = False
    hasUP = False

    # 基本攻击力变化率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 前冲攻击力变化率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 跳跃攻击力变化率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    associate = [{"type":"*skillRation","data":[i-100 if i>0 else 0 for i in data0],"skills":["猎杀枪"]}]


# 回旋钩
# demonic_lancer/dragoon/eb71e1d82d92c7e1d40500a0dcd77aa6
# 3deb7be5f01953ac8b1ecaa1e25e0420/eb71e1d82d92c7e1d40500a0dcd77aa6
class Skill6(ActiveSkill):
    """
    用枪把敌人钩过来后， 再次扔出。\n
    被扔出的敌人会受到冲撞伤害， 并且碰到墙壁时， 会反弹回来。\n
    对无法抓取的敌人不适用控制效果。
    """
    name = "回旋钩"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 9
    rangeLv = 2
    cd = 7
    mp = [20, 300]
    uuid = "eb71e1d82d92c7e1d40500a0dcd77aa6"
    hasVP = False
    hasUP = False

    # 被扔时的冲撞伤害 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 撞到墙壁、 地面时的冲撞伤害 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [学习帝国枪术后]
    # 可抓取的敌人数量 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    mode = ["可抓取","不可抓取"]

    def setMode(self, mode):
        if mode == "可抓取":
            self.hit0 = 1
        elif mode == "不可抓取":
            self.hit0 = 0

# 格挡反击
# demonic_lancer/dragoon/4655101518604f874721b3cc249aae10
# 3deb7be5f01953ac8b1ecaa1e25e0420/4655101518604f874721b3cc249aae10
class Skill7(ActiveSkill):
    """
    斜架长枪抵抗来自前方的攻击。\n
    受到的伤害越多， 接受攻击时被推开的距离越远。\n
    被推开一定距离后， 按下X键可以进行反击。
    """
    name = "格挡反击"
    learnLv = 10
    masterLv = 1
    maxLv = 10
    position = 8
    rangeLv = 2
    cd = 6
    mp = [4, 5]
    uuid = "4655101518604f874721b3cc249aae10"
    hasVP = False
    hasUP = False

    # 反击的攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 所受伤害减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 落凤枪
# demonic_lancer/dragoon/c9664191611af31142e052dfaef84530
# 3deb7be5f01953ac8b1ecaa1e25e0420/c9664191611af31142e052dfaef84530
class Skill8(ActiveSkill):
    """
    从空中快速地斜向落地， 刺向敌人。
    """
    name = "落凤枪"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 4.5
    mp = [12, 125]
    uuid = "c9664191611af31142e052dfaef84530"
    hasVP = False
    hasUP = False

    # 落地攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 地面爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # [范围信息]
    # 爆炸范围 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 横扫
# demonic_lancer/dragoon/fc7a3f4c2852c832a2f20af63d5d212f
# 3deb7be5f01953ac8b1ecaa1e25e0420/fc7a3f4c2852c832a2f20af63d5d212f
class Skill9(ActiveSkill):
    """
    向前方快速横斩， 击飞敌人。
    """
    name = "横扫"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 0
    rangeLv = 2
    cd = 4
    mp = [8, 70]
    uuid = "fc7a3f4c2852c832a2f20af63d5d212f"
    hasVP = False
    hasUP = False

    # 横斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1

# 魔枪发射
# demonic_lancer/dragoon/51a08fd0c90f0a5276cd552047fac93d
# 3deb7be5f01953ac8b1ecaa1e25e0420/51a08fd0c90f0a5276cd552047fac93d
class Skill10(ActiveSkill):
    """
    将气息聚集到魔枪尖端， 然后投掷魔枪。\n
    魔法枪对命中的敌人造成多段伤害后消失。
    """
    name = "魔枪发射"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 4.5
    mp = [10, 115]
    uuid = "51a08fd0c90f0a5276cd552047fac93d"
    hasVP = False
    hasUP = False

    # 魔法枪多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 4
    # 魔法枪多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)


# 连环枪
# demonic_lancer/dragoon/717f1e2104fe4b796f800352fa143ecc
# 3deb7be5f01953ac8b1ecaa1e25e0420/717f1e2104fe4b796f800352fa143ecc
class Skill13(ActiveSkill):
    """
    使用长枪进行连续攻击。 命中敌人时按下技能键， 即刻发动下一次攻击。
    """
    name = "连环枪"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 1
    rangeLv = 2
    cd = 6
    mp = [13, 120]
    uuid = "717f1e2104fe4b796f800352fa143ecc"
    hasVP = False
    hasUP = True

    # 命中敌人后， 即刻发动下一攻击所需的按键间隔 : 0.5秒
    # 横斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 上挑攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 向上攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 下刺攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # 敌人的僵直增加量 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

# 扫堂枪
# demonic_lancer/dragoon/128b9ddef2262f40723deae4407bdb42
# 3deb7be5f01953ac8b1ecaa1e25e0420/128b9ddef2262f40723deae4407bdb42
class Skill14(ActiveSkill):
    """
    攻击敌人足部， 使之倒地。
    """
    name = "扫堂枪"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 0
    rangeLv = 2
    cd = 5
    mp = [12, 120]
    uuid = "128b9ddef2262f40723deae4407bdb42"
    hasVP = False
    hasUP = True

    # 横斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1

# 狩猎技艺
# demonic_lancer/dragoon/147d005ac868e0de52b1f255eea35d62
# 3deb7be5f01953ac8b1ecaa1e25e0420/147d005ac868e0de52b1f255eea35d62
class Skill15(PassiveSkill):
    """
    基本攻击、 前冲攻击、 后跳、 跳跃攻击变更为狩猎魔兽专用的狩猎者固有枪术。
    """
    name = "狩猎技艺"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 5
    rangeLv = 2
    uuid = "147d005ac868e0de52b1f255eea35d62"
    hasVP = False
    hasUP = False

# 光枪精通
# demonic_lancer/dragoon/47bd4871f29defc2a0021ee9261d7a5b
# 3deb7be5f01953ac8b1ecaa1e25e0420/47bd4871f29defc2a0021ee9261d7a5b
class Skill16(PassiveSkill):
    """
    增加武器的魔法攻击力， 装备光枪时， 提升对武器的熟练度， 增加攻击速度和魔法暴击率。
    """
    name = "光枪精通"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 9
    rangeLv = 3
    uuid = "47bd4871f29defc2a0021ee9261d7a5b"
    hasVP = False
    hasUP = False

    # 魔法武器攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 攻击速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 魔法暴击率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    associate = [ {"type":"$*PAtkM","data":data0}, ]

# 猎杀枪
# demonic_lancer/dragoon/8510294202d0e042dd29a2422fc6770d
# 3deb7be5f01953ac8b1ecaa1e25e0420/8510294202d0e042dd29a2422fc6770d
class Skill17(ActiveSkill):
    """
    生成基本攻击或施放技能时可以发射的魔法枪。\n
    施放[鹰坠]和1、 2、 3次觉醒技能时无法发射， 有生成数量限制和发射冷却时间。\n
    魔法枪击中敌人或飞出一定距离后消失。\n
    魔法枪享受[基础精通]的加成。\n
    可利用On/Off功能自动发射魔法枪。\n
    在决斗场中无法自动发射魔法枪， 且施放[格挡反击]时无法发射。
    """
    name = "猎杀枪"
    learnLv = 15
    masterLv = 1
    maxLv = 5
    position = 7
    rangeLv = 2
    mp = [6, 140]
    uuid = "8510294202d0e042dd29a2422fc6770d"
    hasVP = False
    hasUP = False
    cd = 1

    # 魔法枪再次生成时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 恢复的魔法枪数量 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 基本攻击时一次射出的魔法枪数量 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 施放技能时一次射出的魔法枪数量 : {value3}个
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 发射冷却时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 魔法枪攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    hit5 = 1

    def getSkillCD(self, mode=None):
        return self.cd

# 隐鼠之袭
# demonic_lancer/dragoon/38612d8f2561edc2eb68d5057a837bfa
# 3deb7be5f01953ac8b1ecaa1e25e0420/38612d8f2561edc2eb68d5057a837bfa
class Skill18(ActiveSkill):
    """
    从地面攻击， 释放强大的能量。\n
    被击中的敌人会浮空一定高度。\n
    对倒地的敌人也适用同样的浮空力。
    """
    name = "隐鼠之袭"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 5
    mp = [35, 350]
    uuid = "38612d8f2561edc2eb68d5057a837bfa"
    hasVP = False
    hasUP = True

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 浮空力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # 攻击范围扩大率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 光焰飞枪
# demonic_lancer/dragoon/6a1d1f08a6572be420bb3a256c44c015
# 3deb7be5f01953ac8b1ecaa1e25e0420/6a1d1f08a6572be420bb3a256c44c015
class Skill19(ActiveSkill):
    """
    投掷多支魔法枪， 对敌人造成多段伤害， 并将敌人推向后方。
    """
    name = "光焰飞枪"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 6
    mp = [50, 550]
    uuid = "6a1d1f08a6572be420bb3a256c44c015"
    hasVP = False
    hasUP = True

    # 多段攻击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 魔法攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 5
    # [范围信息]
    # 攻击范围扩大率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 狩猎本能
# demonic_lancer/dragoon/e0a072e8cef2d77893aad5f68aeed56a
# 3deb7be5f01953ac8b1ecaa1e25e0420/e0a072e8cef2d77893aad5f68aeed56a
class Skill20(PassiveSkill):
    """
    发挥猎人长期养成的狩猎本能， 增加暴击伤害和命中率。
    """
    name = "狩猎本能"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 8
    rangeLv = 3
    uuid = "e0a072e8cef2d77893aad5f68aeed56a"
    hasVP = False
    hasUP = False

    # 暴击伤害增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 命中率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    associate = [ {"data":data0,"type":"*skillRation"}]


# 能量萃取
# demonic_lancer/dragoon/669f1428193f61f9d92c743b72438c4d
# 3deb7be5f01953ac8b1ecaa1e25e0420/669f1428193f61f9d92c743b72438c4d
class Skill22(ActiveSkill):
    """
    集中精神提取魔法的力量， 提升基本攻击力和技能攻击力。
    """
    name = "能量萃取"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 2
    cd = 5
    uuid = "669f1428193f61f9d92c743b72438c4d"
    hasVP = False
    hasUP = False

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 猎杀枪 : 掠食
# demonic_lancer/dragoon/b3659936a9a74c4ed6f7faf07cca1f9e
# 3deb7be5f01953ac8b1ecaa1e25e0420/b3659936a9a74c4ed6f7faf07cca1f9e
class Skill23(ActiveSkill):
    """
    在基本攻击或技能施放过程中使用， 可以将敌人强制控制一定时间。\n
    可以在地面或空中施放。\n
    [地面版本]\n
    融合猎杀枪生成一个掠食魔法枪后， 向前方射出。\n
    魔法枪命中时能强制控制枪范围内的所有敌人。\n
    [空中版本]\n
    在空中施放时， 猎杀枪从空中坠落， 以落地位置为中心强制控制一定范围内的敌人。\n
    在决斗场中， 施放[落凤枪]时无法使用[猎杀枪 : 掠食]， 且无法在空中施放该技能。
    """
    name = "猎杀枪 : 掠食"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cd = 9
    mp = [30, 500]
    uuid = "b3659936a9a74c4ed6f7faf07cca1f9e"
    hasVP = False
    hasUP = True

    # 地面发射攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 地面发射控制时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 空中发射控制时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 空中发射攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 0

    mode = ["地面","空中"]

    def setMode(self, mode):
        if mode == "地面":
            self.hit0 = 1
            self.hit3 = 0
        elif mode == "空中":
            self.hit0 = 0
            self.hit3 = 1

# 蛮横冲撞
# demonic_lancer/dragoon/a2d943797daca862a6f321aca6ac9bfa
# 3deb7be5f01953ac8b1ecaa1e25e0420/a2d943797daca862a6f321aca6ac9bfa
class Skill24(ActiveSkill):
    """
    向前方突进， 用枪刺穿敌人并将其击退， 然后将敌人下刺向地面。\n
    突进过程中击中敌人时， 再次按技能键可以立即将敌人刺倒在地。\n
    如果突进攻击未击中敌人， 则无法追加下刺攻击。
    """
    name = "蛮横冲撞"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 8
    mp = [65, 650]
    uuid = "a2d943797daca862a6f321aca6ac9bfa"
    hasVP = False
    hasUP = True

    # 突进距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 按前方向键施放时突进距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 突进攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 下刺攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # 生成的魔法枪攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 3

# 光焰枪
# demonic_lancer/dragoon/c7bf7ccab413009640e65ca6f2f0263a
# 3deb7be5f01953ac8b1ecaa1e25e0420/c7bf7ccab413009640e65ca6f2f0263a
class Skill25(ActiveSkill):
    """
    向前方投掷贯穿一切的魔法枪， 并将敌人击飞。
    """
    name = "光焰枪"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 12
    mp = [47, 700]
    uuid = "c7bf7ccab413009640e65ca6f2f0263a"
    hasVP = False
    hasUP = False

    # 魔法枪攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1

# 猎杀枪 : 穿心
# demonic_lancer/dragoon/ecc23c980ea71450c0ad0c3fd232f329
# 3deb7be5f01953ac8b1ecaa1e25e0420/ecc23c980ea71450c0ad0c3fd232f329
class Skill26(ActiveSkill):
    """
    向前方发射猎杀枪。\n
    旋转的猎杀枪对敌人造成多段伤害， 移动到最远位置后返回并将敌人拉到特定位置。\n
    施放技能时无施放动作， 立即施放。\n
    可以在施放其他技能过程中使用， 但[落凤枪]、 [鹰坠]和1、 2、 3次觉醒技除外。\n
    跳跃时也可以使用。\n
    决斗场中无法在跳跃时使用。
    """
    name = "猎杀枪 : 穿心"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cd = 10
    mp = [30, 500]
    uuid = "ecc23c980ea71450c0ad0c3fd232f329"
    hasVP = False
    hasUP = True

    # 旋转多段攻击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 旋转时攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 6
    # 返回时攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 攻击范围扩大率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

# 利刃收割
# demonic_lancer/dragoon/1b1cfab062e0768bcc889e33e1f30dbf
# 3deb7be5f01953ac8b1ecaa1e25e0420/1b1cfab062e0768bcc889e33e1f30dbf
class Skill27(ActiveSkill):
    """
    生成魔法枪， 大范围挥舞魔法枪将敌人聚集起来， 然后将敌人向前方击退； 如果施放时按上方向键， 则会使敌人向上浮空。
    """
    name = "利刃收割"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [45, 850]
    uuid = "1b1cfab062e0768bcc889e33e1f30dbf"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 挥击攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 4
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 击退攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 上升攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 0
    # [范围信息]
    # 攻击范围扩大率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    mode = ["击退","上升"]

    def setMode(self, mode):
        if mode == "击退":
            self.hit0 = 4
            self.hit2 = 1
            self.hit3 = 0
        elif mode == "上升":
            self.hit0 = 4
            self.hit2 = 0
            self.hit3 = 1

    def vp_1(self):
        """
        [利刃收割]\n
        无法进行上升动作\n
        变更为挥动3次攻击\n
        - 每次攻击都会聚集敌人\n
        - 吸附范围 : 400px\n
        总攻击力相同
        """
        self.setMode("击退")
        ...

    def vp_2(self):
        """
        [利刃收割]\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 7.5秒\n
        - 攻击力 -50%\n
        地面施放时快速发动上升动作\n
        可以在空中施放
        """
        self.cd = 7.5
        self.skillRation *= 0.5
        ...

# 光焰囚杀
# demonic_lancer/dragoon/c77a417c43de80c4ce32c1ed405d174a
# 3deb7be5f01953ac8b1ecaa1e25e0420/c77a417c43de80c4ce32c1ed405d174a
class Skill28(ActiveSkill):
    """
    向空中释放枪的气息， 然后使其在前方落下， 生成屏障。 屏障对敌人造成多段伤害， 逐渐向中央合拢， 最后爆炸。
    """
    name = "光焰囚杀"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [45, 850]
    uuid = "c77a417c43de80c4ce32c1ed405d174a"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 屏障生成位置 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 屏障多段攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 屏障爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1

    def vp_1(self):
        """
        [光焰囚杀]\n
        可以在其他动作中施放\n
        - 跳跃状态会被视为其他动作
        """
        ...

    def vp_2(self):
        """
        [光焰囚杀]\n
        变更为向前突进和返回动作\n
        路径上的敌人会被吸附到狩猎者的前方\n
        施放技能时进入无敌状态\n
        总攻击力相同
        """
        ...

# 鹰坠
# demonic_lancer/dragoon/0b8db1e10b3abbd24d38564e708675d5
# 3deb7be5f01953ac8b1ecaa1e25e0420/0b8db1e10b3abbd24d38564e708675d5
class Skill29(ActiveSkill):
    """
    跳到空中期间， 可以用方向键调整降落位置， 然后降落到指定位置。\n
    再次按技能键可以立即降落。\n
    在跳跃过程中也可以施放该技能， 被魔法枪击中的敌人将被强制控制一定时间， 无法移动。\n
    在决斗场中， 无法强制控制被魔法枪击中的敌人， 且无法通过再次按技能键发动终结攻击。
    """
    name = "鹰坠"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [150, 1260]
    uuid = "0b8db1e10b3abbd24d38564e708675d5"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 基本降落位置 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 空中施放技能所需最低高度 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 降落冲撞攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 强制控制时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [范围信息]
    # 冲击波范围扩大率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    def vp_1(self):
        """
        [鹰坠]\n
        变更为猎杀枪发射动作\n
        - 发射出的猎杀枪会追踪前方的敌人
        """
        ...

    def vp_2(self):
        """
        [鹰坠]\n
        攻击力和冷却时间 +100%\n
        落地后短暂维持无敌状态
        """
        self.cd = 50
        self.skillRation *= 2

# 龙鳞碎割
# demonic_lancer/dragoon/852f8ad797db4dca1405cb3e77198401
# 3deb7be5f01953ac8b1ecaa1e25e0420/852f8ad797db4dca1405cb3e77198401
class Skill30(ActiveSkill):
    """
    生成多支魔法枪， 向前方敌人射出。\n
    发射指定数量的魔法枪后， 向正面的敌人发动终结攻击。\n
    终结攻击时， 按前方向键可以增加终结攻击发动距离。\n
    可以在跳跃中使用， 施放过程中可以按跳跃键强制中断。\n
    在决斗场中， 不可以在跳跃中使用。
    """
    name = "龙鳞碎割"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [250, 2500]
    uuid = "852f8ad797db4dca1405cb3e77198401"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 魔法枪发射次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 魔法枪攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 20
    # 终结攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 攻击范围扩大率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [龙鳞碎割]\n
        删除终结攻击\n
        可以在其他动作中施放\n
        总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [龙鳞碎割]\n
        删除猎杀枪攻击\n
        可以强制中断施放后僵直， 并连接部分技能\n
        [可连接技能]\n
        - [光焰枪]\n
        - [天龙破]\n
        - [凌空之狩]\n
        - [无尽毁灭]\n
        总攻击力相同
        """
        ...

# 枪魂感知
# demonic_lancer/dragoon/28b583c75a49103a1d8aabf799c000a4
# 3deb7be5f01953ac8b1ecaa1e25e0420/28b583c75a49103a1d8aabf799c000a4
class Skill31(PassiveSkill):
    """
    增加狩猎者的技能攻击力， 减少猎杀枪的重新生成时间。
    """
    name = "枪魂感知"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 3
    uuid = "28b583c75a49103a1d8aabf799c000a4"
    hasVP = False
    hasUP = False

    # 猎杀枪重新生成时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    associate = [ {"data":[-i for i in data0],"type":"+cd","skills":["猎杀枪"],"ratio":1}, {"data":data1,"type":"*skillRation"}]

# 逐云灭龙杀
# demonic_lancer/dragoon/4f2e001e9a19eb7bae50ad1840dfb329
# 3deb7be5f01953ac8b1ecaa1e25e0420/4f2e001e9a19eb7bae50ad1840dfb329
class Skill32(ActiveSkill):
    """
    射出猎杀枪， 对前方魔法阵内的敌人造成伤害并强控敌人； 然后， 跳到高空中， 以极快的速度降落， 使敌人受到巨大冲撞爆炸伤害。\n
    按住方向键可以调整降落位置。\n
    在最后的冲撞爆炸之前， 被猎杀枪击中并被强制控制的敌人会一直处于强制控制状态。
    """
    name = "逐云灭龙杀"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [980, 8232]
    uuid = "4f2e001e9a19eb7bae50ad1840dfb329"
    hasVP = False
    hasUP = False

    # 直接攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 猎杀枪多段攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 10
    # 降落冲撞爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 长按前方向键时降落位置 : 中间位置的前方300px
    # 长按后方向键时降落位置 : 中间位置的后方300px

# 天龙破
# demonic_lancer/dragoon/dcb31a63ef58954f44ff2070c42a9a98
# 3deb7be5f01953ac8b1ecaa1e25e0420/dcb31a63ef58954f44ff2070c42a9a98
class Skill33(ActiveSkill):
    """
    生成魔法枪发动乱舞攻击。\n
    乱舞后跳起将魔枪插入地面， 并使魔枪爆炸。\n
    跳跃中可以使用， 但只发动地面爆炸攻击。\n
    在地面上按住后方向键施放技能时， 在原地施放技能。
    """
    name = "天龙破"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [400, 1620]
    uuid = "dcb31a63ef58954f44ff2070c42a9a98"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 魔法枪乱舞攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 4
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 地面爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 地面爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [天龙破]\n
        乱舞攻击次数 -2次\n
        最后一击攻击范围增加\n
        空中施放时， 适用地面攻击力100%的攻击力\n
        总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [天龙破]\n
        无法在空中施放\n
        初始化[猎杀枪 : 掠食]、 [猎杀枪 : 穿心]技能的冷却时间， 并自动发动\n
        - 穿心攻击力 : 基础攻击力的74%\n
        - 掠食攻击力 : 基础攻击力的74%
        """
    def effect(self, old, new):
        if self.vp == 2:
            self.associate = [{"type":"*skillRation","data":[0] + [-26]*self.maxLv,"skills":["猎杀枪 : 穿心", "猎杀枪 : 掠食"]}]
        return super().effect(old, new)

# 地龙狩
# demonic_lancer/dragoon/8572675ec6a1f50b6eff6a867376c2de
# 3deb7be5f01953ac8b1ecaa1e25e0420/8572675ec6a1f50b6eff6a867376c2de
class Skill34(ActiveSkill):
    """
    蓄力后立即向前方突进， 突进中途撞到敌人会发出强烈的爆炸攻击， 同时狩猎者向后方跳起。\n
    施放时， 按方向键可以调整跳起的方向。\n
    跳跃中可以使用该技能， 但只能向前方地面突进， 撞到敌人也不会跳起。
    """
    name = "地龙狩"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [800, 1680]
    uuid = "8572675ec6a1f50b6eff6a867376c2de"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 突进攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # [范围信息]
    # 攻击范围扩大率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    def vp_1(self):
        """
        [地龙狩]\n
        变更为可填充2次的技能\n
        - 冷却时间 -50%\n
        - 攻击力 -50%\n
        攻击范围 +50%
        """
        self.cd = 20
        self.skillRation *= 0.5

    def vp_2(self):
        """
        [地龙狩]\n
        未命中时冷却时间缩短为 : 5秒\n
        命中时， 初始化[光焰枪]技能的冷却时间\n
        - [光焰枪]攻击力 : 基础攻击力的77%\n
        突进过程中所受伤害 -75%
        """
    def effect(self, old, new):
        if self.vp == 2:
            self.associate = [{"type":"*skillRation","data":[0] + [-23]*self.maxLv,"skills":["光焰枪"]}]
        return super().effect(old, new)

# 狩猎之心
# demonic_lancer/dragoon/2a0a39184de92acf1c1375e00b77404c
# 3deb7be5f01953ac8b1ecaa1e25e0420/2a0a39184de92acf1c1375e00b77404c
class Skill35(PassiveSkill):
    """
    领悟狩猎之心的狩猎者可以更高效地使用魔兽之力。\n
    提高基本攻击力和技能攻击力， 并增加命中率和攻击速度。
    """
    name = "狩猎之心"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    uuid = "2a0a39184de92acf1c1375e00b77404c"
    hasVP = False
    hasUP = False

    # 基本攻击和技能攻击力增加率量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 攻击速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 命中率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    associate = [ {"data":data0,"type":"*skillRation"}]

# 凌空之狩
# demonic_lancer/dragoon/9dc8438e4572d39243c97da31c113acc
# 3deb7be5f01953ac8b1ecaa1e25e0420/9dc8438e4572d39243c97da31c113acc
class Skill36(ActiveSkill):
    """
    狩猎者向前方高高跃起， 并生成一把猎杀枪进行投掷。\n
    投掷的猎杀枪插入地面， 对周围的敌人造成伤害， 随后从空中突进到猎杀枪的位置， 拔出猎杀枪并大幅度挥斩， 对周围的敌人造成伤害。\n
    施放技能时， 按向前方向键， 可以在拔枪挥斩的同时前进。\n
    跳跃期间也可以施放。
    """
    name = "凌空之狩"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "9dc8438e4572d39243c97da31c113acc"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 投掷攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0  = 1
    # 拔枪挥斩攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1

    def vp_1(self):
        """
        [凌空之狩]\n
        从空中向地面突进时进入无敌状态\n
        命中时初始化[利刃收割]的冷却时间\n
        - [利刃收割]攻击力 : 基础攻击力的73%
        """
        ...

    def vp_2(self):
        """
        [凌空之狩]\n
        变更为可多次发动的技能\n
        - 每次填充冷却时间 -50%\n
        - 每次填充攻击力 -50%\n
        施放结束时维持跳跃状态
        """
        self.cd = 20
        self.skillRation *= 0.5

    def effect(self, old, new):
        if self.vp == 1:
            self.associate = [{"type":"*skillRation","data":[0] + [-27]*self.maxLv,"skills":["利刃收割"]}]
        return super().effect(old, new)

# 无尽毁灭
# demonic_lancer/dragoon/3fb8395ae3b81bd608e0c4223a8eb534
# 3deb7be5f01953ac8b1ecaa1e25e0420/3fb8395ae3b81bd608e0c4223a8eb534
class Skill37(ActiveSkill):
    """
    快速旋转魔法枪， 生成利刃风车粉碎敌人。\n
    生成的利刃风车造成多段攻击伤害后， 飞向前方并爆炸。\n
    可以在跳跃中使用。
    """
    name = "无尽毁灭"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [600, 5000]
    uuid = "3fb8395ae3b81bd608e0c4223a8eb534"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 移动距离上限 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 利刃风车多段攻击攻击力 : {value1}% X {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 11
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 利刃风车爆炸攻击力 : {value3}% X {value4}
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # [范围信息]
    # 利刃风车大小比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)

    def vp_1(self):
        """
        [无尽毁灭]\n
        投掷出两把魔法枪\n
        总攻击力相同\n
        吸附力 +20%\n
        施放过程中所受伤害 -75%
        """
        ...

    def vp_2(self):
        """
        [无尽毁灭]\n
        变更为猎杀枪空中发射动作\n
        - 追踪前方的敌人\n
        可以在其他动作中施放
        """
        ...

# 绝命猎杀 : 死亡穿刺
# demonic_lancer/dragoon/5806440d21e7546d50007a5ba11f8024
# 3deb7be5f01953ac8b1ecaa1e25e0420/5806440d21e7546d50007a5ba11f8024
class Skill38(ActiveSkill):
    """
    融合猎杀枪和光枪生成突击枪， 给最强敌人种下印记并强制控制敌人， 然后光速跃起并发动穿刺攻击。\n
    最后将突击枪插入敌人体内， 并引发爆炸造成伤害。\n
    跳跃时也可以使用。
    """
    name = "绝命猎杀 : 死亡穿刺"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "5806440d21e7546d50007a5ba11f8024"
    hasVP = False
    hasUP = False

    # 探测范围 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 穿刺攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1

# 狩魔之魂
# demonic_lancer/dragoon/002cbdd9bfd0f0b970451ae8d48d029e
# 3deb7be5f01953ac8b1ecaa1e25e0420/002cbdd9bfd0f0b970451ae8d48d029e
class Skill39(PassiveSkill):
    """
    千魂·狩猎者成功控制暴走的利维坦之力， 将力量注入猎杀枪， 锻造出更加强大的光枪。\n
    强化在地面和空中狩猎的能力， 部分技能附加特殊效果。\n
    [蛮横冲撞] : 删除下刺攻击， 下刺攻击力并入突进攻击。 魔法枪会追踪突进攻击命中的敌人中最强大的敌人， 对该位置进行攻击。 按向前方向键可额外增加前进距离。\n
    [光焰枪] : 可以在空中施放。
    """
    name = "狩魔之魂"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "002cbdd9bfd0f0b970451ae8d48d029e"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [蛮横冲撞]按向前方向键时前进距离额外增加 : 30%

    associate = [ {"data":data0,"type":"*skillRation"}]

# 瞬光猎杀枪
# demonic_lancer/dragoon/31823197cc0b04d4c5dcf8f928d9220c
# 3deb7be5f01953ac8b1ecaa1e25e0420/31823197cc0b04d4c5dcf8f928d9220c
class Skill40(ActiveSkill):
    """
     召唤新锻造的猎杀枪后， 发射猎杀枪， 对前方多个敌人造成多段伤害。 然后， 发射的猎杀枪冲向天空， 形成巨型猎杀枪插入地面。 除觉醒技能和部分技能之外， 基本攻击和其他动作过程中也可以施放该技能。
    """
    name = "瞬光猎杀枪"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [800, 6666]
    uuid = "31823197cc0b04d4c5dcf8f928d9220c"
    hasVP = False
    hasUP = False

    # 猎杀枪多段攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0  = 10
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 巨型猎杀枪攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1

# 红月·狂狩盛宴
# demonic_lancer/dragoon/dac8d8207618150c162e4c6f9e168527
# 3deb7be5f01953ac8b1ecaa1e25e0420/dac8d8207618150c162e4c6f9e168527
class Skill41(ActiveSkill):
    """
    释放已吸收的所有魔兽之力， 重塑红月升起之日曾遭遇的最强劲敌。\n
    将自身的力量向天空发射， 化作大量猎杀枪插入地面。 然后， 捕捉最强的猎物， 释放全部力量， 以极限速度贯穿猎物。\n
    可以在跳跃中使用。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。\n
    [无数狩猎者的牺牲， 化作了我的力量。]
    """
    name = "红月·狂狩盛宴"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4027, 8055]
    uuid = "dac8d8207618150c162e4c6f9e168527"
    hasVP = False
    hasUP = False

    # 猎杀枪多段攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 3
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 贯穿攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1

class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'dragoon'
        self.nameCN = '千魂·狩猎者'
        self.role = 'demonic_lancer'
        self.角色 = '魔枪士'
        self.职业 = '狩猎者'
        self.jobId = '3deb7be5f01953ac8b1ecaa1e25e0420'
        self.jobGrowId = '6d459bc74ba73ee4fe5cdc4655400193'

        self.武器选项 = ['长枪','战戟','光枪','暗矛']
        self.输出类型选项 = ['魔法百分比']
        self.输出类型 = '魔法百分比'
        self.防具精通属性 = ['智力']
        self.防具类型 = '重甲'
        self.buff = 1.85

        super().__init__(equVersion, __name__)
