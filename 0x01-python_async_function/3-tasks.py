#!/usr/bin/env python3
"""Import wait_random from 0-basic_async_syntax.

Write a function (do not create an async function, use the regular
function syntax to do this) task_wait_random that takes an integer
max_delay and returns a asyncio.Task.
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio.Task that calls wait_random with the given max_delay.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: The created task.
    """
    return asyncio.create_task(wait_random(max_delay))
