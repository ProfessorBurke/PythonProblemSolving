"""Sentinel loop to average runner ages from a file."""

import typing

# Initialize the sum and count.
total_ages: int = 0
count: int = 0
age_str: str
age: int
ages_file: typing.TextIO

# Open the file and read the first line.
ages_file = open("ages.txt")
age_str = ages_file.readline()

# Add age to sum, increment count, obtain age until the end of file.
while age_str != "":
    age = int(age_str)
    total_ages += age
    count += 1
    age_str = ages_file.readline()
    
# If any ages were entered, average them.
if count != 0:
    average = total_ages / count
    print("The average age is {:.1f}.".format(average))
else:
    print("There were no ages in the file.")

ages_file.close()
