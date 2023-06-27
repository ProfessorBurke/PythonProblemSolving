"""
    Illustrate some examples of complements and assertions.
"""

# Annotate variables.
temperature: int
is_warm: bool

# Obtain a temperature from the user.
temperature = int(input("What is the temperature (F) outside? "))

# Print a message depending on whether it's more than 50 degrees.
if temperature > 50:
    is_warm = True
else:
    assert temperature <= 50
    is_warm = False

if is_warm:
    print("Turn the cooling system on.")
