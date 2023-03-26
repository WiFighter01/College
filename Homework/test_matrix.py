import unittest
import matrix


class MatrixTest(unittest.TestCase):
    def test_matrix(self):
        self.assertEqual(matrix.matrix(2, 2, 1, 1), [[1, 1], [1, 1]])

    def test_sum_m(self):
        self.assertEqual(matrix.sum_m(a, b), c)

    def test_minus_m(self):
        self.assertEqual(matrix.minus_m(a, b), d)

    def test_mult_m(self):
        self.assertEqual(matrix.mult_m(a, b), e)

    def test_mult_m_2(self):
        self.assertEqual(matrix.mult_m_2([[1, 1], [1, 1]], 5), [[5, 5], [5, 5]])

    def test_opred_2(self):
        self.assertEqual(matrix.opred_2(a), -1)

    def test_opred_3(self):
        self.assertEqual(matrix.opred_3(g), 0)

    def test_matrix_equal(self):
        self.assertEqual(matrix.matrix_equal(a, b), True)


a = [[0, 1], [1, 1]]
b = [[2, 1], [1, 3]]
c = [[2, 2], [2, 4]]
d = [[-2, 0], [0, -2]]
e = [[1, 3], [3, 4]]
g = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

if __name__ == '__main__':
    unittest.main()