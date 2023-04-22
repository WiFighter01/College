class Fractions:
    __TYPE_T = (int,)

    # Инициализация идет с помощью сеттера
    def __init__(self, num, den):
        self.set_fractions(num, den)

    # классовый метод проверки типа числа
    @classmethod
    def __check_value(cls, num, den):
        if type(num) in cls.__TYPE_T and type(den) in cls.__TYPE_T and den != 0:
            return type(num), type(den)

    @classmethod
    def __check_num_value(cls, num):
        if type(num) in cls.__TYPE_T:
            return type(num)
        else:
            raise ValueError('Числитель должен быть типа int')

    @classmethod
    def __check_den_value(cls, den):
        if type(den) in cls.__TYPE_T and den != 0:
            return type(den)
        else:
            raise ValueError('Знаменатель должен быть типа int и не равен 0')

    # Свойство числителя
    @property
    def num(self):
        return self.__num

    # Сеттер числителя
    @num.setter
    def num(self, val):
        if self.__check_num_value(val):
            self.__num = val

    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, val):
        if self.__check_den_value(val):
            self.__den = val

    # Геттер
    def get_fractions(self):
        return f'{self.__num}/{self.__den}'

    # Сеттер
    def set_fractions(self, num, den):
        if self.__check_value(num, den):
            self.__num = num
            self.__den = den
        else:
            raise ValueError('У числителя и знаменателя должен быть тип "int", и '
                             'знаменатель не может быть равен "0"')

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
        self.new_num = self.__num * right.__den - right.__num * self.__den
        self.new_den = self.__den * right.__den
        self.nod = self.__get_fast_nod(self.new_num, self.new_den)
        return Fractions(int(self.new_num / self.nod), int(self.new_den / self.nod))

    # Функция умножения дробей
    def __mul__(self, right):
        self.new_num = self.__num * right.__num
        self.new_den = self.__den * right.__den
        self.nod = self.__get_fast_nod(self.new_num, self.new_den)
        return Fractions(int(self.new_num / self.nod), int(self.new_den / self.nod))

    # Функция деления дробей
    def __truediv__(self, right):
        self.new_num = self.__num * right.__den
        self.new_den = self.__den * right.__num
        self.nod = self.__get_fast_nod(self.new_num, self.new_den)
        return Fractions(int(self.new_num / self.nod), int(self.new_den / self.nod))

    # Функция сравнения <=:
    def __le__(self, right):
        self.num1 = self.__num * right.__den
        self.num2 = self.__den * right.__num
        if self.num1 <= self.num2:
            return True
        else:
            return False

    # Функция сравнения >=:
    def __ge__(self, right):
        self.num1 = self.__num * right.__den
        self.num2 = self.__den * right.__num
        if self.num1 >= self.num2:
            return True
        else:
            return False

    # Функция сравнения <:
    def __lt__(self, right):
        self.num1 = self.__num * right.__den
        self.num2 = self.__den * right.__num
        if self.num1 < self.num2:
            return True
        else:
            return False

    # Функция сравнения >:
    def __gt__(self, right):
        self.num1 = self.__num * right.__den
        self.num2 = self.__den * right.__num
        if self.num1 > self.num2:
            return True
        else:
            return False

    # Функция сравнения ==:
    def __eq__(self, right):
        self.num1 = self.__num * right.__den
        self.num2 = self.__den * right.__num
        if self.num1 == self.num2:
            return True
        else:
            return False

    # Функция сравнения =!=:
    def __ne__(self, right):
        self.num1 = self.__num * right.__den
        self.num2 = self.__den * right.__num
        if self.num1 != self.num2:
            return True
        else:
            return False



d1 = Fractions(1, 2)
d2 = Fractions(3, 9)
d1.set_fractions(5, 10)
d3 = Fractions(7, 8)
d4 = Fractions(12, 13)
d5 = Fractions(3, 9)
# print(d1.get_fractions())
# print(d2.get_fractions())
# print(d1)
# print(d2)
# print()
print('d2 + d1:')
print(d2 + d1)
print('d3 + d4:')
print(d3 + d4)
print('d1 - d2:')
print(d1 - d2)
print('d3 - d4:')
print(d3 - d4)
print('d2 * d1:')
print(d2 * d1)
print('d3 * d4:')
print(d3 * d4)
print('d2 / d1:')
print(d2 / d1)
print('d3 / d4:')
print(d3 / d4)
print('d1 <= d2:')
print(d1 <= d2)
print('d1 >= d2:')
print(d1 >= d2)
print('d1 < d2:')
print(d1 < d2)
print('d1 > d2:')
print(d1 > d2)
print('d2 == d5:')
print(d2 == d5)
print('d2 != d5:')
print(d1 != d2)
