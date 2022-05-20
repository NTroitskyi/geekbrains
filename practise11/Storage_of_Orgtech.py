from pprint import pprint
class OrgTech:
  
  def __init__(self, brand, quantity):
    if type(quantity) != int:
      raise ValueError('Количество должно быть целым числом. ')
    self.brand = brand
    self.quantity = quantity

    

    

class Printer(OrgTech):
  def __init__(self, brand, quantity, gamma):
    OrgTech.__init__(self, brand, quantity)
    if gamma != 'Black&White' and gamma != 'Coloured':
      raise ValueError("Gamma: 'Black&White' или 'Coloured'")
    self.gamma = gamma
  
  def store(self, a, aim): 
    if a.__class__.__name__ in aim:
      if self.brand in aim[a.__class__.__name__]:
        if self.gamma in aim[a.__class__.__name__][self.brand]:
          aim[a.__class__.__name__][self.brand][self.gamma] += self.quantity
        else:
          aim[a.__class__.__name__][self.brand][self.gamma] = self.quantity
      else:
        aim[a.__class__.__name__][self.brand] = {self.gamma: self.quantity}
    else:
      aim[a.__class__.__name__] = {self.brand: {self.gamma: self.quantity}}
    return aim


class Scanner(OrgTech):
  def store(self, a, aim):
    if a.__class__.__name__ in aim:
      if self.brand in aim[a.__class__.__name__]:
          aim[a.__class__.__name__][self.brand] += self.quantity
      else:
        aim[a.__class__.__name__][self.brand] = self.quantity
    else:
      aim[a.__class__.__name__] = {self.brand: self.quantity}
    return aim
  


      
class Laptop(OrgTech):
  def __init__(self, brand, quantity, processor):
    OrgTech.__init__(self, brand, quantity)
    self.processor = processor

  
  def store(self, a, aim): #repeated myself, I know
    if a.__class__.__name__ in aim:
      if self.brand in aim[a.__class__.__name__]:
        if self.processor in aim[a.__class__.__name__][self.brand]:
          aim[a.__class__.__name__][self.brand][self.processor] += self.quantity
        else:
          aim[a.__class__.__name__][self.brand][self.processor] = self.quantity
      else:
        aim[a.__class__.__name__][self.brand] = {self.processor: self.quantity}
    else:
      aim[a.__class__.__name__] = {self.brand: {self.processor: self.quantity}}
    return aim
      


a = Printer('Canon', 6, 'Black&White')
b = Laptop('Asus', 3, 'AMD')
c = Scanner('Canon', 6)
d = Laptop('Asus', 4, 'Intel')
e = Printer('Canon', 3, 'Coloured')

storage = {}


storage = a.store(a, storage)
storage = b.store(b, storage)
storage = c.store(c, storage)
storage = d.store(d, storage)
storage = e.store(e, storage)

pprint(storage)