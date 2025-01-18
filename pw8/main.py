import curses
from utils.persistence import PersistenceThread
from compression import check_and_load_data
from input import input_students, input_courses, input_marks
from output import display_marks
from domains.school import School

DATA_FILE = "data/students.dat"

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
    loaded_data = check_and_load_data(DATA_FILE)
    school = loaded_data if loaded_data else School()

    if not loaded_data:
        students = input_students()
        school.add_student(students)

        courses = input_courses()
        school.add_course(courses)

        school.input_marks(input_marks)
        school.calculate_gpa_for_all_students()
        school.sort_students_by_gpa()

    persistence_thread = PersistenceThread(DATA_FILE, lambda: school, interval=5)
    persistence_thread.start()

    try:
        main_program_logic(school, stdscr)
    finally:
        persistence_thread.stop()
        persistence_thread.join()

if __name__ == "__main__":
    curses.wrapper(main)


