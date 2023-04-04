import unittest
import fractions


class TestFractions(unittest.TestCase):
    def setUp(self):
        self.d1 = fractions.Fractions(1, 2)
        self.d2 = fractions.Fractions(3, 9)
        self.d3 = fractions.Fractions(5, 6)
        self.d4 = fractions.Fractions(7, 6)
        self.a = 25
        self.b = 100

    def test_set_fractions(self):
        self.assertEqual(fractions.Fractions.set_fractions(self.d1, 1, 2), None)
        with self.assertRaises(ValueError):
            fractions.Fractions.set_fractions(self.d2, 10, 0)

    def test__str__(self):
        self.assertEqual(fractions.Fractions.__str__(self.d1), '1/2')
        self.assertEqual(fractions.Fractions.__str__(self.d2), '3/9')

    def test_get_fractions(self):
        self.assertEqual(self.d1.get_fractions(), '1/2')
        self.assertEqual(self.d2.get_fractions(), '3/9')

    def test__add__(self):
        self.assertEqual(print(fractions.Fractions.__add__(self.d1, self.d2)), print(self.d3))
        self.assertEqual(print(fractions.Fractions.__add__(self.d2, self.d3)), print(self.d4))

    def test__sub__(self):
        self.assertEqual(print(fractions.Fractions.__sub__(self.d1, self.d2)), print('1/6'))
        self.assertEqual(print(fractions.Fractions.__sub__(self.d2, self.d3)), print('1/2'))

    def test__mul__(self):
        self.assertEqual(print(fractions.Fractions.__mul__(self.d1, self.d2)), print('1/6'))
        self.assertEqual(print(fractions.Fractions.__mul__(self.d2, self.d3)), print('5/18'))

    def test__truediv__(self):
        self.assertEqual(print(fractions.Fractions.__truediv__(self.d1, self.d2)), print('3/2'))
        self.assertEqual(print(fractions.Fractions.__truediv__(self.d2, self.d3)), print('2/5'))


if __name__ == '__main__':
    unittest.main()
