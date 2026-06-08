-- Total Deliveries
SELECT COUNT(*) AS total_deliveries
FROM delivery_kpis;

-- Average Delivery Time
SELECT ROUND(AVG(delivery_minutes),2) AS avg_delivery_time
FROM delivery_kpis;

-- On-Time Delivery %
SELECT ROUND(
SUM(on_time)*100/COUNT(*),
2
) AS on_time_percentage
FROM delivery_kpis;

-- Average Rating
SELECT ROUND(AVG(rating),2) AS avg_rating
FROM delivery_kpis;