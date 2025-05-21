import json

with open('./1.json', encoding='utf-8') as f:
  data = json.load(f)

  result = []

  for i in data:
    Job = i.get("Job", "")
    Grow = i.get("Grow", "")
    temp =  list(filter(lambda x:x["Job"] == Job and x["Grow"] == Grow, result))
    if len(temp) == 0:
      result.append({
        "Job": Job,
        "Grow": Grow,
        "UP": [],
        "VP": []
      })

  for temp in result:
    infos = list(filter(lambda x:x["Job"] == temp["Job"] and x["Grow"] == temp["Grow"], data))
    UP = []
    VP = []
    for i in infos:
      if i["Type"] == "Up" or i["Type"] == "VP":
        UP.append({
          "Skill_Code": i.get("Skill_Code", ""),
          "SP_Lv": i.get("SP_Lv", ""),
          "SP_Name": i.get("SP_Name", "")
        })
      if i["Type"] == "VP":
        VP.append({
          "Skill_Code": i.get("Skill_Code", ""),
          "SP_Lv": i.get("SP_Lv", ""),
          "SP_Name": i.get("SP_Name", ""),
          "vp": [
              {"name": i.get("VP1_name", ""),
              "basic": i.get("VP1_basic", "").replace("\\n", "<br/>"),
              "explain": i.get("VP1_explain", "").replace("\\n", "<br/>"),
              # "special":i.get("VP1_special", "").replace("\\n", "<br/>")
              },
             {"name": i.get("VP2_name", ""),
              "basic": i.get("VP2_basic", "").replace("\\n", "<br/>"),
              "explain": i.get("VP2_explain", "").replace("\\n", "<br/>"),
              # "special":i.get("VP2_special", "").replace("\\n", "<br/>")
            }
          ]
        })
    temp["UP"] = UP
    temp["VP"] = VP

  with open('./1_out.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)