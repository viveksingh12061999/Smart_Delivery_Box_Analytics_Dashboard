from faker import Faker
import pandas as pd
import random
from datetime import timedelta
import os

fake = Faker()

deliveries = []

for i in range(1,10001):

    pickup_time = fake.date_time_between(
        start_date = '-90d',
        end_date = 'now'
    )

    delivery_minutes = random.randint(10,60)

    delivery_time = pickup_time + timedelta(
        minutes = delivery_minutes
    )

    deliveries.append([
        i,
        f"ORD{i:05}",
        random.randint(1,50),
        random.randint(1,1000),
        pickup_time,
        delivery_time,
        round(random.uniform(1,20), 2),
        round(random.uniform(-5,80), 2),
        random.choice(
            ["Delivered", "Delayed", "Cancelled"]
        ),
        round(random.uniform(1,5),1)
    ])


df = pd.DataFrame(
    deliveries,
    columns = [
        'delivery_id',
        'order_id',
        'driver_id',
        'customer_id',
        'pickup_time',
        'delivery_time',
        'distance_km',
        'temperature',
        'delivery_status',
        'rating'
    ]
)

os.makedirs("data/raw", exist_ok = True)

df.to_csv('data/raw/deliveries.csv', index = False)

print(df.head())
print("Deliveries file created successfully")

