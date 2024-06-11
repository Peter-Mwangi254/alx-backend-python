#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write a measure_runtime
coroutine that will execute async_comprehension four times in parallel using
asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.
"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime
    """
    start_time = time.time()

    tasks = []
    for _ in range(4):
        tasks.append(async_comprehension())

    await asyncio.gather(*tasks)

    end_time = time.time()
    total_runtime = end_time - start_time
    return total_runtime
