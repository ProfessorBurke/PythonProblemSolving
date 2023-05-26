"""
    Demonstrate avoiding divide by zero.
"""

# Annotate variables.
dividend: float
divisor: float
quotient: float

# Obtain two values from the user.
dividend = float(input("Please enter a number: "))
divisor = float(input("Please enter another number: "))

if divisor != 0:
    # Divide the first value by the second.
    quotient = dividend / divisor

    # Display the quotient to the user.
    print("The result of {}/{} is{}.".format(dividend, divisor, quotient))
