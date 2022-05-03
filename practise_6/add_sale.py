import csv


def add(j):

  with open("bakery.csv", 'a+', newline = '') as csvfile:
    csvw = csv.writer(csvfile, delimiter = ' ')
    csvw.writerow(j)
  csvfile.close() 
  
j = input('En ')  
add(j)