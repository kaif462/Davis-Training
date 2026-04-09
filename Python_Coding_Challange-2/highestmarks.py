# 1. Take input to create the dictionary
n = int(input("Enter number of students: "))
student_marks = {}

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    marks = int(input(f"Enter marks for {name}: "))
    student_marks[name] = marks

# 2. Find the student with the highest marks
# key=student_marks.get tells max() to compare the values (marks) not the keys (names)
top_student = max(student_marks, key=student_marks.get)
highest_marks = student_marks[top_student]

print(f"The student with the highest marks is {top_student} with {highest_marks} marks.")
