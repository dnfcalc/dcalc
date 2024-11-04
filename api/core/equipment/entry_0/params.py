
entry_chose = []  # (20000 + id, [chose1, 2, 3...]) 额外选项设置，参考20074消灭敌人词条
multi_select = {}  # id : True/False 设置选项是否支持多选
variable_set = {}  # id : setfunc  参数返回设置函数

# zs_bd_rate = 0

# def set_zs_bd_rate(x):
#     global zs_bd_rate
#     zs_bd_rate = x[0]/100


# entry_chose.append((20000, ["冰冻结算灼伤比例：{}%".format(str(i))
#                             for i in range(0, 101)], ""))
# multi_select[20000] = False
# variable_set[20000] = set_zs_bd_rate

control_state = False

def set_control_state(x):
    global control_state
    control_state = (x[0] == 1)


entry_chose.append((20001, ["控制型异常：不生效", "控制型异常：生效"], ""))
multi_select[20001] = False
variable_set[20001] = set_control_state

zd_rate = 1.0

def set_zd_rate(x):
    global zd_rate
    zd_rate = 1 - x[0]/5

entry_chose.append((20002, ["中毒层数:{}层".format(str(6-i))
                            for i in range(0, 6)], ""))
multi_select[20002] = False
variable_set[20002] = set_zd_rate

cx_rate = 1.0

def set_cx_rate(x):
    global cx_rate
    cx_rate = 1 - x[0]/10

entry_chose.append((20003, ["出血层数:{}层".format(str(11-i))
                            for i in range(0, 11)], ""))
multi_select[20003] = False
variable_set[20003] = set_cx_rate

gd_rate = 1.0

def set_gd_rate(x):
    global gd_rate
    gd_rate = 1 - x[0]/10

entry_chose.append((20004, ["感电层数:{}层".format(str(11-i))
                            for i in range(0, 11)], ""))
multi_select[20004] = False
variable_set[20004] = set_gd_rate


bd_cd = 99.99

def set_bd_cd(x):
    global bd_cd
    if x[0] == 0:
        bd_cd = 99
    else:
        bd_cd = 3.5 - x[0]*0.5

entry_chose.append((20005, ["职业无赋予冰冻","职业冰冻CD：3秒","职业冰冻CD：2.5秒","职业冰冻CD：2秒","职业冰冻CD：1.5秒","职业冰冻CD：1秒","职业冰冻CD：0.5秒","职业冰冻CD：0秒"], ""))
multi_select[20005] = False
variable_set[20005] = set_bd_cd

cx_cd = 99.99

def set_cx_cd(x):
    global cx_cd
    if x[0] == 0:
        cx_cd = 99
    else:
        cx_cd = 3.5 - x[0]*0.5

entry_chose.append((20006, ["职业无赋予出血","职业出血CD：3秒","职业出血CD：2.5秒","职业出血CD：2秒","职业出血CD：1.5秒","职业出血CD：1秒","职业出血CD：0.5秒","职业出血CD：0秒"], ""))
multi_select[20006] = False
variable_set[20006] = set_cx_cd

zd_cd = 99.99

def set_zd_cd(x):
    global zd_cd
    if x[0] == 0:
        zd_cd = 99
    else:
        zd_cd = 3.5 - x[0]*0.5

entry_chose.append((20007, ["职业无赋予中毒","职业中毒CD：3秒","职业中毒CD：2.5秒","职业中毒CD：2秒","职业中毒CD：1.5秒","职业中毒CD：1秒","职业中毒CD：0.5秒","职业中毒CD：0秒"], ""))
multi_select[20007] = False
variable_set[20007] = set_zd_cd

gd_cd = 99.99

def set_gd_cd(x):
    global gd_cd
    if x[0] == 0:
        gd_cd = 99
    else:
        gd_cd = 3.5 - x[0]*0.5

entry_chose.append((20008, ["职业无赋予感电","职业感电CD：3秒","职业感电CD：2.5秒","职业感电CD：2秒","职业感电CD：1.5秒","职业感电CD：1秒","职业感电CD：0.5秒","职业感电CD：0秒"], ""))
multi_select[20008] = False
variable_set[20008] = set_gd_cd

zs_cd = 99.99

def set_zs_cd(x):
    global zs_cd
    if x[0] == 0:
        zs_cd = 99
    else:
        zs_cd = 3.5 - x[0]*0.5

entry_chose.append((20009, ["职业无赋予灼伤","职业灼伤CD：3秒","职业灼伤CD：2.5秒","职业灼伤CD：2秒","职业灼伤CD：1.5秒","职业灼伤CD：1秒","职业灼伤CD：0.5秒","职业灼伤CD：0秒"], ""))
multi_select[20009] = False
variable_set[20009] = set_zs_cd

ws_rate = 1.0

def set_ws_rate(x):
    global ws_rate
    ws_rate = 1 - x[0]/100

entry_chose.append((20010, ["雾神武器适用:{}%".format(str(100-i))
                            for i in range(0, 101)], ""))
multi_select[20010] = False
variable_set[20010] = set_ws_rate


# hl = []
# hl_list = [0, 1, 2]


# def set_hl(x):
#     global hl
#     hl = []
#     for i in x:
#         # 暂不确定为什么用户会超过上限
#         try:
#             hl.append(hl_list[min(i,2)])
#         except Exception:
#             pass

# entry_chose.append((31283,
#                     ['选择火龙融合状态',
#                      '火龙之怒buff',
#                      '火龙的气息：44层',
#                      ], ""))
# multi_select[31283] = True
# variable_set[31283] = set_hl


# jl_1 = 1
# jl_2 = 1
# jl_3 = 1
# jl_list = [1, 3, 5, -1]


# def set_jl_1(x):
#     global jl_1
#     jl_1 = jl_list[x[0]]


# def set_jl_2(x):
#     global jl_2
#     jl_2 = jl_list[x[0]]


# def set_jl_3(x):
#     global jl_3
#     jl_3 = jl_list[x[0]]


# entry_chose.append((31286,
#                     ['金龙手镯触发：1次',
#                      '金龙手镯触发：3次',
#                      '金龙手镯触发：5次',
#                      '金龙手镯触发：期望',
#                      ], ""))
# multi_select[31286] = False
# variable_set[31286] = set_jl_1

# entry_chose.append((31287,
#                     ['金龙项链触发：1次',
#                      '金龙项链触发：3次',
#                      '金龙项链触发：5次',
#                      '金龙项链触发：期望',
#                      ], ""))
# multi_select[31287] = False
# variable_set[31287] = set_jl_2

# entry_chose.append((31288,
#                     ['金龙戒指触发：1次',
#                      '金龙戒指触发：3次',
#                      '金龙戒指触发：5次',
#                      '金龙戒指触发：期望',
#                      ], ""))
# multi_select[31288] = False
# variable_set[31288] = set_jl_3

# bl = 5

# zl = 30

# hq_jd = 5


# buff_info = 1
# buff_info_list = [1, 2, 3]


# def set_buff_info(x):
#     global buff_info
#     buff_info = buff_info_list[x[0]]


# entry_chose.append(
#     (31441,  ['武器融合效果：Buff效果', '武器融合效果：80连击效果', '武器融合效果：期望'], ""))
# multi_select[31441] = False
# variable_set[31441] = set_buff_info

# lhjs = 1
# lhjs_list = [round(1-0.1*i, 2) for i in range(0, 11)]


# def set_lhjs(x):
#     global lhjs
#     lhjs = lhjs_list[min(x[0],10)]


# entry_chose.append((31465,
#                     ['灵魂拘束适用{}%技攻'.format(i) for i in lhjs_list], ""))
# multi_select[31465] = False
# variable_set[31465] = set_lhjs

own_type = []
own_type_list = ['', '出血', '中毒', '灼伤', '感电', '眩晕',
                 '诅咒', '睡眠', '束缚', '冰冻', '减速', '石化', '失明', '混乱']


def set_own_type(x):
    global own_type
    own_type = []
    for i in x:
        own_type.append(own_type_list[i])


entry_chose.append((21127, ['选择自身异常状态'] + ['自身处于{}状态'.format(i)
                                           for i in own_type_list[1:]], ""))
variable_set[21127] = set_own_type

# mp_used = 0
# mp_used_list = [0, 1, 2, 3, 4, 5]


# def set_mp_used(x):
#     global mp_used
#     mp_used = mp_used_list[x[0]]


# entry_chose.append((21050,
#                     ['已消耗MP 0~9999',
#                      '已消耗MP 10000~19999',
#                      '已消耗MP 20000~29999',
#                      '已消耗MP 30000~39999',
#                      '已消耗MP 40000~49999',
#                      '已消耗MP 50000+',
#                      ], ""))
# multi_select[21050] = False
# variable_set[21050] = set_mp_used

# sy_cq = 0
# sy_cq_list = [0, 1, 2, 3]


# def set_sy_cq(x):
#     global sy_cq
#     sy_cq = sy_cq_list[x[0]]


# entry_chose.append((20948, ["双音戒指拾取{}个黑球".format(i) for i in sy_cq_list], ""))
# multi_select[20948] = False
# variable_set[20948] = set_sy_cq

# cd_kj = 6
# cd_kj_list = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# def set_cd_kj(x):
#     global cd_kj
#     cd_kj = cd_kj_list[x[0]]


# entry_chose.append((20990, ["快捷栏{}个技能冷却中".format(i) for i in cd_kj_list], ""))
# multi_select[20990] = False
# variable_set[20990] = set_cd_kj


enemy_type = []
enemy_type_list = ['', '机械', '恶魔', '精灵',
                   '天使', '龙族', '人型', '野兽', '植物', '不死', '昆虫']


def set_enemy_type(x):
    global enemy_type
    enemy_type = []
    for i in x:
        enemy_type.append(enemy_type_list[i])


entry_chose.append((20037, ['选择敌人类型'] + ['攻击{}敌人'.format(i)
                                         for i in enemy_type_list[1:]], ""))
variable_set[20037] = set_enemy_type


attack_type = []
attack_type_list = ['', '普通敌人', '稀有敌人', '领主敌人', '正面攻击', '背面攻击', '破招攻击',
                    '非破招攻击', '精英敌人']


def set_attack_type(x):
    global attack_type
    attack_type = []
    for i in x:
        attack_type.append(attack_type_list[i])


entry_chose.append((20351, ['选择攻击类型'] + ['{}'.format(i)
                                         for i in attack_type_list[1:]], ""))
variable_set[20351] = set_attack_type

state_type = []
state_type_list = ['', '出血', '中毒', '灼伤', '感电', '眩晕',
                   '诅咒', '睡眠', '束缚', '冰冻', '减速', '石化', '失明', '混乱']


def set_state_type(x):
    global state_type
    state_type = []
    for i in x:
        state_type.append(state_type_list[i])
    if bd_cd < 99 and '冰冻' not in state_type:
        state_type.append('冰冻')

entry_chose.append((20042, ['选择敌人状态'] + ['攻击{}敌人'.format(i)
                                         for i in state_type_list[1:]], ""))
variable_set[20042] = set_state_type


def get_state_type():
    # global state_type
    temp = list(set(state_type))
    if control_state:
        temp = list(filter(lambda x: x != '', temp))
    else:
        temp = list(filter(lambda x: x not in ['', '眩晕',
                                               '诅咒', '睡眠', '束缚', '冰冻', '减速', '石化', '失明', '混乱'], temp))
    return temp


teammate_num = 1
teammate_num_list = [0, 1, 2, 3, 4]


def set_teammate_num(x):
    global teammate_num
    teammate_num = teammate_num_list[x[0]]


entry_chose.append((20165, ['选择队员数量'] + ['队员：{}名'.format(i)
                                         for i in teammate_num_list[1:]], ""))
multi_select[20165] = False
variable_set[20165] = set_teammate_num

dungeons_type = []
dungeons_type_list = ['', '[贵族机要]', '[毁坏的寂静城(高级)]', '[机械战神试验场]', '[团结]']


def set_dungeons_type(x):
    global dungeons_type
    dungeons_type = []
    for i in x:
        if i < len(dungeons_type_list):
            dungeons_type.append(dungeons_type_list[i])


entry_chose.append((20189, ['选择地下城类型'] + ['{}'.format(i)
                                          for i in dungeons_type_list[1:]], ""))
variable_set[20189] = set_dungeons_type


# distance_num_list = [0, 50, 100, 150, 200, 250, 300]


# def set_distance_num(x):
#     global distance_num
#     distance_num = distance_num_list[x[0]]


# entry_chose.append((20253, ['选择敌人距离'] + ['距离敌人{}~{}px'.format(i, i + 50)
#                                          for i in distance_num_list[1:]], ""))
# multi_select[20253] = False
# variable_set[20253] = set_distance_num

# combo_num = 0

enemy_num = 0
enemy_num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def set_enemy_num(x):
    global enemy_num
    enemy_num = enemy_num_list[min(x[0], 10)]


entry_chose.append((20183, ['选择敌人数量'] + ['{}个敌人'.format(i)
                                         for i in enemy_num_list[1:]], ""))
multi_select[20183] = False
variable_set[20183] = set_enemy_num

# toughness_num = 0
# toughness_num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# def set_toughness_num(x):
#     global toughness_num
#     toughness_num = toughness_num_list[x[0]]


# entry_chose.append((20194, ['选择敌人韧性削减'] + ['韧性减少：{}%'.format(i * 10)
#                                            for i in toughness_num_list[1:]], ""))
# multi_select[20194] = False
# variable_set[20194] = set_toughness_num

hp_rate_num = 0
hp_rate_num_list = [90, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

def get_hp_rate_num(char):
    cur = char.get_eq_params('hp_max')
    cur = 100 if cur == 0 else cur
    return min(cur,hp_rate_num)

def set_hp_rate_num(x):
    global hp_rate_num
    hp_rate_num = hp_rate_num_list[x[0]]


entry_chose.append((20814, ['选择HP范围'] +
                    ['HP:10%以下',
                     'HP:10%~20%',
                     'HP:20%~30%',
                     'HP:30%~40%',
                     'HP:40%~50%',
                     'HP:50%~60%',
                     'HP:60%~70%',
                     'HP:70%~80%',
                     'HP:80%~90%',
                     'HP:90%以上',
                     ], ""))
multi_select[20814] = False
variable_set[20814] = set_hp_rate_num

mp_rate_num = 0
mp_rate_num_list = [90, 0, 10, 20, 30, 40, 50, 60, 70, 80, 90]


def set_mp_rate_num(x):
    global mp_rate_num
    mp_rate_num = mp_rate_num_list[x[0]]

def get_mp_rate_num(char):
    cur = char.get_eq_params('mp_max')
    cur = 100 if cur == 0 else cur
    return min(cur,mp_rate_num)

entry_chose.append((20813, ['选择MP范围'] +
                    ['MP:10%以下',
                     'MP:10%~20%',
                     'MP:20%~30%',
                     'MP:30%~40%',
                     'MP:40%~50%',
                     'MP:50%~60%',
                     'MP:60%~70%',
                     'MP:70%~80%',
                     'MP:80%~90%',
                     'MP:90%以上',
                     ], ""))
multi_select[20813] = False
variable_set[20813] = set_mp_rate_num

# gold_num = 40

# wuse_number = 0
# wuse_number_list = [0, 50, 100, 150, 200, 250]


# def set_wuse_num(x):
#     global wuse_number
#     wuse_number = wuse_number_list[x[0]]


# entry_chose.append((21261, ['累计无色消耗:{}个'.format(i)
#                             for i in wuse_number_list], ""))
# multi_select[21261] = False
# variable_set[21261] = set_wuse_num

cp_soul_bender = 5
cp_soul_bender_list = [5, 4, 3, 2, 1, 0]


def set_cp_soul_bender(x):
    global cp_soul_bender
    cp_soul_bender = cp_soul_bender_list[x[0]]


entry_chose.append((30550, ['CP武器-[冥界之焰]叠加5次',
                            'CP武器-[冥界之焰]叠加4次',
                            'CP武器-[冥界之焰]叠加3次',
                            'CP武器-[冥界之焰]叠加2次',
                            'CP武器-[冥界之焰]叠加1次',
                            'CP武器-[冥界之焰]叠加0次'
                            ], "soul_bender"))
multi_select[30550] = False
variable_set[30550] = set_cp_soul_bender

cp_striker_male = 0
cp_striker_male_list = [1, 0]


def set_cp_striker_male(x):
    global cp_striker_male
    cp_striker_male = cp_striker_male_list[x[0]]


entry_chose.append((30579, ['CP武器-[双重释放]Buff触发',
                            'CP武器-[双重释放]Buff未触发',
                            ], "striker_male"))
multi_select[30579] = False
variable_set[30579] = set_cp_striker_male

cp_elemental_bomber = 0
cp_elemental_bomber_list = [0, 1, 2, 3, 4, 5]


def set_cp_elemental_bomber(x):
    global cp_elemental_bomber
    cp_elemental_bomber = cp_elemental_bomber_list[x[0]]


entry_chose.append((30647, ['CP武器-[元素之力]0层',
                            'CP武器-[元素之力]1层',
                            'CP武器-[元素之力]2层',
                            'CP武器-[元素之力]3层',
                            'CP武器-[元素之力]4层',
                            'CP武器-[元素之力]5层',
                            ], "elemental_bomber"))
multi_select[30647] = False
variable_set[30647] = set_cp_elemental_bomber

cp_witch_1 = 0
cp_witch_list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


def set_cp_witch_1(x):
    global cp_witch_1
    cp_witch_1 = cp_witch_list_1[x[0]]


entry_chose.append((30663, ['CP武器-积攒普通糖果:{}个'.format(i)
                            for i in cp_witch_list_1], "witch"))
multi_select[30663] = False
variable_set[30663] = set_cp_witch_1

cp_witch_2 = 0
cp_witch_list_2 = [0, 1, 2, 3, 4, 5]


def set_cp_witch_2(x):
    global cp_witch_2
    cp_witch_2 = cp_witch_list_2[x[0]]


entry_chose.append((30664, ['CP武器-积攒稀有糖果:{}个'.format(i)
                            for i in cp_witch_list_2], "witch"))
multi_select[30664] = False
variable_set[30664] = set_cp_witch_2

# cp_witch_3 = 0
# cp_witch_list_3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# def set_cp_witch_3(x):
#     global cp_witch_3
#     cp_witch_3 = cp_witch_list_3[x[0]]


# entry_chose.append((30665, ['CP武器-存储普通糖果:{}个'.format(i)
#                             for i in cp_witch_list_3], "witch"))
# multi_select[30665] = False
# variable_set[30665] = set_cp_witch_3


# cp_witch_4 = 0
# cp_witch_list_4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


# def set_cp_witch_4(x):
#     global cp_witch_4
#     cp_witch_4 = cp_witch_list_4[x[0]]


# entry_chose.append((30666, ['CP武器-存储稀有糖果:{}个'.format(i)
#                             for i in cp_witch_list_4], "witch"))
# multi_select[30666] = False
# variable_set[30666] = set_cp_witch_4

combat_max = 0

# in_buff_info = 2
# in_buff_info_list = [1, 2, 3]


# def set_in_buff_info(x):
#     global in_buff_info
#     in_buff_info = in_buff_info_list[x[0]]


# entry_chose.append(
#     (31586,  ['海贼头肩：Buff效果', '海贼头肩：80连击效果', '海贼头肩：期望'], ""))
# multi_select[31586] = False
# variable_set[31586] = set_buff_info



cp_kunoichi = 30

def set_cp_kunoichi(x):
    global cp_kunoichi
    cp_kunoichi = x[0]*0.1

entry_chose.append((30724, ["CP武器灼伤结算加成：{}%".format(str(round(i*0.1,1)))
                            for i in range(0, 101)], "kunoichi"))
multi_select[30724] = False
variable_set[30724] = set_cp_kunoichi



random = 0
# random_list = [0, 1,2]


# def set_random(x):
#     global random
#     random = random_list[x[0]]

# entry_chose.append((30223, ['随机词条-期望计算',
#                             '随机词条-高伤计算',
#                             '随机词条-低伤计算',
#                             ], ""))
# multi_select[30223] = False
# variable_set[30223] = set_random