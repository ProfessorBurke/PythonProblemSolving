"""Compute the current across a circuit with a
   350 ohm resistor and a battery."""

battery: str
current: float

# Set a constant for the resistor.
RESISTANCE: int = 350

# Obtain the type of the battery.
battery = input("Please enter N for a 9V battery and T for 12V: ")

# Compute the current.
if battery == "N":
    current = 9 / RESISTANCE
else:
    assert battery == "T"
    current = 12 / RESISTANCE

# Display the current.
print("The amperage of the circuit is {:.3f}.".format(current))
