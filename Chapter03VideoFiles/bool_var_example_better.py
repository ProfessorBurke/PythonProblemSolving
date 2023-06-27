"""
    Illustrate some examples of complements and assertions.
"""

# Annotate variables.
temperature: int
is_warm: bool

# Obtain a temperature from the user.
temperature = int(input("What is the temperature (F) outside? "))

# Print a message depending on whether it's more than 50 degrees.
is_warm = temperature > 50

if is_warm:
    print("Turn the cooling system on.")
