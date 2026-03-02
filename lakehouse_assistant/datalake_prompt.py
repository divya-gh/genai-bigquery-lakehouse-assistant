#generate a prompt to add GCS file to dataset in bigquery using python code

def build_table_upload_prompt(gcs_uri,project_id, dataset_id):
    prompt = f""" You are a data engineer working with Google Cloud Platform. 
    Your task is to write a sql querry to create an external table or replace it if it already exists from Google Cloud Storage (GCS) to a already existing BigQuery dataset.
    The GCS URI of the file is {gcs_uri}, the project ID is {project_id}, and the dataset ID is {dataset_id}.   
    Please provide the SQL querry using the Google Cloud BigQuery client library to accomplish this task. Files can be csv, json, parquet.
    Make sure to handle the file format correctly in the SQL query.
    Make sure generate only safe SQL query only (no markup,talks, DELETE, DROP, UPDATE)."""
    
    return prompt
'''
project = "genai-lakehouse-assistant"
dataset = "thelook_dataset"

prompt  = build_table_upload_prompt("gs://my_bucket/my_file.csv", project, dataset)
print(prompt)


'''