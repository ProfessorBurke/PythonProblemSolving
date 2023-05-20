"""
    Demonstrate inputting values of different types
    and displaying output.
"""

# Annotate variables.
word: str
num_pencils: int
value_change: float
double_word: str
double_pencils: int
double_change: float

# Obtain a word, number of pencils, and value of change from the user.
word = input("Please enter a word: ")
num_pencils = int(input("Enter the number of pencils on your desk: "))
value_change = float(input("Enter the value of the change in your wallet: "))

# Double the input values.
double_word = word * 2
double_pencils = num_pencils * 2
double_change = value_change * 2

# Display a table of values and their doubles.
print("{:20s}{:20s}{:20s}".format("Word", "Pencils", "Change"))
print("{:20s}{:<20d}{:<20.2f}".format(word, num_pencils, value_change))
print("{:20s}{:<20d}{:<20.2f}".format(double_word, double_pencils, double_change))

##print("Word is {:s}, number of pencils is {:d}, and value of change is ${:.2f}."
##      .format(word,num_pencils, value_change ))
