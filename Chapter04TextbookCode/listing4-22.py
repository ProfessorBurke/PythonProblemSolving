"""Sum a number of user-entered values."""

num_values: int
value: int

# Initialize the sum.
value_sum: int = 0

# Obtain the number of values to read.
num_values = int(input("How many values? "))

# Read in and sum the values.
for i in range(num_values):
    value = int(input("Enter a value: "))
    value_sum += value

# Display the sum.
print("The sum is {}.".format(value_sum))
