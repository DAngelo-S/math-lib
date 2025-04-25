from matrix import Matrix
from error import InvalidTypeException, DivergeColumnsSizeException
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

    def gauss_jordan_method(self):
        def sort_rows_by_pivot_and_apply_to(A, B):
            indexed_pivots = []
            for idx, row in enumerate(A):
                for i, val in enumerate(row):
                    if val != 0:
                        indexed_pivots.append((i, idx))
                        break
                else:
                    indexed_pivots.append((float('inf'), idx))  # linha nula vai para o fim

            # Ordena pelos índices dos pivôs
            indexed_pivots.sort()
            order = [idx for _, idx in indexed_pivots]

            # Reordena self (A) e other (B)
            A = [A[i] for i in order]
            B = [B[i] for i in order]

            return A, B

        A = self.equations.value
        B = self.solutions.value

        for i in range(len(A)):

            A, B = sort_rows_by_pivot_and_apply_to(A, B)

            rowA = A[i]
            pivot = rowA[i]

            k = i + 1
            while pivot == 0 and k + 1 < len(rowA):
                pivot = rowA[k]
                k += 1
            
            if pivot == 0: continue

            A[i] = rowA = [elem / pivot for elem in rowA]
            B[i][0] = B[i][0] / pivot

            for j in range(len(A)):
                if j == i: continue

                factor = A[j][i]
                rowB = A[j]
                A[j] = [b - factor * a for a, b in zip(rowA, rowB)]
                B[j][0] = B[j][0] - factor * B[i][0]

        A, B = sort_rows_by_pivot_and_apply_to(A, B)

        return LinearSystem(A, B)

if __name__ == "__main__":
    L1 = LinearSystem([[1, 2], [3, -7]], [[5], [6]])

    assert(L1.equations == Matrix([[1, 2], [3, -7]]))
    assert(L1.solutions == Matrix([[5], [6]]))
    assert(L1.variables == Matrix([["a"], ["b"]]))

    L2 = LinearSystem([[1, 1, 1], [2, 1, 4], [2, 3, 5]], [[1000], [2000], [2500]])
    L3 = LinearSystem([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[700], [200], [100]])
    assert(L2.gauss_jordan_method() == L3)

    L4 = LinearSystem([[0, 0, 3, -9], [5, 15, -10, 40], [1, 3, -1, 5]], [[6], [-45], [-7]])
    L5 = LinearSystem([[1, 3, 0, 2], [0, 0, 1, -3], [0, 0, 0, 0]], [[-5], [2], [0]])
    assert(L4.gauss_jordan_method() == L5)