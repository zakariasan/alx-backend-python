#!/usr/bin/env python3
"""type-annotated function add that takes a float a and
a float b as arguments and returns their sum as a float."""

import asyncio
import random


async def async_generator():
    """ try to asyc generator """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
