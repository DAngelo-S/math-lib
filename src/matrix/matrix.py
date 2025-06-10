from matrix.error import MatrixsWithDifferentDimensionsException, InvalidDimensionsForMultiplyingColumnsException, InvalidTypeException, InvalidDimensionsForDeterminantFind
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
    
    def is_scalar_multiple(self, other):
        try:
            x = Scalar(self.value[0][0] / other.value[0][0])

            return x * other == self
        except ZeroDivisionError:
            return False
        except:
            raise

    def line_is_null(self, i):
        for n in self.get_ith_line(i):
            if n != 0:
                return False
        return True

    def get_pivot_idx(self, i):
        l = self.get_ith_line(i)

        for idx in range(len(l)):
            if l[idx] != 0:
                return idx
        return float('inf')
    
    def get_indexed_pivots_by_row(self):
        indexed_pivots = [(self.get_pivot_idx(idx), idx) for idx in range(len(self.value))]
        return indexed_pivots
    
    def null_lines_are_bellow(self):
        for i in range(len(self.value) - 1):
            if self.line_is_null(i) and not self.line_is_null(i+1):
                return False
        return True

    def every_pivot_is_one(self):
        for i in range(len(self.value)):
            pivot_index = self.get_pivot_idx(i)
            if pivot_index == float('inf'):
                continue
            pivot = self.value[i][pivot_index]
            if pivot != 1:
                return False
        return True
    
    def pivot_are_ordered(self):
        indexed_pivots = self.get_indexed_pivots_by_row()

        prev = -1
        for pivot_index, _ in indexed_pivots:
            if pivot_index == float('inf'):
                continue
            if prev > pivot_index:
                return False
            prev = pivot_index
        return True
    
    def every_column_is_null_except_for_pivot(self):
        indexed_pivots = self.get_indexed_pivots_by_row()

        for pivot_index, row_index in indexed_pivots:
            if pivot_index == float('inf'):
                continue

            col = self.get_jth_column(pivot_index)

            for j, val in enumerate(col):
                if j == row_index:
                    continue
                if val != 0:
                    return False
                
        return True
    
    def is_reduced_echelon(self):
        return self.null_lines_are_bellow() and self.every_pivot_is_one() and self.pivot_are_ordered() and self.every_column_is_null_except_for_pivot()

    def is_echelon(self):
        return self.null_lines_are_bellow() and self.pivot_are_ordered()

    def is_equivalent_by_lines(self, other):
        pass

    def is_elementar(self):
        pass
       
    # optimize
    def determinant(self):

        def cofactor(i, j):
            matrix = []
            
            for k, l in enumerate(self.value):
                if i == k:
                    continue
                line = l.copy()
                del line[j]
                matrix.append(line)
                
            M = Matrix(matrix)
            return (-1) ** (i+j) * M.determinant() #pro hacktoberfest, mostrar o que acontece se tirar o () do -1

        m, n = self.get_shape()

        if m != n:
            raise InvalidDimensionsForDeterminantFind()
        
        if m == 1:
            return self.value[0][0]
        else:
            return sum([self.value[0][j] * cofactor(0, j) for j in range(m)])

        

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

def get_neutral_element(m, n):
    result = []
    for i in range(m):
        result.append([0] * n)
    
    return Matrix(result)