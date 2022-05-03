import requests
import re
from collections import Counter

link = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
req = requests.get(link)


def spam(req):
  f = open('nginx_logs.txt', 'w+')
  ip_lst = []
  for a in req:
    a = a.decode()
    f.write(a)
  f.close()
  f = open('nginx_logs.txt', 'r+')
  ip = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
  for x in f:
    
    ls = ip.findall(x)
    if len(ls) == 2:
      del ls[1]
    elif len(ls) != 0:
      ip_lst.append(ls[0])

  g = Counter(ip_lst)
  f.close()
  return max(g, key = g.get)
print('Spammer: ', spam(req))