def odd_nums(n):
  return (num for num in range(1, n+1, 2))

odd_n = odd_nums(15)

for el in odd_n:
  print(el)