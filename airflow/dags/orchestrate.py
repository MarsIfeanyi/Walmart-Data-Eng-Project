
from airflow.sdk import dag, task
from airflow.operators.bash import BashOperator
from utils.databricks_ingest_cdc import databricks_ingest_cdc
from utils.databricks_ingest_cdc import databricks_ingest_cdc
from airflow.sdk import dag, task
from pendulum import datetime


time_zone='Africa/Lagos'
start_date_local = datetime(
    year=2026,
    month=8,
    day=27,
    tz=time_zone
)

@dag (
        dag_id="orchestrate_dag",
    start_date=start_date_local,
    schedule="0 23 * * *", # 11pm Daily
    is_paused_upon_creation=False,
    catchup=True
)

def orchestrate_dag():

    @task
    def ingest_cdc():
        
        databricks_ingest_cdc()
        
        return "CDC Ingestion Completed"
    
    @task.bash
    def clean_target():
        return "rm -rf /opt/airflow/walmart_dataeng_project/target && rm -rf /opt/airflow/walmart_dataeng_project/logs"

    @task.bash
    def source_freshness():
        # Manually set the working directory using the 'cd' command before running the dbt command
        return "cd /opt/airflow/walmart_dataeng_project && dbt source freshness"
    

    silver_technical = BashOperator(
        task_id='silver_technical',
        cwd='/opt/airflow/walmart_dataeng_project',
        bash_command='dbt run --select silver_t'
    )

    silver_technical_tests = BashOperator(
        task_id='silver_technical_tests',
        cwd='/opt/airflow/walmart_dataeng_project',
        bash_command='dbt test --select silver_t'
    )

    silver_business = BashOperator(
            task_id='silver_business',
            cwd='/opt/airflow/walmart_dataeng_project',
            bash_command='dbt run --select silver_b'
        )

    silver_business_tests = BashOperator(
        task_id='silver_business_tests',
        cwd='/opt/airflow/walmart_dataeng_project',
        bash_command='dbt test --select silver_b'
    )

    gold_ephermeral = BashOperator(
        task_id='gold_ephermeral',
        cwd='/opt/airflow/walmart_dataeng_project',
        bash_command='dbt run --select gold/ephermeral'
    )

    gold_dimensions = BashOperator(
        task_id='gold_dimensions',
        cwd='/opt/airflow/walmart_dataeng_project',
        bash_command='dbt snapshot'
    )
 
    gold_facts = BashOperator(
        task_id='gold_facts',
        cwd='/opt/airflow/walmart_dataeng_project',
        bash_command='dbt run --select gold/fact'
    )

    ingest_cdc() >> clean_target() >> source_freshness() >> silver_technical >> silver_technical_tests  >> silver_business >> silver_business_tests >> gold_ephermeral >> gold_dimensions >> gold_facts

orchestrate_dag()

