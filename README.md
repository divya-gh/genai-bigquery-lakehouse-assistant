# 🚀 GenAI-Powered BigQuery Lakehouse Assistant

An end-to-end GenAI-driven BigQuery Lakehouse project that integrates Google Cloud services, GenAI (gemini flash) , public datasets, external Parquet tables, and Python SDK automation to answer business questions and export results dynamically.
- bridging Data Engineering + Analytics + GenAI in one integrated solution.
  
## 📌 Project Overview

### This project demonstrates how to:
* Build a Lakehouse-style architecture in BigQuery using GenAI and BigQerry
* Use GenAI (LLM) to dynamically generate SQL
* Query external Parquet files
* Integrate public datasets
* Execute queries via Python
* Export results to structured CSV files
* Implement secure IAM role management and service account authentication
Simulating a real-world enterprise analytics workflow using Gemini flash llm.

### 🏗 Architecture Components
* GenAI Integration: Gemini-2.5-flash LLM; generated SQL & file naming
* Cloud Platform: Google Cloud
* Data Warehouse: BigQuery
* Public Dataset: TheLook eCommerce
* Storage Format: Parquet (External Tables)
* SDK: Python BigQuery Client
* Local Environment: Python Virtual Environment

### 🔄 End-to-End Workflow
  Start
  ↓
Create External Table? (Yes)
  ↓
GenAI generates CREATE EXTERNAL TABLE SQL
  ↓
Table created in BigQuery
  ↓
User asks Business Question
  ↓
GenAI generates analytical SQL query
  ↓
Python executes SQL using BigQuery Client
  ↓
Results retrieved
  ↓
GenAI generates sanitized timestamped filename
  ↓
Results written to CSV file
  ↓
End

### 🎯 Key Features Implemented
* 1️⃣ External Table Creation (Lakehouse Pattern)
    - Created external tables in BigQuery using Parquet files
    - Generated CREATE EXTERNAL TABLE SQL dynamically using GenAI
    - Enabled querying data without ingestion (true lakehouse capability)

* 2️⃣ Public Dataset Integration
    - Added and explored the TheLook eCommerce public dataset
    - Created internal BigQuery tables from public dataset
    - Performed structured data modeling in Google Cloud Console

* 3️⃣ GenAI-Powered SQL Generation
     - Used LLM to:
      - Generate SQL to create external tables
      - Generate SQL to answer business questions
      - Enforce strict SQL-only output rules
      - Reduce manual query writing

* 4️⃣ Business Question Driven Analytics
   - Workflow:
    - User asks a business question
    - LLM converts question → SQL query
    - Python executes query in BigQuery
    - Results exported to CSV

#### Example business questions:
1. Total revenue by region
2. Customer return rate
3. Top selling categories
4. Average order value

Explore the full list of business questions you can ask: [Possible Business Questions to Ask](./Documentation/Possible-Business-Questions-to-Ask.md)

* 5️⃣ Secure IAM & Authentication
    - Implemented production-level access control:
    - Created Service Account
    - Assigned IAM roles (BigQuery Admin, Data Viewer, etc.)
    - Generated Service Account JSON key
    - Configured local SDK authentication
    - Prevented credential leakage via .gitignore
Demonstrating real-world Cloud Security & Governance understanding.

* 6️⃣ BigQuery SDK Execution (Python):
    - Used:
      - from google.cloud import bigquery
    - Implemented:
      - BigQuery client initialization
      - Query job execution
      - Error handling
      - Result fetching
      - Job state monitoring

* 7️⃣ Automated CSV Export
    - Dynamic file naming using LLM and prompt engineering and Writing structured results to CSV

## 🛠 Skills Demonstrated
#### ☁ Cloud & Data Engineering:
- Google Cloud Platform
      - BigQuery
      - External Tables
      - Public Dataset Integration
      - IAM Role Management
      - Service Account & Key Management
      - Lakehouse Architecture
      - Git/Github & rollback handling
      - Virtual environment management

### 🤖 AI Integration:
  - Prompt Engineering
  - SQL Generation via LLM
  - Controlled Output Enforcement
  - Production-safe LLM design

### 📊 Data Analytics
  - Business-driven query design
  - Revenue analysis
  - Return analysis
  - Aggregations
  - Group By logic
  - Structured export



Citation - This project was independently designed and developed using the knowledge gained from the Google Cloud Data Analytics Certification program, with additional guidance and assistance from ChatGPT for prompt refinement, debugging support, and documentation.
Licence - MIT
