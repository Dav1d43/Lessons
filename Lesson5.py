class Mixin:
    def print_attributes(self):
        for attr, value in self.__dict__.items():
            print(f"{attr}: {value}")


class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name} {self.surname}, {self.age} years old"


class Student(Person):
    def __init__(self, name, surname, age, university):
        super().__init__(name, surname, age)
        self.university = university

    def __str__(self):
        return f"{self.name} {self.surname}, {self.age} years old, University: {self.university}"


person = Person(name="Donald", surname="Trump", age=60)
print(person)

student = Student(name="Joe", surname="biden", age=55, university="Georgian University")
print(student)

person.print_attributes()
student.print_attributes()
