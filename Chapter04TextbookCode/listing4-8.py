"""Find the largest value entered by the user."""

largest: float
number: float

# Obtain the first value to initialize the most wanted holder.
largest = float(input("Please enter a value: "))

# Obtain four more values from the user in a loop
# and find the largest.
i: int = 0
while i < 4:
    number = float(input("Please enter a value: "))
    if number > largest:
        largest = number
    i += 1

# Display the largest number entered to the user.
print("The largest number entered was {:.1f}.".format(largest))
