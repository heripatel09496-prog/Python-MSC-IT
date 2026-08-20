from student import get_student_data
from ranking import get_student_rank
from report import get_student_report

print("Student Rank Processing Engine:")

    # Get student records
std_data = get_student_data()

    # Generate ranks
std_data = get_student_rank(std_data)

    # Display final result
get_student_report(std_data)

