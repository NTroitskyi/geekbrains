def correct_name_string(lst):
  return str(element_splitted[-1][0].upper()) + str(element_splitted[-1][1:].lower())
  

lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for el in lst:
  element_splitted = el.split()
  print('Привет,', correct_name_string(element_splitted))