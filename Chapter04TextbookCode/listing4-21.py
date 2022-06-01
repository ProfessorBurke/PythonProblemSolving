"""Compute the sum of even numbers from 2 to 100."""

next_even: int

# Initialize the sum.
even_sum: int = 0

# Add the next even number to the sum.
for next_even in range(2, 101, 2):
    even_sum += next_even

# Display the sum.
print("The sum of the even numbers from 2 to 100 " +\
      "is {:d}.".format(even_sum))
