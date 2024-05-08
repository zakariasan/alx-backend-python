#!/usr/bin/env python3
"""type-annotated function add that takes a float a and
a float b as arguments and returns their sum as a float."""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ try to collect my work """
    return [i async for i in async_generator()]
