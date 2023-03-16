class Person:
    def __init__(self, name: str, phone_number: str = '', email_address: str = ''):  # , a
        self.name = name
        self.phnum = phone_number
        self.eadr = email_address
        self.adr = Address()  # - композиция
        # self.adr = a - агрегация. Еще не проходили

    def purchase_parking_pass(self):
        pass


class Address:
    def __init__(self, street: str = '', city: str = '', state: str = '', postal_code: str = '', country: str = ''):
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country

    def validate(self):
        pass

    def output_as_label(self):
        pass


class Student(Person):
    def __init__(self, student_number: int = None, average_mark: int = None):
        self.student_number = student_number
        self.average_mark = average_mark

    def is_eligible_to_enroll(self):
        pass

    def get_seminars_taken(self):
        pass


class Professor(Person):
    def __init__(self, salary: float = None):
        self.salary = salary


def main():
    print('Вызов конструктора')
    tom = Person('Tom')
    bill = Person('Bill', '+79851190555', '123@gmail.com')  # На самом деле вызываются __new__ __init__
    student1 = Student(777, 5)
    student1.name = 'Ivan'  # Можем создать атрибут из родительского класса
    student1.phnum = 880055545  # Можем создать атрибут из родительского класса
    professor1 = Professor(50000)
    adr1 = Address('Lenina', 'Moscow', 'Moscow area', '117152', 'RU')
    p = Person('Dima')
    p.adr = adr1
    print(tom.name, tom.phnum, tom.eadr)
    print(bill.name, bill.phnum, bill.eadr)
    print(student1.name, student1.phnum, student1.student_number, student1.average_mark)
    print(professor1.salary)
    print(adr1.city, adr1.state, adr1.street)
    print(p.name, p.adr.city, p.adr.country)


if __name__ == '__main__':
    main()
