import pandas as pd


df = pd.DataFrame(
    {"Name": ["Aman", "Priya", "Rahul", "Sneha"], "Age": [20, 21, 22, 23]}
)

print(df.iloc[2])