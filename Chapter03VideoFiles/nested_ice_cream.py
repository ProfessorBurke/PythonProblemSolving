"""
    Obtain the user's favorite flavor of ice cream and
    print a special message if it's coffee.
"""

# Annotate variables.
favorite_flavor: str
from_RI: str

# Ask the user their favorite flavor.
favorite_flavor = input("What is your favorite ice cream flavor? ")

# Print a special message if the user's favorite ice cream flavor is coffee.
if favorite_flavor == "coffee":
    from_RI = input("Are you from Rhode Island? (yes/no)")
    if from_RI == "yes":
        print("You must also love Del's!")
elif favorite_flavor == "vanilla":
    print("Classic.")
elif favorite_flavor == "peanut butter cup":
    print("You must be American.")
else:
    print("{} sounds delicious!".format(favorite_flavor))
    
