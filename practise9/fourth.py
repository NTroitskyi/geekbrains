class Car:
  def __init__(self, speed, color, name, is_police):
    self.speed = speed
    self.color = color
    self.name = name
    self.is_police = is_police

  def go(self):
    print('Машина начала движение.')

  def stop(self):
    print('Машина остановилась.')

  def turn(self, direction):
    print(f'Машина повернула {direction}')

  def show_speed(self):
    print(f'Текущая скорость: {self.speed} км/ч')

class TownCar(Car): 
  def show_speed(self):
    if self.speed > 60:
      print(f'Превышение скорости: {self.speed} км/ч')
    else:
      print(f'Текущая скорость: {self.speed} км/ч')
class SportCar(Car):
  pass
class WorkCar(Car):
  def show_speed(self):
    if self.speed > 40:
      print(f'Превышение скорости: {self.speed} км/ч')
    else:
      print(f'Текущая скорость: {self.speed} км/ч')
class PoliceCar(Car):
  pass


town = TownCar(80, "Красный", "Mazda", 0)
sport = SportCar(200, "Черный", "Bugatti", 0)
work = WorkCar(30, "Серый", "МТЗ", 0) #Трактор считается?
police = PoliceCar(100, "Белый", "Hyundai", 1)

town.go()
town.show_speed()
sport.turn("налево")
work.stop()
work.show_speed()
police.turn("направо")