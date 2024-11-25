import os

import dotenv
from google.cloud import bigquery

# Load the environment variables
dotenv.load_dotenv()

project_id = os.getenv("GOOGLE_CLOUD_PROJECT")
dataset_id = os.getenv("BIGQUERY_DATASET_NAME")
table_id = os.getenv("BIGQUERY_TABLE_NAME")


# Initialize the BigQuery client
client = bigquery.Client()

query = f"""
CREATE OR REPLACE TABLE `{project_id}.{dataset_id}.{table_id}` AS
SELECT *
FROM `bigquery-public-data.chicago_taxi_trips.taxi_trips`
WHERE fare IS NOT NULL
"""

# Execute the query
query_job = client.query(query)

# Wait for the query to finish
query_job.result()

print("Table created or replaced successfully.")
