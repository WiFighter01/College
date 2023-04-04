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

    def get_complex(self):
        return Complex(self.__re, self.__im)

    @property
    def re(self):
        return self.__re

    @re.setter
    def re(self, value):
        if self.__test_value(value):
            self.__re = value

    @re.deleter
    def re(self):
        del self.__re

    def __str__(self):  # вывод в print
        return f'{self.__re} {"+" if self.__im >= 0 else "-"} {abs(self.__im)}i'

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

    ###Функции сравнения __le, ge, lt, gt, eq, ne__ вызываются когда нужно проанализировать
    ###<=, >=, <, >, ==, != return bool

    ### setattr, getattr, getattribute, delattr

    # Этим методом можно запрещать создание новых атрибутов
    # def __setattr__(self, key, value):
    #     print('setattr', key, value)
    #     object.__setattr__(self, key, value)
    #
    # def __getattribute__(self, item):
    #     print('getattribute', item)
    #     return object.__getattribute__(self, item)
    #
    # def __getattr__(self, item):
    #     print('getattr', item)
    #     # return None
    #
    # def __delattr__(self, item):
    #     print('delattr', item)
    #     object.__delattr__(self, item)


def main():
    print('constructor c1')
    c1 = Complex(2, 3)
    print(c1.get_complex())
    print(c1.get_number())
    c1.re = 9
    print(c1.re)
    # print('constructor c3')
    # c2 = Complex(2, 4)
    # # print('c1 + c2')
    # # print(c1 + c2)
    # # print('c1 - c2')
    # # print(c1 - c2)
    # # print('c1 * c2')
    # # print(c1 * c2)
    # # print('c1 / c2')
    # # print(c1 / c2)
    # print(c1.__dict__)
    # print('get not exist attribute')
    # print(c1.a)
    # print('set not exist attribute')
    # c1.a = 10
    # print(c1.__dict__)
    # del c1.a
    # print(c1.__dict__)
    # del c1.__dict__['_Complex__re']
    # print(c1.__dict__)


if __name__ == '__main__':
    main()
