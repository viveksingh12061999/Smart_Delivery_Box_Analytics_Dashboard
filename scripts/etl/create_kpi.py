import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:root123@localhost/grubpac"
)

df = pd.read_sql("SELECT * FROM deliveries", engine)

df["pickup_time"] = pd.to_datetime(df["pickup_time"])
df["delivery_time"] = pd.to_datetime(df["delivery_time"])


df["delivery_minutes"] = (
      df["delivery_time"] - df["pickup_time"]
    ).dt.total_seconds()/60

#KPI Flags

df["on_time"] = df["delivery_minutes"] <= 30
df["delayed"] = df["delivery_minutes"] > 30
df["temp_compliance"] = df["temperature"].between(-5,75)

df.to_sql(
    "deliveries_kpis",
    con=engine,
    if_exists="replace",
    index=False,
)

print("KPI table created successfully")
print(df.head())