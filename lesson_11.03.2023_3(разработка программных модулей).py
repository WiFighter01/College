class Person:
    def __init__(self, n: str, pn: str = '', ea: str = '',): #, a
        self.name = n
        self.phnum = pn
        self.eadr = ea
        # self.adr = Address()  # - композиция
        # self.adr = a - агрегация

    def pppass(self, ):
        pass


class Address:
    pass


class Student(Person):
    pass


class Professor(Person):
    pass


def main():
    print('Вызов конструктора')
    p = Person('Tom')  # На самом деле вызываются __new__ __init__
    print(p.name)


if __name__ == '__main__':
    main()

'''
Почитать:
https://metanit.com/python/tutorial/7.1.php
'''