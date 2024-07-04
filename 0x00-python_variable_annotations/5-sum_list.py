#!/usr/bin/env python3
from typing import List
"""Type-annotated function sum_list which takes a list input_list of floats as argument and returns their sum as a float."""


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of floats"""
    return sum(input_list)