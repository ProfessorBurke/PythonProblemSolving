"""Obtain and store volunteering hours."""

from typing import Dict, List
from collections import defaultdict

# Annotate and initialize variables.
volunteers: Dict[str, List[int]] = defaultdict(list)
name: str
hours: int

# Obtain and add name and hours until done.
name = input("Enter a name or 'done' when finished: ")
while name != "done":
    hours = int(input("How many hours did {} work? ".format(name)))
    volunteers[name].append(hours)
    name = input("Enter a name or 'done' when finished: ")

# Display the dictionary.
print(volunteers)






