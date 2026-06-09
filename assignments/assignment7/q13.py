import pandas as pd


df = pd.DataFrame(
    {"Name": ["Aman", "Priya", "Rahul", "Sneha"], "Marks": [85, 92, 76, 88]}
)

filtered_df = df[df["Marks"] >= 85]
print(filtered_df)