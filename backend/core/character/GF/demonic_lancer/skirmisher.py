#3deb7be5f01953ac8b1ecaa1e25e0420
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "demonic_lancer/skirmisher/cn/skillDetail"

# 刺击
# demonic_lancer/skirmisher/9dda3f4a849dba1a288dd65e116860f2
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
# demonic_lancer/skirmisher/0969cd4054d93da07708108c0cc1c4b5
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
# demonic_lancer/skirmisher/5a56514f35cf0270ae8d6c65f8fefd78
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


# 回旋钩
# demonic_lancer/skirmisher/eb71e1d82d92c7e1d40500a0dcd77aa6
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
# demonic_lancer/skirmisher/4655101518604f874721b3cc249aae10
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
    position = 2
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
# demonic_lancer/skirmisher/c9664191611af31142e052dfaef84530
# 3deb7be5f01953ac8b1ecaa1e25e0420/c9664191611af31142e052dfaef84530
class Skill8(ActiveSkill):
    """
    从空中快速地斜向落地， 刺向敌人。
    """
    name = "落凤枪"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 7
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
# demonic_lancer/skirmisher/fc7a3f4c2852c832a2f20af63d5d212f
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
# demonic_lancer/skirmisher/51a08fd0c90f0a5276cd552047fac93d
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
    position = 3
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
# demonic_lancer/skirmisher/717f1e2104fe4b796f800352fa143ecc
# 3deb7be5f01953ac8b1ecaa1e25e0420/717f1e2104fe4b796f800352fa143ecc
class Skill13(ActiveSkill):
    """
    使用长枪进行连续攻击。 命中敌人时按下技能键， 即刻发动下一次攻击。
    """
    name = "连环枪"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 7
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

# 长枪精通
# demonic_lancer/skirmisher/f2fb27162beb0b87a7cb9af7900e95f2
# 3deb7be5f01953ac8b1ecaa1e25e0420/f2fb27162beb0b87a7cb9af7900e95f2
class Skill14(PassiveSkill):
    """
    增加物理攻击力， 并减少技能冷却时间， 但[流云幻灭]、 [极影无形杀]、 [问鼎·千军破云]的冷却时间不会减少。 熟练掌握长枪技巧， 增加攻击速度和命中率。\n
    学习此技能后， 可以在空中强制取消[落凤枪]。
    """
    name = "长枪精通"
    learnLv = 15
    masterLv = 20
    maxLv = 30
    position = 1
    rangeLv = 3
    uuid = "f2fb27162beb0b87a7cb9af7900e95f2"
    hasVP = False
    hasUP = False

    # 攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 攻击速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 命中率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 冷却时间减少率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    associate = [ {"type":"$*PAtkP","data":data0},{"type":"*cdReduce","data":data3,"exceptSkills":["流云幻灭","极影无形杀","问鼎·千军破云"]},]

# 行云诀
# demonic_lancer/skirmisher/cfacda0647b9a0f595df2c2aad30c18d
# 3deb7be5f01953ac8b1ecaa1e25e0420/cfacda0647b9a0f595df2c2aad30c18d
class Skill15(ActiveSkill):
    """
    使用后， 保留当前技能的幻影， 并用[后跳]脱身后可以自由移动。\n
    在不强制中断攻击技能 (静止状态、 基本攻击)的情况下， 按下技能键会发动[后跳]而不是[行云诀]。\n
    行云系列的技能可以用[行云诀]加上方向键的方式使用。\n
    可以用[行云诀]加方向键的方式施放的技能 :\n
    [行云 : 风]\n
    [行云 : 疾]\n
    [行云 : 落]
    """
    name = "行云诀"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 5
    rangeLv = 1
    cd = 3
    mp = [10, 10]
    uuid = "cfacda0647b9a0f595df2c2aad30c18d"
    hasVP = False
    hasUP = False


# 行云 : 风
# demonic_lancer/skirmisher/8f73f243041c2d27739fe7696f02bf9b
# 3deb7be5f01953ac8b1ecaa1e25e0420/8f73f243041c2d27739fe7696f02bf9b
class Skill16(ActiveSkill):
    """
    行云系列的技能， 在行走、 前冲、 基本攻击、 施放其他攻击技能时， 都可以使用。 使用可以把敌人吸进去的旋风对敌人进行刺击。\n
    在施放其他攻击技能过程中使用， 可以留下正在攻击的幻影， 并施放[行云 : 风]。\n
    开始的第一击有推开靠近的敌人的效果。\n
    可以用[行云诀] + →施放[行云 : 风]。\n
    行走、 基本攻击、 前冲、 前冲攻击时可以使用。
    """
    name = "行云 : 风"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 5
    mp = [45, 234]
    uuid = "8f73f243041c2d27739fe7696f02bf9b"
    hasVP = False
    hasUP = True

    # 旋风多段攻击次数 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 刺击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 旋风攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 8
    # [范围信息]
    # 旋风吸入敌人的范围增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 旋风吸入敌人的力量增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

# 扫堂枪
# demonic_lancer/skirmisher/128b9ddef2262f40723deae4407bdb42
# 3deb7be5f01953ac8b1ecaa1e25e0420/128b9ddef2262f40723deae4407bdb42
class Skill17(ActiveSkill):
    """
    攻击敌人足部， 使之倒地。
    """
    name = "扫堂枪"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 5
    mp = [12, 120]
    uuid = "128b9ddef2262f40723deae4407bdb42"
    hasVP = False
    hasUP = True

    # 横斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1

# 无双枪术
# demonic_lancer/skirmisher/45442bbbe33540b4deeec29437dae70c
# 3deb7be5f01953ac8b1ecaa1e25e0420/45442bbbe33540b4deeec29437dae70c
class Skill18(ActiveSkill):
    """
    将斗气附加于枪上， 给予敌人这次伤害量一定比率的追加伤害。\n
    [无双枪术]的比率伤害会以同样的比率作用在装备的追加伤害效果上。
    """
    name = "无双枪术"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 7
    rangeLv = 3
    cd = 5
    uuid = "45442bbbe33540b4deeec29437dae70c"
    hasVP = False
    hasUP = False

    # 攻击力比率 : 打击量的{value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [无双枪术]持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 双重刺击
# demonic_lancer/skirmisher/d085127b0edd719782bd618d5688f4a1
# 3deb7be5f01953ac8b1ecaa1e25e0420/d085127b0edd719782bd618d5688f4a1
class Skill19(ActiveSkill):
    """
    瞬间施放力量聚于一点的二连刺击。 枪头刺击拥有更强的威力。\n
    近距离攻击和枪头攻击不会同时命中一个敌人， 判定重叠时， 会优先判定为枪头攻击。
    """
    name = "双重刺击"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 7
    mp = [38, 290]
    uuid = "d085127b0edd719782bd618d5688f4a1"
    hasVP = False
    hasUP = True

    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 0
    # 第1击枪头攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 第2击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 0
    # 第2击枪头攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # 枪头攻击判定距离 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    mode = ["枪头","近距离"]

    def setMode(self, mode):
        if mode == "枪头":
            self.hit0 = self.hit2 = 0
            self.hit1 = self.hit3 = 1
        elif mode == "近距离":
            self.hit0 = self.hit2 = 1
            self.hit1 = self.hit3 = 0

# 行云 : 疾
# demonic_lancer/skirmisher/ff171dc487807bb9aa28900ca9a46b41
# 3deb7be5f01953ac8b1ecaa1e25e0420/ff171dc487807bb9aa28900ca9a46b41
class Skill20(ActiveSkill):
    """
    行云系列的技能， 在行走、 前冲、 基本攻击、 施放其他攻击技能时， 都可以使用。 施放向下的横扫攻击。\n
    在施放其他攻击技能过程中使用， 可以留下正在攻击的幻影， 并施放[行云 : 疾]。\n
    可以以基础浮空力的一定比率使倒地的敌人再次浮空。\n
    可以用[行云诀] + ↓施放[行云 : 疾]。\n
    行走、 基本攻击、 前冲、 前冲攻击时可以使用。
    """
    name = "行云 : 疾"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 6
    mp = [40, 220]
    uuid = "ff171dc487807bb9aa28900ca9a46b41"
    hasVP = False
    hasUP = True

    # 横扫攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 基础的浮空力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 使倒地的敌人再次浮空的浮空力比率 : 基础浮空力的{value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [范围信息]
    # 攻击范围 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)


# 行云 : 落
# demonic_lancer/skirmisher/2f5d03c7848effbc0a23f4df45d9ca46
# 3deb7be5f01953ac8b1ecaa1e25e0420/2f5d03c7848effbc0a23f4df45d9ca46
class Skill22(ActiveSkill):
    """
    行云系列的技能， 在行走、 前冲、 基本攻击、 施放其他攻击技能时， 都可以使用。 使用后， 会跳至空中投掷长枪。\n
    在施放其他攻击技能过程中使用， 可以留下正在攻击的幻影， 并施放[行云 : 落]。\n
    投枪会使敌人处于超级控制状态， 并且浮空的敌人的控制时间更久。\n
    跳跃投枪时， 可以左右移动。\n
    可以用[行云诀] + ↑施放[行云 : 落]。\n
    行走、 基本攻击、 前冲、 前冲攻击时可以使用。
    """
    name = "行云 : 落"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 8
    mp = [72, 380]
    uuid = "2f5d03c7848effbc0a23f4df45d9ca46"
    hasVP = False
    hasUP = True

    # 投枪攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 浮空的敌人的超级控制时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 地面的敌人超级控制时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [范围信息]
    # 攻击范围 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

# 旋风枪
# demonic_lancer/skirmisher/01c3a2fb793d293a25ed8dc7a0d70c1a
# 3deb7be5f01953ac8b1ecaa1e25e0420/01c3a2fb793d293a25ed8dc7a0d70c1a
class Skill23(ActiveSkill):
    """
    向前方旋转长枪， 对敌人进行猛烈的打击。 按下前方向键时， 前进距离和旋转次数都会增加。\n
    在决斗场无法攻击倒地的敌人。
    """
    name = "旋风枪"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 1
    rangeLv = 2
    cd = 9
    mp = [37, 370]
    uuid = "01c3a2fb793d293a25ed8dc7a0d70c1a"
    hasVP = False
    hasUP = True

    # 旋转攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 11
    # 击打数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # 大小 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 行云 : 沐
# demonic_lancer/skirmisher/85f7c810ad503790e8626439fe936d56
# 3deb7be5f01953ac8b1ecaa1e25e0420/85f7c810ad503790e8626439fe936d56
class Skill24(PassiveSkill):
    """
    增加基本攻击力和[刺击]、 [落凤枪]、 [连环枪]等转职技能的攻击力。
    """
    name = "行云 : 沐"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 7
    rangeLv = 3
    uuid = "85f7c810ad503790e8626439fe936d56"
    hasVP = False
    hasUP = False

    # 技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)

    associate = [ {"data":data0,"type":"*skillRation"}]

# 无畏波动枪
# demonic_lancer/skirmisher/8c2379737c5acc935c1731f67f607655
# 3deb7be5f01953ac8b1ecaa1e25e0420/8c2379737c5acc935c1731f67f607655
class Skill25(ActiveSkill):
    """
    持枪直线突进进行刺击， 并将敌人刺穿在枪上， 随后敌人会被弹开， 并受到额外伤害。\n
    按下前方向键时， 会增加突进距离。
    """
    name = "无畏波动枪"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 9
    mp = [91, 479]
    uuid = "8c2379737c5acc935c1731f67f607655"
    hasVP = False
    hasUP = True

    # 对被刺穿敌人的攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 0
    # 被刺穿后弹开时的攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 0
    # 普通突进攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 普通刺击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # 弹开的敌人撞到地面时的冲撞攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 0
    # 弹开的敌人撞到墙壁时的冲撞攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    hit5 = 0

    mode = ["不可抓取", "可抓取(地面)", "可抓取(墙壁)"]

    def setMode(self, mode):
        if mode == "不可抓取":
            self.hit2 = self.hit3 = 1
            self.hit0 = self.hit1 = self.hit4 = self.hit5 =0
        elif mode == "可抓取(地面)":
            self.hit0 = self.hit1 = self.hit4 = 1
            self.hit2 = self.hit3 = self.hit5 = 0
        elif mode == "可抓取(墙壁)":
            self.hit0 = self.hit1 = self.hit5 = 1
            self.hit2 = self.hit3 = self.hit4 = 0

# 升龙破空枪
# demonic_lancer/skirmisher/4224f9b0b8c7c903e9a1e0f9d9f6d04d
# 3deb7be5f01953ac8b1ecaa1e25e0420/4224f9b0b8c7c903e9a1e0f9d9f6d04d
class Skill26(ActiveSkill):
    """
    横扫前方、 挑飞敌人、 并大力刺向浮空的敌人。\n
    对无法抓取的敌人不适用控制效果。
    """
    name = "升龙破空枪"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [115, 1150]
    uuid = "4224f9b0b8c7c903e9a1e0f9d9f6d04d"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 横扫攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 上挑攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 攻击范围增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [升龙破空枪]\n
        从上挑攻击开始施放\n
         - 总攻击力相同\n
        施放的同时施放[行云 : 落]
        """
        ...

    def vp_2(self):
        """
        [升龙破空枪]\n
        冷却时间及攻击力 +100%\n
        攻击范围 +30%
        """
        self.cd = 40
        self.skillRation *= 2

# 螺旋波动枪
# demonic_lancer/skirmisher/902a016f6978f13740f237e4740a5646
# 3deb7be5f01953ac8b1ecaa1e25e0420/902a016f6978f13740f237e4740a5646
class Skill27(ActiveSkill):
    """
    向前方大幅挥枪激起气流， 连续攻击敌人。\n
    第二次攻击命中时将敌人拉到前方。\n
    可以在地面和空中施放。
    """
    name = "螺旋波动枪"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 15
    mp = [78, 800]
    uuid = "902a016f6978f13740f237e4740a5646"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 第3击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 攻击范围: {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [螺旋波动枪]\n
        变更为行云系技能； 可以强制中断其他技能， 并施放[螺旋波动枪]\n
        连接施放时， 删除第1次攻击\n
         - 攻击力 +25%
        """
        ...

    def vp_2(self):
        """
        [螺旋波动枪]\n
        第1、 第2击挥击过程中输入[旋风枪]或者[无畏波动枪]技能键时， 将终结攻击变更为该技能\n
         - 终结攻击的攻击力适用额外输入技能的攻击力总和\n
        攻击范围 +50%\n
         - 吸附敌人范围和吸附力 +50%
        """
        ...

# 狂龙怒啸
# demonic_lancer/skirmisher/9cb6f9ed646fa87f9b7680a42ce83d1a
# 3deb7be5f01953ac8b1ecaa1e25e0420/9cb6f9ed646fa87f9b7680a42ce83d1a
class Skill28(ActiveSkill):
    """
    枪身举至头顶高速旋转， 把命中的敌人吸至中心。\n
    提升技能等级可增加旋转速度。
    """
    name = "狂龙怒啸"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 1
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [73, 890]
    uuid = "9cb6f9ed646fa87f9b7680a42ce83d1a"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 旋转攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 15
    # 旋转速度增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 旋转多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [范围信息]
    # 攻击范围 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [狂龙怒啸]\n
        旋转次数 -7次\n
         - 总攻击力相同\n
        旋转过程中增加落雷效果\n
         - 使敌人进入感电状态
        """
        ...

    def vp_2(self):
        """
        [狂龙怒啸]\n
        攻击范围 +50%\n
        旋转结束后在地面生成迷雾\n
         - 在迷雾中决战者的回避率 +20%\n
         - 迷雾持续5秒
        """
        ...

# 夺命雷霆枪
# demonic_lancer/skirmisher/42c82812f86ff6704ae9952a2e6093a4
# 3deb7be5f01953ac8b1ecaa1e25e0420/42c82812f86ff6704ae9952a2e6093a4
class Skill29(ActiveSkill):
    """
    用长枪连续刺击敌人要害。 敌人被枪头刺击命中时， 会积累受创效果， 最后用横斩对积累受创效果的敌人造成额外伤害。\n
    最后横斩的攻击力与连续刺击的次数成正比。\n
    近距离攻击和积累受创判定重叠时， 优先判定为积累受创。 即使攻击范围增加， 积累受创判定距离也不会增加。
    """
    name = "夺命雷霆枪"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [375, 3200]
    uuid = "42c82812f86ff6704ae9952a2e6093a4"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 刺击次数 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 近距离刺击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 0
    # 引起受创效果的刺击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 15
    # 每1次刺击对应的横斩攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 15
    # 最后横斩攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1
    # 积累受创效果判定距离 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # [范围信息]
    # 攻击范围 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

    mode = ["枪头","近距离"]

    def setMode(self, mode):
        if mode == "枪头":
            self.hit1 = 0
            self.hit2 = self.hit3 = 15
            self.hit4 = 1
        elif mode == "近距离":
            self.hit1 = 15
            self.hit2 = self.hit3 = 0
            self.hit4 = 1

    def vp_1(self):
        """
        [夺命雷霆枪]\n
        刺击速度 +70%\n
        最后斩击速度 +20%\n
        - 攻击范围 +70%\n
        刺击全程适用枪头判定
        """
        self.setMode("枪头")

    def vp_2(self):
        """
        [夺命雷霆枪]\n
        部分技能命中时， 获得强化[夺命雷霆枪]的极·受创能量\n
         - 目标技能 : [刺击]、 [双重刺击]、 [无畏波动枪]、 [无双突刺]、 [双龙流云灭]\n
         - 最多可以获得5个\n
        [夺命雷霆枪]命中时， 每消耗1个极·受创能量， 决战者的攻击速度 +4%\n
         - 持续时间 : 20秒\n
        施放[夺命雷霆枪]时， 初始化[行云诀]的冷却时间
        """
        ...

# 行云 : 启
# demonic_lancer/skirmisher/a5fa08f5d509e6ff2ebc68856a470b5a
# 3deb7be5f01953ac8b1ecaa1e25e0420/a5fa08f5d509e6ff2ebc68856a470b5a
class Skill30(PassiveSkill):
    """
    流畅地循环气力， 增加基本攻击和所有技能的攻击力。 而且特定技能可以增加更多的攻击力。
    """
    name = "行云 : 启"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 3
    uuid = "a5fa08f5d509e6ff2ebc68856a470b5a"
    hasVP = False
    hasUP = False

    # [行云 ： 风]攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [行云 ： 疾]攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [行云 ： 落]攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [连环枪]攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 基本攻击和其他技能的攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    associate = [
        {"data":data0,"type":"*skillRation","skills":["行云 : 风"]},
        {"data":data1,"type":"*skillRation","skills":["行云 : 疾"]},
        {"data":data2,"type":"*skillRation","skills":["行云 : 落"]},
        {"data":data3,"type":"*skillRation","skills":["连环枪"]},
        {"data":data4,"type":"*skillRation","exceptSkills":["行云 : 风","行云 : 疾","行云 : 落"]}
    ]

# 流云幻灭
# demonic_lancer/skirmisher/506e7ed77d517419a6e1c437a2cedb17
# 3deb7be5f01953ac8b1ecaa1e25e0420/506e7ed77d517419a6e1c437a2cedb17
class Skill31(ActiveSkill):
    """
    横扫前方并聚集敌人后， 放出使用决战者的技能的分身， 投出聚集斗气的长枪， 虚弱大范围敌人。
    """
    name = "流云幻灭"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [1000, 8400]
    uuid = "506e7ed77d517419a6e1c437a2cedb17"
    hasVP = False
    hasUP = False

    # 第一击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 第3击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 第4击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 3
    # 第5击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1
    # 第6击攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    hit5 = 1
    # 第7击攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    hit6 = 1
    # 第8击攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    hit7 = 1
    # 斗气长枪攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)
    hit8 = 1
    # 第4击多段攻击次数 : {value9}次
    data9 = get_data(f'{prefix}/{uuid}', 9, lambda x = None: x)
    # 斗气长枪的超级控制时间 : {value10}秒
    data10 = get_data(f'{prefix}/{uuid}', 10, lambda x = None: x)
    # [流云幻灭]追加效果
    #  - 斗气长枪攻击力 +10%
    skillRation = 1.1

# 风火燎原
# demonic_lancer/skirmisher/3d8f3d438405d79f8d3ed68072674d1e
# 3deb7be5f01953ac8b1ecaa1e25e0420/3d8f3d438405d79f8d3ed68072674d1e
class Skill32(ActiveSkill):
    """
    可以在地面或空中使用。\n
    在地面使用时， 向前方跳跃， 通过追加按键投出集束长枪。\n
    施放瞬间可以用前后方向键调整跳跃距离， 达到跳跃的最高点时， 按下技能键或X键可以发射集束长枪。\n
    施放[风火燎原]后， 可以接着使用[落凤枪]、 [流光无影闪]。
    """
    name = "风火燎原"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [500, 1300]
    uuid = "3d8f3d438405d79f8d3ed68072674d1e"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 集束长枪的攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 20*2
    #  集束长枪的发射数量 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 最多发射次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [范围信息]
    # 集束长枪大小 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [风火燎原]\n
        再次发射时间减少\n
        发射次数上限 +1次\n
         - 总攻击力相同\n
        施放时进入无敌状态
        """
        ...

    def vp_2(self):
        """
        [风火燎原]\n
        可以强制中断[风火燎原]的施放后僵直并立即施放[行云诀]\n
         - 取消技能僵直并施放[行云诀]时， 在该位置后方落地\n
         - 适用[一身是胆 - 行云诀]强化效果
        """
        ...

# 三一斩月
# demonic_lancer/skirmisher/547ab2b2bd860d3e37355a9cfbc1077c
# 3deb7be5f01953ac8b1ecaa1e25e0420/547ab2b2bd860d3e37355a9cfbc1077c
class Skill33(ActiveSkill):
    """
    向前方大幅挥动枪身， 进行新月攻击。 被击中的敌人会聚集在新月的中间。\n
    近距离的敌人受到枪身的攻击后会被推开。
    """
    name = "三一斩月"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [770, 1800]
    uuid = "547ab2b2bd860d3e37355a9cfbc1077c"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 枪身攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # [三一斩月]攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 8
    # 敌人的僵直度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 新月的基础击打数 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [范围信息]
    # 轨迹大小 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    def vp_1(self):
        """
        [三一斩月]\n
        轨迹范围 +50%\n
        [三一斩月]攻击速度 +50%
        """
        ...

    def vp_2(self):
        """
        [三一斩月]\n
        大幅挥动枪身， 生成迷雾持续10秒\n
        位于迷雾中时， 适用附加效果\n
         - 行云系技能范围 +50%\n
          - 目标技能 : [行云 : 风]、 [行云 : 疾]、 [行云 : 落]\n
         - [行云诀]冷却时间 -50%
        """
        ...

# 行云 : 冥
# demonic_lancer/skirmisher/2a3c96b88d02372505692da0a8b54743
# 3deb7be5f01953ac8b1ecaa1e25e0420/2a3c96b88d02372505692da0a8b54743
class Skill34(PassiveSkill):
    """
    经过重重修炼， 通过魔枪驾驭行云的技术达到顶峰。\n
    学习后， 会增加特定技能的攻击力和物理暴击率。\n
    施放[行云诀]时， 会赋予无敌时间。 施放刺击系列技能时， 可以强制中断并连接施放其他刺击系列技能。 并且施放特定技能时， 将追加与原攻击力成一定比率的幻影攻击。\n
    -  [可追加幻影攻击的技能]  -\n
     - [行云 : 风]、 [行云 : 疾]、 [行云 : 落]\n
     - [刺击]、 [双重刺击]\n
     - 地面基本攻击\n
    -  [可连接使用的刺击系列技能]  -\n
     - 可以以[刺击]、 [双重刺击]、 [无双突刺]的顺序连接使用。\n
     - 连接使用时， 技能的攻击速度会增加。\n
     - 学习技能后， [行云 : 风]的攻击速度会增加。\n
     - 学习技能后， 在[后跳]或[行云诀]状态下可以使用基本攻击。
    """
    name = "行云 : 冥"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    uuid = "2a3c96b88d02372505692da0a8b54743"
    hasVP = False
    hasUP = False

    # 施放[行云诀]时的无敌时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 物理暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 幻影与相应技能原攻击力的比率
    #  - [行云 ： 风]、 [行云 ： 疾]、 [行云 ： 落] : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    #  - [刺击]、 [双重刺击] : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    #  - 地面基本攻击 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 连接使用刺击系列技能时， 攻击速度增加率
    #  - [刺击] → [双重刺击] : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    #  - [双重刺击] → [无双突刺] : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    #  - [刺击] → [双重刺击] → [无双突刺] : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    # [行云 ： 风]攻击速度增加率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)
    # 除行云系外的技能攻击力增加率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9, lambda x = None: x)

    associate = [
        {"data":data2,"type":"*skillRation","skills":["行云 : 风","行云 : 疾","行云 : 落"]},
        {"data":data3,"type":"*skillRation","skills":["刺击","双重刺击"]},
        {"data":data4,"type":"*skillRation","exceptSkills":["行云 : 风","行云 : 疾","行云 : 落","刺击","双重刺击"]}
    ]

# 无双突刺
# demonic_lancer/skirmisher/bc11d28c04e01923a093d65752c55516
# 3deb7be5f01953ac8b1ecaa1e25e0420/bc11d28c04e01923a093d65752c55516
class Skill35(ActiveSkill):
    """
    施放2次牵制刺击后， 追加2次强力的终结刺击。\n
    第3~4击判定为枪头攻击时， 会造成更大的伤害。\n
    近距离攻击和枪头攻击同时命中时， 优先判定为枪头攻击。 即使攻击范围增加， 枪头判定距离也不会增加。
    """
    name = "无双突刺"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 3
    cd = 33
    mp = [783, 3154]
    uuid = "bc11d28c04e01923a093d65752c55516"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 第1~2击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 2
    # 第3~4击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 0
    # 第3~4击枪头攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 2
    # 枪头攻击判定距离 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [范围信息]
    # 攻击范围 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    mode = ["枪头","近距离"]

    def setMode(self, mode):
        if mode == "枪头":
            self.hit1 = 0
            self.hit0 = self.hit2 = 2
        elif mode == "近距离":
            self.hit2 = 0
            self.hit0 = self.hit1 = 2

    def vp_1(self):
        """
        [无双突刺]\n
        变更为行云系技能； 可以强制中断其他技能， 并施放[无双突刺]\n
        删除牵制刺击的第1~2击\n
         - 总攻击力相同\n
        强制中断其他攻击技能并施放技能时， 增加攻击速度
        """
        ...

    def vp_2(self):
        """
        [无双突刺]\n
        牵制刺击第1、 2击会移动至前方最强敌人处发动刺击\n
        全程适用[行云 : 冥]的施放速度增加效果
        """
        ...

# 流光无影闪
# demonic_lancer/skirmisher/faf9cd66281078b51be2ee0b0f6c5530
# 3deb7be5f01953ac8b1ecaa1e25e0420/faf9cd66281078b51be2ee0b0f6c5530
class Skill36(ActiveSkill):
    """
    高速突进， 聚集前方的怪物后， 施展强力的终结击。\n
    可以在空中施放。
    """
    name = "流光无影闪"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 2
    cube = 5
    cd = 44
    mp = [550, 4600]
    uuid = "faf9cd66281078b51be2ee0b0f6c5530"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 突进攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 终结攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # [范围信息]
    # 打击范围 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    def vp_1(self):
        """
        [流光无影闪]\n
        减少[流光无影闪]施放及结束动作僵直\n
        变更为可填充2次的技能\n
        单次攻击力 : -50%
        """
        self.cd = 22
        self.skillRation *= 0.5

    def vp_2(self):
        """
        [流光无影闪]\n
        施放技能时进入无敌状态\n
        决战者消失后， 在命中的敌人中最强敌人后方出现
        """
        ...

# 极影无形杀
# demonic_lancer/skirmisher/1721e94897e9961d5c98130a13392f17
# 3deb7be5f01953ac8b1ecaa1e25e0420/1721e94897e9961d5c98130a13392f17
class Skill37(ActiveSkill):
    """
    施放超长攻击距离的刺击控制敌人， 随后突进过去展开斩击与刺击的乱舞刺击。\n
    刺击后的突进碰到敌人时， 角色会即刻在原地进行乱舞。\n
    该技能无法用行云系技能强制中断。\n
    输入前方向键后， 终结一击会向前突进。
    """
    name = "极影无形杀"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2600, 5300]
    uuid = "1721e94897e9961d5c98130a13392f17"
    hasVP = False
    hasUP = False

    # 第1次刺击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 乱舞斩击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 乱舞斩击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 7
    # 乱舞刺击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 乱舞刺击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 =  17
    # 最后一击攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    hit5 = 1

# 一身是胆
# demonic_lancer/skirmisher/0e409ac3e1c1f3976b3ef2bfe4c13069
# 3deb7be5f01953ac8b1ecaa1e25e0420/0e409ac3e1c1f3976b3ef2bfe4c13069
class Skill38(PassiveSkill):
    """
    千魂·决战者的行动如同幻影， 更加游刃有余地驾驭行云的技术。 增加基本攻击力和转职技能攻击力， 变更部分技能效果。\n
    [行云诀]\n
    行云诀发动期间， 可以使用其他攻击技能。\n
    [无畏波动枪]\n
    施放[无畏波动枪]时， 可以立即强制中断并连接行云系列技能； 强制中断施放时， 幻影分身会将敌人拉近。
    """
    name = "一身是胆"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "0e409ac3e1c1f3976b3ef2bfe4c13069"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)

    associate = [ {"data":data0,"type":"*skillRation"}]

# 双龙流云灭
# demonic_lancer/skirmisher/4c5271b0ecce120d7fc113f377fae76f
# 3deb7be5f01953ac8b1ecaa1e25e0420/4c5271b0ecce120d7fc113f377fae76f
class Skill39(ActiveSkill):
    """
    注入斗气， 用力向地面下劈， 然后与仿佛有生命般的幻影共同攻击。 可以在地面和空中施放。
    """
    name = "双龙流云灭"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [773, 6000]
    uuid = "4c5271b0ecce120d7fc113f377fae76f"
    hasVP = False
    hasUP = False

    # 地面下劈攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 挥击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 2
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 2
    # 挥击多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 爆炸多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

# 问鼎·千军破云
# demonic_lancer/skirmisher/2e2b7efe778656690f9c8cb6e47c3932
# 3deb7be5f01953ac8b1ecaa1e25e0420/2e2b7efe778656690f9c8cb6e47c3932
class Skill40(ActiveSkill):
    """
    将自身斗气聚于一处， 贯穿万物。\n
    施放时， 千魂·决战者大幅挥动魔枪释放斗气， 消失在迷雾中。 然后， 幻影发动乱舞攻击， 滞空的千魂·决战者聚集所有幻影制造巨型魔枪， 贯穿地上的一切。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "问鼎·千军破云"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "2e2b7efe778656690f9c8cb6e47c3932"
    hasVP = False
    hasUP = False

    # 魔枪挥击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 幻影乱舞攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 5
    # 终结穿刺攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 4
    # 乱舞多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 穿刺多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'skirmisher'
        self.nameCN = '千魂·决战者'
        self.role = 'demonic_lancer'
        self.角色 = '魔枪士'
        self.职业 = '决战者'
        self.jobId = '3deb7be5f01953ac8b1ecaa1e25e0420'
        self.jobGrowId = '618326026de1a1f1cfba5dbd0b8396e7'

        self.武器选项 = ['长枪','战戟','光枪','暗矛']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '轻甲'
        self.buff = 2.00

        super().__init__(equVersion, __name__)
