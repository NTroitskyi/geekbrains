from pprint import pprint
from random import randrange

'''
1-2.
def num_translate_adv(num_eng):

  """num_translate_adv(num_eng) -> string"""

  numbers = {
  'zero' : 'ноль',
  'one' : 'один',
  'two' : 'два',
  'three' : 'три',
  'four' : 'четыре',
  'five': 'пять',
  'six' : 'шесть',
  'seven' : 'семь',
  'eight' : 'восемь',
  'nine' : 'девять',
  'ten' : 'десять'
}
  if num_eng[0].isupper():
    return numbers[num_eng.lower()][0].upper() + numbers[num_eng.lower()][1:]
  elif num_eng[0].islower():
    return numbers[num_eng]
  else:
    return None



num_eng = str(input('Введите число на английском: '))
print(f'Число {num_eng} на русском:', num_translate_adv(num_eng))
'''


'''
3-4.
def thesaurus_adv(*args):
  """thesaurus_adv(*args) -> dictionary(key : dictionary(key : value)) """
  dic = {}
  for a in args:
    b = a.split()
    print(b)
    Name = b[0]
    Surname = b[1]
  
    if dic.get(Surname[0]) == None:
      dic[Surname[0]] = {Name[0] : []}
    elif dic.get(Surname[0]).get(Name[0]) == None:
      dic[Surname[0]][Name[0]] = []
    dic[Surname[0]][Name[0]].append(a)


      
  return dic

pprint(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
'''



'''
5.
def get_jokes(n, repeat = True):

  """Формирует список шуток

  Ключевые аргументы:
  n - количество шуток
  repeat - повторяются ли слова? (По умолчанию True)
  """
  
  nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
  adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
  adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

  jokes_list = []
  
  for count in range(n):
    if repeat:
      jokes_list.append(f"{nouns[randrange(len(nouns))]} {adverbs[randrange(len(adverbs))]} {adjectives[randrange(len(adjectives))]}")
      
    else:
      if len(nouns) > 0:        
        noun = nouns[randrange(len(nouns))]
        adverb = adverbs[randrange(len(adverbs))]
        adjective = adjectives[randrange(len(adjectives))]
        jokes_list.append(f"{noun} {adverb} {adjective}")
        
      else:
        jokes_list.append(None)
        
      try:
        nouns.remove(noun)
        adverbs.remove(adverb)
        adjectives.remove(adjective)
        
      except Exception:
        pass

  return jokes_list    

pprint(get_jokes(2))
'''