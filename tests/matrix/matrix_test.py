import unittest
from matrix import Matrix, get_identity
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
        Z = self.A.get_neutral_element()
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
        Z = self.H.get_neutral_element()
        self.assertFalse(self.H.is_scalar_multiple(Z))
        self.assertTrue(Z.is_scalar_multiple(self.H))

if __name__ == '__main__':
    unittest.main()