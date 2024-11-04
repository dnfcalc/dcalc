from core.basic.property import CharacterProperty
from core.equipment.property import 成长词条计算
import core.equipment.entry_0.params as pa

# 固定装备：和平之翼长裤 ， 冤魂的执念上衣 ， 混沌之幕护腿 ， 死亡蚕食胸甲 ， 熔丝项链 ， 无尽的痛苦之戒 ， 暗影之迹短靴 ， 生命本源背包 ， 缥缈的知识 ， 心之潜影 ， 虚影幻息眼镜 ， 梦之呼唤 ， 摇曳的生命之水 ， 空战型 : 战术螺旋桨无人机 ， 自然灵息露珠 ， 诅咒之心 ， 生机盎然的绿宝石 ， 未知文明 - 星石 ， 不败奖牌 ， 逆流之魂灵珠 ， 和平捍卫者 ， 灵犀之音耳环 ， 未知文明 - 人面石 ， 不倦旅程护腿 ， 天才技术大师的研究服上衣 ， 高科技战术腰带 ， 守护之王者铠甲 ， 信念之喘息腰带 ， 摇曳的残影短靴 ， 大地之翼腰带 ， 高科技御敌肩甲 ， 音律的夙愿 ， 和谐之音手镯 ， 灿若繁星手镯 ， 迟钝的感知手镯 ， 温柔的旋律 ， 光学工程眼镜 ， 铭记长夜的黎明 ， 愈合伤痕的誓言 ， 爆龙王的支配 - 武力 ， 爆龙王的支配 - 恐怖 ， 吞噬本源矛 ， 吞噬本源棍棒 ， 吞噬本源魔杖 ， 吞噬本源法杖 ， 吞噬本源扫把 ， 雾之意志追随者上衣 ， 守望者之证 ， 想象力充沛的工程师衬衫 ， 机械工程学的精髓 ， 守护之坚忍 ， 穿云破雾之光
# 自定义装备：公共词条
def entry_1(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['生命值最大值 +600']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 固定装备：吞噬本源匕首 ， 吞噬本源双剑 ， 吞噬本源手杖 ， 吞噬本源苦无 ， 吞噬本源神弦弓 ， 吞噬本源玄机弓 ， 知海沉舟 ， 记录者的宝石 ， 守护之坚忍 ， 吞噬本源强攻弩 ， 吞噬本源妖影弓
# 自定义装备：公共词条
def entry_2(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['生命值最大值 +5%']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 固定装备：天才技术大师的加厚长靴 ， 天才技术大师的百宝腰带 ， 堕落的灵魂 ， 空战型 : 战术螺旋桨无人机 ， 吞噬黑暗的心脏 ， 双面星云皮大衣 ， 和谐之音手镯 ， 重奏者 ， 隐没的邪念戒指 ， 永不停歇的命运 ， 雷达战网戒指 ， 永眠前的准备 ， 胜利约定之时 ， 庇护伤痛的威严 ， 愈合伤痕的誓言 ， 爆龙王的支配 - 武力 ， 吞噬本源手套 ， 吞噬本源臂铠 ， 吞噬本源爪 ， 吞噬本源拳套 ， 吞噬本源东方棍 ， 世界的中心轴 ， 忘却之记载 ， 想象力充沛的工程师长裤 ， 机械工程学核心项链 ， 幻想骑士战靴 ， 被侵蚀的高原之精髓 ， 机械工程学的精髓
# 自定义装备：公共词条
def entry_3(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['魔法值最大值 +945']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 固定装备：金属齿轮护肩 ， 吞噬本源长刀 ， 吞噬本源小太刀 ， 吞噬本源重剑 ， 吞噬本源源力剑 ， 守望溪谷的注视 ， 守望溪谷的行动
# 自定义装备：公共词条
def entry_4(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['魔法值最大值 +5%']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 固定装备：天才技术大师的保护面罩 ， 冤魂的执念上衣 ， 混沌之幕护腿 ， 熔丝项链 ， 魔力抑制手镯 ， 子夜的圣域 ， 玉化亡灵肩甲 ， 炙热之情宝石 ， 和平捍卫者 ， 诅咒的枷锁 ， 隐匿之叹息耳环 ， 灵犀之音耳环 ， 徘徊之魄耳环 ， 轰天裂地石甲 ， 暴走之躯战靴 ， 高科技战术护腿 ， 华丽的清音护肩 ， 高科技战术指挥上衣 ， 玉化亡灵腰甲 ， 高贵的神意上衣 ， 音律的夙愿 ， 万念俱灰短靴 ， 电离掌控手镯 ， 残忍之心项链 ， 石巨人之心项链 ， 脉冲触发器 ， 风化的恶意 ， 生命的脉动 ， 骑士的赎罪 ， 温柔的旋律 ， 磁场探测者戒指 ， 隐没的邪念戒指 ， 瞬息千里戒指 ， 超小型GPS ， 机械装甲下装 ， 指引胜利的正义 ， 鲁莽而合理的作战 ， 含泪之宝石 ， 吞噬本源左轮枪 ， 吞噬本源自动手枪 ， 吞噬本源步枪 ， 吞噬本源手炮 ， 吞噬本源手弩 ， 雾之意志追随者上衣 ， 雾之意志追随者下装 ， 守望溪谷的注视 ， 传令使的祝福 ， 想象力充沛的工程师衬衫 ， 忠诚骑士腰带 ， 守望溪谷的标志 ， 穿云破雾之光
# 自定义装备：公共词条
def entry_5(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理/魔法防御力 +7000']
    if mode == 0:
        char.add_eq_params('defense',7000)
        pass
    if mode == 1:
        pass


# 固定装备：吞噬本源长枪 ， 吞噬本源战戟 ， 吞噬本源光枪 ， 吞噬本源暗矛
# 自定义装备：公共词条
def entry_6(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理/魔法防御力 +5%']
    if mode == 0:
        char.add_eq_params('defense_ratio',0.05)
        pass
    if mode == 1:
        pass


# 固定装备：灵巧的支配者护肩 ， 恐惧缠绕腰带 ， 全能主宰者之戒 ， 德卡制导装置 ， 无色冰晶耳环 ， 挖掘之王部件 ， 猎龙者之证 - 龙骨角笛 ， 未知的黄金石碑 ， 陆战型 : 战术车轮无人机 ， 猎龙者之证 - 龙心加工石 ， 脉冲之源耳环 ， 猎龙者 ， 暴走之躯战靴 ， 黑暗吞噬短靴 ， 御力装甲上衣 ， 苍龙闪影护腿 ， 沧海之覆护腿 ， 远古之法则护肩 ， 骄傲的意志腰带 ， 大地之翼腰带 ， 玉化亡灵胸甲 ， 龙食腐者 ， 天翼之守护短靴 ， 无人机战术手镯 ， 守护龙的庇护 - 慈悲 ， 迟钝的感知手镯 ， 守护龙的庇护 - 勇气 ， 浮光跃金项链 ， 骑士的赎罪 ， 守护龙的庇护 - 祝福 ， 双音交映戒指 ， 能量搜索环 ， 增援号令腰带 ， 混乱核心胸甲 ， 金属齿轮护肩 ， 战胜噩梦的捷报 ， 爆龙王的支配 - 压制 ， 终结之龙玉 ， 临界崩坏之隙 ， 知海沉舟 ， 邪恶力量侵蚀手镯 ， 雾之探索者戒指 ， 守望者之证 ， 俯瞰夜色的工程师之眼 ， 被侵蚀的神兽之泪 ， 守望溪谷的标志 ， 时间工程学的时刻 ， 永不放弃的勇气
# 自定义装备：公共词条
def entry_7(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理/魔法暴击率 +5%']
    if mode == 0:
        char.物理暴击率增加(0.05)
        char.魔法暴击率增加(0.05)
    if mode == 1:
        pass


# 固定装备：六方式脉冲肩甲 ， 金翼戒指 ， 全能主宰者之戒 ， 遥感之心项链 ， 原核之芯耳环 ， 黄昏殿堂 ， 生命的喘息 ， 黑猫头盔 ， 梵塔黑色长裤 ， 静谧之像 ， 无色冰晶耳环 ， 全息通话器 ， 千里之音手镯 ， 未知的黄金石碑 ， 诅咒之心 ， 奔涌之息宝石 ， 猎龙者 ， 苍龙闪影护腿 ， 静谧的星光腰带 ， 龙之开拓者短靴 ， 大地的践踏短靴 ， 祈愿之息短靴 ， 暗影流光战袍 ， 玉化亡灵腿甲 ， 龙食腐者 ， 动力之渊腰带 ， 无人机战术手镯 ， 收获之手 ， 浮光跃金项链 ， 超小型GPS ， 动力导航包 ， 冷静的谋略家上衣 ， 炽热的渴望之证 ， 终结永恒时光的夙愿 ， 告别过去的前进 ， 触手可及之记忆 ， 超界次元 ， 邪恶力量侵蚀手镯 ， 传令使的祝福 ， 想象力充沛的工程师长裤 ， 想象力充沛的工程师工作腰带 ， 被侵蚀的神兽之泪 ， 守护晴烟之力
# 自定义装备：公共词条
def entry_8(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +8%', '施放速度 +12%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.08)
        char.施放速度增加(0.12)
    if mode == 1:
        pass


# 固定装备：天才技术大师的加厚长靴 ， 全息通话器 ， 死亡之冠 ， 不祥的暗纹石板 ， 正义骑士面具 ， 逆流之魂灵珠 ， 万物引力耳环 ， 爆炸型 : 小型战术信号弹 ， 古老的探险家大衣 ， 不倦旅程护腿 ， 无畏的勇气短靴 ， 华丽的清音护肩 ， 静谧的星光腰带 ， 龙之开拓者短靴 ， 摇曳的残影短靴 ， 大地的践踏短靴 ， 祈愿之息短靴 ， 玉化亡灵腰甲 ， 玉化亡灵胸甲 ， 玉化亡灵腿甲 ， 终极掌控者护腿 ， 天才技术大师的百宝裤 ， 天翼之守护短靴 ， 玉化亡灵长靴 ， 电离掌控手镯 ， 五感之灵项链 ， 双音交映戒指 ， 完成型动力控制装置 ， 指引胜利的正义 ， 胜利约定之时 ， 生息之壶觞 ， 如流岁月 ， 忘却之记载 ， 雾之意志追随者下装 ， 雾之探索者腰带 ， 雾之意志追随者鞋 ， 想象力充沛的工程师工作腰带 ， 想象力充沛的工程师防护鞋 ， 封存时空的手镯 ， 压倒性之勇猛 ， 守护晴烟之力
# 自定义装备：公共词条
def entry_9(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['移动速度 +8%']
    if mode == 0:
        char.移动速度增加(0.08)
    if mode == 1:
        pass


# 固定装备：黯星项链 ， 德卡制导装置 ， 迷你电池包 ， 生命的喘息 ， 堕落的灵魂 ， 千丝萦绕腰带 ， 暗影之迹短靴 ， 黑猫头盔 ， 梵塔黑色长裤 ， 子夜的圣域 ， 千里之音手镯 ， 黎明圣杯 ， 猎龙者之证 - 龙骨角笛 ， 陆战型 : 战术车轮无人机 ， 猎龙者之证 - 龙心加工石 ， 吞噬风暴耳环 ， 脉冲之源耳环 ， 隐匿的自然生命 ， 深渊之源上衣 ， 无畏的勇气短靴 ， 屠龙者 ， 舞台的华丽 ， 望穿尽头的视线 ， 远古之法则护肩 ， 应尽之责腰带 ， 暴风骑士 ， 高科技御敌肩甲 ， 骑士的救赎 ， 守护龙的庇护 - 慈悲 ， 收获之手 ， 脉冲触发器 ， 守护龙的庇护 - 勇气 ， 闪耀的音律 ， 石巨人之枢戒指 ， 守护龙的庇护 - 祝福 ， 完成型动力控制装置 ， 光学工程眼镜 ， 冷静的谋略家上衣 ， 欢笑中的祈盼 ， 战胜噩梦的捷报 ， 爆龙王的支配 - 压制 ， 吞噬本源十字架 ， 吞噬本源念珠 ， 吞噬本源图腾 ， 吞噬本源镰刀 ， 吞噬本源战斧 ， 命运的领航标 ， 遥远之刻痕 ， 雾之意志追随者鞋 ， 想象力充沛的工程师防护鞋 ， 俯瞰夜色的工程师之眼 ， 压倒性之勇猛 ， 悲蚀之神兽面纱 ， 时间工程学的时刻 ， 永不放弃的勇气
# 自定义装备：公共词条
def entry_10(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['命中率 +10%']
    if mode == 0:
        char.命中率增加(0.1)
    if mode == 1:
        pass


# 固定装备：天才技术大师的保护面罩 ， 迷你电池包 ， 玉化亡灵肩甲 ， 黎明圣杯 ， 死亡之冠 ， 梦之呼唤 ， 灵动的慧眼 ， 吞噬风暴耳环 ， 万物引力耳环 ， 徘徊之魄耳环 ， 轰天裂地石甲 ， 舞台的华丽 ， 望穿尽头的视线 ， 高科技战术指挥上衣 ， 终极掌控者护腿 ， 天才技术大师的百宝裤 ， 玉化亡灵长靴 ， 万念俱灰短靴 ， 骑士的救赎 ， 磁场探测者戒指 ， 石巨人之枢戒指 ， 永恒的心愿 ， 炽热的渴望之证 ， 吞噬本源长刀 ， 吞噬本源小太刀 ， 吞噬本源重剑 ， 吞噬本源源力剑 ， 吞噬本源神弦弓 ， 吞噬本源玄机弓 ， 铭刻记忆之星尘 ， 如流岁月 ， 虚蚀之神兽斗篷 ， 雾之探索者腰带 ， 封存时空的手镯 ， 铭刻之誓约 ， 悲蚀之神兽面纱 ， 记录者的宝石 ， 吞噬本源强攻弩 ， 吞噬本源妖影弓
# 自定义装备：公共词条
def entry_11(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['回避率 +8%']
    if mode == 0:
        char.回避率增加(0.08)
    if mode == 1:
        pass


# 固定装备：无尽的痛苦之戒 ， 幻影之触控制面板 ， 命运的魔法箱 ， 灵动的慧眼 ， 多德卡全息图 ， 虚伪之石 ， 炙热之情宝石 ， 猎龙者之证 - 龙鳞耳环 ， 时间之念耳环 ， 隐匿之光护肩 ， 高科技战术腰带 ， 白金流光夹克 ， 冰玉之蚀肩甲 ， 白色的信念斗篷 ， 白虹贯日长裤 ， 沙漠星芒披肩 ， 白色秘境皮鞋 ， 百折不挠的梦想 ， 电磁搜索者肩甲 ， 白玉无邪腰带 ， 第二个黑桃 - 权威 ， 第一个黑桃 - 贵族 ， 第三个黑桃 - 死亡 ， 瞬息千里戒指 ， 原子核项链 ， 赛博音速长靴 ， 欢笑中的祈盼 ， 铭记长夜的黎明 ， 终结之龙玉 ， 吞噬本源短剑 ， 吞噬本源太刀 ， 吞噬本源钝器 ， 吞噬本源巨剑 ， 吞噬本源光剑 ， 临界崩坏之隙 ， 化虚为实之想象
# 自定义装备：公共词条
def entry_12(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['每分钟恢复460.2点生命值']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 固定装备：魔力抑制手镯 ， 幻影之触控制面板 ， 命运的魔法箱 ， 吞噬黑暗的心脏 ， 虚伪之石 ， 猎龙者之证 - 龙鳞耳环 ， 隐匿之叹息耳环 ， 爆炸型 : 小型战术信号弹 ， 时间之念耳环 ， 钢筋铁骨披肩 ， 深渊之源上衣 ， 白金流光夹克 ， 屠龙者 ， 白色的信念斗篷 ， 流星追月短靴 ， 白虹贯日长裤 ， 白色秘境皮鞋 ， 白玉无邪腰带 ， 第二个黑桃 - 权威 ， 重奏者 ， 无尽的愤怒项链 ， 第一个黑桃 - 贵族 ， 第三个黑桃 - 死亡 ， 雷达战网戒指 ， 增援号令腰带 ， 赛博音速长靴 ， 鲁莽而合理的作战 ， 终结永恒时光的夙愿 ， 含泪之宝石 ， 吞噬本源矛 ， 吞噬本源棍棒 ， 吞噬本源魔杖 ， 吞噬本源法杖 ， 吞噬本源扫把 ， 触手可及之记忆 ， 铭刻记忆之星尘
# 自定义装备：公共词条
def entry_13(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['每分钟恢复348点魔法值']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 固定装备：不祥的暗纹石板 ， 正义骑士面具 ， 五感之灵项链 ， 吞噬本源匕首 ， 吞噬本源双剑 ， 吞噬本源手杖 ， 吞噬本源苦无
# 自定义装备：公共词条
def entry_14(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['跳跃力 +20', '移动速度 +4%', '跳跃状态期间，移动速度 +30%']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 固定装备：未知文明 - 双子石 ， 神谕之信念 ， 绽放的自然生命 ， 蓝色自然的种子
# 自定义装备：公共词条
def entry_15(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冰属性强化 +20']
    if mode == 0:
        char.冰属性强化加成(20)
    if mode == 1:
        pass


# 固定装备：无尽的生机耳环 ， 霜云暗影长裤 ， 御雷腰带 ， 纯粹的自然秩序
# 自定义装备：公共词条
def entry_16(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['光属性强化 +20']
    if mode == 0:
        char.光属性强化加成(20)
    if mode == 1:
        pass


# 固定装备：战争之主耳环 ， 自由之翼护肩 ， 大地的馈赠上衣 ， 荒漠之界长裤 ， 侵蚀的意志护腿 ， 焰纹加固靴 ， 战士的荣耀项链
# 自定义装备：公共词条
def entry_17(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性强化 +20']
    if mode == 0:
        char.火属性强化加成(20)
    if mode == 1:
        pass


# 固定装备：晨曦的新芽耳环 ， 循环的自然之法 ， 永不破碎的信念
# 自定义装备：公共词条
def entry_18(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暗属性强化 +20']
    if mode == 0:
        char.暗属性强化加成(20)
    if mode == 1:
        pass


# 固定装备：机械装甲下装 ， 正气傲然的理念 ， 庇护伤痛的威严 ， 生息之壶觞 ， 雾之探索者项链 ， 忠诚骑士腰带 ， 被侵蚀的高原之精髓
# 自定义装备：公共词条
def entry_19(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +18']
    if mode == 0:
        char.所有属性强化加成(18)
    if mode == 1:
        pass


# 固定装备：不败奖牌 ， 战争之主耳环 ， 星灭光离腰带 ， 荒漠之界长裤 ， 残忍之心项链 ， 战士的荣耀项链 ， 吞噬本源左轮枪 ， 吞噬本源自动手枪 ， 吞噬本源步枪 ， 吞噬本源手炮 ， 吞噬本源手弩 ， 守护晴烟的意志
# 自定义装备：公共词条
def entry_20(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性抗性 +10']
    if mode == 0:
        char.火属性抗性加成(10)
    if mode == 1:
        pass


# 固定装备：未知文明 - 星石 ， 未知文明 - 双子石 ， 石巨人之心项链 ， 蓝色自然的种子 ， 吞噬本源长枪 ， 吞噬本源战戟 ， 吞噬本源光枪 ， 吞噬本源暗矛
# 自定义装备：公共词条
def entry_21(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冰属性抗性 +10']
    if mode == 0:
        char.冰属性抗性加成(10)
    if mode == 1:
        pass


# 固定装备：生机盎然的绿宝石 ， 无尽的生机耳环 ， 生命的脉动 ， 吞噬本源短剑 ， 吞噬本源太刀 ， 吞噬本源钝器 ， 吞噬本源巨剑 ， 吞噬本源光剑
# 自定义装备：公共词条
def entry_22(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['光属性抗性 +10']
    if mode == 0:
        char.光属性抗性加成(10)
    if mode == 1:
        pass


# 固定装备：自然灵息露珠 ， 晨曦的新芽耳环 ， 风化的恶意 ， 吞噬本源手套 ， 吞噬本源臂铠 ， 吞噬本源爪 ， 吞噬本源拳套 ， 吞噬本源东方棍 ， 记录者的项链
# 自定义装备：公共词条
def entry_23(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暗属性抗性 +10']
    if mode == 0:
        char.暗属性抗性加成(10)
    if mode == 1:
        pass


# 固定装备：古老的探险家大衣 ， 钢筋铁骨披肩 ， 吞噬本源十字架 ， 吞噬本源念珠 ， 吞噬本源图腾 ， 吞噬本源镰刀 ， 吞噬本源战斧
# 自定义装备：公共词条
def entry_24(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物品栏负重上限 +5kg', '生命值最大值 +300', '魔法值最大值 +473']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 固定装备：动力导航包 ， 能量搜索环 ， 正气傲然的理念 ， 超界次元 ， 世界的中心轴 ， 虚蚀之神兽斗篷 ， 雾之探索者戒指 ， 承诺誓约的腰带 ， 化虚为实之想象
# 自定义装备：公共词条
def entry_25(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性抗性 +8']
    if mode == 0:
        char.所有属性抗性加成(8)
    if mode == 1:
        pass


# 固定装备：月落星沉腰带 ， 金翼戒指 ， 遥感之心项链 ， 黯星项链 ， 自由之缚手镯 ， 黄昏殿堂 ， 高科技战术强化靴 ， 无尽的愤怒项链 ， 高科技闪影项链 ， 领域之心项链 ， 闪耀的音律 ， 原子核项链 ， 所愿之行动 ， 爆龙王的支配 - 恐怖 ， 命运的领航标 ， 遥远之刻痕 ， 机械工程学核心项链
# 自定义装备：公共词条
def entry_26(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +20', '辅助职业技能伤害 +3%']
    if mode == 0:
        char.所有属性强化加成(20)
        if char.bufferCarry:
            char.技能攻击力加成(0.03)
    if mode == 1:
        pass


# 固定装备：自由之缚手镯 ， 生命本源背包 ， 缥缈的知识 ， 心之潜影 ， 多德卡全息图 ， 奔涌之息宝石 ， 未知文明 - 人面石 ， 亘古的悬空石腰带 ， 黑暗吞噬短靴 ， 流星飞电战靴 ， 蒸汽朋克音速鞋 ， 灿若繁星手镯 ， 高科技闪影项链 ， 领域之心项链 ， 永恒的心愿 ， 告别过去的前进 ， 幻想骑士战靴
# 自定义装备：公共词条
def entry_27(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理/魔法暴击率 +7%', '所有异常状态抗性 -10%', '辅助职业技能伤害 +5%']
    if mode == 0:
        char.物理暴击率增加(0.07)
        char.魔法暴击率增加(0.07)
        char.所有异常抗性加成(-0.1)
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 耳环 ， 深潜迷航耳环
def entry_35(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +266.8%', '韧性条减少量 +10%', '束缚持续时间 +1秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 耳环 ， 深潜迷航耳环
def entry_36(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +20', '韧性条减少量 +3%']
    if mode == 0:
        char.所有属性强化加成(20)
        pass
    if mode == 1:
        pass


# 自定义装备：特殊装备专属词条
def entry_37(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '攻击机械型敌人时，技能伤害 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        if '机械' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.05, show=False)
        else:
            return '缺少机械类型敌人'


# 自定义装备：特殊装备专属词条
def entry_38(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '攻击恶魔族敌人时，技能伤害 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        if '恶魔' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.05, show=False)
        else:
            return '缺少恶魔类型敌人'


# 自定义装备：特殊装备专属词条
def entry_39(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '攻击精灵族敌人时，技能伤害 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        if '精灵' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.05, show=False)
        else:
            return '缺少精灵类型敌人'
        pass


# 自定义装备：特殊装备专属词条
def entry_40(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '攻击天使型敌人时，技能伤害 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        if '天使' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.05, show=False)
        else:
            return '缺少天使类型敌人'
        pass


# 自定义装备：特殊装备专属词条
def entry_41(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '攻击龙族类型的敌人时，技能伤害 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        if '龙族' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.05, show=False)
        else:
            return '缺少龙族类型敌人'
        pass


# 固定装备：诅咒的枷锁 ， 苍空飞羽耳环 ， 黑灵缠绕手镯
# 自定义装备：特殊装备专属词条
def entry_42(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '出血抗性 +1%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.05)
        char.异常抗性加成('出血',0.01)
        pass
    if mode == 1:
        pass


# 固定装备：石巨人之核手镯
# 自定义装备：特殊装备专属词条
def entry_43(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '中毒抗性 +1%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.05)
        char.异常抗性加成('中毒',0.01)
        pass
    if mode == 1:
        pass


# 固定装备：虚影幻息眼镜 ， 流星飞电手镯 ， 血红生命之戒
# 自定义装备：特殊装备专属词条
def entry_44(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '灼伤抗性 +1%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.05)
        char.异常抗性加成('灼伤',0.01)
        pass
    if mode == 1:
        pass


# 固定装备：生命之力皮护腕 ， 闪耀的生命之戒
# 自定义装备：特殊装备专属词条
def entry_45(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '感电抗性 +1%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.05)
        char.异常抗性加成('感电',0.01)
        pass
    if mode == 1:
        pass


# 固定装备：绿野的纯真手镯 ， 电流星散指环
# 自定义装备：特殊装备专属词条
def entry_46(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击眩晕状态的敌人时，增加15%的技能伤害，效果持续30秒。']
    if mode == 0:
        pass
    if mode == 1:
        if '眩晕' in pa.get_state_type():
            char.技能攻击力加成(part=part, x=0.15)
        else:
            return '敌人未处于眩晕状态'
        pass


# 自定义装备：特殊装备专属词条
def entry_47(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击诅咒状态的敌人时，技能伤害 +10%，效果持续30秒。']
    if mode == 0:
        pass
    if mode == 1:
        if '诅咒' in pa.get_state_type():
            char.技能攻击力加成(part=part, x=0.10)
        else:
            return '敌人未处于诅咒状态'
        pass


# 自定义装备：特殊装备专属词条
def entry_48(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击睡眠状态的敌人时，技能伤害 +15%，效果持续30秒。']
    if mode == 0:
        pass
    if mode == 1:
        if '睡眠' in pa.get_state_type():
            char.技能攻击力加成(part=part, x=0.15)
        else:
            return '敌人未处于睡眠状态'
        pass


# 自定义装备：特殊装备专属词条
def entry_49(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击束缚状态的敌人时，技能伤害 +10%，效果持续30秒。']
    if mode == 0:
        pass
    if mode == 1:
        if '束缚' in pa.get_state_type():
            char.技能攻击力加成(part=part, x=0.10)
        else:
            return '敌人未处于束缚状态'
        pass


# 固定装备：摇曳的生命之水 ， 骑士的骄傲 ， 永不停歇的命运 ， 信守誓约的步伐
# 自定义装备：特殊装备专属词条
def entry_50(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['@[冰冻打击]@', '攻击冰冻状态的敌人时，技能伤害 +15%，效果持续30秒。']
    if mode == 0:
        pass
    if mode == 1:
        if char.get_eq_params('ice_attack_rate') > 0 and '冰冻' in pa.state_type:
            char.技能攻击力加成(0.15*char.get_eq_params('ice_attack_rate'))
        elif '冰冻' in pa.get_state_type():
            char.技能攻击力加成(part=part, x=0.15)
        else:
            return '敌人未处于冰冻状态'
        pass


# 自定义装备：特殊装备专属词条
def entry_51(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击减速状态的敌人时，技能伤害 +10%，效果持续30秒。 ']
    if mode == 0:
        pass
    if mode == 1:
        if '减速' in pa.get_state_type():
            char.技能攻击力加成(part=part, x=0.10)
        else:
            return '敌人未处于减速状态'
        pass


# 固定装备：绽放的神秘之花
# 自定义装备：特殊装备专属词条
def entry_52(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击失明状态的敌人时，增加10%的技能伤害，效果持续30秒。']
    if mode == 0:
        pass
    if mode == 1:
        if '失明' in pa.get_state_type():
            char.技能攻击力加成(part=part, x=0.10)
        else:
            return '敌人未处于失明状态'
        pass


# 固定装备：电弧爆源手镯 ， 原核之芯耳环
# 自定义装备：特殊装备专属词条
def entry_53(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['@[石化打击]@', '攻击石化状态的敌人时，技能伤害 +15%，效果持续30秒。']
    if mode == 0:
        pass
    if mode == 1:
        if '石化' in pa.get_state_type():
            char.技能攻击力加成(part=part, x=0.15)
        elif '石化' in pa.state_type:
            char.技能攻击力加成(0.15*char.get_eq_params('stone_attack_rate'))
        else:
            return '敌人未处于石化状态'
        pass


# 自定义装备：特殊装备专属词条
def entry_54(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击混乱状态的敌人时，技能伤害 +10%，效果持续30秒。 ']
    if mode == 0:
        pass
    if mode == 1:
        if '混乱' in pa.get_state_type():
            char.技能攻击力加成(part=part, x=0.10)
        else:
            return '敌人未处于混乱状态'
        pass


# 自定义装备：特殊装备专属词条
def entry_55(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['出血伤害 +5%']
    if mode == 0:
        char.异常增伤('出血', 0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：特殊装备专属词条
def entry_56(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['中毒伤害 +5%']
    if mode == 0:
        char.异常增伤('中毒', 0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：特殊装备专属词条
def entry_57(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤伤害 +5%']
    if mode == 0:
        char.异常增伤('灼伤', 0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：特殊装备专属词条
def entry_58(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['感电伤害 +5%']
    if mode == 0:
        char.异常增伤('感电', 0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：特殊装备专属词条
def entry_59(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，使敌人进入灼伤状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '灼伤' not in pa.get_state_type():
            pa.state_type.append('灼伤')
        char.异常时间['灼伤'][3] = min(char.异常时间['灼伤'][3],3)
        pass
    if mode == 1:
        pass


# 固定装备：查理的面具
# 自定义装备：特殊装备专属词条
def entry_60(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，使敌人进入中毒状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '中毒' not in pa.get_state_type():
            pa.state_type.append('中毒')
        char.异常时间['中毒'][3] = min(char.异常时间['中毒'][3],3)
        pass
    if mode == 1:
        pass


# 固定装备：苍空飞羽耳环 ， 查理的面具
# 自定义装备：特殊装备专属词条
def entry_61(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，使敌人进入出血状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '出血' not in pa.get_state_type():
            pa.state_type.append('出血')
        char.异常时间['出血'][3] = min(char.异常时间['出血'][3],3)
        pass
    if mode == 1:
        pass


# 固定装备：挖掘之王部件
# 自定义装备：特殊装备专属词条
def entry_62(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，使敌人进入感电状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '感电' not in pa.get_state_type():
            pa.state_type.append('感电')
        char.异常时间['感电'][3] = min(char.异常时间['感电'][3],3)
        pass
    if mode == 1:
        pass


# 自定义装备：特殊装备专属词条
def entry_63(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，使敌人进入冰冻状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '冰冻' not in pa.get_state_type():
            pa.state_type.append('冰冻')
            char.异常时间['冰冻'][3] = min(char.异常时间['冰冻'][3],3)
        pass
    if mode == 1:
        pass


# 自定义装备：特殊装备专属词条
def entry_64(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，使敌人进入减速状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '减速' not in pa.get_state_type():
            pa.state_type.append('减速')
        pass
    if mode == 1:
        pass


# 自定义装备：特殊装备专属词条
def entry_65(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，使敌人进入眩晕状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '眩晕' not in pa.get_state_type():
            pa.state_type.append('眩晕')
        pass
    if mode == 1:
        pass


# 自定义装备：特殊装备专属词条
def entry_66(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，使敌人进入诅咒状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '诅咒' not in pa.get_state_type():
            pa.state_type.append('诅咒')
        pass
    if mode == 1:
        pass


# 自定义装备：特殊装备专属词条
def entry_67(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，使敌人进入失明状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '失明' not in pa.get_state_type():
            pa.state_type.append('失明')
        pass
    if mode == 1:
        pass


# 自定义装备：特殊装备专属词条
def entry_68(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，使敌人进入石化状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '石化' not in pa.get_state_type():
            pa.state_type.append('石化')
        pass
    if mode == 1:
        pass


# 自定义装备：特殊装备专属词条
def entry_69(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，使敌人进入睡眠状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '睡眠' not in pa.get_state_type():
            pa.state_type.append('睡眠')
        pass
    if mode == 1:
        pass


# 自定义装备：特殊装备专属词条
def entry_70(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，使敌人进入混乱状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '混乱' not in pa.get_state_type():
            pa.state_type.append('混乱')
        pass
    if mode == 1:
        pass


# 自定义装备：特殊装备专属词条
def entry_71(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，使敌人进入束缚状态10秒。 (冷却时间3秒)']
    if mode == 0:
        if '束缚' not in pa.get_state_type():
            pa.state_type.append('束缚')
        pass
    if mode == 1:
        pass


# 固定装备：静谧之像
# 自定义装备：特殊装备专属词条
def entry_72(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，进入霸体状态，效果持续30秒。 (冷却时间8秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 自定义装备：特殊装备专属词条
def entry_73(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '物理/魔法防御力 +5000']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.05)
        char.add_eq_params('defense',5000)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 戒指 ， 深潜迷航导航环
def entry_74(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理/魔法暴击率 +20%']
    if mode == 0:
        char.暴击率增加(0.2)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 戒指 ， 深潜迷航导航环
def entry_75(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放技能消耗10个以上无色小晶块时，技能冷却时间恢复速度增加30%，效果持续30秒。 (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.3, excName=char.觉醒技能)


# 自定义装备：首饰专属词条
def entry_76(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['出血抗性 +20%', '物理/魔法防御力 +4000']
    if mode == 0:
        char.异常抗性加成('出血', 0.2)
        char.add_eq_params('defense',4000)
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_77(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['中毒抗性 +20%', '物理/魔法防御力 +4000']
    if mode == 0:
        char.异常抗性加成('中毒', 0.2)
        char.add_eq_params('defense',4000)
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_78(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤抗性 +20%', '物理/魔法防御力 +4000']
    if mode == 0:
        char.异常抗性加成('灼伤', 0.2)
        char.add_eq_params('defense',4000)
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_79(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['感电抗性 +20%', '物理/魔法防御力 +4000']
    if mode == 0:
        char.异常抗性加成('感电', 0.2)
        char.add_eq_params('defense',4000)
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_80(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冰冻抗性 +20%', '物理/魔法防御力 +4000']
    if mode == 0:
        char.异常抗性加成('冰冻', 0.2)
        char.add_eq_params('defense',4000)
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_81(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['减速抗性 +20%', '物理/魔法防御力 +4000']
    if mode == 0:
        char.异常抗性加成('减速', 0.2)
        char.add_eq_params('defense',4000)
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_82(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['眩晕抗性 +20%', '物理/魔法防御力 +4000']
    if mode == 0:
        char.异常抗性加成('眩晕', 0.2)
        char.add_eq_params('defense',4000)
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_83(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['诅咒抗性 +20%', '物理/魔法防御力 +4000']
    if mode == 0:
        char.异常抗性加成('诅咒', 0.2)
        char.add_eq_params('defense',4000)
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_84(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['失明抗性 +20%', '物理/魔法防御力 +4000']
    if mode == 0:
        char.异常抗性加成('失明', 0.2)
        char.add_eq_params('defense',4000)
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_85(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['石化抗性 +20%', '物理/魔法防御力 +4000']
    if mode == 0:
        char.异常抗性加成('石化', 0.2)
        char.add_eq_params('defense',4000)
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_86(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['睡眠抗性 +20%', '物理/魔法防御力 +4000']
    if mode == 0:
        char.异常抗性加成('睡眠', 0.2)
        char.add_eq_params('defense',4000)
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_87(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['混乱抗性 +20%', '物理/魔法防御力 +4000']
    if mode == 0:
        char.异常抗性加成('混乱', 0.2)
        char.add_eq_params('defense',4000)
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_88(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['束缚抗性 +20%', '物理/魔法防御力 +4000']
    if mode == 0:
        char.异常抗性加成('束缚', 0.2)
        char.add_eq_params('defense',4000)
    if mode == 1:
        pass


# 固定装备：血色结晶戒指
# 自定义装备：首饰专属词条
def entry_89(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%', '出血持续时间 -10%']
    if mode == 0:
        char.异常时间['出血'][2] -= 0.1
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_90(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%', '中毒持续时间 -10%']
    if mode == 0:
        char.异常时间['中毒'][2] -= 0.1
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 固定装备：血红生命之戒
# 自定义装备：首饰专属词条
def entry_91(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%', '灼伤持续时间 -10%']
    if mode == 0:
        char.异常时间['灼伤'][2] -= 0.1
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 固定装备：闪耀的生命之戒
# 自定义装备：首饰专属词条
def entry_92(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%', '感电持续时间 -10%']
    if mode == 0:
        char.异常时间['感电'][2] -= 0.1
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 固定装备：骑士的骄傲
# 自定义装备：首饰专属词条
def entry_93(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%', '冰冻持续时间 +2秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_94(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%', '减速持续时间 +2秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 固定装备：绿野的纯真手镯 ， 电流星散指环
# 自定义装备：首饰专属词条
def entry_95(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%', '眩晕持续时间 +2秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_96(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%', '诅咒持续时间 +2秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 固定装备：绽放的神秘之花
# 自定义装备：首饰专属词条
def entry_97(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%', '失明持续时间 +2秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 固定装备：电弧爆源手镯
# 自定义装备：首饰专属词条
def entry_98(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%', '石化持续时间 +2秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_99(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%', '睡眠持续时间 +2秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_100(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%', '混乱持续时间 +2秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_101(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%', '束缚持续时间 +2秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 固定装备：石巨人之核手镯
# 自定义装备：首饰专属词条
def entry_102(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['中毒伤害 +10%']
    if mode == 0:
        char.异常增伤('中毒', 0.1)
    if mode == 1:
        pass


# 固定装备：流星飞电手镯
# 自定义装备：首饰专属词条
def entry_103(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤伤害 +10%']
    if mode == 0:
        char.异常增伤('灼伤', 0.1)
    if mode == 1:
        pass


# 固定装备：生命之力皮护腕
# 自定义装备：首饰专属词条
def entry_104(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['感电伤害 +10%']
    if mode == 0:
        char.异常增伤('感电', 0.1)
    if mode == 1:
        pass


# 固定装备：黑灵缠绕手镯 ， 血色结晶戒指
# 自定义装备：首饰专属词条
def entry_105(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['出血伤害 +10%']
    if mode == 0:
        char.异常增伤('出血', 0.1)
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_106(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '攻击人型敌人时，技能伤害 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        if '人型' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.05, show=False)
        else:
            return '缺少人型类型敌人'
        pass


# 自定义装备：首饰专属词条
def entry_107(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '攻击野兽型敌人时，技能伤害 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        if '野兽' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.05, show=False)
        else:
            return '缺少野兽类型敌人'
        pass


# 自定义装备：首饰专属词条
def entry_108(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '攻击植物型敌人时，技能伤害 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        if '植物' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.05, show=False)
        else:
            return '缺少植物类型敌人'
        pass


# 自定义装备：首饰专属词条
def entry_109(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '攻击不死族敌人时，技能伤害 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        if '不死' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.05, show=False)
        else:
            return '缺少不死类型敌人'
        pass


# 自定义装备：首饰专属词条
def entry_110(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '攻击昆虫型敌人时，技能伤害 +5%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        if '昆虫' in pa.enemy_type:
            char.技能攻击力加成(part=part, x=0.05, show=False)
        else:
            return '缺少昆虫类型敌人'
        pass


# 固定装备：雾之探索者项链
# 自定义装备：首饰专属词条
def entry_111(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['前冲时，赋予30秒的霸体护甲。 (冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_112(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['跳跃时，获得30秒的霸体护甲。 (冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 头肩 ， 深潜迷航气囊
def entry_113(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['光属性强化 +40']
    if mode == 0:
        char.光属性强化加成(40)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 头肩 ， 深潜迷航气囊
def entry_114(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +415.0%', '所有速度 +20%']
    if mode == 0:
        char.所有速度增加(part=part, x=0.2)
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 头肩 ， 深潜迷航气囊
def entry_115(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '受到总生命值10%以上的伤害时，生成相当于生命值最大值30%的保护罩，效果持续20秒。 (冷却时间15秒)']
    if mode == 0:
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.3)
        char.技能攻击力加成(0.06)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 腰带 ， 深潜迷航腰带
def entry_116(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +30%', '施放速度 +45%', '移动速度 +10%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.3)
        char.施放速度增加(0.45)
        char.移动速度增加(0.1)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 腰带 ， 深潜迷航腰带
def entry_117(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +415.0%']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 腰带 ， 深潜迷航腰带
def entry_118(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤伤害 +15%', '物理/魔法防御力 +2000']
    if mode == 0:
        char.异常增伤('灼伤', 0.15)
        char.add_eq_params('defense',2000)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 腰带 ， 深潜迷航腰带
def entry_119(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['出血伤害 +15%', '物理/魔法防御力 +2000']
    if mode == 0:
        char.异常增伤('出血', 0.15)
        char.add_eq_params('defense',2000)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 腰带 ， 深潜迷航腰带
def entry_120(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['感电伤害 +15%', '物理/魔法防御力 +2000']
    if mode == 0:
        char.异常增伤('感电', 0.15)
        char.add_eq_params('defense',2000)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 腰带 ， 深潜迷航腰带
def entry_121(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['中毒伤害 +15%', '物理/魔法防御力 +2000']
    if mode == 0:
        char.异常增伤('中毒', 0.15)
        char.add_eq_params('defense',2000)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 鞋 ， 深潜迷航长靴
def entry_122(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['移动速度 +30%']
    if mode == 0:
        char.移动速度增加(0.3)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 鞋 ， 深潜迷航长靴
def entry_123(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '火属性强化 +25']
    if mode == 0:
        char.火属性强化加成(25)
        char.技能攻击力加成(0.04)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 鞋 ， 深潜迷航长靴
def entry_124(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '冰属性强化 +25']
    if mode == 0:
        char.冰属性强化加成(25)
        char.技能攻击力加成(0.04)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 鞋 ， 深潜迷航长靴
def entry_125(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '光属性强化 +25']
    if mode == 0:
        char.光属性强化加成(25)
        char.技能攻击力加成(0.04)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 鞋 ， 深潜迷航长靴
def entry_126(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '暗属性强化 +25']
    if mode == 0:
        char.暗属性强化加成(25)
        char.技能攻击力加成(0.04)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 鞋 ， 深潜迷航长靴
def entry_127(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '所有速度 +20%']
    if mode == 0:
        char.技能攻击力加成(0.05)
        char.攻击速度增加(part=part, x=0.2)
        char.施放速度增加(0.2)
        char.移动速度增加(0.2)
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_128(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['15级技能范围 +15%', '15级技能攻击力 +5%']
    if mode == 0:
        char.技能倍率加成(15, 15, 0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_129(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['20级技能范围 +15%', '20技能攻击力 +5%']
    if mode == 0:
        char.技能倍率加成(20, 20, 0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_130(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['25级技能范围 +15%', '25级技能攻击力 +5%']
    if mode == 0:
        char.技能倍率加成(25, 25, 0.05)
        pass
    if mode == 1:
        pass


# 固定装备：坚忍骑士肩甲
# 自定义装备：防具专属词条
def entry_131(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['30级技能范围 +15%', '30级技能攻击力 +5%']
    if mode == 0:
        char.技能倍率加成(30, 30, 0.05)
        pass
    if mode == 1:
        pass


# 固定装备：坚忍骑士肩甲
# 自定义装备：防具专属词条
def entry_132(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['35级技能范围 +15%', '35级技能攻击力 +5%']
    if mode == 0:
        char.技能倍率加成(35, 35, 0.05)
        pass
    if mode == 1:
        pass


# 固定装备：挺进之气势
# 自定义装备：防具专属词条
def entry_133(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['40级技能范围 +15%', '40级技能攻击力 +5%']
    if mode == 0:
        char.技能倍率加成(40, 40, 0.05)
        pass
    if mode == 1:
        pass


# 固定装备：挺进之气势
# 自定义装备：防具专属词条
def entry_134(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['45级技能范围 +15%', '45级技能攻击力 +5%']
    if mode == 0:
        char.技能倍率加成(45, 45, 0.05)
        pass
    if mode == 1:
        pass


# 固定装备：对敌之慎重
# 自定义装备：防具专属词条
def entry_135(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['60级技能范围 +15%', '60级技能攻击力 +5%']
    if mode == 0:
        char.技能倍率加成(60, 60, 0.05)
        pass
    if mode == 1:
        pass


# 固定装备：对敌之慎重
# 自定义装备：防具专属词条
def entry_136(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['70级技能范围 +15%', '70级技能攻击力 +5%']
    if mode == 0:
        char.技能倍率加成(70, 70, 0.05)
        pass
    if mode == 1:
        pass


# 固定装备：坚定骑士护腿
# 自定义装备：防具专属词条
def entry_137(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['75级技能范围 +15%', '75级技能攻击力 +5%']
    if mode == 0:
        char.技能倍率加成(75, 75, 0.05)
        pass
    if mode == 1:
        pass


# 固定装备：坚定骑士护腿
# 自定义装备：防具专属词条
def entry_138(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['80级技能范围 +15%', '80级技能攻击力 +5%']
    if mode == 0:
        char.技能倍率加成(80, 80, 0.05)
        pass
    if mode == 1:
        pass


# 固定装备：耀武之威护肩 ， 隐匿之光护肩 ， 信念之喘息腰带
# 自定义装备：防具专属词条
def entry_139(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['每存在1名出血状态的对象，攻击强化 +71.2% (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        num = min(5, (pa.enemy_num + (5 if char.check_equ_by_name("混乱核心胸甲") else 0)) *
                  (1 if '出血' in pa.get_state_type() else 0) + (1 if '出血' in pa.own_type else 0))
        char.攻击强化加成(params[0] * num)
        if num < 5:
            return '缺少{}名出血的对象'.format(5-num)


# 固定装备：亘古的悬空石腰带 ， 沧海之覆护腿 ， 冰玉之蚀肩甲
# 自定义装备：防具专属词条
def entry_140(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['每存在1名中毒状态的对象，攻击强化 +71.2% (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        num = min(5, (pa.enemy_num + (5 if char.check_equ_by_name("混乱核心胸甲") else 0)) *
                  (1 if '中毒' in pa.get_state_type() else 0) + (1 if '中毒' in pa.own_type else 0))
        char.攻击强化加成(params[0] * num)
        if num < 5:
            return '缺少{}名中毒的对象'.format(5-num)


# 固定装备：自由之翼护肩 ， 隐匿的自然生命 ， 御力装甲上衣 ， 大地的馈赠上衣 ， 沙漠星芒披肩 ， 焰纹加固靴 ， 永眠前的准备 ， 守护晴烟的意志 ， 信守誓约的步伐
# 自定义装备：防具专属词条
def entry_141(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['每存在1名灼伤状态的对象，攻击强化 +71.2% (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        num = min(5, (pa.enemy_num + (5 if char.check_equ_by_name("混乱核心胸甲") else 0)) *
                  (1 if '灼伤' in pa.get_state_type() else 0) + (1 if '灼伤' in pa.own_type else 0))
        char.攻击强化加成(params[0] * num)
        if num < 5:
            return '缺少{}名灼伤的对象'.format(5-num)


# 固定装备：御雷腰带 ， 流星飞电战靴 ， 纯粹的自然秩序 ， 骄傲的意志腰带 ， 电磁搜索者肩甲
# 自定义装备：防具专属词条
def entry_142(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['每存在1名感电状态的对象，攻击强化 +71.2% (最多叠加5次)']
    if mode == 0:
        pass
    if mode == 1:
        num = min(5, (pa.enemy_num + (5 if char.check_equ_by_name("混乱核心胸甲") else 0)) *
                  (1 if '感电' in pa.get_state_type() else 0) + (1 if '感电' in pa.own_type else 0))
        char.攻击强化加成(params[0] * num)
        if num < 5:
            return '缺少{}名感电的对象'.format(5-num)


# 固定装备：绽放的自然生命
# 自定义装备：防具专属词条
def entry_143(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +133.4%', '冰冻持续时间 +3秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_144(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +133.4%', '减速持续时间 +3秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_145(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +133.4%', '眩晕持续时间 +3秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 固定装备：暗影流光战袍
# 自定义装备：防具专属词条
def entry_146(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +133.4%', '诅咒持续时间 +3秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 固定装备：循环的自然之法
# 自定义装备：防具专属词条
def entry_147(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +133.4%', '失明持续时间 +3秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 固定装备：六方式脉冲肩甲 ， 月落星沉腰带 ， 蒸汽朋克音速鞋
# 自定义装备：防具专属词条
def entry_148(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +133.4%', '石化持续时间 +3秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_149(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +133.4%', '睡眠持续时间 +3秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_150(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +133.4%', '混乱持续时间 +3秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_151(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +133.4%', '束缚持续时间 +3秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 固定装备：和平之翼长裤 ， 灵巧的支配者护肩 ， 死亡蚕食胸甲 ， 恐惧缠绕腰带 ， 高科技战术强化靴 ， 应尽之责腰带 ， 暴风骑士 ， 动力之渊腰带 ， 混乱核心胸甲 ， 所愿之行动 ， 承诺誓约的腰带 ， 记录者的项链 ， 勇敢骑士甲胄 ， 铭刻之誓约
# 自定义装备：防具专属词条
def entry_152(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能魔法值消耗量 -7%']
    if mode == 0:
        char.MP消耗量加成(-0.07)
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_153(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +355.7%']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 固定装备：星灭光离腰带 ， 侵蚀的意志护腿
# 自定义装备：防具专属词条
def entry_154(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性抗性 +20']
    if mode == 0:
        char.火属性抗性加成(20)
        pass
    if mode == 1:
        pass


# 固定装备：神谕之信念
# 自定义装备：防具专属词条
def entry_155(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冰属性抗性 +20']
    if mode == 0:
        char.冰属性抗性加成(20)
        pass
    if mode == 1:
        pass


# 固定装备：霜云暗影长裤
# 自定义装备：防具专属词条
def entry_156(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['光属性抗性 +20']
    if mode == 0:
        char.光属性抗性加成(20)
    if mode == 1:
        pass


# 固定装备：永不破碎的信念
# 自定义装备：防具专属词条
def entry_157(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暗属性抗性 +20']
    if mode == 0:
        char.暗属性抗性加成(20)
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_158(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['正面被攻击时，物理/魔法所受伤害 -20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_159(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['被背击时，物理/魔法所受伤害 -20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 固定装备：澎湃之心上衣 ， 高科技战术护腿 ， 百折不挠的梦想
# 自定义装备：防具专属词条
def entry_160(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['被破招时，物理/魔法所受伤害 -20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 固定装备：高贵的神意上衣
# 自定义装备：防具专属词条
def entry_161(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['被非破招攻击时，物理/魔法所受伤害 -20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 固定装备：极魂之驱上衣 ， 天才技术大师的研究服上衣 ， 澎湃之心上衣 ， 耀武之威护肩 ， 守护之王者铠甲 ， 勇敢骑士甲胄
# 自定义装备：防具专属词条
def entry_162(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，恢复2200点生命值。 (冷却时间1秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 固定装备：天才技术大师的百宝腰带 ， 千丝萦绕腰带 ， 极魂之驱上衣 ， 流星追月短靴 ， 双面星云皮大衣 ， 守望溪谷的行动
# 自定义装备：防具专属词条
def entry_163(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，恢复3500点魔法值。 (冷却时间1秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_164(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['被攻击时，进入霸体状态30秒。 (冷却时间5秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵手镯 ， 领域之主 - 手镯
def entry_165(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +444.6%', '物理/魔法防御力 +5000']
    if mode == 0:
        char.攻击强化加成(params[0])
        char.add_eq_params('defense',5000)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵手镯 ， 领域之主 - 手镯
def entry_166(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理/魔法所受伤害 -14%']
    if mode == 0:
        char.add_eq_params('hurted_ratio',0.14)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵手镯 ， 领域之主 - 手镯
def entry_167(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +30%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.3)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵手镯 ， 领域之主 - 手镯
def entry_168(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放速度 +45%']
    if mode == 0:
        char.施放速度增加(0.45)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵手镯 ， 领域之主 - 手镯
def entry_169(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有异常状态抗性 +20%']
    if mode == 0:
        char.所有异常抗性加成(0.2)
    if mode == 1:
        pass


# 自定义装备：恩特精灵手镯 ， 领域之主 - 手镯
def entry_170(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理/魔法所受伤害 -25%']
    if mode == 0:
        char.add_eq_params('hurted_ratio',0.25)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵项链 ， 领域之主 - 项链
def entry_171(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['生命值最大值 +1200']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵项链 ， 领域之主 - 项链
def entry_172(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['魔法值最大值 +1890']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵项链 ， 领域之主 - 项链
def entry_173(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性强化 +35', '所有异常状态抗性 -10%']
    if mode == 0:
        char.火属性强化加成(35)
        char.所有异常抗性加成(-0.1)
    if mode == 1:
        pass


# 自定义装备：恩特精灵项链 ， 领域之主 - 项链
def entry_174(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冰属性强化 +35', '所有异常状态抗性 -10%']
    if mode == 0:
        char.冰属性强化加成(35)
        char.所有异常抗性加成(-0.1)
    if mode == 1:
        pass


# 自定义装备：恩特精灵项链 ， 领域之主 - 项链
def entry_175(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['光属性强化 +35', '所有异常状态抗性 -10%']
    if mode == 0:
        char.光属性强化加成(35)
        char.所有异常抗性加成(-0.1)
    if mode == 1:
        pass


# 自定义装备：恩特精灵项链 ， 领域之主 - 项链
def entry_176(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暗属性强化 +35', '所有异常状态抗性 -10%']
    if mode == 0:
        char.暗属性强化加成(35)
        char.所有异常抗性加成(-0.1)
    if mode == 1:
        pass


# 自定义装备：恩特精灵戒指 ， 领域之主 - 戒指
def entry_177(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['将伤害的10%转换为中毒伤害', '中毒抗性 +10%']
    if mode == 0:
        if '中毒' not in pa.get_state_type():
            pa.state_type.append("中毒")
        char.伤害类型转化('直伤', '中毒', 0.1)
        char.异常抗性加成('中毒', 0.1)
    if mode == 1:
        pass


# 自定义装备：恩特精灵戒指 ， 领域之主 - 戒指
def entry_178(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['将伤害的10%转换为灼伤伤害', '灼伤抗性 +10%']
    if mode == 0:
        if '灼伤' not in pa.get_state_type():
            pa.state_type.append("灼伤")
        char.伤害类型转化('直伤', '灼伤', 0.1)
        char.异常抗性加成('灼伤', 0.1)
    if mode == 1:
        pass


# 自定义装备：恩特精灵戒指 ， 领域之主 - 戒指
def entry_179(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['将伤害的10%转换为感电伤害', '感电抗性 +10%']
    if mode == 0:
        if '感电' not in pa.get_state_type():
            pa.state_type.append("感电")
        char.伤害类型转化('直伤', '感电', 0.1)
        char.异常抗性加成('感电', 0.1)
    if mode == 1:
        pass


# 自定义装备：恩特精灵戒指 ， 领域之主 - 戒指
def entry_180(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['将伤害的10%转换为出血伤害', '出血抗性 +10%']
    if mode == 0:
        if '出血' not in pa.get_state_type():
            pa.state_type.append("出血")
        char.伤害类型转化('直伤', '出血', 0.1)
        char.异常抗性加成('出血', 0.1)
    if mode == 1:
        pass


# 自定义装备：恩特精灵戒指 ， 领域之主 - 戒指
def entry_181(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%', '生命值最大值 +600']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵戒指 ， 领域之主 - 戒指
def entry_182(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性抗性数值之和高于250时，中毒伤害 +15%。']
    if mode == 0:
        pass
    if mode == 1:
        # 抗性判断
        抗性 = sum([char.火属性抗性(), char.冰属性抗性(), char.光属性抗性(), char.暗属性抗性()])
        if 抗性 >= 250:
            char.异常增伤('中毒', 0.15)
        else:
            return '所有属性抗性之和缺少{}点'.format(250-抗性)


# 自定义装备：森林之魔女手镯 ， 领域之主 - 手镯
def entry_183(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性强化 +40', '生命值最大值 +200', '辅助职业技能伤害 +7%']
    if mode == 0:
        char.火属性强化加成(40)
        if char.bufferCarry:
            char.技能攻击力加成(0.07)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女手镯 ， 领域之主 - 手镯
def entry_184(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冰属性强化 +40', '生命值最大值 +200', '辅助职业技能伤害 +7%']
    if mode == 0:
        char.冰属性强化加成(40)
        if char.bufferCarry:
            char.技能攻击力加成(0.07)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女手镯 ， 领域之主 - 手镯
def entry_185(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['光属性强化 +40', '生命值最大值 +200', '辅助职业技能伤害 +7%']
    if mode == 0:
        char.光属性强化加成(40)
        if char.bufferCarry:
            char.技能攻击力加成(0.07)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女手镯 ， 领域之主 - 手镯
def entry_186(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暗属性强化 +40', '生命值最大值 +200', '辅助职业技能伤害 +7%']
    if mode == 0:
        char.暗属性强化加成(40)
        if char.bufferCarry:
            char.技能攻击力加成(0.07)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女手镯 ， 领域之主 - 手镯
def entry_187(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['中毒伤害 +15%', '生命值最大值 +300']
    if mode == 0:
        char.异常增伤('中毒', 0.15)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女手镯 ， 领域之主 - 手镯
def entry_188(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['将伤害的30%转换为感电伤害', '感电抗性 +40%']
    if mode == 0:
        if '感电' not in pa.get_state_type():
            pa.state_type.append("感电")
        char.异常抗性加成('感电', 0.4)
        char.伤害类型转化('直伤', '感电', 0.3)
    if mode == 1:
        pass


# 自定义装备：森林之魔女项链 ， 领域之主 - 项链
def entry_189(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '进入贵族机要地下城时，技能伤害 +10%', '辅助职业技能伤害 +2%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        if '[贵族机要]' in pa.dungeons_type:
            char.技能攻击力加成(part=part, x=0.10)
        if char.bufferCarry:
            char.技能攻击力加成(0.02)


# 自定义装备：森林之魔女项链 ， 领域之主 - 项链
def entry_190(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['异常状态持续时间 +20%', '攻击时，使敌人进入出血、中毒、灼伤、感电状态中的1种异常状态10秒。 (冷却时间2秒)', '辅助职业技能伤害 +4%']
    if mode == 0:
        for i in ['出血', '灼伤', '中毒', '感电']:
            char.异常时间[i][2] += 0.2
            if i not in pa.get_state_type():
                pa.state_type.append(i)
            char.异常时间[i][3] = min(char.异常时间[i][3],2)
        if char.bufferCarry:
            char.技能攻击力加成(0.04)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女项链 ， 领域之主 - 项链
def entry_191(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['出血伤害 +15%', '生命值最大值 +300']
    if mode == 0:
        char.异常增伤('出血', 0.15)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女项链 ， 领域之主 - 项链
def entry_192(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['移动速度 +40%', '辅助职业技能伤害 +4%']
    if mode == 0:
        char.移动速度增加(0.4)
        if char.bufferCarry:
            char.技能攻击力加成(0.04)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女项链 ， 领域之主 - 项链
def entry_193(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有速度 +10%', '中毒抗性 +40%', '辅助职业技能伤害 +4%']
    if mode == 0:
        char.异常抗性加成('中毒', 0.4)
        char.攻击速度增加(part=part, x=0.1)
        char.施放速度增加(0.1)
        char.移动速度增加(0.1)
        if char.bufferCarry:
            char.技能攻击力加成(0.04)
    if mode == 1:
        pass


# 自定义装备：森林之魔女项链 ， 领域之主 - 项链
def entry_194(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['45级技能冷却时间恢复速度 +15%', '辅助职业技能伤害 +4%']
    if mode == 0:
        char.技能恢复加成(45, 45, 0.15)
        if char.bufferCarry:
            char.技能攻击力加成(0.04)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女戒指 ， 领域之主 - 戒指
def entry_195(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +281.6%', '韧性条减少量 +10%']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女戒指 ， 领域之主 - 戒指
def entry_196(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤伤害 +15%', '生命值最大值 +300']
    if mode == 0:
        char.异常增伤('灼伤', 0.15)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女戒指 ， 领域之主 - 戒指
def entry_197(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有异常状态抗性 +30%', '辅助职业技能伤害 +3%，所有异常抗性 +30%']
    if mode == 0:
        # 判断暂未实现
        char.所有异常抗性加成(0.3)
        if char.类型 == "辅助":
            char.所有异常抗性加成(0.3)
        if char.bufferCarry:
            char.技能攻击力加成(0.03)
            char.所有异常抗性加成(0.3)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女戒指 ， 领域之主 - 戒指
def entry_198(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +20%', '施放速度 +30%', '辅助职业技能伤害 +3%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.2)
        char.施放速度增加(0.3)
        if char.bufferCarry:
            char.技能攻击力加成(0.03)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女戒指 ， 领域之主 - 戒指
def entry_199(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['最高的异常状态抗性数值高于50%时，技能冷却时间恢复速度 +30% (觉醒技能除外)', '冰冻抗性 +40%']
    if mode == 0:
        char.异常抗性加成('冰冻', 0.4)
    if mode == 1:
        num = 0
        for 类型 in ['中毒', '灼伤', '感电', '出血', '冰冻', '减速', '眩晕', '诅咒', '失明', '石化', '睡眠', '混乱', '束缚']:
            num = max(char.异常抗性获取(类型), num)
        if num >= 0.5:
            char.技能恢复加成(1, 100, 0.3, excName=char.觉醒技能)
        else:
            return '最高异常状态抗性数值缺少{}%'.format(round(50-num*100, 0))


# 自定义装备：森林之魔女戒指 ， 领域之主 - 戒指
def entry_200(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '75级技能冷却时间恢复速度 +15%']
    if mode == 0:
        char.技能攻击力加成(0.05)
        char.技能恢复加成(75, 75, 0.15)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石手镯 ， 领域之主 - 手镯
def entry_201(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '60级技能冷却时间恢复速度 +30%', '使自身进入无法解除的中毒状态']
    if mode == 0:
        char.技能攻击力加成(0.04)
        char.技能恢复加成(60, 60, 0.3)
        if '中毒' not in pa.own_type:
            pa.own_type.append('中毒')
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石手镯 ， 领域之主 - 手镯
def entry_202(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '45级技能冷却时间恢复速度 +30%', '使自身进入无法解除的中毒状态']
    if mode == 0:
        char.技能攻击力加成(0.04)
        char.技能恢复加成(45, 45, 0.3)
        if '中毒' not in pa.own_type:
            pa.own_type.append('中毒')
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石手镯 ， 领域之主 - 手镯
def entry_203(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '35级技能冷却时间恢复速度 +30%', '使自身进入无法解除的中毒状态']
    if mode == 0:
        char.技能攻击力加成(0.04)
        char.技能恢复加成(35, 35, 0.3)
        if '中毒' not in pa.own_type:
            pa.own_type.append('中毒')
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石手镯 ， 领域之主 - 手镯
def entry_204(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +355.7%', '物理/魔法所受伤害 -20%', '减速抗性 +40%']
    if mode == 0:
        char.异常抗性加成('减速', 0.4)
        char.攻击强化加成(params[0])
        char.add_eq_params('hurted_ratio',0.2)
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石手镯 ， 领域之主 - 手镯
def entry_205(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能范围属性数值总和高于30%时，技能伤害 +9%']
    if mode == 0:
        pass
    if mode == 1:
        if char.get_eq_params('skill_range') >= 0.3:
            char.技能攻击力加成(0.09)
        else:
            return '技能范围不足30%'


# 自定义装备：蓝灵绿玉石手镯 ， 领域之主 - 手镯
def entry_206(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有特性技能等级 +1', '技能范围 +10%']
    if mode == 0:
        char.set_eq_params('tp', 1)
        char.set_eq_params('skill_range', char.get_eq_params('skill_range')+0.1)
        char.multiply_eq_params('skill_range_multi',1.1)
        for skill in char.技能栏:
            if hasattr(skill,"TP等级")  and skill.TP等级 > 0:
                skill.TP等级加成(1)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石项链 ， 领域之主 - 项链
def entry_207(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '进入毁坏的寂静城地下城时，技能伤害 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        if '[毁坏的寂静城(高级)]' in pa.dungeons_type:
            char.技能攻击力加成(part=part, x=0.10)


# 自定义装备：蓝灵绿玉石项链 ， 领域之主 - 项链
def entry_208(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '40级技能冷却时间恢复速度 +30%', '使自身进入无法解除的灼伤状态']
    if mode == 0:
        char.技能攻击力加成(0.02)
        char.技能恢复加成(40, 40, 0.3)
        if '灼伤' not in pa.own_type:
            pa.own_type.append('灼伤')
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石项链 ， 领域之主 - 项链
def entry_209(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '70级技能冷却时间恢复速度 +30%', '使自身进入无法解除的灼伤状态']
    if mode == 0:
        char.技能攻击力加成(0.02)
        char.技能恢复加成(70, 70, 0.3)
        if '灼伤' not in pa.own_type:
            pa.own_type.append('灼伤')
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石项链 ， 领域之主 - 项链
def entry_210(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '75级技能冷却时间恢复速度 +30%', '使自身进入无法解除的灼伤状态']
    if mode == 0:
        char.技能攻击力加成(0.02)
        char.技能恢复加成(75, 75, 0.3)
        if '灼伤' not in pa.own_type:
            pa.own_type.append('灼伤')
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石项链 ， 领域之主 - 项链
def entry_211(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +15', '攻击时，敌人韧性条 -5 (冷却时间3秒；辅助角色不适用)']
    if mode == 0:
        char.所有属性强化加成(15)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石项链 ， 领域之主 - 项链
def entry_212(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +148.2% (最多叠加1次 )', '攻击时，敌人韧性条 -5 (冷却时间3秒；辅助角色不适用)']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石戒指 ， 领域之主 - 戒指
def entry_213(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +355.7%', '韧性条减少量 +20%']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石戒指 ， 领域之主 - 戒指
def entry_214(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '80级技能冷却时间恢复速度 +30%']
    if mode == 0:
        char.技能攻击力加成(0.02)
        char.技能恢复加成(80, 80, 0.3)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石戒指 ， 领域之主 - 戒指
def entry_215(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '95级技能冷却时间恢复速度 +30%']
    if mode == 0:
        char.技能攻击力加成(0.02)
        char.技能恢复加成(95, 95, 0.3)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石戒指 ， 领域之主 - 戒指
def entry_216(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['中毒伤害 +13%', '中毒抗性 +5%']
    if mode == 0:
        char.异常增伤('中毒', 0.13)
        char.异常抗性加成('中毒',0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石戒指 ， 领域之主 - 戒指
def entry_217(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暗属性强化 +23']
    if mode == 0:
        char.暗属性强化加成(23)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石戒指 ， 领域之主 - 戒指
def entry_218(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['出血/感电/灼伤/中毒伤害 +14%']
    if mode == 0:
        char.异常增伤('出血', 0.14)
        char.异常增伤('中毒', 0.14)
        char.异常增伤('灼伤', 0.14)
        char.异常增伤('感电', 0.14)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 手镯 ， 深潜迷航腕表
def entry_219(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理/魔法防御力 +14000']
    if mode == 0:
        char.add_eq_params('defense',14000)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 手镯 ， 深潜迷航腕表
def entry_220(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['回避率 +30%']
    if mode == 0:
        char.回避率增加(0.3)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 手镯 ， 深潜迷航腕表
def entry_221(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['消耗无色小晶块的技能攻击力 +10%', '物理/魔法暴击率 +20%']
    if mode == 0:
        char.无色技能加成(1,0.1)
        char.暴击率增加(0.2)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 手镯 ， 深潜迷航腕表
def entry_222(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +30%', '施放速度 +45%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.3)
        char.施放速度增加(0.45)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 手镯 ， 深潜迷航腕表
def entry_223(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '攻击速度 +20%', '施放速度 +30%', '移动速度 +20%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.2)
        char.移动速度增加(0.2)
        char.施放速度增加(0.3)
        char.技能攻击力加成(0.08)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 手镯 ， 深潜迷航腕表
def entry_224(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +370.5%', '物理/魔法所受伤害 -20%']
    if mode == 0:
        char.攻击强化加成(params[0])
        char.add_eq_params('hurted_ratio',0.2)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 项链 ， 深潜迷航项链
def entry_225(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '进入机械七战神实验室地下城时，技能伤害 +10%', '辅助职业技能伤害 +2%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        if '[机械战神试验场]' in pa.dungeons_type:
            char.技能攻击力加成(part=part, x=0.15)
        if char.bufferCarry:
            char.技能攻击力加成(0.02)


# 自定义装备：领域之主 - 项链 ， 深潜迷航项链
def entry_226(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +266.8%', '韧性条减少量 +10%']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 项链 ， 深潜迷航项链
def entry_227(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理/魔法所受伤害 -30%']
    if mode == 0:
        char.add_eq_params('hurted_ratio',0.3)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 项链 ， 深潜迷航项链
def entry_228(char: CharacterProperty = {}, mode: int = 0, text=False, part='', lv=0, params=[]):
    if text:
        return ['所有属性强化 +30']
    if mode == 0:
        char.所有属性强化加成(30)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 项链 ， 深潜迷航项链
def entry_229(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['@[永灭之狂暴]@', '被毁灭侵蚀，每秒减少10%的生命值，强化狂暴状态。', '- 技能伤害 +2%', '- 狂暴状态持续时间上限 +3秒', '需穿戴[死亡蚕食胸甲]。', '', '诅咒抗性 +40%']
    if mode == 0:
        char.异常抗性加成('诅咒', 0.4)
    if mode == 1:
        if 140 in char.装备栏:
            char.技能攻击力加成(0.02)
        pass


# 自定义装备：领域之主 - 项链 ， 深潜迷航项链
def entry_230(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放技能消耗10个以上无色小晶块时，技能伤害 +5%，效果持续30秒。']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.05)
        pass


# 自定义装备：领域之主 - 戒指 ， 深潜迷航导航环
def entry_231(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冰属性强化 +25']
    if mode == 0:
        char.冰属性强化加成(25)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 戒指 ， 深潜迷航导航环
def entry_232(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性强化 +25']
    if mode == 0:
        char.火属性强化加成(25)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 戒指 ， 深潜迷航导航环
def entry_233(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['光属性强化 +25']
    if mode == 0:
        char.光属性强化加成(25)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 戒指 ， 深潜迷航导航环
def entry_234(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暗属性强化 +25']
    if mode == 0:
        char.暗属性强化加成(25)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵胸甲 ， 领域之主 - 上衣 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_235(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +340.9%', '所有速度 +24%']
    if mode == 0:
        char.所有速度增加(part=part, x=0.24)
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵胸甲 ， 领域之主 - 上衣
def entry_236(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['80级技能攻击力 +20%', '95级技能冷却时间 +15%']
    if mode == 0:
        char.技能冷却缩减(95, 95, -0.15)
        char.技能倍率加成(80, 80, 0.2)
    if mode == 1:
        pass


# 自定义装备：恩特精灵胸甲 ， 领域之主 - 上衣
def entry_237(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['80级技能攻击力 +20%', '80级技能冷却时间 +15%']
    if mode == 0:
        char.技能冷却缩减(80, 80, -0.15)
        char.技能倍率加成(80, 80, 0.2)
    if mode == 1:
        pass


# 自定义装备：恩特精灵胸甲 ， 领域之主 - 上衣
def entry_238(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['生命值低于40%时，技能伤害 +8%', '攻击时，恢复1100点生命值/1750点魔法值。 (冷却时间1秒)', '物理/魔法防御力 +25000']
    if mode == 0:
        char.add_eq_params('defense',25000)
        pass
    if mode == 1:
        if pa.get_hp_rate_num(char) <= 40:
            char.技能攻击力加成(part=part, x=0.08)
        else:
            return '生命值高于40%'
        pass


# 自定义装备：恩特精灵胸甲 ， 领域之主 - 上衣
def entry_239(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，恢复5%的生命值。 (冷却时间3秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵胸甲 ， 领域之主 - 上衣
def entry_240(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击时，恢复5%的魔法值。 (冷却时间3秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵护腿 ， 领域之主 - 下装
def entry_241(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['35级技能攻击力 +20%', '35级技能冷却时间 +15%']
    if mode == 0:
        char.技能冷却缩减(35, 35, -0.15)
        char.技能倍率加成(35, 35, 0.2)
    if mode == 1:
        pass


# 自定义装备：恩特精灵护腿 ， 领域之主 - 下装
def entry_242(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['35级技能攻击力 +20%', '40级技能冷却时间 +15%']
    if mode == 0:
        char.技能冷却缩减(40, 40, -0.15)
        char.技能倍率加成(35, 35, 0.2)
    if mode == 1:
        pass


# 自定义装备：恩特精灵护腿 ， 领域之主 - 下装
def entry_243(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['40级技能攻击力 +20%', '40级技能冷却时间 +15%']
    if mode == 0:
        char.技能冷却缩减(40, 40, -0.15)
        char.技能倍率加成(40, 40, 0.2)
    if mode == 1:
        pass


# 自定义装备：恩特精灵护腿 ， 领域之主 - 下装
def entry_244(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['40级技能攻击力 +20%', '45级技能冷却时间 +15%']
    if mode == 0:
        char.技能冷却缩减(45, 45, -0.15)
        char.技能倍率加成(40, 40, 0.2)
    if mode == 1:
        pass


# 自定义装备：恩特精灵护腿 ， 领域之主 - 下装
def entry_245(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['出血伤害 +20%']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('出血', 0.20)


# 自定义装备：恩特精灵护腿 ， 领域之主 - 下装
def entry_246(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['感电伤害 +20%']
    if mode == 0:
        pass
    if mode == 1:
        char.异常增伤('感电', 0.20)


# 自定义装备：恩特精灵护肩 ， 领域之主 - 头肩 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_247(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['用指令施放技能时，该技能攻击力 +12%。 (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        num = char.指令技攻加成(0.12, excName=char.觉醒技能)
        if num == 0:
            return '尚未设置指令施放技能'


# 自定义装备：恩特精灵护肩 ， 领域之主 - 头肩 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_248(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能的指令使用效果 +100% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        for skill in char.技能栏:
            if skill.是否有伤害 == 1 and skill.手搓 and skill.名称 not in char.觉醒技能:
                skill.手搓收益 += 1
        pass


# 自定义装备：恩特精灵护肩 ， 领域之主 - 头肩
def entry_249(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['不消耗无色小晶块的技能攻击力 +15%']
    if mode == 0:
        pass
    if mode == 1:
        char.无色技能加成(0,0.15)
        pass


# 自定义装备：恩特精灵护肩 ， 领域之主 - 头肩
def entry_250(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['45级技能攻击力 +20%', '45级技能冷却时间 +15%']
    if mode == 0:
        char.技能冷却缩减(45, 45, -0.15)
        char.技能倍率加成(45, 45, 0.2)
    if mode == 1:
        pass


# 自定义装备：恩特精灵护肩 ， 领域之主 - 头肩
def entry_251(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['45级技能攻击力 +20%', '60级技能冷却时间 +15%']
    if mode == 0:
        char.技能冷却缩减(60, 60, -0.15)
        char.技能倍率加成(45, 45, 0.2)
    if mode == 1:
        pass


# 自定义装备：恩特精灵护肩 ， 领域之主 - 头肩
def entry_252(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理/魔法暴击率 +15%']
    if mode == 0:
        char.暴击率增加(0.15)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵腰带 ， 领域之主 - 腰带 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_253(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '物理/魔法防御力 +4000']
    if mode == 0:
        char.技能攻击力加成(0.05)
        char.add_eq_params('defense',4000)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵腰带 ， 领域之主 - 腰带 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_254(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '移动速度 +5%']
    if mode == 0:
        char.技能攻击力加成(0.05)
        char.移动速度增加(0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵腰带 ， 领域之主 - 腰带
def entry_255(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['60级技能攻击力 +20%', '60级技能冷却时间 +15%']
    if mode == 0:
        char.技能冷却缩减(60, 60, -0.15)
        char.技能倍率加成(60, 60, 0.2)
    if mode == 1:
        pass


# 自定义装备：恩特精灵腰带 ， 领域之主 - 腰带
def entry_256(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['60级技能攻击力 +20%', '70级技能冷却时间 +15%']
    if mode == 0:
        char.技能冷却缩减(70, 70, -0.15)
        char.技能倍率加成(60, 60, 0.2)
    if mode == 1:
        pass


# 自定义装备：恩特精灵腰带 ， 领域之主 - 腰带
def entry_257(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤伤害 +20%']
    if mode == 0:
        char.异常增伤('灼伤', 0.2)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵腰带 ， 领域之主 - 腰带
def entry_258(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['中毒伤害 +20%']
    if mode == 0:
        char.异常增伤('中毒', 0.2)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵战靴 ， 领域之主 - 鞋 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_259(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能快捷栏每空1个栏位，增加2%的技能伤害。 (最多叠加6次)']
    if mode == 0:
        pass
    if mode == 1:
        num = len(list(filter(lambda i: i == "", char.hotkey)))
        char.技能攻击力加成(part=part, x=min(
            0.12, num*0.02))
        if num < 6:
            return '技能快捷栏空位不足6个'


# 自定义装备：恩特精灵战靴 ， 领域之主 - 鞋
def entry_260(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['70级技能攻击力 +20%', '70级技能冷却时间 +15%']
    if mode == 0:
        char.技能冷却缩减(70, 70, -0.15)
        char.技能倍率加成(70, 70, 0.2)
    if mode == 1:
        pass


# 自定义装备：恩特精灵战靴 ， 领域之主 - 鞋
def entry_261(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['70级技能攻击力 +20%', '75级技能冷却时间 +15%']
    if mode == 0:
        char.技能冷却缩减(75, 75, -0.15)
        char.技能倍率加成(70, 70, 0.2)
    if mode == 1:
        pass


# 自定义装备：恩特精灵战靴 ， 领域之主 - 鞋
def entry_262(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['75级技能攻击力 +20%', '75级技能冷却时间 +15%']
    if mode == 0:
        char.技能冷却缩减(75, 75, -0.15)
        char.技能倍率加成(75, 75, 0.2)
    if mode == 1:
        pass


# 自定义装备：恩特精灵战靴 ， 领域之主 - 鞋
def entry_263(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['75级技能攻击力 +20%', '80级技能冷却时间 +15%']
    if mode == 0:
        char.技能冷却缩减(80, 80, -0.15)
        char.技能倍率加成(75, 75, 0.2)
    if mode == 1:
        pass


# 自定义装备：恩特精灵战靴 ， 领域之主 - 鞋
def entry_264(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['移动速度 +30%']
    if mode == 0:
        char.移动速度增加(0.3)
    if mode == 1:
        pass


# 自定义装备：森林之魔女上衣 ， 领域之主 - 上衣
def entry_265(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['生命值高于40%时，技能伤害 +3%', '数值最高的出血/中毒/灼伤/感电伤害低于20%时，技能伤害 +4%', '辅助职业技能冷却时间 -5% (觉醒技能除外)']
    if mode == 0:
        if char.bufferCarry:
            char.技能冷却缩减(1, 100, 0.05,excName=char.觉醒技能)
        pass
    if mode == 1:
        tip = []
        if pa.get_hp_rate_num(char) >= 40:
            char.技能攻击力加成(part=part, x=0.03)
        else:
            tip.append('生命值低于40%')
        key = max(char.伤害系数, key=char.伤害系数.get)
        if char.类型 == "辅助":
            char.技能冷却缩减(1, 100, 0.05,excName=char.觉醒技能)
        if char.伤害系数.get(key, 1.0) < 1.2:
            char.技能攻击力加成(part=part, x=0.04)
        else:
            tip.append('最高的伤害型异常状态伤害增加数值高于20%')
        if len(tip) > 0:
            return tip
        pass


# 自定义装备：森林之魔女上衣 ， 领域之主 - 上衣
def entry_266(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +370.5%', '生命值最大值 +300']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女上衣 ， 领域之主 - 上衣
def entry_267(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性强化 +25', '生命值最大值 +300']
    if mode == 0:
        char.火属性强化加成(25)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女上衣 ， 领域之主 - 上衣
def entry_268(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冰属性强化 +25', '生命值最大值 +300']
    if mode == 0:
        char.冰属性强化加成(25)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女上衣 ， 领域之主 - 上衣
def entry_269(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['光属性强化 +25', '生命值最大值 +300']
    if mode == 0:
        char.光属性强化加成(25)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女上衣 ， 领域之主 - 上衣
def entry_270(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暗属性强化 +25', '生命值最大值 +300']
    if mode == 0:
        char.暗属性强化加成(25)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女护腿 ， 领域之主 - 下装
def entry_271(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['45级技能攻击力 +20%', '辅助职业技能伤害 +5%']
    if mode == 0:
        char.技能倍率加成(45, 45, 0.2)
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
    if mode == 1:
        pass


# 自定义装备：森林之魔女护腿 ， 领域之主 - 下装
def entry_272(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['35级技能攻击力 +20%', '辅助职业技能伤害 +5%']
    if mode == 0:
        char.技能倍率加成(35, 35, 0.2)
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
    if mode == 1:
        pass


# 自定义装备：森林之魔女护腿 ， 领域之主 - 下装 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_273(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['45级技能冷却时间 -20%', '辅助职业技能伤害 +5%']
    if mode == 0:
        char.技能冷却缩减(45, 45, 0.2)
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
    if mode == 1:
        pass


# 自定义装备：森林之魔女护腿 ， 领域之主 - 下装 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_274(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['35级技能冷却时间 -20%', '辅助职业技能伤害 +5%']
    if mode == 0:
        char.技能冷却缩减(35, 35, 0.2)
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
    if mode == 1:
        pass


# 自定义装备：森林之魔女护腿 ， 领域之主 - 下装
def entry_275(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['45、60、70级技能攻击力 +5%', '45级主动技能等级 +1', '辅助职业技能冷却时间 -5% (觉醒技能除外)']
    if mode == 0:
        char.技能等级加成('主动', 45, 45, 1)
        char.技能倍率加成(45, 45, 0.05)
        char.技能倍率加成(60, 60, 0.05)
        char.技能倍率加成(70, 70, 0.05)
        if char.类型 == "辅助":
            char.技能冷却缩减(1, 100, 0.05,excName=char.觉醒技能)
        if char.bufferCarry:
            char.技能冷却缩减(1, 100, 0.05,excName=char.觉醒技能)
    if mode == 1:
        pass


# 自定义装备：森林之魔女护腿 ， 领域之主 - 下装
def entry_276(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['30~40级技能攻击力 +5%', '35级主动技能等级 +1', '辅助职业技能冷却时间 -5% (觉醒技能除外)']
    if mode == 0:
        char.技能等级加成('主动', 35, 35, 1)
        char.技能倍率加成(30, 40, 0.05)
        if char.类型 == "辅助":
            char.技能冷却缩减(1, 100, 0.05,excName=char.觉醒技能)
        if char.bufferCarry:
            char.技能冷却缩减(1, 100, 0.05,excName=char.觉醒技能)
    if mode == 1:
        pass


# 自定义装备：森林之魔女斗篷 ， 领域之主 - 头肩
def entry_277(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['40级技能攻击力 +20%', '辅助职业技能伤害 +5%']
    if mode == 0:
        char.技能倍率加成(40, 40, 0.2)
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
    if mode == 1:
        pass


# 自定义装备：森林之魔女斗篷 ， 领域之主 - 头肩
def entry_278(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['30级技能攻击力 +20%', '辅助职业技能伤害 +5%']
    if mode == 0:
        char.技能倍率加成(30, 30, 0.2)
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
    if mode == 1:
        pass


# 自定义装备：森林之魔女斗篷 ， 领域之主 - 头肩 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_279(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['40级技能冷却时间 -20%', '辅助技能冷却时间 -5% (觉醒技能除外)']
    if mode == 0:
        char.技能冷却缩减(40, 40, 0.2)
        # char.条件冷却加成("Lv40", 0.2)
        if char.类型 == "辅助":
            char.技能冷却缩减(1, 100, 0.05,excName=char.觉醒技能)
        if char.bufferCarry:
            char.技能冷却缩减(1, 100, 0.05,excName=char.觉醒技能)
    if mode == 1:
        pass


# 自定义装备：森林之魔女斗篷 ， 领域之主 - 头肩 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_280(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['30级技能冷却时间 -20%', '辅助技能冷却时间 -5% (觉醒技能除外)']
    if mode == 0:
        char.技能冷却缩减(30, 30, 0.2)
        # char.条件冷却加成("Lv30", 0.2)
        if char.类型 == "辅助":
            char.技能冷却缩减(1, 100, 0.05,excName=char.觉醒技能)
        if char.bufferCarry:
            char.技能冷却缩减(1, 100, 0.05,excName=char.觉醒技能)
    if mode == 1:
        pass


# 自定义装备：森林之魔女斗篷 ， 领域之主 - 头肩
def entry_281(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['30~40级技能攻击力 +5%', '40级主动技能等级 +1', '辅助职业技能冷却时间 -5% (觉醒技能除外)']
    if mode == 0:
        char.技能等级加成('主动', 40, 40, 1)
        char.技能倍率加成(30, 40, 0.05)
        if char.类型 == "辅助":
            char.技能冷却缩减(1, 100, 0.05,excName=char.觉醒技能)
        if char.bufferCarry:
            char.技能冷却缩减(1, 100, 0.05,excName=char.觉醒技能)
    if mode == 1:
        pass


# 自定义装备：森林之魔女斗篷 ， 领域之主 - 头肩
def entry_282(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +281.6%', '韧性条减少量 +30%']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女腰带 ， 领域之主 - 腰带 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_283(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能冷却时间 -15% (觉醒技能除外)', '辅助职业技能冷却时间 -5% (觉醒技能除外)']
    if mode == 0:
        char.技能冷却缩减(1, 100, 0.15, excName=char.觉醒技能)
        if char.类型 == "辅助":
            char.技能冷却缩减(1, 100, 0.05,excName=char.觉醒技能)
        if char.bufferCarry:
            char.技能冷却缩减(1, 100, 0.05,excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女腰带 ， 领域之主 - 腰带
def entry_284(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +444.6%', '辅助职业技能伤害 +5%']
    if mode == 0:
        char.攻击强化加成(params[0])
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女腰带 ， 领域之主 - 腰带
def entry_285(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['单人挑战时，技能伤害 +10%', '出血抗性 +40%']
    if mode == 0:
        char.异常抗性加成('出血', 0.4)
    if mode == 1:
        if pa.teammate_num == 1:
            char.技能攻击力加成(0.1)
        else:
            return '存在队友'
        pass


# 自定义装备：森林之魔女腰带 ， 领域之主 - 腰带
def entry_286(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '95级技能冷却时间恢复速度 +15%']
    if mode == 0:
        char.技能恢复加成(95, 95, 0.15)
        char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女腰带 ， 领域之主 - 腰带
def entry_287(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '60级技能冷却时间恢复速度 +15%']
    if mode == 0:
        char.技能恢复加成(60, 60, 0.15)
        char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女腰带 ， 领域之主 - 腰带
def entry_288(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放15级技能时，进入霸体状态2秒。 (冷却时间10秒)', '攻击速度 +15%', '施放速度 +22.5%', '辅助职业技能伤害 +5%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.15)
        char.施放速度增加(0.225)
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女长靴 ， 领域之主 - 鞋
def entry_289(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +16%', '施放速度 +24%', '辅助职业技能伤害 +5%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.16)
        char.施放速度增加(0.24)
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
    if mode == 1:
        pass


# 自定义装备：森林之魔女长靴 ， 领域之主 - 鞋
def entry_290(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理/魔法防御力 +8000', '辅助职业技能伤害 +5%']
    if mode == 0:
        char.add_eq_params('defense',8000)
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女长靴 ， 领域之主 - 鞋
def entry_291(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性抗性 +16', '辅助职业技能伤害 +5%']
    if mode == 0:
        char.所有属性抗性加成(16)
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女长靴 ， 领域之主 - 鞋
def entry_292(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '生命值最大值 +200']
    if mode == 0:
        char.技能攻击力加成(0.06)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女长靴 ， 领域之主 - 鞋
def entry_293(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%', '- 需要穿戴[铭刻之誓约]装备', '', '所有速度 +10%', '灼伤抗性 +40%', '辅助职业技能伤害 +8%，所有速度 +10%']
    if mode == 0:
        if char.bufferCarry:
            char.技能攻击力加成(0.08)
            char.所有速度增加(part=part, x=0.1)
        char.异常抗性加成('灼伤', 0.4)
        char.所有速度增加(part=part, x=0.1)
        if char.check_equ_by_name('铭刻之誓约'):
            char.技能攻击力加成(0.08)
        else:
            return '未穿戴穿戴[铭刻之誓约]'
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石胸甲 ， 领域之主 - 上衣
def entry_294(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +370.5%', '物理/魔法防御力 +5000']
    if mode == 0:
        char.攻击强化加成(params[0])
        char.add_eq_params('defense',5000)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石胸甲 ， 领域之主 - 上衣
def entry_295(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['80、95级主动技能等级 +3']
    if mode == 0:
        char.技能等级加成('主动', 80, 95, 3, excName=char.觉醒技能)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石胸甲 ， 领域之主 - 上衣
def entry_296(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['出血伤害 +30%', '物理/魔法所受伤害 +20%', '出血抗性 +20%']
    if mode == 0:
        char.异常增伤('出血', 0.3)
        char.异常抗性加成('出血', 0.2)
        char.add_eq_params('hurted_ratio',-0.2)
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石胸甲 ， 领域之主 - 上衣
def entry_297(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['感电伤害 +30%', '物理/魔法所受伤害 +20%', '感电抗性 +20%']
    if mode == 0:
        char.异常增伤('感电', 0.3)
        char.异常抗性加成('感电', 0.2)
        char.add_eq_params('hurted_ratio',-0.2)
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石胸甲 ， 领域之主 - 上衣
def entry_298(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤伤害 +30%', '物理/魔法所受伤害 +20%', '灼伤抗性 +20%']
    if mode == 0:
        char.异常增伤('灼伤', 0.3)
        char.异常抗性加成('灼伤', 0.2)
        char.add_eq_params('hurted_ratio',-0.2)
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石胸甲 ， 领域之主 - 上衣
def entry_299(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['中毒伤害 +30%', '物理/魔法所受伤害 +20%', '中毒抗性 +20%']
    if mode == 0:
        char.异常增伤('中毒', 0.3)
        char.异常抗性加成('中毒', 0.2)
        char.add_eq_params('hurted_ratio',-0.2)
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石护腿 ， 领域之主 - 下装
def entry_300(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['70~75级主动技能等级 +3']
    if mode == 0:
        if not char.实际名称 == "crusader_male":
            char.技能等级加成('主动', 70, 75, 3)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石护腿 ， 领域之主 - 下装
def entry_301(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性强化 +35']
    if mode == 0:
        char.火属性强化加成(35)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石护腿 ， 领域之主 - 下装
def entry_302(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冰属性强化 +35']
    if mode == 0:
        char.冰属性强化加成(35)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石护腿 ， 领域之主 - 下装
def entry_303(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['光属性强化 +35']
    if mode == 0:
        char.光属性强化加成(35)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石护腿 ， 领域之主 - 下装
def entry_304(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暗属性强化 +35']
    if mode == 0:
        char.暗属性强化加成(35)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石护腿 ， 领域之主 - 下装
def entry_305(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '- 需要穿戴[永恒的心愿]', '所有速度 +15%', '失明抗性 +40%']
    if mode == 0:
        char.异常抗性加成('失明', 0.4)
        char.所有速度增加(0.15)
        if char.check_equ_by_name('永恒的心愿'):
            char.技能攻击力加成(0.05)
        else:
            return '未穿戴穿戴[永恒的心愿]'
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石肩甲 ， 领域之主 - 头肩
def entry_306(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '消耗品效果持续时间 +20%', '所有异常状态抗性 +2.5%', '睡眠抗性 -2.5%']
    if mode == 0:
        char.技能攻击力加成(0.07)
        char.所有异常抗性加成(0.025)
        char.异常抗性加成('睡眠',-0.025)
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石肩甲 ， 领域之主 - 头肩
def entry_307(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +355.7% (最多叠加5次)', '物理/魔法防御力 +5000']
    if mode == 0:
        char.add_eq_params('defense',5000)
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石肩甲 ， 领域之主 - 头肩
def entry_308(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['35~40级主动技能等级 +3', '- 缔造者[终末幻想]系列技能适用该效果。']
    if mode == 0:
        if char.职业 == '缔造者':
            char.技能等级加成('主动', 50, 50, 3)
        else:
            char.技能等级加成('主动', 35, 40, 3)
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石肩甲 ， 领域之主 - 头肩
def entry_309(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +15', '混乱抗性 +40%']
    if mode == 0:
        char.所有属性强化加成(15)
        char.异常抗性加成('混乱', 0.4)
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石肩甲 ， 领域之主 - 头肩
def entry_310(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['45、60、70级技能攻击力 +5%', '60级主动技能等级 +1']
    if mode == 0:
        char.技能倍率加成(45, 45, 0.05)
        char.技能倍率加成(60, 60, 0.05)
        char.技能倍率加成(70, 70, 0.05)
        char.技能等级加成('主动', 60, 60, 1)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石肩甲 ， 领域之主 - 头肩
def entry_311(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['45、60、70级技能攻击力 +5%', '70级主动技能等级 +1']
    if mode == 0:
        char.技能倍率加成(45, 45, 0.05)
        char.技能倍率加成(60, 60, 0.05)
        char.技能倍率加成(70, 70, 0.05)
        char.技能等级加成('主动', 70, 70, 1)
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石腰带 ， 领域之主 - 腰带
def entry_312(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['60级技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(60, 60, 0.2)
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石腰带 ， 领域之主 - 腰带
def entry_313(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['70级技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(70, 70, 0.2)
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石腰带 ， 领域之主 - 腰带 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_314(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['60级技能冷却时间 -20%']
    if mode == 0:
        char.技能冷却缩减(60, 60, 0.2)
        # char.条件冷却加成("Lv60", 0.2)
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石腰带 ， 领域之主 - 腰带 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_315(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['70级技能冷却时间 -20%']
    if mode == 0:
        char.技能冷却缩减(70, 70, 0.2)
        # char.条件冷却加成("Lv70", 0.2)
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石腰带 ， 领域之主 - 腰带
def entry_316(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['按照[技能魔法值消耗量]属性数值总和的1%，增加技能伤害。 (最多10%)']
    if mode == 0:
        pass
    if mode == 1:
        if char.MP消耗倍率() >= 1:
            char.技能攻击力加成(part=part, x=min((char.MP消耗倍率() - 1)*0.01, 0.1))
        if char.MP消耗倍率() < 11:
            return 'MP消耗量增加需提升{}%'.format(round(1100-char.MP消耗倍率()*100), 0)


# 自定义装备：蓝灵绿玉石腰带 ， 领域之主 - 腰带
def entry_317(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['恢复技能消耗的魔法值的10%', '技能魔法值消耗量 +100%']
    if mode == 0:
        char.MP消耗量加成(1)
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石长靴 ， 领域之主 - 鞋
def entry_318(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['20级技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(20, 20, 0.2)
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石长靴 ， 领域之主 - 鞋
def entry_319(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['25级技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(25, 25, 0.2)
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石长靴 ， 领域之主 - 鞋 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_320(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['20级技能冷却时间 -20%']
    if mode == 0:
        char.技能冷却缩减(20, 20, 0.2)
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石长靴 ， 领域之主 - 鞋 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_321(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['25级技能冷却时间 -20%']
    if mode == 0:
        char.技能冷却缩减(25, 25, 0.2)
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石长靴 ， 领域之主 - 鞋
def entry_322(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['45、60主动技能等级 +3', '- 缔造者[终末幻想][构造]系列技能适用该效果。']
    if mode == 0:
        if char.职业 == '缔造者':
            char.技能等级加成('主动', 60, 60, 3)
            char.技能等级加成('主动', 50, 50, 3)
        else:
            char.技能等级加成('主动', 45, 45, 3)
            char.技能等级加成('主动', 60, 60, 3)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石长靴 ， 领域之主 - 鞋
def entry_323(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放技能消耗15个以上无色小晶块时，技能伤害 +15%，效果持续30秒。', '束缚抗性 +40%']
    if mode == 0:
        char.异常抗性加成('束缚', 0.4)
    if mode == 1:
        # 无色判定
        char.技能攻击力加成(0.15)
        pass


# 自定义装备：领域之主 - 上衣 ， 深潜迷航胸甲
def entry_324(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '100级主动技能攻击力 +20%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能攻击力加成(0.02)
        char.技能倍率加成(100, 100, 0.2)
        pass


# 自定义装备：领域之主 - 上衣 ， 深潜迷航胸甲
def entry_325(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '85级主动技能攻击力 +20%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能倍率加成(85, 85, 0.2)
        char.技能攻击力加成(0.02)
        pass


# 自定义装备：领域之主 - 上衣 ， 深潜迷航胸甲
def entry_326(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['95级技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(95, 95, 0.2)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 上衣 ， 深潜迷航胸甲 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_327(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['95级技能冷却时间 -20%']
    if mode == 0:
        char.技能冷却缩减(95, 95, 0.2)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 上衣 ， 深潜迷航胸甲
def entry_328(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['75、80、95级技能攻击力 +5%', '95级主动技能等级 +1']
    if mode == 0:
        char.技能倍率加成(75, 75, 0.05)
        char.技能倍率加成(80, 80, 0.05)
        char.技能倍率加成(95, 95, 0.05)
        char.技能等级加成('主动', 95, 95, 1)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 上衣 ， 深潜迷航胸甲
def entry_329(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '移动速度 +5%']
    if mode == 0:
        char.技能攻击力加成(0.06)
        char.移动速度增加(0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 下装 ， 深潜迷航长裤
def entry_330(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['75级技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(75, 75, 0.2)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 下装 ， 深潜迷航长裤
def entry_331(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['80级技能攻击力 +20%']
    if mode == 0:
        char.技能倍率加成(80, 80, 0.2)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 下装 ， 深潜迷航长裤 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_332(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['75级技能冷却时间 -20%']
    if mode == 0:
        char.技能冷却缩减(75, 75, 0.2)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 下装 ， 深潜迷航长裤 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_333(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['80级技能冷却时间 -20%']
    if mode == 0:
        char.技能冷却缩减(80, 80, 0.2)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 下装 ， 深潜迷航长裤
def entry_334(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['75、80、95级技能攻击力 +5%', '75级主动技能等级 +1']
    if mode == 0:
        char.技能倍率加成(75, 75, 0.05)
        char.技能倍率加成(80, 80, 0.05)
        char.技能倍率加成(95, 95, 0.05)
        if not char.实际名称 == "crusader_male":
            char.技能等级加成('主动', 75, 75, 1)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 下装 ， 深潜迷航长裤
def entry_335(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['75、80、95级技能攻击力 +5%', '80级主动技能等级 +1']
    if mode == 0:
        char.技能倍率加成(75, 75, 0.05)
        char.技能倍率加成(80, 80, 0.05)
        char.技能倍率加成(95, 95, 0.05)
        char.技能等级加成('主动', 80, 80, 1)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 头肩 ， 深潜迷航气囊
def entry_336(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性强化 +40']
    if mode == 0:
        char.火属性强化加成(40)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 头肩 ， 深潜迷航气囊
def entry_337(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冰属性强化 +40']
    if mode == 0:
        char.冰属性强化加成(40)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 头肩 ， 深潜迷航气囊
def entry_338(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暗属性强化 +40']
    if mode == 0:
        char.暗属性强化加成(40)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵圣杯 ， 领域之主 - 辅助装备
def entry_339(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '火属性抗性 +40']
    if mode == 0:
        char.火属性抗性加成(40)
        char.技能攻击力加成(part=part, x=0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵圣杯 ， 领域之主 - 辅助装备
def entry_340(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +311.2%', '冰属性抗性 +40']
    if mode == 0:
        char.冰属性抗性加成(40)
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵圣杯 ， 领域之主 - 辅助装备
def entry_341(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理/魔法防御力 +14000', '光属性抗性 +40']
    if mode == 0:
        char.光属性抗性加成(40)
        char.add_eq_params('defense',14000)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵圣杯 ， 领域之主 - 辅助装备
def entry_342(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +15%', '施放速度 +22.5%', '暗属性抗性 +40']
    if mode == 0:
        char.暗属性抗性加成(40)
        char.攻击速度增加(part=part, x=0.15)
        char.施放速度增加(0.225)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵圣杯 ， 领域之主 - 辅助装备
def entry_343(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['生命值最大值 +2000', '魔法值最大值 +2000']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵圣杯 ， 领域之主 - 辅助装备
def entry_344(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性抗性数值之和高于250时，出血伤害 +15%']
    if mode == 0:
        pass
    if mode == 1:
        抗性 = sum([char.火属性抗性(), char.冰属性抗性(), char.光属性抗性(), char.暗属性抗性()])
        if 抗性 >= 250:
            char.异常增伤('出血', 0.15)
        else:
            return '所有属性抗性之和缺少{}'.format(round(250-抗性, 0))
        # char.异常增伤('出血', 0.15)


# 自定义装备：恩特精灵之心 ， 领域之主 - 魔法石
def entry_345(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['命中率 +20%']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵之心 ， 领域之主 - 魔法石
def entry_346(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性强化 +25', '火属性抗性 +2']
    if mode == 0:
        char.火属性强化加成(25)
        char.火属性抗性加成(2)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵之心 ， 领域之主 - 魔法石
def entry_347(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冰属性强化 +25', '冰属性抗性 +2']
    if mode == 0:
        char.冰属性强化加成(25)
        char.冰属性抗性加成(2)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵之心 ， 领域之主 - 魔法石
def entry_348(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['光属性强化 +25', '光属性抗性 +2']
    if mode == 0:
        char.光属性强化加成(25)
        char.光属性抗性加成(2)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵之心 ， 领域之主 - 魔法石
def entry_349(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['暗属性强化 +25', '暗属性抗性 +2']
    if mode == 0:
        char.暗属性强化加成(25)
        char.暗属性抗性加成(2)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵之心 ， 领域之主 - 魔法石
def entry_350(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性抗性数值之和高于250时，灼伤伤害 +15%']
    if mode == 0:
        pass
    if mode == 1:
        # 抗性判断
        抗性 = sum([char.火属性抗性(), char.冰属性抗性(), char.光属性抗性(), char.暗属性抗性()])
        if 抗性 >= 250:
            char.异常增伤('灼伤', 0.15)
        else:
            return '所有属性抗性之和缺少{}'.format(round(250-抗性, 0))


# 自定义装备：恩特精灵耳环 ， 领域之主 - 耳环 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_351(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +444.6%', '所有属性抗性 +3']
    if mode == 0:
        char.攻击强化加成(params[0])
        char.所有属性抗性加成(2)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵耳环 ， 领域之主 - 耳环
def entry_352(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['出血伤害 +15%', '出血抗性 +1%']
    if mode == 0:
        char.异常增伤('出血', 0.15)
        char.异常抗性加成('出血',0.01)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵耳环 ， 领域之主 - 耳环
def entry_353(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['中毒伤害 +15%', '中毒抗性 +1%']
    if mode == 0:
        char.异常增伤('中毒', 0.15)
        char.异常抗性加成('中毒',0.01)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵耳环 ， 领域之主 - 耳环
def entry_354(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['感电伤害 +15%', '感电抗性 +1%']
    if mode == 0:
        char.异常增伤('感电', 0.15)
        char.异常抗性加成('感电',0.01)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵耳环 ， 领域之主 - 耳环
def entry_355(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤伤害 +15%', '灼伤抗性 +1%']
    if mode == 0:
        char.异常增伤('灼伤', 0.15)
        char.异常抗性加成('灼伤',0.01)
        pass
    if mode == 1:
        pass


# 自定义装备：恩特精灵耳环 ， 领域之主 - 耳环
def entry_356(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性抗性数值之和高于250时，感电伤害 +15%']
    if mode == 0:
        pass
    if mode == 1:
        # 抗性判断
        抗性 = sum([char.火属性抗性(), char.冰属性抗性(), char.光属性抗性(), char.暗属性抗性()])
        if 抗性 >= 250:
            char.异常增伤('感电', 0.15)
        else:
            return '所有属性抗性之和缺少{}'.format(round(250-抗性, 0))


# 自定义装备：森林之魔女篮子 ， 领域之主 - 辅助装备
def entry_357(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['45级技能冷却时间恢复速度 +40%', '辅助职业技能伤害 +3%']
    if mode == 0:
        char.技能恢复加成(45, 45, 0.4)
        if char.bufferCarry:
            char.技能攻击力加成(0.03)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女篮子 ， 领域之主 - 辅助装备
def entry_358(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['60级技能冷却时间恢复速度 +40%', '辅助职业技能伤害 +3%']
    if mode == 0:
        char.技能恢复加成(60, 60, 0.4)
        if char.bufferCarry:
            char.技能攻击力加成(0.03)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女篮子 ， 领域之主 - 辅助装备
def entry_359(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['35级技能冷却时间恢复速度 +40%', '辅助职业技能伤害 +3%']
    if mode == 0:
        char.技能恢复加成(35, 35, 0.4)
        if char.bufferCarry:
            char.技能攻击力加成(0.03)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女篮子 ， 领域之主 - 辅助装备
def entry_360(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['感电伤害 +15%', '生命值最大值 +300']
    if mode == 0:
        char.异常增伤('感电', 0.15)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女篮子 ， 领域之主 - 辅助装备
def entry_361(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['睡眠抗性 +40%', '辅助职业技能伤害 +5%，所有异常状态抗性 +20%']
    if mode == 0:
        char.异常抗性加成('睡眠', 0.4)
        if char.类型 == "辅助":
            char.所有异常抗性加成(0.2)
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
            char.所有异常抗性加成(0.2)
    if mode == 1:
        pass


# 自定义装备：森林之魔女篮子 ， 领域之主 - 辅助装备
def entry_362(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['80级技能冷却时间恢复速度 +15%', '辅助职业技能伤害 +5%']
    if mode == 0:
        char.技能恢复加成(80, 80, 0.15)
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女精灵石 ， 领域之主 - 魔法石
def entry_363(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['70级技能冷却时间恢复速度 +40%']
    if mode == 0:
        char.技能恢复加成(70, 70, 0.4)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女精灵石 ， 领域之主 - 魔法石
def entry_364(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['75级技能冷却时间恢复速度 +40%']
    if mode == 0:
        char.技能恢复加成(75, 75, 0.4)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女精灵石 ， 领域之主 - 魔法石
def entry_365(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['40级技能冷却时间恢复速度 +40%']
    if mode == 0:
        char.技能恢复加成(40, 40, 0.4)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女精灵石 ， 领域之主 - 魔法石
def entry_366(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['眩晕抗性 +40%', '被攻击时，赋予生命值最大值20%的保护罩，效果持续20秒。 (冷却时间10秒)']
    if mode == 0:
        char.异常抗性加成('眩晕', 0.4)
    if mode == 1:
        pass


# 自定义装备：森林之魔女精灵石 ， 领域之主 - 魔法石
def entry_367(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['70级技能冷却时间恢复速度 +15%', '辅助职业技能伤害 +5%']
    if mode == 0:
        char.技能恢复加成(70, 70, 0.15)
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女精灵石 ， 领域之主 - 魔法石
def entry_368(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['装备提供的保护罩上限 +20%', '辅助职业技能伤害 +5%']
    if mode == 0:
        char.set_eq_params('protect_max',char.get_eq_params('protect_max') + 0.2)
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女耳环 ， 领域之主 - 耳环 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_369(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +25', '辅助职业技能伤害 +3%']
    if mode == 0:
        char.所有属性强化加成(25)
        if char.bufferCarry:
            char.技能攻击力加成(0.03)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女耳环 ， 领域之主 - 耳环
def entry_370(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['95级技能冷却时间恢复速度 +40%']
    if mode == 0:
        char.技能恢复加成(95, 95, 0.4)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女耳环 ， 领域之主 - 耳环
def entry_371(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['80级技能冷却时间恢复速度 +40%']
    if mode == 0:
        char.技能恢复加成(80, 80, 0.4)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女耳环 ， 领域之主 - 耳环
def entry_372(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理/魔法所受伤害 -10%', '石化抗性 +40%']
    if mode == 0:
        char.异常抗性加成('石化', 0.4)
        char.add_eq_params('hurted_ratio',0.1)
    if mode == 1:
        pass


# 自定义装备：森林之魔女耳环 ， 领域之主 - 耳环
def entry_373(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['35级技能冷却时间恢复速度增加15%', '辅助职业技能伤害 +3%']
    if mode == 0:
        char.技能恢复加成(35, 35, 0.15)
        if char.bufferCarry:
            char.技能攻击力加成(0.03)
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女耳环 ， 领域之主 - 耳环
def entry_374(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['40级技能冷却时间恢复速度增加15%', '辅助职业技能伤害 +3%']
    if mode == 0:
        char.技能恢复加成(40, 40, 0.15)
        if char.bufferCarry:
            char.技能攻击力加成(0.03)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石香水 ， 领域之主 - 辅助装备
def entry_375(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['魔法值30%以下时，消耗10个无色小晶块，恢复30%的魔法值。 (冷却时间10秒)']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石香水 ， 领域之主 - 辅助装备
def entry_376(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +281.6%', '物理/魔法防御力 +5000']
    if mode == 0:
        char.攻击强化加成(params[0])
        char.add_eq_params('defense',5000)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石香水 ， 领域之主 - 辅助装备
def entry_377(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +20%', '施放速度 +30%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.2)
        char.施放速度增加(0.3)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石香水 ， 领域之主 - 辅助装备
def entry_378(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['出血伤害 +13%']
    if mode == 0:
        char.异常增伤('出血', 0.13)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石香水 ， 领域之主 - 辅助装备
def entry_379(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['冰属性强化 +23']
    if mode == 0:
        char.冰属性强化加成(23)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石香水 ， 领域之主 - 辅助装备
def entry_380(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +237.1%']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石宝石 ， 领域之主 - 魔法石
def entry_381(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理/魔法所受伤害 -15%']
    if mode == 0:
        char.add_eq_params('hurted_ratio',0.15)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石宝石 ， 领域之主 - 魔法石
def entry_382(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤伤害 +13%']
    if mode == 0:
        char.异常增伤('灼伤', 0.13)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石宝石 ， 领域之主 - 魔法石
def entry_383(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['火属性强化 +23']
    if mode == 0:
        char.火属性强化加成(23)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石宝石 ， 领域之主 - 魔法石
def entry_384(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放20级技能时，进入霸体状态2秒。 (冷却时间10秒)', '攻击速度 +15%', '施放速度 +22.5%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.15)
        char.施放速度增加(0.225)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石宝石 ， 领域之主 - 魔法石
def entry_385(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放25级技能时，进入霸体状态2秒。 (冷却时间10秒)', '攻击速度 +15%', '施放速度 +22.5%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.15)
        char.施放速度增加(0.225)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石宝石 ， 领域之主 - 魔法石
def entry_386(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放30级技能时，进入霸体状态2秒。 (冷却时间10秒)', '攻击速度 +15%', '施放速度 +22.5%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.15)
        char.施放速度增加(0.225)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石耳环 ， 领域之主 - 耳环
def entry_387(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['正面攻击时，增加8%的技能伤害。']
    if mode == 0:
        pass
    if mode == 1:
        if '正面攻击' in pa.attack_type:
            # 期望处理
            if '背面攻击' in pa.attack_type:
                char.技能攻击力加成(part=part, x=0.04, show=False)
            else:
                char.技能攻击力加成(part=part, x=0.08, show=False)
        else:
            return '非正面攻击'


# 自定义装备：蓝灵绿玉石耳环 ， 领域之主 - 耳环
def entry_388(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['背击时，增加8%的技能伤害。']
    if mode == 0:
        pass
    if mode == 1:
        if '背面攻击' in pa.attack_type:
            if '正面攻击' in pa.attack_type:
                char.技能攻击力加成(part=part, x=0.04, show=False)
            else:
                char.技能攻击力加成(part=part, x=0.08, show=False)
        else:
            return '非背面攻击'


# 自定义装备：蓝灵绿玉石耳环 ， 领域之主 - 耳环
def entry_389(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['感电伤害 +13%']
    if mode == 0:
        char.异常增伤('感电', 0.13)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石耳环 ， 领域之主 - 耳环
def entry_390(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['光属性强化 +23']
    if mode == 0:
        char.光属性强化加成(23)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石耳环 ， 领域之主 - 耳环
def entry_391(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击速度 +20%', '施放速度 +30%']
    if mode == 0:
        char.攻击速度增加(part=part, x=0.2)
        char.施放速度增加(0.3)
        pass
    if mode == 1:
        pass


# 自定义装备：蓝灵绿玉石耳环 ， 领域之主 - 耳环
def entry_392(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['所有属性强化 +24']
    if mode == 0:
        char.所有属性强化加成(24)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 辅助装备 ， 深潜迷航脚蹼 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_393(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['破招时，随机初始化1个冷却中的1~30级技能。 (冷却时间5秒)', '- 不连续适用于同一技能。']
    if mode == 0:
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 辅助装备 ， 深潜迷航脚蹼
def entry_394(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['出血伤害 +5%', '出血抗性 +5%']
    if mode == 0:
        char.异常增伤('出血', 0.05)
        char.异常抗性加成('出血', 0.05)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 辅助装备 ， 深潜迷航脚蹼
def entry_395(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['中毒伤害 +5%', '中毒抗性 +5%']
    if mode == 0:
        char.异常增伤('中毒', 0.05)
        char.异常抗性加成('中毒', 0.05)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 辅助装备 ， 深潜迷航脚蹼
def entry_396(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +266.8%', '韧性条减少量 +10%', '眩晕持续时间 +1秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 辅助装备 ， 深潜迷航脚蹼
def entry_397(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +266.8%', '韧性条减少量 +10%', '诅咒持续时间 +1秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 辅助装备 ， 深潜迷航脚蹼
def entry_398(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +266.8%', '韧性条减少量 +10%', '石化持续时间 +1秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 魔法石 ， 深潜迷航面罩 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_399(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +8%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.08)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 魔法石 ， 深潜迷航面罩 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_400(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +2%', '被非破招攻击时，物理/魔法所受伤害 -10%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.02)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 魔法石 ， 深潜迷航面罩
def entry_401(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤伤害 +5%', '灼伤抗性 +5%']
    if mode == 0:
        char.异常增伤('灼伤', 0.05)
        char.异常抗性加成('灼伤', 0.05)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 魔法石 ， 深潜迷航面罩
def entry_402(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['感电伤害 +5%', '感电抗性 +5%']
    if mode == 0:
        char.异常增伤('感电', 0.05)
        char.异常抗性加成('感电', 0.05)
    if mode == 1:
        pass


# 自定义装备：领域之主 - 魔法石 ， 深潜迷航面罩
def entry_403(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +266.8%', '韧性条减少量 +10%', '冰冻持续时间 +1秒']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(params[0])
        pass


# 自定义装备：领域之主 - 魔法石 ， 深潜迷航面罩
def entry_404(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +266.8%', '韧性条减少量 +10%', '失明持续时间 +1秒']
    if mode == 0:
        pass
    if mode == 1:
        char.攻击强化加成(params[0])
        pass


# 自定义装备：领域之主 - 耳环 ， 深潜迷航耳环 ， 领域之主 - 短剑 ， 领域之主 - 太刀 ， 领域之主 - 钝器 ， 领域之主 - 巨剑 ， 领域之主 - 光剑 ， 领域之主 - 手套 ， 领域之主 - 臂铠 ， 领域之主 - 爪 ， 领域之主 - 拳套 ， 领域之主 - 东方棍 ， 领域之主 - 左轮枪 ， 领域之主 - 自动手枪 ， 领域之主 - 步枪 ， 领域之主 - 手炮 ， 领域之主 - 手弩 ， 领域之主 - 矛 ， 领域之主 - 棍棒 ， 领域之主 - 魔杖 ， 领域之主 - 法杖 ， 领域之主 - 扫把 ， 领域之主 - 十字架 ， 领域之主 - 念珠 ， 领域之主 - 图腾 ， 领域之主 - 镰刀 ， 领域之主 - 战斧 ， 领域之主 - 匕首 ， 领域之主 - 双剑 ， 领域之主 - 手杖 ， 领域之主 - 苦无 ， 领域之主 - 长枪 ， 领域之主 - 战戟 ， 领域之主 - 光枪 ， 领域之主 - 暗矛 ， 领域之主 - 长刀 ， 领域之主 - 小太刀 ， 领域之主 - 重剑 ， 领域之主 - 源力剑 ， 领域之主 - 玄机弓 ， 领域之主 - 强攻弩 ， 领域之主 - 妖影弓
def entry_405(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '韧性条减少量 +10%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.06)
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 耳环 ， 深潜迷航耳环
def entry_406(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +266.8%', '韧性条减少量 +10%', '睡眠持续时间 +1秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 耳环 ， 深潜迷航耳环
def entry_407(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +266.8%', '韧性条减少量 +10%', '减速持续时间 +1秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：领域之主 - 耳环 ， 深潜迷航耳环
def entry_408(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +266.8%', '韧性条减少量 +10%', '混乱持续时间 +1秒']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：森林之魔女长靴 ， 领域之主 - 鞋
def entry_409(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['物理/魔法暴击率 +12%', '辅助职业技能伤害 +5%']
    if mode == 0:
        char.暴击率增加(0.12)
        if char.bufferCarry:
            char.技能攻击力加成(0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_1731(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +281.6%', '物理/魔法所受伤害 -13%']
    if mode == 0:
        char.攻击强化加成(params[0])
        char.add_eq_params('hurted_ratio',0.13)
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_1732(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '- 需要穿戴[铭刻之誓约]', '', '所有速度 +5%', ' 灼伤抗性 +20%']
    if mode == 0:
        char.异常抗性加成('灼伤', 0.2)
        char.所有速度增加(part=part, x=0.05)
        if char.check_equ_by_name('铭刻之誓约'):
            char.技能攻击力加成(0.04)
        else:
            return '未穿戴穿戴[铭刻之誓约]'
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_1733(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['攻击强化 +222.3%', '弱点控制型异常状态和强控的韧性条减少量 +200%']
    if mode == 0:
        char.攻击强化加成(params[0])
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_1734(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['中毒伤害 +15%', '中毒抗性 +10%']
    if mode == 0:
        char.异常增伤('中毒', 0.15)
        char.异常抗性加成('中毒', 0.1)
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_1735(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['对敌人施加石化状态时，攻击强化 +444.6%，效果持续60秒。', '', '清除自身赋予敌人石化状态的物理/魔法所受伤害减少效果。']
    if mode == 0:
        char.add_eq_params('defense',5000)
        pass
    if mode == 1:
        if '石化' in pa.state_type:
            char.攻击强化加成(params[0])
        pass


# 自定义装备：防具专属词条
def entry_1736(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +7%', '- 需要穿戴[天才技术大师的加厚长靴]']
    if mode == 0:
        if char.check_equ_by_name('天才技术大师的加厚长靴'):
            char.技能攻击力加成(0.07)
        else:
            return '未穿戴穿戴[天才技术大师的加厚长靴]'
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_1737(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['出血伤害 +15%', '@[爆发契约 - 出血]@', '施加出血状态时，一次性结算出血伤害。', '- 通过转换属性施加状态时不适用']
    if mode == 0:
        char.set_eq_params('出血-结算', 1.0)
        char.异常增伤('出血', 0.15)
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_1738(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['感电伤害 +15%', '@[爆发契约 - 感电]@', '施加感电状态时，一次性结算感电伤害。', '- 通过转换属性施加状态时不适用']
    if mode == 0:
        char.异常增伤('感电', 0.15)
        char.set_eq_params('感电-结算', 1.0)
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_1739(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['生命值低于40%时，技能伤害 +6%', '攻击时，恢复550点生命值/875点魔法值。 (冷却时间1秒)', '物理/魔法防御力 +15000']
    if mode == 0:
        if pa.get_hp_rate_num(char) <= 40:
            char.技能攻击力加成(part=part, x=0.06)
        else:
            return '生命值高于40%'
        char.add_eq_params('defense',15000)
        pass
    if mode == 1:
        pass


# 自定义装备：防具专属词条
def entry_1740(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤伤害 +15%', '灼伤状态持续时间 -20%']
    if mode == 0:
        char.异常增伤('灼伤', 0.15)
        char.异常时间['灼伤'][2] -= 0.2
        pass
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_1741(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +4%', '消耗品效果持续时间 +10%', '所有异常状态抗性 +1.5%', '睡眠抗性 -1.5%']
    if mode == 0:
        char.技能攻击力加成(0.04)
        char.所有异常抗性加成(0.015)
        char.异常抗性加成('睡眠',-0.015)
        pass
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_1742(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['灼伤-冰冻联接造成的灼伤伤害 +25%']
    if mode == 0:
        char.异常结算加成['灼伤破冰'] += 0.25
        pass
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_1743(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%']
    if mode == 0:
        char.技能攻击力加成(part=part, x=0.05)
        pass
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_1744(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +6%', '所有速度 +10%']
    if mode == 0:
        char.技能攻击力加成(0.06)
        char.所有速度增加(part=part, x=0.1)
        pass
    if mode == 1:
        pass


# 自定义装备：首饰专属词条
def entry_1745(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['自身当前每适用1种异常状态，技能伤害 +1% (最多叠加4次)']
    if mode == 0:
        pass
    if mode == 1:
        num = len(list(filter(lambda i: i not in ['石化', '睡眠', '眩晕', '冰冻', ''], pa.own_type)) + ((['石化'] if '石化' in pa.own_type and 1537 in char.装备栏 else [] + ['睡眠'] if '睡眠' in pa.own_type and (1684 in char.装备栏 or 295 in char.装备栏) else []) if char.check_fun_by_id(1625) else []))
        for i in range(0, min(num, 4)):
            char.技能攻击力加成(part=part, x=0.01)
        if num < 4:
            return '自身异常状态缺少{}种'.format(4 - num)
        pass


# 自定义装备：首饰专属词条
def entry_1746(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +3%', '- 需要穿戴[永恒的心愿]', '装备的魔法值恢复效果 +15%', '所有速度 +10%', '失明抗性 +20%']
    if mode == 0:
        char.异常抗性加成('失明', 0.2)
        char.所有速度增加(0.10)
        if char.check_equ_by_name('永恒的心愿'):
            char.技能攻击力加成(0.03)
        else:
            return '未穿戴穿戴[永恒的心愿]'
        pass
    if mode == 1:
        pass


# 自定义装备：特殊装备专属词条
def entry_1747(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['回避率 +10%', '辅助职业技能冷却时间恢复速度 +20% (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        if char.类型 == "辅助":
            char.技能恢复加成(1,100,0.2, excName=char.觉醒技能)
        if char.bufferCarry:
            char.技能恢复加成(1,100,0.2, excName=char.觉醒技能)
        pass


# 自定义装备：特殊装备专属词条
def entry_1748(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['施放技能消耗10个以上无色小晶块时，技能冷却时间恢复速度 +15%，效果持续30秒。 (觉醒技能除外)']
    if mode == 0:
        pass
    if mode == 1:
        char.技能恢复加成(1, 100, 0.15, excName=char.觉醒技能)
        pass


# 自定义装备：特殊装备专属词条
def entry_1749(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['50、85、100级技能攻击力 +11%']
    if mode == 0:
        pass
    if mode == 1:
        char.技能倍率加成(50, 50, 0.11)
        char.技能倍率加成(85, 85, 0.11)
        char.技能倍率加成(100, 100, 0.11)
        pass


# 自定义装备：特殊装备专属词条
def entry_1750(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能伤害 +5%', '受到总生命值10%以上的伤害时，生成相当于生命值最大值20%的保护罩，效果持续20秒。 (冷却时间15秒)']
    if mode == 0:
        char.技能攻击力加成(0.05)
        char.set_eq_params('protect',char.get_eq_params('protect') + 0.2)
        pass
    if mode == 1:
        pass


# 自定义装备：特殊装备专属词条
def entry_1751(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['技能范围属性数值总和高于30%时，技能伤害 +6%']
    if mode == 0:
        pass
    if mode == 1:
        if char.get_eq_params('skill_range') >= 0.3:
            char.技能攻击力加成(0.06)
        else:
            return '技能范围不足30%'
        pass


# 自定义装备：蓝灵绿玉石耳环 ， 恩特精灵耳环 ， 森林之魔女耳环 ， 领域之主 - 耳环 ， 深潜迷航耳环 ， 海湾侠踪耳环
def entry_1752(char: CharacterProperty = {}, mode=0, text=False, part='', lv=0, params=[], sj=False, carry=True):
    if text:
        return ['不消耗无色小晶块的技能攻击力 +10%']
    if mode == 0:
        pass
    if mode == 1:
        char.无色技能加成(0,0.1)
        pass

