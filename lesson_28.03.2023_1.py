class Complex:
    __TYPE_T = (float, int)

    @classmethod
    def __test_value(cls, val):
        return type(val) in cls.__TYPE_T

    def set_number(self, re, im):
        if self.__test_value(re) and self.__test_value(im):
            self.__re = re
            self.__im = im
        else:
            raise ValueError('Need for types', self.__TYPE_T)

    def __init__(self, re=0, im=0):  # конструирование объекта
        self.set_number(re, im)

    def get_number(self):
        return self.__re, self.__im

    def set_complex(self, cmpl):
        re, im = cmpl.get_number()
        self.__re = re
        self.__im = im

    # def get_complex(self):
    #     return self

    def __str__(self):  # вывод в print
        return f'{self.__re} {"+" if self.__im >= 0 else "-"} i {abs(self.__im)}'

    def __add__(self, right):  # self + right
        return Complex(self.__re + right.__re, self.__im + right.__im)

    def __sub__(self, right):  # self - right
        return Complex(self.__re - right.__re, self.__im - right.__im)

    def __mul__(self, right):  # self * right
        return Complex(self.__re * right.__re - self.__im * right.__im,
                       self.__re * right.__im + self.__im * right.__re)

    @staticmethod
    def norm(x, y, isSquare=False):
        res = x ** 2 + y ** 2
        if isSquare:
            return res
        return res ** 0.5

    def __truediv__(self, right):  # self / right
        n = self.norm(right.__re, right.__im, True)
        return Complex((self.__re * right.__re + self.__im * right.__im) / n,
                       right.__re * self.__im - self.__re * right.__im)


def main():
    c1 = Complex(1, 2)
    c2 = Complex(2, 4)
    print(c1 + c2)
    print(c1 - c2)
    print(c1 * c2)
    print(c1 / c2)


if __name__ == '__main__':
    main()
