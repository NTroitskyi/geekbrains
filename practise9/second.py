class Road:
  def __init__(self, lenght, width):
    self._length = lenght
    self._width = width
    self._kilos = 25
    self._height = 5 * pow(10, -3)
  
  def calc_mass(self):
    #масса асфальта для покрытия одного кв. метра дороги асфальтом = 25 кг
    #число см толщины полотна = 5 см
    return self._length * self._width * self._kilos * self._height

l = float(input('Введите длинну дороги: '))
w = float(input('Введите ширину дороги: '))

road = Road(l, w)
print(f'Масса: {road.calc_mass()} т.')