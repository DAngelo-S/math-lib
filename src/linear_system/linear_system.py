from matrix import Matrix
from linear_system.error import InvalidTypeException, DivergeColumnsSizeException
import string

class LinearSystem:
    def __init__(self, equations: Matrix | list, solutions: Matrix | list):
        if isinstance(equations, list) and isinstance(solutions, list):
            self.equations = Matrix(equations)
            self.solutions = Matrix(solutions)
        elif isinstance(equations, Matrix) and isinstance(solutions, Matrix):
            self.equations = equations
            self.solutions = solutions
        else:
            raise InvalidTypeException()
        
        self.check_shape_eligibility()

        self.variables = self.get_variables()

    def __str__(self):
        s = ""

        justify = max([len(l[0]) for l in self.variables.value]) + max(len(str(elem)) for row in self.equations.value for elem in row) + 1
        
        for row, sol in zip(self.equations.value, self.solutions.value):
            for e, l in zip(row, self.variables.value):
                s += f" {e}{l[0]}".rjust(justify) + " +"
            s = s[:-1] + f"= {sol[0]}\n"
        return s[:-1]
    
    def __eq__(self, other):
        if self.equations == other.equations and self.solutions == self.solutions:
            return True
        return False

    def get_variables(self):
        rows = self.equations.get_shape()[1]

        return Matrix([[l] for l in list(string.ascii_lowercase[:rows])])

    def check_shape_eligibility(self):
        if self.equations.get_shape()[0] != self.solutions.get_shape()[0]:
            raise DivergeColumnsSizeException()

    def switch_lines(self, i, j):
        self.equations.value[i], self.equations.value[j] = self.equations.value[j], self.equations.value[i]
        self.solutions.value[i], self.solutions.value[j] = self.solutions.value[j], self.solutions.value[i]

    def multiply_line_by_scalar(self, i, alpha):
        self.equations.value[i] = [alpha.value * x for x in self.equations.value[i]]
        self.solutions.value[i] = [alpha.value * x for x in self.solutions.value[i]]

    def sum_line_by_scalar_multiple(self, i, alpha, j):
        self.equations.value[i] = [x + alpha.value * y for x, y in zip(self.equations.value[i], self.equations.value[j])]
        self.solutions.value[i][0] += alpha.value * self.solutions.value[j][0]

    def gauss_jordan_method(self):
        def sort_rows_by_pivot_and_apply_to(A, B):
            indexed_pivots = Matrix(A).get_indexed_pivots_by_row()

            # Ordena pelos índices dos pivôs
            indexed_pivots = sorted(indexed_pivots)
            order = [idx for _, idx in indexed_pivots]

            # Reordena self (A) e other (B)
            A = [A[i] for i in order]
            B = [B[i] for i in order]

            return A, B

        A = self.equations.value
        B = self.solutions.value

        for i in range(len(A)):
            rowA = A[i]
            pivot_index = Matrix(A).get_pivot_idx(i)

            if pivot_index == float('inf'): continue

            pivot = rowA[pivot_index]

            A[i] = rowA = [elem / pivot for elem in rowA]
            B[i][0] = B[i][0] / pivot

            for j in range(len(A)):
                if j == i: continue

                factor = A[j][pivot_index]
                rowB = A[j]
                A[j] = [b - factor * a for a, b in zip(rowA, rowB)]
                B[j][0] = B[j][0] - factor * B[i][0]

        A, B = sort_rows_by_pivot_and_apply_to(A, B)
        
        return LinearSystem(A, B)
