import os

import dotenv
from google.cloud import bigquery

# Load the environment variables
dotenv.load_dotenv()

# Set up your BigQuery client
client = bigquery.Client()

# Define your dataset and table
project = os.getenv("GOOGLE_CLOUD_PROJECT")
dataset_name = os.getenv("BIGQUERY_DATASET_NAME")
dataset_id = f"{project}.{dataset_name}"
table_id = os.getenv("BIGQUERY_TABLE_NAME")


# Function to run a query and return results as a DataFrame
def run_query(query):
    query_job = client.query(query)
    results = query_job.result()
    return results.to_dataframe()


# Example queries for data exploration

# 1. Get a summary of the dataset
summary_query = f"""
SELECT
    COUNT(*) AS total_trips,
    AVG(fare) AS avg_fare,
    MIN(fare) AS min_fare,
    MAX(fare) AS max_fare,
    AVG(trip_seconds) AS avg_trip_seconds,
    AVG(trip_miles) AS avg_trip_miles
FROM `{dataset_id}.{table_id}`
"""
summary = run_query(summary_query)
print("Dataset Summary:")
print(summary)

# 2. Distribution of fares
fare_distribution_query = f"""
SELECT
    fare,
    COUNT(*) AS count
FROM `{dataset_id}.{table_id}`
GROUP BY fare
ORDER BY fare
LIMIT 100
"""
fare_distribution = run_query(fare_distribution_query)
print("Fare Distribution:")
print(fare_distribution)

# 3. Average fare per day of the week
avg_fare_per_day_query = f"""
SELECT
    EXTRACT(DAYOFWEEK FROM trip_start_timestamp) AS day_of_week,
    AVG(fare) AS avg_fare
FROM `{dataset_id}.{table_id}`
GROUP BY day_of_week
ORDER BY day_of_week
"""
avg_fare_per_day = run_query(avg_fare_per_day_query)
print("Average Fare per Day of the Week:")
print(avg_fare_per_day)

# 4. Distribution of trips by pickup location
pickup_location_query = f"""
SELECT
    pickup_latitude,
    pickup_longitude,
    COUNT(*) AS count
FROM `{dataset_id}.{table_id}`
GROUP BY pickup_latitude, pickup_longitude
ORDER BY count DESC
LIMIT 100
"""
pickup_location_distribution = run_query(pickup_location_query)
print("Pickup Location Distribution:")
print(pickup_location_distribution)

# 5. Average fare by payment type
avg_fare_by_payment_type_query = f"""
SELECT
    payment_type,
    AVG(fare) AS avg_fare,
    COUNT(*) AS count
FROM `{dataset_id}.{table_id}`
GROUP BY payment_type
ORDER BY avg_fare DESC
"""
avg_fare_by_payment_type = run_query(avg_fare_by_payment_type_query)
print("Average Fare by Payment Type:")
print(avg_fare_by_payment_type)


# Save results to a CSV file for further analysis if needed
summary.to_csv("summary.csv", index=False)
fare_distribution.to_csv("fare_distribution.csv", index=False)
avg_fare_per_day.to_csv("avg_fare_per_day.csv", index=False)
pickup_location_distribution.to_csv("pickup_location.csv", index=False)
avg_fare_by_payment_type.to_csv("avg_fare_by_payment_type.csv", index=False)
