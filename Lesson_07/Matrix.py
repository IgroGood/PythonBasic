
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    def __str__(self):
        result = ''
        for i in range(len(self.matrix)):
            result += ' '.join(list(map(str, self.matrix[i]))) + '\n'
        return result
    def __add__(self, matrixB):
        width = max(len(self.matrix), len(matrixB.matrix))
        height = max(len(self.matrix[0]), len(matrixB.matrix[0]))
        result = Matrix([[0 for j in range(height)] for i in range(width)])
        for i in range(height + 1):
            for j in range(width + 1):
                if i < len(self.matrix) and j < len(self.matrix[i]):
                    result.matrix[i][j] += self.matrix[i][j]
                if i < len(matrixB.matrix) and j < len(matrixB.matrix[i]):
                    result.matrix[i][j] += matrixB.matrix[i][j]
        return result