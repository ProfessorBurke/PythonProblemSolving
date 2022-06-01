"""Count randomly generated numbers."""
from random import randint
from typing import List

def random_rolls() -> List[int]:
    """Generate and return a list of 1000 random rolls."""
    i: int
    # Create an empty list to hold the rolls.
    rolls: List[int] = []
    # Generate 1000 random rolls.
    for i in range(1000):
        rolls.append(randint(1,6))
    # Return the list of random values.
    return rolls

def main() -> None:
    """Count the frequency of randomly generated numbers."""
    i: int
    # Get 1000 random numbers between 1 and 6.
    numbers: List[int] = random_rolls()

    # Count and display the number of each value.
    for i in range(6):
        print("The number of {}'s generated was {}."
              .format(i+1, numbers.count(i+1)))
    
main()
