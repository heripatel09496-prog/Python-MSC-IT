def get_student_data():
    student_data = []

    num = int(input("Enter number of students: "))

    for i in range(num):
        print("\nEnter details of student", i + 1)

        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")

        mark1 = float(input("Enter marks of Python: "))
        mark2 = float(input("Enter marks of MEARN Stack: "))
        mark3 = float(input("Enter marks of Cyber Security: "))
        mark4 = float(input("Enter marks of Data Analytics: "))
        mark5 = float(input("Enter marks of Machine Learning: "))

        # total  marks
        total = mark1 + mark2 + mark3 + mark4 + mark5

        # percentage
        percentage = total / 5

        # grade
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        student = {
            "roll": roll,
            "name": name,
            "total": total,
            "percentage": percentage,
            "grade": grade
        }

        student_data.append(student)

    return student_data
