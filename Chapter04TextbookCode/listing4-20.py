"""Compute the current for five circuits from 
   resistance and voltage obtained from the user."""

i: int
voltage: float
resistance: float
current: float

# Ask for five sets of values, compute
# and display the result.
for i in range(5):
    voltage = float(input("What is the voltage? "))
    resistance = float(input("What is the resistance? "))
    current = voltage / resistance
    print("The amperage of the circuit is {:.3f}.".format(current))
