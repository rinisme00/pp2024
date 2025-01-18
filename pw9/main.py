import tkinter as tk
from tkinter import messagebox
from utils.persistence import PersistenceThread
from compression import check_and_load_data
from domains.school import School

DATA_FILE = "data/students.dat"

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("600x400")

        # Initialize School instance
        self.school = check_and_load_data(DATA_FILE) or School()

        # Start background persistence thread
        self.persistence_thread = PersistenceThread(DATA_FILE, lambda: self.school, interval=5)
        self.persistence_thread.start()

        self.create_widgets()

    def create_widgets(self):
        # Student Input
        self.student_frame = tk.Frame(self.root, padx=10, pady=10)
        self.student_frame.pack(fill=tk.X)

        tk.Label(self.student_frame, text="Student Name:").grid(row=0, column=0, sticky=tk.W)
        self.student_name = tk.Entry(self.student_frame, width=20)
        self.student_name.grid(row=0, column=1)

        tk.Label(self.student_frame, text="Student ID:").grid(row=1, column=0, sticky=tk.W)
        self.student_id = tk.Entry(self.student_frame, width=20)
        self.student_id.grid(row=1, column=1)

        tk.Label(self.student_frame, text="Date of Birth:").grid(row=2, column=0, sticky=tk.W)
        self.student_dob = tk.Entry(self.student_frame, width=20)
        self.student_dob.grid(row=2, column=1)

        tk.Button(self.student_frame, text="Add Student", command=self.add_student).grid(row=3, column=0, columnspan=2, pady=10)

        # Course Input
        self.course_frame = tk.Frame(self.root, padx=10, pady=10)
        self.course_frame.pack(fill=tk.X)

        tk.Label(self.course_frame, text="Course Name:").grid(row=0, column=0, sticky=tk.W)
        self.course_name = tk.Entry(self.course_frame, width=20)
        self.course_name.grid(row=0, column=1)

        tk.Label(self.course_frame, text="Course ID:").grid(row=1, column=0, sticky=tk.W)
        self.course_id = tk.Entry(self.course_frame, width=20)
        self.course_id.grid(row=1, column=1)

        tk.Label(self.course_frame, text="Credits:").grid(row=2, column=0, sticky=tk.W)
        self.course_credits = tk.Entry(self.course_frame, width=20)
        self.course_credits.grid(row=2, column=1)

        tk.Button(self.course_frame, text="Add Course", command=self.add_course).grid(row=3, column=0, columnspan=2, pady=10)

        # Display
        self.display_frame = tk.Frame(self.root, padx=10, pady=10)
        self.display_frame.pack(fill=tk.BOTH, expand=True)

        tk.Button(self.display_frame, text="List Students", command=self.list_students).pack(fill=tk.X, pady=5)
        tk.Button(self.display_frame, text="List Courses", command=self.list_courses).pack(fill=tk.X, pady=5)
        tk.Button(self.display_frame, text="Exit", command=self.exit_program).pack(fill=tk.X, pady=5)

    def add_student(self):
        name = self.student_name.get()
        student_id = self.student_id.get()
        dob = self.student_dob.get()
        if name and student_id and dob:
            self.school.add_student([{"name": name, "student_id": student_id, "dob": dob}])
            messagebox.showinfo("Success", f"Student {name} added!")
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields!")

    def add_course(self):
        name = self.course_name.get()
        course_id = self.course_id.get()
        credits = self.course_credits.get()
        if name and course_id and credits.isdigit():
            self.school.add_course([{"name": name, "course_id": course_id, "credits": int(credits)}])
            messagebox.showinfo("Success", f"Course {name} added!")
        else:
            messagebox.showwarning("Input Error", "Please fill out all fields correctly!")

    def list_students(self):
        students = "\n".join(str(student) for student in self.school.students)
        messagebox.showinfo("Students", students if students else "No students available!")

    def list_courses(self):
        courses = "\n".join(str(course) for course in self.school.courses)
        messagebox.showinfo("Courses", courses if courses else "No courses available!")

    def exit_program(self):
        self.persistence_thread.stop()
        self.persistence_thread.join()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()



