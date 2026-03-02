# Generate a python function to execute a SQL query using BigQuery client and return the results.

from google.cloud import bigquery
def execute_sql_query(sql_query):
    # Create a BigQuery client
    client = bigquery.Client()

    # Execute the SQL query
    query_job = client.query(sql_query)

    # Wait for the query to finish and get the results
    results = query_job.result()
    #  if sql querry contains create  or replace , then return a message that the table has been created or replaced successfully instead of returning results.
    if "CREATE TABLE" in sql_query.upper() or "REPLACE TABLE" in sql_query.upper():
        return print(f"Table has been created or replaced successfully.\n Job ID: {query_job.job_id}\n State: {query_job.state}")
        

    else:
        # Convert results to a list of dictionaries
        rows = [dict(row) for row in results]
        return rows

'''
sql= """
SELECT
  p.name,
  SUM(oi.sale_price) AS total_sales
FROM
  `thelook_dataset.order_items` AS oi
JOIN
  `thelook_dataset.products` AS p
  ON oi.product_id = p.id
GROUP BY
  p.name
ORDER BY
  total_sales DESC
LIMIT 5
"""


rows = execute_sql_query(sql) 
print(rows)



sql= """
CREATE OR REPLACE EXTERNAL TABLE `genai-lakehouse-assistant.thelook_dataset.returns`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://sureskills-lab-dev/DAC2M2L4/returns/returns_*.parquet']
);
"""

rows = execute_sql_query(sql) 
print(rows)

'''