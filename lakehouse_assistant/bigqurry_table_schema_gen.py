#extract table schema from bigquery database tables using python code

from google.cloud import bigquery
def extract_table_schema(project_id, dataset_id):
    # Create a BigQuery client
    client = bigquery.Client(project=project_id)

    # List tables in the specified dataset
    table_obj = list(client.list_tables(dataset_id))
    #print("table_obj: ", table_obj[0].table_id)

    #extract the table from the table object and print the table id
    tables = []
    for table in table_obj:
        #print(table.table_id)
        tables.append(table.table_id)

    #print(tables)
    #extract schema information for each table
    schema_info = ""
    for table in tables:
        schema_info += f"- {dataset_id}.{table} ("
        table_ref = client.dataset(dataset_id).table(table)
        #print(table_ref)
        #table = client.get_table(table_ref)
        #print(f"Table: {table}")
        # extract the schema information for the table and print it
        schema = client.get_table(table_ref).schema
        #print(f"Schema for table: {schema}:")
        for field in schema:
            #print(f"  - {field.name} ({field.field_type})")
            schema_info += f"{field.name}, "
        schema_info = schema_info[:-2] + ')\n'
        #schema_info += f"- {table} ({', '.join([field.name for field in schema])})\n" 
        #print(f"schema_info: {schema_info}")
        #schema_info += f"({schema_info})\n"
        #print(f"{schema_info}")
    schema_info = f' "{schema_info}"'
    #print(f"{schema_info}")

    return schema_info

#extract_table_schema("genai-lakehouse-assistant", "thelook_dataset")