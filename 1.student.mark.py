# Input number of students
def input_number_of_students():
    return int(input("Enter the number of students: "))

# Input students' info
def input_students_info(students_number):
    students = []
    for info in range (students_number):
        name = input("Enter student's name: ")
        id = input("Enter student's ID: ")
        dob = input("Enter student's date of birth: ")
        students.append({
            'id': id,
            'name': name,
            'dob': dob,
            'marks': {}
        })
    return students

# Input number of courses
def input_number_of_courses():
    return int(input("Enter the number of courses: "))

# Input courses' info
def input_courses_info(courses_number):
    courses = []
    for info in range (courses_number):
        course_id = input("Enter course ID: ")
        course_name = input("Enter course name: ")
        courses.append({
            'id': course_id,
            'name': course_name
        })
    return courses

# Input marks
def input_marks(students, courses):
    for student in students:
        print(f"Enter marks for {student['name']}: ")
        for course in courses:
            mark = float(input(f" {course['name']}, ID: {course['id']}: "))
            student['marks'][course['id']] = mark

# List courses
def list_courses(courses):
    print("\nCourses:")
    for course in courses:
        print(f"Course ID: {course['id']}, Course Name: {course['name']}")

# List students
def list_students(students):
    print("\nStudents:")
    for student in students:
        print(f"Student ID: {student['id']}, Student Name: {student['name']}, DoB: {student['dob']}")

# Show marks of a student
def show_marks(students, courses):
    id = input("Enter the student ID to view marks: ")
    course_id = input("Enter the course ID to view marks: ")

    #Find student by ID
    student = next((student for student in students if student['id'] == id), None)
    if student:
        course = next((course for course in courses if course['id'] == course_id), None)
        if course:
            mark = student['marks'].get(course_id, "No marks entered")
            print(f"{course['name']} - {student['name']}: {mark}")
        else:
            print("Course not found!")
    else:
        print("Student not found!")

def main():
    students_number = input_number_of_students()
    students = input_students_info(students_number)

    courses_number = input_number_of_courses()
    courses = input_courses_info(courses_number)

    input_marks(students, courses)

    while True:
        print("\nChoose an option: ")
        print("1. List courses")
        print("2. List students")
        print("3. Show students' marks for a course")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            list_courses(courses)
        elif choice == '2':
            list_students(students)
        elif choice == '3':
            show_marks(students, courses)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
        