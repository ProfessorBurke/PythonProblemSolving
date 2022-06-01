"""Reduce a fraction to lowest terms."""

def gcd(a: int, b: int) -> int:
    """Compute and return the gcd of a and b
       using Euclid's algorithm."""
    remainder: int
    remainder = b % a
    while remainder != 0:
        b = a
        a = remainder
        remainder = b % a
    return a

def main() -> None:
    """Obtain a fraction from the user and reduce."""
    numerator: int
    denominator: int
    fraction_gcd: int
    
    # Obtain the fraction.
    numerator = int(input("Please enter the numerator: "))
    denominator = int(input("Please enter the denominator: "))

    # Find the greatest common divisor.
    fraction_gcd = gcd(abs(numerator), abs(denominator))

    # Divide the numerator and denominator by the gcd.
    numerator = numerator // fraction_gcd
    denominator = denominator // fraction_gcd

    # Display the reduced fraction
    print("The fraction is {}/{}."
          .format(numerator, denominator))

main()
