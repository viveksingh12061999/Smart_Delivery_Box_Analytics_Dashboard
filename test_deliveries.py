import pandas as pd

df = pd.read_csv("data/raw/deliveries.csv")

print("Rows:", len(df))
print("Columns:", len(df.columns))
print(df.head())
print(df.columns.tolist())