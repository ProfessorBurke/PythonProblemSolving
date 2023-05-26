"""
    Obtain the user's favorite flavor of ice cream and
    print a special message if it's coffee.
"""

# Annotate variables.
favorite_flavor: str

# Ask the user their favorite flavor.
favorite_flavor = input("What is your favorite ice cream flavor? ")

# Print a special message if the user's favorite ice cream flavor is coffee.
if favorite_flavor == "coffee":
    print("You must be from Rhode Island!")
    print("Do you know the Big Blue Bug?")
