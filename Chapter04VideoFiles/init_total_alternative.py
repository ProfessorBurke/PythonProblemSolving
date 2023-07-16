"""
    Obtain values from the user and report on their
    properties.
"""

# Annotate variables.
number: int
i: int
total: int

# Obtain values from the user.
i = 0
total = int(input("Please enter a number: "))
while i < 4:
    number = int(input("Please enter a number: "))
    total += number
    i += 1
