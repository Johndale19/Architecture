from models.student_model import Student

class StudentService:
    def __init__(self):
        self.students = []
        self.counter = 1

    def get_all_students(self):
        return self.students

    def add_student(self, name, course):
        student = Student(self.counter, name, course)
        self.students.append(student)
        self.counter += 1
        return student