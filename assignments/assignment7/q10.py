import pandas as pd


df = pd.DataFrame(
    {"Name": ["Aman", "Priya", "Rahul", "Sneha"], "Marks": [85, 92, 76, 88]}
)

selected_rows = df[df["Marks"] > 80]
print(selected_rows)