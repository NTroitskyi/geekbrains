from pprint import pprint

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