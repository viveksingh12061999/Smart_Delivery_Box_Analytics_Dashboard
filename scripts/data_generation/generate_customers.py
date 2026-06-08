from faker import Faker
import pandas as pd
import random
import os

fake = Faker()

cities = [
    "Delhi",
    "Noida",
    "Gurgaon",
    "Faridabad",
    "Ghaziabad",
    "Meerut",
    "Agra",
]

customer_types = [
    "Regular",
    "Premium",
    "Occasional",
    "Corporate"
]

customers = []
for i in range(1,1001):
    customers.append([
        i,
        fake.name(),
        random.choice(cities),
        random.choice(customer_types)
    ])

df = pd.DataFrame(
    customers,
    columns = [
        'customer_id',
        'customer_name',
        'city',
        'customer_type'
    ]
)

os.makedirs("data/raw", exist_ok=True)

df.to_csv("data/raw/customers.csv", index=False)

print(df.head())
print("Customers file created successfully")