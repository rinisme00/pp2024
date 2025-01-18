import os
import curses
from compression import compress_files, check_and_load_data
from input import input_students, input_courses, input_marks
from output import display_marks
from domains.school import School

def main_program_logic(school, stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Choose an option: ")
        stdscr.addstr(1, 0, "1. List courses")
        stdscr.addstr(2, 0, "2. List students")
        stdscr.addstr(3, 0, "3. Display students' marks for a course")
        stdscr.addstr(4, 0, "4. Exit")

        choice = stdscr.getch()

        if choice == ord('1'):
            stdscr.clear()
            stdscr.addstr(0, 0, "Courses:")
            for course in school.courses:
                stdscr.addstr(f"\n{course}")
            stdscr.addstr("\nPress any key to return to menu...")
            stdscr.getch()
        elif choice == ord('2'):
            stdscr.clear()
            stdscr.addstr(0, 0, "Students:")
            for student in school.students:
                stdscr.addstr(f"\n{student}")
            stdscr.addstr("\nPress any key to return to menu...")
            stdscr.getch()
        elif choice == ord('3'):
            display_marks(school, stdscr)
        elif choice == ord('4'):
            break
        else:
            stdscr.addstr(6, 0, "Invalid choice!!!!")
            stdscr.getch()

def main(stdscr):
    check_and_load_data()

    school = School()

    students = input_students()
    school.add_student(students)

    courses = input_courses()
    school.add_course(courses)

    school.input_marks(input_marks)

    school.calculate_gpa_for_all_students()
    school.sort_students_by_gpa()

    main_program_logic(school, stdscr)

    files_to_compress = ["students.txt", "courses.txt", "marks.txt"]
    compress_files("students.dat", files_to_compress)

if __name__ == "__main__":
    curses.wrapper(main)
