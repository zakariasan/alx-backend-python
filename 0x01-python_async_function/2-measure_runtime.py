#!/usr/bin/env python3
"""type-annotated function add that takes a float a and
a float b as arguments and returns their sum as a float."""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """ Measures total execution time of wait_n coroutine """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time / n
