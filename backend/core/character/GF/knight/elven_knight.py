#0ee8fa5dc525c1a1f23fc6911e921e4a
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "knight/elven_knight/cn/skillDetail"

# class SKill(ActiveSkill):

#     剑盾加成 = 1.0
#     chain = 0

#     形态 = ["6c", "5c", "4c", "3c"]

#     def 形态变更(self, 形态, char: Character):
#         if (形态 == '' or 形态 not in self.形态) and len(self.形态) > 0:
#             形态 = self.形态[0]
#         if 形态 == "6c":
#             self.chain = 6
#         if 形态 == "5c":
#             self.chain = 5
#         if 形态 == "4c":
#             self.chain = 4
#         if 形态 == "3c":
#             self.chain = 3
#         self.剑盾加成 = 1 + self.chain * char.get_skill_by_name("剑盾猛攻").剑盾倍率()

#     def 等效百分比(self, **argv):
#         return super().等效百分比(**argv) * self.剑盾加成

class ActiveSkill(ActiveSkill):

    chain = 0

    chain_power = 0

    def skillInfo(self, char: Character):
        data = super().skillInfo(char)
        chainDamage = 1 + self.chain_power * self.chain
        return data[0],data[1] * chainDamage, data[2]

# 盾挑
# knight/elven_knight/3c5604bdbb0240b8f130f59ab40509c3
# 0ee8fa5dc525c1a1f23fc6911e921e4a/3c5604bdbb0240b8f130f59ab40509c3
class Skill0(ActiveSkill):
    """
    用盾牌攻击敌人并使其浮空。\n
    转职为混沌魔灵或龙骑士后， 技能类型变为独立攻击力。\n
    [帝国骑士的基本技能。\n
    与敌人对战时， 一边防守， 一边寻找敌人的弱点， 看准时机使用盾牌进行强力的攻击， 让敌人防不胜防。\n
    只有完全掌握盾挑的人才有资格当上骑士团团长， 千万不要小看这个技能。]
    """
    name = "盾挑"
    learnLv = 1
    masterLv = 10
    maxLv = 20
    position = 3 #TODO
    rangeLv = 3
    cd = 2
    uuid = "3c5604bdbb0240b8f130f59ab40509c3"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 盾牌挑击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 浮空力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    chain = 6

# 强踢
# knight/elven_knight/9dda3f4a849dba1a288dd65e116860f2
# 0ee8fa5dc525c1a1f23fc6911e921e4a/9dda3f4a849dba1a288dd65e116860f2
class Skill1(ActiveSkill):
    """
    使用脚踢攻击前方敌人， 威势之大甚至能够激起地上的沙石。\n
    沙石会使敌人进入失明和减速状态。 守护者在沙石的掩盖之下会增加回避率。\n
    [帝国的大竞技场中经常能够看到这个技能的身影。 虽然手段有些卑劣， 但是因为它的实用性， 即使是把名誉看的很重的骑士们也会使用。\n
    只有为了国家和君主愿意牺牲小我的人才是真正的骑士。]
    """
    name = "强踢"
    learnLv = 1
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 5
    mp = [2, 350]
    uuid = "9dda3f4a849dba1a288dd65e116860f2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 脚踢攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 减速几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 敌人移动速度减少 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 失明几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 失明持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 回避率增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    chain = 6

# 盾牌转换
# knight/elven_knight/8f73f243041c2d27739fe7696f02bf9b
# 0ee8fa5dc525c1a1f23fc6911e921e4a/8f73f243041c2d27739fe7696f02bf9b
class Skill2(ActiveSkill):
    """
    可以切换手中盾牌的样式。 完成盾牌任务后， 可以在装备栏中的盾牌库里可以要选择备选切换的盾牌。
    """
    name = "盾牌转换"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 2 #TODO
    rangeLv = 1
    cd = 10
    mp = [10, 10]
    uuid = "8f73f243041c2d27739fe7696f02bf9b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501



# 基础精通
# knight/elven_knight/5a56514f35cf0270ae8d6c65f8fefd78
# 0ee8fa5dc525c1a1f23fc6911e921e4a/5a56514f35cf0270ae8d6c65f8fefd78
class Skill4(PassiveSkill):
    """
    增加基本攻击、 前冲攻击、 跳跃攻击的攻击力。\n
    在决斗场中， 增益/减益技能、 被动技能的技能攻击力增加效果对[基础精通]无影响。
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

    associate = [{"type":"*skillDamage","data":[i-100 if i>0 else 0 for i in data0],"skills":["骑乘召唤"]}]


# 盾击
# knight/elven_knight/717f1e2104fe4b796f800352fa143ecc
# 0ee8fa5dc525c1a1f23fc6911e921e4a/717f1e2104fe4b796f800352fa143ecc
class Skill7(ActiveSkill):
    """
    挥舞盾牌对敌人进行强力攻击， 并使其进入眩晕状态。\n
    追加操作时可以提起盾牌向前突进。\n
    [厚重的盾牌本身就是一件强大的武器。 但如果你没有足够的力量的话还是放弃这个想法吧。]
    """
    name = "盾击"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 3
    mp = [5, 180]
    uuid = "717f1e2104fe4b796f800352fa143ecc"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 挥击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 眩晕几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 眩晕持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 追加操作时突进攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1

    chain = 6

# 命运之轮
# knight/elven_knight/4655101518604f874721b3cc249aae10
# 0ee8fa5dc525c1a1f23fc6911e921e4a/4655101518604f874721b3cc249aae10
class Skill8(ActiveSkill):
    """
    使用盾牌将敌人拉过来后， 将其挑至空中禁锢在命运之轮中。\n
    对无法抓取的敌人不适用控制效果。\n
    转职为混沌魔灵或龙骑士后， 技能类型变为独立攻击力。\n
    [命运之轮开始旋转了。]
    """
    name = "命运之轮"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 8
    mp = [5, 249]
    uuid = "4655101518604f874721b3cc249aae10"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 拉扯攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 挑飞攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 0
    # 命运之轮持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)

    mode = ['不可抓取','可抓取']

    def setMode(self, mode):
        if mode == "不可抓取":
            self.hit0 = 1
            self.hit1 = 0
        elif mode == "可抓取":
            self.hit0 = 1
            self.hit1 = 1

    chain = 6

# 自动防御
# knight/elven_knight/f2fb27162beb0b87a7cb9af7900e95f2
# 0ee8fa5dc525c1a1f23fc6911e921e4a/f2fb27162beb0b87a7cb9af7900e95f2
class Skill9(PassiveSkill):
    """
    学习此技能后， 在任何情况下都有几率抵挡敌人的攻击并降低所受伤害。\n
    [利剑和盾牌从来都不是骑士们杀伐的理由， 因为他们知道在利剑和盾牌的后面有着他们要保护的人。]
    """
    name = "自动防御"
    learnLv = 5
    masterLv = 10
    maxLv = 20
    position = 9 #TODO
    rangeLv = 5
    mp = [5, 250]
    uuid = "f2fb27162beb0b87a7cb9af7900e95f2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 格挡几率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 格挡成功时所受伤害减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 发动后的冷却时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 盾牌格挡
# knight/elven_knight/0969cd4054d93da07708108c0cc1c4b5
# 0ee8fa5dc525c1a1f23fc6911e921e4a/0969cd4054d93da07708108c0cc1c4b5
class Skill10(ActiveSkill):
    """
    使用盾牌格挡敌人的攻击。 防御成功时按下基本攻击键， 则会使用盾牌反击； 若按下前方向键， 则会使用手中的武器进行反击。\n
    反击后， 按住技能键可抓取敌人。\n
    [使用狭长的剑招架或使用宽而结实的盾牌格挡。\n
    如何抉择就看你自己了。]
    """
    name = "盾牌格挡"
    learnLv = 10
    masterLv = 1
    maxLv = 7
    position = 4 #TODO
    rangeLv = 5
    cd = 2
    mp = [10, 220]
    uuid = "0969cd4054d93da07708108c0cc1c4b5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 防御成功时伤害减少比率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 使用武器反击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 0
    # 使用武器反击时控制持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 使用盾牌反击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 盾牌反击眩晕几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 盾牌反击的眩晕时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)

    mode = ['盾牌反击','武器反击']

    def setMode(self, mode):
        if mode == "盾牌反击":
            self.hit1 = 0
            self.hit3 = 1
        elif mode == "武器反击":
            self.hit1 = 1
            self.hit3 = 0

    chain = 6

# 致命突刺
# knight/elven_knight/eb71e1d82d92c7e1d40500a0dcd77aa6
# 0ee8fa5dc525c1a1f23fc6911e921e4a/eb71e1d82d92c7e1d40500a0dcd77aa6
class Skill11(ActiveSkill):
    """
    对敌人施放强力的刺击。\n
    蓄气后发动， 可以增加攻击力、 突刺距离和范围。\n
    [原本为帝国贵族剑士所掌握的剑术。 帝国皇帝为了提升骑士团的战斗力， “奉劝”贵族们将秘传剑术传授给骑士们。 迫于压力， 贵族剑士只好将一些初级剑术传授给了骑士团。]
    """
    name = "致命突刺"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 3
    mp = [6, 250]
    uuid = "eb71e1d82d92c7e1d40500a0dcd77aa6"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 最大蓄气时攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 0
    # 蓄气时间上限 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 攻击范围比率 : {value3}% ~ {value4}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 攻击范围比率 : {value3}% ~ {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    chain = 6

    mode = ['常规','蓄气']

    def setMode(self, mode):
        if mode == "常规":
            self.hit0 = 1
            self.hit1 = 0
        elif mode == "蓄气":
            self.hit0 = 0
            self.hit1 = 1

# 跳斩
# knight/elven_knight/c9664191611af31142e052dfaef84530
# 0ee8fa5dc525c1a1f23fc6911e921e4a/c9664191611af31142e052dfaef84530
class Skill12(ActiveSkill):
    """
    向前方跳跃劈砍敌人。\n
    对倒地状态的敌人造成控制效果和更高的伤害。\n
    对无法抓取的敌人不适用控制效果。\n
    [这是骑士们在战场上寻找装死敌人时的常用技能， 可以让那些丧失抵抗能力的人毫无痛苦地死去。 怜悯， 也是骑士的美德之一。]
    """
    name = "跳斩"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 8 #TODO
    rangeLv = 2
    cd = 4
    mp = [7, 250]
    uuid = "c9664191611af31142e052dfaef84530"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 劈砍攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 对倒地状态的敌人的攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    
    chain = 6

# 飞跃截击
# knight/elven_knight/cfacda0647b9a0f595df2c2aad30c18d
# 0ee8fa5dc525c1a1f23fc6911e921e4a/cfacda0647b9a0f595df2c2aad30c18d
class Skill13(ActiveSkill):
    """
    快速的跳向空中的敌人， 并用盾牌将其击落， 并产生冲击波。\n
    [拿着厚重的盾牌， 怎么会跳得这样轻盈？]
    """
    name = "飞跃截击"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 1 #TODO
    rangeLv = 2
    cd = 3
    mp = [10, 220]
    uuid = "cfacda0647b9a0f595df2c2aad30c18d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 挥击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 冲击波范围 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    chain = 6

# 强化 - 后跳
# knight/elven_knight/2b340542e776818b78f3212af184bd6b
# 0ee8fa5dc525c1a1f23fc6911e921e4a/2b340542e776818b78f3212af184bd6b
class Skill14(PassiveSkill):
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
# knight/elven_knight/1fea5a626f15230237946a11a9d11582
# 0ee8fa5dc525c1a1f23fc6911e921e4a/1fea5a626f15230237946a11a9d11582
class Skill15(ActiveSkill):
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

# 防御姿态
# knight/elven_knight/45442bbbe33540b4deeec29437dae70c
# 0ee8fa5dc525c1a1f23fc6911e921e4a/45442bbbe33540b4deeec29437dae70c
class Skill16(PassiveSkill):
    """
    可以在盾牌格挡中进行移动和前冲。 被击一定次数后会解除防御姿态。\n
    - [转职为精灵骑士后追加功能] -\n
    用盾牌格挡成功时， [盾牌格挡]、 [自动防御]、 [铁壁推进]的冷却时间会减少； 施放[盾牌格挡]期间， 免疫异常状态。\n
    [进击吧！ 骑士！]
    """
    name = "防御姿态"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 4 #TODO
    rangeLv = 10
    uuid = "45442bbbe33540b4deeec29437dae70c"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 防御姿态的持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 所受伤害减少率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 防御次数上限 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 破武之轮
# knight/elven_knight/01c3a2fb793d293a25ed8dc7a0d70c1a
# 0ee8fa5dc525c1a1f23fc6911e921e4a/01c3a2fb793d293a25ed8dc7a0d70c1a
class Skill17(ActiveSkill):
    """
    挥剑向前方发射齿轮状的剑气。\n
    被击中的敌人会在一段时间内进入破武器状态。\n
    长按技能键可以蓄气施放， 蓄气时间越长， 破武器效果持续时间越长。\n
    [转职为精灵骑士后附加效果]\n
    始终具有最大蓄气效果。\n
    [冷风吹的越强， 行人却将围巾裹得越严实。\n
    而温暖的阳光照耀下来， 行人很快就把围巾拿掉了。]
    """
    name = "破武之轮"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 6
    mp = [9, 250]
    uuid = "01c3a2fb793d293a25ed8dc7a0d70c1a"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 蓄气时间上限 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 挥剑攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 剑气攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 0
    # 最小蓄气时破武器效果持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 最大蓄气时破武器效果持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 破武器几率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 破武器效果的敌人攻击力减少 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 剑气大小比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    chain = 6

    mode = ['不可抓取','可抓取']

    def setMode(self, mode):
        if mode == "不可抓取":
            self.hit1 = 1
            self.hit2 = 0
        elif mode == "可抓取":
            self.hit1 = 1
            self.hit2 = 1

# 骑乘召唤
# knight/elven_knight/a6c8f69107f8c4f5d1a0c7a57d000290
# 0ee8fa5dc525c1a1f23fc6911e921e4a/a6c8f69107f8c4f5d1a0c7a57d000290
class Skill18(ActiveSkill):
    """
    召唤并骑乘守护独角兽进行协同作战， 效果持续一段时间。\n
    骑乘时进入霸体状态， 当独角兽的体力变成0的时候会提前解除骑乘状态。\n
    守护独角兽的体力以精灵骑士生命值的一定比例适用， 骑乘状态的技能/技能攻击力受[基础精通]的影响。\n
    - 骑乘后技能 -\n
    [前跳]、 [后踢]、 [奔跑]、 [旋风刺]、 [解除骑乘]、 [刺击]
    """
    name = "骑乘召唤"
    learnLv = 15
    masterLv = 1
    maxLv = 11
    position = 2 #TODO
    rangeLv = 2
    cd = 120
    mp = [540, 872]
    uuid = "a6c8f69107f8c4f5d1a0c7a57d000290"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 独角兽持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 独角兽的生命值比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 骑乘状态第1击攻击力 : {value2}% x{value3}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 3
    # 骑乘状态第1击攻击力 : {value2}% x{value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 骑乘状态第2击攻击力 : {value4}% x{value5}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 3
    # 骑乘状态第2击攻击力 : {value4}% x{value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 骑乘状态第3击攻击力 : {value6}% x{value7}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 3
    # 骑乘状态第3击攻击力 : {value6}% x{value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 前冲多段攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    hit8 = 0
    # 刺击冷却时间 : {value9}秒
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 刺击攻击力 : {value10}% x{value11}
    data10 = get_data(f'{prefix}/{uuid}', 10)
    hit10 = 0
    # 刺击攻击力 : {value10}% x{value11}
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 蹄刺冲击波攻击力 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)
    hit12 = 0
    # 前跳攻击力 : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13)
    hit13 = 0
    # 前跳冲击波攻击力 : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)
    hit14 = 0
    # 后踢攻击力 : {value15}%
    data15 = get_data(f'{prefix}/{uuid}', 15)
    hit15 = 0
    # 奔跑多段攻击力 : {value16}%
    data16 = get_data(f'{prefix}/{uuid}', 16)
    hit16 = 0
    # 旋风刺攻击力 : {value17}%
    data17 = get_data(f'{prefix}/{uuid}', 17)
    hit17 = 0
    # 旋风刺多段攻击次数 : {value18}次
    data18 = get_data(f'{prefix}/{uuid}', 18)
    # [范围信息]
    # 蹄刺冲击波大小比率 : {value19}%
    data19 = get_data(f'{prefix}/{uuid}', 19)
    # 前跳冲击波大小比率 : {value20}%
    data20 = get_data(f'{prefix}/{uuid}', 20)
    # 后踢攻击范围比率 : {value21}%
    data21 = get_data(f'{prefix}/{uuid}', 21)
    # 旋风刺旋风大小比率 : {value22}%
    data22 = get_data(f'{prefix}/{uuid}', 22)

    chain = 0

    mode = ['平x一轮','前冲','刺击','践踏','前踏','后撩踢','奔袭','旋风刺击']

    def setMode(self, mode):
        if mode == "平x一轮":
            self.hit2 = self.hit4 = self.hit6 = 3
            self.hit8 = self.hit10 = self.hit12 = self.hit13 = self.hit14 = self.hit15 = self.hit16 = self.hit17  = 0
        elif mode == "前冲":
            self.hit2 = self.hit4 = self.hit6 = 0
            self.hit8 = 8
            self.hit10 = self.hit12 = self.hit13 = self.hit14 = self.hit15 = self.hit16 = self.hit17 = 0
        elif mode == "刺击":
            self.hit2 = self.hit4 = self.hit6 = 0
            self.hit8 = 0
            self.hit10 = 6
            self.hit12 = self.hit13 = self.hit14 = self.hit15 = self.hit16 = self.hit17 = 0
        elif mode == "践踏":
            self.hit2 = self.hit4 = self.hit6 = 0
            self.hit8 = 0
            self.hit10 = 0
            self.hit12 = 1
            self.hit13 = self.hit14 = self.hit15 = self.hit16 = self.hit17 = 0
        elif mode == "前踏":
            self.hit2 = self.hit4 = self.hit6 = 0
            self.hit8 = 0
            self.hit10 = 0
            self.hit12 = 0
            self.hit13 = 1
            self.hit14 = 1
            self.hit15 = self.hit16 = self.hit17 = 0
        elif mode == "后撩踢":
            self.hit2 = self.hit4 = self.hit6 = 0
            self.hit8 = self.hit10 = self.hit12 = self.hit13 = self.hit14 = 0
            self.hit15 = 1
            self.hit16 = self.hit17 = 0
        elif mode == "奔袭":
            self.hit2 = self.hit4 = self.hit6 = 0
            self.hit8 = 0
            self.hit10 = self.hit12 = self.hit13 = self.hit14 = self.hit15 = 0
            self.hit16 = 6
            self.hit17 = 0
        elif mode == "旋风刺击":
            self.hit2 = self.hit4 = self.hit6 = 0
            self.hit8 = 0
            self.hit10 = self.hit12 = self.hit13 = self.hit14 = self.hit15 = 0
            self.hit16 = 0
            self.hit17 = 10

            
# 愤怒冲撞
# knight/elven_knight/dcd536f1674630f01fc9667bb202b851
# 0ee8fa5dc525c1a1f23fc6911e921e4a/dcd536f1674630f01fc9667bb202b851
class Skill19(ActiveSkill):
    """
    以野蛮之力冲撞敌人， 并使敌人进入眩晕状态。
    """
    name = "愤怒冲撞"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 9
    mp = [15, 420]
    uuid = "dcd536f1674630f01fc9667bb202b851"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 突进攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 眩晕几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 眩晕时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 冲撞范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    chain = 6

# 骑士守护
# knight/elven_knight/23a5e0fba03283cb1b324a847b3fe370
# 0ee8fa5dc525c1a1f23fc6911e921e4a/23a5e0fba03283cb1b324a847b3fe370
class Skill20(PassiveSkill):
    """
    受到致命一击后， 会出现独角兽复活精灵骑士。\n
    独角兽会在一段时间内攻击敌人来保护精灵骑士。\n
    独角兽等级与当前精灵骑士的等级相同。 独角兽存在时， 精灵骑士的防御力会增加。\n
    可以用开启/关闭按钮立即让独角兽退场。
    """
    name = "骑士守护"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "23a5e0fba03283cb1b324a847b3fe370"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 复活时恢复生命值 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 复活冷却时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 独角兽持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 防御力增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 复活后的无敌状态持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 蔷薇护甲
# knight/elven_knight/0ed3148658fe37b3336ccb718dc0fdb0
# 0ee8fa5dc525c1a1f23fc6911e921e4a/0ed3148658fe37b3336ccb718dc0fdb0
class Skill21(ActiveSkill):
    """
    穿上蔷薇护甲， 被击时将伤害反弹给敌人， 效果持续一定时间。 玫瑰存在时增加自身硬直， 每次发射玫瑰刺时都会减少玫瑰的数量。\n
    [美丽玫瑰很可能是个甜蜜的陷阱， 一旦陷入， 便无法自拔。]
    """
    name = "蔷薇护甲"
    learnLv = 15
    masterLv = 20
    maxLv = 30
    position = 9 #TODO
    rangeLv = 3
    cd = [10, 10.4, 10.8, 11.2, 11.7, 12.1, 12.5, 12.9, 13.3, 13.7, 14.1, 14.6, 15, 15.4, 15.8, 16.2, 16.6, 17, 17.4, 17.9, 18.3, 18.7, 19.1, 19.5, 19.9, 20.3, 20.8, 21.2, 21.6, 22]
    mp = [7, 450]
    uuid = "0ed3148658fe37b3336ccb718dc0fdb0"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 发射玫瑰刺次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 玫瑰刺攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 硬直增加量 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 发射玫瑰刺的冷却时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 出血攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 出血持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 出血几率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

# 战吼
# knight/elven_knight/01384bbfc346775d1267fa0bc4ca605f
# 0ee8fa5dc525c1a1f23fc6911e921e4a/01384bbfc346775d1267fa0bc4ca605f
class Skill22(ActiveSkill):
    """
    发出战吼鼓舞自己。 增加攻击力和命中率， 效果持续一段时间。
    """
    name = "战吼"
    learnLv = 15
    masterLv = 20
    maxLv = 30
    position = 7 #TODO
    rangeLv = 3
    cd = 5
    uuid = "01384bbfc346775d1267fa0bc4ca605f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 命中率增加量 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 骑士信念
# knight/elven_knight/92360eab6e1f378902018eca681ac629
# 0ee8fa5dc525c1a1f23fc6911e921e4a/92360eab6e1f378902018eca681ac629
class Skill23(PassiveSkill):
    """
    骑士的信念在鼓舞着精灵骑士进行战斗， 减少除[天马流星落]、 [暮光之灵 : 黄昏独角兽]、 [生命之律·神木擎天]之外技能的冷却时间， 同时增加物理攻击力和物理暴击率。\n
    装备巨剑时， 减少魔法值消耗量。
    """
    name = "骑士信念"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 1 #TODO
    rangeLv = 5
    uuid = "92360eab6e1f378902018eca681ac629"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 冷却时间减少率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 武器物理攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 物理暴击率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 装备巨剑时魔法值消耗量减少 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    
    associate = [ 
        {"data":data0,"type":"*cdReduce", 'exceptSkills': ['天马流星落', '暮光之灵 : 黄昏独角兽', '生命之律·神木擎天']},
        {"data":data1,"type":"$*PAtkP"}
        ]

# 伟大的意志
# knight/elven_knight/506e7ed77d517419a6e1c437a2cedb17
# 0ee8fa5dc525c1a1f23fc6911e921e4a/506e7ed77d517419a6e1c437a2cedb17
class Skill24(ActiveSkill):
    """
    解除自身的异常状态。\n
    可解除感电、 石化、 束缚、 出血、 中毒、 诅咒、 冰冻、 减速、 失明、 睡眠、 灼伤、 混乱、 破武器、 破甲、 崩裂等异常状态。\n
    解除后的一段时间内增加对异常状态的免疫力。\n
    但无法解除或免疫部分特殊异常状态。
    """
    name = "伟大的意志"
    learnLv = 20
    masterLv = 1
    maxLv = 11
    position = 8 #TODO
    rangeLv = 5
    cd = 15
    mp = [10, 1280]
    uuid = "506e7ed77d517419a6e1c437a2cedb17"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 异常状态免疫力增加持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)

# 审判之盾
# knight/elven_knight/9bff7f2559e003766fee2853dca00631
# 0ee8fa5dc525c1a1f23fc6911e921e4a/9bff7f2559e003766fee2853dca00631
class Skill25(ActiveSkill):
    """
    将自然之力注入到盾牌内并挥舞盾牌攻击敌人。\n
    命中时使敌人进入审判状态， 攻击审判状态的敌人能造成额外伤害。\n
    审判状态持续一定时间或达到被击次数上限后消失。
    """
    name = "审判之盾"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 7
    mp = [20, 400]
    uuid = "9bff7f2559e003766fee2853dca00631"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 挥舞攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 攻击审判状态的敌人时攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 10
    # 审判状态持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 审判状态叠加次数上限 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    
    chain = 6

# 守护神鹿
# knight/elven_knight/762c4e6d030eaf0abbfe1fec2b298574
# 0ee8fa5dc525c1a1f23fc6911e921e4a/762c4e6d030eaf0abbfe1fec2b298574
class Skill26(ActiveSkill):
    """
    将神鹿精灵的力量赋予在利剑上对敌人进行攻击。\n
    被击中的敌人会受到多段攻击并浮空。
    """
    name = "守护神鹿"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 6
    mp = [10, 300]
    uuid = "762c4e6d030eaf0abbfe1fec2b298574"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 鹿角攻击力 : {value0}% x{value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 6
    # 鹿角攻击力 : {value0}% x{value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 神鹿大小 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    chain = 6

# 暴击
# knight/elven_knight/fc1262c19f3d0477ee8eda47b8db8696
# 0ee8fa5dc525c1a1f23fc6911e921e4a/fc1262c19f3d0477ee8eda47b8db8696
class Skill27(PassiveSkill):
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

# 破甲冲击
# knight/elven_knight/5dc7008b12a459325b548b0715c6b73c
# 0ee8fa5dc525c1a1f23fc6911e921e4a/5dc7008b12a459325b548b0715c6b73c
class Skill28(ActiveSkill):
    """
    产生强力的冲击波， 对周围的敌人造成伤害。\n
    可以在空中施放。\n
    在决斗场中， 只能在地面施放。
    """
    name = "破甲冲击"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cd = 7
    mp = [25, 480]
    uuid = "5dc7008b12a459325b548b0715c6b73c"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 冲击波攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 冲击波范围 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)
    
    chain = 6

# 自然守护
# knight/elven_knight/8ee0099656df08a0b39225f8a21d514b
# 0ee8fa5dc525c1a1f23fc6911e921e4a/8ee0099656df08a0b39225f8a21d514b
class Skill29(ActiveSkill):
    """
    因受到自然守护， 提升自身防御力， 持续一段时间。\n
    自然守护持续时间内， 自身处于霸体状态， 并增加物理防御力和魔法防御力。\n
    在决斗场被击一定次数后该效果消失， 减益效果持续时间内移动速度减慢。
    """
    name = "自然守护"
    learnLv = 25
    masterLv = 20
    maxLv = 30
    position = 9 #TODO
    rangeLv = 3
    cd = 30
    mp = [124, 346]
    uuid = "8ee0099656df08a0b39225f8a21d514b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理防御力增加量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 魔法防御力增加量 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [决斗场]
    # 被击次数上限 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 移动速度减少量 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 剑盾猛攻
# knight/elven_knight/3d8f3d438405d79f8d3ed68072674d1e
# 0ee8fa5dc525c1a1f23fc6911e921e4a/3d8f3d438405d79f8d3ed68072674d1e
class Skill30(ActiveSkill):
    """
    在一定时间内， 施放其他技能后会出现[剑盾猛攻]能量， 可以强制发动该技能， 无间断地对敌人进行盾牌攻击。\n
    盾牌攻击时可以向前移动进行推进攻击。\n
    成功按照指定时间点连续施放后， 下一次强制施放的技能攻击力会增加。 ([天马流星落]、 [暮光之灵 : 黄昏独角兽]、 [生命之律·神木擎天]不适用攻击力增加效果)\n
    在持续时间内成功发动技能时， 保留重叠次数； 失败时， 重叠次数消失。\n
    无法适用的技能 : [盾牌转换]、 [伟大的意志]、 [自然守护]、 [蔷薇护甲]、 [战吼]。\n
    对[剑盾猛攻]无影响的技能 : [受身蹲伏]、 [跃翔]、 [远古记忆]、 [不屈意志]、 [盾牌转换]、 [战吼]、 [蔷薇护甲]、 [伟大的意志]、 [自然守护]\n
    在决斗场中， 减少强制施放技能的攻击力。
    """
    name = "剑盾猛攻"
    learnLv = 30
    masterLv = 6
    maxLv = 16
    position = 3 #TODO
    rangeLv = 5
    cd = 5
    mp = [2, 75]
    uuid = "3d8f3d438405d79f8d3ed68072674d1e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 挥盾物理攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 推进物理攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 0
    # 强制施放技能时攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 技能攻击力增加效果重叠次数上限 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 攻击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    chain = 0

    mode = ['挥盾','推进']

    associate = [{"type":"+chainPower","data":data4}]

    def setMode(self, mode):
        if mode == "挥盾":
            self.hit1 = 1
            self.hit2 = 0
        elif mode == "推进":
            self.hit1 = 0
            self.hit2 = 1

# 神木刺击
# knight/elven_knight/1dad88963abdc96b091fcab185a8820d
# 0ee8fa5dc525c1a1f23fc6911e921e4a/1dad88963abdc96b091fcab185a8820d
class Skill31(ActiveSkill):
    """
    把树精灵的力量赋予在剑上， 向前发动刺击攻击。
    """
    name = "神木刺击"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 10
    mp = [30, 950]
    uuid = "1dad88963abdc96b091fcab185a8820d"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 刺击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 冲击波范围 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    chain = 6

# 精灵之跃
# knight/elven_knight/04883563896fe1adac7505c6146b5f59
# 0ee8fa5dc525c1a1f23fc6911e921e4a/04883563896fe1adac7505c6146b5f59
class Skill32(ActiveSkill):
    """
    跳起来冲向敌人， 并在落地时产生冲击波。\n
    蓄气后发动， 会增加跳跃距离。\n
    可以在空中施放。\n
    在决斗场中， 只能在地面施放。
    """
    name = "精灵之跃"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cd = 7.5
    mp = [30, 650]
    uuid = "04883563896fe1adac7505c6146b5f59"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 冲撞攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 蓄气时间上限 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 冲撞及冲击波范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 学习[生命的恩宠]后使用[剑盾猛攻]连接施放时， 追击距离上限比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    chain = 6

# 一刀两断
# knight/elven_knight/bb34e8854a93fd250347a1c64119f7ab
# 0ee8fa5dc525c1a1f23fc6911e921e4a/bb34e8854a93fd250347a1c64119f7ab
class Skill33(ActiveSkill):
    """
    爆发出强力的战意将前方敌人劈成两半。
    """
    name = "一刀两断"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [35, 1350]
    uuid = "bb34e8854a93fd250347a1c64119f7ab"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 战意攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 敌人断开时伤害 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 战意范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    chain = 6

    def vp_1(self):
        """
        [一刀两断]\n
        施放时只适用战意攻击\n
        - 总攻击力相同\n
        战意攻击攻击时， 向前方发射闪光\n
        - 闪光攻击力与战意攻击力相同\n
        - 战意攻击和闪光攻击为单次攻击
        """
        ...

    def vp_2(self):
        """
        [一刀两断]\n
        战意攻击会将命中的敌人拉向自己\n
        战意攻击范围 +50%
        """
        ...

# 铁壁推进
# knight/elven_knight/27bade584bb42fef68148d3a0b72bace
# 0ee8fa5dc525c1a1f23fc6911e921e4a/27bade584bb42fef68148d3a0b72bace
class Skill34(ActiveSkill):
    """
    将力量集中在盾牌上， 抵消敌人的攻击并保护身后队友。\n
    被盾牌碰到的敌人将受到伤害并被弹开， 使用技能后可以向前、 后方移动。\n
    在盾牌保护范围内的队员会减轻所受伤害， 并且不会发生僵直。 与精灵骑士的距离越近， 则受到的伤害越小。\n
    按住技能键时， 可发动持续推进； 松开技能键时， 则停止推进。
    """
    name = "铁壁推进"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [35, 1400]
    uuid = "27bade584bb42fef68148d3a0b72bace"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 持续时间上限 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击次数上限 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 所受伤害减少率 (物理) : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 所受伤害减少率 (魔法) : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 受保护队员与精灵骑士的距离上限 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 根据距离伤害减少率的适配值 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 与精灵骑士的距离 : {value7}px
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 根据距离伤害减少率的适配值 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [范围信息]
    # 保护领域大小比率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)

    chain = 6

    形态 = ["6c(秒断)", "5c(秒断)", "4c(秒断)", "3c(秒断)",
          "6c(满)", "5c(满)", "4c(满)", "3c(满)"]

    def 形态变更(self, 形态, char: Character):
        if (形态 == '' or 形态 not in self.形态) and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "6c(秒断)":
            self.hit0 = 1
            self.chain = 6
        if 形态 == "5c(秒断)":
            self.hit0 = 1
            self.chain = 5
        if 形态 == "4c(秒断)":
            self.hit0 = 1
            self.chain = 4
        if 形态 == "3c(秒断)":
            self.hit0 = 1
            self.chain = 3
        if 形态 == "6c(满)":
            self.hit0 = 18
            self.chain = 6
        if 形态 == "5c(满)":
            self.hit0 = 18
            self.chain = 5
        if 形态 == "4c(满)":
            self.hit0 = 18
            self.chain = 4
        if 形态 == "3c(满)":
            self.hit0 = 18
            self.chain = 3
        self.剑盾加成 = 1 + self.chain * char.get_skill_by_name("剑盾猛攻").剑盾倍率()

    def vp_1(self):
        """
        [铁壁推进]\n
        施放时进入无敌状态， 效果持续1秒\n
        保护范围 +30%
        """
        ...

    def vp_2(self):
        """
        [铁壁推进]\n
        施放时， [剑盾猛攻]连锁重叠数增加到6\n
        施放时， 瞬间发动盾牌挥击， 随后按住技能键时， 可发动不造成伤害的持续推进\n
        - 总攻击力相同\n
        所受伤害减少效果只适用于自身\n
        - 删除保护范围
        """
        self.setMode("6c(满)")

# 自然束缚
# knight/elven_knight/e49e57b2e8fbeceb0a2c56a0c63fe6c5
# 0ee8fa5dc525c1a1f23fc6911e921e4a/e49e57b2e8fbeceb0a2c56a0c63fe6c5
class Skill35(ActiveSkill):
    """
    在利剑上注入玫瑰藤条的力量后， 抛向前方的敌人， 将其捆绑并向己方拉回。\n
    被藤条击中的敌人有高几率进入束缚状态， 并无法移动。\n
    在决斗场被藤条束缚并拉回的敌人会倒地。
    """
    name = "自然束缚"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 9 #TODO
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [35, 750]
    uuid = "e49e57b2e8fbeceb0a2c56a0c63fe6c5"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 藤条捆绑的物理攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 束缚持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 束缚几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    chain = 6

    def vp_1(self):
        """
        [自然束缚]\n
        将剑插入地面， 使藤蔓从地面向周围所有方向生长\n
        拔剑的瞬间， 藤蔓迅速向中心收缩， 并将藤蔓上的敌人拉向中心\n
        藤蔓生长后施放[剑盾猛攻]时， 藤蔓不会立即消失， 而是会持续到将敌人拉过来为止
        """
        ...

    def vp_2(self):
        """
        [自然束缚]\n
        拉动藤蔓时， 不会吸附敌人，而是飞向被藤蔓抓取的敌人中最强的敌人\n
        范围 +30%
        """
        ...

# 飓风旋枪
# knight/elven_knight/03bb5314ffd41e9458d67ef924fef38f
# 0ee8fa5dc525c1a1f23fc6911e921e4a/03bb5314ffd41e9458d67ef924fef38f
class Skill36(ActiveSkill):
    """
    利用巨剑的旋转产生旋风， 同时将周围的敌人吸附过来并造成多段伤害。
    """
    name = "飓风旋枪"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [40, 2800]
    uuid = "03bb5314ffd41e9458d67ef924fef38f"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 旋转的持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 刺击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1= 2
    # 旋转攻击力 : {value2}% x{value3}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 10
    # 旋转攻击力 : {value2}% x{value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    chain = 6

    def vp_1(self):
        """
        [飓风旋枪]\n
        生成旋风后， 强制施放[剑盾猛攻]时旋风不会消失\n
        剑气大小 +30%
        """
        ...

    def vp_2(self):
        """
        [飓风旋枪]\n
        将剑插入地面旋转， 生成旋风\n
        - 删除刺击攻击\n
        - 范围内的敌人会被吸附至旋风中心\n
        - 总攻击力相同
        """
        ...

# 天陨断空斩
# knight/elven_knight/a5fa08f5d509e6ff2ebc68856a470b5a
# 0ee8fa5dc525c1a1f23fc6911e921e4a/a5fa08f5d509e6ff2ebc68856a470b5a
class Skill37(ActiveSkill):
    """
    使用强力的连锁攻击粉碎敌人。\n
    施放时发动旋转、 上劈攻击， 最后施放闪光下劈生成冲击波。
    """
    name = "天陨断空斩"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [80, 3500]
    uuid = "a5fa08f5d509e6ff2ebc68856a470b5a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 旋转劈砍攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 上劈攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 闪光下劈的攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 闪光下劈的冲击波攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 闪光下劈的冲击波大小 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    chain = 6

    def vp_1(self):
        """
        [天陨断空斩]\n
        上劈后， 在空中追踪并攻击周围最强的敌人\n
        - 按前/后方向键时， 向该方向搜寻敌人\n
        - 删除旋转劈砍\n
        - 总攻击力相同\n
        冲击波范围 +50%
        """
        ...

    def vp_2(self):
        """
        [天陨断空斩]\n
        施放技能过程中施放[生命审判]时， 会在冲击波生成时一同施放该技能\n
        - 适用于[天陨断空斩]的[剑盾猛攻]， 同样适用于一同施放的[生命审判]\n
        冲击波范围 +20%\n
        施放过程中所受伤害 -50%\n
        施放时[生命审判]冷却时间初始化\n
        [生命审判]\n
        攻击力 -40%
        """
        ...

# 自然恩泽
# knight/elven_knight/4b2c90ec226fd40e967875aa5eabefb2
# 0ee8fa5dc525c1a1f23fc6911e921e4a/4b2c90ec226fd40e967875aa5eabefb2
class Skill38(PassiveSkill):
    """
    世界树给予星辰之光庇护。\n
    星辰之光受到大自然的庇护， 增加攻击力、 移动速度、 攻击速度以及火、 冰、 光、 暗属性抗性。\n
    世界树会祝福独角兽， 增加[天马流星落]、 [暮光之灵 : 黄昏独角兽]、 [生命之律·神木擎天]的攻击力。
    """
    name = "自然恩泽"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 3
    uuid = "4b2c90ec226fd40e967875aa5eabefb2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 移动速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 所有属性抗性增加 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [天马流星落]攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [暮光之灵 : 黄昏独角兽]攻击力增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [生命之律·神木擎天]攻击力增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    associate = [
        {"data":data0,"type":"*skillDamage"},
        {"data":data4,"type":"*skillDamage","skills":['天马流星落']},
        {"data":data5,"type":"*skillDamage","skills":['暮光之灵 : 黄昏独角兽']},
        {"data":data6,"type":"*skillDamage","skills":['生命之律·神木擎天']}
    ]

# 天马流星落
# knight/elven_knight/1fadde0eece18649caddbca7bd58cc2f
# 0ee8fa5dc525c1a1f23fc6911e921e4a/1fadde0eece18649caddbca7bd58cc2f
class Skill39(ActiveSkill):
    """
    发动十字剑气后， 飞上天空骑乘天马珀伽索斯， 冲向地面歼灭敌人。\n
    可以使用方向键调整冲锋距离。\n
    施放时， 受到精灵的庇护， 恢复自身生命值和魔法值。
    """
    name = "天马流星落"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [400, 8400]
    uuid = "1fadde0eece18649caddbca7bd58cc2f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 一斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 二斩多段攻击力 : {value1}% x{value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 4
    # 二斩多段攻击力 : {value1}% x{value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 天马冲锋攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 生命值恢复 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 魔法值恢复 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    chain = 0

# 生命审判
# knight/elven_knight/dc1ffbe7bfcc6dc2be737951960da9ad
# 0ee8fa5dc525c1a1f23fc6911e921e4a/dc1ffbe7bfcc6dc2be737951960da9ad
class Skill40(ActiveSkill):
    """
    向前方跳跃， 引发生命爆炸， 对敌人造成伤害。\n
    按住技能键可以蓄气， 可以调整攻击时机， 并且可以保持蓄气姿态到最大持续时间。\n
    中断[剑盾猛攻]施放该技能时， 则会在原地向上跳跃并发动攻击。
    """
    name = "生命审判"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [450, 1560]
    uuid = "dc1ffbe7bfcc6dc2be737951960da9ad"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 蓄气持续时间上限 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 范围 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2)

    chain = 6

    def vp_1(self):
        """
        [生命审判]\n
        最后一击时立即恢复周围队友20%的生命值， 并生成生命领域5秒\n
        - 生命领域内的队友每秒恢复4%的生命值\n
        - 进入生命领域时队友增加5%的移动速度， 效果持续20秒
        """
        ...

    def vp_2(self):
        """
        [生命审判]\n
        不会跃起， 在原地直接猛击地面\n
        - 删除蓄气功能\n
        范围 +30%
        """
        ...

# 壁垒突袭
# knight/elven_knight/547ab2b2bd860d3e37355a9cfbc1077c
# 0ee8fa5dc525c1a1f23fc6911e921e4a/547ab2b2bd860d3e37355a9cfbc1077c
class Skill41(ActiveSkill):
    """
    用巨大的盾牌攻击敌人。\n
    攻击时， 盾牌会生成保护自身的屏障， 并使敌人进入失明状态。\n
    按前方向键， 可以竖起盾牌快速前冲攻击敌人。
    """
    name = "壁垒突袭"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 2
    cube = 3
    cd = 50
    mp = [935, 2360]
    uuid = "547ab2b2bd860d3e37355a9cfbc1077c"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 盾牌击打攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 盾牌破碎时攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 失明几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', "data_2")
    # 失明时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 屏障生命值 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 屏障持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 前冲距离上限 : {value6}px
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [范围信息]
    # 范围比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)

    chain = 6

    def vp_1(self):
        """
        [壁垒突袭]\n
        生成巨大的盾牌后， 出现古代野猪击碎盾牌， 向前方突进\n
        - 古代野猪攻击力与盾牌破碎攻击力相同\n
        - 只适用盾牌破碎或古代野猪突进1次攻击\n
        范围 +50%\n
        施放时， 初始化[愤怒冲撞]冷却时间\n
        [愤怒冲撞]\n
        攻击力 -14.3%
        """
        ...

    def vp_2(self):
        """
        [壁垒突袭]\n
        施放技能时进入无敌状态\n
        [壁垒突袭]屏障效果变更\n
        - 删除[壁垒突袭]屏障生命值\n
        - [壁垒突袭]屏障持续时间 -50%\n
        - [壁垒突袭]屏障持续期间所受伤害 -50%
        """
        ...

    def effect(self, old, new):
        if self.vp == 1:
            self.associate = [{"type":"*skillRation","data":[0] + [-14.3]*self.maxLv,"skills":["愤怒冲撞"]}]
        return super().effect(old, new)
    
# 信仰鼓舞
# knight/elven_knight/2c9d9a36c8401bddff6cdb80fab8dc24
# 0ee8fa5dc525c1a1f23fc6911e921e4a/2c9d9a36c8401bddff6cdb80fab8dc24
class Skill42(PassiveSkill):
    """
    [剑盾猛攻]连锁起始数增加到3， 并且[剑盾猛攻]的连锁数上限增加1。 同时增加大地女神的基本攻击力和技能攻击力。\n
    [防御是最好的攻击。]
    """
    name = "信仰鼓舞"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 3
    uuid = "2c9d9a36c8401bddff6cdb80fab8dc24"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # [剑盾猛攻]连锁起始数值 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 连锁数上限增加 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [ {"data":data0,"type":"*skillDamage"}] 

# 剑盾强袭
# knight/elven_knight/b89c9ab317bc0a443f6497b7cca2f6a8
# 0ee8fa5dc525c1a1f23fc6911e921e4a/b89c9ab317bc0a443f6497b7cca2f6a8
class Skill43(ActiveSkill):
    """
    把叠加在的[剑盾猛攻]的力量浓缩到盾牌中进行攻击。\n
    根据[剑盾猛攻]的阶段增加不同的伤害。 攻击后， [剑盾猛攻]的连锁将会被重置。
    """
    name = "剑盾强袭"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "b89c9ab317bc0a443f6497b7cca2f6a8"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [剑盾猛攻]连锁伤害额外增加 : +{value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    
    chain = 6

    # 剑盾强袭的剑盾猛攻倍率需额外处理，即在原剑盾猛攻倍率上+5%之和，再乘以剑盾层数
    def 形态变更(self, 形态, char: Character):
        if (形态 == '' or 形态 not in self.形态) and len(self.形态) > 0:
            形态 = self.形态[0]
        if 形态 == "6c":
            self.chain = 6
        if 形态 == "5c":
            self.chain = 5
        if 形态 == "4c":
            self.chain = 4
        if 形态 == "3c":
            self.chain = 3
        self.剑盾加成 = 1 + self.chain * char.get_skill_by_name("剑盾猛攻").剑盾倍率1()

    def vp_1(self):
        """
        [剑盾强袭]\n
        使用技能后， 可以连接[剑盾猛攻]\n
        - 在[剑盾猛攻]连锁数6层状态下施放[剑盾强袭]时， 2秒内连锁的所有区域变更为成功区域\n
        范围 +20%
        """
        ...

    def vp_2(self):
        """
        [剑盾强袭]\n
        施放时， 自动施放当前已学习的[自然守护]技能\n
        - 无论[自然守护]技能的冷却时间是否适用， 都会施放\n
        - 未学习[自然守护]技能状态下无法施放\n
        如果没有命中的敌人， 剩余冷却时间缩短为5秒\n
        施放过程中免疫异常状态
        """


# 自然之怒
# knight/elven_knight/7cf17936a039b418660424125dc968d7
# 0ee8fa5dc525c1a1f23fc6911e921e4a/7cf17936a039b418660424125dc968d7
class Skill44(ActiveSkill):
    """
    用盾牌对敌人进行攻击， 并召唤藤蔓束缚敌人。\n
    升起的藤蔓会拉拽周围的敌人并进行束缚。
    """
    name = "自然之怒"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "7cf17936a039b418660424125dc968d7"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 盾牌攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 藤蔓多段攻击力 : {value1}% x{value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 6
    # 藤蔓多段攻击力 : {value1}% x{value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 控制持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 藤蔓爆炸攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # [范围信息]
    # 范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    chain = 6

    def vp_1(self):
        """
        [自然之怒]\n
        可分别使用盾牌打击与藤蔓攻击\n
        - 施放技能时， 使用盾牌打击\n
        - 再次按技能键时， 使用藤蔓多段攻击与爆炸攻击\n
        - 施放技能后10秒内， 可以再次按技能键\n
        - 施放技能与再次按技能键时， 可连接[剑盾猛攻]\n
        - 对被藤蔓命中的敌人附加控制效果
        """
        ...

    def vp_2(self):
        """
        [自然之怒]\n
        删除盾牌攻击的攻击力\n
        - 保留附加控制效果的功能\n
        藤蔓攻击变更为沿地面向前方大范围生长的荆棘攻击\n
        - 多段攻击次数 -50%\n
        - 取消藤蔓爆炸攻击\n
        - 总攻击力相同\n
        - 对被荆棘攻击命中的敌人附加出血异常状态\n
        - 对被荆棘攻击命中的敌人附加额外控制效果
        """
        ...

# 暮光之灵 : 黄昏独角兽
# knight/elven_knight/7f80b887a09e88e2c4728c898bd73654
# 0ee8fa5dc525c1a1f23fc6911e921e4a/7f80b887a09e88e2c4728c898bd73654
class Skill45(ActiveSkill):
    """
    召唤古代幻兽——黄昏独角兽， 进行3段突击。 最后一次突击时， 独角兽会发出耀眼的星光， 并对大范围的敌人造成伤害。
    """
    name = "暮光之灵 : 黄昏独角兽"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "7f80b887a09e88e2c4728c898bd73654"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 突击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 突击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 星光多段攻击攻击力 : {value3}% x{value4}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 5
    # 星光多段攻击攻击力 : {value3}% x{value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)

    chain = 0

# 生命的恩宠
# knight/elven_knight/aa51c4ddf1659092fa9ed612b9837061
# 0ee8fa5dc525c1a1f23fc6911e921e4a/aa51c4ddf1659092fa9ed612b9837061
class Skill46(PassiveSkill):
    """
    皓曦·精灵骑士与大自然更深入地交流， 化作大自然的一部分， 通过尤迪亚的神物获得强大的生命之力。\n
    增加基本攻击力和转职技能攻击力， 部分技能获得附加效果。\n
    [剑盾猛攻]\n
    进入地下城时， 自动施放； 增加[剑盾猛攻]能量持续时间。 增加[剑盾猛攻]能量重叠持续区域， 减少[剑盾猛攻]成功时持续区域的减少量。\n
    增加盾牌攻击 (挥击、 推进攻击) 的Y轴范围； 盾牌攻击命中时， 敌人会被渐渐拉到皓曦·精灵骑士的前方。\n
    [精灵之跃]\n
    使用[剑盾猛攻]强制中断后施放时， 冲撞判定和攻击消失， 追击命中的敌人当中最强大的敌人。\n
    无法追击一定范围之外的敌人； 发动追击功能时， 无法蓄气后使用。
    """
    name = "生命的恩宠"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "aa51c4ddf1659092fa9ed612b9837061"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [剑盾猛攻]能量持续时间 : +5秒

    associate = [ {"data":data0,"type":"*skillDamage"} ]

# 荆棘之城
# knight/elven_knight/863295a0fc634cf5fcc01e82a735fd6b
# 0ee8fa5dc525c1a1f23fc6911e921e4a/863295a0fc634cf5fcc01e82a735fd6b
class Skill47(ActiveSkill):
    """
    挥动尤迪亚神物之一的尤迪亚的树皮进行攻击。 命中敌人时， 尤迪亚的树皮分散成碎片， 在前方地面扎根， 如同尖刺般生长并攻击敌人； 未命中时， 向前方撒下附着在尤迪亚的树皮上的种子， 种子如同尖刺般生长并攻击敌人。\n
    施放时， [剑盾猛攻]连锁重叠数增加到6。
    """
    name = "荆棘之城"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [800, 6667]
    uuid = "863295a0fc634cf5fcc01e82a735fd6b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 盾牌挥击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 根部攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

    chain = 6

# 生命之律·神木擎天
# knight/elven_knight/3153ca0e6752a6283412c59c5ec8e002
# 0ee8fa5dc525c1a1f23fc6911e921e4a/3153ca0e6752a6283412c59c5ec8e002
class Skill48(ActiveSkill):
    """
    用和平之树尤迪亚的树皮锤击地面， 创造出生命庭院。 然后， 跳跃到在生命庭院中生长的尤迪亚的顶端， 装备尤迪亚的神物“伟大自然”后， 撞击地面， 使周围充满大自然的气息。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "生命之律·神木擎天"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "3153ca0e6752a6283412c59c5ec8e002"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 生命庭院铺开攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 伟大自然地面撞击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 冲击波多段攻击力 : {value2}% x{value3}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 6
    # 冲击波多段攻击力 : {value2}% x{value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'elven_knight'
        self.nameCN = '皓曦·精灵骑士'
        self.role = 'knight'
        self.角色 = '守护者'
        self.职业 = '精灵骑士'
        self.jobId = '0ee8fa5dc525c1a1f23fc6911e921e4a'
        self.jobGrowId = '37495b941da3b1661bc900e68ef3b2c6'

        self.武器选项 = ['巨剑', '钝器', '太刀', '短剑'] # TODO
        self.输出类型选项 = ['物理百分比'] # TODO
        self.输出类型 = '物理百分比' # TODO
        self.防具精通属性 = ['力量'] # TODO
        self.防具类型 = '板甲'
        self.buff = 2.103 # TODO

        super().__init__(equVersion, __name__)
