class DivisionByZero(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return '{} is invalid input, DivisionByZero' \
               'cannot be divided by zero'.format(self.value)
