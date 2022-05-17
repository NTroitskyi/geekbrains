class Cell:
  def __init__(self, n):
    self.n = n
  def __str__(self):
    return f'{self.n}'
  def __add__(self, other):
    print(self.n)
    print(other.n)
    return Cell(self.n + other.n)

  def __sub__(self, other):
    if self.n - other.n <= 0:
      raise ValueError('Количество ячеек первой клетки должно быть больше количества второй. ')
    else:
      return Cell(self.n - other.n)

  def __mul__(self, other):
    return Cell(self.n * other.n)

  def __floordiv__(self, other):
    return Cell(self.n // other.n)

  def __truediv__(self, other):
    return Cell(self.n / other.n)

  def make_order(self, k):
    strg = ''
    for a in range(self.n//k):
      strg += '*'*k+'\n'
    strg += '*'*(self.n % k)
    return strg

a = Cell(5)
b = Cell(7)
c = Cell(23)
print(a+b)
#print(a-b) тут исключение
print(a*b)
print(a/b)
print(a//b)

print(c.make_order(4))