name = input("Enter name: ")
cls = input("Enter class: ")

m1 = float(input("Enter mark 1: "))
m2 = float(input("Enter mark 2: "))
m3 = float(input("Enter mark 3: "))
m4 = float(input("Enter mark 4: "))
m5 = float(input("Enter mark 5: "))

total = m1 + m2 + m3 + m4 + m5
per = total / 5

if per >= 60:
    grade = "A"
elif per >= 50:
    grade = "B"
elif per >= 40:
    grade = "C"
elif per >= 33:
    grade = "D"
else:
    grade = "F"

print("Name:", name)
print("Class:", cls)
print("Total:", total)
print("Percentage:", per)
print("Grade:", grade)