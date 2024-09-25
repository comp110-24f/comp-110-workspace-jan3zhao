"""Practice with Conditionals, Local Variables, and User Input!"""

__author__ = "730776252"


def guess_a_number() -> None:
    """Prompts user to guess a number."""
    secret: int = 7
    x: int = int(input("Guess a number: "))
    print("Your guess was " + str(x))
    if x == 7:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))

    return None


if __name__ == "__main__":
    guess_a_number()
