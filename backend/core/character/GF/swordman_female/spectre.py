#1645c45aabb008c98406b3a16447040d
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "swordman_female/spectre/cn/skillDetail"


# 冥思
# swordman_female/spectre/d89f26862e348a801b30bb9fd7125db5
# 1645c45aabb008c98406b3a16447040d/d89f26862e348a801b30bb9fd7125db5
class Skill1(PassiveSkill):
    """
        进行战斗期间， 将根据连击数按比例增加物理或魔法暴击率。\n
        增益效果可以重复触发， 但是有触发次数上限。 增益效果重复触发时， 更新现有增益效果的持续时间。
    """
    name = "冥思"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 8
    rangeLv = 3
    uuid = "d89f26862e348a801b30bb9fd7125db5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 触发增益效果所需连击数 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 暴击率增加上限 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 增益效果持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)


# 基础精通
# swordman_female/spectre/5a56514f35cf0270ae8d6c65f8fefd78
# 1645c45aabb008c98406b3a16447040d/5a56514f35cf0270ae8d6c65f8fefd78
class Skill3(PassiveSkill):
    """
        增加基本攻击、 前冲攻击、 跳跃攻击、 [浮空击]的攻击力。\n
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

    associate = [{"type":"*skillDamage","data":[i-100 if i>0 else 0 for i in data0],"skills":["鬼缚钉"]}]


# 刃之心
# swordman_female/spectre/68062215e75d92575958873ac8ede31a
# 1645c45aabb008c98406b3a16447040d/68062215e75d92575958873ac8ede31a
class Skill5(PassiveSkill):
    """
        不法之地的剑客配备唯一信赖的挚友——刃匣“金刚”。 \n
        大太刀“黑曜”和小太刀“白牙”收纳于“金刚”之中。 基本攻击变更为刃影专属姿势。
    """
    name = "刃之心"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 6
    rangeLv = 3
    uuid = "68062215e75d92575958873ac8ede31a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

# 双重斩
# swordman_female/spectre/9376d04c476cd41d60ed1974ca69ab95
# 1645c45aabb008c98406b3a16447040d/9376d04c476cd41d60ed1974ca69ab95
class Skill6(ActiveSkill):
    """
        同时拔出主武器和白牙， 对敌人快速发动2次斩击。 基本攻击过程中使用时， 无需准备姿势， 立即攻击。
    """
    name = "双重斩"
    learnLv = 1
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 4
    mp = [20, 250]
    uuid = "9376d04c476cd41d60ed1974ca69ab95"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 斩击攻击力 : {value0} x 2
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2


# 鬼缚钉
# swordman_female/spectre/ef9d26746effee9199b54541f01b8752
# 1645c45aabb008c98406b3a16447040d/ef9d26746effee9199b54541f01b8752
class Skill10(ActiveSkill):
    """
        前方一定范围内存在敌人时， 可以施放该技能。\n
        利用鬼缚珠的魔力生成鬼缚丝， 向范围内的敌人中最强的敌人发射并控制敌人， 然后快速接近并连续攻击敌人。\n
        技能受[基础精通]的影响， 且可以在空中施放。\n
        决斗场中无法使用。
    """
    name = "鬼缚钉"
    learnLv = 5
    masterLv = 1
    maxLv = 1
    position = 4
    rangeLv = 2
    cd = 7
    mp = [75, 75]
    uuid = "ef9d26746effee9199b54541f01b8752"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 踢击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 斩击攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 索敌距离 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 索敌范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 索敌高度 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 回旋勾斩
# swordman_female/spectre/dec8961c485edb02036ba00c789010f0
# 1645c45aabb008c98406b3a16447040d/dec8961c485edb02036ba00c789010f0
class Skill17(ActiveSkill):
    """
        向前方大范围挥舞连着鬼缚丝的白牙， 聚拢敌人后， 发动下劈攻击。
    """
    name = "回旋勾斩"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 8
    mp = [60, 560]
    uuid = "dec8961c485edb02036ba00c789010f0"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 挥击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 下劈攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)


# 孤勇之志
# swordman_female/spectre/e36ae35f8964d92e30e33529a65544d7
# 1645c45aabb008c98406b3a16447040d/e36ae35f8964d92e30e33529a65544d7
class Skill19(PassiveSkill):
    """
        为了达到目的， 不惧直面痛苦的过去， 将痛苦化作斗志， 展现出孤勇意志。\n
        增加独立攻击力， 装备太刀时增加命中率， [疾风斩]附加出血效果。 
    """
    name = "孤勇之志"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 3
    uuid = "e36ae35f8964d92e30e33529a65544d7"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 独立攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 装备太刀时命中率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [
        {"type":"$*PAtkI","data":data0},
    ]

# 封喉丝
# swordman_female/spectre/f1fdc6c2482ecc510a2a9f04201ba125
# 1645c45aabb008c98406b3a16447040d/f1fdc6c2482ecc510a2a9f04201ba125
class Skill20(ActiveSkill):
    """
        该技能可以在空中施放。\n
        向前方跳跃。 用鬼缚丝缠绕跳跃时撞到的敌人， 封锁其动作， 然后向前方投掷。\n
        被扔出的敌人砸到地面时产生冲击波， 对其自身和周围敌人造成伤害， 且路径上撞到敌人时也会造成伤害。\n
        可利用方向键调整突进方向和投掷距离。\n
        攻击无法抓取的敌人时， 抓住并切断鬼缚丝， 对敌人造成伤害。\n
        决斗场中不可在空中施放。
    """
    name = "封喉丝"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 8
    mp = [46, 380]
    uuid = "f1fdc6c2482ecc510a2a9f04201ba125"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本投掷的距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 按下方向键时投掷距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 地面冲击波攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 0
    # 路径碰撞攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 对无法抓取敌人的鬼缚丝切断攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # [范围信息]
    # 冲击波范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 利刃旋风
# swordman_female/spectre/8e1891ddbdd5ebfcc4508ff2090c3e0f
# 1645c45aabb008c98406b3a16447040d/8e1891ddbdd5ebfcc4508ff2090c3e0f
class Skill21(ActiveSkill):
    """
        将斗气注入剑中， 强力斩击地面， 然后发动第二次斩击， 生成锋利旋风， 攻击范围内的敌人。
    """
    name = "利刃旋风"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 1
    rangeLv = 2
    cd = 6
    mp = [35, 300]
    uuid = "8e1891ddbdd5ebfcc4508ff2090c3e0f"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 第一次斩击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第二次斩击攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 旋风多段攻击次数上限 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 旋风每段攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 5
    # [范围信息]
    # 旋风大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 追踪术
# swordman_female/spectre/c39c703f72d289fcd5a8f182068140d4
# 1645c45aabb008c98406b3a16447040d/c39c703f72d289fcd5a8f182068140d4
class Skill22(ActiveSkill):
    """
        释放鬼缚珠的魔力， 获取追踪目标所需要的信息。\n
        增加自身基本攻击力、 技能攻击力、 移动速度和[鬼缚钉]的索敌范围。
    """
    name = "追踪术"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 3
    cd = 5
    uuid = "c39c703f72d289fcd5a8f182068140d4"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 移动速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [鬼缚钉]索敌范围增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 白牙落斩
# swordman_female/spectre/8c10cefa65364880451e389bb74d3600
# 1645c45aabb008c98406b3a16447040d/8c10cefa65364880451e389bb74d3600
class Skill23(ActiveSkill):
    """
        该技能可以在空中施放。\n
        在白牙上挂上鬼缚丝， 向天花板掷出， 然后跳起。 到达最高点的瞬间， 拔出白牙， 发动强力下斩。\n
        按下方向键可落回原地； 按向前方向键， 可落到更远的地方。\n
        倒地和空中被击时也可以施放该技能， 此时进入无敌状态。\n
        决斗场中不可在空中、 倒地或空中被击时使用。
    """
    name = "白牙落斩"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 10
    mp = [44, 375]
    uuid = "8c10cefa65364880451e389bb74d3600"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本下落移动距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 按向前方向键时下落移动距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 下斩攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 疾刃之影
# swordman_female/spectre/38805520deffc10fac2e8f881ab7682b
# 1645c45aabb008c98406b3a16447040d/38805520deffc10fac2e8f881ab7682b
class Skill24(ActiveSkill):
    """
        冷静地蓄力后， 拔刀斩击周围敌人， 留下锐利剑痕。
    """
    name = "疾刃之影"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 8
    mp = [61, 640]
    uuid = "38805520deffc10fac2e8f881ab7682b"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 剑痕攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 薄暮利刃
# swordman_female/spectre/66a9967e677651d0def34c475795ccde
# 1645c45aabb008c98406b3a16447040d/66a9967e677651d0def34c475795ccde
class Skill25(ActiveSkill):
    """
        快速拔出黑曜， 发动多段攻击击倒前方敌人。\n
        除[回旋十字刃]和觉醒系列技能之外的转职技能命中敌人时， 可以强制中断并立即施放该技能。\n
        决斗场中， 无法强制中断并立即施放该技能。
    """
    name = "薄暮利刃"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 9
    mp = [70, 700]
    uuid = "66a9967e677651d0def34c475795ccde"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 多段攻击次数上限 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 每段攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 5
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 刃之决意
# swordman_female/spectre/b69d38bcddd41b3566c6d5cf78d060bb
# 1645c45aabb008c98406b3a16447040d/b69d38bcddd41b3566c6d5cf78d060bb
class Skill26(PassiveSkill):
    """
        长期以来多次执行任务， 比任何工具和方法都能更有效地磨炼剑术。\n
        增加暴击攻击力； 装备太刀时， 可增加暴击率。
    """
    name = "刃之决意"
    learnLv = 35
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 3
    uuid = "b69d38bcddd41b3566c6d5cf78d060bb"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 暴击攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 装备太刀时暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [
        {"type":"*skillDamage","data":data0},
    ]

# 黑夜之花
# swordman_female/spectre/030663e99462f628b4c9f813e1406c4e
# 1645c45aabb008c98406b3a16447040d/030663e99462f628b4c9f813e1406c4e
class Skill27(ActiveSkill):
    """
        将主武器和白牙交叉， 然后向反方向快速斩击。\n
        斩击范围内产生冲击波， 对路径内的敌人造成连续攻击。
    """
    name = "黑夜之花"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 1
    rangeLv = 2
    cd = 14
    mp = [156, 822]
    uuid = "030663e99462f628b4c9f813e1406c4e"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 起始斩击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波多段攻击次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 冲击波每段攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 5
    # [范围信息]
    # 剑风攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [黑夜之花]\n
        收刀后向前方大幅挥斩\n
        - 变更为收刀术系列技能\n
        - 无法维持准备动作\n
        - 删除起始斩击和剑风\n
        - 基本冷却时间变更为24.5秒\n
        - 收刀攻击力为攻击力总和的175%
        """
        self.cd = 24.5
        self.skillRation *= 1.75
        ...

    def vp_2(self):
        """
        [黑夜之花]\n
        学习[夜色敌意]后， 施放时立即进入无敌状态， 持续时间上限变更为1.2秒\n
        准备动作维持时间越长， 剑风范围越大 (最多40%)\n
        [招架]\n
        所受伤害减少率 +50%
        """
        ...

# 回旋十字刃
# swordman_female/spectre/150aa05b9ee8b9c7c04a25f3e425900c
# 1645c45aabb008c98406b3a16447040d/150aa05b9ee8b9c7c04a25f3e425900c
class Skill28(ActiveSkill):
    """
        用鬼缚丝牵着白牙发动回旋攻击， 同时跳到空中。 命中时将敌人拉到刃影面前。\n
        回旋攻击后， 在空中回收白牙， 释放锐利剑气， 攻击范围内的敌人。\n
        按向前方向键， 可增加前进距离。\n
        在决斗场中， 无法拉动命中的敌人。
    """
    name = "回旋十字刃"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 1
    cd = 16
    mp = [179, 940]
    uuid = "150aa05b9ee8b9c7c04a25f3e425900c"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 回旋攻击多段攻击次数上限 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 回旋攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 5
    # 终结剑气攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 技能结束后霸体持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 终结斩击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [回旋十字刃]\n
        可以在空中施放\n
        施放时根据角色位置删除部分动作\n
        - 地面施放时删除终结斩击\n
        - 空中施放时删除回旋斩击\n
        - 总攻击力相同\n
        攻击范围 +35%
        """
        ...

    def vp_2(self):
        """
        [回旋十字刃]\n
        终结斩击后处于空中时， 按跳跃键可以跳跃\n
        - 按向左或右方向键时， 可向相应方向跳跃\n
        旋转斩击攻击速度 +100%\n
        终结斩击范围 +50%
        """
        ...

# 夜之风
# swordman_female/spectre/89c505581267af77c6d58dc49b710550
# 1645c45aabb008c98406b3a16447040d/89c505581267af77c6d58dc49b710550
class Skill29(ActiveSkill):
    """
        该技能可以在空中施放。\n
        向后翻滚的同时从剑鞘中拔出黑曜， 然后用力下劈， 释放剑风。 剑风对命中的敌人造成多段伤害。\n
        空中施放时， 落地前可以预输入收刀术系列技能键， 并在落地瞬间发动收刀术。\n
        决斗场中不可在空中施放。
    """
    name = "夜之风"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [235, 1974]
    uuid = "89c505581267af77c6d58dc49b710550"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 黑曜剑风多段攻击次数上限 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 黑曜剑风每段攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 3
    # [范围信息]
    # 剑风大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [夜之风]\n
        被击和倒地状态下可施放该技能， 此时进入无敌状态\n
        剑风大小和前进距离 +15%\n
        变更为单次攻击\n
        - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [夜之风]\n
        无法在空中施放\n
        蹬地后用黑曜划过地面， 向前突进并产生剑风\n
        - 变更为剑风单次攻击\n
        - 被剑风命中的敌人会被吸附到自身下方\n
        - 在空中向下劈斩结束冲锋\n
        - 总攻击力相同\n
        突进过程中再次按技能键或发动[收刀术]时， 立即在该位置后空翻\n
        - 后空翻并回头下劈后下落\n
        - 预输入[收刀术]时， 会在后空翻结束后施放
        """
        ...

# 秘术·心斩
# swordman_female/spectre/a81e5b7defa1819263ed8e86f69fd06f
# 1645c45aabb008c98406b3a16447040d/a81e5b7defa1819263ed8e86f69fd06f
class Skill30(ActiveSkill):
    """
    [收刀术系列]\n
        将黑曜收刀， 精神集中到极致。 然后， 以本人为中心向斜线方向拔刀， 对范围内的敌人发动斩击。\n
        学习[收刀秘术]后， 可通过[收刀术]发动。
    """
    name = "秘术·心斩"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [250, 2503]
    uuid = "a81e5b7defa1819263ed8e86f69fd06f"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 拔刀攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [秘术·心斩]\n
        发动技能时进入无敌状态\n
        使被命中的敌人进入控制状态， 效果持续1.5秒
        """
        ...

    def vp_2(self):
        """
        [秘术·心斩]\n
        精神集中时间 -50%\n
        收刀术连招成功时范围 +20%， 20秒内所有速度+10%
        """
        ...

# 收刀秘术
# swordman_female/spectre/89a4529234904fcbb3abe289e281f2fd
# 1645c45aabb008c98406b3a16447040d/89a4529234904fcbb3abe289e281f2fd
class Skill31(PassiveSkill):
    """
        经过艰苦的修炼， 彻底掌握了收刀术。\n
        学习后， 增加基本攻击力和技能攻击力； 装备太刀时， 增加攻击速度。 \n
        部分转职系列技能可以强制中断并立即施放收刀术系列技能。 \n
        [收刀术]\n
    -    施放过程中， 可以强制中断并施放[收刀术]系列技能。 \n
    -    技能被强制中断后的攻击力并入[收刀术]技能。\n
    -    施放收刀术时， 会出现特殊插画。\n
    -    收刀术技能 : [秘术·心斩]、 [秘术·曜夜斩]、 [黑曜真刃·破晓]\n
        部分技能无法发动收刀术或有发动时机限制。 \n
    -    [白牙落斩]、 [追袭逐影丝] : 在地面上连接鬼缚丝期间可施放收刀术系列技能。\n
    -    [沉寂之狱]、 [悬丝风暴] : 可根据各技能的[特殊功能]中标明的时机预约发动\n
    -    无法发动收刀术的技能 : [鬼缚钉]、 [冲击斩]、 [封喉丝]、 [薄暮利刃]、 [回旋十字刃]、 [绚烂之舞]、 [秘术·雨夜终曲]
    """
    name = "收刀秘术"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 3
    uuid = "89a4529234904fcbb3abe289e281f2fd"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 装备太刀时攻击速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [
        {"type":"*skillDamage","data":data0},
    ]

# 沉寂之狱
# swordman_female/spectre/515b442ffbf61a82371abb645c149a31
# 1645c45aabb008c98406b3a16447040d/515b442ffbf61a82371abb645c149a31
class Skill32(ActiveSkill):
    """
        释放鬼缚珠的力量， 生成无数鬼缚丝穿透周围敌人， 然后拔出黑曜， 和鬼缚丝一同斩击敌人。\n
        鬼缚丝攻击期间可预约[收刀术]技能； 预约[收刀术]技能时， 预约的技能也进入无敌状态。
    """
    name = "沉寂之狱"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [900, 7559]
    uuid = "515b442ffbf61a82371abb645c149a31"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 鬼缚丝攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 黑曜拔刀攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

# 瞬影碎魂击
# swordman_female/spectre/87a918bb22cfc959a16e0bf939bb6c24
# 1645c45aabb008c98406b3a16447040d/87a918bb22cfc959a16e0bf939bb6c24
class Skill33(ActiveSkill):
    """
        将身体反射神经和爆发力发挥到极致。 用强有力的踢击踢开前方的敌人， 然后利用后坐力低空跳跃， 向地面连续发射白牙， 攻击并强制控制范围内的敌人。\n
    然后用剑劈被破坏的地面， 展开终结攻击。\n
        终结攻击前连接收刀术系列技能， 可以延长强制控制时间。
    """
    name = "瞬影碎魂击"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [280, 784]
    uuid = "87a918bb22cfc959a16e0bf939bb6c24"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 踢击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 白牙发射次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 白牙发射攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 3
    # 白牙终结攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 强制控制延长时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 最后一击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [瞬影碎魂击]\n
        除[回旋十字刃]和觉醒技能外的转职技能命中时， 可以强制中断僵直并立即施放[瞬影碎魂击]\n
        [瞬影碎魂击]命中敌人时， 可以强制中断僵直并立即施放转职技能
        """
        ...

    def vp_2(self):
        """
        [瞬影碎魂击]\n
        第1次踢击后不会进行白牙发射攻击， 立即发动最后一击\n
        - 删除白牙发射攻击\n
        - 白牙终结范围 +30%\n
        - 总攻击力相同
        """
        ...

# 追袭逐影丝
# swordman_female/spectre/aa51c4ddf1659092fa9ed612b9837061
# 1645c45aabb008c98406b3a16447040d/aa51c4ddf1659092fa9ed612b9837061
class Skill34(ActiveSkill):
    """
        向对角线方向发射鬼缚丝并将其固定到天花板上， 然后跳跃并释放剑气， 攻击正面的敌人。\n
        然后向命中的敌人中最强的敌人发射鬼缚丝， 确定方向后快速落地并发动下斩。\n
        没有攻击目标时， 向正面最远移动位置发动下斩。
    """
    name = "追袭逐影丝"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [756, 1587]
    uuid = "aa51c4ddf1659092fa9ed612b9837061"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 剑气释放攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 落地下劈攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 没有攻击目标时最远移动距离 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [追袭逐影丝]\n
        更快速地搜寻并攻击敌人\n
        - 剑气施放鬼缚丝动作时间 -20%\n
        - 落地等待时间 -50%\n
        - 下斩范围 +20%\n
        使用[追袭逐影丝]时， [鬼缚钉]冷却时间初始化\n
        [鬼缚钉]\n
        攻击力 -12.3%
        """
        ...

    def vp_2(self):
        """
        [追袭逐影丝]\n
        无法在空中施放\n
        在白牙上挂上鬼缚丝， 向前方最强敌人掷出， 随后回收鬼缚丝并接近敌人将其踢飞\n
        - 总攻击力相同\n
        - 向敌人突进前可以发动收刀术\n
        - 突进失败时， 冷却时间缩短为5秒
        """
        ...
    def effect(self, old, new):
        if self.vp == 1:
            self.associate = [{"type":"*skillDamage","data":[0] + [-12.3]*self.maxLv,"skills":["鬼缚钉"]}]
        return super().effect(old, new)

# 无情夜行
# swordman_female/spectre/863295a0fc634cf5fcc01e82a735fd6b
# 1645c45aabb008c98406b3a16447040d/863295a0fc634cf5fcc01e82a735fd6b
class Skill35(PassiveSkill):
    """
        冷酷无情的夜皇， 手中的剑刃没有一丝慈悲。\n
        增加基本攻击力和转职技能攻击力； 减少除觉醒技能之外的技能冷却时间。
    """
    name = "无情夜行"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 3
    uuid = "863295a0fc634cf5fcc01e82a735fd6b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 技能冷却时间减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [
        {"type":"*skillDamage","data":data0},
        {"type":"*cdReduce","data":data1,"exceptSkills":['沉寂之狱', '黑曜真刃·破晓', '秘术·雨夜终曲']},
    ]

# 秘术·曜夜斩
# swordman_female/spectre/3153ca0e6752a6283412c59c5ec8e002
# 1645c45aabb008c98406b3a16447040d/3153ca0e6752a6283412c59c5ec8e002
class Skill36(ActiveSkill):
    """
    [收刀术系列]\n
        将黑曜收刀后蓄气， 然后向前方拔刀。 剑气划过地面时产生冲击波， 对范围内的敌人造成巨大伤害。\n
        按向前方向键可向前突进， 对路径上的所有敌人造成伤害。
    """
    name = "秘术·曜夜斩"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "3153ca0e6752a6283412c59c5ec8e002"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 拔刀攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 剑气攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [秘术·曜夜斩]\n
        更冷静快速地收刀\n
        - [收刀术]成功连招时， 准备动作时间 -50%\n
        - 按向前方向键时， 增加突进距离\n
        - 剑气攻击范围 +15%\n
        将攻击命中的敌人中后方的敌人拉到前方
        """
        ...

    def vp_2(self):
        """
        [秘术·曜夜斩]\n
        可以在空中施放\n
        - 可施放高度上限 : 400px\n
        - 空中施放时， 删除输入前方向键功能\n
        部分技能空中施放时， 可以发动[收刀术]\n
        - [夜之风] : 学习[黎明]后， 不会后空翻， 转身施放[收刀术]\n
        - [白牙落斩] : 鬼缚丝动作中可施放[收刀术]\n
        - [追袭逐影丝] : 鬼缚丝动作中可预输入， 落地时施放[收刀术]； 学习[追魂丝]后， 突进后也可以施放[收刀术]\n
        可以强制中断命中后僵直并施放[鬼缚钉]\n
        - 连接施放时， 可以通过按方向键转身施放 (包括[薄暮利刃]、 [绚烂之舞])
        """
        ...

# 悬丝风暴
# swordman_female/spectre/02ac8e048f7bbcfa616e74ac68988872
# 1645c45aabb008c98406b3a16447040d/02ac8e048f7bbcfa616e74ac68988872
class Skill37(ActiveSkill):
    """
        快速突进， 将缠着鬼缚丝的白牙插入敌人身体。 然后， 踩着敌人进行跳跃， 将鬼缚丝的张力拉到极限后旋转鬼缚丝， 对目标发动大回旋斩击。 \n
        大回旋斩击的余波吸附四散的空气， 引发剧烈剑气风暴， 风暴命中时对敌人造成多段伤害， 并将敌人吸附到前方。 
    """
    name = "悬丝风暴"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 5
    cd = 50
    mp = [800, 1700]
    uuid = "02ac8e048f7bbcfa616e74ac68988872"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 白牙突进攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 跳跃攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 大回旋斩击攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 剑气风暴攻击次数上限 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 剑气风暴每段攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 14
    # [范围信息]
    # 剑气风暴攻击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [悬丝风暴]\n
        可以在空中施放\n
        删除突进攻击， 变更为向前方范围内最强的敌人投掷附着鬼缚丝的白牙
        """
        ...

    def vp_2(self):
        """
        [悬丝风暴]\n
        踩踏敌人后跃起， 对周围发动乱斩， 引发剑气风暴\n
        - 预输入[收刀术]发动时， 在乱斩之前收刀\n
        - 删除跳跃攻击、 大回旋斩击\n
        - 剑气风暴大小 +50%\n
        - 剑气风暴多段攻击次数 +10次\n
        - 总攻击力相同\n
        白牙突进距离增加
        """
        ...

# 黑曜真刃·破晓
# swordman_female/spectre/ca2536eb56df0e812c88c59cabd38be0
# 1645c45aabb008c98406b3a16447040d/ca2536eb56df0e812c88c59cabd38be0
class Skill38(ActiveSkill):
    """
    [收刀术系列]\n
        周围一定范围内存在敌人时， 可以施放该技能。\n
        增幅鬼缚珠的魔力， 将其注入黑曜。\n
    鬼缚珠因魔力增幅而开始发红光， 随后， 夜皇移动到最强敌人的后方， 拔出黑曜发动斩击。 \n
    拔刀的瞬间， 喷涌出耀眼的闪光， 展开蕴含必杀威力的3次剑击。\n
        光芒逐渐减弱后， 夜皇收刀的瞬间， 对范围内的敌人造成多段伤害。
    """
    name = "黑曜真刃·破晓"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "ca2536eb56df0e812c88c59cabd38be0"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 锁定敌人范围 (半径) : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 黑曜拔刀攻击次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 黑曜每段攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 3

# 夜色敌意
# swordman_female/spectre/7f9ffcd296361f1367b8b74e773d5e99
# 1645c45aabb008c98406b3a16447040d/7f9ffcd296361f1367b8b74e773d5e99
class Skill39(PassiveSkill):
    """
        将鬼缚珠的魔力增幅至极限， 对身体进行强化。\n
        突破鬼缚珠魔力极限时， 鬼缚珠散发红光。\n
        并且增加基本攻击力和转职技能攻击力， 变更部分技能效果。\n
    [疾刃之影]\n
        命中敌人后， 可以强制中断并连接转职技能。\n
    [黑夜之花]\n
        长按技能键， 准备姿势时进入无敌状态。 
    """
    name = "夜色敌意"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 3
    uuid = "7f9ffcd296361f1367b8b74e773d5e99"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # [黑夜之花]无敌持续时间上限 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和转职技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [
        {"type":"*skillDamage","data":data1},
    ]

# 绚烂之舞
# swordman_female/spectre/c1dd8b776fb1dd24c6373c678ef1dd2e
# 1645c45aabb008c98406b3a16447040d/c1dd8b776fb1dd24c6373c678ef1dd2e
class Skill40(ActiveSkill):
    """
        挥动黑曜和白牙收纳状态下的金刚， 用剑鞘攻击周围敌人， 然后发动连续斩击。\n
        在留有攻击余波的状态下突进， 对敌人造成强力伤害， 同时摆好拔刀的姿势， 返回并拔出黑曜， 发动终结攻击。\n
        除[回旋十字刃]和觉醒技能之外的转职技能命中敌人时， 可以强制中断并立即施放该技能。
    """
    name = "绚烂之舞"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [960, 7200]
    uuid = "c1dd8b776fb1dd24c6373c678ef1dd2e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 剑鞘攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 连续斩击次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 连续斩击每段攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 10
    # 突进攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 黑曜拔刀终结攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1

# 秘术·雨夜终曲
# swordman_female/spectre/481348575c1e141925c836b59c5db3ca
# 1645c45aabb008c98406b3a16447040d/481348575c1e141925c836b59c5db3ca
class Skill41(ActiveSkill):
    """
        融入雨夜的黑暗之中， 散发杀气压制敌人。\n
        向压制的敌人中最强大的敌人头顶发射白牙， 然后向对象加速冲刺， 发动黑曜拔刀斩击。\n
        拔刀后， 将黑曜收回剑鞘， 落地的同时， 将鬼缚珠的所有魔力转移至黑曜。 黑曜的刀刃完全染成血色的瞬间， 冲向目标敌人， 发动终结一切的无情斩击。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。\n
        选择[黑曜真刃·破晓]时， 可以通过[收刀术]施放[秘术·雨夜终曲]。
    """
    name = "秘术·雨夜终曲"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4027, 8055]
    uuid = "481348575c1e141925c836b59c5db3ca"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 白牙发射攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 黑曜空中拔刀攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 黑曜终结斩击攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

    mode = ['白牙','非白牙']

    def setMode(self, mode):
        if mode == '非白牙':
            self.hit0 = 0

class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'spectre'
        self.nameCN = '极诣·刃影'
        self.role = 'swordman_female'
        self.角色 = '鬼剑士(女)'
        self.职业 = '刃影'
        self.jobId = '1645c45aabb008c98406b3a16447040d'
        self.jobGrowId = '92da05ec93fb43406e193ffb9a2a629b'

        self.武器选项 = ['巨剑', '钝器', '太刀', '短剑']
        self.输出类型选项 = ['物理固伤']
        self.输出类型 = '物理固伤'
        self.防具精通属性 = ['力量']
        self.防具类型 = '皮甲'
        self.buff = 2.083

        super().__init__(equVersion, __name__)
