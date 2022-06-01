"""Display state data stored in a list of records."""

from typing import List

def main() -> None:
    """Declare the list and print each record."""
    NAME: int = 0
    YEAR: int = 1
    i: int = 0

    states: List[List] = [["DE", 1787], ["PA", 1787], ["NJ", 1787],
                          ["GA", 1788], ["CT", 1788], ["MA", 1788]]

    # Iterate over state data and display.
    while i < len(states):
        print("{} joined the union in {}."
                .format(states[i][NAME], states[i][YEAR]))
        i += 1

main()
