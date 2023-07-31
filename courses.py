class Course:
    def __init__(self, course_id, teacher_name, max_students, standard_charge):
        self.course_id = course_id
        self.teacher_name = teacher_name
        self.max_students = max_students
        self.standard_charge = standard_charge
        self.students_enrolled = []
        self.income = 0
        self.running_cost = 0

    def enroll_student(self, student):
        if len(self.students_enrolled) < self.max_students:
            self.students_enrolled.append(student)
            self.income += self.standard_charge
            return True
        else:
            return False

    def calculate_running_cost(self):
        pass  # This method will be overridden in the subclasses.

    def calculate_profit(self):
        return self.income - self.running_cost


class CookingCourse(Course):
    def __init__(self, course_id, teacher_name):
        super().__init__(course_id, teacher_name, max_students=10, standard_charge=0)

    def calculate_running_cost(self):
        self.running_cost = 1000


class ItalianCooking(CookingCourse):
    def __init__(self):
        super().__init__(course_id="001", teacher_name="Italian Cooking Teacher")
        self.standard_charge = 500

    def calculate_running_cost(self):
        super().calculate_running_cost()


class Seafood(CookingCourse):
    def __init__(self):
        super().__init__(course_id="002", teacher_name="Seafood Cooking Teacher")
        self.standard_charge = 700

    def calculate_running_cost(self):
        super().calculate_running_cost()


class SewingCourse(Course):
    def __init__(self, course_id, teacher_name):
        super().__init__(course_id, teacher_name, max_students=10, standard_charge=300)

    def calculate_running_cost(self):
        self.running_cost = 100 * len(self.students_enrolled)


class WritingCourse(Course):
    def __init__(self, course_id, teacher_name):
        super().__init__(course_id, teacher_name, max_students=15, standard_charge=200)

    def calculate_running_cost(self):
        if self.course_id == "003":
            self.running_cost = 800
        elif self.course_id == "004":
            self.running_cost = 600


class CreativeWriting(WritingCourse):
    def __init__(self):
        super().__init__(course_id="003", teacher_name="Creative Writing Teacher")
        self.standard_charge = 200

    def calculate_running_cost(self):
        super().calculate_running_cost()


class BusinessWriting(WritingCourse):
    def __init__(self):
        super().__init__(course_id="004", teacher_name="Business Writing Teacher")
        self.standard_charge = 200

    def calculate_running_cost(self):
        super().calculate_running_cost()


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name


def main():
    # Creating instances of the courses
    italian_cooking = ItalianCooking()
    seafood_cooking = Seafood()
    sewing_course = SewingCourse(course_id="005", teacher_name="Sewing Teacher")
    creative_writing = CreativeWriting()
    business_writing = BusinessWriting()

    # Creating students
    students = [
        Student("001", "Alice"),
        Student("002", "Bob"),
        Student("003", "Charlie"),
        Student("004", "David"),
        Student("005", "Eve"),
        Student("006", "Frank"),
        Student("007", "Grace"),
        Student("008", "Hannah"),
        Student("009", "Isaac"),
        Student("010", "Jack"),
        Student("011", "Katie"),
    ]

    # Enrolling students in courses
    courses = [italian_cooking, seafood_cooking, sewing_course, creative_writing, business_writing]
    for course in courses:
        for student in students:
            if course.enroll_student(student):
                break

    # Calculating running costs and profits for each course
    for course in courses:
        course.calculate_running_cost()
        print(f"Course ID: {course.course_id}, Teacher: {course.teacher_name}")
        print(f"Enrolled Students: {len(course.students_enrolled)}")
        print(f"Running Cost: ${course.running_cost}")
        print(f"Income: ${course.income}")
        print(f"Profit: ${course.calculate_profit()}")
        print("----------------------------")


if __name__ == "__main__":
    main()
