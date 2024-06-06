#!/usr/bin/env python3
"""
A type-annotated function make_multiplier that takes
a float multiplier as argument and returns a function that
multiplies a float by multiplier.
"""


import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The value to multiply the input float by.

    Returns:
        Callable[[float], float]: A function that takes a float argument
        and returns the product of the input and the multiplier.
    """
    def float_multiply(x: float) -> float:
        return multiplier * x

    return float_multiply
