class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)
    def __mul__(self, other):
        return ComplexNumber(self.a * other.a, self.b * other.b)