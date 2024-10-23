"""Challenge Question 04 - Coordinates"""

__author__ = "730776252"


def get_coords(xs: str, ys: str) -> None:
    """Prints out formatted pairs of each character in 2 input strings"""
    i = 0
    while i < len(xs):
        j = 0
        while j < len(ys):
            print(f"({xs[i]}, {ys[j]})")
            j += 1
        i += 1
