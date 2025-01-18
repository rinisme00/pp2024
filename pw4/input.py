from domains.student import Student
from domains.course import Course

def input_students():
    students = []
    student_nums = int(input("Enter the number of students: "))
    for _ in range(student_nums):
        name = input("Enter student's name: ")
        student_id = input("Enter student's ID: ")
        dob = input("Enter student's date of birth: ")
        students.append(Student(student_id, name, dob))
    return students

def input_courses():
    courses = []
    course_nums = int(input("Enter the number of courses: "))
    for _ in range(course_nums):
        course_name = input("Enter course name: ")
        course_id = input("Enter course ID: ")
        credits = int(input(f"Enter number of credits for {course_name}: "))
        courses.append(Course(course_id, course_name, credits))
    return courses

def input_marks(student, courses):
    print(f"Enter marks for {student.name}: ")
    for course in courses:
        mark = float(input(f" {course.course_name}, ID: {course.course_id}: "))
        student.input_marks(course.course_id, mark, course.credits)
