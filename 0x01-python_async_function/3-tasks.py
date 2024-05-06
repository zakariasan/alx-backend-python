#!/usr/bin/env python3
"""type-annotated function add that takes a float a and
a float b as arguments and returns their sum as a float."""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay seconds."""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """Waits for random delay then returns asyncio.Task object."""
    return asyncio.create_task(wait_random(max_delay))
