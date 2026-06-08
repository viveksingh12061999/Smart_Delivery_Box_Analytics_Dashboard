from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "mysql+pymysql://root:root123@localhost/grubpac"
)

drivers = pd.read_csv("data/raw/drivers.csv")
customers = pd.read_csv("data/raw/customers.csv")
deliveries = pd.read_csv("data/raw/deliveries.csv")

drivers.to_sql(
    "drivers",
    con=engine,
    if_exists="replace",
    index=False
)
customers.to_sql(
    "customers",
    con=engine,
    if_exists="replace",
    index=False
)

deliveries.to_sql(
    "deliveries",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully")