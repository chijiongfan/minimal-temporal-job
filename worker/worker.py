import temporalio
import asyncio
from temporalio.client import Client
from temporalio.worker import Worker

from worker.workflow import JobWorkflow
from worker.activities import compute_sum

async def main():
    client = await Client.connect("localhost:7233")

    worker = Worker(
        client,
        task_queue="job-task-queue",
        workflows=[JobWorkflow],
        activities=[compute_sum],
    )

    print("Worker started and listening for tasks...")
    await worker.run()

if __name__ == "__main__":
    asyncio.run(main())
