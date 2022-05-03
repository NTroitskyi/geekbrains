src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def I_hate_repeats(lst):
  extra_lst = []
  for i in range(len(lst)):
    ct = lst.count(lst[i])
    if ct == 1:
      extra_lst.append(lst[i])
  return extra_lst

print(I_hate_repeats(src))