from core.basic.equipment import Equipments
equ = Equipments("0")

equ.init_oath_suits()
item = equ.oath_suits[3]
for i in range(1, 7):
  print(f"Lv{i}：")
  print(equ.oath_suits[i])
  for skill in equ.oath_suits[i]['skills']:
    print(skill.__dict__)
  print("------------------")