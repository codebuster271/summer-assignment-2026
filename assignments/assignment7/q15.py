import pandas as pd


df = pd.DataFrame(
    {
        "Name": ["Aman", "Priya", "Rahul"],
        "Age": [20, 21, 22],
        "City": ["Jaipur", "Bhopal", "Indore"],
    }
)

row_list = df.values.tolist()
print(row_list)