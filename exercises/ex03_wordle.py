"""Structured Wordle!"""

__author__ = "730776252"


def input_guess(secret_word_len: int) -> str:
    """Prompts the user for a guess of the correct length."""
    guess = input(f"Enter a {secret_word_len} character word: ")
    """while loop to keep prompting user if user doesnt enter the length"""
    while len(guess) != secret_word_len:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Returns True if char_guess is in secret_word, otherwise False."""
    assert len(char_guess) == 1
    """index variable to use with while loop"""
    idx = 0
    """while loop to iterate through secret word
    checks if indexed character is equal to char of guess"""
    while idx < len(secret_word):
        if secret_word[idx] == char_guess:
            return True
        idx += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emoji boxes representing guess accuracy."""
    assert len(guess) == len(secret)
    """empty string to concatenate emoji boxes"""
    result = ""
    """index variable for while loop"""
    idx = 0
    """while loop that iterates through guess word
      checks if char is equal to secret char, or in secret word"""
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        idx += 1
    return result


def main(secret: str) -> None:
    """The entry point of the program and main game loop."""
    count: int = 1
    guess: str = ""
    """while loop that lets the game play out if less than 6 turns and not won"""
    while count <= 6:
        print(f"=== Turn {count}/6 ===")
        guess = input_guess(len(secret))
        emoji_result: str = emojified(guess, secret)
        print(emoji_result)

        if guess == secret:
            print(f"You won in {count}/6 turns!")
            return
        count += 1

        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
