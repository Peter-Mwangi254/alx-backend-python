#!/usr/bin/env python3
"""Write a type-annotated function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple.The first
element of the tuple is the string k. The second element is the
square of the int/float v and should be annotated as a float.
"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """
    Returns a tuple of the string k and the square of the value v as a float.

    Args:
        k (str): A string value.
        v (Union[int, float]): An integer or float value.

    Returns:
        Tuple[str, float]: A tuple containing the string k
        and the square of the value v as a float.
    """
    return (k, float(v * v))
