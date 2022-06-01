"""Compute the weight of some components."""

weight: float
num_components: int
total_weight: float

# Obtain the weight and number of components
# from the user.
weight = float(input("What is the component weight? "))
num_components = int(input("How many components? "))

# Calculate the total weight.
total_weight = weight * num_components

# Display the total weight amount to the user.
print("Total weight of", num_components, "is", total_weight,".")

# String concatenation output (remove comment to use).
##print("Total weight of " + str(num_components) + " is "
##      + str(total_weight) + ".")

# Formatted output (remove comment to use).
##print("Total weight of {:d} is {:.2f}."
##      .format(num_components, total_weight))

