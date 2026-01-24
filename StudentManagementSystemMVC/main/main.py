from controllers.student_controller import StudentController
from services.student_service import StudentService

def main():
    service = StudentService()
    controller = StudentController(service)

    controller.add_student("Alice", "Computer Science")
    controller.add_student("Bob", "Information Technology")

    students = controller.get_students()
    for s in students:
        print(f"{s.student_id}: {s.name} - {s.course}")

if __name__ == "__main__":
    main()