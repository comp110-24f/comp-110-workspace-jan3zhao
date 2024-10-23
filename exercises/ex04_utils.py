"""list Utility Functions!"""

__author__ = "730776252"


def all(lst: list[int], n: int) -> bool:
    """Check if all elements in the list are equal to a given integer.
    lst (list[int]): The list of integers to check.
    n (int): The integer to compare each element of the list against."""
    if len(lst) == 0:
        return False  # Early return if list is empty

    for element in lst:
        """
        element (int): The current integer being checked in the list.
        """
        if element != n:
            return False  # Return False immediately if any element is not equal to n

    return True  # Return True if all elements match n


def max(lst: list[int]) -> int:
    """Find and return the largest integer in the list.
    lst (list[int]): The list of integers from which to find the maximum.
    int: The largest integer in the list.
    """
    if len(lst) == 0:
        raise ValueError("max() arg is an empty List")  # Error if list is empty

    max_value = lst[0]
    """ max_value (int): The current largest integer found in the list, initialized
    to the first element of the list."""

    for element in lst:
        """element (int): The current integer being compared to max_value."""
        if element > max_value:
            max_value = element  # Update max_value if a larger element is found

    return max_value  # Return the largest value found


def is_equal(lst1: list[int], lst2: list[int]) -> bool:
    """Check if two lists are deeply equal, meaning all elements at each index are equal
    lst1 (list[int]): The first list of integers.
    lst2 (list[int]): The second list of integers."""
    if len(lst1) != len(lst2):
        return False  # Return False if lists have different lengths

    for i in range(len(lst1)):
        """i (int): The current index in the lists where elements are being compared."""
        if lst1[i] != lst2[i]:
            return (
                False  # Return False immediately if any pair of elements is not equal
            )

    return True  # Return True if all elements match in both lists


def extend(lst1: list[int], lst2: list[int]) -> None:
    """Append all elements from the second list to the first list.
    lst1 (list[int]): The first list, which will be extended with elements from lst2.
    lst2 (list[int]): The second list, whose elements will be appended to lst1.
    """
    for element in lst2:
        """element (int): The current integer from lst2 being appended to lst1."""
        lst1.append(element)  # Append each element from lst2 to lst1
