"""Calculate the cost of shipping a box."""

package_type: str
size: str
cost: float

# Obtain the type of package.
package_type = input("Is the package a (B)ox or (E)nvelope? ")

# Calculate the cost for a package.
if package_type == "B":

    # Obtain the size.
    size = input("Is the package (S)mall or (L)arge? ")
    # Assign the cost based on size.
    if size == "S":
        cost = 8.15
##        print("Inside S size if, cost = {}.".format(cost))
##        print("Size = {}.".format(size))
    else:
        cost = 21.25

    # Display the cost.
    print("The cost for your box is ${:.2f}.".format(cost))

