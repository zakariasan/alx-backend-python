#!/usr/bin/env python3
"""type-annotated function add that takes a float a and
a float b as arguments and returns their sum as a float."""
import asyncio
from typing import List
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Waits for random delay up to max_delay and returns list of actual"""
    de = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return de
