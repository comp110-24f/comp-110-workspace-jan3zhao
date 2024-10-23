__author__ = "730776252"


def find_and_remove_max(lst: list[int]) -> int:
    """Finds the largest integer in input list, removes all its occurrences from list,
    and returns the largest integer. If the list is empty, returns -1.

    Troubleshooting:
    Had to check if the list is empty before calling `max()` to avoid a ValueError.
    Verify the list is being correctly mutated
    (all instances of the max value should be removed).
    """
    if not lst:
        return -1

    max_value = max(lst)  # Find the max value
    while max_value in lst:
        lst.remove(max_value)  # Remove all instances of the max value

    return max_value
