#!/usr/bin/env python3
"""Annotate the below function's parameters and return
values with the appropriate types

def element_length(lst):
    return [(i, len(i)) for i in lst]

{'lst': typing.Iterable[typing.Sequence], 'return': \
    typing.List[typing.Tuple[typing.Sequence, int]]}
"""


import typing


def element_length(lst: typing.Iterable[typing.Sequence]) -> \
        typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an
    element from the input iterable
    and the length of that element.

    Args:
        lst (Iterable[Sequence]): An iterable of sequences
        (e.g., strings, lists, tuples).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples, where
        the first element of each tuple is a sequence
        from the input iterable and the second element is the
        length of that sequence.
    """
    return [(i, len(i)) for i in lst]
