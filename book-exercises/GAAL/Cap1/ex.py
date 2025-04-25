import unittest
from matrix import Matrix, Scalar, error

class MatrixExercises(unittest.TestCase):

    # 1.1.1.
    def test_considere_as_seguintes_matrizes_e_se_possivel_calcule(self):
        A = Matrix([[2, 0], [6, 7]])
        B = Matrix([[0, 4], [2, -8]])
        C = Matrix([[-6, 9, -7], [7, -3, -2]])
        D = Matrix([[-6, 4, 0], [1, 1, 4], [-6, 0, 6]])
        E = Matrix([[6, 9, -9], [-1, 0, -4], [-6, 0, -1]])

        print("1.1.1. Considere as seguintes matrizes:")
        print("A")
        print(A, "\n")
        print("B")
        print(B, "\n")
        print("C")
        print(C, "\n")
        print("D")
        print(D, "\n")
        print("E")
        print(E, "\n")

        print("Se for possível calcule:")
        print("(a) AB - BA")
        print(A * B - B * A, "\n")
        assert(A*B-B*A == Matrix([[-24, -20], [58, 24]]))

        print("(b) 2C - D")
        try:
            print(Scalar(2) * C - D, "\n")
        except Exception as e:
            print(e, "\n")
            assert isinstance(e, error.MatrixsWithDifferentDimensionsException)

        print("(c) (2D^t - 3E^t)^t")
        print((Scalar(2)*D.transpose() - Scalar(3)*E.transpose()).transpose(), "\n")
        assert((Scalar(2)*D.transpose() - Scalar(3)*E.transpose()).transpose() == Matrix([[-30, -19, 27], [5, 2, 20], [6, 0, 15]]))

        print("(d) D^2 - DE")
        print(D ** 2 - D * E, "\n")
        assert(D ** 2 - D * E == Matrix([[80, 34, -22], [-10, -4, 45], [72, 30, -12]]))

    # 1.1.2
    def test_conhecendo_se_somente_os_produtos_AB_e_AC_como_podemos_calcular(self):
        A = Matrix([[2, 0], [6, 7]])
        B = Matrix([[0, 4], [2, -8]])
        C = Matrix([[-6, 9], [7, -3]])
        
        print("1.1.2. Conhecendo-se somento os profutos AB e AC, como podemos calcular A(B + C), B^t A^t, C^t A^t e (ABA)C?\n")

        assert(A * (B + C) == A * B + A * C)
        print("A(B + C) = AB + AC (teorema j)")
        print("\n")

        assert(B.transpose() * A.transpose() == (A*B).transpose())
        print("B^t A^t = (AB)^t (teorema o)")
        print("\n")

        assert(C.transpose() * A.transpose() == (A*C).transpose())
        print("C^t A^t = (AC)^t (teorema o)")
        print("\n")

        assert((A*B*A)*C == (A*B) * (A*C))
        print("(ABA)C = (AB)(AC) (teorema h)")
        print("\n")

    # 1.1.3
    # 1.1.4
    # 1.1.5
    # 1.1.6
    # 1.1.7
    # 1.1.8
    # 1.1.9
    # 1.1.10
    # 1.1.11
    # 1.1.12
    # 1.1.13
    # 1.1.14
    # 1.1.15
    # 1.1.16
    # 1.1.17
    # 1.1.18
    # 1.1.19
    # 1.1.20
    # 1.1.21
    # 1.1.22
    # 1.1.23
    # 1.1.24
    # 1.1.25
    # 1.1.26
    # 1.1.27
    # 1.1.28
    # 1.1.29

if __name__ == '__main__':
    unittest.main()