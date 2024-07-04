#!/usr/bin/env python3
from typing import List
"""Type-annotated function sum_mixed_list which takes a list mxd_lst of floats and integers and returns their sum as a float."""

def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """Returns the sum of a list of floats and integers"""
    return sum(mxd_lst)