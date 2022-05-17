class Clothes:
  def __init__(self, H):
    self.H = H
    
class Costume(Clothes):
  @property
  def calc(self):
    return 2*self.H + 0.3


class Coat(Clothes):
  @property
  def calc(self):
    return self.H/6.5 + 0.5
    

b = Costume(2)
a = Coat(43)
print(a.calc)
print(b.calc)
