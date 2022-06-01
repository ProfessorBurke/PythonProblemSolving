"""BUGGY Program to suggest a dessert."""

preference: str
kind_of_chocolate: str

# Get the user's preference.
preference = input("Chocolate or fruit for dessert? ")

# Get more information.
if preference == "chocolate":
    kind_of_chocolate = input("Do you prefer dark or milk? ")

# Suggest a dessert.
print("You should try a fruit salad.")
if kind_of_chocolate == "dark":
    print("You should try a dark chocolate truffle.")
else:
    print("You should try a milk chocolate bar.")
