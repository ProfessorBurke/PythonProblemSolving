"""Simulate the roll of two d6, sum, and display the result."""

import random

sum_dice: int

# Simulate the rolls.
die1: int = random.randint(1,6)
die2: int = random.randint(1,6)

# Sum the rolls.
sum_dice = die1 + die2

# Display the result.
print("You rolled {}.".format(sum_dice))
