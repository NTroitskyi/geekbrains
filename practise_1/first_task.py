duration = int(input())
rest = 0
time_mins = 0
time_hours = 0
time_days = 0

if duration > 60:
  time_mins = duration // 60
  if time_mins > 60:
    time_hours = time_mins // 60
    time_mins = time_mins % 60
    if time_hours > 24:
      time_days = time_hours // 24
      time_hours = time_hours % 24
  duration = duration % 60

if time_days != 0:
  print(str(time_days) + ' d', str(time_hours) + ' h', str(time_mins) + ' m', str(duration) + ' s')
else:
  if time_hours != 0:
    print(str(time_hours) + ' h', str(time_mins) + ' m', str(duration) + ' s')
  else:
    if time_mins != 0:
      print(str(time_mins) + ' m', str(duration) + ' s')
    else:
      print(str(duration) + ' s')