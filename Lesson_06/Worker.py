salary_and_bonus = {"wage": 0, "bonus": 0}

class Worker(object):
    name = ''
    surname = ''
    __position = ''
    _income = salary_and_bonus
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.__position = position
        self._income = income
    def set_income(self, salary_and_bonus):
        self._income = salary_and_bonus