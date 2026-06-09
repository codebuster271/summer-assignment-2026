import pandas as pd


df = pd.DataFrame(
    {
        "Name": ["Aman", "Priya", "Rahul", "Sneha"],
        "Age": [20, 21, 22, 23],
        "City": ["Jaipur", "Bhopal", "Indore", "Delhi"],
    }
)

print(df.loc[0:2, ["Name", "City"]])