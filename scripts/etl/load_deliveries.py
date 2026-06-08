import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:root123@localhost/grubpac"
)

deliveries = pd.read_csv("data/raw/deliveries.csv")

print(deliveries.shape)

try:
    deliveries.to_sql(
        "deliveries",
        con=engine,
        if_exists="append",
        index=False
    )
    print("Deliveries loaded successfully!")

except Exception as e:
    print("ERROR:")
    print(type(e))
    print(e)