#!/usr/bin/env python3
"""type-annotated function add that takes a float a and
a float b as arguments and returns their sum as a float."""
import asyncio
from random import uniform
from typing import List
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = []
    for _ in range(n):
        tasks.append(wait_random(max_delay))
    results = await asyncio.gather(*tasks)
    return results
