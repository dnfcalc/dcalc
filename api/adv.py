import json
import os

res = [
  {
    "name": "swordman_male",
    "title": "鬼剑士(男)",
    "children": [
      {
        "title": "极诣·剑魂",
        "name": "weapon_master",
        "open": True
      },
      {
        "name": "soul_bender",
        "title": "极诣·鬼泣",
        "open": True
      },
      {
        "name": "berserker",
        "title": "极诣·狂战士",
        "open": True
      },
      {
        "name": "asura",
        "title": "极诣·阿修罗",
        "open": True
      },
      {
        "name": "ghostblade",
        "title": "极诣·剑影",
        "open": True
      }
    ]
  },
  {
    "name": "swordman_female",
    "title": "鬼剑士(女)",
    "children": [
      {
        "name": "sword_master",
        "title": "极诣·驭剑士",
        "open": True
      },
      {
        "name": "dark_templar",
        "title": "极诣·暗殿骑士",
        "open": True
      },
      {
        "name": "demon_slayer",
        "title": "极诣·契魔者",
        "open": True
      },
      {
        "name": "vegabond",
        "title": "极诣·流浪武士",
        "open": True
      },
      {
        "name": "spectre",
        "title": "极诣·刃影",
        "open": True
      }
    ]
  },
  {
    "name": "fighter_male",
    "title": "格斗家(男)",
    "children": [
      {
        "name": "nenmaster_male",
        "title": "归元·气功师",
        "open": True
      },
      {
        "name": "striker_male",
        "title": "归元·散打",
        "open": True
      },
      {
        "name": "brawler_male",
        "title": "归元·街霸",
        "open": True
      },
      {
        "name": "grappler_male",
        "title": "归元·柔道家",
        "open": True
      },
      {
        "name": "empty",
        "title": "",
        "comment": "首页"
      }
    ]
  },
  {
    "name": "fighter_female",
    "title": "格斗家(女)",
    "children": [
      {
        "name": "nenmaster_female",
        "title": "归元·气功师",
        "open": True
      },
      {
        "name": "striker_female",
        "title": "归元·散打",
        "open": True
      },
      {
        "name": "brawler_female",
        "title": "归元·街霸",
        "open": True
      },
      {
        "name": "grappler_female",
        "title": "归元·柔道家",
        "open": True
    },
      {
        "name": "empty",
        "title": "",
        "comment": "设置"
      }
    ]
  },
  {
    "name": "gunner_male",
    "title": "神枪手(男)",
    "children": [
      {
        "name": "ranger_male",
        "title": "重霄·漫游枪手",
        "open": True

      },
      {
        "name": "launcher_male",
        "title": "重霄·枪炮师",
        "open": True
      },
      {
        "name": "mechanic_male",
        "title": "重霄·机械师",
        "open": True
      },
      {
        "name": "spitfire_male",
        "title": "重霄·弹药专家",
        "open": True
      },
      {
        "name": "assault",
        "title": "重霄·合金战士",
        "open": True
      }
    ]
  },
  {
    "name": "gunner_female",
    "title": "神枪手(女)",
    "children": [
      {
        "name": "ranger_female",
        "title": "重霄·漫游枪手",
        "open": True
      },
      {
        "name": "launcher_female",
        "title": "重霄·枪炮师",
        "open": True
      },
      {
        "name": "mechanic_female",
        "title": "重霄·机械师",
        "open": True

      },
      {
        "name": "spitfire_female",
        "title": "重霄·弹药专家",
        "open": True
      },
      {
        "name": "sponsor",
        "url": "https://bbs.colg.cn",
        "title": "",
        "open": True
      }
    ]
  },
  {
    "name": "mage_male",
    "title": "魔法师(男)",
    "children": [
      {
        "name": "elemental_bomber",
        "title": "知源·元素爆破师",
        "open": True
      },
      {
        "name": "glacial_master",
        "title": "知源·冰结师",
        "open": True
      },
      {
        "name": "blood_mage",
        "title": "知源·血法师",
        "open": True
      },
      {
        "name": "swift_master",
        "title": "知源·逐风者",
        "open": True
      },
      {
        "name": "dimension_walker",
        "title": "知源·次元行者",
        "open": True
      }
    ]
  },
  {
    "name": "mage_female",
    "title": "魔法师(女)",
    "children": [
      {
        "name": "elementalist",
        "title": "知源·元素师",
        "open": True
      },
      {
        "name": "summoner",
        "title": "知源·召唤师",
        "open": True
      },
      {
        "name": "battle_mage",
        "title": "知源·战斗法师",
        "open": True
      },
      {
        "name": "witch",
        "title": "知源·魔道学者",
        "open": True
      },
      {
        "name": "enchantress",
        "title": "知源·小魔女",
        "open": True,
        "options": [
        { "name": "default", "title": "奶", "class": "enchantress" },
        { "name": "default", "title": "输出", "class": "enchantress_carry" }
      ]
      }
    ]
  },
  {
    "name": "priest_male",
    "title": "圣职者(男)",
    "children": [
      {
        "name": "crusader_male",
        "title": "神启·圣骑士",
        "open": True,
        "options": [
          {
            "name": "default",
            "title": "奶",
            "class": "crusader_male"
          },
          {
            "name": "default",
            "title": "审判",
            "class": "crusader_male_carry"
          }
        ]
      },
      {
        "name": "infighter",
        "title": "神启·蓝拳圣使",
        "open": True
      },
      {
        "name": "exorcist",
        "title": "神启·驱魔师",
        "open": True
      },
      {
        "name": "avenger",
        "title": "神启·复仇者",
        "open": True
      },
      {
        "name": "empty",
        "title": ""
      }
    ]
  },
  {
    "name": "priest_female",
    "title": "圣职者(女)",
    "children": [
      {
        "name": "crusader_female",
        "title": "神启·圣骑士",
        "open": True,
        "options": [
          {
            "name": "default",
            "title": "奶",
            "class": "crusader_female"
          },
          {
            "name": "default",
            "title": "输出",
            "class": "crusader_female_carry"
          }
        ]
      },
      {
        "name": "inquistor",
        "title": "神启·异端审判者",
        "open": True
      },
      {
        "name": "sorceress",
        "title": "神启·巫女",
        "open": True
      },
      {
        "name": "mistress",
        "title": "神启·诱魔者",
        "open": True
      },
      {
        "name": "empty",
        "title": ""
      }
    ]
  },
  {
    "name": "thief",
    "title": "暗夜使者",
    "children": [
      {
        "name": "rogue",
        "title": "隐夜·刺客",
        "open": True
      },
      {
        "name": "necro",
        "title": "隐夜·死灵术士",
        "open": True
      },
      {
        "name": "kunoichi",
        "title": "隐夜·忍者",
        "open": True
      },
      {
        "name": "shadow_dancer",
        "title": "隐夜·影舞者",
        "open": True
      },
      {
        "name": "empty",
        "title": ""
      }
    ]
  },
  {
    "name": "knight",
    "title": "守护者",
    "children": [
      {
        "name": "elven_knight",
        "title": "皓曦·精灵骑士",
        "open": True
      },
      {
        "name": "chaos",
        "title": "皓曦·混沌魔灵",
        "open": True
      },
      {
        "name": "paladin",
        "title": "皓曦·帕拉丁",
        "open": True
      },
      {
        "name": "dragon_knight",
        "title": "皓曦·龙骑士",
        "open": True
      },
      {
        "name": "empty",
        "title": ""
      }
    ]
  },
  {
    "name": "demonic_lancer",
    "title": "魔枪士",
    "children": [
      {
        "name": "vanguard",
        "title": "千魂·征战者",
        "open": True
      },
      {
        "name": "skirmisher",
        "title": "千魂·决战者",
        "open": True
      },
      {
        "name": "dragoon",
        "title": "千魂·狩猎者",
        "open": True
      },
      {
        "name": "impaler",
        "title": "千魂·暗枪士",
        "open": True
      },
      {
        "name": "empty",
        "title": ""
      }
    ]
  },
  {
    "name": "gunblader",
    "title": "枪剑士",
    "children": [
      {
        "name": "hitman",
        "title": "苍暮·暗刃",
        "open": True
      },
      {
        "name": "agent",
        "title": "苍暮·特工",
        "open": True
      },
      {
        "name": "trouble_shooter",
        "title": "苍暮·战线佣兵",
        "open": True
      },
      {
        "name": "specialist",
        "title": "苍暮·源能专家",
        "open": True
      },
      {
        "name": "empty",
        "title": ""
      }
    ]
  },
  {
    "name": "archer",
    "title": "弓箭手",
    "children": [
      {
        "name": "muse",
        "title": "聆风·缪斯",
        "open": True
      },
      {
        "name": "traveler",
        "title": "聆风·旅人",
        "open": True
      },
      { "name": "hunter", "title": "聆风·猎人", "open": True },
      { "name": "vigilante", "title": "聆风·妖护使", "open": True },
      { "name": "empty", "title": "" }
    ]
  },
  {
    "name": "extra",
    "title": "外传",
    "children": [
      {
        "name": "creator",
        "title": "知源·缔造者",
        "open": True
      },
      {
        "name": "dark_knight",
        "title": "极诣·黑暗武士",
        "open": True
      },
      {
        "name": "empty",
        "title": ""
      },
      {
        "name": "empty",
        "title": ""
      },
      {
        "name": "empty",
        "title": ""
      }
    ]
  }
]

cur = "../api/core/characters"

toAdd = []

for i in os.listdir(cur):
  if os.path.isdir(os.path.join(cur,i)):
    for j in os.listdir(os.path.join(cur,i)):
      if os.path.isdir(os.path.join(cur,i,j)) and not j.startswith("_"):
        for k in os.listdir(os.path.join(cur,i,j)):
            if not k.startswith("_"):
                toAdd.append(f'{i}.{j}.{k.replace(".py","")}')

for i in res:
   for j in i["children"]:
      items = list(filter(lambda x:j['name'] in x,toAdd))
      if len(items) > 0:
         for item in items:
            temp = j.get("options",[])
            if len(temp) == 0:
               temp.append({
                    "name": "default",
                    "title": "国服",
                    "class": j['name']
                })
            j['options'] = temp.append({
            "name": "default",
            "title": f"{'韩服' if item.startswith('HF') else '国服'}.{item.split('.')[1].split('_')[1]}",
            "class": item
          })
            j['options']= temp

with open("../api/dataFiles/adventure-info.json", "w", encoding="utf-8") as fp:
    json.dump(res, fp, ensure_ascii=False)