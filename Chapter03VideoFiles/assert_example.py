"""
    Illustrate some examples of complements and assertions.
"""

# Annotate variables.
temperature: int

# Obtain a temperature from the user.
temperature = int(input("What is the temperature (F) outside? "))

# Print a message depending on whether it's more than 50 degrees.
if temperature > 50:
    print("It sounds like a lovely day.")
else:
    # This assertion causes an error when the user enters 50 at the prompt.
    assert temperature < 50
    # This assertion is the complement of temperature > 50 and is correct.
    assert temperature <= 50
    print("It seems a little chilly.")
