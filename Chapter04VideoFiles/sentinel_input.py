"""
    Obtain values from the user and report on their
    properties.
"""
import sys

# Annotate variables.
number: int
total: int
largest: int
input_value: str
count: int

# Obtain values from the user.
count = 0
total = 0
largest = -sys.maxsize - 1
input_value = input("Please enter a number or Q to quit: ")
while input_value != "Q":
    number = int(input_value)
    if number > largest:
        largest = number
    total += number
    count += 1
    input_value = input("Please enter a number or Q to quit: ")

if count != 0:
    print("The total is {}.".format(total))
    print("The largest value entered is {}.".format(largest))
else:
    print("No values were entered.")
