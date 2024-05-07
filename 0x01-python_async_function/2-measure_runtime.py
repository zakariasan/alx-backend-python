#!/usr/bin/env python3
"""type-annotated function add that takes a float a and
a float b as arguments and returns their sum as a float."""
import asyncio
import time
w_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """Measures to coroutine."""
    start_time = time.perf_counter()
    asyncio.run(w_n(n, max_delay))
    elapsed_time = time.perf_counter() - start_time
    return elapsed_time / n
