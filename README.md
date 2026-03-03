🚀 GenAI-Powered BigQuery Lakehouse Assistant

An end-to-end GenAI-driven BigQuery Lakehouse project that integrates Google Cloud services, public datasets, external Parquet tables, and Python SDK automation to answer business questions and export results dynamically.

📌 Project Overview

This project demonstrates how to:

Build a Lakehouse-style architecture in BigQuery

Use GenAI (LLM) to dynamically generate SQL

Query external Parquet files

Integrate public datasets

Execute queries via Python

Export results to structured CSV files

Implement secure IAM role management and service account authentication

It simulates a real-world enterprise analytics workflow.

🏗 Architecture Components

Cloud Platform: Google Cloud

Data Warehouse: BigQuery

Public Dataset: TheLook eCommerce

Storage Format: Parquet (External Tables)

SDK: Python BigQuery Client

GenAI Integration: LLM-generated SQL & file naming

Local Environment: Python Virtual Environment

🎯 Key Features Implemented
1️⃣ External Table Creation (Lakehouse Pattern)

Created external tables in BigQuery using Parquet files

Generated CREATE EXTERNAL TABLE SQL dynamically using GenAI

Enabled querying data without ingestion (true lakehouse capability)

2️⃣ Public Dataset Integration

Added and explored the TheLook eCommerce public dataset

Created internal BigQuery tables from public dataset

Performed structured data modeling in Google Cloud Console

3️⃣ GenAI-Powered SQL Generation

Used LLM to:

Generate SQL to create external tables

Generate SQL to answer business questions

Enforce strict SQL-only output rules

Reduce manual query writing

4️⃣ Business Question Driven Analytics

Workflow:

User asks a business question

LLM converts question → SQL query

Python executes query in BigQuery

Results exported to CSV

LLM generates dynamic timestamped file name

Example business questions:

Total revenue by region

Customer return rate

Top selling categories

Average order value

5️⃣ Secure IAM & Authentication

Implemented production-level access control:

Created Service Account

Assigned IAM roles (BigQuery Admin, Data Viewer, etc.)

Generated Service Account JSON key

Configured local SDK authentication

Prevented credential leakage via .gitignore

Demonstrates real-world Cloud Security & Governance understanding.

6️⃣ BigQuery SDK Execution (Python)

Used:

from google.cloud import bigquery

Implemented:

BigQuery client initialization

Query job execution

Error handling

Result fetching

Job state monitoring

7️⃣ Automated CSV Export

Dynamic file naming using LLM

Timestamp injection (YYYYMMDDHHMMSS)

Special character removal

25-character constraint enforcement

Automatic directory creation

Writing structured results to CSV

🛠 Skills Demonstrated
☁ Cloud & Data Engineering

Google Cloud Platform

BigQuery

External Tables

Public Dataset Integration

IAM Role Management

Service Account & Key Management

Lakehouse Architecture

🤖 AI Integration

Prompt Engineering

SQL Generation via LLM

Controlled Output Enforcement

Production-safe LLM design

🐍 Python & SDK

BigQuery Python Client

File Handling

Exception Handling

OS directory management

Regex sanitization

Timestamp automation

📊 Data Analytics

Business-driven query design

Revenue analysis

Return analysis

Aggregations

Group By logic

Structured export

🔐 DevOps & Git

.gitignore configuration

Preventing credential exposure

Git uncommit & rollback handling

Virtual environment management
