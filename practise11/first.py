class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date):
        day, month, year = map(int, date.split('-'))
        return day, month, year

    @staticmethod
    def is_date_valid(date):
        day, month, year = map(int, date.split('-'))
        return day <= 31 and month <= 12

date2 = Date.from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')
print(date2)
print(is_date)
