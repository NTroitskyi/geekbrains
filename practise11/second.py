class ZeroEx(Exception):
  def __init__(self, msg):
    self.msg = msg

try:
  a = int(input('Введите число: '))
  if a == 0:
    raise ZeroEx('Деление на ноль невозможно.')
  else:
    print(10/a)
except TypeError:
  print('Это не число.')
except ZeroEx as ze:
  print(ze)