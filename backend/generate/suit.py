from database.connect import get_db_engine as get_engine
from database.models import Session, EquData, SuitData

engine = get_engine('0')

with Session(engine) as session:
  db_list = session.query(SuitData).all()

res = ''

curSuit = ''

for i in db_list:
  if i.suitId != curSuit:
    curSuit = i.suitId
    res += f'''
# endregion
# region {i.suitName}
    '''
  res += f'''
def suit_{i.id}(char: Character):
  \'''
  {i.value}
  \'''
  pass
  '''

  with open('/Users/imelon/Desktop/Code/dnf/dcalc/backend/output.py', 'w') as file:
    file.write(res)