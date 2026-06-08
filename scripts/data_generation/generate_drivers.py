from faker import Faker
import pandas as pd

fake = Faker()

drivers = []

for i in range(1,51):
    drivers.append([
        i,
        fake.name(),
        fake.random_element(['Bike', 'Car', 'Van', 'Truck']),
        fake.date_between(start_date='-2y', end_date='today')
    ])

    df = pd.DataFrame(
        drivers,
        columns = [
            'driver_id',
            'driver_name',
            'vehicle_type',
            'joining_date'
        ]
    )

    df.to_csv('drivers.csv',index=False)

    print("drivers.csv generated successfully!")
    print(df.head())
    