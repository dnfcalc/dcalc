#ddc49e9ad1ff72a00b53c6cff5b1e920
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "thief/necro/cn/skillDetail"



# 切割
# thief/necro/9dda3f4a849dba1a288dd65e116860f2
# ddc49e9ad1ff72a00b53c6cff5b1e920/9dda3f4a849dba1a288dd65e116860f2
class Skill6(ActiveSkill):
    """
    前冲攻击中输入攻击键时， 施放追加斩击。\n
    攻击力、 攻击范围、 前进速度和前进距离随技能等级增加而增大。
    """
    name = "切割"
    learnLv = 5
    masterLv = 1
    maxLv = 6
    position = 0 #TODO
    rangeLv = 2
    cd = 2.5
    mp = [6, 56]
    uuid = "9dda3f4a849dba1a288dd65e116860f2"
    hasVP = False
    hasUP = False

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 前冲速度和距离比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)


# 暗魂波
# thief/necro/ade01c1d6afc8a05055225045e89fe49
# ddc49e9ad1ff72a00b53c6cff5b1e920/ade01c1d6afc8a05055225045e89fe49
class Skill9(ActiveSkill):
    """
    向敌人发射暗属性球体。\n
    球体会自动寻找敌人， 发现敌人后对敌人造成伤害， 最后球体爆炸。\n
    -  [转职为黑夜术士后附加效果]  -\n
    施放[降临 : 暴君巴拉克]的状态下， 可以蓄气施放[暗魂波]。\n
    蓄气施放[暗魂波]时， 球体变大且增加攻击力。\n
    在决斗场中， 地图内球体的存在时间减少。
    """
    name = "暗魂波"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 3.5
    mp = [15, 161]
    uuid = "ade01c1d6afc8a05055225045e89fe49"
    hasVP = False
    hasUP = False

    # 多段攻击次数上限 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 多段攻击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 3
    power1 = 0
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    power2 = 0
    # 诱导力比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [转职为黑夜术士后]
    # 蓄气时攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 地图内球体存在时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [冥河之钥]
    # 多段攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 4


# 骨盾
# thief/necro/ff171dc487807bb9aa28900ca9a46b41
# ddc49e9ad1ff72a00b53c6cff5b1e920/ff171dc487807bb9aa28900ca9a46b41
class Skill11(ActiveSkill):
    """
    在自身或队员周围召唤由骨头碎片形成的骨盾， 可以增加被骨盾守护的角色的物理防御力和魔法防御力。\n
    该角色被攻击时， 骨头碎片会自动飞向敌人， 并使敌人受到无属性魔法伤害。\n
    每次被攻击时， 骨头碎片会逐块消失。 当骨头碎片全部消失时， 增加的物理防御力和魔法防御力效果就会消失。\n
    [转职为黑夜术士后功能变更]\n
    减少骨盾的持续时间。\n
    学习后减少所受伤害， 施放技能后被攻击一定次数内附加霸体护甲。\n
    可以在其他动作中施放， 不受冷却时间减少效果的影响。\n
    在决斗场中， 不适用持续时间减少和霸体护甲效果， 施放技能时减少所受伤害。
    """
    name = "骨盾"
    learnLv = 10
    masterLv = 1
    maxLv = 7
    position = 5 #TODO
    rangeLv = 3
    cd = 15
    mp = [20, 400]
    uuid = "ff171dc487807bb9aa28900ca9a46b41"
    hasVP = False
    hasUP = False

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 骨盾持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 骨头碎片数量 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 魔法防御力增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 物理防御力增加 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 发射骨头碎片冷却时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [转职为黑夜术士后]
    # 持续时间减少率 : 85%
    # 所受伤害减少率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 霸体护甲生效次数 : {value7}次
    data7 = get_data(f'{prefix}/{uuid}', 7)


# 诅咒之箭
# thief/necro/547ab2b2bd860d3e37355a9cfbc1077c
# ddc49e9ad1ff72a00b53c6cff5b1e920/547ab2b2bd860d3e37355a9cfbc1077c
class Skill19(ActiveSkill):
    """
    召唤暗属性的诅咒之箭后， 向前方敌人发射； 被诅咒之箭命中的敌人会受到暗属性多段魔法伤害， 并有一定几率进入诅咒状态。
    """
    name = "诅咒之箭"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 10
    mp = [22, 235]
    uuid = "547ab2b2bd860d3e37355a9cfbc1077c"
    hasVP = False
    hasUP = True

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 发射数量 : {value1}发
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 诅咒几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 诅咒持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 多段攻击次数上限 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 降临 : 尼古拉斯
# thief/necro/1fadde0eece18649caddbca7bd58cc2f
# ddc49e9ad1ff72a00b53c6cff5b1e920/1fadde0eece18649caddbca7bd58cc2f
class Skill20(ActiveSkill):
    """
    召唤蜘蛛族王子尼古拉斯。\n
    若黑夜术士死亡或再次按技能键， 则尼古拉斯会消失。\n
    尼古拉斯的生命值和防御力以角色数值的一定比例换算。\n
    在地下城中， 不会被敌人击中。\n
    在决斗场中， 适用单独的生命值和防御力。\n
    - [攻击模式] -\n
    黑蜘蛛 : 接近敌人时， 向敌人投掷极速旋转的黑蜘蛛。\n
    艾克尼亚 : 释放出艾克尼亚的灵体， 造成大量伤害。
    """
    name = "降临 : 尼古拉斯"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 5
    mp = [30, 420]
    uuid = "1fadde0eece18649caddbca7bd58cc2f"
    hasVP = False
    hasUP = False

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 尼古拉斯等级 : {value1}级
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 黑蜘蛛旋转攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 4
    # 艾克尼亚攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # - [决斗场] -
    # 尼古拉斯生命值 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)

    mode = ['蜘蛛', '艾克']

    def setMode(self, mode):
        if mode == '蜘蛛':
            self.hit2 = 4
            self.hit3 = 0
            self.cd = 2
        elif mode == '艾克':
            self.hit2 = 0
            self.hit3 = 1
            self.cd = 6

    def getSkillCD(self, mode=None):
        return self.cd

# 手杖精通
# thief/necro/c47b66efd27845ef14954928ea2f95c8
# ddc49e9ad1ff72a00b53c6cff5b1e920/c47b66efd27845ef14954928ea2f95c8
class Skill21(PassiveSkill):
    """
    除[千魂祭]、 [亡者君临 : 巴拉克之戮]、 [命运殇痕·摩罗斯之咒]的其他技能的冷却时间减少。 装备手杖时， 施放速度增加。
    """
    name = "手杖精通"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 4 #TODO
    rangeLv = 1
    uuid = "c47b66efd27845ef14954928ea2f95c8"
    hasVP = False
    hasUP = False

    # 施放速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 技能冷却时间减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"type":"*cdReduce","data":data1,"exceptSkills":["千魂祭","亡者君临 : 巴拉克之戮","命运殇痕·摩罗斯之咒"]}]

# 驱使枯灵
# thief/necro/d0cdaca82892e54097f22a1f60817048
# ddc49e9ad1ff72a00b53c6cff5b1e920/d0cdaca82892e54097f22a1f60817048
class Skill22(ActiveSkill):
    """
    命令尼古拉斯召唤枯灵群。\n
    枯灵会对敌人进行撕咬攻击， 且经过一定时间后还会进行暗属性爆炸攻击。\n
    被枯灵攻击的敌人有一定几率进入诅咒状态。\n
    对无法抓取的敌人不适用控制效果。\n
    在决斗场中， 枯灵的撕咬攻击失败时， 一定时间后才能再次发动撕咬攻击。\n
    尼古拉斯的生命值和防御力以角色数值的一定比例换算。\n
    在地下城中， 不会被敌人击中。\n
    在决斗场中， 适用单独的生命值和防御力。
    """
    name = "驱使枯灵"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 8
    mp = [32, 343]
    uuid = "d0cdaca82892e54097f22a1f60817048"
    hasVP = False
    hasUP = True

    # 枯灵等级 : {value0}级
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 枯灵召唤持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 枯灵生命值 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 枯灵撕咬攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 枯灵最后撕咬攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 枯灵撕咬次数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 诅咒几率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 诅咒持续时间 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 诅咒等级 : {value8}级
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 枯灵召唤数量上限 : {value9}
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 爆炸魔法攻击力 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    hit10 = 5
    # [范围信息]
    # 枯灵爆炸扩大率 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # [决斗场]
    # 枯灵撕咬攻击冷却时间 : {value12}秒
    data12 = get_data(f'{prefix}/{uuid}', 12)

    mode = ["自爆", "撕咬"]

    def setMode(self, mode):
        if mode == "自爆":
            self.hit3 = 0
            self.hit4 = 0
            self.hit10 = 5
        elif mode == "撕咬":
            self.hit3 = 2
            self.hit4 = 1
            self.hit10 = 5

# 服从
# thief/necro/0232c151ef3731c2dede51931a374723
# ddc49e9ad1ff72a00b53c6cff5b1e920/0232c151ef3731c2dede51931a374723
class Skill23(ActiveSkill):
    """
    改变尼古拉斯的战斗模式。\n
    尼古拉斯的战斗模式有近战模式 (右) 、 远程模式 (左) 以及守护模式 (上) ； 施放技能后， 可以利用方向键改变。\n
    - [近战模式] -\n
    以近身攻击为主。新增[蜘蛛斩]技能。\n
    - [远程模式] -\n
    以远程攻击为主。该模式下， 可以大幅增加尼古拉斯的蜘蛛团攻击力和艾克洛索攻击力。\n
    - [守护模式] -\n
    停止攻击行为， 环绕在黑夜术士周围， 增加黑夜术士的防御力。\n
    在决斗场中， 守护模式下的尼古拉斯适用霸体状态。
    """
    name = "服从"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 1 #TODO
    rangeLv = 5
    cd = 1
    mp = [10, 100]
    uuid = "0232c151ef3731c2dede51931a374723"
    hasVP = False
    hasUP = False

    # [近战模式]
    # [蜘蛛斩]攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [远程模式]
    # 蜘蛛团攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 艾克洛索攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [守护模式]
    # 黑夜术士物理防御力增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 黑夜术士魔法防御力增加 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)

    associate = [{"data":data1,"skills":["降临 : 尼古拉斯"]}]


# 毁灭之爪
# thief/necro/27bade584bb42fef68148d3a0b72bace
# ddc49e9ad1ff72a00b53c6cff5b1e920/27bade584bb42fef68148d3a0b72bace
class Skill25(ActiveSkill):
    """
    用毁灭之爪攻击敌人。
    """
    name = "毁灭之爪"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 7
    mp = [24, 259]
    uuid = "27bade584bb42fef68148d3a0b72bace"
    hasVP = False
    hasUP = True

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 范围增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 暗黑仪式
# thief/necro/92360eab6e1f378902018eca681ac629
# ddc49e9ad1ff72a00b53c6cff5b1e920/92360eab6e1f378902018eca681ac629
class Skill26(ActiveSkill):
    """
    增加黑夜术士的技能攻击力。
    """
    name = "暗黑仪式"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 6 #TODO
    rangeLv = 3
    cd = 5
    uuid = "92360eab6e1f378902018eca681ac629"
    hasVP = False
    hasUP = False

    # 技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 暗影蛛丝阵
# thief/necro/1803b6a67047cafb9e289b4f33cc507b
# ddc49e9ad1ff72a00b53c6cff5b1e920/1803b6a67047cafb9e289b4f33cc507b
class Skill27(ActiveSkill):
    """
    命令尼古拉斯展开蛛丝阵。\n
    蛛丝阵对范围内的敌人造成伤害。\n
    施放技能时， 大幅增加尼古拉斯的暗属性抗性， 且进入蛛丝阵内的敌人会把尼古拉斯作为优先目标。\n
    若施放技能时按住技能键， 尼古拉斯会瞬移到死灵术士前方展开蛛丝阵。
    """
    name = "暗影蛛丝阵"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 20
    mp = [95, 952]
    uuid = "1803b6a67047cafb9e289b4f33cc507b"
    hasVP = False
    hasUP = True

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 19
    # 多段攻击间隔 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 蛛丝阵范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 黑暗之环
# thief/necro/c4a5b868f1e8e60cd1867a2cfab4a242
# ddc49e9ad1ff72a00b53c6cff5b1e920/c4a5b868f1e8e60cd1867a2cfab4a242
class Skill28(PassiveSkill):
    """
    黑暗之环是隶属元老院的黑夜术士的身份证明， 对使用黑咒术有很大帮助。\n
    学习后， 增加属性攻击力。
    """
    name = "黑暗之环"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 4 #TODO
    rangeLv = 2
    uuid = "c4a5b868f1e8e60cd1867a2cfab4a242"
    hasVP = False
    hasUP = False

    # 属性攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]

# 百鬼夜行
# thief/necro/04883563896fe1adac7505c6146b5f59
# ddc49e9ad1ff72a00b53c6cff5b1e920/04883563896fe1adac7505c6146b5f59
class Skill29(ActiveSkill):
    """
    向前方地面投掷夜游魂。\n
    夜游魂落地后， 若再次输入技能指令， 则夜游魂周围的百鬼之灵立即攻击周围的敌人。\n
    夜游魂落地后， 经过一定时间或黑夜术士死亡， 百鬼之灵会自动出现。\n
     在决斗场中， 夜游魂落地瞬间就会出现百鬼之灵。
    """
    name = "百鬼夜行"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 12
    mp = [65, 699]
    uuid = "04883563896fe1adac7505c6146b5f59"
    hasVP = False
    hasUP = True

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 24
    # 持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 多段攻击间隔 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 自动发动时， 攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 对诅咒状态下敌人的攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 攻击范围增加率 {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    mode = ["自爆","引爆"]

    def setMode(self, mode):
        if mode == "自爆":
            self.skillRation *= 1.2

# 复苏者之怨
# thief/necro/c27418ae613c647527200a7ca17d97fd
# ddc49e9ad1ff72a00b53c6cff5b1e920/c27418ae613c647527200a7ca17d97fd
class Skill30(ActiveSkill):
    """
    向前方地面召唤复苏者， 并使复苏者范围内的敌人在一定时间内受到持续伤害。\n
    敌人受到伤害时， 有一定的几率进入减速和减少跳跃力的减益状态。
    """
    name = "复苏者之怨"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 10
    mp = [32, 336]
    uuid = "c27418ae613c647527200a7ca17d97fd"
    hasVP = False
    hasUP = True

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 13
    # 持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击次数上限 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 减速几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 减速持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 移动速度减少率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 攻击速度减少率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 跳跃力减少率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [范围信息]
    # 攻击范围扩大率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

# 黑魔法书 : 亡者之魂
# thief/necro/0e409ac3e1c1f3976b3ef2bfe4c13069
# ddc49e9ad1ff72a00b53c6cff5b1e920/0e409ac3e1c1f3976b3ef2bfe4c13069
class Skill31(PassiveSkill):
    """
    记载黑魔法知识的书， 增加除[降临 : 尼古拉斯]外的技能攻击力， 并增加[复苏者之缚]的复苏者区域范围。
    """
    name = "黑魔法书 : 亡者之魂"
    learnLv = 30
    masterLv = 1
    maxLv = 10
    position = 4 #TODO
    rangeLv = 5
    uuid = "0e409ac3e1c1f3976b3ef2bfe4c13069"
    hasVP = False
    hasUP = False

    # 技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [复苏者之缚]范围增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [{"data":data0,"exceptSkills":["降临 : 尼古拉斯"]},]

# 降临 : 暴君巴拉克
# thief/necro/dcd536f1674630f01fc9667bb202b851
# ddc49e9ad1ff72a00b53c6cff5b1e920/dcd536f1674630f01fc9667bb202b851
class Skill32(ActiveSkill):
    """
    召唤暴君巴拉克， 使其依附在黑夜术士的身上。\n
    [暴君巴拉克降临状态下]\n
    - 基本攻击变更。\n
    - 跳跃攻击时， 巴拉克巨大的手碾压敌人。\n
    - 可以施放[暗击拳]、 [巴拉克强击]、 [狂野乱舞]、 [巴拉克的野心]、 [千魂祭]、 [巴拉克的愤怒]、 [暴君湮灭斩]、 [亡者君临 : 巴拉克之戮]。\n
    - 施放[暗魂波]时可以蓄力后发射， 并且增加攻击力。\n
    - 增加物理防御力、 魔法防御力和暗属性抗性， 但会降低光属性抗性。
    """
    name = "降临 : 暴君巴拉克"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cd = 5
    mp = [338, 3702]
    uuid = "dcd536f1674630f01fc9667bb202b851"
    hasVP = True
    hasUP = False
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # [巴拉克基本攻击]
    # 基本攻击第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 基本攻击第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 基本攻击第3击攻击力 : {value2}% x {value3}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 5
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 基本攻击第4击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # 跳跃攻击攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [暗击拳]
    # 暗击拳攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 暗击拳爆炸攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [狂野乱舞]
    # 狂野乱舞挥剑攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [巴拉克强击]
    # 强击攻击力 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [防御力和抗性]
    # 物理防御力增加量 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 魔法防御力增加量 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 暗属性抗性增加量 : {value12}
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 光属性抗性减少量 : {value13}
    data13 = get_data(f'{prefix}/{uuid}', 13)

    mode = ["x4","x3"]

    def setMode(self, mode):
        if mode == "x4":
            self.hit4 = 1
        elif mode == "x3":
            self.hit4 = 0

    def vp_1(self):
        """
        [狂野乱舞]\n
        施放[狂野乱舞]时， 投掷带有暴君怒意的剑\n
        - 投掷出的剑旋转着造成5次伤害
        """
        ...

    def vp_2(self):
        """
        [降临 : 暴君巴拉克]\n
        巴拉克部分动作变更\n
        - 删除基本攻击第4击\n
        - 可以强制中断[百鬼夜行]、 [复苏者之缚]、 [怨噬之沼]、 [亡者之茧]的施放后僵直， 施放巴拉克的基本攻击\n
        [暗击拳]\n
        施放时， 巴拉克固定在该位置， 再次施放或施放觉醒技能时， 回到黑夜术士的位置\n
        [巴拉克强击]\n
        可在普通状态下施放
        """
        self.setMode("x3")
        ...

    associate = [
        {"type":"+power0","data":data6,"skills":["暗击拳"],"ratio":1},
        {"type":"+power1","data":data7,"skills":["暗击拳"],"ratio":1},
        {"type":"+power0","data":data8,"skills":["狂野乱舞"],"ratio":1},
        {"type":"+power0","data":data9,"skills":["巴拉克强击"],"ratio":1}
        ]

# 暗击拳
# thief/necro/1c1a9606eb702ebe5a7bb4397f3aeae0
# ddc49e9ad1ff72a00b53c6cff5b1e920/1c1a9606eb702ebe5a7bb4397f3aeae0
class Skill33(ActiveSkill):
    """
    巴拉克用拳头进行抓取攻击， 对敌人造成伤害。\n
    只能在前冲时施放。 
    """
    name = "暗击拳"
    learnLv = 35
    masterLv = 1
    maxLv = 1
    position = 8 #TODO
    rangeLv = 2
    cd = 3
    uuid = "1c1a9606eb702ebe5a7bb4397f3aeae0"
    hasVP = False
    hasUP = False

    # [暗击拳]的攻击力适用[降临：暴君巴拉克]中的数值。 
    data0 = [0,1]
    power0 = 0
    hit0 = 1

    data1= [0,1]
    power1 = 0
    hit1 = 1


# 狂野乱舞
# thief/necro/56aa7844a2da23f5bea9b585aea5ae45
# ddc49e9ad1ff72a00b53c6cff5b1e920/56aa7844a2da23f5bea9b585aea5ae45
class Skill34(ActiveSkill):
    """
    巴拉克向前方移动， 挥剑攻击。 命中时将敌人向后击退。
    """
    name = "狂野乱舞"
    learnLv = 35
    masterLv = 1
    maxLv = 1
    position = 9 #TODO
    rangeLv = 2
    cd = 7
    uuid = "56aa7844a2da23f5bea9b585aea5ae45"
    hasVP = False
    hasUP = False

    # [狂野乱舞]的攻击力适用[降临：暴君巴拉克]中的数值。
    data0 = [0,1]
    power0 = 0
    hit0 = 1

# 巴拉克强击
# thief/necro/68062215e75d92575958873ac8ede31a
# ddc49e9ad1ff72a00b53c6cff5b1e920/68062215e75d92575958873ac8ede31a
class Skill35(ActiveSkill):
    """
    巴拉克连接特定的行动， 用剑碾压敌人。
    """
    name = "巴拉克强击"
    learnLv = 35
    masterLv = 1
    maxLv = 1
    position = 10 #TODO
    rangeLv = 2
    cd = 2
    uuid = "68062215e75d92575958873ac8ede31a"
    hasVP = False
    hasUP = False

    # [巴拉克强击]的攻击力适用[降临：暴君巴拉克]中的数值。
    data0 = [0,1]
    power0 = 0
    hit0 = 1

# 巴拉克的野心
# thief/necro/23a5e0fba03283cb1b324a847b3fe370
# ddc49e9ad1ff72a00b53c6cff5b1e920/23a5e0fba03283cb1b324a847b3fe370
class Skill36(ActiveSkill):
    """
    施放技能后， 前方地面上出现手掌形状的邪恶气息， 此气息会攻击敌人并对敌人产生吸附效果。\n
    若再次输入技能指令， 则手掌气息会变成握拳气息攻击敌人。\n
    只有在召唤巴拉克的状态下， 才能使用该技能。
    """
    name = "巴拉克的野心"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [165, 1393]
    uuid = "23a5e0fba03283cb1b324a847b3fe370"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 攻击范围扩大率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [巴拉克的野心]\n
        可在除巴拉克系列技能外的其他动作中施放\n
        删除第1击\n
        总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [巴拉克的野心]\n
        巴拉克抬手间生成怨恨漩涡\n
        - 怨恨漩涡会吸附周围的敌人\n
        - 多段攻击伤害\n
        - 攻击范围 +30%\n
        - 基本冷却时间变更为50秒\n
        - 攻击力 +100%
        """
        self.cd = 50
        self.skillRation *= 1 + 1
        ...

# 吸影暗劲波
# thief/necro/d2c6df5105577fb59fb92529a36165a0
# ddc49e9ad1ff72a00b53c6cff5b1e920/d2c6df5105577fb59fb92529a36165a0
class Skill37(ActiveSkill):
    """
    命令尼古拉斯施放吸影暗劲波。\n
    尼古拉斯施放吸影暗劲波时， 会向周围敌人放出吸影线， 给予敌人暗属性伤害。\n
    吸影结束时， 被吸影线缠住的敌人会受到暗属性爆炸伤害。\n
    施放吸影暗劲波时， 若按住技能指令， 则尼古拉斯将瞬移到黑夜术士的前方施放吸影暗劲波。 (在决斗场中， 恢复尼古拉斯的生命值， 不发动瞬移效果， 且无法攻击倒地状态的敌人)
    """
    name = "吸影暗劲波"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cube = 1
    cd = 35
    mp = [164, 1376]
    uuid = "d2c6df5105577fb59fb92529a36165a0"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 抓取攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2
    # 爆炸魔法攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 最高抓取数量 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 每抓取1个敌人可恢复的生命值量 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [吸影暗劲波]\n
        命中时， 黑夜术士进入无敌状态\n
        - 吸影结束时， 恢复黑夜术士9%的生命值
        """
        ...

    def vp_2(self):
        """
        [吸影暗劲波]\n
        尼古拉斯召唤自己的分身来施放\n
        - 分身追踪黑夜术士前方的敌人\n
        - 若尼古拉斯不存在， 则重新召唤\n
        - 删除追加操作功能
        """
        ...

# 巴拉克的盟约
# thief/necro/31823197cc0b04d4c5dcf8f928d9220c
# ddc49e9ad1ff72a00b53c6cff5b1e920/31823197cc0b04d4c5dcf8f928d9220c
class Skill38(PassiveSkill):
    """
    与巴拉克签订盟约， 增加技能攻击力。\n
    学习[巴拉克的盟约]后， 施放[巴拉克的野心]和[巴拉克的愤怒]时， 立即发动追加攻击。
    """
    name = "巴拉克的盟约"
    learnLv = 40
    masterLv = 1
    maxLv = 10
    position = 6 #TODO
    rangeLv = 3
    uuid = "31823197cc0b04d4c5dcf8f928d9220c"
    hasVP = False
    hasUP = False

    # 技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]

# 巴拉克的愤怒
# thief/necro/0ed3148658fe37b3336ccb718dc0fdb0
# ddc49e9ad1ff72a00b53c6cff5b1e920/0ed3148658fe37b3336ccb718dc0fdb0
class Skill39(ActiveSkill):
    """
    发动后， 巴拉克会用手抓向地面并攻击敌人， 使敌人进入僵直状态， 最后用巨大的刀斩击敌人。 施放技能时， 再次按技能键可以立即施放斩击攻击。\n
    只有在召唤巴拉克的状态下， 才能使用该技能。\n
    使用该技能时， 无法强制中断当前进行的普通攻击动作。
    """
    name = "巴拉克的愤怒"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [380, 3192]
    uuid = "0ed3148658fe37b3336ccb718dc0fdb0"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第1击冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 抓地多段攻击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 4
    # 第2击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 第2击冲击波攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # [范围信息]
    # 攻击范围扩大率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [巴拉克的愤怒]\n
        仅发动用手抓向地面的动作\n
        吸附被抓地攻击命中的敌人\n
        总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [巴拉克的愤怒]\n
        仅发动下劈攻击\n
        - 下劈范围 +25%\n
        总攻击力相同
        """
        ...

# 降临 : 莱迪娅
# thief/necro/f4a561e272cc434a4905b3aa0c0de090
# ddc49e9ad1ff72a00b53c6cff5b1e920/f4a561e272cc434a4905b3aa0c0de090
class Skill40(ActiveSkill):
    """
    召唤莱迪娅。 莱迪娅被召唤出来后， 会在原地悲痛嚎叫。 悲痛嚎叫会给敌人造成暗属性的多段魔法伤害。\n
    按住技能键时， 攻击力会增加， 并施放不贯穿的悲痛嚎叫。\n
    其他技能施放过程中， 可以无施放动作立即施放该技能。\n
    无法在决斗场使用。
    """
    name = "降临 : 莱迪娅"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [380, 3192]
    uuid = "f4a561e272cc434a4905b3aa0c0de090"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 悲痛嚎叫攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 30
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 追加操作时攻击力 : {value2}% X {value3}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 发射距离 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)

    mode = ["长按","普通"]

    def setMode(self, mode):
        if mode == "长按":
            self.hit0 = 0
            self.hit2 = 30
        elif mode == "普通":
            self.hit0 = 30
            self.hit2 = 0

    def vp_1(self):
        """
        [降临 : 莱迪娅]\n
        莱迪娅爆炸\n
        - 未命中时冷却时间缩短为 : 5秒\n
        总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [降临 : 莱迪娅]\n
        莱迪娅展开亵渎之地\n
        - 对范围内敌人造成伤害\n
        - 删除长按技能键功能\n
        - 始终适用长按操作攻击力\n
        - 对受到伤害的敌人施加亵渎的诅咒\n
        [亵渎的诅咒]\n
        - 附加所有诅咒效果\n
        总攻击力相同
        """
        self.setMode("长按")
        ...

# 无形之惧
# thief/necro/202edb928046f4fa6dedf6337377efd5
# ddc49e9ad1ff72a00b53c6cff5b1e920/202edb928046f4fa6dedf6337377efd5
class Skill41(PassiveSkill):
    """
    巴拉克降临时， 使灵魂收割者周围的敌人进入恐惧状态， 恐惧状态下的敌人受到的暴击伤害大幅增加。 掌握技能后， 由于暴君之力的影响， 增加灵魂收割者的暴击率。
    """
    name = "无形之惧"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 3
    uuid = "202edb928046f4fa6dedf6337377efd5"
    hasVP = False
    hasUP = False

    # 恐惧状态诱发范围 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 恐惧持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 暴击率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 暴击伤害增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    associate = [{"data":data2}]

# 千魂祭
# thief/necro/2a3c96b88d02372505692da0a8b54743
# ddc49e9ad1ff72a00b53c6cff5b1e920/2a3c96b88d02372505692da0a8b54743
class Skill42(ActiveSkill):
    """
    在巴拉克周围的敌人身上刻上战印， 并把刻上战印的敌人作为祭品召唤出复苏者军队攻击敌人。\n
    施放技能后， 强化尼古拉斯和巴拉克， 效果持续一定时间。\n
    只有在召唤巴拉克的状态下， 才能使用该技能。
    """
    name = "千魂祭"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [881, 7403]
    uuid = "2a3c96b88d02372505692da0a8b54743"
    hasVP = False
    hasUP = False

    # 战印的范围 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 漩涡持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 漩涡攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 9
    # 漩涡多段攻击间隔 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 复苏者军团攻击持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 复苏者军团攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 13
    # 复苏者军团多段攻击间隔 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 最后爆炸攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    hit7 = 1
    # 增加[降临 ： 尼古拉斯]技能等级 : {value8}级
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [降临 ： 尼古拉斯]等级增加效果的持续时间 : {value9}秒
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 增加[降临 ： 暴君巴拉克]技能等级 : {value10}级
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # [降临 ： 暴君巴拉克]等级增加效果的持续时间 : {value11}秒
    data11 = get_data(f'{prefix}/{uuid}', 11)

# 复苏者之缚
# thief/necro/b3659936a9a74c4ed6f7faf07cca1f9e
# ddc49e9ad1ff72a00b53c6cff5b1e920/b3659936a9a74c4ed6f7faf07cca1f9e
class Skill43(ActiveSkill):
    """
    向前方地面召唤复苏者， 使复苏者范围内的敌人在一定时间内受到持续伤害， 并进入束缚状态。\n
    只有在召唤范围内， 敌人才会进入束缚状态； 脱离范围或召唤结束时， 束缚状态将解除。
    """
    name = "复苏者之缚"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 2
    cube = 2
    cd = 30
    mp = [400, 1120]
    uuid = "b3659936a9a74c4ed6f7faf07cca1f9e"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 20
    # 束缚几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 多段攻击间隔 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 召唤持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 攻击范围扩大率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [复苏者之缚]\n
        召唤亡者漩涡\n
        - 删除束缚效果\n
        - 将敌人吸附至漩涡中心\n
        总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [复苏者之缚]\n
        对[复苏者之缚]范围内的敌人赋予恶毒诅咒\n
        [恶毒诅咒]\n
        - 持续时间内附着在敌人身上造成伤害\n
        - 赋予所有诅咒效果
        """
        ...

# 怨噬之沼
# thief/necro/e36ae35f8964d92e30e33529a65544d7
# ddc49e9ad1ff72a00b53c6cff5b1e920/e36ae35f8964d92e30e33529a65544d7
class Skill44(ActiveSkill):
    """
    召唤亡者的怨念。\n
    怨念配合黑夜术士的动作攻击前方敌人， 并在地面凝聚成怨噬之沼， 跟随黑夜术士。\n
    再次按技能键， 怨噬之沼再次向前方发动攻击， 最多可以发动3次。
    """
    name = "怨噬之沼"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 2
    cube = 1
    cd = 50
    mp = [800, 1680]
    uuid = "e36ae35f8964d92e30e33529a65544d7"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第2击攻击力 : {value1}% X {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 3
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 第3击喷涌攻击力 : {value3}% X {value4}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 3
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 第3击撕咬攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # 怨噬之沼持续时间 : 20秒
    # [范围信息]
    # 攻击范围扩大率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [怨噬之沼]\n
        可以在[巴拉克的野心]、 [巴拉克的愤怒]、 [暴君湮灭斩]施放过程中使用\n
        可以取消施放后僵直并立即施放黑夜术士系列技能
        """
        ...

    def vp_2(self):
        """
        [怨噬之沼]\n
        仅发动最后一击\n
        - 攻击范围 +50%\n
        总攻击力相同
        """
        ...

# 暗黑蛛丝引
# thief/necro/dac8d8207618150c162e4c6f9e168527
# ddc49e9ad1ff72a00b53c6cff5b1e920/dac8d8207618150c162e4c6f9e168527
class Skill45(ActiveSkill):
    """
    尼古拉斯张开暗影蛛丝， 将敌人牵引至身边。\n
    被牵引的敌人将在一段时间内无法移动。\n
    对于无法抓取和固定的敌人， 无法牵引到自己身边。\n
    施放暗黑蛛丝引时， 若按住技能键， 则尼古拉斯将瞬移到黑夜术士的前方施放暗黑蛛丝引。
    """
    name = "暗黑蛛丝引"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 2 #TODO
    rangeLv = 2
    cube = 3
    cd = 20
    mp = [580, 4500]
    uuid = "dac8d8207618150c162e4c6f9e168527"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 张开蛛丝攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 收回蛛丝攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 束缚蛛丝攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 6
    # 束缚蛛丝持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 攻击范围扩大率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [暗黑蛛丝引]\n
        尼古拉斯召唤自己的妹妹安吉丽娜\n
        - 安吉丽娜生成蜘蛛丝， 强制控制触碰蜘蛛丝的敌人3秒， 并造成持续伤害\n
        - 攻击范围 +50%\n
        总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [暗黑蛛丝引]\n
        尼古拉斯召唤出自己的分身， 代替自己施放技能\n
        - 施放时立即初始化[降临 : 莱迪娅]的冷却时间\n
        - [降临 : 莱迪娅]攻击力 -56%
        """
        ...

    def effect(self, old, new):
        if self.vp == 2:
            self.associate = [{"data":[0]+[-50]*self.maxLv,"skills":["降临 : 莱迪娅"]}]
        return super().effect(old, new)

# 亡魂之息
# thief/necro/78b86e64fbb74c1db1b71c50a5ac21cd
# ddc49e9ad1ff72a00b53c6cff5b1e920/78b86e64fbb74c1db1b71c50a5ac21cd
class Skill46(PassiveSkill):
    """
    学习后， 增加黑夜术士的所有攻击力。\n
    [暗魂波]、 [诅咒之箭]适用单独的攻击力增加量。
    """
    name = "亡魂之息"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 3
    uuid = "78b86e64fbb74c1db1b71c50a5ac21cd"
    hasVP = False
    hasUP = False

    # [暗魂波]、 [诅咒之箭]以外的所有攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [暗魂波]、 [诅咒之箭]攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    associate = [
        {"data":data0,"exceptSkills":["暗魂波","诅咒之箭"]},
        {"data":data1,"skills":["暗魂波","诅咒之箭"]}
    ]

# 暴君湮灭斩
# thief/necro/8e358ecf99ac9df31a6132aeafe378a9
# ddc49e9ad1ff72a00b53c6cff5b1e920/8e358ecf99ac9df31a6132aeafe378a9
class Skill47(ActiveSkill):
    """
    巴拉克召唤出具象化的天罚之剑， 横扫前方敌人。\n
    只能在巴拉克降临的状态下施放， 并且被[暴君湮灭斩]命中的敌人有一定几率陷入[无形之惧]。
    """
    name = "暴君湮灭斩"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "8e358ecf99ac9df31a6132aeafe378a9"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 天罚之剑攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [无形之惧]触发几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 攻击范围扩大率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [暴君湮灭斩]\n
        除巴拉克系列技能外的所有技能都具有以下效果\n
        - [暴君湮灭斩]施放过程中可强制中断\n
        - 施放过程中可施放[暴君湮灭斩]
        """
        ...

    def vp_2(self):
        """
        [暴君湮灭斩]\n
        巴拉克向前方突进并施放强力横斩\n
        - 施放技能时进入无敌状态
        """
        ...

# 亡者君临 : 巴拉克之戮
# thief/necro/4c5271b0ecce120d7fc113f377fae76f
# ddc49e9ad1ff72a00b53c6cff5b1e920/4c5271b0ecce120d7fc113f377fae76f
class Skill48(ActiveSkill):
    """
    巴拉克寻回本然之力， 现身于真实之中。\n
    现身的巴拉克会制造出一个黑洞， 对敌人造成伤害的同时， 将敌人拉向自己。\n
    巴拉克彻底具象化后， 会粉碎黑洞， 引发剧烈的爆炸。\n
    对无法抓取的敌人不适用控制效果。\n
    巴拉克登场后， 敌人会感受到[无形之惧]。
    """
    name = "亡者君临 : 巴拉克之戮"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [1500, 5000]
    uuid = "4c5271b0ecce120d7fc113f377fae76f"
    hasVP = False
    hasUP = False

    # 巴拉克登场攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 黑洞多段攻击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 11
    # 毁灭抓取攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

# 冥河之钥
# thief/necro/96e72ec364dada85600c907ecd95a140
# ddc49e9ad1ff72a00b53c6cff5b1e920/96e72ec364dada85600c907ecd95a140
class Skill49(PassiveSkill):
    """
    学习后， 进入地下城时自动施放[降临 : 暴君巴拉克]， 增加基本攻击力和转职技能攻击力， 且部分技能附加特殊效果。\n
    [暗魂波] : 删除蓄气操作但保留蓄气时攻击力增加效果， 召唤附着在敌人身上并持续造成伤害的灵魂。\n
    [驱使枯灵] : 由黑夜术士直接召唤。
    """
    name = "冥河之钥"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "96e72ec364dada85600c907ecd95a140"
    hasVP = False
    hasUP = False

    # 基本攻击和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data":data0}]

# 亡者之茧
# thief/necro/b1ccbd90d0b40f543ece3b18fcef827f
# ddc49e9ad1ff72a00b53c6cff5b1e920/b1ccbd90d0b40f543ece3b18fcef827f
class Skill50(ActiveSkill):
    """
    从不死世界召唤由怨念和腐肉构成的诅咒之茧。\n
    召唤时， 吸附周围的敌人后结茧； 使范围内所有敌人进入灵魂状态。\n
    黑夜术士的所有攻击都能对茧造成伤害， 茧每隔一段时间逐渐膨胀， 膨胀到最大后经过一段时间爆炸， 对敌人造成伤害。\n
    灵魂状态的敌人不会受到黑夜术士的攻击伤害， 但会共担茧所受到的伤害。\n
    再次按技能键时， 立即引发爆炸。\n
    对无法抓取的敌人不适用控制效果。
    """
    name = "亡者之茧"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [1066, 8000]
    uuid = "b1ccbd90d0b40f543ece3b18fcef827f"
    hasVP = False
    hasUP = False

    # 持续时间上限 : 7秒
    # 结茧多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 终结爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

# 命运殇痕·摩罗斯之咒
# thief/necro/394e2f09c1f37ae61d831d8567707170
# ddc49e9ad1ff72a00b53c6cff5b1e920/394e2f09c1f37ae61d831d8567707170
class Skill51(ActiveSkill):
    """
    召唤摩罗斯。\n
    巴拉克和尼古拉斯仓惶退下。\n
    摩罗斯以黑夜术士为媒介， 向敌人散布恐怖之力。\n
    结束后， 退下的尼古拉斯和巴拉克回归。\n
    解除召唤后， [降临 : 暴君巴拉克]的防御力和抗性效果维持不变。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
     若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "命运殇痕·摩罗斯之咒"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4027, 12888]
    uuid = "394e2f09c1f37ae61d831d8567707170"
    hasVP = False
    hasUP = False

    # 恐怖之力攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'necro'
        self.nameCN = '隐夜·死灵术士'
        self.role = 'thief'
        self.角色 = '暗夜使者'
        self.职业 = '死灵术士'
        self.jobId = 'ddc49e9ad1ff72a00b53c6cff5b1e920'
        self.jobGrowId = '618326026de1a1f1cfba5dbd0b8396e7'

        self.武器选项 = ['匕首', '双剑', '手杖']
        self.输出类型选项 = ["魔法百分比"] # TODO
        self.输出类型 = '魔法百分比' # TODO
        self.防具精通属性 = ['智力'] # TODO
        self.防具类型 = '轻甲'
        self.buff = 2.225

        super().__init__(equVersion, __name__)
