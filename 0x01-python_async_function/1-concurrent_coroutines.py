#!/usr/bin/env python3
"""type-annotated function add that takes a float a and
a float b as arguments and returns their sum as a float."""
import asyncio
from typing import List
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(num_tasks: int, max_delay: int = 10) -> List[float]:
    """Waits for a random delay up to max_delay and returns a list """
    tasks = []
    delays = []

    for _ in range(num_tasks):
        task = asyncio.create_task(wait_random(max_delay))
        task.add_done_callback(lambda future: delays.append(future.result()))
        tasks.append(task)

    await asyncio.gather(*tasks)

    return delays
