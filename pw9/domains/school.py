from domains.student import Student
from domains.course import Course

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, students):
        self.students.extend(students)

    def add_course(self, courses):
        self.courses.extend(courses)

    def input_marks(self, input_func):
        for student in self.students:
            input_func(student, self.courses)

    def display_courses(self):
        print("\nCourses:")
        for course in self.courses:
            print(course)

    def display_students(self):
        print("\nStudents:")
        for student in self.students:
            print(student)

    def calculate_gpa_for_all_students(self):
        for student in self.students:
            student.calculate_gpa()

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda s: s.gpa if s.gpa else 0, reverse=True)
