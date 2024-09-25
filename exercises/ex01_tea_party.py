"""
Determines supplies needed and total cost depending on the amount of guests.
"""

__author__ = "730776252"


def tea_bags(people: int) -> int:
    """
    Calculates how many tea bags are needed. Each guest will have two bags of tea.
    """
    return people * 2


def treats(people: int) -> int:
    """
    Calculates how many treats are needed depending on the number of tea bags.
    Each cup of tea should correspond to 1.5 treats.
    """
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """
    Calculate the total cost of the tea bags and treats.
    """
    return (tea_count * 0.5) + (treat_count * 0.75)


def main_planner(guests: int) -> None:
    """
    Main function to plan the tea party. It calculates the number of tea bags,
    treats, and cost, then prints out the results.

    I tried calculating within the main function before noticing
    the exercise instructions said that we should not be performing
    any arithmetic computations within the planner.
    I then realized I should be calling the helper functions and fixed my code.

    I struggled a lot with having ghost variables in my code.
    I learned that it is better to have my code be concise.
    To combat this, I embedded and called my variables within the function.
    """
    print("A Cozy Tea Party For " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
