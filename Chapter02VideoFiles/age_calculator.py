"""
    Obtain the year the user was born, calculate their age,
    and report their age.
"""

# Annotate variables and constants.
CURRENT_YEAR: int
birth_year: int
age: int

CURRENT_YEAR = 2024

# Obtain the user's birth year.
birth_year = int(input("Please enter your birth year: "))

# Calculate the user's age this year.
age = CURRENT_YEAR - birth_year

# Report the user's age.
print("You will be", age, "years old this year.")
