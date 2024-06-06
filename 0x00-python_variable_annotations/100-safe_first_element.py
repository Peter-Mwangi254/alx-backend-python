#!/usr/bin/env pythion3
"""Augment the following code with the correct duck-typed annotations:

The types of the elements of the input are not know
def safe_first_element(lst):
    if lst:
        return lst[0]
    else:
        return None

{'lst': typing.Sequence[typing.Any], 'return': \
    typing.Union[typing.Any, NoneType]}
"""


import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """
    Returns the first element of the input sequence, or None if the
    sequence is empty.

    Args:
        lst (Sequence[Any]): A sequence of elements of unknown type.

    Returns:
        Union[Any, None]: The first element of the input sequence,
        or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
