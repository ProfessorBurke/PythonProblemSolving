"""
    Ask the user for a file name, open the file, read a
    line, and tell the user if the file is empty or not.
"""
# Import os.path to check if the file exists
# and io to annotate the file reference variable.
import os.path
import io

# Annotate variables.
line: str
filename: str
file: io.TextIOWrapper

# Obtain the file name and, if it exists, open the file.
filename = input("What is the name of the file? ")
if os.path.isfile(filename):
    file = open(filename, "r")

    # Read the first line or end of file marker.
    line = file.readline()

    # If the first line is equal to end of file, let the
    # user know the file is empty, otherwise tell them it's not.
    if line == "":
        print("{} is empty.".format(filename))
    else:
        print("{} is not empty.".format(filename))

    file.close()
else:
    print("Can't find {}.  Check the spelling and location.".format(filename))
