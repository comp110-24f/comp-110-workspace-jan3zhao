"""where you implement some more list utility functions"""

__author__ = "730776252"


def only_evens(xs: list[int]) -> list[int]:
    """Return a list of only the even elements from the input list."""
    result = []
    for x in xs:
        if x % 2 == 0:
            result.append(x)
    return result


def sub(xs: list[int], start: int, end: int) -> list[int]:
    """Return subset of the input list, between the start index and end index."""
    result = []
    if len(xs) == 0 or start >= len(xs) or end <= 0:
        return result

    if start < 0:
        start = 0
    if end > len(xs):
        end = len(xs)

    for i in range(start, end):
        result.append(xs[i])

    return result


def add_at_index(xs: list[int], value: int, index: int) -> None:
    """Insert an element at a given index in the list, mutating the input list."""
    if index < 0 or index > len(xs):
        raise IndexError("Index is out of bounds for the input list")

    xs.append(0)  # Add space at the end
    for i in range(len(xs) - 1, index, -1):
        xs[i] = xs[i - 1]

    xs[index] = value
