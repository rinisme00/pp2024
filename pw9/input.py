from domains.student import Student
from domains.course import Course
import json

def input_students():
    students = []
    student_nums = int(input("Enter the number of students: "))
    for _ in range(student_nums):
        name = input("Enter student's name: ")
        student_id = input("Enter student's ID: ")
        dob = input("Enter student's date of birth: ")
        students.append(Student(student_id, name, dob))
    with open("students.txt", "w") as file:
        student_data = [{"id": s.student_id, "name": s.name, "dob": s.dob} for s in students]
        json.dump(student_data, file)
    return students

def input_courses():
    courses = []
    course_nums = int(input("Enter the number of courses: "))
    for _ in range(course_nums):
        course_name = input("Enter course name: ")
        course_id = input("Enter course ID: ")
        credits = int(input(f"Enter number of credits for {course_name}: "))
        courses.append(Course(course_id, course_name, credits))
    with open("courses.txt", "w") as file:
        course_data = [{"id": c.course_id, "name": c.course_name, "credits": c.credits} for c in courses]
        json.dump(course_data, file)
    return courses

def input_marks(student, courses):
    print(f"Enter marks for {student.name}: ")
    marks = []
    for course in courses:
        mark = float(input(f" {course.course_name}, ID: {course.course_id}: "))
        student.input_marks(course.course_id, mark, course.credits)
        marks.append({
            "student_id": student.student_id,
            "course_id": course.course_id,
            "mark": mark
        })
    with open("marks.txt", "a") as file:
        json.dump(marks, file)
        file.write("\n")

