#41f1cdc2ff58bb5fdc287be0db2a8df3
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "swordman_male/ghostblade/cn/skillDetail"

# 鬼人化
# swordman_male/ghostblade/c39c703f72d289fcd5a8f182068140d4
# 41f1cdc2ff58bb5fdc287be0db2a8df3/c39c703f72d289fcd5a8f182068140d4
class Skill5(PassiveSkill):
    """
    与幻鬼之魂融合、 承载幻鬼灵魂的剑影将使用与一般鬼剑士不同的特殊剑术。\n
    剑影的基本攻击和前冲攻击变更， 前冲攻击后可以立即施放技能。\n
    [鬼斩]、 [三段刃]变更为剑影特殊形态， [后跳]中可以发动空中斩击。
    """
    name = "鬼人化"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 3
    uuid = "c39c703f72d289fcd5a8f182068140d4"
    hasVP = False
    hasUP = False

    # [后跳]空中斩击冷却时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)

# 鬼连击
# swordman_male/ghostblade/8c10cefa65364880451e389bb74d3600
# 41f1cdc2ff58bb5fdc287be0db2a8df3/8c10cefa65364880451e389bb74d3600
class Skill18(ActiveSkill):
    """
    连续斩击前方敌人3次， 造成物理伤害。\n
     在[鬼步]准备姿势下按技能键， 可以发动特殊功能。\n
    - [特殊功能] -\n
     [鬼步]的终结动作变更为[鬼连击]终结动作， 并对命中的所有敌人额外适用[鬼连击]的攻击力。
    """
    name = "鬼连击"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 5
    mp = [20, 210]
    uuid = "8c10cefa65364880451e389bb74d3600"
    hasVP = False
    hasUP = True

    # 第一次斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 第二次斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 第三次斩击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 连续斩击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [鬼连击 : 极]的交叉斩击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

# 鬼步
# swordman_male/ghostblade/38805520deffc10fac2e8f881ab7682b
# 41f1cdc2ff58bb5fdc287be0db2a8df3/38805520deffc10fac2e8f881ab7682b
class Skill19(ActiveSkill):
    """
    施放时摆出准备姿势， 再次按<Z>、 <X>或技能键时， 以肉眼无法追踪的速度快速向前方移动， 攻击路径上的敌人。\n
    剑影现身时对移动路径上的敌人造成多段物理伤害。\n
    准备姿势下， 可发动剑术技能相关的特殊功能。\n
    [特殊功能]\n
    准备姿势下， 剑术技能的图标颜色改变， 按剑术技能键时， 鬼步的终结动作将会变更， 并对鬼步命中的所有敌人额外适用该剑术技能的攻击力。\n
    - 剑术技能 : [鬼连击]、 [鬼连牙]、 [魂破斩]、 [冥灵断魂斩]、 [裂魂乱舞]\n
    在准备姿势下， 若一定时间内不按键， 则自动发动攻击。 按<C>键可以取消准备姿势。\n
     在决斗场中， 连接施放剑术技能时， 减少技能攻击力。
    """
    name = "鬼步"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 6
    mp = [20, 210]
    uuid = "38805520deffc10fac2e8f881ab7682b"
    hasVP = False
    hasUP = True

    # 多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 3
    # 多段攻击次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 连接剑术技能时攻击力合并计算比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)


# 幻鬼 : 一闪
# swordman_male/ghostblade/66a9967e677651d0def34c475795ccde
# 41f1cdc2ff58bb5fdc287be0db2a8df3/66a9967e677651d0def34c475795ccde
class Skill21(ActiveSkill):
    """
    幻鬼快速向前方突进， 攻击路径上的敌人。\n
    施放剑术技能过程中使用该技能时， 可以无施放动作立即出现幻鬼攻击敌人。\n
    在决斗场中， 无法在[格挡]过程中使用。
    """
    name = "幻鬼 : 一闪"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 6
    mp = [32, 336]
    uuid = "66a9967e677651d0def34c475795ccde"
    hasVP = False
    hasUP = True

    # 一闪攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # [范围信息]
    # 幻鬼突进距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 幻鬼步
# swordman_male/ghostblade/b69d38bcddd41b3566c6d5cf78d060bb
# 41f1cdc2ff58bb5fdc287be0db2a8df3/b69d38bcddd41b3566c6d5cf78d060bb
class Skill22(ActiveSkill):
    """
    剑影专属步法。 在幻鬼分离状态下使用该技能， 剑影可以快速移动到幻鬼身边。\n
    移动过程中剑影处于无敌状态， 到达后也在一定时间内适用无敌判定。\n
    每使用1次幻鬼分离技能， 只能使用一次该技能。\n
    在决斗场中存在冷却时间， 且移动后不适用无敌判定。
    """
    name = "幻鬼步"
    learnLv = 20
    masterLv = 1
    maxLv = 1
    position = 2
    rangeLv = 1
    mp = [336, 336]
    uuid = "b69d38bcddd41b3566c6d5cf78d060bb"
    hasVP = False
    hasUP = False

    # 无敌时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)

# 剑影太刀精通
# swordman_male/ghostblade/030663e99462f628b4c9f813e1406c4e
# 41f1cdc2ff58bb5fdc287be0db2a8df3/030663e99462f628b4c9f813e1406c4e
class Skill23(PassiveSkill):
    """
    增加剑影的物理攻击力， 使用太刀系武器时， 增加命中率。\n
    同时， 太刀武器的物理攻击力 (包含强化、 增幅所增加的数值) 提升至与魔法攻击力相同。
    """
    name = "剑影太刀精通"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 1
    rangeLv = 3
    uuid = "030663e99462f628b4c9f813e1406c4e"
    hasVP = False
    hasUP = False

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 命中率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    associate = [{"data":data0}]

# 幻鬼 : 连击
# swordman_male/ghostblade/150aa05b9ee8b9c7c04a25f3e425900c
# 41f1cdc2ff58bb5fdc287be0db2a8df3/150aa05b9ee8b9c7c04a25f3e425900c
class Skill25(ActiveSkill):
    """
    幻鬼快速连续斩击前方敌人， 造成物理伤害。\n
    施放剑术技能过程中使用该技能时， 可以无施放动作立即出现幻鬼攻击敌人。\n
    在决斗场中， 无法在[格挡]过程中使用。
    """
    name = "幻鬼 : 连击"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 8
    mp = [60, 600]
    uuid = "150aa05b9ee8b9c7c04a25f3e425900c"
    hasVP = False
    hasUP = True

    # 第一次斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 第二次斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 第三次斩击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 第四次斩击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # [范围信息]
    # 连续斩击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

# 鬼连牙
# swordman_male/ghostblade/89c505581267af77c6d58dc49b710550
# 41f1cdc2ff58bb5fdc287be0db2a8df3/89c505581267af77c6d58dc49b710550
class Skill26(ActiveSkill):
    """
    将灵魂之力聚集到剑上， 然后强力刺击敌人。\n
     被击中的敌人进入僵直状态， 并被拉到剑影前方。\n
     可以推开霸体状态的敌人， 攻击倒地或浮空的敌人时， 强制将敌人拉到面前。\n
     在[鬼步]准备姿势下按技能键， 发动特殊功能。\n
    [特殊功能]\n
     [鬼步]的终结动作变更为[鬼连牙]终结动作， 将所有命中的敌人拉到前方并额外适用[鬼连牙]的攻击力。\n
    在决斗场中， 无法拉起浮空或倒地的敌人。
    """
    name = "鬼连牙"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 8
    mp = [46, 483]
    uuid = "89c505581267af77c6d58dc49b710550"
    hasVP = False
    hasUP = True

    # 刺击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1

# 幻鬼之力
# swordman_male/ghostblade/a81e5b7defa1819263ed8e86f69fd06f
# 41f1cdc2ff58bb5fdc287be0db2a8df3/a81e5b7defa1819263ed8e86f69fd06f
class Skill27(PassiveSkill):
    """
    学习后， 增加剑影的攻击速度、 移动速度、 物理暴击率和暴击伤害。\n
    [青蓝色的血肉上， 似乎已经浸染幻鬼的气息。]
    """
    name = "幻鬼之力"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 0
    rangeLv = 3
    uuid = "a81e5b7defa1819263ed8e86f69fd06f"
    hasVP = False
    hasUP = False

    # 攻击速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 移动速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 物理暴击率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 暴击伤害增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    associate = [{"data":data3}]

# 双魂共鸣
# swordman_male/ghostblade/89a4529234904fcbb3abe289e281f2fd
# 41f1cdc2ff58bb5fdc287be0db2a8df3/89a4529234904fcbb3abe289e281f2fd
class Skill28(ActiveSkill):
    """
    施放时， 两个灵魂在剑影身体里产生共鸣， 强化身体。\n
    增加剑影的基本攻击力、 [鬼斩]、 [三段刃]和转职后技能的攻击力。\n
    [别忘了， 你与我是一体……]
    """
    name = "双魂共鸣"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    cd = 5
    uuid = "89a4529234904fcbb3abe289e281f2fd"
    hasVP = False
    hasUP = False

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 基本攻击和技能攻击增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 共鸣 : 离魂一闪
# swordman_male/ghostblade/515b442ffbf61a82371abb645c149a31
# 41f1cdc2ff58bb5fdc287be0db2a8df3/515b442ffbf61a82371abb645c149a31
class Skill29(ActiveSkill):
    """
    幻鬼快速向前方突进斩击敌人， 然后与剑影交叉斩击直线上的敌人， 造成物理伤害。\n
    在剑影与幻鬼分离的状态下施放[共鸣 : 离魂一闪]时， 幻鬼中断当前的动作并立即发动交叉斩击， 此时突进斩击的攻击力与交叉共鸣合并计算。\n
    在决斗场中， 施放时不适用霸体， 在分离状态下使用时攻击力减少。
    """
    name = "共鸣 : 离魂一闪"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cd = 12
    mp = [61, 640]
    uuid = "515b442ffbf61a82371abb645c149a31"
    hasVP = False
    hasUP = True

    # 突进斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 交叉共鸣攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # [范围信息]
    # 幻鬼突进距离 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 鬼连击 : 极
# swordman_male/ghostblade/ebff277c02cc8b54c32635cd0d25f6f3
# 41f1cdc2ff58bb5fdc287be0db2a8df3/ebff277c02cc8b54c32635cd0d25f6f3
class Skill30(ActiveSkill):
    """
    学习后， 鬼连击的最后一击后追加一次交叉斩击。\n
    [鬼连击 : 极]的技能等级与[鬼连击]的技能等级同时提升， 攻击范围同时受[鬼连击]范围的影响。
    """
    name = "鬼连击 : 极"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    type = "passive"
    uuid = "ebff277c02cc8b54c32635cd0d25f6f3"
    hasVP = False
    hasUP = False
    # 交叉斩击攻击力 : {value0}% x 3
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 3

    def getSkillCD(self,mode=None):
      return self.char.GetSkillByName("鬼连击").getSkillCD(mode)

# 魂破斩
# swordman_male/ghostblade/87a918bb22cfc959a16e0bf939bb6c24
# 41f1cdc2ff58bb5fdc287be0db2a8df3/87a918bb22cfc959a16e0bf939bb6c24
class Skill31(ActiveSkill):
    """
     聚集魂魄的力量下劈前方敌人， 造成巨大物理伤害。\n
     在[鬼步]准备姿势下按技能键， 发动特殊功能。\n
    - [特殊功能] -\n
     [鬼步]的终结动作变更为[魂破斩]终结动作， 并对命中的所有敌人额外适用[魂破斩]的攻击力。
    """
    name = "魂破斩"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 1
    cd = 12
    mp = [129, 1083]
    uuid = "87a918bb22cfc959a16e0bf939bb6c24"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 下劈攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # [范围信息]
    # 下斩范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    def vp_1(self):
        """
        [魂破斩]\n
        攻击范围 +25%\n
        [鬼步]和剑术技能攻击后可以强制中断\n
        攻击后可以强制中断并立即施放[鬼步]和剑术技能
        """
        ...

    def vp_2(self):
        """
        [魂破斩]\n
        与[鬼步]连接施放时， 初始化[鬼步]冷却时间\n
        与[鬼步]连接施放时， Y轴攻击范围 +20%\n
        [鬼步]攻击力 -25%
        """
        ...

    def effect(self, old, new):
        if self.vp == 2:
            self.associate = [{"type":"*skillRation","data":[0] + [-25]*self.maxLv,"skills":["鬼步"]}]
        return super().effect(old, new)

# 共鸣 : 鬼灵斩
# swordman_male/ghostblade/aa51c4ddf1659092fa9ed612b9837061
# 41f1cdc2ff58bb5fdc287be0db2a8df3/aa51c4ddf1659092fa9ed612b9837061
class Skill32(ActiveSkill):
    """
    与幻鬼一起挥剑， 对大范围内的敌人造成巨大物理伤害。\n
    在剑影与幻鬼分离的状态下施放[共鸣 : 鬼灵斩]时，  幻鬼中断当前的动作并在原地立即施放鬼灵斩。\n
    在决斗场中， 施放时不适用霸体， 在分离状态下使用时攻击力减少， 且无法攻击倒地的敌人。
    """
    name = "共鸣 : 鬼灵斩"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [129, 1083]
    uuid = "aa51c4ddf1659092fa9ed612b9837061"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 鬼灵斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # [范围信息]
    # 鬼灵斩范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    def vp_1(self):
        """
        [共鸣 : 鬼灵斩]\n
        变更为剑术系列技能\n
        施放时不会出现幻鬼\n
        可以强制中断[鬼步]和剑术技能的施放后僵直， 并施放[共鸣 : 鬼灵斩]\n
        可以强制中断[共鸣 : 鬼灵斩]的施放后僵直， 并施放[鬼步]和剑术技能
        """
        ...

    def vp_2(self):
        """
        [共鸣 : 鬼灵斩]\n
        变更为幻鬼系列技能\n
        施放时幻鬼出现， 斩击并击退敌人\n
        攻击范围 +30%
        """
        ...

# 幻鬼 : 回天
# swordman_male/ghostblade/863295a0fc634cf5fcc01e82a735fd6b
# 41f1cdc2ff58bb5fdc287be0db2a8df3/863295a0fc634cf5fcc01e82a735fd6b
class Skill33(ActiveSkill):
    """
    幻鬼发动回旋斩击， 对周围敌人造成巨大物理伤害。\n
    施放剑术技能过程中使用该技能时， 可以无施放动作立即出现幻鬼攻击敌人。\n
    在决斗场中， 无法在[格挡]过程中使用。
    """
    name = "幻鬼 : 回天"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [170, 1428]
    uuid = "863295a0fc634cf5fcc01e82a735fd6b"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 回旋斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 终结斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    def vp_1(self):
        """
        [幻鬼 : 回天]\n
        幻鬼出现在前方并进行旋转攻击， 生成黑色风暴\n
        黑色风暴会对敌人造成多段伤害并吸附至风暴中心\n
        - 旋转斩击、 终结斩击攻击力 -75%\n
        - 黑色风暴多段攻击次数 : 20次\n
        - 总攻击力相同\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 10秒\n
        - 单次攻击力 -50%
        """
        self.cd = 10
        self.skillRation *= 0.5
        ...

    def vp_2(self):
        """
        [幻鬼 : 回天]\n
        幻鬼出现后， 向前方挥剑发射巨大的剑气\n
        - 总攻击力相同
        """
        ...

# 冥灵断魂斩
# swordman_male/ghostblade/3153ca0e6752a6283412c59c5ec8e002
# 41f1cdc2ff58bb5fdc287be0db2a8df3/3153ca0e6752a6283412c59c5ec8e002
class Skill34(ActiveSkill):
    """
     将灵魂的力量聚集于灵魂刀中， 将身边的敌人向后推并大幅度挥剑， 造成巨大物理伤害。\n
     在[鬼步]准备姿势下按技能键， 发动特殊功能。\n
    - [特殊功能] -\n
     [鬼步]的终结动作变更为[冥灵断魂斩]终结动作， 并对命中的所有敌人额外适用[冥灵断魂斩]的攻击力。
    """
    name = "冥灵断魂斩"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [299, 2511]
    uuid = "3153ca0e6752a6283412c59c5ec8e002"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 断魂斩攻击力 : {value0}%%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # [范围信息]
    # 断魂斩攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    def vp_1(self):
        """
        [冥灵断魂斩]\n
        斩击前僵直 -40%\n
        可以强制中断[鬼步]和剑术技能的施放后僵直， 并施放[冥灵断魂斩]\n
        可以强制中断[冥灵断魂斩]的施放后僵直， 并施放[鬼步]和剑术技能
        """
        ...

    def vp_2(self):
        """
        [冥灵断魂斩]\n
        与[鬼步]连接施放时， 初始化[鬼步]冷却时间\n
        与[鬼步]连接施放时， Y轴攻击范围 +20%\n
        [鬼步]攻击力 -11%
        """
        ...

    def effect(self, old, new):
        if self.vp == 2:
            self.associate = [{"type":"*skillRation","data":[0] + [-11]*self.maxLv,"skills":["鬼步"]}]
        return super().effect(old, new)

# 鬼夜
# swordman_male/ghostblade/02ac8e048f7bbcfa616e74ac68988872
# 41f1cdc2ff58bb5fdc287be0db2a8df3/02ac8e048f7bbcfa616e74ac68988872
class Skill35(PassiveSkill):
    """
    拥有人类外形的冷酷无情的斗鬼， 人们称之为“夜刀神”。\n
    学习后， 增加夜刀神的基本攻击力、 [鬼斩]、 [三段刃]和转职后技能的攻击力、 物理暴击率。
    """
    name = "鬼夜"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "02ac8e048f7bbcfa616e74ac68988872"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 物理暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    associate = [{"data":data0}]

# 冥夜鬼天杀
# swordman_male/ghostblade/ca2536eb56df0e812c88c59cabd38be0
# 41f1cdc2ff58bb5fdc287be0db2a8df3/ca2536eb56df0e812c88c59cabd38be0
class Skill36(ActiveSkill):
    """
    夜刀神凝聚灵魂之力， 周围陷入黑暗， 幻鬼在前方出现。\n
    然后， 夜刀神和幻鬼交叉斩击敌人， 造成巨大物理伤害。
    """
    name = "冥夜鬼天杀"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [998, 8383]
    uuid = "ca2536eb56df0e812c88c59cabd38be0"
    hasVP = False
    hasUP = False

    # 交叉斩击攻击力 : {value0}% x 4
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 4

# 幻鬼 : 奈落
# swordman_male/ghostblade/7f9ffcd296361f1367b8b74e773d5e99
# 41f1cdc2ff58bb5fdc287be0db2a8df3/7f9ffcd296361f1367b8b74e773d5e99
class Skill37(ActiveSkill):
    """
    幻鬼从一定范围内最强的敌人上方下劈。\n
    施放剑术技能过程中使用该技能时， 可以无施放动作立即出现幻鬼攻击敌人。
    """
    name = "幻鬼 : 奈落"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 2
    cube = 2
    cd = 20
    mp = [334, 935]
    uuid = "7f9ffcd296361f1367b8b74e773d5e99"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 下劈攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # [范围信息]
    # 锁定敌人范围 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    def vp_1(self):
        """
        [幻鬼 : 奈落]\n
        使被幻鬼直接击中的敌人进入强制控制状态， 效果持续3秒\n
        - 基本冷却时间变更为10秒\n
        - 总攻击力 -50%
        """
        self.cd = 10
        self.skillRation *= 0.5
        ...

    def vp_2(self):
        """
        [幻鬼 : 奈落]\n
        识别敌人范围 +50%\n
        下劈冲击波范围 +30%\n
        - 基本冷却时间变更为40秒\n
        总攻击力 +100%
        """
        self.cd = 40
        self.skillRation *= 2.0
        ...

# 共鸣 : 聚渊
# swordman_male/ghostblade/c1dd8b776fb1dd24c6373c678ef1dd2e
# 41f1cdc2ff58bb5fdc287be0db2a8df3/c1dd8b776fb1dd24c6373c678ef1dd2e
class Skill38(ActiveSkill):
    """
    幻鬼向前方移动， 攻击敌人后用封印符强制控制敌人。\n
    随后， 夜刀神扔出灵魂刀， 吸收鬼气并将敌人聚到一起， 与幻鬼一起发动强力斩击， 造成巨大物理伤害。\n
    在夜刀神与幻鬼分离的状态下施放[共鸣 : 聚渊]时， 幻鬼中断当前动作并向夜刀神方向移动并攻击敌人。
    """
    name = "共鸣 : 聚渊"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 8
    rangeLv = 2
    cube = 3
    cd = 50
    mp = [686, 1440]
    uuid = "c1dd8b776fb1dd24c6373c678ef1dd2e"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 幻鬼移动斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 幻鬼终结攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 夜刀神终结攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 夜刀神终结下斩范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [共鸣 : 聚渊]\n
        施放技能时进入无敌状态\n
        灵魂刀吸收范围 +30%\n
        夜刀神、 幻鬼终结攻击范围 +30%\n
        终结攻击后夜刀神和幻鬼发动追加斩击\n
        - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [共鸣 : 聚渊]\n
        夜刀神和幻鬼摆出准备姿势后向前方快速移动， 对敌人发动一闪\n
        合算幻鬼移动斩击、 夜刀神终结攻击、 幻鬼终结攻击攻击力\n
        - 总攻击力相同
        """
        ...

# 鬼咲
# swordman_male/ghostblade/481348575c1e141925c836b59c5db3ca
# 41f1cdc2ff58bb5fdc287be0db2a8df3/481348575c1e141925c836b59c5db3ca
class Skill39(PassiveSkill):
    """
    夜见罗刹以压倒性的力量压制无数敌人和鬼神。\n
    学习后， 增加夜见罗刹的基本攻击力、 [鬼斩]、 [三段刃]和转职后技能的攻击力， 强化移动技能， 并增强与幻鬼的灵魂共鸣， 随心所欲地使用幻鬼技能。\n
    - [移动技能强化] -\n
    三段刃 : 冷却时间 -1秒\n
    鬼步 : 冷却时间 -1秒； Y轴攻击范围增加\n
    - [幻鬼技能强化] -\n
    基本攻击、 前冲攻击中，可以无施放动作立即连接幻鬼技能。 \n
    站立状态下， 被攻击时可以使用幻鬼技能和[幻鬼步]。 \n
    [戴上面具， 化身罗刹。]
    """
    name = "鬼咲"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "481348575c1e141925c836b59c5db3ca"
    hasVP = False
    hasUP = False

    # 基本攻击和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [三段刃]、 [鬼步]冷却时间减少量 : 1秒
    # [鬼步]Y轴攻击范围增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    associate = [
        {"type":"*skillRation","data":data0},
        {"type":"+cd","data":[0] + [-1]*maxLv,"skills":["鬼步"],"ratio":1},
    ]

# 幻鬼 : 大回天
# swordman_male/ghostblade/5f4c55fe2ebdf0623bd76d4fda872ddc
# 41f1cdc2ff58bb5fdc287be0db2a8df3/5f4c55fe2ebdf0623bd76d4fda872ddc
class Skill40(ActiveSkill):
    """
    幻鬼快速向前方旋转突进， 斩击周围敌人， 造成多段物理伤害； 并且将击中的敌人聚集到X轴上。\n
    施放剑术技能过程中使用该技能时， 可以无施放动作立即出现幻鬼攻击敌人。
    """
    name = "幻鬼 : 大回天"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [568, 4402]
    uuid = "5f4c55fe2ebdf0623bd76d4fda872ddc"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 旋转斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 3
    # 旋转斩击多段攻击次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # 回旋斩范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    def vp_1(self):
        """
        [幻鬼 : 大回天]\n
        幻鬼出现在对面， 向剑影方向发起攻击并吸附敌人\n
        可以吸附霸体状态的敌人\n
        攻击范围 +30%\n
        幻鬼攻击速度 +50%
        """
        ...

    def vp_2(self):
        """
        [幻鬼 : 大回天]\n
        变更为无法普通施放的技能， 剑术技能攻击时生成黑影闪， 对敌人追加多段攻击伤害\n
        - 总攻击力相同\n
        适用多段伤害时， 15秒内剑影的攻击速度 +5% (最多叠加3次)\n
        变更为可填充4次的技能\n
        - 每次填充冷却时间 : 10秒\n
        - 单次攻击力 -75%
        """
        self.cd = 10
        self.skillRation *= 0.25
        ...

# 裂魂乱舞
# swordman_male/ghostblade/95b58ec89893dd9e50da1281ebe57175
# 41f1cdc2ff58bb5fdc287be0db2a8df3/95b58ec89893dd9e50da1281ebe57175
class Skill41(ActiveSkill):
    """
     连续斩击前方敌人， 然后旋转融合的灵魂刀， 对范围内的敌人造成巨大物理伤害。\n
     在[鬼步]准备姿势下按技能键， 发动特殊功能。\n
    - [特殊功能] -\n
     [鬼步]的终结动作变更为[裂魂乱舞]终结动作， 并对命中的所有敌人额外适用[裂魂乱舞]的攻击力。
    """
    name = "裂魂乱舞"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [823, 6172]
    uuid = "95b58ec89893dd9e50da1281ebe57175"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 第一次斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 第二次斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 第三次斩击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 旋转斩击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 2
    # 终结斩击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1
    # [范围信息]
    # 连舞攻击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)

    def vp_1(self):
        """
        [裂魂乱舞]\n
        删除旋转攻击、 最后一击\n
        第1、 2、 3次斩击动作变更\n
        可以分别施放每次斩击\n
        - 总攻击力相同\n
        - 斩击攻击间可输入时间 : 10秒\n
        可以强制中断剑术技能施放后僵直， 并施放该技能\n
        可以强制中断施放后僵直， 并施放剑术技能\n
        连接施放剑术技能时， 该剑术技能施放速度 +30%
        """
        ...

    def vp_2(self):
        """
        [裂魂乱舞]\n
        删除第1、 2、 3次斩击攻击\n
        - 旋转斩击攻击力 +60%\n
        - 终结斩击攻击力 +72%\n
        - 总攻击力相同\n
        增加旋转攻击时的移动距离\n
        攻击范围 +35%
        """
        ...

# 鬼隐 · 夜奈落
# swordman_male/ghostblade/573723c8c0614f5b1218ca9ff992115b
# 41f1cdc2ff58bb5fdc287be0db2a8df3/573723c8c0614f5b1218ca9ff992115b
class Skill42(ActiveSkill):
    """
    施放时， 夜见罗刹和幻鬼爆发鬼气， 让世界笼罩在黑暗之中。 \n
    然后， 幻鬼从一定范围内最强的敌人上方下劈， 造成巨大物理伤害， 并与夜见罗刹一起连续斩击敌人。\n
    夜见罗刹与幻鬼攻击时可以强制控制敌人， 发动终结攻击时解除控制。\n
    在夜见罗刹和幻鬼分离的状态下施放时， 增加索敌范围。\n
    [永堕黑暗吧！]
    """
    name = "鬼隐 · 夜奈落"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2329, 4658]
    uuid = "573723c8c0614f5b1218ca9ff992115b"
    hasVP = False
    hasUP = False

    # 索敌范围 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 第一次下劈攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 第二次横斩攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 第三次横斩攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # 终结交叉斩击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1

# 睥睨万物
# swordman_male/ghostblade/38c485cc41f46a7959ae4336325aa45c
# 41f1cdc2ff58bb5fdc287be0db2a8df3/38c485cc41f46a7959ae4336325aa45c
class Skill43(PassiveSkill):
    """
    极诣·剑影达到睥睨万物、 战无不胜的境界。\n
    增加[鬼斩]、 [三段刃]、 基本攻击力和除[幻鬼 : 连击]之外的转职技能攻击力， 部分技能附加特殊效果。\n
    [幻鬼步] : 空中、 倒地状态下被攻击时可施放 (适用独立冷却时间)\n
    [幻鬼 : 连击] : 增加空中范围、 斩击速度， 追加终结斩击\n
    [我们即是万物的梦魇。]
    """
    name = "睥睨万物"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "38c485cc41f46a7959ae4336325aa45c"
    hasVP = False
    hasUP = False

    # [鬼斩]、 [三段刃]、 基本攻击力和除[幻鬼 : 连击]之外的转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [幻鬼 : 连击]
    # 追加斩击攻击力 : 总攻击力的 {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 攻击范围增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 斩击速度增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [幻鬼步]
    # 空中、 倒地状态下被攻击时施放冷却时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    associate = [{"data":data0}]

# 无式·极影剑
# swordman_male/ghostblade/7a3fc9d473e8ffe21dd900ddf228a437
# 41f1cdc2ff58bb5fdc287be0db2a8df3/7a3fc9d473e8ffe21dd900ddf228a437
class Skill44(ActiveSkill):
    """
    极诣·剑影的新剑术。\n
    根据不同的使用方法， 施展不同系列的剑术攻击敌人。\n
    普通施放\n
    [共鸣系列]\n
    剑影和幻鬼快速连续斩击前方敌人。\n
    基本攻击和使用剑术技能时施放\n
    [幻鬼系列]\n
    幻鬼出现， 快速连续斩击前方敌人。\n
    [鬼步]姿势下施放\n
    [剑术系列]\n
    [鬼步]的终结动作变更为[无式·极影剑]的终结动作， 并对命中的所有敌人额外适用[无式·极影剑]的攻击力。\n
    [牵绊是一种无用的情感。]
    """
    name = "无式·极影剑"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [1097, 8229]
    uuid = "7a3fc9d473e8ffe21dd900ddf228a437"
    hasVP = False
    hasUP = False

    # [共鸣系列]
    # 剑影鬼连续斩击攻击力 : {value0}% x 5
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 5
    # 幻鬼连续斩击攻击力 : {value1}% x 5
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 5
    # 剑影终结斩击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 幻鬼终结斩击 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # [幻鬼系列]
    # 幻鬼连续斩击攻击力 : {value4}% x 5
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 0
    # 幻鬼终结斩击攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    hit5 = 0

    mode = ["共鸣", "幻鬼"]

    def setMode(self, mode):
        if mode == '幻鬼':
            self.hit0 = self.hit1 = self.hit2 = self.hit3 = 0
            self.hit4 = 5
            self.hit5 = 1
        if mode == '共鸣':
            self.hit0 = self.hit1 = 5
            self.hit2 = self.hit3 = 1
            self.hit4 = 0
            self.hit5 = 0

# 灭魂极影剑·止煞
# swordman_male/ghostblade/6166762c62f234c5f50c2d2ebc5e48d0
# 41f1cdc2ff58bb5fdc287be0db2a8df3/6166762c62f234c5f50c2d2ebc5e48d0
class Skill45(ActiveSkill):
    """
    开启灵魂的世界， 剑影与幻鬼以极快的速度移动， 互相比剑。\n
    剑影和幻鬼使刀剑横扫的敌人受到多段伤害， 然后双方交汇斩裂灵魂世界和敌人。\n
    [呵呵呵……我与你总是如此相似。]\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    关联的技能在冷却中时， 无法使用三次觉醒技能。
    """
    name = "灭魂极影剑·止煞"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [3752, 7505]
    uuid = "6166762c62f234c5f50c2d2ebc5e48d0"
    hasVP = False
    hasUP = False

    # 最初碰撞攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 剑影连续斩击攻击力 : {value1}% x 7
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 7
    # 幻鬼横斩攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 剑影、 幻鬼连续斩击攻击力 : {value3}% x 7
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 7
    # 终结攻击碰撞攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1
    # 终结剑击攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    hit5 = 1
    # 终结爆炸攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    hit6 = 1


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'ghostblade'
        self.nameCN = '极诣·剑影'
        self.role = 'swordman_male'
        self.角色 = '鬼剑士(男)'
        self.职业 = '剑影'
        self.jobId = '41f1cdc2ff58bb5fdc287be0db2a8df3'
        self.jobGrowId = '3ff5b661925ac59d1ca290b05ca914cc'

        self.武器选项 = ['太刀', '钝器', '巨剑', '短剑']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '皮甲'
        self.buff = 2.083

        super().__init__(equVersion, __name__)
