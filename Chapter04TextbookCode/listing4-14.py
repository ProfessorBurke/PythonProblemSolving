"""Sentinel loop to obtain, process, and store information
   about runners."""

import typing

runners: typing.TextIO
age: int
name: str
division: str

# Obtain the runner's age.
age = int(input("Please enter the runner's age, -1 to quit: "))

# Open the file.
runners = open("runners.txt", "w")

# Loop until the user enters -1 for age, 
# obtaining name and determining division. 
while age != -1:
    name = input("Please enter the runner's name: ")
    if age < 12:
        division = "Under 12 division"
    elif age < 20:
        division = "12 - under 20 division"
    elif age < 40:
        division = "20 - under 40 division"
    else:
        division = "40+ division"
    # Write runner information to the file.
    runners.write(name + "\t" + str(age) + "\t" + division + "\n")
    age = int(input("Please enter the runner's age, -1 to quit: "))

# Close the runner information file.
runners.close()
