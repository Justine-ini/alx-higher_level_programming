#!/usr/bin/python3
"""

This module is composed by a function that adds two numbers

"""


def add_integer(a, b=98):
    """ Function that adds two integer and/or float numbers

    Args:
        a: The first integer.
        b: The second integer. Defaults to 98.

    Returns:
        The sum of a and b.

    Raises:
        TypeError: If a or b aren't integer and/or float numbers

    """

    if not isinstance(a, int) or not isinstance(a, float):
        raise TypeError('a must be an integer or float')
    if not isinstance(b, int) or not isinstance(a, float):
        raise TypeError('b must be an integer or float')

    a = int(a)
    b = int(b)

    return a + b
