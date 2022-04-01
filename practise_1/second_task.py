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