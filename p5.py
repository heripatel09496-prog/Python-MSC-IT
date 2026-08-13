print("Student Rank Processing Engine")

num = int(input("Enter number of students: "))

students = []

for i in range(num):

    print("\nEnter details of student", i + 1)

    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")

    mark1 = float(input("Enter marks of Python: "))
    mark2 = float(input("Enter marks of MEARN Stack: "))
    mark3 = float(input("Enter marks of Cyber Security: "))
    mark4 = float(input("Enter marks of Data Analitics: "))
    mark5 = float(input("Enter marks of Matchine Learning :"))

    total = mark1 + mark2 + mark3 + mark4 + mark5
    percentage = total / 5

    # Grade
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

    # Dictionary
    student = {
        "roll": roll,
        "name": name,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)


# Sorting by percentage  highest first
for i in range(num):
    for j in range(i + 1, num):
        if students[i]["percentage"] < students[j]["percentage"]:
            temp = students[i]
            students[i] = students[j]
            students[j] = temp


print("\n STUDENT RANKING LIST ")

rank = 1

for i in range(num):

    if i == 0:
        rank = 1
    elif students[i]["percentage"] != students[i - 1]["percentage"]:
        rank = i + 1

    print("\nRank:", rank)
    print("Roll No:", students[i]["roll"])
    print("Name:", students[i]["name"])
    print("Total:", students[i]["total"])
    print("Percentage:", students[i]["percentage"])
    print("Grade:", students[i]["grade"])
