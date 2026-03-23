#ca0f0e0e9e1d55b5f9955b03d9dd213c
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "fighter_male/brawler_male/cn/skillDetail"


# 剧毒抵抗
# fighter_male/brawler_male/03bb5314ffd41e9458d67ef924fef38f
# ca0f0e0e9e1d55b5f9955b03d9dd213c/03bb5314ffd41e9458d67ef924fef38f
class Skill1(PassiveSkill):
    """
        通过对毒的修炼， 减少自身受到的中毒伤害。
    """
    name = "剧毒抵抗"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "03bb5314ffd41e9458d67ef924fef38f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 中毒伤害减少率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

# 毒攻掌握
# fighter_male/brawler_male/bb34e8854a93fd250347a1c64119f7ab
# ca0f0e0e9e1d55b5f9955b03d9dd213c/bb34e8854a93fd250347a1c64119f7ab
class Skill2(PassiveSkill):
    """
    정통 격투가 사이에서 금기시되는 사파의 속성 무공을 수련한다. 체내에 특수한 독으로 된 혈도를 생성하는 위험한 시술로 잘못 익히면 목숨이 위태로울 수 있다.\n
    이 독특한 무공은 외공을 주로 수련하는 이에게는 내공 증진의 효과를 가져다주며, 반대로 내공을 주로 수련하는 이에게는 외공 증진의 효과를 가져다주는 것으로 알려져 있다.\n
        力量和智力、 物理暴击率和魔法暴击率中会按照一定比率相互补正。\n
    사공을 수련한 부작용으로 넨 계열의 스킬(넨탄, 분신)을 시전 시 일정 확률로 주화입마(기절)에 빠지게 된다.
    """
    name = "毒攻掌握"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 6
    rangeLv = 1
    uuid = "bb34e8854a93fd250347a1c64119f7ab"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 力量和智力补正比率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理暴击率和魔法暴击率补正比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 施放念气系列技能时眩晕几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)


# 基础精通
# fighter_male/brawler_male/5a56514f35cf0270ae8d6c65f8fefd78
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
    associate = [{"type":"*skillDamage","data":[i-100 if i>0 else 0 for i in data0],"skills":["罗网投掷"]}]


# 下段踢
# fighter_male/brawler_male/4655101518604f874721b3cc249aae10
# ca0f0e0e9e1d55b5f9955b03d9dd213c/4655101518604f874721b3cc249aae10
class Skill9(ActiveSkill):
    """
        向敌人下段发出高伤害的踢脚攻击， 可以攻击倒地的敌人， 而且能使被击中的敌人出现较长时间的僵直。\n
        攻击成功时产生冲击波， 对周围敌人造成伤害。\n
        被直接命中的敌人不受冲击波伤害。
    """
    name = "下段踢"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 2
    mp = [10, 112]
    uuid = "4655101518604f874721b3cc249aae10"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 下段踢攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 发动速度增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 冲击波大小比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 分身
# fighter_male/brawler_male/f2fb27162beb0b87a7cb9af7900e95f2
# ca0f0e0e9e1d55b5f9955b03d9dd213c/f2fb27162beb0b87a7cb9af7900e95f2
class Skill10(ActiveSkill):
    """
        生成分身扰乱敌人的攻击或阻挡子弹。\n
        经过一定时间或受一定伤害后， 生成的分身消失。\n
        转职成气功师后， 可以学习[幻影爆碎]技能。
    """
    name = "分身"
    learnLv = 5
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
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

# 膝击
# fighter_male/brawler_male/cfacda0647b9a0f595df2c2aad30c18d
# ca0f0e0e9e1d55b5f9955b03d9dd213c/cfacda0647b9a0f595df2c2aad30c18d
class Skill11(ActiveSkill):
    """
        抓住前方敌人并用膝盖对其进行猛力的撞击。\n
        对无法抓取的敌人不适用控制效果。\n
        转职为柔道家后， 可以对无法抓取的敌人施放， 增加攻击次数， 且使用方向键时， 使最后一击发生变化。\n
    [转职为柔道家后]\n
    上方向键 : 使敌人浮空， 且柔道家也一并跳跃\n
    下方向键 : 把敌人扔向地面， 并产生冲击波攻击周围敌人
    """
    name = "膝击"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 5
    mp = [20, 168]
    uuid = "cfacda0647b9a0f595df2c2aad30c18d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 膝击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 膝击多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 膝击最后一击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 落地冲击波攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 冲击波范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)


# 钢筋铁骨
# fighter_male/brawler_male/c9664191611af31142e052dfaef84530
# ca0f0e0e9e1d55b5f9955b03d9dd213c/c9664191611af31142e052dfaef84530
class Skill13(PassiveSkill):
    """
        使自身的身体强悍如钢铁， 并增加一定的物防和体力。 被击时， 有一定几率使自身进入霸体状态。
    """
    name = "钢筋铁骨"
    learnLv = 10
    masterLv = 50
    maxLv = 60
    position = 8
    rangeLv = 3
    uuid = "c9664191611af31142e052dfaef84530"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 增加物防 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 增加体力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 霸体发动几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 鹰踏
# fighter_male/brawler_male/78bd107acd474518b606be1e4fd38239
# ca0f0e0e9e1d55b5f9955b03d9dd213c/78bd107acd474518b606be1e4fd38239
class Skill14(ActiveSkill):
    """
        在空中跳跃着踩踏敌人并给予敌人一定伤害。\n
        可以连续对敌人进行一定次数的踩踏。 技能的冷却时间从最后一次踩踏结束落地时开始计算。
    """
    name = "鹰踏"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 7
    mp = [10, 97]
    uuid = "78bd107acd474518b606be1e4fd38239"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 踩踏攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 踩踏次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后踩踏攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

# 疾风追击
# fighter_male/brawler_male/dcb31a63ef58954f44ff2070c42a9a98
# ca0f0e0e9e1d55b5f9955b03d9dd213c/dcb31a63ef58954f44ff2070c42a9a98
class Skill15(ActiveSkill):
    """
        前冲攻击后， 通过快速连续的攻击给予敌人一定伤害。\n
    호신연격을 배우면 대시 공격 시 적이 다운되지 않게 된다.\n
    대시 공격 후 공격키를 누르거나 스킬키를 누르면 연타를 하게 되며 그 때마다 MP가 소모 된다.\n
    기본은 1타까지만 사용 가능하고 호포 습득 시 2타까지 추가로 공격이 가능하게 된다.
    """
    name = "疾风追击"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 9
    rangeLv = 2
    cd = 2
    mp = [8, 67]
    uuid = "dcb31a63ef58954f44ff2070c42a9a98"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 第1击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第2击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

# 金刚碎
# fighter_male/brawler_male/4f2e001e9a19eb7bae50ad1840dfb329
# ca0f0e0e9e1d55b5f9955b03d9dd213c/4f2e001e9a19eb7bae50ad1840dfb329
class Skill16(ActiveSkill):
    """
        向前方小跳后用双脚猛击地面引发冲击波。\n
        发动时， 可以用方向键控制攻击地点。\n
        处于攻击地点中心的敌人， 会受到脚踢和冲击波的二次伤害。\n
        技能等级越高， 技能施放后的僵直时间越短。\n
    - [转职为柔道家时] -\n
        可以强制中断基本攻击动作， 并立即施放该技能； 攻击方式变更为肘击， 且对敌人造成更多伤害； 可以强制中断施放后的僵直动作， 并立即施放[霹雳旋踢]。
    """
    name = "金刚碎"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 1
    rangeLv = 2
    cd = 5
    mp = [20, 238]
    uuid = "4f2e001e9a19eb7bae50ad1840dfb329"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 踢击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 浮空力比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 施放后的僵直时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 对倒地的敌人攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 瞬步
# fighter_male/brawler_male/9dc8438e4572d39243c97da31c113acc
# ca0f0e0e9e1d55b5f9955b03d9dd213c/9dc8438e4572d39243c97da31c113acc
class Skill17(ActiveSkill):
    """
        向前方快速移动一定距离。\n
        撞到敌人时停止移动。
    """
    name = "瞬步"
    learnLv = 10
    masterLv = 1
    maxLv = 1
    position = 6
    rangeLv = 2
    cd = 5
    mp = [10, 10]
    uuid = "9dc8438e4572d39243c97da31c113acc"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 移动距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)


# 抛沙
# fighter_male/brawler_male/8f73f243041c2d27739fe7696f02bf9b
# ca0f0e0e9e1d55b5f9955b03d9dd213c/8f73f243041c2d27739fe7696f02bf9b
class Skill21(ActiveSkill):
    """
        卑鄙地抛出沙子攻击敌人， 使敌人进入失明状态。\n
        转职为街霸后， 可以强制中断基本攻击并施放。
    """
    name = "抛沙"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 3
    mp = [15, 154]
    uuid = "8f73f243041c2d27739fe7696f02bf9b"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 失明几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 失明持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 减少视野 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 命中率减少 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 毒瓶投掷
# fighter_male/brawler_male/762c4e6d030eaf0abbfe1fec2b298574
# ca0f0e0e9e1d55b5f9955b03d9dd213c/762c4e6d030eaf0abbfe1fec2b298574
class Skill22(ActiveSkill):
    """
    [投掷]\n
        施放后， 在消耗完所有装填次数之前， 具有固有的重新投掷冷却时间。\n
        向前方的敌人投掷毒瓶\n
        发动[后街战术]和[后备口袋]效果时， 第2个毒瓶替换为火焰瓶。\n
    (灼伤攻击力和异常状态持续时间与中毒相同)\n
    [投掷强化]\n
    - 向前方投掷毒瓶， 在一定范围内暂时形成猛毒地带\n
    - 按向下方向键可以向脚底投掷毒瓶， 在自身周围生成猛毒地带\n
    (在决斗场中无效)\n
    [学习逆道·皆允后]\n
    - 普通投掷时， 会投掷1次结合毒瓶和火焰瓶功能的特制火焰瓶。\n
    - 使用[投掷强化]时， 在地面生成毒雾， 爆炸后进入的敌人也会进入中毒状态。
    """
    name = "毒瓶投掷"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 3
    # 装填cd
    # cd = 7
    # 投掷cd
    cd = 2
    mp = [50, 420]
    uuid = "762c4e6d030eaf0abbfe1fec2b298574"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 投掷冷却时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 毒瓶数量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 毒瓶攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 2
    # 猛毒地带范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 中毒持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 中毒攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 2
    # [投掷强化]
    # 毒瓶消耗量 : {value6}个
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 中毒攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    hit7 = 1
    # [范围信息]
    # [投掷强化]猛毒地带范围比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

    data9 = data7
    power9 = 0
    hit9 = 1

    mode = ['常规','强化','爆破污桶']

    def setMode(self, mode):
        if mode == "常规":
            self.hit2 = self.hit5 = 2
            self.hit7 = self.hit9 = 0
        elif mode == "强化":
            self.hit7 = 1
            self.hit2 = self.hit5 = self.hit9 = 0
        elif mode == "爆破污桶":
            self.hit9 = 1
            self.hit2 = self.hit5 = self.hit7 = 1

    def getSkillCD(self, mode=None):
        if mode == "爆破污桶":
            return self.char.GetSkillByName("爆破污桶").getSkillCD(mode)
        return super().getSkillCD(mode)

# 投掷强化
# fighter_male/brawler_male/3fb8395ae3b81bd608e0c4223a8eb534
# ca0f0e0e9e1d55b5f9955b03d9dd213c/3fb8395ae3b81bd608e0c4223a8eb534
class Skill23(ActiveSkill):
    """
        施放后， 强化下次投掷技能。\n
        消耗更多装填数， 发动方式发生变化。\n
    [毒瓶投掷]\n
        向前方投掷毒瓶， 在一定范围内暂时形成猛毒地带。\n
    [毒针投掷]\n
        一次性投掷变更为范围攻击判定的多枚毒针， 呈扇形分布。\n
    [砖块投掷]\n
        举起巨石从空中向前方投掷。 (学习[逆道·皆允]后， 可以在地面投掷)\n
    [罗网投掷]\n
        投掷更大的罗网， 将命中的敌人吸附到前面。\n
    [逆道·爆狱]\n
        用装有易燃物质的金属桶代替木桶， 使其发生连锁爆炸。
    """
    name = "投掷强化"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 4
    rangeLv = 3
    cd = 0.1
    mp = [24, 24]
    uuid = "3fb8395ae3b81bd608e0c4223a8eb534"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 自动填充
# fighter_male/brawler_male/5806440d21e7546d50007a5ba11f8024
# ca0f0e0e9e1d55b5f9955b03d9dd213c/5806440d21e7546d50007a5ba11f8024
class Skill24(PassiveSkill):
    """
        消耗投掷技能的装填数时， 自动重新装填。\n
    [投掷技能]\n
    - [毒瓶投掷]、 [毒针投掷]、 [砖块投掷]、 [罗网投掷]\n
    - 投掷时间间隔 : 技能属性描述中的下一次投掷为止的冷却时间\n
    - 自动填充时间 : 技能冷却时间显示的装填数全部消耗后， 可重新装填的冷却时间\n
    [学习诡诈之道后]\n
        进入地下城和复活时， 自动装填投掷技能。
    """
    name = "自动填充"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 0
    rangeLv = 5
    uuid = "5806440d21e7546d50007a5ba11f8024"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 擒月炎
# fighter_male/brawler_male/0969cd4054d93da07708108c0cc1c4b5
# ca0f0e0e9e1d55b5f9955b03d9dd213c/0969cd4054d93da07708108c0cc1c4b5
class Skill25(ActiveSkill):
    """
        先用扫腿攻击前方敌人并用后踢将1名敌人踢飞， 然后再用强威力的侧踢， 引爆火药使敌人受到伤害。\n
        攻击处于异常状态的敌人时， 造成更大的伤害。 (最多叠加3次)\n
        火药爆炸会引发持续时间较长的灼伤异常状态。\n
        对无法抓取的不适用控制效果， 立即引爆火药。\n
        在决斗场中， 攻击无法抓取的敌人时， 不会发生爆炸。
    """
    name = "擒月炎"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 5.5
    mp = [30, 280]
    uuid = "0969cd4054d93da07708108c0cc1c4b5"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 扫腿攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 后踢攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 每个异常状态的攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 灼伤几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 灼伤持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 爆炸范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    #每个异常增伤20%，最高60%增伤
    skillDamage = 1.6

# 后街战术
# fighter_male/brawler_male/4b2c90ec226fd40e967875aa5eabefb2
# ca0f0e0e9e1d55b5f9955b03d9dd213c/4b2c90ec226fd40e967875aa5eabefb2
class Skill26(ActiveSkill):
    """
        遵循后街法则， 准备更多暗器。\n
        增加基本攻击力和转职技能攻击力， 可以双重投掷暗器， 并增加部分技能的爆炸范围。\n
    [双重投掷]\n
    - 投掷道具时可以连续投掷两个\n
    - 消耗两个投掷类消耗品或填装数\n
    - 技能的第二个投掷物攻击力降低\n
    - 适用范围 : 投掷类消耗品、 [抛沙]、 [毒瓶投掷]、 [毒针投掷]、 [砖块投掷]\n
    - 使用[后备口袋]、 [投掷强化]时， 各自的技能优先生效
    """
    name = "后街战术"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 3
    rangeLv = 3
    cd = 5
    uuid = "4b2c90ec226fd40e967875aa5eabefb2"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和转职技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [擒月炎]爆炸范围增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [毒雷引爆]毒气柱大小增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)


# 爪精通
# fighter_male/brawler_male/e4c354a89c337310aeb7041d5e742828
# ca0f0e0e9e1d55b5f9955b03d9dd213c/e4c354a89c337310aeb7041d5e742828
class Skill29(PassiveSkill):
    """
    물리 공격력, 마법 공격력이 증가하고, 클로 장착 시 경직률, 적중률이 증가한다.
    """
    name = "爪精通"
    learnLv = 25
    masterLv = 20
    maxLv = 30
    position = 2
    rangeLv = 3
    uuid = "e4c354a89c337310aeb7041d5e742828"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 魔法攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [冲膝]
    # 僵直率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 命中率增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    associate = [
        {"type":"$*PAtkP","data":data0},
        {"type":"$*MAtkP","data":data1},
    ]

# 毒针投掷
# fighter_male/brawler_male/38612d8f2561edc2eb68d5057a837bfa
# ca0f0e0e9e1d55b5f9955b03d9dd213c/38612d8f2561edc2eb68d5057a837bfa
class Skill30(ActiveSkill):
    """
    [投掷]\n
        施放后， 在消耗完所有装填次数之前， 具有固有的重新投掷冷却时间。\n
        向敌人发射毒针， 使命中的敌人进入出血状态。\n
        发动[后街战术]和[后备口袋]效果时， 投掷带电的毒针， 使敌人进入感电状态。\n
    (感电攻击力及持续时间为出血的200%)\n
    [投掷强化]\n
    - 一次性投掷变更为范围攻击判定的多枚毒针， 呈扇形分布。\n
        在决斗场中， 强化投掷时的毒针具有单独的攻击判定。
    """
    name = "毒针投掷"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    # cd = 6
    # 投掷CD
    cd = 3
    mp = [50, 420]
    uuid = "38612d8f2561edc2eb68d5057a837bfa"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 投掷冷却时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 毒针数量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 毒针攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 2
    # 出血攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 2
    # 出血持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [投掷强化]
    # 毒针消耗量 : {value5}个
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 毒针攻击上限 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 毒针攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    hit7 = 4
    # 出血攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    hit8 = 4

    # 飞沙走石 VP2部分伤害
    data9 = data2
    power9 = 0
    hit9 = 1
    data10 = data3
    power10 = 0
    hit10 = 1

    mode = ['常规','强化','飞沙走石']

    def setMode(self, mode):
        if mode == "常规":
            self.hit2 = self.hit3 = 2
            self.hit7 = self.hit8 = self.hit9 = self.hit10 = 0
        elif mode == "强化":
            self.hit7 = self.hit8 = 4
            self.hit2 = self.hit3 = self.hit9 = self.hit10 = 0
        elif mode == "飞沙走石":
            self.hit9 = self.hit10 = 1
            self.hit2 = self.hit3 = self.hit7 = self.hit8 = 0

# 后备口袋
# fighter_male/brawler_male/2e9c5a06ff3fe8aea672a2a55c40fdbf
# ca0f0e0e9e1d55b5f9955b03d9dd213c/2e9c5a06ff3fe8aea672a2a55c40fdbf
class Skill31(PassiveSkill):
    """
        使用基本攻击和转职技能的过程中， 可以使用[投掷强化]。\n
        [后街战术]状态下， 使用[毒瓶投掷]或[毒针投掷]时， 各技能可以获得以下效果。\n
    [毒瓶投掷]\n
    - 普通投掷时， 第二个投掷物变更为火焰瓶。\n
    - 施加灼伤而非中毒。\n
    - 灼伤攻击力与持续时间 : 普通[毒瓶投掷]中毒的100%\n
    [毒针投掷]\n
    - 普通投掷时， 投掷1次通电的毒针。\n
    - 施加感电异常状态。\n
    - 感电攻击力与持续时间 : 普通[毒针投掷]出血的200%
    """
    name = "后备口袋"
    learnLv = 25
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 5
    uuid = "2e9c5a06ff3fe8aea672a2a55c40fdbf"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501


# 伏虎霸王拳
# fighter_male/brawler_male/8c2379737c5acc935c1731f67f607655
# ca0f0e0e9e1d55b5f9955b03d9dd213c/8c2379737c5acc935c1731f67f607655
class Skill32(ActiveSkill):
    """
        将敌人击倒并发出强威力的伏虎霸王拳， 可以向敌人连续发出3次攻击。\n
        每次攻击倒地的敌人， 都会产生冲击波攻击周围的敌人。\n
        对无法抓取的敌人不适用控制效果。
    """
    name = "伏虎霸王拳"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 15
    mp = [80, 672]
    uuid = "8c2379737c5acc935c1731f67f607655"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # [伏虎霸王拳]攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 冲击波范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 旋风腿
# fighter_male/brawler_male/202edb928046f4fa6dedf6337377efd5
# ca0f0e0e9e1d55b5f9955b03d9dd213c/202edb928046f4fa6dedf6337377efd5
class Skill33(ActiveSkill):
    """
        在原地快速旋转身体并用连续的扫腿攻击周围的敌人。\n
    지상과 공중에서 모두 사용 가능하며, 맞은 적을 끌어당기는 효과가 있다.\n
    시전 중 이동은 불가하며, 점프 키를 누르면 취소된다. \n
        转职成为散打时， 才可以强制中断基本攻击动作， 并立即施放该技能。
    """
    name = "旋风腿"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 8
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

# 砖块投掷
# fighter_male/brawler_male/bc11d28c04e01923a093d65752c55516
# ca0f0e0e9e1d55b5f9955b03d9dd213c/bc11d28c04e01923a093d65752c55516
class Skill34(ActiveSkill):
    """
    [投掷]\n
        施放后， 在消耗完所有装填次数之前， 具有固有的重新投掷冷却时间。\n
        用砖块攻击敌人。\n
        砖块命中敌人后会碎裂并给予周围敌人伤害。\n
    [投掷强化]\n
    - 举起圆形巨石砸向前方。\n
    - 巨石被举在空中时， 可以按方向键控制投掷方向。\n
        学习[逆道·皆允]后， 使用[投掷强化]时， 圆形巨石可以在地面砸向前方。\n
        在决斗场中， 减少处于[罗网投掷]束缚状态敌人的眩晕时间。
    """
    name = "砖块投掷"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    # cd = 6
    # 投掷cd
    cd = 4
    mp = [50, 420]
    uuid = "bc11d28c04e01923a093d65752c55516"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 投掷冷却时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 砖块数量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 砖块打击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 2
    # 砖块碎片攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 2
    # 眩晕几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 眩晕持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [投掷强化]
    # 砖块消耗量 : {value6}个
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 岩石攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 岩石碎片攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 岩石碎片眩晕几率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 眩晕持续时间 : {value10}秒
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 学习[逆道·皆允]后巨石攻击力 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    hit11 = 1
    # [范围信息]
    # 碎片范围比率 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)


    # 暗街夺命锁 VP2部分伤害
    data13 = data2
    power13 = 0
    hit13 = 1
    data14 = data3
    power14 = 0
    hit14 = 1

    mode = ['常规','强化','暗街夺命锁']

    def setMode(self, mode):
        if mode == "常规":
            self.hit2 = self.hit3 = 1
            self.hit11 = self.hit13 = self.hit14 = 0
        elif mode == "强化":
            self.hit11 = 1
            self.hit2 = self.hit3 = self.hit13 = self.hit14 = 0
        elif mode == "暗街夺命锁":
            self.hit13 = self.hit14 = 1
            self.hit2 = self.hit3 = self.hit11 = 0

# 挑衅
# fighter_male/brawler_male/e49e57b2e8fbeceb0a2c56a0c63fe6c5
# ca0f0e0e9e1d55b5f9955b03d9dd213c/e49e57b2e8fbeceb0a2c56a0c63fe6c5
class Skill35(ActiveSkill):
    """
        学习后， 持续减少一定范围内敌人的控制型异常状态抗性， 并增加对敌人造成的伤害。\n
        施放时， 向自身周围的敌人发出挑衅， 使被挑衅的敌人集中攻击施放者。\n
        被挑衅的敌人会变得异常兴奋从而降低命中率。\n
        按前方向键时， 将会向该方向发射挑衅音波挑衅更远处的敌人。\n
        在决斗场里无法使用挑衅功能。
    """
    name = "挑衅"
    learnLv = 35
    masterLv = 10
    maxLv = 20
    position = 2
    rangeLv = 3
    cd = 5
    mp = [60, 252]
    uuid = "e49e57b2e8fbeceb0a2c56a0c63fe6c5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # [持续效果]
    # 控制型异常状态抗性减少值 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 伤害增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [施放时效果]
    # 挑衅持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 命中率减少 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 控制型异常状态抗性减少及挑衅范围 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 前方挑衅射程 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5)

    associate = [ {"type": "*skillDamage", "data":data1} ]

# 罗网投掷
# fighter_male/brawler_male/d0cdaca82892e54097f22a1f60817048
# ca0f0e0e9e1d55b5f9955b03d9dd213c/d0cdaca82892e54097f22a1f60817048
class Skill36(ActiveSkill):
    """
    [投掷]\n
        施放后， 在消耗完所有装填次数之前， 具有固有的重新投掷冷却时间。\n
        投掷罗网强制控制命中的敌人， 并使其进入束缚状态。\n
        罗网攻击力受[基础精通]等级的影响。\n
    [投掷强化]\n
        投掷更大的罗网， 将命中的敌人吸附到前面。\n
        在决斗场中， 使用[投掷强化]后罗网命中浮空或倒地的敌人时， 会把敌人拉到面前并使敌人处于倒地状态， 但不强制控制。
    """
    name = "罗网投掷"
    learnLv = 35
    masterLv = 1
    maxLv = 11
    position = 4
    rangeLv = 3
    # cd = 17
    # 投掷cd
    cd = 14.7
    mp = [180, 1512]
    uuid = "d0cdaca82892e54097f22a1f60817048"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 投掷冷却时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 填装数量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 束缚几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 束缚持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 控制时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [罗网投掷]\n
        无法使用普通投掷； 强化[罗网投掷]命中时， 可以立即连接[毒瓶投掷]、 [毒针投掷]、 [砖块投掷]， 随后1.5秒内投掷物得到强化\n
        - 可以强制中断施放后僵直并施放[毒瓶投掷]、 [毒针投掷]、 [砖块投掷]\n
        - 持续时间内最多可以自动使用3次投掷强化\n
        [罗网投掷]速度 +100%\n
        再次投掷冷却时间 -70%\n
        - 总攻击力 -70%\n
        [罗网投掷]基本装填数变为1个
        """
        self.cd *= 0.3
        self.skillRation *= 0.3
        ...

    def vp_2(self):
        """
        [罗网投掷]\n
        无法使用[投掷强化]； 投掷更大的罗网、 投掷距离更远\n
        - 更快地投掷罗网\n
        束缚持续时间增加3秒， 控制时间增加1秒\n
        [毒瓶投掷]\n
        普通投掷时， 射程 +100%\n
        [毒针投掷]\n
        学习[后备口袋]后， 通电毒针打击攻击力 +110%\n
        [砖块投掷]\n
        普通投掷时， 射程 +100%
        """
        ...

    def effect(self, old, new):
        if self.vp == 2:
            self.associate = [
                {"type":"*power2","data":[0] + [(200+110)/(200)]*self.maxLv,"skills":["毒针投掷"]}
            ]
        return super().effect(old, new)

# 螺旋滑铲
# fighter_male/brawler_male/e0a072e8cef2d77893aad5f68aeed56a
# ca0f0e0e9e1d55b5f9955b03d9dd213c/e0a072e8cef2d77893aad5f68aeed56a
class Skill37(ActiveSkill):
    """
        向前方滑铲一定距离。\n
        移动时， 对碰撞的敌人造成伤害并使其进入失明状态。\n
        对无法抓取的敌人造成更多伤害。\n
        命中敌人时， 可以强制中断并施放[狂 · 霸王拳]， 施放技能时， 按向后方向键可以缩短滑铲距离。 (在决斗场中无效)
    """
    name = "螺旋滑铲"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [200, 1820]
    uuid = "e0a072e8cef2d77893aad5f68aeed56a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    power0 = 1.0
    # 多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 失明几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 失明时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 对无法抓取的怪物的伤害增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    mode = ['不可抓取','可抓取']

    def setMode(self, mode):
        if mode == "不可抓取":
            self.power0 = 1.2
        elif mode == "可抓取":
            self.power0 = 1.0

    def vp_1(self):
        """
        [螺旋滑铲]\n
        全力跃起后猛烈地滑铲地面， 激起大量尘土并落地\n
        - 变更为单次攻击\n
        - 总攻击力相同\n
        更细微地调整移动距离\n
        - 按向后方向键时， 移动距离大幅减少\n
        - 按向前方向键时， 移动距离增加
        """
        ...

    def vp_2(self):
        """
        [螺旋滑铲]\n
        可以强制中断[抛沙]及投掷类技能的施放后僵直并施放\n
        命中时， 可以强制中断并施放部分技能\n
        目标技能 : [毒雷引爆]、 [极恶飞锁]、 [千锁乱舞]、 [爆破污桶]、 [暗街夺命锁]、 [飞沙走石]\n
        - 按向后方向键施放技能时， 角色会回头施放\n
        减少多段攻击间隔
        """
        ...

# 狂 · 霸王拳
# fighter_male/brawler_male/b3659936a9a74c4ed6f7faf07cca1f9e
# ca0f0e0e9e1d55b5f9955b03d9dd213c/b3659936a9a74c4ed6f7faf07cca1f9e
class Skill38(PassiveSkill):
    """
        伏虎霸王拳攻击次数变更为1次， 攻击力和周围冲击波的范围大幅增加。\n
        对无法抓取的敌人也可以施放。 (不适用控制效果)\n
        攻击异常状态的敌人时， 伤害会更加强大， 冲击波范围也会增加(最多叠加3次)。
    """
    name = "狂 · 霸王拳"
    learnLv = 40
    masterLv = 1
    maxLv = 11
    position = 5
    rangeLv = 3
    cube = 1
    uuid = "b3659936a9a74c4ed6f7faf07cca1f9e"
    hasVP = True
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 伏虎霸王拳攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 冲击波范围增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 每种状态异常攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 每种异常状态的冲击波范围额外增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [狂·霸王拳]\n
        施放时投掷火焰瓶炸弹， 引发大范围爆炸\n
        - 对周围敌人造成与被抓取敌人相同的伤害\n
        - 抓取失败时也可以发动\n
        每个异常状态攻击力增加率变更为5%\n
        - 基本攻击力 +39.2%
        """
        ...

    def vp_2(self):
        """
        [狂·霸王拳]\n
        用锁链压制敌人后， 靠近并猛烈下砸\n
        - 基本冷却时间变更为45秒\n
        - 总攻击力 +200%
        """
        ...

    def effect(self, old, new):
        self.associate = [
        {"data":[i - 100 if i > 0 else i for i in self.data0],"skills":["伏虎霸王拳"]},
        {"type":"+hit0","data":[0] + [-200]*self.maxLv,"skills":["伏虎霸王拳"]},
        {"data":[i * 3 for i in self.data3],"skills":["伏虎霸王拳"]}
    ]
        if self.vp == 2:
            self.associate.append({"data":[0] + [-200]*self.maxLv,"skills":["伏虎霸王拳"],"type":"*cdRatio"})
            self.associate.append({"type":"*skillRation","data":[0] + [200]*self.maxLv,"skills":["伏虎霸王拳"]})
        return super().effect(old, new)

# 毒雷引爆
# fighter_male/brawler_male/6a1d1f08a6572be420bb3a256c44c015
# ca0f0e0e9e1d55b5f9955b03d9dd213c/6a1d1f08a6572be420bb3a256c44c015
class Skill39(ActiveSkill):
    """
        在前方悬空放置一枚毒地雷， 然后用侧踢击中地雷使其爆炸。\n
        爆炸的毒地雷会向喷发毒气柱攻击敌人， 并使敌人进入中毒状态。
    """
    name = "毒雷引爆"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 1
    cd = 24
    mp = [180, 1512]
    uuid = "6a1d1f08a6572be420bb3a256c44c015"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 踢击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 毒气柱攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 中毒攻击力: {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 中毒持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 爆炸范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [毒雷引爆]\n
        变更为同时引爆3枚毒地雷\n
        - 删除侧踢判定\n
        - 总攻击力相同\n
        - [后备口袋]开启时， 其中一个毒地雷造成灼伤效果
        """
        ...

    def vp_2(self):
        """
        [毒雷引爆]\n
        变更为投掷添加了特殊爆炸物的地雷\n
        地雷不会立即爆炸， 而是附着在敌人身上， 随后每次用消耗型投掷物或[爆破污桶]命中敌人时， 地雷会发生反应并爆炸\n
        - 地雷爆炸次数 : 3次\n
        - 最大附着时间 : 6秒\n
        - 爆炸时， 附加感电异常状态\n
        - 异常状态持续时间 +100%\n
        - 总攻击力相同
        """
        ...

# 极恶飞锁
# fighter_male/brawler_male/030663e99462f628b4c9f813e1406c4e
# ca0f0e0e9e1d55b5f9955b03d9dd213c/030663e99462f628b4c9f813e1406c4e
class Skill40(ActiveSkill):
    """
        挥舞数次锁链进行攻击后， 向前方下挥聚拢敌人。\n
        被锁链击中的敌人进入出血状态， 被终结打击命中的敌人会被拉到角色前方。\n
        挥舞锁链时， 可快速连按增加攻击速度， 按跳跃键时立即进行终结打击。
    """
    name = "极恶飞锁"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [450, 3780]
    uuid = "030663e99462f628b4c9f813e1406c4e"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 锁链挥舞攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 8
    # 锁链横扫出血攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 8
    # 锁链横扫攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最后一击攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 最后一击出血攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # 出血持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [极恶飞锁]\n
        发动技能时， 进入无敌状态\n
        锁链挥动范围 +10%
        """
        ...

    def vp_2(self):
        """
        [极恶飞锁]\n
        删除锁链挥动攻击力和攻击次数\n
        - 最后一击范围 +50%\n
        - 总攻击力相同
        """
        ...

# 千手奥义
# fighter_male/brawler_male/ab6fc3303df03b58911967dfca2b5d07
# ca0f0e0e9e1d55b5f9955b03d9dd213c/ab6fc3303df03b58911967dfca2b5d07
class Skill41(PassiveSkill):
    """
        熟练地使用各种投掷物， 让敌人更快地进入安息。\n
        增加投掷类技能的填装数和射出的速度， 并且减少投掷的时间间隔和填装间隔。\n
        并增加基本攻击力、 技能攻击力、 物理暴击率和魔法暴击率。
    """
    name = "千手奥义"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 3
    uuid = "ab6fc3303df03b58911967dfca2b5d07"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 填装数增加量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 强化的[砖块投掷]、 [毒瓶投掷]和[罗网投掷]的射出速度变化率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 其它投掷的射出速度变化率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 投掷时间间隔减少率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 填装时间间隔减少率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 基本攻击力和技能攻击力增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 物理、 魔法暴击率增加量 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    associate = [
        {"data":data5,"type":"*skillDamage"},
        {"data":data4,"type":"*cdReduce","skills":["抛沙","毒瓶投掷","毒针投掷","砖块投掷","罗网投掷"]},
    ]

# 天崩地裂
# fighter_male/brawler_male/c5a2956d8ed3af1746ed2f76ca971a09
# ca0f0e0e9e1d55b5f9955b03d9dd213c/c5a2956d8ed3af1746ed2f76ca971a09
class Skill42(ActiveSkill):
    """
        先用钩子抓裂地面， 使地面上的敌人受到爆炸伤害； 然后将地上的碎石勾起， 聚集成一块巨型石块投向地面。 石块落地时会产生强烈的冲击波并使周围的敌人受到巨大伤害。\n
    갈고리로 땅을 긁을 때 출혈 상태 이상을 걸며, 땅을 들어낸 지역에는 화염 지대가 생성되어 영역 내에 있는 적들에게 중독 및 화상을 건다.\n
        施放时， 使剩余填装数多于1的投掷类技能填装至最大值。
    """
    name = "天崩地裂"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [900, 7559]
    uuid = "c5a2956d8ed3af1746ed2f76ca971a09"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 地面爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 石块落地攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 出血攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 出血持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 火焰地带持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 每秒灼伤攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 6
    # 每秒中毒攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 6

# 爆破污桶
# fighter_male/brawler_male/5cac3411ccef1af333953e0ded5e942d
# ca0f0e0e9e1d55b5f9955b03d9dd213c/5cac3411ccef1af333953e0ded5e942d
class Skill43(ActiveSkill):
    """
        向前方敌人投掷一个装满炸药的肮脏木桶， 攻击大范围的敌人。\n
        受爆炸伤害的敌人进入减速和灼伤状态。
    """
    name = "爆破污桶"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [280, 784]
    uuid = "5cac3411ccef1af333953e0ded5e942d"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆炸攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 灼伤攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 灼伤持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 中毒攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 中毒持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 减速持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 移动速度减少率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 攻击速度减少率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [范围信息]
    # 爆炸范围比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

    def vp_1(self):
        """
        [爆破污桶]\n
        [诡诈之道]可强制中断其他技能后施放的技能列表中添加[爆破污桶]\n
        - 强制施放[爆破污桶]时进入无敌状态
        """
        ...

    def vp_2(self):
        """
        [爆破污桶]\n
        木桶中装填了更多的剧毒物质， 爆炸后形成毒雾区域\n
        - 施放时消耗10个[毒瓶投掷]装填数\n
        - 毒雾区域 : [毒瓶投掷] (强化)攻击力的1043%， 造成3秒中毒效果\n
        投掷物和爆炸范围 +40%\n
        投掷速度和距离 +100%\n
        [毒瓶投掷]\n
        攻击力 -50%
        """
        ...

    def effect(self, old, new):
        if self.vp == 2:
            self.associate = [
                {"type":"*skillRation","data":[0] + [-50]*self.maxLv,"skills":["毒瓶投掷"]},
                {"type":"+power9","data":[0] + [1043]*self.maxLv,"skills":["毒瓶投掷"]}
            ]
        return super().effect(old, new)

# 千锁乱舞
# fighter_male/brawler_male/dac8d8207618150c162e4c6f9e168527
# ca0f0e0e9e1d55b5f9955b03d9dd213c/dac8d8207618150c162e4c6f9e168527
class Skill44(ActiveSkill):
    """
        大幅挥舞锁链攻击敌人， 聚集至中央后强力拉拽。\n
        被最后拉拽攻击命中的远处敌人会被拉至前方。
    """
    name = "千锁乱舞"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [800, 1680]
    uuid = "dac8d8207618150c162e4c6f9e168527"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 打击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 出血攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 4
    # 出血持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 拉拽最小触发距离 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [千锁乱舞]\n
        更快地连续挥舞锁链聚集敌人\n
        - 连续打击次数 +100%\n
        - 施放速度 +35%\n
        - 范围 +30%\n
        - 总攻击力相同\n
        - 最后一击无视距离将敌人拉到自己面前\n
        利用[诡诈之道]连接消耗型投掷类技能时， 将该技能的装填数填装至最大值
        """
        ...

    def vp_2(self):
        """
        [千锁乱舞]\n
        挥舞锁链后不会拉回敌人， 直接结束技能\n
        变更为可填充2次的技能\n
        - 每次填充冷却时间 : 25秒\n
        - 单次攻击力 -50%\n
        可以强制中断[抛沙]及投掷类技能的施放后僵直并施放
        """
        ...
        self.cd = 25
        self.skillRation *= 0.5

# 诡诈之道
# fighter_male/brawler_male/a3880ba488ddca966c36c640cce927a7
# ca0f0e0e9e1d55b5f9955b03d9dd213c/a3880ba488ddca966c36c640cce927a7
class Skill45(PassiveSkill):
    """
        破坏规则， 并获得强力的战斗技术。\n
        增加基本攻击力和技能攻击力； 减少所有敌人的控制型异常状态抗性。 若学习了自动填充技能， 则进入地下城或复活时， 将自动装填消耗型投掷物。\n
        可以强制中断[毒雷引爆]、 [极恶飞锁]、 [千锁乱舞]、 [爆破污桶]、 [飞沙走石]， 并立即使用[抛沙]和投掷类技能。强制中断后使用技能时会进入霸体状态， 且不消耗投掷物。\n
        此功能可以在已学习的技能窗口上用鼠标右键设置开启/关闭。
    """
    name = "诡诈之道"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    uuid = "a3880ba488ddca966c36c640cce927a7"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 控制型异常状态抗性减少 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [ {"data":data1,"type":"*skillDamage"} ]

# 暗街夺命锁
# fighter_male/brawler_male/2b39a776471c142f581ad3cc8bb89e55
# ca0f0e0e9e1d55b5f9955b03d9dd213c/2b39a776471c142f581ad3cc8bb89e55
class Skill46(ActiveSkill):
    """
        把锁链插进地面后， 旋转锁链把周围敌人挑到空中， 使其进入出血状态， 随后抓起来扔到地面上。\n
        把周围敌人挑到空中时， 进入无敌状态。 扔出敌人之前， 按前方向键可以调整扔出的位置。\n
        按上方向键时， 会扔到最远的位置。 按前方向键时， 会把敌人扔到锁链插进地面的位置。 除此之外， 都会把敌人扔到面前。\n
        对无法抓取的敌人会造成单独的伤害， 不适用控制效果。
    """
    name = "暗街夺命锁"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 8
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "2b39a776471c142f581ad3cc8bb89e55"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 翻转地面攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 地面冲撞攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 对无法抓取的敌人的攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 出血时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 出血攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # [范围信息]
    # 地面冲撞爆炸范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    mode = ['不可抓取','可抓取']

    def setMode(self, mode):
        if mode == "不可抓取":
            self.hit0 = self.hit1 = 0
            self.hit2 = 1
        elif mode == "可抓取":
            self.hit0 = self.hit1 = 1
            self.hit2 = 0

    def vp_1(self):
        """
        [暗街夺命锁]\n
        电流通过锁链传导， 与地面碰撞时产生火花\n
        - 引发火焰， 攻击更大范围的敌人\n
        - 使陷入火焰中的敌人当前出血、 中毒异常状态伤害爆发\n
        - 使敌人进入灼伤、 感电状态， 效果持续15秒
        """
        ...

    def vp_2(self):
        """
        [暗街夺命锁]\n
        利用锁链破坏地面， 将巨型石块合并后与锁链一同向前方投掷\n
        - 投掷时， 消耗9个[砖块投掷]装填数\n
        - 删除翻转地面攻击力\n
        - 删除无法抓取敌人的例外情况\n
        - 删除附加出血效果\n
        - 石块命中时， 造成相当于[砖块投掷]砖块打击攻击力1671%的额外伤害， 并使敌人进入眩晕异常状态， 效果持续3秒\n
        - 投掷后， 可使用[诡诈之道]的强制中断功能\n
        - [暗街夺命锁]总攻击力相同\n
        [砖块投掷]\n
        攻击力 -30%
        """
        ...

    def effect(self, old, new):
        if self.vp == 2:
            self.associate = [
                {"type":"*skillRation","data":[0] + [-30]*self.maxLv,"skills":["砖块投掷"]},
                {"type":"+power13","data":[0] + [1671]*self.maxLv,"skills":["砖块投掷"]},
                {"type":"+power14","data":[0] + [1671]*self.maxLv,"skills":["砖块投掷"]}
            ]
        return super().effect(old, new)

# 飞沙走石
# fighter_male/brawler_male/b306cc4c67c775ab7ddff9785a3fe6a4
# ca0f0e0e9e1d55b5f9955b03d9dd213c/b306cc4c67c775ab7ddff9785a3fe6a4
class Skill47(ActiveSkill):
    """
        把锁镰插到天花板上， 随后拉拽铁链摧毁天花板， 掉落大量石块。\n
        石块可以强控敌人。\n
        最后掉落巨型石块， 使敌人进入出血状态并引起冲击波。
    """
    name = "飞沙走石"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "b306cc4c67c775ab7ddff9785a3fe6a4"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 小石块攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 10
    # 巨型石块攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 冲击波攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 出血持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 出血攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # [范围信息]
    # 攻击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [飞沙走石]\n
        不再掉落小型石块， 从天花板立即掉落巨型石块\n
        - 删除小石块攻击力\n
        - 总攻击力相同\n
        学习[诡诈之道]后， 强制中断时机变更为从天花板拉拽锁链后\n
        - 除[抛沙]和消耗型投掷技能外， 可以强制中断并施放转职技能
        """
        ...

    def vp_2(self):
        """
        [飞沙走石]\n
        向天花板投掷锁镰时， 同时投掷毒针， 毒针与破碎的天花板碎片一同坠落\n
        - 施放时， 消耗20个[毒针投掷]装填数\n
        - 不会掉落巨型石块\n
        - 小型石块掉落次数 +60%， 速度 +50%\n
        - 毒针攻击力 : [毒针投掷] (普通)攻击力的210%\n
        - 掉落的毒针中， 有一半不是造成出血状态， 而是造成感电状态\n
        - [飞沙走石]总攻击力相同\n
        攻击范围 +25%\n
        [毒针投掷]\n
        攻击力 -40%
        """
        ...

    def effect(self, old, new):
        if self.vp == 2:
            self.associate = [
                {"type":"*skillRation","data":[0] + [-40]*self.maxLv,"skills":["毒针投掷"]},
                {"type":"+power9","data":[0] + [210]*self.maxLv,"skills":["毒针投掷"]},
                {"type":"+power10","data":[0] + [210]*self.maxLv,"skills":["毒针投掷"]}
            ]
        return super().effect(old, new)

# 燃火轰天炮
# fighter_male/brawler_male/949849d5791944973d60af7e2a7eefb0
# ca0f0e0e9e1d55b5f9955b03d9dd213c/949849d5791944973d60af7e2a7eefb0
class Skill48(ActiveSkill):
    """
        用气势压制周围敌人， 强控敌人后， 用捆绑着轰天炮的铁管攻击。\n
        随后轰天炮连续爆炸并造成伤害。\n
        压制敌人时， 若敌人处于状态异常中， 则会造成更强力的伤害。 (最多叠加3次)
    """
    name = "燃火轰天炮"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 8
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "949849d5791944973d60af7e2a7eefb0"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 铁管打击 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第1次~第2次爆炸 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 2
    # 第3次~第5五次爆炸 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 3
    # 每种状态异常攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    associate = [
        {"type":"*skillDamage","data":[i*3 if i > 0 else i for i in data3],"skills":["燃火轰天炮"]}
    ]

# 逆道·爆狱
# fighter_male/brawler_male/dec8961c485edb02036ba00c789010f0
# ca0f0e0e9e1d55b5f9955b03d9dd213c/dec8961c485edb02036ba00c789010f0
class Skill49(ActiveSkill):
    """
        将装有特殊硬化剂的木桶滚向前方敌人， 造成伤害后， 用脚踢飞炸药桶使其爆炸。\n
        爆炸时， 强制控制范围内的敌人一定时间。\n
    [投掷强化]\n
    - 用装有易燃物质的金属桶代替木桶， 使其发生连锁爆炸。\n
    - 代替强制控制， 使敌人进入灼伤状态， 效果持续一定时间。
    """
    name = "逆道·爆狱"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [960, 7200]
    uuid = "dec8961c485edb02036ba00c789010f0"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 木桶攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    # 木桶攻击次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 强制控制时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [投掷强化]
    # 金属桶攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 5
    # 金属桶攻击次数上限 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 连锁爆炸攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 5
    # 连锁爆炸攻击次数上限 : {value7}次
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 灼伤持续时间 : {value8}秒
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 灼伤攻击力 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    hit9 = 5

    mode = ['常规','强化']

    def setMode(self, mode):
        if mode == "常规":
            self.hit0 = 5
            self.hit2 = 1
            self.hit4 = self.hit6 = self.hit9 = 0
        elif mode == "强化":
            self.hit0 = self.hit2 = 0
            self.hit4 = self.hit6 = self.hit9 = 5

# 逆道·皆允
# fighter_male/brawler_male/8e1891ddbdd5ebfcc4508ff2090c3e0f
# ca0f0e0e9e1d55b5f9955b03d9dd213c/8e1891ddbdd5ebfcc4508ff2090c3e0f
class Skill50(PassiveSkill):
    """
        不择手段， 只为追求胜利， 增加基本攻击力和转职技能攻击力， 变更部分投掷技能。\n
    [毒瓶投掷]\n
    - 普通投掷时， 投掷合并毒瓶和烈焰瓶的功能的特殊瓶。\n
    -  [投掷强化]状态下， 一段时间内在地面上生成毒雾， 进入毒雾范围的敌人会中毒。\n
    [砖块投掷]\n
    - 强化投掷时， 技能变更为抽起地面的锁链， 将圆形巨石向前方砸出的形态。\n
    [毒瓶投掷]普通投掷变更效果适用条件 : 在[后街战术]状态下， 获得[后备口袋]技能， 装填消耗量和攻击力与原技能一致。
    """
    name = "逆道·皆允"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "8e1891ddbdd5ebfcc4508ff2090c3e0f"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 强化毒瓶投掷毒雾持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [ {"data":data0,"type":"*skillDamage"} ]

# 逆道·幽链之界
# fighter_male/brawler_male/f1fdc6c2482ecc510a2a9f04201ba125
# ca0f0e0e9e1d55b5f9955b03d9dd213c/f1fdc6c2482ecc510a2a9f04201ba125
class Skill51(ActiveSkill):
    """
        将敌人引到街霸的大本营暗街， 用锁链攻击周围的敌人， 并摧毁建筑物。\n
        然后， 跳到空中， 将建筑物碎片聚集成巨型爆弹， 扔向敌人并将其引爆。\n
        爆炸攻击命中的敌人进入出血、 中毒、 灼伤状态， 效果持续一定时间。\n
        施放时， 使剩余填装数多于1的投掷类技能填装至最大值。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "逆道·幽链之界"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4025, 8055]
    uuid = "f1fdc6c2482ecc510a2a9f04201ba125"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

    # 锁链横扫次数上限 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 锁链挥舞攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 5
    # 锁链突刺攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 锁链旋转攻击次数上限 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 锁链旋转攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 10
    # 建筑炸弹地面上攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # 建筑炸弹爆炸攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 1
    # 异常状态持续时间 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 出血攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    hit8 = 1
    # 中毒攻击力 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    hit9 = 1
    # 灼伤攻击力 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    hit10 = 1


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'brawler_male'
        self.nameCN = '归元·街霸'
        self.role = 'fighter_male'
        self.角色 = '格斗家(男)'
        self.职业 = '街霸'
        self.jobId = 'ca0f0e0e9e1d55b5f9955b03d9dd213c'
        self.jobGrowId = '6d459bc74ba73ee4fe5cdc4655400193'

        self.武器选项 = ['手套', '臂铠','爪','东方棍']
        self.输出类型选项 = ['魔法百分比', '物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量', '智力']
        self.防具类型 = '重甲'
        self.buff = 1.861

        super().__init__(equVersion, __name__)
