from database.connect import get_db_engine as get_engine
from database.models import Session, EquData, SuitData

engine = get_engine('0')

with Session(engine) as session:
  db_list = session.query(EquData).all()

res = ''

curPart = ''

# for i in db_list:
#   if i.itemType == '武器' and i.itemType != curPart:
#     curPart = i.itemType
#     res += f'''
# # endregion
# # region {curPart}
#     '''
#   if i.itemType != '武器' and i.categorize != curPart:
#     curPart = i.categorize
#     res += f'''
# # endregion
# # region {curPart}
#     '''
#   res += f'''
# def equ_{i.id}(char: Character):
#   \'''
# {i.name}
# {i.rarity} {i.itemType} {i.itemDetailType}

# {i.detail}
#   \'''
#   pass
#   '''

for i in db_list:
  if i.id <= 1000:
    continue
  if i.itemType != '武器' and i.categorize != curPart:
    curPart = i.categorize
    res += f'''
# endregion
# region {curPart}
    '''
  res += f'''
def equ_{i.id}(char: Character):
  \'''
{i.name}
{i.rarity} {i.itemType} {i.itemDetailType}

{i.detail}
  \'''
  pass
  '''

  with open('/Users/imelon/Desktop/Code/dnf/dcalc/backend/output.py', 'w') as file:
    file.write(res)
