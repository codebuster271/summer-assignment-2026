student_name = input("Enter the name: ")
student_class = input("Enter class: ")

list_subjects = ['English', 'Math', 'Hindi', 'Science', 'Computer Science']
marks = []

for subjects in list_subjects:
    mark = float(input(f"Enter marks of {subjects}: "))
    marks.append(mark)

total_marks = sum(marks)
percentage = (total_marks/(len(list_subjects) * 100)) * 100

# Determine grade based on percentage
if percentage >= 60:
    grade = 'A'
elif percentage >= 50:
    grade = 'B'
elif percentage >= 40:
    grade = 'C'
elif percentage >= 33:
    grade = 'D'
else:
    grade = 'Fail'

print(f"\nStudent name: {student_name}")
print(f"Student class: {student_class}")
print(f"Student percentage: {percentage}")
print(f"Student grade: {grade}")
