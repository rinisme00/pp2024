class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def input_marks(self, course_id, mark):
        self.marks[course_id] = mark

    def display_marks(self, course_id, course_name):
        mark = self.marks.get(course_id, "No marks have been input!")
        return f"{course_name} - {self.name}: {mark}"

    def __str__(self):
        return f"Student Name: {self.name}, Student ID: {self.student_id}, DoB: {self.dob}"


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def __str__(self):
        return f"Course Name: {self.course_name}, Course ID: {self.course_id}"


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
            course = Course(course_id, course_name)
            self.courses.append(course)

    def input_marks(self):
        for student in self.students:
            print(f"Enter marks for {student.name}: ")
            for course in self.courses:
                mark = float(input(f" {course.course_name}, ID: {course.course_id}: "))
                student.input_marks(course.course_id, mark)

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

    def main(self):
        student_nums = int(input("Enter the number of students: "))
        self.add_student(student_nums)

        course_nums = int(input("Enter the number of courses: "))
        self.add_course(course_nums)

        self.input_marks()

        while True:
            print("\nChoose an option: ")
            print("1. List courses")
            print("2. List students")
            print("3. Display students' marks for a course")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == '1':
                self.display_courses()
            elif choice == '2':
                self.display_students()
            elif choice == '3':
                self.display_marks()
            elif choice == '4':
                break
            else:
                print("Invalid choice!")


if __name__ == "__main__":
    school = School()
    school.main()
