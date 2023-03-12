class Person:
    def __init__(self, name: str, phone_number: str = '', email_address: str = ''):  # , a
        self.name = name
        self.phnum = phone_number
        self.eadr = email_address
        # self.adr = Address()  # - композиция
        # self.adr = a - агрегация

    def purchase_parking_pass(self):
        pass


class Address:
    def __init__(self, street='', city='', state='', postal_code='', country=''):
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
    def __int__(self, student_number, average_mark=''):
        self.student_number = student_number
        self.average_mark = average_mark

    def is_eligible_to_enroll(self):
        pass

    def get_seminars_taken(self):
        pass


class Professor(Person):
    def __init__(self, salary):
        self.salary = salary


def main():
    print('Вызов конструктора')
    Tom = Person('Tom')
    Bill = Person('Bill', '+79851190555', '123@gmail.com')  # На самом деле вызываются __new__ __init__
    Student1 = Student('Ivanov Ivan')
    print(Tom.name, Tom.phnum, Tom.eadr)
    print(Bill.name, Bill.phnum, Bill.eadr)
    print(Student1.name, Student1.phnum, Student1.eadr)


if __name__ == '__main__':
    main()
