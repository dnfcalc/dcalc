#b9cb48777665de22c006fabaf9a560b3
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "archer/hunter/cn/skillDetail"

class HunterActiveSkill(ActiveSkill):

    normalRation = 0
    markRation = 0
    # 标记消耗，大于0为消耗，小于0为生成
    def getSkillData(self, lv: int = 0):
        res = 0
        keys = [key.replace('data', '') for key in dir(self) if key.startswith('data') and not key.startswith('dataplus')]
        for i in keys:
            data = getattr(self, f'data{i}', [])
            plus = getattr(self, f'plus{i}', 0)
            hit = getattr(self, f'hit{i}', 0)
            if len(data) == 0 or hit == 0:
                continue
            if lv < len(data):
                hit = getattr(self, f'hit{i}', 0)
                power = getattr(self, f'power{i}', 1)
                cost = getattr(self, f'cost{i}', 0)
                res += hit * power * (data[lv] + plus) * ((1 + self.normalRation) if cost <= 0 else (1 + self.markRation * cost))
        keys = [key.replace('dataplus', '') for key in dir(self) if key.startswith('dataplus')]
        for i in keys:
            data = getattr(self, f'dataplus{i}', 0)
            hit = getattr(self, f'hitplus{i}', 1)
            power = getattr(self, f'powerplus{i}', 1)
            res += hit * power * data
        return res

# 凌跃一击
# archer/hunter/0969cd4054d93da07708108c0cc1c4b5
# b9cb48777665de22c006fabaf9a560b3/0969cd4054d93da07708108c0cc1c4b5
class Skill0(HunterActiveSkill):
    """
        该技能可在地面和空中施放。\n
        向后微微跃起， 并根据武器的不同， 向地面发射不同的投射物， 使敌人浮空。\n
        攻击时， 有霸体判定； 转职为缪斯或奇美拉后， 技能类型变为独立攻击力。
    """
    name = "凌跃一击"
    learnLv = 1
    masterLv = 10
    maxLv = 20
    position = 4 #TODO
    rangeLv = 3
    cd = 2
    uuid = "0969cd4054d93da07708108c0cc1c4b5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 箭矢攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 冲击波浮空力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [转职为缪斯后]
    # 棱镜攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 冲击波攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [转职为妖护使后]
    # 妖兽上勾拳攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [转职为奇美拉后]
    # 箭矢攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 冲击波攻击力 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)

# 狩猎之瞳
# archer/hunter/8510294202d0e042dd29a2422fc6770d
# b9cb48777665de22c006fabaf9a560b3/8510294202d0e042dd29a2422fc6770d
class Skill1(PassiveSkill):
    """
        呼唤在上方侦察的神兽帕伊卡来到身边。\n
        掌控广阔视野的帕伊卡将敌人位置告知猎人。\n
        学习后， 可使用“帕伊卡”和“联合作战”系列技能。\n
    [帕伊卡！ 过来， 这里！]
    """
    name = "狩猎之瞳"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 2 #TODO
    rangeLv = 3
    uuid = "8510294202d0e042dd29a2422fc6770d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 定位敌人范围 : 左右{value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 最大可定位敌人数量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 强攻弩掌握
# archer/hunter/b3659936a9a74c4ed6f7faf07cca1f9e
# b9cb48777665de22c006fabaf9a560b3/b3659936a9a74c4ed6f7faf07cca1f9e
class Skill2(PassiveSkill):
    """
        可穿戴强攻弩系列武器。\n
        减少除觉醒技能外转职技能的冷却时间。\n
        猎人无法穿戴除强攻弩之外的武器。\n
    [虽然不知道是谁制作的， 但做工很棒， 对吧帕伊卡？]
    """
    name = "强攻弩掌握"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 3 #TODO
    rangeLv = 3
    uuid = "b3659936a9a74c4ed6f7faf07cca1f9e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 转职技能冷却时间减少 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

    associate = [ {"data":data0,"type":"*cdReduce", 'exceptSkills': ['联合作战：围猎', '完美瞄准', '联合作战：最终一役']} ]

# 帕伊卡 : 奇袭
# archer/hunter/38612d8f2561edc2eb68d5057a837bfa
# b9cb48777665de22c006fabaf9a560b3/38612d8f2561edc2eb68d5057a837bfa
class Skill3(HunterActiveSkill):
    """
        帕伊卡前冲一小段距离， 用身体撞击敌人后快速返回。\n
        被击中的敌人有一定几率进入眩晕状态。\n
        无论猎人当前处于什么状态都可施放该技能， 但无法和其他“帕伊卡”和“联合作战”系列技能同时使用。
    """
    name = "帕伊卡 : 奇袭"
    learnLv = 1
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cd = 5
    mp = [16, 91]
    uuid = "38612d8f2561edc2eb68d5057a837bfa"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 身体撞击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 眩晕几率 : 100%
    # 眩晕持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 冲击波范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 迅猛速射
# archer/hunter/6a1d1f08a6572be420bb3a256c44c015
# b9cb48777665de22c006fabaf9a560b3/6a1d1f08a6572be420bb3a256c44c015
class Skill4(HunterActiveSkill):
    """
        向前方快速发射多枚小型弩箭。 发射时按跳跃键可以提前结束技能。
    """
    name = "迅猛速射"
    learnLv = 1
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 5
    mp = [16, 91]
    uuid = "6a1d1f08a6572be420bb3a256c44c015"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 小型弩箭攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    cost0 = -5
    # 发射数量 : {value1}发
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 弩箭最大移动距离 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 基础精通
# archer/hunter/5a56514f35cf0270ae8d6c65f8fefd78
# b9cb48777665de22c006fabaf9a560b3/5a56514f35cf0270ae8d6c65f8fefd78
class Skill6(PassiveSkill):
    """
        增加基本攻击、 前冲攻击、 跳跃攻击、 [凌跃一击]技能的攻击力。\n
        决斗场中， 增益/减益技能、 被动技能的技能攻击力增加效果对[基础精通]无影响。
    """
    name = "基础精通"
    learnLv = 1
    masterLv = 115
    maxLv = 200
    position = 1 #TODO
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

    associate = [{"type":"*skillDamage","data":[i-100 if i>0 else 0 for i in data0],"skills":["急速扳机"]}]


# 全力挥击
# archer/hunter/4655101518604f874721b3cc249aae10
# b9cb48777665de22c006fabaf9a560b3/4655101518604f874721b3cc249aae10
class Skill9(HunterActiveSkill):
    """
        用力挥舞弓， 击打周围的敌人， 并向前推出。\n
    转职为猎人时， 再次按技能键会立即发射一枚爆炸箭矢， 造成额外伤害。\n
    转职为缪斯或奇美拉时， 技能类型变为独立攻击力。
    """
    name = "全力挥击"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 5
    mp = [28, 165]
    uuid = "4655101518604f874721b3cc249aae10"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 击打攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [转职为猎人后]
    # 爆炸箭矢攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit0 = 1
    # [范围信息]
    # 转职为猎人时， 爆炸箭矢射程 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 转职为猎人时， 爆炸箭矢爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 推进装置
# archer/hunter/a2d943797daca862a6f321aca6ac9bfa
# b9cb48777665de22c006fabaf9a560b3/a2d943797daca862a6f321aca6ac9bfa
class Skill10(HunterActiveSkill):
    """
        从特制的鞋子中喷射迷雾， 推进自身前冲一段距离。\n
        按方向键时， 可朝指定方向前进。 再次按技能键可连续追加前冲。\n
        可以强制中断其他技能的施放后僵直并立即施放[推进装置]， 也可以强制中断[推进装置]的施放后僵直并立即使用其他技能。\n
        在部分技能发动后的共同装填过程中也可使用， 这种情况下使用时没有冷却时间。 发动收割技能后， 技能冷却时间初始化。\n
        装填过程中可使用技能 : [引爆发射]、 [重型穿甲箭]、 [光爆箭]、 [三弓弩箭]、 [终结穿刺]、 [完美瞄准]
    """
    name = "推进装置"
    learnLv = 5
    masterLv = 1
    maxLv = 1
    position = 3 #TODO
    rangeLv = 2
    cd = 5
    mp = [19, 19]
    uuid = "a2d943797daca862a6f321aca6ac9bfa"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 单次移动距离 : 180px

# 引爆发射
# archer/hunter/c7bf7ccab413009640e65ca6f2f0263a
# b9cb48777665de22c006fabaf9a560b3/c7bf7ccab413009640e65ca6f2f0263a
class Skill11(HunterActiveSkill):
    """
        装填一枚爆炸型大型弩箭， 向前方发射。\n
        弩箭触碰敌人会发生爆炸， 并对周围敌人造成伤害。
    """
    name = "引爆发射"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 5
    mp = [33, 187]
    uuid = "c7bf7ccab413009640e65ca6f2f0263a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 弩箭爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    cost0 = 5
    # 学习[猎物识别]后， 标记层数最大消耗 : 5个
    # [范围信息]
    # 弩箭射程 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 弩箭爆炸范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 翻月翔击
# archer/hunter/c9664191611af31142e052dfaef84530
# b9cb48777665de22c006fabaf9a560b3/c9664191611af31142e052dfaef84530
class Skill12(HunterActiveSkill):
    """
        前冲并踢飞命中的敌人。\n
        踢击仅对一名敌人造成伤害， 冲击波可以对除该敌人外附近的敌人造成伤害。\n
        对无法抓取的敌人不适用控制效果。\n
        可以按方向键调整冲刺方向。\n
        转职为缪斯或奇美拉后， 技能类型变为独立攻击力。\n
        转职为旅人时， 可以强制中断踢击后的僵直并施放空中技能。\n
        转职为妖护使时， 可以在空中施放。
    """
    name = "翻月翔击"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 5
    mp = [35, 206]
    uuid = "c9664191611af31142e052dfaef84530"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 踢击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)


# 猎物识别
# archer/hunter/1b1cfab062e0768bcc889e33e1f30dbf
# b9cb48777665de22c006fabaf9a560b3/1b1cfab062e0768bcc889e33e1f30dbf
class Skill15(PassiveSkill):
    """
        在小型弩箭中注入特制迷雾。\n
        特制迷雾具有识别猎物的标记功能， 并且可以如同催化剂一样最大限度地提高大型弩箭的伤害。\n
        角色命中率增加。 一部分转职技能区分为标记/收割技能， 为攻击赋予标记/收割属性。\n
        每1次标记攻击会对被攻击的敌人赋予1层标记， 收割攻击会消耗敌人身上累积的标记层数， 造成更大的伤害。 标记达到最大层数时， 敌人的回避率会减少。 如果敌人从地图上消失一段时间， 则累积在敌人身上的标记层数将会初始化。\n
        此外， 除收割伤害外的基本攻击力和技能攻击力也会增加。\n
        标记/收割技能的攻击信息与收割攻击的标记层数消耗量可以在各技能信息中查看。 一个技能可能可以同时拥有标记和收割属性的攻击。\n
    [帕伊卡， 看到了吗？ 就是那个家伙。]
    """
    name = "猎物识别"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 2 #TODO
    rangeLv = 3
    uuid = "1b1cfab062e0768bcc889e33e1f30dbf"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 除收割技能外基本/技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 每1层标记的收割攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 命中率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最大标记层数时敌人回避率减少 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 单个敌人最大可标记层数 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)

    associate = [{"data":data0,"type":"+normalRation"},{"data":data1,"type":"+markRation"}]

# 帕伊卡 : 刃羽
# archer/hunter/c77a417c43de80c4ce32c1ed405d174a
# b9cb48777665de22c006fabaf9a560b3/c77a417c43de80c4ce32c1ed405d174a
class Skill16(HunterActiveSkill):
    """
        帕伊卡挥舞翅膀， 将翅膀辅助装置上的多枚弩箭发射到前方。\n
        无论猎人当前处于什么状态都可施放该技能， 但无法和其他“帕伊卡”和“联合作战”系列技能同时使用。
    """
    name = "帕伊卡 : 刃羽"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cd = 6
    mp = [65, 361]
    uuid = "c77a417c43de80c4ce32c1ed405d174a"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 弩箭多段攻击力 : {value0}% x{value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    cost0 = -5
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 炽热喷涌
# archer/hunter/ecc23c980ea71450c0ad0c3fd232f329
# b9cb48777665de22c006fabaf9a560b3/ecc23c980ea71450c0ad0c3fd232f329
class Skill17(HunterActiveSkill):
    """
    [标记技能]\n
        向后跳跃， 向地面发射内置多枚小型弩箭的榴弹型大型弩箭。\n
        大型弩箭插入地面后爆炸， 向四周射出多枚小型弩箭。\n
        可以在空中使用。
    """
    name = "炽热喷涌"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 6
    mp = [65, 361]
    uuid = "ecc23c980ea71450c0ad0c3fd232f329"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 榴弹爆炸多段攻击力(标记) : {value0}% x{value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    cost0 = -5
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 榴弹爆炸范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 急速扳机
# archer/hunter/0b8db1e10b3abbd24d38564e708675d5
# b9cb48777665de22c006fabaf9a560b3/0b8db1e10b3abbd24d38564e708675d5
class Skill18(HunterActiveSkill):
    """
        向前方快速发射一定数量的小型弩箭和爆炸型弩箭。\n
        技能受[基础精通]影响。
    """
    name = "急速扳机"
    learnLv = 20
    masterLv = 1
    maxLv = 1
    position = 4 #TODO
    rangeLv = 2
    cd = 4
    mp = [40, 40]
    uuid = "0b8db1e10b3abbd24d38564e708675d5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 小型弩箭攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    cost0 = -3
    # 小型弩箭发射数量 : {value1}发
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸型弩箭爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 小型弩箭射程 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 大型弩箭射程 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 大型弩箭爆炸范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 高压喷射
# archer/hunter/852f8ad797db4dca1405cb3e77198401
# b9cb48777665de22c006fabaf9a560b3/852f8ad797db4dca1405cb3e77198401
class Skill19(HunterActiveSkill):
    """
        使用强攻弩的炮口将近距离敌人挑起后， 喷射高压迷雾击飞敌人。\n
        对无法抓取的敌人不适用控制效果。\n
    [不管再怎么喜欢我……也别靠这么近嘛。]
    """
    name = "高压喷射"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 7
    mp = [81, 453]
    uuid = "852f8ad797db4dca1405cb3e77198401"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 挑起攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 喷射迷雾攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 喷射迷雾范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 暴击
# archer/hunter/fc1262c19f3d0477ee8eda47b8db8696
# b9cb48777665de22c006fabaf9a560b3/fc1262c19f3d0477ee8eda47b8db8696
class Skill20(PassiveSkill):
    """
        集中精神， 提升物理/魔法暴击率。
    """
    name = "暴击"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 5 #TODO
    rangeLv = 3
    uuid = "fc1262c19f3d0477ee8eda47b8db8696"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 物理/魔法暴击率增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

# 强攻弩精通
# archer/hunter/dcb31a63ef58954f44ff2070c42a9a98
# b9cb48777665de22c006fabaf9a560b3/dcb31a63ef58954f44ff2070c42a9a98
class Skill21(PassiveSkill):
    """
        对强攻弩的使用更加得心应手。\n
        增加物理攻击力。 穿戴强攻弩时， 增加攻击速度， 转职技能的魔法值消耗量减少。
    """
    name = "强攻弩精通"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 2 #TODO
    rangeLv = 3
    uuid = "dcb31a63ef58954f44ff2070c42a9a98"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 魔法值消耗量减少 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [{"type":"$*PAtkP","data":data0}]

# 重型穿甲箭
# archer/hunter/8572675ec6a1f50b6eff6a867376c2de
# b9cb48777665de22c006fabaf9a560b3/8572675ec6a1f50b6eff6a867376c2de
class Skill22(HunterActiveSkill):
    """
    [收割技能]\n
        装填一枚大型弩箭， 弩箭附带沉重而锐利的贯穿型箭头， 向前方发射。\n
        发射的弩箭贯穿所有敌人后飞走。
    """
    name = "重型穿甲箭"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 7
    mp = [77, 428]
    uuid = "8572675ec6a1f50b6eff6a867376c2de"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 贯穿型弩箭攻击力(收割) : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    cost0 = 5
    # 标记层数最大消耗 : 5个
    # [范围信息]
    # 弩箭射程 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 狩猎开始
# archer/hunter/4f2e001e9a19eb7bae50ad1840dfb329
# b9cb48777665de22c006fabaf9a560b3/4f2e001e9a19eb7bae50ad1840dfb329
class Skill23(HunterActiveSkill):
    """
        装上小型弩箭弹匣， 提起战意。\n
        增加基本攻击和转职技能的攻击力和移动速度。\n
    [帕伊卡！ 今天也去抓个大家伙吧！]
    """
    name = "狩猎开始"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 2 #TODO
    rangeLv = 3
    cd = 5
    uuid = "4f2e001e9a19eb7bae50ad1840dfb329"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和转职技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 移动速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 帕伊卡 : 迷惑之舞
# archer/hunter/b8f4966608e4ebb3cc80ba4eac3649bb
# b9cb48777665de22c006fabaf9a560b3/b8f4966608e4ebb3cc80ba4eac3649bb
class Skill24(HunterActiveSkill):
    """
        帕伊卡快速穿梭战场攻击敌人， 同时辅助装置喷射特制迷雾， 在战场上形成迷雾区域。\n
        迷雾区域内部的敌人会进入失明状态。\n
        无论猎人当前处于什么状态都可施放该技能， 但无法和其他“帕伊卡”和“联合作战”系列技能同时使用。
    """
    name = "帕伊卡 : 迷惑之舞"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cd = 8
    mp = [99, 550]
    uuid = "b8f4966608e4ebb3cc80ba4eac3649bb"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 高速移动攻击力 : {value0}% x{value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 6
    cost0 = -6
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 迷雾区域维持时间 : 1秒
    # 失明几率 : 100%
    # 失明持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [学习追猎者勋章后]
    # 混乱几率 : 100%
    # 混乱持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 霰弹之箭
# archer/hunter/d53301bb328baf12a3ae482cc6a565dd
# b9cb48777665de22c006fabaf9a560b3/d53301bb328baf12a3ae482cc6a565dd
class Skill25(HunterActiveSkill):
    """
    [标记技能]\n
        压缩迷雾后释放， 多发小型弩箭如同霰弹枪一样爆发射出。
    """
    name = "霰弹之箭"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 8
    mp = [99, 550]
    uuid = "d53301bb328baf12a3ae482cc6a565dd"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 霰弹枪多段攻击力(标记) : {value0}% x{value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    cost0 = -5
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 霰弹枪攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 二重助推
# archer/hunter/7e904ea3d2a9faa054604e55120a9268
# b9cb48777665de22c006fabaf9a560b3/7e904ea3d2a9faa054604e55120a9268
class Skill26(PassiveSkill):
    """
        在[重型穿甲箭]的贯穿型箭头上附加一个加速装置， 使其可以更快更强力地贯穿敌人。\n
        弩箭产生冲击波造成更大的打击范围， 弩箭的攻击力和飞行速度增加。
    """
    name = "二重助推"
    learnLv = 35
    masterLv = 1
    maxLv = 11
    position = 5 #TODO
    rangeLv = 3
    uuid = "7e904ea3d2a9faa054604e55120a9268"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # [重型穿甲箭]攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [重型穿甲箭]弩箭速度增加量 : 25%

    associate = [ {"type":"*skillDamage","data":data0,"skills":["重型穿甲箭"]}, ]


# 光爆箭
# archer/hunter/dbf8b30c7057032af0d68fcfa289fdae
# b9cb48777665de22c006fabaf9a560b3/dbf8b30c7057032af0d68fcfa289fdae
class Skill27(HunterActiveSkill):
    """
    [收割技能]\n
        装填可以短时间造成多次爆炸的爆炸型大型弩箭， 向前方发射。\n
        弩箭在接触敌人时爆炸。
    """
    name = "光爆箭"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [219, 1220]
    uuid = "dbf8b30c7057032af0d68fcfa289fdae"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 弩箭爆炸多段攻击力(收割) : {value0}% x{value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    cost0 = 5
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 标记层数最大消耗 : 5个
    # [范围信息]
    # 弩箭射程 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [光爆箭]\n
        即使发射的弩箭没有接触敌人， 在移动一段距离后也会爆炸\n
        爆炸范围 +20%\n
        爆炸攻击默认消耗2个标记层数\n
         - 不会增加消耗量上限
        """
        ...

    def vp_2(self):
        """
        [光爆箭]\n
        - 基本冷却时间变更为24秒\n
        总攻击力 +60%\n
        [霰弹之箭]连接施放[光爆箭]时， 删除装填动作\n
        施放时初始化[霰弹之箭]的冷却时间\n
        [霰弹之箭]\n
        攻击力 -20%
        """
        self.cd = 24
        self.skillRation *= 1.6

    def effect(self, old, new):
        if self.vp == 2:
            self.associate = [{"type":"*skillRation","data":[0] + [-20]*self.maxLv,"skills":["霰弹之箭"]}]
        return super().effect(old, new)

# 帕伊卡 : 困兽之网
# archer/hunter/5152480fdde81362575a488d4cec4af9
# b9cb48777665de22c006fabaf9a560b3/5152480fdde81362575a488d4cec4af9
class Skill28(HunterActiveSkill):
    """
        帕伊卡发射背部辅助装置上的罗网弹， 罗网弹呈抛物线下落， 在下落过程中爆炸并展开罗网。\n
        被罗网捕获的敌人会进入束缚状态， 并且罗网在地面保持展开状态一段时间。\n
        一段时间后或再次按技能键时， 罗网收束并聚拢敌人。\n
        无论猎人当前处于什么状态都可施放该技能， 但无法和其他“帕伊卡”和“联合作战”系列技能同时使用。\n
    [这种妖兽毒液肯定能让大多数敌人都无法动弹了！ 别担心， 帕伊卡！ 绝对跑不掉的……吧？]\n
    [？！！]
    """
    name = "帕伊卡 : 困兽之网"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [422, 2353]
    uuid = "5152480fdde81362575a488d4cec4af9"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 罗网攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 罗网展开后最大持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 束缚几率 : 100%
    # [范围信息]
    # 罗网大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [帕伊卡 : 困兽之网]\n
        罗网落在地面上的同时快速旋转并吸附敌人\n
         - 在持续时间内持续旋转\n
         - 删除追加按键功能\n
         - 罗网旋转多段攻击30次\n
         - 总攻击力相同\n
        罗网大小 +50%
        """
        ...

    def vp_2(self):
        """
        [帕伊卡 : 困兽之网]\n
        被罗网触碰到的敌人将进入束缚和强制控制状态\n
        变更为可填充2次的技能\n
         - 每次填充冷却时间 : 12.5秒\n
         - 单次攻击力 -50%
        """
        self.cd = 12.5
        self.skillRation *= 0.5

# 箭雨
# archer/hunter/2391a27457b5a8c6fa4b4670a91bdd11
# b9cb48777665de22c006fabaf9a560b3/2391a27457b5a8c6fa4b4670a91bdd11
class Skill29(HunterActiveSkill):
    """
    [标记技能]\n
        向天空发射装有大量小型弩箭的机械装置。 发射的装置会在到达一定高度时展开， 滞空一段时间后向地面如同下雨一样倾泻小型弩箭。
    """
    name = "箭雨"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [338, 1882]
    uuid = "2391a27457b5a8c6fa4b4670a91bdd11"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 小型弩箭多段攻击力(标记) : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 20
    cost0 = -20
    # 小型弩箭最大攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 装置持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [箭雨]\n
        改造为单发装置， 如同霰弹枪一样发射一次\n
         - 最大攻击次数 -75%\n
         - 总攻击力相同
        """
        self.cost0 = -5

    def vp_2(self):
        """
        [箭雨]\n
        施放时， 由帕伊卡发射装置\n
         - 无视猎人的当前状态， 可以直接发动\n
         - 无法与“帕伊卡”、 “联合作战”系列技能同时施放\n
        范围 +20%
        """
        ...

# 三弓弩箭
# archer/hunter/5892d1fa4462e561ac8f8d2c74892b0a
# b9cb48777665de22c006fabaf9a560b3/5892d1fa4462e561ac8f8d2c74892b0a
class Skill30(HunterActiveSkill):
    """
    [标记+收割技能]\n
        射出两发强化迷雾反应性的特制弩箭后， 发射强大的爆炸型弩箭。\n
        最后发射的爆炸型弩箭为收割属性， 首先发射的2发特制弩箭为标记属性， 增加最后一发爆炸型弩箭可消耗的标记层数限制。\n
        所有弩箭都会朝着前方一定范围内最强的敌人发射， 第二发特制弩箭和最后一发爆炸型弩箭都会优先瞄准之前的弩箭命中过的敌人。\n
        每发弩箭发射之间都可以自由行动一段时间， 如果在持续时间结束前不再发射下一发弩箭， 则技能会终止。
    """
    name = "三弓弩箭"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [585, 3262]
    uuid = "5892d1fa4462e561ac8f8d2c74892b0a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 第一发特制弩箭攻击力(标记) : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    cost0 = -1
    # 第二发特制弩箭攻击力(标记) : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    cost1 = -1
    # 每发特制弩箭增加爆炸型弩箭标记层数最大消耗量 : {value2}个
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 每发之间可自由行动时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 最后一发爆炸型弩箭攻击力(收割) : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    cost4 = 15
    # 标记层数最大消耗 : 5个
    # [范围信息]
    # 弩箭射程 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 最后一发弩箭爆炸范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [三弓弩箭]\n
        准备发射弩箭时， 使用推进装置朝着前方一定范围内最强敌人的位置移动后发射\n
        每发之间可自由行动时间 +10秒\n
        施放技能时进入无敌状态
        """
        ...

    def vp_2(self):
        """
        [三弓弩箭]\n
        施放时， 进入坐姿射击集中状态\n
         - 每次按技能键或攻击键时， 依次发射一发弩箭\n
         - 集中状态下无法使用方向键移动， 但可以使用推进装置\n
         - 从第二发弩箭开始发射\n
         - 总攻击力相同\n
         - 被第二发弩箭命中的敌人， 最后一发爆炸型弩箭的最大消耗标记层数 +10\n
        所有弩箭都会命中前方一定范围内的最强敌人\n
        集中状态下， 推进装置的冷却时间 -50%\n
        按跳跃键时， 结束技能\n
        未发射弩箭并结束技能时， 剩余冷却时间缩短为5秒
        """
        ...

# 帕伊卡锐眼
# archer/hunter/fc458e449ee00b01dbf88d09aae65462
# b9cb48777665de22c006fabaf9a560b3/fc458e449ee00b01dbf88d09aae65462
class Skill31(PassiveSkill):
    """
        在冒险中进一步成长的帕伊卡辅助着猎人。\n
        更广阔的视野可以发现更远距离的猎物， 猎人在帕伊卡精确搜索的帮助下， 可以更精准地瞄准敌人的要害。\n
    [帕伊卡！ 不要放过这个家伙！]
    """
    name = "帕伊卡锐眼"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 2 #TODO
    rangeLv = 3
    uuid = "fc458e449ee00b01dbf88d09aae65462"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # [狩猎之瞳]探索范围增加 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 暴击伤害增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [ {"data":data2,"type":"*skillDamage"}]

# 联合作战 : 围猎
# archer/hunter/1812a1ece67bb37b6b44b54766450064
# b9cb48777665de22c006fabaf9a560b3/1812a1ece67bb37b6b44b54766450064
class Skill32(HunterActiveSkill):
    """
    [标记+收割技能]\n
        与帕伊卡展开配合进行狩猎。\n
        帕伊卡抓起后空翻的猎人快速向前方飞行， 在过程中猎人使用小型弩箭扫射地面逼退敌人。 当帕伊卡放下猎人时， 猎人从空中下落并向聚集的敌人发射爆炸型弩箭收尾。\n
        可在[联合作战 : 空中轰炸]过程中施放。
    """
    name = "联合作战 : 围猎"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [1670, 7095]
    uuid = "1812a1ece67bb37b6b44b54766450064"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 小型弩箭多段攻击力(标记) : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 10
    cost0 = -10
    # 最大多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸型弩箭攻击力(终结) : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    cost2 = 5
    # 标记叠加层数最大消耗 : 5个

# 联合作战 : 空中轰炸
# archer/hunter/d89f26862e348a801b30bb9fd7125db5
# b9cb48777665de22c006fabaf9a560b3/d89f26862e348a801b30bb9fd7125db5
class Skill33(HunterActiveSkill):
    """
    [标记+收割技能]\n
        与帕伊卡一起在空中轰炸敌人。\n
        一段时间内帕伊卡抓住猎人， 进入飞行模式。 在飞行模式下， 可以在空中通过方向键自由移动并减少所受伤害， 按攻击键 (默认X) 可以向地面发射多枚小型弩箭， 按技能键 (默认Z) 可以向地面发射一枚爆炸型弩箭。\n
        发射完装填的所有爆炸型弩箭或飞行模式持续时间结束时， 技能结束。 在飞行模式中按跳跃键 (默认C) 时， 可让技能提前结束。\n
        飞行模式中可以施放[联合作战 : 围猎]。\n
        可以在空中使用。
    """
    name = "联合作战 : 空中轰炸"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [418, 1775]
    uuid = "d89f26862e348a801b30bb9fd7125db5"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 飞行模式持续时间上限 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 小型弩箭多段攻击力 (标记) : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 19*2
    cost1 = 19*(-2)
    # 爆炸型弩箭攻击力 (收割) : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 5*1
    cost2 = 5*5
    # 每发爆炸型弩箭消耗的标记层数上限 : 5个
    # 爆炸型弩箭装填数量 : {value3}发
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 飞行模式中所受伤害减少率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 爆炸型弩箭爆炸范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [联合作战 : 空中轰炸]\n
        飞行中可以使用推进装置\n
         - 根据方向键输入的方向， 向前方或后方一定距离冲刺\n
         - 无法连续冲刺\n
         - 推进装置冷却时间变更为0.5秒\n
        飞行模式最大维持时间 +10秒\n
        小型弩箭多段攻击间隔 -50%\n
         - 小型弩箭多段攻击次数 +100%\n
         - 总攻击力相同\n
        爆炸型弩箭发射冷却时间 -50%\n
         - 爆炸型弩箭爆炸范围 +20%\n
         - 爆炸型弩箭发射数 +2\n
         - 总攻击力相同
        """
        self.hit1 = 21*4
        self.power1 *= 0.5
        self.cost1 = 21*(-4)
        self.hit2 = 7*1
        self.cost2 = 7*5

    def vp_2(self):
        """
        [联合作战 : 空中轰炸]\n
        飞行模式中可以使用[重型穿甲箭]、 [霰弹之箭]、 [光爆箭]技能\n
        - 飞行模式中上述技能的攻击力和冷却时间 -40%\n
        - 飞行模式中施放[重型穿甲箭]时， 穿甲箭插入地面并引发冲击波进行攻击， 直接被弩箭命中的敌人进入强制控制1秒\n
        - 飞行模式中施放[霰弹之箭]时， 向地面一定范围爆炸性地倾泻小型弩箭\n
        - 飞行模式中施放[光爆箭]时， 将[光爆箭]弩箭发射到地面， 弩箭接触地面时爆炸\n
        飞行模式中所受伤害额外 -50%
        """
        ...

# 帕伊卡 : 翼之刀锋
# archer/hunter/2ba299855fc22192cba4f73db75e9d0e
# b9cb48777665de22c006fabaf9a560b3/2ba299855fc22192cba4f73db75e9d0e
class Skill34(HunterActiveSkill):
    """
        帕伊卡在空中旋转一圈， 随后以肉眼看不见的速度冲向敌人。\n
        无论猎人当前处于什么状态都可施放该技能， 但无法和其他“帕伊卡”和“联合作战”系列技能同时使用。
    """
    name = "帕伊卡 : 翼之刀锋"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 3
    cd = 50
    mp = [632, 2687]
    uuid = "2ba299855fc22192cba4f73db75e9d0e"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 突进攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [帕伊卡 : 翼之刀锋]\n
        向前方冲刺后立即调头， 朝着反方向追加一次冲刺\n
         - 总攻击力相同\n
        被冲刺攻击命中的敌人会被拖移一定距离\n
        冲刺攻击范围 +30%\n
        突进距离 +50%
        """
        ...

    def vp_2(self):
        """
        [帕伊卡 : 翼之刀锋]\n
        帕伊卡不再旋转一周， 而是短暂等待后瞬间加速突进\n
        突进速度 +30%
        """
        ...

# 装置升级
# archer/hunter/2c9d9a36c8401bddff6cdb80fab8dc24
# b9cb48777665de22c006fabaf9a560b3/2c9d9a36c8401bddff6cdb80fab8dc24
class Skill35(PassiveSkill):
    """
        改良强攻弩武器和鞋子的推进装置。\n
    [强攻弩改良]\n
        基础攻击和转职技能攻击力增加， 对部分小型弩箭攻击赋予标记属性及穿刺效果。\n
        - 地面基本攻击小型弩箭\n
        - [迅猛速射]\n
        - [急速扳机]小型弩箭\n
        - [帕伊卡 : 刃羽]\n
    [推进装置改良]\n
        使用[推进装置]时进入霸体状态。 [推进装置]可在被击或滞空状态中使用。\n
        被击过程中使用时会后空翻拉开距离， 空中状态使用时会加快下落速度。\n
        此外， 通过收割攻击消耗5个以上的标记层数时， 初始化[推进装置]的冷却时间。
    """
    name = "装置升级"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 2 #TODO
    rangeLv = 3
    uuid = "2c9d9a36c8401bddff6cdb80fab8dc24"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

    associate = [ {"data":data0,"type":"*skillDamage"}]

# 终结穿刺
# archer/hunter/b89c9ab317bc0a443f6497b7cca2f6a8
# b9cb48777665de22c006fabaf9a560b3/b89c9ab317bc0a443f6497b7cca2f6a8
class Skill36(HunterActiveSkill):
    """
    [收割技能]\n
        装填钻头型弩箭， 向前方发射。\n
        弩箭命中敌人后剧烈旋转， 对被击中的敌人造成巨大伤害。\n
    [那……减少穿透力的同时提高破坏力总可以了吧？]
    """
    name = "终结穿刺"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [1170, 4969]
    uuid = "b89c9ab317bc0a443f6497b7cca2f6a8"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 弩箭命中攻击力(收割) : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    cost0 = 5
    # 钻头旋转攻击力 : {value1}% x{value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 10
    cost1 = 5
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 标记层数最大消耗 : 5个
    # [范围信息]
    # 弩箭射程 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [终结穿刺]\n
        命中敌人的弩箭会更加剧烈旋转\n
         - 多段攻击次数 +50%\n
         - 以弩箭为中心， 吸附一定范围内的敌人\n
         - 总攻击力相同\n
        若发射的弩箭没有击中敌人而消失， 则技能剩余冷却时间缩短为5秒\n
        弩箭嵌入敌人后开始旋转前的时间 -70%
        """
        ...

    def vp_2(self):
        """
        [终结穿刺]\n
        装弹时可以发动[重型穿甲箭]， 发动时将钻头型弩箭替换为高重量的钻头型弩箭进行发射\n
         - 发射后的弩箭将穿透敌人并直线飞行\n
         - 删除弩箭碰撞攻击\n
         - 多段攻击次数减少为3次\n
         - 总攻击力相同\n
         - 攻击时同时适用[重型穿甲箭]的攻击力\n
         - 最多消耗5个标记层数， 消耗的层数同样适用于[重型穿甲箭]攻击力
        """
        ...

# 帕伊卡 : 索敌集束弹
# archer/hunter/7cf17936a039b418660424125dc968d7
# b9cb48777665de22c006fabaf9a560b3/7cf17936a039b418660424125dc968d7
class Skill37(HunterActiveSkill):
    """
    [标记技能]\n
        帕伊卡以超近距离追踪一定范围内的最强的一个敌人， 并植入大量的小型弩箭。\n
        随后将改造后的喷射式炸弹植入敌人后离开， 炸弹在一定时间后爆炸， 将小型弩箭发射出去， 对范围内的所有敌人造成伤害。\n
        施放技能时， 可以预输入以下技能中的一个， 植入喷射式炸弹后会在原地马上施放预输入的技能。\n
        - [帕伊卡 : 迷惑之舞]\n
        - [帕伊卡 : 翼之刀锋]\n
        无论猎人当前处于什么状态都可施放该技能， 但无法和其他“帕伊卡”和“联合作战”系列技能同时使用。
    """
    name = "帕伊卡 : 索敌集束弹"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [1462, 6210]
    uuid = "7cf17936a039b418660424125dc968d7"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 追踪小型弩箭攻击力(标记) : {value0}% x{value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 15
    cost0 = -15
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 喷射式炸弹爆炸攻击力(标记) : {value2}% x{value3}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 5
    cost2 = -5
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 寻敌范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 喷射式炸弹爆炸范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [帕伊卡 : 索敌集束弹]\n
        变更为可填充2次的技能\n
         - 每次填充冷却时间 : 22.5秒\n
         - 追踪小型弩箭攻击次数减少到10次\n
         - 单次攻击力 -50%
        """
        self.cd = 22.5
        self.skillRation *= 0.5

    def vp_2(self):
        """
        [帕伊卡 : 索敌集束弹]\n
        删除追踪小型弩箭攻击\n
        仅植入改良炸弹后离开\n
         - 炸弹会植入在敌人身上， 以固定时间间隔爆炸3次\n
         - 喷射式炸弹1次爆炸多段攻击次数 +100%\n
         - 总攻击力相同\n
         - 爆炸范围 +30%
        """
        ...

# 完美瞄准
# archer/hunter/7f80b887a09e88e2c4728c898bd73654
# b9cb48777665de22c006fabaf9a560b3/7f80b887a09e88e2c4728c898bd73654
class Skill38(HunterActiveSkill):
    """
    [收割技能]\n
        向天空发射一枚爆炸型弩箭， 之后稍稍后退， 瞄准落下的第一枚弩箭发射第二枚弩箭。\n
        两枚弩箭碰撞后产生巨大爆炸， 对范围内所有敌人造成伤害。\n
    [如果连这都做不到的话， 这个战斗飞行团的标记就要被摘掉了， 不是吗？]
    """
    name = "完美瞄准"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2780, 11814]
    uuid = "7f80b887a09e88e2c4728c898bd73654"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 爆炸攻击力(收割) : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    cost0 = 5
    # 标记层数最大消耗 : 5个

# 追猎者勋章
# archer/hunter/e5c09f9132a48dc1d695968592cc5878
# b9cb48777665de22c006fabaf9a560b3/e5c09f9132a48dc1d695968592cc5878
class Skill39(PassiveSkill):
    """
        决定不再逃避责任的聆风·猎人， 将长久以来藏在口袋里的勋章挂在胸前。\n
        增加基本攻击和转职技能的攻击力， 变更部分技能效果。\n
    [重型穿甲箭]\n
        攻击时， 默认视为消耗了4个标记层数， 但是不会增加最大消耗量。\n
    [帕伊卡 : 迷惑之舞]\n
        变更为标记技能， 为帕伊卡高速移动攻击赋予标记属性。 迷雾区域增加引发混乱异常状态。\n
    [以后， 我不会再以自由的名义逃避自己的责任了。]
    """
    name = "追猎者勋章"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 3
    uuid = "e5c09f9132a48dc1d695968592cc5878"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

    associate = [ {"data":data0,"type":"*skillDamage"}]

# 联合作战 : 扭转战局
# archer/hunter/e0daa922b19cdc35de879e938361464e
# b9cb48777665de22c006fabaf9a560b3/e0daa922b19cdc35de879e938361464e
class Skill40(HunterActiveSkill):
    """
    [收割技能]\n
        采取紧急战术扭转危机。\n
        帕伊卡向前方大幅度盘旋， 喷洒弩箭骚扰敌人， 随后合二为一， 猎人踩着帕伊卡的后背跃起， 出其不意地向前方地面发射爆炸型弩箭收尾。
    """
    name = "联合作战 : 扭转战局"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [1636, 6951]
    uuid = "e0daa922b19cdc35de879e938361464e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 帕伊卡小型弩箭攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5*2
    # 小型弩箭最大命中次数 : {value1}次x2
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 猎人爆炸型弩箭攻击力(收割) : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    cost2 = 5
    # 标记层数最大消耗 : 5个

# 联合作战 : 最终一役
# archer/hunter/0fbb8de70002ad34f046c94c2cb3e863
# b9cb48777665de22c006fabaf9a560b3/0fbb8de70002ad34f046c94c2cb3e863
class Skill41(HunterActiveSkill):
    """
    [标记+收割技能]\n
        帕伊卡开启辅助装置， 用迷雾覆盖周围大片区域， 随后聆风·猎人与帕伊卡一起腾空而起， 装填足以摧毁整座悬浮岛的超大型特殊弩箭向地面发射， 将战场夷为平地。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "联合作战 : 最终一役"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4538, 19283]
    uuid = "0fbb8de70002ad34f046c94c2cb3e863"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 小型弩箭多段攻击力(标记) : {value0}% x{value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 15
    cost0 = -15
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 超大型特殊弩箭爆炸攻击力(收割) : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    cost2 = 5
    # 标记层数最大消耗 : 5个


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'hunter'
        self.nameCN = '聆风·猎人'
        self.role = 'archer'
        self.角色 = '弓箭手'
        self.职业 = '猎人'
        self.jobId = 'b9cb48777665de22c006fabaf9a560b3'
        self.jobGrowId = '6d459bc74ba73ee4fe5cdc4655400193'

        self.武器选项 = ["强攻弩"] # TODO
        self.输出类型选项 = ["物理百分比"] # TODO
        self.输出类型 = "物理百分比" # TODO
        self.防具精通属性 = ["力量"] # TODO
        self.防具类型 = "重甲"
        self.buff = 2.00 # TODO

        super().__init__(equVersion, __name__)
