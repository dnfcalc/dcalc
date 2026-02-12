#1645c45aabb008c98406b3a16447040d
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
from core.basic.roleinfo import CharacterEquipInfo
from core.basic.formula import 武器强化计算, 增幅计算
prefix = "swordman_female/vegabond/cn/skillDetail"


# 光剑掌握
# swordman_female/vegabond/1812a1ece67bb37b6b44b54766450064
# 1645c45aabb008c98406b3a16447040d/1812a1ece67bb37b6b44b54766450064
class Skill2(PassiveSkill):
    """
        可以使用光剑系武器攻击敌人。\n
    可以减少觉醒技能之外所有技能的冷却时间。
    """
    name = "光剑掌握"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 7
    rangeLv = 1
    uuid = "1812a1ece67bb37b6b44b54766450064"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 技能冷却时间减少率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

    associate = [
        {"data":data0,"type":"*cdReduce", 'exceptSkills': ['花开寒影', '飞花逐月', '轻云出月风静夜']}
    ]

# 副武器可装备
# swordman_female/vegabond/f45301a5590cccefbe0becf2f8d029f5
# 1645c45aabb008c98406b3a16447040d/f45301a5590cccefbe0becf2f8d029f5
class Skill7(PassiveSkill):
    """
        可以在左手装备副武器。 副武器只能为光剑， 并且只有一部分属性生效。\n
    [生效属性]\n
    武器攻击力、 力量
    """
    name = "副武器可装备"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 0 #TODO
    rangeLv = 1
    uuid = "f45301a5590cccefbe0becf2f8d029f5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 武器攻击力生效比率 : 10%
    # 力量生效比率 : 10%


# 十字剑
# swordman_female/vegabond/1b1cfab062e0768bcc889e33e1f30dbf
# 1645c45aabb008c98406b3a16447040d/1b1cfab062e0768bcc889e33e1f30dbf
class Skill12(ActiveSkill):
    """
        以十字形交叉斩击后产生剑气。\n
        再次按技能键， 可连接下劈追加攻击。
    """
    name = "十字剑"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 3
    mp = [10, 170]
    uuid = "1b1cfab062e0768bcc889e33e1f30dbf"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 剑气攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 下劈攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 剑气距离比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)


# 两仪功
# swordman_female/vegabond/c77a417c43de80c4ce32c1ed405d174a
# 1645c45aabb008c98406b3a16447040d/c77a417c43de80c4ce32c1ed405d174a
class Skill19(ActiveSkill):
    """
        增加基本攻击的攻击力和命中率， 并利用内劲在一只手上形成念力武器， 将基本攻击变更为二刀流\n
        念力武器默认为光剑， 每当重新使用技能时， 按照光剑 - 刀 - 钝器 - 短剑 - 巨剑的顺序变化。\n
        基本攻击时， 根据装备中的念力武器种类， 适用附加效果。\n
        进入地下城时自动发动。
    """
    name = "两仪功"
    learnLv = 15
    masterLv = 1
    maxLv = 11
    position = 0 #TODO
    rangeLv = 1
    cd = 0.5
    mp = [10, 10]
    uuid = "c77a417c43de80c4ce32c1ed405d174a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 命中率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # - [光剑] -
    # 感电几率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 感电持续时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 感电攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # - [太刀] -
    # 出血几率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 出血持续时间 : {value6}秒
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 出血攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # - [钝器] -
    # 眩晕几率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8)
    # 眩晕持续时间 : {value9}秒
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # - [短剑] -
    # 束缚几率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)
    # 束缚持续时间 : {value11}秒
    data11 = get_data(f'{prefix}/{uuid}', 11)
    # - [巨剑] -
    # 基本攻击力增加率 : {value12}%
    data12 = get_data(f'{prefix}/{uuid}', 12)

# 三才剑
# swordman_female/vegabond/ecc23c980ea71450c0ad0c3fd232f329
# 1645c45aabb008c98406b3a16447040d/ecc23c980ea71450c0ad0c3fd232f329
class Skill20(ActiveSkill):
    """
        用剑挥出相连的三角形状的剑气攻击敌人， 命中的敌人会进入僵直状态。\n
        形成三角形剑气时， 再按一次技能键， 剑气可以向前发射一定距离， 并使命中的敌人倒地。\n
        [三才剑]的技能等级与[三才轮回剑]的技能等级同步提升。
    """
    name = "三才剑"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 5
    mp = [40, 330]
    uuid = "ecc23c980ea71450c0ad0c3fd232f329"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 剑气攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 3
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 附加效果剑气攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 轮回剑
# swordman_female/vegabond/852f8ad797db4dca1405cb3e77198401
# 1645c45aabb008c98406b3a16447040d/852f8ad797db4dca1405cb3e77198401
class Skill21(ActiveSkill):
    """
        将内劲施加在武器上， 使其快速旋转， 造成多段攻击伤害。\n
        旋转攻击中输入跳跃键时， 立即施放终结斩击。\n
        [轮回剑]的技能等级与[三才轮回剑]的技能等级同步提升。
    """
    name = "轮回剑"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    cd = 7
    mp = [20, 250]
    uuid = "852f8ad797db4dca1405cb3e77198401"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 多段攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 10
    # 多段攻击次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后一击物理攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 三才回轮剑
# swordman_female/vegabond/ab6fc3303df03b58911967dfca2b5d07
# 1645c45aabb008c98406b3a16447040d/ab6fc3303df03b58911967dfca2b5d07
class Skill22(PassiveSkill):
    """
        可以修炼基本剑术三才剑和轮回剑。\n
        学习后， 可以增加三才剑和轮回剑的技能等级。
    """
    name = "三才回轮剑"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 0 #TODO
    rangeLv = 2
    uuid = "ab6fc3303df03b58911967dfca2b5d07"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501

# 返本归元
# swordman_female/vegabond/e49e57b2e8fbeceb0a2c56a0c63fe6c5
# 1645c45aabb008c98406b3a16447040d/e49e57b2e8fbeceb0a2c56a0c63fe6c5
class Skill23(PassiveSkill):
    """
        流浪武士达到返本归元境界， 基本攻击、 剑术与掌法变得更强， 并增加物理暴击率。
    """
    name = "返本归元"
    learnLv = 20
    masterLv = 1
    maxLv = 11
    position = 2
    rangeLv = 2
    uuid = "e49e57b2e8fbeceb0a2c56a0c63fe6c5"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击、 剑术、 掌法技能攻击力增加量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 物理暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    associate = [
        {"data":data0,"type":"*skillDamage"}
    ]

# 四象引
# swordman_female/vegabond/0b8db1e10b3abbd24d38564e708675d5
# 1645c45aabb008c98406b3a16447040d/0b8db1e10b3abbd24d38564e708675d5
class Skill24(ActiveSkill):
    """
        利用内劲抓取前方的敌人， 并将其拉到角色面前。 被抓取的敌人受到倒地伤害， 未被抓的敌人受到周围冲击波伤害。\n
        对于无法抓取的敌人， 可使其进入短暂强制控制状态并受到伤害。
    """
    name = "四象引"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 0
    rangeLv = 2
    cd = 7
    mp = [20, 250]
    uuid = "0b8db1e10b3abbd24d38564e708675d5"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 倒地时攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 冲击波攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [范围信息]
    # 冲击波范围比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 可吸附的范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 五气朝元
# swordman_female/vegabond/dcb31a63ef58954f44ff2070c42a9a98
# 1645c45aabb008c98406b3a16447040d/dcb31a63ef58954f44ff2070c42a9a98
class Skill25(ActiveSkill):
    """
        通过蓄气激发自身的潜力， 增加暴击伤害、 攻击速度和移动速度， 效果持续一段时间。
    """
    name = "五气朝元"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    cd = 5
    uuid = "dcb31a63ef58954f44ff2070c42a9a98"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 增益效果持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 暴击伤害增加率 : {value1}% X 5
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击、 移动速度增加 : {value2}% X 5
    data2 = get_data(f'{prefix}/{uuid}', 2)


# 一花渡江
# swordman_female/vegabond/8572675ec6a1f50b6eff6a867376c2de
# 1645c45aabb008c98406b3a16447040d/8572675ec6a1f50b6eff6a867376c2de
class Skill27(ActiveSkill):
    """
        使用流浪武士领悟的轻功， 快速向前方移动。\n
        向前方移动时， 对周围发动爆炸攻击。
    """
    name = "一花渡江"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 6
    mp = [40, 300]
    uuid = "8572675ec6a1f50b6eff6a867376c2de"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 移动距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 爆炸攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 3
    # 多段攻击次数上限 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 樱落斩
# swordman_female/vegabond/4f2e001e9a19eb7bae50ad1840dfb329
# 1645c45aabb008c98406b3a16447040d/4f2e001e9a19eb7bae50ad1840dfb329
class Skill28(ActiveSkill):
    """
        抓取敌人使其浮空， 然后向上跃起在空中对敌人进行连续斩击， 并将敌人劈落地面
    """
    name = "樱落斩"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 7
    mp = [35, 350]
    uuid = "4f2e001e9a19eb7bae50ad1840dfb329"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 浮空攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 空中劈斩攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 连续斩击攻击力 : {value2}% X {value3}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 向下斩击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 1
    # [范围信息]
    # 范围比率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)

# 圆舞斩
# swordman_female/vegabond/b8f4966608e4ebb3cc80ba4eac3649bb
# 1645c45aabb008c98406b3a16447040d/b8f4966608e4ebb3cc80ba4eac3649bb
class Skill29(ActiveSkill):
    """
        刺中前方敌人， 将其向后抛出并造成伤害。\n
        可以同时抓取多名敌人， 刺中敌人后按向前方向键， 则不将敌人向后抛出， 而是用剑砸向前方， 对其造成伤害。\n
        对无法抓取的敌人施放时， 用巨大的剑砸向前方\n
        用巨大的剑砸向前方产生冲击波， 并对周围的敌人造成伤害。 
    """
    name = "圆舞斩"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 11
    mp = [70, 400]
    uuid = "b8f4966608e4ebb3cc80ba4eac3649bb"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 刺击物理攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2
    # 砸地物理攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 周围冲击波攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [范围信息]
    # 冲击波范围 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

# 碎岩裂地掌
# swordman_female/vegabond/d53301bb328baf12a3ae482cc6a565dd
# 1645c45aabb008c98406b3a16447040d/d53301bb328baf12a3ae482cc6a565dd
class Skill30(ActiveSkill):
    """
        利用内劲之力压缩空间减速敌人的移动， 然后以掌击地打倒敌人并引发巨大伤害。\n
        倒地的敌人暂时无法起身。
    """
    name = "碎岩裂地掌"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 1
    rangeLv = 2
    cd = 12
    mp = [60, 390]
    uuid = "d53301bb328baf12a3ae482cc6a565dd"
    hasVP = False
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

# 乱花葬
# swordman_female/vegabond/7e904ea3d2a9faa054604e55120a9268
# 1645c45aabb008c98406b3a16447040d/7e904ea3d2a9faa054604e55120a9268
class Skill31(ActiveSkill):
    """
        施展快速连续攻击并逐渐生成念气之花， 最后发动斩击将念气之花震散。 念气之花散开时对敌人造成多段伤害后爆炸。\n
        按住向前方向键施放时， 角色前冲一小段距离后再施展快速连续攻击。\n
        若在完成念气之花前按下跳跃键， 则可以中断技能。
    """
    name = "乱花葬"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 0
    rangeLv = 3
    cube = 1
    cd = 25
    mp = [100, 1400]
    uuid = "7e904ea3d2a9faa054604e55120a9268"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 连续攻击攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 6
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 最后斩击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 念气之花散开时攻击力 : {value3}% X {value4}
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 5
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 念气之花爆炸攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    hit5 = 1
    # [范围信息]
    # 范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)

    def vp_1(self):
        """
        [乱花葬]\n
        连续攻击后， 一击斩断花朵结束攻击\n
         - 连续攻击速度增加\n
         - 删除念气之花散开攻击、 念气之花爆炸\n
         - 总攻击力相同\n
        使被最后斩击命中的敌人进入强制控制状态3秒
        """
        ...

    def vp_2(self):
        """
        [乱花葬]\n
        前冲动作可以击退霸体状态的敌人\n
        连续攻击命中的敌人会被吸附至花中的中心位置\n
        攻击范围 +45%
        """
        ...

# 游龙掌
# swordman_female/vegabond/5152480fdde81362575a488d4cec4af9
# 1645c45aabb008c98406b3a16447040d/5152480fdde81362575a488d4cec4af9
class Skill32(ActiveSkill):
    """
        向前方施放游龙形态的剑气。\n
        若按前方向键， 可以聚集剑气发射角度。\n
        可以在空中使用， 但存在最低跳跃高度限制。
    """
    name = "游龙掌"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 12
    mp = [100, 900]
    uuid = "5152480fdde81362575a488d4cec4af9"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 剑气施放次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 剑气攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 10
    # [范围信息]
    # 剑气大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 发射距离 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [游龙掌]\n
        将剑气周围的敌人吸附到路径中心位置\n
        剑气大小和发射距离 +60%
        """
        ...

    def vp_2(self):
        """
        [游龙掌]\n
        迅速以直线方向发射剑气\n
         - 剑气发射次数 : 5次\n
         - 总攻击力相同\n
        施放[湮烈掌]、 [如来神掌]时， 若[游龙掌]处于可施放状态， 则可以无施放动作发射剑气
        """
        ...

# 回天璇鸣剑
# swordman_female/vegabond/2391a27457b5a8c6fa4b4670a91bdd11
# 1645c45aabb008c98406b3a16447040d/2391a27457b5a8c6fa4b4670a91bdd11
class Skill33(ActiveSkill):
    """
        将念气附加在武器上， 幻化成巨剑后向前方施展旋转攻击并给敌人造成多段伤害， 然后再砸向地面引发爆炸。\n
        按向前或上方向键， 可以小幅度增加前进距离。\n
        准备动作中， 额外输入技能键、 <Z>键或向后方向键时， 变更为在原地直接砸向前方地面后引发爆炸。\n
        在决斗场中， 通过输入方向键增加前进距离的功能不生效。
    """
    name = "回天璇鸣剑"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [70, 860]
    uuid = "2391a27457b5a8c6fa4b4670a91bdd11"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 0
    # 旋转斩击多段攻击次数上限 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 原地斩击攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # 爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [回天璇鸣剑]\n
        固定在原地挥剑引发爆炸\n
         - 删除按方向键和技能键功能\n
        可以在空中施放， 此时会快速下落并挥剑\n
        攻击范围 +30%
        """
        ...

    def vp_2(self):
        """
        [回天璇鸣剑]\n
        强化旋转攻击后结束技能\n
         - 删除爆炸攻击\n
         - 旋转斩击多段攻击次数 : 3次\n
         - 总攻击力相同\n
        删除按方向键功能\n
        旋转中移动距离 +200%\n
        旋转攻击可以击退霸体状态的敌人
        """
        ...

# 湮烈掌
# swordman_female/vegabond/fc458e449ee00b01dbf88d09aae65462
# 1645c45aabb008c98406b3a16447040d/fc458e449ee00b01dbf88d09aae65462
class Skill34(ActiveSkill):
    """
        将内劲凝聚于双手， 攻击前方敌人。 被湮烈掌击中的敌人会吸收一部分的内劲， 经过一定时间后再次受到内劲爆炸伤害。
    """
    name = "湮烈掌"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 1
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [350, 3000]
    uuid = "fc458e449ee00b01dbf88d09aae65462"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 内劲释放攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 内劲被吸收至爆炸的时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 内劲爆炸攻击力 : {value2}% x {value3}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 3
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # [范围信息]
    # 范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [湮烈掌]\n
        在原地快速释放内劲后结束技能\n
         - 凝聚内劲时间 -50%\n
         - 删除内劲爆炸攻击\n
         - 总攻击力相同
        """
        ...

    def vp_2(self):
        """
        [湮烈掌]\n
        内劲释放攻击范围 +30%\n
        强化内劲爆炸攻击\n
         - 变更为单次攻击\n
         - 总攻击力相同\n
         - 发生爆炸时自身所有速度 +10%， 效果持续20秒
        """
        ...

# 花舞千魂
# swordman_female/vegabond/5892d1fa4462e561ac8f8d2c74892b0a
# 1645c45aabb008c98406b3a16447040d/5892d1fa4462e561ac8f8d2c74892b0a
class Skill35(ActiveSkill):
    """
        冲向敌人并进行强力的连续攻击。\n
        一闪攻击结束前， 输入技能键或攻击键可连接后续攻击； 没有输入技能键时， 中断技能
    """
    name = "花舞千魂"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 0
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [130, 2100]
    uuid = "5892d1fa4462e561ac8f8d2c74892b0a"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 一闪攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 剑插地面攻击力 : {value1}% X {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 2
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 最后下斩攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1
    # [范围信息]
    # 范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)

    def vp_1(self):
        """
        [花舞千魂]\n
        删除剑插地攻击和最后下斩攻击\n
         - 总攻击力相同\n
        攻击范围 +30%\n
        一闪攻击后僵直时间 -30%\n
        一闪攻击后转换角色朝向
        """
        ...

    def vp_2(self):
        """
        [花舞千魂]\n
        施放技能时进入无敌状态\n
        一闪后转身连续斩击并返回原位， 然后用巨剑下劈进行最后一击\n
         - 删除按键连接施放功能\n
         - 总攻击力相同\n
        使被一闪命中的敌人进入强制控制状态，  直至技能结束
        """
        ...

# 三花聚顶
# swordman_female/vegabond/669f1428193f61f9d92c743b72438c4d
# 1645c45aabb008c98406b3a16447040d/669f1428193f61f9d92c743b72438c4d
class Skill36(PassiveSkill):
    """
        达到能随心所欲运用纯正内劲境界的剑豪， 利用这股力量进一步强化自身基本攻击力、 剑术和掌法的威力。\n
        另外， 进入异常状态时， 燃烧并立即解除异常状态， 并且增加攻击速度和移动速度。\n
        技能冷却时间过后， 可以再次解除异常状态。
    """
    name = "三花聚顶"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 3
    uuid = "669f1428193f61f9d92c743b72438c4d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击、 剑术、 掌法技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # - [解除异常状态时] -
    # 再次施放冷却时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 攻击速度增加 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 移动速度增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 增益效果持续时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4)

    associate = [
        {"data":data0,"type":"*skillDamage"}
    ]

# 花开寒影
# swordman_female/vegabond/8510294202d0e042dd29a2422fc6770d
# 1645c45aabb008c98406b3a16447040d/8510294202d0e042dd29a2422fc6770d
class Skill37(ActiveSkill):
    """
        将内功融入斩击之中， 在前方制造树枝， 绽放气花。\n
        生成气花和树枝的过程中会造成多段伤害， 花盛开时会回到原来的位置， 使花和树枝爆炸， 造成巨大伤害。
    """
    name = "花开寒影"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 6
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [1500, 12232]
    uuid = "8510294202d0e042dd29a2422fc6770d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 斩击攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 念气之花和树枝生成时攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 13
    # 生成时多段攻击次数 : {value2}次
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 念气之花和树枝爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1

# 啸空十字刃
# swordman_female/vegabond/2c9d9a36c8401bddff6cdb80fab8dc24
# 1645c45aabb008c98406b3a16447040d/2c9d9a36c8401bddff6cdb80fab8dc24
class Skill38(ActiveSkill):
    """
        将空间水平大幅度劈开后， 在空中出现并垂直下劈落地， 使敌人进入僵直状态， 十字形的剑气会维持一段时间后爆炸，造成额外伤害。\n
        垂直斩击是以最靠近水平斩中心部分的敌人头部为落地点。
    """
    name = "啸空十字刃"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [450, 1200]
    uuid = "2c9d9a36c8401bddff6cdb80fab8dc24"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 水平斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 垂直斩击攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [啸空十字刃]\n
        删除垂直斩击， 水平斩击持续时间 +1.5秒\n
         - 总攻击力相同\n
        再次按技能键时， 立即引发爆炸\n
        爆炸攻击范围 +30%
        """
        ...

    def vp_2(self):
        """
        [啸空十字刃]\n
        追踪并瞬移到前方一定范围内最强敌人位置\n
        之后同时施放水平斩击和垂直斩击， 结束动作的同时， 引爆十字刃造成伤害
        """
        ...

# 如来神掌
# swordman_female/vegabond/2ba299855fc22192cba4f73db75e9d0e
# 1645c45aabb008c98406b3a16447040d/2ba299855fc22192cba4f73db75e9d0e
class Skill39(ActiveSkill):
    """
        将内劲之力凝于手中， 然后向外发出巨型手掌模样的掌风。\n
        施放时，按向前方向键， 可以发射中等距离； 按上方向键， 可以发射最大距离。\n
        掌风拍出一定距离后会引爆并给敌人造成伤害， 被掌风击中的敌人将被击退一段距离。\n
        可以在空中施放， 但是需要达到一定的高度才能施放。\n
        被空中如来神掌击中的敌人将被拍入地面一定时间， 无法起身。
    """
    name = "如来神掌"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 2
    cube = 2
    cd = 50
    mp = [800, 1700]
    uuid = "2ba299855fc22192cba4f73db75e9d0e"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 掌风飞行距离上限 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # 攻击力 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 1
    # 爆炸攻击力 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 1
    # [范围信息]
    # 范围比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    def vp_1(self):
        """
        [如来神掌]\n
        发射掌风强制控制敌人后， 引发巨大爆炸\n
         - 掌风命中敌人时， 角色进入无敌状态\n
         - 爆炸发生时， 对掌风命中的敌人和爆炸范围内的敌人造成1次伤害\n
         - 删除直接攻击力\n
         - 总攻击力相同\n
        爆炸发生时， 技能结束后进入无敌状态， 效果持续0.2秒\n
        掌风未命中时不会引发爆炸， 结束技能\n
        地面施放时， 掌风可以击退可抓取的敌人
        """
        ...

    def vp_2(self):
        """
        [如来神掌]\n
        掌风基础移动距离增加\n
         - 删除通过方向键调整距离的功能\n
        掌风贯穿前方路径上的敌人后造成伤害， 此后贯穿的敌人身体发生爆炸， 造成额外伤害\n
        空中施放技能所需最低高度减少， 后跳过程中也可以施放\n
         - 在较低高度施放时， 跳到一定高度后发射掌风\n
        被击过程中也可以施放， 此时角色会因为强大的后座力而后退， 掌风的移动距离减少
        """
        ...

# 莲花剑舞
# swordman_female/vegabond/8b08f9504167a9c0f3a1d29d71b7943e
# 1645c45aabb008c98406b3a16447040d/8b08f9504167a9c0f3a1d29d71b7943e
class Skill40(ActiveSkill):
    """
        施展华丽的剑舞攻击前方的敌人， 然后迅速回到原位。\n
        剑舞分为4个招式， 被最后的回旋剑舞命中的敌人将会进入僵直状态。    \n
        在第4招回旋攻击前， 若按下前方向键， 则会原地攻击而不会回归原位。\n
        在跳跃状态下也可以施放技能， 此时取消第1招的前斩攻击并增加最后回旋斩的攻击力。
    """
    name = "莲花剑舞"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [800, 6000]
    uuid = "8b08f9504167a9c0f3a1d29d71b7943e"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 前斩攻击力 : {value0}% X {value1}
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 2
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # 空斩攻击力 : {value2}% X {value3}
    data2 = get_data(f'{prefix}/{uuid}', 2)
    hit2 = 2
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 后斩攻击力 : {value4}% X {value5}
    data4 = get_data(f'{prefix}/{uuid}', 4)
    hit4 = 2
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 回旋斩攻击力 : {value6}% X {value7}
    data6 = get_data(f'{prefix}/{uuid}', 6)
    hit6 = 2
    data7 = get_data(f'{prefix}/{uuid}', 7)
    # 在跳跃状态下施放技能时， 回旋斩攻击力 : {value8}% X {value9}
    data8 = get_data(f'{prefix}/{uuid}', 8)
    data9 = get_data(f'{prefix}/{uuid}', 9)
    # [范围信息]
    # 范围比率 : {value10}%
    data10 = get_data(f'{prefix}/{uuid}', 10)

    def vp_1(self):
        """
        [莲花剑舞]\n
        地面施放时招式发生变化\n
         - 删除1招式攻击\n
         - 总攻击力相同\n
        2招式与3招式攻击将敌人吸附至角色前方\n
        攻击范围 +20%
        """
        ...

    def vp_2(self):
        """
        [莲花剑舞]\n
        可以强制中断转职技能的施放后僵直并施放\n
        每次施放技能时， 会在原地展开一个招式， 按向前方向键时会向前滑动并使用招式\n
         - 首次施放时使用第1招\n
         - 在接下来的10秒内， 可以依次使用第2招、 第3招、 第4招\n
         - 在空中施放时固定使用第3招\n
         - 总攻击力相同
        """
        ...

# 七星耀华
# swordman_female/vegabond/ac21c02567f04a92b54dd85c091d1e5a
# 1645c45aabb008c98406b3a16447040d/ac21c02567f04a92b54dd85c091d1e5a
class Skill41(PassiveSkill):
    """
        突破五气朝元的极限， 进入七星耀华的境界。剑术变得比之前更加锋利， 内劲大幅提升， 增加基本攻击、 剑术和掌法的攻击力。
    """
    name = "七星耀华"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 1
    rangeLv = 3
    uuid = "ac21c02567f04a92b54dd85c091d1e5a"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击、 剑术、 掌法技能攻击力增加量 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)

    associate = [
        {"data":data0,"type":"*skillDamage"}
    ]

# 樱花劫
# swordman_female/vegabond/0113c8b1306ca76d208f83f2d093dd62
# 1645c45aabb008c98406b3a16447040d/0113c8b1306ca76d208f83f2d093dd62
class Skill42(ActiveSkill):
    """
        冲向前方极速斩击敌人后回到原位， 并造成巨大伤害。 \n
        敌人将进入被挑衅的状态， 无法动弹。\n
        剑帝将剑收进剑鞘的瞬间， 敌人将受到巨大的伤害，并被强行控制后倒地。\n
        剑帝开始移动的那一刻， 进入无敌状态。\n
        前方斩击时若按向前方向键， 则剑帝不会回到原位， 而是出现在前方并收剑入鞘。\n
        可以取消部分转职技能的施放后僵直并立即施放该技能； 收剑入鞘的瞬间可以连接除增益技能之外的所有主动技能。
    """
    name = "樱花劫"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 2
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [580, 4500]
    uuid = "0113c8b1306ca76d208f83f2d093dd62"
    hasVP = True
    hasUP = True
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # [范围信息]
    # 范围比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1)

    def vp_1(self):
        """
        [樱花劫]\n
        向前方斩击后返回， 将剑插入剑鞘前再次按技能键时， 移动至斩击敌人中最强大的敌人， 并将剑插入剑鞘\n
        技能结束后， 维持无敌状态0.3秒
        """
        ...

    def vp_2(self):
        """
        [樱花劫]\n
        - 基本冷却时间变更为67.5秒\n
        - 攻击力 +50%\n
        攻击范围 +50%
        """
        self.cd = 67.5
        self.skillRation *= 1.5
        ...

# 飞花逐月
# swordman_female/vegabond/7ec521d063d2190e1fcc5bd229af9bcf
# 1645c45aabb008c98406b3a16447040d/7ec521d063d2190e1fcc5bd229af9bcf
class Skill43(ActiveSkill):
    """
        拔出月光飞剑刺进地面快速斩击周围的敌人。\n
        随后冲向前方进行多次斩击， 并跳到空中， 以蕴含月之气息的巨大剑气给予敌人最后一击。\n
        被月光飞剑击中的敌人会被强制控制。\n
        施放技能时， 可以利用前/后方向键控制斩击的方向。
    """
    name = "飞花逐月"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "7ec521d063d2190e1fcc5bd229af9bcf"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 月光飞剑刺进地面攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 20
    # 连续斩击攻击力 : {value1}% X {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 前冲攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    # 空中斩击攻击力 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4)
    # 回落斩击攻击力 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5)
    # 上挑斩击攻击力 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6)
    # 最后一击攻击力 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7)
    hit7 = 1

# 落英惊鸿掌
# swordman_female/vegabond/92360eab6e1f378902018eca681ac629
# 1645c45aabb008c98406b3a16447040d/92360eab6e1f378902018eca681ac629
class Skill44(ActiveSkill):
    """
        利用轻功快速靠近敌人， 随后向敌人倾注大量内劲。\n
        命中的敌人将处于走火入魔状态， 并受到多段攻击伤害。 一定时间过后， 注入的内劲产生强烈的爆炸造成巨大伤害。\n
        可以在地面或者空中使用。
    """
    name = "落英惊鸿掌"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [773, 6000]
    uuid = "92360eab6e1f378902018eca681ac629"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 注入攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1
    # 内劲多段攻击力 : {value1}% X {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1)
    hit1 = 4
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # 内劲爆炸攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)
    hit3 = 1

# 剑仙之境
# swordman_female/vegabond/5cac3411ccef1af333953e0ded5e942d
# 1645c45aabb008c98406b3a16447040d/5cac3411ccef1af333953e0ded5e942d
class Skill45(PassiveSkill):
    """
        达到剑仙境界的极诣·流浪武士的剑术和掌法得到进一步强化， 增加基本攻击力和转职技能攻击力， 提高内劲的运用能力， 使部分技能产生附加效果。\n
    [一花渡江]\n
    减少冷却时间， 可以强制中断转职系列技能的僵直后使用。\n
    [游龙掌]\n
    增加剑气大小及发射速度， 施放时进入霸体状态。
    """
    name = "剑仙之境"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "5cac3411ccef1af333953e0ded5e942d"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    # [一花渡江]冷却时间减少 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1)
    # [游龙掌]剑气大小比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2)
    # [游龙掌]发射速度比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3)

    associate = [
        {"data":data0,"type":"*skillDamage"}
    ]

# 轻云出月风静夜
# swordman_female/vegabond/3cb633d00f8f6ee088682c9171020d26
# 1645c45aabb008c98406b3a16447040d/3cb633d00f8f6ee088682c9171020d26
class Skill46(ActiveSkill):
    """
        集中精神凝缩内劲。 完成一闪准备后， 向前方突进并进行强力的回旋斩击。\n
    [三次觉醒技能]\n
        使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
        若关联的技能还在冷却中， 则无法使用三次觉醒技能。
    """
    name = "轻云出月风静夜"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "3cb633d00f8f6ee088682c9171020d26"
    hasVP = False
    hasUP = False
    custom = get_data(f'{prefix}/{uuid}', "custom") # noqa: E501
    # 横斩攻击力 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0)
    hit0 = 1


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'vegabond'
        self.nameCN = '极诣·流浪武士'
        self.role = 'swordman_female'
        self.角色 = '鬼剑士(女)'
        self.职业 = '流浪武士'
        self.jobId = '1645c45aabb008c98406b3a16447040d'
        self.jobGrowId = 'c9b492038ee3ca8d27d7004cf58d59f3'

        self.武器选项 = ['光剑', '巨剑', '钝器', '太刀', '短剑']
        self.副武器选项 = ['光剑']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '皮甲'
        self.buff = 2.335

        super().__init__(equVersion, __name__)


    def calc_weapon(self,cur:CharacterEquipInfo):
        if cur.equInfo is None:
            return
        if cur.equInfo.itemType == "副武器":
            if '传世武器' in cur.equInfo.categorize:
                ATKP = 武器强化计算(115, '史诗', cur.reinforce, cur.equInfo.itemDetailType, '物理', 1.12)
            else:
                # 强化计算
                ATKP = 武器强化计算(115, '史诗', cur.reinforce, cur.equInfo.itemDetailType, '物理')
            # 武器基础
            STR = cur.equInfo.STR
            if cur.reinforceType == 1:
                # 增幅四维
                STR += 增幅计算(115, '史诗', cur.reinforce)
            self.SetStatus(AtkP = (cur.equInfo.AtkP + ATKP) * 0.1,STR = STR*0.1)
        else:
            super().calc_weapon(cur)