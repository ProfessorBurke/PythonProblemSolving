"""
    Ask the user for their three favorite flavors of ice cream.
    Then repeat them back.
"""

# Annotate variables.
flavor1: str
flavor2: str
flavor3: str

# Obtain the user's three favorite flavors.
flavor1 = input("What is your favorite ice cream flavor? ")
flavor2 = input("And your second favorite flavor? ")
flavor3 = input("What's your third favorite flavor? ")

# Repeat the favorite flavors back to the user.
print("Your three favorite ice cream flavors are {}, {}, and {}."
      .format(flavor1, flavor2, flavor3))
