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
name: str
candy: str
amount: int
most_name: str
most_candy: str
largest_amount: int = -1
filename: str
halloween_file: io.TextIOWrapper

# Obtain the file name and, if it exists, open the file.
filename = input("What is the name of the file? ")
if os.path.isfile(filename):
    halloween_file = open(filename, "r")

    # Read the three flavors
    name = halloween_file.readline().strip()
    while name != "":
        # Finish reading a record.
        candy = halloween_file.readline().strip()
        amount = int(halloween_file.readline())
        
        # Process the record.
        print("{} got {} {}.".format(name, amount, candy))
        if amount > largest_amount:
            largest_amount = amount
            most_name = name
            most_candy = candy

        # Read the start of the next record or eof.
        name = halloween_file.readline().strip()

    # Display the person who got the most candy, as long as the
    # file wasn't empty.
    if largest_amount != -1:
        print("{} got the most candy: {} {}.".format(most_name, largest_amount, most_candy))
    halloween_file.close()
else:
    print("Can't find {}.  Check the spelling and location.".format(filename))
