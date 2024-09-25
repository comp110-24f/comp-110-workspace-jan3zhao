"""Using a while loop to iterate over a string"""

__author__ = "730776252"


def num_instances(phrase: str, search_char: str) -> int:
    i: int = 0
    count: int = 0
    while i < len(phrase):
        if search_char == phrase[i]:
            count += 1
        i += 1
    return count


print(num_instances(phrase="Happy Tuesday!", search_char="z"))
