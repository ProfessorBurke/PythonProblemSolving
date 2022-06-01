"""Obtain names from the user and report
   the one that is alphabetically first and the
   average length of the names.
"""

# Annotate and initialize variables.
name: str 
first: str
total_length: int = 0
count: int = 0

# Obtain the first name.
name = input("Please enter a name, or type \"done\" when finished: ")
first = name

# Obtain names until the user types done.
while not "done" in name:
    if name.upper() < first.upper():
        first = name
    total_length += len(name)
    count += 1
    name = input("Please enter a name, or type \"done\" when finished: ")

# Report the results.
if count > 0:
    print("The name that is alphabetically first is {}."
          .format(first))
    print("The average length of the names entered is {:.2f}."
          .format(total_length / count))
else:
    print("No names were entered.")
