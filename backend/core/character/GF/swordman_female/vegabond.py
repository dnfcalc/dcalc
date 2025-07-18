#1645c45aabb008c98406b3a16447040d
from core.basic.roleinfo import CharacterEquipInfo
from core.basic.skill import PassiveSkill, ActiveSkill
from core.basic.character import Character
from core.basic.formula import 武器强化计算, 锻造计算

# 光剑掌握 광검 사용 가능
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/1812a1ece67bb37b6b44b54766450064?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill0(PassiveSkill):
    name = "光剑掌握"
    learnLv = 1
    masterLv = 1
    maxLv = 1
    position = 7
    rangeLv = 1
    uuid = "1812a1ece67bb37b6b44b54766450064"

    data0 = [0, 10]# noqa: E501

    associate = [
        {"data":data0,"type":"*cdReduce", 'exceptSkills': ['花开寒影', '飞花逐月', '轻云出月风静夜']}
    ]

# 返本归元 삼화취정
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/e49e57b2e8fbeceb0a2c56a0c63fe6c5?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill1(PassiveSkill):
    name = "返本归元"
    learnLv = 20
    masterLv = 1
    maxLv = 11
    position = 2
    rangeLv = 2
    uuid = "e49e57b2e8fbeceb0a2c56a0c63fe6c5"

    data0 = [0, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60]# noqa: E501
    associate = [
        {"data":data0,"type":"*skillRation"}
    ]


# 四象引 흡기
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/0b8db1e10b3abbd24d38564e708675d5?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill2(ActiveSkill):
    name = "四象引"
    learnLv = 20
    masterLv = 60
    maxLv = 70
    position = 0
    rangeLv = 2
    cd = 7
    mp = [20, 250]
    uuid = "0b8db1e10b3abbd24d38564e708675d5"

    data0 = [0, 9282, 10234, 11137, 12094, 13042, 13967, 14918, 15873, 16822, 17746, 18697, 19621, 20555, 21503, 22454, 23382, 24334, 25282, 26236, 27146, 28089, 29039, 29973, 30918, 31870, 32795, 33750, 34695, 35600, 36553, 37505, 38456, 39382, 40334, 41281, 42211, 43143, 44091, 45021, 45971, 46923, 47872, 48799, 49749, 50694, 51605, 52559, 53502, 54432, 55384, 56333, 57265, 58210, 59160, 60088, 61018, 61965, 62924, 63855, 64799, 65748, 66654, 67609, 68556, 69510, 70431, 71385, 72335, 73260, 74210]# noqa: E501
    hit0 = 1

# 一花渡江 일화도강
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/8572675ec6a1f50b6eff6a867376c2de?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill3(ActiveSkill):
    name = "一花渡江"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 2
    rangeLv = 2
    cd = 6
    mp = [40, 300]
    uuid = "8572675ec6a1f50b6eff6a867376c2de"

    data0 = [0, 2832, 3116, 3403, 3689, 3981, 4267, 4553, 4840, 5127, 5415, 5700, 5991, 6276, 6564, 6848, 7138, 7424, 7711, 7997, 8286, 8573, 8860, 9146, 9433, 9719, 10010, 10299, 10583, 10870, 11157, 11444, 11730, 12019, 12305, 12594, 12878, 13168, 13454, 13741, 14027, 14314, 14603, 14890, 15179, 15463, 15751, 16036, 16327, 16612, 16900, 17185, 17473, 17760, 18047, 18336, 18622, 18909, 19195, 19485, 19771, 20057, 20342, 20631, 20915, 21206, 21493, 21780, 22068, 22352, 22642]# noqa: E501
    hit0 = 3


# 樱落斩 비상
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/4f2e001e9a19eb7bae50ad1840dfb329?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill4(ActiveSkill):
    name = "樱落斩"
    learnLv = 25
    masterLv = 60
    maxLv = 70
    position = 4
    rangeLv = 2
    cd = 7
    mp = [35, 350]
    uuid = "4f2e001e9a19eb7bae50ad1840dfb329"

    data0 = [0, 1110, 1214, 1331, 1445, 1573, 1671, 1797, 1906, 2015, 2139, 2242, 2360, 2474, 2589, 2698, 2812, 2934, 3038, 3160, 3273, 3386, 3500, 3614, 3730, 3840, 3958, 4072, 4184, 4304, 4410, 4527, 4646, 4753, 4872, 4979, 5100, 5212, 5323, 5440, 5552, 5663, 5778, 5901, 6001, 6127, 6237, 6356, 6465, 6576, 6700, 6802, 6919, 7031, 7143, 7266, 7373, 7492, 7604, 7720, 7829, 7944, 8063, 8174, 8289, 8400, 8515, 8638, 8740, 8862, 8978]# noqa: E501
    hit0 = 1

    data1 = [0, 1484, 1630, 1775, 1926, 2084, 2234, 2380, 2542, 2691, 2842, 2987, 3152, 3300, 3448, 3602, 3755, 3905, 4049, 4208, 4362, 4522, 4667, 4816, 4969, 5119, 5270, 5423, 5576, 5732, 5877, 6040, 6186, 6338, 6487, 6644, 6797, 6941, 7098, 7249, 7405, 7555, 7711, 7856, 8007, 8155, 8310, 8463, 8617, 8767, 8923, 9076, 9221, 9376, 9525, 9683, 9829, 9982, 10134, 10290, 10443, 10596, 10749, 10894, 11050, 11196, 11353, 11512, 11654, 11810, 11961]# noqa: E501
    hit1 = 1

    data2 = [0, 422, 466, 508, 547, 600, 636, 687, 726, 767, 811, 853, 899, 944, 981, 1030, 1069, 1117, 1163, 1205, 1243, 1292, 1331, 1382, 1425, 1459, 1510, 1549, 1595, 1635, 1676, 1726, 1770, 1809, 1856, 1896, 1945, 1986, 2033, 2071, 2113, 2156, 2203, 2242, 2288, 2331, 2377, 2417, 2462, 2502, 2553, 2594, 2633, 2684, 2723, 2764, 2810, 2848, 2895, 2941, 2984, 3031, 3075, 3114, 3157, 3203, 3245, 3290, 3329, 3378, 3417]# noqa: E501
    hit2 = 8

    data3 = [0, 2946, 3247, 3548, 3852, 4168, 4454, 4769, 5073, 5381, 5683, 5977, 6285, 6589, 6888, 7205, 7506, 7813, 8109, 8417, 8713, 9025, 9326, 9627, 9945, 10229, 10543, 10849, 11150, 11458, 11752, 12063, 12362, 12665, 12981, 13284, 13586, 13887, 14188, 14493, 14800, 15101, 15400, 15717, 16006, 16320, 16621, 16929, 17241, 17532, 17845, 18139, 18448, 18758, 19057, 19365, 19659, 19965, 20267, 20573, 20881, 21177, 21491, 21779, 22095, 22403, 22698, 23013, 23302, 23616, 23919]# noqa: E501
    hit3 = 1

# 圆舞斩 극검
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/b8f4966608e4ebb3cc80ba4eac3649bb?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill5(ActiveSkill):
    name = "圆舞斩"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 11
    mp = [70, 400]
    uuid = "b8f4966608e4ebb3cc80ba4eac3649bb"

    data0 = [0, 7060, 7778, 8495, 9212, 9920, 10637, 11356, 12072, 12793, 13507, 14227, 14943, 15649, 16369, 17085, 17802, 18520, 19239, 19958, 20672, 21383, 22095, 22812, 23533, 24245, 24966, 25680, 26398, 27112, 27829, 28548, 29257, 29976, 30700, 31411, 32127, 32841, 33563, 34275, 34995, 35714, 36431, 37143, 37851, 38571, 39287, 40006, 40727, 41441, 42158, 42862, 43581, 44297, 45016, 45733, 46449, 47170, 47891, 48601, 49309, 50033, 50745, 51459, 52182, 52899, 53616, 54329, 55044, 55763, 56477]# noqa: E501
    hit0 = 2

# 碎岩裂地掌 거압
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/d53301bb328baf12a3ae482cc6a565dd?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill6(ActiveSkill):
    name = "碎岩裂地掌"
    learnLv = 30
    masterLv = 60
    maxLv = 70
    position = 1
    rangeLv = 2
    cd = 12
    mp = [60, 390]
    uuid = "d53301bb328baf12a3ae482cc6a565dd"

    data0 = [0, 15094, 16618, 18149, 19681, 21211, 22744, 24276, 25808, 27341, 28868, 30401, 31928, 33465, 34989, 36526, 38048, 39590, 41109, 42656, 44181, 45711, 47243, 48773, 50305, 51828, 53365, 54886, 56423, 57950, 59490, 61016, 62553, 64076, 65610, 67136, 68675, 70200, 71735, 73258, 74802, 76328, 77860, 79390, 80923, 82453, 83982, 85512, 87037, 88572, 90098, 91644, 93163, 94695, 96232, 97759, 99292, 100822, 102350, 103884, 105409, 106950, 108475, 110012, 111534, 113069, 114597, 116134, 117657, 119196, 120720]# noqa: E501
    hit0 = 1 #TODO

# 乱花葬 난화검
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/7e904ea3d2a9faa054604e55120a9268?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill7(ActiveSkill):
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
    vps = [
          {
            "name": "花无语",
            "desc": "攻击时间减少<br/>追加强制控制功能",
            "explain": "[乱花葬]<br/>连续斩击后， 一击斩断花朵， 结束攻击<br/>- 连续斩击速度 + 30%<br/>- 删除念气之花散开攻击、 念气之花爆炸<br/>- 总攻击力相同<br/><br/>被最后斩击命中的敌人将进入强制控制状态3秒"
          },
          {
            "name": "万紫千红",
            "desc": "追加聚集敌人<br/>范围增加",
            "explain": "[乱花葬]<br/>前冲动作可以击退霸体状态的敌人<br/><br/>连续攻击命中的敌人会被吸附至花中的中心位置<br/><br/>攻击范围 45%"
          }
        ]
    data0 = [0, 690, 801, 911, 1019, 1131, 1242, 1349, 1461, 1569, 1680, 1794, 1901, 2010, 2121, 2231, 2345, 2450, 2559, 2672, 2781, 2894, 3003, 3111, 3222, 3332, 3441, 3552, 3662, 3770, 3881, 3992, 4104, 4209, 4322, 4433, 4542, 4652, 4761, 4871, 4983, 5091, 5202, 5312, 5424, 5532, 5643, 5753, 5862, 5973, 6081, 6191, 6303, 6410, 6524, 6633, 6741, 6854, 6962, 7076, 7185, 7290, 7404, 7512, 7623, 7734, 7841, 7953, 8064, 8174, 8285]# noqa: E501
    hit0 = 6

    data1 = [0, 6873, 7970, 9065, 10160, 11258, 12353, 13448, 14547, 15639, 16737, 17832, 18929, 20024, 21117, 22215, 23313, 24407, 25503, 26598, 27693, 28788, 29886, 30981, 32073, 33174, 34269, 35364, 36461, 37557, 38652, 39746, 40842, 41939, 43037, 44130, 45228, 46323, 47417, 48515, 49608, 50706, 51801, 52895, 53994, 55091, 56186, 57281, 58376, 59474, 60567, 61662, 62760, 63858, 64950, 66050, 67143, 68237, 69335, 70428, 71528, 72618, 73716, 74816, 75906, 77006, 78099, 79194, 80289, 81386, 82482]# noqa: E501
    hit1 = 1

    data2 = [0, 1112, 1289, 1466, 1641, 1818, 1998, 2175, 2351, 2528, 2708, 2883, 3062, 3237, 3416, 3594, 3768, 3947, 4124, 4304, 4478, 4655, 4832, 5009, 5187, 5363, 5543, 5721, 5895, 6074, 6248, 6426, 6603, 6783, 6960, 7137, 7314, 7488, 7667, 7844, 8024, 8201, 8378, 8555, 8727, 8907, 9084, 9263, 9440, 9620, 9795, 9972, 10146, 10323, 10503, 10680, 10859, 11034, 11214, 11388, 11564, 11742, 11921, 12099, 12275, 12453, 12630, 12807, 12986, 13160, 13338]# noqa: E501
    hit2 = 5

    data3 = [0, 10952, 12698, 14444, 16190, 17934, 19680, 21422, 23172, 24914, 26661, 28407, 30153, 31901, 33647, 35390, 37136, 38882, 40629, 42374, 44121, 45867, 47609, 49358, 51101, 52848, 54593, 56342, 58085, 59832, 61580, 63323, 65070, 66815, 68559, 70307, 72053, 73799, 75545, 77292, 79035, 80778, 82527, 84270, 86019, 87765, 89511, 91256, 93002, 94749, 96494, 98238, 99984, 101729, 103476, 105221, 106967, 108713, 110457, 112205, 113949, 115697, 117441, 119186, 120933, 122678, 124425, 126171, 127919, 129662, 131408]# noqa: E501
    hit3 = 1

# 游龙掌 비연장
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/5152480fdde81362575a488d4cec4af9?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill8(ActiveSkill):
    name = "游龙掌"
    learnLv = 35
    masterLv = 60
    maxLv = 70
    position = 3
    rangeLv = 2
    cd = 12
    mp = [100, 900]
    uuid = "5152480fdde81362575a488d4cec4af9"
    vps = [
          {
            "name": "暴流掌",
            "desc": "追加聚集敌人<br/>范围增加",
            "explain": "[游龙掌]<br/>剑气周围的敌人被卷进来， 吸附到路径中央<br/><br/>剑气大小和前进距离 + 60%"
          },
          {
            "name": "快刀乱麻",
            "desc": "施放时间减少<br/>取消僵直",
            "explain": "[游龙掌]<br/>迅速以直线方向发射剑气<br/>- 剑气发射次数 : 5次<br/>- 总攻击力相同<br/><br/>施放时可以强制中断[湮烈掌]、 [如来神掌]的施放后僵直<br/>- 可以强制中断[游龙掌]的施放后僵直， 并施放[湮烈掌]、 [如来神掌]"
          }
        ]
    data0 = [0, 1772, 1958, 2148, 2315, 2502, 2688, 2877, 3051, 3237, 3426, 3608, 3777, 3963, 4154, 4335, 4520, 4709, 4884, 5070, 5253, 5439, 5618, 5802, 5996, 6173, 6345, 6536, 6723, 6903, 7086, 7280, 7451, 7635, 7820, 8007, 8184, 8364, 8559, 8739, 8912, 9096, 9282, 9468, 9654, 9828, 10019, 10202, 10386, 10557, 10752, 10931, 11120, 11307, 11483, 11666, 11847, 12036, 12218, 12396, 12576, 12770, 12950, 13127, 13316, 13497, 13677, 13854, 14046, 14235, 14415]# noqa: E501
    hit0 = 10

# 回天璇鸣剑 폭검
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/2391a27457b5a8c6fa4b4670a91bdd11?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill9(ActiveSkill):
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
    vps = [
          {
            "name": "天女神剑",
            "desc": "施放时间减少<br/>可以在空中施放<br/>范围增加",
            "explain": "[回天璇鸣剑]<br/>固定在原地挥剑引发爆炸<br/>- 删除按方向键和技能键功能<br/><br/>可以在空中施放， 此时会快速下落并挥剑<br/><br/>攻击范围 +30%"
          },
          {
            "name": "花连舞",
            "desc": "范围增加<br/>追加聚集敌人<br/>施放时间减少",
            "explain": "[回天璇鸣剑]<br/>强化旋转攻击后结束技能<br/>- 删除爆炸攻击<br/>- 旋转斩击多段攻击次数 : 3次<br/>- 总攻击力相同<br/><br/>删除按方向键功能<br/><br/>旋转中移动距离 + 200%<br/><br/>旋转攻击可以击退霸体状态的敌人"
          }
        ]
    data0 = [0, 6864, 7524, 8280, 8984, 9644, 10299, 11057, 11714, 12416, 13127, 13836, 14489, 15146, 15906, 16610, 17267, 18026, 18681, 19341, 20091, 20751, 21459, 22113, 22872, 23522, 24233, 24939, 25646, 26304, 26963, 27714, 28373, 29078, 29840, 30495, 31148, 31808, 32567, 33272, 33926, 34682, 35337, 35997, 36704, 37413, 38118, 38774, 39530, 40188, 40896, 41604, 42303, 42962, 43718, 44376, 45035, 45788, 46494, 47156, 47912, 48570, 49226, 49983, 50639, 51342, 52104, 52761, 53412, 54173, 54828]# noqa: E501
    hit0 = 1 #TODO

    data1 = [0, 20001, 22029, 24063, 26094, 28118, 30152, 32174, 34205, 36240, 38264, 40286, 42324, 44345, 46379, 48411, 50435, 52470, 54495, 56525, 58560, 60581, 62613, 64635, 66671, 68711, 70734, 72753, 74787, 76806, 78843, 80868, 82901, 84932, 86957, 88989, 91014, 93044, 95082, 97103, 99140, 101159, 103196, 105227, 107252, 109277, 111312, 113331, 115364, 117399, 119424, 121457, 123476, 125511, 127547, 129569, 131594, 133626, 135660, 137688, 139718, 141747, 143774, 145794, 147833, 149855, 151884, 153918, 155942, 157980, 160001]# noqa: E501
    hit1 = 1 #TODO

# 湮烈掌 폭멸장
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/fc458e449ee00b01dbf88d09aae65462?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill10(ActiveSkill):
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
    vps = [
          {
            "name": "湮灭掌",
            "desc": "施放时间减少",
            "explain": "[湮烈掌]<br/>凝聚内劲时间 -50%<br/><br/>删除内劲爆炸攻击<br/>- 总攻击力相同"
          },
          {
            "name": "激流绽放",
            "desc": "范围增加<br/>攻击时间减少<br/>赋予速度增益效果",
            "explain": "[湮烈掌]<br/>内劲释放攻击范围 + 30%<br/><br/>强化内劲爆炸攻击<br/>- 变更为单次攻击<br/>- 总攻击力相同<br/>- 发生爆炸时自身所有速度 + 10%， 效果持续20秒"
          }
        ]
    data0 = [0, 23949, 26381, 28817, 31242, 33671, 36102, 38532, 40961, 43392, 45825, 48254, 50681, 53108, 55544, 57974, 60404, 62832, 65262, 67695, 70119, 72549, 74984, 77411, 79844, 82272, 84704, 87132, 89562, 91994, 94424, 96852, 99281, 101712, 104144, 106572, 109001, 111432, 113862, 116289, 118724, 121151, 123584, 126011, 128439, 130875, 133304, 135732, 138161, 140591, 143021, 145452, 147884, 150311, 152741, 155171, 157601, 160032, 162462, 164889, 167321, 169754, 172181, 174612, 177041, 179471, 181902, 184331, 186761, 189188, 191622]# noqa: E501
    hit0 = 1 #TODO

    data1 = [0, 3420, 3767, 4115, 4461, 4808, 5160, 5507, 5853, 6198, 6545, 6891, 7241, 7587, 7937, 8282, 8630, 8978, 9324, 9671, 10017, 10365, 10710, 11058, 11406, 11751, 12098, 12447, 12792, 13142, 13491, 13839, 14184, 14531, 14876, 15227, 15572, 15920, 16266, 16614, 16961, 17309, 17657, 18000, 18348, 18695, 19040, 19389, 19739, 20085, 20430, 20777, 21125, 21473, 21819, 22167, 22512, 22860, 23207, 23559, 23903, 24251, 24597, 24945, 25290, 25638, 25988, 26333, 26678, 27027, 27375]# noqa: E501
    hit1 = 3

# 花舞千魂杀 혜성만리
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/5892d1fa4462e561ac8f8d2c74892b0a?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill11(ActiveSkill):
    name = "花舞千魂杀"
    learnLv = 45
    masterLv = 60
    maxLv = 70
    position = 0
    rangeLv = 2
    cube = 2
    cd = 40
    mp = [130, 2100]
    uuid = "5892d1fa4462e561ac8f8d2c74892b0a"
    vps = [
          {
            "name": "花飞万里",
            "desc": "施放时间减少<br/>范围增加",
            "explain": "[花舞千魂]<br/>删除剑插地攻击和最后下斩攻击<br/>- 总攻击力相同<br/><br/>攻击范围 +30%<br/><br/>一闪攻击后僵直时间 -30%<br/><br/>一闪攻击后转换角色朝向"
          },
          {
            "name": "花舞一闪",
            "desc": "赋予无敌状态<br/>追加强制控制功能",
            "explain": "[花舞千魂]<br/>施放过程中进入无敌状态<br/><br/>一闪后转身连续斩击并返回原位， 然后用巨剑下劈进行最后一击<br/>- 删除按键连接施放功能<br/>- 总攻击力相同<br/><br/>使被一闪命中的敌人进入强制控制状态，  直至技能结束。"
          }
        ]
    data0 = [0, 23998, 26433, 28867, 31302, 33736, 36171, 38605, 41040, 43475, 45909, 48344, 50778, 53213, 55647, 58082, 60517, 62951, 65386, 67820, 70255, 72689, 75124, 77559, 79993, 82428, 84862, 87297, 89731, 92166, 94601, 97035, 99470, 101904, 104339, 106773, 109208, 111643, 114077, 116512, 118946, 121381, 123815, 126250, 128685, 131119, 133554, 135988, 138423, 140857, 143292, 145727, 148161, 150596, 153030, 155465, 157899, 160334, 162769, 165203, 167638, 170072, 172507, 174941, 177376, 179811, 182245, 184680, 187114, 189549, 191983]# noqa: E501
    hit0 = 1

    data1 = [0, 3302, 3637, 3972, 4307, 4642, 4977, 5312, 5647, 5982, 6317, 6652, 6987, 7322, 7657, 7992, 8327, 8662, 8997, 9332, 9667, 10002, 10337, 10672, 11007, 11342, 11677, 12012, 12347, 12682, 13017, 13352, 13687, 14022, 14357, 14692, 15027, 15362, 15697, 16032, 16367, 16702, 17037, 17372, 17707, 18042, 18377, 18712, 19047, 19382, 19717, 20052, 20387, 20722, 21057, 21392, 21727, 22062, 22397, 22732, 23067, 23402, 23737, 24072, 24407, 24742, 25077, 25412, 25747, 26082, 26417]# noqa: E501
    hit1 = 2

    data2 = [0, 13209, 14549, 15889, 17229, 18569, 19909, 21249, 22589, 23929, 25269, 26609, 27949, 29289, 30629, 31969, 33309, 34649, 35989, 37329, 38669, 40010, 41350, 42690, 44030, 45370, 46710, 48050, 49390, 50730, 52070, 53410, 54750, 56090, 57430, 58770, 60110, 61450, 62790, 64130, 65470, 66810, 68150, 69490, 70830, 72170, 73510, 74850, 76190, 77530, 78870, 80210, 81551, 82891, 84231, 85571, 86911, 88251, 89591, 90931, 92271, 93611, 94951, 96291, 97631, 98971, 100311, 101651, 102991, 104331, 105671]# noqa: E501
    hit2 = 1

# 三花聚顶 삼매진화
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/669f1428193f61f9d92c743b72438c4d?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill12(PassiveSkill):
    name = "三花聚顶"
    learnLv = 48
    masterLv = 40
    maxLv = 50
    position = 4
    rangeLv = 3
    uuid = "669f1428193f61f9d92c743b72438c4d"

    data0 = [0, 8.5, 10.5, 12.5, 14.5, 16.5, 18.5, 20.5, 22.5, 24.5, 26.5, 28.5, 30.5, 32.5, 34.5, 36.5, 38.5, 40.5, 42.5, 44.5, 46.5, 48.5, 50.5, 52.5, 54.5, 56.5, 58.5, 60.5, 62.5, 64.5, 66.5, 68.5, 70.5, 72.5, 74.5, 76.5, 78.5, 80.5, 82.5, 84.5, 86.5, 88.5, 90.5, 92.5, 94.5, 96.5, 98.5, 100.5, 102.5, 104.5, 106.5]# noqa: E501

    associate = [
        {"data":data0,"type":"*skillRation"}
    ]


# 花开寒影 경전지화
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/8510294202d0e042dd29a2422fc6770d?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill13(ActiveSkill):
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

    data0 = [0, 9900, 12195, 14490, 16786, 19081, 21378, 23671, 25967, 28262, 30558, 32854, 35148, 37443, 39739, 42035, 44331, 46623, 48919, 51213, 53511, 55804, 58100, 60395, 62695, 64989, 67285, 69578, 71875, 74172, 76466, 78762, 81055, 83351, 85648, 87942, 90238, 92532, 94828, 97125, 99419, None, None, None, None, None, None, None, None, None, None]# noqa: E501
    hit0 = 1

    data1 = [0, 1522, 1876, 2228, 2583, 2936, 3288, 3639, 3996, 4346, 4701, 5052, 5406, 5761, 6112, 6467, 6819, 7172, 7527, 7879, 8232, 8585, 8940, 9291, 9646, 9999, 10350, 10705, 11056, 11410, 11762, 12118, 12468, 12823, 13177, 13529, 13881, 14237, 14588, 14939, 15297, None, None, None, None, None, None, None, None, None, None]# noqa: E501
    hit1 = 13

    data2 = [0, 69292, 85359, 101428, 117498, 133564, 149630, 165701, 181766, 197834, 213905, 229970, 246040, 262107, 278173, 294244, 310309, 326379, 342444, 358513, 374583, 390648, 406718, 422783, 438853, 454923, 470987, 487058, 503124, 519192, 535262, 551327, 567398, 583463, 599531, 615601, 631666, 647737, 663802, 679869, 695941, None, None, None, None, None, None, None, None, None, None]# noqa: E501
    hit2 = 1


# 啸空十字斩 십자검
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/2c9d9a36c8401bddff6cdb80fab8dc24?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill14(ActiveSkill):
    name = "啸空十字斩"
    learnLv = 60
    masterLv = 40
    maxLv = 50
    position = 3
    rangeLv = 2
    cube = 1
    cd = 30
    mp = [450, 1200]
    uuid = "2c9d9a36c8401bddff6cdb80fab8dc24"
    vps = [
          {
            "name": "日落黄昏",
            "desc": "施放时间减少<br/>范围增加",
            "explain": "[啸空十字刃]<br/>删除垂直斩击， 水平斩击持续时间 + 1.5秒<br/>- 总攻击力相同<br/><br/>再次按技能键时， 立即引发爆炸<br/><br/>爆炸攻击范围 + 30%"
          },
          {
            "name": "逐邪剑",
            "desc": "追踪<br/>施放时间减少",
            "explain": "[啸空十字刃]<br/>追踪并瞬移到前方一定范围内最强敌人位置<br/>之后同时施放水平斩击和垂直斩击， 结束动作的同时， 引爆十字刃造成伤害"
          }
        ]
    data0 = [0, 11351, 12504, 13656, 14804, 15956, 17108, 18260, 19410, 20562, 21716, 22863, 24017, 25166, 26319, 27467, 28619, 29774, 30923, 32073, 33225, 34379, 35523, 36675, 37830, 38981, 40133, 41283, 42435, 43587, 44736, 45891, 47045, 48194, 49346, 50496, 51651, 52797, 53949, 55101, 56253, 57405, 58556, 59705, 60858, 62010, 63162, 64311, 65465, 66617, 67772]# noqa: E501
    hit0 = 1

    data1 = [0, 13242, 14585, 15927, 17270, 18612, 19961, 21303, 22638, 23987, 25332, 26673, 28019, 29361, 30705, 32046, 33389, 34734, 36075, 37419, 38768, 40109, 41451, 42795, 44138, 45483, 46827, 48165, 49511, 50853, 52197, 53540, 54885, 56226, 57572, 58914, 60255, 61602, 62945, 64286, 65630, 66971, 68316, 69659, 71004, 72345, 73686, 75032, 76379, 77721, 79065]# noqa: E501
    hit1 = 1

    data2 = [0, 15137, 16670, 18204, 19739, 21276, 22808, 24347, 25883, 27419, 28950, 30489, 32019, 33554, 35093, 36626, 38162, 39695, 41234, 42770, 44303, 45839, 47376, 48908, 50445, 51980, 53514, 55052, 56588, 58121, 59652, 61191, 62729, 64259, 65796, 67334, 68867, 70404, 71937, 73473, 75008, 76542, 78080, 79614, 81149, 82686, 84216, 85754, 87294, 88820, 90362]# noqa: E501
    hit2 = 1


# 如来神掌 백보신장
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/2ba299855fc22192cba4f73db75e9d0e?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill15(ActiveSkill):
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
    vps = [
          {
            "name": "如影随形",
            "desc": "范围增加<br/>追加强制控制功能",
            "explain": "[如来神掌]<br/>向空中跳跃后， 向地面发射无形掌风<br/>- 攻击范围 50%<br/>- 删除爆炸攻击<br/>- 总攻击力相同<br/>- 地面施放时， 也会跳跃后发射掌风<br/>- 空中施放技能所需最低高度减少， 后跳过程中也可以施放<br/><br/>被掌风命中的敌人将进入强制控制状态3秒"
          },
          {
            "name": "反弹掌",
            "desc": "范围增加<br/>可以在被击时施放",
            "explain": "[如来神掌]<br/>掌风基础移动距离增加<br/>- 删除通过方向键调整距离的功能<br/><br/>掌风贯穿前方路径上的敌人后造成伤害， 此后贯穿的敌人身体发生爆炸， 造成额外伤害<br/><br/>空中施放技能所需最低高度减少， 后跳过程中也可以施放<br/>- 在较低高度使用时， 跳到一定高度后发射掌风<br/><br/>被击过程中也可以使用， 这种情况下角色会因为强大的后座力而后退， 掌风的移动距离减少"
          }
        ]
    data0 = [0, 29427, 32412, 35403, 38387, 41370, 44352, 47345, 50322, 53312, 56303, 59279, 62265, 65247, 68238, 71225, 74207, 77198, 80175, 83165, 86153, 89138, 92120, 95102, 98097, 101084, 104063, 107052, 110034, 113022, 115998, 118991, 121977, 124961, 127950, 130934, 133916, 136896, 139892, 142872, 145856, 148845, 151832, 154812, 157796, 160788, 163770, 166751, 169743, 172728, 175713]# noqa: E501
    hit0 = 1

    data1 = [0, 44144, 48618, 53100, 57578, 62058, 66524, 71004, 75482, 79964, 84440, 88920, 93395, 97878, 102357, 106827, 111309, 115788, 120267, 124743, 129225, 133697, 138182, 142649, 147132, 151608, 156090, 160563, 165047, 169521, 174005, 178484, 182954, 187436, 191909, 196392, 200865, 205352, 209825, 214310, 218774, 223256, 227732, 232211, 236687, 241172, 245649, 250130, 254604, 259076, 263555]# noqa: E501
    hit1 = 1

# 莲花剑舞 연화검무
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/8b08f9504167a9c0f3a1d29d71b7943e?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill16(ActiveSkill):
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
    vps = [
          {
            "name": "绝密一剑",
            "desc": "施放时间减少<br/>追加聚集敌人<br/>范围增加",
            "explain": "[莲花剑舞]<br/>地面施放时招式发生变化<br/>- 删除1招式攻击<br/>- 总攻击力相同<br/><br/>2招式与3招式攻击将敌人吸附至角色前方<br/><br/>攻击范围 20%"
          },
          {
            "name": "莲花连剑",
            "desc": "取消僵直<br/>每秒分开使用",
            "explain": "[莲花剑舞]<br/>可以强制中断转职技能的施放后僵直并施放<br/><br/>每次施放技能时， 会在原地展开一个招式， 按下前方向键时会向前滑动并使用招式<br/>- 首次施放时使用第1招<br/>- 在接下来的10秒内， 可以依次使用第2招、 第3招、 第4招<br/>- 在空中施放时固定使用第3招<br/>- 总攻击力相同"
          }
        ]
    data0 = [0, 3930, 4329, 4728, 5128, 5525, 5924, 6322, 6722, 7119, 7518, 7918, 8317, 8712, 9114, 9511, 9912, 10313, 10711, 11105, 11506, 11903, 12300, 12706, 13103, 13499, 13896, 14295, 14693, 15092, 15495, 15891, 16289, 16690, 17086, 17485, 17883, 18285, 18681, 19084, 19479, 19878, 20274, 20677, 21076, 21473, 21874, 22270, 22668, 23067, 23471]# noqa: E501
    hit0 = 2

    data1 = [0, 5895, 6492, 7090, 7689, 8286, 8887, 9484, 10080, 10678, 11275, 11876, 12474, 13074, 13668, 14268, 14866, 15462, 16061, 16661, 17260, 17854, 18452, 19055, 19653, 20247, 20849, 21448, 22041, 22643, 23239, 23840, 24430, 25030, 25628, 26225, 26826, 27423, 28023, 28618, 29217, 29819, 30416, 31012, 31611, 32212, 32804, 33405, 34004, 34603, 35198]# noqa: E501
    hit1 = 2

    data2 = [0, 5895, 6492, 7090, 7689, 8286, 8887, 9484, 10080, 10678, 11275, 11876, 12474, 13074, 13668, 14268, 14866, 15462, 16061, 16661, 17260, 17854, 18452, 19055, 19653, 20247, 20849, 21448, 22041, 22643, 23239, 23840, 24430, 25030, 25628, 26225, 26826, 27423, 28023, 28618, 29217, 29819, 30416, 31012, 31611, 32212, 32804, 33405, 34004, 34603, 35198]# noqa: E501
    hit2 = 2

    data3 = [0, 23579, 25974, 28365, 30761, 33151, 35541, 37933, 40325, 42719, 45111, 47502, 49893, 52287, 54679, 57070, 59466, 61854, 64246, 66636, 69034, 71427, 73813, 76206, 78604, 80993, 83382, 85775, 88169, 90558, 92951, 95343, 97739, 100128, 102522, 104913, 107305, 109696, 112090, 114480, 116872, 119265, 121661, 124050, 126441, 128836, 131222, 133616, 136011, 138405, 140795]# noqa: E501
    hit3 = 2

# 七星耀华 등봉조극
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/ac21c02567f04a92b54dd85c091d1e5a?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill17(PassiveSkill):
    name = "七星耀华"
    learnLv = 75
    masterLv = 40
    maxLv = 50
    position = 1
    rangeLv = 3
    uuid = "ac21c02567f04a92b54dd85c091d1e5a"

    data0 = [0, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118]# noqa: E501

    associate = [
        {"data":data0,"type":"*skillRation"}
    ]
# 樱花劫 연화섬
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/0113c8b1306ca76d208f83f2d093dd62?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill18(ActiveSkill):
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
    vps = [
          {
            "name": "移形换位闪",
            "desc": "追踪<br/>无敌强化",
            "explain": "[樱花劫]<br/>向前方斩击后返回， 将剑插入剑鞘前， 再次按技能键时， 移动至斩击敌人中最强大的敌人， 并将剑插入剑鞘。<br/><br/>技能结束后， 维持0.3秒的无敌状态"
          },
          {
            "name": "花舞十日红",
            "desc": "攻击力和冷却时间增加<br/>范围增加",
            "explain": "[樱花劫]<br/>基本冷却时间变更为67.5秒<br/>攻击力 50%<br/><br/>攻击范围 50%"
          }
        ]
    data0 = [0, 94825, 104443, 114058, 123679, 133299, 142921, 152540, 162162, 171779, 181403, 191020, 200642, 210259, 219877, 229497, 239120, 248738, 258362, 267977, 277599, 287219, 296840, 306461, 316079, 325697, 335317, 344935, 354559, 364175, 373799, 383416, 393039, 402657, 412279, 421894, 431514, 441133, 450754, 460375, 469994, 479614, 489235, 498855, 508475, 518091, 527715, 537333, 546948, 556570, 566189]# noqa: E501
    hit0 = 1

    def vp_2(self):
        self.cd = 67.5
        self.skillRation *= 1.5

# 飞花逐月 월광비무
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/7ec521d063d2190e1fcc5bd229af9bcf?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill19(ActiveSkill):
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

    data0 = [0, 5048, 6217, 7389, 8559, 9732, 10902, 12074, 13238, 14413, 15583, 16754, 17921, 19091, 20265, 21434, 22603, 23777, 24943, 26113, 27286, 28453, 29629, 30798, 31962, 33138, 34309, 35477, 36649, 37819, 38989, 40159, 41327, 42499, 43669, 44842, 46014, 47178, 48352, 49524, 50692, 51864, 53035, 54202, 55375, 56544, 57716, 58884, 60056, 61222, 62396]# noqa: E501
    hit0 = 20

    data1 = [0, 105995, 130568, 155149, 179725, 204301, 228883, 253461, 278038, 302613, 327190, 351772, 376348, 400924, 425503, 450085, 474662, 499236, 523818, 548391, 572972, 597551, 622127, 646704, 671281, 695862, 720439, 745016, 769596, 794169, 818751, 843327, 867903, 892480, 917061, 941639, 966218, 990798, 1015371, 1039949, 1064531, 1089104, 1113683, 1138261, 1162840, 1187423, 1211994, 1236574, 1261148, 1285728, 1310307]# noqa: E501
    hit1 = 1

# 落英惊鸿掌 엽해소옥
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/92360eab6e1f378902018eca681ac629?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill20(ActiveSkill):
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

    data0 = [0, 14829, 16333, 17835, 19340, 20844, 22350, 23855, 25358, 26862, 28365, 29870, 31374, 32879, 34384, 35888, 37392, 38896, 40399, 41905, 43409, 44913, 46417, 47922, 49426, 50932, 52435, 53938, 55443, 56947, 58452, 59956, 61459, 62964, 64469, 65973, 67478, 68980, 70485, 71991, 73495, 74999, 76502, 78006, 79511, 81017, 82521, 84025, 85527, 87032, 88537]# noqa: E501
    hit0 = 1

    data1 = [0, 7413, 8165, 8918, 9670, 10423, 11174, 11928, 12679, 13430, 14184, 14935, 15687, 16440, 17191, 17943, 18696, 19448, 20200, 20953, 21704, 22456, 23207, 23961, 24713, 25465, 26218, 26969, 27722, 28475, 29226, 29977, 30729, 31482, 32233, 32987, 33739, 34490, 35244, 35995, 36748, 37501, 38251, 39004, 39754, 40508, 41259, 42011, 42764, 43516, 44269]# noqa: E501
    hit1 = 4

    data2 = [0, 103795, 114325, 124853, 135384, 145915, 156444, 166973, 177503, 188034, 198564, 209093, 219624, 230153, 240683, 251212, 261742, 272273, 282802, 293331, 303862, 314393, 324922, 335452, 345982, 356512, 367040, 377571, 388101, 398630, 409160, 419690, 430221, 440748, 451281, 461812, 472341, 482870, 493400, 503930, 514460, 524989, 535518, 546049, 556579, 567108, 577638, 588170, 598699, 609228, 619759]# noqa: E501
    hit2 = 1


# 剑仙之境 검선지경
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/5cac3411ccef1af333953e0ded5e942d?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill21(PassiveSkill):
    name = "剑仙之境"
    learnLv = 95
    masterLv = 40
    maxLv = 50
    position = 5
    rangeLv = 3
    uuid = "5cac3411ccef1af333953e0ded5e942d"

    data0 = [0, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118]# noqa: E501

    associate = [
        {"data":data0,"type":"*skillRation"}
    ]

# 轻云出月风静夜 월하무즉정야
# https://api.neople.co.kr/df/skills/1645c45aabb008c98406b3a16447040d/3cb633d00f8f6ee088682c9171020d26?apikey=fdvit1Kj64EAJm0qfB3JEAD8FLExLDD0
class Skill22(ActiveSkill):
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

    data0 = [0, 575704, 709203, 842696, 976194, 1109690, 1243187, 1376684, 1510181, 1643679, 1777175, 1910671, 2044168, 2177664, 2311161, 2444658, 2578156, 2711651, 2845149, 2978645, 3112141, 3245638, 3379136, 3512630, 3646129, 3779626, 3913122, 4046618, 4180116, 4313612, 4447108, 4580605, 4714103, 4847598, 4981096, 5114592, 5248090, 5381584, 5515082, 5648578, 5782076, 5915572, 6049070, 6182567, 6316062, 6449560, 6583054, 6716552, 6850050, 6983546, 7117044]# noqa: E501
    hit0 = 1

class classChange(Character):
    def __init__(self, equVersion):

        self.name = 'vegabond'
        self.nameCN = '极诣·流浪武士'
        self.role = 'swordman_female'

        self.武器选项 = ['光剑', '巨剑', '钝器', '太刀', '短剑']
        self.副武器选项 = ['光剑']
        self.输出类型选项 = ['物理百分比']
        self.输出类型 = '物理百分比'
        self.防具精通属性 = ['力量']
        self.防具类型 = '皮甲'
        self.buff = 2.335

        self.角色 = '鬼剑士(女)'

        self.职业 = '流浪武士'

        super().__init__(equVersion, __name__)


    def calc_weapon(self,cur:CharacterEquipInfo):
        if cur.equInfo is None:
            return
        if cur.equInfo.itemType == "副武器":
            if cur.equInfo.categorize == '传世武器':
                ATKP = 武器强化计算(115, '史诗', cur.reinforce, cur.equInfo.itemDetailType, '物理', 1.12)
            else:
                # 强化计算
                ATKP = 武器强化计算(115, '史诗', cur.reinforce, cur.equInfo.itemDetailType, '物理')
            self.SetStatus(AtkP =  (cur.equInfo.AtkP + ATKP) * 0.1)
        else:
            super().calc_weapon(cur)