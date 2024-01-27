#



class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}

    def register_course(self, course, grade=None):
        self.courses[course] = grade
        print(f'Student {self.name} has successfully registered for the course "{course}".')

    def display_info(self):
        print(f"Student Information:\nStudent ID: {self.student_id}\nName: {self.name}")
        print("Registered Courses:")
        for course, grade in self.courses.items():
            if grade is not None:
                print(f'"{course}" - Grade: {grade}')
            else:
                print(f'"{course}" - Grade: Waiting for grade entry')

class Course:
    def __init__(self, course_code, title):
        self.course_code = course_code
        self.title = title


student1 = Student("12345", "Ali")


course1 = Course("CS101", "Introduction to Computer Science")
course2 = Course("MATH202", "Mathematics 2")


student1.register_course(course1.title)
student1.register_course(course2.title)


student1.display_info()
