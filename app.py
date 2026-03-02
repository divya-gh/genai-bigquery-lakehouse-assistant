# import the necessary packages from other files
from lakehouse_assistant.datalake_prompt import build_table_upload_prompt
from lakehouse_assistant.datalake_prompt import build_table_upload_prompt
from lakehouse_assistant.llm import generate_sql_query
from lakehouse_assistant.bigquery_client import execute_sql_query
from lakehouse_assistant.prompt_template import build_sql_prompt
from lakehouse_assistant.bigqurry_table_schema_gen import extract_table_schema

project = "genai-lakehouse-assistant"
dataset = "thelook_dataset"


def main():

    file_upload_question = input("Do you want to create external table in BigQuery? (yes/no): ")
    if file_upload_question.lower() == "yes":
        gcs_uri = input("Enter the GCS URI of the file to upload: ")
        project_id = input("Enter the BigQuery project ID: ")
        dataset_id = input("Enter the BigQuery dataset ID: ")
        # Build the prompt for uploading a file to BigQuery
        upload_prompt = build_table_upload_prompt(gcs_uri, project_id, dataset_id)
        #print("Generated Prompt for File Upload:", upload_prompt)
        # Here you would call a GenAI function to generate and execute the upload code based on the prompt
        upload_querry = generate_sql_query(upload_prompt)
        #print(f"Generated SQL Query for File Upload: {upload_querry}")
        # execute_upload_code(upload_code)
        upload_results = execute_sql_query(upload_querry)
        print("File Upload Results:", upload_results)

    else:
        print("Skipping file upload. Proceeding to ask business questions.")
    
        
        # For example:
        # upload_code = generate_upload_code(upload_prompt)
    # Ask a business question to solve using SQL query
    question = input("Ask a Business Question: ")

# Example schema information and question
    schema_info = extract_table_schema(project, dataset)
    # print("Schema Information:", schema_info)


    # Build the prompt for the LLM
    prompt = build_sql_prompt(question, schema_info)
    #print("Generated Prompt for LLM:", prompt)
    # Generate the SQL query using the LLM na dthe prompt
    sql_query = generate_sql_query(prompt)
    print(f"Generated SQL Query:\n {sql_query}")
    
    # Execute the SQL query and get results
    
    #results = execute_sql_query(sql_query)
    #print("Query Results:", results)
    ##for row in results:
     ##   print(row)


    try:
        results = execute_sql_query(sql_query)
        if results:
            print("\nResults:")
            for row in results:
                print(row)
        else:
            print("Query executed successfully but returned no results.")
    except Exception as e:
        print("Query Execution Error:", e)



if __name__ == "__main__":    
    main()


