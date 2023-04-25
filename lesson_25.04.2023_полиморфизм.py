class Figure:
    def __init__(self, x1, y1, x2, y2):
        print('init figure')
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def name(self):
        print(self.__class__)

    def getPerimeter(self):
        pass
        raise NotImplementedError('Метод должен быть переопределен '
                                  'в дочерних классах')


class Line(Figure):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        print('init line')

    def getPerimeter(self):
        print(((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5)


# class Triangle(Figure):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def getPerimeter(self):
#         print(self.a + self.b + self.c)


class Rectangle(Figure):
    def __init__(self, x1, y1, x2, y2, fill=False):
        super().__init__(x1, y1, x2, y2)
        print('init rectangle')
        self.fill = fill

    def getPerimeter(self):
        print(2 * (abs(self.x2 - self.x1)) + (abs(self.y2 - self.y1)))


line = Line(0, 0, 3, 4)
line.getPerimeter()
rect = Rectangle(1, 1, 5, 10)
rect.getPerimeter()

# f = []
# f.append(Line(5))
# f.append(Line(10))
# f.append(Triangle(3, 4, 5))
# f.append(Rectangle(2, 3))
# f.append(Rectangle(5, 8))
# for i in f:
#     i.getPerimeter()

# f = Figure()
# l = Line()
# f.name()
# l.name()
# print(isinstance(f, Figure))
# print(isinstance(l, Figure))
# print(isinstance(f, Line))
# print(isinstance(l, Line))
# print(isinstance(f, object))
# print(isinstance(l, object))
