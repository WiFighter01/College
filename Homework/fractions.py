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

    # Нахождение общего наименьщего делителя
    # Пока не придумал зачем мне это здесь
    # def getFastNOD(a, b):
    #     if a < b:
    #         a, b = b, a
    #     while b:
    #         a, b = b, a % b
    #     return a

    # Функция печати экземпляра класса
    def __str__(self):
        return f'{self.__num}/{self.__den}'

    # Функция сложения дробей
    def __add__(self, right):
        pass

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
print(d1.get_fractions())
print(d2.get_fractions())
print(d1)
print(d2)
