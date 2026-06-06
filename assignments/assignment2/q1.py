name = input("Enter name: ")
cls = input("Enter class: ")

sub1 = float(input("Enter subject 1 mark: "))
sub2 = float(input("Enter subject 2 mark: "))
sub3 = float(input("Enter subject 3 mark: "))
sub4 = float(input("Enter subject 4 mark: "))
sub5 = float(input("Enter subject 5 mark: "))

total = sub1 + sub2 + sub3 + sub4 + sub5
per = total / 5

print("Name:", name)
print("Class:", cls)
print("Total:", total)
print("Percentage:", per)