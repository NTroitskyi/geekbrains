class OnlyNumsInList(Exception):
  def __init__(self, msg):
    self.msg = msg


lst = []
while True:
  try:
    a = input('Введите элемент списка: ')
    
    if type(int(a)) != int:
      raise OnlyNumsInList('Это не число. ')
    
  except ValueError as ve:
    if a.lower() == 'stop':
      print('Остановлено. ')
      break
    print(ve)
  except OnlyNumsInList as onil:
    print(onil)
  else:
    lst.append(int(a))

print(lst)