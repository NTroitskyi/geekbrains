import sys


import csv

def show_from(a):

  with open("bakery.csv", 'r' ) as csvfile:
    csvr = csv.reader(csvfile, delimiter=" ")
    i = 2
    while i <= int(a):
      try:
        next(csvr)
      except StopIteration:
        sys.exit()
        break
      else:
        i += 1  
    while True:
      try:
        print(''.join(next(csvr)))
      except StopIteration:
        break
    csvfile.close()

def show_from_to(a, b):

  with open("bakery.csv", 'r' ) as csvfile:
    csvr = csv.reader(csvfile, delimiter=" ")
    i = 2
    while i <= int(a):
      try:
        next(csvr)
      except StopIteration:
        sys.exit()
        break
      else:
        i += 1 
    while i <= int(b) + 1:
      try:
        print(''.join(next(csvr)))
      except StopIteration:
        print(None)
        i += 1
      else:
        i += 1
    csvfile.close()
    
a = input('Введите рамки: ')
if len(str(a)) == 1:
  show_from(a)
elif  len(str(a)) == 3:
  b = a.split(' ')
  show_from_to(b[0], b[1])
else:
  print('Ошибка ввода.')

