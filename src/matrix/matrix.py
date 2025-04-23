from matrix.error import MatrixsWithDifferentDimensionsException, InvalidDimensionsForMultiplyingColumnsException, InvalidTypeException
from matrix.scalar import Scalar

class Matrix:
    def __init__(self, matrix):
        self.value = matrix

    def __str__(self):
        string_matrix = [[str(elem) for elem in row] for row in self.value]
        justify = max([max([len(string_matrix[i][j]) for i in range(self.get_shape()[0])]) for j in range(self.get_shape()[1])])

        s = ""
        for row in self.value:
            s += "[ " + ' '.join([str(elem).rjust(justify) for elem in row]) + " ]" + "\n"
        return s[:-1]
    
    def __add__(self, other):
        if self.get_shape() != other.get_shape():
            raise MatrixsWithDifferentDimensionsException()
        
        return Matrix([[a + b for a, b in zip(rowa, rowb)] for rowa, rowb in zip(self.value, other.value)])

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        if self.get_shape() != other.get_shape():
            raise MatrixsWithDifferentDimensionsException()
        
        return Matrix([[a - b for a, b in zip(rowa, rowb)] for rowa, rowb in zip(self.value, other.value)])
    
    def __isub__(self, other):
        return self - other

    def __eq__(self, other):
        if self.get_shape() != other.get_shape():
            return False
        for line1, line2 in zip(self.value, other.value):
            for element1, element2 in zip(line1, line2):
                if element1 != element2:
                    return False
        return True

    def __mul__(self, other):
        if isinstance(other, Scalar):
            return Matrix([[other.value * a for a in row] for row in self.value])
        
        elif isinstance(other, Matrix):
            if self.get_shape()[1] != other.get_shape()[0]:
                raise InvalidDimensionsForMultiplyingColumnsException()
            result = []

            m, n = self.get_shape()[0], other.get_shape()[1]
            for i in range(m):
                row = []
                for j in range(n):
                    a_row = self.get_ith_line(i)
                    b_col = other.get_jth_column(j)
                    row.append(sum([a * b for a, b in zip(a_row, b_col)]))
                result.append(row)
            
            return Matrix(result)
        
        else:
            raise InvalidTypeException()
    
    def __imul__(self, other):
        return self * other
    
    def __neg__(self):
        return Scalar(-1) * self

    def __truediv__(self, other):
        pass

    def __pow__(self, other):
        if self.get_shape()[1] != self.get_shape()[0]:
            raise InvalidDimensionsForMultiplyingColumnsException()
        
        if not isinstance(other, int) or other < 0:
            raise InvalidTypeException()
        
        result = get_identity(self.get_shape()[0])

        while(other > 0):
            result *= self
            other -= 1
        
        return result

    def __ipow__(self, other):
        return self ** other

    def __invert__(self):
        return self.transpose()

    def get_shape(self):
        m = len(self.value)
        n = len(self.value[0])

        return (m, n)
    
    def get_ith_line(self, i):
        return self.value[i]
    
    def get_jth_column(self, j):
        column = []

        for line in self.value:
            column.append(line[j])
        
        return column
    
    def transpose(self):
        result = []

        for j in range(len(self.value[0])):
            result.append(self.get_jth_column(j))

        return Matrix(result)
    
    def get_neutral_element(self):
        m, n = self.get_shape()

        result = []
        for i in range(m):
            result.append([0] * n)
        
        return Matrix(result)
    
    def is_scalar_multiple(self, other):
        try:
            x = Scalar(self.value[0][0] / other.value[0][0])

            return x * other == self
        except ZeroDivisionError:
            return False
        except:
            raise


def get_identity(size):
    result = []

    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        result.append(row)
        
    return Matrix(result)