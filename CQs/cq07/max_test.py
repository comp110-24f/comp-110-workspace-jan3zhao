__author__ = "730776252"

import unittest
from find_max import find_and_remove_max


class TestFindAndRemoveMax(unittest.TestCase):

    def test_return_value(self) -> None:  # Added return type annotation
        lst: list[int] = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        result = find_and_remove_max(lst)
        self.assertEqual(result, 9)

    def test_mutation(self) -> None:  # Added return type annotation
        lst: list[int] = [7, 3, 7, 2, 7]
        find_and_remove_max(lst)
        self.assertEqual(lst, [3, 2])

    def test_empty_list(self) -> None:  # Added return type annotation
        lst: list[int] = []  # Added type annotation for lst
        result = find_and_remove_max(lst)
        self.assertEqual(result, -1)
        self.assertEqual(lst, [])

    def test_all_elements_same(self) -> None:  # Added return type annotation
        lst: list[int] = [5, 5, 5, 5]  # Added type annotation for lst
        result = find_and_remove_max(lst)
        self.assertEqual(result, 5)
        self.assertEqual(lst, [])


if __name__ == "__main__":
    unittest.main()
