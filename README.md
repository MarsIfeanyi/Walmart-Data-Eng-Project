# Walmart Data Engineering Project

Walmart Data Engineering Project  Using: 
* [Agentic Database-Ghost DB](https://ghost.build/) = Source
* [Databricks](https://www.databricks.com/) = Lakehouse
* [DBT](https://www.getdbt.com/) = Transformation
* [Airflow](https://airflow.apache.org/) = Orchestration
* [AWS-S3](https://aws.amazon.com/s3/) = Storage
* [Docker](https://www.docker.com/) = Containerization



## Data Ingestion
The data ingestion from the Agentic Database to Databricks uses Change Data Capture (CDC) technique


The CDC-based data ingestion pipeline that ingests data from Ghost DB into a Databricks Lakehouse, following a Bronze → Silver → Gold architecture."

The CDC INgestion is a Databricks job







### Dataset
Reviews.csv, This is used by the managers and stakers holders for general product overview and performance. Its is not part of the Dimensional Data Analysis.
