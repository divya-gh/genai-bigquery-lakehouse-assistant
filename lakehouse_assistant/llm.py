# create a python code for a function that acceepts prompt and generates a sql query using gemini 2.0 flash model

from google import genai
import os
from dotenv import load_dotenv
# load .env file to get the api key
load_dotenv()

def generate_sql_query(prompt):
    # Set up the Gemini api client
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    # Generate the response based on the prompt
    response = client.models.generate_content(
            model="gemini-2.5-flash",
        contents=prompt,

    )

    # Extract and return the generated SQL query
    sql_query = response.text.strip()
    return sql_query


'''
prompt = """ You are a data engineer working with Google Cloud Platform. 
    Your task is to write a sql querry to create an external table or replace it if it already exists from Google Cloud Storage (GCS) to a already existing BigQuery dataset.
    The GCS URI of the file is gs://my_bucket/my_file.csv, the project ID is genai-lakehouse-assistant, and the dataset ID is thelook_dataset.   
    Please provide the SQL querry using the Google Cloud BigQuery client library to accomplish this task. Files can be csv, json, parquet.
    Make sure to handle the file format correctly in the SQL query.
    Make sure generate only safe SQL query only (no markup,talks, DELETE, DROP, UPDATE)."""


sql_querry = generate_sql_query(prompt)
print(sql_querry)



'''


'''
Task : Genetate sql querry to answer the business question.
prompt = """ You are a BigQuery SQL expert working with a Lakehouse architecture.

Available Tables:"- thelook_dataset.order_items (id, order_id, user_id, product_id, inventory_item_id, status, created_at, shipped_at, delivered_at, returned_at, sale_price)
- thelook_dataset.orders (order_id, user_id, status, gender, created_at, returned_at, shipped_at, delivered_at, num_of_item)
- thelook_dataset.products (id, cost, category, name, brand, retail_price, department, sku, distribution_center_id)
- thelook_dataset.users (id, first_name, last_name, email, age, gender, state, street_address, postal_code, city, country, latitude, longitude, traffic_source, created_at, user_geom)
"

Generate a safe SELECT SQL query only (no DELETE, DROP, UPDATE).

Question:
What are the top 5 products by total sales?

Return only SQL."""

sql_querry = generate_sql_query(prompt)
print(sql_querry)

'''

