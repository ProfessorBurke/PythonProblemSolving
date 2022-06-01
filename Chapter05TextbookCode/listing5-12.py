"""Obtain a positive integer from the user."""

def is_positive(value: int) -> bool:
    """Return True if value is positive."""
    valid: bool = False
    if value > 0:
        valid = True
    return valid

def main() -> None:
    number: int
    
    # Obtain a value from the user.
    number = int(input("Enter a positive number: "))

    # Validate the input values.
    while not is_positive(number):
        print("That is not a positive number.")
        number = int(input("Enter a positive number: "))

    # Acknowledge the positive number.
    print("{} is a positive number.".format(number))

main()
