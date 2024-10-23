"""where you define unit tests for them"""

__author__ = "730776252"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index


def test_only_evens_all_even():
    """Test only_evens with all even numbers.
    It should return the same list since all elements are even."""
    assert only_evens([2, 4, 6]) == [2, 4, 6]


def test_only_evens_mixed():
    """Test only_evens with a mix of odd and even numbers.
    It should return only the even numbers in the list."""
    assert only_evens([1, 2, 3, 4, 5]) == [2, 4]


def test_only_evens_empty():
    """Test only_evens with an empty list.
    It should return an empty list."""
    assert only_evens([]) == []


def test_sub_normal():
    """Test sub with normal start and end indexes.
    It should return the subset from the start index to end index (exclusive)."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_negative_start():
    """Test sub with a negative start index.
    It should treat the negative start index as 0 and return the correct subset."""
    assert sub([10, 20, 30, 40], -1, 3) == [10, 20, 30]


def test_sub_out_of_bounds():
    """Test sub with an end index greater than the list length.
    It should return a subset up to the end of the list."""
    assert sub([10, 20, 30, 40], 1, 10) == [20, 30, 40]


def test_add_at_index_normal():
    """Test add_at_index with a valid index.
    It should insert the value at the specified index and modify the list in place."""
    xs = [1, 2, 3]
    add_at_index(xs, 4, 1)
    assert xs == [1, 4, 2, 3]


def test_add_at_index_out_of_bounds():
    """Test add_at_index with an index out of bounds. It should raise an IndexError."""
    xs = [1]
    with pytest.raises(IndexError):
        add_at_index(xs, 2, 5)


def test_add_at_index_empty():
    """Test add_at_index with an empty list.
    It should correctly insert the value at index 0."""
    xs = []
    add_at_index(xs, 1, 0)
    assert xs == [1]
