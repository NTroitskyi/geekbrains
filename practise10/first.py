class Matrix:
  def __init__(self, row):
    self.rows = row
  def __str__(self):
    def plus(lst):
      res = ''
      for i in range(len(lst)):
        res += f'{lst[i]}\n'
      return res
    return plus(self.rows)

  def __add__(self, other):
    if (len(self.rows) != len(other.rows)) or (len(self.rows[0]) != len(other.rows[0])):
      raise ValueError('Размерности не совпадают')
    def new_m(a, b):
      matrix = []
      for i in range(len(a)):
        lst = []
        for n in range(len(a[i])):
          lst.append(a[i][n] + b[i][n])
        matrix.append(lst)  
      return matrix  
    return Matrix(new_m(self.rows, other.rows))
    
a = Matrix([[1, 2], [3, 4]])
b = Matrix([[3, 5], [6, 2]])

c = Matrix([[33, 32], [37, 43], [51, 86]])
d = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])

print(a+b)
print(c+d)