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
flavor1: str
flavor2: str
flavor3: str
filename: str
icecream_file: io.TextIOWrapper
number: int

# Obtain the file name and, if it exists, open the file.
filename = input("What is the name of the file? ")
if os.path.isfile(filename):
    icecream_file = open(filename, "r")

    # Read the three flavors
    flavor1 = icecream_file.readline()
    flavor1 = flavor1.strip()
    flavor2 = icecream_file.readline().strip()
    flavor3 = icecream_file.readline().strip()
    number = int(icecream_file.readline())

    # Repeat the favorite flavors back to the user.
    print("Your three favorite ice cream flavors are {}, {}, and {}."
          .format(flavor1, flavor2, flavor3))

    icecream_file.close()
else:
    print("Can't find {}.  Check the spelling and location.".format(filename))
