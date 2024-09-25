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
        print("Error: Input must be a single character.")
        exit()


def contains_char(word: str, letter: str) -> None:
    """checks input chars equal to the index of the word using loop"""
    count = 0
    """to count the # of character matches:
    initialized count to zero + incremented it within the loop.
    had to play around w/ it a bit to figure out the conditionals"""
    for index in range(len(word)):
        if word[index] == letter:
            print(f"Letter '{letter}' found at index {index}.")
            count += 1
    if count == 0:
        print(f"No instance of '{letter}' found in the word.")
    elif count == 1:
        print(f"1 instance of '{letter}' found in the word.")
    else:
        print(f"{count} instance of '{letter}' found in the word.")


if __name__ == "__main__":
    main()
