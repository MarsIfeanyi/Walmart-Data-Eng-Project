### Create Environment for the project with UV
    * Pip install uv

    * Uv init

uv sync

.venv/Scripts/activate

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