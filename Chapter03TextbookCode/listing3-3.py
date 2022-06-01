"""Compute the current across a circuit with a 350 ohm resistor 
   and a battery."""

battery: str
current: float

# Set a constant for the resistor.
RESISTANCE: int = 350

# Obtain the type of the battery.
battery = input("Enter battery type (N for 9V, T for 12V, " +
                "O for 1.5V): ")

# Compute the current.
if battery == "N":
    current = 9 / RESISTANCE
elif battery == "O":
    current = 1.5 / RESISTANCE
else:
    current = 12 / RESISTANCE

# Display the current.
print("The amperage of the circuit is {:.3f}.".format(current))
