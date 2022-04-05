

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