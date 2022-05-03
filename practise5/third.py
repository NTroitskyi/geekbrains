tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]



def tut_class_gen(tutors, classes):
  for i in range(len(tutors)):
    try:
      yield (tutors[i], classes[i])
    except IndexError:
      yield (tutors[i], None)


a = tut_class_gen(tutors, klasses)

#for i in a:
#  print(i)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
#print(next(a)) Stopiteration