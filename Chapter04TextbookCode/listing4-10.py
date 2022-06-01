"""Validate that the user's input is positive."""

age: int

# Obtain an age from the user.
age = int(input("Please enter an age: "))

# Loop if the age is less than zero
# until the user enters a positive value.
while age <= 0:
    print("Age must be a positive number.")
    age = int(input("Please enter an age: "))
assert age > 0

# The age is positive, display a message.
print("{:d} is a positive value.".format(age))
