def get_student_rank(student_data):

    # Sorting students by total marks
    for i in range(len(student_data)):
        for j in range(i + 1, len(student_data)):

            if student_data[i]["total"] < student_data[j]["total"]:
                temp = student_data[i]
                student_data[i] = student_data[j]
                student_data[j] = temp

    # ranks of student
    for i in range(len(student_data)):

        if i == 0:
            student_data[i]["rank"] = 1

        elif student_data[i]["total"] == student_data[i - 1]["total"]:
            student_data[i]["rank"] = student_data[i - 1]["rank"]

        else:
            student_data[i]["rank"] = i + 1

    return student_data
