import time

class TrafficLight:
  def __init__(self, color1, color2, color3):
    self.__color = [color1, color2, color3]

  def running(self):
    if self.__color != ["red", "yellow", "green"]:
      raise ValueError("Wrong order")
    time_lst = [7, 2, 7]
    while True:
      for a in range(3):
        print(self.__color[a])
        time.sleep(time_lst[a])
      print(self.__color[1])
      time.sleep(time_lst[1])

a = "red"
b = "yellow"
c = "green"


#TrafficLight(a, c, b).running()
TrafficLight(a, b, c).running()