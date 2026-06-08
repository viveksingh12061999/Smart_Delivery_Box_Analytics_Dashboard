# GrubPac Smart Delivery Analytics Dashboard

## Project Overview

This project simulates a real-world food delivery analytics system for GrubPac. It demonstrates an end-to-end data analytics pipeline using Python, MySQL, SQL, and Power BI.

The system generates delivery data, stores it in a MySQL database, performs analytics, and visualizes key business metrics through interactive dashboards.

---

## Objectives

- Analyze delivery performance
- Track driver efficiency
- Monitor customer activity
- Measure on-time delivery rates
- Identify delivery delays
- Predict delayed deliveries using Machine Learning

---

## Tech Stack

- Python
- Pandas
- NumPy
- Faker
- SQLAlchemy
- MySQL
- SQL
- Power BI
- Scikit-Learn

---

## Project Architecture

Data Generation
↓
Python ETL
↓
MySQL Database
↓
SQL Analytics
↓
Power BI Dashboard
↓
Machine Learning Model

---

## Database Schema

### Drivers

- driver_id
- driver_name
- vehicle_type
- joining_date

### Customers

- customer_id
- customer_name
- city
- customer_type

### Deliveries

- delivery_id
- order_id
- driver_id
- customer_id
- pickup_time
- delivery_time
- distance_km
- temperature
- delivery_status
- rating

---

## Key KPIs

- Total Deliveries
- On-Time Delivery %
- Average Delivery Time
- Average Rating
- Delayed Deliveries
- Temperature Compliance %
- Driver Performance Score

---

## Dashboard Pages

### Executive Dashboard

- Total Deliveries
- On-Time %
- Average Rating
- Average Delivery Time

### Driver Dashboard

- Driver Rankings
- Driver Ratings
- Deliveries by Driver

### Customer Dashboard

- Orders by City
- Customer Segments
- Top Customers

### Operations Dashboard

- Temperature Compliance
- Delay Analysis
- Delivery Trends

---

## Machine Learning

Model:
- RandomForestClassifier

Target:
- Delayed Delivery

Features:
- Distance
- Hour
- Temperature
- Driver
- City

---

## Folder Structure

```text
grubpac_analytics/
│
├── data/
├── scripts/
├── sql/
├── powerbi/
├── models/
├── reports/
└── README.md
```

## Future Enhancements

- Real-time dashboard
- Driver route optimization
- Demand forecasting
- Automated email reports
- Cloud deployment using AWS

---

## Author

Vivek Singh
