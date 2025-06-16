#b9cb48777665de22c006fabaf9a560b3
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "archer/chimera/cn/skillDetail"

# 凌跃一击
# archer/chimera/0969cd4054d93da07708108c0cc1c4b5
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
    position = 6
    rangeLv = 3
    cd = 2
    uuid = "0969cd4054d93da07708108c0cc1c4b5"
    hasVP = False
    hasUP = False

    # 箭矢攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
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
    hit6 = 1
    # 冲击波攻击力 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)
    hit7 = 1



# 基础精通
# archer/chimera/5a56514f35cf0270ae8d6c65f8fefd78
# b9cb48777665de22c006fabaf9a560b3/5a56514f35cf0270ae8d6c65f8fefd78
class Skill2(PassiveSkill):
    """
    增加基本攻击、 前冲攻击、 跳跃攻击、 [凌跃一击]技能的攻击力。\n
    决斗场中， 增益/减益技能、 被动技能的技能攻击力增加效果对[基础精通]无影响。
    """
    name = "基础精通"
    learnLv = 1
    masterLv = 190
    maxLv = 200
    position = 1
    rangeLv = 1
    uuid = "5a56514f35cf0270ae8d6c65f8fefd78"
    icon = "$common/$uuid"
    hasVP = False
    hasUP = False

    # 基本攻击力变化率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 前冲攻击力变化率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 跳跃攻击力变化率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [{"type":"*skillRation","data":[i-100 if i>0 else 0 for i in data0],"skills":["华丽回收"]}]

# 肃静！
# archer/chimera/e2cfb515fe293cf121a649fcc4bab84b
# b9cb48777665de22c006fabaf9a560b3/e2cfb515fe293cf121a649fcc4bab84b
class Skill4(PassiveSkill):
    """
    奇美拉似乎被他人的说教影响了， 其技能和部分台词将变得更加乖巧。
    """
    name = "肃静！"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 5
    rangeLv = 2
    uuid = "e2cfb515fe293cf121a649fcc4bab84b"
    hasVP = False
    hasUP = False


# 回收利用
# archer/chimera/7e60ce8aaca12593f889e8551fd1b03a
# b9cb48777665de22c006fabaf9a560b3/7e60ce8aaca12593f889e8551fd1b03a
class Skill5(PassiveSkill):
    """
    由于频繁的研究和实验， 奇美拉经常面临资金困境， 因此选择使用可回收的暗器。\n
    可以装备嵌合弓， 并在后跳时进行基本攻击。\n
    施放各系列技能后， 会留下可“回收利用”武器。 装备嵌合弓回收武器后， 将减少该系列技能的剩余冷却时间。 冷却时间减少比率按照各技能冷却时间的比率减少， 每个技能最多可使用1次减少冷却时间功能。\n
    学习后， 在可回收范围内， 最近的“回收利用”武器处会显示提醒回收的特效。\n
    每种类型的“回收利用”武器在地图上最多存在6个， 超出数量时， 最早出现的“回收利用”武器将消失。
    """
    name = "回收利用"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 1
    rangeLv = 2
    uuid = "7e60ce8aaca12593f889e8551fd1b03a"
    hasVP = False
    hasUP = False

    # 回收武器后， 技能剩余冷却时间减少率 : {value0}%
    # 国服改成了15%，原CD基础*50%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x: [62.5 if i >0 else i for i in x])

    associate = [ {"type":"*cdRatio","data":data0,"skills":['投掷匕首', '首足连击', '空翻刃袭', '利剑四重奏', '土星环', '环形毒液', '狂锯旋斧', '刺猬困境', '王冠粉碎者', '巨镰斯诺克', '环阿拉德狂飙']}, ]


# 全力挥击
# archer/chimera/4655101518604f874721b3cc249aae10
# b9cb48777665de22c006fabaf9a560b3/4655101518604f874721b3cc249aae10
class Skill7(ActiveSkill):
    """
    用力挥舞弓， 击打周围的敌人， 并向前推出。\n
    转职为猎人时， 再次按技能键会立即发射一枚爆炸箭矢， 造成额外伤害。\n
    转职为缪斯或奇美拉时， 技能类型变为独立攻击力。
    """
    name = "全力挥击"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 7
    rangeLv = 2
    cd = 5
    mp = [28, 165]
    uuid = "4655101518604f874721b3cc249aae10"
    hasVP = False
    hasUP = False

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

# 投掷匕首
# archer/chimera/05a07505ea102d31540afdb1fbec491f
# b9cb48777665de22c006fabaf9a560b3/05a07505ea102d31540afdb1fbec491f
class Skill8(ActiveSkill):
    """
    [匕首系列]\n
    可以消灭试图逼近的小型敌人， 向前方投掷匕首， 攻击敌人。\n
    投掷后， 匕首会击中敌人身体或插入地面， 并可“回收利用”。
    """
    name = "投掷匕首"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 10 #5
    mp = [28, 165]
    uuid = "05a07505ea102d31540afdb1fbec491f"
    hasVP = False
    hasUP = False

    # 匕首投掷攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1

# 翻月翔击
# archer/chimera/c9664191611af31142e052dfaef84530
# b9cb48777665de22c006fabaf9a560b3/c9664191611af31142e052dfaef84530
class Skill9(ActiveSkill):
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
    position = 8
    rangeLv = 2
    cd = 5
    mp = [35, 206]
    uuid = "c9664191611af31142e052dfaef84530"
    hasVP = False
    hasUP = False

    # 踢击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

# 瞬影
# archer/chimera/e11831002360a0d4e08c53ff686eea67
# b9cb48777665de22c006fabaf9a560b3/e11831002360a0d4e08c53ff686eea67
class Skill12(ActiveSkill):
    """
    持剑向前突进并斩击前方敌人， 以突破敌群或占据有利的战斗位置。 若附近有“回收利用”的武器， 将移动至其位置进行攻击。\n
    施放技能后， 在突进及首次斩击前再次按下技能键， 可发动追加斩击， 并移动至最近的可“回收利用”武器处。\n
    可通过[回收利用]的技能特效预测到达位置， 第一次触发时为蓝色回收特效， 第二次为红色回收特效。 可预测各自的移动目标。\n
    学习[败果之慧]技能后， 施放技能时会处于无敌状态。
    """
    name = "瞬影"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cd = 4
    mp = [23, 138]
    uuid = "e11831002360a0d4e08c53ff686eea67"
    hasVP = False
    hasUP = False

    # 持剑突进时斩击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 追加斩击攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # [范围信息]
    # 斩击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 可回收武器的搜索范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 首足连击
# archer/chimera/3f4ddb4df24a9f78c7778568e80107dd
# b9cb48777665de22c006fabaf9a560b3/3f4ddb4df24a9f78c7778568e80107dd
class Skill13(ActiveSkill):
    """
    [斧头系列]\n
    向前方对角线方向投掷斧头以转移视线， 随后瞄准敌人足部方向， 再次向地面投掷斧头。\n
    第二次投掷的斧头将用力砸向地面， 并可“回收利用”。
    """
    name = "首足连击"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 10
    mp = [45, 267]
    uuid = "3f4ddb4df24a9f78c7778568e80107dd"
    hasVP = False
    hasUP = True

    # 第一个斧头攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 第二个斧头攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

# 华丽回收
# archer/chimera/438e291ec31b6b831b0c8e33ff41f138
# b9cb48777665de22c006fabaf9a560b3/438e291ec31b6b831b0c8e33ff41f138
class Skill14(ActiveSkill):
    """
    利用奇美拉的遗物变形魔方来“回收利用”武器。 回收时可对周围的敌人造成伤害。\n
    攻击力会受[基础精通]的影响， 但无法获得[双重螺旋]技能的异常状态附加伤害效果。
    """
    name = "华丽回收"
    learnLv = 15
    masterLv = 1
    maxLv = 10
    position = 0
    rangeLv = 2
    uuid = "438e291ec31b6b831b0c8e33ff41f138"
    type = "passive"
    hasVP = False
    hasUP = False

    # 回收武器的攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 攻击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 双重螺旋
# archer/chimera/b224e3c19599a2496f7470936485e0ad
# b9cb48777665de22c006fabaf9a560b3/b224e3c19599a2496f7470936485e0ad
class Skill16(ActiveSkill):
    """
    使用奇美拉制作的特殊药品。 学习后， 将提升转职技能的攻击力。\n
    施放技能时， 赋予除普通攻击和[华丽回收]的回收攻击外， 其它所有攻击技能都将附加出血或中毒的异常状态伤害的效果。 该效果仅在装备嵌合弓时生效。\n
    再次施放技能， 可切换异常状态效果； 进入地下城时， 最后选择的异常状态效果将自动生效。
    """
    name = "双重螺旋"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 1
    rangeLv = 3
    cd = 3
    mp = [613, 820]
    uuid = "b224e3c19599a2496f7470936485e0ad"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 异常状态攻击力比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 异常状态持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [
        {"type":"*skillRation","data":data0},
        {"type":"*skillRation","data":data1,"exceptSkills":["华丽回收"]},
    ]

# 空翻刃袭
# archer/chimera/683ecd07d9b89dbe9afee8570a3a828d
# b9cb48777665de22c006fabaf9a560b3/683ecd07d9b89dbe9afee8570a3a828d
class Skill17(ActiveSkill):
    """
    [匕首系列]\n
    奇美拉后跃时， 向前方直线上逼近的敌人投掷多把匕首， 最多可命中3次。 若攻击范围达到特定数值， 将增加匕首投掷数量。\n
    最先投掷的匕首会击中敌人身体或插入地面， 并可“回收利用”。
    """
    name = "空翻刃袭"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 18 #9
    mp = [87, 516]
    uuid = "683ecd07d9b89dbe9afee8570a3a828d"
    hasVP = False
    hasUP = True

    # 匕首投掷攻击力 : {value0} X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 匕首投掷范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 喷毒
# archer/chimera/a988247dfc78c82e364af39ef66e84a0
# b9cb48777665de22c006fabaf9a560b3/a988247dfc78c82e364af39ef66e84a0
class Skill18(ActiveSkill):
    """
    举起嵌合弓进入防御姿态， 降低所受的伤害。 施放技能后短时间内， 若防御成功， 可格挡敌人的攻击， 免除自身所受伤害并进行反击。 反击成功后， 进入短暂无敌状态。
    """
    name = "喷毒"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 5
    rangeLv = 2
    cd = 12
    mp = [183, 1084]
    uuid = "a988247dfc78c82e364af39ef66e84a0"
    hasVP = False
    hasUP = True

    # 防御姿态伤害减少率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 反击攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 可反击时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 反击成功后无敌时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 唯物主义魔方
# archer/chimera/5f75a60c73b72ad60bd4321b96b16662
# b9cb48777665de22c006fabaf9a560b3/5f75a60c73b72ad60bd4321b96b16662
class Skill19(ActiveSkill): #不用
    """
    启动神秘的遗物——变形魔方， 解锁充满变数的战斗模式， 提升基本攻击力、 技能攻击力和物理暴击率。
    """
    name = "唯物主义魔方"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 0
    rangeLv = 3
    cd = 5
    mp = [728, 1713]
    uuid = "5f75a60c73b72ad60bd4321b96b16662"
    hasVP = False
    hasUP = False

    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 基本攻击力和技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 物理暴击率增加 :  {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 利剑四重奏
# archer/chimera/04c7b4361ca81f041e868169ff044252
# b9cb48777665de22c006fabaf9a560b3/04c7b4361ca81f041e868169ff044252
class Skill20(ActiveSkill):
    """
    [剑系列]\n
    与其它投掷攻击技能衔接时， 可以高效消灭敌人。 短暂滞空后射出利剑， 并额外克隆三柄， 一共发射四柄利剑。 其中克隆的利剑可将命中的敌人聚集于一处。\n
    最先射出的利剑会击中敌人身体或插入地面， 并可“回收利用”。
    """
    name = "利剑四重奏"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 15 #7.5
    mp = [64, 379]
    uuid = "04c7b4361ca81f041e868169ff044252"
    hasVP = False
    hasUP = True

    # 剑发射攻击力 : {value0} x {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0  = 4
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 遗物之力 · 克隆
# archer/chimera/67e7dd8996b5735e788c9420730c077d
# b9cb48777665de22c006fabaf9a560b3/67e7dd8996b5735e788c9420730c077d
class Skill21(PassiveSkill):
    """
    解锁神秘的遗物——变形魔方的“克隆”能力。 可提升技能攻击力， 且由于无需携带过多武器， 也将提升角色的速度。\n
    [外形和结构能轻松复刻， 但性能却没那么简单！ 得指定向量， 这可是非常繁琐的工作。 而且， 克隆品的维持时间非常短， 所以用于印钞是不现实的。]
    """
    name = "遗物之力 · 克隆"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 3
    uuid = "67e7dd8996b5735e788c9420730c077d"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率: {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击速度增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 移动速度增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)

    associate = [ {"type":"*skillRation","data":data0} ]

# 土星环
# archer/chimera/e862146efac2fce3de3a12f038f4116b
# b9cb48777665de22c006fabaf9a560b3/e862146efac2fce3de3a12f038f4116b
class Skill22(ActiveSkill):
    """
    [斧头系列]\n
    奇美拉落入敌阵中心后， 横扫周围敌人的技能。 投掷旋转的斧头， 斧头将围绕奇美拉转动， 斩击四周敌人。\n
    耗尽旋转次数的斧头， 会落在技能施放位置的前方， 并可“回收利用”。 若施放技能时按住向下方向键， 斧头会额外旋转半圈， 落在后方位置， 再“回收利用”。\n
    [学习败果之慧后]\n
    施放[瞬影]过程中， 可以预输入[土星环]技能。 预输入成功时， 可以配合[瞬影]技能的斩击动作施放[土星环]。
    """
    name = "土星环"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 30 #15
    mp = [175, 1036]
    uuid = "e862146efac2fce3de3a12f038f4116b"
    hasVP = False
    hasUP = True

    # 旋转斧头攻击力 : {value0} x {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 碎心连刺
# archer/chimera/5f11bba71728448bb64de0dba2b252cf
# b9cb48777665de22c006fabaf9a560b3/5f11bba71728448bb64de0dba2b252cf
class Skill23(ActiveSkill):
    """
    用剑对被控制的敌人发动致命一击。 持剑突进刺中敌人， 将其控制后再用匕首补刀， 并利用刺入的剑将敌人劈成两半， 造成高额伤害， 手段极为残忍。\n
    对于无法抓取的敌人， 踩住刺入的剑， 借助旋转力将其纵向劈开， 造成伤害， 同样相当残忍。
    """
    name = "碎心连刺"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 5
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [183, 1083]
    uuid = "5f11bba71728448bb64de0dba2b252cf"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps")

    # 剑刺击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 匕首刺击攻击力 : {value1} x {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 0
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 剑斩击攻击力 : {value3} x {value4}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 0
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 剑最后一击攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 0
    # [无法抓取的敌人]
    # 旋转剑攻击力 : {value6} x {value7}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 3
    data7 = get_data(f'{prefix}/{uuid}', 7)

    mode = ['不可抓取','可抓取']

    def setMode(self, mode):
        if mode == "不可抓取":
            self.hit0 = 1
            self.hit1 = 0
            self.hit3 = 0
            self.hit5 = 0
            self.hit6 = 3
        elif mode == "可抓取":
            self.hit0 = 1
            self.hit1 = 2
            self.hit3 = 3
            self.hit5 = 1
            self.hit6 = 0

    #点VP1两个形态都适用可抓取的伤害
    def vp_1(self):
        """
        [碎心连刺]\n
        无论敌人是否可抓取， 都用剑刺中后用斧头下劈， 使剑旋转进行攻击\n
        攻击力与对可抓取的敌人的攻击力相同
        """
        self.setMode("可抓取")
        ...

    def vp_2(self):
        """
        [碎心连刺]\n
        成功命中敌人时， 初始化[瞬影]技能的冷却时间\n
        [瞬影]技能攻击力 -26%
        """
        ...

    def effect(self, old, new):
        if self.vp == 2:
            self.associate = [{"data":[0]+[-26]*self.maxLv,"skills":["瞬影"]}]
        return super().effect(old, new)
# 环形毒液
# archer/chimera/854997c3bdfc3a2b498b4c4001f69e06
# b9cb48777665de22c006fabaf9a560b3/854997c3bdfc3a2b498b4c4001f69e06
class Skill24(ActiveSkill):
    """
    [匕首系列]\n
    向前跳跃， 借助离心力将涂有剧毒的匕首投掷到地面， 对聚集的敌人造成范围伤害。 然后通过跺脚， 使匕首上的毒液触发连锁反应， 引发爆炸造成伤害。 施放技能时， 可通过上下方向键在Y轴方向小幅调整位置。\n
    在施放技能位置稍前方所投掷的匕首可“回收利用”， 若匕首命中敌人， 将附着于其身上。
    """
    name = "环形毒液"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cube = 1
    cd = 30 #15
    mp = [121, 286]
    uuid = "854997c3bdfc3a2b498b4c4001f69e06"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps")

    # 匕首投掷攻击力 : {value0} x {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 5
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 毒液爆炸攻击力 : {value2} x {value3}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 5
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 爆炸攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [环形毒液]\n
        删除匕首投掷攻击力， 合算至爆炸攻击力\n
        投掷匕首后， 可通过再次按技能键引发爆炸\n
        追加操作等待时间 : 5秒\n
        爆炸范围 +20%
        """
        ...

    def vp_2(self):
        """
        [环形毒液]\n
        向前方投掷变形魔方\n
        变形魔方开启后， 以圆形范围自动投掷匕首\n
        变形魔方关闭时， 回收投掷的匕首并吸附周围的敌人\n
        匕首回收时， 发动匕首“回收利用”效果
        """
        ...

# 狂锯旋斧
# archer/chimera/61c8cb33dd20b4ff335e8deed70d3d9c
# b9cb48777665de22c006fabaf9a560b3/61c8cb33dd20b4ff335e8deed70d3d9c
class Skill25(ActiveSkill):
    """
    [斧头系列]\n
    用力投掷斧头， 以割裂坚硬的表皮， 并使其旋转着攻击敌人。 若命中敌人， 斧头会附着于其身上旋转， 随后掉落地面； 若未命中， 则在掉落的位置继续旋转。\n
    耗尽旋转次数的斧头会落在地面， 并可“回收利用”。
    """
    name = "狂锯旋斧"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 1
    cd = 40 #20
    mp = [283, 1672]
    uuid = "61c8cb33dd20b4ff335e8deed70d3d9c"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps")

    # 斧头第一击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 斧头旋转时攻击力 : {value1} x {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 15
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 斧头最后一击攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 斧头旋转时攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [狂锯旋斧]\n
        攻击力的20%变更为灼伤攻击力\n
        多段攻击间隔与施放时间 -50%\n
        将被命中的敌人吸附到斧头中心
        """
        ...

    def vp_2(self):
        """
        [狂锯旋斧]\n
        不再附着在敌人身上\n
        斧头第一击攻击和最后一击伤害合算至多段攻击伤害\n
        落在地面时， 挖出4种“回收利用”武器中的1种\n
        攻击范围 +30%
        """
        ...

# 刺猬困境
# archer/chimera/38c485cc41f46a7959ae4336325aa45c
# b9cb48777665de22c006fabaf9a560b3/38c485cc41f46a7959ae4336325aa45c
class Skill26(ActiveSkill):
    """
    [剑系列]\n
    该技能适用于对付擅长全方位防御的敌人。 在前方克隆并放置6柄利剑， 随后用嵌合弓发射手中的剑， 与克隆的利剑一同射向敌人。\n
    手中直接发射的剑命中敌人后， 可“回收利用”； 若未命中， 剑将插进地面。
    """
    name = "刺猬困境"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 2
    cd = 90 #45
    mp = [490, 2900]
    uuid = "38c485cc41f46a7959ae4336325aa45c"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps")

    # 克隆剑的攻击力 : {value0} x {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 6
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 手中剑的攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 爆炸攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [刺猬困境]\n
        攻击速度适用比率增加\n
        变更为长兵器系列技能\n
        攻击力的20%变更为感电攻击力\n
        聚集利剑时， 将敌人吸附到中心位置
        """
        ...

    def vp_2(self):
        """
        [刺猬困境]\n
        变更为普通系列技能\n
        冷却时间 -55%\n
        向前方跳跃并生成利剑后， 踩住生成的利剑移动到高处\n
        随后与生成的利剑一起下落， 进行最后一击\n
        下落攻击力与发射体攻击力相同\n
        技能过程中进入无敌状态
        """
        ...

# 遗物之力 · 巨大化
# archer/chimera/7a3fc9d473e8ffe21dd900ddf228a437
# b9cb48777665de22c006fabaf9a560b3/7a3fc9d473e8ffe21dd900ddf228a437
class Skill27(PassiveSkill):
    """
    解锁神秘的遗物——变形魔方的“巨大化”能力。 可提升技能攻击力， 且由于防具变得更厚， 也将提升物理防御力。\n
    [巨大化效果可以增加质量和密度， 真厉害！ 但遗憾的是， 结构复杂的生物没办法享受这个能力。]
    """
    name = "遗物之力 · 巨大化"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    uuid = "7a3fc9d473e8ffe21dd900ddf228a437"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理防御力增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [ {"type":"*skillRation","data":data0} ]

# 重力加速度
# archer/chimera/94c450d6214cafdc673f763badceeaf1
# b9cb48777665de22c006fabaf9a560b3/94c450d6214cafdc673f763badceeaf1
class Skill28(ActiveSkill):
    """
    将斧头投掷向墙壁， 借助反作用力飞向高空， 随后将斧头巨大化， 使其砸向地面， 粉碎敌人的头颅。
    """
    name = "重力加速度"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [1423, 6389]
    uuid = "94c450d6214cafdc673f763badceeaf1"
    hasVP = False
    hasUP = False

    # 斧头砸落攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1

# 废物清理
# archer/chimera/a99040fc36c75e998aa3ed012b7759c5
# b9cb48777665de22c006fabaf9a560b3/a99040fc36c75e998aa3ed012b7759c5
class Skill29(ActiveSkill):
    """
    清除附近敌人的群体攻击技能。 施放技能时消耗填充数量， 用斧头强力捶击地面， 对周围敌人造成伤害， 并强制“回收利用”武器。\n
    此时回收的武器不会触发“华丽回收”效果。\n
    按住前方向键并施放技能， 角色会先向前移动， 再用斧头进行捶击。\n
    施放技能后， 每隔一定时间填充施放次数。
    """
    name = "废物清理"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 1
    cd = 16 / 2 #这个20是堆栈两层，每层10韩服的，国服是16，每层8
    mp = [234, 1052]
    uuid = "a99040fc36c75e998aa3ed012b7759c5"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps")

    # 斧头冲击波攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [废物清理]层数 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 攻击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 武器回收范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    #VP2点了后堆栈层数-1，伤害翻倍，冷却也算是翻倍，就是把2堆栈合成1次伤害，CD就是原来2堆栈的CD
    def vp_1(self):
        """
        [废物清理]\n
        武器回收范围 +70%\n
        攻击范围 +25%
        """
        ...

    def vp_2(self):
        """
        [废物清理]\n
        填充次数 -1\n
        攻击力 +100%\n
        通过[废物清理]回收武器时， 发动[华丽回收]。
        """
        self.cd = 16
        self.skillRation *= 2
        ...

# 王冠粉碎者
# archer/chimera/b39ccc3dadab9d94569430e39cdf7d60
# b9cb48777665de22c006fabaf9a560b3/b39ccc3dadab9d94569430e39cdf7d60
class Skill30(ActiveSkill):
    """
    [剑系列]\n
    该技能适用于对付处于防御姿态和反应迅速的敌人。 克隆多柄利剑并使其短暂悬空， 然后用斧头向上击打， 使空中的剑高速坠落， 攻击敌人并造成伤害。 最后巨剑会直插地面， 造成高额伤害。\n
    可在最后坠落的剑所在位置进行“回收利用”。
    """
    name = "王冠粉碎者"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 3
    cd = 80 #40
    mp = [214, 959]
    uuid = "b39ccc3dadab9d94569430e39cdf7d60"
    hasVP = True
    hasUP = True
    vps = [{'name': '躁动之心', 'desc': '追踪<br/>施放时间减少'}, {'name': '旋斧狂欢', 'desc': '变更为斧头系列技能'}] # noqa: E501

    # 剑的坠落攻击力 : {value0} x 4
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    # 最后一剑的坠落攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1

    def vp_1(self):
        """
        [王冠粉碎者]\n
        攻击速度适用比率增加\n
        追踪周围800px内的敌人后落下武器
        """
        ...

    def vp_2(self):
        """
        [王冠粉碎者]\n
        变更为斧头系列技能\n
        变更为单次攻击\n
        攻击范围 +50%\n
        同时生成可“回收利用”的剑和斧头
        """
        ...

# 遗物奥义 · 变形
# archer/chimera/696721534394b40e78ac96e880f19e5a
# b9cb48777665de22c006fabaf9a560b3/696721534394b40e78ac96e880f19e5a
class Skill31(PassiveSkill):
    """
    解锁神秘的遗物——变形魔方的“变形”能力。 凭借对万物真理的领悟 (至少奇美拉本人如此认为)， 能够看透敌人， 进而提升暴击率、 基本攻击力和转职技能攻击力。\n
    [虽然我也不清楚具体原理， 但只要是我能理解的结构， 通通都能变形， 甚至连成分都能改变！ 变形魔方为什么会有这种力量？ 简直太可怕了！]
    """
    name = "遗物奥义 · 变形"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    uuid = "696721534394b40e78ac96e880f19e5a"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理暴击率增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [ {"type":"*skillRation","data":data0} ]

# 巨镰斯诺克
# archer/chimera/0dbdeaf846356f8b9380f8fbb8e97377
# b9cb48777665de22c006fabaf9a560b3/0dbdeaf846356f8b9380f8fbb8e97377
class Skill32(ActiveSkill):
    """
    [长兵器系列]\n
    该技能适用于消灭地面上的野兽群。 向前方敌人射出长矛， 刺入敌人身体的长矛会克隆成3个， 随后变形为巨镰， 在命中的敌人周围进行乱舞攻击并造成伤害， 最终一齐向目标敌人发动最后一击。\n
    若长矛未命中敌人， 将插在地面并攻击周围敌人。\n
    命中敌人身体的长兵器， 可“回收利用”； 若未命中， 长兵器则会插在地面。
    """
    name = "巨镰斯诺克"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 1
    rangeLv = 2
    cube = 3
    cd = 80 #40
    mp = [989, 4441]
    uuid = "0dbdeaf846356f8b9380f8fbb8e97377"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps")

    # 第一击攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 乱舞多段攻击力 : {value1} x {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 15
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最后一击攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 乱舞攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [巨镰斯诺克]\n
        删除发射体\n
        发射体攻击力合算至最终攻击\n
        跳跃后脚下立刻生成可“回收利用”的长兵器\n
        变形的巨镰追踪施放者进行攻击
        """
        ...

    def vp_2(self):
        """
        [巨镰斯诺克]\n
        发射体未命中时， 不会发动技能\n
        发动该效果时， 冷却时间变更为5秒\n
        乱舞速度 +20%\n
        多段攻击间隔 -20%
        """
        ...

# 环阿拉德狂飙
# archer/chimera/56fca6cff74d828e92301a40cd2148b9
# b9cb48777665de22c006fabaf9a560b3/56fca6cff74d828e92301a40cd2148b9
class Skill33(ActiveSkill):
    """
    [长兵器系列]\n
    该技能适用于聚集大量敌人后进行群体攻击。 将长兵器堆叠后发射， 随后长兵器变形为巨型齿轮， 向前方射出并攻击敌人。 该齿轮绕行圆形的阿拉德星球一圈后， 将再次出现发动最后一击， 并引发最终爆炸， 造成高额伤害。\n
    最后一击时， 根据齿轮经过的路径 (概率决定)， 附加灼伤、 冰冻、 感电异常状态。
    """
    name = "环阿拉德狂飙"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 1
    rangeLv = 2
    cube = 5
    cd = 90
    mp = [1239, 5566]
    uuid = "56fca6cff74d828e92301a40cd2148b9"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps")

    # 第一个齿轮攻击力 : {value0} x {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 4
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 第二个齿轮攻击力 : {value2} x {value3}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 3
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 第三个齿轮攻击力 : {value4} x {value5}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # [灼伤最后一击]
    # 灼伤最终爆炸攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 1
    # 灼伤最后一击攻击力 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7)
    hit7 = 1
    power7 = 1/1.1 # BUG 10%是双重螺旋的异常倍率，这个灼伤在不点VP的时候，这部分无法收到这个加成，如果点VP1就能收到加成
    # 灼伤最后一击持续时间 : {value8}秒
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # [冰冻最后一击]
    # 冰冻最终爆炸攻击力 : {value9}
    data9 = get_data(f'{prefix}/{uuid}', 9)
    hit9 = 0
    # 冰冻最后一击持续时间 : {value10}秒
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # [感电最后一击]
    # 感电最终爆炸攻击力 : {value11}
    data11 = get_data(f'{prefix}/{uuid}', 11)
    hit11 = 0
    # 感电最后一击攻击力 : {value12}
    data12 = get_data(f'{prefix}/{uuid}', 12)
    hit12 = 0
    # 感电最后一击持续时间 : {value13}秒
    data13 = get_data(f'{prefix}/{uuid}', 13)
    # [范围信息]
    # 攻击范围比率 : {value14}%
    data14 = get_data(f'{prefix}/{uuid}', 14)

    mode = ['灼伤','冰冻','感电']

    def setMode(self, mode):
        if mode == "灼伤":
            self.hit0 = 4
            self.hit2 = 3
            self.hit4 = 1
            self.hit6 = 1
            self.hit7 = 1
            self.hit9 = self.hit11 = self.hit12 = 0
        elif mode == "冰冻":
            self.hit0 = 4
            self.hit2 = 3
            self.hit4 = 1
            self.hit9 = 1
            self.hit6 = self.hit7 = self.hit11 = self.hit12 = 0
        elif mode == "感电":
            self.hit0 = 4
            self.hit2 = 3
            self.hit4 = 1
            self.hit11 = 1
            self.hit12 = 1
            self.hit6 = self.hit7 = self.hit9 = 0

    def vp_1(self):
        """
        [环阿拉德狂飙]\n
        最后一击变更为一次性特殊爆炸\n
        特殊爆炸攻击力为原技能爆炸攻击力和灼伤伤害之和\n
        特殊爆炸攻击会一次性结算自身造成的中毒/灼伤/感电/出血异常状态伤害
        """
        self.setMode("灼伤")
        self.power7 *= 1.1

    def vp_2(self):
        """
        [环阿拉德狂飙]\n
        变更为普通系列技能\n
        冷却时间 -55%\n
        召唤无限制锯齿轮\n
        - 锯齿轮攻击力为总攻击力的20%\n
        - 锯齿轮出现的冷却时间为当前技能冷却时间的20%\n
        - 再次施放技能时， 不再召唤锯齿轮
        """
        #冷却和伤害变为原技能灼伤状态的20%

# 幻爆天使之翼
# archer/chimera/6166762c62f234c5f50c2d2ebc5e48d0
# b9cb48777665de22c006fabaf9a560b3/6166762c62f234c5f50c2d2ebc5e48d0
class Skill34(ActiveSkill):
    """
    利用变形魔方与所持有武器的力量， 施展终极技能。 靠近附近最强的敌人后， 暂时开启变形魔方， 将敌人吸入遗物内部， 随后将其中的无数武器与敌人一同释放， 造成致命伤害。\n
    若附近没有可追踪的目标， 则无法施放此技能。
    """
    name = "幻爆天使之翼"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2400, 10777]
    uuid = "6166762c62f234c5f50c2d2ebc5e48d0"
    hasVP = False
    hasUP = False

    # 武器总释放伤害 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 追踪范围 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 败果之慧
# archer/chimera/d59c9840f65381bde8487757f1753c71
# b9cb48777665de22c006fabaf9a560b3/d59c9840f65381bde8487757f1753c71
class Skill35(PassiveSkill):
    """
    聆风·奇美拉克服了对遗物的未知恐惧。 突破束缚后， 她凭着更加狂暴的战斗风格， 成为了战场的主宰。 可提升基本攻击力和转职技能攻击力， [瞬影]和[土星环]技能将获得附加效果。\n
    [瞬影] : 施放技能时处于无敌状态。\n
    [土星环] : 在施放[瞬影]过程中， 可预输入该技能指令。 预输入成功后， 发动[瞬影]的斩击动作， 可同时投掷旋转的斧头。
    """
    name = "败果之慧"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    uuid = "d59c9840f65381bde8487757f1753c71"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

    associate = [ {"type":"*skillRation","data":data0} ]

# 颠倒之浩劫
# archer/chimera/bbc15561bec24f9c1e79e23d715b1dd2
# b9cb48777665de22c006fabaf9a560b3/bbc15561bec24f9c1e79e23d715b1dd2
class Skill36(ActiveSkill):
    """
    该技能可占据战场制高点， 从空中袭击最强大的敌人。 角色倒悬于最高处， 选定好降落地点后， 通过攻击键和技能键， 用矛发动强袭。 随后对插在地面的矛进行“变形”和“巨大化”， 使武器穿透地面， 造成穿刺伤害。\n
    经常丢三落四的聆风·奇美拉在倒悬时， 会掉落自己的随身物品以及“回收利用”的匕首、 剑、 斧头、 长兵器各1个。
    """
    name = "颠倒之浩劫"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [1400, 6288]
    uuid = "bbc15561bec24f9c1e79e23d715b1dd2"
    hasVP = False
    hasUP = False

    # 长矛坠落攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 变形武器穿刺攻击力 : {value1} x {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 8
    data2 = get_data(f'{prefix}/{uuid}', 2)

# 熵变 : 非线性跳跃
# archer/chimera/de20372767d014d62dc7361ac686834e
# b9cb48777665de22c006fabaf9a560b3/de20372767d014d62dc7361ac686834e
class Skill37(ActiveSkill):
    """
    最致命的攻击， 便是出其不意的突袭。 聆风·奇美拉先用斧头使敌人眩晕 (控制)， 再用弓穿刺敌人身体。 随后踩住弓身， 借助弓的张力施展强力一击。 攻击后， 立即借助遗物——变形魔方的力量，发射巨大化的剑， 彻底消灭敌人。
    """
    name = "熵变 : 非线性跳跃"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [3944, 17712]
    uuid = "de20372767d014d62dc7361ac686834e"
    hasVP = False
    hasUP = False

    # 斧头攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 弓穿刺攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 超乎常理的强力一击攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 巨大化的剑最后一击攻击力 : {value3} x {value4}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 10
    data4 = get_data(f'{prefix}/{uuid}', 4)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'chimera'
        self.nameCN = '聆风·奇美拉'
        self.role = 'archer'
        self.角色 = '弓箭手'
        self.职业 = '奇美拉'
        self.jobId = 'b9cb48777665de22c006fabaf9a560b3'
        self.jobGrowId = '92da05ec93fb43406e193ffb9a2a629b'

        self.武器选项 = ['嵌合弓']
        self.输出类型选项 = ['物理固伤']
        self.输出类型 = '物理固伤'
        self.防具精通属性 = ['力量']
        self.防具类型 = '重甲'
        self.buff = 2.083

        super().__init__(equVersion, __name__)
