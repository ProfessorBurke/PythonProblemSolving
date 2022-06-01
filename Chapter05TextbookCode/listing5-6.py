"""Program to demonstrate function returns."""
import math, random

rand_num: int
root: float
rounded_root: int

# Generate a random number between 1 and 100.
rand_num = random.randint(1, 100)
print("Your lucky number is {}!".format(rand_num))

# Take the square root, round it, and print.
root = math.sqrt(rand_num)
rounded_root = round(root)
print("Or maybe it's {}.".format(rounded_root))
