"""Sum and average the values in a list."""

from typing import List

def main():
    average: float
    total: int = 0
    i: int = 0
    
    # Declare list of rainfall data.
    inches: List[float] = [0, .2, .22, .16, 0, .31, 0]

    # Loop over the list and sum the values.
    while i < len(inches):
        total += inches[i]
        i += 1

    # Average the values.
    if len(inches) != 0:
        average = total / len(inches)

        # Display the total and average.
        print("The total rainfall is {:.2f} and the average is {:.2f}."\
              .format(total, average))
    else:
        print("There is no rainfall data.")

main()
