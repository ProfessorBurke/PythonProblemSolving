"""Count the days no rain fell in a list of rainfall data."""

from typing import List

def main():

    num_dry: int = 0
    i: int = 0

    # Declare list of rainfall data.
    inches: List[float] = [0, .2, .22, .16, 0, .31, 0]

    # Loop over the list and count the days no rain fell.
    while i < len(inches):
        if inches[i] == 0:
            num_dry += 1
        i += 1

    # Display the number of days no rain fell.
    print("No rain fell on {} days.".format(num_dry))

main()
