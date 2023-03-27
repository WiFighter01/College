import unittest
import matrix


class TestMatrixFunctions(unittest.TestCase):
    def setUp(self):
        self.a = [[0, 1], [1, 1]]
        self.b = [[2, 1], [1, 3]]
        self.c = [[2, 2], [2, 4]]
        self.d = [[-2, 0], [0, -2]]
        self.e = [[1, 3], [3, 4]]
        self.g = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def test_matrix(self):
        self.assertEqual(matrix.matrix(2, 2, 1, 1), [[1, 1], [1, 1]])

    def test_sum_m(self):
        self.assertEqual(matrix.sum_m(self.a, self.b), self.c)

    def test_minus_m(self):
        self.assertEqual(matrix.minus_m(self.a, self.b), self.d)

    def test_mult_m(self):
        self.assertEqual(matrix.mult_m(self.a, self.b), self.e)

    def test_mult_m_2(self):
        self.assertEqual(matrix.mult_m_2([[1, 1], [1, 1]], 5), [[5, 5], [5, 5]])

    def test_opred_2(self):
        self.assertEqual(matrix.opred_2(self.a), -1)

    def test_opred_3(self):
        self.assertEqual(matrix.opred_3(self.g), 0)

    def test_matrix_equal(self):
        self.assertEqual(matrix.matrix_equal(self.a, self.b), True)


if __name__ == '__main__':
    unittest.main()