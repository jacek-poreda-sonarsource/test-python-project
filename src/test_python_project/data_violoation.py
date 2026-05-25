import asyncio

async def fetch_data_violation():
    try:
        print("Fetching data from a slow API...")
        await asyncio.sleep(10)  # Simulating a long network request
        return "Data"
    except asyncio.CancelledError:
        # VIOLATION: We catch the cancellation to clean up, but swallow it!
        print("Task was cancelled! Cleaning up connection connections...")
        # Missing 'raise' here means the cancellation is cancelled!
