"""Create a weekly list of daily hours and display it."""

from typing import List

def main() -> None:
    """Declare the list of hours and print each element."""

    week: int
    day: int = 0
    hours: List[List[float]] = [[0, 1.5, 0, 1, 0, 3, 0],
	     [0, 2, 0, 1, 0, 2, 0],
	     [0, 1, 0, 1, 0, 0, 3]]

    # Iterate over each column.
    # Each column is one day of the week.
    while day < len(hours[0]):
        # Iterate over each row.
        # Each row is a week.
        week = 0
        while week < len(hours):
            print("Hours worked on day {} of week {} is {}."
                  .format(day, week, hours[week][day]))
            week += 1
        day += 1

main()
