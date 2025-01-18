import math

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
