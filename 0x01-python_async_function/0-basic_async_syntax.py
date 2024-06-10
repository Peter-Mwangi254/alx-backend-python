#!/usr/bin/env python3
"""
 An asynchronous coroutine that waits for a random
 delay between 0 and max_delay seconds.
 """


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Args:
        max_delay (int, optional): Maximum delay in seconds. Defaults to 10.

    Returns:
        float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
