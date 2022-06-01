"""Find the highest rainfall value."""

from typing import List

def main():
    average: float
    total: int = 0
    i: int = 1
    i_largest: int = 0
    
    # Declare list of rainfall data.
    inches: List[float] = [0, .2, .22, .16, 0, .31, 0]

    # Loop over the list and count the days no rain fell.
    while i < len(inches):
        if inches[i] > inches[i_largest]:
            i_largest = i
        i += 1

    # Display the largest value.
    if len(inches) != 0:
        print("The largest value is {:.2f}."
              .format(inches[i_largest]))
    else:
        print("There is no rainfall data.")

main()



