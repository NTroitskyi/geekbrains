def type_logger(func):
  def inlog(*arg):
    for i in arg:
      print(f'{i}: {type(i)}', end = ', ') 
  return inlog


@type_logger
def calc_cube(x):
  return x**3


a = calc_cube(2)