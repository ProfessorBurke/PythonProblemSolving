"""
    Obtain values from the user and report on their
    properties.
"""
import sys

# Annotate variables.
number: int
i: int
total: int
largest: int

# Obtain values from the user.
i = 0
total = 0
largest = -sys.maxsize - 1
while i < 5:
    number = int(input("Please enter a number: "))
    if number > largest:
        largest = number
    total += number
    i += 1

# Display the properties of the numbers.
print("The total is {}.".format(total))
print("The largest value entered is {}.".format(largest))
