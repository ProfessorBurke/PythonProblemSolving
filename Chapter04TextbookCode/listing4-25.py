"""Read vocabulary information from a file
   and produce a table."""

import os.path
import typing

file_name: str
vocabulary_file: typing.TextIO
language1: str
language2: str
vocabulary1: str
vocabulary2: str

# Obtain the file name from the user, check
# that it exists, and open it if so.
file_name = input("Please enter the file name: ")
if os.path.isfile(file_name):
    vocabulary_file = open(file_name)

    # Read the header record from the file
    # and print the table header.
    language1 = vocabulary_file.readline().strip()
    language2 = vocabulary_file.readline().strip()

    print("{:35s}{:35s}".format(language1, language2))

    # Read the vocabulary from the file until the end
    # and print the vocabulary table lines.
    vocabulary1 = vocabulary_file.readline().strip()
    while vocabulary1 != "":
        vocabulary2 = vocabulary_file.readline().strip()
        print("{:35s}{:35s}".format(vocabulary1, vocabulary2))
        vocabulary1 = vocabulary_file.readline().strip()

# Display an error if the file was not found.
else:
    print("That file was not found.")
