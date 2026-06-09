import pandas as pd


employees = pd.DataFrame(
    {
        "EmpID": [1, 2, 3, 4],
        "Dept": ["HR", "IT", "IT", "Sales"],
        "Name": ["Aman", "Priya", "Rahul", "Sneha"],
    }
)

targets = pd.DataFrame(
    {
        "EmpID": [1, 2, 3, 5],
        "Dept": ["HR", "IT", "IT", "Finance"],
        "Target": [80, 90, 88, 75],
    }
)

merged = pd.merge(employees, targets, on=["EmpID", "Dept"], how="inner")

print("Employees DataFrame:")
print(employees)
print()
print("Targets DataFrame:")
print(targets)
print()
print("Merged on multiple keys (EmpID and Dept):")
print(merged)