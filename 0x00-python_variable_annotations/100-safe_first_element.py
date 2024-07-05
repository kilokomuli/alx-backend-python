#!/usr/bin/env python3
"""Correct duck typed annotations"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Iterable object"""
    if lst:
        return lst[0]
    else:
        return None
