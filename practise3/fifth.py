from random import randrange
from pprint import pprint




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