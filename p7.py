
from datetime import datetime


class Course:
    def __init__(self, code, day, start_time, end_time):
        self.code = code.upper()
        self.day = day.title()
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return (
            f"{self.code} | {self.day} | "
            f"{self.start_time} - {self.end_time}"
        )


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}"


def convert_time(time_text):
    return datetime.strptime(time_text, "%H:%M").time()


def get_time(prompt):
    while True:
        try:
            time_text = input(prompt).strip()
            return convert_time(time_text)
        except ValueError:
            print("Invalid time! Enter time in HH:MM format, e.g. 09:30.")


def get_course(student):
    while True:
        code = input("Enter course code: ").strip()

        if code:
            break

        print("Course code cannot be empty.")

    valid_days = [
        "Monday", "Tuesday", "Wednesday", "Thursday",
        "Friday", "Saturday", "Sunday"
    ]

    while True:
        day = input("Enter day: ").strip().title()

        if day in valid_days:
            break

        print("Invalid day! Enter a valid day of the week.")

    while True:
        start_time = get_time("Enter start time (HH:MM): ")
        end_time = get_time("Enter end time (HH:MM): ")

        if start_time < end_time:
            break

        print("End time must be later than start time.")

    course = Course(code, day, start_time, end_time)
    student.add_course(course)


def is_conflict(course1, course2):
    if course1.day != course2.day:
        return False

    return (
        course1.start_time < course2.end_time
        and course2.start_time < course1.end_time
    )


def display_timetable(student):
    print("\nRegistered Timetable")
    
    print(student)

    for course in student.courses:
        print(course)

    print("Total registered courses:", len(student.courses))


def check_conflicts(student):
    conflicts = []

    for i in range(len(student.courses)):
        for j in range(i + 1, len(student.courses)):
            course1 = student.courses[i]
            course2 = student.courses[j]

            if is_conflict(course1, course2):
                conflicts.append((course1, course2))

    print("\nConflict Report")
    
    print(student)

    if conflicts:
        print("Timetable conflicts found:")

        for course1, course2 in conflicts:
            print(f"\n{course1.code} conflicts with {course2.code}")
            print(course1)
            print(course2)
    else:
        print("No timetable conflicts found.")
        display_timetable(student)

    print("\nTotal registered courses:", len(student.courses))


def main():
    print("COURSE REGISTRATION CONFLICT DETECTOR")
    

    while True:
        try:
            number_of_students = int(input("Enter number of students: "))

            if number_of_students > 0:
                break

            print("Number of students must be greater than zero.")

        except ValueError:
            print("Invalid input! Enter a whole number.")

    students = []

    for i in range(number_of_students):
        print(f"\nEnter details for Student {i + 1}")

        while True:
            student_id = input("Enter student ID: ").strip()

            if student_id:
                break

            print("Student ID cannot be empty.")

        while True:
            name = input("Enter student name: ").strip()

            if name:
                break

            print("Student name cannot be empty.")

        student = Student(student_id, name)

        while True:
            try:
                number_of_courses = int(
                    input("Enter number of registered courses: ")
                )

                if number_of_courses >= 0:
                    break

                print("Course count cannot be negative.")

            except ValueError:
                print("Invalid input! Enter a whole number.")

        for j in range(number_of_courses):
            print(f"\nCourse {j + 1}")
            get_course(student)

        students.append(student)

    print("\n\nFINAL RESULTS")
    

    for student in students:
        check_conflicts(student)
    


if __name__ == "__main__":
    main()
