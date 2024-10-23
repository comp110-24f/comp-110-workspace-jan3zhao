"""Mutating functions"""

__author__ = "730776252"


def manual_append(lst: list[int], to_append: int) -> None:
    lst.append(to_append)


def double(lst: list[int]) -> None:
    i: int = 0
    while i < len(lst):
        lst[i] *= 2
        i += 1


"""global variables"""
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

"""calling the double function on list_2"""
double(list_2)

"""printing both lists"""
print("list_1:", list_1)
"""output: [2, 4, 6]"""
print("list_2:", list_2)
"""output: [2, 4, 6]"""
