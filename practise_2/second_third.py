def quotation_of_numbers(lst):
  idx = 0
  while idx < len(lst):
    if lst[idx].isdigit():
      if float(lst[idx]) // 10 == 0:
        lst[idx] = '0' + str(lst[idx])
      lst.insert(idx+1, '"')
      lst.insert(idx, '"')
      idx += 2
    else:
      if (lst[idx][0] == '+' or lst[idx][0] == '-') and lst[idx][1:].isdigit():
        if float(lst[idx][1:]) // 10 == 0:
          lst[idx] = lst[idx][0] + '0' + str(lst[idx][1:])
        lst.insert(idx+1, '"')
        lst.insert(idx, '"')
        idx += 2
      idx += 1
  return lst

def string_from_list(lst):
  ind = 0
  my_string = ''
  while ind < len(lst):
    if lst[ind] == '"':
      my_string += lst[ind] + lst[ind+1] + lst[ind+2] + ' '
      ind += 3
    else:
      my_string += lst[ind] + ' '
      ind += 1
  return my_string

lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

print(string_from_list(quotation_of_numbers(lst)))