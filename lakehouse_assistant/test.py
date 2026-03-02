from google.cloud import bigquery

client = bigquery.Client(project="genai-lakehouse-assistant")
tables = list(client.list_tables("thelook_dataset"))
for table in tables:
    print(table.table_id)