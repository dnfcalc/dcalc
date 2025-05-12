#3909d0b188e9c95311399f776e331da5
from core.basic.skill import PassiveSkill, ActiveSkill
from core.basic.character import Character



# 杰克爆弹 랜턴 파이어
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/9cb6f9ed646fa87f9b7680a42ce83d1a?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill0(ActiveSkill):
    name = "杰克爆弹"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 1
    mp = [18, 175]
    uuid = "9cb6f9ed646fa87f9b7680a42ce83d1a"    

    data1 = [0, 1902, 2098, 2287, 2485, 2674, 2866, 3062, 3256, 3451, 3643, 3835, 4031, 4219, 4410, 4607, 4799, 4995, 5187, 5379, 5574, 5768, 5959, 6154, 6343, 6540, 6730, 6926, 7120, 7312, 7507, 7699, 7890, 8085, 8276, 8471, 8663, 8857, 9051, 9245, 9438, 9632, 9823, 10018, 10210, 10399, 10596, 10788, 10982, 11176, 11366, 11562, 11756, 11949, 12143, 12332, 12527, 12719, 12913, 13109, 13299, 13493, 13687, 13879, 14076, 14266, 14462, 14652, 14846, 15038, 15232]# noqa: E501
    hit1 = 1 #TODO

# 光电鳗 플로레 비비기
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/78bd107acd474518b606be1e4fd38239?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill1(ActiveSkill):
    name = "光电鳗"
    learnLv = 5
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 2
    mp = [20, 168]
    uuid = "78bd107acd474518b606be1e4fd38239"    

    data2 = [0, 842, 928, 1015, 1100, 1188, 1273, 1358, 1443, 1528, 1615, 1702, 1787, 1875, 1960, 2043, 2128, 2219, 2304, 2387, 2475, 2557, 2647, 2727, 2815, 2902, 2987, 3074, 3162, 3244, 3330, 3419, 3500, 3587, 3670, 3760, 3847, 3929, 4017, 4104, 4187, 4274, 4362, 4446, 4532, 4621, 4702, 4791, 4874, 4962, 5049, 5129, 5221, 5304, 5387, 5474, 5561, 5646, 5732, 5814, 5904, 5989, 6074, 6159, 6246, 6333, 6419, 6506, 6588, 6674, 6763]# noqa: E501
    hit2 = 1 #TODO


# 魔法护盾 오라 실드
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/dcd536f1674630f01fc9667bb202b851?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill2(ActiveSkill):
    name = "魔法护盾"
    learnLv = 5
    masterLv = 10
    maxLv = 20
    position = 8 #TODO
    rangeLv = 3
    cd = 5
    mp = [10, 14]
    damage = False
    uuid = "dcd536f1674630f01fc9667bb202b851"    

# 替身草人 위상변화
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/0969cd4054d93da07708108c0cc1c4b5?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill3(ActiveSkill):
    name = "替身草人"
    learnLv = 10
    masterLv = 10
    maxLv = 20
    position = 7 #TODO
    rangeLv = 3
    cd = [30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11]
    mp = [20, 70]
    uuid = "0969cd4054d93da07708108c0cc1c4b5"    
    
    damage = False

# 冰霜雪人 프로스트 헤드
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/4224f9b0b8c7c903e9a1e0f9d9f6d04d?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill4(ActiveSkill):
    name = "冰霜雪人"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 1
    mp = [20, 210]
    uuid = "4224f9b0b8c7c903e9a1e0f9d9f6d04d"    
    
    data1 = [0, 2145, 2365, 2581, 2800, 3019, 3235, 3454, 3667, 3893, 4106, 4325, 4546, 4763, 4978, 5194, 5411, 5629, 5850, 6066, 6285, 6504, 6720, 6939, 7157, 7378, 7589, 7810, 8029, 8245, 8464, 8685, 8893, 9114, 9331, 9547, 9772, 9986, 10205, 10423, 10640, 10853, 11074, 11290, 11516, 11728, 11948, 12169, 12386, 12604, 12821, 13034, 13253, 13473, 13687, 13909, 14125, 14346, 14557, 14776, 14996, 15213, 15434, 15652, 15871, 16087, 16305, 16517, 16737, 16956, 17170]# noqa: E501
    hit1 = 1 #TODO


# 暗影夜猫 플루토
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/d085127b0edd719782bd618d5688f4a1?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill5(ActiveSkill):
    name = "暗影夜猫"
    learnLv = 10
    masterLv = 60
    maxLv = 70
    position = 5 #TODO
    rangeLv = 2
    cd = 1.2
    mp = [20, 210]
    uuid = "d085127b0edd719782bd618d5688f4a1"    
    
    data1 = [0, 1216, 1333, 1455, 1574, 1705, 1824, 1948, 2074, 2196, 2319, 2436, 2567, 2686, 2807, 2933, 3055, 3174, 3300, 3426, 3548, 3674, 3791, 3915, 4036, 4162, 4284, 4410, 4532, 4653, 4772, 4896, 5018, 5148, 5268, 5392, 5515, 5634, 5758, 5884, 6008, 6132, 6248, 6375, 6497, 6622, 6746, 6870, 6992, 7108, 7232, 7358, 7477, 7609, 7725, 7851, 7973, 8097, 8216, 8335, 8464, 8588, 8707, 8833, 8954, 9078, 9197, 9328, 9447, 9568, 9693]# noqa: E501
    hit1 = 2

# 魔法记忆 메모라이즈
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/42c82812f86ff6704ae9952a2e6093a4?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill6(PassiveSkill):
    name = "魔法记忆"
    learnLv = 15
    masterLv = 1
    maxLv = 11
    position = 0 #TODO
    rangeLv = 3
    uuid = "42c82812f86ff6704ae9952a2e6093a4"    

# 驱散魔法 디스인챈트
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/9bff7f2559e003766fee2853dca00631?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill7(ActiveSkill):
    name = "驱散魔法"
    learnLv = 15
    masterLv = 10
    maxLv = 20
    position = 8 #TODO
    rangeLv = 3
    cd = [0, 20, 19.5, 19.1, 18.6, 18.1, 17.6, 17.2, 16.7, 16.2, 15.7, 15.3, 14.8, 14.3, 13.8, 13.4, 12.9, 12.4, 11.9, 11.5, 11]
    mp = [30, 126]
    uuid = "9bff7f2559e003766fee2853dca00631"    
    
    damage = False


# 移动施法 이동 캐스팅
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/762c4e6d030eaf0abbfe1fec2b298574?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill8(PassiveSkill):
    name = "移动施法"
    learnLv = 15
    masterLv = 1
    maxLv = 11
    position = 1 #TODO
    rangeLv = 3
    uuid = "762c4e6d030eaf0abbfe1fec2b298574"    


# 空中施放 : 杰克爆弹 공중 랜턴 파이어
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/dc1ffbe7bfcc6dc2be737951960da9ad?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill9(PassiveSkill):
    name = "空中施放 : 杰克爆弹"
    learnLv = 15
    masterLv = 1
    maxLv = 1
    position = 3 #TODO
    rangeLv = 1
    uuid = "dc1ffbe7bfcc6dc2be737951960da9ad"    

# 烈焰冲击 플레임 스트라이크
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/c61f5a010370101402b05b21916c2071?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill10(ActiveSkill):
    name = "烈焰冲击"
    learnLv = 15
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cd = 7
    mp = [40, 462]
    uuid = "c61f5a010370101402b05b21916c2071"    
    
    data0 = [0, 6057, 6676, 7290, 7905, 8520, 9138, 9748, 10365, 10979, 11591, 12209, 12827, 13439, 14056, 14668, 15283, 15898, 16512, 17129, 17741, 18355, 18972, 19591, 20201, 20818, 21434, 22047, 22663, 23278, 23888, 24506, 25121, 25740, 26352, 26965, 27584, 28198, 28810, 29425, 30041, 30654, 31272, 31887, 32504, 33118, 33731, 34347, 34961, 35574, 36193, 36805, 37417, 38034, 38650, 39263, 39880, 40496, 41109, 41725, 42337, 42957, 43568, 44183, 44800, 45416, 46029, 46646, 47258, 47870, 48489]# noqa: E501
    hit0 = 1

# 魔法秀 쇼타임
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/9dda3f4a849dba1a288dd65e116860f2?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill11(ActiveSkill):
    name = "魔法秀"
    learnLv = 20
    masterLv = 10
    maxLv = 20
    position = 0 #TODO
    rangeLv = 3
    cd = 40
    mp = [60, 360]
    uuid = "9dda3f4a849dba1a288dd65e116860f2"    

    data1 = [0, 2.2, 4.3, 6.5, 8.6, 10.8, 13, 15.1, 17.3, 19.4, 21.6, 23.8, 25.9, 28.1, 30.2, 32.4, 32.4, 32.4, 32.4, 32.4, 32.4]# noqa: E501

    _ratio = 1

    associate = [{"type":"*cdRatio","data":data1,"skills":['冰墙', '元素之门', '元素之幕', '元素震荡', '圣灵水晶', '烈焰冲击','天雷', '雷旋', '杰克降临', '湮灭黑洞', '极冰盛宴', '虚无之球', '光与暗的交响']}]

    @property
    def ratio(self):
        return self._ratio

    @ratio.setter
    def ratio(self, value):
        if self._ratio != value:
            data = self.associate[0]
            ratio = (1 - data['data'][self.lv] / 100 * value) / (1 - data['data'][self.lv] / 100 * self._ratio) 
            for item in data['skills']:
                skill = self.char.GetSkillByName(item)
                if skill is not None:
                    skill.cdRatio *= ratio
            self._ratio = value

    # 技能等级变化的时候，系数对应的数值变化
    def update_skill_attribute(self,skill, type, old, new, data,ratio = 100,weapon = []):
        super().update_skill_attribute(skill, type, old, new, data, ratio / self.ratio, weapon)


# 虚无之球 보이드
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/5dc7008b12a459325b548b0715c6b73c?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill12(ActiveSkill):
    name = "虚无之球"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cd = 6
    mp = [60, 616]
    uuid = "5dc7008b12a459325b548b0715c6b73c"    
    
    data1 = [0, 974, 1071, 1176, 1272, 1367, 1465, 1566, 1663, 1760, 1860, 1962, 2057, 2159, 2256, 2356, 2453, 2553, 2654, 2747, 2853, 2948, 3050, 3142, 3245, 3342, 3443, 3541, 3645, 3735, 3837, 3936, 4036, 4129, 4233, 4327, 4427, 4522, 4627, 4726, 4823, 4925, 5025, 5119, 5214, 5318, 5413, 5518, 5612, 5714, 5809, 5911, 6006, 6108, 6202, 6307, 6404, 6501, 6603, 6700, 6800, 6894, 6999, 7094, 7191, 7295, 7392, 7489, 7585, 7687, 7788]# noqa: E501
    hit1 = 8

# 元素点燃 엘레멘탈 번
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/da6e37c1e3f0e8867f70007d89c239ff?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill13(ActiveSkill):
    name = "元素点燃"
    learnLv = 20
    masterLv = 15
    maxLv = 25
    position = 5 #TODO
    rangeLv = 3
    cd = 5
    mp = [194, 1840]
    uuid = "da6e37c1e3f0e8867f70007d89c239ff"    
    
    damage = False

# 冰墙 칠링 팬스
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/de3fea2d65c597f4d55c70a02b97fc79?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill14(ActiveSkill):
    name = "冰墙"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cd = 15
    mp = [60, 616]
    uuid = "de3fea2d65c597f4d55c70a02b97fc79"    

    data0 = [0, 15018, 16539, 18057, 19577, 21112, 22625, 24147, 25667, 27198, 28720, 30240, 31761, 33279, 34809, 36332, 37849, 39370, 40904, 42422, 43943, 45463, 46991, 48510, 50031, 51551, 53088, 54604, 56127, 57645, 59177, 60699, 62213, 63735, 65272, 66783, 68303, 69822, 71358, 72877, 74399, 75917, 77447, 78970, 80488, 82008, 83541, 85065, 86581, 88101, 89629, 91149, 92670, 94190, 95724, 97242, 98765, 100283, 101813, 103335, 104853, 106374, 107899, 109421, 110942, 112460, 113990, 115515, 117035, 118565, 120080]# noqa: E501
    hit0 = 1 #TODO

# 雷旋 썬버스트
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/3829c15bf5f520c13998a3479ba0ce7b?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill15(ActiveSkill):
    name = "雷旋"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cd = 8
    mp = [40, 462]
    uuid = "3829c15bf5f520c13998a3479ba0ce7b"    

    data1 = [0, 10715, 11801, 12888, 13976, 15062, 16148, 17236, 18323, 19409, 20497, 21583, 22670, 23758, 24844, 25932, 27020, 28106, 29192, 30280, 31367, 32453, 33541, 34627, 35714, 36802, 37888, 38974, 40062, 41150, 42237, 43325, 44411, 45497, 46585, 47671, 48758, 49846, 50932, 52018, 53106, 54193, 55279, 56369, 57455, 58541, 59629, 60716, 61802, 62890, 63976, 65062, 66150, 67237, 68323, 69411, 70499, 71585, 72673, 73760, 74846, 75934, 77020, 78107, 79195, 80281, 81367, 82455, 83541, 84628, 85717]# noqa: E501
    hit1 = 1 #TODO

# 属性精通 속성 마스터리
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/96c8ddd388e1b08e7fc98c5041382e26?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill16(PassiveSkill):
    name = "属性精通"
    learnLv = 30
    masterLv = 5
    maxLv = 15
    position = 1 #TODO
    rangeLv = 7
    uuid = "96c8ddd388e1b08e7fc98c5041382e26"    

    data0 = [0, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]# noqa: E501

    _ratio = 1

    associate = [{"type":"*skillRation","data":data0}]

    @property
    def ratio(self):
        return self._ratio

    @ratio.setter
    def ratio(self, value):
        if self._ratio != value:
            data = self.associate[0]
            ratio = (1 + data['data'][self.lv] / 100 * value) / (1 + data['data'][self.lv] / 100 * self._ratio)
            for item in self.char.GetSkillNames('all', True):
                skill = self.char.GetSkillByName(item)
                if skill is not None:
                    skill.skillRation *= ratio
            self._ratio = value

    # 技能等级变化的时候，系数对应的数值变化
    def update_skill_attribute(self,skill, type, old, new, data,ratio = 100,weapon = []):
        super().update_skill_attribute(skill, type, old, new, data, ratio / self.ratio, weapon)

# 天雷 썬더 콜링
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/d2c6df5105577fb59fb92529a36165a0?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill17(ActiveSkill):
    name = "天雷"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 6 #TODO
    rangeLv = 2
    cube = 1
    cd = 15
    mp = [125, 436]
    uuid = "d2c6df5105577fb59fb92529a36165a0"    

    data2 = [0, 6170, 6795, 7421, 8048, 8675, 9299, 9927, 10551, 11180, 11805, 12431, 13058, 13682, 14310, 14933, 15560, 16185, 16812, 17439, 18065, 18687, 19316, 19941, 20568, 21194, 21818, 22449, 23072, 23702, 24324, 24950, 25577, 26202, 26828, 27456, 28082, 28707, 29333, 29958, 30585, 31209, 31838, 32460, 33089, 33714, 34340, 34967, 35592, 36218, 36843, 37469, 38097, 38724, 39350, 39977, 40601, 41229, 41852, 42479, 43106, 43731, 44357, 44984, 45609, 46233, 46860, 47486, 48113, 48740, 49365]# noqa: E501
    hit2 = 3


# 天雷冲击 썬더 스트라이크
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/a3c4f89a129ebd16896961fd273181e8?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill18(PassiveSkill):
    name = "天雷冲击"
    learnLv = 35
    masterLv = 1
    maxLv = 1
    line = 40
    position = 6 #TODO
    rangeLv = 2
    uuid = "a3c4f89a129ebd16896961fd273181e8"    

    data0 = [0, 55]# noqa: E501
    associate = [
        {"type":"+cd","data":[0,5],"skills":["天雷"],"ratio":1},
        {"type":"*skillRation","data":data0,"skills":["天雷"]}
    ]

# 湮灭黑洞 나이트 할로우
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/202edb928046f4fa6dedf6337377efd5?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill19(ActiveSkill):
    name = "湮灭黑洞"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 3 #TODO
    rangeLv = 2
    cube = 2
    cd = 35
    mp = [300, 2520]
    uuid = "202edb928046f4fa6dedf6337377efd5"    

    
    data3 = [0, 2081, 2294, 2502, 2714, 2925, 3140, 3348, 3560, 3771, 3984, 4191, 4404, 4614, 4830, 5039, 5250, 5459, 5672, 5882, 6095, 6303, 6518, 6728, 6938, 7148, 7361, 7574, 7785, 7994, 8207, 8417, 8627, 8838, 9050, 9258, 9474, 9684, 9897, 10104, 10317, 10529, 10739, 10950, 11163, 11372, 11585, 11795, 12009, 12218, 12429, 12641, 12854, 13061, 13274, 13484, 13700, 13908, 14120, 14328, 14541, 14751, 14964, 15173, 15387, 15597, 15809, 16019, 16232, 16443, 16655]# noqa: E501
    hit3 = 15
    
    data5 = [0, 10421, 11480, 12531, 13587, 14648, 15702, 16760, 17820, 18876, 19934, 20988, 22047, 23103, 24161, 25220, 26276, 27333, 28392, 29447, 30503, 31563, 32621, 33674, 34734, 35790, 36846, 37902, 38961, 40016, 41075, 42132, 43191, 44247, 45305, 46361, 47417, 48476, 49533, 50589, 51650, 52706, 53762, 54815, 55877, 56930, 57987, 59046, 60104, 61160, 62219, 63273, 64331, 65388, 66447, 67503, 68559, 69620, 70676, 71730, 72791, 73847, 74903, 75962, 77019, 78074, 79134, 80187, 81243, 82301, 83360]# noqa: E501
    hit5 = 1 #TODO

    mode = ["满","秒炸"]

    def setMode(self, mode):
        if mode == "秒C":
            self.hit3 = 2

# 极冰盛宴 아크틱 피스트
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/2a3c96b88d02372505692da0a8b54743?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill20(ActiveSkill):
    name = "极冰盛宴"
    learnLv = 40
    masterLv = 60
    maxLv = 70
    position = 4 #TODO
    rangeLv = 2
    cube = 2
    cd = 19
    mp = [380, 3192]
    uuid = "2a3c96b88d02372505692da0a8b54743"    

    data1 = [0, 2984, 3285, 3587, 3890, 4194, 4494, 4797, 5099, 5405, 5705, 6008, 6311, 6611, 6917, 7217, 7518, 7823, 8126, 8427, 8730, 9030, 9336, 9639, 9941, 10242, 10548, 10850, 11148, 11456, 11754, 12060, 12362, 12663, 12968, 13271, 13574, 13874, 14177, 14480, 14781, 15086, 15387, 15692, 15992, 16295, 16596, 16901, 17204, 17505, 17805, 18110, 18411, 18716, 19017, 19319, 19625, 19926, 20231, 20528, 20837, 21137, 21438, 21741, 22043, 22347, 22650, 22950, 23253, 23558, 23859]# noqa: E501
    hit1 = 8

# 杰克降临 핼로윈 버스터
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/8ee0099656df08a0b39225f8a21d514b?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill21(ActiveSkill):
    name = "杰克降临"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 2 #TODO
    rangeLv = 2
    cube = 2
    cd = 45
    mp = [160, 1344]
    uuid = "8ee0099656df08a0b39225f8a21d514b"    

    data1 = [0, 9135, 10064, 10991, 11921, 12842, 13770, 14700, 15624, 16556, 17478, 18405, 19335, 20261, 21191, 22115, 23040, 23972, 24894, 25826, 26751, 27681, 28602, 29529, 30461, 31386, 32315, 33245, 34164, 35096, 36021, 36951, 37875, 38801, 39729, 40655, 41586, 42510, 43439, 44369, 45291, 46221, 47145, 48074, 49004, 49926, 50858, 51780, 52712, 53636, 54564, 55490, 56417, 57345, 58272, 59198, 60128, 61052, 61982, 62906, 63834, 64763, 65687, 66617, 67541, 68466, 69395, 70325, 71256, 72177, 73103]# noqa: E501
    hit1 = 1 #TODO
    
    data2 = [0, 36552, 40262, 43968, 47675, 51386, 55092, 58800, 62511, 66219, 69927, 73637, 77342, 81051, 84762, 88469, 92172, 95885, 99593, 103301, 107009, 110721, 114425, 118136, 121842, 125552, 129260, 132969, 136677, 140387, 144089, 147801, 151508, 155217, 158928, 162633, 166341, 170054, 173759, 177468, 181179, 184886, 188592, 192299, 196011, 199719, 203423, 207137, 210845, 214548, 218261, 221967, 225674, 229386, 233091, 236799, 240512, 244218, 247928, 251633, 255342, 259053, 262757, 266469, 270179, 273882, 277592, 281301, 285008, 288720, 292424]# noqa: E501
    hit2 = 1 #TODO
    

# 魔力增幅 마력 증폭
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/8510294202d0e042dd29a2422fc6770d?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill22(PassiveSkill):
    name = "魔力增幅"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "8510294202d0e042dd29a2422fc6770d"    

    data0 = [0, 9, 10.5, 12, 13.5, 15, 16.5, 18, 19.5, 21, 22.5, 24, 25.5, 27, 28.5, 30, 31.5, 33, 34.5, 36, 37.5, 39, 40.5, 42, 43.5, 45, 46.5, 48, 49.5, 51, 52.5, 54, 55.5, 57, 58.5, 60, 61.5, 63, 64.5, 66, 67.5, 69, 70.5, 72, 73.5, 75, 76.5, 78, 79.5, 81, 82.5]# noqa: E501
    
    associate = [{"type":"$*PAtkM","data":data0}]

# 陨星幻灭 애스트럴 스톰
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/b3659936a9a74c4ed6f7faf07cca1f9e?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill23(ActiveSkill):
    name = "陨星幻灭"
    learnLv = 50
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 5
    cube = 5
    cd = 145
    mp = [1200, 10080]
    uuid = "b3659936a9a74c4ed6f7faf07cca1f9e"    

    data0 = [0, 275, 339, 403, 466, 530, 594, 658, 721, 785, 849, 913, 976, 1040, 1104, 1168, 1232, 1295, 1359, 1423, 1487, 1550, 1614, 1678, 1742, 1805, 1869, 1933, 1997, 2061, 2124, 2188, 2252, 2316, 2379, 2443, 2507, 2571, 2634, 2698, 2762, 2826, 2890, 2953, 3017, 3081, 3145, 3208, 3272, 3336, 3400]# noqa: E501
    hit0 = 40
    
    data1 = [0, 1100, 1354, 1609, 1864, 2119, 2374, 2629, 2884, 3139, 3394, 3649, 3904, 4159, 4414, 4669, 4924, 5179, 5434, 5689, 5944, 6199, 6454, 6709, 6964, 7219, 7474, 7728, 7983, 8238, 8493, 8748, 9003, 9258, 9513, 9768, 10023, 10278, 10533, 10788, 11043, 11298, 11553, 11808, 12063, 12318, 12573, 12828, 13083, 13338, 13593]# noqa: E501
    hit1 = 40
    
    data4 = [0, 2199, 2708, 3218, 3728, 4238, 4748, 5257, 5767, 6277, 6787, 7297, 7806, 8316, 8826, 9336, 9846, 10355, 10865, 11375, 11885, 12395, 12904, 13414, 13924, 14434, 14944, 15453, 15963, 16473, 16983, 17493, 18002, 18512, 19022, 19532, 20042, 20552, 21061, 21571, 22081, 22591, 23101, 23610, 24120, 24630, 25140, 25650, 26159, 26669, 27179]# noqa: E501
    hit4 = 5
    
    data5 = [0, 8794, 10833, 12873, 14912, 16951, 18990, 21029, 23069, 25108, 27147, 29186, 31226, 33265, 35304, 37343, 39382, 41422, 43461, 45500, 47539, 49579, 51618, 53657, 55696, 57735, 59775, 61814, 63853, 65892, 67932, 69971, 72010, 74049, 76088, 78128, 80167, 82206, 84245, 86285, 88324, 90363, 92402, 94441, 96481, 98520, 100559, 102598, 104637, 106677, 108716]# noqa: E501
    hit5 = 5

# 元素之幕 엘레멘탈 커튼
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/d429147c372b549c3dadcabcba50787f?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill24(ActiveSkill):
    name = "元素之幕"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 2
    cube = 2
    cd = 30
    mp = [400, 1000]
    uuid = "d429147c372b549c3dadcabcba50787f"    

    data3 = [0, 1709, 1884, 2055, 2229, 2403, 2577, 2753, 2924, 3098, 3272, 3444, 3617, 3792, 3965, 4137, 4313, 4485, 4659, 4832, 5006, 5178, 5354, 5525, 5700, 5874, 6047, 6221, 6393, 6567, 6743, 6914, 7088, 7262, 7436, 7607, 7782, 7955, 8129, 8303, 8475, 8651, 8823, 8996, 9170, 9344, 9515, 9690, 9864, 10037, 10212]# noqa: E501
    hit3 = 20
    data4 = [0, 8550, 9419, 10286, 11151, 12020, 12888, 13757, 14621, 15489, 16358, 17225, 18092, 18960, 19827, 20694, 21561, 22430, 23298, 24165, 25031, 25899, 26766, 27635, 28503, 29367, 30236, 31104, 31973, 32838, 33707, 34574, 35442, 36308, 37176, 38045, 38913, 39777, 40646, 41514, 42381, 43250, 44115, 44984, 45851, 46719, 47586, 48453, 49320, 50189, 51056]# noqa: E501
    hit4 = 1 #TODO

# 元素震荡 엘레멘탈 퀘이크
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/0113c8b1306ca76d208f83f2d093dd62?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill25(ActiveSkill):
    name = "元素震荡"
    learnLv = 70
    masterLv = 40
    maxLv = 50
    position = 3 #TODO
    rangeLv = 2
    cube = 3
    cd = 50
    mp = [860, 1500]
    uuid = "0113c8b1306ca76d208f83f2d093dd62"    

    data1 = [0, 10629, 11711, 12786, 13868, 14948, 16026, 17102, 18185, 19263, 20340, 21417, 22499, 23576, 24659, 25736, 26813, 27890, 28976, 30050, 31133, 32207, 33290, 34364, 35447, 36524, 37601, 38682, 39762, 40838, 41919, 42996, 44076, 45155, 46235, 47310, 48393, 49469, 50546, 51627, 52703, 53784, 54858, 55943, 57015, 58101, 59180, 60257, 61332, 62415, 63492]# noqa: E501
    hit1 = 3
    
    data2 = [0, 47850, 52703, 57558, 62415, 67271, 72122, 76977, 81837, 86685, 91539, 96396, 101247, 106104, 110960, 115814, 120668, 125525, 130380, 135230, 140088, 144942, 149796, 154650, 159507, 164358, 169215, 174069, 178926, 183779, 188631, 193490, 198341, 203198, 208052, 212906, 217761, 222618, 227469, 232323, 237182, 242036, 246890, 251744, 256602, 261450, 266304, 271163, 276014, 280871, 285726]# noqa: E501
    hit2 = 1 #TODO


# 元素奥义 엘레멘탈 포텐셜
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/03bb5314ffd41e9458d67ef924fef38f?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill26(PassiveSkill):
    name = "元素奥义"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 0 #TODO
    rangeLv = 3
    uuid = "03bb5314ffd41e9458d67ef924fef38f"    

    data0 = [0, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118]# noqa: E501
    
    associate = [{"type":"*skillRation","data":data0}]

# 圣灵符文 초월의 룬
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/bb34e8854a93fd250347a1c64119f7ab?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill27(ActiveSkill):
    name = "圣灵符文"
    learnLv = 75
    masterLv = 1
    maxLv = 11
    position = 1 #TODO
    rangeLv = 3
    cd = 5
    mp = [2320, 6800]
    uuid = "bb34e8854a93fd250347a1c64119f7ab"    
    data0 = [0, 16, 17.4, 18.8, 20.1, 21.6, 22.9, 24.4, 25.7, 27.2, 28.5, 29.9]# noqa: E501
    
    data2 = [0, 13.1, 14.4, 15.6, 16.9, 18.1, 19.4, 20.6, 21.9, 23.1, 24.4, 25.6]# noqa: E501
    
    associate = [
        {"type":"+ratio","data":data0,"skills":["魔法秀"]},
        {"type":"+ratio","data":data2,"skills":["属性精通"]}
    ]


# 圣灵水晶 초월의 크리스탈
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/97972dba4694d6c0fcd2f7e8efb3a499?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill28(ActiveSkill):
    name = "圣灵水晶"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 2
    cube = 3
    cd = 40
    mp = [580, 4500]
    uuid = "97972dba4694d6c0fcd2f7e8efb3a499"    

    data1 = [0, 78396, 86348, 94302, 102255, 110210, 118162, 126112, 134066, 142019, 149975, 157928, 165881, 173833, 181789, 189739, 197691, 205645, 213597, 221552, 229506, 237460, 245413, 253366, 261316, 269273, 277224, 285176, 293130, 301086, 309039, 316993, 324943, 332897, 340851, 348804, 356757, 364709, 372666, 380618, 388569, 396522, 404475, 412428, 420383, 428336, 436289, 444243, 452197, 460147, 468102]# noqa: E501
    hit1 = 1 #TODO


# 元素之门 더 게이트
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/1dad88963abdc96b091fcab185a8820d?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill29(ActiveSkill):
    name = "元素之门"
    learnLv = 80
    masterLv = 40
    maxLv = 50
    position = 4 #TODO
    rangeLv = 2
    cube = 5
    cd = 45
    mp = [800, 6000]
    uuid = "1dad88963abdc96b091fcab185a8820d"    

    data3 = [0, 8206, 9042, 9874, 10707, 11539, 12377, 13199, 14034, 14866, 15701, 16540, 17363, 18203, 19035, 19869, 20701, 21533, 22364, 23198, 24022, 24859, 25693, 26524, 27361, 28194, 29030, 29856, 30693, 31525, 32360, 33197, 34017, 34856, 35686, 36523, 37355, 38191, 39018, 39853, 40684, 41521, 42358, 43190, 44015, 44846, 45685, 46508, 47348, 48181, 49014]# noqa: E501
    hit3 = 10
    # 根据外门数量的攻击力最大增幅率110%
    skillRation = 1.1

# 第六元素 제6원소
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/147d005ac868e0de52b1f255eea35d62?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill30(ActiveSkill):
    name = "第六元素"
    learnLv = 85
    masterLv = 40
    maxLv = 50
    position = 6 #TODO
    rangeLv = 5
    cube = 10
    cd = 180
    mp = [2500, 8000]
    uuid = "147d005ac868e0de52b1f255eea35d62"    

    data0 = [0, 3792, 4673, 5551, 6430, 7305, 8190, 9065, 9944, 10824, 11704, 12581, 13463, 14340, 15219, 16094, 16980, 17853, 18737, 19614, 20493, 21380, 22256, 23136, 24010, 24897, 25772, 26652, 27530, 28410, 29286, 30169, 31045, 31925, 32800, 33684, 34559, 35437, 36318, 37197, 38076, 38961, 39836, 40716, 41594, 42474, 43353, 44236, 45112, 45992, 46867]# noqa: E501
    hit0 = 20
    
    data2 = [0, 176927, 217951, 258984, 300005, 341036, 382064, 423088, 464117, 505146, 546169, 587199, 628226, 669255, 710285, 751311, 792337, 833367, 874393, 915422, 956447, 997471, 1038503, 1079526, 1120558, 1161587, 1202610, 1243642, 1284672, 1325694, 1366722, 1407750, 1448777, 1489811, 1530828, 1571857, 1612887, 1653913, 1694944, 1735970, 1776996, 1818025, 1859052, 1900081, 1941109, 1982136, 2023166, 2064185, 2105215, 2146246, 2187270]# noqa: E501
    hit2 = 1 #TODO

# 元素之源 어시밀레이트
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/73f7da7230b46b3ff471e00d77e836cf?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill31(PassiveSkill):
    name = "元素之源"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 3
    uuid = "73f7da7230b46b3ff471e00d77e836cf"    

    data0 = [0, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118]# noqa: E501
    
    associate = [{"type":"*skillRation","data":data0}]

# 光与暗的交响 썬더 레이지
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/bdb73ed79f64fbfa8024978ac7f2e0f2?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill32(ActiveSkill):
    name = "光与暗的交响"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 7 #TODO
    rangeLv = 2
    cube = 7
    cd = 60
    mp = [833, 2666]
    uuid = "bdb73ed79f64fbfa8024978ac7f2e0f2"    

    data1 = [0, 11800, 12998, 14196, 15394, 16590, 17788, 18986, 20181, 21378, 22577, 23774, 24970, 26169, 27367, 28563, 29758, 30958, 32155, 33351, 34550, 35747, 36943, 38140, 39338, 40535, 41731, 42929, 44127, 45323, 46521, 47719, 48916, 50114, 51310, 52508, 53706, 54902, 56098, 57296, 58494, 59690, 60888, 62087, 63283, 64479, 65678, 66875, 68072, 69269, 70467]# noqa: E501
    hit1 = 15

# 宇宙寂灭 : 冰火之歌 코스믹 캘러미티
# https://api.neople.co.kr/df/skills/3909d0b188e9c95311399f776e331da5/86950d7f2717ec59633999187e4a2c16?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill33(ActiveSkill):
    name = "宇宙寂灭 : 冰火之歌"
    learnLv = 100
    masterLv = 40
    maxLv = 50
    position = 5 #TODO
    rangeLv = 5
    cube = 15
    cd = 290
    mp = [4027, 12888]
    uuid = "86950d7f2717ec59633999187e4a2c16"    
    
    data0 = [0, 405134, 499075, 593022, 686967, 780909, 874855, 968800, 1062745, 1156688, 1250629, 1344576, 1438522, 1532464, 1626409, 1720352, 1814297, 1908243, 2002185, 2096130, 2190076, 2284018, 2377964, 2471907, 2565850, 2659798, 2753739, 2847685, 2941627, 3035574, 3129519, 3223460, 3317406, 3411349, 3505294, 3599238, 3693183, 3787127, 3881073, 3975015, 4068962, 4162902, 4256850, 4350792, 4444737, 4538682, 4632624, 4726570, 4820515, 4914456, 5008404]# noqa: E501
    hit0 = 1 #TODO
    
    data1 = [0, 38585, 47531, 56478, 65426, 74372, 83320, 92267, 101213, 110161, 119107, 128054, 137002, 145948, 154898, 163843, 172789, 181737, 190684, 199633, 208578, 217524, 226473, 235419, 244369, 253314, 262261, 271208, 280154, 289103, 298049, 306996, 315944, 324890, 333838, 342784, 351732, 360678, 369626, 378574, 387520, 396467, 405413, 414361, 423309, 432256, 441203, 450149, 459096, 468044, 476992]# noqa: E501
    hit1 = 7
    
class classChange(Character):
    def __init__(self, equVersion):
        self.name = 'elementalist'
        self.nameCN = '知源·元素师'
        self.role = 'mage_female'

        self.武器选项 = ['魔杖', '法杖', '矛', '棍棒']
        self.输出类型选项 = ['魔法百分比']
        self.输出类型 = '魔法百分比'
        self.防具精通属性 = ['智力']
        self.防具类型 = '布甲'
        self.buff = 1.922

        self.角色 = '魔法师(女)'

        self.职业 = '元素师'

        super().__init__(equVersion, __name__)
