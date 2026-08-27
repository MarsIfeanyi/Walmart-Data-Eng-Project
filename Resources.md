### Agentic DB
* https://ghost.build/

* https://ghost.build/docs/#introduction

### Create Environment for the project with UV
* Pip install uv

* Uv init

uv sync

.venv/Scripts/activate

### Initializing Ghost DB (Agentic DB)
* ghost init

### Creating DB 
* ghost create --name walmart_db

    ** Copy and put inside .env

### Create API KEY
* ghost api-key create --name mars_api_walmart --env > .env


### List the Database
ghost list

### Using Prompts on the Vscode Agent to create the table

Hey I want you to create tables for me  inside my ghost walmart_db. 
I want you to create one schema called raw for me inside the walmart_db, then you need to create tables inside that schema using my ddl script saved insde @file:walmart_schema.sql


### Inserting Data

Perfect, you to insert you to insert the csv data inside each table. I have the csv files stored at @file:walmart_dataset and inside it i have the data folder. You need to insert the csv data using '\copy' or 'copy_export' method


### Verifying the Data Ingestion

I want to see top 10 record of my orders table inside raw schema inside ghost walmart_db


### Creating the DB Fork
As a best practice when working Agentic DB, It is advisable to create a fork and work directly on the fork, so that If you accidential delete it, you can always get back the data from the main DB.
This ensure that your main(production DB) is always intact

prompt: 
I want to create a fork of my ghost walmart_db

### Getting more details from the fork db

prompt:
what is the primary key in the store table inside my ghost walmart_db-fork


Prompt 2:
how many products do I have the product table inside raw schema inside walmart_db-fork

Prompt 3:
I want to see average order size for each customer


### Getting the Ghost connection String
ghost connect walmart_db


### Create Environment for the project with UV
    * Pip install uv

    * Uv init

    * uv sync

    * .venv/Scripts/activate

### Installing DBT
uv add dbt-core

### Adding the Databricks connector
uv add dbt-databricks


### Initializing DBT
dbt init

### Debugging
dbt debug


### Refreshing
dbt run --full-refresh