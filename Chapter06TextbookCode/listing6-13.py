"""Display state data stored in parallel lists."""

from typing import List

def main() -> None:
    """Declare the lists and print related elements."""

    i: int = 0
    states: List[str] = ["DE", "PA", "NJ", "GA", "CT", "MA"]
    years: List[int] = [1787, 1787, 1787, 1788, 1788, 1788]

    # Iterate over state and year data and display.
    if len(states) == len(years):
        while i < len(states):
            print("{} joined the union in {}."
                  .format(states[i], years[i]))
            i += 1

main()
