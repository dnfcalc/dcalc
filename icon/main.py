import os
import requests
import json


with open('./icon/res.json', 'r') as file:
  data = json.load(file)

for item in data:
  if not os.path.exists(f"./icon/{item['dcalc']}"):
    os.makedirs(f"./icon/{item['dcalc']}")
  for i in range(0, 2333):
    url = f"https://image.avatar.dnf.qq.com/icon/{item['name']}/{i:05}.png"
    response = requests.get(url)
    if response.status_code == 200:
      if response.content:
        with open(
          f"./icon/{item['dcalc']}/{i:05}.png", "wb"
        ) as file:
          file.write(response.content)
    else:
      print(f"Failed to fetch {url}, status code: {response.status_code}")
      break

# for part in ['plate_belt', 'plate_coat', 'plate_pants', 'plate_neck', 'plate_shoes', 'magicstone', 'amalgamationstone', 'ring', 'ring_jp', 'harmor_belt', 'harmor_coat', 'harmor_pants', 'harmor_neck', 'harmor_shoes', 'larmor_belt', 'larmor_coat', 'larmor_pants', 'larmor_neck', 'larmor_shoes', 'flag', 'necklace', 'necklace_jp', 'bracelet_jp', 'bracelet_cn', 'bracelet', 'cloth_belt', 'cloth_coat', 'cloth_pants', 'cloth_neck', 'cloth_shoes', 'talismanicon', 'knuckle', 'bglove', 'claw', 'gauntlet', 'tonfa', 'ebow', 'sbow', 'lbow', 'cbow', 'club', 'sswd', 'katana', 'beamswd', 'lswd', 'rod', 'spear', 'broom', 'staff', 'pole', 'revolver', 'automatic', 'bowgun', 'musket', 'hcannon', 'pike', 'javelin', 'halberd', 'beamspear', 'shield', 'twinswd', 'dagger', 'chakraweapon', 'wand', 'scythe', 'cross', 'rosary', 'axe', 'totem', 'sblade', 'lblade', 'coreswd', 'mswd', 'earrring', 'support', 'leather_belt', 'leather_coat', 'leather_pants', 'leather_neck', 'leather_shoes']:
#   if os.path.exists(f"./images/equipment/new_equipment/{part}"):
#       pass
#   else:
#       os.makedirs(f"./images/equipment/new_equipment/{part}")

#   for i in range(0, 999):
#       url = f"https://image.avatar.dnf.qq.com/icon/{part}/{i:05}.png"
#       response = requests.get(url)
#       if response.status_code == 200:
#           if response.content:
#               with open(
#                   f"./images/equipment/new_equipment/{part}/{i:05}.png", "wb"
#               ) as file:
#                   file.write(response.content)
