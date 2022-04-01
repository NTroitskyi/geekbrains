'''
1.

def typ(*args):
  a = 1
  for operation in args:
    print('Тип результата выражения №',a, ':', type(operation))
    a += 1




typ(15 * 3, 15 / 3, 15 // 2, 15**2)

'''
'''
2-3.
def quotation_of_numbers(lst):
  idx = 0
  while idx < len(lst):
    if lst[idx].isdigit():
      if float(lst[idx]) // 10 == 0:
        lst[idx] = '0' + str(lst[idx])
      lst.insert(idx+1, '"')
      lst.insert(idx, '"')
      idx += 2
    else:
      if (lst[idx][0] == '+' or lst[idx][0] == '-') and lst[idx][1:].isdigit():
        if float(lst[idx][1:]) // 10 == 0:
          lst[idx] = lst[idx][0] + '0' + str(lst[idx][1:])
        lst.insert(idx+1, '"')
        lst.insert(idx, '"')
        idx += 2
      idx += 1
  return lst

def string_from_list(lst):
  ind = 0
  my_string = ''
  while ind < len(lst):
    if lst[ind] == '"':
      my_string += lst[ind] + lst[ind+1] + lst[ind+2] + ' '
      ind += 3
    else:
      my_string += lst[ind] + ' '
      ind += 1
  return my_string

lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

print(string_from_list(quotation_of_numbers(lst)))

'''
'''
4.
def correct_name_string(lst):
  return str(element_splitted[-1][0].upper()) + str(element_splitted[-1][1:].lower())
  

lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for el in lst:
  element_splitted = el.split()
  print('Привет,', correct_name_string(element_splitted))


'''


'''
5.
prices = [57.8,
          46.51,
          97,
          14.24,
          92.1,
          54.25,
          79.99,
          12.02,
          18.89,
          43,
          12.5,
          15.06
]

for ind in range(len(prices)):
  kop = int(round(prices[ind] % 1, 2)*100)
  if kop < 10:
    kop = '0' + str(kop)
  prices[ind] = str(int(prices[ind] // 1)) + ' руб ' + str(kop) + ' коп'

print('Цены, по возростанию:')
prices.sort()
for a in prices:
  print(a)


print('_'*15)

prices_by_reduction = prices
prices_by_reduction.sort(reverse = True)


print('Цены, по убыванию:')
for a in prices_by_reduction:
  print(a)

print('_'*15)

print('Цены пяти самых дорогих товаров из списка(по возрастанию): ')
for a in prices[len(prices)-5:]:
  print(a)
'''