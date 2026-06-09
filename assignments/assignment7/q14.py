import pandas as pd


df = pd.DataFrame(
    {"Name": ["Aman", "Priya", "Rahul"], "Age": [20, 21, 22]}
)

new_row = pd.DataFrame([["Sneha", 23]], columns=["Name", "Age"])
top_part = df.iloc[:1]
bottom_part = df.iloc[1:]
updated_df = pd.concat([top_part, new_row, bottom_part], ignore_index=True)

print(updated_df)