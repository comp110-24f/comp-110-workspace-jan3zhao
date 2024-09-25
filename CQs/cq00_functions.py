"""My first Challenge Question in COMP110!"""

__author__ = "730776252"


def mimic(message: str) -> str:
    """A function that mimics what you input."""
    return message


def main() -> None:
    """This prints the result of calling mimic."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
