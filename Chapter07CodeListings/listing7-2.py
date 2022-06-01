"""Find the greatest common divisor of two integers."""

def gcd(a: int, b: int) -> int:
    """Compute and return the gcd of a and b
       using Euclid's algorithm."""
    remainder: int = b % a
    if remainder == 0:
        return a
    else:
        return gcd(remainder, a)

def main() -> None:
    """Obtain two integers from the user and find the gcd."""
    # Obtain two integers.
    a: int = int(input("Please enter an integer: "))
    b: int = int(input("Please enter another integer: "))

    # Find the greatest common divisor.
    greatest_divisor: int = gcd(abs(a), abs(b))

    # Display the greatest common divisor.
    print("The greatest common divisor of {} and {} is {}." 
          .format(a, b, greatest_divisor))

main()
