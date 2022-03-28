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