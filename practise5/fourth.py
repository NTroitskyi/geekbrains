src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def cursed_sorting(lst):
  extra_lst = []
  for idx in range(1, len(lst)):
    if lst[idx-1] < lst[idx]:
      extra_lst.append(lst[idx])
  return extra_lst


print(cursed_sorting(src))