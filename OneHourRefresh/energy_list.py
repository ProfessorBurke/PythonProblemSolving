"""
    Obtain energy usage per capita for a single country over a series of
    years.  Report the highest, lowest, and average.
"""
from typing import TextIO

# Annotate variables.
file_name: str
file: TextIO
lines: list[str]
power_usage: float
total: float = 0
count: int = 0
max_usage: float = -1
min_usage: float = 10**6
i: int = 0

# Get the file name from the user and open the file.
file_name = input("What is the name of the file? ")
file = open(file_name)

# Read the lines from the file and close it.
lines = file.readlines()
file.close()

while i < len(lines):
    power_usage = float(lines[i])
    # Add the current value to the total.
    total += power_usage
    # Increment the count of values read.
    count += 1
    # Check if this value is the minimum or maximum so far.
    if power_usage > max_usage:
        max_usage = power_usage
    if power_usage < min_usage:
        min_usage = power_usage
    i += 1


# Display the average, min, and max usage values.
if count != 0:
    print(f"The average usage is {total/count:.3f}.")
    print(f"The max usage is {max_usage}.")
    print(f"The min usage is {min_usage}.")



