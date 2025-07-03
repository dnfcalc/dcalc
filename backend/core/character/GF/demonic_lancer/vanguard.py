#3deb7be5f01953ac8b1ecaa1e25e0420
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "demonic_lancer/vanguard/cn/skillDetail"

# 刺击
# demonic_lancer/vanguard/9dda3f4a849dba1a288dd65e116860f2
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
    position = 3
    rangeLv = 2
    cd = 5
    mp = [6, 40]
    uuid = "9dda3f4a849dba1a288dd65e116860f2"
    hasVP = False
    hasUP = False

    # 近距离攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 0
    # 枪头攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
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
# demonic_lancer/vanguard/0969cd4054d93da07708108c0cc1c4b5
# 3deb7be5f01953ac8b1ecaa1e25e0420/0969cd4054d93da07708108c0cc1c4b5
class Skill1(ActiveSkill):
    """
    从下往上挑击， 使敌人浮空。
    """
    name = "枪挑"
    learnLv = 1
    masterLv = 10
    maxLv = 20
    position = 5
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
# demonic_lancer/vanguard/5a56514f35cf0270ae8d6c65f8fefd78
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

    associate = [{"type":"*skillRation","data":[i-100 if i>0 else 0 for i in data0],"skills":["霸王戟"]}]


# 回旋钩
# demonic_lancer/vanguard/eb71e1d82d92c7e1d40500a0dcd77aa6
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
    position = 4
    rangeLv = 2
    cd = 7
    mp = [20, 300]
    uuid = "eb71e1d82d92c7e1d40500a0dcd77aa6"
    hasVP = False
    hasUP = False

    # 被扔时的冲撞伤害 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
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
# demonic_lancer/vanguard/4655101518604f874721b3cc249aae10
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
    position = 7
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
# demonic_lancer/vanguard/c9664191611af31142e052dfaef84530
# 3deb7be5f01953ac8b1ecaa1e25e0420/c9664191611af31142e052dfaef84530
class Skill8(ActiveSkill):
    """
    从空中快速地斜向落地， 刺向敌人。
    """
    name = "落凤枪"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 5
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
# demonic_lancer/vanguard/fc7a3f4c2852c832a2f20af63d5d212f
# 3deb7be5f01953ac8b1ecaa1e25e0420/fc7a3f4c2852c832a2f20af63d5d212f
class Skill9(ActiveSkill):
    """
    向前方快速横斩， 击飞敌人。
    """
    name = "横扫"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 3
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
# demonic_lancer/vanguard/51a08fd0c90f0a5276cd552047fac93d
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
    position = 1
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
# demonic_lancer/vanguard/717f1e2104fe4b796f800352fa143ecc
# 3deb7be5f01953ac8b1ecaa1e25e0420/717f1e2104fe4b796f800352fa143ecc
class Skill13(ActiveSkill):
    """
    使用长枪进行连续攻击。 命中敌人时按下技能键， 即刻发动下一次攻击。
    """
    name = "连环枪"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 8
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

# 狂暴战戟
# demonic_lancer/vanguard/0ed3148658fe37b3336ccb718dc0fdb0
# 3deb7be5f01953ac8b1ecaa1e25e0420/0ed3148658fe37b3336ccb718dc0fdb0
class Skill14(PassiveSkill):
    """
    征战者特有的枪术， 能更有破坏力地使用魔枪。 学习后， 基础攻击动作将会改变。 同时， [枪挑]将会被[上斩]代替， [上斩]技能等级受[枪挑]影响， 但是造成的伤害更高。
    """
    name = "狂暴战戟"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 0
    rangeLv = 3
    uuid = "0ed3148658fe37b3336ccb718dc0fdb0"
    hasVP = False
    hasUP = False

    # [枪挑]攻击力增加率 : 120%

# 扫堂枪
# demonic_lancer/vanguard/128b9ddef2262f40723deae4407bdb42
# 3deb7be5f01953ac8b1ecaa1e25e0420/128b9ddef2262f40723deae4407bdb42
class Skill15(ActiveSkill):
    """
    攻击敌人足部， 使之倒地。
    """
    name = "扫堂枪"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 5
    mp = [12, 120]
    uuid = "128b9ddef2262f40723deae4407bdb42"
    hasVP = False
    hasUP = True

    # 横斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1

# 霸王戟
# demonic_lancer/vanguard/78be08a3f8c834d3b06fa20c6a08c5a5
# 3deb7be5f01953ac8b1ecaa1e25e0420/78be08a3f8c834d3b06fa20c6a08c5a5
class Skill16(ActiveSkill):
    """
    强制中断基本攻击、 前冲攻击、 后跳， 并进行强力一击。 基本攻击第一击或前冲攻击后使用时， 会拉开距离并向下斩； 基本攻击第二击之后使用时， 会施放横斩； 基本攻击第三击后使用时， 角色会后退并施放强力的横斩。 使用技能时按向前方向键， 角色不会后退， 并在原地进行横斩。 可以强制中断基本攻击并施放的技能都可以强制中断[霸王戟]并施放， 且受到[基础精通]的影响。\n
    [后跳]中施放技能时有冷却时间。
    """
    name = "霸王戟"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 2
    rangeLv = 2
    mp = [3, 3]
    uuid = "78be08a3f8c834d3b06fa20c6a08c5a5"
    hasVP = False
    hasUP = False

    # 后跳中使用时冷却时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 接平x第一下
    data1 = [(i*1.091*1.051) for i in [0, 289.33]]
    hit1 = 1
    # 接平x第二下
    data2 = [(i*1.091*1.051) for i in [0, 399.60]]
    hit2 = 0
    # 接平x第三下
    data3 = [(i*1.091*1.051) for i in [0, 429.59]]
    hit3 = 0

    mode = ["下斩","横斩","强力横斩"]

    def setMode(self, mode):
        if mode == "下斩":
            self.hit1 = 1
            self.hit0 = self.hit2 = self.hit3 = 0
        elif mode == "横斩":
            self.hit2 = 1
            self.hit0 = self.hit1 = self.hit3 = 0
        elif mode == "强力横斩":
            self.hit3 = 1
            self.hit0 = self.hit1 = self.hit2 = 0

# 战戟精通
# demonic_lancer/vanguard/c61f5a010370101402b05b21916c2071
# 3deb7be5f01953ac8b1ecaa1e25e0420/c61f5a010370101402b05b21916c2071
class Skill17(PassiveSkill):
    """
    征战者手握魔枪后， 把体内的破坏欲与潜力全都激发出来， 把攻击性最大化， 产生强大的破坏力。\n
    [装备战戟时的效果]\n
    减少魔法值消耗量。\n
    增加攻击速度和命中率。\n
    [基础效果]\n
    增加物理攻击力， 攻击过程中遭受一定伤害以下的攻击时， 不会僵直。 (可以开启与关闭)
    """
    name = "战戟精通"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 3
    uuid = "c61f5a010370101402b05b21916c2071"
    hasVP = False
    hasUP = False

    # 物理武器攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 装备战戟时， 攻击速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 装备战戟时， 命中率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 装备战戟时， 魔法值消耗减少率 : 20%
    # 被普通怪物攻击时， 不会僵直的伤害量上限 : 生命值最大值的{value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 被稀有怪物攻击时， 不会僵直的伤害量上限 : 生命值最大值的{value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 被领主怪物攻击时， 不会僵直的伤害量上限 : 生命值最大值的{value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)

    associate = [ {"type":"$*PAtkP","data":data0}]

# 破军突击
# demonic_lancer/vanguard/c27418ae613c647527200a7ca17d97fd
# 3deb7be5f01953ac8b1ecaa1e25e0420/c27418ae613c647527200a7ca17d97fd
class Skill18(ActiveSkill):
    """
    进行强力的突进攻击。 按下向前方向键可以突进更远的距离， 按上/下方向键会以对角线的轨迹突进。\n
    被最后一击命中的敌人会进入眩晕状态。
    """
    name = "破军突击"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 5
    mp = [12, 200]
    uuid = "c27418ae613c647527200a7ca17d97fd"
    hasVP = False
    hasUP = True

    # 多段打击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 5
    # 多段攻击次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 眩晕几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 眩晕持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

# 不灭战戟
# demonic_lancer/vanguard/de3fea2d65c597f4d55c70a02b97fc79
# 3deb7be5f01953ac8b1ecaa1e25e0420/de3fea2d65c597f4d55c70a02b97fc79
class Skill19(ActiveSkill):
    """
    瞬间解放为了不被魔枪支配而抑制的魔枪之力， 在一段时间内使自身的破坏力极大化。\n
    增加物理暴击率和暴击伤害。
    """
    name = "不灭战戟"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 3
    cd = 5
    uuid = "de3fea2d65c597f4d55c70a02b97fc79"
    hasVP = False
    hasUP = False

    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 暴击伤害增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 物理暴击率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)


# 追魂斩
# demonic_lancer/vanguard/01384bbfc346775d1267fa0bc4ca605f
# 3deb7be5f01953ac8b1ecaa1e25e0420/01384bbfc346775d1267fa0bc4ca605f
class Skill21(ActiveSkill):
    """
    向前方施放两段强力的横斩。 被击中的敌人会进入短暂的僵直。 按向前方向键施放技能， 可以前进更远的距离并施放横斩。
    """
    name = "追魂斩"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 6
    mp = [15, 300]
    uuid = "01384bbfc346775d1267fa0bc4ca605f"
    hasVP = False
    hasUP = True

    # 横斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # [范围信息]
    # 斩击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 战戟猛攻
# demonic_lancer/vanguard/92360eab6e1f378902018eca681ac629
# 3deb7be5f01953ac8b1ecaa1e25e0420/92360eab6e1f378902018eca681ac629
class Skill22(ActiveSkill):
    """
    突破极限， 其他技能命中敌人后可以强制中断并施放[战戟猛攻]， 发动强力一击。(觉醒技能除外)\n
    相反， 也可以在[战戟猛攻]命中敌人后强制中断并使用其他技能。\n
    [战戟猛攻]只能按现有的能量层数使用， 消耗的能量层数在能量蓄满后恢复。施放技能时按向前方向键， 会向前前进。 一直按住技能键会维持攻击准备状态， 所受伤害也会减少。\n
    使用[霸王戟]或[战戟猛攻]攻击敌人时， 会在一段时间内增加物理攻击力和生命值最大值。\n
    在决斗场不会增加生命值最大值。
    """
    name = "战戟猛攻"
    learnLv = 25
    masterLv = 20
    maxLv = 30
    position = 2
    rangeLv = 3
    uuid = "92360eab6e1f378902018eca681ac629"
    hasVP = False
    hasUP = False
    type = "passive"
    cd = 3

    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 所受伤害减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 增益效果持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 物理攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 生命值最大值增加 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 能量层数 : 2
    # 能量恢复时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # [范围信息]
    # 斩击范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

    associate = [ {"type":"$*PAtkP","data":data3}]

    def getSkillCD(self, mode=None):
        return self.cd

# 落月斩
# demonic_lancer/vanguard/dc1ffbe7bfcc6dc2be737951960da9ad
# 3deb7be5f01953ac8b1ecaa1e25e0420/dc1ffbe7bfcc6dc2be737951960da9ad
class Skill23(ActiveSkill):
    """
    跳跃后， 强力下劈攻击敌人。 施放技能时按向前方向键， 可以跳跃更远的距离进行下劈。
    """
    name = "落月斩"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 7
    mp = [30, 350]
    uuid = "dc1ffbe7bfcc6dc2be737951960da9ad"
    hasVP = False
    hasUP = True

    # 下劈攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # [范围信息]
    # 下斩范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 冷血突刺
# demonic_lancer/vanguard/e49e57b2e8fbeceb0a2c56a0c63fe6c5
# 3deb7be5f01953ac8b1ecaa1e25e0420/e49e57b2e8fbeceb0a2c56a0c63fe6c5
class Skill24(ActiveSkill):
    """
    聚集力量， 向前方施放破坏性刺击。 被击中的敌人会被击退， 并受到多段伤害。
    """
    name = "冷血突刺"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cube = 1
    cd = 16
    mp = [100, 920]
    uuid = "e49e57b2e8fbeceb0a2c56a0c63fe6c5"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 刺击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 每1次旋风打击的攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 6
    # 多段攻击次数上限 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [范围信息]
    # 旋风范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [冷血突刺]\n
        旋风会吸附周围的敌人\n
         - 攻击范围 +45%
        """
        ...

    def vp_2(self):
        """
        [冷血突刺]\n
        施放时， 跳向600px内的最强敌人并插入魔枪\n
         - 删除旋风多段攻击\n
         - 总攻击力相同\n
        魔枪的斗气会强制控制敌人\n
         - 持续时间 : 3秒
        """
        ...

# 破灭斩
# demonic_lancer/vanguard/e4c354a89c337310aeb7041d5e742828
# 3deb7be5f01953ac8b1ecaa1e25e0420/e4c354a89c337310aeb7041d5e742828
class Skill25(ActiveSkill):
    """
    聚集力量， 向前方施放致命的横斩。
    """
    name = "破灭斩"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 1
    cd = 14
    mp = [60, 850]
    uuid = "e4c354a89c337310aeb7041d5e742828"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 横斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # [范围信息]
    # 斩击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    def vp_1(self):
        """
        [破灭斩]\n
        变更为可填充2次的技能\n
         - 每次填充冷却时间 : 7秒\n
         - 单次攻击力 -50%\n
        攻击范围 +70%
        """
        self.cd = 7
        self.skillRation *= 0.5

    def vp_2(self):
        """
        [破灭斩]\n
        除觉醒技能外的其他技能命中敌人后， 可以强制中断并施放[破灭斩]\n
         - [破灭斩]命中时， 5秒内命中率 +50%
        """
        ...

# 灭袭乱舞
# demonic_lancer/vanguard/1fadde0eece18649caddbca7bd58cc2f
# 3deb7be5f01953ac8b1ecaa1e25e0420/1fadde0eece18649caddbca7bd58cc2f
class Skill26(ActiveSkill):
    """
    在原地反复地快速横斩后， 施放强力的最后一击。 被横斩击中的敌人会渐渐聚在中间， 连续按下攻击键或技能键可以加快攻击速度。
    """
    name = "灭袭乱舞"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cube = 1
    cd = 18
    mp = [150, 1260]
    uuid = "1fadde0eece18649caddbca7bd58cc2f"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 每1次横斩的攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 12
    # 横斩次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [灭袭乱舞]\n
        用力挥动战戟， 以确保更有效的攻击\n
         - 横劈次数 -10次\n
         - 总攻击力相同\n
         - 删除连按时增加攻击速度的功能\n
        攻击范围 +40%
        """
        ...

    def vp_2(self):
        """
        [灭袭乱舞]\n
        与魔枪一起进入疯狂状态， 施放技能过程中所受伤害 -80%\n
        每次命中时， 技能结束后获得攻击速度和移动速度增益\n
         - 每次攻击时， 攻击速度和移动速度 +1%\n
         - 增益持续时间 : 15秒
        """
        ...

# 横扫八荒
# demonic_lancer/vanguard/4b2c90ec226fd40e967875aa5eabefb2
# 3deb7be5f01953ac8b1ecaa1e25e0420/4b2c90ec226fd40e967875aa5eabefb2
class Skill27(ActiveSkill):
    """
    将长枪举过头顶， 大幅旋转攻击敌人后， 施放强力的最后一击。 旋转攻击命中时将敌人聚集到中心。 使用方向键可以移动角色， 并且连续按下攻击键或技能键可以加快攻击速度。 技能施放过程中按下Z键， 会立即施放最后一击。
    """
    name = "横扫八荒"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [222, 2225]
    uuid = "4b2c90ec226fd40e967875aa5eabefb2"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 每1次旋转横斩的攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 9
    # 旋转横斩次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 挥斩范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [横扫八荒]\n
        旋转斩击攻击次数 -7次\n
         - 总攻击力相同\n
        最后一击命中时恢复2次[战戟猛攻]能量层数， 并使敌人进入眩晕异常状态\n
         - 眩晕几率100%\n
         - 持续时间3秒
        """
        ...

    def vp_2(self):
        """
        [横扫八荒]\n
        施放技能时进入无敌状态\n
        攻击范围 +20%
        """
        ...

# 战戟之魂
# demonic_lancer/vanguard/d2c6df5105577fb59fb92529a36165a0
# 3deb7be5f01953ac8b1ecaa1e25e0420/d2c6df5105577fb59fb92529a36165a0
class Skill28(PassiveSkill):
    """
    从无数次绝境中存活下来并变强的征战者， 可以不用抑制魔枪之力， 并且可以支配魔枪之力。\n
    增加基本攻击力和技能攻击力， 并且征战者的生命值低于一定值时， 会产生下列效果。 (强化效果共分为2阶段)\n
     - 增加攻击速度\n
     - 增加攻击过程中被击时， 不会僵直的伤害量上限\n
     - 在第2阶段， 无视僵直不仅适用于攻击， 还适用于除攻击以外的所有情况。
    """
    name = "战戟之魂"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    uuid = "d2c6df5105577fb59fb92529a36165a0"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [战戟猛攻]叠加次数增加量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [战戟猛攻]效果额外攻击速度 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # -  [每个阶段发动效果所需的生命值比率]  -
    # 第1阶段 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 第2阶段 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # [第1阶段]被击时， 不会进入僵直的伤害量上限增加 : 生命值最大值的{value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # [第2阶段]被击时， 不会进入僵直的伤害量上限增加 : 生命值最大值的{value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

    associate = [ {"data":data0,"type":"*skillRation"}]

# 千魂弑
# demonic_lancer/vanguard/d0cdaca82892e54097f22a1f60817048
# 3deb7be5f01953ac8b1ecaa1e25e0420/d0cdaca82892e54097f22a1f60817048
class Skill29(ActiveSkill):
    """
    瞬间释放全部魔枪之力， 强力地砸向地面使敌人浮空， 之后用强力的横斩斩掉所有敌人。\n
    对无法抓取的敌人， 不适用浮空判定。\n
    施放技能时， 适用[战戟猛攻]增益效果。
    """
    name = "千魂弑"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [980, 8232]
    uuid = "d0cdaca82892e54097f22a1f60817048"
    hasVP = False
    hasUP = False

    # 下劈攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 最后一击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1

# 长虹贯日
# demonic_lancer/vanguard/1803b6a67047cafb9e289b4f33cc507b
# 3deb7be5f01953ac8b1ecaa1e25e0420/1803b6a67047cafb9e289b4f33cc507b
class Skill30(ActiveSkill):
    """
    刺穿敌人并将敌人举起， 跳向空中强力地砸向地面， 对周围的敌人造成冲击波伤害。 如果刺穿攻击没有命中敌人， 随后的攻击也无法施放。
    """
    name = "长虹贯日"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [250, 1000]
    uuid = "1803b6a67047cafb9e289b4f33cc507b"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 刺击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 最后一击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # [范围信息]
    # 最后冲击波范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 最终爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [长虹贯日]\n
        删除刺击攻击\n
         - 总攻击力相同\n
        最后一击命中时， 生命值低于20%的普通怪物立即被击败\n
        攻击范围 +50%
        """
        ...

    def vp_2(self):
        """
        [长虹贯日]\n
        基本冷却时间变更为37.5秒\n
         - 总攻击力 +50%\n
        刺击未命中时， 剩余冷却时间缩短为3秒
        """
        self.cd = 37.5
        self.skillRation *= 1.5

# 穿云裂地斩
# demonic_lancer/vanguard/0232c151ef3731c2dede51931a374723
# 3deb7be5f01953ac8b1ecaa1e25e0420/0232c151ef3731c2dede51931a374723
class Skill31(ActiveSkill):
    """
    跳跃并聚集力量， 强力地砸向地面， 对敌人造成致命伤害， 并且破坏地面， 对附近的敌人也造成伤害。 被下劈命中的敌人不会受到冲击波伤害。
    """
    name = "穿云裂地斩"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [600, 1480]
    uuid = "0232c151ef3731c2dede51931a374723"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 下劈攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # 冲击波范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    def vp_1(self):
        """
        [穿云裂地斩]\n
        施放[穿云裂地斩]后连接[战戟猛攻]时， 发动[落月斩]\n
         - 不消耗[战戟猛攻]可使用次数\n
        攻击范围 +40%
        """
        ...

    def vp_2(self):
        """
        [穿云裂地斩]\n
        向后跳跃并施放[穿云裂地斩]\n
        施放技能后的一定时间内， 征战者所受伤害减少\n
         - 伤害减少量 : 15%\n
         - 持续时间 : 10秒\n
        变更为可填充2次的技能\n
         - 每次填充冷却时间 : 25秒\n
         - 单次攻击力 -50%
        """
        self.cd = 25
        self.skillRation *= 0.5

# 破灭轮回刺
# demonic_lancer/vanguard/d296043df164385a14cb973c8c7c4d07
# 3deb7be5f01953ac8b1ecaa1e25e0420/d296043df164385a14cb973c8c7c4d07
class Skill32(ActiveSkill):
    """
    将长枪大幅度地旋转2次， 控制住附近的敌人， 使之聚集在前方后， 进行强力的最后一击。
    """
    name = "破灭轮回刺"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 8
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "d296043df164385a14cb973c8c7c4d07"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 回旋斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 2
    # 旋转斩击次数 : 2次
    # 最后一击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    def vp_1(self):
        """
        [破灭轮回刺]\n
        旋转攻击不吸附周围敌人； 使用战戟下劈地面， 引发冲击波\n
         - 总攻击力相同\n
        攻击范围 +30%
        """
        ...

    def vp_2(self):
        """
        [破灭轮回刺]\n
        战意喷薄而出， 对周围敌人造成伤害； 同时展开战意领域， 造成持续伤害\n
         - 总攻击力相同\n
        [战意领域效果]\n
        在战意领域中， 征战者每次攻击命中时增加攻击速度\n
         - 每次命中攻击速度增加量 : 10%\n
         - 增加量上限 : 70%\n
         - 战意领域持续时间 : 8秒
        """
        ...

# 战神之力
# demonic_lancer/vanguard/6e33d47e6622ce03b6defdd912140270
# 3deb7be5f01953ac8b1ecaa1e25e0420/6e33d47e6622ce03b6defdd912140270
class Skill33(PassiveSkill):
    """
    不灭战神和魔枪完全融为一体， 可以使用魔枪内所有潜在力量。 攻击敌人时， 会引发更猛烈的攻击， 并会对敌人造成这次伤害量一定比率的追加伤害。 该比率伤害会以同样的比率作用在装备的追加伤害效果上。 此外， [战戟猛攻]的能量层数会增加1。
    """
    name = "战神之力"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    uuid = "6e33d47e6622ce03b6defdd912140270"
    hasVP = False
    hasUP = False

    # 追加伤害比率 : 击打量的{value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [战戟猛攻]能量层数增加量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    associate = [ {"data":data0,"type":"*skillRation"}]

# 断魂裂岩斩
# demonic_lancer/vanguard/ca75c965f20a150f99f54155a37400df
# 3deb7be5f01953ac8b1ecaa1e25e0420/ca75c965f20a150f99f54155a37400df
class Skill34(ActiveSkill):
    """
    向前方施展强力的下斩， 把敌人斩断。 被斩断的敌人会在一瞬间成为超级控制状态。 随后裂开的地面上溅出碎片和火花， 对敌人造成多段伤害。
    """
    name = "断魂裂岩斩"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "ca75c965f20a150f99f54155a37400df"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 多段打击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 10
    # 多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 控制时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    def vp_1(self):
        """
        [断魂裂岩斩]\n
        除觉醒技能外的转职技能命中敌人后， 可以强制中断并施放[断魂裂岩斩]技能\n
         - 技能[断魂裂岩斩]命中敌人后， 可以强制中断[断魂裂岩斩]的施放后僵直， 并施放除觉醒技能外的其他转职技能\n
        攻击范围 +20%
        """
        ...

    def vp_2(self):
        """
        [断魂裂岩斩]\n
        将灭天状态的魔枪巨大化后发动猛烈一击\n
         - 删除控制及多段攻击\n
         - 总攻击力相同\n
        [断魂裂岩斩]施放过程中可以施放部分技能\n
         - 施放的技能伤害合算至[断魂裂岩斩]\n
         - 可使用的技能 : [落月斩]、 [长虹贯日]、 [穿云裂地斩]\n
        攻击范围 +40%
        """
        ...

# 血战天狱
# demonic_lancer/vanguard/b163d099c8cc27fdb6fd3639c2ee6df9
# 3deb7be5f01953ac8b1ecaa1e25e0420/b163d099c8cc27fdb6fd3639c2ee6df9
class Skill35(ActiveSkill):
    """
    挥舞不灭战神的斗气和魔枪的究极之力合体的巨型魔枪， 使前方化为焦土， 并且再次聚集力量后， 施展毁灭一切存在的强力最后一击。
    """
    name = "血战天狱"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "b163d099c8cc27fdb6fd3639c2ee6df9"
    hasVP = False
    hasUP = False

    # 第1~4击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 4
    # 最后一击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1

# 灭天之魂
# demonic_lancer/vanguard/8e358ecf99ac9df31a6132aeafe378a9
# 3deb7be5f01953ac8b1ecaa1e25e0420/8e358ecf99ac9df31a6132aeafe378a9
class Skill36(PassiveSkill):
    """
    千魂·征战者通过修炼获得更加强大的身体和精神力， 完全掌控力量激发至极限的“灭天状态”的魔枪。 增加基本攻击力和转职技能攻击力， 变更部分技能效果。\n
    [战戟猛攻]\n
    每次施放[战戟猛攻]命中敌人时， 能量恢复时间减少0.6秒。\n
    [战戟猛攻]单次命中多个敌人时， 能量恢复时间减少效果仅适用1次。\n
    [落月斩]\n
    若施放[落月斩]后使用[战戟猛攻]， 则发动落月冲击， 动作变更为后退并斩击敌人。\n
    落月冲击攻击力与[战戟猛攻]相同。\n
    前进并使用[战戟猛攻]时， 发动原来的前进攻击。
    """
    name = "灭天之魂"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "8e358ecf99ac9df31a6132aeafe378a9"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [战戟猛攻]
    # 命中时能量恢复时间减少量 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    associate = [ {"data":data0,"type":"*skillRation"},{"data":[-i for i in data1],"type":"+cd","skills":["战戟猛攻"],"ratio":1}]

# 镇狱裂地枪
# demonic_lancer/vanguard/78b86e64fbb74c1db1b71c50a5ac21cd
# 3deb7be5f01953ac8b1ecaa1e25e0420/78b86e64fbb74c1db1b71c50a5ac21cd
class Skill37(ActiveSkill):
    """
    挥动魔枪将其插入地面， 对敌人造成伤害。 然后拔出魔枪， 强力上挑， 造成巨大伤害。
    """
    name = "镇狱裂地枪"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [960, 7200]
    uuid = "78b86e64fbb74c1db1b71c50a5ac21cd"
    hasVP = False
    hasUP = False

    # 魔枪插地攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 终结上挑攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1

# 天劫·斗灭乾坤
# demonic_lancer/vanguard/f4a561e272cc434a4905b3aa0c0de090
# 3deb7be5f01953ac8b1ecaa1e25e0420/f4a561e272cc434a4905b3aa0c0de090
class Skill38(ActiveSkill):
    """
    千魂·征战者将魔枪插入地面， 利用自身斗气， 将周围化为荒地。 然后用力跳跃至高空， 使魔枪狂化， 并向正面强力下劈， 消灭眼前的敌人。\n
    施放时， 适用[战戟猛攻]的增益效果。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "天劫·斗灭乾坤"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4027, 8055]
    uuid = "f4a561e272cc434a4905b3aa0c0de090"
    hasVP = False
    hasUP = False

    # 下劈攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'vanguard'
        self.nameCN = '千魂·征战者'
        self.role = 'demonic_lancer'
        self.角色 = '魔枪士'
        self.职业 = '征战者'
        self.jobId = '3deb7be5f01953ac8b1ecaa1e25e0420'
        self.jobGrowId = '37495b941da3b1661bc900e68ef3b2c6'

        self.武器选项 = ['长枪','战戟','光枪','暗矛']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '重甲'
        self.buff = 1.80

        super().__init__(equVersion, __name__)
