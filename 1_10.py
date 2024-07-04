def get_student_details(n):
    students = []
    for i in range(n):
        print(f"\nEnter details of Student {i+1}: ")
        name = input("Enter student name: ")
        roll_no = input("Enter the roll no: ")
        marks = int(input("Enter the marks: "))
        student = {
            'name': name,
            'roll_no': roll_no,
            'marks': marks
        }
        students.append(student)
    return students

#function to find who is top
def find_top_student(students):
    top_student = max(students, key=lambda x: x['marks'])
    return top_student

n = int(input("Enter the number of students: "))
students = get_student_details(n)
print("Student Details:\n")
print(students)
top_student = find_top_student(students)
print("Details of Top Student:\n")
print(f"Name: {top_student['name']}")
print(f"Roll No: {top_student['roll_no']}")
print(f"Marks: {top_student['marks']}")
