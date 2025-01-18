class Course:
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits

    def __str__(self):
        return f"Course Name: {self.course_name}, Course ID: {self.course_id}, Credits: {self.credits}"
