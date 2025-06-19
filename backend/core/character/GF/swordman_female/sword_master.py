#1645c45aabb008c98406b3a16447040d
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "swordman_female/sword_master/cn/skillDetail"


# 冥思
# swordman_female/sword_master/d89f26862e348a801b30bb9fd7125db5
# 1645c45aabb008c98406b3a16447040d/d89f26862e348a801b30bb9fd7125db5
class Skill0(PassiveSkill):
    """
    进行战斗期间， 将根据连击数按比例增加物理或魔法暴击率。\n
    增益效果可以重复触发， 但是有触发次数上限。 增益效果重复触发时， 更新现有增益效果的持续时间。
    """
    name = "冥思"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0
    rangeLv = 3
    uuid = "d89f26862e348a801b30bb9fd7125db5"
    hasVP = False
    hasUP = False

    # 触发增益效果所需连击数 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 暴击率增加上限 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 增益效果持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)


# 帝国剑术
# swordman_female/sword_master/b89c9ab317bc0a443f6497b7cca2f6a8
# 1645c45aabb008c98406b3a16447040d/b89c9ab317bc0a443f6497b7cca2f6a8
class Skill1(ActiveSkill):
    """
    只传授给帝国剑士的秘密剑术。 根据佩戴的武器不同基本攻击的招式会发生变化。\n
    可以结合基本攻击使用， 但施放最后一击后无法衔接基本攻击或[帝国剑术]。\n
    可使用[驭剑术]强制中断[帝国剑术]并施放转职技能。
    """
    name = "帝国剑术"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 4
    rangeLv = 1
    mp = [6, 6]
    uuid = "b89c9ab317bc0a443f6497b7cca2f6a8"
    hasVP = False
    hasUP = False

    # 巨剑 180.53+205.90+127.83
    data0 = [int(i) for i in [0, 514.25]]
    hit0 = 0
    # 太刀 122.81+170.41+195.72
    data1 = [int(i) for i in [0, 486.67]]
    hit1 = 0
    # 短剑 (69.16+74.22+80.97+86.03)*2
    data2 = [int(i) for i in [0, 310.37]]
    hit2 = 0
    # 钝器 102.14+153.95+179.12+76.98
    data3 = [int(i) for i in [0, 512.19]]
    hit3 = 0

    def setMode(self, mode):
        weapon = self.char.GetWeaponType()
        if weapon[0] == "巨剑":
            self.hit0 = 1
        if weapon[0] == "太刀":
            self.hit1 = 1
        if weapon[0] == "短剑":
            self.hit2 = 2
        if weapon[0] == "钝器":
            self.hit3 = 3


# 基础精通
# swordman_female/sword_master/5a56514f35cf0270ae8d6c65f8fefd78
# 1645c45aabb008c98406b3a16447040d/5a56514f35cf0270ae8d6c65f8fefd78
class Skill2(PassiveSkill):
    """
    增加基本攻击、 前冲攻击、 跳跃攻击、 [浮空击]的攻击力。\n
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

    data0 = data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)

    associate = [{"type":"*skillRation","data":[i-100 if i>0 else 0 for i in data0],"skills":["帝国剑术"]}]


# 招架反击
# swordman_female/sword_master/2f5d03c7848effbc0a23f4df45d9ca46
# 1645c45aabb008c98406b3a16447040d/2f5d03c7848effbc0a23f4df45d9ca46
class Skill3(ActiveSkill):
    """
    [招架]成功后可激活该技能； 使用后， 可以进行2次快速斩击。
    """
    name = "招架反击"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cdList = [0, 2, 2, 2, 2, 2, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.1, 2.2, 2.2, 2.2, 2.2, 2.2, 2.2, 2.2, 2.2, 2.3, 2.3, 2.3, 2.3, 2.3, 2.3, 2.3, 2.3, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2.4, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.6, 2.6, 2.6, 2.6, 2.6, 2.6, 2.6, 2.6, 2.7, 2.7, 2.7, 2.7, 2.7, 2.7, 2.7, 2.7, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.8, 2.9]
    uuid = "2f5d03c7848effbc0a23f4df45d9ca46"
    damage = False
    hasVP = False
    hasUP = True

    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [范围信息]
    # 反击范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)


    def getSkillCD(self,mode=None):
        self.cd = self.cdList[self.lv]
        return super().getSkillCD()


# 兵刃奥义
# swordman_female/sword_master/4224f9b0b8c7c903e9a1e0f9d9f6d04d
# 1645c45aabb008c98406b3a16447040d/4224f9b0b8c7c903e9a1e0f9d9f6d04d
class Skill4(PassiveSkill):
    """
    驭剑士精通各种武器， 能够极致地发挥每种武器的特性。\n
    学习后， 增加所有武器的精通等级。\n
    首次学习时， 可使所有武器精通各提升2级； 以后技能每提升1级时， 武器精通提升1级。\n
    可以使用驭剑士专属的基础攻击动作。
    """
    name = "兵刃奥义"
    learnLv = 15
    masterLv = 20
    maxLv = 30
    position = 0
    rangeLv = 3
    uuid = "4224f9b0b8c7c903e9a1e0f9d9f6d04d"
    hasVP = False
    hasUP = False

    associate = [{"type":"+lv","data":[i + 1 if i > 0 else i for i in range(0, maxLv + 2)],"ratio":1,"skills":["波动之钝器精通","血影之太刀精通","毁灭之巨剑精通","魔性之短剑精通"]}]

# 驭剑术 발검술
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/78bd107acd474518b606be1e4fd38239?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill5(PassiveSkill):
    name = "驭剑术"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 2
    uuid = "78bd107acd474518b606be1e4fd38239"
    hasVP = False
    hasUP = False

    damage = False


# 魔剑降临
# swordman_female/sword_master/ade01c1d6afc8a05055225045e89fe49
# 1645c45aabb008c98406b3a16447040d/ade01c1d6afc8a05055225045e89fe49
class Skill6(ActiveSkill):
    """
    汇聚魔力， 将佩戴的武器任意幻化成4把魔剑中的一把， 每把剑都有固定属性。\n
    魔剑包括 : 火焰之普朗兹(火)、 寒冰之凯拉丁(冰)、 闪电之斯灵格(光)、 冥炎之巴萨达(暗)\n
    施放技能后， 可以利用方向键选择所需的魔剑； 若按下空格键， 可以解除[魔剑降临]； 基本攻击或施放[浮空击]时， 有一定几率触发各自的属性效果。\n
    掌握[魔性之短剑精通]后， 可以再幻化一把不同属性的魔剑。
    """
    name = "魔剑降临"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 5
    mp = [94, 1029]
    uuid = "ade01c1d6afc8a05055225045e89fe49"
    hasVP = False
    hasUP = False
    # 火属性效果触发几率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 火属性攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 0
    # 冰属性效果触发几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 冰属性攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 0
    # 光属性效果触发几率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 光属性攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    hit5 = 1
    # 暗属性效果触发几率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # 暗属性攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    hit7 = 1
    # 暗属性效果持续时间 : {value8}秒
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)
    # 暗属性效果下， 怪物身上可附加的冥炎上限 : {value9}个
    data9 = get_data(f'{prefix}/{uuid}', 9, lambda x = None: x)

    mode = ["火", "冰", "光", "暗"]

    def setMode(self, mode):
        if mode == "火":
            self.hit1 = 1
        elif mode == "冰":
            self.hit3 = 1
        elif mode == "光":
            self.hit5 = 3
        elif mode == "暗":
            self.hit7 = 4

    def getSkillCD(self,mode=None):
        return 1.0

# 魔性之短剑精通
# swordman_female/sword_master/d2c6df5105577fb59fb92529a36165a0
# 1645c45aabb008c98406b3a16447040d/d2c6df5105577fb59fb92529a36165a0
class Skill8(PassiveSkill):
    """
    使用短剑系武器攻击敌人时， 增加物理攻击力， 且附加特殊攻击效果。\n
    [附加效果]\n
    可以重叠[魔剑降临]， 同时拥有2把魔剑效果， 且减少冷却时间。\n
    重叠[魔剑降临]时增加技能攻击力； 最后幻化的魔剑为主魔剑， 前一个为副魔剑； 副魔剑的攻击力为基础攻击力的一定百分比。\n
    增加[魔剑降临]的攻击力、 减少冷却时间； 增加[瞬影三绝斩]异常状态几率和攻击力。
    """
    name = "魔性之短剑精通"
    learnLv = 15
    masterLv = 1
    maxLv = 40
    position = 1
    rangeLv = 3
    uuid = "d2c6df5105577fb59fb92529a36165a0"

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [魔剑降临]冷却时间 : 2秒
    # 重叠[魔剑降临]时技能攻击力增加量 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 副魔剑属性攻击力比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [魔剑奥义]攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [魔剑奥义]冷却时间减少率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # [瞬影三绝斩]异常状态伤害增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # [瞬影三绝斩]异常状态几率增加 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

    associate = [
        {"type":"$*PAtkP","data":data0,"weapon":["短剑"]},
        {"type":"*skillRation","data":data1,"weapon":["短剑"]},
        {"type":"+power_sub","data":data2,"skills":["魔剑奥义"],"weapon":["短剑"]},
        {"type":"+power_sub","data":data2,"skills":["魔剑奥义"],"weapon":["短剑"]},
        {"type":"*skillRation","data":data3,"skills":["魔剑奥义"],"weapon":["短剑"]},
        {"type":"*cdReduce","data":data4,"skills":["魔剑奥义"],"weapon":["短剑"]},
        ]

# 血影之太刀精通 쾌속의 도 마스터리
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/de3fea2d65c597f4d55c70a02b97fc79?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill9(PassiveSkill):
    """
    使用太刀系武器攻击敌人时， 增加物理攻击力； 且施放[魔剑降临]和[帝国剑术]时， 附加特殊攻击效果。\n
    [附加效果]\n
    [帝国剑术]、 [魔剑降临] : 增加攻击力\n
    [驭剑术] : 增加强制中断次数， 减少恢复时间； 10连击达成时可以恢复1次[驭剑术]\n
    [驭剑术施放时]\n
    强制中断技能时， 可增加技能攻击力并减少相应技能的冷却时间。\n
    [恶即斩]、 [破军旋舞斩] : 可直接发动最高阶段蓄气效果\n
    [瞬影三绝斩] : 追加发射剑气
    """
    name = "血影之太刀精通"
    learnLv = 15
    masterLv = 1
    maxLv = 40
    position = 2
    rangeLv = 3
    uuid = "de3fea2d65c597f4d55c70a02b97fc79"
    hasVP = False
    hasUP = False

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [帝国剑术]攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [魔剑降临]攻击力增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [驭剑术]施放次数增加 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [驭剑术]恢复时间减少 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # [驭剑术]恢复所需连击次数 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # [使用驭剑术时]
    # 强制中断技能时， 技能攻击力增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # [驭剑术]强制中断技能时， 冷却时间减少率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    # [瞬影三绝斩]剑气追加次数 : 1次
    data8 = [0] + [1]*maxLv

    associate = [
        {"type":"$*PAtkP","data":data0,"weapon":["太刀"]},
        {"type":"*skillRation","data":data1,"skills":["帝国剑术"],"weapon":["太刀"]},
        {"type":"*skillRation","data":data2,"skills":["魔剑降临"],"weapon":["太刀"]},
        {"type":"*skillRation","data":data6,"weapon":["太刀"]},
        {"type":"*cdReduce","data":data7,"weapon":["太刀"]},
        {"type":"+hit0","data":data8,"skills":["瞬影三绝斩"],"weapon":["太刀"],"ratio":1},
        {"type":"+hit3","data":data8,"skills":["瞬影三绝斩"],"weapon":["太刀"],"ratio":1},
        ]


# 毁灭之巨剑精通
# swordman_female/sword_master/c61f5a010370101402b05b21916c2071
# 1645c45aabb008c98406b3a16447040d/c61f5a010370101402b05b21916c2071
class Skill10(PassiveSkill):
    """
    使用巨剑系武器攻击敌人时， 增加巨剑物理攻击力， 且附加特殊攻击效果。\n
    [附加效果]\n
    [连环斩]、 [瞬影三绝斩] : 施放时有霸体判定\n
    [破军旋舞斩] : 施放时有霸体判定； 多段攻击变更为一次攻击\n
    [破军旋舞斩]、 [恶即斩]、 [帝国剑术]巨剑蓄气时， 增加该技能攻击范围和所有技能的攻击力。\n
    [破军旋舞斩] : 巨剑蓄气时增加攻击力。\n
    [恶即斩] : 增加3阶段蓄气时间， 巨剑蓄气时增加最终一击攻击力， 并获得无敌状态。
    """
    name = "毁灭之巨剑精通"
    learnLv = 15
    masterLv = 1
    maxLv = 40
    position = 4
    rangeLv = 3
    uuid = "c61f5a010370101402b05b21916c2071"

    # 武器物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [帝国剑术]巨剑攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [瞬影三绝斩]霸体持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [破军旋舞斩]、 [恶即斩]、 [帝国剑术]巨剑蓄气时
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 技能攻击力增加的增益效果持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 技能攻击力增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # [破军旋舞斩]额外攻击力增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # [恶即斩]3阶段蓄气时攻击力增加率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    # [恶即斩]蓄气后最终一击攻击力增加率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)

    associate = [
        {"type":"$*PAtkP","data":data0,"weapon":["巨剑"]},
        {"type":"*skillRation","data":data1,"skills":["帝国剑术"],"weapon":["巨剑"]},
        {"type":"*skillRation","data":data5,"weapon":["巨剑"]},
        {"type":"*skillRation","data":data6,"skills":["破军旋舞斩"],"weapon":["巨剑"]},
        {"type":"*power1","data":data8,"skills":["恶即斩"],"weapon":["巨剑"]},
    ]

# 波动之钝器精通
# swordman_female/sword_master/202edb928046f4fa6dedf6337377efd5
# 1645c45aabb008c98406b3a16447040d/202edb928046f4fa6dedf6337377efd5
class Skill11(PassiveSkill):
    """
    使用钝器系武器攻击敌人时， 增加钝器的物理攻击力， 且部分技能附加特殊攻击效果。\n
    -  [附加效果]  -\n
    [跃空斩] : 无需在跳跃状态下施放\n
    [穿云破空剑] : 增加冲击波范围和攻击力\n
    [幻剑术] : 攻击时会产生冲击波\n
    [雷鸣千军破] : 只发动最后一击， 增加攻击力\n
    冲击波命中敌人时， 增加技能攻击力， 效果持续一定时间。
    """
    name = "波动之钝器精通"
    learnLv = 15
    masterLv = 1
    maxLv = 40
    position = 5
    rangeLv = 3
    uuid = "202edb928046f4fa6dedf6337377efd5"

    # 物理攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [跃空斩]冲击波攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [穿云破空剑]冲击波范围增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [穿云破空剑]冲击波攻击力增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [幻剑术]冲击波范围 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # [幻剑术]冲击波攻击力增加率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # [雷鸣千军破]冲击波范围增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # [雷鸣千军破]攻击力增加率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    # 技能攻击力增加率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)
    # 技能攻击力增加增益效果持续时间 : {value9}秒
    data9 = get_data(f'{prefix}/{uuid}', 9, lambda x = None: x)
    associate = [
        {"type":"$*PAtkP","data":data0,"weapon":["钝器"]},
        {"type":"*power3","data":data3,"skills":["穿云破空剑"],"weapon":["钝器"]},
        {"type":"*power2","data":data5,"skills":["幻剑术"],"weapon":["钝器"]},
        {"type":"*skillRation","data":data8,"weapon":["钝器"]},
        {"type":"*skillRation","data":data7,"skills":["雷鸣千军破"],"weapon":["钝器"]},
    ]

# 自动招架
# swordman_female/sword_master/45442bbbe33540b4deeec29437dae70c
# 1645c45aabb008c98406b3a16447040d/45442bbbe33540b4deeec29437dae70c
class Skill12(ActiveSkill):
    """
    有一定的几率以剑士的本能进行招架， 效果持续一定时间。
    """
    name = "自动招架"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 8
    rangeLv = 3
    cd = 30
    mp = [60, 420]
    uuid = "45442bbbe33540b4deeec29437dae70c"
    hasVP = False
    hasUP = False

    # 触发几率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 疾影斩
# swordman_female/sword_master/8f73f243041c2d27739fe7696f02bf9b
# 1645c45aabb008c98406b3a16447040d/8f73f243041c2d27739fe7696f02bf9b
class Skill13(ActiveSkill):
    """
    以闪电般的速度冲向敌人并进行斩击。\n
    被击中的目标将进入短暂的僵直状态， 然后倒地。\n
    冲刺过程中， 若再次按下技能键， 则会停止冲刺并原地施放斩击。
    """
    name = "疾影斩"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 1
    rangeLv = 2
    cd = 7
    mp = [20, 210]
    uuid = "8f73f243041c2d27739fe7696f02bf9b"
    hasVP = False
    hasUP = True

    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 冲刺距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [范围信息]
    # 斩击范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 升龙剑
# swordman_female/sword_master/eb71e1d82d92c7e1d40500a0dcd77aa6
# 1645c45aabb008c98406b3a16447040d/eb71e1d82d92c7e1d40500a0dcd77aa6
class Skill15(ActiveSkill):
    """
    向前突进将敌人撞退后， 再用强力上斩攻击， 使敌人浮空。
    """
    name = "升龙剑"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 8
    mp = [30, 350]
    uuid = "eb71e1d82d92c7e1d40500a0dcd77aa6"
    hasVP = False
    hasUP = True

    # 突进的多段攻击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 突进攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 4
    # 上斩攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)


# 幻剑术
# swordman_female/sword_master/01c3a2fb793d293a25ed8dc7a0d70c1a
# 1645c45aabb008c98406b3a16447040d/01c3a2fb793d293a25ed8dc7a0d70c1a
class Skill16(ActiveSkill):
    name = "幻剑术"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 8
    rangeLv = 2
    cd = 8
    mp = [30, 350]
    uuid = "01c3a2fb793d293a25ed8dc7a0d70c1a"
    hasVP = False
    hasUP = True

    # 幻影斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 6
    # 幻影攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 冲击波攻击力 : {value2}%
    # data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    data2 = [0, 424, 468, 510, 555, 599, 641, 684, 725, 771, 813, 856, 900, 941, 988, 1032, 1073, 1117, 1162, 1202, 1247, 1291, 1332, 1376, 1420, 1462, 1507, 1549, 1592, 1636, 1678, 1721, 1763, 1808, 1853, 1894, 1940, 1983, 2025, 2069, 2110, 2154, 2199, 2239, 2284, 2329, 2370, 2414, 2459, 2499, 2544, 2584, 2629, 2673, 2714, 2760, 2804, 2845, 2889, 2931, 2979, 3020, 3062, 3105, 3149, 3193, 3237, 3278, 3322, 3366, 3409]# noqa: E501
    # [范围信息]
    # 攻击范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def setMode(self, mode):
        weapon = self.char.GetWeaponType()
        if weapon[0] == "钝器":
            self.hit2 = 6


# 人剑合一
# swordman_female/sword_master/8c2379737c5acc935c1731f67f607655
# 1645c45aabb008c98406b3a16447040d/8c2379737c5acc935c1731f67f607655
class Skill17(ActiveSkill):
    """
    将武器与身心合一， 探知敌人的弱点， 进行致命的攻击。\n
    该效果持续时间内， 可提高自身暴击伤害、 暴击率和敌人僵直时间。
    """
    name = "人剑合一"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 6
    rangeLv = 4
    cd = 5
    mp = [333, 2978]
    uuid = "8c2379737c5acc935c1731f67f607655"

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 暴击伤害增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 暴击率增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 敌人僵直时间增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)


# 穿云破空剑
# swordman_female/sword_master/5dc7008b12a459325b548b0715c6b73c
# 1645c45aabb008c98406b3a16447040d/5dc7008b12a459325b548b0715c6b73c
class Skill18(ActiveSkill):
    """
    使用强力的上斩击退敌人后， 对其进行多段斩击， 最后使用下砸并引发冲击波。\n
    对无法抓取的敌人不适用控制效果。
    """
    name = "穿云破空剑"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 3
    cd = 12
    mp = [60, 390]
    uuid = "5dc7008b12a459325b548b0715c6b73c"
    hasVP = False
    hasUP = True

    # 上斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 多段斩击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 多段斩击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 15
    # 冲击波攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # [学习剑心 : 魔剑唤醒后]
    # 魔剑攻击力: {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # [范围信息]
    # 斩击与冲击波范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)


# 魔剑奥义
# swordman_female/sword_master/bb34e8854a93fd250347a1c64119f7ab
# 1645c45aabb008c98406b3a16447040d/bb34e8854a93fd250347a1c64119f7ab
class Skill19(ActiveSkill):
    """
    除基本攻击、 [浮空击]以及增益/减益类技能之外， 使用其它技能攻击敌人时， 有一定几率触发魔剑的属性效果。\n
    使用暗属性的[冥炎之巴萨达]时， 可以召唤冥炎进行范围攻击； 使用冰属性的[寒冰之凯拉丁]时， 可以施放寒冰之枪进行攻击， 并有一定几率使敌人进入冰冻状态； 使用火属性的[火焰之普朗兹]时， 可以施放燃烧之眼进行攻击， 并有一定几率使敌人进入灼伤状态； 使用光属性的[闪电之斯灵格]时， 可以召唤落雷进行攻击， 并有一定几率使敌人进入失明状态。\n
    在[攻击类型转换]技能目录中， 可以on/off转换属性的魔法剑的外形。 外形off时， 魔剑的力量隐藏于剑中， 恢复原本的武器攻击范围。
    """
    name = "魔剑奥义"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    uuid = "bb34e8854a93fd250347a1c64119f7ab"
    hasVP = False
    hasUP = False
    type = "passive"

    # 触发几率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 触发间隔时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 冥炎攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 0
    # 寒冰之枪攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 0
    # 寒冰之枪飞行距离 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 冰冻持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 冰冻几率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # 燃烧之眼攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    hit7 = 0
    # 灼伤几率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)
    # 灼伤攻击力 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9, lambda x = None: x)
    # 灼伤持续时间 : {value10}秒
    data10 = get_data(f'{prefix}/{uuid}', 10, lambda x = None: x)
    # 落雷攻击力 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11, lambda x = None: x)
    hit11 = 0
    # 失明几率 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12, lambda x = None: x)
    # 失明持续时间 : {value13}秒
    data13 = get_data(f'{prefix}/{uuid}', 13, lambda x = None: x)

    power_sub = 0

    mode = ["火/暗", "暗火", "冰/光", "冰光", "冰火", "暗冰"]

    associate = [
        {"type":"+dataplus0","data":data7,"skills":["飓风魔剑"],"ratio":1},
    ]

    def setMode(self, mode):
        weapon = self.char.GetWeaponType()
        if weapon[0] == '短剑' and len(mode) == 3:
            self.skillRation *= 0
        if weapon[0] != '短剑' and len(mode) == 2:
            self.skillRation *= 0
        if len(mode) == 3:
            mode = mode[:1]
        for element, hit_attr, power_attr in [("火", "hit2", "power2"), ("冰", "hit3", "power3"), ("暗", "hit7", "power7"), ("光", "hit11", "power11")]:
            if element in mode:
                index = mode.index(element)
                setattr(self, hit_attr, 1)
                if mode.index(element) == 1:
                    setattr(self, power_attr, getattr(self, power_attr) * (self.power_sub if index > 0 else 1.0))

# 魔剑觉醒
# swordman_female/sword_master/1ff42548e611b94781a1ae8f063dd679
# 1645c45aabb008c98406b3a16447040d/1ff42548e611b94781a1ae8f063dd679
class Skill20(PassiveSkill):
    """
    魔剑开始觉醒自我意识， 对敌人发动致命攻击。 增加基本攻击力和转职技能的攻击力。
    """
    name = "魔剑觉醒"
    learnLv = 30
    masterLv = 5
    maxLv = 15
    position = 6
    rangeLv = 3
    uuid = "1ff42548e611b94781a1ae8f063dd679"

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)

    associate = [
        {"type":"*skillRation","data":data0},
    ]


# 瞬影三绝斩
# swordman_female/sword_master/cfacda0647b9a0f595df2c2aad30c18d
# 1645c45aabb008c98406b3a16447040d/cfacda0647b9a0f595df2c2aad30c18d
class Skill21(ActiveSkill):
    """
    聚集力量， 向前方连续斩出3道巨大的剑气。\n
    根据当前[魔剑降临]的状态， 触发对应的属性效果。\n
    在决斗场中， 武器的攻击属性不影响技能的攻击属性。
    """
    name = "瞬影三绝斩"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [110, 924]
    uuid = "cfacda0647b9a0f595df2c2aad30c18d"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 剑气攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 3
    # 剑气发射次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 剑气攻击射程 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [火属性魔剑附加效果]
    # 灼伤几率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 灼伤攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1
    # 灼伤持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # [冰属性魔剑附加效果]
    # 冰冻几率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # 剑气攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    hit7 = 0
    # 冰冻持续时间 : {value8}秒
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)
    # [光属性魔剑附加效果]
    # 感电几率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9, lambda x = None: x)
    # 感电攻击力 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10, lambda x = None: x)
    # 感电持续时间 : {value11}秒
    data11 = get_data(f'{prefix}/{uuid}', 11, lambda x = None: x)
    # [暗属性魔剑附加效果]
    # 失明几率 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12, lambda x = None: x)
    # 失明持续时间 : {value13}秒
    data13 = get_data(f'{prefix}/{uuid}', 13, lambda x = None: x)
    # 剑气攻击力 : {value14}% x 3
    data14 = get_data(f'{prefix}/{uuid}', 14, lambda x = None: x)
    # [范围信息]
    # 剑气范围比率 : {value15}%
    data15 = get_data(f'{prefix}/{uuid}', 15, lambda x = None: x)

    mode = ["火/光", "冰/暗"]

    def setMode(self, mode):
        if mode == "冰/暗":
            self.hit0 = self.hit4 = 0
            self.hit7 = 3

    def vp_1(self):
        """
        [瞬影三绝斩]\n
        更加迅速地攻击敌人\n
         - 蓄力时间减少\n
         - 单次动作瞬间释放所有剑气\n
        剑气命中敌人时， 恢复[驭剑术]使用次数\n
         - 每道剑气最多可恢复1次
        """
        ...

    def vp_2(self):
        """
        [瞬影三绝斩]\n
        不再发射剑气， 集中精神后， 斩击所有被赋予魂标志的敌人\n
         - 强化对敌人的感知能力\n
        斩击敌人后， 增加所有速度， 效果持续一定时间\n
         - 30秒内所有速度 +10%\n
        [斩魂术]\n
         - 寻敌范围 +10%
        """
        ...



# 破军旋舞斩
# swordman_female/sword_master/9cb6f9ed646fa87f9b7680a42ce83d1a
# 1645c45aabb008c98406b3a16447040d/9cb6f9ed646fa87f9b7680a42ce83d1a
class Skill22(ActiveSkill):
    """
    身体旋转一周的同时， 对敌人进行拔刀斩击。\n
    蓄气后施放可以增加前冲距离。\n
    使用方向键可以控制前冲方向(原地、 前方、 对角线)。 若不指定方向， 则默认向前移动。\n
    若已掌握[血影之太刀精通]， 使用[驭剑术]施放该技能时， 则直接施放已蓄满状态的[破军旋舞斩]。
    """
    name = "破军旋舞斩"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 1
    rangeLv = 3
    cube = 1
    cd = 15
    mp = [110, 924]
    uuid = "9cb6f9ed646fa87f9b7680a42ce83d1a"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 3
    # 多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 蓄气时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 蓄气时间(最短) : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 蓄气时攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # [范围信息]
    # 拔刀范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)

    mode = ["蓄力","普通"]

    def setMode(self, mode):
        if mode == "蓄力":
            self.skillRation *= 1.2


    def vp_1(self):
        """
        [破军旋舞斩]\n
        在原地凭空快速斩击\n
         - 删除移动功能\n
         - 删除斩击直接攻击\n
        沿挥剑的轨迹生成残影\n
         - 变更为单次攻击 \n
         - 总攻击力相同\n
        生成轨迹过程中施放[驭剑术]时， 立即生成残影攻击敌人
        """
        ...

    def vp_2(self):
        """
        [破军旋舞斩]\n
        凭借磅礴的意志发动进化后的[破军旋舞斩]\n
        始终以最大蓄气发动\n
         - 攻击范围 +35%\n
         - 移动距离额外增加\n
        承受突进中的伤害\n
         - 技能施放过程中进入霸体状态\n
         - 使用巨剑施放时， 蓄气和突进过程中所受伤害 -40%
        """
        ...

# 雷鸣千军破
# swordman_female/sword_master/d085127b0edd719782bd618d5688f4a1
# 1645c45aabb008c98406b3a16447040d/d085127b0edd719782bd618d5688f4a1
class Skill23(ActiveSkill):
    """
    聚集手上的魔力， 召唤出远古巨剑攻击敌人。\n
    斩击敌人2次后， 施放引发爆炸的强力最后一击。 按技能键填充时， 可以快速恢复[驭剑术]使用次数。\n
    掌握[波动之钝器精通]后， 攻击时， 只发动最后一击。
    """
    name = "雷鸣千军破"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [50, 840]
    uuid = "d085127b0edd719782bd618d5688f4a1"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 2
    # 斩击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 最后一击爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 爆炸攻击范围比率 : {value3}%

    def setMode(self, mode):
        weapon = self.char.GetWeaponType()
        if weapon[0] == "钝器":
            self.hit0 = 0

    def vp_1(self):
        """
        [雷鸣千军破]\n
        通过强烈的意志力集中精神， 减少集中精神时的所受伤害\n
         - 所受伤害 -70%\n
         - 集中精神持续时间 : 最长3秒\n
        集中精神过程中， 强化[驭剑术]强制中断次数恢复功能\n
         - 恢复速度增加\n
         - 施放时， 立即开始恢复[驭剑术]强制中断次数\n
        [驭剑术]\n
        通过[驭剑术]施放该技能时， 不消耗[驭剑术]强制中断次数
        """
        ...

    def vp_2(self):
        """
        [雷鸣千军破]\n
        变更为可填充2次的技能\n
         - 每次填充冷却时间 : 10秒\n
         - 单次攻击力 -50%\n
        施放速度和范围增加\n
         - 施放速度 +50%\n
         - 攻击范围 +20%
        """
        self.cd = 10
        self.skillRation *= 0.5

# 恶即斩
# swordman_female/sword_master/8ee0099656df08a0b39225f8a21d514b
# 1645c45aabb008c98406b3a16447040d/8ee0099656df08a0b39225f8a21d514b
class Skill24(ActiveSkill):
    """
    向前冲刺一段距离后， 对敌人进行快速的连续斩击。\n
    根据蓄气时间的不同， 斩击次数和冲刺距离会有所变化。\n
    蓄气到第1~2阶段时， 会发动快速的终结技； 蓄气到第3阶段时， 则会发动强威力的终结技。\n
    按向后方向键， 则在原地直接施放。\n
    掌握[血影之太刀精通]后， 利用[驭剑术]的效果发动技能时， 直接发动最大蓄气效果。
    """
    name = "恶即斩"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [120, 2024]
    uuid = "8ee0099656df08a0b39225f8a21d514b"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 第1阶段所需蓄气时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 第1阶段斩击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 第2阶段所需蓄气时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 第2阶段斩击次数 : {value3}次
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 第3阶段所需蓄气时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 第3阶段斩击次数 : {value5}次
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 第1阶段连续斩击攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # 第2阶段连续斩击攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    # 第3阶段连续斩击攻击力 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)
    hit8 = 15 # 不连按为13
    # 第1阶段终结攻击力 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9, lambda x = None: x)
    # 第2阶段终结攻击力 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10, lambda x = None: x)
    # 第3阶段终结攻击力 : {value11}%
    data11 = get_data(f'{prefix}/{uuid}', 11, lambda x = None: x)
    hit11 = 1
    # 蓄气时间(最短) : {value12}秒
    data12 = get_data(f'{prefix}/{uuid}', 12, lambda x = None: x)
    # [范围信息]
    # 斩击范围比率 : {value13}%
    data13 = get_data(f'{prefix}/{uuid}', 13, lambda x = None: x)

    def vp_1(self):
        """
        [恶即斩]\n
        以强韧的意志缩短时间进行攻击\n
         - 始终以最大蓄气发动\n
        连续斩击过程中使用[驭剑术]强制中断时\n
         - 留下残影继续攻击
        """
        ...

    def vp_2(self):
        """
        [恶即斩]\n
        删除蓄气、 前冲、 连续攻击\n
        挥动究极魔剑雷沃汀， 对前方大范围发动一次斩击\n
         - 变更为单次攻击\n
         - 总攻击力相同\n
         - 固定以最大蓄气发动
        """
        ...


# 斩魂术
# swordman_female/sword_master/d0cdaca82892e54097f22a1f60817048
# 1645c45aabb008c98406b3a16447040d/d0cdaca82892e54097f22a1f60817048
class Skill25(PassiveSkill):
    """
    利用暴击命中带有‘魂’标志的敌人时， 可以获得增加基本攻击和技能伤害的效果。\n
    增益效果持续时间内， 再次利用暴击命中时将会刷新效果时间。
    """
    name = "斩魂术"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 3
    uuid = "d0cdaca82892e54097f22a1f60817048"

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 效果叠加次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 增益效果持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 魂标志持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 魂标志生成的时间间隔 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # [范围信息]
    # 寻敌范围 : {value5}px
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)

    # 国服特色被动+3%
    associate = [
        {"type":"*skillRation","data":[i + 3 if i> 0 else 0 for i in data0]},
    ]

# 极 · 驭剑术 (时空斩)
# swordman_female/sword_master/0232c151ef3731c2dede51931a374723
# 1645c45aabb008c98406b3a16447040d/0232c151ef3731c2dede51931a374723
class Skill26(ActiveSkill):
    """
    将驭剑术修炼到极致后， 连时空都可以斩断。
    """
    name = "极 · 驭剑术 (时空斩)"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [980, 8232]
    uuid = "0232c151ef3731c2dede51931a374723"

    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 3
    # 斩击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 最后一击爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1


# 裂刃天冲
# swordman_female/sword_master/0fc47245af1f21c3e9217d03aa9fff0a
# 1645c45aabb008c98406b3a16447040d/0fc47245af1f21c3e9217d03aa9fff0a
class Skill27(ActiveSkill):
    """
    前冲攻击前方敌人， 召唤四种属性剑合并后引发爆炸。\n
    输入前进键可以向更远处前冲。\n
    剑宗召唤一柄魔法剑射向前方， 若击中敌人， 则会生成四种属性剑刺向目标， 最后融合四属性之力形成远古巨剑冲向敌人并抛向地面， 造成爆炸伤害。
    """
    name = "裂刃天冲"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [400, 1500]
    uuid = "0fc47245af1f21c3e9217d03aa9fff0a"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 刺击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 升空时多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 升空时多段攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 8
    # 爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # [范围信息]
    # 爆炸范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    def vp_1(self):
        """
        [裂刃天冲]\n
        与魔法剑一起前冲\n
         - 删除刺击和升空多段攻击\n
         - 前冲过程中接触敌人时停下\n
        与敌人接触或前冲结束时， 魔法剑会发动爆炸攻击\n
         - 将删除的攻击力合算至魔法剑爆炸攻击中 \n
         - 总攻击力相同\n
        前冲功能强化\n
         - 按向前方向键时增加前冲范围\n
         - 前冲过程中按上或下方向键， 可以进行Y轴移动
        """
        ...

    def vp_2(self):
        """
        [裂刃天冲]\n
        魔法剑会聚集周围的敌人， 并在聚集后立即引发爆炸\n
         - 删除升空多段攻击\n
        爆炸的同时产生魔力风暴， 持续攻击敌人\n
         - 将删除的攻击力合算至魔力风暴中\n
         - 总攻击力相同\n
         - 风暴持续时间 : 3秒
        """
        ...



# 极 · 驭剑术 (幻剑阵)
# swordman_female/sword_master/5197b141332a65a89d452adf227c2f30
# 1645c45aabb008c98406b3a16447040d/5197b141332a65a89d452adf227c2f30
class Skill28(ActiveSkill):
    """
    在前方召唤四种属性剑， 并生成幻剑阵压制敌人， 随后召唤远古巨剑给予敌人终极一击。\n
    生成幻剑阵时， 会使阵内敌人浮空并滞留， 同时剑宗会跃起对滞空的敌人进行连续攻击； 发动终极一击时， 则会将敌人轰落至地面， 同时引发强烈的爆炸。\n
    施放技能后， 若连续按下攻击键， 可以加快攻击速度。\n
    对无法抓取的敌人不适用控制效果。
    """
    name = "极 · 驭剑术 (幻剑阵)"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [800, 1680]
    uuid = "5197b141332a65a89d452adf227c2f30"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 空中斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 4
    # 移动次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [范围信息]
    # 最后一击爆炸范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    def vp_1(self):
        """
        [极 · 驭剑术 (幻剑阵)]\n
        展开魔法阵后， 不再进行移动攻击， 而是落下强化魔剑\n
         - 删除移动攻击和强控敌人效果\n
        强化魔剑与地面碰撞时爆炸， 攻击更大的范围\n
         - 将删除的攻击力合算在爆炸攻击力中 \n
         - 爆炸次数 : 4次\n
         - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [极 · 驭剑术 (幻剑阵)]\n
        展开魔法阵时， 立即用魔力保护自身\n
         - 施放时立即进入无敌状态\n
        最后一击会追踪敌人\n
         - 追踪魔法阵内最强敌人并落下
        """
        ...

# 飓风魔剑
# swordman_female/sword_master/e5c09f9132a48dc1d695968592cc5878
# 1645c45aabb008c98406b3a16447040d/e5c09f9132a48dc1d695968592cc5878
class Skill29(ActiveSkill):
    """
    在魔剑注入力量， 生成强力的魔力飓风， 然后射向前方进行多段攻击并引发爆炸。\n
    施放时， 可以蓄气控制出招时机。\n
    学习该技能后， 可将[魔剑奥义]的力量存储为魔剑堆， 根据[魔剑奥义]的冷却时间， 每隔一段时间可以存储一次魔剑堆。\n
    施放技能时， 可以利用存储的魔剑堆强化[飓风魔剑]的技能效果， 最终爆炸攻击力随[魔剑奥义]的攻击力增加而增加。\n
    魔力飓风的属性随[魔剑降临]幻化的武器类型变化， 命中敌人时可以引发异常状态， 异常状态等级与[魔剑奥义]的异常状态等级相同。\n
    只有在[魔剑降临]状态下才能施放该技能。
    """
    name = "飓风魔剑"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 3
    cd = 25
    mp = [580, 4500]
    uuid = "e5c09f9132a48dc1d695968592cc5878"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 魔力飓风多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 40
    # 蓄气时多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 发射后多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 爆炸攻击力 : {value3}% + [魔剑奥义]攻击力
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1
    # 每个魔剑堆伤害增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 魔剑堆最高存储次数 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 火属性效果 : 灼伤
    # 冰属性效果 : 冰冻
    # 光属性效果 : 感电
    # 暗属性效果 : 暗化
    # [范围信息]
    # 魔剑范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

    magicHit = 5
    magicPower = 0.03

    # 暗魔剑部分的特殊逻辑
    dataplus0 = 0
    hitplus0 = 10
    powerplus0 = 1


    def setMode(self, mode: str | None = None):
        # 魔剑层数对飓风魔剑的加成，但是不加成暗刀的额外部分伤害
        self.power0 *= 1 + self.magicHit * self.magicPower
        self.power3 *= 1 + self.magicHit * self.magicPower
        self.powerplus0 = (0.09 + self.lv / 100)

    def skillInfo(self, mode = None):
        return super().skillInfo(mode)
        # 暂不在此处计算魔剑奥义伤害，容易误解
        basic =  super().skillInfo(mode)
        # 魔剑奥义单独计算 不享受飓风魔剑特化部分
        weapon = self.char.GetWeaponType()
        if weapon[0] == '短剑':
            magic = self.char.GetSkillByName("魔剑奥义").skillInfo("暗火")
        else:
            magic = self.char.GetSkillByName("魔剑奥义").skillInfo("火/暗")
        return basic[0] + magic[0] * magic[1] * self.magicHit / basic[1],basic[1],basic[2]

    def vp_1(self):
        """
        [飓风魔剑]\n
        施放时立即向前发射魔剑\n
         - 删除技能键蓄力操作\n
        魔剑命中敌人时展开魔力风暴攻击敌人\n
         - 飓风多段攻击次数增加\n
         - 总攻击力相同\n
         - 魔力风暴会将敌人吸附到风暴中心\n
        [魔剑奥义]保存次数上限 -2次\n
         - 每1个魔剑层数额外增加2%的增加量
        """
        self.magicHit = 3
        self.magicPower = 0.05
        ...

    def vp_2(self):
        """
        [飓风魔剑]\n
        基本冷却时间变更为50秒\n
        总攻击力 +100%\n
        不再发射属性魔剑， 而是将魔力注入剑中挥动， 召唤究极魔剑雷沃汀\n
         - 删除多段攻击\n
         - 删除魔力风暴攻击\n
        撕裂空间后降落的雷沃汀会强制控制命中的敌人， 并在地面上生成裂缝\n
         - 强制控制时间 : 1秒\n
        随后裂缝会发生爆炸， 对裂缝上的所有敌人造成伤害\n
         - 将删除的攻击力合算在爆炸攻击中\n
         - 总攻击力相同\n
        增加魔剑层数强化效果\n
         - 每1个魔剑层数雷沃汀和裂缝大小 +7%
        """
        self.skillRation *= 2
        self.cd = 50
        ...

# 帝皇盟约
# swordman_female/sword_master/e0daa922b19cdc35de879e938361464e
# 1645c45aabb008c98406b3a16447040d/e0daa922b19cdc35de879e938361464e
class Skill30(PassiveSkill):
    """
    领悟到剑之奥义的剑皇， 更加熟练的使用武器。 依据不同的武器特性， 增加不同程度的物理攻击力。
    """
    name = "帝皇盟约"
    name = "帝皇盟约"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 3
    uuid = "e0daa922b19cdc35de879e938361464e"

    # 使用短剑时物理攻击力增加量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 使用太刀时物理攻击力增加量 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 使用钝器时物理攻击力增加量 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 使用巨剑时物理攻击力增加量 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

    associate = [
        {"type":"$*PAtkP","data":data0},
    ]

# 极 · 驭剑术 (破剑阵)
# swordman_female/sword_master/7f80b887a09e88e2c4728c898bd73654
# 1645c45aabb008c98406b3a16447040d/7f80b887a09e88e2c4728c898bd73654
class Skill31(ActiveSkill):
    """
    召唤出远古魔剑的墓地， 然后举起魔剑向敌人砍去。 除了手中的魔剑之外的其他魔剑将被引爆， 对敌人造成伤害。\n
    施放技能时， 若用[驭剑术]强制中断技能， 则所有魔剑同时爆炸。
    """
    name = "极 · 驭剑术 (破剑阵)"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "7f80b887a09e88e2c4728c898bd73654"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 2
    # 斩击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 8
    # 最终爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 0
    # 爆炸次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # [范围信息]
    # 攻击范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)

    mode = ["满","柔化"]

    def setMode(self, mode):
        if mode == '柔化':
            self.hit0 = self.hit2 = 0
            self.hit3 = 8

    def vp_1(self):
        """
        [极 · 驭剑术 (破剑阵)]\n
        引发强化爆炸\n
         - 魔剑爆炸次数减少\n
         - 总攻击力相同\n
        使用[驭剑术]强制中断并施放时， 效果变更\n
         - 不会中断正在施放的技能\n
         - 在前方落下强化魔剑， 立即引发强化爆炸
        """
        ...

    def vp_2(self):
        """
        [极 · 驭剑术 (破剑阵)]\n
        在更大范围内召唤魔剑\n
        快速移动到召唤魔剑范围内最强敌人的背后进行攻击\n
         - 斩击次数 -1次\n
        所有魔剑同时爆炸， 对范围内敌人造成伤害\n
         - 总攻击力相同
        """
        ...

# 誓约之剑 : 雷沃汀
# swordman_female/sword_master/7cf17936a039b418660424125dc968d7
# 1645c45aabb008c98406b3a16447040d/7cf17936a039b418660424125dc968d7
class Skill32(ActiveSkill):
    """
    凝缩魔剑的力量， 召唤出凝聚四大元素力量的誓约之剑， 斩破次元的界限。\n
    次元震动的期间， 敌人将进入长时间的僵直状态， 当次元破裂时受到巨大的伤害。
    """
    name = "誓约之剑 : 雷沃汀"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "7cf17936a039b418660424125dc968d7"
    hasVP = False
    hasUP = False

    # 次元斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1


# 极诣 · 驭剑术 : 聚魔剑
# swordman_female/sword_master/78be08a3f8c834d3b06fa20c6a08c5a5
# 1645c45aabb008c98406b3a16447040d/78be08a3f8c834d3b06fa20c6a08c5a5
class Skill33(ActiveSkill):
    """
    利用无限魔力的力量， 召唤更加强大的魔剑和雷沃汀冲向前方刺击敌人。 被强化版雷沃汀命中的敌人暂时进入僵直状态， 然后受到强化版魔剑的攻击。 当收起雷沃汀时， 无限的魔力瞬间爆炸。\n
    输入方向键时， 可增加前冲距离。
    """
    name = "极诣 · 驭剑术 : 聚魔剑"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [773, 6000]
    uuid = "78be08a3f8c834d3b06fa20c6a08c5a5"
    hasVP = False
    hasUP = False

    # 刺击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 强化版魔剑攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 4
    # 强化版魔剑多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 魔力爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 1

# 剑心 : 魔剑唤醒
# swordman_female/sword_master/1803b6a67047cafb9e289b4f33cc507b
# 1645c45aabb008c98406b3a16447040d/1803b6a67047cafb9e289b4f33cc507b
class Skill34(PassiveSkill):
    """
    利用强大的魔力唤醒魔剑和雷沃汀的真正面貌， 掌控新的力量。 学习后， 增加转职技能攻击力， 部分技能赋予额外效果。\n
    [升龙剑]\n
    上挑敌人后快速向地面下劈。\n
    [穿云破空剑]\n
    掉落[魔剑降临]选择的魔剑并造成爆炸攻击。\n
    [驭剑术]\n
    增加可以强制中断的次数。
    """
    name = "剑心 : 魔剑唤醒"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "1803b6a67047cafb9e289b4f33cc507b"

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [升龙剑]
    # 下劈攻击力 : 总攻击力的{value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [穿云破空剑]
    # 强化属性魔剑攻击力 : [穿云破空剑]冲击波攻击力的100%
    # [驭剑术]
    # 可以强制中断的次数增加 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    associate = [
        {"type":"*skillRation","data":data0},
    ]

# 誓约之引 : 万剑之巅
# swordman_female/sword_master/9f57da5cb3651d81ca7dc9f78be33d01
# 1645c45aabb008c98406b3a16447040d/9f57da5cb3651d81ca7dc9f78be33d01
class Skill35(ActiveSkill):
    """
    召唤隐藏在次元中的魔剑军团。 魔剑军团在誓约之剑 : 雷沃汀的指挥下， 向敌人斩击后腾空， 随后冲向地面歼灭敌人。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "誓约之引 : 万剑之巅"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "9f57da5cb3651d81ca7dc9f78be33d01"

    # 强化版魔剑攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 4
    # 强化版魔剑攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 下劈冲击波 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 爆炸伤害 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 15
    # 爆炸伤害多段攻击次数 : {value4}次
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'sword_master'
        self.nameCN = '极诣·驭剑士'
        self.role = 'swordman_female'

        self.武器选项 = ['巨剑', '钝器', '太刀', '短剑']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '轻甲'
        self.buff = 1.78

        self.角色 = '鬼剑士(女)'

        self.职业 = '驭剑士'

        super().__init__(equVersion, __name__)

    def AddSkillLv(self, min: int, max: int, lv: int, type=-1, exceptSkills:list[str]=[]) -> None:
        """
        增加技能等级
        type: -1 全部, 0 被动, 1 主动
        """
        for skill in self.skills:
            # 四个武器精通不享受技能范围等级加成
            if min <= skill.learnLv <= max and skill.name not in ["波动之钝器精通","血影之太刀精通","毁灭之巨剑精通","魔性之短剑精通"] + exceptSkills:
                skillType = "all" if type == -1 else ("active" if type == 1 else "passive")
                if (skillType == "all" or skill.type == skillType) and skill.lv > 0:
                    skill.lv += lv
