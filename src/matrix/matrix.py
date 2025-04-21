from .error import MatrixsWithDifferentDimensionsException, InvalidDimensionsForMultiplyingColumnsException, InvalidTypeException
from .scalar import Scalar

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
    
if __name__ == "__main__":
    A = Matrix([[1, 2, -3], [3, 4, 0]])
    A_t = Matrix([[1, 3], [2, 4], [-3, 0]])
    B = Matrix([[-2, 1, 5], [0, 3, -4]])
    C = Matrix([[-1, 3, 2], [3, 7, -4]])
    D = Matrix([[3, 1, -8], [3, 1, 4]])
    E = Matrix([[2, 4, -6], [6, 8, 0]])
    F = Matrix([[-17, 19, 0], [-6, 15, 0]])
    G = Matrix([[1, 2, -3], [3, 4, 0]])
    H = Matrix([[-2, 1, 0], [0, 3, 0], [5, -4, 0]])
    I = H * Scalar(5)

    assert A != B, "A different than B"
    assert A + B == C, "sum two Matrixs"
    assert A - B == D, "subtract two Matrixs"
    assert A * Scalar(2) == E, "multiply Matrix and scalar"
    assert Scalar(2) * A == E, "multiply scalar and Matrix"
    assert G * H == F, "multiplying two Matrixs"
    try:
        H * G
        assert False, "Expected an error for invalid dimesions"
    except InvalidDimensionsForMultiplyingColumnsException as e:
        assert True
    assert A_t == A.transpose() == ~A, "transposed Matrix"

    ### properties ###

    # comutatividade
    assert A + B == B + A
    # associatividade
    assert A + (B + C) == (A + B) + C
    # elemento neutro
    Z = A.get_neutral_element()
    assert A + Z == A
    # elemento simétrico
    assert A + (-A) == Z
    # associatividade 
    assert Scalar(3) * (Scalar(5) * A) == (Scalar(3) * Scalar(5)) * A
    # distributividade
    assert Scalar(7) * (A + B) == Scalar(7) * A + Scalar(7) * B
    # distributividade
    assert (Scalar(11) + Scalar(13)) * A == Scalar(11) * A + Scalar(13) * A
    # associatividade
    assert G * (H * I) == (G * H) * I
    # elemento neutro
    Im = get_identity(A.get_shape()[0])
    In = get_identity(A.get_shape()[1])
    assert A * In == Im * A == A
    # distributividade
    assert G * (H + I) == G * H + G * I
    assert (G + E) * H == G * H + E * H
    assert Scalar(7) * (G * H) == (Scalar(7) * G) * H == G * (Scalar(7) * H)
    assert ~~A == A
    assert ~(A + B) == ~A + ~B
    assert ~(Scalar(7) * A) == Scalar(7) * ~A
    assert ~(G * H) == ~H * ~G

    # potencializaçao
    assert H ** 0 == get_identity(H.get_shape()[0])
    assert H ** 1 == H
    assert H ** 2 == H * H
    assert H ** 3 == H * H * H

    # produtos notaveis
    assert (H + I) * (H - I) == H ** 2 - I ** 2
    assert (H + I) ** 2 == H ** 2 + Scalar(2) * H * I + I ** 2
