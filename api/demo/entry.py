def pre_recurrence(func):
  def inner(*args,**kwargs):
    if args[0].id in args[1]:
      return 0
    else:
      args[1].append(args[0].id)
    return func(*args,**kwargs)
  return inner


from basic import entry

class entry_0(entry):

  id = 0

  @pre_recurrence
  def 攻击强化(self,list=[]):
    if self.char.攻击速度(list) > 1:
      return 1000
    else:
      self.tips.append("攻速不足")
      return 500

  @pre_recurrence
  def 火属性抗性(self, list=[]):
    if self.char.火属性强化(list) > 10:
      return 10
    else:
      self.tips.append("火强不足")
      return 5

  @pre_recurrence
  def 火属性强化(self, list=[]):
    if self.char.火属性抗性(list) > 10:
      return 10
    else:
      self.tips.append("火抗不足")
      return 5

class entry_1(entry):

  id = 1

  @pre_recurrence
  def 攻击强化(self,list=[]):
    return 2

  @pre_recurrence
  def 攻击速度(self,list=[]):
      return 1

