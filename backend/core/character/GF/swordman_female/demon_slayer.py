#1645c45aabb008c98406b3a16447040d
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "swordman_female/demon_slayer/cn/skillDetail"


# 唤魔 : 蛇腹剑
# swordman_female/demon_slayer/3829c15bf5f520c13998a3479ba0ce7b
# 1645c45aabb008c98406b3a16447040d/3829c15bf5f520c13998a3479ba0ce7b
class Skill17(PassiveSkill):
    """
        召唤魔王塔莫斯的专属剑。\n
        进入地下城时， 武器更换为蛇腹剑， 增加命中率和硬直。\n
        增加基本攻击力和转职系技能攻击力； 攻击时， 使敌人进入出血异常状态。
    """
    name = "唤魔 : 蛇腹剑"
    learnLv = 15
    masterLv = 1
    maxLv = 11
    position = 6
    rangeLv = 3
    uuid = "3829c15bf5f520c13998a3479ba0ce7b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 命中率增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 硬直增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 基本攻击力和转职系列技能攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [出血效果]
    # 出血攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 出血几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 出血持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)

    associate = [
        {"data":data2,"type":"*skillDamage"}
    ]

# 蛇腹剑 : 破
# swordman_female/demon_slayer/dcd536f1674630f01fc9667bb202b851
# 1645c45aabb008c98406b3a16447040d/dcd536f1674630f01fc9667bb202b851
class Skill18(ActiveSkill):
    """
        将剑刺向地面后， 剑刃破地而出。
    """
    name = "蛇腹剑 : 破"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 1
    rangeLv = 2
    cd = 5
    mp = [8, 170]
    uuid = "dcd536f1674630f01fc9667bb202b851"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 破开地面的攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 破开地面的多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 破开地面的大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 唤魔 : 狂暴
# swordman_female/demon_slayer/03bb5314ffd41e9458d67ef924fef38f
# 1645c45aabb008c98406b3a16447040d/03bb5314ffd41e9458d67ef924fef38f
class Skill19(ActiveSkill):
    """
        让魔王塔莫斯的精神支配着契魔者进行战斗。\n
         增加攻击速度、 移动速度、 基本攻击力和技能攻击力。
    """
    name = "唤魔 : 狂暴"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 8
    rangeLv = 3
    cd = 5
    uuid = "03bb5314ffd41e9458d67ef924fef38f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 移动速度增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 蛇腹剑 : 舞
# swordman_female/demon_slayer/04883563896fe1adac7505c6146b5f59
# 1645c45aabb008c98406b3a16447040d/04883563896fe1adac7505c6146b5f59
class Skill20(ActiveSkill):
    """
        向前挥剑三次。\n
        每次挥动时剑会变长。\n
        第1、 2击可以击退敌人， 第3击缠住敌人的腿， 将其拉向契魔者并击倒。
    """
    name = "蛇腹剑 : 舞"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 6
    mp = [15, 300]
    uuid = "04883563896fe1adac7505c6146b5f59"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 挥剑第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 挥剑第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 挥剑第3击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)


# 蛇腹剑 : 缠
# swordman_female/demon_slayer/3d8f3d438405d79f8d3ed68072674d1e
# 1645c45aabb008c98406b3a16447040d/3d8f3d438405d79f8d3ed68072674d1e
class Skill22(ActiveSkill):
    """
        缠绕前方的敌人后撕扯并拉向契魔者。\n
        对无法抓取的敌人不适用控制效果。
    """
    name = "蛇腹剑 : 缠"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 8
    mp = [25, 325]
    uuid = "3d8f3d438405d79f8d3ed68072674d1e"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 缠绕攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    power0 = 1
    # 撕扯攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 3
    power1 = 1
    # 撕扯多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 冲击波范围攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 冲击波范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    data6 = data0
    hit6 = 1
    power6 = 0

    data7 = data1
    hit7 = 3
    power7 = 0

# 蛇腹剑 : 刺
# swordman_female/demon_slayer/1dad88963abdc96b091fcab185a8820d
# 1645c45aabb008c98406b3a16447040d/1dad88963abdc96b091fcab185a8820d
class Skill23(ActiveSkill):
    """
        向前挥剑后收回， 命中时将敌人拉向契魔者。
    """
    name = "蛇腹剑 : 刺"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 8
    mp = [35, 300]
    uuid = "1dad88963abdc96b091fcab185a8820d"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 伸剑攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 收回攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 魔剑控制
# swordman_female/demon_slayer/27bade584bb42fef68148d3a0b72bace
# 1645c45aabb008c98406b3a16447040d/27bade584bb42fef68148d3a0b72bace
class Skill24(PassiveSkill):
    """
        获得控制魔剑普诺的力量， 可以灵活自如地操控魔剑。\n
        增加物理、 魔法攻击力和物理暴击率。
    """
    name = "魔剑控制"
    learnLv = 30
    masterLv = 20
    maxLv = 30
    position = 8
    rangeLv = 3
    uuid = "27bade584bb42fef68148d3a0b72bace"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 物理/魔法攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [
        {"data":data0,"type":"*skillDamage"}
    ]

# 蛇腹剑 : 灭
# swordman_female/demon_slayer/01384bbfc346775d1267fa0bc4ca605f
# 1645c45aabb008c98406b3a16447040d/01384bbfc346775d1267fa0bc4ca605f
class Skill25(ActiveSkill):
    """
        如同鞭子一样快速前后挥剑。\n
        连按攻击键可增加攻击速度。\n
        攻击中按跳跃键可以强制中断技能。
    """
    name = "蛇腹剑 : 灭"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 12
    mp = [40, 300]
    uuid = "01384bbfc346775d1267fa0bc4ca605f"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 挥剑攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 12
    # 挥剑多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 碎魔剑
# swordman_female/demon_slayer/128b9ddef2262f40723deae4407bdb42
# 1645c45aabb008c98406b3a16447040d/128b9ddef2262f40723deae4407bdb42
class Skill26(ActiveSkill):
    """
        剑身分裂成刀刃攻击敌人。\n
        分裂的刀刃沿着一定轨迹移动后重新变回剑。\n
        在决斗场中， 减少攻击范围， 吸附攻击中霸体不生效， 挥剑攻击无法攻击倒地的敌人。
    """
    name = "碎魔剑"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [199, 839]
    uuid = "128b9ddef2262f40723deae4407bdb42"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 克库斯飞出攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 克库斯飞出多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 克库斯返回攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 克库斯返回多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [碎魔剑]\n
        可以强制中断施放后僵直， 并施放蛇腹剑技能 (觉醒技能除外)\n
        可以强制中断蛇腹剑技能施放后僵直， 并施放该技能 (觉醒技能除外)\n
        施放时， 初始化[蛇腹剑 : 破]技能冷却时间\n
        - [蛇腹剑 : 破]攻击力 -20%\n
        蛇腹剑技能列表 (觉醒技能除外)\n
        - [蛇腹剑 : 破]、 [蛇腹剑 : 舞]、 [蛇腹剑 : 缠]、 [蛇腹剑 : 刺]、 [蛇腹剑 : 灭]、 [魔刃狂舞]、 [唤魔 : 塔莫斯之袭]、[汲血魔剑]、 [空绝斩 : 地裂]、 [弑神剑 : 极]、 [蛇舞血轮剑]
        """
        ...

    def vp_2(self):
        """
        [碎魔剑]\n
        塔莫斯现身挥剑， 向最强敌人发动刃风\n
        - 范围内没有敌人时不会生成\n
        - 刃风多段攻击次数 : 20次\n
        - 总攻击力相同\n
        - 施放除觉醒技能外的转职技能时， 可以施放[碎魔剑]\n
        - 删除施放动作
        """
        ...

    def effect(self, old, new):
        if self.vp == 1:
            self.associate = [{"type":"*skillRation","data":[0] + [-11]*self.maxLv,"skills":["蛇腹剑 : 破"]}]
        return super().effect(old, new)

# 魔刃狂舞
# swordman_female/demon_slayer/1fadde0eece18649caddbca7bd58cc2f
# 1645c45aabb008c98406b3a16447040d/1fadde0eece18649caddbca7bd58cc2f
class Skill27(ActiveSkill):
    """
        如同鞭子一样快速向前挥剑。\n
        多段攻击中按跳跃键可以强制中断技能。
    """
    name = "魔刃狂舞"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [100, 920]
    uuid = "1fadde0eece18649caddbca7bd58cc2f"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 挥剑攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 14
    # 挥剑多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    # 幻影部分伤害

    data4 = data0
    power4 = 0
    hit4 = 10

    data5 = data1
    power5 = 0
    hit5 = 1

    def vp_1(self):
        """
        [魔刃狂舞]\n
        多段攻击次数 -7次\n
        - 总攻击力相同\n
        可以强制中断施放后僵直， 并施放蛇腹剑技能 (觉醒技能除外)\n
        可以强制中断蛇腹剑技能施放后僵直， 并施放该技能 (觉醒技能除外)\n
        蛇腹剑技能列表 (觉醒技能除外)\n
        - [蛇腹剑 : 破]、 [蛇腹剑 : 舞]、 [蛇腹剑 : 缠]、 [蛇腹剑 : 刺]、 [蛇腹剑 : 灭]、 [魔刃狂舞]、 [唤魔 : 塔莫斯之袭]、[汲血魔剑]、 [空绝斩 : 地裂]、 [弑神剑 : 极]、 [蛇舞血轮剑]
        """
        ...

    def vp_2(self):
        """
        [魔刃狂舞]\n
        施放时进入无敌状态\n
        攻击范围 +20%
        """
        ...

# 群魔乱舞
# swordman_female/demon_slayer/da6e37c1e3f0e8867f70007d89c239ff
# 1645c45aabb008c98406b3a16447040d/da6e37c1e3f0e8867f70007d89c239ff
class Skill28(ActiveSkill):
    """
        召唤出多个自身幻影。\n
        幻影会自动寻找敌人进行攻击。\n
        幻影会使用[蛇腹剑 : 破]、 [蛇腹剑 : 舞]、 [蛇腹剑 : 刺]、 [蛇腹剑 : 灭]、 [魔刃狂舞]等技能。
    """
    name = "群魔乱舞"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 3
    cube = 1
    cd = 25
    mp = [360, 3024]
    uuid = "da6e37c1e3f0e8867f70007d89c239ff"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 幻影召唤数量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 敌人可承受攻击的幻影数量上限 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [蛇腹剑 ： 破]幻影攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 4
    # [蛇腹剑 ： 破]幻影多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [蛇腹剑 ： 舞]幻影攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 3
    # [蛇腹剑 ： 舞]幻影多段攻击次数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [蛇腹剑 ： 刺]幻影攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 2
    # [蛇腹剑 ： 刺]幻影多段攻击次数 : {value7}次
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [蛇腹剑 ： 灭]幻影攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    hit8 = 12
    # [蛇腹剑 ： 灭]幻影多段攻击次数 : {value9}次
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [魔刃狂舞]幻影攻击力 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    hit10 = 11
    # [魔刃狂舞]幻影多段攻击次数 : {value11}次
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # [范围信息]
    # 搜索范围 : {value12}px
    data12 = get_data(f'{prefix}/{uuid}', 12)

    def vp_1(self):
        """
        [群魔乱舞]\n
        幻影召唤数量增加至10个\n
        - 敌人可承受攻击的幻影数量上限增加至10个\n
        - 基本冷却时间变更为50秒\n
        - 总攻击力 +100%\n
        命中时恢复生命值\n
        - 每个幻影恢复1%的生命值 (最多10%)
        """
        self.cd = 50
        self.skillRation *= 2
        ...

    def vp_2(self):
        """
        [群魔乱舞]\n
        召唤一个强大的克隆体， 施放[空绝斩 : 地裂]\n
        冲击波大小 +30%
        """
        ...

# 唤魔 : 塔莫斯之袭
# swordman_female/demon_slayer/9bff7f2559e003766fee2853dca00631
# 1645c45aabb008c98406b3a16447040d/9bff7f2559e003766fee2853dca00631
class Skill29(ActiveSkill):
    """
        挥剑时出现魔王塔莫斯， 塔莫斯会对敌人进行连续斩击， 最后以强力的交叉攻击结束并消失。\n
        可以在地面和空中施放， 按上方向键时， 可以发动强袭。\n
        快速向前飞一段距离， 在移动途中按技能键可以挥剑。
    """
    name = "唤魔 : 塔莫斯之袭"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [90, 1500]
    uuid = "9bff7f2559e003766fee2853dca00631"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 挥剑攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 塔莫斯连击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 8
    # 塔莫斯连击多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 塔莫斯最后一击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 塔莫斯大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [唤魔 : 塔莫斯之袭]\n
        向最强敌人身边召唤塔莫斯\n
        - 未命中敌人时无法施放技能\n
        - 总攻击力相同\n
        除觉醒技能外的技能命中时， 可以施放[唤魔 : 塔莫斯之袭]\n
        - 删除施放动作
        """
        ...

    def vp_2(self):
        """
        [唤魔 : 塔莫斯之袭]\n
        塔莫斯出现后立即使用强力交叉斩击\n
        - 总攻击力相同\n
        塔莫斯大小 +30%
        """
        ...

# 贪欲之燔祭
# swordman_female/demon_slayer/dc1ffbe7bfcc6dc2be737951960da9ad
# 1645c45aabb008c98406b3a16447040d/dc1ffbe7bfcc6dc2be737951960da9ad
class Skill30(PassiveSkill):
    """
        利用契魔者的转职技能击败敌人时， 有一定几率产生云雾。 魔王塔莫斯会感知并吸收云雾。\n
        敌人的云雾将持续一定时间， 吸收云雾后， 可以获得获得增加基本攻击力和技能攻击力的效果。\n
        该效果有重叠次数限制。
    """
    name = "贪欲之燔祭"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 3
    uuid = "dc1ffbe7bfcc6dc2be737951960da9ad"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 云雾发动几率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 云雾持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 吸收云雾时， 基本攻击力和技能攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 吸收效果持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 效果叠加上限 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)

    associate = [
        {"data":data2,"type":"*skillDamage"}
    ]

# 空绝斩 : 千刃
# swordman_female/demon_slayer/42c82812f86ff6704ae9952a2e6093a4
# 1645c45aabb008c98406b3a16447040d/42c82812f86ff6704ae9952a2e6093a4
class Skill31(ActiveSkill):
    """
        从异次元裂缝召唤出魔人克库斯， 同时角色化成恶魔形态。\n
        完成变身后向前滑铲， 进行强力的下斩攻击并引发爆炸。
    """
    name = "空绝斩 : 千刃"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [1500, 12232]
    uuid = "42c82812f86ff6704ae9952a2e6093a4"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 克库斯攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 7
    # 克库斯多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 克库斯爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 7
    # 克库斯爆炸多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 前冲攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # 下斩攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # 最终爆炸攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 1

# 唤魔 : 逆天之普诺
# swordman_female/demon_slayer/328867949b763ce73e243da84fd59157
# 1645c45aabb008c98406b3a16447040d/328867949b763ce73e243da84fd59157
class Skill32(ActiveSkill):
    """
        克库斯魔人环绕在角色周围， 当魔人普诺觉察出剑魔的弱点企图将其吞噬， 此时塔莫斯现身拯救剑魔。\n
        塔莫斯每次攻击时， 飞散的普诺碎片会对周围的敌人造成伤害， 普诺最终被消灭时引发爆炸。
    """
    name = "唤魔 : 逆天之普诺"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [120, 1200]
    uuid = "328867949b763ce73e243da84fd59157"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 生命值消耗比率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 克库斯飞散攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 5
    # 克库斯飞散多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 普诺碎片攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 8
    # 普诺碎片多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 普诺爆炸攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # [范围信息]
    # 克库斯飞散大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 普诺碎片大小比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 普诺爆炸大小比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

    def vp_1(self):
        """
        [唤魔 : 逆天之普诺]\n
        普诺吞噬后， 塔莫斯下劈引发爆炸\n
        - 总攻击力相同\n
        普诺爆炸范围 +20%
        """
        ...

    def vp_2(self):
        """
        [唤魔 : 逆天之普诺]\n
        克库斯命中时吸附敌人\n
        普诺碎片多段攻击次数 +6次\n
        - 总攻击力相同
        """
        ...

# 汲血魔剑
# swordman_female/demon_slayer/2a3c96b88d02372505692da0a8b54743
# 1645c45aabb008c98406b3a16447040d/2a3c96b88d02372505692da0a8b54743
class Skill33(ActiveSkill):
    """
        召唤塔莫斯， 塔莫斯和剑魔一起发动十字形斩击。
    """
    name = "汲血魔剑"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [400, 1500]
    uuid = "2a3c96b88d02372505692da0a8b54743"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 十字形斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [汲血魔剑]\n
        可以强制中断施放后僵直， 并施放蛇腹剑技能 (觉醒技能除外)\n
        可以强制中断蛇腹剑技能施放后僵直， 并施放该技能 (觉醒技能除外)\n
        - 删除施放前僵直\n
        蛇腹剑技能列表 (觉醒技能除外)\n
        - [蛇腹剑 : 破]、 [蛇腹剑 : 舞]、 [蛇腹剑 : 缠]、 [蛇腹剑 : 刺]、 [蛇腹剑 : 灭]、 [魔刃狂舞]、 [唤魔 : 塔莫斯之袭]、[汲血魔剑]、 [空绝斩 : 地裂]、 [弑神剑 : 极]、 [蛇舞血轮剑]
        """
        ...

    def vp_2(self):
        """
        [汲血魔剑]\n
        与使用太刀的塔莫斯一同发动 多次斩击\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 25秒\n
        - 单次攻击力 -50%
        """
        self.cd = 25
        self.skillRation *= 0.5
        ...

# 空绝斩 : 地裂
# swordman_female/demon_slayer/5806440d21e7546d50007a5ba11f8024
# 1645c45aabb008c98406b3a16447040d/5806440d21e7546d50007a5ba11f8024
class Skill34(ActiveSkill):
    """
        跳跃后， 将普诺变形为巨剑向下猛击形成冲击波。 被冲击波命中的敌人， 会被击倒在冲击波中心， 利用方向键可以控制跳跃的距离。\n
    方向键(无操作) : 原地\n
    方向键(向前) : 中距离\n
    方向键(向上) : 长距离
    """
    name = "空绝斩 : 地裂"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 9
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "5806440d21e7546d50007a5ba11f8024"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 冲击波攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 冲击波大小比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [空绝斩 : 地裂]\n
        在技能施放过程中输入[蛇腹剑 : 破]时， 生成冲击波的同时巨大的剑刃从地面涌起\n
        - 删除[蛇腹剑 : 破]施放动作， 合算攻击力\n
        施放时， 初始化[蛇腹剑 : 舞]技能冷却时间\n
        - [蛇腹剑 : 舞]攻击力 -11%\n
        施放过程中所受伤害 -90%\n
        冲击波大小 +30%
        """
        ...

    def vp_2(self):
        """
        [空绝斩 : 地裂]\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 20秒\n
        - 单次攻击力 -50%\n
        可以强制中断蛇腹剑技能施放后僵直， 并施放该技能 (觉醒技能除外)\n
        蛇腹剑技能列表 (觉醒技能除外)\n
        - [蛇腹剑 : 破]、 [蛇腹剑 : 舞]、 [蛇腹剑 : 缠]、 [蛇腹剑 : 刺]、 [蛇腹剑 : 灭]、 [魔刃狂舞]、 [唤魔 : 塔莫斯之袭]、[汲血魔剑]、 [空绝斩 : 地裂]、 [弑神剑 : 极]、 [蛇舞血轮剑]
        """
        self.cd = 20
        self.skillRation *= 0.5
        ...

    def effect(self, old, new):
        if self.vp == 1:
            self.associate = [{"type":"*skillDamage","data":[0] + [-11]*self.maxLv,"skills":["蛇腹剑 : 舞"]}]
        return super().effect(old, new)

# 唤魔 : 弑神剑
# swordman_female/demon_slayer/d429147c372b549c3dadcabcba50787f
# 1645c45aabb008c98406b3a16447040d/d429147c372b549c3dadcabcba50787f
class Skill35(PassiveSkill):
    """
        将力量赋予到蛇腹剑上， 强化技能效果。\n
        增加基本攻击力和转职技能攻击力， 部分技能附加特殊效果。\n
    [增加攻击力技能]\n
    [十字剑]、 [蛇腹剑 : 破]、 [蛇腹剑 : 舞]、 [蛇腹剑 : 刺]、 [碎魔剑]、 [群魔乱舞]、 [唤魔 : 逆天之普诺]、 [汲血魔剑]、 [空绝斩 : 千刃]、 [空绝斩 : 地裂]、 [弑神剑 : 极]、 [弑神剑 : 诸神献祭]、 [蛇舞血轮剑]、 [弑神剑 : 恶魔孤岛]\n
    [蛇腹剑 : 破]\n
        增加施放速度和攻击范围。\n
    [蛇腹剑 : 舞]\n
        可以强制中断施放后僵直， 并施放蛇腹剑技能。 (觉醒技能除外)\n
        可以强制中断蛇腹剑技能施放后僵直， 并施放该技能。 (觉醒技能除外)\n
    蛇腹剑技能 (觉醒技能除外)\n
    - [蛇腹剑 : 破]、 [蛇腹剑 : 舞]、 [蛇腹剑 : 缠]、 [蛇腹剑 : 刺]、 [蛇腹剑 : 灭]、  [魔刃狂舞]、 [唤魔 : 塔莫斯之袭]、 [汲血魔剑]、 [空绝斩 : 地裂]、 [弑神剑 : 极]、 [蛇舞血轮剑]\n
    [[蛇腹剑 : 刺]\n
        增加攻击范围。\n
    [蛇腹剑 : 缠]\n
        魔人灵体将会缠住敌人， 并造成持续伤害后爆炸。\n
    [蛇腹剑 : 灭/魔刃狂舞]\n
        生成魔人的剑气， 造成更多的伤害。\n
    [唤魔 : 塔莫斯之袭]\n
        增加塔莫斯的攻击次数和最终一击的攻击力， 减少多段攻击间隔。
    """
    name = "唤魔 : 弑神剑"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 3
    uuid = "d429147c372b549c3dadcabcba50787f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和部分技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [蛇腹剑 ： 缠]灵体攻击力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [蛇腹剑 ： 灭]残影攻击力比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [魔刃狂舞]残影攻击力比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [唤魔 ： 塔莫斯之袭]
    # 塔莫斯攻击次数增加 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 塔莫斯最终一击攻击力增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    associate = [
        {"data":data0,"type":"*skillDamage","exceptSkills":["魔刃狂舞","蛇腹剑 : 缠","唤魔 : 塔莫斯之袭"]},
        {"data":data1,"type":"+power6","skills":["蛇腹剑 : 缠"]},
        {"data":data1,"type":"+power7","skills":["蛇腹剑 : 缠"]},
        {"data":data2,"type":"+power4","skills":["魔刃狂舞"]},
        {"data":data2,"type":"+power5","skills":["魔刃狂舞"]},
        {"data":data4,"type":"+hit1","skills":["唤魔 : 塔莫斯之袭"],"ratio": 1},
        {"data":data5,"type":"*power3","skills":["唤魔 : 塔莫斯之袭"]}
    ]

# 弑神剑 : 极
# swordman_female/demon_slayer/3fb8395ae3b81bd608e0c4223a8eb534
# 1645c45aabb008c98406b3a16447040d/3fb8395ae3b81bd608e0c4223a8eb534
class Skill36(ActiveSkill):
    """
        魔人克库斯化身为镰刀， 抓住敌人左右甩动。 抓住敌人前， 可以通过输入左/右方向键指定抛出敌人的方向。\n
        对无法抓取的敌人不适用控制效果。
    """
    name = "弑神剑 : 极"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "3fb8395ae3b81bd608e0c4223a8eb534"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # [对可抓取的敌人]
    # 甩动攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 冲击波多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最后一击冲击波攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [对无法抓取的敌人]
    # 甩动攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # [范围信息]
    # 攻击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [弑神剑 : 极]\n
        命中时， 以无法抓取形态发动\n
        可以强制中断施放后僵直， 并施放蛇腹剑技能 (觉醒技能除外)\n
        可以强制中断蛇腹剑技能施放后僵直， 并施放该技能 (觉醒技能除外)\n
        蛇腹剑技能列表 (觉醒技能除外)\n
        - [蛇腹剑 : 破]、 [蛇腹剑 : 舞]、 [蛇腹剑 : 缠]、 [蛇腹剑 : 刺]、 [蛇腹剑 : 灭]、 [魔刃狂舞]、 [唤魔 : 塔莫斯之袭]、[汲血魔剑]、 [空绝斩 : 地裂]、 [弑神剑 : 极]、 [蛇舞血轮剑]
        """
        ...

    def vp_2(self):
        """
        [弑神剑 : 极]\n
        如果没有命中的敌人， 剩余冷却时间缩短为5秒\n
        命中时， 获得速度增加增益\n
        - 增益持续时间 : 15秒\n
        - 攻击速度 +15%\n
        - 移动速度 +15%
        """
        ...

# 弑神剑 : 诸神献祭
# swordman_female/demon_slayer/9dc8438e4572d39243c97da31c113acc
# 1645c45aabb008c98406b3a16447040d/9dc8438e4572d39243c97da31c113acc
class Skill37(ActiveSkill):
    """
        跃向空中， 与塔莫斯合体。 利用合体后的强大力量， 将普诺变形为最佳攻击形态向地面进行乱舞攻击， 之后再将普诺变形为巨剑形态刺向地面引发冲击波并使敌人进入僵直状态， 最后使用巨大的剑刃进行最终一击。
    """
    name = "弑神剑 : 诸神献祭"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 9
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "9dc8438e4572d39243c97da31c113acc"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 鞭挞攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 10
    # 鞭挞多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 巨剑冲击波攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 3
    # 巨剑冲击波多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 最后一击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1

# 蛇舞血轮剑
# swordman_female/demon_slayer/c91a62dc0a18360acf5031ac0ebf09f5
# 1645c45aabb008c98406b3a16447040d/c91a62dc0a18360acf5031ac0ebf09f5
class Skill38(ActiveSkill):
    """
        将与塔莫斯合体的蛇腹剑插入地面， 击穿前方的敌人。
    """
    name = "蛇舞血轮剑"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [1065, 8000]
    uuid = "c91a62dc0a18360acf5031ac0ebf09f5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 合体的蛇腹剑攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 合体的蛇腹剑多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 合体的蛇腹剑终结攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

# 魔源觉醒
# swordman_female/demon_slayer/0c3a468aee1f7ce06bf91eb3319518c1
# 1645c45aabb008c98406b3a16447040d/0c3a468aee1f7ce06bf91eb3319518c1
class Skill39(PassiveSkill):
    """
        吸收魔人真正的力量， 成为魔人的女王。\n
        增加基本攻击力和转职技能攻击力 ([蛇腹剑 : 缠]除外)， 部分技能赋予特殊效果。\n
    [蛇腹剑 : 破]\n
        召唤的剑增加为6个。\n
    [蛇腹剑 : 缠]\n
        抓取并鞭笞敌人后，额外进行下劈攻击。 
    """
    name = "魔源觉醒"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "0c3a468aee1f7ce06bf91eb3319518c1"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [蛇腹剑 ： 缠]下劈攻击力 : 总攻击力的{value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [
        {"data":data0,"type":"*skillDamage","exceptSkills":["蛇腹剑 : 缠"]},
        {"data":data1,"type":"+power6","skills":["蛇腹剑 : 缠"]},
        {"data":data1,"type":"+power7","skills":["蛇腹剑 : 缠"]},
    ]

# 弑神剑 : 恶魔孤岛
# swordman_female/demon_slayer/6d7c9a15c08cc41d70125083e869e1a1
# 1645c45aabb008c98406b3a16447040d/6d7c9a15c08cc41d70125083e869e1a1
class Skill40(ActiveSkill):
    """
        穿戴魔人的盔甲后， 与变身为剑的塔莫斯一起挥动蛇腹剑， 创造巨大的监狱。\n
        使用巨剑凝聚所有魔人的力量后， 摧毁整个监狱。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "弑神剑 : 恶魔孤岛"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4025, 8055]
    uuid = "6d7c9a15c08cc41d70125083e869e1a1"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 巨剑攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 15
    # 巨剑多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 巨剑终结攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'demon_slayer'
        self.nameCN = '极诣·契魔者'
        self.role = 'swordman_female'
        self.角色 = '鬼剑士(女)'
        self.职业 = '契魔者'
        self.jobId = '1645c45aabb008c98406b3a16447040d'
        self.jobGrowId = '6d459bc74ba73ee4fe5cdc4655400193'

        self.武器选项 = ['巨剑', '钝器', '太刀', '短剑']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '重甲'
        self.buff = 2.083

        super().__init__(equVersion, __name__)
