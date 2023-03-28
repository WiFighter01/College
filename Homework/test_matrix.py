import unittest
import matrix


class TestMatrixFunctions(unittest.TestCase):
    # Данные для тестирования функций
    def setUp(self):
        self.a = [[0, 1], [1, 1]]
        self.b = [[2, 1], [1, 3]]
        self.c = [[2, 2], [2, 4]]
        self.d = [[-2, 0], [0, -2]]
        self.e = [[1, 3], [3, 4]]
        self.g = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Тестирование генерации матрицы
    def test_matrix(self):
        # Матрица 2х2 диапазон от 1 до 1
        self.assertListEqual(matrix.matrix(2, 2, 1, 1), [[1, 1], [1, 1]])
        # Матрица 3х3 диапазон от 2 до 2
        self.assertListEqual(matrix.matrix(3, 3, 2, 2), [[2, 2, 2], [2, 2, 2], [2, 2, 2]])
        # Матрица 5х2 диапазон от 3 до 3
        self.assertListEqual(matrix.matrix(5, 2, 3, 3), [[3, 3], [3, 3], [3, 3], [3, 3], [3, 3]])

    # Тестирование сложения матриц
    # Тест на размер матриц не требуется, так как эта проверка происходит в самом модуле matrix
    def test_sum_m(self):
        # Сложение матриц 2х2
        self.assertListEqual(matrix.sum_m(self.a, self.b), self.c)
        # Сложение матриц 3х3
        self.assertListEqual(matrix.sum_m([[0, 1, 2], [3, 4, 5], [6, 7, 8]], [[8, 7, 6], [5, 4, 3], [2, 1, 0]]),
                             [[8, 8, 8], [8, 8, 8], [8, 8, 8]])

    # Тестирование вычитания матриц
    # Тест на размер матриц не требуется, так как эта проверка происходит в самом модуле matrix
    def test_minus_m(self):
        # Вычитание матриц 2х2
        self.assertListEqual(matrix.minus_m(self.a, self.b), self.d)
        # Вычитание матриц 3х3
        self.assertListEqual(matrix.minus_m([[0, 1, 2], [3, 4, 5], [6, 7, 8]], [[8, 7, 6], [5, 4, 3], [2, 1, 0]]),
                             [[-8, -6, -4], [-2, 0, 2], [4, 6, 8]])

    # Тестирование умножения матриц
    # Тест на размер матриц не требуется, так как эта проверка происходит в самом модуле matrix
    def test_mult_m(self):
        # Умножение матриц 2х2
        self.assertListEqual(matrix.mult_m(self.a, self.b), self.e)
        # Умножение матрицы 2х3 на матрицу 3х2
        self.assertListEqual(matrix.mult_m([[0, 1, 2], [3, 4, 5]], [[5, 4], [3, 2], [1, 0]]), [[5, 2], [32, 20]])

    # Тестирование умножения матрицы на число
    def test_mult_m_2(self):
        # Матрица 2х2 умножается на чило 5
        self.assertListEqual(matrix.mult_m_2([[1, 1], [1, 1]], 5), [[5, 5], [5, 5]])
        # Матрица 4х2 умножается на чило -2
        self.assertListEqual(matrix.mult_m_2([[0, 1], [2, 3], [4, 5], [6, 7]], -2),
                             [[0, -2], [-4, -6], [-8, -10], [-12, -14]])

    # Тестирование вычисления определителя 2 порядка
    # Тест на размер матриц не требуется, так как в самом модуле matrix можно задать матрицу только 2х2
    def test_opred_2(self):
        self.assertEqual(matrix.opred_2(self.a), -1)

    # Тестирование вычисления определителя 3 порядка
    # Тест на размер матриц не требуется, так как в самом модуле matrix можно задать матрицу только 2х2
    def test_opred_3(self):
        self.assertEqual(matrix.opred_3(self.g), 0)

    # Тестирование матриц на одинаковую размерность
    def test_matrix_equal(self):
        # Матрицы 2х2
        self.assertTrue(matrix.matrix_equal(self.a, self.b))
        # Матрицы 4х3
        self.assertTrue(matrix.matrix_equal([[0, 0, 0, 0], [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]],
                                            [[9, 9, 9, 9], [1, 1, 1, 1], [5, 5, 5, 5], [0, 0, 0, 0]]))


if __name__ == '__main__':
    unittest.main()
