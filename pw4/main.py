import curses
from domains.school import School
from input import input_students, input_courses, input_marks
from output import display_marks

def main(stdscr):
    school = School()

    students = input_students()
    school.add_student(students)

    courses = input_courses()
    school.add_course(courses)

    school.input_marks(input_marks)
    school.calculate_gpa_for_all_students()
    school.sort_students_by_gpa()

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Choose an option: ")
        stdscr.addstr(1, 0, "1. List courses")
        stdscr.addstr(2, 0, "2. List students")
        stdscr.addstr(3, 0, "3. Display students' marks for a course")
        stdscr.addstr(4, 0, "4. Exit")

        choice = stdscr.getch()

        if choice == ord('1'):
            school.display_courses()
        elif choice == ord('2'):
            school.display_students()
        elif choice == ord('3'):
            display_marks(school, stdscr)
        elif choice == ord('4'):
            break

if __name__ == "__main__":
    curses.wrapper(main)
