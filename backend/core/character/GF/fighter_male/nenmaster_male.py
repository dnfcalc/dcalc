#ca0f0e0e9e1d55b5f9955b03d9dd213c
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "fighter_male/nenmaster_male/cn/skillDetail"

# 光之亲和
# fighter_male/nenmaster_male/da6e37c1e3f0e8867f70007d89c239ff
# ca0f0e0e9e1d55b5f9955b03d9dd213c/da6e37c1e3f0e8867f70007d89c239ff
class Skill1(PassiveSkill):
    """
    强化对光的亲和力， 可以增加自身的光属性抗性， 但暗属性抗性将减少。
    """
    name = "光之亲和"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 9
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
# fighter_male/nenmaster_male/27bade584bb42fef68148d3a0b72bace
# ca0f0e0e9e1d55b5f9955b03d9dd213c/27bade584bb42fef68148d3a0b72bace
class Skill2(PassiveSkill):
    """
    增加[念气波]感电几率， 用念气侦察敌人的位置， 提高失明抗性。
    """
    name = "念气感知"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 8
    rangeLv = 1
    uuid = "27bade584bb42fef68148d3a0b72bace"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 失明抗性增加 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 念气波感电几率 : 当前感电几率的3倍


# 基础精通
# fighter_male/nenmaster_male/5a56514f35cf0270ae8d6c65f8fefd78
# ca0f0e0e9e1d55b5f9955b03d9dd213c/5a56514f35cf0270ae8d6c65f8fefd78
class Skill5(PassiveSkill):
    """
    增加基本攻击、 前冲攻击、 跳跃攻击、 [后踢]的攻击力。\n
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

    associate = [{"type":"*skillDamage","data":[i-100 if i>0 else 0 for i in data0],"skills":["念兽 : 龙虎啸"]}]


# 分身
# fighter_male/nenmaster_male/f2fb27162beb0b87a7cb9af7900e95f2
# ca0f0e0e9e1d55b5f9955b03d9dd213c/f2fb27162beb0b87a7cb9af7900e95f2
class Skill9(ActiveSkill):
    """
    生成分身扰乱敌人的攻击或阻挡子弹。\n
    经过一定时间或受一定伤害后， 生成的分身消失。\n
    转职成气功师后， 可以学习[幻影爆碎]技能。
    """
    name = "分身"
    learnLv = 5
    masterLv = 10
    maxLv = 20
    position = 4
    rangeLv = 3
    cd = 7
    mp = [6, 84]
    uuid = "f2fb27162beb0b87a7cb9af7900e95f2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 分身持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 分身生成数量 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def skillInfo(self, mode: str | None = None):
        self.hit2 = self.data1[self.lv]
        self.data2 = [0] + [1] * self.maxLv
        return super().skillInfo(mode)

# 蹲伏
# fighter_male/nenmaster_male/9dda3f4a849dba1a288dd65e116860f2
# ca0f0e0e9e1d55b5f9955b03d9dd213c/9dda3f4a849dba1a288dd65e116860f2
class Skill11(ActiveSkill):
    """
    蹲下并避开敌人的上段判定式攻击。\n
    若在前冲中使用此技能， 可以边向前滑行边蹲下。\n
    蹲下时进入无敌状态， 起身的瞬间也会进入无敌状态。\n
    [蹲伏]姿势中按攻击键， 可以用肩尖撞击敌人； 经过一定时间或按跳跃键可以中断蹲伏状态。
    """
    name = "蹲伏"
    learnLv = 10
    masterLv = 1
    maxLv = 11
    position = 7
    rangeLv = 1
    cd = 3
    mp = [3, 4]
    uuid = "9dda3f4a849dba1a288dd65e116860f2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 姿势持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 肩撞攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 钢筋铁骨
# fighter_male/nenmaster_male/c9664191611af31142e052dfaef84530
# ca0f0e0e9e1d55b5f9955b03d9dd213c/c9664191611af31142e052dfaef84530
class Skill12(PassiveSkill):
    """
    使自身的身体强悍如钢铁， 并增加一定的物防和体力。 被击时， 有一定几率使自身进入霸体状态。
    """
    name = "钢筋铁骨"
    learnLv = 10
    masterLv = 50
    maxLv = 60
    position = 5
    rangeLv = 3
    uuid = "c9664191611af31142e052dfaef84530"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 增加物理防御力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 增加体力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 霸体发动几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 雷霆踏
# fighter_male/nenmaster_male/45442bbbe33540b4deeec29437dae70c
# ca0f0e0e9e1d55b5f9955b03d9dd213c/45442bbbe33540b4deeec29437dae70c
class Skill19(ActiveSkill):
    """
    把雷电之力注入腿部， 用力进行下劈攻击。\n
    踢击地点会落下闪电， 对敌人造成伤害， 并让敌人进入感电状态。
    """
    name = "雷霆踏"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cd = 7
    mp = [20, 168]
    uuid = "45442bbbe33540b4deeec29437dae70c"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 雷霆踏攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [感电效果]
    # 感电攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 感电几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 感电持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 闪电大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 念气波
# fighter_male/nenmaster_male/01c3a2fb793d293a25ed8dc7a0d70c1a
# ca0f0e0e9e1d55b5f9955b03d9dd213c/01c3a2fb793d293a25ed8dc7a0d70c1a
class Skill20(ActiveSkill):
    """
    使念气实体化后向前方敌人发射。\n
    念气命中敌人后会引发爆炸并对周围敌人造成光属性魔法伤害， 而且有一定几率使敌人进入感电状态。\n
    转职为气功师后， 可以强制中断基本攻击和前冲攻击动作， 并立即施放该技能， 同时可以学习[蓄念炮]。
    """
    name = "念气波"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 2.5
    mp = [15, 154]
    uuid = "01c3a2fb793d293a25ed8dc7a0d70c1a"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 念气弹攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [感电效果]
    # 感电攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 感电几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 感电持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 念气弹大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 射程距离 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)

    mode = ["蓄力","普通"]

    def setMode(self, mode):
        if mode == "蓄力":
            if self.char.GetSkillByName("蓄念炮").lv == 0:
                self.skillRation *= 0
                return
            self.cd = 6.5
        elif mode == "普通":
            self.cd = 2.5
            self.power0 = 1

# 念气流转
# fighter_male/nenmaster_male/04883563896fe1adac7505c6146b5f59
# ca0f0e0e9e1d55b5f9955b03d9dd213c/04883563896fe1adac7505c6146b5f59
class Skill22(ActiveSkill):
    """
    通过纹饰施术师纹的纹饰强制改变体内的念气流动， 暂时增加武器魔法攻击力、 属性攻击力、 攻击速度和施放速度。\n
    强制改变念气流动的副作用导致体力下降。
    """
    name = "念气流转"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 3
    cd = 5
    uuid = "04883563896fe1adac7505c6146b5f59"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 属性攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 魔法攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 体力减少 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 攻击速度增加 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 施放速度增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    associate = [
        {"type":"$*PAtkM","data":[0]+[48.7]*maxLv},
        {"data":[0]+[21]*maxLv},
        ]

# 念气环绕
# fighter_male/nenmaster_male/0ed3148658fe37b3336ccb718dc0fdb0
# ca0f0e0e9e1d55b5f9955b03d9dd213c/0ed3148658fe37b3336ccb718dc0fdb0
class Skill23(ActiveSkill):
    """
    生成念气珠环绕在自身周围， 可以使敌人受到一定的魔法伤害。\n
    念气珠自动生成， 并持续消耗魔法值。\n
    增加基本攻击力、 技能攻击力和物理防御力。\n
    再次按技能键， 可以直接关闭念气珠。
    """
    name = "念气环绕"
    learnLv = 20
    masterLv = 25
    maxLv = 35
    position = 2
    rangeLv = 3
    cd = 4
    mp = [5, 210]
    uuid = "0ed3148658fe37b3336ccb718dc0fdb0"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 念气珠持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 念气珠攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 每个念气珠增加物防 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 念气珠自动生成周期 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)


    data5 = data2
    hit5 = 0

    associate = [{"data":data0}]

    mode = ["常规","御"]

    def setMode(self, mode):
        if mode == "御":
            self.hit5 = 10
            self.hit2 = 0

    def getSkillCD(self,mode=None):
        return 1.0

# 蓄念炮
# fighter_male/nenmaster_male/c7bf7ccab413009640e65ca6f2f0263a
# ca0f0e0e9e1d55b5f9955b03d9dd213c/c7bf7ccab413009640e65ca6f2f0263a
class Skill24(PassiveSkill):
    """
    使念气波变成可以蓄气的念气波， 蓄气完毕后， 可以大幅度增加念气波的大小、 攻击力和射程， 并100%穿刺敌人； 但冷却时间比普通念气波长。
    """
    name = "蓄念炮"
    learnLv = 20
    masterLv = 1
    maxLv = 11
    position = 3
    rangeLv = 1
    cd = 6.5
    mp = [40, 56]
    uuid = "c7bf7ccab413009640e65ca6f2f0263a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 念气波攻击力变化率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 念气波持续时间增加 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 发射速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [ {"type":"*power0","data":data0,"skills":["念气波"]} ]

# 念气罩
# fighter_male/nenmaster_male/dc1ffbe7bfcc6dc2be737951960da9ad
# ca0f0e0e9e1d55b5f9955b03d9dd213c/dc1ffbe7bfcc6dc2be737951960da9ad
class Skill27(ActiveSkill):
    """
    在自身周围生成一个巨大的念气守护罩， 使守护罩内的所有队员进入无敌状态。\n
    经过一段时间或受到一定伤害后， 念气罩就会消失。\n
    念气罩生成后施放者可以移动， 但念气罩不会跟随移动； 念气罩消失过程中， 效果也会消失。
    """
    name = "念气罩"
    learnLv = 25
    masterLv = 1
    maxLv = 11
    position = 5
    rangeLv = 3
    mp = [60, 560]
    uuid = "dc1ffbe7bfcc6dc2be737951960da9ad"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 念气罩持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 念气罩生命值 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 念气罩攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 念气罩范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 念气环绕 : 袭
# fighter_male/nenmaster_male/d429147c372b549c3dadcabcba50787f
# ca0f0e0e9e1d55b5f9955b03d9dd213c/d429147c372b549c3dadcabcba50787f
class Skill28(ActiveSkill):
    """
    向前方敌人发射攻击力强化的念气珠。 念气珠在敌人附近旋转一定时间后会再次回到施放者周围。\n
    [念气环绕 : 御]状态下， 攻击力增加量无法叠加。\n
    学习[禅意·万象]后\n
    存在敌人时， 在追击的敌人周围生成念气并引爆， 对敌人造成伤害。
    """
    name = "念气环绕 : 袭"
    learnLv = 25
    masterLv = 1
    maxLv = 11
    position = 2
    rangeLv = 2
    cd = 4.5
    mp = [75, 630]
    uuid = "d429147c372b549c3dadcabcba50787f"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 念气珠攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 对敌人生成的念气珠维持时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 学习[禅意·万象]后
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 可以锁定的X轴距离 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 可以锁定的Y轴距离 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 可以锁定的Z轴距离 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 学习[禅意·万象]后锁定范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

# 念雷轰
# fighter_male/nenmaster_male/8c10cefa65364880451e389bb74d3600
# ca0f0e0e9e1d55b5f9955b03d9dd213c/8c10cefa65364880451e389bb74d3600
class Skill29(ActiveSkill):
    """
    聚集念能量后向前方释放。释放的念能量对敌人造成多段伤害， 使敌人进入感电状态。\n
    释放念能量的瞬间附近敌人非霸体状态时， 将敌人击退至前方。
    """
    name = "念雷轰"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cd = 7
    mp = [20, 168]
    uuid = "8c10cefa65364880451e389bb74d3600"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 释放攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 释放多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [感电效果]
    # 感电攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 4
    # 感电几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 感电持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 旋风腿
# fighter_male/nenmaster_male/202edb928046f4fa6dedf6337377efd5
# ca0f0e0e9e1d55b5f9955b03d9dd213c/202edb928046f4fa6dedf6337377efd5
class Skill30(ActiveSkill):
    """
    在原地快速旋转身体并用连续的扫腿攻击周围的敌人； 可以在地面或空中使用， 对命中的敌人有吸附效果。\n
    施放后不能移动， 可以按跳跃键中断技能。\n
    转职成为散打时， 才可以强制中断基本攻击动作， 并立即施放该技能。
    """
    name = "旋风腿"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 8
    mp = [50, 420]
    uuid = "202edb928046f4fa6dedf6337377efd5"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 旋风腿攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 10
    # 攻击次数 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 幻影爆碎
# fighter_male/nenmaster_male/f0cc2c950f3bdf4103c75fa496bcac34
# ca0f0e0e9e1d55b5f9955b03d9dd213c/f0cc2c950f3bdf4103c75fa496bcac34
class Skill31(PassiveSkill):
    """
    学习[幻影爆碎]后， 增加分身的冷却时间。 施放时， 分身会转换为一个念气球在融合后爆炸。\n
    爆炸攻击力和范围会随着融合的分身数量增加。 分身的数量与当前[分身]生成的分身数量相同， 且分身在爆炸后消失。\n
    可以中断基本攻击并立即施放[分身]技能。\n
    在决斗场， 学习[幻影爆碎]后减少分身的冷却时间， 并无法使用立即爆炸功能。
    """
    name = "幻影爆碎"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    uuid = "f0cc2c950f3bdf4103c75fa496bcac34"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # [幻影爆碎]冷却时间 : 12秒
    # 每个分身爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [范围信息]
    # 分身爆炸大小比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [
        {"type": "*skillDamage","data":data0,"skills":["分身"],"ratio":1},
        {"type": "+cd","data":[0]+[5]*maxLv,"skills":["分身"],"ratio":1}
    ]

# 念兽 : 龙虎啸
# fighter_male/nenmaster_male/1b1cfab062e0768bcc889e33e1f30dbf
# ca0f0e0e9e1d55b5f9955b03d9dd213c/1b1cfab062e0768bcc889e33e1f30dbf
class Skill32(ActiveSkill):
    """
    召唤出念兽龙虎， 强化自身能力。\n
    此状态下， 可以使基本攻击增加至5次， 而且基本攻击、 前冲攻击、 跳跃攻击时， 与龙虎一起进行攻击。\n
    基本攻击、 前冲攻击、 跳跃攻击时， 适用念兽龙虎的攻击力。\n
    同时还可以使前冲攻击、 跳跃攻击和最后一次基本攻击命中的敌人进入感电状态。\n
    自身的攻击范围会增加， 并且基本攻击、 跳跃攻击、 前冲攻击变更为受[基础精通]影响的魔法攻击。\n
    增加基本攻击力、 技能攻击力、 移动速度、 物理防御力和魔法防御力。\n
    增加基本攻击力和技能攻击力。\n
    进入地下城时自动施放。(在决斗场中无效)
    """
    name = "念兽 : 龙虎啸"
    learnLv = 30
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    cd = 5
    mp = [357, 2911]
    uuid = "1b1cfab062e0768bcc889e33e1f30dbf"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 第1击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 第2击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 第3击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 第4击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # 第5击攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # 前冲攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 跳跃攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [感电效果]
    # 感电攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 感电几率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 前冲攻击、 跳跃攻击感电几率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 感电持续时间 : {value11}秒
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # [持续效果]
    # 基本攻击力和技能攻击力增加率 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 移动速度增加率 : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # 物理/魔法防御力增加量 : {value14}
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # [范围信息]
    # 范围比率 : {value15}%
    data15 = get_data(f'{prefix}/{uuid}', 15)

    associate = [ {"type":"*skillDamage","data":data12} ]

    mode = ['一轮平x','前冲','跳跃']

    def setMode(self, mode):
        if mode == "一轮平x":
            self.hit1 = self.hit2 = self.hit3 = self.hit4 = self.hit5 = 1
            self.hit6 = self.hit7 = 0
        elif mode == "前冲":
            self.hit1 = self.hit2 = self.hit3 = self.hit4 = self.hit5 = self.hit7 = 0
            self.hit6 = 1
        elif mode == "跳跃":
            self.hit1 = self.hit2 = self.hit3 = self.hit4 = self.hit5 = self.hit6 = 0
            self.hit7 = 1

# 念气环绕 : 御
# fighter_male/nenmaster_male/7ec521d063d2190e1fcc5bd229af9bcf
# ca0f0e0e9e1d55b5f9955b03d9dd213c/7ec521d063d2190e1fcc5bd229af9bcf
class Skill33(ActiveSkill):
    """
    使念气珠环绕的半径变长、 环绕速度加快， 并且改变念气珠的攻击力， 效果持续一定时间。
    """
    name = "念气环绕 : 御"
    learnLv = 30
    masterLv = 1
    maxLv = 11
    position = 2
    rangeLv = 2
    cd = 40
    mp = [200, 980]
    uuid = "7ec521d063d2190e1fcc5bd229af9bcf"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 念气珠攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [
        {"type":"*power5","data":[i-100 if i > 0 else i for i in data0],"skills":["念气环绕"]}
    ]

# 狮子吼
# fighter_male/nenmaster_male/9cb6f9ed646fa87f9b7680a42ce83d1a
# ca0f0e0e9e1d55b5f9955b03d9dd213c/9cb6f9ed646fa87f9b7680a42ce83d1a
class Skill34(ActiveSkill):
    """
    发出可对周围敌人造成伤害的狮吼， 并有一定几率使敌人进入眩晕状态。\n
    施放[风雷啸]时， 进入霸体状态。
    """
    name = "狮子吼"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cube = 1
    cd = 17
    mp = [120, 1008]
    uuid = "9cb6f9ed646fa87f9b7680a42ce83d1a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 狮子吼攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [眩晕效果]
    # 眩晕几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 眩晕持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [狮子吼]\n
        使用念气波动攻击周围敌人\n
        风雷能量消耗量 +50%\n
        消耗风雷能量时， 获得强化内功的增益效果\n
        - 增益持续时间 : 30秒\n
        - 增益效果 : 需消耗风雷能量的技能， 可以无消耗使用1次\n
        [禅语·形灭]\n
        内功强化增益状态下使用时， 生成螺旋念气珠后可以移动
        """
        ...

    def vp_2(self):
        """
        [狮子吼]\n
        可以强制中断部分转职技能的施放后僵直并施放\n
        - 可强制中断的技能 : [天雷虎踢]、 [念兽 : 猛虎震地]、 [禅语·形灭]\n
        使命中的敌人进入强制控制状态\n
        - 删除眩晕效果\n
        - 控制时间 : 2秒\n
        - 消耗风雷能量时， 额外增加1秒控制时间\n
        施放速度 +15%\n
        风雷能量消耗量 -25%
        """
        ...

# 天雷虎踢
# fighter_male/nenmaster_male/38805520deffc10fac2e8f881ab7682b
# ca0f0e0e9e1d55b5f9955b03d9dd213c/38805520deffc10fac2e8f881ab7682b
class Skill35(ActiveSkill):
    """
    在腿部聚集念能量， 形成念兽的形象后下劈。\n
    下劈的瞬间引发强烈的念气爆炸， 爆炸地点留下念能量。留下的能量对敌人造成多段伤害， 使敌人进入感电状态。
    """
    name = "天雷虎踢"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cube = 1
    cd = 17
    mp = [120, 1008]
    uuid = "38805520deffc10fac2e8f881ab7682b"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 残留能量攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 8
    # 残留能量多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [感电效果]
    # 感电攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 8
    # 感电几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 感电持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [天雷虎踢]\n
        攻击范围 +35%\n
        - 基本冷却时间变更为34秒\n
        - 攻击力 +100%\n
        风雷能量获取量 +20%\n
        风雷能量消耗量 +20%
        """
        self.cd = 34
        self.skillRation *= 2
        ...

    def vp_2(self):
        """
        [天雷虎踢]\n
        快速下劈引发爆炸\n
        - 施放速度 +25%\n
        - 删除残留能量攻击\n
        - 螺旋球体攻击变更为单次攻击\n
        - 总攻击力相同\n
        基本冷却时间变更为8.5秒\n
        总攻击力 -50%\n
        风雷能量获取量 -50%\n
        风雷能量消耗量 -50%
        """
        self.cd = 8.5
        self.skillRation *= 0.5
        ...

# 螺旋念气场
# fighter_male/nenmaster_male/4224f9b0b8c7c903e9a1e0f9d9f6d04d
# ca0f0e0e9e1d55b5f9955b03d9dd213c/4224f9b0b8c7c903e9a1e0f9d9f6d04d
class Skill36(ActiveSkill):
    """
    凝聚念气生成念气场， 使周围敌人受到光属性伤害并有一定几率使其进入感电状态。\n
    施放[风雷啸]时， 发动霸体护甲。
    """
    name = "螺旋念气场"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [170, 1428]
    uuid = "4224f9b0b8c7c903e9a1e0f9d9f6d04d"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 螺旋念气场攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 17
    # 螺旋念气场多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # {感电效果]
    # 感电攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 感电几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 感电持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [螺旋念气场]\n
        消耗风雷能量施放技能后可以移动\n
        [螺旋念气场]多段攻击间隔 -50%
        """
        ...

    def vp_2(self):
        """
        [螺旋念气场]\n
        激起气流， 将周围敌人吸附到螺旋念气场中心\n
        攻击范围 +35%\n
        施放时所受伤害 -90%
        """
        ...

# 念兽 : 猛虎震地
# fighter_male/nenmaster_male/dbf8b30c7057032af0d68fcfa289fdae
# ca0f0e0e9e1d55b5f9955b03d9dd213c/dbf8b30c7057032af0d68fcfa289fdae
class Skill37(ActiveSkill):
    """
    蓄气后， 召唤出念兽猛虎并使其扑向敌人； 被猛虎扑中的敌人会受到多段攻击和爆炸伤害。
    """
    name = "念兽 : 猛虎震地"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [450, 3780]
    uuid = "dbf8b30c7057032af0d68fcfa289fdae"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 突进攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 突进多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [念兽 : 猛虎震地]\n
        念兽以猛烈的气势迅速袭击敌人造成伤害\n
        - 删除突进多段攻击\n
        - 总攻击力相同\n
        - 施放速度 +30%\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 22.5秒\n
        - 单次攻击力 -50%\n
        - 风雷能量补给量 -50%\n
        - 风雷能量消耗量 -50%
        """
        self.cd = 22.5
        self.skillRation *= 0.5
        ...

    def vp_2(self):
        """
        [念兽 : 猛虎震地]\n
        念兽咆哮后引发大爆炸\n
        - 被咆哮命中的敌人将被吸附到念兽中心\n
        - 攻击范围 +30%\n
        风雷能量消耗量 -50%
        """
        ...

# 念之奥义
# fighter_male/nenmaster_male/8b08f9504167a9c0f3a1d29d71b7943e
# ca0f0e0e9e1d55b5f9955b03d9dd213c/8b08f9504167a9c0f3a1d29d71b7943e
class Skill38(PassiveSkill):
    """
    据说， 领悟念之奥义后可以看到生命体内流动的念气。 因此， 狂虎帝不仅能控制体内念气的流动保持身体健康， 还能将自身的战斗技术修炼到极致。 在战斗中， 狂虎帝可以集中攻击敌人念气最薄弱的地方， 并给予其致命一击。\n
    将念气的力量发挥到极致， 从而解读生命体内流动的念气， 增加魔法暴击率和魔法暴击伤害。
    """
    name = "念之奥义"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 3
    uuid = "8b08f9504167a9c0f3a1d29d71b7943e"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 魔法暴击伤害增加率 : {value0}%魔法暴击率增加 : {value1}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法暴击伤害增加率 : {value0}%魔法暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [ {"type":"*skillDamage","data":data0} ]

# 念兽 : 审判之金雷虎
# fighter_male/nenmaster_male/51a08fd0c90f0a5276cd552047fac93d
# ca0f0e0e9e1d55b5f9955b03d9dd213c/51a08fd0c90f0a5276cd552047fac93d
class Skill39(ActiveSkill):
    """
    召唤出审判念兽金雷虎攻击周围的敌人。\n
    骑乘金雷虎时， 可以按方向键移动。\n
    金雷虎在跳跃三次之后会发生爆炸， 并使周围的敌人受到巨大伤害。
    """
    name = "念兽 : 审判之金雷虎"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [900, 7559]
    uuid = "51a08fd0c90f0a5276cd552047fac93d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 金雷虎身体攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 6
    # 金雷虎身体总攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 金雷虎落地时的冲击波总攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 3
    # 金雷虎落地时的冲击波攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 金雷虎爆炸攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1

# 念之战矛
# fighter_male/nenmaster_male/c91a62dc0a18360acf5031ac0ebf09f5
# ca0f0e0e9e1d55b5f9955b03d9dd213c/c91a62dc0a18360acf5031ac0ebf09f5
class Skill40(ActiveSkill):
    """
    将念气化作矛的形态攻击前方敌人， 有一定几率使敌人进入感电状态。 念之战矛在最后会爆炸并给予敌人爆炸伤害。
    """
    name = "念之战矛"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [450, 1260]
    uuid = "c91a62dc0a18360acf5031ac0ebf09f5"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 穿刺攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [感电效果]
    # 感电攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 感电几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 感电持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 爆炸范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [念之战矛]\n
        向前方投掷巨大的念之战矛\n
        - 投掷射程 : 300px\n
        - 中途击中敌人时爆炸\n
        - 删除强制控制效果\n
        - 删除穿刺攻击\n
        - 总攻击力相同\n
        - 念之战矛大小 +40%
        """
        ...

    def vp_2(self):
        """
        [念之战矛]\n
        强制控制时间增加， 被[念之战矛]刺中的敌人被[蓄念炮]或[幻影爆碎]命中时立即爆炸\n
        - 控制时间 : 3秒\n
        - 立即爆炸时恢复20%风雷能量
        """
        ...

# 冲云念气场
# fighter_male/nenmaster_male/85f7c810ad503790e8626439fe936d56
# ca0f0e0e9e1d55b5f9955b03d9dd213c/85f7c810ad503790e8626439fe936d56
class Skill41(ActiveSkill):
    """
    在手中凝聚念气结晶之后， 将念气结晶砸向地面生成柱型念气场， 可以使敌人受到光属性伤害并有一定几率进入感电状态。\n
    在准备阶段按前、 后方向键可以调整柱型念气场的生成位置。\n
    [风雷啸]在激活状态时， 会新增把怪物们聚集到前方的能力。
    """
    name = "冲云念气场"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [800, 1680]
    uuid = "85f7c810ad503790e8626439fe936d56"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 柱形念气攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 6
    # 柱形念气多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [感电效果]
    # 感电攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 6
    # 感电几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 感电持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [冲云念气场]\n
        [念兽 : 龙虎啸]最后基本攻击、 [雷霆踏]、 [天雷虎踢]命中时自动引发落雷\n
        - 删除吸附功能\n
        - 删除螺旋球体\n
        - 柱形念气攻击力 +70%\n
        - [风雷啸]未激活状态或风雷能量不足时技能不发动\n
        变更为可填充3次的技能\n
        - 每次填充冷却时间 : 16.6秒\n
        - 每次消耗风雷能量 : 80\n
        - 每次落雷多段攻击次数 : 2次
        """
        self.cd = 16.6
        self.hit0 = self.hit2 = 2
        ...

    def vp_2(self):
        """
        [冲云念气场]\n
        使用巨大的光柱攻击敌人\n
        - 攻击范围 +50%\n
        - 消耗风雷能量时， 吸附范围 +50%\n
        风雷能量消耗量 -50%
        """
        ...

# 奔雷螺旋击
# fighter_male/nenmaster_male/c4a5b868f1e8e60cd1867a2cfab4a242
# ca0f0e0e9e1d55b5f9955b03d9dd213c/c4a5b868f1e8e60cd1867a2cfab4a242
class Skill42(ActiveSkill):
    """
    在手上生成雷电之刃插入一名敌人体内， 并把雷电能量注入进去， 随后在体内引起爆炸造成强力的伤害。\n
    施放[风雷啸]后， 进入霸体状态， 通过技能键蓄气每0.1秒使用10点能量， 最多可以蓄气2.5秒。
    """
    name = "奔雷螺旋击"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 3
    cd = 42
    mp = [170, 1428]
    uuid = "c4a5b868f1e8e60cd1867a2cfab4a242"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 风雷能量注入时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 爆炸范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [奔雷螺旋击]\n
        消耗风雷啸能量， 挥动雷电之手， 立即引发爆炸\n
        - 删除强制控制效果\n
        - 删除念气球\n
        - 总攻击力相同\n
        雷电爆炸范围 +30%
        """
        ...

    def vp_2(self):
        """
        [奔雷螺旋击]\n
        消耗风雷能量时， 追踪并攻击前方500px范围内最强敌人\n
        - 无需按住技能键即可立即产生念气球\n
        - 念气球攻击次数 -50%\n
        - 减少雷电注入时间上限\n
        - 总攻击力相同\n
        [念雷轰]\n
        可以在[奔雷螺旋击]施放过程中施放\n
        - 此时， [念雷轰]的风雷能量恢复量 +100%
        """
        ...

# 风雷啸
# fighter_male/nenmaster_male/8d996a242c5c0efd8cfe6cb4bc6defcc
# ca0f0e0e9e1d55b5f9955b03d9dd213c/8d996a242c5c0efd8cfe6cb4bc6defcc
class Skill43(ActiveSkill):
    """
    激活储存在体内的风雷能量， 学习技能后， 可以增加基本攻击力和技能攻击力。\n
    风雷能量储存到500以上时可以激活效果， 再次使用技能时， 将会解除效果状态。\n
    使用技能时， 拥有的风雷能量少于消耗的能量时， 效果将会结束。\n
    激活增益效果后施放技能时， 螺旋球体的旋转力会加强， 强化部分转职技能攻击力。\n
    [螺旋球体适用技能]\n
    [狮子吼]、 [天雷虎踢]、 [螺旋念气场]、 [念兽 : 猛虎震地]、 [念兽 : 审判之金雷虎]、 [念之战矛]、 [冲云念气场]、 [奔雷螺旋击]、 [禅语·形灭]
    """
    name = "风雷啸"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    cd = 1
    mp = [5, 5]
    uuid = "8d996a242c5c0efd8cfe6cb4bc6defcc"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [螺旋球体效果]
    # 螺旋球体攻击力 : 相应技能攻击力总和的{value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [念气环绕 ： 袭]、 [念气环绕 ： 御]的念气球范围增加 : 50%

    associate = [
        {"data":data0},
        {"data":data1,"skills":["狮子吼","天雷虎踢","螺旋念气场","念兽 : 猛虎震地","念兽 : 审判之金雷虎","念之战矛","冲云念气场","奔雷螺旋击","禅语·形灭"]}
    ]

# 风雷引
# fighter_male/nenmaster_male/9bc30e0f6e22b0333762d04acae7d252
# ca0f0e0e9e1d55b5f9955b03d9dd213c/9bc30e0f6e22b0333762d04acae7d252
class Skill44(PassiveSkill):
    """
    使用技能时， 把周围的能量吸入体内， 转换为风雷能量。\n
    使用技能攻击敌人时， 会储存风雷能量。\n
    [风雷啸]激活的状态下， 只能用[念兽 : 龙虎啸]的基本攻击、 [念气波]、 [蓄念炮]、 [雷霆踏]、 [幻影爆碎]储存风雷能量。
    """
    name = "风雷引"
    learnLv = 75
    masterLv = 1
    maxLv = 1
    position = 8
    rangeLv = 2
    uuid = "9bc30e0f6e22b0333762d04acae7d252"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # [风雷能量收集/使用量]
    # [念气波] : {value0}/0
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [蓄念炮] : {value1}/0
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [雷霆踏] : {value2}/0
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [念雷轰] : {value3}/0
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [念气环绕 ： 袭] : {value4}/{value5}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [念气环绕 ： 袭] : {value4}/{value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [念气环绕 ： 御] : {value6}/0
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [幻影爆碎] : {value7}/0
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [念兽 ： 龙虎啸]基本攻击 : {value8}/0
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [狮子吼] : {value9}/{value10}
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [狮子吼] : {value9}/{value10}
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # [天雷虎踢] : {value11}/{value12}
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # [天雷虎踢] : {value11}/{value12}
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # [螺旋念气场] : {value13}/{value14}
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # [螺旋念气场] : {value13}/{value14}
    data14 = get_data(f'{prefix}/{uuid}', 14)
    # [念兽 ： 猛虎震地]  : {value15}/{value16}
    data15 = get_data(f'{prefix}/{uuid}', 15)
    # [念兽 ： 猛虎震地]  : {value15}/{value16}
    data16 = get_data(f'{prefix}/{uuid}', 16)
    # [念兽 ： 审判之金雷虎] : {value17}/{value18}
    data17 = get_data(f'{prefix}/{uuid}', 17)
    # [念兽 ： 审判之金雷虎] : {value17}/{value18}
    data18 = get_data(f'{prefix}/{uuid}', 18)
    # [念之战矛] : {value19}/{value20}
    data19 = get_data(f'{prefix}/{uuid}', 19)
    # [念之战矛] : {value19}/{value20}
    data20 = get_data(f'{prefix}/{uuid}', 20)
    # [冲云念气场] : {value21}/{value22}
    data21 = get_data(f'{prefix}/{uuid}', 21)
    # [冲云念气场] : {value21}/{value22}
    data22 = get_data(f'{prefix}/{uuid}', 22)
    # [奔雷螺旋击] : {value23}/{value24}~{value25}
    data23 = get_data(f'{prefix}/{uuid}', 23)
    # [奔雷螺旋击] : {value23}/{value24}~{value25}
    data24 = get_data(f'{prefix}/{uuid}', 24)
    # [奔雷螺旋击] : {value23}/{value24}~{value25}
    data25 = get_data(f'{prefix}/{uuid}', 25)
    # [禅语·形灭] : {value26}/{value27}
    data26 = get_data(f'{prefix}/{uuid}', 26)
    # [禅语·形灭] : {value26}/{value27}
    data27 = get_data(f'{prefix}/{uuid}', 27)

# 月辉念气破
# fighter_male/nenmaster_male/3af805da8505fe6234a95b535610f064
# ca0f0e0e9e1d55b5f9955b03d9dd213c/3af805da8505fe6234a95b535610f064
class Skill45(ActiveSkill):
    """
    运用月光般强大的念气攻击敌人。\n
    被念气击中的敌人的能量会被吸收到体内， 转化为风雷能量。
    """
    name = "月辉念气破"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [450, 1260]
    uuid = "3af805da8505fe6234a95b535610f064"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 月光能量攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 10
    # 月光能量多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 月光能量持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 击打时风雷能量恢复量 : 7%
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [月辉念气破]\n
        发射念气后， 将月光能量集中至一点并引发爆炸\n
        - 爆炸命中时， 恢复30%的风雷啸能量\n
        - 总攻击力相同\n
        施放过程中所受伤害 -90%\n
        [风雷啸]\n
        施放[月辉念气破]后自动施加增益效果\n
        - 需要累积500以上的风雷啸能量
        """
        ...

    def vp_2(self):
        """
        [月辉念气破]\n
        生成浓缩念气珠， 大范围散发月光能量\n
        - 攻击范围 +40%\n
        - 生成念气珠后可以移动\n
        对命中的敌人附加失明效果\n
        - 失明几率 : 100%\n
        - 失明持续时间 : 3秒
        """
        ...

# 月华万象
# fighter_male/nenmaster_male/087d1068ff506d090710566608a17760
# ca0f0e0e9e1d55b5f9955b03d9dd213c/087d1068ff506d090710566608a17760
class Skill46(ActiveSkill):
    """
    瞬间把敌人聚于身边后， 再度释放念气引发爆炸。\n
    爆炸结束后的一段时间内身体会被月华包裹。\n
    身体被月华包裹期间， 风雷能量会持续在满额状态。\n
    把敌人聚于中间的过程中无法移动， 连续按下攻击键或技能键时， 聚集的速度会加快。
    """
    name = "月华万象"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [500, 4480]
    uuid = "087d1068ff506d090710566608a17760"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 电击球体火花攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 11
    # 火花多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 电击爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 辉光持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 禅意·万象
# fighter_male/nenmaster_male/6067de229738524687e5a9ee1c53d583
# ca0f0e0e9e1d55b5f9955b03d9dd213c/6067de229738524687e5a9ee1c53d583
class Skill47(PassiveSkill):
    """
    掌握自然万物的气息， 增加基本攻击力和技能攻击力， 使部分技能附加额外效果。\n
    [风雷啸]\n
    进入地下城时， 风雷能量为最高状态， 且战斗状态下自动恢复风雷能量。\n
    [蓄念炮]\n
    施放技能时， 直接以蓄气后的状态发动。\n
    [念气环绕 : 袭]\n
    在追击的敌人周围生成念气， 并产生爆炸。\n
    爆炸攻击力不受[念气环绕]攻击力的影响。
    """
    name = "禅意·万象"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "6067de229738524687e5a9ee1c53d583"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 风雷啸能量自然恢复量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 风雷啸能量自然恢复周期 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [ {"data":data0} ]

# 禅语·形灭
# fighter_male/nenmaster_male/33ad4930f4724a7d025c3046c6f6074b
# ca0f0e0e9e1d55b5f9955b03d9dd213c/33ad4930f4724a7d025c3046c6f6074b
class Skill48(ActiveSkill):
    """
    生成蕴含自然气息的螺旋念气珠。\n
    念气以螺旋形态旋转一定时间后， 幻化为狂虎的形态攻击， 随后爆炸对敌人进行强力的攻击。
    """
    name = "禅语·形灭"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [773, 6000]
    uuid = "33ad4930f4724a7d025c3046c6f6074b"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 念气珠多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 10
    # 念气珠多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

# 禅念·归一
# fighter_male/nenmaster_male/9ceb0c55f40f1fc0fe0fcc65c8fee3a0
# ca0f0e0e9e1d55b5f9955b03d9dd213c/9ceb0c55f40f1fc0fe0fcc65c8fee3a0
class Skill49(ActiveSkill):
    """
    在自身的周围生成念气， 并缓缓升至空中。\n
    在空中打坐结印， 将周围的念气珠合为一体， 形成巨大的光轮。\n
    缓慢合掌后光轮爆炸， 万物归一。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "禅念·归一"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4027, 8054]
    uuid = "9ceb0c55f40f1fc0fe0fcc65c8fee3a0"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 光轮爆炸单段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 光轮爆炸多段攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 6
    # 光轮爆炸多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'nenmaster_male'
        self.nameCN = '归元·气功师'
        self.role = 'fighter_male'
        self.角色 = '格斗家(男)'
        self.职业 = '气功师'
        self.jobId = 'ca0f0e0e9e1d55b5f9955b03d9dd213c'
        self.jobGrowId = '37495b941da3b1661bc900e68ef3b2c6'

        self.武器选项 = ['手套', '臂铠','爪','东方棍']
        self.输出类型选项 = ['魔法百分比']
        self.输出类型 = '魔法百分比'
        self.防具精通属性 = ['智力']
        self.防具类型 = '布甲'
        self.buff = 1.487 * 1.21

        self.角色 = '格斗家(男)'

        self.职业 = '气功师'


        super().__init__(equVersion, __name__)
