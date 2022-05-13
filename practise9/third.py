class Worker:
  def __init__(self, name, surname, position, income):
    self.name = name
    self.surname = surname
    self.position = position
    self._income = income

class Position(Worker):
  def get_full_name(self):
    if type(self.name) != str or type(self.surname) != str:
      raise ValueError('Неверное имя')
    if type(self.position) != str:
      raise ValueError('Неверная должность')
    return f'Работник: {self.name} {self.surname}.\nДолжность: {self.position}'

  def get_total_income(self):
    income = self._income["wage"] + self._income["bonus"]
    return f'Доход: {income}$'

income = {"wage": 50000, "bonus": 5000}
name = "Иван"
surname = "Иванов"
position = "Back-end developer"

worker = Position(name, surname, position, income)
print(worker.get_full_name())
print(worker.get_total_income())