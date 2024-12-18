import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = None

    def input_marks(self, course_id, mark, credits):
        rounded_mark = math.floor(mark * 10) / 10 
        self.marks[course_id] = {'mark': rounded_mark, 'credits': credits}

    def display_marks(self, course_id, course_name):
        mark_info = self.marks.get(course_id, None)
        if mark_info:
            return f"{course_name} - {self.name}: {mark_info['mark']} (Credits: {mark_info['credits']})"
        else:
            return f"No marks entered for {course_name}"

    def calculate_gpa(self):
        total_weighted_marks = sum(m['mark'] * m['credits'] for m in self.marks.values())
        total_credits = sum(m['credits'] for m in self.marks.values())
        if total_credits > 0:
            self.gpa = total_weighted_marks / total_credits
        else:
            self.gpa = 0
        return self.gpa

    def __str__(self):
        return f"Student Name: {self.name}, Student ID: {self.student_id}, DoB: {self.dob}, GPA: {self.gpa if self.gpa else 'Not Calculated'}"


class Course:
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits

    def __str__(self):
        return f"Course Name: {self.course_name}, Course ID: {self.course_id}, Credits: {self.credits}"


class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, student_nums):
        for _ in range(student_nums):
            name = input("Enter student's name: ")
            student_id = input("Enter student's ID: ")
            dob = input("Enter student's date of birth: ")
            student = Student(student_id, name, dob)
            self.students.append(student)

    def add_course(self, course_nums):
        for _ in range(course_nums):
            course_name = input("Enter course name: ")
            course_id = input("Enter course ID: ")
            credits = int(input(f"Enter number of credits for {course_name}: "))
            course = Course(course_id, course_name, credits)
            self.courses.append(course)

    def input_marks(self):
        for student in self.students:
            print(f"Enter marks for {student.name}: ")
            for course in self.courses:
                mark = float(input(f" {course.course_name}, ID: {course.course_id}: "))
                student.input_marks(course.course_id, mark, course.credits)

    def display_courses(self):
        print("\nCourses:")
        for course in self.courses:
            print(course)

    def display_students(self):
        print("\nStudents:")
        for student in self.students:
            print(student)

    def display_marks(self):
        student_id = input("Enter the student ID to view marks: ")
        course_id = input("Enter the course ID to view marks: ")

        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            course = next((c for c in self.courses if c.course_id == course_id), None)
            if course:
                print(student.display_marks(course.course_id, course.course_name))
            else:
                print("Course not found!")
        else:
            print("Student not found!")

    def calculate_gpa_for_all_students(self):
        for student in self.students:
            student.calculate_gpa()

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda s: s.gpa if s.gpa else 0, reverse=True)

    def main(self, stdscr):
        student_nums = int(input("Enter the number of students: "))
        self.add_student(student_nums)

        course_nums = int(input("Enter the number of courses: "))
        self.add_course(course_nums)

        self.input_marks()
        self.calculate_gpa_for_all_students()
        self.sort_students_by_gpa()

        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "Choose an option: ")
            stdscr.addstr(1, 0, "1. List courses")
            stdscr.addstr(2, 0, "2. List students")
            stdscr.addstr(3, 0, "3. Display students' marks for a course")
            stdscr.addstr(4, 0, "4. Exit")

            choice = stdscr.getch()

            if choice == ord('1'):
                self.display_courses()
            elif choice == ord('2'):
                self.display_students()
            elif choice == ord('3'):
                self.display_marks()
            elif choice == ord('4'):
                break
            else:
                stdscr.addstr(6, 0, "Invalid choice!!!!")
                stdscr.getch()


if __name__ == "__main__":
    school = School()
    curses.wrapper(school.main)
