"""Reading a string, an integer, and a float from a file."""

import typing

simple_file: typing.TextIO
greeting: str
int_number: int
float_number: float

# Open the file in read mode.
simple_file = open("three_values.txt")

# Read three values from the file.
greeting = simple_file.readline()
greeting = greeting.strip()
int_number = int(simple_file.readline())
float_number = float(simple_file.readline())

# Print them all.
print(greeting, int_number, float_number)

# Close the file.
simple_file.close()
