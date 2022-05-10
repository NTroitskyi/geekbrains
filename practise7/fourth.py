import os
from pathlib import Path

a = os.path.abspath(os.curdir)


def dir_files_size(dict = {}):
  

  
  for i in os.listdir(os.curdir):
    if Path(i).is_file():

      sz = os.stat(Path(i)).st_size  
      key = int('1' + '0'*len(str(sz)))
      if key in dict:
        dict[key] += 1
      else:
        dict[key] = 1
    else:

    
      os.chdir(i)
      dir_files_size(dict)
  os.chdir('..')
  return dict






dir = f'{a}/fourth_dir'
os.chdir(dir)
print(dir_files_size())