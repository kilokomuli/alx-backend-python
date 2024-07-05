#!/usr/bin/env python3
""" use of typevar in type annotations """
from typing import Any, Union, Mapping, TypeVar
F = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[F, None]) -> Union[Any, F]:
    """ returns a map. """
    if key in dct:
        return dct[key]
    else:
        return default
