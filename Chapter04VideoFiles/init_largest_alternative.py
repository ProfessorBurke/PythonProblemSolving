"""
    Obtain values from the user and report on their
    properties.
"""

# Annotate variables.
number: int
i: int
total: int
largest: int

# Obtain values from the user.
i = 0
total = int(input("Please enter a number: "))
largest = total
while i < 4:
    number = int(input("Please enter a number: "))
    if number > largest:
        largest = number
    total += number
    i += 1
