def get_student_report(student_data):

    print("STUDENT RANKING LIST")
    print("Rank\tRoll No\tName\t\tTotal\tPercentage\tGrade")
    for student in student_data:

        print(
            student["rank"],
            "\t",
            student["roll"],
            "\t",
            student["name"],
            "\t\t",
            student["total"],
            "\t",
            student["percentage"],
            "\t\t",
            student["grade"]
        )
