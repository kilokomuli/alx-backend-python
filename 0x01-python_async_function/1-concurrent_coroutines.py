#!/usr/bin/env python3
"""Executing multiple coroutines at the same time with async"""
import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """asynchronous coroutine that takes in an integer argument
    (n) and a integer argument (max_delay) and that waits for a
    random delay between 0 and max_delay seconds and returns it."""
    delays: List[float] = []
    tasks: List = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)
    return delays
