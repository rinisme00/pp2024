def display_marks(school, stdscr):
    stdscr.addstr("Enter the student ID to view marks: ")
    student_id = stdscr.getstr().decode()
    stdscr.addstr("Enter the course ID to view marks: ")
    course_id = stdscr.getstr().decode()

    student = next((s for s in school.students if s.student_id == student_id), None)
    if student:
        course = next((c for c in school.courses if c.course_id == course_id), None)
        if course:
            stdscr.addstr(f"\n{student.display_marks(course.course_id, course.course_name)}\n")
        else:
            stdscr.addstr("Course not found!\n")
    else:
        stdscr.addstr("Student not found!\n")
    stdscr.getch()
