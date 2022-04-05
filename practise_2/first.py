
def typ(*args):
  a = 1
  for operation in args:
    print('Тип результата выражения №',a, ':', type(operation))
    a += 1




typ(15 * 3, 15 / 3, 15 // 2, 15**2)
