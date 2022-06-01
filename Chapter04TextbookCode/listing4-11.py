"""Sentinel loop to place runners in the
   correct division."""

age: int

# Obtain the runner's age.
age = int(input("Please enter the runner's age, -1 to quit: "))

# Loop until the user enters -1, printing the division
# and obtaining the next age.
while age != -1:
    if age < 12:
        print("Under 12 division")
    elif age < 20:
        print("12 - under 20 division")
    elif age < 40:
        print("20 - under 40 division")
    else:
        print("40+ division")
    age = int(input("Please enter the runner's age, -1 to quit: "))
