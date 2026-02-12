#b9cb48777665de22c006fabaf9a560b3
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "archer/vigilante/cn/skillDetail"

# 凌跃一击
# archer/vigilante/0969cd4054d93da07708108c0cc1c4b5
# b9cb48777665de22c006fabaf9a560b3/0969cd4054d93da07708108c0cc1c4b5
class Skill0(ActiveSkill):
    """
        该技能可在地面和空中施放。\n
        向后微微跃起， 并根据武器的不同， 向地面发射不同的投射物， 使敌人浮空。\n
        攻击时， 有霸体判定； 转职为缪斯或奇美拉后， 技能类型变为独立攻击力。
    """
    name = "凌跃一击"
    learnLv = 1
    masterLv = 10
    maxLv = 20
    position = 3 #TODO
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
    hit5 = 0
    # [转职为奇美拉后]
    # 箭矢攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 冲击波攻击力 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)

    mode = ["人","妖兽"]

    def setMode(self, mode):
        if mode == "人":
            self.hit0 = self.hit0 = 1
            self.hit5 = 0
        elif mode == "妖兽":
            self.hit0 = self.hit0 = 0
            self.hit5 = 1

# 超越两界
# archer/vigilante/e0a072e8cef2d77893aad5f68aeed56a
# b9cb48777665de22c006fabaf9a560b3/e0a072e8cef2d77893aad5f68aeed56a
class Skill1(PassiveSkill):
    """
        既非人类又非妖兽， 但又同时属于两者的妖护使， 为了生存必须充分发挥其能力。\n
        改变基本攻击， 并可穿戴妖影弓。\n
        穿戴妖影弓的妖护使可通过基本攻击和技能获得妖兽形技能所需的妖气。
    """
    name = "超越两界"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 1 #TODO
    rangeLv = 3
    uuid = "e0a072e8cef2d77893aad5f68aeed56a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 妖兽化
# archer/vigilante/2a0a39184de92acf1c1375e00b77404c
# b9cb48777665de22c006fabaf9a560b3/2a0a39184de92acf1c1375e00b77404c
class Skill2(ActiveSkill):
    """
        妖护使变身为人形或妖兽， 当前为人形则转变成妖兽， 反之则由妖兽转变成人形。\n
        输入方向键时， 可朝对应方向移动并变身， 未输入方向键时会原地变身。\n
        学习该技能后， 使用和当前变身形态不符的技能时， 会自动变身并施放技能， 技能之间可以中断施放后的僵直时间。 无论当前的变身形态如何， 都可以中断技能的施放后僵直， 但觉醒技能除外。\n
        可在地面或空中施放。
    """
    name = "妖兽化"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 5 #TODO
    rangeLv = 1
    cd = 2.2
    mp = [3, 3]
    uuid = "2a0a39184de92acf1c1375e00b77404c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 妖痕抓击
# archer/vigilante/9dc8438e4572d39243c97da31c113acc
# b9cb48777665de22c006fabaf9a560b3/9dc8438e4572d39243c97da31c113acc
class Skill3(ActiveSkill):
    """
    [人形技能]\n
        妖护使将妖影弓变化为潜行形态， 挥舞由妖气形成的利刃。\n
        可在地面或空中施放。
    """
    name = "妖痕抓击"
    learnLv = 1
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 3
    mp = [7, 54]
    uuid = "9dc8438e4572d39243c97da31c113acc"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 妖气利刃攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 后跳
# archer/vigilante/7822d6d52e10964a6755f142c666b494
# b9cb48777665de22c006fabaf9a560b3/7822d6d52e10964a6755f142c666b494
class Skill4(ActiveSkill):
    """
        使自身向后方小跳并避开敌人的攻击。
    """
    name = "后跳"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 3 #TODO
    rangeLv = 1
    mp = [1, 1]
    uuid = "7822d6d52e10964a6755f142c666b494"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 基础精通
# archer/vigilante/5a56514f35cf0270ae8d6c65f8fefd78
# b9cb48777665de22c006fabaf9a560b3/5a56514f35cf0270ae8d6c65f8fefd78
class Skill5(PassiveSkill):
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

    associate = [{"type":"*skillDamage","data":[i-100 if i>0 else 0 for i in data0],"skills":["妖爪"]}]

# 受身蹲伏
# archer/vigilante/ce26c6b69d02a440a81b552bec94f03b
# b9cb48777665de22c006fabaf9a560b3/ce26c6b69d02a440a81b552bec94f03b
class Skill6(ActiveSkill):
    """
        使自身在倒地状态下迅速起身并采取蹲伏姿势； 蹲伏状态下， 自身会进入无敌状态， 效果持续一定时间。
    """
    name = "受身蹲伏"
    learnLv = 1
    masterLv = 10
    maxLv = 20
    position = 2 #TODO
    rangeLv = 1
    cd = 5
    mp = [1, 1]
    uuid = "ce26c6b69d02a440a81b552bec94f03b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 蹲伏姿势最短无敌时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 蹲伏姿势最长无敌时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 起身时霸体时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 防具精通
# archer/vigilante/892ef624d8bf3d7fc045f84825fd6104
# b9cb48777665de22c006fabaf9a560b3/892ef624d8bf3d7fc045f84825fd6104
class Skill7(PassiveSkill):
    """
        穿戴防具时， 可以增加各种属性。\n
        穿戴的防具越多， 效果越强； 可根据转职， 增加不同的属性种类及数值。
    """
    name = "防具精通"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "892ef624d8bf3d7fc045f84825fd6104"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 全力挥击
# archer/vigilante/4655101518604f874721b3cc249aae10
# b9cb48777665de22c006fabaf9a560b3/4655101518604f874721b3cc249aae10
class Skill8(ActiveSkill):
    """
        用力挥舞弓， 击打周围的敌人， 并向前推出。\n
    转职为猎人时， 再次按技能键会立即发射一枚爆炸箭矢， 造成额外伤害。\n
    转职为缪斯或奇美拉时， 技能类型变为独立攻击力。
    """
    name = "全力挥击"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 5
    mp = [28, 165]
    uuid = "4655101518604f874721b3cc249aae10"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 击打攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [转职为猎人后]
    # 爆炸箭矢攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 转职为猎人时， 爆炸箭矢射程 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 转职为猎人时， 爆炸箭矢爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 切割之影
# archer/vigilante/3fb8395ae3b81bd608e0c4223a8eb534
# b9cb48777665de22c006fabaf9a560b3/3fb8395ae3b81bd608e0c4223a8eb534
class Skill9(ActiveSkill):
    """
    [妖兽形技能]\n
        变身为妖兽的妖护使以迅雷不及掩耳的速度掠过敌人进行抓挠攻击。 成功击中敌人时， 落地后会转身出现在被击中的敌人里最强的敌人的身后。
    """
    name = "切割之影"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cd = 3
    mp = [5, 37]
    uuid = "3fb8395ae3b81bd608e0c4223a8eb534"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 抓挠多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 抓挠多段攻击次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 妖气能量消耗 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 移动距离 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 翻月翔击
# archer/vigilante/c9664191611af31142e052dfaef84530
# b9cb48777665de22c006fabaf9a560b3/c9664191611af31142e052dfaef84530
class Skill10(ActiveSkill):
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
    position = 2 #TODO
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

# 见面礼
# archer/vigilante/5806440d21e7546d50007a5ba11f8024
# b9cb48777665de22c006fabaf9a560b3/5806440d21e7546d50007a5ba11f8024
class Skill11(ActiveSkill):
    """
    [人形技能]\n
        妖护使将妖影弓变化为十字弩形态， 连续发射快速而锋利的妖气箭。\n
        可在地面或空中施放。
    """
    name = "见面礼"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 5
    mp = [19, 19]
    uuid = "5806440d21e7546d50007a5ba11f8024"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 妖气箭攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 妖气箭多段攻击次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 拒绝屏障
# archer/vigilante/d429147c372b549c3dadcabcba50787f
# b9cb48777665de22c006fabaf9a560b3/d429147c372b549c3dadcabcba50787f
class Skill12(ActiveSkill):
    """
    [人形/妖兽形技能]\n
        妖护使将妖气化为结晶覆盖全身， 拒绝对自己的所有攻击， 减少所受伤害。\n
        人形/妖兽形都可施放， 施放时短暂进入无敌状态， 持续按技能键可维持妖气结晶化状态。\n
        可在地面或空中施放。
    """
    name = "拒绝屏障"
    learnLv = 10
    masterLv = 5
    maxLv = 15
    position = 6 #TODO
    rangeLv = 2
    cd = 5
    mp = [17, 39]
    uuid = "d429147c372b549c3dadcabcba50787f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 所受伤害减少率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 妖气结晶化最大维持时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 强化 - 后跳
# archer/vigilante/2b340542e776818b78f3212af184bd6b
# b9cb48777665de22c006fabaf9a560b3/2b340542e776818b78f3212af184bd6b
class Skill13(PassiveSkill):
    """
    施放技能期间、 被击或倒地的状态下， 可以施放无敌状态的[后跳]。\n
    该能力适用与[后跳]不同的冷却时间， 并且不受冷却时间减少效果的影响。\n
    根据施放情况的不同(强制中断技能和被敌人攻击)， 进入不同冷却时间。\n
    无法强制中断觉醒技能和跳跃超过一定高度的技能。
    """
    name = "强化 - 后跳"
    learnLv = 10
    masterLv = 1
    maxLv = 1
    position = 4 #TODO
    rangeLv = 1
    cd = 30
    uuid = "2b340542e776818b78f3212af184bd6b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 强制中断技能时的冷却时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 被击或倒地期间施放时的冷却时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 跃翔
# archer/vigilante/1fea5a626f15230237946a11a9d11582
# b9cb48777665de22c006fabaf9a560b3/1fea5a626f15230237946a11a9d11582
class Skill14(ActiveSkill):
    """
        增加自身20%的跳跃力， 效果持续一定时间。\n
        效果持续期间内， 再次按技能键可以结束。
    """
    name = "跃翔"
    learnLv = 10
    masterLv = 1
    maxLv = 1
    position = 6 #TODO
    rangeLv = 3
    cd = 5
    mp = [13, 13]
    uuid = "1fea5a626f15230237946a11a9d11582"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)

# 妖爪
# archer/vigilante/7ec521d063d2190e1fcc5bd229af9bcf
# b9cb48777665de22c006fabaf9a560b3/7ec521d063d2190e1fcc5bd229af9bcf
class Skill15(ActiveSkill):
    """
    [人形/妖兽形技能]\n
        挥舞由妖气形成的利爪。\n
        人形/妖兽形都可施放， 人形可以在空中施放技能。\n
        技能受[基础精通]的影响。
    """
    name = "妖爪"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 5 #TODO
    rangeLv = 2
    cd = 2
    mp = [14, 14]
    uuid = "7ec521d063d2190e1fcc5bd229af9bcf"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 人形斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 妖兽形抓挠第一击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 0
    # 妖兽形抓挠第二击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 0
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    mode = ["人","妖兽"]

    def setMode(self, mode):
        if mode == "人":
            self.hit0 = 1
            self.hit1 = self.hit2 = 0
        elif mode == "妖兽":
            self.hit0 = 0
            self.hit1 = self.hit2 = 1

# 捕猎箭
# archer/vigilante/0113c8b1306ca76d208f83f2d093dd62
# b9cb48777665de22c006fabaf9a560b3/0113c8b1306ca76d208f83f2d093dd62
class Skill16(ActiveSkill):
    """
    [人形技能]\n
        对于妖护使来说， 理论上妖兽也许和同族无异。 但如果你问她， 她可能会回答这只是她最厌恶的猎物。\n
        将妖影弓变形为长弓形态， 发射强力的妖气结晶贯穿敌人， 并将敌人聚集在一起赋予强制控制状态。\n
        可在地面或空中施放。
    """
    name = "捕猎箭"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 7
    mp = [63, 457]
    uuid = "0113c8b1306ca76d208f83f2d093dd62"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 妖气结晶贯穿攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 妖气结晶爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 苦痛送行
# archer/vigilante/8b08f9504167a9c0f3a1d29d71b7943e
# b9cb48777665de22c006fabaf9a560b3/8b08f9504167a9c0f3a1d29d71b7943e
class Skill17(ActiveSkill):
    """
    [妖兽形技能]\n
        变身为妖兽的妖护使飞扑向前方敌人进行攻击后， 进入一段时间的强化状态。\n
        强化状态下增加攻击速度， 基本攻击变得更强。\n
        强化状态在持续时间结束或变身为人形时消失。
    """
    name = "苦痛送行"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cd = 10
    mp = [89, 653]
    uuid = "8b08f9504167a9c0f3a1d29d71b7943e"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 强化气息持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 突进攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 妖气能量消耗 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 突进距离比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 特殊体质
# archer/vigilante/ac21c02567f04a92b54dd85c091d1e5a
# b9cb48777665de22c006fabaf9a560b3/ac21c02567f04a92b54dd85c091d1e5a
class Skill18(PassiveSkill):
    """
        虽然不想承认， 但从生存的角度来看， 没有比这更好的体质了。\n
        妖护使的基本攻击和转职技能攻击力增加， 变身为妖兽形时， 增加移动速度和物理/魔法防御力。
    """
    name = "特殊体质"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 1 #TODO
    rangeLv = 3
    uuid = "ac21c02567f04a92b54dd85c091d1e5a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 妖兽形移动速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 妖兽形物理/魔法防御力增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [ {"data":data0,"type":"*skillDamage"}]

# 暴击
# archer/vigilante/fc1262c19f3d0477ee8eda47b8db8696
# b9cb48777665de22c006fabaf9a560b3/fc1262c19f3d0477ee8eda47b8db8696
class Skill19(PassiveSkill):
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

# 威慑低吼
# archer/vigilante/ab6fc3303df03b58911967dfca2b5d07
# b9cb48777665de22c006fabaf9a560b3/ab6fc3303df03b58911967dfca2b5d07
class Skill20(ActiveSkill):
    """
        对敌人表示出高度警戒， 全身毛发倒竖， 进入完全战斗状态。\n
        基本攻击和转职技能攻击力增加。
    """
    name = "威慑低吼"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 5 #TODO
    rangeLv = 3
    cd = 5
    uuid = "ab6fc3303df03b58911967dfca2b5d07"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和转职技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 破颜击
# archer/vigilante/c91a62dc0a18360acf5031ac0ebf09f5
# b9cb48777665de22c006fabaf9a560b3/c91a62dc0a18360acf5031ac0ebf09f5
class Skill21(ActiveSkill):
    """
    [人形技能]\n
        追踪进入妖护使警戒范围内最近的敌人。 成功追踪敌人时， 快速划破目标的面部后进行终结攻击， 拉开和敌人的距离。\n
        可在地面或空中施放。
    """
    name = "破颜击"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 6
    mp = [51, 371]
    uuid = "c91a62dc0a18360acf5031ac0ebf09f5"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 第一次斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第二次斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 终结攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 妖刺结阵
# archer/vigilante/0c3a468aee1f7ce06bf91eb3319518c1
# b9cb48777665de22c006fabaf9a560b3/0c3a468aee1f7ce06bf91eb3319518c1
class Skill22(ActiveSkill):
    """
    [妖兽形技能]\n
        变身为妖兽， 生成多个妖气利刃， 穿刺前方敌人。\n
        被妖气利刃击中的敌人会在一段时间内进入出血状态。
    """
    name = "妖刺结阵"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 8
    mp = [42, 309]
    uuid = "0c3a468aee1f7ce06bf91eb3319518c1"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 妖气利刃攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 妖气利刃多段攻击次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 出血攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 出血持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 妖气能量消耗 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 攻击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 利爪锋芒
# archer/vigilante/5cac3411ccef1af333953e0ded5e942d
# b9cb48777665de22c006fabaf9a560b3/5cac3411ccef1af333953e0ded5e942d
class Skill23(ActiveSkill):
    """
    [人形技能]\n
        接近妖护使的敌人将会尝到她隐藏起来的利爪的厉害。 将妖影弓变化为潜行形态， 横斩周围的敌人。\n
        可在地面或空中施放。
    """
    name = "利爪锋芒"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 7
    mp = [67, 487]
    uuid = "5cac3411ccef1af333953e0ded5e942d"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 横斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 横斩多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 巡猎终结
# archer/vigilante/85f7c810ad503790e8626439fe936d56
# b9cb48777665de22c006fabaf9a560b3/85f7c810ad503790e8626439fe936d56
class Skill24(ActiveSkill):
    """
    [人形技能]\n
        敌人是否终结并不是用眼睛确认的。 使用十字弩迅速射出两发弩箭， 然后变化为长弓作最后的射击。\n
        可在地面或空中施放。
    """
    name = "巡猎终结"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 9
    mp = [86, 627]
    uuid = "85f7c810ad503790e8626439fe936d56"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 十字弩妖气箭攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2
    # 十字弩妖气箭多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 长弓妖气箭攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 御蛇
# archer/vigilante/002cbdd9bfd0f0b970451ae8d48d029e
# b9cb48777665de22c006fabaf9a560b3/002cbdd9bfd0f0b970451ae8d48d029e
class Skill25(ActiveSkill):
    """
    [人形技能]\n
        将妖气化作毒蛇， 朝着猎物飞扑过去。\n
        每次攻击时， 妖气蛇都会探索新的敌人飞扑过去， 进行一定次数的攻击后消失。\n
        可在地面或空中施放。
    """
    name = "御蛇"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [170, 1242]
    uuid = "002cbdd9bfd0f0b970451ae8d48d029e"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 妖气蛇攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 首次施放时索敌范围 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 每次攻击后增加探索范围 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最大可攻击次数 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 探索范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [御蛇]\n
        最后一次攻击后若没有可追踪的敌人， 妖气箭会回到妖护使身边盘旋， 并给予妖护使有益的增益效果\n
        - 所受伤害 -20%\n
        - 移动速度 +20%\n
        - 环绕持续时间 : 5秒
        """
        ...

    def vp_2(self):
        """
        [御蛇]\n
        最后一次攻击后若没有可追踪的敌人， 妖气箭会回到妖护使身边盘旋， 等待新的追踪目标出现\n
        若有命中的目标， 妖气箭不会立即消失， 而是在目标周围盘旋并施加减益效果\n
        在盘旋期间， 若出现新的敌人， 则会追踪并攻击该敌人， 然后再次施加减益效果\n
        - 攻击速度 -30%\n
        - 移动速度 -30%\n
        - 盘旋持续时间 : 5秒
        """
        ...

# 幻妖之噬
# archer/vigilante/31823197cc0b04d4c5dcf8f928d9220c
# b9cb48777665de22c006fabaf9a560b3/31823197cc0b04d4c5dcf8f928d9220c
class Skill26(ActiveSkill):
    """
    [妖兽形技能]\n
        变身为妖兽的妖护使嗅到附近最强大猎物的气味， 飞扑上去一顿撕咬。\n
        命中的敌人会进入出血状态并恢复妖护使的生命值。\n
        可在地面或空中施放。
    """
    name = "幻妖之噬"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cube = 1
    cd = 10
    mp = [85, 621]
    uuid = "31823197cc0b04d4c5dcf8f928d9220c"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 飞扑攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 撕咬多段攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 3
    # 撕咬多段攻击次数 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 出血攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 出血持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 生命值恢复量 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 妖气能量消耗 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 索敌范围比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    def vp_1(self):
        """
        [幻妖之噬]\n
        大幅增加寻敌范围， 并适用单独的范围\n
        - 前方800px\n
        - 后方800px\n
        - 寻敌宽度500px\n
        最后一击变更为单段攻击\n
        - 总攻击力相同\n
        最后一击命中敌人时， 补充妖气能量\n
        - 妖气能量充能量 : 10
        """
        ...

    def vp_2(self):
        """
        [幻妖之噬]\n
        终结攻击后额外增加无敌时间\n
        命中的敌人是领主怪物时， 生命值恢复量增加\n
        - 生命值恢复量增加量 : 50%
        """
        ...

# 野性愈烈
# archer/vigilante/dac8d8207618150c162e4c6f9e168527
# b9cb48777665de22c006fabaf9a560b3/dac8d8207618150c162e4c6f9e168527
class Skill27(PassiveSkill):
    """
        不顾本人的意志， 被赋予的野性越来越强烈。\n
        妖护使的暴击伤害和暴击率增加， 命中率增加。
    """
    name = "野性愈烈"
    learnLv = 35
    masterLv = 10
    maxLv = 20
    position = 1 #TODO
    rangeLv = 3
    uuid = "dac8d8207618150c162e4c6f9e168527"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 暴击伤害增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 命中率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [ {"data":data0,"type":"*skillDamage"}]

# 狂妖风暴
# archer/vigilante/8e358ecf99ac9df31a6132aeafe378a9
# b9cb48777665de22c006fabaf9a560b3/8e358ecf99ac9df31a6132aeafe378a9
class Skill28(ActiveSkill):
    """
    [人形技能]\n
        妖护使跃向空中， 向地面发射妖气箭， 在地面爆炸的妖气引发强烈的妖气风暴， 吸附周围的敌人。 被妖气风暴击中的敌人会被强制控制。 在妖气风暴消失前再次按技能键， 将发动斩断风暴的终结斩击并结束技能。\n
        施放技能时， 可以通过方向键决定跳跃的方向。\n
        可在地面或空中施放。
    """
    name = "狂妖风暴"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cube = 1
    cd = 18
    mp = [237, 1732]
    uuid = "8e358ecf99ac9df31a6132aeafe378a9"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 妖气箭爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 妖气风暴多段攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 30
    # 妖气风暴多段攻击次数 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 终结斩击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [狂妖风暴]\n
        删除终结攻击， 终结攻击力合算至风暴多段攻击力\n
        - 总攻击力相同\n
        增加在风暴消失之前追踪周围敌人移动的功能\n
        风暴移动速度大幅增加\n
        风暴大小 +15%\n
        攻击敌人时妖气能量获取量 +12
        """
        ...

    def vp_2(self):
        """
        [狂妖风暴]\n
        终结攻击总共可以进行3次\n
        妖气风暴会在持续时间结束或进行最后终结攻击时消失\n
        - 总攻击力相同\n
        变更妖气能量的获取方式\n
        - 首次攻击时不获取妖气能量\n
        - 每次终结攻击时获取9妖气能量
        """
        ...

# 凶兽噬咬
# archer/vigilante/78b86e64fbb74c1db1b71c50a5ac21cd
# b9cb48777665de22c006fabaf9a560b3/78b86e64fbb74c1db1b71c50a5ac21cd
class Skill29(ActiveSkill):
    """
    [妖兽形技能]\n
        变身为妖兽的妖护使咬住附近最强敌人的脖子飞向空中， 身体生成大量妖气尖刺并进行旋转攻击， 随后和敌人一起冲向地面并产生强力冲击波。 最后， 对无力抵抗的敌人进行绝息撕咬。\n
        如果对象是无法抓取的敌人， 则不会飞向空中， 只适用旋转攻击和坠地冲击波攻击， 并将最后的绝息撕咬攻击力并入坠地冲击波攻击力中。\n
        被击中的敌人会在一段时间内进入出血状态。
    """
    name = "凶兽噬咬"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [163, 1190]
    uuid = "78b86e64fbb74c1db1b71c50a5ac21cd"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 旋转多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 旋转多段攻击次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 坠地冲击波攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 绝息撕咬攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 出血攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # 出血持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 妖气能量消耗 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 攻击范围比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    def vp_1(self):
        """
        [凶兽噬咬]\n
        妖兽原地变为妖气后消失， 随后出现在附近被锁定的敌人上方， 进行旋转攻击\n
        无论对象是否可被抓取， 删除绝息撕咬攻击， 绝息撕咬攻击力并入坠地冲击波攻击力\n
        - 总攻击力相同\n
        技能施放速度 +30%\n
        攻击范围 +30%
        """
        ...

    def vp_2(self):
        """
        [凶兽噬咬]\n
        变更为人形技能； 向前方灵活地斩击3次后， 进行终结斩击\n
        - 总攻击力 -5%\n
        - 按向前方向键时， 向前方移动并施放终结攻击\n
        - 可以在地面和空中施放\n
        - 删除妖气能量消耗量\n
        - 三连斩击获取8点妖气能量\n
        - 终结斩击获取12点妖气能量
        """
        self.skillRation *= 0.95

# 野息狂放
# archer/vigilante/f4a561e272cc434a4905b3aa0c0de090
# b9cb48777665de22c006fabaf9a560b3/f4a561e272cc434a4905b3aa0c0de090
class Skill30(PassiveSkill):
    """
        将部分压抑着的妖兽之力释放出来作为自身的力量， 并努力无视那一瞬间不知从何处传来的声音。\n
        妖护使的基本攻击和转职技能攻击力增加。\n
        [幻妖之噬]、 [鲜活宴场]的生命值恢复量增加。
    """
    name = "野息狂放"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 1 #TODO
    rangeLv = 3
    uuid = "f4a561e272cc434a4905b3aa0c0de090"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [幻妖之噬]生命值恢复量增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [鲜活宴场]生命值恢复量增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [ {"data":data0,"type":"*skillDamage"}]

# 鲜活宴场
# archer/vigilante/0e409ac3e1c1f3976b3ef2bfe4c13069
# b9cb48777665de22c006fabaf9a560b3/0e409ac3e1c1f3976b3ef2bfe4c13069
class Skill31(ActiveSkill):
    """
        缠绕妖护使身体的妖气幻化成茧的形态， 向四面八方伸出妖气触须， 从那些来不及躲避的可怜牺牲品身上夺取生命。 充分吸取敌人生命力来恢复自身生命值后， 妖护使制造出巨大的妖气刀刃， 斩断妖气茧回归人形。 被妖气触须击中的敌人会被强制控制。
    """
    name = "鲜活宴场"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [1406, 7707]
    uuid = "0e409ac3e1c1f3976b3ef2bfe4c13069"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 妖气触须攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 终结斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 生命值恢复量 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 妖气能量恢复 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 妖蛇暴雨
# archer/vigilante/4c5271b0ecce120d7fc113f377fae76f
# b9cb48777665de22c006fabaf9a560b3/4c5271b0ecce120d7fc113f377fae76f
class Skill32(ActiveSkill):
    """
    [人形技能]\n
        妖护使向天空发射充满妖气的箭， 大量妖气形成的蛇从空中倾泻而下， 搜索范围内的敌人并飞扑上去撕咬。
    """
    name = "妖蛇暴雨"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [277, 1520]
    uuid = "4c5271b0ecce120d7fc113f377fae76f"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 妖气蛇攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 20
    # 妖气蛇数量 : 20
    # [范围信息]
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [妖蛇暴雨]\n
        妖气箭不追击敌人， 而是直接在攻击范围内直射\n
        基本冷却时间变更为50秒\n
        总攻击力 +100%\n
        攻击范围 +50%\n
        妖气能量获取量 +24
        """
        self.cd = 50
        self.skillRation *= 2

    def vp_2(self):
        """
        [妖蛇暴雨]\n
        施放时， 直接从弓中倾泻出妖气箭\n
        施放技能时， 若[御蛇]技能处于可施放状态， 则无额外施放动作同时施放\n
        - 基本冷却时间变更为15秒\n
        - 妖气箭数量 -10个\n
        - 总攻击力 -40%\n
        - 可以在地面和空中施放\n
        - 妖气能量获取量 -8
        """
        self.cd = 15
        self.skillRation *= 0.6

# 盛怒狂潮
# archer/vigilante/2e2b7efe778656690f9c8cb6e47c3932
# b9cb48777665de22c006fabaf9a560b3/2e2b7efe778656690f9c8cb6e47c3932
class Skill33(ActiveSkill):
    """
    [妖兽形技能]\n
        因处于战斗的兴奋， 无法压抑的妖气溢出瞬间幻化成巨大的妖兽形态。 在前方生成巨大的结晶并击碎， 对被击中的敌人造成伤害。\n
        被终结攻击命中的敌人将会进入出血状态。
    """
    name = "盛怒狂潮"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [204, 1120]
    uuid = "2e2b7efe778656690f9c8cb6e47c3932"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 第一次打击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第二次打击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 终结打击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 出血攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 出血持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 妖气能量消耗 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 攻击范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [盛怒狂潮]\n
        不使用第1、 第2次攻击， 仅使用终结攻击\n
        - 总攻击力相同\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 25秒\n
        - 单次攻击力 -50%\n
        - 妖气能量消耗量 -22
        """
        self.cd = 25
        self.skillRation *= 0.5

    def vp_2(self):
        """
        [盛怒狂潮]\n
        施放技能后进入兴奋状态， 增加攻击速度和移动速度， 效果持续10秒\n
        - 攻击速度 +30%\n
        - 移动速度 +30%\n
        施放技能过程中所受伤害 -90%\n
        施放技能过程中控制型异常状态抗性 +100%
        """
        ...

# 妖人合一
# archer/vigilante/dde3b443bd5e61d90c34e5ee771e2c28
# b9cb48777665de22c006fabaf9a560b3/dde3b443bd5e61d90c34e5ee771e2c28
class Skill34(PassiveSkill):
    """
        妖护使开始理解和接受内心的妖兽， 变得可以自如地运用妖气。\n
        妖护使的基本攻击和转职技能攻击力增加。 此外， 在妖兽形态下可以在空中按跳跃键(C)再次进行跳跃， 使用[切割之影]技能不再消耗妖气。
    """
    name = "妖人合一"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 1 #TODO
    rangeLv = 3
    uuid = "dde3b443bd5e61d90c34e5ee771e2c28"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

    associate = [ {"data":data0,"type":"*skillDamage"}]

# 卸骨
# archer/vigilante/527cdc3ecca985e18ef819d456532b26
# b9cb48777665de22c006fabaf9a560b3/527cdc3ecca985e18ef819d456532b26
class Skill35(ActiveSkill):
    """
    [人形技能]\n
        妖护使快速藏匿进黑暗之中， 并在附近最强的敌人身后出现， 向目标深深地插入妖气刀刃后， 给予足以分离骨肉的强力终结斩击。\n
        施放技能时， 可通过方向键调整终结斩击的方向。
    """
    name = "卸骨"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 2 #TODO
    rangeLv = 2
    cube = 3
    cd = 38
    mp = [904, 4957]
    uuid = "527cdc3ecca985e18ef819d456532b26"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 刺击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 终结斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [卸骨]\n
        删除刺击攻击， 改为单段斩击攻击\n
        - 总攻击力相同\n
        长按技能键时， 可维持准备动作\n
        - 动作维持时间上限 : 2秒\n
        施放时进入无敌状态\n
        - 无敌状态持续时间 : 2秒\n
        单段斩击的妖气能量获取量 +6
        """
        ...

    def vp_2(self):
        """
        [卸骨]\n
        若存在被第1次斩击命中的敌人， 则发动第2次斩击时， 可根据充能的治疗能量恢复生命值\n
        第1次斩击后， 可以通过再次按下技能键发动第2次斩击\n
        - 治疗能量条充满时间 : 5秒\n
        - 充满后持续时间 : 5秒\n
        - 生命值恢复量上限 : 30%\n
        攻击范围 +30%\n
        寻敌范围 +30%
        """
        ...

# 妖芒之茧
# archer/vigilante/e788de1a4498c99fcc790302c4d41fed
# b9cb48777665de22c006fabaf9a560b3/e788de1a4498c99fcc790302c4d41fed
class Skill36(ActiveSkill):
    """
    [妖兽形技能]\n
        妖护使用坚硬的茧覆盖身体， 将锋利的妖气尖刺向四周发射， 瞬间穿透敌人。\n
        被妖气尖刺命中的敌人会进入强制控制状态， 收回尖刺时会被拉到妖护使身旁。\n
        命中敌人时， 妖护使恢复生命值。\n
        可在地面或空中施放。
    """
    name = "妖芒之茧"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [803, 4402]
    uuid = "e788de1a4498c99fcc790302c4d41fed"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 妖气尖刺攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 每击中1个敌人的生命值恢复量 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 妖气能量消耗 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [妖芒之茧]\n
        变更为可填充3次的技能\n
        - 每次填充冷却时间 : 15秒\n
        - 单次攻击力 -66.7%\n
        - 妖气能量消耗量 -32
        """
        self.cd = 15
        self.skillRation *= 1/3

    def vp_2(self):
        """
        [妖芒之茧]\n
        施放时， 在地面生成跟随妖护使的妖气地带\n
        进入妖气地带范围的敌人将被喷涌的妖气结晶刺穿并受到伤害， 并且每次攻击时妖护使都会恢复生命值\n
        - 妖气地带持续时间 : 30秒\n
        - 妖气结晶生成数量 : 10个\n
        - 每命中1名敌人生命值恢复量 : 2.5%\n
        - 在空中施放时， 落地后发动技能
        """
        ...

# 妖潮狂袭
# archer/vigilante/902a016f6978f13740f237e4740a5646
# b9cb48777665de22c006fabaf9a560b3/902a016f6978f13740f237e4740a5646
class Skill37(ActiveSkill):
    """
        尽情地释放体内的妖气， 破坏周围的一切。\n
        消耗当前所有的妖气能量， 根据消耗的妖气能量成比例增加技能攻击力。\n
        如果在妖气能量满格时施放， 技能表现会得到强化。
    """
    name = "妖潮狂袭"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2484, 13617]
    uuid = "902a016f6978f13740f237e4740a5646"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 妖气爆炸多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 15
    # 妖气爆炸多段攻击次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 消耗1点妖气的攻击力增加率 : 0.3%
    # 攻击力增加最大值 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 妖气能量消耗 : 全部

    mode = ["满强化","无强化"]

    def setMode(self, mode):
        if mode == "满强化":
            self.power0 = 1.3
        elif mode == "无强化":
            self.power0 = 1

# 万物巅峰
# archer/vigilante/370586038cf40378f20d338d507a780c
# b9cb48777665de22c006fabaf9a560b3/370586038cf40378f20d338d507a780c
class Skill38(PassiveSkill):
    """
        妖护使完全承认并接受内心妖兽的存在， 仿佛立身于万物之巅。\n
        基本攻击和转职技能攻击力增加。 [妖兽化/人形化]的妖气特效发生变化。 此外， [特殊体质]的物理/魔法防御力强化效果也适用于人形， [苦痛送行]基本攻击增加多段攻击次数和表现效果， 部分技能得到强化。\n
    [妖兽化/人形化]\n
        使用妖护使转职技能时， [妖兽化]/[人形化]技能冷却时间减少。\n
    [破颜击]\n
        第一次、 第二次斩击合并为一次斩击， 并减少终结斩击后的僵直时间。
    """
    name = "万物巅峰"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 1 #TODO
    rangeLv = 3
    uuid = "370586038cf40378f20d338d507a780c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

    associate = [ {"data":data0,"type":"*skillDamage"}]

# 神妖之爪
# archer/vigilante/dd32a9825ec1af42a91f2223be6658e5
# b9cb48777665de22c006fabaf9a560b3/dd32a9825ec1af42a91f2223be6658e5
class Skill39(ActiveSkill):
    """
    [人形/妖兽形技能]\n
        达到神妖境界之时， 即使是同样的力量也可以被以不同的方式使用。 在任何状态下都可以完美使用妖兽之力的妖护使， 根据自身目前的变身状态使用不同的力量。\n
    [人形施放时]\n
        在前方凝聚强大的妖气， 发射妖气箭。 妖气箭在命中敌人或飞行一段距离后旋转， 对周围敌人造成多段攻击伤害， 攻击会持续不断地补充妖气能量。\n
    [妖兽形施放时]\n
        爪子凝聚强烈的妖气拍打地面引发爆炸。 消耗当前所有的妖气能量， 根据消耗的妖气能量成比例增加技能攻击力。\n
        如果在妖气能量满格时施放， 技能表现会得到强化。
    """
    name = "神妖之爪"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [1406, 7710]
    uuid = "dd32a9825ec1af42a91f2223be6658e5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # [人形施放时]
    # 妖气箭多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 20
    # 妖气箭多段攻击次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 妖气箭终结爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [妖兽形施放时]
    # 地面打击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 0
    # 多段攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 0
    # 多段攻击次数 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 终结地面爆炸攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 0
    # 每消耗1点妖气的攻击力增加率 : 0.3%
    # 攻击力增加最大值 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 妖气能量消耗 : 全部

    mode = ["人","妖兽(满强化)","妖兽(无强化)"]

    def setMode(self, mode):
        if mode == "人":
            self.hit0 = 20
            self.hit2 = 1
            self.hit3 = self.hit4 = self.hit6 = 0
        elif mode == "妖兽(满强化)":
            self.hit0 = self.hit2 = 0
            self.hit3 = 1
            self.hit4 = 3
            self.hit6 = 1
            self.power3 = self.power4 = self.power6 = 1.3
        elif mode == "妖兽(无强化)":
            self.hit0 = self.hit2 = 0
            self.hit3 = 1
            self.hit4 = 3
            self.hit6 = 1
            self.power3 = self.power4 = self.power6 = 1

# 极夜·妖刃千散
# archer/vigilante/fa3ee243b36699e9d3fc34328adf6417
# b9cb48777665de22c006fabaf9a560b3/fa3ee243b36699e9d3fc34328adf6417
class Skill40(ActiveSkill):
    """
        对于拥有妖兽之力的人来说， 接受自身的存在就是与永恒的黑暗融为一体。\n
        投身于妖气之海的妖护使浓缩妖气的精髓制造出妖气刀刃后， 一跃而起， 挥舞着刀刃将闪烁着邪恶之光的恶意一刀两断。\n
        可在地面或空中施放。
    """
    name = "极夜·妖刃千散"
    learnLv = 100
    masterLv = 30
    maxLv = 40
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [3904, 17834]
    uuid = "fa3ee243b36699e9d3fc34328adf6417"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 下落多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 下落多段攻击次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 上斩攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 终结斩击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'vigilante'
        self.nameCN = '聆风·妖护使'
        self.role = 'archer'
        self.角色 = '弓箭手'
        self.职业 = '妖护使'
        self.jobId = 'b9cb48777665de22c006fabaf9a560b3'
        self.jobGrowId = 'c9b492038ee3ca8d27d7004cf58d59f3'

        self.武器选项 = ["妖影弓"] # TODO
        self.输出类型选项 = ["魔法百分比"] # TODO
        self.输出类型 = "魔法百分比" # TODO
        self.防具精通属性 = ["智力"] # TODO
        self.防具类型 = "布甲"
        self.buff = 2.00 # TODO

        super().__init__(equVersion, __name__)
