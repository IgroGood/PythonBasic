from Worker import Worker


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    def get_total_income(self):
        return self._income['wage'] * self._income['bonus']