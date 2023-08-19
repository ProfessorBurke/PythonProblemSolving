"""
    Ask the user for a file name, open the file, and read
    three ice cream flavors from the file and tell them to
    the user.
"""
# Import os.path to check if the file exists
# and io to annotate the file reference variable.
import os.path
import io

# Annotate variables.
flavor: str
num_chocolate: int = 0
filename: str
icecream_file: io.TextIOWrapper

# Obtain the file name and, if it exists, open the file.
filename = input("What is the name of the file? ")
if os.path.isfile(filename):
    icecream_file = open(filename, "r")

    # Read the three flavors
    flavor = icecream_file.readline().strip()
    while flavor != "":
        print(flavor)
        if "chocolate" in flavor.lower():
            num_chocolate += 1
        flavor = icecream_file.readline().strip()

    print("The number of chocolate flavors is {}.".format(num_chocolate))
    icecream_file.close()
else:
    print("Can't find {}.  Check the spelling and location.".format(filename))
