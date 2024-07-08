#!/usr/bin/env python3
"""Measures run time"""
import asyncio
import time
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n."""
    start_time = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    end_time = time.perf_counter() - start_time
    total_time = end_time / n
    
    return total_time