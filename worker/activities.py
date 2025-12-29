from temporalio import activity

@activity.defn
async def compute_sum(numbers, fail_first_attempt: bool):
    attempt = activity.info().attempt
    print(f"Activity attempt: {attempt}")

    if fail_first_attempt and attempt == 1:
        raise Exception("Intentional failure on first attempt")

    return sum(numbers)

