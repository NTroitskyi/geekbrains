'''
#1 задание
duration = int(input())
rest = 0
time_mins = 0
time_hours = 0
time_days = 0

if duration > 60:
  time_mins = duration // 60
  if time_mins > 60:
    time_hours = time_mins // 60
    time_mins = time_mins % 60
    if time_hours > 24:
      time_days = time_hours // 24
      time_hours = time_hours % 24
  duration = duration % 60

if time_days != 0:
  print(str(time_days) + ' d', str(time_hours) + ' h', str(time_mins) + ' m', str(duration) + ' s')
else:
  if time_hours != 0:
    print(str(time_hours) + ' h', str(time_mins) + ' m', str(duration) + ' s')
  else:
    if time_mins != 0:
      print(str(time_mins) + ' m', str(duration) + ' s')
    else:
      print(str(duration) + ' s')
'''


'''
#2 задание
cubes = []
def summary(lst):               #функция расчета суммы нужных элементов в списке
  SUM = 0
  for idx in range(len(lst)):
    sum = 0
    new_el = lst[idx]
    #print(new_el)
    while new_el != 0:
      sum += new_el % 10
      new_el = new_el // 10   
    if sum % 7 == 0:
      SUM += lst[idx]
      #print('Добавлено')
  return SUM

for a in range(1, 1000):
  if a % 2 == 1:
    b = a*a*a
    cubes.append(b)

print('До:', summary(cubes))
#print('Кубы нечетных чисел от 1 до 100: ', cubes)
for idx in range(len(cubes)):
  cubes[idx] = cubes[idx] + 17

print('После:', summary(cubes))
'''



'''
#3 задание
for num in range(1, 100+1):
  if num in range(11, 20):
    print(num, 'процентов')
  else:
    last_digit = num % 10
    if last_digit == 1:
      print(num, 'процент')
    elif last_digit in range(2, 4+1):
      print(num, 'процента')
    else:
      print(num, 'процентов')
'''