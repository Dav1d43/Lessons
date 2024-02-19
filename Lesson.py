class Person:
    def __init__(self, student_id, name):
        self._student_id = student_id
        self._name = name

    @property
    def student_id(self):
        return self._student_id

    @property
    def name(self):
        return self._name

    def display_details(self):
        print(f"Student ID: {self._student_id}\nName: {self._name}")


class GradeMixin:
    def __init__(self):
        self._grades = {}

    def add_grade(self, subject, grade):
        if 0 <= grade <= 100:
            self._grades[subject] = grade
            print(f"Grade {grade} added for {subject}")
        else:
            print("Invalid grade. Please enter a grade between 0 and 100.")

    def average_grade(self):
        if self._grades:
            return sum(self._grades.values()) / len(self._grades)
        else:
            return 0


class Student(Person, GradeMixin):
    def __init__(self, student_id, name):
        super().__init__(student_id, name)
        GradeMixin.__init__(self)


class StudentManagementSystem:
    def __init__(self):
        self._students = []

    def add_student(self, student):
        self._students.append(student)
        print(f"Student {student.name} added to the system.")

    def show_student_details(self, student_id):
        for student in self._students:
            if student.student_id == student_id:
                student.display_details()
                return
        print(f"Student with ID {student_id} not found.")

    def show_student_average_grade(self, student_id):
        for student in self._students:
            if student.student_id == student_id:
                avg_grade = student.average_grade()
                print(f"Average Grade for {student.name}: {avg_grade}")
                return
        print(f"Student with ID {student_id} not found.")


# Example usage:
student1 = Student(student_id="S001", name="Selena gomez")
student2 = Student(student_id="S002", name="Will Smith")

system = StudentManagementSystem()

system.add_student(student1)
system.add_student(student2)

student1.add_grade("Math", 86)
student1.add_grade("English", 89)

student2.add_grade("Math", 94)
student2.add_grade("English", 77)

system.show_student_details("S001")
system.show_student_average_grade("S001")

system.show_student_details("S003")
