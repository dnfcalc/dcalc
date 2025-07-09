#ddc49e9ad1ff72a00b53c6cff5b1e920
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "thief/rogue/cn/skillDetail"

class PassiveSkill(PassiveSkill):
    endpower = 1

class ActiveSkill(ActiveSkill):
    endpower = 1

    def getSkillData(self,lv:int=0):
        res = 0
        keys = [key.replace("data","") for key in dir(self) if key.startswith('data') and not key.startswith('dataplus')]
        for i in keys:
            data = getattr(self, f'data{i}', [])
            plus = getattr(self, f'plus{i}', 0)
            if len(data) == 0:
                break
            if lv < len(data):
                hit = getattr(self, f'hit{i}', 0)
                power = getattr(self, f'power{i}', 1)
                group = getattr(self, f'group{i}', "normal")
                res += hit * power * (data[lv] + plus) * (self.endpower if group == "end" else 1)
        keys = [key.replace("dataplus","") for key in dir(self) if key.startswith('dataplus')]
        for i in keys:
            data = getattr(self, f'dataplus{i}', 0)
            hit = getattr(self, f'hitplus{i}', 1)
            power = getattr(self, f'powerplus{i}', 1)
            group = getattr(self, f'groupplus{i}', "normal")
            res += hit * power * data * (self.endpower if group == "end" else 1)
        return res

# 翔击
# thief/rogue/3c5604bdbb0240b8f130f59ab40509c3
# ddc49e9ad1ff72a00b53c6cff5b1e920/3c5604bdbb0240b8f130f59ab40509c3
class Skill0(ActiveSkill):
    """
    向敌人发出向上的切割攻击， 并使敌人浮空。\n
    在空中也可以使用[翔击]， 且按住技能键的时间越长， [翔击]的跳跃高度就越高。\n
    可消耗连击点数发动[终结之击]。
    """
    name = "翔击"
    learnLv = 1
    masterLv = 10
    maxLv = 20
    position = 5 #TODO
    rangeLv = 3
    cd = 2
    uuid = "3c5604bdbb0240b8f130f59ab40509c3"
    hasVP = False
    hasUP = False

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 浮空力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [终结之击]攻击力 : {value2}% X {value3}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    data2 = [0, 71, 83, 94, 105, 117, 128, 139, 151, 162, 173, 185, 196, 207, 219, 230, 241, 253, 264, 276, 287]# noqa: E501
    hit2 = 5
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [终结之击]浮空力比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)


# 基础精通
# thief/rogue/5a56514f35cf0270ae8d6c65f8fefd78
# ddc49e9ad1ff72a00b53c6cff5b1e920/5a56514f35cf0270ae8d6c65f8fefd78
class Skill3(PassiveSkill):
    """
    增加基本攻击、 前冲攻击、 跳跃攻击、 [翔击]的攻击力。\n
    在决斗场中， 增益/减益技能、 被动技能的技能攻击力增加效果对[基础精通]无影响。
    """
    name = "基础精通"
    learnLv = 1
    masterLv = 115
    maxLv = 200
    position = 1 #TODO
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


# 弧光闪
# thief/rogue/0969cd4054d93da07708108c0cc1c4b5
# ddc49e9ad1ff72a00b53c6cff5b1e920/0969cd4054d93da07708108c0cc1c4b5
class Skill10(ActiveSkill):
    """
    急速冲向前方的敌人并对其进行闪电般的攻击。\n
    按上下方向键可向Y轴移动； 若急速前冲过程中按跳跃键， 则可停止移动。\n
    暗星可以连续发动两次[弧光闪]； 可在空中施放[弧光闪]； 可强制中断转职技能， 并施放[弧光闪]； 可消耗连击点数发动可控制左右方向的[终结之击]； 学习[弧光连闪]后， 增加追加攻击的可发动次数。\n
    转职为影舞者后， 可以强制中断技能并施放[追影步]； 学习[潜行教义]后， 可以再次按技能键发动追加攻击。\n
    可以利用方向键调整移动方向。
    """
    name = "弧光闪"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 6
    mp = [18, 190]
    uuid = "0969cd4054d93da07708108c0cc1c4b5"
    hasVP = False
    hasUP = False

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [终结之击]攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    data1 = [0, 850, 932, 1020, 1108, 1192, 1278, 1363, 1450, 1533, 1622, 1712, 1794, 1882, 1965, 2055, 2135, 2224, 2307, 2395, 2485, 2567, 2655, 2739, 2827, 2910, 2999, 3082, 3169, 3257, 3344, 3429, 3512, 3602, 3686, 3774, 3856, 3946, 4038, 4116, 4206, 4289, 4379, 4457, 4549, 4627, 4719, 4809, 4893, 4983, 5063, 5153, 5236, 5321, 5409, 5494, 5581, 5664, 5755, 5840, 5926, 6010, 6100, 6183, 6270, 6355, 6443, 6530, 6611, 6701, 6783]# noqa: E501
    hit1 = 1 #TODO
    group1 = "end"
    # 发动速度比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 僵直时间比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)


# 碎踝
# thief/rogue/5dc7008b12a459325b548b0715c6b73c
# ddc49e9ad1ff72a00b53c6cff5b1e920/5dc7008b12a459325b548b0715c6b73c
class Skill13(ActiveSkill):
    """
    用强力的扫腿踢攻击敌人的脚踝。
    """
    name = "碎踝"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cd = 7
    mp = [15, 168]
    uuid = "5dc7008b12a459325b548b0715c6b73c"
    hasVP = False
    hasUP = False

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 减速几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 减速持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 移动速度减少率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 攻击速度减少率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)


# 疾空踏
# thief/rogue/717f1e2104fe4b796f800352fa143ecc
# ddc49e9ad1ff72a00b53c6cff5b1e920/717f1e2104fe4b796f800352fa143ecc
class Skill16(ActiveSkill):
    """
    从空中快速下降并向敌人发出连续踢击。\n
    连续踢击结束前， 输入Z键可以发动最后一击。\n
    只能在空中使用， 且在下落过程中有敌人时才能施放连续踢击。\n
    终结攻击会引发冲击波， 被命中的敌人会被击飞。\n
    连续踢击过程中连续按下攻击键时， 会增加连续踢击的速度和命中次数。
    """
    name = "疾空踏"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 6.5
    mp = [22, 235]
    uuid = "717f1e2104fe4b796f800352fa143ecc"
    hasVP = False
    hasUP = True

    # 连续踢击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 13
    # 连续踢击次数 : {value1}次~{value2}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 最后一击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # 冲击波攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1
    # 最后一击浮空力比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # [范围信息]
    # 冲击波范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

# 终结之击
# thief/rogue/cfacda0647b9a0f595df2c2aad30c18d
# ddc49e9ad1ff72a00b53c6cff5b1e920/cfacda0647b9a0f595df2c2aad30c18d
class Skill19(ActiveSkill):
    """
    [终结之击]只能在有连击点数的情况下施放， 施放后将消耗所有连击点数并发动追加攻击。\n
    消耗的连击点数越多， 该技能给予敌人的伤害就越大。
    """
    name = "终结之击"
    learnLv = 15
    masterLv = 20
    maxLv = 30
    position = 6 #TODO
    rangeLv = 2
    mp = [18, 56]
    uuid = "cfacda0647b9a0f595df2c2aad30c18d"
    hasVP = False
    hasUP = False

    # [终结之击]攻击力比率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # - 消耗连击点数后， 攻击力增加比率 -
    # 1点 : {value1}% 
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 2点 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 3点 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 4点 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 5点 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 6点 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # 7点 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)

    _maxLayer = 6

    associate = [
        {"type":"*endpower","data":data0},
        {"type":"*endpower"}
    ]

    @property
    def maxLayer(self):
        return self._maxLayer

    @maxLayer.setter
    def maxLayer(self, value):
        if self._maxLayer != value:
            skills = self.char.GetSkillNames('all', True)
            if self.lv > 0:
                raito = (getattr(self, f"data{int(value)}")[self.lv] - 100) / (getattr(self, f"data{int(self.maxLayer)}")[self.lv] - 100)
                for name in skills:
                    skill = self.char.GetSkillByName(name)
                    if skill.type == "active" and skill.damage:
                        skill.endpower *= raito
            self._maxLayer = value

    def update_skill_attribute(self, skill, type, old, new, data,ratio,weapon = []):
        if len(data) == 0:
            data = getattr(self, f"data{int(self.maxLayer)}")
            data = [ i - 100 if i > 100 else 0  for i in data]
        super().update_skill_attribute(skill, type, old, new, data, ratio, weapon)

# 弧光连闪
# thief/rogue/4b2c90ec226fd40e967875aa5eabefb2
# ddc49e9ad1ff72a00b53c6cff5b1e920/4b2c90ec226fd40e967875aa5eabefb2
class Skill21(PassiveSkill):
    """
    增加[弧光闪]的追加攻击发动次数。
    """
    name = "弧光连闪"
    learnLv = 15
    masterLv = 1
    maxLv = 10
    position = 5 #TODO
    rangeLv = 2
    uuid = "4b2c90ec226fd40e967875aa5eabefb2"
    hasVP = False
    hasUP = False

    # [弧光闪]追加攻击发动次数增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    associate = [{"type":"+hit0","data":data0,"ratio":1,"skills":["弧光闪"]}]

# 迅影
# thief/rogue/1b1cfab062e0768bcc889e33e1f30dbf
# ddc49e9ad1ff72a00b53c6cff5b1e920/1b1cfab062e0768bcc889e33e1f30dbf
class Skill22(PassiveSkill):
    """
    使暗星的行动变得更加敏捷， 可增加命中率、 回避率、 攻击速度和移动速度。\n
    强制中断后施放的技能命中敌人时， 可以获得连击点数。\n
    可通过攻击敌人时收集的攻击点数， 额外获得连击点数； 攻击点数能量条蓄满后， 可自动转换为连击点数。\n
    学习后， 后跳过程中可以发动基本攻击。
    """
    name = "迅影"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 1 #TODO
    rangeLv = 5
    uuid = "1b1cfab062e0768bcc889e33e1f30dbf"
    hasVP = False
    hasUP = False

    # 攻击速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 移动速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 命中率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 回避率增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [每个技能命中敌人时可收集的攻击点数 / 攻击点数收集上限]
    # 基本攻击 : {value4}P / {value5}P
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 前冲攻击 : {value6}P / {value7}P
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    # 跳跃攻击 : {value8}P / {value9}P
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)
    data9 = get_data(f'{prefix}/{uuid}', 9, lambda x = None: x)
    # [翔击] : {value10}P / {value11}P
    data10 = get_data(f'{prefix}/{uuid}', 10, lambda x = None: x)
    data11 = get_data(f'{prefix}/{uuid}', 11, lambda x = None: x)
    # [弧光闪] : {value12}P / {value13}P
    data12 = get_data(f'{prefix}/{uuid}', 12, lambda x = None: x)
    data13 = get_data(f'{prefix}/{uuid}', 13, lambda x = None: x)
    # [双刃穿刺] : {value14}P / {value15}P
    data14 = get_data(f'{prefix}/{uuid}', 14, lambda x = None: x)
    data15 = get_data(f'{prefix}/{uuid}', 15, lambda x = None: x)
    # [绝心击] : {value16}P / {value17}P
    data16 = get_data(f'{prefix}/{uuid}', 16, lambda x = None: x)
    data17 = get_data(f'{prefix}/{uuid}', 17, lambda x = None: x)
    # [旋舞斩] : {value18}P / {value19}P
    data18 = get_data(f'{prefix}/{uuid}', 18, lambda x = None: x)
    data19 = get_data(f'{prefix}/{uuid}', 19, lambda x = None: x)
    # [旋刃] : {value20}P / {value21}P
    data20 = get_data(f'{prefix}/{uuid}', 20, lambda x = None: x)
    data21 = get_data(f'{prefix}/{uuid}', 21, lambda x = None: x)
    # [剑刃风暴] : {value22}P / {value23}P
    data22 = get_data(f'{prefix}/{uuid}', 22, lambda x = None: x)
    data23 = get_data(f'{prefix}/{uuid}', 23, lambda x = None: x)
    # [雷光刃影] : {value24}P / {value25}P
    data24 = get_data(f'{prefix}/{uuid}', 24, lambda x = None: x)
    data25 = get_data(f'{prefix}/{uuid}', 25, lambda x = None: x)
    # [螺旋穿刺] : {value26}P / {value27}P
    data26 = get_data(f'{prefix}/{uuid}', 26, lambda x = None: x)
    data27 = get_data(f'{prefix}/{uuid}', 27, lambda x = None: x)
    # [疾风乱舞] : {value28}P / {value29}P
    data28 = get_data(f'{prefix}/{uuid}', 28, lambda x = None: x)
    data29 = get_data(f'{prefix}/{uuid}', 29, lambda x = None: x)
    # [绝境瞬狱袭] : {value30}P / {value31}P
    data30 = get_data(f'{prefix}/{uuid}', 30, lambda x = None: x)
    data31 = get_data(f'{prefix}/{uuid}', 31, lambda x = None: x)
    # [旋刃冲击] : {value32}P / {value33}P
    data32 = get_data(f'{prefix}/{uuid}', 32, lambda x = None: x)
    data33 = get_data(f'{prefix}/{uuid}', 33, lambda x = None: x)
    # [陨落螺旋刺] : {value34}P / {value35}P
    data34 = get_data(f'{prefix}/{uuid}', 34, lambda x = None: x)
    data35 = get_data(f'{prefix}/{uuid}', 35, lambda x = None: x)
    # [乱空杀] : {value36}P / {value37}P
    data36 = get_data(f'{prefix}/{uuid}', 36, lambda x = None: x)
    data37 = get_data(f'{prefix}/{uuid}', 37, lambda x = None: x)
    # [月影突袭] : {value38}P / {value39}P
    data38 = get_data(f'{prefix}/{uuid}', 38, lambda x = None: x)
    data39 = get_data(f'{prefix}/{uuid}', 39, lambda x = None: x)
    # [天渊星狱] : {value40}P / {value41}P
    data40 = get_data(f'{prefix}/{uuid}', 40, lambda x = None: x)
    data41 = get_data(f'{prefix}/{uuid}', 41, lambda x = None: x)
    # [幻灭瞬杀] : {value42}P / {value43}P
    data42 = get_data(f'{prefix}/{uuid}', 42, lambda x = None: x)
    data43 = get_data(f'{prefix}/{uuid}', 43, lambda x = None: x)

# 绝心击
# thief/rogue/4224f9b0b8c7c903e9a1e0f9d9f6d04d
# ddc49e9ad1ff72a00b53c6cff5b1e920/4224f9b0b8c7c903e9a1e0f9d9f6d04d
class Skill23(ActiveSkill):
    """
    快速迈进并向前方敌人进行斩击， 被斩击命中的敌人将受到伤害， 并有一定几率进入眩晕状态。\n
    斩击后， 可消耗连击点数发动[终结之击]。
    """
    name = "绝心击"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 7
    mp = [25, 273]
    uuid = "4224f9b0b8c7c903e9a1e0f9d9f6d04d"
    hasVP = False
    hasUP = True

    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 眩晕几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 眩晕持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # -  [终结之击]时  -
    # 踢击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1 #TODO
    group3 = "end"
    # 切割攻击力 : {value4}% X {value5}
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 3
    group4 = "end"
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # [范围信息]
    # 范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

# 空跃
# thief/rogue/d085127b0edd719782bd618d5688f4a1
# ddc49e9ad1ff72a00b53c6cff5b1e920/d085127b0edd719782bd618d5688f4a1
class Skill24(ActiveSkill):
    """
    在跳跃中进行再一次跳跃。
    """
    name = "空跃"
    learnLv = 20
    masterLv = 1
    maxLv = 1
    position = 10 #TODO
    rangeLv = 1
    uuid = "d085127b0edd719782bd618d5688f4a1"
    hasVP = False
    hasUP = False


# 双刃穿刺
# thief/rogue/8ee0099656df08a0b39225f8a21d514b
# ddc49e9ad1ff72a00b53c6cff5b1e920/8ee0099656df08a0b39225f8a21d514b
class Skill25(ActiveSkill):
    """
    用双手把武器插入敌人身体后， 再用脚踢进行攻击。\n
    对可抓取的敌人命中刺击时， 进入无敌状态并强控敌人。\n
    对无法抓取的敌人不适用控制效果。\n
    可消耗连击点数发动[终结之击]。
    """
    name = "双刃穿刺"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 7
    mp = [47, 518]
    uuid = "8ee0099656df08a0b39225f8a21d514b"
    hasVP = False
    hasUP = True

    # 双手刺击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 第1次踢击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 第2次踢击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [终结之击]攻击力比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1 #TODO
    group3 = "end"
    # 周围敌人的伤害比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # [范围信息]
    # 范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)

# 暗星武器精通
# thief/rogue/da6e37c1e3f0e8867f70007d89c239ff
# ddc49e9ad1ff72a00b53c6cff5b1e920/da6e37c1e3f0e8867f70007d89c239ff
class Skill26(PassiveSkill):
    """
       学习后， 增加物理攻击力， 并减少转职技能的冷却时间， 同时增加[终结之击]攻击力。 技能达到15级以上时， 提升每个技能命中敌人时可收集的攻击点数和攻击点数收集上限， 并且在装备匕首和双剑时获得额外效果。\n
    [装备匕首时]\n
    使用匕首系武器时， 增加攻击速度、 回避率、 命中率。\n
    [装备双剑时]\n
    使用双剑系武器时， 增加敌人的僵直率、 回避率、 命中率。
    """
    name = "暗星武器精通"
    learnLv = 20
    masterLv = 20
    maxLv = 30
    position = 0 #TODO
    rangeLv = 4
    uuid = "da6e37c1e3f0e8867f70007d89c239ff"
    hasVP = False
    hasUP = False

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 冷却时间减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [终结之击]攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 每次攻击可收集的攻击点数比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 每次攻击可收集的攻击点数最大值比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # [装备匕首时]
    # 攻击速度增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 回避率增加 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # 命中率增加 : {value7}%.
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    # [装备双剑时]
    # 敌人僵直率增加 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)
    # 回避率增加 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9, lambda x = None: x)
    # 命中率增加 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10, lambda x = None: x)

    associate = [
        {"type":"$*PAtkP","data":data0},
        {"type":"$*cdReduce","data":data1,"exceptSkills":[]},
        {"type":"+maxLayer","data":data2,"ratio":1,"skills":["终结追击"]},
    ]

# 旋舞斩
# thief/rogue/c7bf7ccab413009640e65ca6f2f0263a
# ddc49e9ad1ff72a00b53c6cff5b1e920/c7bf7ccab413009640e65ca6f2f0263a
class Skill27(ActiveSkill):
    """
    在原地快速旋转并攻击周围敌人。\n
    在地上施放转职技能时， 可强制中断当前进行的技能动作， 并立即施放[旋舞斩]。\n
    可消耗1点连击点数发动[终结之击]。 [终结之击]发动后若存在连击点数， 则可以继续发动[终结之击]。
    """
    name = "旋舞斩"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 8 #TODO
    rangeLv = 2
    cd = 7
    mp = [25, 273]
    uuid = "c7bf7ccab413009640e65ca6f2f0263a"
    hasVP = False
    hasUP = True

    # 回旋斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # [终结之击]攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1 #TODO
    group1 = "end"
    # [范围信息]
    # 范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)


# 旋刃
# thief/rogue/01384bbfc346775d1267fa0bc4ca605f
# ddc49e9ad1ff72a00b53c6cff5b1e920/01384bbfc346775d1267fa0bc4ca605f
class Skill29(ActiveSkill):
    """
    旋转刀锋， 以极快速度切割敌人。\n
    再次输入技能键或Z键， 可以发动第二击和第三击横扫攻击， 第三击横扫后消耗连击点数发动[终结之击]。\n
    学习[绝命时刻]后， 施放时将以极快的速度一次性发动第一击、 第二击、 第三击横扫攻击。
    """
    name = "旋刃"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cd = 8
    mp = [45, 469]
    uuid = "01384bbfc346775d1267fa0bc4ca605f"
    hasVP = False
    hasUP = True

    # 第1次斩击攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 3
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 第2次斩击攻击力 : {value2}% X {value3}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 3
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 第3次斩击攻击力 : {value4}% X {value5}
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 3
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # [终结之击]攻击力 : {value6}% X {value7}
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    hit6 = 3
    group6 = "end"
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    # [范围信息]
    # 范围比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)

# 疾驰
# thief/rogue/42c82812f86ff6704ae9952a2e6093a4
# ddc49e9ad1ff72a00b53c6cff5b1e920/42c82812f86ff6704ae9952a2e6093a4
class Skill30(ActiveSkill):
    """
    用极快的速度向前方冲刺。\n
    施放技能时， 若按上/下方向键， 则可以控制冲刺方向； 移动时， 进入无敌状态。\n
    可以强制中断冲刺并立即施放基本攻击、 跳跃以及技能； 可以强制中断当前进行的技能动作， 并立即施放[疾驰]。
    """
    name = "疾驰"
    learnLv = 30
    masterLv = 1
    maxLv = 1
    position = 4 #TODO
    rangeLv = 2
    cd = 5
    mp = [10, 10]
    uuid = "42c82812f86ff6704ae9952a2e6093a4"
    hasVP = False
    hasUP = False


# 剑刃风暴
# thief/rogue/3829c15bf5f520c13998a3479ba0ce7b
# ddc49e9ad1ff72a00b53c6cff5b1e920/3829c15bf5f520c13998a3479ba0ce7b
class Skill31(ActiveSkill):
    """
    快速旋转切割周围的敌人。\n
    旋转时， 可以用方向键控制移动方向， 在空中也可以发动。\n
    旋转攻击中可以消耗连击点数发动[终结之击]； 发动[终结之击]时， 可以垂直上升并使敌人浮空。\n
    学习[绝命时刻]后， 增加移动速度和吸附力， 减少多段攻击间隔。
    """
    name = "剑刃风暴"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 8 #TODO
    rangeLv = 2
    cd = 10
    mp = [65, 699]
    uuid = "3829c15bf5f520c13998a3479ba0ce7b"
    hasVP = False
    hasUP = True

    # 旋转攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 10
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [终结之击]攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    group2 = "end"
    # 旋转时移动速度 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [范围信息]
    # 范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

# 侧步
# thief/rogue/e49e57b2e8fbeceb0a2c56a0c63fe6c5
# ddc49e9ad1ff72a00b53c6cff5b1e920/e49e57b2e8fbeceb0a2c56a0c63fe6c5
class Skill32(ActiveSkill):
    """
    向Y轴侧跳移动， 按上下方向键可以控制移动方向。 若不按方向键， 则默认向下方移动。\n
    可以强制中断转职技能并立即施放[侧步]。 施放时可以按攻击键进行跳跃攻击。\n
    在决斗场中施放[侧步]时无法进行跳跃攻击。
    """
    name = "侧步"
    learnLv = 30
    masterLv = 1
    maxLv = 1
    position = 3 #TODO
    rangeLv = 1
    cd = 1.2
    mp = [3, 3]
    uuid = "e49e57b2e8fbeceb0a2c56a0c63fe6c5"
    hasVP = False
    hasUP = False


# 暗掠
# thief/rogue/b501ae53638d33a32351904f31cb6aa3
# ddc49e9ad1ff72a00b53c6cff5b1e920/b501ae53638d33a32351904f31cb6aa3
class Skill33(ActiveSkill):
    """
    增加暴击伤害， 效果持续一定时间。
    """
    name = "暗掠"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 1 #TODO
    rangeLv = 2
    cd = 5
    uuid = "b501ae53638d33a32351904f31cb6aa3"
    hasVP = False
    hasUP = False

    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 暴击伤害增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 螺旋穿刺
# thief/rogue/bb34e8854a93fd250347a1c64119f7ab
# ddc49e9ad1ff72a00b53c6cff5b1e920/bb34e8854a93fd250347a1c64119f7ab
class Skill34(ActiveSkill):
    """
    向前移动并使自身急速旋转攻击敌人。\n
    若在地面上施放该技能， 则以抛物线跳跃并旋转； 若在空中施放该技能， 则水平前进并发动旋转攻击。\n
    向前移动过程中， 若再次按技能键或<Z>键， 则直接向下进行强力攻击并形成冲击波； 此时， 可以消耗连击点数发动[终结之击]。
    """
    name = "螺旋穿刺"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [128, 1072]
    uuid = "bb34e8854a93fd250347a1c64119f7ab"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 移动距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 旋转攻击力 : {value1}% X {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 6
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 向下强击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1 #TODO
    # 冲击波攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # [终结之击]攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    hit5 = 1 #TODO
    group5 = "end"
    # [范围信息]
    # 范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

    def vp_1(self):
        """
        [螺旋穿刺]\n
        基本冷却时间变更为30秒\n
        - 总攻击力 +100%\n
        施放过程中回避率 +50%\n
        可以通过按左、 右方向键调整[终结之击]发动方向
        """
        self.cd = 30
        self.skillRation *= 2
        ...

    def vp_2(self):
        """
        [螺旋穿刺]\n
        攻击范围及移动距离 +60%\n
        地面施放时， 会跳跃后发动技能\n
        旋转攻击强化\n
        - 不穿透敌人\n
        - 多段攻击次数 +200%\n
        - 多段攻击间隔 -67%\n
        [终结之击]变更\n
        - 旋转攻击中再次按技能键无法发动下劈\n
        - 旋转攻击中可以发动[终结之击]\n
        - [终结之击]变更为下劈攻击\n
        - 下劈攻击及下劈冲击波攻击力合算至[终结之击]\n
        总攻击力相同
        """
        ...

# 雷光刃影
# thief/rogue/e4c354a89c337310aeb7041d5e742828
# ddc49e9ad1ff72a00b53c6cff5b1e920/e4c354a89c337310aeb7041d5e742828
class Skill35(ActiveSkill):
    """
    抓取敌人后， 对其进行连续地突刺攻击， 最后再向下猛踢敌人。\n
    向下猛踢碰到地面时， 生成冲击波； 抓取成功时， 进入无敌状态， 并使敌人进入强制控制状态。\n
    攻击无法抓取的敌人时， 将直接进行向下猛踢， 增加向下猛踢攻击力且不会控制敌人。 向下猛踢后， 可消耗连击点数发动[终结之击]。\n
    在决斗场中[终结之击]无法使敌人浮空。
    """
    name = "雷光刃影"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [91, 763]
    uuid = "e4c354a89c337310aeb7041d5e742828"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 突刺攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 0
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 踢击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 0
    # 踢击攻击力  (无法抓取的敌人) : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # 踢击冲击波攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1
    # [终结之击]攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    hit5 = 1
    group5 = "end"
    # [范围信息]
    # 范围比率 (除踢击冲击波) : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # 踢击冲击波范围比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)

    def vp_1(self):
        """
        [雷光刃影]\n
        固定以对无法抓取目标的形态发动\n
        - 踢击攻击下落速度 +40%\n
        [月轮舞]\n
        使用[雷光刃影]的[终结之击]时， 攻击速度和移动速度增加量增加20%， 效果持续15秒
        """
        ...

    def vp_2(self):
        """
        [雷光刃影]\n
        吸附周围敌人并抓取\n
        攻击范围 +25%\n
        抓取失败时冷却时间变更为2秒
        """
        ...

# 疾风乱舞
# thief/rogue/1dad88963abdc96b091fcab185a8820d
# ddc49e9ad1ff72a00b53c6cff5b1e920/1dad88963abdc96b091fcab185a8820d
class Skill36(ActiveSkill):
    """
    快速接近前方敌人， 并对该敌人进行狂风般的乱舞攻击。\n
    突进过程中， 按上下方向键可以调整移动方向， 成功抓住后进入无敌状态并强控敌人。\n
    乱舞攻击时， 若按跳跃键， 则会向周围的其他敌人瞬移， 并对其进行乱舞攻击。此时， 会在之前乱舞攻击过的敌人身上留下一个分身； 分身会在一定时间内持续攻击该敌人后消失。\n
    后踢后， 可消耗连击点数发动[终结之击]。\n
    在决斗场中， 强制中断基本攻击和技能动作发动时， 无法沿Y轴移动。
    """
    name = "疾风乱舞"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [164, 1376]
    uuid = "1dad88963abdc96b091fcab185a8820d"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 乱舞攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 11
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 分身攻击力 : {value2}% X {value3}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 4
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 最后一击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1
    # [终结之击]攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    hit5 = 1
    group5 = "end"
    # 瞬移距离上限 : {value6}px
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # [范围信息]
    # 范围比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)

    def vp_1(self):
        """
        [疾风乱舞]\n
        移动功能强化\n
        施放时追踪最近的敌人\n
        - 突进距离上限 +50%\n
        - 瞬移范围 +100%
        """
        ...

    def vp_2(self):
        """
        [疾风乱舞]\n
        突进过程中， 进入无敌状态\n
        抓取成功时， 为600px范围内的所有敌人赋予与暗星的攻击相同的瞬移分身\n
        无法通过跳跃键瞬移
        """
        ...

# 死亡风暴
# thief/rogue/c77a417c43de80c4ce32c1ed405d174a
# ddc49e9ad1ff72a00b53c6cff5b1e920/c77a417c43de80c4ce32c1ed405d174a
class Skill37(PassiveSkill):
    """
    施放[剑刃风暴]时， 由风暴中心向外呈环形投掷匕首。
    """
    name = "死亡风暴"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 8 #TODO
    rangeLv = 3
    uuid = "c77a417c43de80c4ce32c1ed405d174a"
    hasVP = True
    hasUP = False
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 匕首攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 30
    # 投掷匕首数量 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

    def getSkillCD(self,mode=None) -> float:
        return self.char.GetSkillByName("剑刃风暴").getSkillCD(mode)

    def vp_1(self):
        """
        [死亡风暴]\n
        向600px范围内最强敌人投掷匕首\n
        匕首发射数 -33%\n
        - 总攻击力相同\n
        [剑刃风暴]\n
        每次攻击获得的连击点数 +100%\n
        施放[终结之击]时， 剩余旋转攻击力合算至[终结之击]攻击力\n
        - 学习[陨落风暴]后， 合算[陨落螺旋刺]的旋转攻击力
        """
        ...

    def vp_2(self):
        """
        [死亡风暴]\n
        不再投掷匕首， 而是在风暴内部生成刀刃飓风\n
        - 刀刃飓风多段攻击次数 : 10次\n
        - 总攻击力相同\n
        [剑刃风暴]\n
        - 攻击范围及移动距离 +30%\n
        聚集敌人功能强化\n
        - 吸附力 +200%\n
        - 可以吸附霸体状态的敌人
        """
        ...

# 绝境瞬狱袭
# thief/rogue/128b9ddef2262f40723deae4407bdb42
# ddc49e9ad1ff72a00b53c6cff5b1e920/128b9ddef2262f40723deae4407bdb42
class Skill38(ActiveSkill):
    """
    前冲突击使敌人浮空， 然后发动连续攻击。\n
    前冲和连续攻击过程中， 自身进入无敌状态， 前冲攻击没有命中敌人时， 不会发动连续攻击。\n
    可以在地上和空中发动， 第3击后可消耗连击点数发动[终结之击]。\n
    在决斗场中， 无法在空中发动。
    """
    name = "绝境瞬狱袭"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [311, 2612]
    uuid = "128b9ddef2262f40723deae4407bdb42"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 前冲突击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 第1击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 第2击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 第3击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # [终结之击]攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1
    group4 = "end"
    # [范围信息]
    # 范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)

    def vp_1(self):
        """
        [绝境瞬狱袭]\n
        移动功能强化\n
        - 前冲攻击范围 +60%\n
        - 前冲攻击时可以Y轴移动\n
        施放速度 +20%
        """
        ...

    def vp_2(self):
        """
        [绝境瞬狱袭]\n
        变更为可填充2次的技能\n
        - 首次施放后10秒内可以施放第二次\n
        - 删除第2击、 第3击攻击\n
        - 前冲、 第1击攻击后发动[终结之击]\n
        - 发动[终结之击]时命中率增加20%， 效果持续10秒\n
        - 包括[终结之击]在内的所有攻击可以获得最大连击点数\n
        - 总攻击力相同
        """
        ...

# 月弧
# thief/rogue/de3fea2d65c597f4d55c70a02b97fc79
# ddc49e9ad1ff72a00b53c6cff5b1e920/de3fea2d65c597f4d55c70a02b97fc79
class Skill39(PassiveSkill):
    """
    获得连击点数时， 增加命中率、 回避率、 物理暴击率和暴击伤害， 效果持续一定时间。
    """
    name = "月弧"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 3
    uuid = "de3fea2d65c597f4d55c70a02b97fc79"
    hasVP = False
    hasUP = False

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 暴击伤害增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 物理暴击率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 回避率增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 命中率增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    associate = [{"data":data1}]

# 月轮舞
# thief/rogue/c61f5a010370101402b05b21916c2071
# ddc49e9ad1ff72a00b53c6cff5b1e920/c61f5a010370101402b05b21916c2071
class Skill40(ActiveSkill):
    """
    施放[月轮舞]后， 会进入月舞模式并持续一定时间。 在月舞模式下， 增加攻击范围， 且基本攻击、 前冲攻击和跳跃攻击变成多段攻击； 获得连击点数时， 增加攻击速度和移动速度。\n
    在月舞模式下， 基本攻击、 跳跃攻击和前冲攻击不受[基础精通]的影响。 增加攻击速度和移动速度的增益效果可以重叠一定次数。\n
    施放技能动作中， 进入无敌状态； 可以在空中施放。
    """
    name = "月轮舞"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 7
    cd = 145
    mp = [850, 7000]
    uuid = "c61f5a010370101402b05b21916c2071"
    hasVP = False
    hasUP = False
    damage = False
    bind = False

    # 月舞模式持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 普通/跳跃/前冲攻击次数增加 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 效果重叠次数上限 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 每次重叠攻击速度增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 每次重叠移动速度增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

# 月舞终结
# thief/rogue/dec8961c485edb02036ba00c789010f0
# ddc49e9ad1ff72a00b53c6cff5b1e920/dec8961c485edb02036ba00c789010f0
class Skill41(ActiveSkill):
    """
    可以在[月轮舞]增益状态下施放， 施放时发动强力连续斩击。\n
    共发动4次斩击， 1~3次斩击命中时， 分身进行突进攻击后发动终结斩击。\n
    被1~3段斩击命中的敌人会被强制控制并吸附过来， 并且可以在空中发动。\n
    学习后， 技能等级补正为与[月轮舞]相同。
    """
    name = "月舞终结"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cd = 145
    mp = [850, 7000]
    uuid = "dec8961c485edb02036ba00c789010f0"
    hasVP = False
    hasUP = False

    # 第1次斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 第2次斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 第3次斩击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 分身突进攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # 最后斩击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1

# 旋刃冲击
# thief/rogue/6a1d1f08a6572be420bb3a256c44c015
# ddc49e9ad1ff72a00b53c6cff5b1e920/6a1d1f08a6572be420bb3a256c44c015
class Skill42(ActiveSkill):
    """
    向前方投掷2个旋转刀刃。\n
    旋转刀刃在一定时间内聚拢敌人， 造成多段伤害。\n
    投掷出的旋转刀刃在触碰到敌人时停止移动， 若没有触碰到敌人， 则会移动至最大距离。\n
    旋转刀刃持续期间， 可消耗连击点数发动[终结之击]。 发动[终结之击]时， 快速移动到第一次投掷的旋转刀刃的位置， 对敌人造成多段伤害。 多次施放技能后发动[终结之击]时， 移动到存在的旋转刀刃中最先投掷的刀锋位置。\n
    在持续时间内， 即使发动[终结之击]， 旋转刀刃也不会消失。
    """
    name = "旋刃冲击"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 2
    cd = 30
    mp = [400, 1120]
    uuid = "6a1d1f08a6572be420bb3a256c44c015"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 旋转刀刃攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 30
    # 旋转刀刃持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 旋转刀刃多段攻击间隔 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 旋转刀刃投掷距离上限 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [终结之击]攻击力 : {value4}% X {value5}
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 5
    group4 = "end"
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # [范围信息]
    # 范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

    def vp_1(self):
        """
        [旋刃冲击]\n
        [双刃穿刺]命中时自动施放[旋刃冲击]， 并适用以下效果\n
        - 可施放[旋刃冲击]时发动\n
        - [双刃穿刺]的第2、 3次攻击生成旋转刀刃\n
        - 旋转刀刃不吸附敌人\n
        [终结之击]攻击强化\n
        - 施放速度 +80%\n
        - 多段攻击次数 -80%\n
        - 总攻击力相同\n
        [双刃穿刺]\n
        攻击范围 +25%
        """
        ...

    def vp_2(self):
        """
        [旋刃冲击]\n
        范围 +70%\n
        旋转刀刃强化\n
        - 每次攻击获得的连击点数 +100%\n
        - 可获得的连击点数上限 +1100%\n
        - 持续时间 +100%\n
        - 总攻击力相同\n
        [终结之击]攻击时， 获得最大连击点数
        """
        ...

# 陨落螺旋刺
# thief/rogue/38612d8f2561edc2eb68d5057a837bfa
# ddc49e9ad1ff72a00b53c6cff5b1e920/38612d8f2561edc2eb68d5057a837bfa
class Skill43(ActiveSkill):
    """
    跳跃后， 以极快的速度旋转并冲向地面， 落地时生成冲击波。\n
    在地面发动时， 可以使用方向键调整落地位置； 在空中发动时， 立即向地面发动旋转攻击。\n
    可消耗连击点数发动[终结之击]。
    """
    name = "陨落螺旋刺"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 2
    cube = 3
    cd = 50
    mp = [800, 1680]
    uuid = "38612d8f2561edc2eb68d5057a837bfa"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 旋转攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 3
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # [终结之击]攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [陨落螺旋刺]\n
        处于可以施放状态下施放[剑刃风暴]时， 自动发动[陨落螺旋刺]， 并适用以下效果\n
        - 删除冲击波攻击\n
        - 旋转攻击多段攻击次数上限 +7\n
        - [剑刃风暴]旋转攻击时， 附加[陨落螺旋刺]旋转攻击力\n
        - [剑刃风暴]终结之击攻击时， 附加[陨落螺旋刺]终结之击攻击力\n
        - 以施放[剑刃风暴]终结之击时消耗的连击点数为标准， 适用[陨落螺旋刺]终结之击攻击力\n
        - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [陨落螺旋刺]\n
        攻击范围 +40%\n
        降落速度 +300%\n
        - 增加落地后可发动[终结之击]的时间\n
        - 地面施放时跳跃高度 +50%\n
        删除旋转攻击\n
        - 每次攻击获得的连击点数 +300%\n
        - 总攻击力相同
        """
        ...

# 极限追击
# thief/rogue/0c3a468aee1f7ce06bf91eb3319518c1
# ddc49e9ad1ff72a00b53c6cff5b1e920/0c3a468aee1f7ce06bf91eb3319518c1
class Skill44(PassiveSkill):
    """
    将身体能力强化到极致， 增加物理攻击力和连击点数上限， 并可以强制中断技能后施放。\n
    强制中断技能的功能可以在已学的技能栏中， 通过鼠标右击进行开启/关闭切换。
    """
    name = "极限追击"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "0c3a468aee1f7ce06bf91eb3319518c1"
    hasVP = False
    hasUP = False

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 连击点数上限增加量 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    associate = [{"data":data0,"type":"$*PAtkP"}]

# 乱空杀
# thief/rogue/5cac3411ccef1af333953e0ded5e942d
# ddc49e9ad1ff72a00b53c6cff5b1e920/5cac3411ccef1af333953e0ded5e942d
class Skill45(ActiveSkill):
    """
    以极快的速度掠过敌人进行攻击。\n
    下劈后， 可以通1过消耗连击点数使用[终结之击]。
    """
    name = "乱空杀"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 3
    cube = 3
    cd = 30
    mp = [580, 4500]
    uuid = "5cac3411ccef1af333953e0ded5e942d"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 连续斩击攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 6
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 向下斩击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [终结之击]攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    group3 = "end"
    # [范围信息]
    # 范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    def vp_1(self):
        """
        [乱空杀]\n
        施放以下技能过程中发动时， 由分身施放\n
        - 适用技能 : [疾驰]、 [旋刃]、 [疾风乱舞]、 [月影突袭]\n
        - 分身施放时， 无法获得[乱空杀]的连击点数， 按最大连击点数适用[终结之击]攻击力\n
        - 基本冷却时间变更为24.9秒\n
        - 总攻击力 -17%
        """
        self.cd = 24.9
        self.skillRation *= 1 - 0.17
        ...

    def vp_2(self):
        """
        [乱空杀]\n
        攻击范围 +45%\n
        快速地攻击前后方\n
        - 连续斩击多段攻击次数 -50%\n
        - 每次攻击获得的连击点数 +67%\n
        - 总攻击力相同
        """
        ...

# 月影突袭
# thief/rogue/e1daab884dd07fc9e70d08b83d1790eb
# ddc49e9ad1ff72a00b53c6cff5b1e920/e1daab884dd07fc9e70d08b83d1790eb
class Skill46(ActiveSkill):
    """
    向前方突进， 用肉眼看不见的速度多次斩击。\n
    斩击可以将敌人聚集到中央。 多段斩击后， 可消耗连击点数发动[终结之击]。
    """
    name = "月影突袭"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 2
    cube = 5
    cd = 50
    mp = [800, 6000]
    uuid = "e1daab884dd07fc9e70d08b83d1790eb"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 多段斩击攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 10
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [终结之击]攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1 #TODO
    group2 = "end"
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [月影突袭]\n
        可以在空中施放\n
        多段攻击强化\n
        - 施放速度 +25%\n
        - 使敌人进入混乱异常状态， 效果持续3秒\n
        [终结之击]攻击强化\n
        - 施放速度 +25%\n
        - 多段攻击后可以立即发动
        """
        ...

    def vp_2(self):
        """
        [月影突袭]\n
        攻击范围 +35%\n
        多段攻击可以吸附霸体和无法抓取类型的敌人\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 25秒\n
        - 单次攻击力 -50%
        """
        self.cd = 25
        self.skillRation *= 1 - 0.5
        ...

# 天渊星狱
# thief/rogue/002cbdd9bfd0f0b970451ae8d48d029e
# ddc49e9ad1ff72a00b53c6cff5b1e920/002cbdd9bfd0f0b970451ae8d48d029e
class Skill47(ActiveSkill):
    """
    化为一束星光快速造成多段攻击， 随后从空中坠下引起爆炸。\n
       吸附多段攻击命中的敌人， 可以在空中施放。\n
    对无法抓取的敌人不适用控制效果。\n
    从空中坠下后， 可消耗连击点数发动[终结之击]。
    """
    name = "天渊星狱"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 8000]
    uuid = "002cbdd9bfd0f0b970451ae8d48d029e"
    hasVP = False
    hasUP = False

    # 星光多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 7
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # [终结之击]攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    group2 = "end"

# 幻灭瞬杀
# thief/rogue/9376d04c476cd41d60ed1974ca69ab95
# ddc49e9ad1ff72a00b53c6cff5b1e920/9376d04c476cd41d60ed1974ca69ab95
class Skill48(ActiveSkill):
    """
    瞬间释放超越身体极限的力量， 向前方突进。 突进时， 隐夜·暗星如残影攻击般快速攻击敌人。\n
    前方范围内存在敌人时才能施放该技能， 可以在地上和空中发动。\n
    突进后， 可以消耗连击点数发动[终结之击]。 
    """
    name = "幻灭瞬杀"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [960, 7200]
    uuid = "9376d04c476cd41d60ed1974ca69ab95"
    hasVP = False
    hasUP = False

    # 突进残影攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 5
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [终结之击]攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    group2 = "end"

# 绝命时刻
# thief/rogue/5536486eaf9b13c9a8283447cb5e77ab
# ddc49e9ad1ff72a00b53c6cff5b1e920/5536486eaf9b13c9a8283447cb5e77ab
class Skill49(PassiveSkill):
    """
    激发超越身体极限的力量， 获得强大的攻击力和敌人无法感知的行动速度。\n
    学习后， 增加基本攻击力和转职技能攻击力， [旋刃]和[剑刃风暴]技能附加特殊效果。\n
    [旋刃]\n
    以极快的速度发动第1击、第2击和第3击。\n
    [剑刃风暴]\n
    增加移动速度和吸附力。
    """
    name = "绝命时刻"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "5536486eaf9b13c9a8283447cb5e77ab"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [剑刃风暴]
    # 移动速度增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 吸附力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 多段攻击间隔减少率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    associate = [{"data":data0}]

# 影·万古星辰
# thief/rogue/ef9d26746effee9199b54541f01b8752
# ddc49e9ad1ff72a00b53c6cff5b1e920/ef9d26746effee9199b54541f01b8752
class Skill50(ActiveSkill):
    """
    集中精神后， 暂时突破身体的极限， 将力量强化到极致。 然后， 凝聚星辰能量， 如光速般移动。\n
    移动时， 隐夜·暗星以极快的速度对范围内最强的敌人进行多次旋转斩击。\n
    可以在地上和空中施放， 施放时， 连击点数累积到上限。\n
    可以在旋转斩击后， 消耗连击点数发动[终结之击]。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "影·万古星辰"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 9667]
    uuid = "ef9d26746effee9199b54541f01b8752"
    hasVP = False
    hasUP = False

    # 旋转斩击攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 13
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [终结之击]攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    group2 = "end"


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'rogue'
        self.nameCN = '隐夜·刺客'
        self.role = 'thief'
        self.角色 = '暗夜使者'
        self.职业 = '刺客'
        self.jobId = 'ddc49e9ad1ff72a00b53c6cff5b1e920'
        self.jobGrowId = '37495b941da3b1661bc900e68ef3b2c6'

        self.武器选项 = ['匕首', '双剑', '手杖']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '皮甲'
        self.buff = 1.84

        super().__init__(equVersion, __name__)
