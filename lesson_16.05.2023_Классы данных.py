# class Thing:
#     def __init__(self, name, weight, price, dims=None):
#         if dims is None:
#             dims = []
#         self.name = name
#         self.weight = weight
#         self.price = price
#         self.dims = dims
#
#     def __repr__(self):
#         return f'Thing: {self.__dict__}'
#
#
# t = Thing(name='Book', weight=100, price=1000)
# print(t)
# t.dims.append(10)
# print(t.dims)
# t1 = Thing('Book1', 1, 2)
# print(t1)


# from dataclasses import dataclass, field
#
#
# @dataclass
# class ThingData:
#     name: str
#     weight: int
#     price: int = 0
#     dims: list = field(default_factory=list)
#
#
# td = ThingData('Book', 100, 1000)
# print(td)
# td1 = ThingData('OOP book', 200, 1500)
# print(td == td1)
# td2 = ThingData('OOP book', 200, 1500)
# print(td1 == td2)
# td3 = ThingData('OOP book', 200)
# print(td3)


# class Vector
#     def __init__(self, x:float, y:float, calc_len:bool = True):
#         self.x = x
#         self.y = y
#         self.length = (x**2 + y**2)**0.5 if calc_len else 0


from dataclasses import dataclass, field, InitVar


# @dataclass(init=False)
# class Vector:
#     x: float = field(repr=False)
#     y: float = field(compare=False)
#     calc_len: InitVar[bool] = True
#     length: float = field(init=False, compare=False, default=0)
#
#     def __post_init__(self, calc_len: bool):
#         if calc_len:
#             self.length = (self.x ** 2 + self.y ** 2) ** 0.5
#
#
# v = Vector(1, 20)
# print(v)
# v2 = Vector(1, 30)
# print(v == v2)
# print(v.__dict__)


@dataclass
class Vector:
    x: float = 0
    y: float = 0
    calc_len: InitVar[bool] = True
    length: float = field(init=False, compare=False, default=0)

    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = (self.x ** 2 + self.y ** 2) ** 0.5


v = Vector()
print(v)
v2 = Vector()
print(v == v2)
print(v.__dict__)
v.x = 3
print(v)
