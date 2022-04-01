
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
