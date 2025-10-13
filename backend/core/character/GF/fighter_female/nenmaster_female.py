#a7a059ebe9e6054c0644b40ef316d6e9
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "fighter_female/nenmaster_female/cn/skillDetail"

# 光之亲和
# fighter_female/nenmaster_female/da6e37c1e3f0e8867f70007d89c239ff
# a7a059ebe9e6054c0644b40ef316d6e9/da6e37c1e3f0e8867f70007d89c239ff
class Skill1(PassiveSkill):
    """
        强化对光的亲和力， 可以增加自身的光属性抗性， 但暗属性抗性将减少。
    """
    name = "光之亲和"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "da6e37c1e3f0e8867f70007d89c239ff"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 光属性抗性增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 暗属性抗性减少 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 念气感知
# fighter_female/nenmaster_female/27bade584bb42fef68148d3a0b72bace
# a7a059ebe9e6054c0644b40ef316d6e9/27bade584bb42fef68148d3a0b72bace
class Skill2(PassiveSkill):
    """
        增加[念气波]感电几率， 用念气侦察敌人的位置， 提高失明抗性。
    """
    name = "念气感知"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "27bade584bb42fef68148d3a0b72bace"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 失明抗性增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 念气波感电几率 : 当前感电几率的3倍


# 基础精通
# fighter_female/nenmaster_female/5a56514f35cf0270ae8d6c65f8fefd78
# a7a059ebe9e6054c0644b40ef316d6e9/5a56514f35cf0270ae8d6c65f8fefd78
class Skill5(PassiveSkill):
    """
        增加基本攻击、 前冲攻击、 跳跃攻击、 [上勾拳]的攻击力。\n
        在决斗场中， 增益/减益技能、 被动技能的技能攻击力增加效果对[基础精通]无影响。
    """
    name = "基础精通"
    learnLv = 1
    masterLv = 115
    maxLv = 200
    position = 0 #TODO
    rangeLv = 1
    uuid = "5a56514f35cf0270ae8d6c65f8fefd78"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力变化率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 前冲攻击力变化率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 跳跃攻击力变化率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    associate = [{"type":"*skillRation","data":[i-100 if i>0 else 0 for i in data0],"skills":["念兽 : 龙虎啸"]}]

# 分身
# fighter_female/nenmaster_female/f2fb27162beb0b87a7cb9af7900e95f2
# a7a059ebe9e6054c0644b40ef316d6e9/f2fb27162beb0b87a7cb9af7900e95f2
class Skill9(ActiveSkill):
    """
        生成分身扰乱敌人的攻击或阻挡子弹。\n
        经过一定时间或受一定伤害后， 生成的分身就会消失。\n
        转职为气功师后， 分身仿照施放者的样子。\n
        在决斗场中，转职为气功师后， 增加分身的持续时间。
    """
    name = "分身"
    learnLv = 5
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 2
    cd = 7
    mp = [6, 84]
    uuid = "f2fb27162beb0b87a7cb9af7900e95f2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 分身生成数 : {value0}
    hit = get_data(f'{prefix}/{uuid}', 0)
    data0 = [0] + [1] * maxLv
    # 分身持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 气功师分身持续时间 : 5秒


# 念气波
# fighter_female/nenmaster_female/01c3a2fb793d293a25ed8dc7a0d70c1a
# a7a059ebe9e6054c0644b40ef316d6e9/01c3a2fb793d293a25ed8dc7a0d70c1a
class Skill20(ActiveSkill):
    """
        使念气实体化后向前方敌人发射。\n
        念气波对周围敌人具有诱导性， 在命中时爆炸， 对附近的敌人造成光属性伤害并进入感电状态。\n
        转职为气功师后， 可以强制中断基本攻击动作施放， 并大幅度减少冷却时间。
    """
    name = "念气波"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 1
    mp = [15, 154]
    uuid = "01c3a2fb793d293a25ed8dc7a0d70c1a"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    power0 = 1
    # 诱导性比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 感电几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 感电持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 感电攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [转职为气功师后]
    # 念气波冷却时间减少率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 念气波大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 射程距离 : {value7}px
    data7 = get_data(f'{prefix}/{uuid}', 7)

    mode = ["蓄力","普通"]

    def setMode(self, mode):
        if mode == "蓄力":
            self.cd = 3
        if mode == "普通":
            self.cd = 1
            self.power0 = 1

# 光之兵刃
# fighter_female/nenmaster_female/a6c8f69107f8c4f5d1a0c7a57d000290
# a7a059ebe9e6054c0644b40ef316d6e9/a6c8f69107f8c4f5d1a0c7a57d000290
class Skill21(ActiveSkill):
    """
        使自身和一定范围内所有队员的武器属性变成光属性， 并增加自身的基本攻击力、 技能攻击力和属性攻击力， 效果持续一定时间。
    """
    name = "光之兵刃"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 5
    rangeLv = 3
    cd = 5
    uuid = "a6c8f69107f8c4f5d1a0c7a57d000290"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 施放范围 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 基本攻击力和技能攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 属性攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 气玉弹
# fighter_female/nenmaster_female/3fb8395ae3b81bd608e0c4223a8eb534
# a7a059ebe9e6054c0644b40ef316d6e9/3fb8395ae3b81bd608e0c4223a8eb534
class Skill22(ActiveSkill):
    """
        把念气聚为小型球状向前抛出， 对敌人造成光属性的多段攻击伤害， 并把附近的敌人拉拽到一起。\n
        施放技能时按下前方向键， 念气珠会抛向更远处。
    """
    name = "气玉弹"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 8
    mp = [20, 168]
    uuid = "3fb8395ae3b81bd608e0c4223a8eb534"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 11
    # 念气珠多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 念气珠持续时间 : 1.5秒
    # [范围信息]
    # 念气珠大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 烈日气息
# fighter_female/nenmaster_female/04883563896fe1adac7505c6146b5f59
# a7a059ebe9e6054c0644b40ef316d6e9/04883563896fe1adac7505c6146b5f59
class Skill23(ActiveSkill):
    """
        增加周围队友的光属性抗性、 魔法防御力、 攻击速度和施放速度， 效果持续一定时间。
    """
    name = "烈日气息"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 7
    rangeLv = 3
    cd = 5
    mp = [194, 1502]
    uuid = "04883563896fe1adac7505c6146b5f59"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 施放范围 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 光属性抗性增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 魔法防御力增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 攻击速度增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 施放速度增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 队员攻击速度增加 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 队员施放速度增加 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 队员光属性抗性增加 : {value8}
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 队员魔法防御力增加 : {value9}
    data9 = get_data(f'{prefix}/{uuid}', 9)

# 幻影爆碎
# fighter_female/nenmaster_female/f0cc2c950f3bdf4103c75fa496bcac34
# a7a059ebe9e6054c0644b40ef316d6e9/f0cc2c950f3bdf4103c75fa496bcac34
class Skill24(PassiveSkill):
    """
        分身的冷却时间增加， 可强制中断基本攻击后使用。 敌人碰撞分身时引发光属性爆炸， 对周围敌人造成伤害。\n
        在决斗场中， 学习幻影爆碎后， 分身的冷却时间减少。
    """
    name = "幻影爆碎"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    uuid = "f0cc2c950f3bdf4103c75fa496bcac34"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 每个分身攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [范围信息]
    # 分身爆炸大小比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 学习念气归元后搜寻敌人范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [
        {"type": "*skillRation","data":data0,"skills":["分身"],"ratio":1},
        {"type": "+cd","data":[0]+[3]*maxLv,"skills":["分身"],"ratio":1}
    ]

# 蓄念炮
# fighter_female/nenmaster_female/c7bf7ccab413009640e65ca6f2f0263a
# a7a059ebe9e6054c0644b40ef316d6e9/c7bf7ccab413009640e65ca6f2f0263a
class Skill25(PassiveSkill):
    """
        使念气波变成可以蓄气的念气波， 蓄气完毕后， 可以大幅度增加念气波的大小、 攻击力和射程， 并100%穿刺敌人； 但冷却时间比普通念气波长。
    """
    name = "蓄念炮"
    learnLv = 20
    masterLv = 1
    maxLv = 11
    position = 1
    rangeLv = 1
    cd = 3
    mp = [40, 56]
    uuid = "c7bf7ccab413009640e65ca6f2f0263a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 念气波攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 增加感电几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 增加念气波飞行时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 增加念气波发射速度 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    associate = [
        {"type":"*power0","data":data0,"skills":["念气波"]}
    ]


# 念气罩
# fighter_female/nenmaster_female/dc1ffbe7bfcc6dc2be737951960da9ad
# a7a059ebe9e6054c0644b40ef316d6e9/dc1ffbe7bfcc6dc2be737951960da9ad
class Skill28(ActiveSkill):
    """
        学习后， 在自身周围生成一个巨大的念气罩， 使念气罩内的所有队员进入无敌状态。\n
        经过一段时间或受到一定伤害后， 念气罩就会消失。\n
        念气罩生成后施放者可以移动， 但念气罩不会跟随移动； 念气罩消失过程中， 效果也会消失。
    """
    name = "念气罩"
    learnLv = 25
    masterLv = 1
    maxLv = 11
    position = 2
    rangeLv = 3
    cd = 30
    mp = [60, 560]
    uuid = "dc1ffbe7bfcc6dc2be737951960da9ad"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 念气罩持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 念气罩生命值 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 念气罩范围 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 念雷破
# fighter_female/nenmaster_female/4c5271b0ecce120d7fc113f377fae76f
# a7a059ebe9e6054c0644b40ef316d6e9/4c5271b0ecce120d7fc113f377fae76f
class Skill29(ActiveSkill):
    """
        用念气环绕身体， 向前方突进并推开移动路径上的所有敌人， 突进结束时念气爆炸， 对周围造成伤害。\n
        按向前方向键， 可以增加突进距离。 
    """
    name = "念雷破"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 6
    mp = [48, 403]
    uuid = "4c5271b0ecce120d7fc113f377fae76f"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 念气爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 念气爆炸大小比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 念气环绕
# fighter_female/nenmaster_female/0ed3148658fe37b3336ccb718dc0fdb0
# a7a059ebe9e6054c0644b40ef316d6e9/0ed3148658fe37b3336ccb718dc0fdb0
class Skill30(ActiveSkill):
    """
        生成念气珠环绕在自身周围， 可以使敌人受到一定的光属性伤害。\n
        念气珠自动生成， 并持续消耗魔法值。\n
        再次按技能键， 可以直接关闭念气珠。\n
        念气珠的数量越多， 基本攻击力和技能攻击力越高。
    """
    name = "念气环绕"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 3
    rangeLv = 2
    cd = 4
    mp = [268, 1694]
    uuid = "0ed3148658fe37b3336ccb718dc0fdb0"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 每个念气珠物理防御力增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 每个念气珠基本攻击力和技能攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 学习念气归元后， 念气珠搜寻敌人范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 学习念气归元后， 念气珠爆炸大小比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    associate = [
        # 总共两个珠子
        {"type":"*skillRation","data":data3,"ratio":100/2}
    ]

    def getSkillCD(self,mode=None):
        # 攻击间隔时间
        return 0.5

# 旋风腿
# fighter_female/nenmaster_female/202edb928046f4fa6dedf6337377efd5
# a7a059ebe9e6054c0644b40ef316d6e9/202edb928046f4fa6dedf6337377efd5
class Skill31(ActiveSkill):
    """
        快速旋转身体向前移动并用连续的扫腿攻击周围的敌人； 可以在地面或空中使用， 最后的扫腿还可以击倒敌人。\n
        施放后， 可以按上/下方向键改变移动方向， 或按跳跃键中断技能。\n
        转职成为散打时， 可以强制中断基本攻击动作， 并立即施放该技能。
    """
    name = "旋风腿"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cd = 8
    mp = [50, 420]
    uuid = "202edb928046f4fa6dedf6337377efd5"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 回旋踢攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0  = 4
    # 攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 念兽螺旋波
# fighter_female/nenmaster_female/2e2b7efe778656690f9c8cb6e47c3932
# a7a059ebe9e6054c0644b40ef316d6e9/2e2b7efe778656690f9c8cb6e47c3932
class Skill32(ActiveSkill):
    """
        向前方发出一只念兽。 念兽呈螺旋状飞出， 吸附移动路径上的敌人并造成伤害。 然后再发出一只念兽， 对路径上的敌人造成伤害， 并有一定几率使敌人进入感电状态。
    """
    name = "念兽螺旋波"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 12
    mp = [96, 806]
    uuid = "2e2b7efe778656690f9c8cb6e47c3932"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 第一个念兽攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 第一个念兽多段攻击次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 第二个念兽攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 4
    # 第二个念兽多段攻击次数上限 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 感电几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 感电持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 感电攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 念兽大小比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

# 狮子吼
# fighter_female/nenmaster_female/9cb6f9ed646fa87f9b7680a42ce83d1a
# a7a059ebe9e6054c0644b40ef316d6e9/9cb6f9ed646fa87f9b7680a42ce83d1a
class Skill33(ActiveSkill):
    """
        发出可对周围敌人造成伤害的狮吼， 并有一定几率使敌人进入眩晕状态。
    """
    name = "狮子吼"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [120, 1008]
    uuid = "9cb6f9ed646fa87f9b7680a42ce83d1a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 眩晕几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 眩晕时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 狮子吼范围 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [狮子吼]\n
        命中敌人时不会使敌人眩晕； 念气爆炸后强制控制敌人3秒\n
        可以解除自身的异常状态并施放\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 7.5秒\n
        - 单次攻击力 -50%
        """
        self.cd = 7.5
        self.skillRation *= 0.5
        ...

    def vp_2(self):
        """
        [狮子吼]\n
        生成分身代替施放[狮子吼]\n
        - 可以在其他技能施放过程中无施放动作施放[狮子吼] (觉醒技能除外)
        """
        ...

# 螺旋念气场
# fighter_female/nenmaster_female/4224f9b0b8c7c903e9a1e0f9d9f6d04d
# a7a059ebe9e6054c0644b40ef316d6e9/4224f9b0b8c7c903e9a1e0f9d9f6d04d
class Skill34(ActiveSkill):
    """
        凝聚念气生成念气场， 使周围敌人受到光属性伤害并有一定几率使其进入感电状态。
    """
    name = "螺旋念气场"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [170, 1428]
    uuid = "4224f9b0b8c7c903e9a1e0f9d9f6d04d"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 15
    # 感电几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 感电持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 感电攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 念气场范围 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [螺旋念气场]\n
        从螺旋念气场正面发射\n
        念气场范围 +50%
        """
        ...

    def vp_2(self):
        """
        [螺旋念气场]\n
        在前方生成巨大的螺旋念气场， 聚集敌人后爆炸\n
        - 删除多段攻击\n
        - 总攻击力相同
        """
        ...

# 念兽 : 龙虎啸
# fighter_female/nenmaster_female/1b1cfab062e0768bcc889e33e1f30dbf
# a7a059ebe9e6054c0644b40ef316d6e9/1b1cfab062e0768bcc889e33e1f30dbf
class Skill35(ActiveSkill):
    """
        召唤出念兽龙虎， 强化自身和队员的能力。\n
        此状态下， 可以使基本攻击增加至5次， 而且基本攻击、 前冲攻击、 跳跃攻击时， 与龙虎一起进行攻击。\n
        基本攻击、 前冲攻击、 跳跃攻击时， 适用念兽龙虎的攻击力。\n
        同时还可以使前冲攻击、 跳跃攻击和最后一次基本攻击命中的敌人进入感电状态。\n
        自身的攻击范围会增加， 并且基本攻击、 跳跃攻击、 前冲攻击变更为受[基础精通]影响的攻击。\n
        技能持续期间， 增加自身基本攻击力和技能攻击力。\n
        自身和队友的移动速度、物防和魔防增加； 队友的增益效果在一定范围内实时生效。\n
        进入地下城时自动施放。 (决斗场除外)
    """
    name = "念兽 : 龙虎啸"
    learnLv = 40
    masterLv = 10
    maxLv = 20
    position = 5
    rangeLv = 3
    cd = 5
    mp = [550, 5217]
    uuid = "1b1cfab062e0768bcc889e33e1f30dbf"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
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
    # 前冲攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # 跳跃攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 1
    # 持续时间 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 最后一次基本攻击感电几率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 前冲、 跳跃攻击感电几率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 感电持续时间 : {value10}秒
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 感电攻击力 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 基本攻击力和技能攻击力增加率 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 有效范围 : {value13}px
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # 队员移动速度增加 : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # 队员物理防御力增加 : {value15}
    data15 = get_data(f'{prefix}/{uuid}', 15)
    # 队员魔法防御力增加 : {value16}
    data16 = get_data(f'{prefix}/{uuid}', 16)

    associate = [
        {"type":"*skillRation","data":data12}
    ]

# 狂龙升天破
# fighter_female/nenmaster_female/dbf8b30c7057032af0d68fcfa289fdae
# a7a059ebe9e6054c0644b40ef316d6e9/dbf8b30c7057032af0d68fcfa289fdae
class Skill36(ActiveSkill):
    """
        将念聚集于脚后上踢， 释放出念兽龙。\n
        念兽龙从地面升起， 对范围内敌人造成多段伤害。
    """
    name = "狂龙升天破"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [316, 2488]
    uuid = "dbf8b30c7057032af0d68fcfa289fdae"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 念兽龙攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 11
    # 念兽龙多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [狂龙升天破]\n
        取消聚集念气的动作\n
        - 念兽龙释放速度 +25%\n
        - 多段攻击间隔 -25%\n
        攻击范围 +30%
        """
        ...

    def vp_2(self):
        """
        [狂龙升天破]\n
        可以强制中断转职技能的施放后僵直并施放[狂龙升天破] (觉醒技能除外)\n
        上踢动作后可以连接施放[奔雷掌]
        """
        ...

# 乱舞 · 千叶花
# fighter_female/nenmaster_female/669f1428193f61f9d92c743b72438c4d
# a7a059ebe9e6054c0644b40ef316d6e9/669f1428193f61f9d92c743b72438c4d
class Skill37(PassiveSkill):
    """
        千叶花的气息凝聚在周围， 增加自身的魔法暴击率、 魔法暴击伤害、 施放速度和移动速度。\n
        每隔一段时间， 自身周围会生成防御型千叶花。 若千叶花盛开状态下遭受敌人攻击， 则可以免除自身所受伤害并提高硬直， 但千叶花会消失。\n
        受到中毒、 出血等持续性伤害时， 千叶花免除伤害的效果无效， 消失的千叶花经一定时间后又会重新盛开。
    """
    name = "乱舞 · 千叶花"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 3
    uuid = "669f1428193f61f9d92c743b72438c4d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 硬直增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法暴击伤害增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 魔法暴击率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 施放速度增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 移动速度增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 重新盛开所需时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)

    associate = [{"type":"*skillRation","data":data1}]

# 千莲怒放
# fighter_female/nenmaster_female/51a08fd0c90f0a5276cd552047fac93d
# a7a059ebe9e6054c0644b40ef316d6e9/51a08fd0c90f0a5276cd552047fac93d
class Skill38(ActiveSkill):
    """
        凝聚念气生成6个花蕾形态的念花。\n
        花蕾状态为0阶段， 若花蕾受到光属性伤害， 则会成长为念花。\n
        念花从第1阶段到第3阶段依次成长， 念花的成长阶段越高， 攻击力越强、 攻击范围越广。\n
        再次按技能键或经过一段时间后， 念花会依次产生爆炸并给予周围敌人光属性伤害。\n
        在空中或者技能施放过程中， 可以再次按技能键。\n
        花蕾状态下的0阶段时无法引爆， 持续时间结束后会消失。
    """
    name = "千莲怒放"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [900, 7559]
    uuid = "51a08fd0c90f0a5276cd552047fac93d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 念花持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 成长到1阶段所需的伤害 : 3阶段的{value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 成长到2阶段所需的伤害 : 3阶段的{value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 成长到3阶段所需的伤害 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 1阶段攻击力 : 3阶段的{value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 2阶段攻击力 : 3阶段的{value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 3阶段攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 6
    # 念花攻击次数上限 : {value7}次
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 1阶段攻击范围 : 3阶段的{value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 2阶段攻击范围 : 3阶段的{value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 3阶段攻击范围 : {value10}px
    data10 = get_data(f'{prefix}/{uuid}', 10)

# 究极念气罩
# fighter_female/nenmaster_female/2c9d9a36c8401bddff6cdb80fab8dc24
# a7a059ebe9e6054c0644b40ef316d6e9/2c9d9a36c8401bddff6cdb80fab8dc24
class Skill39(PassiveSkill):
    """
        在自身周围生成一个巨大的念气罩， 使念气罩内的所有队员进入无敌状态。 与普通念气罩相比， 巨大念气罩的范围更大、 生命值更高、 持续时间更长。\n
        念气罩受到伤害时， 可以使队员恢复一定量的生命值， 并对敌人造成伤害。\n
        队员的生命值恢复量随念气罩生命值的增加而增加。\n
        经过一段时间或受到一定伤害后， 念气罩就会消失。
    """
    name = "究极念气罩"
    learnLv = 60
    masterLv = 1
    maxLv = 11
    position = 2
    rangeLv = 2
    uuid = "2c9d9a36c8401bddff6cdb80fab8dc24"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 念气罩持续时间增加 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 念气罩范围增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 念气罩生命值增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 念气罩生命值与队员生命值恢复比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 奔雷掌
# fighter_female/nenmaster_female/5806440d21e7546d50007a5ba11f8024
# a7a059ebe9e6054c0644b40ef316d6e9/5806440d21e7546d50007a5ba11f8024
class Skill40(ActiveSkill):
    """
        跳到空中后， 向地面发射念气波动造成光属性伤害。 \n
        在空中使用时， 需要在一定高度以上才能施放技能。
    """
    name = "奔雷掌"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [450, 1260]
    uuid = "5806440d21e7546d50007a5ba11f8024"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 小狂龙爆炸攻击力 : {value0}% 
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 6
    # 最后一击巨大狂龙爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 小狂龙爆炸攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 巨大狂龙爆炸攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 狂龙爆炸范围 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [奔雷掌]\n
        删除小狂龙爆炸攻击\n
        - 总攻击力相同\n
        - 巨大狂龙下降速度 -300%\n
        - 将移动路径上敌人聚集到前方
        """
        ...

    def vp_2(self):
        """
        [奔雷掌]\n
        与分身一起施放更强力、 攻击范围更广的[奔雷掌]\n
        - 小型狂龙爆炸攻击次数 : 10次\n
        - 巨型狂龙爆炸攻击次数 : 2次\n
        - 基本冷却时间变更为60秒\n
        - 总攻击力 +100%\n
        攻击范围 +30%
        """
        self.cd = 60
        self.skillRation *= 2
        ...

# 狂狮怒吼
# fighter_female/nenmaster_female/7cf17936a039b418660424125dc968d7
# a7a059ebe9e6054c0644b40ef316d6e9/7cf17936a039b418660424125dc968d7
class Skill41(ActiveSkill):
    """
        发出可以对周围敌人造成光属性伤害的狮吼。\n
        可以解除我方队员的异常状态； 狮吼可以增加我方队员的命中率和回避率， 该效果持续一定时间。
    """
    name = "狂狮怒吼"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 2
    cube = 2
    cd = 30
    mp = [800, 1680]
    uuid = "7cf17936a039b418660424125dc968d7"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 解除异常状态数量上限 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 队友命中率增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 队友回避率增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 增益效果持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # [狂狮怒吼]范围 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [狂狮怒吼]\n
        施放时吸附敌人\n
        - 吸附范围和攻击范围相同\n
        命中时3秒内， 所受伤害 -60%\n
        攻击范围 +20%
        """
        ...

    def vp_2(self):
        """
        [狂狮怒吼]\n
        施放[狂狮怒吼]时， 初始化[狮子吼]的冷却时间\n
        - [狮子吼]攻击力 -33%\n
        [狮子吼]、 [狂狮怒吼]技能施放时间 -20%
        """
        ...

    def effect(self, old, new):
        if self.vp == 2:
            self.associate = [{"type":"*skillRation","data":[0] + [-33]*self.maxLv,"skills":["狮子吼"]}]
        return super().effect(old, new)

# 念花守心
# fighter_female/nenmaster_female/547ab2b2bd860d3e37355a9cfbc1077c
# a7a059ebe9e6054c0644b40ef316d6e9/547ab2b2bd860d3e37355a9cfbc1077c
class Skill42(PassiveSkill):
    """
        获得领悟， 部分念气技能变更， 操控念气的能力提升。\n
        施放部分念气技能时， 进入霸体状态， 效果持续3秒。\n
        在霸体持续时间内再次施放时， 持续时间刷新。\n
        增加攻击速度、 施放速度、 基本攻击力和转职技能攻击力。\n
        究极念气罩技能结束时， 念气罩范围内的队友生成移动型迷你念气罩。\n
        迷你念气罩的生命值为究极念气罩一定比例。\n
        [霸体适用技能]\n
        [狮子吼]、 [螺旋念气场]、 [狂龙升天破]、 [奔雷掌]、 [狂狮怒吼]、 [击电奔星]、 [聚能念气炮]、 [天雷分身步]
    """
    name = "念花守心"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 3
    uuid = "547ab2b2bd860d3e37355a9cfbc1077c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击、 施放速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和转职技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 念气罩生命值增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 迷你念气罩生命值比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 迷你念气罩持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 分身生成距离减少率 : 50%

    associate = [
        {"type":"*skillRation","data":data1}
    ]

# 击电奔星
# fighter_female/nenmaster_female/a5fa08f5d509e6ff2ebc68856a470b5a
# a7a059ebe9e6054c0644b40ef316d6e9/a5fa08f5d509e6ff2ebc68856a470b5a
class Skill43(ActiveSkill):
    """
        在前方召出分身后， 与分身一起向前突进并攻击敌人。 按向前方向键， 可以突进更远的距离。\n
        若队友接触到该技能的光属性爆炸， 则可恢复少量生命值。\n
        施放中按跳跃键， 可以立即发动终结攻击。
    """
    name = "击电奔星"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "a5fa08f5d509e6ff2ebc68856a470b5a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 幻影爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 幻影爆炸攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 每次爆炸队员生命值恢复量 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 爆炸大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [击电奔星]\n
        分身在穿透敌人后， 在最大移动距离处爆炸\n
        - 角色不再突进\n
        - 分身突进和爆炸距离 -20%\n
        - 分身爆炸范围 +30%\n
        技能进程速度 -20%
        """
        ...

    def vp_2(self):
        """
        [击电奔星]\n
        与分身一起突进\n
        变更为单次攻击\n
        - 总攻击力相同\n
        使被命中的敌人进入眩晕异常状态， 效果持续5秒
        """
        ...

# 聚能念气炮
# fighter_female/nenmaster_female/506e7ed77d517419a6e1c437a2cedb17
# a7a059ebe9e6054c0644b40ef316d6e9/506e7ed77d517419a6e1c437a2cedb17
class Skill44(ActiveSkill):
    """
        聚集念气波使之爆炸， 并向前方发射强力的念气炮。
    """
    name = "聚能念气炮"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "506e7ed77d517419a6e1c437a2cedb17"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 能量波大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [聚能念气炮]\n
        生成2个分身， 代替发射聚能念气炮\n
        攻击范围 +30%
        """
        ...

    def vp_2(self):
        """
        [聚能念气炮]\n
        发射追踪型念气珠\n
        发射念气珠的同时， 为自身生成保护型念气珠\n
        - 追踪型念气珠 : 3秒内攻击最强敌人\n
        - 寻敌范围 : 角色前方800px\n
        - 保护型念气珠 : [乱舞 · 千叶花]技能剩余冷却时间 -50%
        """
        ...

# 念帝旋天破
# fighter_female/nenmaster_female/5dc7008b12a459325b548b0715c6b73c
# a7a059ebe9e6054c0644b40ef316d6e9/5dc7008b12a459325b548b0715c6b73c
class Skill45(ActiveSkill):
    """
        跳到空中聚集念气能量， 然后强力释放， 对敌人造成大伤害， 使其进入感电状态。\n
        按住技能键可进行蓄气， 蓄气时间越久， 攻击范围越大。\n
        强力释放时， 攻击力与蓄气无关。
    """
    name = "念帝旋天破"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "5dc7008b12a459325b548b0715c6b73c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 攻击范围 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 达到蓄气上限时， 攻击范围 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 蓄气时间上限 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 感电几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 感电持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 感电攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

# 念气归元
# fighter_female/nenmaster_female/5cac3411ccef1af333953e0ded5e942d
# a7a059ebe9e6054c0644b40ef316d6e9/5cac3411ccef1af333953e0ded5e942d
class Skill46(PassiveSkill):
    """
        将意志注入念气之中， 用意志控制念气， 从而实现更高境界的念气操控。\n
        增加基本攻击力和转职技能攻击力， 部分技能附加额外效果。\n
        [幻影爆碎] : 不会减少分身的生成距离间隔。\n
        删除再次输入技能键功能， 施放时会向探索范围内级别最高的怪物突进并爆炸。 范围内没有敌人时，无法施放技能。\n
        [念气环绕] : 施放转职攻击技能时， 念气珠自动飞向范围内级别最高的怪物并爆炸。
    """
    name = "念气归元"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "5cac3411ccef1af333953e0ded5e942d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [幻影爆碎]搜寻敌人范围 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [念气环绕]搜寻敌人范围 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [念气环绕]爆炸攻击力 : 每个念气珠攻击力的400%
    # 念气珠发射后再次生成间隔 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    associate = [
        {"type":"*skillRation","data":data0}
    ]

# 天雷分身步
# fighter_female/nenmaster_female/85f7c810ad503790e8626439fe936d56
# a7a059ebe9e6054c0644b40ef316d6e9/85f7c810ad503790e8626439fe936d56
class Skill47(ActiveSkill):
    """
        向前方全力突进后， 与召唤的分身一起向周围进行多次乱舞攻击。\n
    乱舞攻击结束后， 与分身一起将念之力凝聚于一点后引爆。
    """
    name = "天雷分身步"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [833, 1667]
    uuid = "85f7c810ad503790e8626439fe936d56"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 突进攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 乱舞攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 10
    # 乱舞多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1

# 念印幻流破
# fighter_female/nenmaster_female/002cbdd9bfd0f0b970451ae8d48d029e
# a7a059ebe9e6054c0644b40ef316d6e9/002cbdd9bfd0f0b970451ae8d48d029e
class Skill48(ActiveSkill):
    """
        将自身的意志注入存在于天地万物的念气之中， 幻化为念花中绽放的念兽龙的形态后释放。\n
        依次释放承载意志大地之念幻化的黄色念兽龙， 以及承载意志的天空之念幻化的蓝色念兽龙。\n
        操控释放的念兽龙横扫周围一切， 然后为身体注入极致的念气力量， 与念兽龙联合发动终结攻击。\n
    [三次觉醒技能]\n
        施放三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法施放三次觉醒技能。
    """
    name = "念印幻流破"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 4028]
    uuid = "002cbdd9bfd0f0b970451ae8d48d029e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 黄色念兽龙横扫攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 黄色念兽龙横扫多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 蓝色念兽龙横扫攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 5
    # 蓝色念兽龙横扫多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 助跑后第一次踢击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # 第二次踢击攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # 最后一击爆炸攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 1


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'nenmaster_female'
        self.nameCN = '归元·气功师'
        self.role = 'fighter_female'
        self.角色 = '格斗家(女)'
        self.职业 = '气功师'
        self.jobId = 'a7a059ebe9e6054c0644b40ef316d6e9'
        self.jobGrowId = '37495b941da3b1661bc900e68ef3b2c6'

        self.武器选项 = ['手套', '臂铠','爪','东方棍']
        self.输出类型选项 = ['魔法百分比']
        self.输出类型 = '魔法百分比'
        self.防具精通属性 = ['智力']
        self.防具类型 = '布甲'
        self.buff = 1.628*1.21

        super().__init__(equVersion, __name__)
