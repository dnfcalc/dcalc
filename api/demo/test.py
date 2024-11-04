from ref import ref,ref_computed,Ref
from signe import effect, computed

class Character:

    # region 属性强化 属性抗性

    fireRef:Ref[float]
    """火属性强化"""
    fireResistanceRef:Ref[float]
    """火属性抗性"""
    waterRef:Ref[float]
    """冰属性强化"""
    waterResistanceRef:Ref[float]
    """冰属性抗性"""
    lightRef:Ref[float]
    """光属性强化"""
    lightResistanceRef:Ref[float]
    """光属性抗性"""
    shadowRef:Ref[float]
    """暗属性强化"""
    shadowResistanceRef:Ref[float]
    """暗属性强化"""

    # endregion

    # region 基础属性

    strengthRef:Ref[float]
    '''力量'''
    intelligenceRef:Ref[float]
    '''智力'''
    vitalityRef:Ref[float]
    '''体力'''
    spiritRef:Ref[float]
    '''精神'''
    physicalAtkRef:Ref[float]
    '''物理攻击力'''
    magicalAtkRef:Ref[float]
    '''魔法攻击力'''
    independentAtkRef:Ref[float]
    '''独立攻击力'''

    # endregion

    # 速度

    movementSpeedRef:Ref[float]
    '''移动速度'''
    attackSpeedRef:Ref[float]
    '''攻击速度'''
    castingSpeedRef:Ref[float]
    '''施放速度'''

    # endregion

    def __init__(self):
        self.fireRef = ref(.0)
        self.waterRef = ref(.0)
        self.lightRef = ref(.0)
        self.shadowRef = ref(.0)
        self.fireResistanceRef = ref(.0)
        self.waterResistanceRef = ref(.0)
        self.lightResistanceRef = ref(.0)
        self.shadowResistanceRef = ref(.0)

    @property
    def fire(self):
       @computed
       def _():
          return self.fireRef.value + 2
       return _()


char = Character()

def entry_0(char:Character):
  char.fireRef.value = 19

def entry_1(char:Character):
   @effect
   def _():
    if char.fire < 20:
        char.waterRef.value  = 10
    else:
        char.waterRef.value  = 20

entry_1(char)
entry_0(char)

print("冰强"+str(char.waterRef.value))
print(char.fire)