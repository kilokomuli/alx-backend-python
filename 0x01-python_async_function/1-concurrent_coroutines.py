#!/usr/bin/env python3
"""Executing multiple coroutines at the same time with async"""
import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """asynchronous coroutine that takes in an integer argument
    (n) and a integer argument (max_delay) and that waits for a
    random delay between 0 and max_delay seconds and returns it."""
    delays = [wait_random(max_delay) for i in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]