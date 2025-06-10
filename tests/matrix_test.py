import unittest
from matrix import Matrix, get_identity, get_neutral_element
from matrix import Scalar
from matrix.error import InvalidDimensionsForMultiplyingColumnsException

class TestMatrixOperations(unittest.TestCase):
    def setUp(self):
        self.A = Matrix([[1, 2, -3], [3, 4, 0]])
        self.A_t = Matrix([[1, 3], [2, 4], [-3, 0]])
        self.B = Matrix([[-2, 1, 5], [0, 3, -4]])
        self.C = Matrix([[-1, 3, 2], [3, 7, -4]])
        self.D = Matrix([[3, 1, -8], [3, 1, 4]])
        self.E = Matrix([[2, 4, -6], [6, 8, 0]])
        self.F = Matrix([[-17, 19, 0], [-6, 15, 0]])
        self.G = Matrix([[1, 2, -3], [3, 4, 0]])
        self.H = Matrix([[-2, 1, 0], [0, 3, 0], [5, -4, 0]])
        self.I = self.H * Scalar(5)

    def test_basic_operations(self):
        self.assertNotEqual(self.A, self.B)
        self.assertEqual(self.A + self.B, self.C)
        self.assertEqual(self.A - self.B, self.D)
        self.assertEqual(self.A * Scalar(2), self.E)
        self.assertEqual(Scalar(2) * self.A, self.E)
        self.assertEqual(self.G * self.H, self.F)
        with self.assertRaises(InvalidDimensionsForMultiplyingColumnsException):
            self.H * self.G
        self.assertEqual(self.A_t, self.A.transpose())
        self.assertEqual(~self.A, self.A.transpose())

    def test_properties(self):
        m, n = self.A.get_shape()
        Z = get_neutral_element(m, n)
        self.assertEqual(self.A + self.B, self.B + self.A)
        self.assertEqual(self.A + (self.B + self.C), (self.A + self.B) + self.C)
        self.assertEqual(self.A + Z, self.A)
        self.assertEqual(self.A + (-self.A), Z)
        self.assertEqual(Scalar(3) * (Scalar(5) * self.A), (Scalar(3) * Scalar(5)) * self.A)
        self.assertEqual(Scalar(7) * (self.A + self.B), Scalar(7) * self.A + Scalar(7) * self.B)
        self.assertEqual((Scalar(11) + Scalar(13)) * self.A, Scalar(11) * self.A + Scalar(13) * self.A)
        self.assertEqual(self.G * (self.H * self.I), (self.G * self.H) * self.I)

    def test_identity_and_transpose(self):
        Im = get_identity(self.A.get_shape()[0])
        In = get_identity(self.A.get_shape()[1])
        self.assertEqual(self.A * In, self.A)
        self.assertEqual(Im * self.A, self.A)

    def test_distributivity(self):
        self.assertEqual(self.G * (self.H + self.I), self.G * self.H + self.G * self.I)
        self.assertEqual((self.G + self.E) * self.H, self.G * self.H + self.E * self.H)
        self.assertEqual(Scalar(7) * (self.G * self.H), (Scalar(7) * self.G) * self.H)
        self.assertEqual(Scalar(7) * (self.G * self.H), self.G * (Scalar(7) * self.H))

    def test_transpose_properties(self):
        self.assertEqual(~~self.A, self.A)
        self.assertEqual(~(self.A + self.B), ~self.A + ~self.B)
        self.assertEqual(~(Scalar(7) * self.A), Scalar(7) * ~self.A)
        self.assertEqual(~(self.G * self.H), ~self.H * ~self.G)

    def test_power_and_notables(self):
        self.assertEqual(self.H ** 0, get_identity(self.H.get_shape()[0]))
        self.assertEqual(self.H ** 1, self.H)
        self.assertEqual(self.H ** 2, self.H * self.H)
        self.assertEqual(self.H ** 3, self.H * self.H * self.H)
        self.assertEqual((self.H + self.I) * (self.H - self.I), self.H ** 2 - self.I ** 2)
        self.assertEqual((self.H + self.I) ** 2, self.H ** 2 + Scalar(2) * self.H * self.I + self.I ** 2)

    def test_if_A_matrix_is_scalar_multiple_of_B(self):
        self.assertFalse(self.A.is_scalar_multiple(self.B))
        self.assertTrue(self.H.is_scalar_multiple(self.I))
        self.assertTrue(self.I.is_scalar_multiple(self.H))
        m, n = self.H.get_shape()
        Z = get_neutral_element(m, n)
        self.assertFalse(self.H.is_scalar_multiple(Z))
        self.assertTrue(Z.is_scalar_multiple(self.H))

    def test_if_line_is_null(self):
        B = Matrix([[0, 2, -3], [0, 0, 0]])
        self.assertTrue(B.line_is_null(1))
        self.assertFalse(B.line_is_null(0))

    def test_get_pivot_idx(self):
        A = Matrix([[1, 2, -3], [3, 4, 0]])
        B = Matrix([[0, 2, -3], [0, 0, 0]])
        
        self.assertEqual(A.get_pivot_idx(0), 0)
        self.assertEqual(A.get_pivot_idx(1), 0)
        self.assertEqual(B.get_pivot_idx(0), 1)
        self.assertEqual(B.get_pivot_idx(1), float('inf'))

    def test_get_indexed_pivots_by_row(self):
        B = Matrix([[0, 0, 0], [1, 2, 3], [0, 2, -3], [0, 0, 0]])

        self.assertEqual(B.get_indexed_pivots_by_row(), [(float('inf'), 0), (0, 1), (1, 2), (float('inf'), 3)])

    def test_get_every_pivot_is_one(self):
        B = Matrix([[0, 0, 0], [1, 2, 3], [0, 2, -3], [0, 0, 0]])
        C = Matrix([[1, 0, 0], [0, 1, 3], [0, 0, 1], [0, 0, 0]])

        self.assertFalse(B.every_pivot_is_one())
        self.assertTrue(C.every_pivot_is_one())

    def test_pivot_are_ordered(self):
        B = Matrix([[0, 0, 0], [1, 2, 3], [0, 2, -3], [1, 0, 0]])
        C = Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 3], [0, 0, 1], [0, 0, 0]])

        self.assertFalse(B.pivot_are_ordered())
        self.assertTrue(C.pivot_are_ordered())

    def test_every_column_is_null_except_for_pivot(self):
        B = Matrix([[0, 0, 0], [1, 2, 3], [0, 2, -3], [1, 0, 0]])
        C = Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]])

        self.assertFalse(B.every_column_is_null_except_for_pivot())
        self.assertTrue(C.every_column_is_null_except_for_pivot())

    def test_if_matrix_is_reduced_echelon(self):
        A = Matrix([[1, 0, 0, 3], [0, 1, 0, -2], [0, 0, 1, 5]])
        B = Matrix([[1, 3, 0, 2], [0, 0, 1, -3], [0, 0, 0, 0]])
        C = Matrix([[1, 3, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        D = Matrix([[1, 1, 1], [0, -1, 2], [0, 0, 5]])
        E = Matrix([[1, 3, -1, 5], [0, 0, -5, 15], [0, 0, 0, 0]])

        self.assertTrue(A.is_reduced_echelon())
        self.assertTrue(B.is_reduced_echelon())
        self.assertTrue(C.is_reduced_echelon())
        self.assertFalse(D.is_reduced_echelon())
        self.assertFalse(E.is_reduced_echelon())

    def test_if_matrix_is_reduced_echelon(self):
        A = Matrix([[1, 0, 0, 3], [0, 1, 0, -2], [0, 0, 1, 5]])
        B = Matrix([[1, 3, 0, 2], [0, 0, 1, -3], [0, 0, 0, 0]])
        C = Matrix([[1, 3, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
        D = Matrix([[1, 1, 1], [0, -1, 2], [0, 0, 5]])
        E = Matrix([[1, 3, -1, 5], [0, 0, -5, 15], [0, 0, 0, 0]])

        self.assertTrue(A.is_echelon())
        self.assertTrue(B.is_echelon())
        self.assertTrue(C.is_echelon())
        self.assertTrue(D.is_echelon())
        self.assertTrue(E.is_echelon())

    def test_determinant(self):
        A = Matrix([[1, 1028931, 123], [0, 0, 0], [-2, 1, 3]])
        B = Matrix([[-13]]) # B = Matrix([-13]) should not exist, edit code and test it
        C = Matrix([[4, 3], [2, 1]])
        D = Matrix([[1, 4, 1], [2, 2, -1], [3, 0, 1]])

        self.assertTrue(A.determinant() == 0)
        self.assertTrue(B.determinant() == -13)
        self.assertTrue(C.determinant() == -2)
        self.assertTrue(D.determinant() == -24)

        # > **Corolário:** Seja A uma matriz n x n. Se A possui duas linhas iguais, então det(A) = 0.
        E = Matrix([[1, 1028931, 123], [1, 1028931, 123], [-2, 1, 3]])
        self.assertTrue(E.determinant() == 0)

        # Se B = XA (X real), entao det(B) = X det(A)
        F = Matrix([[1, 10], [-15, 20]])
        G = Matrix([[23*1, 23*10], [-15, 20]])
        self.assertTrue(G.determinant() == 23 * F.determinant())
        # Se B resulta de A pela troca da posiçao de duas linhas, ent det(B) = -det(A)
        H = Matrix([[-15, 20], [1, 10]])
        self.assertTrue(H.determinant() == - F.determinant())
        # Se B é obtida de A substituindo-se a linha i por ela somada a um multiplo escalar de uma linha k diferente de i, entao det(B) = det(A)
        J = Matrix([[1+(-15)*9, 10+(20)*9], [-15, 20]])
        self.assertTrue(F.determinant() == J.determinant())

        # O determinante do produto A por B é igual ao produto dos seus determinantes
        self.assertTrue((C*F).determinant() == C.determinant() * F.determinant())

        # Os determinantes de A e de sua transposta A^t sao iguais
        self.assertTrue(A.determinant() == A.transpose().determinant())

        # test: (IBADE 2018) Considere as matrizes A e B, quadradas de ordem 2, com detA = 10 e detB = 2. Então o valor de det[(4.A).(3.B)] é igual: 2ˆ6*3^2*5

if __name__ == '__main__':
    unittest.main()