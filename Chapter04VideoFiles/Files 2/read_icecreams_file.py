"""
    Ask the user for a file name, open the file, and read
    all the flavors from the file and display them to
    the console.
    Flavors are one to a line in the file.
"""
# Import os.path to check if the file exists
# and io to annotate the file reference variable.
import os.path
import io

# Annotate variables.
flavor: str
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
        flavor = icecream_file.readline().strip()

    icecream_file.close()
else:
    print("Can't find {}.  Check the spelling and location.".format(filename))
