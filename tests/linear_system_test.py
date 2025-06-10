import unittest
from matrix import Matrix, Scalar
from linear_system import LinearSystem

class TestLinearSystem(unittest.TestCase):
    def test_basic_attributes(self):
        L1 = LinearSystem([[1, 2], [3, -7]], [[5], [6]])
        self.assertEqual(L1.equations, Matrix([[1, 2], [3, -7]]))
        self.assertEqual(L1.solutions, Matrix([[5], [6]]))
        self.assertEqual(L1.variables, Matrix([["a"], ["b"]]))

    def test_elementar_operations(self):
        L1 = LinearSystem([[1, 2], [3, -7]], [[5], [6]])

        def test_swith_lines():
            L1.switch_lines(0, 1)

        def test_multiply_line_by_scalar():
            L1.multiply_line_by_scalar(0, Scalar(2))

        def test_sum_line_by_scalar_multiple():
            L1.sum_line_by_scalar_multiple(0, Scalar(-7), 1)

        test_swith_lines()
        self.assertEqual(L1, LinearSystem([[3, -7], [1, 2]], [[5], [6]]))

        test_multiply_line_by_scalar()
        self.assertEqual(L1, LinearSystem([[6, -14], [1, 2]], [[5], [6]]))

        test_sum_line_by_scalar_multiple()
        self.assertEqual(L1, LinearSystem([[-1, -28], [1, 2]], [[5], [6]]))


    def test_gauss_jordan(self):
        L2 = LinearSystem([[1, 1, 1], [2, 1, 4], [2, 3, 5]], [[1000], [2000], [2500]])
        L3 = LinearSystem([[1, 0, 0], [0, 1, 0], [0, 0, 1]], [[700], [200], [100]])
        self.assertTrue(L2.gauss_jordan_method() == L3)

        L4 = LinearSystem([[0, 0, 3, -9], [5, 15, -10, 40], [1, 3, -1, 5]], [[6], [-45], [-7]])
        L5 = LinearSystem([[1, 3, 0, 2], [0, 0, 1, -3], [0, 0, 0, 0]], [[-5], [2], [0]])
        self.assertTrue(L4.gauss_jordan_method() == L5)

        L6 = LinearSystem([[5, -3, 1], [0, 4, 3], [-10, 18, 7]], [[10],[-2],[5]])
        print(L6.gauss_jordan_method())

        ## TODO: mudar as soluçoes para termos independentes

if __name__ == '__main__':
    unittest.main()