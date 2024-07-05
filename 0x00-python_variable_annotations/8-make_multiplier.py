#!/usr/bin/env python3
"""Ty[e-annotated function that takes a floatas an argument and
returns a function that multiplies a float"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplied a float by multiplier
    """
    return lambda multiplier1: multiplier1 * multiplier
