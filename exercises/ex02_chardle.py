"""EX02 - Chardle - A cute step towards Wordle."""

__author__ = "730776252"


def main() -> None:
    """had a hard time making sure functions were called in right order.
    i put main at the end at first.
    used main properly + placed at beginning to make code more organized"""

    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    """checks if len is same in user input and word, returns word"""
    user_input = input("Please enter a 5-character word: ")
    if len(user_input) == 5:
        return user_input
    else:
        print("Error: Word must contain 5 characters.")
        exit()


def input_letter() -> str:
    """checks if input is a char, returns user input"""
    user_input = input("Please enter a single character: ")

    if len(user_input) == 1:
        return user_input
    else:
        print("Error: Character must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    """checks input chars equal to the index of the word"""
    count = 0
    print(f"Searching for {letter} in {word}")
    if word[0] == letter:
        print(f"{letter} found at index 0")
        count += 1
    if word[1] == letter:
        print(f"{letter} found at index 1")
        count += 1
    if word[2] == letter:
        print(f"{letter} found at index 2")
        count += 1
    if word[3] == letter:
        print(f"{letter} found at index 3")
        count += 1
    if word[4] == letter:
        print(f"{letter} found at index 4")
        count += 1
    if count == 0:
        print(f"No instances of {letter} found in {word}")
    elif count == 1:
        print(f"1 instance of {letter} found in {word}")
    else:
        print(f"{count} instances of {letter} found in {word}")


if __name__ == "__main__":
    main()
