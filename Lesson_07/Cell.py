class Cell:
    def __init__(self, quantity):
        self.quantity = quantity
    def __add__(self, other):
        return Cell(self.quantity + other.quantity)
    def __sub__(self, other):
        return Cell(self.quantity + other.quantity)
    def __mul__(self, other):
        return Cell(self.quantity * other.quantity)
    def __truediv__(self, other):
        return int(Cell(self.quantity / other.quantity))
    def make_order(self, number_of_cells_in_row):
        result = ''
        cells_left = 0
        size = self.quantity
        if self.quantity / number_of_cells_in_row > int(self.quantity / number_of_cells_in_row):
            size += number_of_cells_in_row - self.quantity % number_of_cells_in_row

        for i in range(round(size)):
            if cells_left <= self.quantity:
                result += '*'
            else:
                result += '.'
            cells_left += 1
            if cells_left % number_of_cells_in_row == 0:
                result += '\n'
        return result
