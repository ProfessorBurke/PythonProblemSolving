"""Obtain and store volunteering hours."""

from typing import Dict, List

# Annotate and initialize variables.
volunteers: Dict[str, List[int]] = {}
name: str
hours: int

# Obtain and add name and hours until done.
name = input("Enter a name or 'done' when finished: ")
while name != "done":
    hours = int(input("How many hours did {} work? ".format(name)))
    if name in volunteers:
        volunteers[name].append(hours)
    else:
        volunteers[name] = [hours]
    name = input("Enter a name or 'done' when finished: ")

# Display the dictionary.
print(volunteers)




