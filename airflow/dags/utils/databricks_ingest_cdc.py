from databricks.sdk import WorkspaceClient
from databricks.sdk.service.jobs import RunLifeCycleState, RunResultState
import os
import time
from dotenv import load_dotenv

load_dotenv()


def databricks_ingest_cdc():

    ws = WorkspaceClient(
        host=os.getenv("DATABRICKS_HOST"),
        token=os.getenv("DATABRICKS_TOKEN")
    )

    job_trigger = ws.jobs.run_now(
        job_id=int(os.getenv("DATABRICKS_JOB_ID"))
    )

    while True:

        job_run = ws.jobs.get_run(job_trigger.run_id)

        if job_run.state.life_cycle_state in [
            RunLifeCycleState.TERMINATED,
            RunLifeCycleState.SKIPPED,
            RunLifeCycleState.INTERNAL_ERROR
        ]:

            if job_run.state.result_state == RunResultState.SUCCESS:
                print("Job completed successfully!")
                break

            else:
                raise Exception(
                    f"Job failed with state: {job_run.state.result_state}"
                )

        time.sleep(5)  # Wait 5 seconds before checking again.