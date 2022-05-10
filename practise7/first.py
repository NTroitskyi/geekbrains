import os
from pathlib import Path

d = os.path.abspath(os.curdir)
def ph(name):
  p = Path(f'{d}/{dr}/{name}')
  return p
def mkdr(path):
  path.mkdir(parents = True, exist_ok = True)
dr = 'my_project_1'
lst = ['settings', 'mainapp', 'adminapp', 'authapp']
for a in lst:
  p = ph(a)
  mkdr(p)