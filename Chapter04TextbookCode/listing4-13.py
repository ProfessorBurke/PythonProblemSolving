"""Write a string, an integer, and a float to a file."""

import typing

simple_file: typing.TextIO

# Open the file in write mode.
simple_file = open("three_values.txt", "w")

# Write three values to the file.
simple_file.write("Hello, world!")
simple_file.write(str(5))
simple_file.write(str(2.71828))

# Close the file.
simple_file.close()
