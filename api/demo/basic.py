from typing import List

class entry:

  id  = 0

  char = None
  params = []
  tips = []

  def __init__(self,char,params=[]) -> None:
    self.char = char
    self.params = params
    self.tips=[]

  def 攻击强化(self,list=[]):
    return 0

  def 火属性强化(self,list=[]):
    return 0

  def 火属性抗性(self,list=[]):
    return 0

  def 暗属性强化(self,list=[]):
    return 0

  def 暗属性抗性(self,list=[]):
    return 0

  def 光属性强化(self,list=[]):
    return 0

  def 光属性抗性(self,list=[]):
    return 0

  def 冰属性强化(self,list=[]):
    return 0

  def 冰属性抗性(self,list=[]):
    return 0

  def 攻击速度(self,list=[]):
    return 0

  def 技能攻击力(self,list=[]):
    return 0


class Character:

  entry_list:List[entry] = []

  def 攻击强化(self,list=[]):
    res = 0
    for entry in self.entry_list:
      res += entry.攻击强化(list)
    return res

  def 火属性强化(self,list=[]):
    res = 0
    for entry in self.entry_list:
      res += entry.火属性强化(list)
    return res

  def 火属性抗性(self,list=[]):
    res = 0
    for entry in self.entry_list:
      res += entry.火属性抗性(list)
    return res

  def 攻击速度(self,list=[]):
    res = 0
    for entry in self.entry_list:
      res += entry.攻击速度(list)
    return res

  def 技能攻击力(self,list=[]):
    res = 0
    for entry in self.entry_list:
      res += entry.技能攻击力(list)
    return res