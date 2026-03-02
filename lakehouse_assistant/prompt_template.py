''' Create a python tool to generate prompt template when a schema and question are provided. '''

def build_sql_prompt(question, schema_info):
    return f"""
You are a BigQuery SQL expert working with a Lakehouse architecture.

Available Tables:
{schema_info}

Generate a safe SELECT SQL query only (no markdown, DELETE, DROP, UPDATE).

Question:
{question}

Return only SQL.
"""
#question = "What are the top 5 products by total sales?"
'''schema_info = """ order_items (id, order_id, user_id, product_id, inventory_item_id, status, created_at, shipped_at, delivered_at, returned_at, sale_price)
- orders (order_id, user_id, status, gender, created_at, returned_at, shipped_at, delivered_at, num_of_item)
- products (id, cost, category, name, brand, retail_price, department, sku, distribution_center_id)      
- users (id, first_name, last_name, email, age, gender, state, street_address, postal_code, city, country, latitude, longitude, traffic_source, created_at, user_geom)"""
sql_prompt = build_sql_prompt(question, schema_info)
print(sql_prompt)'''