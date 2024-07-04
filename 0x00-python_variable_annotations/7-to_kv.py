#!/usr/bin/env python3
from typing import Union

def to_kv(k: str, v: Union[int, float])-> tuple:
    """Returns a tuple"""
    return (k, v * v)