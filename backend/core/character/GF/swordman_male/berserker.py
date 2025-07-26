#41f1cdc2ff58bb5fdc287be0db2a8df3
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "swordman_male/berserker/cn/skillDetail"

# 血气旺盛
# swordman_male/berserker/d296043df164385a14cb973c8c7c4d07
# 41f1cdc2ff58bb5fdc287be0db2a8df3/d296043df164385a14cb973c8c7c4d07
class Skill2(PassiveSkill):
    """
    施放[十字刃]时， 用生命值的消减来代替魔法值消减， 并增加召唤出的十字的大小。\n
    包括[十字刃]与[崩山击]在内的转职后技能新增出血效果。
    """
    name = "血气旺盛"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "d296043df164385a14cb973c8c7c4d07"
    hasVP = False
    hasUP = False

    # [十字刃]攻击范围增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 出血几率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 出血持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 出血攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 崩山击
# swordman_male/berserker/6e33d47e6622ce03b6defdd912140270
# 41f1cdc2ff58bb5fdc287be0db2a8df3/6e33d47e6622ce03b6defdd912140270
class Skill13(ActiveSkill):
    """
    向前低跃并用武器砸击地面， 对敌人造成多段攻击伤害， 最后一击可以使敌人倒地。\n
    跳跃距离和冲击波范围会随技能键按放间隔长短而改变。\n
    转职为狂战士后， 可以强制中断基本攻击动作， 并立即施放该技能。
    """
    name = "崩山击"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 4
    mp = [17, 150]
    uuid = "6e33d47e6622ce03b6defdd912140270"
    hasVP = False
    hasUP = False

    # 下砸攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3 # 3.4
    # 下砸多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 冲击波攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 冲击波范围比率 : {value3} ~ {value4}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    data4 = get_data(f'{prefix}/{uuid}', 4)


# 狂暴血气
# swordman_male/berserker/2f5d03c7848effbc0a23f4df45d9ca46
# 41f1cdc2ff58bb5fdc287be0db2a8df3/2f5d03c7848effbc0a23f4df45d9ca46
class Skill17(PassiveSkill):
    """
    进入狂暴血气状态， 乱刀攻击敌人。\n
    激活该技能后， [狂暴之力]下的基本攻击会一直反复第一击和第二击。\n
    可使用右键点击技能On/Off技能特效。
    """
    name = "狂暴血气"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 5
    rangeLv = 3
    uuid = "2f5d03c7848effbc0a23f4df45d9ca46"
    hasVP = False
    hasUP = False


# 力量唤醒
# swordman_male/berserker/42c82812f86ff6704ae9952a2e6093a4
# 41f1cdc2ff58bb5fdc287be0db2a8df3/42c82812f86ff6704ae9952a2e6093a4
class Skill22(PassiveSkill):
    """
    增加技能攻击力、 攻击速度和移动速度。\n
    生命值越低增加的值越大， 且根据剩余生命值的比例阶段性增加。
    """
    name = "力量唤醒"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 7
    rangeLv = 3
    uuid = "42c82812f86ff6704ae9952a2e6093a4"
    hasVP = False
    hasUP = False

    # 技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击速度增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 移动速度增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [力量唤醒1阶段]
    # 发动的生命值比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 攻击速度增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 移动速度增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 回避率增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # [力量唤醒2阶段]
    # 发动的生命值比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 攻击速度增加率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 移动速度增加率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # 回避率增加率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # [力量唤醒3阶段]
    # 发动的生命值比率 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # 攻击速度增加率 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)
    # 移动速度增加率 : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # 回避率增加率 : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)

    associate = [{"data":data0}]

# 十字刃
# swordman_male/berserker/ca75c965f20a150f99f54155a37400df
# 41f1cdc2ff58bb5fdc287be0db2a8df3/ca75c965f20a150f99f54155a37400df
class Skill24(ActiveSkill):
    """
    挥动武器向敌人发出十字形攻击， 并召唤出十字攻击敌人。\n
    若已学习[血气旺盛]， 则施放技能时用生命值的消耗来代替魔法值消耗， 并且使被击中的敌人进入出血状态。\n
    转职为狂战士后， 可以强制中断其他动作并立即施放该技能。 若在召唤十字的瞬间按技能键， 可以发动可击退敌人的强力追击。\n
    [学习血气界限后]\n
    删除斩击和追加按键功能； 发动交叉斩击， 向前方发射十字。
    """
    name = "十字刃"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 6
    mp = [58, 249]
    uuid = "ca75c965f20a150f99f54155a37400df"
    hasVP = False
    hasUP = True

    # 斩击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2
    # 斩击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 血十字攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 追击攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 学习[血气旺盛]后生命值消耗量 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 学习[血气界限]后
    # 血十字攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [范围信息]
    # 血十字大小比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

# 狂暴之力
# swordman_male/berserker/6a1d1f08a6572be420bb3a256c44c015
# 41f1cdc2ff58bb5fdc287be0db2a8df3/6a1d1f08a6572be420bb3a256c44c015
class Skill25(ActiveSkill):
    """
    施放[狂暴之力]后， 每隔一段时间会消耗一定量的生命值， 提升命中率和硬直， 同时增加基本攻击力和[崩山击]、 [十字刃]等狂战士转职技能的攻击力， 并减少冷却时间。\n
    基本攻击会转变成二刀流攻击。\n
    [连突刺]、 [空之连刃]变更为独立攻击力。\n
    若击败出血状态的敌人， 则可以恢复自身一定量的生命值。\n
    可以通过On/Off激活或关闭技能。\n
    [狂暴之力]处于On状态时， 进入地下城或复活时将自动施放[狂暴之力]。\n
    学习[血气旺盛]后， 可以使被击中的敌人进入出血状态。
    """
    name = "狂暴之力"
    learnLv = 15
    masterLv = 20
    maxLv = 30
    position = 4
    rangeLv = 3
    cd = 10
    mp = [10, 35]
    uuid = "6a1d1f08a6572be420bb3a256c44c015"
    hasVP = False
    hasUP = False

    # 施放时生命值消耗量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 每10秒生命值消耗量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 命中率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 硬直增加量 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 基本攻击力和技能攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 转职系列技能冷却时间减少率 : {value5}% (觉醒技能除外)
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 生命值吸收量上限 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)

    associate = [
        {"data": data4, "type": '*skillRation'},
        {'data': data5, 'type': '*cdReduce', 'exceptSkills': ['魔狱血刹', '血魔 · 弑天', '血魔极道 : 灭世']}
    ]

# 死亡抗拒
# swordman_male/berserker/1dad88963abdc96b091fcab185a8820d
# 41f1cdc2ff58bb5fdc287be0db2a8df3/1dad88963abdc96b091fcab185a8820d
class Skill27(ActiveSkill):
    """
    恢复自身一定量的生命值并增加物理/魔法防御力和硬直， 效果持续一定时间， 但只能在自身生命值较低时施放。
    """
    name = "死亡抗拒"
    learnLv = 20
    masterLv = 1
    maxLv = 11
    position = 6
    rangeLv = 3
    cd = 10
    mp = [40, 448]
    uuid = "1dad88963abdc96b091fcab185a8820d"
    hasVP = False
    hasUP = False

    # 恢复时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 生命值恢复 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 增加物防 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 增加魔防 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 增加硬直 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 可发动技能的生命值比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

# 狂气斩
# swordman_male/berserker/bbc15561bec24f9c1e79e23d715b1dd2
# 41f1cdc2ff58bb5fdc287be0db2a8df3/bbc15561bec24f9c1e79e23d715b1dd2
class Skill29(ActiveSkill):
    """
    只能在[狂暴之力]状态下使用。\n
    用双手的剑斩击敌人。 斩击过程中再次按技能键时， 可以额外攻击1次。\n
    按前方向键时， 可以向前滑行并施放技能， 按后方向键则往反方向施放。\n
    学习[血气旺盛]后， 可以使被击中的敌人进入出血状态。
    """
    name = "狂气斩"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 6
    mp = [62, 266]
    uuid = "bbc15561bec24f9c1e79e23d715b1dd2"
    hasVP = False
    hasUP = True

    # 第一次斩击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2
    # 第一次斩击多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 第二次斩击攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 2
    # 第二次斩击多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

# 嗜魂之手
# swordman_male/berserker/3829c15bf5f520c13998a3479ba0ce7b
# 41f1cdc2ff58bb5fdc287be0db2a8df3/3829c15bf5f520c13998a3479ba0ce7b
class Skill30(ActiveSkill):
    """
    抓取前方一名敌人并吸进其血气后， 再把吸进的血气喷发， 对敌人造成伤害。\n
    对出血状态的敌人施放时， 可以造成更多伤害。\n
    对无法抓取的敌人不适用控制效果。\n
    [转职为狂战士后]\n
    在[饥渴]状态下， 可增加吸血次数。\n
    学习[血气旺盛]后， 可以使被击中的敌人进入出血状态。\n
    学习[血气界限]后， 血气喷发范围变更为全方位； 即使未抓住敌人， 也可以生成血块后使其爆炸。
    """
    name = "嗜魂之手"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 6
    mp = [37, 290]
    uuid = "3829c15bf5f520c13998a3479ba0ce7b"
    hasVP = False
    hasUP = True

    # 抓取攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 喷发攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 抓取出血状态的敌人时追加攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 饥渴状态下吸收次数变化值 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 攻击无法抓取敌人时的喷发攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 0
    # [学习血气界限后]
    # 抓取攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 气息爆炸攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 抓取失败时， 攻击无法抓取敌人时的气息爆炸攻击力 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # [范围信息]
    # 喷发范围比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)

    mode = ['不可抓取','可抓取']

    def setMode(self, mode):
        if mode == '可抓取':
            self.hit0 = self.hit1 = self.hit2 = 1
            self.hit4 = 0
        if mode == '不可抓取':
            self.hit0 = self.hit1 = self.hit2 = 0
            self.hit4 = 1


# 暴走
# swordman_male/berserker/0ed3148658fe37b3336ccb718dc0fdb0
# 41f1cdc2ff58bb5fdc287be0db2a8df3/0ed3148658fe37b3336ccb718dc0fdb0
class Skill31(ActiveSkill):
    """
    使自身进入暴走状态， 可以增加技能攻击力、 移动速度、 攻击速度、 眩晕和睡眠异常状态抗性和硬直， 效果持续一定时间； 但自身的智力、 物防、 魔防将减少。\n
    暴走状态下， 增加[狂暴之力]基本攻击和[崩山击]、 [十字刃]技能的僵直度， 减少动作延迟。
    """
    name = "暴走"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 3
    cd = 5
    uuid = "0ed3148658fe37b3336ccb718dc0fdb0"
    hasVP = False
    hasUP = False

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击速度增加量 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 移动速度增加量 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 眩晕、 睡眠异常状态抗性增加量 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 智力减少量 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 物理防御力减少量 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 魔法防御力减少量 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 硬直增加 : {value8}
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [十字刃]、 [崩山击]、 [狂暴之力]基本攻击僵直增加 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [十字刃]、 [崩山击]、 [狂暴之力]基本攻击动作延迟减少 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)

# 怒气爆发
# swordman_male/berserker/506e7ed77d517419a6e1c437a2cedb17
# 41f1cdc2ff58bb5fdc287be0db2a8df3/506e7ed77d517419a6e1c437a2cedb17
class Skill32(ActiveSkill):
    """
    向自身周围的敌人爆发怒气， 使周围的敌人受到一定的物理伤害并浮空。\n
    学习[血气旺盛]后， 可以使被击中的敌人进入出血状态。
    """
    name = "怒气爆发"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 13
    mp = [142, 607]
    uuid = "506e7ed77d517419a6e1c437a2cedb17"
    hasVP = False
    hasUP = True

    # 冲击波攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 血气喷发攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 10
    # 血气喷发多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 狂热回旋
# swordman_male/berserker/de20372767d014d62dc7361ac686834e
# 41f1cdc2ff58bb5fdc287be0db2a8df3/de20372767d014d62dc7361ac686834e
class Skill33(ActiveSkill):
    """
    挥剑将两边的敌人吸附到自己的前方后， 在原地使用回旋上斩击飞敌人。\n
    学习[血气旺盛]后， 可以使被击中的敌人进入出血状态。
    """
    name = "狂热回旋"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 6
    rangeLv = 2
    cd = 10
    mp = [110, 467]
    uuid = "de20372767d014d62dc7361ac686834e"
    hasVP = False
    hasUP = True

    # 第一次吸附攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第二次吸附攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 上斩物理攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 饥渴
# swordman_male/berserker/547ab2b2bd860d3e37355a9cfbc1077c
# 41f1cdc2ff58bb5fdc287be0db2a8df3/547ab2b2bd860d3e37355a9cfbc1077c
class Skill34(ActiveSkill):
    """
    长按技能键进行蓄气， 每次蓄气都会消耗生命值， 进入饥渴状态。\n
    进入[饥渴]状态时生成攻击波。 被冲击波攻击的敌人进入出血状态。\n
    在[饥渴]状态下， 大幅度提升基本攻击力和[崩山击]、 [十字刃]等狂战士转职技能的攻击力。
    """
    name = "饥渴"
    learnLv = 35
    masterLv = 10
    maxLv = 20
    position = 3
    rangeLv = 3
    cd = 5
    uuid = "547ab2b2bd860d3e37355a9cfbc1077c"
    hasVP = False
    hasUP = False

    # 基本生命值减少 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 蓄气每阶段生命值减少 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 基本攻击力和技能攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # - [使用饥渴时冲击波] -
    # 出血攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 出血持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 出血诱发范围 : {value6}px
    data6 = get_data(f'{prefix}/{uuid}', 6)
    associate = [{"data":data3}]

# 嗜魂封魔斩
# swordman_male/berserker/1b1cfab062e0768bcc889e33e1f30dbf
# 41f1cdc2ff58bb5fdc287be0db2a8df3/1b1cfab062e0768bcc889e33e1f30dbf
class Skill35(ActiveSkill):
    """
    只能在[狂暴之力]已施放的状态下使用。\n
    用旋风把前方敌人吸附到近身处， 强力击打敌人并将其击飞。\n
    对无法抓取的敌人不适用控制效果。\n
    学习[血气旺盛]后， 可以使被击中的敌人进入出血状态。
    """
    name = "嗜魂封魔斩"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cube = 1
    cd = 25
    mp = [323, 1377]
    uuid = "1b1cfab062e0768bcc889e33e1f30dbf"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 击打攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 击打范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [嗜魂封魔斩]\n
        变更为全方位吸附敌人\n
        斩击时将周围的敌人推向前方\n
        吸附敌人时， 可以预输入[浴血之怒]或[致命血陨]技能\n
         - 代替斩击发动预输入的技能\n
         - [浴血之怒]或[致命血陨]的最后一击会合算斩击的伤害\n
        吸附到敌人时， 恢复7%生命值
        """
        ...

    def vp_2(self):
        """
        [嗜魂封魔斩]\n
        长按技能键时， 可以维持吸附后斩击的准备动作\n
         - 最多可以维持5秒\n
        发动斩击前为止， 所受伤害 -80%\n
        可以强制中断斩击后僵直， 并施放包括格挡在内的其他攻击技能\n
        吸附范围和斩击范围 +30%
        """
        ...

# 暴怒狂斩
# swordman_male/berserker/e36ae35f8964d92e30e33529a65544d7
# 41f1cdc2ff58bb5fdc287be0db2a8df3/e36ae35f8964d92e30e33529a65544d7
class Skill36(ActiveSkill):
    """
    只能在[狂暴之力]状态下使用。\n
    用武器下劈， 使敌人浮空后发动二刀流乱砍攻击。\n
    每次挥动武器时， 在空中留下剑痕， 最后与剑痕一起撕裂敌人。\n
    学习[血气旺盛]后， 可以使被击中的敌人进入出血状态。
    """
    name = "暴怒狂斩"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 1
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [113, 1117]
    uuid = "e36ae35f8964d92e30e33529a65544d7"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 锤击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 乱砍攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 8
    # 乱砍攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最后一击攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 2
    # 最后一击攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # [范围信息]
    # 范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

    def vp_1(self):
        """
        [暴怒狂斩]\n
        删除下劈， 以强化形态发动\n
         - 总攻击力相同\n
        可以强制中断最后一击的施放后僵直， 并施放包括格挡在内的其他攻击技能\n
        施放过程中所受伤害 -50%
        """
        ...

    def vp_2(self):
        """
        [暴怒狂斩]\n
        在空中挥剑留下血痕， 然后猛击地面使血痕爆炸\n
         - 总攻击力相同\n
        施放时消耗3%的当前生命值进行强化\n
         - 攻击范围 +50%\n
         - 命中时恢复5%的生命值
        """
        ...

# 爆发之刃
# swordman_male/berserker/e0daa922b19cdc35de879e938361464e
# 41f1cdc2ff58bb5fdc287be0db2a8df3/e0daa922b19cdc35de879e938361464e
class Skill37(ActiveSkill):
    """
    只能在[狂暴之力]状态下使用。\n
    在前方生成爆发之刃， 然后向敌人发出强威力的刺击； 技能命中敌人时， 会产生爆炸。\n
    技能命中后， 可以强制中断， 施放包括格挡在内的其他攻击技能。\n
    施放技能时， 按后方向键， 可以原地刺击敌人。\n
    学习[血气旺盛]后， 可以使被击中的敌人进入出血状态。
    """
    name = "爆发之刃"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [297, 1267]
    uuid = "e0daa922b19cdc35de879e938361464e"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 爆炸攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 爆炸范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [爆发之刃]\n
        即使血刃未刺中敌人也会快速发生爆炸\n
        爆炸范围 +50%\n
        若爆炸未命中敌人， 剩余冷却时间缩短为3秒
        """
        ...

    def vp_2(self):
        """
        [爆发之刃]\n
        施放时消耗当前3%的生命值， 以强化形态发动\n
         - 爆炸范围 +20%\n
         - 命中时恢复10%的生命值\n
        爆炸前会将一定范围内的敌人吸附至爆炸中心
        """
        ...

# 崩山裂地斩
# swordman_male/berserker/ecc23c980ea71450c0ad0c3fd232f329
# 41f1cdc2ff58bb5fdc287be0db2a8df3/ecc23c980ea71450c0ad0c3fd232f329
class Skill38(ActiveSkill):
    """
    只能在[狂暴之力]已施放的状态下使用。\n
    召唤出血气之剑， 跳跃后猛力捶击地面， 地面喷出的炙热岩浆攻击敌人。\n
    施放技能时， 按向后方向键可以减少前进距离， 按向前方向键可以增加前近距离。\n
    学习[血气旺盛]后， 可以使被击中的敌人进入出血状态。
    """
    name = "崩山裂地斩"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [456, 1944]
    uuid = "ecc23c980ea71450c0ad0c3fd232f329"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 捶击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 岩浆攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 6
    # 岩浆多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [崩山裂地斩]\n
        血剑锤击地面的瞬间喷出岩浆\n
        范围 +40%\n
        被命中的敌人不会倒地， 但会进入僵直状态， 并且每次被击时逐渐向中心位置移动
        """
        ...

    def vp_2(self):
        """
        [崩山裂地斩]\n
        变更为可填充2次的技能\n
         - 单次攻击力 -50%\n
         - 每次填充冷却时间 : 20秒\n
         - 降低跳跃高度\n
        施放技能时进入无敌状态
        """
        self.cd = 20
        self.skillRation *= 0.5
        ...

# 鲜血之忆
# swordman_male/berserker/dbf8b30c7057032af0d68fcfa289fdae
# 41f1cdc2ff58bb5fdc287be0db2a8df3/dbf8b30c7057032af0d68fcfa289fdae
class Skill39(PassiveSkill):
    """
    若周围一定范围内存在处于出血状态的敌人或友军， 则可以增加自身的独立攻击力、 命中率和物理暴击率。
    """
    name = "鲜血之忆"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    uuid = "dbf8b30c7057032af0d68fcfa289fdae"
    hasVP = False
    hasUP = False

    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 独立攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 命中率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 物理暴击率增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    associate = [{"data": data1,"type": '$*PAtkI'}]

# 魔狱血刹
# swordman_male/berserker/8572675ec6a1f50b6eff6a867376c2de
# 41f1cdc2ff58bb5fdc287be0db2a8df3/8572675ec6a1f50b6eff6a867376c2de
class Skill40(ActiveSkill):
    """
    施放技能后， 召唤出血气之剑。\n
    持续时间结束或再次按技能键时， 下劈血气之剑， 引发血气爆炸并强控敌人， 使敌人受到多段伤害。\n
    召唤出血气之剑的状态下， 攻击速度和移动速度增加。\n
    学习[血气旺盛]后， 可以使被击中的敌人进入出血状态。
    """
    name = "魔狱血刹"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [900, 7559]
    uuid = "8572675ec6a1f50b6eff6a867376c2de"
    hasVP = False
    hasUP = False

    # 血气之剑持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击速度增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 移动速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 下劈攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # 血气爆发多段攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 27
    # 血气爆发多段攻击次数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 狂怒暴掠
# swordman_male/berserker/f1fdc6c2482ecc510a2a9f04201ba125
# 41f1cdc2ff58bb5fdc287be0db2a8df3/f1fdc6c2482ecc510a2a9f04201ba125
class Skill41(ActiveSkill):
    """
    抓取前方敌人后， 跳起将敌人砸向地面， 引发剧烈血气爆炸。\n
    按向前方向键施放时， 向前突进并抓取敌人。\n
    对无法抓取的敌人不适用控制效果。\n
    学习[血气旺盛]后， 可以使被击中的敌人进入出血状态。
    """
    name = "狂怒暴掠"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 2
    cd = 30
    mp = [344, 963]
    uuid = "f1fdc6c2482ecc510a2a9f04201ba125"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 抓起攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 气息爆炸攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 最后一击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [狂怒暴掠]\n
        不抓取敌人也可以引发气息爆炸\n
        施放过程中发动[强悍碾压]或[崩山裂地斩]时， 引发气息爆炸的同时发动该技能\n
        气息爆炸范围 20%
        """
        ...

    def vp_2(self):
        """
        [狂怒暴掠]\n
        施放时， 追踪并抓取一定范围内最强的敌人\n
         - 若范围内没有敌人则无法施放\n
        可以强制中断气息爆炸后僵直并施放转职技能
        """
        ...

# 狂气涌动
# swordman_male/berserker/75747c67e14eec6088ce67f63ea41628
# 41f1cdc2ff58bb5fdc287be0db2a8df3/75747c67e14eec6088ce67f63ea41628
class Skill42(ActiveSkill):
    """
    在持续时间内， 狂战士即使受到伤害， 生命值也不会减少到一定程度以下。\n
    当生命值降到一定程度以下后被攻击时， 会生成血气防御罩， 并在较短的时间平复所受伤害。\n
       除被击状态以外， 该技能可以在任何状态下使用。\n
    冷却时间减少效果不适用于该技能。
    """
    name = "狂气涌动"
    learnLv = 65
    masterLv = 1
    maxLv = 1
    position = 3
    rangeLv = 3
    mp = [450, 450]
    uuid = "75747c67e14eec6088ce67f63ea41628"
    hasVP = False
    hasUP = False

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 未减少的生命值比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 血气防御罩持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 冷却时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 强悍碾压
# swordman_male/berserker/3a691a432c58abebc08211df45c4f4bd
# 41f1cdc2ff58bb5fdc287be0db2a8df3/3a691a432c58abebc08211df45c4f4bd
class Skill43(ActiveSkill):
    """
    伸手并用剑划开自己的手掌， 用手上喷发出来的血气形成血剑后， 高举血剑砸向地面， 引发巨大的爆炸。\n
    学习[血气旺盛]后， 可以使被击中的敌人进入出血状态。
    """
    name = "强悍碾压"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [534, 1771]
    uuid = "3a691a432c58abebc08211df45c4f4bd"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 生命值消耗量 : 当前生命值的{value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 血气爆发多段攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 5
    # 血气爆发多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [强悍碾压]\n
        爆炸范围缩小， 额外发生2次爆炸\n
         - 多段攻击次数 +80%\n
         - 总攻击力相同\n
        爆炸的血气化作盔甲将自身包围\n
         - 发生爆炸后进入霸体状态10秒\n
         - 发生爆炸后10秒内所有速度 +10%
        """
        ...

    def vp_2(self):
        """
        [强悍碾压]\n
        施放过程中发动[狂怒暴掠]或[崩山裂地斩]时， 引发气息爆炸的同时发动该技能\n
        爆炸范围 +15%
        """
        ...

# 汲血之力
# swordman_male/berserker/374f53e8989ef04a8506c8ec99d9ecdc
# 41f1cdc2ff58bb5fdc287be0db2a8df3/374f53e8989ef04a8506c8ec99d9ecdc
class Skill44(PassiveSkill):
    """
    增加基本攻击力和[崩山击]、 [十字刃]等狂战士转职技能的攻击力。 施放[嗜魂之手]时进入霸体状态。 
    """
    name = "汲血之力"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "374f53e8989ef04a8506c8ec99d9ecdc"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data": data0,"type": '*skillRation'}]

# 浴血之怒
# swordman_male/berserker/8ec9da6f808889b63adf2680fbf1f331
# 41f1cdc2ff58bb5fdc287be0db2a8df3/8ec9da6f808889b63adf2680fbf1f331
class Skill45(ActiveSkill):
    """
    爆发血气之怒， 而使角色在指定地点发动大规模的血气爆炸。\n
    被爆炸命中的敌人会受到伤害。\n
    学习[血气旺盛]后， 可以使被击中的敌人进入出血状态。
    """
    name = "浴血之怒"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "8ec9da6f808889b63adf2680fbf1f331"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 施放时生命值消耗量 : 当前生命值的{value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 大规模血气爆炸攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    def vp_1(self):
        """
        [浴血之怒]\n
        气息爆炸命中敌人时吸收目标的血气\n
         - 每命中1名敌人恢复5%的生命值(最多6人)\n
         - 吸收血气时力量唤醒固定为3阶段， 效果持续20秒\n
        气息爆炸范围 +30%
        """
        ...

    def vp_2(self):
        """
        [浴血之怒]\n
        变更为可填充2次的技能\n
         - 单次攻击力 -50%\n
         - 每次填充冷却时间 : 20秒\n
        立即在手中生成血气并引爆
        """
        self.cd = 20
        self.skillRation *= 0.5
        ...

# 致命血陨
# swordman_male/berserker/00e4f916cc182df49e5efd29c3e2069c
# 41f1cdc2ff58bb5fdc287be0db2a8df3/00e4f916cc182df49e5efd29c3e2069c
class Skill46(ActiveSkill):
    """
    吸取血气生成剑， 快速斩击敌人两次后发动交叉斩击， 造成致命伤害。\n
    施放时按向前方向键， 可以增加前进距离。\n
    学习[血气旺盛]后， 可以使被击中的敌人进入出血状态。
    """
    name = "致命血陨"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 5
    cd = 50
    mp = [848, 6360]
    uuid = "00e4f916cc182df49e5efd29c3e2069c"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 上斩攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 横斩攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 交叉斩击攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [致命血陨]\n
        删除交叉斩击， 上斩、 横斩各增加1次\n
         - 总攻击力相同\n
        按向前方向键时， 可以前进更远\n
        使命中的敌人聚集到前方\n
        施放过程中所受伤害 -80%
        """
        ...

    def vp_2(self):
        """
        [致命血陨]\n
        施放时消耗当前3%的生命值， 发动一次致命斩击\n
         - 总攻击力相同\n
         - 命中时恢复15%的生命值
        """
        ...

# 血魔 · 弑天
# swordman_male/berserker/c524c4f378d1cd0ff99e4580750a4567
# 41f1cdc2ff58bb5fdc287be0db2a8df3/c524c4f378d1cd0ff99e4580750a4567
class Skill47(ActiveSkill):
    """
    化身为血魔， 暴走并突击前方的敌人， 同时引发血气爆炸。\n
    学习[血气旺盛]后， 可以使被击中的敌人进入出血状态。
    """
    name = "血魔 · 弑天"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "c524c4f378d1cd0ff99e4580750a4567"
    hasVP = False
    hasUP = False

    # 血魔突击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2
    # 血魔突击多段攻击次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 血气爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1

# 疯魔血魂斩
# swordman_male/berserker/a99040fc36c75e998aa3ed012b7759c5
# 41f1cdc2ff58bb5fdc287be0db2a8df3/a99040fc36c75e998aa3ed012b7759c5
class Skill48(ActiveSkill):
    """
    生成巨大血气团， 并下劈将其破坏， 然后将血气团在前方击碎， 飞散血气碎片。\n
    学习[血气旺盛]后， 可以使被击中的敌人进入出血状态。
    """
    name = "疯魔血魂斩"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [1017, 7632]
    uuid = "a99040fc36c75e998aa3ed012b7759c5"
    hasVP = False
    hasUP = False

    # 冲击波攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 血气碎片攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 5
    # 血气喷发多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 血气界限
# swordman_male/berserker/b39ccc3dadab9d94569430e39cdf7d60
# 41f1cdc2ff58bb5fdc287be0db2a8df3/b39ccc3dadab9d94569430e39cdf7d60
class Skill49(PassiveSkill):
    """
    成功利用血气抑制卡赞综合征， 并获得爆发性的力量， 性情变得更加残忍。\n
    增加基本攻击力和[崩山击]、 [十字刃]等转职技能攻击力， 并变更部分技能。\n
    [十字刃]\n
    删除斩击和追加按键功能； 发动交叉斩击， 向前方发射十字。\n
    [嗜魂之手]\n
    血气喷发范围变更为全方位； 即使未抓住敌人， 也可以生成血块后使其爆炸。
    """
    name = "血气界限"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "b39ccc3dadab9d94569430e39cdf7d60"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    associate = [{"data": data0,"type": '*skillRation'}]

# 血魔极道 : 灭世
# swordman_male/berserker/d59c9840f65381bde8487757f1753c71
# 41f1cdc2ff58bb5fdc287be0db2a8df3/d59c9840f65381bde8487757f1753c71
class Skill50(ActiveSkill):
    """
    使血气上涨， 抑制卡赞综合征的暴走， 变身成为血魔， 获得超越肉体极限的爆发性力量。\n
    追踪最强大的敌人， 并对其连续斩击， 以压倒性的力量将敌人砸向地面， 拔出血剑攻击敌人。 然后， 地面喷发血气， 对周围所有敌人造成伤害。\n
    掌握[血气旺盛]时， 可以使被击中的敌人进入出血状态。\n
    [三次觉醒技能]\n
    选择[魔狱血刹]使用三次觉醒技能时， 可以使用三次觉醒技能代替[魔狱血刹]的终结攻击。 三次觉醒技能在冷却中或[魔狱血刹]未激活的状态下， 无法使用三次觉醒技能。\n
    选择[血魔 · 弑天]使用三次觉醒技能时， 与[血魔 · 弑天]共享冷却时间。 [血魔 · 弑天]在冷却中时， 无法使用三次觉醒技能。
    """
    name = "血魔极道 : 灭世"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4027, 8055]
    uuid = "d59c9840f65381bde8487757f1753c71"
    hasVP = False
    hasUP = False

    # 乱舞攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 乱舞攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 跳跃下斩攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 2
    # 跳跃下斩多段攻击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 地面捶击攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # 斩击攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # 血气喷发攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 8
    # 血气喷发多段攻击次数 : {value7}次
    data7 = get_data(f'{prefix}/{uuid}', 7)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'berserker'
        self.nameCN = '极诣·狂战士'
        self.role = 'swordman_male'
        self.角色 = '鬼剑士(男)'
        self.职业 = '狂战士'
        self.jobId = '41f1cdc2ff58bb5fdc287be0db2a8df3'
        self.jobGrowId = '6d459bc74ba73ee4fe5cdc4655400193'

        self.武器选项 = ['太刀', '钝器', '巨剑', '短剑']
        self.输出类型选项 = ['物理固伤','魔法固伤']
        self.输出类型 = '物理固伤'
        self.防具精通属性 = ['力量']
        self.防具类型 = '重甲'
        self.buff = 2.245

        super().__init__(equVersion, __name__)
