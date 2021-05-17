class CheckingForNumbers(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return 'is invalid input, CheckingForNumbers' \
               'Not a number found {}'.format(self.value)
