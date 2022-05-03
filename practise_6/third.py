import sys
import csv

dict = {}
with open("FIO.csv") as fio:
  with open("hobby.csv") as hob:
    
    fio_r = csv.reader(fio, delimiter =',')
    hob_r = csv.reader(hob, delimiter =',')
    
    try:
      for row1 in fio_r:
        dict.update({' '.join(row1): ' '.join(next(hob_r))})
    except StopIteration:
      dict.update({' '.join(row1): None})
    else:
      sys.exit()

    with open('fio_hobby.csv', 'w+') as d:
      w = csv.DictWriter(d, dict.keys())
      w.writeheader()
      w.writerow(dict)
      d.close()
    hob.close()
  fio.close()