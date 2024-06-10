#!/usr/bin/env python3
"""
Measures the total execution time for wait_n(n, max_delay)
and returns the average time per coroutine.
"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Args:
        n (int): The number of coroutines to wait for.
        max_delay (int): The maximum delay for each coroutine.

    Returns:
        float: The average time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()

    total_time = end_time - start_time
    return (total_time/n)
