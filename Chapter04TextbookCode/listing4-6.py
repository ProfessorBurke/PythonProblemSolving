"""Compute the current for five circuits from 
   resistance and voltage obtained from the user."""

voltage: float
resistance: float
current: float

# Initialize the loop control variable.
i: int = 0

# Ask for five sets of values, compute
# and display the result.
while i < 5:
    voltage = float(input("What is the voltage? "))
    resistance = float(input("What is the resistance? "))
    current = voltage / resistance
    print("The amperage of the circuit is {:.3f}.".format(current))
    i += 1
