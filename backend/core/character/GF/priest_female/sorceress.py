#0c1b401bb09241570d364420b3ba3fd7
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "priest_female/sorceress/cn/skillDetail"



# 基础精通
# priest_female/sorceress/5a56514f35cf0270ae8d6c65f8fefd78
# 0c1b401bb09241570d364420b3ba3fd7/5a56514f35cf0270ae8d6c65f8fefd78
class Skill3(PassiveSkill):
    """
        增加基本攻击、 前冲攻击、 跳跃攻击、 [升空斩]的攻击力。\n
        在决斗场中， 增益/减益技能、 被动技能的技能攻击力增加效果对[基础精通]无影响。
    """
    name = "基础精通"
    learnLv = 1
    masterLv = 115
    maxLv = 200
    position = 1
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
    associate = [{"type":"*skillDamage","data":[i-100 if i>0 else 0 for i in data0],"skills":["念珠连射"]}]


# 武器格挡
# priest_female/sorceress/eb71e1d82d92c7e1d40500a0dcd77aa6
# 0c1b401bb09241570d364420b3ba3fd7/eb71e1d82d92c7e1d40500a0dcd77aa6
class Skill9(ActiveSkill):
    """
        竖起武器， 抵挡来自前方的攻击， 减少所受伤害。\n
        按住技能键可以维持防御姿态。 抵挡前方的攻击后， 可以强制使用其他技能。
    """
    name = "武器格挡"
    learnLv = 10
    masterLv = 5
    maxLv = 15
    position = 3
    rangeLv = 5
    cd = 2
    mp = [3, 4]
    uuid = "eb71e1d82d92c7e1d40500a0dcd77aa6"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 所受伤害减少率 (物理) : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 所受伤害减少率 (魔法) : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)


# 唤雷符
# priest_female/sorceress/45442bbbe33540b4deeec29437dae70c
# 0c1b401bb09241570d364420b3ba3fd7/45442bbbe33540b4deeec29437dae70c
class Skill14(ActiveSkill):
    """
        使用符咒在前方召唤落雷。\n
    [转职为驱魔师后附加效果]\n
    - 增加落雷大小\n
    - 使命中的敌人撞地反弹。 \n
    [学习乾坤之境后]\n
    - 可以探索施放者周围的350px内的敌人后发动攻击。\n
    - 周围没有敌人时无法施放。\n
    - 无法攻击物体。\n
    - 最多攻击12名敌人。\n
    - 对每名敌人攻击1次。
    """
    name = "唤雷符"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 5
    mp = [30, 252]
    uuid = "45442bbbe33540b4deeec29437dae70c"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 落雷攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 落雷距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 落雷大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 念珠连射
# priest_female/sorceress/0232c151ef3731c2dede51931a374723
# 0c1b401bb09241570d364420b3ba3fd7/0232c151ef3731c2dede51931a374723
class Skill15(ActiveSkill):
    """
        发射念珠。\n
    发射过程中， 按方向键， 可以调整为向上/向下发射， 发射时， 可以使用其他技能。\n
        连按技能键可以连续发射念珠， 可以在空中使用该技能。\n
        根据[基础精通]增加攻击力， 施放使用念珠的技能后， 无法使用[念珠连射]。
    """
    name = "念珠连射"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 4
    rangeLv = 1
    mp = [1, 1]
    uuid = "0232c151ef3731c2dede51931a374723"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    cd = 0.7

    # 念珠冷却时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # TODO 具体伤害数据

# 木槵子经
# priest_female/sorceress/d2c6df5105577fb59fb92529a36165a0
# 0c1b401bb09241570d364420b3ba3fd7/d2c6df5105577fb59fb92529a36165a0
class Skill16(ActiveSkill):
    """
        在空中排列念珠后， 一同射向前方。\n
        念珠会击退敌人并造成伤害。\n
        敌人离得越近， 击退距离越远。 处于远处的敌人不会被击退。
    """
    name = "木槵子经"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 4
    mp = [30, 252]
    uuid = "d2c6df5105577fb59fb92529a36165a0"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 6
    # 念珠连射出数量 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 发射体前进距离比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 缩地成寸
# priest_female/sorceress/e0a072e8cef2d77893aad5f68aeed56a
# 0c1b401bb09241570d364420b3ba3fd7/e0a072e8cef2d77893aad5f68aeed56a
class Skill17(ActiveSkill):
    """
        使用法力缩小地形， 快速移动远距离。\n
        输入方向键时向该位置移动， 未输入时向后移动。\n
        到达地点后引发冲击波使敌人浮空。\n
        在决斗场中， [缩地成寸]没有浮空功能。
    """
    name = "缩地成寸"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 8
    rangeLv = 2
    cd = 4
    mp = [30, 30]
    uuid = "e0a072e8cef2d77893aad5f68aeed56a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # X轴移动距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # Y轴移动距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 束灵符
# priest_female/sorceress/de3fea2d65c597f4d55c70a02b97fc79
# 0c1b401bb09241570d364420b3ba3fd7/de3fea2d65c597f4d55c70a02b97fc79
class Skill18(ActiveSkill):
    """
        抛出符咒， 束缚敌人。\n
        符咒前行一定距离后， 生成束缚领域， 触碰到的敌人受到魔法伤害， 并使敌人进入短暂的强制控制状态； 可以在空中使用。\n
        [驱魔的方法有殴打法、 辟火法、 光明法、 阴阳法、 符咒法等。]
    """
    name = "束灵符"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cd = 7
    mp = [40, 300]
    uuid = "de3fea2d65c597f4d55c70a02b97fc79"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 束缚持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 护符爆炸大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 神谕之祈愿
# priest_female/sorceress/c61f5a010370101402b05b21916c2071
# 0c1b401bb09241570d364420b3ba3fd7/c61f5a010370101402b05b21916c2071
class Skill19(ActiveSkill):
    """
        向神龙祈祷， 给自身降下神谕。\n
        受到神谕后， 增加驱魔师的基本攻击力和技能攻击力， 并增加物理/魔法防御力。\n
        [用虔诚的心传承意志吧。]
    """
    name = "神谕之祈愿"
    learnLv = 20
    masterLv = 20
    maxLv = 30
    position = 2
    rangeLv = 3
    cd = 5
    uuid = "c61f5a010370101402b05b21916c2071"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理防御力增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 魔法防御力增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 增益效果持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)


# 驱邪咒
# priest_female/sorceress/202edb928046f4fa6dedf6337377efd5
# 0c1b401bb09241570d364420b3ba3fd7/202edb928046f4fa6dedf6337377efd5
class Skill21(ActiveSkill):
    """
        念出驱魔咒语， 击退敌人。\n
        施放过程中可以移动， 连按攻击键将以更快的速度发射。\n
        按跳跃键会终止该技能， 按Z键会转换方向。\n
        无苦集灭道， 无智亦无得。\n
        [学习乾坤之境后]\n
        额外生成除灵符， 对更大范围的敌人进行攻击。 
    """
    name = "驱邪咒"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 12
    mp = [35, 350]
    uuid = "202edb928046f4fa6dedf6337377efd5"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 15
    # 咒语发射数量 : {value1}字
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 发射间隔 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 文字大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 祈雨祭
# priest_female/sorceress/e1f72ce0c2592e738f711345efd8e25d
# 0c1b401bb09241570d364420b3ba3fd7/e1f72ce0c2592e738f711345efd8e25d
class Skill22(PassiveSkill):
    """
        作为被神龙选择的龙女， 拥有祈愿下雨的能力。\n
        增加驱魔师的基本攻击力和转职技能攻击力。
    """
    name = "祈雨祭"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 3
    uuid = "e1f72ce0c2592e738f711345efd8e25d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]

# 和合之玉
# priest_female/sorceress/2a3c96b88d02372505692da0a8b54743
# 0c1b401bb09241570d364420b3ba3fd7/2a3c96b88d02372505692da0a8b54743
class Skill23(ActiveSkill):
    """
        将念珠的力量汇聚成一个球体发射出去。\n
        和合之玉会穿透敌人， 达到一定距离后回到驱魔师位置。
    """
    name = "和合之玉"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 12
    mp = [150, 420]
    uuid = "2a3c96b88d02372505692da0a8b54743"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 前进时球体攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 返回时球体攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 球体大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 神术强化
# priest_female/sorceress/b8f4966608e4ebb3cc80ba4eac3649bb
# 0c1b401bb09241570d364420b3ba3fd7/b8f4966608e4ebb3cc80ba4eac3649bb
class Skill24(PassiveSkill):
    """
        提升驱魔师的法力， 增加暴击伤害、 暴击率、 命中率和施放速度。\n
        [在我面前放肆， 会得到刻骨铭心的教训！]
    """
    name = "神术强化"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 5
    rangeLv = 3
    uuid = "b8f4966608e4ebb3cc80ba4eac3649bb"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 暴击伤害增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 命中率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 施放速度增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    associate = [{"data":data0}]

# 聚魂吸星符
# priest_female/sorceress/b163d099c8cc27fdb6fd3639c2ee6df9
# 0c1b401bb09241570d364420b3ba3fd7/b163d099c8cc27fdb6fd3639c2ee6df9
class Skill25(ActiveSkill):
    """
        向前方发射神符， 吸附周围的邪恶之人。\n
        神符前进一定距离后， 吸附敌人并造成多段伤害。
    """
    name = "聚魂吸星符"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [200, 850]
    uuid = "b163d099c8cc27fdb6fd3639c2ee6df9"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 20
    # 符咒持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 多段攻击间隔 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 吸星符球体大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [聚魂吸星符]\n
        球体更强力地吸附周围敌人\n
        - 周围敌人吸附范围 +30%\n
        - 周围敌人吸附力 +30%\n
        球体大小 +30%
        """
        ...

    def vp_2(self):
        """
        [聚魂吸星符]\n
        存在被束灵符命中的敌人时， 在该敌人的位置生成球体\n
        - 可以在部分转职技能施放过程中施放， 使用该功能时可以无施法动作立即施放 (觉醒技能除外)
        """
        ...

# 龙魂之怒
# priest_female/sorceress/bc11d28c04e01923a093d65752c55516
# 0c1b401bb09241570d364420b3ba3fd7/bc11d28c04e01923a093d65752c55516
class Skill26(ActiveSkill):
    """
        将神龙的一部分力量具象化， 攻击前方一定范围内的敌人。\n
        [南无三曼多勃驮喃 喃舵 诃 喃舵 娑婆诃]
    """
    name = "龙魂之怒"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [250, 1260]
    uuid = "bc11d28c04e01923a093d65752c55516"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 技能攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 降落距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 爆炸大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [龙魂之怒]\n
        施放时， 驱魔师与神龙一起升空后猛击地面， 造成大范围伤害\n
        - 施放过程中所受伤害 -70%\n
        [唤雷符]\n
        施放[龙魂之怒]时， 自动施放强化版[唤雷符]\n
        - 强化版[唤雷符]攻击力为原[唤雷符]的350%\n
        - 无法使用普通[唤雷符]
        """
        ...

    def vp_2(self):
        """
        [龙魂之怒]\n
        施放时， 破开前方的天空， 随后在该位置降下神龙猛击\n
        - 可以在部分转职技能施放过程中施放， 使用该功能时可以无施放动作立即施放 (觉醒技能除外)
        """
        ...

# 百八念珠
# priest_female/sorceress/faf9cd66281078b51be2ee0b0f6c5530
# 0c1b401bb09241570d364420b3ba3fd7/faf9cd66281078b51be2ee0b0f6c5530
class Skill27(ActiveSkill):
    """
        集中神力， 生成多个念珠射向敌人。\n
    生成的念珠在碰到敌人后爆炸， 给单个目标造成很高的伤害。\n
    当发现被[束灵符]束缚的敌人时， 念珠会追击该敌人。\n
        如果持续按住技能键， 将射出可穿透敌人的念珠， 在地面形成大量的爆炸， 给范围内的所有敌人造成大范围爆炸伤害。\n
        可以在空中施放， 但是无法使用大范围爆炸。\n
        在决斗场中， 念珠不会向被[束灵符]束缚的敌人移动。\n
        [文楹当知， 四众龙神， 瞻察仁者， 为说何等]
    """
    name = "百八念珠"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [250, 1260]
    uuid = "faf9cd66281078b51be2ee0b0f6c5530"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # [百八念珠]攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 20
    # 念珠射出数量 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 范围爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 0
    # 范围多段攻击次数 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 念珠大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 范围爆炸攻击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [百八念珠]\n
        - 普通施放时， 念珠会追踪驱魔师前方一定范围内最近的敌人， 并追加飞向敌人的功能\n
        - 施放时， 念珠速度 +30%\n
        - 施放时， 念珠大小 +10%\n
        施放范围爆炸时， 生成无数念珠， 对驱魔师周围大范围进行最多5次的多段攻击\n
        - 施放时， 念珠速度 +30%\n
        - 施放时， 爆炸范围 +10%
        """
        ...

    def vp_2(self):
        """
        [百八念珠]\n
        普通施放时， 10秒内所有速度 +10%\n
        施放范围爆炸时， 10秒内回避率 +10%\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 12.5秒\n
        - 单次攻击力 -50%
        """
        self.cd = 12.5
        self.skillRation *= 1 - 0.5
        ...

# 不动珠箔阵
# priest_female/sorceress/d296043df164385a14cb973c8c7c4d07
# 0c1b401bb09241570d364420b3ba3fd7/d296043df164385a14cb973c8c7c4d07
class Skill28(ActiveSkill):
    """
        生成可以困住敌人的阵法后， 移动念珠攻击敌人。\n
        阵法内的敌人无法出去， 阵法外的敌人也无法进来。\n
        多段攻击时， 按跳跃键会立即施放最后一击。\n
        在决斗场中， 按跳跃键不会立即施放最后一击。
    """
    name = "不动珠箔阵"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [250, 2500]
    uuid = "d296043df164385a14cb973c8c7c4d07"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 念珠多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 24
    # 念珠旋转次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 魔法阵大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [不动珠箔阵]\n
        [不动珠箔阵]发动后结束施放动作\n
        - 攻击范围 +20%
        """
        ...

    def vp_2(self):
        """
        [不动珠箔阵]\n
        施放技能时进入无敌状态\n
        - 使攻击中的目标进入强制控制状态
        """
        ...

# 神龙如意珠
# priest_female/sorceress/6e33d47e6622ce03b6defdd912140270
# 0c1b401bb09241570d364420b3ba3fd7/6e33d47e6622ce03b6defdd912140270
class Skill29(ActiveSkill):
    """
        吸收神龙的力量， 攻击时造成额外的魔法伤害， 并增加驱魔师的基本攻击和所有技能攻击力。\n
        在决斗场中， 攻击时不造成额外的魔法伤害。
    """
    name = "神龙如意珠"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 3
    uuid = "6e33d47e6622ce03b6defdd912140270"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    type = "passive"
    cd = 1
    cdReduceP = 1

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 追加攻击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 追加攻击冷却时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 追加打击大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    associate = [{"data":data0}]

    def getSkillCD(self, mode=None):
        return self.cd * (1-self.cdReduceP)

# 神谕 : 神龙雷雨祭
# priest_female/sorceress/ca75c965f20a150f99f54155a37400df
# 0c1b401bb09241570d364420b3ba3fd7/ca75c965f20a150f99f54155a37400df
class Skill30(ActiveSkill):
    """
        驱魔师通过神谕， 使神龙降临到现世。\n
        神龙会制造铺天盖地的乌云和强烈的雷雨， 惩罚世上的一切罪恶。\n
        [神龙大人！ 拯救这些受苦的人吧！]
    """
    name = "神谕 : 神龙雷雨祭"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [900, 7559]
    uuid = "ca75c965f20a150f99f54155a37400df"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 雷雨多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 16
    # 雷雨持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 雷雨多段攻击间隔 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最后一击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1

# 因果业火符
# priest_female/sorceress/1721e94897e9961d5c98130a13392f17
# 0c1b401bb09241570d364420b3ba3fd7/1721e94897e9961d5c98130a13392f17
class Skill31(ActiveSkill):
    """
        抛出减速周围敌人， 并在被击时爆炸的符咒。\n
        符咒前进一定距离后生成阵法， 减速阵法内的敌人。 当驱魔师用转职技能攻击符咒时， 符咒会爆炸， 给周围的敌人造成伤害。\n
        达到爆炸次数上限、 追加技能操作， 或者符咒持续时间结束后， 引起最后一次爆炸。\n
        利用ON/OFF可以开启或关闭减速敌人的功能， 施放时可以通过前方向键来增加放置距离。\n
        [神龙赐予的灵力和龙女虔诚的心与意志凝聚而成的神气， 虽无形体， 却可通过符咒留下自己的痕迹。]
    """
    name = "因果业火符"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [400, 1620]
    uuid = "1721e94897e9961d5c98130a13392f17"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 范围内的敌人移动速度减少 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 范围内的敌人攻击速度减少 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 打击时爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 7
    # 爆炸最大次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 护符最大持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 最后一击爆炸攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # [范围信息]
    # 大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [因果业火符]\n
        魔法阵碰到敌人时， 强制控制敌人2秒\n
        爆炸攻击次数上限变更为3次\n
        - 总攻击力相同\n
        范围大小 +10%
        """
        ...

    def vp_2(self):
        """
        [因果业火符]\n
        投掷因果业火符后立即爆炸\n
        - 在被爆炸攻击到的所有敌人的身体上， 附着可以爆炸7次的因果业火符\n
        - 附着的因果业火符持续10秒， 在持续期间赋予与[束灵符]相同的技能追踪功能
        """
        ...

# 夺命大念阵
# priest_female/sorceress/51a08fd0c90f0a5276cd552047fac93d
# 0c1b401bb09241570d364420b3ba3fd7/51a08fd0c90f0a5276cd552047fac93d
class Skill32(ActiveSkill):
    """
        驱魔师将法力注入念珠， 在前方画出夺命大念阵。\n
        赋予法力的念珠会击退敌人， 稍后阵法会爆炸， 对范围内的所有敌人造成伤害。
    """
    name = "夺命大念阵"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [800, 1680]
    uuid = "51a08fd0c90f0a5276cd552047fac93d"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 念珠撞击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 6
    # 念珠撞击多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 阵法爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 爆炸大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [夺命大念阵]\n
        施放时在地面生成魔法阵， 升天的神龙对范围内所有敌人进行多段攻击后爆炸\n
        - 魔法阵在驱魔师周围500px内最强敌人的位置生成\n
        - 仅在攻击范围内存在敌人时可以使用\n
        最终爆炸范围 +10%
        """
        ...

    def vp_2(self):
        """
        [夺命大念阵]\n
        [夺命大念阵]施放速度 +40%\n
        [缩地成寸]\n
        施放[夺命大念阵]时， 初始化[缩地成寸]的冷却时间\n
        [夺命大念阵]念珠发射后， 可以施放[缩地成寸]
        """
        ...

# 龙神之力
# priest_female/sorceress/2c9d9a36c8401bddff6cdb80fab8dc24
# 0c1b401bb09241570d364420b3ba3fd7/2c9d9a36c8401bddff6cdb80fab8dc24
class Skill33(PassiveSkill):
    """
        龙神之力赋予御龙仙女强大的力量， 在攻击时造成附加伤害， 提高念珠射出的攻击力， 减少神龙如意珠附加伤害的冷却时间。\n
        被击时一段时间内增加物理/魔法防御力。
    """
    name = "龙神之力"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 3
    uuid = "2c9d9a36c8401bddff6cdb80fab8dc24"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 附加伤害 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 念珠射出攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [神龙如意珠]附加伤害冷却时间减少率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 物理/魔法防御力增加量 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 所受伤害减少效果持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 所受伤害减少效果冷却时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)

    associate = [
        {"data":data0},
        {"data":data1,"skills":["念珠连射"]},
        {"data":data2,"skills":["神龙如意珠"],"type":"-cdReduceP"},
    ]

# 退魔阴阳符
# priest_female/sorceress/b89c9ab317bc0a443f6497b7cca2f6a8
# 0c1b401bb09241570d364420b3ba3fd7/b89c9ab317bc0a443f6497b7cca2f6a8
class Skill34(ActiveSkill):
    """
        在前方形成多个退魔符， 然后射出退魔阴阳玉攻击敌人。\n
        阴阳玉把敌人击退， 然后用退魔符进行多段攻击。
    """
    name = "退魔阴阳符"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "b89c9ab317bc0a443f6497b7cca2f6a8"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 击退念珠攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 弹射打击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 12
    # 弹射次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [退魔阴阳符]\n
        使用符咒生成魔魂爆炎阵\n
        弹射攻击结束后， 引发魔魂爆炎阵爆炸\n
        - 总攻击力相同\n
        攻击范围 +35%
        """
        ...

    def vp_2(self):
        """
        [退魔阴阳符]\n
        施放时， 退魔阴阳符攻击更大的范围， 并自动使用[驱邪咒]\n
        - 在前方召唤[驱邪咒]并发射\n
        - [驱邪咒]在冷却时间内时， 不发动该效果\n
        基本冷却时间变更为24秒\n
        - 总攻击力 -40%\n
        [驱邪咒]\n
        [驱邪咒]发射次数变更为6次\n
        - 总攻击力相同
        """
        self.cd = 24
        self.skillRation *= 1 - 0.4
        ...

# 天坠阴阳玉
# priest_female/sorceress/7cf17936a039b418660424125dc968d7
# 0c1b401bb09241570d364420b3ba3fd7/7cf17936a039b418660424125dc968d7
class Skill35(ActiveSkill):
    """
        召唤超大型阴阳玉， 将前方区域炙烤成一片焦土。\n
        阴阳玉坠落时， 可以利用前方方向键调整降落位置； 可以在空中施放。
    """
    name = "天坠阴阳玉"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [580, 4500]
    uuid = "7cf17936a039b418660424125dc968d7"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 下降打击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 下降最多打击次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 念珠大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [天坠阴阳玉]\n
        下降速度增加； 并且删除下降攻击， 立即爆炸\n
        - 下降速度 +25%\n
        - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [天坠阴阳玉]\n
        施放时破开天空， 一定时间内自动向驱魔师周围最强敌人掉落念珠\n
        - 小型念珠掉落结束后或破开天空状态下再次按技能键时， 召唤巨型阴阳玉\n
        - 无法在空中施放\n
        - 有被束灵符]束缚的目标时， 念珠会优先追踪目标\n
        - 基本冷却时间变更为67.5秒\n
        总攻击力 +50%
        """
        self.cd = 67.5
        self.skillRation *= 1.5
        ...

# 龙威如狱·龙恩如海
# priest_female/sorceress/7f80b887a09e88e2c4728c898bd73654
# 0c1b401bb09241570d364420b3ba3fd7/7f80b887a09e88e2c4728c898bd73654
class Skill36(ActiveSkill):
    """
        神龙现身这个世界解救众生。 御龙仙女与神龙合为一体惩戒世上的邪恶， 随后升天消失。\n
        被打击的敌人处于强制控制状态并且受到伤害。\n
    <连按效果>\n
        连续按技能快捷键或<X>攻击键， 可以加快技能施放速度。
    """
    name = "龙威如狱·龙恩如海"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "7f80b887a09e88e2c4728c898bd73654"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 神龙移动攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 9
    # 神龙移动多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 升天多段攻击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 6
    # 升天多段攻击次数 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 最后一击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1

# 乾坤之境
# priest_female/sorceress/5806440d21e7546d50007a5ba11f8024
# 0c1b401bb09241570d364420b3ba3fd7/5806440d21e7546d50007a5ba11f8024
class Skill37(PassiveSkill):
    """
        作为行使神龙之力的代行者， 获得掌控天空气息的权能。 增加基本攻击力和技能攻击力， 部分技能附加特殊效果。\n
    [唤雷符] : 可以探索施放者周围的350px内的敌人后施放， 最多向12名敌人召唤落雷。 闪电对每名敌人最多造成1次伤害。\n
    [驱邪咒] : 生成除灵符， 对更大范围的敌人进行攻击。 
    """
    name = "乾坤之境"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "5806440d21e7546d50007a5ba11f8024"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]

# 天泽神龙阵
# priest_female/sorceress/d429147c372b549c3dadcabcba50787f
# 0c1b401bb09241570d364420b3ba3fd7/d429147c372b549c3dadcabcba50787f
class Skill38(ActiveSkill):
    """
        使用蕴含神力的符咒画出阵法后， 通过阵法释放神龙气息。 随后， 投掷符咒并将其引爆。
    """
    name = "天泽神龙阵"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [870, 6750]
    uuid = "d429147c372b549c3dadcabcba50787f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 神龙的气息攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 10
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 符咒爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

# 神龙之舞·天一
# priest_female/sorceress/7ec521d063d2190e1fcc5bd229af9bcf
# 0c1b401bb09241570d364420b3ba3fd7/7ec521d063d2190e1fcc5bd229af9bcf
class Skill39(ActiveSkill):
    """
        光启·驱魔师翩翩起舞， 与神龙化为一体， 将蕴含神力的念珠和神龙一起升至空中， 然后向敌人降下天罚。\n
       最后念珠化为神龙如意珠， 与神龙一起歼灭地上的敌人。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "神龙之舞·天一"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4000, 8000]
    uuid = "7ec521d063d2190e1fcc5bd229af9bcf"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 念珠碰撞攻击力 : {value0}% x {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 如意珠碰撞攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 如意珠爆炸多段攻击力 : {value3}% x {value4}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 7
    data4 = get_data(f'{prefix}/{uuid}', 4)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'sorceress'
        self.nameCN = '神启·巫女'
        self.role = 'priest_female'
        self.角色 = '圣职者(女)'
        self.职业 = '巫女'
        self.jobId = '0c1b401bb09241570d364420b3ba3fd7'
        self.jobGrowId = '6d459bc74ba73ee4fe5cdc4655400193'

        self.武器选项 = ['光杖','念珠','图腾','镰刀','战斧']
        self.输出类型选项 = ['魔法百分比']
        self.输出类型 = '魔法百分比' # TODO
        self.防具精通属性 = ['智力'] # TODO
        self.防具类型 = '智力'
        self.buff = 2.153

        super().__init__(equVersion, __name__)
