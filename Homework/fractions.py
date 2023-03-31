class Fractions:

    # Инициализация идет с помощью сеттера
    def __init__(self, num, den):
        self.set_fractions(num, den)

    # классовый метод проверки типа числа
    @classmethod
    def __check_value(cls, num, den):
        if type(num) == int and type(den) == int and den != 0:
            return type(num), type(den)

    # Сеттер
    def set_fractions(self, num, den):
        if self.__check_value(num, den):
            self.__num = num
            self.__den = den
        else:
            raise ValueError('У числителя и знаменателя должен быть тип "int", и '
                             'знаменатель не может быть равен "0"')

    # Геттер
    def get_fractions(self):
        return f'{self.__num}/{self.__den}'

    @staticmethod
    # Нахождение общего наименьщего делителя
    def __get_fast_nod(a, b):
        if a < b:
            a, b = b, a
        while b:
            a, b = b, a % b
        return int(a)

    # Функция печати экземпляра класса
    def __str__(self):
        return f'{self.__num}/{self.__den}'

    # Функция сложения дробей
    def __add__(self, right):
        self.new_num = self.__num * right.__den + right.__num * self.__den
        self.new_den = self.__den * right.__den
        self.nod = self.__get_fast_nod(self.new_num, self.new_den)
        return Fractions(int(self.new_num / self.nod), int(self.new_den / self.nod))


    # Функция вычитания дробей
    def __sub__(self, right):
        pass

    # Функция умножения дробей
    def __mul__(self, right):
        pass

    # Функция деления дробей
    def __truediv__(self, right):
        pass


d1 = Fractions(1, 2)
d2 = Fractions(3, 9)
d1.set_fractions(5, 10)
d3 = Fractions(7, 8)
d4 = Fractions(12, 13)
# print(d1.get_fractions())
# print(d2.get_fractions())
# print(d1)
# print(d2)
# print()
print(d2 + d1)
print(d3 + d4)
