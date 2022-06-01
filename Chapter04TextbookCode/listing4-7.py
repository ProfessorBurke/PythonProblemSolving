"""Compute the sum of the even numbers from 2 to 100."""

# Initialize the sum and first even number.
even_sum: int = 0
next_even: int = 2

# Add the next even number to the sum
# and increment to the next even number.
while next_even < 101:
    even_sum += next_even
    next_even += 2

print("The sum of the even numbers from 2 to 100 " +\
      "is {:d}.".format(even_sum))
