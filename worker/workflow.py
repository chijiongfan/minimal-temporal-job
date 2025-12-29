from temporalio import workflow
from datetime import timedelta
from temporalio.common import RetryPolicy

@workflow.defn
class JobWorkflow:
    def __init__(self):
        self.result = None

    @workflow.query
    def get_status(self):
        return {
            "status": "RUNNING" if self.result is None else "COMPLETED",
            "result": self.result,
        }

    @workflow.run

    async def run(self, input, options):
        result = await workflow.execute_activity(
        "compute_sum",
        args=[input["numbers"], options["fail_first_attempt"]],
        start_to_close_timeout=timedelta(seconds=5),
        retry_policy=RetryPolicy(maximum_attempts=3),
    )


        self.result = result
        return result

