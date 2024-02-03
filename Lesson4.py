class Student:

    def __init__(self, name, grade, age):
        self.name = name
        self._grade = grade
        self.age = age

    def __str__(self):
        return Name: {self.name}, Age: {self.age}, Grade: {self._grade}"

    @property
    def is_passing(self):
        return self._grade > 60

    def grade(self, amount):
        self._grade += amount


student1 = Student(name="Selena Gomez", grade=70, age=20)
print(student1)
print({student1.is_passing})
student1.grade(5)



