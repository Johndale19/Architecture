from services.student_service import StudentService

class StudentController:
    def __init__(self, service: StudentService):
        self.service = service

    def get_students(self):
        return self.service.get_all_students()

    def add_student(self, name, course):
        return self.service.add_student(name, course)