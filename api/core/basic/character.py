import importlib
from copy import deepcopy
from pyclbr import Function
from typing import Dict, List, Union
from uuid import uuid1
from utils.exception import ResponseException

from core.basic.equipment import equipment, get_equ, get_global_data
from core.basic.property import CharacterProperty
from core.basic.skill import 主动技能, 技能, 被动技能
from core.equipment.avatar import 装扮套装, 装扮套装集合, 装扮集合
from core.equipment.emblems import get_emblems_setinfo
from core.equipment.enchanting import get_enchanting_setinfo
from core.equipment.jade import get_jade_setinfo
from core.equipment.property import (
    增幅计算,
    左右计算,
    成长词条计算,
    武器强化计算,
    精通计算,
    耳环计算,
    获取基础属性,
    获取属性抗性基础,
    获取异常抗性基础,
    辅助精通计算,
    部位列表,
    锻造四维,
    锻造计算,
)
from core.equipment.sundry import get_sundries_setinfo

# from core.basic.enchanting import get_encfunc_by_id
# from core.basic.emblems import get_embfunc_by_id
# from core.basic.jade import get_jadefunc_by_id

MAXEQULV = 105


class Character(CharacterProperty):
    等级 = 110
    # 辟邪玉属性
    附加伤害增加增幅: float = 1.0
    属性附加伤害增加增幅: float = 1.0
    技能伤害增加增幅: float = 1.0
    暴击伤害增加增幅: float = 1.0
    伤害增加增幅: float = 1.0
    最终伤害增加增幅: float = 1.0
    力量智力增加增幅: float = 1.0
    物理魔法攻击力增加增幅: float = 1.0
    所有属性强化增幅: float = 1.0
    version = "default"
    equVersion = ""
    bufferCarry = False

    等级: int = 110
    防御输入: int = 506109
    防御系数: int = 1
    火抗输入: int = 0
    冰抗输入: int = 0
    光抗输入: int = 0
    暗抗输入: int = 0
    打造详情: Dict[str, Dict[str, int]] = {}
    装备栏: List[int] = []  # [装备id]
    部位装备: Dict[str, int] = {}  # {部位: 装备id}
    部位附魔: Dict[str, Function] = {}  # {部位: 附魔函数}
    词条等级: Dict[str, List[int]] = {}  # {部位: [等级1, 2, 3, 4]}
    药剂: List[int] = []

    # 需要职业自定义数据
    实际名称 = ""
    名称 = ""
    角色 = ""
    角色类型 = ""
    职业 = ""
    武器选项: List[str] = []
    输出类型选项: List[str] = []
    防具精通属性: List[str] = []
    排行类型 = "物理百分比"
    适用属性 = "智力"
    适用数值 = 0
    类型 = ""
    武器类型 = ""
    防具类型 = ""
    转职 = ""
    # 技能栏: List[技能 | 主动技能 | 被动技能] = []
    # 技能序号: Dict[int, 技能 | 主动技能 | 被动技能] = {}
    技能栏: List[Union[技能, 主动技能, 被动技能]] = []
    技能序号: Dict[str, int] = {}
    自定义词条: Dict[int, List[int]] = {}
    buff: float = 1.00
    hotkey: List[str] = [""] * 14
    技能队列 = []
    护石技能 = []
    护石栏 = []
    符文 = []
    skills_passive: Dict = {}
    融合列表 = []
    武器融合 = []

    装扮栏: Dict[str, int] = {}
    装扮选项: Dict[str, str] = {}

    # 职业技能特殊选项
    individuation: Dict[str, int] = {}

    技攻列表: Dict[str, List[float]] = {}

    打造: Dict = {}
    觉醒技能 = []
    冷却缩减 = 1.0
    冷却恢复 = 0.0
    tip_part: List[str] = []
    trigger_set = {}
    eq_params = {}
    suits = []
    特性列表 = []

    def __init__(self, equVersion="") -> None:
        self.equVersion = equVersion
        self.eq_params = {}
        # 计算变量 ##########
        self.__基础力量: int = 0
        self.__基础智力: int = 0
        self.__基础体力: int = 0
        self.__基础精神: int = 0

        self.进图力量: int = 0
        self.进图智力: int = 0
        self.__进图体力: int = 0
        self.__进图精神: int = 0
        self.__进图三攻: int = 0
        self.__BUFF补正智力: int = 0
        self.__BUFF补正体力: int = 0
        self.__BUFF补正精神: int = 0

        self.__力量: int = 0
        self.__智力: int = 0
        self.__体力: int = 0
        self.__精神: int = 0

        self.系统奶系数: float = 0.0
        self.系统奶基数: float = 0.0

        self.冷却缩减 = 1.0
        self.冷却恢复 = 0

        self.斗神宠物 = 1.0
        # self.年宠技能 = False
        # self.白兔子技能 = False
        # self.斗神之吼秘药 = False

        self.辅助对象力智 = 5000
        self.辅助对象三攻 = 3000

        self.__物理攻击力: int = 65
        self.__魔法攻击力: int = 65
        self.__独立攻击力: int = 1134
        self.__火属性强化: float = 13
        self.__冰属性强化: float = 13
        self.__光属性强化: float = 13
        self.__暗属性强化: float = 13

        # 旧词条
        self.__百分比力智: float = 0.0
        self.__百分比三攻: float = 0.0
        self.__伤害增加: float = 0.0
        self.__附加伤害: float = 0.0
        self.__属性附加: float = 0.0
        self.__暴击伤害: float = 0.0
        self.__最终伤害: float = 0.0
        self.技能攻击力: float = 1.0
        self.__面板技能攻击力: float = 1.0
        self.技能攻击力累加: float = 0.0
        self.__持续伤害: float = 0.0
        self.__加算冷却缩减: float = 0.0
        self.__百分比减防: float = 0.0
        self.__固定减防: int = 0
        self.__buff固定力智: int = 0
        self.__buff百分比力智: float = 1.0
        self.__buff固定三攻: int = 0
        self.__buff百分比三攻: float = 1.0

        self.__觉醒固定力智: int = 0
        self.__觉醒百分比力智: float = 1.0
        self.__觉醒百分比力智Total: float = 1.0

        # 其它词条
        self.__攻击速度: float = 0.00
        self.__攻击速度_其他: float = 0.00
        self.__移动速度: float = 0.00
        self.__施放速度: float = 0.00
        self.__命中率: float = 0.0
        self.__回避率: float = 0.0
        self.__物理暴击率: float = 0.00
        self.__魔法暴击率: float = 0.00
        self.__火属性抗性: int = 0
        self.__冰属性抗性: int = 0
        self.__光属性抗性: int = 0
        self.__暗属性抗性: int = 0

        self.属强抗性倍率 = 1.0

        # 新属性
        self.__攻击强化: int = 0
        self.__百分比攻击强化: float = 0.0
        self.__buff量: int = 0
        self.__百分比buff量: float = 0.0
        self.__基础精通倍率: float = 1.0
        self.伤害比例: Dict[str, float] = {
            "直伤": 1.0,
            "中毒": 0.0,
            "灼伤": 0.0,
            "感电": 0.0,
            "出血": 0.0,
        }
        self.伤害系数: Dict[str, float] = {
            "中毒": 1.0,
            "灼伤": 1.0,
            "感电": 1.0,
            "出血": 1.0,
        }
        self.特效 = []
        self.__异常抗性: Dict[str, float] = {}
        self.__异常抗性_职业基础: Dict[str, float] = {}
        self.__指令效果: Dict[str, float] = {}
        self.__MP消耗量: float = 1.0
        self.觉醒技能 = []

        self.skills_passive = {}
        self.异常基础加成 = {
            "中毒": 1.1,
            "灼伤": 1.0,
            "感电": 1.05,
            "出血": 1.1,
            "灼伤破冰": 1.1,
        }
        self.异常结算加成 = {
            "中毒": 1.0,
            "灼伤": 1.0,
            "感电": 1.0,
            "出血": 1.0,
            "灼伤破冰": 1.0,
        }
        self.异常时间 = {
            # 基础持续时间 持续时间增加值 持续时间增加率 CD
            "中毒": [5, 0, 1.0, 99],
            "灼伤": [5, 0, 1.0, 99],
            "感电": [10, 0, 1.0, 99],
            "出血": [3, 0, 1.0, 99],
            "冰冻": [5, 0, 10, 99],
        }
        self.打造 = {}
        self.trigger_set = {}
        for item in 部位列表 + ("称号", "宠物"):
            self.打造[item] = {
                # 成长
                "attack": [0] * 4,
                # 成长
                "buffer": [0] * 4,
                # 强化
                "强化四维": [0] * 4,
                # 增幅
                "增幅四维": [0] * 4,
                # 攻击力
                "强化攻击力": [0] * 3,
                # 独立,四维
                "锻造加成": [0] * 2,
                "params": [[None]] * 4,
                "tips": [],
            }

        self.tip_part = []
        if self.转职 == "":
            self.转职 = self.职业

        # 设置基础属性
        self.__设置基础属性()
        self.技攻列表 = {}

    def __设置基础属性(self):
        temp = 获取基础属性(self.角色, self.职业)
        self.__基础力量 = temp[0]
        self.__基础智力 = temp[1]
        self.__基础体力 = temp[2]
        self.__基础精神 = temp[3]

        self.__力量 = self.__基础力量
        self.__智力 = self.__基础智力
        self.__体力 = self.__基础体力
        self.__精神 = self.__基础精神

        temp = 获取属性抗性基础(self.角色, self.职业)
        self.__火属性抗性 += temp[0]
        self.__冰属性抗性 += temp[1]
        self.__光属性抗性 += temp[2]
        self.__暗属性抗性 += temp[3]

        temp = 获取异常抗性基础(self.角色, self.职业)

        异常状态 = [
            "出血",
            "中毒",
            "灼伤",
            "感电",
            "冰冻",
            "减速",
            "眩晕",
            "诅咒",
            "失明",
            "石化",
            "睡眠",
            "混乱",
            "束缚",
        ]
        for index in range(0, len(异常状态)):
            self.异常抗性加成(异常状态[index], temp[index], mode=0)

    def 职业特殊设置(self):
        pass

    # region 返回前端信息

    def getinfo(self) -> Dict:
        info = {}
        info["alter"] = self.实际名称
        info["version"] = self.version
        info["name"] = self.名称
        info["character"] = self.职业
        info["role"] = "buffer" if self.类型 == "辅助" else "delear"
        info["weapon_types"] = self.武器选项
        info["carry_type_list"] = self.输出类型选项
        info["armor"] = self.防具类型
        info["armor_mastery"] = self.防具精通属性
        info["buff_ratio"] = self.buff
        self.set_skill_info(info)
        self.set_individuation(info)
        dress_list = {}
        i = 0
        for dress in 装扮集合:
            部位 = dress.部位
            if 部位 not in dress_list:
                dress_list[部位] = []
            选项集合 = dress.选项集合
            if dress.部位 == "上衣":
                选项集合 = 选项集合 + tuple(info["clothes_coat"])
            elif dress.部位 == "下装":
                选项集合 = 选项集合 + tuple(info["clothes_pants"])
            data = {}
            data["id"] = i
            data["options"] = 选项集合
            data["part"] = 部位
            data["rarity"] = dress.品质
            data["suit"] = dress.套装
            data["name"] = "{品质}装扮{部位}".format(品质=dress.品质, 部位=dress.部位)
            i += 1
            dress_list[部位].append(data)
        info["dress"] = dress_list
        info["enchanting"] = get_enchanting_setinfo(self)
        info["emblem"] = get_emblems_setinfo(self)
        info["jade"] = get_jade_setinfo()
        info["especificity"] = get_equ(self.equVersion).get_funs_info(
            "specificity", self
        )
        info["asrahan"] = get_equ(self.equVersion).get_funs_info("asrahan", self)
        info["sundries"] = get_sundries_setinfo()

        for item in info["platinum"]:
            info["emblem"].append(
                {
                    "id": item,
                    "maxFame": 232,
                    "position": ["辅助装备", "魔法石"],
                    "props": item + " Lv+1" + " 四维 + 8",
                    "type": "技能",
                    "rarity": "白金",
                    "rate": 2000,
                }
            )
        return info

    def set_skills(self):
        pass

    def get_acitve_skill_detail(
        self, skill, temp_info, temp_char, weapon, ratio, skill_info
    ):
        if skill.是否有伤害:
            if len(skill.形态) == 0:
                skill.形态 = [""]
            if (
                self.实际名称 == "elven_knight"
                and len(list(filter(lambda x: "6c" in x, skill.形态))) > 0
            ):
                skill.形态 = list(filter(lambda x: "6c" in x, skill.形态))
            for 形态 in skill.形态:
                original = 0
                for i in ["直伤", "中毒", "灼伤", "感电", "出血"]:
                    original += skill.等效百分比(
                        char=temp_info, 武器类型=weapon, 形态=形态, 伤害类型=i
                    )
                skill_info["skills_active"].append(
                    {
                        "name": skill.名称,
                        "need_level": skill.所在等级,
                        "lv": skill.等级,
                        "data": original * ratio * skill.被动倍率,
                        "cd": skill.等效CD(武器类型=weapon, 输出类型=temp_info.类型, char=temp_info),
                        "mode": 形态,
                        "cost": skill.无色消耗,
                        "tp": skill.TP等级,
                    }
                )
                if skill.是否有护石 == 1:
                    temp = temp_char.get_skill_by_name(skill.名称)
                    cp = 0
                    for i in ["直伤", "中毒", "灼伤", "感电", "出血"]:
                        cp += temp.等效百分比(
                            char=temp_char, 武器类型=weapon, 形态=形态, 伤害类型=i
                        )
                    skill_info["skills_cp"].append(
                        {
                            "name": skill.名称,
                            "need_level": skill.所在等级,
                            "lv": skill.等级,
                            "data": cp * ratio * temp.被动倍率,
                            "cd": temp.等效CD(武器类型=weapon, 输出类型=temp_info.类型, char=temp_info),
                            "original_data": original * ratio * skill.被动倍率,
                            "original_cd": skill.等效CD(
                                武器类型=weapon, 输出类型=temp_info.类型, char=temp_info
                            ),
                            "mode": 形态,
                            "cost": temp.无色消耗,
                            "tp": skill.TP等级,
                        }
                    )
                pass
            pass

    def get_passive_skill_detail(self, skill, temp_info):
        if temp_info.类型 == "物理百分比":
            倍率 = skill.物理攻击力倍率(temp_info.武器类型)
            if 倍率 != 1:
                temp_info.skills_passive[skill.名称]["info"].append(
                    {
                        "type": "物理攻击力",
                        "info": [round((倍率 - 1) * 100), "所有", ""],
                    }
                )
            倍率 = skill.物理攻击力倍率进图(temp_info.武器类型)
            if 倍率 != 1:
                temp_info.skills_passive[skill.名称]["info"].append(
                    {
                        "type": "物理攻击力[进图]",
                        "info": [round((倍率 - 1) * 100), "所有", ""],
                    }
                )
        elif temp_info.类型 == "魔法百分比":
            倍率 = skill.魔法攻击力倍率(temp_info.武器类型)
            if 倍率 != 1:
                temp_info.skills_passive[skill.名称]["info"].append(
                    {
                        "type": "魔法攻击力",
                        "info": [round((倍率 - 1) * 100), "所有", ""],
                    }
                )
            倍率 = skill.魔法攻击力倍率进图(temp_info.武器类型)
            if 倍率 != 1:
                temp_info.skills_passive[skill.名称]["info"].append(
                    {
                        "type": "魔法攻击力[进图]",
                        "info": [round((倍率 - 1) * 100), "所有", ""],
                    }
                )

        elif temp_info.类型 == "物理固伤" or temp_info.类型 == "魔法固伤":
            倍率 = skill.独立攻击力倍率(temp_info.武器类型)
            if skill.名称 not in temp_info.skills_passive:
                return
            if 倍率 != 1:
                temp_info.skills_passive[skill.名称]["info"].append(
                    {
                        "type": "独立攻击力",
                        "info": [round((倍率 - 1) * 100), "所有", ""],
                    }
                )
            倍率 = skill.独立攻击力倍率进图(temp_info.武器类型)
            if skill.名称 not in temp_info.skills_passive:
                return
            if 倍率 != 1:
                temp_info.skills_passive[skill.名称]["info"].append(
                    {
                        "type": "独立攻击力[进图]",
                        "info": [round((倍率 - 1) * 100), "所有", ""],
                    }
                )

    def 设置觉醒技能(self):
        self.觉醒技能 = []
        for i in self.技能栏:
            if i.是否有伤害 == 1 and i.所在等级 in [50, 85, 100]:
                self.觉醒技能.append(i.名称)

    def getskillinfos(self):
        # 技能等级、技能TP
        for skill in self.技能栏:
            if skill.是否有伤害:
                skill.TP等级 = skill.TP上限
            skill.等级 = skill.基础等级
        # 宠物
        self.加算冷却缩减(0.05)
        self.技能等级加成("所有", 1, 95, 1)
        # 光环
        self.技能等级加成("所有", 1, 95, 1)
        # 至尊称号
        self.技能等级加成("被动", 95, 95, 1)
        self.职业特殊设置()
        # 白金、时装、BUFF
        self.set_skills()

        for skill in self.技能栏:
            self.skills_passive[skill.名称] = {
                "info": [],
                "lv": skill.等级,
                "need_lv": skill.所在等级,
            }

        self.加算冷却计算()

        ratio = self.buff

        infos = []
        for weapon in self.武器选项:
            temp_info = deepcopy(self)
            temp_char = deepcopy(self)
            temp_char.护石栏 = []
            for skill in temp_char.技能栏:
                if skill.是否有伤害 and skill.是否有护石 == 1:
                    temp_char.护石栏.append(skill.名称)
                    skill.装备护石(char=self)
            temp_info.武器类型 = weapon
            temp_info.职业特殊计算()
            temp_info.被动倍率计算()
            if self.类型 == "物理百分比":
                ratio *= temp_info.站街物理攻击力倍率() * temp_info.进图物理攻击力倍率()
            elif self.类型 == "魔法百分比":
                ratio *= temp_info.站街魔法攻击力倍率() * temp_info.进图魔法攻击力倍率()
            elif self.类型 == "物理固伤":
                ratio *= temp_info.站街独立攻击力倍率() * temp_info.进图独立攻击力倍率()
            elif self.类型 == "魔法固伤":
                ratio *= temp_info.站街独立攻击力倍率() * temp_info.进图独立攻击力倍率()
            temp_info.CD倍率计算()
            temp_info.伤害指数计算()
            temp_char.武器类型 = weapon
            temp_char.职业特殊计算()
            temp_char.被动倍率计算()
            temp_char.CD倍率计算()
            temp_char.伤害指数计算()
            skill_info = {
                "weapon": weapon,
                "skills_active": [],
                "skills_passive": [],
                "skills_cp": [],
                "type": temp_info.类型,
                "buff": temp_info.buff,
            }
            for skill in temp_info.技能栏:
                self.get_acitve_skill_detail(
                    skill, temp_info, temp_char, weapon, ratio, skill_info
                )
                self.get_passive_skill_detail(skill, temp_info)
            for i in temp_info.skills_passive:
                skill = temp_info.skills_passive[i]
                if len(skill["info"]) > 0:
                    for item in skill["info"]:
                        skill_info["skills_passive"].append(
                            {
                                "name": i,
                                "need_level": skill["need_lv"],
                                "lv": temp_info.get_skill_by_name(i).等级,
                                "data": item["info"][0],
                                "type": item["type"],
                                "remark": "{}{}".format(
                                    "、".join(item["info"][1].split(",")),
                                    "({}除外)".format(
                                        "、".join(item["info"][2].split(","))
                                    )
                                    if item["info"][2] != "无"
                                    and item["info"][2] != ""
                                    and item["info"][2] != 0
                                    else "",
                                ),
                            }
                        )
            infos.append(skill_info)
        return infos

    def 基础属性加成(
        self,
        物理攻击力=0.00,
        魔法攻击力=0.00,
        独立攻击力=0.00,
        三攻=0,
        力量=0.00,
        智力=0,
        力智=0,
        体力=0,
        精神=0,
        体精=0,
        四维=0,
        物理暴击率=0.00,
        魔法暴击率=0.00,
        暴击率=0.00,
        攻击速度=0.00,
        施放速度=0.00,
        移动速度=0.00,
        三速=0.00,
        火属性抗性=0,
        光属性抗性=0,
        冰属性抗性=0,
        暗属性抗性=0,
        所有属性抗性=0,
        所有异常抗性=0,
        所有职业异常抗性=0,
        进图力量=0.00,
        进图智力=0.00,
        **kwargs,
    ):
        self.__物理攻击力 += 物理攻击力 + 三攻
        self.__魔法攻击力 += 魔法攻击力 + 三攻
        self.__独立攻击力 += 独立攻击力 + 三攻
        self.__力量 += 力量 + 力智 + 四维
        self.__智力 += 智力 + 力智 + 四维
        self.__体力 += 体力 + 体精 + 四维
        self.__精神 += 精神 + 体精 + 四维
        self.__物理暴击率 += float(物理暴击率) + float(暴击率)
        self.__魔法暴击率 += float(魔法暴击率) + float(暴击率)
        self.__攻击速度 += float(攻击速度) + float(三速)
        self.__施放速度 += float(施放速度) + float(三速)
        self.__移动速度 += float(移动速度) + float(三速)
        self.__火属性抗性 += 火属性抗性 + 所有属性抗性
        self.__光属性抗性 += 光属性抗性 + 所有属性抗性
        self.__冰属性抗性 += 冰属性抗性 + 所有属性抗性
        self.__暗属性抗性 += 暗属性抗性 + 所有属性抗性
        self.进图力量 += 进图力量
        self.进图智力 += 进图智力
        for 类型 in [
            "中毒",
            "灼伤",
            "感电",
            "出血",
            "冰冻",
            "减速",
            "眩晕",
            "诅咒",
            "失明",
            "石化",
            "睡眠",
            "混乱",
            "束缚",
        ]:
            self.__异常抗性[类型] = self.__异常抗性.get(类型, 0.0) + 所有异常抗性
            self.__异常抗性_职业基础[类型] = (
                self.__异常抗性_职业基础.get(类型, 0.0) + 所有职业异常抗性
            )
        super().基础属性加成(
            物理攻击力,
            魔法攻击力,
            独立攻击力,
            三攻,
            力量,
            智力,
            力智,
            体力,
            精神,
            体精,
            四维,
            物理暴击率,
            魔法暴击率,
            暴击率,
            攻击速度,
            施放速度,
            移动速度,
            三速,
            火属性抗性,
            光属性抗性,
            冰属性抗性,
            暗属性抗性,
            所有属性抗性,
            所有异常抗性,
            所有职业异常抗性,
            进图力量,
            进图智力,
        )

    def set_skill_info(
        self, info, rune_except=[], clothes_pants=[], rune_start_lv=20
    ) -> None:
        skillInfo = []  # 技能
        rune = []  # 符文
        talisman = []  # 护石
        platinum = []  # 白金
        clothes_coat = []  # 时装
        for skill in self.技能栏:
            skill.等级 = skill.基础等级
            skillInfo.append(
                {
                    "name": skill.名称,
                    "type": skill.是否有伤害,
                    "need_level": skill.所在等级,
                    "level_master": skill.等级精通,
                    "level_max": skill.等级上限,
                    "cooldown": 0
                    if not skill.是否有伤害
                    else (
                        skill.CD[skill.等级] if isinstance(skill.CD, list) else skill.CD
                    ),
                    "current_level": skill.基础等级,
                    "data": 0 if not skill.是否有伤害 else skill.等效百分比(char=self),
                    "tp_max": skill.TP上限 if skill.是否有伤害 else None,
                    "tp_level": skill.TP等级 if skill.是否有伤害 else None,
                    "mode": [] if not skill.是否有伤害 else skill.形态,
                }
            )
            # 护石
            if skill.是否有伤害 == 1 and skill.是否有护石 == 1:
                talisman.append(skill.名称)
            # 符文
            if (
                skill.所在等级 >= rune_start_lv
                and skill.所在等级 <= 80
                and skill.所在等级 != 50
                and (
                    skill.是否有伤害 == 1
                    or (skill.是否主动 == 1 and self.类型 == "辅助")
                )
                and skill.名称 not in rune_except
            ):
                rune.append(skill.名称)
            # 白金
            if (
                skill.所在等级 >= 15
                and skill.所在等级 <= 70
                and skill.所在等级 not in [48, 50]
            ):
                platinum.append(skill.名称)
            # 时装
            if skill.所在等级 <= 95:
                clothes_coat.append(skill.名称)
        if self.类型 == "辅助":
            talisman += self.护石技能
        info["skills"] = skillInfo
        info["rune"] = rune
        info["talisman"] = talisman
        info["platinum"] = platinum
        info["clothes_coat"] = clothes_coat
        info["clothes_pants"] = clothes_pants

    def set_individuation(self, info) -> None:
        pass

    # endregion

    # region 词条属性
    def set_eq_params(self, key, value):
        self.eq_params[key] = value

    def add_eq_params(self, key, value, default=0):
        self.eq_params[key] = self.eq_params.get(key, default) + value

    def multiply_eq_params(self, key, value, default=1):
        self.eq_params[key] = self.eq_params.get(key, default) * value

    def get_eq_params(self, key, default=0):
        return self.eq_params.get(key, default)

    def 基础精通加成(self, x: float) -> None:
        self.__基础精通倍率 *= 1 + x

    def 百分比防御减少(self, x: float) -> None:
        self.__百分比减防 += x

    def 固定防御减少(self, x: int) -> None:
        self.__固定减防 += x

    def 伤害类型转化(self, 类型1: str, 类型2: str, x: float) -> None:
        # 直伤 中毒 灼伤 感电 出血
        # if self.伤害比例.get(类型1, 0.0) - x <= 0:
        #     pass
        self.伤害比例[类型1] = max(self.伤害比例.get(类型1, 0.0) - x, 0)
        self.伤害比例[类型2] = self.伤害比例.get(类型2, 0.0) + x

    def 异常增伤(self, 类型: str, x: float) -> None:
        # 中毒 灼伤 感电 出血
        self.伤害系数[类型] = self.伤害系数.get(类型, 1.0) + x

    def 异常抗性加成(self, 类型: str, x: float, mode: int = 1) -> None:
        # 中毒 灼伤 感电 出血 冰冻 减速 眩晕 诅咒 失明 石化 睡眠 混乱 束缚
        if mode == 1:
            self.__异常抗性[类型] = self.__异常抗性.get(类型, 0.0) + x
        else:
            self.__异常抗性_职业基础[类型] = self.__异常抗性_职业基础.get(类型, 0.0) + x

    def 异常抗性获取(self, 类型: str, mode: int = 1) -> float:
        # mode = 1 显示抗性 mode = 0 装备加成抗性
        return round(
            self.__异常抗性.get(类型, 0.0)
            + (self.__异常抗性_职业基础.get(类型, 0.0) if mode == 1 else 0.0),
            4,
        )

    def 属性攻击(self, 类型: str) -> None:
        pass

    def 所有异常抗性加成(self, x: float, mode: int = 1) -> None:
        for 类型 in [
            "中毒",
            "灼伤",
            "感电",
            "出血",
            "冰冻",
            "减速",
            "眩晕",
            "诅咒",
            "失明",
            "石化",
            "睡眠",
            "混乱",
            "束缚",
        ]:
            self.异常抗性加成(类型, x, mode)

    def 指令效果加成(self, 类型: str, x: float) -> None:
        # 所有 消耗无色 不消耗无色  (觉醒技能默认除外)
        self.__指令效果[类型] = self.__指令效果.get(类型, 1.0) * (1 + x)

    def 指令技攻加成(self, x: float, min=1, max=100, exc=[], excName=[]) -> None:
        count = 0
        for i in self.技能栏:
            if (
                i.所在等级 >= min
                and i.所在等级 <= max
                and i.所在等级 not in exc
                and i.手搓
                and i.名称 not in excName
            ):
                count += 1
                if i.是否有伤害 == 1:
                    i.倍率 *= 1 + x * self.技能伤害增加增幅
                if i.名称 == "鬼连斩":
                    self.get_skill_by_name("鬼连斩：极").额外加成 /= (
                        1 + x * self.技能伤害增加增幅
                    )
        return count

    def MP消耗量加成(self, x: float) -> None:
        self.__MP消耗量 += x

    def 攻击强化加成(self, x: float) -> None:
        self.__攻击强化 += x

    def 百分比攻击强化加成(self, x: float) -> None:
        self.__百分比攻击强化 += x
        super().百分比攻击强化加成(x)

    def buff量加成(self, x: float) -> None:
        self.__buff量 += x

    def 辅助属性加成(
        self,
        buff固定力智=0,
        buff百分比力智=0.0,
        buff固定三攻=0,
        buff百分比三攻=0.0,
        觉醒固定力智=0,
        觉醒百分比力智=0.0,
        buff量=0,
        百分比buff量=0.0,
        觉醒百分比力智Total=0.0,
    ):
        self.__buff固定力智 += buff固定力智
        self.__buff百分比力智 *= 1.0 + buff百分比力智
        self.__buff固定三攻 += buff固定三攻
        self.__buff百分比三攻 *= 1.0 + buff百分比三攻
        self.__觉醒固定力智 += 觉醒固定力智
        self.__觉醒百分比力智 *= 1.0 + 觉醒百分比力智
        self.__觉醒百分比力智Total *= 1.0 + 觉醒百分比力智Total
        self.__buff量 += buff量
        self.__百分比buff量 += 百分比buff量

        super().辅助属性加成(
            buff固定力智,
            buff百分比力智,
            buff固定三攻,
            buff百分比三攻,
            觉醒固定力智,
            觉醒百分比力智,
            buff量,
            百分比buff量,
        )

    def 附加伤害加成(self, x: float, 辟邪玉加成=1) -> None:
        self.__附加伤害 += self.附加伤害增加增幅 * x if 辟邪玉加成 == 1 else x

    def 持续伤害加成(self, x: float) -> None:
        self.__持续伤害 += x

    def 属性附加加成(self, x: float) -> None:
        self.__属性附加 += self.属性附加伤害增加增幅 * x

    def 技能攻击力加成(
        self, x: float, 辟邪玉加成=1, 适用累加=1, part="", show=True
    ) -> None:
        if x != 0:
            self.技攻列表[part] = self.技攻列表.get(part, []) + [x]
        last = 0
        if 辟邪玉加成 == 1:
            if 适用累加 == 0:
                last = self.技能伤害增加增幅 * x
                # self.技能攻击力 *= 1 + self.技能伤害增加增幅 * x
            else:
                if self.技能攻击力累加 > 2:  # 累计已经大于2不再加成
                    # self.技能攻击力 *= 1 + x
                    last = x
                elif (
                    self.技能攻击力累加 + x > 2
                ):  # 此次累计导致大于2，一部分加成，一部分不加成
                    overflow = self.技能攻击力累加 + x - 2  # 溢出部分
                    # self.技能攻击力 *= 1 + self.技能伤害增加增幅 * (x - overflow) + overflow
                    last = self.技能伤害增加增幅 * (x - overflow) + overflow
                else:  # 累计后仍小于等于2
                    # self.技能攻击力 *= 1 + self.技能伤害增加增幅 * x
                    last = self.技能伤害增加增幅 * x
                self.技能攻击力累加 += x  # 累计计算
        else:
            last = x
            # self.技能攻击力 *= 1 + x
        self.技能攻击力 *= 1 + last
        self.__面板技能攻击力 *= 1 + (last if show else 0)
        # print(self.技攻列表)
        super().技能攻击力加成(x=x)

    def 暴击伤害加成(self, x: float, 辟邪玉加成=1) -> None:
        self.__暴击伤害 += self.暴击伤害增加增幅 * x if 辟邪玉加成 == 1 else x

    def 伤害增加加成(self, x: float, 辟邪玉加成=1) -> None:
        self.__伤害增加 += self.伤害增加增幅 * x if 辟邪玉加成 == 1 else x

    def 最终伤害加成(self, x: float, 辟邪玉加成=1) -> None:
        self.__最终伤害 += self.最终伤害增加增幅 * x if 辟邪玉加成 == 1 else x

    def 百分比力智加成(self, x: float, 辟邪玉加成=1) -> None:
        self.__百分比力智 += self.力量智力增加增幅 * x if 辟邪玉加成 == 1 else x

    def 百分比三攻加成(self, x: float, 辟邪玉加成=1) -> None:
        self.__百分比三攻 += self.物理魔法攻击力增加增幅 * x if 辟邪玉加成 == 1 else x

    def 火属性强化加成(self, x: float, 辟邪玉加成=1, mode=0) -> None:
        if mode == 0:
            self.__火属性强化 += self.所有属性强化增幅 * x if 辟邪玉加成 == 1 else x
        else:
            self.__火属性强化 += int(self.所有属性强化增幅 * x)

    def 冰属性强化加成(self, x: float, 辟邪玉加成=1, mode=0) -> None:
        if mode == 0:
            self.__冰属性强化 += self.所有属性强化增幅 * x if 辟邪玉加成 == 1 else x
        else:
            self.__冰属性强化 += int(self.所有属性强化增幅 * x)

    def 光属性强化加成(self, x: float, 辟邪玉加成=1, mode=0) -> None:
        if mode == 0:
            self.__光属性强化 += self.所有属性强化增幅 * x if 辟邪玉加成 == 1 else x
        else:
            self.__光属性强化 += int(self.所有属性强化增幅 * x)

    def 暗属性强化加成(self, x: float, 辟邪玉加成=1, mode=0) -> None:
        if mode == 0:
            self.__暗属性强化 += self.所有属性强化增幅 * x if 辟邪玉加成 == 1 else x
        else:
            self.__暗属性强化 += int(self.所有属性强化增幅 * x)

    def 所有属性强化加成(
        self,
        所有属性强化: float = 0,
        火属性强化: float = 0.00,
        冰属性强化: float = 0.00,
        光属性强化: float = 0.00,
        暗属性强化: float = 0.00,
        辟邪玉加成=1,
        mode=0,
    ) -> None:
        super().所有属性强化加成(
            所有属性强化, 火属性强化, 冰属性强化, 光属性强化, 暗属性强化
        )
        火属性强化 += 所有属性强化
        冰属性强化 += 所有属性强化
        光属性强化 += 所有属性强化
        暗属性强化 += 所有属性强化
        # if 火属性强化 > 0:
        self.火属性强化加成(火属性强化, 辟邪玉加成, mode)
        # if 冰属性强化 > 0:
        self.冰属性强化加成(冰属性强化, 辟邪玉加成, mode)
        # if 光属性强化 > 0:
        self.光属性强化加成(光属性强化, 辟邪玉加成, mode)
        # if 暗属性强化 > 0:
        self.暗属性强化加成(暗属性强化, 辟邪玉加成, mode)
        # if mode == 0:
        #     temp = self.所有属性强化增幅 * 所有属性强化 if 辟邪玉加成 == 1 else 所有属性强化
        # else:
        #     temp = int(self.所有属性强化增幅 * 所有属性强化)
        # self.__所有属性强化(temp)
        # super().属性强化加成(所有属性强化=所有属性强化)

    def 火属性抗性加成(self, x: int) -> None:
        self.__火属性抗性 += x

    def 冰属性抗性加成(self, x: int) -> None:
        self.__冰属性抗性 += x

    def 光属性抗性加成(self, x: int) -> None:
        self.__光属性抗性 += x

    def 暗属性抗性加成(self, x: int) -> None:
        self.__暗属性抗性 += x

    def 所有属性抗性加成(self, x: int) -> None:
        self.火属性抗性加成(x)
        self.冰属性抗性加成(x)
        self.光属性抗性加成(x)
        self.暗属性抗性加成(x)

    def 攻击速度增加(self, x: float, part: str = "") -> None:
        if part != "武器" and part != "特性":
            self.__攻击速度 += x
        else:
            self.__攻击速度_其他 += x

    def 攻击速度(self) -> float:
        return self.__攻击速度

    def 移动速度增加(self, x: float) -> None:
        self.__移动速度 += x

    def 施放速度增加(self, x: float) -> None:
        self.__施放速度 += x

    def 所有速度增加(self, x: float, part: str = "") -> None:
        if part != "武器" and part != "特性":
            self.__攻击速度 += x
        else:
            self.__攻击速度_其他 += x
        self.__移动速度 += x
        self.__施放速度 += x

    def 命中率增加(self, x: float) -> None:
        self.__命中率 += x

    def 回避率增加(self, x: float) -> None:
        self.__回避率 += x

    def 物理暴击率增加(self, x: float) -> None:
        self.__物理暴击率 += x

    def 魔法暴击率增加(self, x: float) -> None:
        self.__魔法暴击率 += x

    def 暴击率增加(self, x: float) -> None:
        self.物理暴击率增加(x)
        self.魔法暴击率增加(x)

    def buff技能等级加成(self, LV: int, lv: int) -> None:
        # LV级 buff技能等级 + lv
        pass

    def 特殊主动等级加成(self, Lv: int, lv: int) -> None:
        for i in self.技能栏:
            if (
                i.所在等级 == Lv
                and i.是否主动 == 1
                and i.名称 not in ["念兽：龙虎啸", "风雷啸", "圣灵符文", "神圣之光"]
            ):
                i.等级加成(lv, char=self)

    def 技能获取(self, min: int, max: int, exc=[]) -> None:
        temp = []
        for i in self.技能栏:
            if (
                i.所在等级 >= min
                and i.所在等级 <= max
                and i.是否主动 == 1
                and i.名称 not in exc
            ):
                temp.append(i.名称)
        return temp

    def 技能等级加成(
        self, 加成类型: str, min: int, max: int, lv: int, exc=[], excName=[]
    ) -> None:
        for i in self.技能栏:
            if (
                i.所在等级 >= min
                and i.所在等级 <= max
                and i.所在等级 not in exc
                and i.名称 not in excName
            ):
                if 加成类型 == "所有":
                    i.等级加成(lv, char=self)
                else:
                    if (i.是否主动 == 1) == (加成类型 == "主动"):
                        i.等级加成(lv, char=self)

        super().技能等级加成(加成类型, min, max, lv, exc)

    def 技能冷却缩减(self, min: int, max: int, x: float, exc=[], excName=[]) -> None:
        if min == 1 and max == 100:
            self.冷却缩减 *= 1 - x
        for i in self.技能栏:
            if (
                i.所在等级 >= min
                and i.所在等级 <= max
                and i.所在等级 not in exc
                and i.名称 not in excName
            ):
                if i.是否有伤害 == 1:
                    i.CDR *= 1 - x

    def 无色技能加成(self, cost=0, x=0, min=1, max=100):
        # 不消耗无色的技能加成
        if cost == 0:
            for skill in self.技能队列:
                if not (min == 1 and max == 100):
                    lv = self.get_skill_by_name(skill["名称"]).所在等级
                    if lv < min or lv > max:
                        continue
                if (
                    skill["名称"] == "神罚之锤"
                    and self.实际名称 == "crusader_male_carry"
                ):
                    skill["倍率"] *= (
                        1 + x * self.get_skill_by_name("神罚之锤").非无色占比()
                    )
                elif skill["无色消耗"] == 0 and skill["名称"] != "鬼连斩：极":
                    skill["倍率"] *= 1 + x
            pass
        if cost > 0:
            for skill in self.技能队列:
                if not (min == 1 and max == 100):
                    lv = self.get_skill_by_name(skill["名称"]).所在等级
                    if lv < min or lv > max:
                        continue
                if (
                    skill["名称"] == "神罚之锤"
                    and self.实际名称 == "crusader_male_carry"
                ):
                    skill["倍率"] *= (
                        1 + x * self.get_skill_by_name("神罚之锤").无色占比()
                    )
                elif skill["无色消耗"] >= cost:
                    skill["倍率"] *= 1 + x
            pass

    def 加算冷却缩减(self, x: float) -> None:
        self.__加算冷却缩减 += x

    def 技能恢复加成(self, min: int, max: int, x: float, exc=[], excName=[]) -> None:
        if min == 1 and max == 100:
            self.冷却恢复 += x
        for i in self.技能栏:
            if (
                i.所在等级 >= min
                and i.所在等级 <= max
                and i.所在等级 not in exc
                and i.名称 not in excName
            ):
                if i.是否有伤害 == 1:
                    i.恢复 += x

    def 技能倍率加成(
        self,
        min: int,
        max: int,
        x: float,
        exc=[],
        type="all",
        excName=[],
        changeSkill=False,
    ) -> None:
        for i in self.技能栏:
            if (
                i.所在等级 >= min
                and i.所在等级 <= max
                and i.所在等级 not in exc
                and i.名称 not in excName
            ):
                if i.是否有伤害 == 1:
                    if type == "all" or (type == "active" and i.是否主动 == 1):
                        if changeSkill:
                            i.倍率 *= 1 + x * self.技能伤害增加增幅
                        else:
                            i.技攻 *= 1 + x * self.技能伤害增加增幅

    def 单技能加成(self, 名称: str, 倍率=1.0, CD=1.0, lv=0) -> None:
        i = self.get_skill_by_name(名称)
        i.等级加成(lv, char=self)
        if i.是否有伤害 == 1:
            i.倍率 *= 倍率
            i.CDR *= CD

    def __所有属性强化(self, x: float) -> None:
        self.__火属性强化 += x
        self.__冰属性强化 += x
        self.__光属性强化 += x
        self.__暗属性强化 += x

    def 斗神宠物加成(self, x: float) -> None:
        self.斗神宠物 += x

    # endregion

    # region 面板相关函数

    # 基础力量智力(站街力量智力)
    def 站街力量(self) -> int:
        return int(self.__力量)

    def 站街智力(self) -> int:
        return int(self.__智力)

    def MP消耗倍率(self) -> float:
        return self.__MP消耗量

    def 火属性强化(self) -> float:
        if self.check_fun_by_id(20045):
            return max(
                [
                    self.__火属性强化,
                    self.__冰属性强化,
                    self.__光属性强化,
                    self.__暗属性强化,
                ]
            )
        return self.__火属性强化

    def 冰属性强化(self) -> float:
        if self.check_fun_by_id(20045):
            return max(
                [
                    self.__火属性强化,
                    self.__冰属性强化,
                    self.__光属性强化,
                    self.__暗属性强化,
                ]
            )
        return self.__冰属性强化

    def 光属性强化(self) -> float:
        if self.check_fun_by_id(20045):
            return max(
                [
                    self.__火属性强化,
                    self.__冰属性强化,
                    self.__光属性强化,
                    self.__暗属性强化,
                ]
            )
        return self.__光属性强化

    def 暗属性强化(self) -> float:
        if self.check_fun_by_id(20045):
            return max(
                [
                    self.__火属性强化,
                    self.__冰属性强化,
                    self.__光属性强化,
                    self.__暗属性强化,
                ]
            )
        return self.__暗属性强化

    def 火属性抗性(self) -> float:
        return int(self.__火属性抗性 * self.属强抗性倍率)

    def 冰属性抗性(self) -> float:
        return int(self.__冰属性抗性 * self.属强抗性倍率)

    def 光属性抗性(self) -> float:
        return int(self.__光属性抗性 * self.属强抗性倍率)

    def 暗属性抗性(self) -> float:
        return int(self.__暗属性抗性 * self.属强抗性倍率)

    def 被动力智系数(self) -> float:
        return 0

    # 新词条计算的力量智力

    def 基础面板力量(self) -> float:
        return (
            (
                self.__力量
                + int(
                    (self.__力量 - self.__基础力量) * self.系统奶系数 + self.系统奶基数
                )
            )
            + self.进图力量
        ) * (1 + self.被动力智系数())

    def 基础面板智力(self) -> float:
        return (
            (
                self.__智力
                + int(
                    (self.__智力 - self.__基础智力) * self.系统奶系数 + self.系统奶基数
                )
            )
            + self.进图智力
        ) * (1 + self.被动力智系数())

    # 旧词条计算的力量智力(图内力量智力)

    def 面板力量(self) -> float:
        return (self.基础面板力量()) * (1 + self.__百分比力智)

    def 面板智力(self) -> float:
        return (self.基础面板智力()) * (1 + self.__百分比力智)

    # 站街生效的技能三攻倍率

    def 站街物理攻击力倍率(self) -> float:
        站街物理攻击倍率 = 1.0
        for i in self.技能栏:
            if hasattr(i, "物理攻击力倍率"):
                倍率 = i.物理攻击力倍率(self.武器类型)
                if 倍率 != 1 and 倍率  is not None:
                    站街物理攻击倍率 *= 倍率
        return 站街物理攻击倍率

    def 站街魔法攻击力倍率(self) -> float:
        站街魔法攻击倍率 = 1.0
        for i in self.技能栏:
            if hasattr(i, "魔法攻击力倍率"):
                倍率 = i.魔法攻击力倍率(self.武器类型)
                if 倍率 != 1 and 倍率  is not None:
                    站街魔法攻击倍率 *= 倍率
        return 站街魔法攻击倍率

    def 站街独立攻击力倍率(self) -> float:
        站街独立攻击倍率 = 1.0
        for i in self.技能栏:
            if hasattr(i, "独立攻击力倍率"):
                倍率 = i.独立攻击力倍率(self.武器类型)
                if 倍率 != 1 and 倍率  is not None:
                    站街独立攻击倍率 *= 倍率
        return 站街独立攻击倍率

    def 进图物理攻击力倍率(self) -> float:
        进图物理攻击倍率 = 1.0
        for i in self.技能栏:
            if hasattr(i, "物理攻击力倍率进图"):
                倍率 = i.物理攻击力倍率进图(self.武器类型)
                if 倍率 != 1 and 倍率  is not None:
                    进图物理攻击倍率 *= 倍率
        return 进图物理攻击倍率

    def 进图魔法攻击力倍率(self) -> float:
        进图魔法攻击倍率 = 1.0
        for i in self.技能栏:
            if hasattr(i, "魔法攻击力倍率进图"):
                倍率 = i.魔法攻击力倍率进图(self.武器类型)
                if 倍率 != 1 and 倍率  is not None:
                    进图魔法攻击倍率 *= 倍率
        return 进图魔法攻击倍率

    def 进图独立攻击力倍率(self) -> float:
        进图独立攻击倍率 = 1.0
        for i in self.技能栏:
            if hasattr(i, "独立攻击力倍率进图"):
                倍率 = i.独立攻击力倍率进图(self.武器类型)
                if 倍率 != 1 and 倍率  is not None:
                    进图独立攻击倍率 *= 倍率
        return 进图独立攻击倍率

    # 站街三攻

    def 站街物理攻击力(self) -> float:
        return self.__物理攻击力 * self.站街物理攻击力倍率()

    def 站街魔法攻击力(self) -> float:
        return self.__魔法攻击力 * self.站街魔法攻击力倍率()

    def 站街独立攻击力(self) -> float:
        return self.__独立攻击力 * self.站街独立攻击力倍率()

    # 新词条计算的三攻(旧词条需要额外乘百分比三攻)

    def 基础面板物理攻击力(self) -> float:
        面板物理攻击 = self.__物理攻击力 + int(self.__进图三攻)
        for i in self.技能栏:
            面板物理攻击 *= i.物理攻击力倍率进图(self.武器类型)
        return 面板物理攻击 * self.站街物理攻击力倍率()

    def 基础面板魔法攻击力(self) -> float:
        面板魔法攻击 = self.__魔法攻击力 + int(self.__进图三攻)
        for i in self.技能栏:
            面板魔法攻击 *= i.魔法攻击力倍率进图(self.武器类型)
        return 面板魔法攻击 * self.站街魔法攻击力倍率()

    def 基础面板独立攻击力(self) -> float:
        面板独立攻击 = self.__独立攻击力 + int(self.__进图三攻)
        for i in self.技能栏:
            面板独立攻击 *= i.独立攻击力倍率进图(self.武器类型)
        return 面板独立攻击 * self.站街独立攻击力倍率()

    # 图内显示的三攻(不参与伤害计算)

    def 面板物理攻击力(self) -> float:
        面板物理攻击 = (
            self.基础面板物理攻击力() * (1 + self.__百分比三攻) * (self.斗神宠物加成)
        )
        return 面板物理攻击

    def 面板魔法攻击力(self) -> float:
        面板魔法攻击 = (
            self.基础面板魔法攻击力() * (1 + self.__百分比三攻) * (self.斗神宠物加成)
        )
        return 面板魔法攻击

    def 面板独立攻击力(self) -> float:
        面板独立攻击 = self.基础面板独立攻击力() * (1 + self.__百分比三攻)
        return 面板独立攻击

    # endregion

    # region 其它函数
    #     def get_skill_by_name(self, name) -> 技能 | 主动技能 | 被动技能:

    def 部位是否穿戴(self, part):
        if self.部位装备.get(part, None)  is None and part not in [
            "光环",
            "武器装扮",
            "皮肤",
            "宠物装备-红",
            "宠物装备-绿",
            "宠物装备-蓝",
            "快捷装备",
        ]:
            return False
        else:
            return True

    def get_skill_by_name(self, name) -> Union[技能, 主动技能, 被动技能]:
        return self.技能栏[self.技能序号.get(name, 0)]

    def 已穿戴神话(self):
        for i in self.装备栏:
            temp = get_equ(self.equVersion).get_equ_by_id(i)
            if temp.品质 == "神话":
                return True
        return False

    def 传说词条等级之和(self):
        total = 0
        for i in self.装备栏:
            temp = get_equ(self.equVersion).get_equ_by_id(i)
            if (
                temp.等级 == 105
                and temp.部位 not in ["称号", "宠物"]
                and temp.品质 == "传说"
            ):
                total += sum(self.词条等级.get(temp.部位, [0]))
        return total

    def 已传说装备数目(self):
        count = 0
        for i in self.装备栏:
            temp = get_equ(self.equVersion).get_equ_by_id(i)
            if (
                temp.等级 == 105
                and temp.部位 not in ["称号", "宠物"]
                and temp.品质 == "传说"
            ):
                count += 1
        return count

    def 穿戴低于105(self):
        for i in self.装备栏:
            temp = get_equ(self.equVersion).get_equ_by_id(i)
            if temp.等级 < 105 and temp.部位 not in ["称号", "宠物"]:
                return True
        return False

    def 获取强化等级(self, part=[]):
        num = 0
        temp = part
        if len(temp) == 0:
            temp += 部位列表
        for i in temp:
            num += self.打造详情.get(i, {}).get("cursed_number", 0)
        return num

    def 获取改造等级(self, part=[]):
        num = 0
        temp = part
        if len(temp) == 0:
            temp += 部位列表
        for i in temp:
            num += self.打造详情.get(i, {}).get("wisdom_number", 0)
        return num

    # endregion

    # 打造设置

    def __打造设置(self, setinfo):
        self.打造详情 = setinfo
        for i in 部位列表 + (
            "称号",
            "宠物",
            "光环",
            "武器装扮",
            "皮肤",
            "宠物装备-红",
            "宠物装备-绿",
            "宠物装备-蓝",
            "快捷装备",
        ):
            from core.equipment.enchanting import get_encfunc_by_id

            id = setinfo.get(i, {}).get("enchanting", 0)
            self.部位附魔[i] = get_encfunc_by_id(id)

    def 技能队列设置(self, setinfo):
        self.技能队列 = []
        for item in setinfo:
            self.技能队列.append(
                {
                    "名称": item["name"],
                    "无色消耗": self.get_skill_by_name(item["name"]).无色消耗,
                    "倍率": 1.0,
                    "等级变化": 0,
                    "CDR": 1.0,
                    "恢复": 0,
                    "形态": item.get("mode", ""),
                }
            )

    def __药剂设置(self, setinfo):
        self.药剂 = setinfo

    def __怪物信息设置(self, id):
        from core.basic.monster import get_monster_data

        data = get_monster_data(str(id))
        self.防御输入 = data["防御"]
        self.火抗输入 = data["火抗"]
        self.冰抗输入 = data["冰抗"]
        self.光抗输入 = data["光抗"]
        self.暗抗输入 = data["暗抗"]
        pass

    def __场景设置(self, id):
        from core.basic.monster import get_scene_data

        data = get_scene_data(str(id))
        self.系统奶系数 = data["系统奶系数"]
        self.系统奶基数 = data["系统奶基数"]
        self.防御系数 = data["防御系数"]
        pass

    # 设置技能相关参数
    def __skill_set(self, setinfo):
        for i in setinfo:
            k = self.get_skill_by_name(i["name"])
            k.等级 = i["level"]
            k.TP等级 = i["tp"]
            k.手搓 = i["direct"]
            k.手搓指令数 = i["directNumber"]
            k.count = i["count"]

    # 设置装备选项参数
    def __equ_chose_set(self, setinfo):
        get_equ(self.equVersion).set_func_chose(setinfo)
        # for i in setinfo:
        #    equ.set_func_chose({i['id']: i['select']})

    def hotkey_set(self, setinfo):
        self.hotkey = setinfo

    def __set_char(self, info):
        self.类型 = info["carry_type"] if self.类型 != "辅助" else self.类型
        try:
            self.buff = info["buff_ratio"] / 100 + 1
        except Exception:
            raise ResponseException("请在技能页设置buff倍率")
        self.护石栏 = info["talisman_set"]
        self.符文 = info["rune_set"]

        pass

    # 设置穿戴的装备

    def __穿戴装备(self, idlist):
        self.装备栏 = []
        self.部位装备 = {}
        idlist = sorted(idlist)
        for i in idlist:
            装备 = get_equ(self.equVersion).get_equ_by_id(i)
            self.部位装备.update({装备.部位: i})
        for k in self.部位装备.keys():
            self.装备栏.append(self.部位装备[k])

    def __穿戴装扮(self, info):
        self.装扮栏 = {}
        self.装扮选项 = {}
        for i in info:
            self.装扮栏[i] = info[i].get("id", 0)
            self.装扮选项[i] = info[i].get("option", 0)
        # print(len(self.装扮栏))

    # region 伤害计算相关函数
    def __计算前预处理(self):
        # 防止中途变更影响其他计算
        self.__equ_chose_set(self.trigger_set)
        self.设置觉醒技能()
        self.职业特殊设置()
        self.__辟邪玉计算()
        self.护石计算()
        self.符文计算()
        self.装备属性计算()
        self.skills_passive = {}
        for i in self.技能栏:
            self.skills_passive[i.名称] = {"info": [], "lv": i.等级}
        self.职业特殊计算()
        if self.类型 != "辅助":
            self.CD倍率计算()
            self.加算冷却计算()
            self.被动倍率计算()
            self.伤害指数计算()

    def 适用数值计算(self):
        进图智力 = 0
        进图体力 = 0
        进图精神 = 0
        for skill in self.技能栏:
            if skill.是否启用:
                结算 = skill.结算统计(self)
                if skill.站街生效:
                    self.__智力 += 结算[2]
                    self.__体力 += 结算[3]
                    self.__精神 += 结算[4]
                else:
                    进图智力 += 结算[2]
                    进图体力 += 结算[3]
                    进图精神 += 结算[4]

        进图 = 0
        BUFF补正 = 0

        if self.适用属性 == "体力":
            进图 = self.__体力 + 进图体力
            BUFF补正 = self.__BUFF补正体力
        elif self.适用属性 == "精神":
            进图 = self.__精神 + 进图精神
            BUFF补正 = self.__BUFF补正精神
        else:
            进图 = self.__智力 + 进图智力
            BUFF补正 = self.__BUFF补正智力

        awake = self.get_skill_by_name("一次觉醒")
        buff = self.get_skill_by_name("BUFF")

        awake.适用数值 = 进图
        awake.一觉力智 = self.__觉醒固定力智
        awake.一觉力智per = self.__觉醒百分比力智
        awake.一觉力智perTotal = self.__觉醒百分比力智Total

        buff.适用数值 = 进图 + BUFF补正
        buff.BUFF力智per = self.__buff百分比力智
        buff.BUFF力智 = self.__buff固定力智
        buff.BUFF三攻per = self.__buff百分比三攻
        buff.BUFF三攻 = self.__buff固定三攻

        self.适用数值 = 进图
        # print('copaosee:', self.适用数值, [
        #       self.__智力, self.__体力, self.__精神], 进图, BUFF补正)

    def 站街系数(self):
        if self.适用属性 == "体力":
            return self.__体力
        elif self.适用属性 == "精神":
            return self.__精神
        return self.__智力

    def 提升率计算(self, 总数据):
        力智合计 = 0
        三攻合计 = 0

        for i in 总数据:
            力智合计 += i[0]
            三攻合计 += i[1]

        x1 = (
            (
                self.辅助对象力智
                + (self.辅助对象力智 - 950) * self.系统奶系数
                + self.系统奶基数
            )
            / 250
            + 1
        ) * self.辅助对象三攻

        x2 = (
            (
                self.辅助对象力智
                + (self.辅助对象力智 - 950) * self.系统奶系数
                + self.系统奶基数
                + 力智合计
            )
            / 250
            + 1
        ) * (self.辅助对象三攻 + 三攻合计)
        return [
            x2 / x1 * 100 * self.被动增伤倍率,
            int(self.站街系数()),
            力智合计,
            三攻合计,
        ]

    def BUFF量(self):
        return self.__buff量 * (1 + self.__百分比buff量)

    def 辅助计算(self):
        self.适用数值计算()
        data = {}
        data["无色消耗"] = 0

        skills = {}

        values = []

        CDR = []

        for i in self.技能栏:
            rs = i.结算统计(self)[:2]
            cd = "-" if not i.是否主动 else i.等效CD()
            cd_p = "-" if not i.是否主动 else round(100 - i.等效CD() / i.CD * 100, 2)
            k = {}
            k["name"] = i.名称
            k["data"] = rs
            if hasattr(i, "适用数值"):
                k["apply_status"] = i.适用数值
            if sum(rs) > 0 or cd != "-":
                values.append(rs)
                skills[i.名称] = {
                    "name": i.名称,
                    "level": i.等级,
                    "data": rs,
                    "cd": cd,
                    "cd_p": cd_p,
                }
            if i.是否主动:
                CDR.append(
                (i.名称,cd_p/100,cd)
                )
                pass
        结果 = self.提升率计算(values)

        data["total_data"] = 结果[0]
        data["buffer_addition"] = 结果
        data["skills"] = skills
        data["CDR"] = CDR

        return data

    def 结果计算(self):
        if self.类型 == "辅助":
            return self.辅助计算()
        else:
            return self.伤害计算()

    def 职业特殊计算(self):
        pass

    def 伤害计算技能特殊处理(self, skill: 技能):
        pass

    def 异常系数计算(self, item, skill):
        cur = item
        pa = ""
        if item == "中毒":
            pa = "zd_rate"
        if item == "出血":
            pa = "cx_rate"
        if item == "感电":
            pa = "gd_rate"
        if item == "灼伤":
            pa = "zs_rate"
        if (
            item == "灼伤"
            and "灼伤" in get_global_data("state_type", self.equVersion)
            and (
                "冰冻" in get_global_data("get_state_type", self.equVersion)
                or (
                    "冰冻" in get_global_data("state_type", self.equVersion)
                    and self.check_equ_by_name("永眠前的准备")
                )
            )
        ):
            pa = "zs_bd_rate"
            cur = "灼伤破冰"
        保有率 = 0
        异常基础加成 = 1.0
        异常结算加成 = 1.0
        装备加成异常结算 = 1.0
        if pa == "zs_bd_rate":
            保有率 = self.异常保有率计算(pa, cur)
            异常基础加成 = 1.0
            异常结算加成 = self.异常基础加成["灼伤破冰"]
            装备加成异常结算 = self.异常结算加成.get(cur, 1.0)
        else:
            保有率 = self.异常保有率计算(pa, cur)
            # 叠层处理
            异常基础加成 = 1 + (self.异常基础加成.get(cur, 1.0) - 1) * get_global_data(
                pa, self.equVersion, 1.0
            )
            异常结算加成 = 1.0
            装备加成异常结算 = self.异常结算加成.get(cur, 1.0)
        系数 = self.伤害系数.get(item, 0.0) * (
            (1 - 保有率) * 异常基础加成
            + 保有率 * 异常基础加成 * 异常结算加成 * 装备加成异常结算
        )
        return 系数
        pass

    def 伤害计算(self):
        data = {}
        total_data = 0

        skill_dict = {}
        # 无色消耗 = 0
        CDR = []

        for i in self.技能队列:
            k = self.get_skill_by_name(i["名称"])
            if k.是否有伤害 == 1:
                temp = skill_dict.get(k.名称, {})
                self.伤害计算技能特殊处理(k)
                if k.名称 not in data.keys():
                    temp["rate"] = k.被动倍率
                    if temp.get("cd", 0) > 0:
                        temp["cd"] = (
                            k.等效CD(
                                武器类型=self.武器类型,
                                输出类型=self.类型,
                                额外CDR=i["CDR"],
                                额外恢复=i["恢复"],
                                形态=i["形态"],
                                char=self
                            )
                            + temp["cd"] * temp["count"]
                        ) / (temp["count"] + 1)
                    else:
                        temp["cd"] = k.等效CD(
                            武器类型=self.武器类型,
                            输出类型=self.类型,
                            额外CDR=i["CDR"],
                            额外恢复=i["恢复"],
                            形态=i["形态"],
                            char=self
                        )
                    temp["mp"] = k.MP消耗(
                        武器类型=self.武器类型,
                        输出类型=self.类型,
                        额外倍率=self.__MP消耗量,
                        char=self,
                    )
                    temp["atk_rate"] = k.等效百分比(
                        武器类型=self.武器类型, 形态=i["形态"], char=self
                    )
                    temp["cosume_cube_frag"] = k.无色消耗
                    temp["level"] = k.等级
                    temp["cd_o"] = k.CD[k.等级] if isinstance(k.CD, list) else k.CD
                    temp["cd_unsave"] = (
                        (k.恢复 + i["恢复"])
                        if temp.get("cd_unsave", 1) == 1
                        else (temp.get("cd_unsave", 1) + k.恢复 + i["恢复"]) / 2
                    )
                直伤 = k.等效百分比(
                    武器类型=self.武器类型,
                    额外等级=i["等级变化"],
                    额外倍率=i["倍率"],
                    伤害类型="直伤",
                    形态=i["形态"],
                    char=self,
                )

                # 直伤处理：直伤伤害*比例*系数
                damage = (
                    直伤
                    * self.伤害指数
                    * k.被动倍率
                    * (self.伤害比例.get("直伤", 0.0))
                    / 100
                )
                for item in ["中毒", "灼伤", "感电", "出血"]:
                    系数 = self.异常系数计算(item, k)
                    # 直伤转换的异常处理：直伤伤害*异常比例*异常系数
                    damage += (
                        直伤
                        * self.伤害指数
                        * k.被动倍率
                        * (self.伤害比例.get(item, 0.0) * 系数)
                        / 100
                    )
                    # 异常伤害处理：异常伤害*异常系数
                    damage += (
                        k.等效百分比(
                            武器类型=self.武器类型,
                            额外等级=i["等级变化"],
                            额外倍率=i["倍率"],
                            伤害类型=item,
                            形态=i["形态"],
                            char=self,
                        )
                        * self.伤害指数
                        * k.被动倍率
                        * 系数
                        / 100
                    )
                total_data += damage
                temp["name"] = k.名称
                temp["damage"] = temp.get("damage", 0) + round(damage,0)
                temp["count"] = temp.get("count", 0) + 1
                skill_dict[k.名称] = temp
                # if k.名称 not in ['爆裂弹', '杀意波动', '万毒噬心诀', '神罚之锤']:
                #     无色消耗 += i['无色消耗']
                # if k.CD > 1:
                #     CDR.append(
                #         (k.名称, round(1 - temp.get('cd', 0)/temp.get('cd_o', 0), 4)))
        data["skills_passive"] = {}
        for i in self.技能栏:
            if i.关联技能 != ["无"] or i.冷却关联技能 != ["无"]:
                temp = {}
                temp["lv"] = i.等级
                temp["name"] = i.名称
                data["skills_passive"][i.名称] = temp
            if skill_dict.get(i.名称, None)  is not None:
                if (i.CD[k.等级] if isinstance(i.CD, list) else i.CD) > 1:
                    temp = skill_dict.get(i.名称, {})
                    if temp.get("cd_o", 0) == 0:
                        CDR.append((i.名称, 0, 0))
                    else:
                        CDR.append(
                            (
                                i.名称,
                                round(1 - temp.get("cd", 0) / temp.get("cd_o", 0), 4),
                                temp.get("cd", 0),
                            )
                        )
                pass
        data["skills"] = skill_dict
        data["total_data"] = round(total_data,0)
        # data['无色消耗'] = 无色消耗
        data["CDR"] = CDR
        dps = 0
        for temp in data["skills"]:
            skill = data["skills"][temp]
            try:
                dps += (
                    (skill["damage"] / skill["count"])
                    / skill["cd"]
                    * skill["damage"]
                    / total_data
                )
            except Exception:
                pass
        data["dps"] = dps
        return data

    def 装备属性计算(self):
        self.套装统计()
        self.装备基础()
        self.__时装基础()
        self.__附魔计算()
        self.__杂项计算()
        self.__徽章计算()
        if self.类型 != "辅助":
            self.药剂计算()
        self.__装备词条计算()

    def __时装基础(self):
        时装品级列表 = {}
        for 部位 in self.装扮栏:
            id = int(self.装扮栏[部位])
            时装 = 装扮集合[id]
            时装.效果(角色=self, 选项=self.装扮选项[部位])
            时装品级列表[时装.套装] = 时装品级列表.get(时装.套装, 0) + 1

        套装集合: List[装扮套装] = []

        for 套装 in 装扮套装集合:
            数量 = 时装品级列表.get(套装.名称, 0)
            if 数量 > 0:
                if 数量 >= 套装.所需数量:
                    查找 = len(
                        [
                            i
                            for i in 套装集合
                            if hasattr(i, "兼容于")
                            and i.兼容于 == 套装.名称
                            and i.所需数量 == 套装.所需数量
                        ]
                    )
                    if 查找 == 0:
                        套装集合.append(套装)
                else:
                    if hasattr(套装, "兼容于") and 套装.兼容于  is not None:
                        数量 += 时装品级列表.get(套装.兼容于, 0)
                        时装品级列表[套装.兼容于] = 数量
                        时装品级列表.pop(套装.名称)
        for 套装 in 套装集合:
            套装.效果(self)

        pass

    def __辟邪玉计算(self):
        if "jade" not in self.打造详情.keys():
            return
        setinfo = self.打造详情["jade"]
        info = {}
        for i in ["jade_First", "jade_Second", "jade_Third", "jade_Fourth"]:
            if i + "_type" in setinfo.keys():
                try:
                    id = setinfo[i + "_type"]
                    value = float(setinfo[i + "_value"])
                except Exception:
                    id = 0
                    value = 0
                info[str(id)] = info.get(str(id), 0) + value
        from core.equipment.jade import get_jadefunc_by_id

        for id in info.keys():
            func = get_jadefunc_by_id(int(id))
            func(self, value=info.get(str(id), 0))
            # 打印相关函数和效果

    def 护石计算(self):
        for item in self.护石栏:
            try:
                if item  is not None and item != "" and item != "无":
                    self.get_skill_by_name(item).装备护石(char=self)
            except Exception:
                pass

    def 符文计算(self):
        for item in self.符文:
            if item  is not None and item != "":
                skill_name: str = item[0:-1]
                type = item[-1]
                skill = self.get_skill_by_name(skill_name)

                if skill  is not None and skill.名称 == skill_name:
                    # 紫
                    if type == "1":
                        skill.倍率 *= 1.04
                        # 红
                    if type == "2":
                        skill.倍率 *= 1.06
                        skill.CDR *= 1.04
                        # 绿
                    if type == "3":
                        skill.倍率 *= 0.96
                        skill.CDR *= 0.93
                        # 蓝
                    if type == "4":
                        skill.CDR *= 0.95
                else:
                    print(f"skill not found {skill_name}")
            pass

    def __杂项计算(self, mode=0):
        if "others" not in self.打造详情.keys():
            return
        setinfo = self.打造详情["others"]
        # 收集箱
        try:
            from core.equipment.sundry import get_sundriesfunc_by_id

            func = get_sundriesfunc_by_id(setinfo["SJX_TYPE"])
            # print(func)
            func(self, 0, False, setinfo["SJX_XY"], setinfo["SJX_SQ"])
        except Exception:
            pass
        # 勋章
        try:
            from core.equipment.sundry import get_sundriesfunc_by_id

            func = get_sundriesfunc_by_id(setinfo["XZ_TYPE"])
            func(
                self,
                0,
                False,
                setinfo.get("XZ_SHZ", 0),
                setinfo.get("XZ_QH", 0),
                setinfo.get("XZ_GS", 0),
            )
        except Exception:
            pass
        # 勋章 - New
        # 老徽章选择为无 才生效
        if int(setinfo.get("XZ_TYPE", 0)) == 0:
            try:
                from core.equipment.sundry import get_sundriesfunc_by_id

                func = get_sundriesfunc_by_id(27063)
                func(
                    self,
                    0,
                    False,
                    setinfo.get("medal_quality", 0),
                    setinfo.get("medal_lv", 0),
                    [
                        setinfo.get("medal_gems_1", 0),
                        setinfo.get("medal_gems_2", 0),
                        setinfo.get("medal_gems_3", 0),
                        setinfo.get("medal_gems_4", 0),
                    ],
                    0.1,
                )
                pass
            except Exception:
                pass
        for i in setinfo.keys():
            if i.startswith("SJX") or i.startswith("XZ"):
                pass
            else:
                try:
                    id = setinfo[i]
                    from core.equipment.sundry import get_sundriesfunc_by_id

                    func = get_sundriesfunc_by_id(id)
                    # 站街
                    func(self)
                    # 进图
                    func(self, mode=1)
                except Exception:
                    pass

    def __徽章计算(self):
        idlist = []
        for i in 部位列表 + (
            "皮肤",
            "光环",
            "武器装扮",
        ):  # ('皮肤', '光环', '武器装扮', )
            if i in self.打造详情.keys() and self.部位是否穿戴(i):
                temp = self.打造详情[i]
                for j in ["socket_left", "socket_right"]:
                    id = temp.get(j, 0)
                    if id == 0:
                        pass
                    elif str(id).isdigit():
                        idlist.append(id)
                    else:
                        # 白金技能等级加成处理 id:技能名称
                        self.单技能加成(名称=id, lv=1)
                        self.基础属性加成(四维=8)
                        pass
        for i in idlist:
            from core.equipment.emblems import get_embfunc_by_id

            func = get_embfunc_by_id(i)
            func(self)
            # 打印相关函数和效果
            # print('{}: {}'.format(func, func(self, text=TRUE)))

    def __附魔计算(self):
        for i in self.部位附魔.keys():
            if self.部位是否穿戴(i):
                func = self.部位附魔[i]
                func(self, part=i)
                func(self, mode=1, part=i)
            # 打印相关函数和效果
            # print('{}: {}: {}'.format(i, func, func(self, text=TRUE)))

    def 装备基础(self):
        # 移除不符合版本的装备，不参与后续计算
        self.装备栏 = list(
            filter(
                lambda x: get_equ(self.equVersion).get_equ_by_id(x).名称 != "",
                self.装备栏,
            )
        )
        for id in self.装备栏:
            temp = get_equ(self.equVersion).get_equ_by_id(id)
            temp = get_equ(self.equVersion).get_equ_by_id(
                id, self.打造详情.get(temp.部位, {}).get("growth_sj", 0) > 0
            )
            if "甲" in temp.类型:
                self.__防具计算(temp)
            elif temp.类型 == "首饰":
                self.__首饰计算(temp)
            elif temp.类型 == "特殊装备":
                self.__特殊装备计算(temp)
            elif temp.部位 == "武器":
                self.武器计算(temp)
            elif temp.部位 in ["称号", "宠物"]:
                self.__称号宠物计算(temp)
            if temp.部位 not in ["称号", "宠物"]:
                self.__增幅计算(temp)
        pass

        # if temp.所属套装 != '智慧产物':
        #    return 精通计算(temp.等级, temp.品质, self.打造详情.get(部位, {}).get('cursed_number', 0), 部位)
        # else:
        #    return 精通计算(temp.等级, temp.品质, self.打造详情.get(部位, {}).get('wisdom_number', 0), 部位)

    def __防具计算(self, temp: equipment) -> None:
        self.基础属性加成(**temp.__dict__)

        部位 = temp.部位
        强化等级 = self.打造详情.get(部位, {}).get("cursed_number", 0)

        力量 = 智力 = 体力 = 精神 = 0

        if self.类型 == "辅助":
            if "智力" in self.防具精通属性:
                智力 += 辅助精通计算(
                    110 if temp.神 else temp.等级, temp.品质, 强化等级, 部位, "智力"
                )
            if "精神" in self.防具精通属性:
                精神 += 辅助精通计算(
                    110 if temp.神 else temp.等级, temp.品质, 强化等级, 部位, "精神"
                )
            if "体力" in self.防具精通属性:
                体力 += 辅助精通计算(
                    110 if temp.神 else temp.等级, temp.品质, 强化等级, 部位, "体力"
                )
        else:
            精通数值 = 精通计算(
                110 if temp.神 else temp.等级, temp.品质, 强化等级, 部位, self.防具类型
            )
            if "力量" in self.防具精通属性:
                力量 += 精通数值
            if "智力" in self.防具精通属性:
                智力 += 精通数值

        # if temp.等级 == 105:
        #     if self.类型 == '辅助':
        #         self.技能等级加成('主动', 30, 30, 1)
        #         self.技能等级加成('主动', 50, 50, 1)
        self.基础属性加成(力量=力量, 智力=智力, 体力=体力, 精神=精神)

    def __增幅计算(self, temp: equipment) -> None:
        if self.打造详情.get(temp.部位, {}).get("cursed_type", 1) == 1:
            x = 增幅计算(
                min(temp.等级, MAXEQULV),
                temp.品质,
                self.打造详情.get(temp.部位, {}).get("cursed_number", 0),
            )
            if self.类型 == "物理百分比" or self.类型 == "物理固伤":
                self.基础属性加成(力量=x)
                self.打造[temp.部位]["增幅四维"][0] = x
            elif self.类型 == "魔法百分比" or self.类型 == "魔法固伤":
                self.基础属性加成(智力=x)
                self.打造[temp.部位]["增幅四维"][1] = x
            elif self.类型 == "辅助":
                if self.适用属性 == "体力":
                    self.基础属性加成(体力=x)
                    self.打造[temp.部位]["增幅四维"][2] = x
                elif self.适用属性 == "精神":
                    self.基础属性加成(精神=x)
                    self.打造[temp.部位]["增幅四维"][3] = x
                else:
                    self.基础属性加成(智力=x)
                    self.打造[temp.部位]["增幅四维"][1] = x
        # if self.是否增幅[i] and temp.所属套装 != '智慧产物':
        #    x = 增幅计算(temp.等级, temp.品质, self.强化等级[i])

    def __称号宠物计算(self, temp: equipment) -> None:
        self.基础属性加成(**temp.__dict__)

    def __首饰计算(self, temp: equipment) -> None:
        self.基础属性加成(**temp.__dict__)
        # if temp.等级 == 105 and self.类型 == '辅助':
        #     self.技能等级加成('主动', 30, 30, 1)
        #     self.技能等级加成('主动', 50, 50, 1)

    def __特殊装备计算(self, temp: equipment) -> None:
        self.基础属性加成(**temp.__dict__)
        # if temp.等级 == 105 and self.类型 == '辅助':
        #     self.技能等级加成('主动', 30, 30, 1)
        #     self.技能等级加成('主动', 50, 50, 1)
        #     if temp.品质 == '史诗' and temp.部位 == '魔法石':
        #         self.技能等级加成('主动', 50, 50, 1)
        # 耳环
        if temp.部位 == "耳环":
            # if temp.所属套装 != '智慧产物':
            x = 耳环计算(
                min(temp.等级, MAXEQULV),
                temp.品质,
                self.打造详情.get(temp.部位, {}).get("cursed_number", 0),
            )
            self.打造["耳环"]["强化攻击力"] = [x] * 3
            self.基础属性加成(三攻=x)
        # 辅助装备、魔法石
        else:
            # if temp.所属套装 != '智慧产物':
            x = 左右计算(
                min(temp.等级, MAXEQULV),
                temp.品质,
                self.打造详情.get(temp.部位, {}).get("cursed_number", 0),
            )
            if self.类型 == "辅助":
                self.打造[temp.部位]["强化四维"] = [x] * 4
            else:
                self.打造[temp.部位]["强化四维"] = [x] * 2
            self.基础属性加成(四维=x)

    def 武器计算(self, temp: equipment) -> None:
        self.基础属性加成(**temp.__dict__)
        self.武器类型 = temp.类型
        # if temp.等级 == 105 and self.类型 == '辅助':
        #     self.技能等级加成('主动', 30, 30, 3)
        #     self.技能等级加成('主动', 50, 50, 4)
        # if temp.品质 == '史诗':
        #     self.技能等级加成('主动', 50, 50, 1)
        # if temp.所属套装 != '智慧产物':
        info = self.打造详情.get(temp.部位, {})
        # 暂时没有用110计算强化增幅的
        物理攻击力 = 武器强化计算(
            min(temp.等级, MAXEQULV),
            temp.品质,
            info.get("cursed_number", 0),
            temp.类型,
            "物理",
        )
        魔法攻击力 = 武器强化计算(
            min(temp.等级, MAXEQULV),
            temp.品质,
            info.get("cursed_number", 0),
            temp.类型,
            "魔法",
        )
        独立攻击力 = 锻造计算(
            min(temp.等级, MAXEQULV), temp.品质, info.get("dz_number", 0)
        )

        self.打造["武器"]["强化攻击力"] = [物理攻击力, 魔法攻击力, 0]

        self.打造["武器"]["锻造加成"][0] = 独立攻击力

        四维 = 0
        if self.类型 == "辅助":
            四维 = 锻造四维(min(temp.等级, MAXEQULV), temp.品质, info.get("dz_number", 0))
            self.打造["武器"]["锻造加成"][1] = 四维

        self.基础属性加成(
            物理攻击力=物理攻击力,
            魔法攻击力=魔法攻击力,
            独立攻击力=独立攻击力,
            四维=四维,
        )

    def 职业装备特殊计算(self) -> None:
        pass

    def 药剂计算(self, rate=1.0) -> None:
        from core.equipment.consumable import get_sundriesfunc_by_id

        for item in self.药剂:
            func = get_sundriesfunc_by_id(item)
            func(self, rate=rate, mode=0)
            func(self, rate=rate, mode=1)

    def 是否升级110(self, part):
        return self.词条等级[part][0] > 80

    def 兼容数量统计(self, suit):
        equs = get_equ(self.equVersion)
        count = 0
        for i in 部位列表:
            equ = equs.get_equ_by_id(self.部位装备.get(i, 0))
            if len(equ.suits) < 2:
                continue
            if suit in equ.suits:
                count += 1
        return count

    def 套装统计(self):
        suit = []
        self.suits = []
        equs = get_equ(self.equVersion)
        for i in 部位列表:
            equ = equs.get_equ_by_id(self.部位装备.get(i, 0))
            if len(equ.suits) < 0:
                continue
            # 星辰百变
            if len(equ.可选属性) > 0:
                if self.打造详情.get(i, {}).get("changeable", True):
                    suit += equ.suits
            else:
                suit += equ.suits
        for i in self.融合列表:
            equ = equs.get_equ_by_id(i)
            if len(equ.suits) < 0:
                continue
            suit += equ.suits
        suit_count = {}
        for i in set(suit):
            suit_count[i] = suit.count(i)
        suits = []
        compatibility = []
        for i in suit_count:
            suitsInfo = list(
                filter(
                    lambda x: x["suit_id"] == i and x["need_num"] <= suit_count[i],
                    equs.suit_info,
                )
            )
            for j in suitsInfo:
                suits.append(j["id"])
                compatibility += j["compatibility"]
        self.suits = list(set(suits) - set(compatibility))
        self.suitInfo = []
        for i in self.suits:
            temp = list(filter(lambda x: x["id"] == i, equs.suit_info))[0]
            self.suitInfo.append(f'{temp["name"]}[{temp["need_num"]}]')
        pass

    def __装备词条计算(self):
        # 攻击强化相关计算
        for i in 部位列表:
            temp = []
            equ = get_equ(self.equVersion).get_equ_by_id(self.部位装备.get(i, 0))
            if equ.品质 == "传说":
                # limit = 80
                # limit = 70
                # for j in [
                #     "growth_cs_first",
                #     "growth_cs_second",
                #     "growth_cs_third",
                #     "growth_cs_fourth",
                # ]:
                temp = [80] * 4
            else:
                temp = [140]*4
                # limit = 80
                # growth_sj = self.打造详情.get(i, {}).get("growth_sj", 0)
                # if growth_sj > 0:
                #     temp = [80 + growth_sj] * 4
                # else:
                #     for j in [
                #         "growth_first",
                #         "growth_second",
                #         "growth_third",
                #         "growth_fourth",
                #     ]:
                #         temp.append(min(limit, self.打造详情.get(i, {}).get(j, 1)))
                # 锁定等级 常规武器升级锁神40 传说武器锁定70
                for name in ["霜", "雨", "雷", "风", "焰", "失衡"]:
                    if equ.名称.startswith(f"{name} :"):
                        temp = [120] * 4
                if equ.名称.startswith("跨越之忆"):
                    temp = [70] * 4
            # limit = 70 if get_equ(self.equVersion).get_equ_by_id(
            #     self.部位装备.get(i, 0)).品质 == "传说" else 80
            # for j in ["growth_first", "growth_second", "growth_third", "growth_fourth"]:
            #     temp.append(min(limit, self.打造详情.get(i, {}).get(j, 1)))
            self.词条等级[i] = temp

        asrahan = False
        weapon = (
            get_equ(self.equVersion).get_equ_by_id(self.部位装备.get("武器", 0)).名称
        )
        for index, name in enumerate(["雷", "风", "霜", "焰", "雨", "失衡"]):
            if weapon.startswith(f"{name} :") and self.asrahan.get("type", 0) == index:
                asrahan = True
        if weapon.startswith("跨越之忆") and self.asrahan.get("type", 0) in [0, 1, 2, 3, 4]:
            asrahan = True
        if asrahan:
            get_equ(self.equVersion).get_asrahan()(
                self,
                self.asrahan.get("type", 0),
                self.asrahan.get("lv", 0),
                self.asrahan.get("additional", 0),
            )
        武器融合词条 = self.武器融合.get(str(self.部位装备.get("武器", 0)), [])
        成长词条组合 = get_equ(self.equVersion).get_damagelist_by_idlist(
            self.装备栏, self.自定义词条, self.融合列表, 武器融合词条
        )

        temp_params = {}
        for 部位, 序号, atk, buff, params, _type, index in 成长词条组合:
            if _type > 0:
                等级 = self.词条等级[部位][序号]
            else:
                # 贴膜/融合
                等级 = 1
            attack = 成长词条计算(atk, 等级, self.equVersion)
            if (
                get_equ(self.equVersion).get_equ_by_id(self.部位装备.get(部位, 0)).品质
                == "传说"
                and 等级 > 60
            ):
                attack += 10 * (等级 - 60) / 4
            buffer = 成长词条计算(buff, 等级, self.equVersion)
            self.攻击强化加成(attack)
            self.辅助属性加成(buff量=buffer)
            # 装备打造
            if _type > 0:
                self.打造[部位]["attack"][序号] = attack
                self.打造[部位]["buffer"][序号] = buffer
                self.打造[部位]["params"][序号] = []

            temp_params[部位] = temp_params.get(部位, {})
            temp_params[部位][str(序号)] = temp_params[部位].get(str(序号), [])

            params = [] if params  is None else params
            for param in params:
                param = 成长词条计算(param, 等级, self.equVersion)
                if _type > 0:
                    self.打造[部位]["params"][序号].append(param)
                temp_params[部位][str(序号)].append(param)

        # 词条效果相关计算
        for func, 部位, 序号, index, _type, id, 融合石词条位置 in get_equ(
            self.equVersion
        ).get_func_list_by_idlist(self):
            if _type > 0:
                等级 = self.词条等级[部位][序号]
            # 特性
            elif _type == -2:
                等级 = self.特性等级.get(str(index), 0)
            # 融合
            elif _type == -3:
                等级 = self.融合石等级.get(str(id),[0,0,0])[融合石词条位置]
            else:
                等级 = 1
            params = temp_params.get(部位, {}).get(str(序号), [])
            # print(部位, 序号, self.打造[部位]["params"][序号], index)
            params = [] if params == [None] else params
            # print(序号, params, index)
            # print(序号, params, 部位)
            res = func(self, mode=0, part=部位, lv=等级, params=params)  # 进图效果
            if res  is not None:
                # print(res, type(res))
                if isinstance(res,list):
                    for i in res:
                        self.打造[部位]["tips"].append(i)
                else:
                    self.打造[部位]["tips"].append(res)
                if 部位 not in self.tip_part:
                    self.tip_part.append(部位)

        for func, 部位, 序号, index, _type, id, 融合石词条位置 in get_equ(
            self.equVersion
        ).get_func_list_by_idlist(self):
            if _type > 0:
                等级 = self.词条等级[部位][序号]
            # 特性
            elif _type == -2:
                等级 = self.特性等级.get(str(index), 0)
            # 融合
            elif _type == -3:
                等级 = self.融合石等级.get(str(id),[0,0,0])[融合石词条位置]
            else:
                等级 = 1
            params = temp_params.get(部位, {}).get(str(序号), [])
            # print(部位, 序号, self.打造[部位]["params"][序号], index)
            params = [] if params == [None] else params
            # print(序号, params, index)
            # print(序号, params, 部位)
            # func(self, part=部位, lv=等级, params=params)  # 站街效果
            res = func(self, mode=1, part=部位, lv=等级, params=params)  # 进图效果
            if res  is not None:
                # print(res, type(res))
                if isinstance(res,list):
                    for i in res:
                        self.打造[部位]["tips"].append(i)
                else:
                    self.打造[部位]["tips"].append(res)
                if 部位 not in self.tip_part:
                    self.tip_part.append(部位)
            # 打印相关函数和效果
            # print('{}(lv.{}): {} {}'.format(部位, 等级, func, func(self, text=TRUE)))

    def check_fun_by_id(self, id):
        idList = get_equ(self.equVersion).get_func_list_by_idlist(self)
        return id in [index for _, _, _, index, _,_,_ in idList]

    def check_equ_by_name(self, name):
        id = get_equ(self.equVersion).get_equ_by_name(name).id
        return id > 0 and (id in self.装备栏 or id in self.融合列表)

    def check_fusion_upgrade(self, part):
        return self.打造详情.get(part, {}).get("fusion_upgrade", False)

    def 被动倍率计算(self):
        if self.__基础精通倍率 != 1:
            基础精通 = self.get_skill_by_name("基础精通")
            if 基础精通.名称 == "基础精通":
                基础精通.倍率 *= self.__基础精通倍率

        for i in self.技能栏:
            i.被动倍率 = 1
        for i in self.技能栏:
            for index in range(0, 4):
                index = "" if index == 0 else str(index)
                关联技能 = getattr(i, "关联技能" + index, ["无"])
                非关联技能 = getattr(i, "非关联技能" + index, ["无"])
                try:
                    加成倍率 = eval("i.加成倍率" + index + "(self.武器类型)")
                except Exception:
                    加成倍率 = 1.0
                try:
                    # print(i.名称, 加成倍率, eval("i.加成描述"+index+"(self.武器类型)"))
                    if 加成倍率 != 1:
                        self.skills_passive[i.名称]["info"].append(
                            {
                                "type": "倍率",
                                "info": eval("i.加成描述" + index + "(self.武器类型)"),
                            }
                        )
                except Exception:
                    pass
                if 关联技能 != ["无"]:
                    if 关联技能 == ["所有"]:
                        for j in self.技能栏:
                            if j.是否有伤害 == 1:
                                j.被动倍率 *= 加成倍率
                    else:
                        # print(self.技能序号)
                        for k in 关联技能:
                            self.技能栏[self.技能序号[k]].被动倍率 *= 加成倍率
                if 非关联技能 != ["无"]:
                    if 非关联技能 == ["所有"]:
                        for j in self.技能栏:
                            if j.是否有伤害 == 1:
                                j.被动倍率 /= 加成倍率
                    else:
                        for k in 非关联技能:
                            self.技能栏[self.技能序号[k]].被动倍率 /= 加成倍率

    def 加算冷却计算(self):
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                i.CDR *= 1 - self.__加算冷却缩减

    def CD倍率计算(self):
        for i in self.技能栏:
            for index in range(0, 4):
                index = "" if index == 0 else str(index)
                关联技能 = getattr(i, "冷却关联技能" + index, ["无"])
                非关联技能 = getattr(i, "非冷却关联技能" + index, ["无"])
                冷却类型 = getattr(i, "冷却类型" + index, 0)
                try:
                    加成倍率 = eval("i.CD缩减倍率" + index + "(self.武器类型)")
                except Exception:
                    加成倍率 = 1.0
                try:
                    if 加成倍率 != 1:
                        self.skills_passive[i.名称]["info"].append(
                            {
                                "type": "CDR",
                                "info": eval(
                                    "i.CD缩减描述" + index + "(self.武器类型)"
                                ),
                            }
                        )
                except Exception:
                    pass
                if 关联技能 != ["无"]:
                    if 关联技能 == ["所有"]:
                        for j in self.技能栏:
                            if j.是否有伤害 == 1:
                                if 冷却类型 == 0:
                                    j.CDR *= 加成倍率
                                if 冷却类型 == 1:
                                    j.CDR_O *= 加成倍率
                    else:
                        for k in 关联技能:
                            if 冷却类型 == 0:
                                self.技能栏[self.技能序号[k]].CDR *= 加成倍率
                            if 冷却类型 == 1:
                                self.技能栏[self.技能序号[k]].CDR_O *= 加成倍率
                if 非关联技能 != ["无"]:
                    if 非关联技能 == ["所有"]:
                        for j in self.技能栏:
                            if j.是否有伤害 == 1:
                                if 冷却类型 == 0:
                                    j.CDR /= 加成倍率
                                if 冷却类型 == 1:
                                    j.CDR_O /= 加成倍率
                    else:
                        for k in 非关联技能:
                            if 冷却类型 == 0:
                                self.技能栏[self.技能序号[k]].CDR /= 加成倍率
                            if 冷却类型 == 1:
                                self.技能栏[self.技能序号[k]].CDR_O /= 加成倍率

    def __属性倍率计算(self):
        # 火、冰、光、暗
        self.属性倍率组 = []
        self.属性倍率组.append(1.05 + 0.0045 * int(self.__火属性强化 - self.火抗输入))
        self.属性倍率组.append(1.05 + 0.0045 * int(self.__冰属性强化 - self.冰抗输入))
        self.属性倍率组.append(1.05 + 0.0045 * int(self.__光属性强化 - self.光抗输入))
        self.属性倍率组.append(1.05 + 0.0045 * int(self.__暗属性强化 - self.暗抗输入))
        self.属性倍率 = max(self.属性倍率组)

    def __面板系数计算(self, mode=1):
        if self.类型  is None or self.类型 == "":
            self.类型 = self.输出类型选项[0]
        # 基础面板 不含百分比力智和百分比三攻
        if mode == 0:
            if self.类型 == "物理百分比":
                return int((self.基础面板力量() / 250 + 1) * self.基础面板物理攻击力())
            elif self.类型 == "魔法百分比":
                return int((self.基础面板智力() / 250 + 1) * self.基础面板魔法攻击力())
            elif self.类型 == "物理固伤":
                return int((self.基础面板力量() / 250 + 1) * self.基础面板独立攻击力())
            elif self.类型 == "魔法固伤":
                return int((self.基础面板智力() / 250 + 1) * self.基础面板独立攻击力())
        # 旧版算法 不含斗神、宠物技能等
        else:
            if self.类型 == "物理百分比":
                return int(
                    (self.面板力量() / 250 + 1)
                    * self.基础面板物理攻击力()
                    * (1 + self.__百分比三攻)
                )
            elif self.类型 == "魔法百分比":
                return int(
                    (self.面板智力() / 250 + 1)
                    * self.基础面板魔法攻击力()
                    * (1 + self.__百分比三攻)
                )
            elif self.类型 == "物理固伤":
                return int(
                    (self.面板力量() / 250 + 1)
                    * self.基础面板独立攻击力()
                    * (1 + self.__百分比三攻)
                )
            elif self.类型 == "魔法固伤":
                return int(
                    (self.面板智力() / 250 + 1)
                    * self.基础面板独立攻击力()
                    * (1 + self.__百分比三攻)
                )

    def 伤害指数计算(self):
        防御 = max(self.防御输入 * self.防御系数 - self.__固定减防, 0) * (
            1 - self.__百分比减防
        )

        # 固定攻击方100级
        基准倍率 = 1.5 * self.buff * (1 - 防御 / (防御 + 200 * 100))

        self.__属性倍率计算()

        # 基础面板 不含百分比力智和百分比三攻
        基础面板 = self.__面板系数计算(mode=0)
        旧版面板 = self.__面板系数计算(mode=1)

        # 攻击强化显示改版
        新 = self.__攻击强化 * (1 + self.__百分比攻击强化) * 0.01
        # 攻击强化显示改版

        旧 = (
            1 + int((self.__伤害增加 + 0.00000001) * 100) / 100
        )  # 避免出现浮点数取整BUG
        旧 *= 1 + self.__暴击伤害
        旧 *= 1 + self.__最终伤害
        旧 *= 1 + self.__持续伤害
        旧 *= 1 + self.__附加伤害 + self.__属性附加 * self.属性倍率

        self.伤害指数 = (
            (新 * 基础面板 + 旧 * 旧版面板)
            * self.技能攻击力
            * self.属性倍率
            * 基准倍率
            * self.斗神宠物
            * (
                1.25
                if "破招攻击" in get_global_data("attack_type", self.equVersion)
                else 1.0
            )
        )

        # 7.8日,伤害数据压缩
        self.伤害指数 /= 1000

    def 基础属性修正(self, info):
        from core.util.toNum import str_to_num

        self.攻击强化加成(str_to_num(info.get("攻击强化", 0)))
        self.buff量加成(str_to_num(info.get("BUFF量", 0)))
        self.百分比攻击强化加成(str_to_num(info.get("攻击强化百分比", 0)) / 100)
        self.__百分比buff量 += str_to_num(info.get("BUFF量百分比", 0)) / 100
        if self.类型 == "辅助":
            self.基础属性加成(四维=str_to_num(info.get("四维", 0)))
        else:
            self.基础属性加成(
                进图力量=str_to_num(info.get("四维", 0)),
                进图智力=str_to_num(info.get("四维", 0)),
                体精=str_to_num(info.get("四维", 0)),
                三攻=str_to_num(info.get("三攻", 0)),
            )
        self.技能攻击力加成(str_to_num(info.get("技攻", 0)) / 100)
        self.基础属性加成(
            火属性抗性=str_to_num(info.get("火抗", 0)),
            光属性抗性=str_to_num(info.get("光抗", 0)),
            冰属性抗性=str_to_num(info.get("冰抗", 0)),
            暗属性抗性=str_to_num(info.get("暗抗", 0)),
        )
        self.攻击速度增加(str_to_num(info.get("攻速", 0)) / 100)
        self.火属性强化加成(str_to_num(info.get("火强", 0)))
        self.光属性强化加成(str_to_num(info.get("光强", 0)))
        self.冰属性强化加成(str_to_num(info.get("冰强", 0)))
        self.暗属性强化加成(str_to_num(info.get("暗强", 0)))
        for 抗性 in [
            "出血",
            "中毒",
            "灼伤",
            "感电",
            "冰冻",
            "减速",
            "眩晕",
            "诅咒",
            "失明",
            "石化",
            "睡眠",
            "混乱",
            "束缚",
        ]:
            self.异常抗性加成(抗性, str_to_num(info.get(抗性 + "抗性", 0)) / 100)
        self.MP消耗量加成(str_to_num(info.get("MP消耗量", 0)) / 100)
        self.set_eq_params(
            "skill_range",
            self.get_eq_params("skill_range")
            + str_to_num(info.get("技能范围Σ", 0)) / 100,
        )

    # endregion

    def get_individuation(self, index):
        if index >= len(self.individuation):
            return 0
        else:
            return 0 if self.individuation[index]  is None else self.individuation[index]

    def calc_init(self, info, equipList: List[int] = []):
        # 获取打造数据
        self.__打造设置(info.get("forge_set", {}))

        self.asrahan = info.get("asrahan", {})
        # 设置职业信息
        self.__set_char(info)

        self.__怪物信息设置(info.get("monster", 2))

        self.__场景设置(info.get("scene", 1))

        # 自定义词条部分
        self.自定义词条 = info.get("customize", {})
        #  时装设置
        self.__穿戴装扮(info.get("dress_set", {}))
        # 获取装备列表
        self.__穿戴装备(list(map(int, equipList)))

        # 获取技能数据
        self.__skill_set(info.get("skill_set", {}))
        # 获取装备选项数据
        self.trigger_set = info.get("trigger_set", {})
        self.__equ_chose_set(self.trigger_set)
        # 药剂设置
        self.__药剂设置(info.get("consumable_list", []))

        self.hotkey_set(info.get("hotkey_set", []))

        self.融合列表 = list(map(int, info.get("fusion_list", [])))

        self.武器融合 = info.get("merge", {})

        self.特性列表 = [int(i) for i in list(info.get("specificity", {}).keys())]

        self.特性等级 = info.get("specificity", {})

        self.融合石等级 = info.get("stone_set", {})

        self.技能队列设置(info.get("skill_que", []))

        self.individuation = info.get("individuation", [])
        self.基础属性修正(
            info.get(
                "corrections",
                {
                    "BUFF量": 0,
                    "BUFF量百分比": 0,
                    "三攻": 0,
                    "光强": 0,
                    "光抗": 0,
                    "冰强": 0,
                    "冰抗": 0,
                    "力智": 0,
                    "四维": 0,
                    "技攻": 0,
                    "攻击强化": 0,
                    "攻击强化百分比": 0,
                    "攻速": 0,
                    "暗强": 0,
                    "暗抗": 0,
                    "火强": 0,
                    "火抗": 0,
                },
            )
        )

    def jade_upgrade(self):
        temp = []
        from core.equipment.jade import get_jade_setinfo, get_jadefunc_by_id

        num_range = [26001, 26020]
        if self.类型 == "辅助":
            num_range = [26011, 26206]
        for jade in get_jade_setinfo():
            if jade["id"] > num_range[0] and jade["id"] <= num_range[1]:
                char = deepcopy(self)
                func = get_jadefunc_by_id(jade["id"])
                func(char, value=jade["max"])
                char.__计算前预处理()
                temp.append(
                    {
                        "id": jade["id"],
                        "name": jade["props"]
                        + "  "
                        + ("" if jade["max"] == 1 else ("+" + str(jade["max"])))
                        + jade["unit"],
                        "damage": round(char.结果计算()["total_data"], 2),
                        "order": jade["order"],
                    }
                )
        return temp

    def 异常保有率计算(self, pa, cur):
        if cur == "灼伤破冰":
            冰冻CD = min(
                self.异常时间["冰冻"][3], get_global_data("bd_cd", self.equVersion)
            )
            # 不带鞋子，内置3秒结算CD
            if not self.check_equ_by_name("信守誓约的步伐"):
                冰冻CD = max(3, 冰冻CD)
            # 破韧后，原本的CD是多少就是多少
            if get_global_data("control_state", self.equVersion):
                冰冻CD = min(
                    self.异常时间["冰冻"][3],
                    冰冻CD,
                    get_global_data("bd_cd", self.equVersion),
                )
            灼伤 = self.异常时间["灼伤"]
            return max(1 - (2 * 冰冻CD + 1) / (4 * (灼伤[0] * 灼伤[2] + 灼伤[1])), 0)
        else:
            if self.get_eq_params(f"{cur}-结算") == 0:
                return 0
            持续时间 = (
                self.异常时间[cur][0] * self.异常时间[cur][2] + self.异常时间[cur][1]
            )
            异常CD = min(
                self.异常时间[cur][3],
                get_global_data(pa.split("_")[0] + "_cd", self.equVersion, 99),
            )
            if self.check_equ_by_name("承诺誓约的腰带"):
                异常CD = max(0.5, 异常CD)
            return max(1 - (2 * 异常CD + 1) / (4 * 持续时间), 0)

    def calc(
        self,
        setName: str = "set",
        equipList: List[int] = [],
        withJade=False,
        withSet=False,
        info=None,
    ):
        self.calc_init(info, equipList)
        jade = []
        # cus = []
        # merge = []
        if withJade:
            jade = self.jade_upgrade()
        # if withCus and self.类型 != '辅助':
        #     cus = self.cus_upgrade(CusPosition)
        # if withMerge and self.类型 != '辅助':
        #     merge = self.merge_upgrade()
        self.__计算前预处理()
        temp = self.结果计算()
        calc_info = {}

        if self.类型 == "辅助":
            calc_info[self.适用属性] = self.站街系数()
        elif self.类型 == "物理百分比":
            calc_info["力量"] = self.基础面板力量()
            calc_info["物理攻击"] = self.站街物理攻击力()
        elif self.类型 == "魔法百分比":
            calc_info["智力"] = self.基础面板智力()
            calc_info["魔法攻击"] = self.站街魔法攻击力()
        elif self.类型 == "物理固伤":
            calc_info["力量"] = self.基础面板力量()
            calc_info["独立攻击"] = self.站街独立攻击力()
        elif self.类型 == "魔法固伤":
            calc_info["智力"] = self.基础面板智力()
            calc_info["独立攻击"] = self.站街独立攻击力()
        # print(suitInfo)
        calc_info["火"] = int(self.火属性强化())
        calc_info["冰"] = int(self.冰属性强化())
        calc_info["光"] = int(self.光属性强化())
        calc_info["暗"] = int(self.暗属性强化())
        calc_info["火抗"] = self.火属性抗性()
        calc_info["冰抗"] = self.冰属性抗性()
        calc_info["光抗"] = self.光属性抗性()
        calc_info["暗抗"] = self.暗属性抗性()

        for i in self.技能栏:
            倍率 = i.独立攻击力倍率(self.武器类型)
            if i.名称 not in self.skills_passive:
                continue
            if 倍率 != 1:
                self.skills_passive[i.名称]["info"].append(
                    {
                        "type": "独立攻击力",
                        "info": [round((倍率 - 1) * 100), "所有", ""],
                    }
                )
            倍率 = i.魔法攻击力倍率(self.武器类型)
            if 倍率 != 1:
                self.skills_passive[i.名称]["info"].append(
                    {
                        "type": "魔法攻击力",
                        "info": [round((倍率 - 1) * 100), "所有", ""],
                    }
                )
            倍率 = i.物理攻击力倍率(self.武器类型)
            if 倍率 != 1:
                self.skills_passive[i.名称]["info"].append(
                    {
                        "type": "物理攻击力",
                        "info": [round((倍率 - 1) * 100), "所有", ""],
                    }
                )
            倍率 = i.独立攻击力倍率进图(self.武器类型)
            if i.名称 not in self.skills_passive:
                continue
            if 倍率 != 1:
                self.skills_passive[i.名称]["info"].append(
                    {
                        "type": "独立攻击力[进图]",
                        "info": [round((倍率 - 1) * 100), "所有", ""],
                    }
                )
            倍率 = i.魔法攻击力倍率进图(self.武器类型)
            if 倍率 != 1:
                self.skills_passive[i.名称]["info"].append(
                    {
                        "type": "魔法攻击力[进图]",
                        "info": [round((倍率 - 1) * 100), "所有", ""],
                    }
                )
            倍率 = i.物理攻击力倍率进图(self.武器类型)
            if 倍率 != 1:
                self.skills_passive[i.名称]["info"].append(
                    {
                        "type": "物理攻击力[进图]",
                        "info": [round((倍率 - 1) * 100), "所有", ""],
                    }
                )
        buff = self.get_skill_by_name("BUFF")
        awake = self.get_skill_by_name("一次觉醒")

        skills_passive = {}
        for i in self.skills_passive.keys():
            if len(self.skills_passive[i].get("info", [])) > 0:
                skills_passive[i] = self.skills_passive[i]

        result = {
            "id": uuid1().hex,
            "alter": self.实际名称,
            "name": self.名称,
            "role": "buffer" if self.类型 == "辅助" else "delear",
            "equips_forge": self.打造,
            "suits": self.suitInfo,
            "info": {
                # 站街
                "站街": calc_info,
                # 词条
                "properties": {
                    # 攻击强化
                    "攻击强化": round(self.__攻击强化, 0),
                    "buffer_power": round(self.BUFF量(), 0),
                    "buffer_power_value": round(self.__buff量, 0),
                    "buffer_power_per": round(self.__百分比buff量 * 100, 2),
                    "技能攻击力": round(100 * (self.技能攻击力 - 1), 2),
                    "面板技能攻击力": round(100 * (self.__面板技能攻击力 - 1), 2),
                    "百分比攻击强化": round(self.__百分比攻击强化 * 100, 1),
                    "MP消耗量": round(self.__MP消耗量 * 100 - 100, 2),
                    "伤害比例": [
                        self.伤害比例.get("直伤", 1),
                        self.伤害比例.get("中毒", 0),
                        self.伤害比例.get("灼伤", 0),
                        self.伤害比例.get("感电", 0),
                        self.伤害比例.get("出血", 0),
                    ],
                    "伤害系数": [
                        self.伤害系数.get("直伤", 1),
                        self.伤害系数.get("中毒", 1) - 1,
                        self.伤害系数.get("灼伤", 1) - 1,
                        self.伤害系数.get("感电", 1) - 1,
                        self.伤害系数.get("出血", 1) - 1,
                    ],
                    "技能范围": self.get_eq_params("skill_range"),
                    "技能范围∏": self.get_eq_params("skill_range_multi", 1),
                    "保护罩": self.get_eq_params("protect")
                    * (1 + self.get_eq_params("protect_max")),
                    # '无色消耗': temp['无色消耗'],
                    "apply_value": self.适用数值,
                    "buff_level": buff.等级,
                    "buff_name": buff.名称,
                    "awake_level": awake.等级,
                    "awake_name": awake.名称,
                    "buff_intstr_per": self.__buff百分比力智,
                    "buff_intstr": self.__buff固定力智,
                    "buff_attack_per": self.__buff百分比三攻,
                    "buff_attack": self.__buff固定三攻,
                    "awake_intstr_per": self.__觉醒百分比力智,
                    "awake_intstr": self.__觉醒固定力智,
                    "攻击速度": self.__攻击速度,
                    "其他攻击速度": self.__攻击速度_其他,
                    "施放速度": self.__施放速度,
                    "移动速度": self.__移动速度,
                    "cdr": temp.get("CDR", []),
                    "冷却缩减": self.冷却缩减 * (1 - self.__加算冷却缩减),
                    "冷却恢复": self.冷却恢复,
                    "defense": self.get_eq_params("defense"),
                    "defense_ratio": self.get_eq_params("defense_ratio"),
                    "hurted_ratio": self.get_eq_params("hurted_ratio"),
                    "era": round(
                        (
                            1
                            - (
                                1
                                - self.get_eq_params("defense")
                                * (1 + self.get_eq_params("defense_ratio"))
                                / (
                                    100000
                                    + self.get_eq_params("defense")
                                    * (1 + self.get_eq_params("defense_ratio"))
                                )
                            )
                            * (1 - self.get_eq_params("hurted_ratio"))
                        )
                        * 100,
                        2,
                    ),
                },
            },
            "total_data": temp["buffer_addition"]
            if "buffer_addition" in temp
            else [temp["total_data"], 0, 0, 0],
            "skills": temp["skills"],
            "skills_passive": skills_passive,
            "specificity": info.get("specificity", []),
            "jade": sorted(jade, key=lambda x: x["order"]),
            "talisman_set":info.get("talisman_set", []),
            "rune_set":info.get("rune_set", []),
            # "cus": cus,
            "tip_part": self.tip_part,
        }

        if withSet:
            result["forge_set"] = info["forge_set"]
            result["equips"] = list(
                map(lambda x: get_equ(self.equVersion).get_json(x), self.装备栏)
            )
            result["merge_list"] = self.武器融合
            result["fusion_list"] = self.融合列表
            result["customize"] = info["customize"]

        for 抗性 in [
            "出血",
            "中毒",
            "灼伤",
            "感电",
            "冰冻",
            "减速",
            "眩晕",
            "诅咒",
            "失明",
            "石化",
            "睡眠",
            "混乱",
            "束缚",
        ]:
            result["info"]["properties"][抗性 + "抗性"] = self.异常抗性获取(抗性) * 100
        return result


def createCharacter(alter: str, equVersion: str = "0"):
    character: Character = None
    module_name = "core.characters." + alter
    try:
        character = importlib.import_module(module_name).classChange(equVersion)
    except Exception as ex:
        print(ex)
        print("create character " + module_name + " error.")
        pass
    return character
