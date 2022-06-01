"""Create a weekly list of daily hours and display it."""

from typing import List

def main() -> None:
    """Declare the list of hours and print each element."""

    week: int = 0
    day: int
    hours: List[List[float]] = [[0, 1.5, 0, 1, 0, 3, 0], 
                                [0, 2, 0, 1, 0, 2, 0],
	                        [0, 1, 0, 1, 0, 0, 3]]

    # Iterate over each row. Each row is one week.
    while week < len(hours):
        # Iterate over each column element.
        # Each column element is one day of the week.
        day = 0
        while day < len(hours[week]):
            print("Hours worked on week {}, day {} is {}."
                  .format(week, day, hours[week][day]))
            day += 1
        week += 1

main()
