def report_decorator(func):
    def wrapper(*args, **kwargs):
        print("\n" + "=" * 45)
        print("      STUDENT REPORT CARD")
        print("=" * 45)
        func(*args, **kwargs)
        print("=" * 45)
        print("Report Generated Successfully!")
        print("=" * 45)
    return wrapper


class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):

    school = "MIT ADT University"

    def __init__(self, roll, name, marks):
        super().__init__(name)
        self.roll = roll
        self.__marks = marks

    def calculate_average(self):
        return sum(self.__marks.values()) / len(self.__marks)

    def calculate_grade(self):
        avg = self.calculate_average()

        if avg >= 90:
            return "A+"
        elif avg >= 80:
            return "A"
        elif avg >= 70:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 50:
            return "D"
        else:
            return "Fail"

    @report_decorator
    def display_report(self):
        print(f"School : {Student.school}")
        print(f"Roll No: {self.roll}")
        print(f"Name   : {self.name}")

        print("\nSubject Marks")

        for subject, mark in self.__marks.items():
            print(f"{subject:<15}: {mark}")

        print("\nAverage :", round(self.calculate_average(), 2))
        print("Grade   :", self.calculate_grade())

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

    @staticmethod
    def pass_marks():
        return 40


try:
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")

    n = int(input("How many subjects? "))

    marks = {}

    for i in range(n):
        subject = input(f"\nEnter Subject {i+1} Name: ")
        score = int(input(f"Enter Marks in {subject}: "))

        if score < 0 or score > 100:
            raise ValueError("Marks should be between 0 and 100.")

        marks[subject] = score

    student = Student(roll, name, marks)

    student.display_report()

    print("\nPass Marks:", Student.pass_marks())

except ValueError as e:
    print("Error:", e)

except Exception as e:
    print("Unexpected Error:", e)
