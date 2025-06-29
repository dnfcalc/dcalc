#a5ccbaf5538981c6ef99b236c0a60b73
from core.basic.skill import PassiveSkill, ActiveSkill, get_data
from core.basic.character import Character
prefix = "mage_male/dimension_walker/cn/skillDetail"


# 不死之身
# mage_male/dimension_walker/bb34e8854a93fd250347a1c64119f7ab
# a5ccbaf5538981c6ef99b236c0a60b73/bb34e8854a93fd250347a1c64119f7ab
class Skill2(PassiveSkill):
    """
    角色死亡后带着少量生命值原地复活， 并且进入自动恢复生命值模式。\n
    自动恢复生命值模式下， 角色的生命值值可以在一定时间内自动恢复至100%， 但无法借用任何道具或其它途径恢复生命值， 且所受到的伤害还会加剧。\n
    若在恢复模式下死亡， 则无法再次通过该技能复活。
    """
    name = "不死之身"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 1 #TODO
    rangeLv = 3
    uuid = "bb34e8854a93fd250347a1c64119f7ab"
    hasVP = False
    hasUP = False

    # 恢复模式下所受伤害增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 死亡时立即恢复的生命值量 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 恢复模式持续时间(普通地下城) : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 恢复模式持续时间(亡者峡谷) : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

# 黑暗之眼
# mage_male/dimension_walker/6e33d47e6622ce03b6defdd912140270
# a5ccbaf5538981c6ef99b236c0a60b73/6e33d47e6622ce03b6defdd912140270
class Skill3(PassiveSkill):
    """
    增加魔法师的魔法值最大值； 若魔法值低于一定比率时， 还可增加魔法值恢复速度。
    """
    name = "黑暗之眼"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 2 #TODO
    rangeLv = 1
    uuid = "6e33d47e6622ce03b6defdd912140270"
    hasVP = False
    hasUP = False

    # 魔法值最大值增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 可触发恢复效果时的魔法值比率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 魔法值恢复速度增加 : {value2}倍
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 超然感知
# mage_male/dimension_walker/d53301bb328baf12a3ae482cc6a565dd
# a5ccbaf5538981c6ef99b236c0a60b73/d53301bb328baf12a3ae482cc6a565dd
class Skill4(PassiveSkill):
    """
    基本攻击变更为蕴含次元能量的魔法球， 并生成边界能量。\n
    [次元边界]\n
    -基本攻击或次元系列技能命中敌人时， 增加边界能量。\n
    -次元系列技能命中敌人时， 引发次元波动。\n
    - 能量条填满时， 可以获得次元石。\n
    -若在一定时间内没有引发次元波动， 边界能量条和波动数会逐渐减少。\n
    施放[次元边界]技能时， 会消耗次元石。\n
    [若你能看见别人看不见的东西， 只会让你更麻烦。]
    """
    name = "超然感知"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 3 #TODO
    rangeLv = 1
    uuid = "d53301bb328baf12a3ae482cc6a565dd"
    hasVP = False
    hasUP = False

    # 边界能量条最大值 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 次元石持有量上限 : {value1}个
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 普通攻击命中时能量条增加量 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

# 次元边界
# mage_male/dimension_walker/7e904ea3d2a9faa054604e55120a9268
# a5ccbaf5538981c6ef99b236c0a60b73/7e904ea3d2a9faa054604e55120a9268
class Skill5(ActiveSkill):
    """
    施放时消耗一个次元石， 在下一个次元系列技能附加特殊能力或改变形态。\n
    已附加[次元边界]效果的次元系列技能， 将减少边界能量条获得量。\n
    可以强制中断释放中的转职技能， 并立即施放该技能。\n
    [请注意使用， 请尽快使用， 请不要给别人看， 除非你想其他人把你当成骗子。]
    """
    name = "次元边界"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 5 #TODO
    rangeLv = 3
    cd = 0.1
    uuid = "7e904ea3d2a9faa054604e55120a9268"
    hasVP = False
    hasUP = False

    # 施放时所需次元石数量 : {value0}个
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)

# 次元之乖离扫把精通
# mage_male/dimension_walker/5152480fdde81362575a488d4cec4af9
# a5ccbaf5538981c6ef99b236c0a60b73/5152480fdde81362575a488d4cec4af9
class Skill6(PassiveSkill):
    """
    可以装备扫把。 装备扫把时， 增加施放速度和命中率。\n
    学习[虚空之力]后， 装备扫把的状态下， 进入地下城或完全死亡后复活时， 增加1个边界能量条的波动次数。\n
    [很可惜， 由于某些原因， 需要放弃一些天生的东西。]
    """
    name = "次元之乖离扫把精通"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 7 #TODO
    rangeLv = 1
    uuid = "5152480fdde81362575a488d4cec4af9"
    hasVP = False
    hasUP = False

    # 施放速度增加 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 命中率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)


# 基础精通
# mage_male/dimension_walker/5a56514f35cf0270ae8d6c65f8fefd78
# a5ccbaf5538981c6ef99b236c0a60b73/5a56514f35cf0270ae8d6c65f8fefd78
class Skill8(PassiveSkill):
    """
    增加基本攻击、 前冲攻击、 跳跃攻击、 [魔法旋风]的攻击力。\n
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

    associate = [{"type":"*skillRation","data":[i-100 if i>0 else 0 for i in data0],"skills":["乖离 : 禁忌之奈雅丽"]}]

# 幽冥火
# mage_male/dimension_walker/cfacda0647b9a0f595df2c2aad30c18d
# a5ccbaf5538981c6ef99b236c0a60b73/cfacda0647b9a0f595df2c2aad30c18d
class Skill13(ActiveSkill):
    """
    生成两团幽冥火， 可以增加自身的物理和魔法防御力， 且造成一定伤害， 效果持续一定时间。\n
    转职成次元行者时， 可以学习[虚妄之火]技能。\n
    学习[虚妄之火]后， 持续时间变更为无限， 且无法发动攻击。
    """
    name = "幽冥火"
    learnLv = 10
    masterLv = 10
    maxLv = 20
    position = 1 #TODO
    rangeLv = 3
    cd = 10
    mp = [30, 345]
    uuid = "cfacda0647b9a0f595df2c2aad30c18d"
    hasVP = False
    hasUP = False

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 每个火球增加物理防御力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 每个火球增加魔法防御力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 每个火球的攻击力 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # - [虚妄之火效果] -
    # 物理防御力增加 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 魔法防御力增加 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)


# 瞬移
# mage_male/dimension_walker/3d8f3d438405d79f8d3ed68072674d1e
# a5ccbaf5538981c6ef99b236c0a60b73/3d8f3d438405d79f8d3ed68072674d1e
class Skill14(ActiveSkill):
    """
    向指定方向快速移动一定距离。
    """
    name = "瞬移"
    learnLv = 10
    masterLv = 1
    maxLv = 1
    position = 5 #TODO
    rangeLv = 2
    cd = 1.5
    mp = [40, 40]
    uuid = "3d8f3d438405d79f8d3ed68072674d1e"
    hasVP = False
    hasUP = False

    # X轴移动距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # Y轴移动距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 次元 : 坠落
# mage_male/dimension_walker/4f2e001e9a19eb7bae50ad1840dfb329
# a5ccbaf5538981c6ef99b236c0a60b73/4f2e001e9a19eb7bae50ad1840dfb329
class Skill19(ActiveSkill):
    """
    在空中开启次元之门， 掉落杂物箱。 被杂物箱命中的敌人将会进入眩晕状态， 还有一定几率掉落装有爆炸物的箱子。 施放时若按方向键， 可以在更远处掉落箱子。\n
    转职为次元行者后， 可以适用[次元边界]的效果。\n
    [次元边界效果]\n
    可将箱子掉落点周围的敌人汇聚到一起。\n
    [初学次元学的怪才们， 通常第一次犯的失误是将次元之门开在自己的头部上方， 第二次犯的失误是重复第一个失误……]
    """
    name = "次元 : 坠落"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 4
    mp = [30, 280]
    uuid = "4f2e001e9a19eb7bae50ad1840dfb329"
    hasVP = False
    hasUP = True

    # 普通情况下箱子掉落位置 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 按方向键时箱子掉落位置 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 边界能量条增加量 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 箱子魔法攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit0 = 1
    # 箱子冲击波攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 0
    # 爆炸物箱子出现几率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 爆炸物箱子攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    hit6 = 1
    # 眩晕持续时间 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    # [次元边界效果]
    # 次元边界能量条增加量 : {value8}
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)
    # 周围敌人吸附范围 : {value9}px
    data9 = get_data(f'{prefix}/{uuid}', 9, lambda x = None: x)

    mode = ["箱子","普通"]

    def setMode(self, mode):
        if mode == "普通":
            self.hit6 = 0
            self.hit4 = 1
        return super().setMode(mode)

# 乖离 : 虚无
# mage_male/dimension_walker/dbf8b30c7057032af0d68fcfa289fdae
# a5ccbaf5538981c6ef99b236c0a60b73/dbf8b30c7057032af0d68fcfa289fdae
class Skill20(PassiveSkill):
    """
    召唤异界的怪物——虚无环绕在脚下。\n
    虚无存在的时间内， 可以增加角色和奈雅丽的基本攻击力和次元系列技能的伤害。\n
    虚无可通过[乖离 : 迷雾]向前方发射， 附着敌人时， 技能效果发生改变。\n
    虚无的技能等级每次上升时， 怪物的影响力会变得更强， 施放[乖离 : 迷雾]时的生命值消耗量会增加。\n
    [是狂气的痕迹还是我的过失？]
    """
    name = "乖离 : 虚无"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 7 #TODO
    rangeLv = 3
    uuid = "dbf8b30c7057032af0d68fcfa289fdae"
    hasVP = False
    hasUP = False

    # 基本攻击和次元系列技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 迷雾附着敌人时， 基本攻击和次元系列技能攻击力增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    associate = [{"data":data0,"skills":["次元 : 坠落","次元 : 虚影","次元 : 跃迁","次元 : 离子束","次元 : 万花镜","次元 : 粒子风暴","次元 : 时空磁场","次元 : 粒子波","次元 : 思维聚爆","次元 : 奇点","禁断之盛宴","未明·次元崩坏","乖离 : 禁忌之奈雅丽"]}]

# 次元扭曲装置
# mage_male/dimension_walker/fc458e449ee00b01dbf88d09aae65462
# a5ccbaf5538981c6ef99b236c0a60b73/fc458e449ee00b01dbf88d09aae65462
class Skill21(PassiveSkill):
    """
    为了研究次元之力开发的道具。\n
    增加自身的技能攻击力、 魔法暴击率、 魔法值和施放速度。\n
    [虽然呼吸不畅， 但总比死了好多了吧……]
    """
    name = "次元扭曲装置"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    uuid = "fc458e449ee00b01dbf88d09aae65462"
    hasVP = False
    hasUP = False

    # 基本攻击力和技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 魔法暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 魔法值上限增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 施放速度增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    associate = [{"data":data0}]

# 次元 : 虚影
# mage_male/dimension_walker/1812a1ece67bb37b6b44b54766450064
# a5ccbaf5538981c6ef99b236c0a60b73/1812a1ece67bb37b6b44b54766450064
class Skill22(ActiveSkill):
    """
    将自身的形象投射到次元， 向前发射并攻击敌人。\n
    使用上下方向键时， 可以改变发射方向。\n
    [次元边界效果]\n
    缩短发射距离， 但是可以击退路径上的敌人。\n
    [有没有想过镜中的世界才是真实的？]
    """
    name = "次元 : 虚影"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 5
    mp = [20, 210]
    uuid = "1812a1ece67bb37b6b44b54766450064"
    hasVP = False
    hasUP = True

    # 边界能量条增加量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # [次元边界效果]
    # 次元边界能量条增加量 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [范围信息]
    # 一般状态下突进距离比率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

# 次元 : 跃迁
# mage_male/dimension_walker/2ba299855fc22192cba4f73db75e9d0e
# a5ccbaf5538981c6ef99b236c0a60b73/2ba299855fc22192cba4f73db75e9d0e
class Skill23(ActiveSkill):
    """
    开启异次元裂缝， 引发次元场攻击敌人并使敌人进入强制控制状态后， 向后方瞬移。\n
    被击状态下也可以施放该技能， 但是消耗1个次元石。\n
    在决斗场中， 不会强控敌人， 被击时可以施放的次数固定为1次。
    """
    name = "次元 : 跃迁"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 3
    cds = [0, 15, 14.9, 14.9, 14.8, 14.7, 14.7, 14.6, 14.5, 14.5, 14.4, 14.3, 14.3, 14.2, 14.2, 14.1, 14, 14, 13.9, 13.8, 13.8, 13.7, 13.6, 13.6, 13.5, 13.4, 13.4, 13.3, 13.2, 13.2, 13.1, 13, 13, 12.9, 12.8, 12.8, 12.7, 12.7, 12.6, 12.5, 12.5, 12.4, 12.3, 12.3, 12.2, 12.1, 12.1, 12, 11.9, 11.9, 11.8, 11.7, 11.7, 11.6, 11.5, 11.5, 11.4, 11.3, 11.3, 11.2, 11.2, 11.1, 11, 11, 10.9, 10.8, 10.8, 10.7, 10.6, 10.6, 10.5]
    mp = [20, 70]
    uuid = "2ba299855fc22192cba4f73db75e9d0e"
    hasVP = False
    hasUP = True

    # 边界能量条增加量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 后方瞬移距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 次元场攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 控制时间 : {value3}秒
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [范围信息]
    # 冲击波大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    def getSkillCD(self, mode=None):
        self.cd = self.cds[self.lv]
        return super().getSkillCD(mode)

# 乖离 : 禁忌之奈雅丽
# mage_male/dimension_walker/7f80b887a09e88e2c4728c898bd73654
# a5ccbaf5538981c6ef99b236c0a60b73/7f80b887a09e88e2c4728c898bd73654
class Skill24(ActiveSkill):
    """
    消耗自身生命值， 从异界召唤奈雅丽。\n
    奈雅丽可以提升次元行者的独立攻击力； 奈雅丽可以自由移动， 并且可以代替自身施放部分技能。\n
    召唤奈雅丽的状态下， 次元行者施放转职技能命中敌人时， 减少奈雅丽的攻击冷却时间、 增加移动速度， 效果持续一定时间。\n
    该效果可以重叠， 达到重叠上限时， 奈雅丽的身上会出现红心效果。\n
    奈雅丽的攻击力与次元行者同步， 受[基础精通]和[乖离 : 虚无]的影响； 召唤奈雅丽的状态下， 若按下技能键， 则会解除召唤。
    """
    name = "乖离 : 禁忌之奈雅丽"
    learnLv = 20
    masterLv = 1
    maxLv = 11
    position = 7 #TODO
    rangeLv = 2
    cd = 5
    mp = [30, 90]
    uuid = "7f80b887a09e88e2c4728c898bd73654"
    hasVP = False
    hasUP = True

    # 召唤时生命值消耗 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 召唤持续时间 : {value1}秒
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 近距离攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 远程攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 独立攻击力增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # - [转职技能命中时附加效果] -
    # 奈雅丽攻击冷却时间减少率 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 奈雅丽移动速度增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # 持续时间 : {value7}秒
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    # 重叠次数上限 : {value8}次
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)

    associate = [{"data":data4,"type":"$*PAtkI"}]

    def getSkillCD(self, mode=None):
        return 0.75

# 奈雅丽的茶歇时间
# mage_male/dimension_walker/e5c09f9132a48dc1d695968592cc5878
# a5ccbaf5538981c6ef99b236c0a60b73/e5c09f9132a48dc1d695968592cc5878
class Skill25(ActiveSkill):
    """
    奈雅丽停止攻击动作。 停止攻击动作的状态下可以施放技能。\n
    茶歇时间持续到再次施放为止。 持续期间， 增加次元行者的魔法值恢复量。\n
    决斗场中， 茶歇时间持续期间， 奈雅丽会逐渐恢复生命值。\n
    [我非常惊讶。 从异界来过来的人， 居然能泡出一杯这么好喝的茶……起码在这一点上， 我的研究是有价值的。 对了， 这是什么茶呢？]
    """
    name = "奈雅丽的茶歇时间"
    learnLv = 20
    masterLv = 1
    maxLv = 1
    position = 8 #TODO
    rangeLv = 2
    cd = 1
    uuid = "e5c09f9132a48dc1d695968592cc5878"
    hasVP = False
    hasUP = False

    # 角色每10秒魔法值恢复量增加 : 1%

# 次元 : 离子束
# mage_male/dimension_walker/d89f26862e348a801b30bb9fd7125db5
# a5ccbaf5538981c6ef99b236c0a60b73/d89f26862e348a801b30bb9fd7125db5
class Skill27(ActiveSkill):
    """
    开启次元之门， 从里面连续发射激光。\n
    [次元边界效果]\n
    压缩能量， 发射强力的激光。\n
    [选择或集中， 在任何情况下都适用。]
    """
    name = "次元 : 离子束"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 7
    mp = [35, 350]
    uuid = "d89f26862e348a801b30bb9fd7125db5"
    hasVP = False
    hasUP = True

    # 边界能量条增加量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 激光攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 6
    # [次元边界效果]
    # 边界能量增加量 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 压缩能量后的激光攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 0
    # [范围信息]
    # 激光大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    mode = ["强化","普通"]

    def setMode(self, mode):
        if mode == "强化":
            self.hit1 = 6
            self.hit3 = 0
        elif mode == "普通":
            self.hit1 = 0
            self.hit3 = 1
# 时空壁障
# mage_male/dimension_walker/2c9d9a36c8401bddff6cdb80fab8dc24
# a5ccbaf5538981c6ef99b236c0a60b73/2c9d9a36c8401bddff6cdb80fab8dc24
class Skill28(ActiveSkill):
    """
    打破时空边界， 将异界的气息环绕在自身周围。\n
    增加基本攻击力、  次元系列技能和乖离系列技能的攻击力。
    """
    name = "时空壁障"
    learnLv = 25
    masterLv = 10
    maxLv = 20
    position = 4 #TODO
    rangeLv = 3
    cd = 5
    uuid = "2c9d9a36c8401bddff6cdb80fab8dc24"
    hasVP = False
    hasUP = False

    # 持续时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 基本攻击和技能攻击增加率 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)

# 虚妄之火
# mage_male/dimension_walker/dde3b443bd5e61d90c34e5ee771e2c28
# a5ccbaf5538981c6ef99b236c0a60b73/dde3b443bd5e61d90c34e5ee771e2c28
class Skill29(PassiveSkill):
    """
    将[幽冥火]变更为[虚妄之火]。 \n
    删除发射功能， 火球持续时间变更为无限制。 并且增加更多的防御力。\n
    变更后的防御力增加量遵循[幽冥火]的数值。\n
    [偶然中发明的东西， 但是用上去还可以。]
    """
    name = "虚妄之火"
    learnLv = 25
    masterLv = 1
    maxLv = 1
    position = 1 #TODO
    rangeLv = 2
    uuid = "dde3b443bd5e61d90c34e5ee771e2c28"
    hasVP = False
    hasUP = False


# 乖离 : 迷雾
# mage_male/dimension_walker/5892d1fa4462e561ac8f8d2c74892b0a
# a5ccbaf5538981c6ef99b236c0a60b73/5892d1fa4462e561ac8f8d2c74892b0a
class Skill30(ActiveSkill):
    """
    虚无变换为迷雾之怪向前方发射。\n
    迷雾之怪碰到敌人或障碍物时， 会附身到周围级别最高的敌人身上。\n
    [乖离 : 虚无]的基本攻击和次元系列技能对迷雾附身的敌人具有更高的伤害增幅效果。 (维持对周围其他敌人的基础伤害增幅效果)\n
    此外， 部分技能施放后会优先追踪并攻击被附着的敌人。\n
    附身到敌人身上时， 边界能量条上方会标记敌人。 若再次按技能键， 可以召回附身的迷雾之怪。\n
    学习[古史记忆]后， 一定距离内存在敌人时可以使用， 会飞向敌人并附着。\n
    在决斗场中， 附身时间有上限。\n
    [用起来还不错， 但是对健康不太好……尤其是装备信条装置的情况下。]
    """
    name = "乖离 : 迷雾"
    learnLv = 30
    masterLv = 1
    maxLv = 1
    position = 7 #TODO
    rangeLv = 2
    cd = 1
    uuid = "5892d1fa4462e561ac8f8d2c74892b0a"
    hasVP = False
    hasUP = False

    # 生命值消耗 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 在决斗场内， 迷雾附身时间上限 : 5秒
    # [范围信息]
    # 索敌范围 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [学习古史记忆后]
    # 索敌距离 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 索敌宽度 : {value3}px
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 索敌高度 : {value4}px
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 召回等待时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)

# 次元 : 万花镜
# mage_male/dimension_walker/b89c9ab317bc0a443f6497b7cca2f6a8
# a5ccbaf5538981c6ef99b236c0a60b73/b89c9ab317bc0a443f6497b7cca2f6a8
class Skill31(ActiveSkill):
    """
    将次元的能量聚集到自身后， 冲刺到前方， 并给命中的敌人施展瞬间移动攻击。\n
    攻击过程中进入无敌状态， 被攻击的敌人会进入强制控制状态。\n
    可以利用上/下方向键改变冲刺方向。\n
    若有敌人被[乖离 : 迷雾]所附身， 则施放技能时， 无视距离直接瞬移到敌人身旁并展开攻击。\n
    [次元边界效果]\n
    攻击方式变更为， 投射自身的分身， 让分身代替本人攻击敌人。\n
    分身的攻击力比角色本身低。\n
    [将次元之力直接投射到人体……只有疯子才会这么做， 这样做实在是太疲惫了。]
    """
    name = "次元 : 万花镜"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 10
    mp = [180, 1512]
    uuid = "b89c9ab317bc0a443f6497b7cca2f6a8"
    hasVP = False
    hasUP = True

    # 边界能量条增加量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 乱打攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 4
    # [次元边界效果]
    # 边界能量增加量 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 下乱打攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 4
    # [范围信息]
    # 冲击波大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    mode = ["普通","强化"]

    def setMode(self, mode):
        if mode == "强化":
            self.hit1 = 0
            self.hit3 = 4
        elif mode == "普通":
            self.hit1 = 4
            self.hit3 = 0


# 乖离 : 魅魔之舞
# mage_male/dimension_walker/0fbb8de70002ad34f046c94c2cb3e863
# a5ccbaf5538981c6ef99b236c0a60b73/0fbb8de70002ad34f046c94c2cb3e863
class Skill32(ActiveSkill):
    """
    奈雅丽瞬间移动到角色位置， 然后向前方突进并鞭笞遇到的敌人。\n
    若按向下方向键， 则会在原地攻击敌人。\n
    若有敌人被[乖离 : 迷雾]所附身， 则瞬移到敌人身旁并展开攻击。(决斗场中不适用)\n
    [看到她鞭笞别人时那欢快的样子， 我再忙也要抽出时间陪她玩。]
    """
    name = "乖离 : 魅魔之舞"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 8 #TODO
    rangeLv = 2
    cd = 10
    mp = [185, 1526]
    uuid = "0fbb8de70002ad34f046c94c2cb3e863"
    hasVP = False
    hasUP = True

    # 乱打攻击次数 : {value0}次
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 乱打攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 15
    # 最终一击攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1

# 次元 : 粒子风暴
# mage_male/dimension_walker/7cf17936a039b418660424125dc968d7
# a5ccbaf5538981c6ef99b236c0a60b73/7cf17936a039b418660424125dc968d7
class Skill33(ActiveSkill):
    """
    扭曲空间引发多次爆炸。 \n
    施放时， 利用方向键可以在前方更远处引发爆炸。\n
    [次元边界效果]\n
    增加爆炸倒计时， 但威力更高。 该魔法球无法增加边界能量条。\n
    [稍微调整了数值， 但结果完全不同啊。]
    """
    name = "次元 : 粒子风暴"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cube = 1
    cd = 16
    mp = [185, 1526]
    uuid = "7cf17936a039b418660424125dc968d7"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 边界能量增加量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 基础施放距离 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 使用方向键时施放距离 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 3
    # [次元边界效果]
    # 边界能量条增加量 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 爆炸倒计时 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    hit6 = 1
    # [范围信息]
    # 冲击波大小比率 : {value7}%
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)

    mode = ["普通","强化"]

    def setMode(self, mode):
        if mode == "强化":
            self.hit3 = 0
            self.hit6 = 1
        elif mode == "普通":
            self.hit3 = 3
            self.hit6 = 0

    def vp_1(self):
        """
        [次元 : 粒子风暴]\n
        在前方连续快速生成多个次元爆炸\n
        - 不消耗次元石， 固定以次元边界效果发动\n
        - 对领域内的敌人造成相同的连锁伤害\n
        - 爆炸速度增加\n
        - 总攻击力相同\n
        [分散， 反而能发挥更大的威力。]
        """
        self.setMode("强化")
        ...

    def vp_2(self):
        """
        [次元 : 粒子风暴]\n
        使用次元系列技能时可以施放\n
        若存在被[乖离 : 迷雾]附身的敌人， 则扭曲该位置\n
        [可以说是省略了坐标系。]
        """
        ...

# 次元 : 时空磁场
# mage_male/dimension_walker/3fb8395ae3b81bd608e0c4223a8eb534
# a5ccbaf5538981c6ef99b236c0a60b73/3fb8395ae3b81bd608e0c4223a8eb534
class Skill34(ActiveSkill):
    """
    以自身为中心展开次元场。\n
    被命中的敌人会受到次元扭曲效果， 此时若按下技能键， 则可以将所有处于次元扭曲效果的敌人聚集到一点并额外造成伤害。\n
    使用次元系技能攻击次元扭曲状态下的敌人时， 可以恢复更多的边界能量条； 次元扭曲造成额外伤害后， 次元扭曲依然持续一段时间。\n
    [次元边界效果]\n
    次元扭曲造成额外伤害后， 使敌人进入束缚状态。\n
    [很多人觉得瞬移很方便， 我这是专门为那些人研发的魔法术式……请你们不要骂我……]
    """
    name = "次元 : 时空磁场"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cube = 1
    cd = 14
    mp = [160, 1344]
    uuid = "3fb8395ae3b81bd608e0c4223a8eb534"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 边界能量条增加量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 2
    # 次元扭曲持续时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 边界能量条额外增加率 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [次元边界效果]
    # 次元边界能量条增加量 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 束缚持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # [范围信息]
    # 范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

    def vp_1(self):
        """
        [次元 : 时空磁场]\n
        若奈雅丽已经被召唤出来， 则以奈雅丽的位置为中心展开次元场\n
        再次按技能键时， 与奈雅丽调换位置并回收次元场\n
        - 不会移动敌人\n
        - 移动后3秒内所受伤害 -90%\n
        [替换坐标， 就是调换位置。 不过， 想要换谁， 也得先问问奈雅丽同不同意。]
        """
        ...

    def vp_2(self):
        """
        [次元 : 时空磁场]\n
        无法再次按技能键\n
        生成次元场时， 以被击中的敌人为中心， 次元场会再次展开， 造成相同伤害\n
        发动[次元边界]时的效果变更\n
        - 范围 +15%\n
        - 次元场命中时， 使敌人进入束缚状态\n
        [要是不躲开， 那就等着再挨一次吧。]
        """
        ...

# 乖离 : 异界蜂群
# mage_male/dimension_walker/c5a2956d8ed3af1746ed2f76ca971a09
# a5ccbaf5538981c6ef99b236c0a60b73/c5a2956d8ed3af1746ed2f76ca971a09
class Skill35(ActiveSkill):
    """
    消耗自身生命值， 从异次元裂缝召唤异界蜂群攻击敌人。 受到攻击的敌人进入减速状态， 以及受到持续的伤害， 效果持续一定时间。\n
    给敌人造成持续伤害的同时， 恢复角色生命值。\n
    在决斗场中， 减速效果不生效。\n
    [我不是很乐意将奈雅丽的朋友们介绍给别人， 但也要看具体情况。]
    """
    name = "乖离 : 异界蜂群"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 7 #TODO
    rangeLv = 2
    cube = 1
    cd = 20
    mp = [350, 3080]
    uuid = "c5a2956d8ed3af1746ed2f76ca971a09"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 生命值消耗 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 召唤数量 : {value1}只
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 打击攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 20
    # 每秒持续攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 6
    # 持续攻击时间 : {value4}秒
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 减速持续时间 : {value5}秒
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 生命值恢复量 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # [范围信息]
    # 突进距离 : {value7}px
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    # 蜂群大小比率 : {value8}%
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)

    def vp_1(self):
        """
        [乖离 : 异界蜂群]\n
        奈雅丽在地图上时， 奈雅丽代替施放者发动技能 (不消耗生命值)\n
        蜂群最初登场时间 -0.5秒\n
        每次生命值恢复时， 额外恢复当前生命值的2%\n
        [偶尔交给奈雅丽来处理， 也不错呢。]
        """
        ...

    def vp_2(self):
        """
        [乖离 : 异界蜂群]\n
        若不存在被[乖离 : 迷雾]附身的敌人， 则无法施放\n
        被[乖离 : 迷雾]附身的敌人被撕裂， 异界蜂群从中出现\n
        - 蜂群登场间隔 -50%\n
        - 蜂群突进距离 -50%\n
        - 蜂群大小 -25%\n
        [既然奈雅丽坚持要它们来， 那就改变召唤术， 按照它们的方式来邀请吧……我好像听到远方传来了欢呼声。]
        """
        ...

# 次元 : 粒子波
# mage_male/dimension_walker/e0a072e8cef2d77893aad5f68aeed56a
# a5ccbaf5538981c6ef99b236c0a60b73/e0a072e8cef2d77893aad5f68aeed56a
class Skill36(ActiveSkill):
    """
    开启异次元裂缝， 发射强力的粒子炮。\n
    [次元边界效果]\n
    在角色前方设置异次元裂缝， 替自身发射粒子炮。\n
    [开启3个裂缝比起2个裂缝有本质上的区别， 所以万一开启失败也不要嘲笑我， 尤其是你， 奈雅丽。]
    """
    name = "次元 : 粒子波"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [350, 3080]
    uuid = "e0a072e8cef2d77893aad5f68aeed56a"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 边界能量条增加量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 粒子炮攻击力 : {value1}  x {value2}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 10
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [次元边界效果]
    # 边界能量增加量 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 粒子炮攻击力 : {value4}  x {value5}
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 20
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # [范围信息]
    # 中心范围比率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

    mode = ["强化","普通"]

    def setMode(self, mode):
        if mode == "强化":
            self.hit1 = 10
            self.hit4 = 0
        elif mode == "普通":
            self.hit1 = 0
            self.hit4 = 1


    def vp_1(self):
        """
        [次元 : 粒子波]\n
        施放时， 生成重力场， 将敌人吸附到中心位置\n
        若[次元 : 粒子风暴]为可施放的状态， 则维持重力场\n
        - 同时消耗[次元 : 粒子风暴]的冷却时间 (不额外消耗次元石)\n
        - 粒子炮结束时爆炸\n
        - 攻击力 : [次元 : 粒子风暴]次元边界效果攻击力的100%\n
        [开启多个次元之缝时， 中心位置容易出现强大的扭曲现象。 只要利用那一点点缝隙……]
        """
        ...

    def vp_2(self):
        """
        [次元 : 粒子波]\n
        分身化形出实体， 从各个次元裂缝中发射压缩的粒子炮\n
        - 多段攻击次数 -50%\n
        - 多段攻击结束后， 在中心发生强力爆炸\n
        - 总攻击力相同\n
        - 普通施放时， 可强制中断施放后僵直并施放次元系列技能\n
        以次元边界效果发动时， 边界能量恢复量变为100\n
        [如果大家都各自只开启一个次元裂缝呢？ 前提是， 其他次元的我也点头同意。]
        """
        ...

# 虚空之力
# mage_male/dimension_walker/2a0a39184de92acf1c1375e00b77404c
# a5ccbaf5538981c6ef99b236c0a60b73/2a0a39184de92acf1c1375e00b77404c
class Skill37(PassiveSkill):
    """
    边界能量条的波动数变更为最少1个、 最多3个。\n
    魔法暴击率和暴击伤害按波动数成比例增加。\n
    施放[次元边界]时， 有一定几率不消耗次元石， 此时角色上方会出现紫色图标。\n
    - [次元之乖离扫把精通]附加效果 -\n
    在装备扫把的状态下进入地下城或死亡后复活时， 增加1个波动数。\n
    [没有任何事情比不确定更加确定。]
    """
    name = "虚空之力"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 1 #TODO
    rangeLv = 3
    uuid = "2a0a39184de92acf1c1375e00b77404c"
    hasVP = False
    hasUP = False

    # 不消耗次元石的几率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # [1个波动次数]
    # 魔法暴击率增加 : {value1}%
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 暴击伤害增加率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # [2个波动次数]
    # 魔法暴击率增加 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 暴击伤害增加率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # [3个波动次数]
    # 魔法暴击率增加 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    # 暴击伤害增加率 : {value6}%
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)

    associate = [{"data":data6}]

# 乖离 : 扭曲之恐惧
# mage_male/dimension_walker/9dc8438e4572d39243c97da31c113acc
# a5ccbaf5538981c6ef99b236c0a60b73/9dc8438e4572d39243c97da31c113acc
class Skill38(ActiveSkill):
    """
    开启异次元裂缝， 强制召唤某不知名怪物的片鳞只甲。\n
    怪物利用触手攻击后引发次元爆炸。\n
    召唤时会增加2个边界能量条的波动次数。\n
    [经常与怪物战斗的人， 需要警惕自己也变成怪物。 如果你长时间关注深渊， 你会发现深渊也有东西在关注你……]
    """
    name = "乖离 : 扭曲之恐惧"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [1200, 10080]
    uuid = "9dc8438e4572d39243c97da31c113acc"
    hasVP = False
    hasUP = False

    # 怪物出现时攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    hit0 = 1
    # 触须攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 23
    # 爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 次元石获得量 : {value3}个
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)

# 次元 : 思维聚爆
# mage_male/dimension_walker/e0daa922b19cdc35de879e938361464e
# a5ccbaf5538981c6ef99b236c0a60b73/e0daa922b19cdc35de879e938361464e
class Skill39(ActiveSkill):
    """
    在被[乖离 : 迷雾]附身的敌人身边引发强力的异次元崩塌， 造成持续的伤害后爆炸。\n
    - [次元边界效果] -\n
    被击中的敌人会进入强制控制状态。 攻击过程中次元行者进入无敌状态。\n
    [说白了就是一直重复开关非常脆弱的玻璃门。]
    """
    name = "次元 : 思维聚爆"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [400, 1120]
    uuid = "e0daa922b19cdc35de879e938361464e"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 边界能量增加量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 持续攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 12
    # 最后爆炸攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # [次元边界效果]
    # 边界能量增加量 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # [范围信息]
    # 最后爆炸大小比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    mode = ["瞬爆","打满"]

    def setMode(self, mode):
        if mode == "瞬爆":
            self.hit1 = 1

    def vp_1(self):
        """
        [次元 : 思维聚爆]\n
        没有敌人被[乖离 : 迷雾]附身的状态下也可以施放该技能 (在前方250px处发动)\n
        施放过程中可以发动[次元边界]效果， 且不消耗次元石\n
        异次元崩塌的最后阶段变得更加强烈\n
        - 总攻击力相同\n
        - 最后爆炸范围 +40%\n
        [只要稍微碰一下， 它马上就会碎掉。]
        """
        ...

    def vp_2(self):
        """
        [次元 : 思维聚爆]\n
        异次元崩塌， 持续吸附次元附近的敌人\n
        - 普通施放时， 大幅增加吸附范围， 施放过程中所受伤害减少90%\n
        发动[次元边界]效果时， 异次元崩塌开始后角色可以行动\n
        - 异次元崩塌自行维持一段时间后爆炸\n
        - 无法通过跳跃键延迟发动终结攻击\n
        [要是想让它发挥威力， 就别急着关上。 不过， 要是差不多了， 就该赶紧收手。]
        """
        ...

# 乖离 : 禁锢
# mage_male/dimension_walker/5806440d21e7546d50007a5ba11f8024
# a5ccbaf5538981c6ef99b236c0a60b73/5806440d21e7546d50007a5ba11f8024
class Skill40(ActiveSkill):
    """
    奈雅丽瞬移到角色后方后， 将魔力聚集到鞭子上向前刺击。\n
    成功命中时， 奈雅丽抓取敌人并持续一段时间。\n
    [能把敌人彻底击穿这一点倒是不错， 但为什么他们第二天会对我露出笑容？]
    """
    name = "乖离 : 禁锢"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 8 #TODO
    rangeLv = 2
    cube = 3
    cd = 50
    mp = [900, 1820]
    uuid = "5806440d21e7546d50007a5ba11f8024"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 束缚时间 : {value0}秒
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 刺击攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # [范围信息]
    # 刺击距离比率 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)

    def effect(self, old, new):
        if self.vp == 1:
            self.associate = [{"type":"*skillRation","data":[0] + [-14]*self.maxLv,"skills":["乖离 : 魅魔之舞"]}]
        return super().effect(old, new)

    def vp_1(self):
        """
        [乖离 : 禁锢]\n
        [乖离 : 禁锢]命中时， 初始化[乖离 : 魅魔之舞]的冷却时间\n
        [乖离 : 禁锢]命中后， 强制中断并施放其他奈雅丽技能时， 束缚效果不消失\n
        [乖离 : 魅魔之舞]\n
        攻击力 -14%\n
        分身代替奈雅丽施放[乖离 : 魅魔之舞]\n
        [光是本尊就够难应付了， 连分身都一起捣乱……这种场面， 实在令人百感交集。]
        """
        ...

    def vp_2(self):
        """
        [乖离 : 禁锢]\n
        奈雅丽瞬间显现自身的部分力量攻击敌人\n
        施放后， 奈雅丽将回收的力量变换为不规则多面体送给次元行者\n
        - 次元石 +1个\n
        - 边界能量条的波动数变更为最大值\n
        [曾经问过奈雅丽关于她真身的事情……但她只是一直笑着， 没有回答。]
        """
        ...

# 混沌源能石
# mage_male/dimension_walker/5c45f69c9ebc7a784e994369d2cc3c66
# a5ccbaf5538981c6ef99b236c0a60b73/5c45f69c9ebc7a784e994369d2cc3c66
class Skill41(PassiveSkill):
    """
    奈雅丽给的神秘宝石， 部分技能的效果会增加或变更。\n
     [超然感知]\n
    -增加次元石持有量上限\n
    -进入地下城或复活时， 可以获得一定数量的次元石\n
    -根据边界能量条的波动次数增加技能攻击力。\n
    [乖离 : 迷雾]\n
    -不消耗生命值\n
    -无需发动动作即可施放\n
    -除了跳跃和被击状态， 其他状态下都可以发射迷雾。\n
    [乖离 : 禁忌之奈雅丽]\n
    转职系列技能命中敌人时， 增加奈雅丽的攻击速度。\n
       [冒着死亡的危险接收了这块异界宝石。 奈雅丽说为了方便我使用， 只提取了原宝石的一部分， 并进行了改进。 如果这只是一部分， 那原始的宝石该有多强大？]
    """
    name = "混沌源能石"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 1 #TODO
    rangeLv = 3
    uuid = "5c45f69c9ebc7a784e994369d2cc3c66"
    hasVP = False
    hasUP = False

    # 进入地下城时获得的次元石数量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 次元石持有量上限增加 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 1个波动次数时攻击力增加量 : {value2}%
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 2个波动次数时攻击力增加量 : {value3}%
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 3个波动次数时攻击力增加量 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 转职技能命中敌人时， 奈雅丽攻击速度增加量 : {value5}%
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    associate = [{"data":data4}]

# 次元 : 奇点
# mage_male/dimension_walker/4402c6977bf5c9b0d2febe14dc81de6c
# a5ccbaf5538981c6ef99b236c0a60b73/4402c6977bf5c9b0d2febe14dc81de6c
class Skill42(ActiveSkill):
    """
    操纵异次元领域， 生成特殊的能量地带， 然后将敌人吸附到能量地带并连续抛出。\n
    撞到地面冲击波对不可抓取的敌人造成更大伤害。\n
    若能量地带只存在无法抓取的敌人时， 则将异次元之力汇聚到能量地带中， 生成异次元水晶并攻击周围的敌人。\n
    对无法抓取的敌人不适用控制效果。\n
    [次元边界效果]\n
    在自身周围较大的范围内生成水晶地带攻击敌人。\n
    [根据奈雅丽提点的公式勉强完成了这个魔法术式， 但是过于复杂， 好像没法应用到其他术式中。 稍有不慎， 自己就有可能被吸进能量地带， 或者变成水晶……奈雅丽应该不会是想让我变成那样吧？] 
    """
    name = "次元 : 奇点"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "4402c6977bf5c9b0d2febe14dc81de6c"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 边界能量条增加量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 被抓取敌人撞击墙壁时冲击波攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 被抓取敌人撞击地面时的冲击波攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 撞击地面时冲击波对不可抓取敌人的攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 异次元水晶对不可抓取敌人的攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1
    # 异次元水晶对不可抓取敌人的爆炸攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    hit5 = 1
    # [次元边界效果]
    # 次元边界能量条增加量 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    # 水晶地带单次攻击力 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    hit7 = 0
    # 水晶地带每次爆炸攻击力 : {value8}
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)
    hit8 = 0
    # [范围信息]
    # 攻击范围比率 : {value9}%
    data9 = get_data(f'{prefix}/{uuid}', 9, lambda x = None: x)

    mode = ["强化","普通"]

    def setMode(self, mode):
        if mode == "强化":
            self.hit7 = self.hit8 = 1
            self.hit4 = self.hit5 = 0
        elif mode == "普通":
            self.hit7 = self.hit8 = 0
            self.hit4 = self.hit5 = 1

    def vp_1(self):
        """
        [次元 : 奇点]\n
        无施放动作， 立即施放\n
        普通施放时， 即使不存在敌人， 也会在能量领域生成次元水晶\n
        - 控制范围内无法抓取的敌人2秒\n
        技能范围 +30%\n
        [好不容易改良了部分术式。 虽然奈雅丽有点失望， 但这个程度已经是最好的办法了……不会吧， 你们不会还期待着别的结果吧？]
        """
        ...

    def vp_2(self):
        """
        [次元 : 奇点]\n
        普通施放时， 对无法抓取的敌人也进行相同的流程\n
        - 第1击和第2击变更为不会移动敌人， 而是通过次元力进行打击\n
        首次能量地带范围 +40%\n
        发动[次元边界]效果时， 效果变更如下\n
        - 不生成水晶地带， 而是生成能量地带\n
        - 生成能量地带时进入无敌状态\n
        - 即使能量地带范围内没有敌人， 仍继续进行流程\n
        [看起来复杂的东西， 其实答案可能简单得惊人。 不过看奈雅丽的表情， 她好像不太认同……]
        """
        ...

# 乖离 : 沉沦
# mage_male/dimension_walker/96bd070daacc6c1b81d9f24e6d77f48a
# a5ccbaf5538981c6ef99b236c0a60b73/96bd070daacc6c1b81d9f24e6d77f48a
class Skill43(ActiveSkill):
    """
    奈雅丽将异次元彼端的怪物召唤到角色前方。\n
    被召唤的怪物发出悲鸣攻击敌人， 同时敌人被吸附到怪物身边。\n
    若有敌人被[乖离 : 迷雾]所附身， 则将该敌人作为媒介召唤。 此时， 悲鸣的攻击力有所降低， 但召唤瞬间会给敌人造成巨大伤害。\n
    [有什么可以代表“永远的睡眠相当于死亡”这一说法？ 毫无疑问是摇篮曲。 至少在异次元彼端， 摇篮曲真的是用在战斗中。 当然， 我不想知道那个摇篮曲是唱给谁听的。]
    """
    name = "乖离 : 沉沦"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 8 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "96bd070daacc6c1b81d9f24e6d77f48a"
    hasVP = True
    hasUP = True
    vps = get_data(f'{prefix}/{uuid}', "vps") # noqa: E501

    # 彼端怪物每次悲鸣时攻击力 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 彼端怪物悲鸣次数 : {value1}次
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # [媒介召唤]
    # 媒介对象受到的伤害 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 彼端怪物每次悲鸣时攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 25
    # [范围信息]
    # 攻击范围比率 : {value4}%
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)

    def vp_1(self):
        """
        [乖离 : 沉沦]\n
        变更为彼端的存在爆炸后， 一次性造成伤害\n
        - 总攻击力相同\n
        召唤媒介时， 向媒介对象刻下印章， 使其即使脱离爆炸范围， 也会受到伤害\n
        攻击范围 +50%\n
        [在异次元彼端， 他们居然把这种爆炸声当成摇篮曲……实在搞不懂。]
        """
        ...

    def vp_2(self):
        """
        [乖离 : 沉沦]\n
        与以往不同外形的彼端的存在登场\n
        - 无法召唤媒介\n
        - 登场的同时悲鸣， 造成相当于变更前媒介召唤总攻击力100%的伤害\n
        - 奈雅丽看到出乎意料的存在后有些慌张， 移动到附近后通过有效方法压制对方\n
        压制过程中， 异次元彼端的怪物拼命挣扎\n
        - 对周围敌人造成相当于奈雅丽近身攻击力100%的伤害 (最多攻击10次)\n
        - 若存在被[乖离 : 迷雾]附身的敌人， 则攻击该敌人\n
        [这家伙从来没见过啊……怎么感觉越来越困……还有奈雅丽为什么慌成那样？]
        """
        ...

# 禁断之盛宴
# mage_male/dimension_walker/c9a29f5c3509b90a96d5ca9b70dc9c85
# a5ccbaf5538981c6ef99b236c0a60b73/c9a29f5c3509b90a96d5ca9b70dc9c85
class Skill44(ActiveSkill):
    """
    次元行者与奈雅丽的合击技。\n
    次元行者在天空中开启巨大的异次元之门， 攻击地面的敌人， 奈雅丽化身为泥土和迷雾笼罩地面。\n
    此时敌人会被吸附到角色身边并进入束缚状态， 同时被强制控制。\n
    - [次元边界效果] -\n
    奈雅丽不再化身为泥土和迷雾， 直接进入异次元魔法阵， 将魔法术式发动为极限状态。 \n
    开始发动瞬间按跳跃键， 可以省略次元炮击和奈雅丽落下动作， 发动简化版技能。\n
    在没有召唤奈雅丽的状态下也可以施放该技能， 但若召唤奈雅丽时， 次元边界效果下的最终一击威力将会更大。\n
    [乖离 : 禁锢]状态下施放该技能时， 会保留[乖离 : 禁锢]的强制控制效果。\n
    [恐惧缘于无知， 真实发光于谎言之中。 所以不管你喜不喜欢， 我们会一直在一起的……哈哈哈……]
    """
    name = "禁断之盛宴"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 5000]
    uuid = "c9a29f5c3509b90a96d5ca9b70dc9c85"
    hasVP = False
    hasUP = False

    # 边界能量条增加量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 奈雅丽迷雾每一击攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 10
    # 奈雅丽迷雾束缚时间 : {value2}秒
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 次元炮击每一击攻击力 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 12
    # [次元边界效果]
    # 边界能量增加量 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    # 次元炮击每一击攻击力 : {value5}
    data5 = get_data(f'{prefix}/{uuid}', 5, lambda x = None: x)
    hit5 = 18
    # 强化的次元炮击每一击攻击力 : {value6}
    data6 = get_data(f'{prefix}/{uuid}', 6, lambda x = None: x)
    hit6 = 18
    # 最终一击攻击力 : {value7}
    data7 = get_data(f'{prefix}/{uuid}', 7, lambda x = None: x)
    hit7 = 0
    # 召唤奈雅丽时最终一击攻击力 : {value8}
    data8 = get_data(f'{prefix}/{uuid}', 8, lambda x = None: x)
    hit8 = 1

    mode = ["强化全","强化简","普通"]

    def setMode(self, mode):
        if mode == "强化全":
            self.hit1 = 0
            self.hit3 = 0
            self.hit5 = 10
            self.hit6 = 17
            self.hit7 = 0
            self.hit8 = 1
        elif mode == "强化简":
            self.hit1 = 0
            self.hit3 = 0
            self.hit5 = 0
            self.hit6 = 17
            self.hit7 = 0
            self.hit8 = 1
        elif mode == "普通":
            self.hit1 = 10
            self.hit3 = 12
            self.hit5 = 0
            self.hit6 = 0
            self.hit7 = 0
            self.hit8 = 0

# 古史记忆
# mage_male/dimension_walker/ae7608b87b6e965c6bdd0b3ef4e6d63e
# a5ccbaf5538981c6ef99b236c0a60b73/ae7608b87b6e965c6bdd0b3ef4e6d63e
class Skill45(PassiveSkill):
    """
    连接乖离世界边界的古书， 记载着一些无法解析的文字。\n
    首次施放[时空壁障]时， 增加边界能量条的波动数； 未召唤奈雅丽的状态下， 召唤奈雅丽。 (若已发动[时空壁障]， 则不增加波动数)\n
    通过On/Off功能， 可以设置是否召唤奈雅丽。 增加基本攻击力和转职技能攻击力， 变更部分技能效果。\n
    [乖离 : 迷雾]\n
    变更为前方一定范围内存在敌人时可以施放。\n
    范围内存在敌人时， 追加释放黄色雾气， 附着在范围内最强的敌人身上。 (再次按技能键可以召回； 存在召回等待时间)\n
    [乖离 : 魅魔之舞]\n
    乱打或终结攻击过程中， 中断魅魔之舞发动其他奈雅丽技能时， 利用古史记忆的力量生成奈雅丽分身继续攻击。\n
    [无数与我的意志无关的“某种东西”传到脑海里， 回过神来， 竟发现这些已经转移到了纸上。 究竟想从我的身上得到什么？] 
    """
    name = "古史记忆"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "ae7608b87b6e965c6bdd0b3ef4e6d63e"
    hasVP = False
    hasUP = False

    # 基本攻击力和转职技能攻击力增加率 : {value0}%
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 首次施放[时空壁障]时，波动数增加量 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    associate = [{"data":data0}]

# 乖离 : 边缘之兽
# mage_male/dimension_walker/626cfc24770b72b5d7a24c24cda3768b
# a5ccbaf5538981c6ef99b236c0a60b73/626cfc24770b72b5d7a24c24cda3768b
class Skill46(ActiveSkill):
    """
    前方一定范围内存在敌人时， 可以施放该技能。\n
    部分解除古史记忆的封印， 使[乖离 : 迷雾]附身范围内最强大的敌人， 召唤边缘之兽。\n
    跳到现界的野兽形成完整的形态后， 向目标位置突袭， 吞噬一切。\n
    前方一定范围内存在敌人时， 可以施放该技能。\n
    若已存在被[乖离 : 迷雾]附身敌人， 则无视距离向该目标发动技能。\n
    [不要靠近角落……永远……永远……]
    """
    name = "乖离 : 边缘之兽"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [1067, 8000]
    uuid = "626cfc24770b72b5d7a24c24cda3768b"
    hasVP = False
    hasUP = False

    # 索敌距离 : {value0}px
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 索敌宽度 : {value1}px
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    # 索敌高度 : {value2}px
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    # 生命值消耗 : {value3}
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    # 突袭攻击力 : {value4}
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)
    hit4 = 1

# 未明·次元崩坏
# mage_male/dimension_walker/7a96c262533919beee21b5a666062880
# a5ccbaf5538981c6ef99b236c0a60b73/7a96c262533919beee21b5a666062880
class Skill47(ActiveSkill):
    """
    次元行者越过理性的红线， 完全解除古史记忆的封印。 世界逆转， 现世与异界发生不完整地交缠， 次元行者被拉入异界。 \n
    奈雅丽跳入异界， 从未知存在的手中拯救次元行者， 在逃跑的瞬间， 未知存在因受到奈雅丽阻碍而暴怒， 继续攻击， 使不完整的世界崩坏。\n
    未召唤奈雅丽的状态下， 也可以施放该技能； 可以在[禁断之盛宴]普通模式中施放该技能。\n
    [三次觉醒技能]\n
    使用三次觉醒技能时， 与关联的技能共享冷却时间。\n
    若关联的技能还在冷却中， 则无法使用三次觉醒技能。\n
    [“虽然这一天总会到来， 但不是现在。”奈雅丽说的这句话无法从脑海中消失。 ……总有一天必须去往那里吗？]
    """
    name = "未明·次元崩坏"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4028, 8056]
    uuid = "7a96c262533919beee21b5a666062880"
    hasVP = False
    hasUP = False

    # 边界能量增加量 : {value0}
    data0 = get_data(f'{prefix}/{uuid}', 0, lambda x = None: x)
    # 奈雅丽光线攻击力 : {value1}
    data1 = get_data(f'{prefix}/{uuid}', 1, lambda x = None: x)
    hit1 = 1
    # 未知存在攻击力 : {value2}
    data2 = get_data(f'{prefix}/{uuid}', 2, lambda x = None: x)
    hit2 = 1
    # 不完整的世界崩坏攻击力 : {value3} x {value4}
    data3 = get_data(f'{prefix}/{uuid}', 3, lambda x = None: x)
    hit3 = 4
    data4 = get_data(f'{prefix}/{uuid}', 4, lambda x = None: x)


class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'dimension_walker'
        self.nameCN = '知源·次元行者'
        self.role = 'mage_male'
        self.角色 = '魔法师(男)'
        self.职业 = '次元行者'
        self.jobId = 'a5ccbaf5538981c6ef99b236c0a60b73'
        self.jobGrowId = '92da05ec93fb43406e193ffb9a2a629b'

        self.武器选项 = ['扫把', '矛', '魔杖', '法杖', '棍棒']
        self.输出类型选项 = ['魔法固伤']
        self.输出类型 = '魔法固伤'
        self.防具精通属性 = ['智力']
        self.防具类型 = '扫把'
        self.buff = 1.922

        super().__init__(equVersion, __name__)
