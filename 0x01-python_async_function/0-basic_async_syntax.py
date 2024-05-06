#!/usr/bin/env python3
"""type-annotated function add that takes a float a and
a float b as arguments and returns their sum as a float."""
import asyncio
import random


async def wait_random(max_delay=10):
    """Return playing with random"""
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
