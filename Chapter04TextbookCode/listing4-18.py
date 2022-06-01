"""Program to check whether a file exists."""

import os.path

file_name: str

# Obtain a file name from the user.
file_name = input("Enter the file name: ")

# Check if the file is in the same directory as
# the program, and report.
if os.path.isfile(file_name):
    print("The file exists.")
else:
    print("That file was not found.")
