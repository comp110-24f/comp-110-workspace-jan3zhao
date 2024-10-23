"""Summing the elements of a list using different loops"""

__author__ = "730776252"


def w_sum(vals: list[float]) -> float:
    """Compute the sum of all elements in the list using a while loop.
    If the list is empty, return 0.0."""

    total = 0.0
    """total (float): Accumulates the sum of the elements in the list."""

    i = 0
    """i (int): The current index of the element being processed in the list."""

    while i < len(vals):
        total += vals[i]
        i += 1

    return total


def f_sum(vals: list[float]) -> float:
    """Compute the sum of all elements in the list using a for ... in ... loop.
    If the list is empty, return 0.0."""

    total = 0.0

    for val in vals:
        """val (float): The current float value being processed in the list."""
        total += val

    return total


def f_range_sum(vals: list[float]) -> float:
    """Compute the sum of all elements in the list using a for ... in range(...) loop.
    If the list is empty, return 0.0."""
    total = 0.0

    for i in range(len(vals)):
        """i (int): The current index being used to access elements in the list."""
        total += vals[i]

    return total
