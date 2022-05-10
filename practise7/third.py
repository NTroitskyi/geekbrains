import os
from pathlib import Path
import shutil




d = os.getcwd()
proj_dir = f'{d}/my_project'
os.chdir(proj_dir)


def templ():
  dest = 'templates'



  dir_lst = os.listdir(os.curdir)
  for i in dir_lst:
    if Path(i).is_file():
      pass
    else:
      
      if i == dest:
        if dest in os.listdir(proj_dir):
          for papka in os.listdir(i):
            try:
              shutil.copytree(f'{i}/{papka}', f'{proj_dir}/{dest}/{papka}')
            except FileExistsError:
              pass
          

        else:
          try:
            shutil.copytree(i, f'{proj_dir}/{dest}')
          except FileExistsError:
              pass
          
      os.chdir(i)
      templ()
  os.chdir('..')
  return


templ()