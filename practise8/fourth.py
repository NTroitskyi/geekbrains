def val_checker(cond):
  def func(func):
    def extra(arg):
      if cond(arg) == True:
        print(func(arg))
      else:
        raise ValueError(f'Wrong val {arg}')
    return extra
  return func


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

a = calc_cube(5)