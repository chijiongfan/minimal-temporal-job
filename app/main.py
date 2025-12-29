import uuid
from worker.workflow import JobWorkflow
from fastapi import FastAPI
from temporalio.client import Client

app = FastAPI()


@app.post("/jobs")
async def start_job(payload: dict):
    """
    Starts a Temporal workflow.
    """
    job_id = f"job-{uuid.uuid4()}"

    client = await Client.connect("localhost:7233")

    await client.start_workflow(
    JobWorkflow.run,
    args=[payload["input"], payload["options"]],
    id=job_id,
    task_queue="job-task-queue",
)


    return {"job_id": job_id}


@app.get("/jobs/{job_id}")
async def get_job(job_id: str):
    """
    Queries workflow status via Temporal Workflow Query.
    """
    client = await Client.connect("localhost:7233")
    handle = client.get_workflow_handle(job_id)

    return await handle.query(JobWorkflow.get_status)

