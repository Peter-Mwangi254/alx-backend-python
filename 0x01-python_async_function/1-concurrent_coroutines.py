#!/usr/bin/env python3
"""
    An asynchronous coroutine that spawns `n` times the `wait_random` coroutine
    with the specified `max_delay`.
"""


import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn `wait_random` `n` times with the specified `max_delay`.

    Args:
        n (int): The number of times to spawn the `wait_random` coroutine.
        max_delay (int): The maximum delay in seconds for the
 `wait_random` coroutine.

    Returns:
        List[float]: The list of delays (in seconds)
    returned by each call to `wait_random`.
    """
    tasks = []
    delays = []

    for i in range(n):
        task = wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
