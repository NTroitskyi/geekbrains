from math import sqrt
class Complex:
  def __init__(self, real, imagine):
    self.real = real
    self.imagine = imagine

  def __add__(self, other):
    return Complex(self.real+other.real, self.imagine+other.imagine)


  def __mul__(self, other):
    return Complex(self.real*other.real-self.imagine*other.imagine, self.real * other.imagine + self.imagine * other.real)

  def __str__(self):
    if self.imagine == 0:
        return f'{round(float(self.real), 2)}'
    if self.real == 0:
        return f'{round(float(self.imagine), 2)}i'
    if self.imagine < 0:
      return f'{round(float(self.real), 2)} - {round(float(-self.imagine), 2)}i'
    else:
      return f'{round(float(self.real), 2)} + {round(float(self.imagine), 2)}i'
    def mod(self):
      return sqrt(self.real*self.real+self.imagine*self.imagine)

  
a = Complex(2, -3)
b = Complex(1, -2)

print(a + b)