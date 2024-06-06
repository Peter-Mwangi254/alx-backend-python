#!/usr/bin/env python3
"""Write a type-annotated function sum_mixed_list which takes a list
mxd_lst of integers and floats and returns their sum as a float.
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    Returns the sum of the list as a float.

    Args:
        mxd_lst (List[Union[int, float]]): A list containing integers
        and floats.

    Returns:
        float: The sum of the values in the input list.
    """
    return float(sum(mxd_lst))
